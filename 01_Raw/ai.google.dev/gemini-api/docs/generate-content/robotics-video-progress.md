---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=zh-TW
fetched_at: 2026-08-24T02:28:19.326545+00:00
title: "\u5f71\u7247\u89e3\u8b80 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 影片解讀

Gemini Robotics ER 2 可透過兩項功能，從連續的影片串流追蹤工作進度：

- 時刻尋找：找出重要事件發生的確切時間戳記。
- 進度分類：將每部影片歸入五個完成度範圍之一 (0% 至 20%、20% 至 40%、40% 至 60%、60% 至 80%、80% 至 100%)。

## 尋找重要時刻

時刻發現功能可找出發生重大事件的確切影片影格，例如杯子裝滿水或打結。機器人會使用這項資訊驗證成功、序列步驟，以及觸發修正。

以下範例提示會要求模型找出影片中特定工作完成的時刻：

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

以下是尋找時刻影片的範例影格，模型會識別工作完成時間戳記：

![影片畫面範例，顯示含有時間戳記疊加層的時刻尋找輸出內容](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=zh-tw)

## 進度分類

進度分類會將影片歸入五個完成度範圍之一：0% 至 20%、20% 至 40%、40% 至 60%、60% 至 80% 或 80% 至 100%。這項功能可讓機器人即時掌握情況，因此不必重新啟動整個工作流程，就能調整動作或重試失敗的步驟。

以下範例提示會要求模型根據影片分類目前的進度等級：

```
from google import genai
from google.genai import types

client = genai.Client()

with open("task_video.mp4", "rb") as f:
    video_bytes = f.read()

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(data=video_bytes, mime_type="video/mp4"),
        prompt,
    ],
)

print(response.text)
```

下圖顯示進度分類影片的範例影格，模型會指派進度範圍：

![影片影格範例，顯示進度分類輸出內容和進度括號標籤](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=zh-tw)

## 範例

如需完整的可執行範例 (包括多步驟工作追蹤)，請參閱[機器人食譜](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)。

## 後續步驟

- [機器人即時 API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-tw)：即時雙向串流。
- [工作自動化調度管理](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-tw)：需要空間推理的長期工作。
- [Gemini Robotics ER 總覽](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-tw)：模型比較和功能。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-30 (世界標準時間)。"],[],[]]
