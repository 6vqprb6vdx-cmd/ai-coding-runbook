---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=pl
fetched_at: 2026-06-22T06:24:21.618927+00:00
title: "Pierwsze kroki z interfejsem Gemini Live API za pomoc\u0105 protoko\u0142u WebSocket \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Pierwsze kroki z interfejsem Gemini Live API za pomocą protokołu WebSocket

Interfejs Gemini Live API umożliwia dwukierunkową interakcję w czasie rzeczywistym z modelami Gemini. Obsługuje on dane wejściowe audio, wideo i tekstowe oraz natywne wyjścia audio. Z tego przewodnika dowiesz się, jak zintegrować się bezpośrednio z interfejsem API za pomocą surowych protokołów WebSocket.

[Wypróbuj interfejs Live API w Google AI Studiomic](https://aistudio.google.com/live?hl=pl)
[Sklonuj przykładową aplikację z GitHubacode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[Użyj umiejętności agenta kodowaniaterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl)

## Przegląd

Interfejs Gemini Live API używa protokołów WebSocket do komunikacji w czasie rzeczywistym. W przeciwieństwie do korzystania z pakietu SDK to podejście polega na bezpośrednim zarządzaniu połączeniem WebSocket oraz wysyłaniu i odbieraniu wiadomości w określonym formacie JSON zdefiniowanym przez interfejs API.

Najważniejsze pojęcia:

- **Punkt końcowy WebSocket**: konkretny adres URL, z którym należy się połączyć.
- **Format wiadomości**: cała komunikacja odbywa się za pomocą wiadomości JSON zgodnych ze strukturami [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentclientmessage) i [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentservermessage).
- **Zarządzanie sesją**: odpowiadasz za utrzymywanie połączenia WebSocket.

## Uwierzytelnianie

Uwierzytelnianie odbywa się przez dodanie klucza interfejsu API jako parametru zapytania w adresie URL WebSocket.

Format punktu końcowego jest następujący:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

Zastąp `YOUR_API_KEY` swoim kluczem interfejsu API.

## Uwierzytelnianie za pomocą tokenów tymczasowych

Jeśli używasz [tokenów tymczasowych](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pl), musisz połączyć się z punktem końcowym `v1alpha`.
Token tymczasowy musi być przekazywany jako parametr zapytania `access_token`.

Format punktu końcowego dla kluczy tymczasowych jest następujący:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

Zastąp `{short-lived-token}` rzeczywistym tokenem tymczasowym.

## Łączenie się z interfejsem Live API

Aby rozpocząć sesję na żywo, nawiąż połączenie WebSocket z uwierzytelnionym punktem końcowym.
Pierwsza wiadomość wysłana przez WebSocket musi być komunikatem [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentsetup) zawierającym `config`.
Pełne opcje konfiguracji znajdziesz w dokumentacji interfejsu [Live API – WebSockets API](https://ai.google.dev/api/live?hl=pl).

### Python

```
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY"
MODEL_NAME = "gemini-3.1-flash-live-preview"
WS_URL = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={API_KEY}"

async def connect_and_configure():
    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket Connected")

        # 1. Send the initial configuration
        setup_message = {
            "setup": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(setup_message))
        print("Configuration sent")

        # Keep the session alive for further interactions
        await asyncio.sleep(3600) # Example: keep open for an hour

async def main():
    await connect_and_configure()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.1-flash-live-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  // 1. Send the initial configuration
  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
  console.log('Configuration sent');
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);
  // Handle different types of responses here
};

websocket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

websocket.onclose = () => {
  console.log('WebSocket Closed');
};
```

## Wysyłam tekst

Aby wysłać dane wejściowe w postaci tekstu, utwórz wiadomość [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentrealtimeinput) z polem `text`.

### Python

```
# Inside the websocket context
async def send_text(websocket, text):
    text_message = {
        "realtimeInput": {
            "text": text
        }
    }
    await websocket.send(json.dumps(text_message))
    print(f"Sent text: {text}")

# Example usage: await send_text(websocket, "Hello, how are you?")
```

### JavaScript

```
function sendTextMessage(text) {
  if (websocket.readyState === WebSocket.OPEN) {
    const textMessage = {
      realtimeInput: {
        text: text
      }
    };
    websocket.send(JSON.stringify(textMessage));
    console.log('Text message sent:', text);
  } else {
    console.warn('WebSocket not open.');
  }
}

// Example usage:
sendTextMessage("Hello, how are you?");
```

## Wysyłanie plików audio

Dźwięk musi być wysyłany jako surowe dane PCM (surowe 16-bitowe audio PCM, 16 kHz, little-endian). Utwórz wiadomość [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentrealtimeinput) z danymi audio. Kluczowe znaczenie ma `mimeType`.

### Python

```
# Inside the websocket context
async def send_audio_chunk(websocket, chunk_bytes):
    import base64
    encoded_data = base64.b64encode(chunk_bytes).decode('utf-8')
    audio_message = {
        "realtimeInput": {
            "audio": {
                "data": encoded_data,
                "mimeType": "audio/pcm;rate=16000"
            }
        }
    }
    await websocket.send(json.dumps(audio_message))
    # print("Sent audio chunk") # Avoid excessive logging

# Assuming 'chunk' is your raw PCM audio bytes
# await send_audio_chunk(websocket, chunk)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
    // console.log('Sent audio chunk');
  }
}
// Example usage: sendAudioChunk(audioBuffer);
```

Przykład pobierania dźwięku z urządzenia klienta (np. przeglądarki)
znajdziesz w przykładzie kompleksowym w [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## Wysyłam film

Klatki wideo są wysyłane jako pojedyncze obrazy (np. JPEG lub PNG). Podobnie jak w przypadku dźwięku użyj `realtimeInput` z `Blob`, określając prawidłowy `mimeType`.

### Python

```
# Inside the websocket context
async def send_video_frame(websocket, frame_bytes, mime_type="image/jpeg"):
    import base64
    encoded_data = base64.b64encode(frame_bytes).decode('utf-8')
    video_message = {
        "realtimeInput": {
            "video": {
                "data": encoded_data,
                "mimeType": mime_type
            }
        }
    }
    await websocket.send(json.dumps(video_message))
    # print("Sent video frame")

# Assuming 'frame' is your JPEG-encoded image bytes
# await send_video_frame(websocket, frame)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
function sendVideoFrame(frame, mimeType = 'image/jpeg') {
  if (websocket.readyState === WebSocket.OPEN) {
    const videoMessage = {
      realtimeInput: {
        video: {
          data: frame.toString('base64'),
          mimeType: mimeType
        }
      }
    };
    websocket.send(JSON.stringify(videoMessage));
    // console.log('Sent video frame');
  }
}
// Example usage: sendVideoFrame(jpegBuffer);
```

Przykład pobierania filmu z urządzenia klienta (np. przeglądarki)
znajdziesz w przykładzie kompleksowym w [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## Odbieranie odpowiedzi

WebSocket będzie odsyłać [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentservermessage) wiadomości. Musisz przeanalizować te wiadomości JSON i obsługiwać różne typy treści.

### Python

```
# Inside the websocket context, in a receive loop
async def receive_loop(websocket):
    async for message in websocket:
        response = json.loads(message)
        print("Received:", response)

        if "serverContent" in response:
            server_content = response["serverContent"]
            # Receiving Audio
            if "modelTurn" in server_content and "parts" in server_content["modelTurn"]:
                for part in server_content["modelTurn"]["parts"]:
                    if "inlineData" in part:
                        audio_data_b64 = part["inlineData"]["data"]
                        # Process or play the base64 encoded audio data
                        # audio_data = base64.b64decode(audio_data_b64)
                        print(f"Received audio data (base64 len: {len(audio_data_b64)})")

            # Receiving Text Transcriptions
            if "inputTranscription" in server_content:
                print(f"User: {server_content['inputTranscription']['text']}")
            if "outputTranscription" in server_content:
                print(f"Gemini: {server_content['outputTranscription']['text']}")

        # Handling Tool Calls
        if "toolCall" in response:
            await handle_tool_call(websocket, response["toolCall"])

# Example usage: await receive_loop(websocket)
```

### JavaScript

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);

  if (response.serverContent) {
    const serverContent = response.serverContent;
    // Receiving Audio
    if (serverContent.modelTurn?.parts) {
      for (const part of serverContent.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data; // Base64 encoded string
          // Process or play audioData
          console.log(`Received audio data (base64 len: ${audioData.length})`);
        }
      }
    }

    // Receiving Text Transcriptions
    if (serverContent.inputTranscription) {
      console.log('User:', serverContent.inputTranscription.text);
    }
    if (serverContent.outputTranscription) {
      console.log('Gemini:', serverContent.outputTranscription.text);
    }
  }

  // Handling Tool Calls
  if (response.toolCall) {
    handleToolCall(response.toolCall);
  }
};
```

Przykład obsługi odpowiedzi znajdziesz w przykładzie kompleksowym w [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## Obsługa wywołań narzędzi

Gdy model zażąda wywołania narzędzia, [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontentservermessage) będzie zawierać pole `toolCall`. Musisz wykonać funkcję lokalnie i wysłać wynik z powrotem do WebSocket za pomocą wiadomości [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=pl#bidigeneratecontenttoolresponse).

### Python

```
# Placeholder for your tool function
def my_tool_function(args):
    print(f"Executing tool with args: {args}")
    # Implement your tool logic here
    return {"status": "success", "data": "some result"}

async def handle_tool_call(websocket, tool_call):
    function_responses = []
    for fc in tool_call["functionCalls"]:
        # 1. Execute the function locally
        try:
            result = my_tool_function(fc.get("args", {}))
            response_data = {"result": result}
        except Exception as e:
            print(f"Error executing tool {fc['name']}: {e}")
            response_data = {"error": str(e)}

        # 2. Prepare the response
        function_responses.append({
            "name": fc["name"],
            "id": fc["id"],
            "response": response_data
        })

    # 3. Send the tool response back to the session
    tool_response_message = {
        "toolResponse": {
            "functionResponses": function_responses
        }
    }
    await websocket.send(json.dumps(tool_response_message))
    print("Sent tool response")

# This function is called within the receive_loop when a toolCall is detected.
```

### JavaScript

```
// Placeholder for your tool function
function myToolFunction(args) {
  console.log(`Executing tool with args:`, args);
  // Implement your tool logic here
  return { status: 'success', data: 'some result' };
}

function handleToolCall(toolCall) {
  const functionResponses = [];
  for (const fc of toolCall.functionCalls) {
    // 1. Execute the function locally
    let result;
    try {
      result = myToolFunction(fc.args || {});
    } catch (e) {
      console.error(`Error executing tool ${fc.name}:`, e);
      result = { error: e.message };
    }

    // 2. Prepare the response
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }

  // 3. Send the tool response back to the session
  if (websocket.readyState === WebSocket.OPEN) {
    const toolResponseMessage = {
      toolResponse: {
        functionResponses: functionResponses
      }
    };
    websocket.send(JSON.stringify(toolResponseMessage));
    console.log('Sent tool response');
  } else {
    console.warn('WebSocket not open to send tool response.');
  }
}
// This function is called within websocket.onmessage when a toolCall is detected.
```

## Co dalej?

- Przeczytaj pełny przewodnik po funkcjach interfejsu Live API [Capabilities](https://ai.google.dev/gemini-api/docs/live-guide?hl=pl), aby poznać najważniejsze funkcje i konfiguracje, w tym wykrywanie aktywności głosowej i natywne funkcje audio.
- Przeczytaj przewodnik dotyczący [korzystania z narzędzi](https://ai.google.dev/gemini-api/docs/live-tools?hl=pl), aby dowiedzieć się, jak zintegrować interfejs Live API z narzędziami i wywoływaniem funkcji.
- Przeczytaj przewodnik dotyczący [zarządzania sesjami](https://ai.google.dev/gemini-api/docs/live-session?hl=pl), aby dowiedzieć się, jak zarządzać długotrwałymi rozmowami.
- Przeczytaj przewodnik dotyczący [tokenów tymczasowych](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pl), aby dowiedzieć się, jak bezpiecznie uwierzytelniać się w aplikacjach typu [klient-serwer](#implementation-approach).
- Więcej informacji o bazowym interfejsie WebSockets API znajdziesz w [dokumentacji interfejsu WebSockets API](https://ai.google.dev/api/live?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-09 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-09 UTC."],[],[]]
