---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ru
fetched_at: 2026-11-02T07:21:40.413651+00:00
title: "\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044f\u043c Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Руководство по возможностям Live API

Это подробное руководство, в котором рассказывается о возможностях и настройках Live API.
Общие сведения и образец кода для распространенных вариантов использования приведены на странице [Начало работы с Live API](https://ai.google.dev/gemini-api/docs/live?hl=ru).

## Подготовка

- **Ознакомьтесь с основными понятиями.** Если вы ещё этого не сделали, прочитайте статью [Начало работы с Live API](https://ai.google.dev/gemini-api/docs/live?hl=ru) .
  Вы узнаете об основных принципах работы Live API и [способах его реализации](https://ai.google.dev/gemini-api/docs/live?hl=ru#implementation-approach).
- **Попробуйте Live API в AI Studio.** Прежде чем начать разработку, вы можете протестировать Live API в [Google AI Studio](https://aistudio.google.com/app/live?hl=ru). Чтобы использовать Live API в Google AI Studio, выберите **Stream (Трансляция)**.

## Сравнение моделей

В таблице ниже описаны основные различия между моделями [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ru), [Gemini 3.8 Live Extended Thinking](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=ru) и [Gemini 3.1 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ru).

| Функция | Gemini 3.8 Live | Gemini 3.8 Live Extended Thinking | Gemini 3.1 Flash Live Preview |
| --- | --- | --- | --- |
| **Рекомендуется для** | Вариант по умолчанию для большинства голосовых агентов с низкой задержкой. | Рекомендуется, когда требуется более глубокое рассуждение. | Устаревшая предварительная версия модели. Рекомендуем перейти на [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ru). |
| **[Думаю…](#native-audio-output-thinking)** | Поддерживается (чередующиеся рассуждения). `thinkingLevel` не поддерживается (не включайте в настройку). | Поддерживается. Настраиваемое обоснование для фонового режима (`thinkingLevel`: `low`, `medium`, `high`; `minimal` не поддерживается). | Использует `thinkingLevel` для управления глубиной рассуждений с помощью таких настроек, как `minimal`, `low`, `medium` и `high`. По умолчанию используется значение `minimal`, чтобы оптимизировать задержку. Подробнее [о Thinking в Live API](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=ru)… |
| **[Получение ответа](https://ai.google.dev/api/live?hl=ru#bidigeneratecontentservercontent)** | Одно серверное событие может содержать несколько частей контента одновременно. | Одно серверное событие может содержать несколько частей контента одновременно. Когда включено асинхронное рассуждение, `turnComplete: true` не указывает на бездействующий сеанс. Используйте `interaction_status` (`IN_PROGRESS` вместо `IDLE`). | Одно событие сервера может содержать несколько частей контента одновременно (например, `inlineData` и расшифровку). Убедитесь, что ваш код обрабатывает все части каждого события, чтобы не упустить контент. |
| **[Контент клиента](#incremental-updates)** | `send_client_content` поддерживается на протяжении всего жизненного цикла сеанса с явными ролями (`user` или `model`). `turn_complete=true` безусловно прерывает генерацию. | `send_client_content` поддерживается на протяжении всего жизненного цикла сеанса с явными ролями (`user` или `model`). `turn_complete=true` безусловно прерывает генерацию. | `send_client_content` поддерживается на протяжении всего жизненного цикла сеанса с явными ролями (`user` или `model`). `turn_complete=true` безусловно прерывает генерацию. |
| **[Асинхронный вызов функций](https://ai.google.dev/gemini-api/docs/live-tools?hl=ru#async-function-calling)** (`behavior: NON_BLOCKING`) | Поддерживается (по умолчанию). Задайте `behavior: NON_BLOCKING` или используйте обратно совместимый режим блокировки с `behavior: BLOCKING`. Поддерживается планирование функций (`SILENT`, `WHEN_IDLE`, `INTERRUPTED`). | Поддерживается (только асинхронный режим). Поддерживается только выполнение `NON_BLOCKING`. Режим блокировки и планирование функций не поддерживаются. | Не поддерживается. Вызов функций выполняется только последовательно. Модель не начнет отвечать, пока вы не отправите ответ инструмента. |

Чтобы перейти на Gemini 3.8 Live, ознакомьтесь с [руководством по переходу](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ru#migrating).
Чтобы узнать больше о Thinking, ознакомьтесь с [руководством по Thinking](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=ru) и [руководством по обновлению](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=ru#upgrading).

## Установка подключения

В примере ниже показано, как создать подключение с помощью ключа API.

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

## Способы взаимодействия

В следующих разделах приведены примеры и контекст для различных модальностей ввода и вывода, доступных в Live API.

### Отправка аудио…

Аудио должно отправляться в виде необработанных данных PCM (необработанное 16-битное аудио PCM, 16 кГц, прямой порядок байтов).

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

### Аудиоформаты

Аудиоданные в Live API всегда необработанные, с прямым порядком байтов, 16-битные PCM. Частота дискретизации аудиовыхода всегда составляет 24 кГц. Входной аудиосигнал имеет частоту 16 кГц, но Live API при необходимости выполнит ресемплирование, поэтому можно отправлять любую частоту дискретизации. Чтобы передать частоту дискретизации входного аудио, задайте для MIME-типа каждого объекта [Blob](https://ai.google.dev/api/caching?hl=ru#Blob), содержащего аудио, значение, подобное `audio/pcm;rate=16000`.

### Получение аудио

Аудиоответы модели поступают в виде фрагментов данных.

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

### Отправка сообщения…

Текст можно отправить с помощью `send_realtime_input` (Python) или `sendRealtimeInput` (JavaScript).

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

### Отправка видео…

Кадры видео отправляются как отдельные изображения (например, JPEG или PNG) с определенной частотой (не более одного кадра в секунду).

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

#### Дополнительные обновления контента

Используйте инкрементные обновления, чтобы отправлять текстовые данные, устанавливать или восстанавливать контекст сеанса. Для коротких контекстов вы можете отправлять пошаговые взаимодействия, чтобы представить точную последовательность событий:

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

Для более длинных контекстов рекомендуется предоставить сводку одного сообщения, чтобы освободить окно контекста для последующих взаимодействий. Другой способ загрузки контекста сеанса описан в разделе [Возобновление сеанса](https://ai.google.dev/gemini-api/docs/live-session?hl=ru#session-resumption).

### Транскрипции

Помимо ответа модели, вы также можете получить расшифровки как аудиовыхода, так и аудиовхода.

Чтобы включить расшифровку аудиовывода модели, отправьте `output_audio_transcription` в конфигурации настройки. Язык расшифровки определяется по ответу модели.

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

Чтобы включить расшифровку аудиоввода модели, отправьте `input_audio_transcription` в конфигурации настройки.

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

Чтобы улучшить распознавание определенных терминов, таких как имена собственные, названия брендов или технические термины, добавьте список `custom_vocabulary` в `input_audio_transcription`. Вы можете указать до 1000 терминов, но наилучшие результаты обычно достигаются при использовании до 100 терминов. Подробнее [о смещении пользовательского словаря](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=ru#custom-vocabulary-biasing)…

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {
        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"],
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### Как изменить голос и язык

Модели с [прямым аудиовыводом](#native-audio-output) поддерживают любые голоса, доступные для моделей [Text-to-Speech (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru#voices). Послушать все голоса можно в [AI Studio](https://aistudio.google.com/app/live?hl=ru).

Чтобы указать голос, задайте его название в объекте `speechConfig` в рамках конфигурации сеанса:

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

Live API поддерживает [несколько языков](#supported-languages).
Модели с [прямым аудиовыводом](#native-audio-output) автоматически выбирают подходящий язык и не поддерживают явное указание кода языка.

## Возможности нативной аудиорекламы

В наших последних моделях есть функция [прямого аудиовывода](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ru), которая обеспечивает естественное, реалистичное звучание речи и улучшенную многоязычную производительность.

### Думающая

Модели Gemini 3.8 Live Extended Thinking и Gemini 3.1 используют `thinkingLevel` для управления глубиной мышления. Для `gemini-3.8-live` не поддерживается `thinkingLevel`, поэтому его нужно опустить в настройках. Gemini 3.8 Live Extended Thinking поддерживает `low`, `medium` и `high` (`minimal` не поддерживается). Модели Gemini 3.1 поддерживают `minimal`, `low`, `medium` и `high`. Подробнее о том, [как работает Live API](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=ru)…

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

Вы также можете включить краткие пересказы мыслей, задав для параметра `includeThoughts` значение `true` в конфигурации. Подробнее [о кратких пересказах рассуждений](https://ai.google.dev/gemini-api/docs/thinking?hl=ru#summaries)…

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

### Эмоциональная коммуникация

Эта функция позволяет Gemini адаптировать стиль ответа к выражению и тону ввода.

Чтобы использовать эмоциональную коммуникацию, укажите версию API `v1beta` и задайте для `enable_affective_dialog` значение `true` в сообщении настройки:

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

### Проактивное аудио

Если эта функция включена, Gemini может не отвечать, если контент нерелевантен.

Чтобы использовать его, задайте для версии API значение `v1beta`, настройте поле `proactivity` в сообщении о настройке и задайте для `proactive_audio` значение `true`:

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

## Устный перевод

Live API поддерживает перевод устной речи в реальном времени с низкой задержкой. Эта функция позволяет создавать приложения для голосового перевода в реальном времени.

Дополнительную информацию и примеры можно найти в [руководстве по мгновенному переводу](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=ru).

## Обнаружение голосовой активности (VAD)

Обнаружение голосовой активности (VAD) позволяет модели распознавать, когда говорит человек. Это важно для естественного общения, поскольку позволяет пользователю прервать модель в любой момент.

Когда VAD обнаруживает прерывание, текущая генерация отменяется и отбрасывается. В истории сеанса сохраняется только информация, которая уже была отправлена клиенту. Затем сервер отправляет сообщение [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=ru#bidigeneratecontentservercontent), чтобы сообщить о прерывании.

Затем сервер Gemini отменяет все ожидающие вызовы функций и отправляет сообщение `BidiGenerateContentServerContent` с идентификаторами отмененных вызовов.

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

### Автоматическое определение активности голоса

По умолчанию модель автоматически выполняет VAD для непрерывного входного аудиопотока. VAD можно настроить с помощью поля [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=ru#RealtimeInputConfig.AutomaticActivityDetection) в [конфигурации настройки](https://ai.google.dev/api/live?hl=ru#BidiGenerateContentSetup).

Если аудиопоток приостановлен более чем на секунду (например, пользователь отключил микрофон), необходимо отправить событие [`audioStreamEnd`](https://ai.google.dev/api/live?hl=ru#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end), чтобы очистить кеш аудио. Клиент может возобновить отправку аудиоданных в любое время.

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

Если задано значение `send_realtime_input`, API будет автоматически отвечать на аудио на основе VAD. В то время как `send_client_content` добавляет сообщения в контекст модели по порядку, `send_realtime_input` оптимизирован для быстрого ответа за счет детерминированного упорядочивания.

### Автоматическая настройка VAD

Чтобы лучше контролировать работу VAD, можно настроить следующие параметры: Подробную информацию можно найти в [документации по API](https://ai.google.dev/api/live?hl=ru#automaticactivitydetection).

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

### Гибридный VAD

Гибридный VAD сочетает в себе преимущества автоматического (надежное обнаружение начала речи) и ручного (быстрое завершение ответа).

В этой конфигурации:

1. **Автоматическое определение голосовой активности остается включенным** на сервере. Сервер автоматически определяет начало речи пользователя, используя заполнение префикса, чтобы избежать обрезки начала высказываний.
2. Клиент использует **клиентский VAD**, чтобы определить, когда пользователь перестает говорить.
3. Когда клиентский VAD обнаруживает конец речи, он отправляет на сервер сигнал [`audio_stream_end`](https://ai.google.dev/api/live?hl=ru#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end).
4. Сервер обрабатывает сигнал `audio_stream_end` как запрос на немедленное завершение, обходя стандартную задержку обнаружения тишины на стороне сервера и возвращая расшифровку и ответ модели с минимальной задержкой.
5. Если VAD на стороне клиента не срабатывает, VAD на стороне сервера действует как резервный вариант для обнаружения конца речи.

Обратите внимание, что если пороговое значение VAD на стороне клиента установлено слишком агрессивно, это может привести к прерыванию речи. Однако этот подход позволяет избежать проблем с усечением начала, которые могут возникнуть при ручном VAD.

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

### Отключить автоматическое определение активности голоса

Вы также можете отключить автоматическое определение активности голоса, задав для параметра `realtimeInputConfig.automaticActivityDetection.disabled` значение `true` в сообщении setup. В этой конфигурации клиент отвечает за обнаружение речи пользователя и отправку сообщений [`activityStart`](https://ai.google.dev/api/live?hl=ru#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) и [`activityEnd`](https://ai.google.dev/api/live?hl=ru#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) в подходящее время. В этой конфигурации `audioStreamEnd` не отправляется. Вместо этого любое прерывание потока помечается сообщением `activityEnd`.

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

### Параметры VAD и их влияние на качество

При использовании автоматического VAD два ключевых параметра управляют тем, как аудио сегментируется на речевые повороты перед отправкой в модель:

- **`prefixPaddingMs`** – количество аудио, которое нужно включить *до* обнаружения речи. Это позволяет модели захватить начало речи, включая первый слог, который может быть произнесен до срабатывания детектора. Если задать значение `0`, начало слов может быть обрезано.
- **`silenceDurationMs`** – время, в течение которого сервер ожидает ответа, прежде чем завершить речевой ход. Это определяет, насколько система терпима к естественным паузам в середине предложения (например, на размышление, дыхание или границы предложения).

#### Влияние `silenceDurationMs` на качество звука

Значение `silenceDurationMs` напрямую влияет на размер и полноту аудиофрагментов, которые модель получает для обработки:

- **Рекомендуемое значение (500–800 мс).** Обеспечивает хороший баланс: модель получает полные, контекстуально насыщенные аудиофрагменты, а задержка остается разумной. По умолчанию на сервере установлено значение около 800 мс.
- **Слишком низкое значение (например, 100–200 мс).** Система завершает реплику во время естественных пауз, разбивая одно высказывание на несколько небольших аудиофрагментов. Модель получает эти фрагменты по отдельности, теряя контекст между ними, что приводит к снижению качества расшифровки и ответа.
- **Слишком высокое значение (например, более 2000 мс).** Система долго ждет после того, как пользователь перестает говорить, что увеличивает воспринимаемую задержку перед ответом модели.

#### Рекомендации по ручному (клиентскому) VAD

Если вы отключите автоматическое определение активности голоса и будете управлять сигналами `activityStart`/`activityEnd` с помощью собственного клиентского детектора голоса, встроенные механизмы буферизации аудио на сервере будут обходиться. Вот что это значит:

1. **Нет буфера перед речью.** Сервер больше не добавляет аудио перед началом распознанной речи. Прежде чем отправлять `activityStart`, клиент должен включить достаточный аудиоконтекст.
2. **Без задержки.** Сервер сразу же реагирует на сигнал `activityEnd`. Если в вашем клиентском VAD используется агрессивный порог окончания речи (например, 200 мс тишины), речь может прерываться в середине предложения во время естественных пауз.

Чтобы сохранить качество звука при ручном обнаружении голосовой активности, используйте порог тишины в конце речи не менее **500 мс** в детекторе голосовой активности клиента.
Пороговые значения ниже этого часто приводят к фрагментации аудио, что ухудшает качество расшифровки и ответа модели.

## Число токенов

Общее количество использованных токенов можно найти в поле [usageMetadata](https://ai.google.dev/api/live?hl=ru#usagemetadata) возвращенного сообщения сервера.

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

## Разрешение медиаконтента

Вы можете указать разрешение для входного медиаконтента, задав поле `mediaResolution` в конфигурации сеанса:

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

Вы можете настроить `mediaResolution` для мультимодальных сеансов, которые включают аудио, видео или изображения. В то время как `mediaResolution` корректирует распределение токенов на кадр для визуальных входных данных, аудиопотоки токенизируются с фиксированной скоростью в секунду для всех настроек разрешения. Подробную информацию можно найти в [руководстве по разрешению медиаконтента](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ru).

## Ограничения

При планировании проекта учитывайте следующие ограничения Live API.

### Модальности ответов

Встроенные аудиомодели поддерживают только модальность ответа `AUDIO`. Если вам нужен ответ модели в виде текста, используйте функцию [расшифровки аудиовыхода](#audio-transcription).

### Аутентификация клиента

По умолчанию Live API поддерживает только аутентификацию между серверами. Если вы реализуете приложение Live API, используя [подход "клиент-сервер"](https://ai.google.dev/gemini-api/docs/live?hl=ru#implementation-approach), вам нужно использовать [временные токены](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ru), чтобы снизить риски безопасности.

### длительность сеанса;

Аудиосеансы ограничены 15 минутами, а аудио- и видеосеансы – двумя минутами.
Однако вы можете настроить разные [методы управления сеансами](https://ai.google.dev/gemini-api/docs/live-session?hl=ru) для неограниченного продления длительности сеанса.

### Окно контекста

Для сеанса действуют следующие ограничения на размер окна контекста:

- 128 000 токенов для моделей с [прямым аудиовыводом](#native-audio-output).
- 32 000 токенов для других моделей Live API.

## Поддерживаемые языки

Live API поддерживает 99 языков, перечисленных ниже.

| Язык | Код BCP-47 | Язык | Код BCP-47 |
| --- | --- | --- | --- |
| Африкаанс | `af` | Латвийский | `lv` |
| Акан | `ak` | Литовский | `lt` |
| Албанский | `sq` | Македонский | `mk` |
| Амхарский | `am` | Малайский | `ms` |
| Арабский | `ar` | Малаялам | `ml` |
| Армянский | `hy` | Мальтийский | `mt` |
| Ассамский | `as` | Маори | `mi` |
| Азербайджанский | `az` | Маратхи | `mr` |
| Баскский | `eu` | Монгольский | `mn` |
| Belarusian | `be` | Непальский | `ne` |
| Бенгальский | `bn` | Норвежский | `no`, `nb` |
| Боснийский | `bs` | Ория | `or` |
| Болгарский | `bg` | Оромо | `om` |
| Бирманский | `my` | Пашто | `ps` |
| Каталанский | `ca` | Персидский | `fa` |
| Себуанский | `ceb` | Польский | `pl` |
| Китайский (упрощенный) | `zh-Hans` | Португальский (Бразилия) | `pt-BR` |
| Китайский (традиционный) | `zh-Hant` | Португальский (Португалия) | `pt-PT` |
| Хорватский | `hr` | Пенджабский | `pa` |
| Чешский | `cs` | Кечуа | `qu` |
| Датский | `da` | Румынский | `ro` |
| Нидерландский | `nl` | Романшский | `rm` |
| Английский | `en` | Русский | `ru` |
| Эстонский | `et` | Сербский | `sr` |
| Фарерский | `fo` | Синдхи | `sd` |
| Филиппинский | `fil` | Сингальский | `si` |
| Финский | `fi` | Словацкий | `sk` |
| Французский | `fr` | Словенский | `sl` |
| Галисийский | `gl` | Сомали | `so` |
| Грузинский | `ka` | Южный сото | `st` |
| Немецкий | `de` | Испанский | `es` |
| Греческий | `el` | Суахили | `sw` |
| Гуджарати | `gu` | Шведский | `sv` |
| Хауса | `ha` | Таджикский | `tg` |
| Иврит | `he` | Тамильский | `ta` |
| хинди | `hi` | Телугу | `te` |
| Венгерский | `hu` | Тайский | `th` |
| Исландский | `is` | Тсвана | `tn` |
| Индонезийский | `id` | Турецкий | `tr` |
| Ирландский | `ga` | Туркменский | `tk` |
| Итальянский | `it` | Украинский | `uk` |
| Японский | `ja` | Урду | `ur` |
| Каннада | `kn` | Узбекский | `uz` |
| Казахский | `kk` | Вьетнамский | `vi` |
| Кхмерский | `km` | валлийский | `cy` |
| Киньяруанда | `rw` | Западнофризский | `fy` |
| Корейский | `ko` | Волоф | `wo` |
| Курдский | `ku` | Йоруба | `yo` |
| Киргизский | `ky` | Зулу | `zu` |
| Лаосский | `lo` |  |  |

## Дальнейшие действия

- Прочитайте руководства по [использованию инструментов](https://ai.google.dev/gemini-api/docs/live-tools?hl=ru) и [управлению сеансами](https://ai.google.dev/gemini-api/docs/live-session?hl=ru), чтобы узнать, как эффективно работать с Live API.
- Попробуйте Live API в [Google AI Studio](https://aistudio.google.com/app/live?hl=ru).
- Дополнительную информацию о моделях Live API можно найти на страницах [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ru) и [Gemini 3.8 Live Extended Thinking](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=ru).
- Попробуйте другие примеры из [руководства по Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=ru),
  [руководства по инструментам Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=ru)
  и [скрипта для начала работы с Live API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py).

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-29 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-29 UTC."],[],[]]
