---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=pl
fetched_at: 2026-07-06T05:13:24.717304+00:00
title: "T\u0142umaczenie na \u017cywo za pomoc\u0105 interfejsu Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Tłumaczenie na żywo za pomocą interfejsu Gemini Live API

Interfejs Gemini Live API obsługuje tłumaczenie mowy na mowę w czasie rzeczywistym z krótkim czasem oczekiwania w ponad 70 językach za pomocą modelu [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=pl). Konfigurując interfejs Live API z ustawieniami tłumaczenia, możesz przesyłać strumieniowo dźwięk w jednym języku i otrzymywać przetłumaczony dźwięk w innym języku, co umożliwia płynne tłumaczenie głosu na głos w czasie rzeczywistym.

[Wypróbuj tłumaczenie na żywo w Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=pl)
[Sklonuj przykładową aplikację z GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Korzystaj z umiejętności agenta do kodowaniaterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl#gemini-live-api-dev)

## Czat na żywo z pracownikiem obsługi klienta a tłumaczenie na żywo

Obie funkcje korzystają z interfejsu Live API, ale model mentalny tłumaczenia na żywo różni się od interakcji z agentem w czasie rzeczywistym.

| Czat z pracownikiem | Tłumaczenie na żywo |
| --- | --- |
| **Model działa jako asystent** – słucha, analizuje i podejmuje działania w Twoim imieniu. | **Model działa jak tłumacz.** Działa jak potok tłumaczenia w czasie rzeczywistym. |
| **Wykorzystuje interakcje oparte na turach.** Opiera się na przerwach, wykrywaniu intencji i obsłudze przerw. | **Wykorzystuje ciągłe przetwarzanie strumieniowe** – tłumaczy wypowiedzi mówcy na bieżąco, bez czekania na swoją kolej. |
| **Obsługuje narzędzia i agenty.** Natywna obsługa wywoływania funkcji, wyszukiwarki Google i instrukcji. | **Obsługuje tylko tłumaczenie.** Tłumaczenie z niskim opóźnieniem bez obsługi narzędzi ani instrukcji. |
| **W pełni multimodalny** – obsługuje dane wejściowe w postaci tekstu, dźwięku, wideo i obrazów. | **Dźwięk ograniczony.** Dane wejściowe są ograniczone do dźwięku, aby zapewnić ścisłe progi opóźnienia w czasie rzeczywistym. |
| **Szczegółowa konfiguracja** Korzysta z generowania, mowy, narzędzi i instrukcji systemowych. | **Uproszczona konfiguracja.** Ustaw `target_language_code` i przełączniki, takie jak `echo_target_language`. |

## Rozpocznij

Poniższe przykłady pokazują, jak zainicjować klienta i połączyć się z interfejsem Live API za pomocą konfiguracji tłumaczenia.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## Wysyłanie dźwięku

Aby przesyłać strumieniowo dane wejściowe głosowe do tłumaczenia, wysyłaj surowe, 16-bitowe dane audio PCM w formacie little-endian.

- **Format dźwięku wejściowego:** surowy 16-bitowy PCM przy 16 kHz (mono, little-endian).
- **Format dźwięku wyjściowego:** surowy 16-bitowy PCM przy 24 kHz (mono, little-endian).
- **Rozmiar fragmentu i czas oczekiwania:** wysyłaj dźwięk w fragmentach o długości 100 ms.

Poniższe przykłady pokazują, jak wysyłać do sesji fragmenty dźwięku.

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

### WebSockets

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
  }
}
```

## Konfiguracja

Aby włączyć tłumaczenie, musisz określić `translationConfig` w ramach `generationConfig` podczas konfigurowania sesji.

### Konfigurowanie wiadomości dotyczących konfiguracji

`generationConfig` obsługuje te pola, aby włączyć transkrypcje:

- **`inputAudioTranscription`**: obiekt, który po wystąpieniu umożliwia modelowi wysyłanie transkrypcji tekstowych wejściowego dźwięku.
- **`outputAudioTranscription`**: obiekt, który po wystąpieniu umożliwia modelowi wysyłanie transkrypcji tekstowych wyjściowego (przetłumaczonego) dźwięku.

`translationConfig` obsługuje te pola:

- **`targetLanguageCode`**: [kod języka BCP-47](#supported-languages), na który ma tłumaczyć model (np. `"pl"` w przypadku języka polskiego, `"es"` w przypadku języka hiszpańskiego). Domyślnie `"en"`.
- **`echoTargetLanguage`**: wartość logiczna wskazująca, jak należy obsługiwać dźwięk wejściowy, który jest już w języku docelowym. Jeśli ustawisz wartość `true`, model będzie powtarzać dźwięk wejściowy, który jest już w języku docelowym. Jeśli ustawisz wartość `false`, model będzie milczeć, gdy mowa wejściowa jest już w języku docelowym. Domyślnie ustawiona jest wartość `false`.

Oto przykład struktury wiadomości konfiguracyjnej:

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## Tokeny tymczasowe dla aplikacji po stronie klienta

W przypadku aplikacji działających w modelu klient-serwer możesz używać [tokenów tymczasowych](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pl) (obecnie w `v1alpha`), aby uniknąć ujawnienia klucza interfejsu API.

Podczas korzystania z tokenów tymczasowych z tłumaczeniem na żywo:

1. Musisz użyć punktu końcowego `v1alpha`.
2. **Konfiguracja blokowania:** domyślnie w ograniczeniach tworzenia tokena na serwerze należy określić `translationConfig`. Dzięki temu konfiguracja tłumaczenia jest zablokowana i klient nie może w nią ingerować.
3. **Odblokowywanie konfiguracji:** jeśli chcesz mieć możliwość ustawienia parametru `translationConfig` po stronie klienta (np. aby umożliwić użytkownikowi wybór języka docelowego), musisz pominąć go w żądaniu utworzenia tokena i zamiast niego ustawić parametr `"lock_additional_fields": []`. Umożliwi to ustawienie wartości `translationConfig` po stronie klienta.

### Tworzenie ograniczonego tokena efemerycznego

Poniższe przykłady pokazują, jak utworzyć token tymczasowy z ograniczeniami dotyczącymi tłumaczenia.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha'}
)

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
        'http_options': {'api_version': 'v1alpha'},
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    },
});
```

## Ograniczenia

- **Rodzaje danych wejściowych:** w przypadku tłumaczenia obsługiwane są tylko dane audio. Wpisywanie tekstu nie jest obsługiwane.
- **Replikacja głosu:** replikacja głosu może być niespójna. Głosy mogą się zmieniać po długich przerwach, przypisywać niewłaściwą płeć na podstawie tego, jak zaczyna się mowa, lub utknąć na jednym głosie podczas szybkich rozmów z wieloma mówcami.
- **Wykrywanie języka:** wykrywanie języka może być utrudnione w przypadku silnego akcentu, podobnych języków (np. hiszpańskiego i portugalskiego) lub szybkiego przełączania się między językami. **Uwaga:** powinno to mieć wpływ tylko na transkrypcję danych wejściowych. Kody języków i ostateczne tłumaczenie powinny być nadal prawidłowe.
- **Dźwięk w tle:** model został zaprojektowany tak, aby odfiltrowywać szumy i muzykę w celu uzyskania czystej mowy, ale nie wszystkie dźwięki w tle mogą być ignorowane.
- **Echo Target Language** (Powtórz język docelowy): gdy `echoTargetLanguage: true`, szumy w tle lub muzyka mogą wprowadzać artefakty w przetłumaczonym dźwięku, jeśli dźwięk wejściowy jest już w języku docelowym.

## Obsługiwane języki

Tłumaczenie na żywo jest dostępne w tych językach.

| Język | Kod BCP-47 | Język | Kod BCP-47 |
| --- | --- | --- | --- |
| afrikaans | af | kazachski | kk |
| akan | ak | khmerski | km |
| albański | sq | ruanda-rundi | rw |
| amharski | am | koreański | ko |
| arabski | ar | laotański | lo |
| ormiański | hy | łotewski | lv |
| azerski | az | litewski | lt |
| baskijski | eu | macedoński | mk |
| białoruski | be | malajski | ms |
| bengalski | bn | malajalam | ml |
| bułgarski | bg | marathi | mr |
| birmański (Mjanma) | my | mongolski | mn |
| kataloński | ca | nepalski | ne |
| Chiński (uproszczony) | zh-Hans | norweski | no, nb |
| chiński (tradycyjny) | zh-Hant | perski | fa |
| chorwacki | h | polski | pl |
| czeski | cs | portugalski (Brazylia) | pt-BR |
| duński | da | portugalski (Portugalia) | pt-PT |
| niderlandzki | nl | pendżabski | pa |
| angielski | en | rumuński | ro |
| estoński | et | rosyjski | ru |
| filipiński | fil | serbski | sr |
| fiński | fi | sindhi | sd |
| francuski | fr | syngaleski | si |
| galicyjski | gl | słowacki | sk |
| gruziński | ka | słoweński | sl |
| niemiecki | de | hiszpański | es |
| Kuchnia grecka | el | sundajski | su |
| gudżarati | gu | suahili | sw |
| hausa | ha | szwedzki | sv |
| hebrajski | on | tamilski | ta |
| hindi | hi | telugu | te |
| węgierski | hu | tajski | th |
| islandzki | jest | turecki | tr |
| indonezyjski | id | ukraiński | uk |
| włoski | it | urdu | ur |
| japoński | ja | uzbecki | uz |
| jawajski | jv | wietnamski | vi |
| kannada | kn | zulu | zu |

## Co dalej?

- Przeczytaj pełny przewodnik po [możliwościach](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=pl) interfejsu Live API.
- Zapoznaj się z przewodnikiem [Pierwsze kroki z pakietem SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=pl).
- Przeczytaj przewodnik [Pierwsze kroki z WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=pl).
- Przeczytaj przewodnik [Tokeny tymczasowe](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pl), aby dowiedzieć się, jak bezpiecznie uwierzytelniać aplikacje działające w modelu klient-serwer.
- Sklonuj [przykłady Live API](https://github.com/google-gemini/gemini-live-api-examples) z GitHuba.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-09 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-09 UTC."],[],[]]
