---
source_url: https://ai.google.dev/gemini-api/docs/temporal-example?hl=hi
fetched_at: 2026-08-31T06:35:07.943269+00:00
title: "Gemini \u0914\u0930 Temporal \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947, \u092d\u0930\u094b\u0938\u0947\u092e\u0902\u0926 \u090f\u0906\u0908 \u090f\u091c\u0947\u0902\u091f \u092c\u0928\u093e\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini और Temporal की मदद से, भरोसेमंद एआई एजेंट बनाना

इस ट्यूटोरियल में,
[ReAct-स्टाइल](https://arxiv.org/abs/2210.03629) का एजेंटिक लूप बनाने का तरीका बताया गया है. यह लूप, तर्क देने के लिए
Gemini API और डेटा को सेव रखने के लिए [Temporal](https://temporal.io/) का इस्तेमाल करता है.
इस ट्यूटोरियल का पूरा सोर्स कोड,
[GitHub](https://github.com/temporal-community/durable-react-agent-gemini) पर उपलब्ध है.

एजेंट, टूल को कॉल कर सकता है. जैसे, मौसम की चेतावनियां देखना या किसी आईपी पते की जगह की जानकारी पाना. साथ ही, जब तक उसके पास जवाब देने के लिए ज़रूरी जानकारी नहीं होगी, तब तक वह लूप में रहेगा.

यह एजेंट डेमो, आम एजेंट डेमो से **डेटा सेव रखने की सुविधा** के मामले में अलग है. Temporal, एलएलएम के हर कॉल, हर टूल के इस्तेमाल, और एजेंटिक लूप के हर चरण को सेव रखता है. अगर प्रोसेस क्रैश हो जाती है, नेटवर्क बंद हो जाता है या एपीआई की समयसीमा खत्म हो जाती है, तो Temporal अपने-आप फिर से कोशिश करता है और पिछली बार पूरे हुए चरण से आगे बढ़ता है. चैट का इतिहास नहीं मिटता और टूल के कॉल, गलत तरीके से दोहराए नहीं जाते.

## आर्किटेक्चर

आर्किटेक्चर के तीन हिस्से होते हैं:

- **वर्कफ़्लो:** एजेंटिक लूप, जो एक्ज़ीक्यूशन लॉजिक को व्यवस्थित करता है.
- **ऐक्टिविटी:** काम की अलग-अलग यूनिट (एलएलएम कॉल, टूल कॉल), जिन्हें Temporal सेव रखता है.
- **वर्कर:** वह प्रोसेस जो वर्कफ़्लो और ऐक्टिविटी को एक्ज़ीक्यूट करती है.

इस उदाहरण में, इन तीनों हिस्सों को एक ही फ़ाइल (`durable_agent_worker.py`) में रखा जाएगा. असल में, इन्हें अलग-अलग रखा जाता है, ताकि इन्हें अलग-अलग जगह पर डिप्लॉय किया जा सके और स्केल किया जा सके. एजेंट को प्रॉम्प्ट देने वाला कोड, दूसरी फ़ाइल (`start_workflow.py`) में रखा जाएगा.

## ज़रूरी शर्तें

इस गाइड को पूरा करने के लिए, आपको इनकी ज़रूरत होगी:

- Gemini API पासकोड. इसे
  [Google AI Studio](https://aistudio.google.com/apikey?hl=hi) में मुफ़्त में बनाया जा सकता है.
- [Python](https://www.python.org/downloads/) का वर्शन 3.10 या इसके बाद का वर्शन.
- लोकल
  डेवलपमेंट सर्वर चलाने के लिए, [Temporal CLI](https://docs.temporal.io/cli).

## सेटअप

शुरू करने से पहले, पक्का करें कि आपके पास एक
[Temporal डेवलपमेंट सर्वर](https://docs.temporal.io/cli#start-dev-server)
लोकल तौर पर चल रहा हो:

```
temporal server start-dev
```

इसके बाद, ज़रूरी डिपेंडेंसी इंस्टॉल करें:

```
pip install temporalio google-genai httpx pydantic python-dotenv
```

अपने प्रोजेक्ट डायरेक्ट्री में, Gemini API पासकोड के साथ `.env` फ़ाइल बनाएं. [Google AI Studio](https://aistudio.google.com/apikey?hl=hi) से एपीआई पासकोड पाया जा सकता है.

```
echo "GOOGLE_API_KEY=your-api-key-here" > .env
```

## लागू करना

इस ट्यूटोरियल के बाकी हिस्से में, `durable_agent_worker.py` को ऊपर से नीचे तक दिखाया गया है. इसमें एजेंट को धीरे-धीरे बनाया गया है. फ़ाइल बनाएं और साथ-साथ काम करें.

### इंपोर्ट और सैंडबॉक्स सेटअप

सबसे पहले, उन इंपोर्ट को तय करें जिन्हें पहले से तय किया जाना चाहिए. `workflow.unsafe.imports_passed_through()` ब्लॉक, Temporal के वर्कफ़्लो सैंडबॉक्स को बताता है कि कुछ मॉड्यूल को बिना किसी पाबंदी के पास होने दिया जाए. ऐसा इसलिए ज़रूरी है, क्योंकि कई लाइब्रेरी (खास तौर पर `httpx`, जो `urllib.request.Request` की सबक्लास है) ऐसे पैटर्न का इस्तेमाल करती हैं जिन्हें सैंडबॉक्स आम तौर पर ब्लॉक कर देता है.

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

### सिस्टम के निर्देश

इसके बाद, एजेंट की पर्सनैलिटी तय करें. सिस्टम के निर्देश, मॉडल को बताते हैं कि उसे कैसा व्यवहार करना है. इस एजेंट को निर्देश दिया गया है कि अगर टूल की ज़रूरत न हो, तो वह हाइकू में जवाब दे.

```
SYSTEM_INSTRUCTIONS = """
You are a helpful agent that can use tools to help the user.
You will be given an input from the user and a list of tools to use.
You may or may not need to use the tools to satisfy the user ask.
If no tools are needed, respond in haikus.
"""
```

### टूल की परिभाषाएं

अब उन टूल को तय करें जिनका इस्तेमाल एजेंट कर सकता है. हर टूल एक एसिंक फ़ंक्शन होता है, जिसमें जानकारी देने वाला डॉकस्ट्रिंग होता है. जिन टूल में पैरामीटर लिए जाते हैं वे अपने सिंगल आर्ग्युमेंट के तौर पर, Pydantic मॉडल का इस्तेमाल करते हैं. यह Temporal का सबसे सही तरीका है. इससे समय के साथ-साथ, ज़रूरी नहीं वाले फ़ील्ड जोड़ने पर भी, ऐक्टिविटी के सिग्नेचर स्थिर रहते हैं.

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

इसके बाद, आईपी पते की जगह की जानकारी पाने के लिए टूल तय करें:

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

### टूल रजिस्ट्री

इसके बाद, एक रजिस्ट्री बनाएं जो टूल के नामों को हैंडलर फ़ंक्शन से मैप करती है.
`get_tools()` फ़ंक्शन, `FunctionDeclaration.from_callable_with_api_option()` का इस्तेमाल करके, कॉल किए जा सकने वाले फ़ंक्शन से Gemini के साथ काम करने वाले `FunctionDeclaration` ऑब्जेक्ट
जनरेट करता है.

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

### एलएलएम ऐक्टिविटी

अब वह ऐक्टिविटी तय करें जो Gemini API को कॉल करती है. `GeminiChatRequest` और `GeminiChatResponse` डेटाक्लास, कॉन्ट्रैक्ट तय करते हैं.

फ़ंक्शन को अपने-आप कॉल करने की सुविधा बंद कर दी जाएगी, ताकि एलएलएम के इस्तेमाल और टूल के इस्तेमाल को अलग-अलग टास्क के तौर पर हैंडल किया जा सके. इससे आपके एजेंट को ज़्यादा समय तक सेव रखा जा सकेगा. एसडीके टूल के बिल्ट-इन रीट्राय (`attempts=1`) को भी बंद कर दिया जाएगा, क्योंकि Temporal, रीट्राय को सेव रखता है.

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

### डाइनैमिक टूल ऐक्टिविटी

इसके बाद, वह ऐक्टिविटी तय करें जो टूल को एक्ज़ीक्यूट करती है. इसमें Temporal की डाइनैमिक ऐक्टिविटी सुविधा का इस्तेमाल किया जाता है: टूल हैंडलर (कॉल किया जा सकने वाला फ़ंक्शन) को `get_handler` फ़ंक्शन के ज़रिए, टूल रजिस्ट्री से हासिल किया जाता है. इससे, टूल और सिस्टम के निर्देशों का अलग-अलग सेट देकर, अलग-अलग एजेंट तय किए जा सकते हैं. एजेंटिक लूप को लागू करने वाले वर्कफ़्लो में कोई बदलाव करने की ज़रूरत नहीं होती.

ऐक्टिविटी, आर्ग्युमेंट पास करने का तरीका तय करने के लिए, हैंडलर के सिग्नेचर की जांच करती है. अगर हैंडलर को Pydantic मॉडल की ज़रूरत होती है, तो वह Gemini के जनरेट किए गए नेस्टेड आउटपुट
फ़ॉर्मैट को हैंडल करता है. उदाहरण के लिए, `{"request": {"state": "CA"}}` फ़्लैट `{"state": "CA"}` के बजाय.

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

### एजेंटिक लूप वर्कफ़्लो

अब आपके पास एजेंट बनाने के लिए सभी हिस्से मौजूद हैं. `AgentWorkflow` क्लास, एजेंट लूप वाला वर्कफ़्लो लागू करती है. उस लूप में, एलएलएम को ऐक्टिविटी के ज़रिए इस्तेमाल किया जाता है (इससे इसे सेव रखा जा सकता है). इसके आउटपुट की जांच की जाती है. अगर एलएलएम ने किसी टूल को चुना है, तो उसे `dynamic_tool_activity` के ज़रिए इस्तेमाल किया जाता है.

ReAct स्टाइल के इस आसान एजेंट में, एलएलएम के किसी टूल का इस्तेमाल न करने का विकल्प चुनने के बाद, लूप को पूरा माना जाता है और एलएलएम का फ़ाइनल नतीजा दिखाया जाता है.

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
                    model="gemini-3.5-flash",
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

एजेंटिक लूप को पूरी तरह से सेव रखा जा सकता है. अगर लूप के कई बार चलने के बाद, एजेंट वर्कर क्रैश हो जाता है, तो Temporal ठीक वहीं से शुरू होगा जहां से वह बंद हुआ था. इसके लिए, पहले से एक्ज़ीक्यूट किए गए एलएलएम के इस्तेमाल या टूल कॉल को फिर से इस्तेमाल करने की ज़रूरत नहीं होगी.

### वर्कर स्टार्टअप

आखिर में, सभी को एक साथ जोड़ें. कोड, ज़रूरी बिज़नेस लॉजिक को इस तरह लागू करता है कि ऐसा लगता है कि वह एक ही प्रोसेस में चल रहा है. हालांकि, Temporal के इस्तेमाल से यह एक इवेंट-ड्रिवन सिस्टम (खास तौर पर, इवेंट-सोर्स्ड) बन जाता है. इसमें वर्कफ़्लो और ऐक्टिविटी के बीच, Temporal की ओर से उपलब्ध कराए गए मैसेजिंग के ज़रिए कम्यूनिकेशन होता है.

Temporal वर्कर, Temporal सेवा से कनेक्ट होता है और वर्कफ़्लो और ऐक्टिविटी टास्क के लिए शेड्यूलर के तौर पर काम करता है. वर्कर, वर्कफ़्लो और दोनों ऐक्टिविटी को रजिस्टर करता है. इसके बाद, टास्क के लिए सुनना शुरू करता है.

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

## क्लाइंट स्क्रिप्ट

क्लाइंट स्क्रिप्ट (`start_workflow.py`) बनाएं. यह क्वेरी सबमिट करती है और नतीजे का इंतज़ार करती है. ध्यान दें कि यह उसी टास्क क्यू से कनेक्ट होती है जिसका रेफ़रंस एजेंट वर्कर में दिया गया है. `start_workflow` स्क्रिप्ट, उपयोगकर्ता के प्रॉम्प्ट के साथ उस टास्क क्यू में वर्कफ़्लो टास्क भेजती है. इससे एजेंट का एक्ज़ीक्यूशन शुरू होता है.

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

## एजेंट चलाएं

अगर आपने अब तक Temporal डेवलपमेंट सर्वर शुरू नहीं किया है, तो उसे शुरू करें:

```
temporal server start-dev
```

नई टर्मिनल विंडो में, एजेंट वर्कर शुरू करें:

```
python -m durable_agent_worker
```

तीसरी टर्मिनल विंडो में, अपने एजेंट को क्वेरी सबमिट करें:

```
python -m start_workflow "are there any weather alerts for where I am?"
```

`durable_agent_worker` के टर्मिनल में आउटपुट देखें. इसमें एजेंटिक लूप के हर इटरेशन में होने वाली कार्रवाइयां दिखती हैं. एलएलएम, अपने पास मौजूद टूल की सीरीज़ को इस्तेमाल करके, उपयोगकर्ता के अनुरोध को पूरा कर पाता है. `http://localhost:8233/namespaces/default/workflows` पर Temporal यूज़र इंटरफ़ेस (यूआई) के ज़रिए, एक्ज़ीक्यूट किए गए चरण देखे जा सकते हैं.

एजेंट के तर्क और टूल को कॉल करने की सुविधा देखने के लिए, कुछ अलग-अलग प्रॉम्प्ट आज़माएं:

```
python -m start_workflow "are there any weather alerts for New York?"
python -m start_workflow "where am I?"
python -m start_workflow "what is my ip address?"
python -m start_workflow "tell me a joke"
```

आखिरी प्रॉम्प्ट के लिए किसी टूल की ज़रूरत नहीं होती. इसलिए, एजेंट `SYSTEM_INSTRUCTIONS` के आधार पर हाइकू में जवाब देता है.

## डेटा सेव रखने की सुविधा की जांच करना (ज़रूरी नहीं)

Temporal पर बनाने से, आपका एजेंट गड़बड़ियों से आसानी से बच जाता है. इसे दो अलग-अलग तरीकों से आज़माया जा सकता है.

### नेटवर्क बंद होने की स्थिति को सिम्युलेट करना

इस टेस्ट में, आपको कुछ समय के लिए अपने कंप्यूटर का इंटरनेट कनेक्शन बंद करना होगा. इसके बाद, वर्कफ़्लो सबमिट करना होगा. फिर, Temporal के अपने-आप रीट्राय करने की सुविधा देखनी होगी. इसके बाद, नेटवर्क को वापस चालू करना होगा, ताकि यह देखा जा सके कि वह ठीक होता है या नहीं.

1. अपने डिवाइस को इंटरनेट से डिसकनेक्ट करें. उदाहरण के लिए, वाई-फ़ाई बंद करें.
2. वर्कफ़्लो सबमिट करें:

   ```
   python -m start_workflow "tell me a joke"
   ```
3. Temporal यूआई (`http://localhost:8233`) देखें. आपको एलएलएम ऐक्टिविटी में गड़बड़ी दिखेगी. साथ ही, Temporal बैकग्राउंड में रीट्राय को अपने-आप मैनेज करेगा.
4. इंटरनेट से फिर से कनेक्ट करें.
5. अगली बार अपने-आप रीट्राय करने पर, Gemini API को कॉल किया जा सकेगा. साथ ही, आपके टर्मिनल पर फ़ाइनल नतीजा दिखेगा.

### वर्कर क्रैश होने की स्थिति को सिम्युलेट करना

इस टेस्ट में, आपको एक्ज़ीक्यूशन के बीच में वर्कर को बंद करना होगा और उसे रीस्टार्ट करना होगा. Temporal, वर्कफ़्लो के इतिहास (इवेंट सोर्सिंग) को फिर से चलाता है और पिछली बार पूरी हुई ऐक्टिविटी से आगे बढ़ता है. पहले से पूरे हो चुके एलएलएम के इस्तेमाल और टूल कॉल को फिर से नहीं चलाया जाता.

1. वर्कर को बंद करने के लिए, `durable_agent_worker.py` खोलें. इसके बाद, `AgentWorkflow`
   `run` लूप में, `await asyncio.sleep(10)` को कुछ समय के लिए अनकमेंट करें.
2. वर्कर को रीस्टार्ट करें:

   ```
   python -m durable_agent_worker
   ```
3. ऐसी क्वेरी सबमिट करें जिससे कई टूल ट्रिगर हों:

   ```
   python -m start_workflow "are there any weather alerts where I am?"
   ```
4. पूरा होने से पहले किसी भी समय वर्कर प्रोसेस को बंद करें. इसके लिए, वर्कर टर्मिनल में `Ctrl-C` दबाएं या बैकग्राउंड में चल रहा होने पर, `kill %1` का इस्तेमाल करें.
5. वर्कर को रीस्टार्ट करें:

   ```
   python -m durable_agent_worker
   ```

Temporal, वर्कफ़्लो के इतिहास को फिर से चलाता है. एलएलएम कॉल और टूल के इस्तेमाल जो पहले ही पूरे हो चुके हैं उन्हें **फिर से** एक्ज़ीक्यूट नहीं किया जाता. उनके नतीजे, इतिहास (इवेंट लॉग) से तुरंत फिर से दिखाए जाते हैं. वर्कफ़्लो, पूरी तरह से पूरा हो जाता है.

## अतिरिक्त संसाधन

- [Temporal के दस्तावेज़](https://docs.temporal.io/)
- [Temporal Python SDK](https://docs.temporal.io/develop/python)
- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [इस ट्यूटोरियल का सोर्स कोड](https://github.com/temporal-community/durable-react-agent-gemini)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया."],[],[]]
