---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=vi
fetched_at: 2026-09-07T05:36:44.125323+00:00
title: "Ng\u01b0\u1eddi m\u00e1y c\u00f3 t\u00ednh n\u0103ng truy\u1ec1n ph\u00e1t tr\u1ef1c tuy\u1ebfn \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Người máy có tính năng truyền phát trực tuyến

Điểm cuối mô hình `gemini-robotics-er-2-streaming-preview` cung cấp một điểm cuối truyền trực tuyến chuyên dụng, tích hợp với [Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=vi), cho phép tương tác hai chiều theo thời gian thực giữa ứng dụng của bạn và robot. Điều này khiến nó phù hợp với những tác nhân cần vòng phản hồi nhanh và phản ứng nhanh với môi trường.

[Dùng thử trong Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=vi)
[Sao chép các ứng dụng mẫu từ GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## Trường hợp sử dụng

- **Điều phối nhiều robot**: Nhiều robot giao tiếp trạng thái tác vụ và uỷ quyền các tác vụ phụ thông qua một phiên dùng chung.
- **Giám sát liên tục**: Các robot quan sát một cảnh và kích hoạt hành động khi các sự kiện cụ thể xảy ra, chẳng hạn như khi một thùng chứa đạt đến mức đổ đầy.
- **Kho hàng và hoạt động kho vận**: Nhân viên chọn và đóng gói xác minh các mặt hàng bằng mắt, theo dõi tiến trình đóng gói và khắc phục lỗi.

## Quy cách kỹ thuật

Bảng sau đây trình bày các quy cách kỹ thuật của Live API:

| Danh mục | Thông tin chi tiết |
| --- | --- |
| Phương thức nhập | Âm thanh (âm thanh PCM 16 bit thô, 16 kHz, little-endian), hình ảnh (JPEG <= 1 khung hình/giây), văn bản |
| Phương thức đầu ra | Văn bản |
| Giao thức | Kết nối WebSocket có trạng thái (WSS) |

## Xây dựng một chế độ thiết lập dựa trên tác nhân

Mọi tác nhân robot được xây dựng trên Live API đều tuân theo 3 bước:

1. **Khai báo các chức năng của robot dưới dạng công cụ.** Mỗi hành động mà robot có thể thực hiện (điều hướng, nắm bắt, nói) sẽ trở thành một khai báo hàm có tên, nội dung mô tả và giản đồ tham số. Các hành động thực tế phải sử dụng `"behavior": "BLOCKING"` để mô hình đợi robot hoàn thành trước khi chọn bước tiếp theo.
2. **Truyền thông tin đầu vào đa phương thức vào một phiên liên tục.** Mở một phiên `live.connect` và giữ phiên đó mở trong suốt thời gian thực hiện nhiệm vụ. Gửi khung hình video, âm thanh hoặc văn bản khi chúng đến từ các cảm biến của robot.
3. **Xử lý lệnh gọi công cụ trong một vòng lặp nhận.** Mỗi khi chọn một hành động, mô hình sẽ gửi thông báo `tool_call`. Vòng lặp nhận của bạn thực thi hàm đối với SDK robot và gửi lại một `tool_response`. Phiên vẫn mở và mô hình sẽ chọn hành động tiếp theo dựa trên kết quả.

Các phần sau đây cho biết cách áp dụng các bước này cho 3 mẫu phổ biến: vòng lặp tác nhân cơ sở, tính năng giám sát cảnh chủ động bằng tín hiệu nhịp tim và định tuyến lời nói thông qua TTS như một công cụ.

## Điều phối một robot thông qua tính năng gọi hàm

Ví dụ sau đây cho thấy cả 3 bước được kết nối với nhau trong một tập lệnh Python duy nhất.

Bước 1 – định nghĩa công cụ – khai báo các chức năng của robot dưới dạng khai báo hàm. Hàm `navigate` sử dụng `"behavior": "BLOCKING"` nên mô hình sẽ đợi robot đến điểm tham chiếu trước khi gọi một công cụ khác.
Thêm nhiều khai báo hàm hơn vào cùng một danh sách để cho thấy các chức năng bổ sung của robot.

Bước 2 – trình trợ giúp đầu vào – cho thấy 3 hàm truyền trực tuyến các đầu vào có phương thức khác nhau vào phiên: `send_text` cho các lệnh, `send_image` cho khung hình camera có câu lệnh văn bản không bắt buộc và `send_audio` cho âm thanh PCM thô từ micrô.

Bước 3 – vòng lặp nhận – chạy đồng thời và xử lý hai loại thông báo: thông báo `server_content` (đầu ra văn bản của mô hình) và thông báo `tool_call` (mô hình yêu cầu một hành động của robot). Khi một lệnh gọi công cụ đến, vòng lặp sẽ gọi `execute_tool` – một mã giả lập mà bạn thay thế bằng SDK robot thực của mình – sau đó gửi lại `tool_response` để mô hình có thể chọn hành động tiếp theo.

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

Vòng lặp nhận vẫn hoạt động sau mỗi phản hồi của công cụ. Mô hình này xây dựng và sửa đổi kế hoạch dài hạn mà không cần bạn mã hoá trước toàn bộ chuỗi hành động.

## Suy luận chủ động về không gian và thời gian

Live API truyền trực tiếp video, nhưng chỉ khung hình video không kích hoạt lượt suy luận mới. Khung hình video phải đi kèm với một câu lệnh bằng văn bản hoặc âm thanh để kích hoạt phản hồi của mô hình. Hãy xem [Các chức năng của Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=vi) để biết thêm thông tin chi tiết.

Để bật tính năng suy luận chủ động, hãy triển khai một **xung nhịp**: định kỳ gửi khung hình camera mới nhất, sau đó là một câu lệnh văn bản ngắn buộc mô hình kiểm tra cảnh và đưa ra quyết định rõ ràng. Tốc độ đầu vào của video bị giới hạn ở một khung hình mỗi giây.

Thêm coroutine này cùng với vòng lặp nhận từ phần trước. Thao tác này chạy dưới dạng một tác vụ `asyncio` riêng biệt trong cùng một phiên:

```
async def heartbeat(session, camera):  # camera is your robot camera API
    while True:
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
        await asyncio.sleep(1)
```

Bạn không cần tạm dừng tín hiệu nhịp tim trong các thao tác của robot. Khi được dùng làm **trình phát hiện thành công ngầm**, việc duy trì hoạt động của nó cho phép mô hình liên tục quan sát hành động đang diễn ra (theo dõi xem thao tác nắm có chắc chắn hay không, thao tác đổ có đúng mục tiêu hay không hoặc một đối tượng có đang ổn định đúng cách hay không) và phản ứng ngay khi kết quả trở nên rõ ràng.

Thông báo nhịp tim đóng vai trò là lượt của người dùng và làm gián đoạn quá trình tạo mô hình đang diễn ra.
Hãy xem [hướng dẫn về API Phát trực tiếp đối với các trường hợp gián đoạn](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=vi#interruptions) để tìm hiểu cách API Phát trực tiếp xử lý hành vi này.

## Đầu ra âm thanh thông qua TTS bên ngoài

Gemini Robotics ER 2 trả về văn bản. Ứng dụng của bạn sẽ định tuyến các phản hồi đã hoàn tất đến một nhà cung cấp TTS riêng biệt (chẳng hạn như [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi)) thông qua một lệnh gọi lại được chèn.
Điều này giúp bạn kiểm soát độ trễ của lời nói, lựa chọn giọng nói và hành vi gián đoạn, đồng thời cho phép bạn hoán đổi các phần phụ trợ TTS mà không cần thay đổi logic của tác nhân.

Bạn cũng có thể khai báo TTS là một công cụ để mô hình coi "nói điều gì đó" giống như "di chuyển cánh tay". Thêm khai báo hàm sau vào danh sách `tools` của bạn từ phần đầu tiên:

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

Bằng cách bao bọc TTS trong một khai báo hàm, mô hình sẽ xử lý lời nói thông qua cùng một đường dẫn gọi công cụ như mọi hành động khác của robot. Ứng dụng của bạn thực hiện lệnh gọi bằng một lệnh gọi lại được chèn.

## Ví dụ trên GitHub

Để xem các ví dụ đầy đủ về cách thức hoạt động, bao gồm cả bản minh hoạ về việc lấy đồ ăn nhẹ của robot Spot và bản minh hoạ về việc xoay và nghiêng Tinybot, hãy xem [Các ví dụ về Robotics Live API](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## Bước tiếp theo

- [Hiểu video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=vi) – tìm khoảnh khắc và phân loại tiến trình.
- [Điều phối tác vụ](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=vi) – các tác vụ dài hạn không có tính năng truyền trực tuyến.
- [Tổng quan về Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=vi) – tài liệu đầy đủ về Live API.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-31 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-31 UTC."],[],[]]
