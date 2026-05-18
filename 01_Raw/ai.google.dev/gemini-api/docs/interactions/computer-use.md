---
source_url: https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=ko
fetched_at: 2026-05-18T13:09:30.438573+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Computer Use

Computer Use를 사용하면 브라우저를 제어하고 상호작용하며 작업을 자동화하는 에이전트를 빌드할 수 있습니다. 스크린샷을 사용하면 모델이 컴퓨터 화면을 '보고' 마우스 클릭 및 키보드 입력과 같은 특정 UI 작업을 생성하여 '작업'할 수 있습니다. 함수 호출과 마찬가지로 Computer Use 작업을 수신하고 실행하는 클라이언트 측 애플리케이션 코드를 작성해야 합니다.

Computer Use를 사용하면 다음 작업을 할 수 있는 에이전트를 빌드할 수 있습니다.

- 웹사이트에서 반복적인 데이터 입력과 양식 작성을 자동화합니다.
- 웹 애플리케이션 및 사용자 흐름의 자동 테스트 실행
- 다양한 웹사이트에서 조사 수행 (예: 전자상거래 사이트에서 제품 정보, 가격, 리뷰를 수집하여 구매에 대한 정보 제공)

컴퓨터 사용 기능을 테스트하는 가장 쉬운 방법은 [참조 구현](https://github.com/google/computer-use-preview/) 또는 [Browserbase 데모 환경](http://gemini.browserbase.com)을 사용하는 것입니다.

## Computer Use 작동 방식

Computer Use 모델로 브라우저 제어 에이전트를 빌드하려면 다음 작업을 실행하는 에이전트 루프를 구현하세요.

1. [**모델에 요청 보내기**](#send-request)

   - API 요청에 Computer Use 도구를 추가하고 맞춤 사용자 정의 함수 또는 제외된 함수를 선택적으로 추가합니다.
   - 사용자 요청을 사용하여 Computer Use 모델을 프롬프트합니다.
2. [**모델 대답 수신**](#model-response)

   - Computer Use 모델은 사용자 요청과 스크린샷을 분석하고 UI 작업을 나타내는 추천 `function_call` (예: '좌표 (x,y) 클릭' 또는 ''텍스트' 입력')이 포함된 대답을 생성합니다. 컴퓨터 사용 모델에서 지원하는 모든 UI 작업에 관한 설명은 [지원되는 작업](#supported-actions)을 참고하세요.
   - API 응답에는 모델의 제안된 작업을 확인하는 내부 안전 시스템의 `safety_decision`도 포함될 수 있습니다. 이 `safety_decision`는 작업을 다음과 같이 분류합니다.
     - **일반 / 허용됨:** 작업이 안전하다고 간주됩니다. `safety_decision`가 없는 것으로도 나타낼 수 있습니다.
     - **확인 필요 (`require_confirmation`):** 모델이 위험할 수 있는 작업을 수행하려고 합니다 (예: '쿠키 배너 수락' 클릭).
3. [**수신된 작업 실행**](#execute-actions)

   - 클라이언트 측 코드에서 `function_call` 및 함께 제공되는 `safety_decision`를 수신합니다.
     - **일반 / 허용:** `safety_decision`가 일반/허용을 나타내는 경우 (또는 `safety_decision`가 없는 경우) 클라이언트 측 코드는 대상 환경 (예: 웹브라우저)에서 지정된 `function_call`을 실행할 수 있습니다.
     - **확인 필요:** `safety_decision`에 확인이 필요하다고 표시되면 애플리케이션은 `function_call`을 실행하기 전에 최종 사용자에게 확인하라는 메시지를 표시해야 합니다. 사용자가 확인하면 작업을 실행합니다. 사용자가 거부하면 작업을 실행하지 마세요.
4. [**새 환경 상태 캡처**](#capture-state)

   - 작업이 실행되면 클라이언트가 GUI의 새 스크린샷과 현재 URL을 캡처하여 `function_result`의 일부로 Computer Use 모델에 다시 전송합니다.
   - 안전 시스템에서 작업을 차단하거나 사용자가 확인을 거부하면 애플리케이션에서 모델에 다른 의견 양식을 전송하거나 상호작용을 종료할 수 있습니다.

이 프로세스는 2단계부터 반복되며 모델은 새 스크린샷과 지속적인 목표를 사용하여 다음 작업을 제안합니다. 태스크가 완료되거나 오류가 발생하거나 프로세스가 종료될 때까지(예: '차단' 안전 응답 또는 사용자 결정으로 인해) 루프는 계속됩니다.

![컴퓨터 사용 개요](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=ko)

## 컴퓨터 사용 구현 방법

컴퓨터 사용 도구로 빌드하기 전에 다음을 설정해야 합니다.

- **안전한 실행 환경:** 안전상의 이유로 안전하고 통제된 환경 (예: 샌드박스 가상 머신, 컨테이너 또는 권한이 제한된 전용 브라우저 프로필)에서 컴퓨터 사용 에이전트를 실행해야 합니다.
- **클라이언트 측 작업 핸들러:** 모델에서 생성된 작업을 실행하고 각 작업 후 환경의 스크린샷을 캡처하는 클라이언트 측 로직을 구현해야 합니다.

이 섹션의 예시에서는 브라우저를 실행 환경으로 사용하고 [Playwright](https://playwright.dev/)를 클라이언트 측 작업 핸들러로 사용합니다. 이러한 샘플을 실행하려면 필요한 종속 항목을 설치하고 Playwright 브라우저 인스턴스를 초기화해야 합니다.

#### Playwright 설치

```
    pip install google-genai playwright
    playwright install chromium
```

#### Playwright 브라우저 인스턴스 초기화

```
    from playwright.sync_api import sync_playwright

    # 1. Configure screen dimensions for the target environment
    SCREEN_WIDTH = 1440
    SCREEN_HEIGHT = 900

    # 2. Start the Playwright browser
    # In production, utilize a sandboxed environment.
    playwright = sync_playwright().start()
    # Set headless=False to see the actions performed on your screen
    browser = playwright.chromium.launch(headless=False)

    # 3. Create a context and page with the specified dimensions
    context = browser.new_context(
        viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
    )
    page = context.new_page()

    # 4. Navigate to an initial page to start the task
    page.goto("https://www.google.com")

    # The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
    # will be used in the steps below.
```

Android 환경으로 확장하는 샘플 코드는 [맞춤 사용자 정의 함수 사용](#custom-functions) 섹션에 포함되어 있습니다.

### 1. 모델에 요청 보내기

API 요청에 Computer Use 도구를 추가하고 사용자 목표가 포함된 프롬프트를 모델에 전송합니다. 컴퓨터 사용 지원 모델 중 하나를 사용해야 합니다. 그렇지 않으면 오류가 발생합니다.

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

다음 매개변수를 선택적으로 추가할 수도 있습니다.

- **제외된 작업:** 모델에서 수행하지 않기를 원하는 작업이 [지원되는 UI 작업](#supported-actions) 목록에 있으면 `excluded_predefined_functions`에 이러한 작업을 지정합니다.
- **사용자 정의 함수:** Computer Use 도구 외에 커스텀 사용자 정의 함수를 포함할 수 있습니다.

요청을 발행할 때 디스플레이 크기를 지정할 필요는 없습니다. 모델은 화면의 높이와 너비에 맞게 조정된 픽셀 좌표를 예측합니다.

### Python

```
from google import genai

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        }
    ]
)

print(interaction)
```

커스텀 함수가 포함된 예시는 [커스텀 사용자 정의 함수 사용](#custom-functions)을 참고하세요.

### 2. 모델 대답 수신

Computer Use 도구가 사용 설정된 경우 모델은 태스크를 완료하는 데 UI 작업이 필요하다고 판단되면 `function_call` 단계 하나 이상으로 응답합니다.
Computer Use는 병렬 함수 호출을 지원합니다. 즉, 모델이 싱글턴에서 여러 작업을 반환할 수 있습니다.

다음은 모델 응답의 예시입니다.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I will type the search query into the search bar. The search bar is in the center of the page."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "type_text_at",
      "arguments": {
        "x": 371,
        "y": 470,
        "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
        "press_enter": true
      }
    }
  ]
}
```

### 3. 수신된 작업 실행

애플리케이션 코드는 모델 응답을 파싱하고, 작업을 실행하고, 결과를 수집해야 합니다.

다음 예시 코드는 Computer Use 모델 응답에서 함수 호출을 추출하고 Playwright로 실행할 수 있는 작업으로 변환합니다.
모델은 입력 이미지 크기와 관계없이 정규화된 좌표 (0~999)를 출력하므로 변환 단계의 일부는 이러한 정규화된 좌표를 실제 픽셀 값으로 다시 변환하는 것입니다.

Computer Use 모델과 함께 사용하기에 권장되는 화면 크기는 (1440, 900)입니다. 모델은 모든 해상도에서 작동하지만 결과의 품질은 영향을 받을 수 있습니다.

이 예시에는 가장 일반적인 UI 작업 3가지(`open_web_browser`, `click_at`, `type_text_at`)의 구현만 포함되어 있습니다. 프로덕션 사용 사례의 경우 `excluded_predefined_functions`로 명시적으로 추가하지 않는 한 [지원되는 작업](#supported-actions) 목록의 다른 모든 UI 작업을 구현해야 합니다.

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(interaction, page, screen_width, screen_height):
    results = []
    function_calls = [
        step for step in interaction.steps if step.type == "function_call"
    ]

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.arguments
        print(f"  -> Executing: {fname}")

        try:
            if fname == "open_web_browser":
                pass # Already open
            elif fname == "click_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                page.mouse.click(actual_x, actual_y)
            elif fname == "type_text_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                text = args["text"]
                press_enter = args.get("press_enter", False)

                page.mouse.click(actual_x, actual_y)
                # Simple clear (Command+A, Backspace for Mac)
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            else:
                print(f"Warning: Unimplemented or custom function {fname}")

            # Wait for potential navigations/renders
            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### 4. 새 환경 상태 캡처

작업을 실행한 후 이 정보를 사용하여 다음 작업을 생성할 수 있도록 함수 실행 결과를 모델에 다시 전송합니다. 작업 여러 개(병렬 호출)가 실행된 경우 후속 사용자 턴에서 작업마다 `function_result`를 전송해야 합니다.

### Python

```
import json
import base64

def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, call_id, result in results:
        function_responses.append({
            "type": "function_result",
            "name": name,
            "call_id": call_id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps({"url": current_url, **result})
                },
                {
                    "type": "image",
                    "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
                    "mime_type": "image/png"
                }
            ]
        })
    return function_responses
```

## 에이전트 루프 빌드

다단계 상호작용을 사용 설정하려면 [컴퓨터 사용 구현 방법](#implement-computer-use) 섹션의 네 단계를 루프로 결합합니다.
모델 대답과 함수 응답을 모두 추가하여 대화 기록을 올바르게 관리해야 합니다.

이 코드 샘플을 실행하려면 다음을 충족해야 합니다.

- [필요한 Playwright 종속 항목](#implement-computer-use)을 설치합니다.
- [(3) 수신된 작업 실행](#execute-actions) 및 [(4) 새 환경 상태 캡처](#capture-state) 단계에서 도우미 함수를 정의합니다.

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Take initial screenshot
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    # First interaction
    interaction = client.interactions.create(
        model='gemini-2.5-computer-use-preview-10-2025',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser"
        }]
    )

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")

        has_function_calls = any(
            step.type == "function_call"
            for step in interaction.steps
        )
        if not has_function_calls:
            text_response = " ".join([
                content_block.text for step in interaction.steps if step.type == "model_output"
                for content_block in step.content if content_block.type == "text"
            ])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        # Continue conversation with function responses
        interaction = client.interactions.create(
            model='gemini-2.5-computer-use-preview-10-2025',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser"
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## 맞춤 사용자 정의 함수 사용

원하는 경우 요청에 맞춤 사용자 정의 함수를 포함하여 모델의 기능을 확장할 수 있습니다. 다음 예에서는 브라우저별 작업을 제외하면서 `open_app`, `long_press_at`, `go_home`과 같은 맞춤 사용자 정의 작업을 포함하여 모바일 사용 사례에 맞게 Computer Use 모델과 도구를 적용합니다. 모델은 표준 UI 작업과 함께 이러한 맞춤 함수를 지능적으로 호출하여 브라우저가 아닌 환경에서 작업을 완료할 수 있습니다.

### Python

```
from typing import Optional, Dict, Any

from google import genai

client = genai.Client()

SYSTEM_PROMPT = """You are operating an Android phone. Today's date is October 15, 2023, so ignore any other date provided.
* To provide an answer to the user, *do not use any tools* and output your answer on a separate line. IMPORTANT: Do not add any formatting or additional punctuation/text, just output the answer by itself after two empty lines.
* Make sure you scroll down to see everything before deciding something isn't available.
* You can open an app from anywhere. The icon doesn't have to currently be on screen.
* Unless explicitly told otherwise, make sure to save any changes you make.
* If text is cut off or incomplete, scroll or click into the element to get the full text before providing an answer.
* IMPORTANT: Complete the given task EXACTLY as stated. DO NOT make any assumptions that completing a similar task is correct.  If you can't find what you're looking for, SCROLL to find it.
* If you want to edit some text, ONLY USE THE `type` tool. Do not use the onscreen keyboard.
* Quick settings shouldn't be used to change settings. Use the Settings app instead.
* The given task may already be completed. If so, there is no need to do anything.
"""

# Custom function definitions for mobile
custom_functions = [
    {
        "type": "function",
        "name": "open_app",
        "description": "Opens an app by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app to open"},
                "intent": {"type": "string", "description": "Optional deep-link or action"}
            },
            "required": ["app_name"]
        }
    },
    {
        "type": "function",
        "name": "long_press_at",
        "description": "Long-press at a specific screen coordinate.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "X coordinate"},
                "y": {"type": "integer", "description": "Y coordinate"}
            },
            "required": ["x", "y"]
        }
    },
    {
        "type": "function",
        "name": "go_home",
        "description": "Navigates to the device home screen.",
        "parameters": {"type": "object", "properties": {}}
    }
]

# Exclude browser-specific functions
excluded_functions = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    system_instruction=SYSTEM_PROMPT,
    input="Open Chrome, then long-press at 200,400.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        },
        *custom_functions
    ]
)

print(interaction)
```

## 지원되는 UI 작업

모델은 `function_call`을 사용하여 다음 UI 작업을 요청할 수 있습니다. 클라이언트 측 코드에서 이러한 작업의 실행 로직을 구현해야 합니다. 예시는 [참조 구현](https://github.com/google/computer-use-preview)을 참고하세요.

| 명령어 이름 | 설명 | 인수(함수 호출에서) | 함수 호출 예시 |
| --- | --- | --- | --- |
| **open\_web\_browser** | 웹브라우저를 엽니다. | 없음 | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | 동적 콘텐츠가 로드되거나 애니메이션이 완료되도록 5초 동안 실행을 일시중지합니다. | 없음 | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | 브라우저 기록의 이전 페이지로 이동합니다. | 없음 | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | 브라우저 기록의 다음 페이지로 이동합니다. | 없음 | `{"name": "go_forward", "arguments": {}}` |
| **search** | 기본 검색엔진 홈페이지 (예: Google)로 이동합니다. 새 검색 태스크를 시작하는 데 유용합니다. | 없음 | `{"name": "search", "arguments": {}}` |
| **navigate** | 브라우저를 지정된 URL로 직접 이동합니다. | `url`: 문자열 | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | 웹페이지의 특정 좌표를 클릭합니다. x 및 y 값은 1000x1000 그리드를 기반으로 하며 화면 크기에 맞게 조정됩니다. | `y`: 정수(0~999), `x`: 정수(0~999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | 웹페이지의 특정 좌표에 마우스를 가져갑니다. 하위 메뉴를 표시하는 데 유용합니다. x 및 y는 1000x1000 그리드를 기반으로 합니다. | `y`: 정수(0~999) `x`: 정수(0~999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | 특정 좌표에 텍스트를 입력합니다. 기본적으로 먼저 필드를 지우고 입력한 후 Enter 키를 누르지만 이를 사용 중지할 수 있습니다. x 및 y는 1000x1000 그리드를 기반으로 합니다. | `y`: 정수(0~999), `x`: 정수(0~999), `text`: 문자열, `press_enter`: 불리언(선택사항, 기본값: True), `clear_before_typing`: 불리언(선택사항, 기본값: True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | 'Control+C' 또는 'Enter'와 같은 키보드 키나 조합을 누릅니다. 작업(예: 'Enter' 키를 사용하여 양식 제출) 또는 클립보드 작업을 트리거하는 데 유용합니다. | `keys`: 문자열 (예: 'enter', 'control+c') | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | 전체 웹페이지를 '위', '아래', '왼쪽' 또는 '오른쪽'으로 스크롤합니다. | `direction`: 문자열('up', 'down', 'left', 'right') | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | 지정된 방향으로 특정 요소나 영역을 좌표(x, y)에서 특정 크기만큼 스크롤합니다. 좌표와 크기(기본값 800)는 1000x1000 그리드를 기반으로 합니다. | `y`: 정수(0~999), `x`: 정수(0~999), `direction`: 문자열('up', 'down', 'left', 'right'), `magnitude`: 정수(0~999, 선택사항, 기본값: 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | 시작 좌표(x, y)에서 요소를 드래그하여 대상 좌표(destination\_x, destination\_y)에 놓습니다. 모든 좌표는 1000x1000 그리드를 기반으로 합니다. | `y`: 정수(0~999), `x`: 정수(0~999), `destination_y`: 정수(0~999), `destination_x`: 정수(0~999) | `{"name": "drag_and_drop", "arguments": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## 안전 및 보안

### 안전 결정 확인

작업에 따라 모델 응답에 모델의 제안된 작업을 확인하는 내부 안전 시스템의 `safety_decision`이 포함될 수도 있습니다.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95)."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "click_at",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

`safety_decision`이 `require_confirmation`인 경우 작업을 실행하기 전에 최종 사용자에게 확인을 요청해야 합니다. [서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko)에 따라 인간 확인 요청을 우회할 수 없습니다.

이 코드 샘플은 작업을 실행하기 전에 최종 사용자에게 확인을 요청합니다. 사용자가 작업을 확인하지 않으면 루프가 종료됩니다. 사용자가 작업을 확인하면 작업이 실행되고 `safety_acknowledgement` 필드가 `True`로 표시됩니다.

### Python

```
import termcolor

def get_safety_confirmation(safety_decision):
    """Prompt user for confirmation when safety check is triggered."""
    termcolor.cprint("Safety service requires explicit confirmation!", color="red")
    print(safety_decision["explanation"])

    decision = ""
    while decision.lower() not in ("y", "n", "ye", "yes", "no"):
        decision = input("Do you wish to proceed? [Y]es/[N]o\n")

    if decision.lower() in ("n", "no"):
        return "TERMINATE"
    return "CONTINUE"

def execute_function_calls(interaction, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.arguments:
            decision = get_safety_confirmation(function_call.arguments['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = True # Safety acknowledgement

        # ... Execute function call and append to results ...
```

사용자가 확인하면 `function_result`에 안전 확인을 포함해야 합니다.

```
```python
function_responses.append({
    "type": "function_result",
    "name": name,
    "call_id": function_call.id,
    "result": [
        {
            "type": "text",
            "text": json.dumps({
                "url": current_url,
                "safety_acknowledgement": True,
                **extra_fr_fields
            })
        },
        {
            "type": "image",
            "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
            "mime_type": "image/png"
        }
    ]
})
```
```

### 안전 권장사항

Computer Use는 새로운 도구이며 개발자가 유의해야 하는 새로운 위험이 있습니다.

- **신뢰할 수 없는 콘텐츠 및 사기:** 모델이 사용자 목표를 달성하려고 할 때 신뢰할 수 없는 정보 소스와 화면의 안내를 사용할 수 있습니다. 예를 들어 사용자 목표가 Pixel 휴대전화 구매이고 모델에서 '설문조사를 완료하면 Pixel 무료' 사기를 발견한 경우 모델에서 설문조사를 완료할 가능성이 있습니다.
- **가끔 의도하지 않은 작업:** 모델이 사용자 목표나 웹페이지 콘텐츠를 잘못 해석하여 잘못된 버튼 클릭 또는 잘못된 양식 작성과 같은 잘못된 작업을 수행할 수 있습니다. 이로 인해 태스크가 실패하거나 데이터 유출이 발생할 수 있습니다.
- **정책 위반:** API 기능이 의도적으로 또는 의도치 않게 Google 정책 ([생성형 AI 금지된 사용 정책](https://policies.google.com/terms/generative-ai/use-policy?hl=ko) 및 [Gemini API 추가 서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko))을 위반하는 활동으로 이어질 수 있습니다. 여기에는 시스템의 무결성을 방해하거나 보안을 훼손하거나 보안 조치를 우회하거나 의료 기기를 제어할 수 있는 작업이 포함됩니다.

이러한 위험을 해결하려면 다음 안전 조치와 권장사항을 구현하면 됩니다.

1. **인간 참여형 (Human-In-The-Loop, HITL):**

   - **사용자 확인 구현:** 안전 대답에 `require_confirmation`이 표시되면 실행 전에 사용자 확인을 구현해야 합니다. 샘플 코드는 [안전 결정 확인](#safety-decisions)을 참고하세요.
   - **맞춤 안전 지침 제공:** 개발자는 내장된 사용자 확인 검사 외에도 특정 모델 작업을 차단하거나 모델이 되돌릴 수 없는 중요한 작업을 수행하기 전에 사용자 확인을 요구하는 자체 안전 정책을 적용하는 맞춤 [시스템 지침](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko#system-instructions)을 선택적으로 추가할 수 있습니다. 다음은 모델과 상호작용할 때 포함할 수 있는 맞춤 안전 시스템 요청 사항의 예시입니다.

     #### 안전 지침 예시

     맞춤 안전 규칙을 시스템 안내로 설정합니다.

     ```
         ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

         This is your first and most important check. If the next required action falls
         into any of the following categories, you MUST stop immediately, and seek the
         user's explicit permission.

         **Procedure for Seeking Confirmation:**  * **For Consequential Actions:**
         Perform all preparatory steps (e.g., navigating, filling out forms, typing a
         message). You will ask for confirmation **AFTER** all necessary information is
         entered on the screen, but **BEFORE** you perform the final, irreversible action
         (e.g., before clicking "Send", "Submit", "Confirm Purchase", "Share").  * **For
         Prohibited Actions:** If the action is strictly forbidden (e.g., accepting legal
         terms, solving a CAPTCHA), you must first inform the user about the required
         action and ask for their confirmation to proceed.

         **USER_CONFIRMATION Categories:**

         *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
             agreeing to any of the following on the user's behalf. You must ask the
             user to confirm before performing these actions.
             *   Terms of Service
             *   Privacy Policies
             *   Cookie consent banners
             *   End User License Agreements (EULAs)
             *   Any other legally significant contracts or agreements.
         *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
             following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
             *   Any other anti-robot or human-verification mechanisms, even if you are
                 capable.
         *   **Financial Transactions:**
             *   Completing any purchase.
             *   Managing or moving money (e.g., transfers, payments).
             *   Purchasing regulated goods or participating in gambling.
         *   **Sending Communications:**
             *   Sending emails.
             *   Sending messages on any platform (e.g., social media, chat apps).
             *   Posting content on social media or forums.
         *   **Accessing or Modifying Sensitive Information:**
             *   Health, financial, or government records (e.g., medical history, tax
                 forms, passport status).
             *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
                 account number, credit card number).
         *   **User Data Management:**
             *   Accessing, downloading, or saving files from the web.
             *   Sharing or sending files/data to any third party.
             *   Transferring user data between systems.
         *   **Browser Data Usage:**
             *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
                 or saved passwords.
         *   **Security and Identity:**
             *   Logging into any user account.
             *   Any action that involves misrepresentation or impersonation (e.g.,
                 creating a fan account, posting as someone else).
         *   **Insurmountable Obstacles:** If you are technically unable to interact with
             a user interface element or are stuck in a loop you cannot resolve, ask the
             user to take over.
         ---

         ## **RULE 2: Default Behavior (ACTUATE)**

         If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
         your default behavior is to **Actuate**.

         **Actuation Means:**  You MUST proactively perform all necessary steps to move
         the user's request forward. Continue to actuate until you either complete the
         non-consequential task or encounter a condition defined in Rule 1.

         *   **Example 1:** If asked to send money, you will navigate to the payment
             portal, enter the recipient's details, and enter the amount. You will then
             **STOP** as per Rule 1 and ask for confirmation before clicking the final
             "Send" button.
         *   **Example 2:** If asked to post a message, you will navigate to the site,
             open the post composition window, and write the full message. You will then
             **STOP** as per Rule 1 and ask for confirmation before clicking the final
             "Post" button.

             After the user has confirmed, remember to get the user's latest screen
             before continuing to perform actions.

         # Final Response Guidelines:
         Write final response to the user in the following cases:
         - User confirmation
         - When the task is complete or you have enough information to respond to the user
     ```
2. **안전한 실행 환경:** 안전한 샌드박스 환경에서 에이전트를 실행하여 잠재적 영향을 제한합니다 (예: 샌드박스 가상 머신(VM), 컨테이너 (예: Docker) 또는 권한이 제한된 전용 브라우저 프로필).
3. **입력 삭제:** 의도하지 않은 요청 사항이나 프롬프트 인젝션의 위험을 완화하기 위해 프롬프트에서 사용자가 생성한 모든 텍스트를 삭제합니다. 이는 유용한 보안 강화책이지만 안전한 실행 환경을 대체하지는 않습니다.
4. **콘텐츠 가드레일:** 가드레일과 [콘텐츠 안전 API](https://ai.google.dev/gemma/docs/shieldgemma?hl=ko)를 사용하여 사용자 입력, 도구 입력 및 출력, 에이전트의 적절성 응답, 프롬프트 인젝션, 탈옥 감지를 평가합니다.
5. **허용 목록 및 차단 목록:** 모델에서 탐색할 수 있는 위치와 수행할 수 있는 작업을 제어하는 필터링 메커니즘을 구현합니다. 금지된 웹사이트 차단 목록이 좋은 시작점이며 더 제한적인 허용 목록이 더 안전합니다.
6. **관측 가능성 및 로깅:** 디버깅, 감사, 사고 대응에 사용되는 자세한 로그를 유지합니다. 클라이언트는 프롬프트, 스크린샷, 모델 추천 작업 (function\_call), 안전 대답, 클라이언트에서 최종적으로 실행한 모든 작업을 로깅해야 합니다.
7. **환경 관리:** GUI 환경이 일관되도록 합니다.
   예상치 못한 팝업, 알림 또는 레이아웃 변경은 모델에 혼동을 줄 수 있습니다. 가능하면 각 새 작업에 대해 알려진 깨끗한 상태에서 시작하세요.

## 모델 버전

`gemini-3-flash-preview`에는 Computer Use 지원이 내장되어 있으므로 도구에 액세스하기 위해 별도의 모델이 필요하지 않습니다.

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| save 지원되는 데이터 유형 | **입력**  이미지, 텍스트  **출력**  텍스트 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  128,000  **출력 토큰 한도**  64,000 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 미리보기: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_month최신 업데이트 | 2025년 10월 |

## 다음 단계

- [Browserbase 데모 환경](http://gemini.browserbase.com)에서 컴퓨터 사용을 실험해 보세요.
- 예시 코드는 [참조 구현](https://github.com/google/computer-use-preview)을 확인하세요.
- 다른 Gemini API 도구 알아보기:
  - [함수 호출](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ko)
  - [Google 검색으로 그라운딩](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-13(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-13(UTC)"],[],[]]
