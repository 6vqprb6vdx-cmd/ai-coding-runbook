---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=zh-CN
fetched_at: 2026-09-28T06:12:31.180814+00:00
title: "API \u9519\u8bef \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# API 错误

本页提供了所有 Interactions API 错误代码的参考信息，介绍了错误响应格式，并说明了该 API 如何针对不同的请求类型传递错误。

## 标准 API 错误代码

这些常规请求级错误代码对应于标准 HTTP 状态代码。使用应用逻辑中的 `code` 字段以编程方式处理错误。

| 代码 | HTTP Status | 说明 | 建议采取的操作 |
| --- | --- | --- | --- |
| `invalid_request` | 400 无效请求 | 请求载荷格式不正确或包含无效参数。 | 对照 [API 参考文档](https://ai.google.dev/api/interactions-api?hl=zh-cn)检查您的请求语法和参数。 |
| `failed_precondition` | 400 无效请求 | 由于未满足前提条件（例如，结算已停用），因此无法处理相应请求。 | 验证项目结算状态或账号前提条件。 |
| `out_of_range` | 416 Requested Range Not Satisfiable | 请求参数超出有效范围。 | 检查参数值和限制。 |
| `parameter_unknown` | 400 无效请求 | 请求包含未知参数。 | 移除无法识别的参数，然后重试。 |
| `authentication` | 401 未经授权 | API 密钥缺失、无效或已过期。 | 验证您的 [API 密钥](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn)。 |
| `payment_required` | 402 Payment Required | 您的预付款余额已用完。 | 向结算账号[添加点数](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#buy-credits)，或开启[自动充值](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn#auto-reload)。请勿重试：在添加积分之前，请求不会成功。 |
| `permission_denied` | 403 禁止访问 | 您的 API 密钥没有此资源的权限。 | 检查您的 API 密钥权限和项目访问权限。 |
| `not_found` | 404 未找到 | 找不到所请求的资源。 | 验证资源路径和参数。 |
| `model_not_found` | 404 未找到 | 未找到指定的模型。 | 验证模型名称或回退到其他模型。 |
| `already_exists` | 409 Conflict | 您尝试创建的实体已存在。 | 在重新创建之前，检查资源是否已存在。 |
| `aborted` | 409 Conflict | 由于存在冲突或并发检查失败，操作已中止。 | 在更高的应用级别重试请求。 |
| `rate_limit_exceeded` | 429 请求过多 | 您已超出每分钟或每秒请求数或令牌数上限。 | 等待一段时间并重试（使用指数退避算法）。 |
| `quota_exceeded` | 429 请求过多 | 您已超出每日配额。 | 请等待配额重置，或申请增加配额。 |
| `too_many_requests` | 429 请求过多 | 您在短时间内发出的请求过多。 | 等待一段时间并重试（使用指数退避算法）。 |
| `cancelled` | 499 Client Closed Request | 客户端在请求完成之前取消了该请求。 | 您无需执行任何操作。这通常表示客户端已断开连接。 |
| `api_error` | 500 内部服务器错误 | 服务器上发生了意外错误。 | 重试请求。如果问题仍然存在，请与支持团队联系。 |
| `unimplemented` | 501 Not Implemented | 相应操作或功能未实现或不受支持。 | 检查 API 功能或切换到受支持的功能。 |
| `service_unavailable` | 503 Service Unavailable | 服务暂时过载或关闭。 | 等待一段时间并重试（使用指数退避算法）。 |
| `deadline_exceeded` | 504 Gateway Timeout | 请求未在截止期限内完成。 | 移除或增加客户端截止期限设置以使用服务器默认值。 |

## 生成被屏蔽的代码

这些错误代码表明，政策、安全或内容限制阻止了模型的输出。收到这些代码之一时，请修改输入并重试。

| 代码 | 说明 |
| --- | --- |
| `safety` | 安全违规行为（有害内容）导致请求被屏蔽。 |
| `recitation` | 版权或朗诵限制导致请求被屏蔽。 |
| `language` | 请求因语言不受支持而被阻止。 |
| `prohibited_content` | 由于违反了禁止的内容准则，系统屏蔽了该请求。 |
| `spii` | “敏感的个人身份信息”限制阻止了相应请求。 |
| `blocklist` | 屏蔽名单中的禁止字词导致请求被屏蔽。 |
| `image_safety` | 安全违规行为导致图片生成被阻止。 |
| `image_prohibited_content` | 禁止的内容准则阻止了图片生成。 |
| `image_recitation` | 版权或朗诵限制导致图片生成被阻止。 |
| `image_other` | 因不明原因而无法生成图片。 |
| `content_blocked` | 因不明政策原因而阻止了相应请求。 |

## 生成错误代码

这些错误代码表示模型生成的输出存在结构性问题（例如函数调用格式不正确或工具调用未声明）。

| 代码 | 说明 |
| --- | --- |
| `malformed_function_call` | 模型生成了无法解析的函数调用。 |
| `malformed_tool_call` | 模型生成的工具调用无法解析。 |
| `unexpected_tool_call` | 模型调用了未在请求中声明的工具。 |
| `no_image` | 模型无法生成图片。 |
| `too_many_tool_calls` | 模型生成的工具调用次数超出了允许的次数。 |
| `missing_thought_signature` | 回答缺少必需的思路签名。 |

## 错误响应格式

来自 Interactions API 的所有错误都会返回一个包含 `code` 和 `message` 的 `error` 对象。例如，传递不受支持的工具类型会返回：

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `code` | 字符串 | `snake_case` 中的机器可读错误代码。 |
| `message` | 字符串 | 直观易懂的错误说明。 |

## 错误传递方式

该 API 会以不同的方式传递错误，具体取决于您是发出标准 HTTP 请求还是流式传输 (SSE) 请求。

### 标准 HTTP 请求

对于标准（非流式）请求，API 会设置 HTTP 响应状态代码（例如 `400 Bad Request`、`401 Unauthorized` 或 `429 Too Many Requests`），并在 JSON 响应正文中返回 `error` 对象：

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### 流式传输 (SSE) 请求

对于流式请求 (`stream: true`)，API 会通过服务器发送的事件 (SSE) 流发送错误事件，并将 `event_type` 设置为 `"error"`。`error` 字段包含相同的 `code` 和 `message` 结构：

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

如需查看完整的 SSE 事件架构，请参阅 [Interactions API 参考文档](https://ai.google.dev/api/interactions-api?hl=zh-cn)。

## 后续步骤

- [API 问题排查](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=zh-cn)：解决常见问题和错误情形。
- [速率限制](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-cn)：了解请求限制和配额处理。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-20。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-20。"],[],[]]
