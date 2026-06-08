---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=de
fetched_at: 2026-06-08T14:56:33.638732+00:00
title: "Erste Schritte mit der Gemini Live API \u00fcber WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Erste Schritte mit der Gemini Live API über WebSockets

Die Gemini Live API ermöglicht die bidirektionale Interaktion mit Gemini-Modellen in Echtzeit und unterstützt Audio-, Video- und Texteingaben sowie native Audioausgaben. In diesem Leitfaden wird beschrieben, wie Sie die API direkt mit Raw WebSockets einbinden.

[Live API in Google AI Studio ausprobierenmic](https://aistudio.google.com/live?hl=de)
[Beispiel-App von GitHub klonencode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[Coding-Agent-Skills verwendenterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=de)

## Übersicht

Die Gemini Live API verwendet WebSockets für die Echtzeitkommunikation. Im Gegensatz zur Verwendung eines SDKs müssen Sie bei diesem Ansatz die WebSocket-Verbindung direkt verwalten und Nachrichten in einem bestimmten JSON-Format senden/empfangen, das von der API definiert wird.

Wichtige Konzepte:

- **WebSocket-Endpunkt**: Die spezifische URL, mit der eine Verbindung hergestellt werden soll.
- **Nachrichtenformat**: Die gesamte Kommunikation erfolgt über JSON-Nachrichten, die den Strukturen [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=de#bidigeneratecontentclientmessage) und [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=de#bidigeneratecontentservermessage) entsprechen.
- **Sitzungsverwaltung**: Sie sind für die Aufrechterhaltung der WebSocket-Verbindung verantwortlich.

## Authentifizierung

Die Authentifizierung erfolgt durch Einfügen Ihres API-Schlüssels als Suchparameter in die WebSocket-URL.

Das Endpunktformat ist:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

Ersetzen Sie `YOUR_API_KEY` durch Ihren tatsächlichen API-Schlüssel.

## Authentifizierung mit temporären Tokens

Wenn Sie [flüchtige Tokens](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=de) verwenden, müssen Sie eine Verbindung zum `v1alpha`-Endpunkt herstellen.
Das temporäre Token muss als `access_token`-Abfrageparameter übergeben werden.

Das Endpunktformat für sitzungsspezifische Schlüssel lautet:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

Ersetzen Sie `{short-lived-token}` durch das tatsächliche temporäre Token.

## Verbindung zur Live API herstellen

Um eine Live-Sitzung zu starten, stellen Sie eine WebSocket-Verbindung zum authentifizierten Endpunkt her.
Die erste Nachricht, die über den WebSocket gesendet wird, muss ein [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=de#bidigeneratecontentsetup) mit dem `config` sein.
Die vollständigen Konfigurationsoptionen finden Sie in der [Live API – WebSockets API-Referenz](https://ai.google.dev/api/live?hl=de).

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
        config_message = {
            "config": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(config_message))
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
  const configMessage = {
    config: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(configMessage));
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

## SMS wird gesendet

Wenn Sie Texteingaben senden möchten, erstellen Sie eine [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=de#bidigeneratecontentrealtimeinput)-Nachricht mit dem Feld `text`.

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

## Audio senden

Audio muss als rohe PCM-Daten gesendet werden (rohes 16‑Bit-PCM-Audio, 16 kHz, Little Endian). Erstellen Sie eine [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=de#bidigeneratecontentrealtimeinput)-Nachricht mit den Audiodaten. Die `mimeType` ist entscheidend.

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

Ein Beispiel dafür, wie Sie die Audioausgabe vom Clientgerät (z.B. dem Browser) abrufen, finden Sie im End-to-End-Beispiel auf [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## Video wird gesendet

Videoframes werden als einzelne Bilder (z.B. JPEG oder PNG) gesendet. Verwenden Sie `realtimeInput` mit einem `Blob` und geben Sie das richtige `mimeType` an.

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

Ein Beispiel dafür, wie Sie das Video vom Clientgerät (z.B. dem Browser) abrufen, finden Sie im End-to-End-Beispiel auf [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## Antworten erhalten

Der WebSocket sendet [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=de#bidigeneratecontentservermessage)-Nachrichten zurück. Sie müssen diese JSON-Nachrichten parsen und verschiedene Arten von Inhalten verarbeiten.

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

Ein Beispiel für die Verarbeitung der Antwort finden Sie im End-to-End-Beispiel auf [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## Toolaufrufe verarbeiten

Wenn das Modell einen Tool-Aufruf anfordert, enthält [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=de#bidigeneratecontentservermessage) das Feld `toolCall`. Sie müssen die Funktion lokal ausführen und das Ergebnis mit einer [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=de#bidigeneratecontenttoolresponse)-Nachricht an den WebSocket zurücksenden.

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

## Nächste Schritte

- Im vollständigen Leitfaden zu den [Funktionen der Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=de) findest du wichtige Funktionen und Konfigurationen, darunter die Spracherkennung und native Audiofunktionen.
- Im [Leitfaden zur Tool-Nutzung](https://ai.google.dev/gemini-api/docs/live-tools?hl=de) erfahren Sie, wie Sie die Live API in Tools und Funktionsaufrufe einbinden.
- Im Leitfaden [Sitzungsverwaltung](https://ai.google.dev/gemini-api/docs/live-session?hl=de) finden Sie Informationen zum Verwalten von Unterhaltungen mit langer Ausführungszeit.
- Lesen Sie den Leitfaden zu [Einmal-Tokens](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=de) für die sichere Authentifizierung in [Client-zu-Server](#implementation-approach)-Anwendungen.
- Weitere Informationen zur zugrunde liegenden WebSockets API finden Sie in der [WebSockets API-Referenz](https://ai.google.dev/api/live?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-01 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-01 (UTC)."],[],[]]
