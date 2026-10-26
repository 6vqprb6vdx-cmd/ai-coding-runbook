---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=id
fetched_at: 2026-10-26T05:55:55.387536+00:00
title: "Mulai menggunakan Gemini Live API menggunakan Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Mulai menggunakan Gemini Live API menggunakan Google GenAI SDK

Gemini Live API memungkinkan interaksi dua arah real-time dengan model Gemini, yang mendukung input audio, video, dan teks serta output audio native. Panduan ini menjelaskan cara berintegrasi dengan API menggunakan Google GenAI SDK di server Anda.

[Coba Live API di Google AI Studiomic](https://aistudio.google.com/live?hl=id)
[Clone aplikasi contoh dari GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Gunakan keterampilan agen pengodeanterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=id)

## Ringkasan

Gemini Live API menggunakan WebSocket untuk komunikasi real-time. `google-genai` SDK menyediakan antarmuka asinkron tingkat tinggi untuk mengelola koneksi ini.

Konsep utama:

- **Sesi**: Koneksi persisten ke model.
- **Konfigurasi**: Menyiapkan modalitas (audio/teks), suara, dan petunjuk sistem.
- **Input Real-time**: Mengirim frame audio dan video sebagai blob.

## Menghubungkan ke Live API

Mulai sesi Live API dengan kunci API:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

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

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
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

## Mengirim SMS

Teks dapat dikirim menggunakan `send_realtime_input` (Python) atau `sendRealtimeInput` (JavaScript).

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

## Mengirim audio

Audio harus dikirim sebagai data PCM mentah (audio PCM 16-bit mentah, 16 kHz, little-endian).

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

Untuk contoh cara mendapatkan audio dari perangkat klien (misalnya, browser)
lihat contoh lengkap di [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## Mengirim video

Frame video dikirim sebagai gambar individual (misalnya, JPEG atau PNG) pada kecepatan frame tertentu (maks. 1 frame per detik).

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

Untuk contoh cara mendapatkan video dari perangkat klien (misalnya, browser)
lihat contoh lengkap di [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## Menerima audio

Respons audio model diterima sebagai potongan data.

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

Lihat aplikasi contoh di GitHub untuk mempelajari cara [menerima audio di server Anda](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) dan [memutarnya di browser](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## Menerima SMS

Transkripsi untuk input pengguna dan output model tersedia dalam konten server.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## Menangani panggilan alat

API ini mendukung panggilan alat (panggilan fungsi). Saat model meminta panggilan alat, Anda harus menjalankan fungsi dan mengirim respons kembali.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## Langkah berikutnya

- Baca panduan [Kemampuan](https://ai.google.dev/gemini-api/docs/live-guide?hl=id) Live API lengkap untuk mengetahui kemampuan dan konfigurasi utama, termasuk Deteksi Aktivitas Suara dan fitur audio native.
- Baca panduan [Penggunaan alat](https://ai.google.dev/gemini-api/docs/live-tools?hl=id) untuk mempelajari cara mengintegrasikan Live API dengan alat dan panggilan fungsi.
- Baca panduan [Pengelolaan sesi](https://ai.google.dev/gemini-api/docs/live-session?hl=id) untuk mengelola percakapan yang berjalan lama.
- Baca panduan [Token sementara](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=id) untuk autentikasi yang aman di aplikasi [klien ke server](https://ai.google.dev/gemini-api/docs/live-api?hl=id#implementation-approach).
- Untuk mengetahui informasi selengkapnya tentang WebSockets API yang mendasarinya, lihat [Referensi WebSockets API](https://ai.google.dev/api/live?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-17 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-17 UTC."],[],[]]
