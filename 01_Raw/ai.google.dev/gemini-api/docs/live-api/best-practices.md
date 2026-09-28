---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=zh-CN
fetched_at: 2026-09-28T06:20:43.926276+00:00
title: "Live API \u6700\u4f73\u5b9e\u8df5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Live API 最佳实践

本指南介绍了可用于优化 Live API 使用的最佳实践。
如需查看概览和常见用例的示例代码，请参阅[开始使用 Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-cn) 页面。

## 设计清晰的系统指令

为了充分发挥 Live API 的性能，建议您有一套清晰定义的系统指令 (SI)，按照智能体角色、对话规则和保护措施的顺序进行定义。

为获得最佳结果，请将每个智能体分离到不同的 SI 中。

1. **指定智能体的角色设定**：详细说明智能体的名称、角色和任何偏好特征。如果您想指定口音，请务必同时指定首选输出语言（例如，针对说英语的人指定英式口音）。
2. **指定对话规则**：按您希望模型遵循的顺序放置这些规则。划分对话中一次性元素和对话循环之间的界限。例如：

   - **一次性元素**：一次性收集客户的详细信息（例如姓名、位置、会员卡号）。
   - **对话循环**：用户可以讨论建议、价格、退货和配送，并可能希望在不同主题之间切换。让模型知道，只要用户愿意，就可以一直进行这种对话循环。
3. **在流程中以单独的句子指定工具调用**：例如，如果收集客户详细信息的一次性步骤需要调用一个 `get_user_info` 函数，您可以这样说：*第一步是收集用户信息。首先，要求用户提供其姓名、位置信息和会员卡号。然后，使用这些详细信息调用 `get_user_info`。*
4. **添加任何必要的保护措施**：提供您不希望模型执行的任何通用对话保护措施。您可以随意提供具体示例，例如，说明如果发生 *x*，您希望模型执行 *y*。如果您仍未获得所需的精确度，请使用“*毫无疑问*”一词来引导模型提高精确度。

## 精确定义工具

将工具与 Live API 搭配使用时，工具定义应具体明确。务必告知 Gemini 在什么条件下应调用工具。如需了解详情，请参阅示例部分中的[工具定义](#tool-definitions-example)。

## 撰写有效的提示

- **使用清晰的提示**：在提示中提供模型应该和不应该做什么的示例，并尽量限制每个提示只针对一个角色或身份。考虑使用提示链代替冗长的多页提示。模型在涉及单一函数调用的任务上表现最佳。
- **提供起始命令和信息**：Live API 在响应前需要用户输入。如要让 Live API 发起对话，请添加一个要求它向用户问好或开始对话的提示。添加有关用户的信息，以便 Live API 对问候语进行个性化设置。

## 指定语言

实时 API 音频模型会自动检测并适应用户的口语，而无需明确的语言代码。

如果您希望模型以特定语言回答，请在系统指令中添加相关指令：

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## 流式

在实现实时音频时，请遵循以下最佳实践：

- **块大小和延迟时间**：以 20 毫秒到 40 毫秒的块发送音频。
- **中断处理**：当用户在模型回复期间说话时，服务器会发送包含 `"interrupted": true` 的 `server_content` 消息。您必须立即舍弃客户端音频缓冲区，以防止智能体继续打断用户说话。

## 上下文管理

对于长时间会话，请使用 `ContextWindowCompressionConfig`，因为原生音频 token 会快速累积（大约每秒音频 25 个 token）。

## 客户端缓冲

在发送之前，不要大幅缓冲输入音频（例如 1 秒）。发送小块（20 毫秒 - 100 毫秒）以最大限度减少延迟时间。

## 重新采样

确保您的客户端应用在传输之前将麦克风输入（通常为 44.1kHz 或 48kHz）重新采样为 16kHz。

## 会话管理

请遵循以下准则来处理会话生命周期，并确保提供可靠的用户体验：

- **启用上下文窗口压缩**：音频 token 的累积速度约为每秒 25 个 token。如果不压缩，纯音频会话时长上限为 15 分钟，音频-视频会话时长上限为 2 分钟。启用[上下文窗口压缩](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-cn#context-window-compression)，将对话时长延长至无限时长。
- **实现会话恢复**：服务器可能会定期重置 WebSocket 连接。使用[会话恢复](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-cn#session-resumption)功能，在不丢失上下文的情况下无缝重新连接。保留来自 `SessionResumptionUpdate` 条消息的最新恢复令牌，并在重新连接时将其作为句柄传递。恢复令牌在上次会话终止后 2 小时内有效。
- **处理 GoAway 消息**：服务器会在终止连接之前发送 [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-cn#goaway-message) 消息。侦听此消息，并在连接关闭之前使用 `timeLeft` 字段来正常结束或重新连接。
- **处理 generationComplete 信号**：使用 [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-cn#generation-complete-message) 消息来了解模型何时完成回答生成，以便您的应用可以更新其界面或继续执行下一个操作。

如需了解实现详情，请参阅[会话管理](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-cn)。

## 示例

此示例结合了最佳实践和[系统指令设计指南](#system-instruction-guidelines)，旨在引导模型发挥职业规划师的作用。

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### 工具定义

此 JSON 定义了职业规划师示例中调用的相关函数。为获得最佳效果，请在定义函数时添加其名称、说明、参数和调用条件。

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## 定价和结算

Gemini Live API 严格按令牌使用量计费。由于 Live API 会维护持久的 WebSocket 会话，因此费用会根据有效上下文窗口采用复合模型进行计算。

### 会话上下文窗口（复合费用）

API 会根据会话上下文窗口中存在的所有令牌按轮次向您收费。“轮次”是指一次用户输入和模型相应的回答。

- **累积**：上下文窗口包含当前轮次的新 token，以及之前轮次的所有累积 token。
- **重新结算**：系统会在每个新回合中重新处理之前的 token 并将其纳入结算范围，直至达到您配置的上下文窗口大小。随着会话时长的增加，每轮对话的费用也会增加，因为系统会重新处理对话历史记录。

### 音频令牌和转写内容

Live API 采用原生多模态架构。它会以原始音频令牌的形式保留对话历史记录，以保留声音细微差别和音调。

- **音频结算**：API 会在每个回合中按标准音频输入费率向您收取累积的原生音频令牌费用。
- **转写附加费**：启用音频转写为文本功能（`inputAudioTranscription` 或 `outputAudioTranscription`）后，除了标准的音频 token 费用外，API 还会按文本 token 输出费率针对转写生成的所有文本 token 收费。

### 通过上下文限制管理费用

为防止长时间会话中的费用无限增长，请使用 `contextWindowCompression` 配置上下文窗口大小。

通过设置压缩触发器（例如 25,000 个令牌）和滑动窗口（例如 8,000 个令牌），API 会在达到阈值后自动逐出较旧的令牌。然后，该 API 仅针对保留的历史记录和任何新令牌收取后续对话轮次的费用。

### 主动音频

启用主动音频后，API 会在 Live API 监听的整个时间段内针对输入令牌收费，并且仅在 API 做出响应时针对输出令牌收费。

- **针对 Gemini 3.8 的注意事项**：在 `gemini-3.8-live` 和 `gemini-3.8-live-extended-thinking` 中，主动音频功能永久处于启用状态。
- **Gemini 3.1 注意事项**：`gemini-3.1-flash-live-preview` 不支持主动音频。对于此模型，当您主动流式传输输入时，API 仅针对音频收费。

如需详细了解价格信息，请参阅 [Gemini API 价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-17。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-17。"],[],[]]
