---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-TW
fetched_at: 2026-11-02T07:17:18.230028+00:00
title: "\u900f\u904e\u4e32\u6d41\u529f\u80fd\u4f7f\u7528\u6a5f\u5668\u4eba \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 透過串流功能使用機器人

`gemini-robotics-er-2-streaming-preview` 模型端點會公開專用的串流端點，與 [Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-tw) 整合，讓應用程式與機器人之間進行即時雙向互動。因此適合需要快速意見回饋循環，以及對環境做出反應式回應的代理程式。

[在 Google AI Studio 中試用](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=zh-tw)
[從 GitHub 複製範例應用程式](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## 用途

- **多機器人協調**：多個機器人透過共用工作階段傳達工作狀態並委派子工作。
- **持續監控**：機器人會觀察場景並在發生特定事件時觸發動作，例如容器達到填充量。
- **倉庫和物流**：揀貨和包裝人員會目視檢查商品、追蹤包裝進度，以及從錯誤中復原。

## 技術規格

下表列出 Live API 的技術規格：

| 類別 | 詳細資料 |
| --- | --- |
| 輸入模態 | 音訊 (原始 16 位元 PCM 音訊，16 kHz，小端序)、圖片 (JPEG <= 1 FPS)、文字 |
| 輸出模態 | 文字 |
| 通訊協定 | 具狀態的 WebSocket 連線 (WSS) |

## 建構代理設定

透過 Live API 建構的每個機器人代理程式都會經過下列三個步驟：

1. **將機器人功能宣告為工具。**機器人可執行的每個動作 (例如導覽、抓取、說話) 都會成為函式宣告，並包含名稱、說明和參數結構定義。實體動作必須使用 `"behavior": "BLOCKING"`，模型才會等待機器人完成動作，再選擇下一個步驟。
2. **將多模態輸入內容串流至持續性工作階段。**開啟 `live.connect`
   工作階段，並在工作期間保持開啟狀態。從機器人感應器接收影片畫面、音訊或文字時，立即傳送。
3. **在接收迴圈中處理工具呼叫。**模型每次選取動作時，都會傳送 `tool_call` 訊息。接收迴圈會針對機器人 SDK 執行函式，並傳回 `tool_response`。工作階段會保持開啟，模型會根據結果選擇下一個動作。

以下各節說明如何將這些步驟套用至三種常見模式：基準代理迴圈、透過活動訊號主動監控場景，以及透過文字轉語音將語音路由為工具。

## 透過函式呼叫協調機器人

以下範例顯示在單一 Python 指令碼中，這三個步驟如何連結在一起。

步驟 1 - 工具定義 - 將機器人功能宣告為函式宣告。`navigate` 函式會使用 `"behavior": "BLOCKING"`，因此模型會等待機器人抵達航點，再呼叫其他工具。在同一個清單中新增更多函式宣告，即可公開其他機器人功能。

步驟 2 - 輸入輔助程式 - 顯示三個函式，可將不同模式的輸入內容串流至工作階段：`send_text` 用於指令、`send_image` 用於攝影機畫面 (可選用文字提示詞)，以及 `send_audio` 用於麥克風的原始 PCM 音訊。

步驟 3 (接收迴圈) 會同時執行，並處理兩種訊息：`server_content` 訊息 (模型的文字輸出內容) 和 `tool_call` 訊息 (模型要求機器人執行的動作)。收到工具呼叫時，迴圈會呼叫 `execute_tool` (您以實際的機器人 SDK 取代這個存根)，然後傳回 `tool_response`，模型即可選取下一個動作。

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

每次工具回覆後，接收迴圈都會保持啟用狀態。模型會建構及修訂長期計畫，您不必預先編碼整個動作序列。

## 主動式時空推論

Live API 會串流播放影片，但單獨的影片影格不會觸發新的推理回合。影片影格必須附上文字或音訊提示，才能觸發模型回應。詳情請參閱[即時 API 功能](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=zh-tw)。

如要啟用主動推論功能，請實作**活動訊號**：定期傳送最新的相機畫面，然後傳送簡短的文字提示詞，強制模型檢查場景並做出明確的決定。影片輸入的速率限制為每秒一個影格。

### 實作心跳

心跳協同程式會在同一個工作階段中，以單獨的 `asyncio` 工作形式執行。
在等待每個回合完成 (`er_turn_done`) 時，系統會盡量以 1 Hz 的節奏為目標 (符合影片輸入速率限制)，避免中斷進行中的推理：

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### 更新接收迴圈

如要指出模型何時完成輪流，請更新 `receive_loop` 將 `er_turn_done` 設為：

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## 透過外部 TTS 輸出音訊

Gemini Robotics ER 2 會傳回文字。應用程式會透過插入的回呼，將完成的回覆傳送至其他 TTS 供應商 (例如 [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw))。這樣一來，您就能控管語音延遲、語音選擇和中斷行為，並在不變更代理程式邏輯的情況下，切換 TTS 後端。

你也可以將 TTS 宣告為工具，這樣模型就會將「說些什麼」視為與「移動手臂」相同的指令。將下列函式宣告新增至第一個區段的 `tools` 清單：

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

將 TTS 包裝在函式宣告中，模型會透過與任何其他機器人動作相同的工具呼叫路徑處理語音。您的應用程式會透過插入的回呼執行呼叫。

## GitHub 上的範例

如需完整的有效範例，包括 Spot 機器人零食取回示範和 Tinybot 雲台 Hello World，請參閱 [Robotics Live API 範例](https://github.com/google-gemini/robotics-samples/tree/main/live-api)。

## 後續步驟

- [影片理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=zh-tw)：尋找特定時刻和分類進度。
- [工作自動化調度管理](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-tw)：不需串流的長期工作。
- [Live API 總覽](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-tw)：完整的 Live API 說明文件。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-16 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-16 (世界標準時間)。"],[],[]]
