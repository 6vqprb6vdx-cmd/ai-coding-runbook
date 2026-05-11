---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ja
fetched_at: 2026-05-11T12:36:30.330287+00:00
title: "Get started with Gemini Live API using the Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Get started with Gemini Live API using the Google GenAI SDK

Gemini Live API を使用すると、Gemini モデルとのリアルタイムの双方向インタラクションが可能になります。音声、動画、テキストの入力とネイティブ音声出力をサポートしています。このガイドでは、サーバーで Google GenAI SDK を使用して API と統合する方法について説明します。

[Google AI Studio で Live API を試すmic](https://aistudio.google.com/live?hl=ja)
[GitHub からサンプルアプリを複製するcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[コーディング エージェントのスキルを使用するterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja)

## 概要

Gemini Live API は、リアルタイム通信に WebSocket を使用します。`google-genai` SDK は、これらの接続を管理するための高レベルの非同期インターフェースを提供します。

クラウド セキュリティの主な概念には、

- **セッション**: モデルへの永続的な接続。
- **Config**: モダリティ（音声/テキスト）、音声、システム指示を設定します。
- **リアルタイム入力**: 音声フレームと動画フレームを Blob として送信します。

## Live API への接続

API キーを使用して Live API セッションを開始します。

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.1-flash-live-preview"
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
const model = 'gemini-3.1-flash-live-preview';
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

## テキストを送信しています

テキストは、`send_realtime_input`（Python）または `sendRealtimeInput`（JavaScript）を使用して送信できます。

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

## 音声を送信する

音声は RAW PCM データ（RAW 16 ビット PCM 音声、16kHz、リトル エンディアン）として送信する必要があります。

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

クライアント デバイス（ブラウザなど）から音声を取得する方法の例については、[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70) のエンドツーエンドの例をご覧ください。

## 動画を送信しています

動画フレームは、特定のフレームレート（最大 1 フレーム / 秒）で個々の画像（JPEG や PNG など）として送信されます。

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

クライアント デバイス（ブラウザなど）から動画を取得する方法の例については、[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120) のエンドツーエンドの例をご覧ください。

## 音声の受信

モデルの音声レスポンスは、データのチャンクとして受信されます。

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

[サーバーで音声を受信](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98)して[ブラウザで再生](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174)する方法については、GitHub のサンプルアプリをご覧ください。

## テキストを受信しています

ユーザー入力とモデル出力の両方の文字起こしがサーバー コンテンツで利用できます。

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

## ツール呼び出しの処理

この API はツール呼び出し（関数呼び出し）をサポートしています。モデルがツール呼び出しをリクエストした場合は、関数を実行してレスポンスを返す必要があります。

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

## 次のステップ

- 音声検出やネイティブ音声機能など、主な機能と構成については、Live API の[機能](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja)ガイドをご覧ください。
- [ツールの使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=ja)ガイドを読んで、Live API をツールや関数呼び出しと統合する方法を確認します。
- 長時間にわたる会話を管理するには、[セッション管理](https://ai.google.dev/gemini-api/docs/live-session?hl=ja)ガイドをご覧ください。
- [クライアントとサーバー間の](#implementation-approach)アプリケーションで安全な認証を行うには、[エフェメラル トークン](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ja)のガイドをご覧ください。
- 基盤となる WebSockets API について詳しくは、[WebSockets API リファレンス](https://ai.google.dev/api/live?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
