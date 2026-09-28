---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=zh-CN
fetched_at: 2026-09-28T06:14:34.506879+00:00
title: "\u89c6\u9891\u7406\u89e3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 视频理解

Gemini Robotics ER 2 可以使用以下两种功能跟踪连续视频馈送中的任务进度：

- 时刻查找：识别关键事件发生的精确时间戳。
- 进度分类：将每个视频分配到五个完成度范围之一（0-20%、20-40%、40-60%、60-80%、80-100%）。

## 时刻查找

时刻查找功能可以识别关键事件发生的精确视频帧，例如杯子装满或结被系好时。机器人使用此功能来验证成功、按顺序执行步骤和触发更正。

以下示例提示要求模型识别视频中给定任务的完成时刻：

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

以下示例展示了时刻查找视频中的示例帧，模型识别了任务完成时间戳：

![示例视频帧，显示了带有时间戳叠加层的精彩瞬间查找输出](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=zh-cn)

## 进度分类

进度分类功能会将视频分配到五个完成度范围之一：0-20%、20-40%、40-60%、60-80% 或
80-100%。这使机器人能够实时了解情况，以便调整操作或重试失败的步骤，而无需重启整个工作流。

以下示例提示要求模型对视频中的当前进度级别进行分类：

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

以下示例展示了进度分类视频中的示例帧，模型分配了进度范围：

![示例视频帧，显示了带有进度括号标签的进度分类输出](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=zh-cn)

## 示例

如需查看包含多步任务跟踪的完整可运行示例，请参阅
[机器人技术 Cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)。

## 后续步骤

- [机器人技术 Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-cn) - 实时双向流式传输。
- [任务编排](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-cn) - 具有空间推理的长时程任务。
- [Gemini Robotics ER 概览](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-cn) - 模型比较和功能。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-08。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-08。"],[],[]]
