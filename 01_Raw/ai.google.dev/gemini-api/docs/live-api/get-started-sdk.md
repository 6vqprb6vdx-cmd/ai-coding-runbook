---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=fr
fetched_at: 2026-08-17T02:22:35.967857+00:00
title: "Premiers pas avec l'API Gemini\u00a0Live \u00e0 l'aide du SDK Google GenAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Premiers pas avec l'API Gemini Live à l'aide du SDK Google GenAI

L'API Gemini Live permet une interaction bidirectionnelle en temps réel avec les modèles Gemini, et accepte les entrées audio, vidéo et texte, ainsi que les sorties audio natives. Ce guide explique comment intégrer l'API à l'aide du SDK Google GenAI sur votre serveur.

[Essayer l'API Live dans Google AI Studiomic](https://aistudio.google.com/live?hl=fr)
[Clonez l'exemple d'application depuis GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Utiliser les compétences de l'agent de codageterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr)

## Présentation

L'API Gemini Live utilise WebSockets pour la communication en temps réel. Le SDK `google-genai` fournit une interface asynchrone de haut niveau pour gérer ces connexions.

Concepts clés :

- **Session** : connexion persistante au modèle.
- **Configuration** : configuration des modalités (audio/texte), de la voix et des instructions système.
- **Entrée en temps réel** : envoi de frames audio et vidéo sous forme de blobs.

## Se connecter à l'API Live

Démarrez une session de l'API Live avec une clé API :

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

## Envoi d'un SMS…

Le texte peut être envoyé à l'aide de `send_realtime_input` (Python) ou `sendRealtimeInput` (JavaScript).

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

## Envoi de l'audio

L'audio doit être envoyé sous forme de données PCM brutes (audio PCM 16 bits brut, 16 kHz, little-endian).

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

Pour obtenir un exemple de récupération de l'audio à partir de l'appareil client (par exemple, le navigateur)
consultez l'exemple de bout en bout sur [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## Envoi de la vidéo…

Les frames vidéo sont envoyées sous forme d'images individuelles (par exemple, JPEG ou PNG) à une fréquence d'images spécifique (1 frame par seconde maximum).

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

Pour obtenir un exemple de récupération de la vidéo à partir de l'appareil client (par exemple, le navigateur)
consultez l'exemple de bout en bout sur [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## Réception de l'audio

Les réponses audio du modèle sont reçues sous forme de blocs de données.

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

Consultez l'exemple d'application sur GitHub pour découvrir comment [recevoir l'audio sur votre serveur](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) et [le lire dans le navigateur](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## Réception d'un SMS…

Les transcriptions des entrées utilisateur et des sorties du modèle sont disponibles dans le contenu du serveur.

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

## Gérer les appels d'outils

L'API est compatible avec les appels d'outils (appels de fonction). Lorsque le modèle demande un appel d'outil, vous devez exécuter la fonction et renvoyer la réponse.

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

## Étape suivante

- Consultez le guide complet des fonctionnalités de l'API Live [Fonctionnalités](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr) pour découvrir les principales fonctionnalités et configurations, y compris la détection d'activité vocale et les fonctionnalités audio natives.
- Consultez le [guide d'utilisation des outils](https://ai.google.dev/gemini-api/docs/live-tools?hl=fr) pour découvrir comment intégrer l'API Live aux outils et aux appels de fonction.
- Consultez le [guide de gestion des sessions](https://ai.google.dev/gemini-api/docs/live-session?hl=fr) pour gérer les conversations de longue durée.
- Consultez le guide sur les [jetons éphémères](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=fr) pour une authentification sécurisée dans les applications [client-serveur](https://ai.google.dev/gemini-api/docs/live-api?hl=fr#implementation-approach).
- Pour en savoir plus sur l'API WebSockets sous-jacente, consultez la [documentation de référence de l'API WebSockets](https://ai.google.dev/api/live?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/08 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/08 (UTC)."],[],[]]
