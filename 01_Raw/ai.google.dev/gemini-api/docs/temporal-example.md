---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=ko
fetched_at: 2026-05-18T12:58:55.635304+00:00
title: "Gemini \ubc0f Temporal\uc744 \uc0ac\uc6a9\ud55c \uc9c0\uc18d \uac00\ub2a5\ud55c AI \uc5d0\uc774\uc804\ud2b8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini 및 Temporal을 사용한 지속 가능한 AI 에이전트

이 가이드에서는 추론을 위해
[ReAct 스타일](https://arxiv.org/abs/2210.03629) 에이전트 루프를 빌드하는 방법을 안내합니다. 이 루프는
Gemini API를 사용하고 내구성을 위해 [Temporal](https://temporal.io/)을 사용합니다.
이 가이드의 전체 소스 코드는
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini)에서 확인할 수 있습니다.

에이전트는 날씨 알림 조회 또는 IP 주소의 지리적 위치 찾기와 같은 도구를 호출할 수 있으며 응답할 충분한 정보가 있을 때까지 루프합니다.

일반적인 에이전트 데모와 다른 점은 **내구성** 입니다. 모든 LLM 호출, 모든 도구 호출, 에이전트 루프의 모든 단계는 Temporal에 의해 지속됩니다. 프로세스가 다운되거나, 네트워크가 끊어지거나, API가 시간 초과되면 Temporal은 자동으로 재시도하고 마지막으로 완료된 단계부터 다시 시작합니다. 대화 기록이 손실되지 않으며 도구 호출이 잘못 반복되지 않습니다.

## 아키텍처

아키텍처는 세 부분으로 구성됩니다.

- **워크플로:** 실행 로직을 조정하는 에이전트 루프입니다.
- **활동:** Temporal이 지속적으로 만드는 개별 작업 단위 (LLM 호출, 도구 호출)입니다.
- **작업자:** 워크플로와 활동을 실행하는 프로세스입니다.

이 예에서는 이 세 가지를 모두 단일 파일(`durable_agent_worker.py`)에 배치합니다. 실제 구현에서는 다양한 배포 및 확장성 이점을 위해 이를 분리합니다. 에이전트에 프롬프트를 제공하는 코드를 두 번째 파일(`start_workflow.py`)에 배치합니다.

## 기본 요건

이 가이드를 완료하려면 다음이 필요합니다.

- Gemini API 키. Google AI Studio에서 무료로 만들 수 있습니다.
- [Python](https://www.python.org/downloads/) 버전 3.10 이상.
- 로컬
  개발 서버를 실행하기 위한 [Temporal CLI](https://docs.temporal.io/cli).

## 설정

시작하기 전에 로컬에서
[Temporal 개발 서버](https://docs.temporal.io/cli#start-dev-server)
가 실행되고 있는지 확인하세요.

```
temporal server start-dev
```

그런 후 필수 종속 항목을 설치합니다.

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

Gemini API 키를 사용하여 프로젝트 디렉터리에 `.env` 파일을 만듭니다. [Google AI Studio](https://aistudio.google.com/apikey?hl=ko)에서 API 키를 가져올 수 있습니다.

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## 구현

이 가이드의 나머지 부분에서는 `durable_agent_worker.py`를 위에서 아래로 살펴보고 에이전트를 조금씩 빌드합니다. 파일을 만들고 따라 해 보세요.

### 가져오기 및 샌드박스 설정

먼저 정의해야 하는 가져오기로 시작합니다. `workflow.unsafe.imports_passed_through()` 블록은 Temporal의 워크플로 샌드박스에 특정 모듈이 제한 없이 통과하도록 지시합니다. 이는 여러 라이브러리 (특히 `urllib.request.Request`를 서브클래스하는 `httpx`)가 샌드박스에서 차단하는 패턴을 사용하기 때문에 필요합니다.

```
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    import pydantic_core  # noqa: F401
    import annotated_types  # noqa: F401

    import httpx
    from pydantic import BaseModel, Field
    from google import genai
    from google.genai import types
```

### 시스템 안내

다음으로 에이전트의 개성을 정의합니다. 시스템 안내는 모델의 동작 방식을 알려줍니다. 이 에이전트는 도구가 필요하지 않을 때 하이쿠로 응답하도록 지시됩니다.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### 도구 정의

이제 에이전트가 사용할 수 있는 도구를 정의합니다. 각 도구는 설명적인 독스트링이 있는 비동기 함수입니다. 매개변수를 사용하는 도구는 Pydantic 모델을 단일 인수로 사용합니다. 이는 시간이 지남에 따라 선택적 필드를 추가할 때 활동 서명을 안정적으로 유지하는 Temporal 권장사항입니다.

```
import json

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

class GetWeatherAlertsRequest(BaseModel):
    """Request model for getting weather alerts."""

    state: str = Field(description="Two-letter US state code (e.g. CA, NY)")

async def get_weather_alerts(request: GetWeatherAlertsRequest) -> str:
    """Get weather alerts for a US state.

    Args:
        request: The request object containing:
            - state: Two-letter US state code (e.g. CA, NY)
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    url = f"{NWS_API_BASE}/alerts/active/area/{request.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=5.0)
        response.raise_for_status()
        return json.dumps(response.json())
```

다음으로 IP 주소 지리적 위치 찾기 도구를 정의합니다.

```
class GetLocationRequest(BaseModel):
    """Request model for getting location info from an IP address."""

    ipaddress: str = Field(description="An IP address")

async def get_ip_address() -> str:
    """Get the public IP address of the current machine."""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://icanhazip.com")
        response.raise_for_status()
        return response.text.strip()

async def get_location_info(request: GetLocationRequest) -> str:
    """Get the location information for an IP address including city, state, and country.

    Args:
        request: The request object containing:
            - ipaddress: An IP address to look up
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://ip-api.com/json/{request.ipaddress}")
        response.raise_for_status()
        result = response.json()
        return f"{result['city']}, {result['regionName']}, {result['country']}"
```

### 도구 레지스트리

다음으로 도구 이름을 핸들러 함수에 매핑하는 레지스트리를 만듭니다.
`get_tools()` 함수는 호출 가능 항목에서 Gemini 호환 `FunctionDeclaration` 객체
를 `FunctionDeclaration.from_callable_with_api_option()` 사용하여 생성합니다.

```
from typing import Any, Awaitable, Callable

ToolHandler = Callable[..., Awaitable[Any]]

def get_handler(tool_name: str) -> ToolHandler:
    """Get the handler function for a given tool name."""
    if tool_name == "get_location_info":
        return get_location_info
    if tool_name == "get_ip_address":
        return get_ip_address
    if tool_name == "get_weather_alerts":
        return get_weather_alerts
    raise ValueError(f"Unknown tool name: {tool_name}")

def get_tools() -> types.Tool:
    """Get the Tool object containing all available function declarations.

    Uses FunctionDeclaration.from_callable_with_api_option() from the Google GenAI SDK
    to generate tool definitions from the handler functions.
    """
    return types.Tool(
        function_declarations=[
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_weather_alerts, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_location_info, api_option="GEMINI_API"
            ),
            types.FunctionDeclaration.from_callable_with_api_option(
                callable=get_ip_address, api_option="GEMINI_API"
            ),
        ]
    )
```

### LLM 활동

이제 Gemini API를 호출하는 활동을 정의합니다. `GeminiChatRequest` 및 `GeminiChatResponse` 데이터 클래스는 계약을 정의합니다.

LLM 호출과 도구 호출이 별도의 작업으로 처리되도록 자동 함수 호출을 사용 중지하여 에이전트의 내구성을 높입니다. Temporal이 재시도를 지속적으로 처리하므로 SDK의 기본 제공 재시도 (`attempts=1`)도 사용 중지합니다.

```
import os
from dataclasses import dataclass

from temporalio import activity

@dataclass
class GeminiChatRequest:
    """Request parameters for a Gemini chat completion."""

    model: str
    system_instruction: str
    contents: list[types.Content]
    tools: list[types.Tool]

@dataclass
class GeminiChatResponse:
    """Response from a Gemini chat completion."""

    text: str | None
    function_calls: list[dict[str, Any]]
    raw_parts: list[types.Part]

@activity.defn
async def generate_content(request: GeminiChatRequest) -> GeminiChatResponse:
    """Execute a Gemini chat completion with tool support."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(attempts=1),
        ),
    )

    config = types.GenerateContentConfig(
        system_instruction=request.system_instruction,
        tools=request.tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )

    response = await client.aio.models.generate_content(
        model=request.model,
        contents=request.contents,
        config=config,
    )

    function_calls = []
    raw_parts = []
    text_parts = []

    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            raw_parts.append(part)
            if part.function_call:
                function_calls.append(
                    {
                        "name": part.function_call.name,
                        "args": dict(part.function_call.args) if part.function_call.args else {},
                    }
                )
            elif part.text:
                text_parts.append(part.text)

    text = "".join(text_parts) if text_parts and not function_calls else None

    return GeminiChatResponse(
        text=text,
        function_calls=function_calls,
        raw_parts=raw_parts,
    )
```

### 동적 도구 활동

다음으로 도구를 실행하는 활동을 정의합니다. 이는 Temporal의 동적 활동 기능을 사용합니다. 도구 핸들러 (호출 가능 항목)는 `get_handler` 함수를 통해 도구 레지스트리에서 가져옵니다. 이를 통해 다양한 도구 및 시스템 안내를 제공하여 다양한 에이전트를 간단히 정의할 수 있습니다. 에이전트 루프를 구현하는 워크플로에는 변경이 필요하지 않습니다.

활동은 핸들러의 서명을 검사하여 인수를 전달하는 방법을 결정합니다. 핸들러가 Pydantic 모델을 예상하는 경우 Gemini에서 생성하는 중첩된 출력
형식 (예: 평면 `{"state": "CA"}` 대신 `{"request": {"state": "CA"}}`)을 처리합니다.

```
import inspect
from collections.abc import Sequence

from temporalio.common import RawValue

@activity.defn(dynamic=True)
async def dynamic_tool_activity(args: Sequence[RawValue]) -> dict:
    """Execute a tool dynamically based on the activity name."""
    tool_name = activity.info().activity_type
    tool_args = activity.payload_converter().from_payload(args[0].payload, dict)
    activity.logger.info(f"Running dynamic tool '{tool_name}' with args: {tool_args}")

    handler = get_handler(tool_name)

    if not inspect.iscoroutinefunction(handler):
        raise TypeError("Tool handler must be async (awaitable).")

    sig = inspect.signature(handler)
    params = list(sig.parameters.values())

    if len(params) == 0:
        result = await handler()
    else:
        param = params[0]
        param_name = param.name
        ann = param.annotation

        if isinstance(ann, type) and issubclass(ann, BaseModel):
            nested_args = tool_args.get(param_name, tool_args)
            result = await handler(ann(**nested_args))
        else:
            result = await handler(**tool_args)

    activity.logger.info(f"Tool '{tool_name}' result: {result}")
    return result
```

### 에이전트 루프 워크플로

이제 에이전트 빌드를 완료하는 데 필요한 모든 항목이 있습니다. `AgentWorkflow` 클래스는 에이전트 루프가 포함된 워크플로를 구현합니다. 이 루프 내에서 LLM은 활동을 통해 호출되고 (지속적으로 만듦) 출력이 검사되며 LLM에서 도구를 선택한 경우 `dynamic_tool_activity`를 통해 호출됩니다.

이 간단한 ReAct 스타일 에이전트에서 LLM이 도구를 사용하지 않기로 선택하면 루프가 완료된 것으로 간주되고 최종 LLM 결과가 반환됩니다.

```
from datetime import timedelta

@workflow.defn
class AgentWorkflow:
    """Agentic loop workflow that uses Gemini for LLM calls and executes tools."""

    @workflow.run
    async def run(self, input: str) -> str:
        contents: list[types.Content] = [
            types.Content(role="user", parts=[types.Part.from_text(text=input)])
        ]

        tools = [get_tools()]

        while True:
            result = await workflow.execute_activity(
                generate_content,
                GeminiChatRequest(
                    model="gemini-3-flash-preview",
                    system_instruction=SYSTEM_INSTRUCTIONS,
                    contents=contents,
                    tools=tools,
                ),
                start_to_close_timeout=timedelta(seconds=60),
            )

            if result.function_calls:
                # Sending the complete raw_parts here ensures Gemini 3 thought
                # signatures are propagated correctly.
                contents.append(types.Content(role="model", parts=result.raw_parts))

                for function_call in result.function_calls:
                    tool_result = await self._handle_function_call(function_call)

                    contents.append(
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call["name"],
                                    response={"result": tool_result},
                                )
                            ],
                        )
                    )
            else:
                return result.text
            # Leave this in place. You will un-comment it during a durability
            # test later on.
            # await asyncio.sleep(10)

    async def _handle_function_call(self, function_call: dict) -> str:
        """Execute a tool via dynamic activity and return the result."""
        tool_name = function_call["name"]
        tool_args = function_call.get("args", {})

        result = await workflow.execute_activity(
            tool_name,
            tool_args,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return result
```

에이전트 루프는 완전히 지속됩니다. 루프를 여러 번 반복한 후 에이전트 작업자가 다운되면 Temporal은 이미 실행된 LLM 호출 또는 도구 호출을 다시 호출할 필요 없이 중단된 지점부터 정확히 다시 시작합니다.

### 작업자 시작

마지막으로 모든 것을 연결합니다. 코드는 단일 프로세스에서 실행되는 것처럼 보이도록 필요한 비즈니스 로직을 구현하지만 Temporal을 사용하면 워크플로와 활동 간의 통신이 Temporal에서 제공하는 메시징을 통해 이루어지는 이벤트 기반 시스템 (특히 이벤트 소싱)이 됩니다.

Temporal 작업자는 Temporal 서비스에 연결하고 워크플로 및 활동 작업의 스케줄러 역할을 합니다. 작업자는 워크플로와 두 활동을 모두 등록한 다음 작업을 리슨하기 시작합니다.

```
import asyncio
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv
from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter
from temporalio.envconfig import ClientConfig
from temporalio.worker import Worker

async def main():
    config = ClientConfig.load_client_connect_config()
    config.setdefault("target_host", "localhost:7233")
    client = await Client.connect(
        **config,
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="gemini-agent-python-task-queue",
        workflows=[
            AgentWorkflow,
        ],
        activities=[
            generate_content,
            dynamic_tool_activity,
        ],
        activity_executor=ThreadPoolExecutor(max_workers=10),
    )
    await worker.run()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
```

## 클라이언트 스크립트

클라이언트 스크립트 (`start_workflow.py`)를 만듭니다. 쿼리를 제출하고 결과를 기다립니다. 에이전트 작업자에서 참조되는 동일한 태스크 큐에 연결됩니다. `start_workflow` 스크립트는 사용자 프롬프트가 포함된 워크플로 태스크를 해당 태스크 큐에 디스패치하여 에이전트 실행을 시작합니다.

```
import asyncio
import sys
import uuid

from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter

async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Tell me about recursion"

    result = await client.execute_workflow(
        "AgentWorkflow",
        query,
        id=f"gemini-agent-id-{uuid.uuid4()}",
        task_queue="gemini-agent-python-task-queue",
    )
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## 에이전트 실행

아직 시작하지 않았다면 Temporal 개발 서버를 시작합니다.

```
temporal server start-dev
```

새 터미널 창에서 에이전트 작업자를 시작합니다.

```
python -m durable_agent_worker
```

세 번째 터미널 창에서 에이전트에 쿼리를 제출합니다.

```
python -m start_workflow "are there any weather alerts for where I am?"
```

에이전트 루프의 각 반복에서 발생하는 작업을 보여주는 `durable_agent_worker`의 터미널 출력을 확인합니다. LLM은 사용할 수 있는 일련의 도구를 호출하여 사용자 요청을 충족할 수 있습니다. `http://localhost:8233/namespaces/default/workflows`의 Temporal UI를 통해 실행된 단계를 확인할 수 있습니다.

몇 가지 다른 프롬프트를 사용하여 에이전트 추론 및 도구 호출을 확인합니다.

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

마지막 프롬프트에는 도구가 필요하지 않으므로 에이전트는 `SYSTEM_INSTRUCTIONS`에 따라 하이쿠로 응답합니다.

## 내구성 테스트 (선택사항)

Temporal을 기반으로 빌드하면 에이전트가 오류를 원활하게 처리할 수 있습니다. 두 가지 실험을 사용하여 이를 테스트할 수 있습니다.

### 네트워크 중단 시뮬레이션

이 테스트에서는 컴퓨터의 인터넷 연결을 일시적으로 사용 중지하고, 워크플로를 제출하고, Temporal이 자동으로 재시도하는 것을 확인한 다음, 네트워크를 복원하여 복구되는지 확인합니다.

1. 컴퓨터를 인터넷에서 연결 해제합니다 (예: Wi-Fi 사용 중지).
2. 워크플로를 제출합니다.

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Temporal UI (`http://localhost:8233`)를 확인합니다. LLM 활동이 실패하고 Temporal이 백그라운드에서 재시도를 자동으로 관리하는 것을 확인할 수 있습니다.
4. 인터넷에 다시 연결합니다.
5. 다음 자동 재시도는 Gemini API에 성공적으로 도달하고 터미널에 최종 결과가 출력됩니다.

### 작업자 다운에서 살아남기

이 테스트에서는 실행 중에 작업자를 종료하고 다시 시작합니다. Temporal은 워크플로 기록 (이벤트 소싱)을 재생하고 마지막으로 완료된 활동부터 다시 시작합니다. 이미 완료된 LLM 호출 및 도구 호출은 반복되지 않습니다.

1. 작업자를 종료할 시간을 확보하려면 `durable_agent_worker.py`를 열고 `AgentWorkflow`
   `run` 루프 내에서 `await asyncio.sleep(10)`의 주석 처리를 일시적으로 삭제합니다.
2. 작업자를 다시 시작합니다.

   ```
   python -m durable_agent_worker
   ```
3. 여러 도구를 트리거하는 쿼리를 제출합니다.

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. 완료되기 전에 언제든지 작업자 프로세스를 종료합니다 (작업자 터미널에서 `Ctrl-C` 또는 백그라운드에서 실행 중인 경우 `kill %1` 사용).
5. 작업자를 다시 시작합니다.

   ```
   python -m durable_agent_worker
   ```

Temporal은 워크플로 기록을 재생합니다. 이미 완료된 LLM 호출 및 도구 호출은 다시 실행되지 **않습니다**. 결과는 기록 (이벤트 로그)에서 즉시 재생됩니다. 워크플로가 성공적으로 완료됩니다.

## 추가 자료

- [Temporal 문서](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [이 가이드의 소스 코드](https://github.com/temporal-community/durable-react-agent-gemini)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
