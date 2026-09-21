---
source_url: https://ai.google.dev/gemini-api/docs/llama-index?hl=zh-CN
fetched_at: 2026-09-21T05:47:40.590306+00:00
title: "\u4f7f\u7528 Gemini \u548c LlamaIndex \u7684\u7814\u7a76\u4ee3\u7406 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Gemini 和 LlamaIndex 的研究代理

LlamaIndex 是一个框架，用于使用连接到数据的 LLM 构建知识智能体。此示例向您展示了如何为研究智能体构建多智能体工作流。在 LlamaIndex 中，[`Workflows`](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
是智能体和多智能体系统的构建块。

您需要 Gemini API 密钥。如果您还没有 API 密钥，可以在
[Google AI Studio 中获取一个](https://aistudio.google.com/apikey?hl=zh-cn)。
首先，安装所有必需的 LlamaIndex 库。LlamaIndex 在后台使用 `google-genai` 软件包。

```
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## 在 LlamaIndex 中设置 Gemini

任何 LlamaIndex 智能体的引擎都是一个大语言模型，用于处理推理和文本处理。此示例使用 Gemini 3 Flash。[请确保将 API 密钥设置为环境变量。](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn)

```
import os
from llama_index.llms.google_genai import GoogleGenAI

# Set your API key in the environment elsewhere, or with os.environ['GEMINI_API_KEY'] = '...'
assert 'GEMINI_API_KEY' in os.environ

llm = GoogleGenAI(model="gemini-3.6-flash")
```

## 构建工具

智能体使用工具与外部世界互动，例如搜索网络或存储信息。[LlamaIndex 中的工具](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
可以是常规 Python 函数，也可以从预先存在的 `ToolSpecs` 中导入。
Gemini 附带一个用于使用 Google 搜索的内置工具，此处将使用该工具。

```
from google.genai import types

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

llm_with_search = GoogleGenAI(
    model="gemini-3.6-flash",
    generation_config=types.GenerateContentConfig(tools=[google_search_tool])
)
```

现在，使用需要搜索的查询测试 LLM 实例。本指南假定有一个正在运行的事件循环（例如 `python -m asyncio` 或 Google Colab）。

```
response = await llm_with_search.acomplete("What's the weather like today in Biarritz?")
print(response)
```

研究智能体将使用 Python 函数作为工具。您可以通过多种方式构建一个系统来执行此任务。在此示例中，您将使用以下内容：

1. `search_web` 使用 Gemini 和 Google 搜索在网络上搜索有关给定主题的信息。
2. `record_notes` 将在网络上找到的研究结果保存到状态，以便其他工具可以使用它。
3. `write_report` 使用 `ResearchAgent` 找到的信息编写报告
4. `review_report` 审核报告并提供反馈。

`Context` 类在智能体/工具之间传递状态，每个智能体都可以访问系统的当前状态。

```
from llama_index.core.workflow import Context

async def search_web(ctx: Context, query: str) -> str:
    """Useful for searching the web about a specific query or topic"""
    response = await llm_with_search.acomplete(f"""Please research given this query or topic,
    and return the result\n<query_or_topic>{query}</query_or_topic>""")
    return response

async def record_notes(ctx: Context, notes: str, notes_title: str) -> str:
    """Useful for recording notes on a given topic."""
    current_state = await ctx.store.get("state")
    if "research_notes" not in current_state:
        current_state["research_notes"] = {}
    current_state["research_notes"][notes_title] = notes
    await ctx.store.set("state", current_state)
    return "Notes recorded."

async def write_report(ctx: Context, report_content: str) -> str:
    """Useful for writing a report on a given topic."""
    current_state = await ctx.store.get("state")
    current_state["report_content"] = report_content
    await ctx.store.set("state", current_state)
    return "Report written."

async def review_report(ctx: Context, review: str) -> str:
    """Useful for reviewing a report and providing feedback."""
    current_state = await ctx.store.get("state")
    current_state["review"] = review
    await ctx.store.set("state", current_state)
    return "Report reviewed."
```

## 构建多智能体助理

如需构建多智能体系统，您需要定义智能体及其互动。
您的系统将包含三个智能体：

1. `ResearchAgent` 在网络上搜索有关给定主题的信息。
2. `WriteAgent` 使用 `ResearchAgent` 找到的信息编写报告。
3. `ReviewAgent` 审核报告并提供反馈。

此示例使用 `AgentWorkflow` 类创建一个多智能体系统，该系统将按顺序执行这些智能体。每个智能体都会获取一个 `system_prompt`，该提示会告知智能体应执行的操作，并建议如何与其他智能体协作。

（可选）您可以使用 `can_handoff_to` 指定多智能体系统可以与其他哪些智能体通信，从而帮助该系统（否则，它会尝试自行确定）。

```
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)
from llama_index.core.agent.workflow import FunctionAgent, ReActAgent

research_agent = FunctionAgent(
    name="ResearchAgent",
    description="Useful for searching the web for information on a given topic and recording notes on the topic.",
    system_prompt=(
        "You are the ResearchAgent that can search the web for information on a given topic and record notes on the topic. "
        "Once notes are recorded and you are satisfied, you should hand off control to the WriteAgent to write a report on the topic."
    ),
    llm=llm,
    tools=[search_web, record_notes],
    can_handoff_to=["WriteAgent"],
)

write_agent = FunctionAgent(
    name="WriteAgent",
    description="Useful for writing a report on a given topic.",
    system_prompt=(
        "You are the WriteAgent that can write a report on a given topic. "
        "Your report should be in a markdown format. The content should be grounded in the research notes. "
        "Once the report is written, you should get feedback at least once from the ReviewAgent."
    ),
    llm=llm,
    tools=[write_report],
    can_handoff_to=["ReviewAgent", "ResearchAgent"],
)

review_agent = FunctionAgent(
    name="ReviewAgent",
    description="Useful for reviewing a report and providing feedback.",
    system_prompt=(
        "You are the ReviewAgent that can review a report and provide feedback. "
        "Your feedback should either approve the current report or request changes for the WriteAgent to implement."
    ),
    llm=llm,
    tools=[review_report],
    can_handoff_to=["ResearchAgent","WriteAgent"],
)
```

智能体已定义，现在您可以创建 `AgentWorkflow` 并高效运转它。

```
from llama_index.core.agent.workflow import AgentWorkflow

agent_workflow = AgentWorkflow(
    agents=[research_agent, write_agent, review_agent],
    root_agent=research_agent.name,
    initial_state={
        "research_notes": {},
        "report_content": "Not written yet.",
        "review": "Review required.",
    },
)
```

在工作流执行期间，您可以将事件、工具调用和更新流式传输到控制台。

```
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)

research_topic = """Write me a report on the history of the web.
Briefly describe the history of the world wide web, including
the development of the internet and the development of the web,
including 21st century developments"""

handler = agent_workflow.run(
    user_msg=research_topic
)

current_agent = None
current_tool_calls = ""
async for event in handler.stream_events():
    if (
        hasattr(event, "current_agent_name")
        and event.current_agent_name != current_agent
    ):
        current_agent = event.current_agent_name
        print(f"\n{'='*50}")
        print(f"🤖 Agent: {current_agent}")
        print(f"{'='*50}\n")
    elif isinstance(event, AgentOutput):
        if event.response.content:
            print("📤 Output:", event.response.content)
        if event.tool_calls:
            print(
                "🛠️  Planning to use tools:",
                [call.tool_name for call in event.tool_calls],
            )
    elif isinstance(event, ToolCallResult):
        print(f"🔧 Tool Result ({event.tool_name}):")
        print(f"  Arguments: {event.tool_kwargs}")
        print(f"  Output: {event.tool_output}")
    elif isinstance(event, ToolCall):
        print(f"🔨 Calling Tool: {event.tool_name}")
        print(f"  With arguments: {event.tool_kwargs}")
```

工作流完成后，您可以打印报告的最终输出，以及审核智能体的最终审核状态。

```
state = await handler.ctx.store.get("state")
print("Report Content:\n", state["report_content"])
print("\n------------\nFinal Review:\n", state["review"])
```

## 使用自定义工作流进一步探索

`AgentWorkflow` 是开始使用多智能体系统的绝佳方式。但如果您需要更多控制权，该怎么办？您可以从头开始构建工作流。以下是您可能需要构建自己的工作流的一些原因：

- **更好地控制流程**：您可以决定智能体采取的确切路径
  。这包括创建循环、在特定时间点做出决策，或让智能体并行处理不同的任务。
- **使用复杂数据**：超越纯文本。借助自定义工作流，您可以将更多结构化数据（例如 JSON 对象或自定义类）用于输入和输出。
- **使用不同的媒体**：构建不仅可以理解和处理文本，还可以理解和处理图像、音频和视频的智能体。
- **更智能的规划**：您可以设计一个工作流，让智能体先制定
  详细计划，然后再开始工作。这对于需要多个步骤的复杂任务非常有用。
- **启用自我纠正**：创建可以审核自己工作的智能体。如果输出不够好，智能体可以重试，从而创建一个改进循环，直到结果完美为止。

如需详细了解 LlamaIndex 工作流，请参阅 [LlamaIndex 工作流
文档](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-12。"],[],[]]
