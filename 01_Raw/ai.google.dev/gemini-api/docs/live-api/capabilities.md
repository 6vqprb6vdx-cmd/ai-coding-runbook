---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=vi
fetched_at: 2026-09-28T06:22:54.357258+00:00
title: "H\u01b0\u1edbng d\u1eabn v\u1ec1 c\u00e1c ch\u1ee9c n\u0103ng c\u1ee7a Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hướng dẫn về các chức năng của Live API

Đây là hướng dẫn toàn diện trình bày các chức năng và cấu hình có trong Live API.
Hãy xem trang [Bắt đầu sử dụng Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi) để biết thông tin tổng quan và mã mẫu cho các trường hợp sử dụng phổ biến.

## Trước khi bắt đầu

- **Làm quen với các khái niệm cốt lõi:** Nếu bạn chưa làm việc này, trước tiên hãy đọc trang [Bắt đầu sử dụng Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi) .
  Điều này sẽ giới thiệu cho bạn các nguyên tắc cơ bản của Live API, cách hoạt động và các [phương pháp triển khai](https://ai.google.dev/gemini-api/docs/live?hl=vi#implementation-approach) khác nhau.
- **Dùng thử Live API trong AI Studio:** Bạn có thể thấy việc dùng thử Live API trong [Google AI Studio](https://aistudio.google.com/app/live?hl=vi) là hữu ích trước khi bắt đầu xây dựng. Để sử dụng Live API trong Google AI Studio, hãy chọn **Stream** (Phát trực tiếp).

## So sánh mô hình

Bảng sau đây tóm tắt những điểm khác biệt chính giữa các mô hình [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=vi), [Gemini 3.8 Live Extended Thinking](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=vi) và [Gemini 3.1 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=vi):

| Tính năng | Gemini 3.8 Live | Gemini 3.8 Live Extended Thinking | Bản xem trước Gemini 3.1 Flash Live |
| --- | --- | --- | --- |
| **Được đề xuất cho** | Lựa chọn mặc định cho hầu hết các trải nghiệm với trợ lý thoại có độ trễ thấp. | Được đề xuất khi cần có khả năng suy luận nền cao hơn. | Mô hình xem trước cũ. Bạn nên cập nhật lên [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=vi). |
| **[Tư duy](#native-audio-output-thinking)** | Được hỗ trợ (suy luận xen kẽ). `thinkingLevel` không được hỗ trợ (bỏ qua trong quá trình thiết lập). | Được hỗ trợ. Lý luận có thể định cấu hình ở chế độ nền (`thinkingLevel`: `low`, `medium`, `high`; không hỗ trợ `minimal`). | Sử dụng `thinkingLevel` để kiểm soát độ sâu tư duy bằng các chế độ cài đặt như `minimal`, `low`, `medium` và `high`. Mặc định là `minimal` để tối ưu hoá cho độ trễ thấp nhất. Xem phần [Tư duy trong Live API](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=vi). |
| **[Nhận phản hồi](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentservercontent)** | Một sự kiện máy chủ có thể chứa nhiều phần nội dung cùng lúc. | Một sự kiện máy chủ có thể chứa nhiều phần nội dung cùng lúc. Khi tính năng suy luận không đồng bộ đang hoạt động, `turnComplete: true` không cho biết phiên không hoạt động; hãy sử dụng `interaction_status` (`IN_PROGRESS` so với `IDLE`). | Một sự kiện trên máy chủ có thể chứa nhiều phần nội dung cùng lúc (ví dụ: `inlineData` và bản chép lời). Đảm bảo mã của bạn xử lý tất cả các phần trong mỗi sự kiện để tránh bỏ lỡ nội dung. |
| **[Nội dung của khách hàng](#incremental-updates)** | `send_client_content` được hỗ trợ trong toàn bộ vòng đời của phiên với các vai trò rõ ràng (`user` hoặc `model`). `turn_complete=true` sẽ ngắt quá trình tạo vô điều kiện. | `send_client_content` được hỗ trợ trong toàn bộ vòng đời của phiên với các vai trò rõ ràng (`user` hoặc `model`). `turn_complete=true` sẽ ngắt quá trình tạo vô điều kiện. | `send_client_content` được hỗ trợ trong toàn bộ vòng đời của phiên với các vai trò rõ ràng (`user` hoặc `model`). `turn_complete=true` sẽ ngắt quá trình tạo vô điều kiện. |
| **[Gọi hàm không đồng bộ](https://ai.google.dev/gemini-api/docs/live-tools?hl=vi#async-function-calling)** (`behavior: NON_BLOCKING`) | Được hỗ trợ (mặc định). Đặt `behavior: NON_BLOCKING` hoặc sử dụng chế độ chặn tương thích ngược bằng `behavior: BLOCKING`. Tính năng lập lịch hàm (`SILENT`, `WHEN_IDLE`, `INTERRUPTED`) được hỗ trợ. | Được hỗ trợ (Chỉ không đồng bộ). Chỉ hỗ trợ việc thực thi `NON_BLOCKING`. Không hỗ trợ chế độ chặn và lập lịch cho hàm. | Không được hỗ trợ. Chỉ có thể gọi hàm tuần tự. Mô hình sẽ không bắt đầu phản hồi cho đến khi bạn gửi phản hồi của công cụ. |

Để di chuyển sang Gemini 3.8 Live, hãy xem [hướng dẫn di chuyển](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=vi#migrating).
Để tìm hiểu thêm về Thinking, hãy xem [hướng dẫn về Thinking](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=vi) và [hướng dẫn nâng cấp](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=vi#upgrading).

## Thiết lập kết nối

Ví dụ sau đây minh hoạ cách tạo một kết nối bằng khoá API:

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.8-live"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## Phương thức tương tác

Các phần sau đây cung cấp ví dụ và bối cảnh hỗ trợ cho nhiều phương thức đầu vào và đầu ra có trong Live API.

### Đang gửi âm thanh

Bạn cần gửi âm thanh dưới dạng dữ liệu PCM thô (âm thanh PCM thô 16 bit, 16 kHz, little-endian).

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### Định dạng âm thanh

Dữ liệu âm thanh trong Live API luôn là PCM 16 bit, little-endian, thô. Đầu ra âm thanh luôn sử dụng tốc độ lấy mẫu là 24 kHz. Âm thanh đầu vào vốn là 16 kHz, nhưng Live API sẽ lấy lại mẫu nếu cần, vì vậy, bạn có thể gửi bất kỳ tốc độ lấy mẫu nào. Để truyền tốc độ lấy mẫu của âm thanh đầu vào, hãy đặt loại MIME của mỗi [Blob](https://ai.google.dev/api/caching?hl=vi#Blob) chứa âm thanh thành một giá trị như `audio/pcm;rate=16000`.

### Nhận âm thanh

Các câu trả lời bằng âm thanh của mô hình được nhận dưới dạng các khối dữ liệu.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### Đang gửi tin nhắn

Bạn có thể gửi văn bản bằng `send_realtime_input` (Python) hoặc `sendRealtimeInput` (JavaScript).

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### Đang gửi video

Khung hình video được gửi dưới dạng hình ảnh riêng lẻ (ví dụ: JPEG hoặc PNG) ở một tốc độ khung hình cụ thể (tối đa 1 khung hình/giây).

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### Bản cập nhật nội dung bổ sung

Sử dụng các bản cập nhật gia tăng để gửi dữ liệu đầu vào văn bản, thiết lập bối cảnh phiên hoặc khôi phục bối cảnh phiên. Đối với các ngữ cảnh ngắn, bạn có thể gửi các lượt tương tác từng bước để biểu thị chính xác trình tự của các sự kiện:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

Đối với các ngữ cảnh dài hơn, bạn nên cung cấp một bản tóm tắt thông báo duy nhất để giải phóng cửa sổ ngữ cảnh cho các hoạt động tương tác tiếp theo. Hãy xem phần [Tiếp tục phiên](https://ai.google.dev/gemini-api/docs/live-session?hl=vi#session-resumption) để biết một phương thức khác để tải ngữ cảnh phiên.

### Bản chép lời

Ngoài câu trả lời của mô hình, bạn cũng có thể nhận được bản chép lời của cả đầu ra âm thanh và đầu vào âm thanh.

Để bật tính năng chép lời cho đầu ra âm thanh của mô hình, hãy gửi `output_audio_transcription` trong cấu hình thiết lập. Ngôn ngữ chép lời được suy luận từ câu trả lời của mô hình.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Để bật tính năng chép lời cho đầu vào âm thanh của mô hình, hãy gửi `input_audio_transcription` trong cấu hình thiết lập.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### Thay đổi giọng nói và ngôn ngữ

Các mô hình [đầu ra âm thanh gốc](#native-audio-output) hỗ trợ mọi giọng nói có sẵn cho các mô hình [Chuyển văn bản sang lời nói (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#voices) của chúng tôi. Bạn có thể nghe tất cả các giọng nói trong [AI Studio](https://aistudio.google.com/app/live?hl=vi).

Để chỉ định một giọng nói, hãy đặt tên giọng nói trong đối tượng `speechConfig` trong cấu hình phiên:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Live API hỗ trợ [nhiều ngôn ngữ](#supported-languages).
Các mô hình [đầu ra âm thanh gốc](#native-audio-output) sẽ tự động chọn ngôn ngữ phù hợp và không hỗ trợ việc đặt mã ngôn ngữ một cách rõ ràng.

## Khả năng âm thanh gốc

Các mô hình mới nhất của chúng tôi có [đầu ra âm thanh gốc](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=vi), mang đến lời nói tự nhiên, chân thực và hiệu suất đa ngôn ngữ được cải thiện.

### Tư duy

Các mô hình Gemini 3.8 Live Extended Thinking và Gemini 3.1 sử dụng `thinkingLevel` để kiểm soát độ sâu tư duy. Đối với `gemini-3.8-live`, `thinkingLevel` không được hỗ trợ và bạn phải bỏ qua trong quá trình thiết lập. Gemini 3.8 Live Extended Thinking hỗ trợ `low`, `medium` và `high` (không được hỗ trợ `minimal`). Các mô hình Gemini 3.1 hỗ trợ `minimal`, `low`, `medium` và `high`. Để biết thêm thông tin, hãy xem bài viết [Tư duy trong Live API](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=vi).

### Python

```
model = "gemini-3.8-live-extended-thinking"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.8-live-extended-thinking';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

Ngoài ra, bạn có thể bật tính năng tóm tắt suy nghĩ bằng cách đặt `includeThoughts` thành `true` trong cấu hình. Xem [bản tóm tắt ý tưởng](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#summaries) để biết thêm thông tin:

### Python

```
model = "gemini-3.8-live-extended-thinking"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.8-live-extended-thinking';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### Đối thoại cảm xúc

Tính năng này cho phép Gemini điều chỉnh phong cách phản hồi theo biểu thức và giọng điệu đầu vào.

Để sử dụng đối thoại cảm xúc, hãy đặt phiên bản API thành `v1beta` và đặt `enable_affective_dialog` thành `true` trong thông báo thiết lập:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### Âm thanh chủ động

Khi tính năng này được bật, Gemini có thể chủ động quyết định không phản hồi nếu nội dung không liên quan.

Để sử dụng, hãy đặt phiên bản API thành `v1beta` và định cấu hình trường `proactivity` trong thông báo thiết lập, đồng thời đặt `proactive_audio` thành `true`:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## Dịch trực tiếp

Live API hỗ trợ dịch các cuộc trò chuyện bằng lời nói theo thời gian thực với độ trễ thấp. Tính năng này cho phép bạn tạo các ứng dụng dịch giọng nói theo thời gian thực.

Để biết thêm thông tin và ví dụ, hãy xem [hướng dẫn về tính năng Dịch trực tiếp](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=vi).

## Phát hiện hoạt động giọng nói (VAD)

Tính năng Phát hiện hoạt động giọng nói (VAD) cho phép mô hình nhận biết thời điểm một người đang nói. Đây là yếu tố cần thiết để tạo ra các cuộc trò chuyện tự nhiên, vì nó cho phép người dùng ngắt lời mô hình bất cứ lúc nào.

Khi VAD phát hiện thấy một đoạn ngắt, quá trình tạo đang diễn ra sẽ bị huỷ và loại bỏ. Chỉ những thông tin đã được gửi đến máy khách mới được giữ lại trong nhật ký phiên. Sau đó, máy chủ sẽ gửi một thông báo [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=vi#bidigeneratecontentservercontent) để báo cáo sự gián đoạn.

Sau đó, máy chủ Gemini sẽ loại bỏ mọi lệnh gọi hàm đang chờ xử lý và gửi thông báo `BidiGenerateContentServerContent` kèm theo mã nhận dạng của các lệnh gọi đã huỷ.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### VAD tự động

Theo mặc định, mô hình sẽ tự động thực hiện VAD trên luồng đầu vào âm thanh liên tục. Bạn có thể định cấu hình VAD bằng trường [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=vi#RealtimeInputConfig.AutomaticActivityDetection) của [cấu hình thiết lập](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentSetup).

Khi luồng âm thanh bị tạm dừng hơn một giây (ví dụ: vì người dùng tắt micrô), bạn nên gửi sự kiện [`audioStreamEnd`](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) để xoá mọi âm thanh được lưu vào bộ nhớ đệm. Ứng dụng có thể tiếp tục gửi dữ liệu âm thanh bất cứ lúc nào.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Với `send_realtime_input`, API sẽ tự động phản hồi âm thanh dựa trên VAD. Mặc dù `send_client_content` thêm các thông báo vào ngữ cảnh mô hình theo thứ tự, nhưng `send_realtime_input` được tối ưu hoá để có khả năng phản hồi nhanh chóng, nhưng lại không đảm bảo được thứ tự xác định.

### Cấu hình VAD tự động

Để kiểm soát hoạt động VAD tốt hơn, bạn có thể định cấu hình các thông số sau. Hãy xem [Tài liệu tham khảo API](https://ai.google.dev/api/live?hl=vi#automaticactivitydetection) để biết thêm thông tin.

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### VAD kết hợp

VAD kết hợp mang lại lợi ích của VAD tự động (phát hiện chính xác thời điểm bắt đầu lời nói) và VAD thủ công (hoàn tất phản hồi có độ trễ thấp).

Trong cấu hình này:

1. **Tính năng VAD tự động vẫn được bật** trên máy chủ. Máy chủ sẽ tự động phát hiện thời điểm bắt đầu lời nói của người dùng, sử dụng khoảng đệm tiền tố để tránh cắt bớt phần đầu của câu nói.
2. Ứng dụng sử dụng **VAD phía máy khách** để phát hiện thời điểm người dùng ngừng nói.
3. Khi VAD phía máy khách phát hiện thấy đoạn cuối của lời nói, VAD sẽ gửi tín hiệu [`audio_stream_end`](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) đến máy chủ.
4. Máy chủ coi tín hiệu `audio_stream_end` là một lời nhắc hoàn tất ngay lập tức, bỏ qua độ trễ phát hiện im lặng mặc định phía máy chủ và trả về bản chép lời cũng như phản hồi của mô hình với độ trễ tối thiểu.
5. Nếu VAD phía máy khách không kích hoạt được, thì VAD phía máy chủ sẽ đóng vai trò là một cơ chế dự phòng để phát hiện điểm kết thúc của lời nói.

Xin lưu ý rằng nếu bạn đặt ngưỡng VAD phía máy khách quá cao, điều này có thể khiến lời nói bị cắt. Tuy nhiên, phương pháp này giúp ngăn chặn các vấn đề về việc cắt bớt phần đầu có thể xảy ra với VAD thủ công.

### Python

```
# Set up with automatic VAD enabled (default)
config = {
    "response_modalities": ["AUDIO"],
}

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio data normally
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects the end of speech, send:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Set up with automatic VAD enabled (default)
const config = {
  responseModalities: [Modality.AUDIO],
};

// Send audio data normally
session.sendRealtimeInput({
  audio: {
    data: base64Audio,
    mimeType: "audio/pcm;rate=16000"
  }
});

// When client-side VAD detects the end of speech, send:
session.sendRealtimeInput({ audioStreamEnd: true });
```

### Tắt tính năng tự động phát hiện hoạt động thoại

Ngoài ra, bạn có thể tắt tính năng VAD tự động bằng cách đặt `realtimeInputConfig.automaticActivityDetection.disabled` thành `true` trong thông báo thiết lập. Trong cấu hình này, ứng dụng chịu trách nhiệm phát hiện lời nói của người dùng và gửi thông báo [`activityStart`](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) và [`activityEnd`](https://ai.google.dev/api/live?hl=vi#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) vào thời điểm thích hợp. `audioStreamEnd` không được gửi trong cấu hình này. Thay vào đó, mọi sự gián đoạn luồng đều được đánh dấu bằng thông báo `activityEnd`.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### Tìm hiểu các thông số VAD và tác động của chúng đến chất lượng

Khi sử dụng VAD tự động, 2 thông số chính sẽ kiểm soát cách phân đoạn âm thanh thành các lượt lời nói trước khi được gửi đến mô hình:

- **`prefixPaddingMs`**: Lượng âm thanh cần đưa vào *trước* khi phát hiện thấy lời nói. Tính năng "xem lại" này đảm bảo mô hình ghi lại toàn bộ thời điểm bắt đầu của lời nói, bao gồm cả âm tiết đầu tiên có thể bắt đầu trước khi VAD kích hoạt. Giá trị `0` có thể khiến phần đầu của các từ bị cắt.
- **`silenceDurationMs`**: Khoảng thời gian máy chủ chờ trong khi không có âm thanh trước khi kết thúc một lượt lời nói. Thông số này xác định mức độ chấp nhận của hệ thống đối với các khoảng dừng tự nhiên giữa câu (ví dụ: suy nghĩ, hít thở hoặc ranh giới mệnh đề).

#### Ảnh hưởng của `silenceDurationMs` đến chất lượng âm thanh

Giá trị `silenceDurationMs` ảnh hưởng trực tiếp đến kích thước và tính hoàn chỉnh của các đoạn âm thanh mà mô hình nhận được để xử lý:

- **Nên dùng (500 mili giây – 800 mili giây):** Cung cấp sự cân bằng hợp lý – mô hình nhận được các đoạn âm thanh hoàn chỉnh, giàu ngữ cảnh trong khi vẫn duy trì độ trễ hợp lý. Giá trị mặc định nội bộ của máy chủ là khoảng 800 mili giây.
- **Quá thấp (ví dụ: 100 mili giây – 200 mili giây):** Hệ thống kết thúc lượt lời nói trong khi tạm dừng tự nhiên, chia một câu nói thành nhiều đoạn âm thanh nhỏ. Mô hình này nhận từng đoạn riêng lẻ, mất ngữ cảnh giữa các đoạn và dẫn đến chất lượng bản chép lời và phản hồi thấp hơn.
- **Quá cao (ví dụ: 2000 mili giây trở lên):** Hệ thống đợi một thời gian dài sau khi người dùng ngừng nói, làm tăng độ trễ cảm nhận trước khi mô hình phản hồi.

#### Các phương pháp hay nhất cho VAD thủ công (phía máy khách)

Khi bạn tắt tính năng VAD tự động và quản lý các tín hiệu `activityStart`/`activityEnd` từ tính năng phát hiện giọng nói phía máy khách của riêng bạn, hãy lưu ý rằng các cơ chế đệm âm thanh tích hợp của máy chủ sẽ bị bỏ qua. Điều này có nghĩa là:

1. **Không có bộ nhớ đệm trước lời nói:** Máy chủ không còn thêm âm thanh vào trước khi bắt đầu lời nói được phát hiện. Ứng dụng của bạn phải có đủ ngữ cảnh âm thanh trước khi gửi `activityStart`.
2. **Không có khoảng thời gian chờ:** Máy chủ sẽ hành động ngay lập tức dựa trên tín hiệu `activityEnd` mà không cần chờ thêm. Nếu VAD phía máy khách của bạn sử dụng ngưỡng kết thúc lời nói quá cao (ví dụ: 200 mili giây im lặng), thì lời nói có thể bị cắt giữa câu trong các khoảng dừng tự nhiên.

Để duy trì chất lượng âm thanh bằng VAD thủ công, hãy sử dụng ngưỡng im lặng cuối lời nói ít nhất là **500 mili giây** trong trình phát hiện hoạt động thoại của ứng dụng.
Các ngưỡng dưới giá trị này thường gây ra âm thanh rời rạc, làm giảm chất lượng bản chép lời và phản hồi của mô hình.

## Số token

Bạn có thể tìm thấy tổng số mã thông báo đã sử dụng trong trường [usageMetadata](https://ai.google.dev/api/live?hl=vi#usagemetadata) của thông báo máy chủ được trả về.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## Độ phân giải của nội dung nghe nhìn

Bạn có thể chỉ định độ phân giải của nội dung nghe nhìn đầu vào bằng cách đặt trường `mediaResolution` trong cấu hình phiên:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

Bạn có thể định cấu hình `mediaResolution` cho các phiên đa phương thức bao gồm đầu vào là âm thanh, video hoặc hình ảnh. Mặc dù `mediaResolution` điều chỉnh việc phân bổ mã thông báo cho mỗi khung hình đối với dữ liệu đầu vào trực quan, nhưng các luồng âm thanh được mã hoá ở tốc độ cố định mỗi giây trên tất cả các chế độ cài đặt độ phân giải. Để biết thêm thông tin, hãy xem hướng dẫn về [Độ phân giải của nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi).

## Các điểm hạn chế

Hãy cân nhắc những hạn chế sau của Live API khi bạn lên kế hoạch cho dự án của mình.

### Phương thức phản hồi

Các mô hình âm thanh gốc chỉ hỗ trợ phương thức phản hồi `AUDIO. Nếu bạn cần phản hồi của mô hình dưới dạng văn bản, hãy sử dụng tính năng [bản chép lời âm thanh đầu ra](#audio-transcription).

### Xác thực ứng dụng

Theo mặc định, Live API chỉ cung cấp tính năng xác thực từ máy chủ đến máy chủ. Nếu đang triển khai ứng dụng Live API bằng [phương pháp từ máy khách đến máy chủ](https://ai.google.dev/gemini-api/docs/live?hl=vi#implementation-approach), bạn cần sử dụng [mã thông báo tạm thời](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=vi) để giảm thiểu rủi ro bảo mật.

### Thời lượng phiên

Các phiên chỉ có âm thanh bị giới hạn ở 15 phút và các phiên có cả âm thanh và video bị giới hạn ở 2 phút.
Tuy nhiên, bạn có thể định cấu hình [các kỹ thuật quản lý phiên](https://ai.google.dev/gemini-api/docs/live-session?hl=vi) khác nhau cho số lượng tiện ích không giới hạn trong thời lượng phiên.

### Cửa sổ ngữ cảnh

Một phiên có giới hạn cửa sổ ngữ cảnh là:

- 128.000 token cho các mô hình [đầu ra âm thanh gốc](#native-audio-output)
- 32 nghìn token cho các mô hình Live API khác

## Ngôn ngữ được hỗ trợ

Live API hỗ trợ 99 ngôn ngữ sau.

| Ngôn ngữ | Mã BCP-47 | Ngôn ngữ | Mã BCP-47 |
| --- | --- | --- | --- |
| Tiếng Hà Lan ở Nam Phi | `af` | Tiếng Latvia | `lv` |
| Tiếng Akan | `ak` | Tiếng Lithuania | `lt` |
| Tiếng Albania | `sq` | Tiếng Macedonia | `mk` |
| Tiếng Amhara | `am` | Tiếng Malay | `ms` |
| Tiếng Ả Rập | `ar` | Tiếng Malayalam | `ml` |
| Tiếng Armenia | `hy` | Tiếng Malta | `mt` |
| Tiếng Assam | `as` | Tiếng Maori | `mi` |
| Tiếng Azerbaijan | `az` | Tiếng Marathi | `mr` |
| Tiếng Basque | `eu` | Tiếng Mông Cổ | `mn` |
| Tiếng Belarus | `be` | Tiếng Nepal | `ne` |
| Tiếng Bengal | `bn` | Tiếng Na Uy | `no`, `nb` |
| Tiếng Bosnia | `bs` | Tiếng Odia | `or` |
| Tiếng Bungary | `bg` | Tiếng Oromo | `om` |
| Tiếng Miến Điện | `my` | Tiếng Pashto | `ps` |
| Tiếng Catalan | `ca` | Persian | `fa` |
| Tiếng Cebuano | `ceb` | Tiếng Ba Lan | `pl` |
| Tiếng Trung (Giản thể) | `zh-Hans` | Tiếng Bồ Đào Nha (Brazil) | `pt-BR` |
| Tiếng Trung (Phồn thể) | `zh-Hant` | Tiếng Bồ Đào Nha (Bồ Đào Nha) | `pt-PT` |
| Tiếng Croatia | `hr` | Tiếng Punjab | `pa` |
| Tiếng Séc | `cs` | Tiếng Quechua | `qu` |
| Tiếng Đan Mạch | `da` | Tiếng Rumani | `ro` |
| Tiếng Hà Lan | `nl` | Tiếng Romansh | `rm` |
| Tiếng Anh | `en` | Tiếng Nga | `ru` |
| Tiếng Estonia | `et` | Tiếng Serbia | `sr` |
| Tiếng Faroe | `fo` | Tiếng Sindh | `sd` |
| Tiếng Philippines | `fil` | Tiếng Sinhala | `si` |
| Tiếng Phần Lan | `fi` | Tiếng Slovak | `sk` |
| Tiếng Pháp | `fr` | Tiếng Slovenia | `sl` |
| Tiếng Galicia | `gl` | Tiếng Somali | `so` |
| Tiếng Gruzia | `ka` | Tiếng Nam Sotho | `st` |
| Tiếng Đức | `de` | Tiếng Tây Ban Nha | `es` |
| Tiếng Hy Lạp | `el` | Tiếng Swahili | `sw` |
| Tiếng Gujarat | `gu` | Tiếng Thuỵ Điển | `sv` |
| Tiếng Hausa | `ha` | Tiếng Tajik | `tg` |
| Tiếng Do Thái | `he` | Tiếng Tamil | `ta` |
| Tiếng Hindi | `hi` | Tiếng Telugu | `te` |
| Tiếng Hungary | `hu` | Tiếng Thái | `th` |
| Tiếng Iceland | `is` | Tiếng Tswana | `tn` |
| Tiếng Indonesia | `id` | Tiếng Thổ Nhĩ Kỳ | `tr` |
| Tiếng Ireland | `ga` | Tiếng Turkmen | `tk` |
| Tiếng Ý | `it` | Tiếng Ukraina | `uk` |
| Tiếng Nhật | `ja` | Tiếng Urdu | `ur` |
| Tiếng Kannada | `kn` | Tiếng Uzbek | `uz` |
| Tiếng Kazakh | `kk` | Tiếng Việt | `vi` |
| Tiếng Khmer | `km` | Tiếng Wales | `cy` |
| Tiếng Kinyarwanda | `rw` | Tiếng Tây Frisia | `fy` |
| Tiếng Hàn | `ko` | Tiếng Wolof | `wo` |
| Tiếng Kurd | `ku` | Tiếng Yoruba | `yo` |
| Tiếng Kyrgyz | `ky` | Tiếng Zulu | `zu` |
| Tiếng Lào | `lo` |  |  |

## Bước tiếp theo

- Đọc hướng dẫn về [Cách sử dụng công cụ](https://ai.google.dev/gemini-api/docs/live-tools?hl=vi) và [Quản lý phiên](https://ai.google.dev/gemini-api/docs/live-session?hl=vi) để biết thông tin cần thiết về cách sử dụng Live API một cách hiệu quả.
- Dùng thử Live API trong [Google AI Studio](https://aistudio.google.com/app/live?hl=vi).
- Để biết thêm thông tin về các mô hình Live API, hãy xem các trang mô hình [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=vi) và [Gemini 3.8 Live Extended Thinking](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=vi).
- Hãy thử xem thêm các ví dụ trong [sổ tay Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=vi), [sổ tay Live API Tools](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=vi) và [tập lệnh Live API Get Started](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-19 UTC."],[],[]]
