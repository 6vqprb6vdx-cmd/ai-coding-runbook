---
source_url: https://ai.google.dev/gemini-api/docs/langgraph-example?hl=th
fetched_at: 2026-05-11T12:40:20.532949+00:00
title: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e40\u0e2d\u0e40\u0e08\u0e19\u0e15\u0e4c ReAct \u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48\u0e15\u0e49\u0e19\u0e14\u0e49\u0e27\u0e22 Gemini \u0e41\u0e25\u0e30 LangGraph \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# สร้างเอเจนต์ ReAct ตั้งแต่ต้นด้วย Gemini และ LangGraph

LangGraph เป็นเฟรมเวิร์กสำหรับสร้างแอปพลิเคชัน LLM แบบมีสถานะ จึงเป็นตัวเลือกที่ดีในการสร้างเอเจนต์ ReAct (การให้เหตุผลและการดำเนินการ)

เอเจนต์ ReAct ผสานการให้เหตุผลของ LLM กับการดำเนินการ โดยจะคิดอย่างเป็นขั้นตอน
ใช้เครื่องมือ และดำเนินการตามสิ่งที่สังเกตได้เพื่อบรรลุเป้าหมายของผู้ใช้ พร้อมทั้งปรับแนวทางแบบไดนามิก
รูปแบบนี้ซึ่งเปิดตัวใน ["ReAct: Synergizing Reasoning and Acting
in Language Models"](https://arxiv.org/abs/2210.03629) (2023) พยายาม
จำลองการแก้ปัญหาที่ยืดหยุ่นแบบมนุษย์แทนที่จะใช้เวิร์กโฟลว์ที่เข้มงวด

LangGraph มีเอเจนต์ ReAct ที่สร้างไว้ล่วงหน้า ([`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent))
ซึ่งจะทำงานได้ดีเมื่อคุณต้องการควบคุมและปรับแต่งการใช้งาน ReAct เพิ่มเติม คู่มือนี้จะแสดงเวอร์ชันที่เรียบง่าย

LangGraph สร้างโมเดล Agent เป็นกราฟโดยใช้คอมโพเนนต์หลัก 3 อย่าง ได้แก่

- `State`: โครงสร้างข้อมูลที่แชร์ (โดยปกติคือ `TypedDict` หรือ `Pydantic BaseModel`) ซึ่งแสดงถึงสแนปชอตปัจจุบันของแอปพลิเคชัน
- `Nodes`: เข้ารหัสตรรกะของเอเจนต์ โดยจะรับสถานะปัจจุบันเป็นอินพุต ทำการคำนวณหรือผลข้างเคียงบางอย่าง และส่งคืนสถานะที่อัปเดตแล้ว เช่น การเรียก LLM หรือการเรียกเครื่องมือ
- `Edges`: กำหนด`Node`ถัดไปที่จะดำเนินการตาม`State`ปัจจุบัน เพื่อให้ใช้ตรรกะแบบมีเงื่อนไขและการเปลี่ยนสถานะแบบคงที่ได้

หากยังไม่มีคีย์ API คุณสามารถรับคีย์ได้จาก [Google AI
Studio](https://aistudio.google.com/app/apikey?hl=th)

```
pip install langgraph langchain-google-genai geopy requests
```

ตั้งค่าคีย์ API ในตัวแปรสภาพแวดล้อม `GEMINI_API_KEY`

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")
```

คู่มือนี้จะอธิบายตัวอย่างการใช้งานจริงเพื่อให้คุณเข้าใจวิธีใช้เอเจนต์ ReAct โดยใช้ LangGraph ได้ดียิ่งขึ้น
คุณจะสร้าง Agent ที่มีเป้าหมายคือ
ใช้เครื่องมือเพื่อค้นหาสภาพอากาศปัจจุบันของสถานที่ที่ระบุ

สำหรับเอเจนต์สภาพอากาศนี้ `State` จะเก็บประวัติการสนทนาที่ดำเนินอยู่ (เป็นรายการข้อความ) และตัวนับ (เป็นจำนวนเต็ม) สำหรับจำนวนขั้นตอนที่ดำเนินการเพื่อเป็นตัวอย่าง

LangGraph มีฟังก์ชันตัวช่วย `add_messages` สำหรับอัปเดตรายการข้อความสถานะ โดยจะทำหน้าที่เป็น[ตัวลด](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers)
ซึ่งจะรับรายการปัจจุบันรวมกับข้อความใหม่ แล้วแสดงผลเป็นรายการที่รวมกัน โดยจะ
จัดการการอัปเดตตามรหัสข้อความ และค่าเริ่มต้นจะเป็นลักษณะการทำงานแบบ "ต่อท้ายเท่านั้น" สำหรับข้อความใหม่
ที่ยังไม่ได้อ่าน

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages  # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

จากนั้นกำหนดเครื่องมือสภาพอากาศ

```
from langchain_core.tools import tool
from geopy.geocoders import Nominatim
from pydantic import BaseModel, Field
import requests

geolocator = Nominatim(user_agent="weather-app")

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """Retrieves the weather using Open-Meteo API.

    Takes a given location (city) and a date (yyyy-mm-dd).

    Returns:
        A dict with the time and temperature for each hour.
    """
    # Note that Colab may experience rate limiting on this service. If this
    # happens, use a machine to which you have exclusive access.
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return dict(zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]))
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}

tools = [get_weather_forecast]
```

ตอนนี้ให้เริ่มต้นโมเดลและเชื่อมโยงเครื่องมือกับโมเดล

```
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-3-flash-preview",
    temperature=1.0,
    max_retries=2,
    google_api_key=api_key,
)

# Bind tools to the model
model = llm.bind_tools([get_weather_forecast])

# Test the model with tools
res=model.invoke(f"What is the weather in Berlin on {datetime.today()}?")

print(res)
```

ขั้นตอนสุดท้ายก่อนที่จะเรียกใช้ Agent ได้คือการกำหนดโหนดและขอบ
ในตัวอย่างนี้ คุณมี 2 โหนดและ 1 ขอบ

- `call_tool` โหนดที่เรียกใช้เมธอดเครื่องมือ LangGraph มีโหนดที่สร้างไว้ล่วงหน้า
  สำหรับฟังก์ชันนี้ชื่อว่า [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)
- `call_model` โหนดที่ใช้ `model_with_tools` เพื่อเรียกโมเดล
- `should_continue` ที่ตัดสินใจว่าจะเรียกใช้เครื่องมือหรือโมเดล

จำนวนโหนดและขอบไม่คงที่ คุณเพิ่มโหนดและขอบ
ได้มากเท่าที่ต้องการลงในกราฟ เช่น คุณอาจเพิ่มโหนดสำหรับการเพิ่มเอาต์พุตที่มีโครงสร้าง หรือโหนดการตรวจสอบ/การไตร่ตรองด้วยตนเองเพื่อตรวจสอบเอาต์พุตของโมเดลก่อนเรียกใช้เครื่องมือหรือโมเดล

```
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig

tools_by_name = {tool.name: tool for tool in tools}

# Define our tool node
def call_tool(state: AgentState):
    outputs = []
    # Iterate over the tool calls in the last message
    for tool_call in state["messages"][-1].tool_calls:
        # Get the tool by name
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # Invoke the model with the system prompt and the messages
    response = model.invoke(state["messages"], config)
    # This returns a list, which combines with the existing messages state
    # using the add_messages reducer.
    return {"messages": [response]}

# Define the conditional edge that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    # If the last message is not a tool call, then finish
    if not messages[-1].tool_calls:
        return "end"
    # default to continue
    return "continue"
```

เมื่อคอมโพเนนต์ของเอเจนต์ทั้งหมดพร้อมแล้ว คุณก็สามารถประกอบคอมโพเนนต์เหล่านั้นได้

```
from langgraph.graph import StateGraph, END

# Define a new graph with our state
workflow = StateGraph(AgentState)

# 1. Add the nodes
workflow.add_node("llm", call_model)
workflow.add_node("tools",  call_tool)
# 2. Set the entrypoint as `agent`, this is the first node called
workflow.set_entry_point("llm")
# 3. Add a conditional edge after the `llm` node is called.
workflow.add_conditional_edges(
    # Edge is used after the `llm` node is called.
    "llm",
    # The function that will determine which node is called next.
    should_continue,
    # Mapping for where to go next, keys are strings from the function return,
    # and the values are other nodes.
    # END is a special node marking that the graph is finish.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)
# 4. Add a normal edge after `tools` is called, `llm` node is called next.
workflow.add_edge("tools", "llm")

# Now we can compile and visualize our graph
graph = workflow.compile()
```

คุณสามารถแสดงภาพกราฟโดยใช้`draw_mermaid_png`วิธีนี้

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

![png](https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png?hl=th)

ตอนนี้ให้เรียกใช้ Agent

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

ตอนนี้คุณสามารถสนทนาต่อ ถามถึงสภาพอากาศในเมืองอื่น หรือขอเปรียบเทียบได้แล้ว

```
state["messages"].append(("user", "Would it be warmer in Munich?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
