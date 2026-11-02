---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=ru
fetched_at: 2026-11-02T07:24:01.458398+00:00
title: "\u041e\u0431\u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441 Google \u041a\u0430\u0440\u0442\u0430\u043c\u0438 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs/generate-content?hl=ru)

Отправить отзыв

# Обоснование с Google Картами

Обоснование с Google Картами связывает генеративные возможности Gemini с подробными, фактическими и актуальными данными Google Карт. Этот API позволяет разработчикам легко добавлять в свои приложения функции, связанные с местоположением. Когда запрос пользователя связан с данными Карт, модель Gemini использует Google Карты, чтобы предоставить точные и актуальные ответы, относящиеся к указанному местоположению или приблизительному местоположению пользователя.

- **Точные ответы с учетом местоположения.** Используйте обширные и актуальные данные Google Карт для запросов, связанных с географическим положением.
- **Улучшенная персонализация.** Рекомендации и информация подбираются с учетом местоположений, указанных пользователями.

## Начать

В этом примере показано, как интегрировать обоснование с Google Картами в приложение, чтобы предоставлять точные ответы на запросы пользователей с учетом местоположения. В запросе запрашиваются местные рекомендации с необязательным местоположением пользователя, что позволяет модели Gemini использовать данные Google Карт.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Как работает обоснование с Google Картами

Обоснование с Google Картами интегрирует Gemini API с экосистемой Google Geo, используя Maps API в качестве источника обоснования. Если запрос пользователя содержит географический контекст, модель Gemini может вызвать инструмент обоснования с Google Картами. Затем модель может генерировать ответы на основе данных Google Карт, относящихся к указанному местоположению.

Обычно процесс включает следующие этапы:

1. **Запрос пользователя.** Пользователь отправляет запрос в ваше приложение, возможно, с указанием географического контекста (например, "кофейни рядом", "музеи в Сан-Франциско").
2. **Вызов инструмента.** Модель Gemini распознает географический контекст и вызывает инструмент обоснования с Google Картами. В этом инструменте можно указать `latitude` и `longitude` пользователя. Это инструмент текстового поиска, который работает так же, как поиск на Картах: в локальных запросах ("рядом со мной") используются координаты, а на конкретные или нелокальные запросы явное указание местоположения вряд ли повлияет.
3. **Получение данных.** Сервис Grounding with Google Maps отправляет в Google Карты запросы на получение нужной информации, например о местах, отзывах, фотографиях, адресах и часах работы.
4. **Обоснованная источниками генерация.** Полученные данные Maps используются для формирования ответа модели Gemini, что обеспечивает фактическую точность и релевантность.
5. **Ответ.** Модель возвращает текстовый ответ, который включает цитаты из источников Google Карт.

## Зачем и когда использовать обоснование с Google Картами

Основание на Google Картах идеально подходит для приложений, которым требуется точная, актуальная и привязанная к местоположению информация. Это повышает удобство использования, предоставляя релевантный и персонализированный контент, основанный на обширной базе данных Google Карт, содержащей более 250 миллионов мест по всему миру.

Используйте Grounding with Google Maps, если ваше приложение должно:

- Дайте полные и точные ответы на вопросы, связанные с местоположением.
- Создавайте разговорные планировщики путешествий и местные путеводители.
- Рекомендовать интересные места, например рестораны или магазины, на основе местоположения и предпочтений пользователя.
- Создавайте сервисы с учетом местоположения для социальных сетей, розничной торговли или доставки еды.

Обоснование с Google Картами отлично подходит для случаев, когда важны близость и актуальные фактические данные, например при поиске лучшей кофейни поблизости или построении маршрута.

## Методы и параметры API

Обоснование с помощью Google Карт доступно через Gemini API как инструмент в методе [`generateContent`](https://ai.google.dev/api/generate-content?hl=ru). Чтобы включить и настроить Grounding with Google Maps, добавьте объект [`googleMaps`](https://ai.google.dev/api/caching?hl=ru#GoogleMaps) в параметр `tools` запроса.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

Кроме того, инструмент поддерживает передачу контекстного местоположения в виде `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### Как интерпретировать ответ с обоснованием

Если ответ успешно обоснован данными Google Карт, он содержит поле [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ru#GroundingMetadata).
Эти структурированные данные необходимы для проверки утверждений и создания в приложении удобных цитат, а также для соблюдения требований к использованию сервиса.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Gemini API возвращает следующую информацию с [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ru#GroundingMetadata):

- `groundingChunks` – массив объектов, содержащих источники `maps` (`uri`, `placeId` и `title`).
- `groundingSupports`: массив фрагментов, позволяющих связать текст ответа модели с источниками в `groundingChunks`. Каждый фрагмент связывает текстовый диапазон (определенный с помощью тегов `startIndex` и `endIndex`) с одним или несколькими тегами `groundingChunkIndices`. Это ключ к созданию встроенных цитат.

Фрагмент кода, показывающий, как отображать встроенные цитаты в тексте, можно найти в [примере](https://ai.google.dev/gemini-api/docs/google-search?hl=ru#attributing_sources_with_inline_citations) в документации по обоснованию с Google Поиском.

## Примеры использования

Обоснование с Google Картами поддерживает различные варианты использования с учетом местоположения. В примерах ниже показано, как использовать обоснование с Google Картами с разными запросами и параметрами. Информация в обоснованных результатах Google Карт может отличаться от фактических условий.

### Как отвечать на вопросы о конкретных местах

Задавайте подробные вопросы о конкретном месте, чтобы получить ответы на основе отзывов пользователей Google и других данных Карт.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### Персонализация на основе местоположения

Получайте рекомендации, адаптированные к предпочтениям пользователя и конкретному географическому региону.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### Помощь в планировании маршрута

Создавайте планы на несколько дней с маршрутами и информацией о различных местах. Это отлично подходит для приложений, связанных с путешествиями.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## Требования к использованию сервиса

В этом разделе описаны требования к использованию сервиса Grounding with Google Maps.

### Уведомляйте пользователей о том, что вы используете источники Google Карт

В каждом обоснованном результате поиска на Google Картах вы найдете источники в `groundingChunks`, подтверждающие ответ. Также возвращаются следующие метаданные:

- URI источника
- название
- ID

При показе результатов обоснования с Google Картами вы должны указать связанные источники Google Карт и сообщить пользователям следующее:

- Источники Google Карт должны быть указаны сразу после сгенерированного контента, который они подтверждают. Такой контент также называется обоснованным результатом Google Карт.
- Источники Google Карт должны быть видны в рамках одного взаимодействия с пользователем.

### Показывать источники Google Карт со ссылками на Карты

Для каждого источника в `groundingChunks` и `grounding_chunks.maps.placeAnswerSources.reviewSnippets` необходимо сгенерировать предварительный просмотр ссылки, соответствующий следующим требованиям:

- Укажите Google Карты в качестве источника данных в соответствии с [правилами указания авторства Google Карт](#maps-attribution-guidelines).
- Показывать название источника, указанное в ответе.
- Перейдите к источнику, используя значок `uri` или `googleMapsUri` из ответа.

На этих изображениях показаны минимальные требования к отображению источников и ссылок на Google Карты.

![Запрос с ответом, в котором указаны источники](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=ru)

Вы можете свернуть источники.

![Запрос с ответом и источниками свернут](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=ru)

Дополнительно: улучшите предпросмотр ссылки, добавив в него контент, например:

- Перед текстовой атрибуцией Google Карт вставляется [значок Google Карт](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=ru).
- Фотография с URL источника (`og:image`).

Дополнительную информацию о некоторых поставщиках данных для Google Карт и условиях лицензирования можно найти в [юридических уведомлениях Google Карт и Google Планеты Земля](https://www.google.com/help/legalnotices_maps/?hl=ru).

### Правила атрибуции текста на Google Картах

При указании источников Google Карт в тексте следуйте этим рекомендациям:

- Не изменяйте текст "Google Карты":
  - Не меняйте регистр букв в названии Google Maps.
  - Не переносите Google Карты на несколько строк.
  - Не локализуйте Google Карты.
  - Запретите браузерам переводить Google Карты с помощью HTML-атрибута translate="no".
- Стиль текста на Картах Google можно задать так, как описано в таблице ниже.

| Свойство | Стиль |
| --- | --- |
| `Font family` | Roboto. Загружать шрифт необязательно. |
| `Fallback font family` | Любой шрифт без засечек, который уже используется в вашем продукте, или Sans-Serif, чтобы использовать системный шрифт по умолчанию. |
| `Font style` | Обычный |
| `Font weight` | 400 |
| `Font color` | Белый, черный (#1F1F1F) или серый (#5E5E5E). Контрастность по отношению к фону должна быть не менее 4,5:1. |
| `Font size` | - Минимальный размер шрифта: 12 sp. - Максимальный размер шрифта: 16 sp. - Подробнее о единицах sp можно узнать на [сайте Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | Обычный |

#### Пример CSS

Ниже приведен код CSS, с помощью которого можно отобразить слово "Google" на белом или светлом фоне с использованием подходящего шрифта и цвета.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### идентификатор места и идентификатор отзыва;

Данные Google Карт включают идентификатор места и идентификатор отзыва. Вы можете кешировать, хранить и экспортировать следующие данные ответов:

- `placeId`
- `reviewId`

Ограничения на кеширование, указанные в Условиях использования обоснования с Google Картами, не применяются.

### Запрещенная деятельность и территория

Чтобы платформа оставалась безопасной и надежной, для обоснования с Google Картами действуют дополнительные ограничения на определенный контент и действия. В дополнение к ограничениям на использование, указанным в [Условиях](https://ai.google.dev/gemini-api/terms?hl=ru#grounding-with-google-maps):

- Вы не будете использовать обоснование с Google Картами для деятельности с высоким риском, включая работу экстренных служб.
- Вы не будете распространять или продвигать свое приложение, в котором предлагается обоснование с Google Картами, на запрещенной территории. Подробнее [о запрещенных территориях платформы Google Карт](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=ru)…
  Список запрещенных территорий может время от времени обновляться.

## Рекомендации

- **Указывайте местоположение пользователя.** Чтобы получать наиболее релевантные и персонализированные ответы, всегда включайте `user_location` (широту и долготу) в конфигурацию `googleMapsGrounding`, когда местоположение пользователя известно.
- **Информируйте конечных пользователей.** Четко сообщайте конечным пользователям, что для ответов на их запросы используются данные Google Карт, особенно когда инструмент включен.
- **Отслеживайте задержку.** В разговорных приложениях убедитесь, что задержка P95 для обоснованных ответов остается в допустимых пределах, чтобы обеспечить удобство работы.
- **Отключайте, когда не нужно.** Обоснование с Google Картами по умолчанию отключено. Включайте ее (`"tools": [{"googleMaps": {}}]`), только если запрос имеет четкий географический контекст, чтобы оптимизировать эффективность и расходы.

## Ограничения

- **Географический охват.** Обоснование с Google Картами доступно во всех странах.
- **Поддерживаемые модели.** См. раздел [Поддерживаемые модели](#supported-models).
- **Мультимодальные входные и выходные данные.** Обоснование с Google Картами в настоящее время не поддерживает мультимодальные входные и выходные данные, кроме текста.
- **Состояние по умолчанию.** Инструмент "Обоснование с Google Картами" по умолчанию отключен.
  Его нужно явно включить в запросах к API.

## Цены и ограничения частоты запросов

Цены на обоснование с Google Картами зависят от поколения модели:

- **Gemini 3 и более новые модели.** За каждый поисковый запрос, который модель решит выполнить, с вашего проекта будет взиматься плата. При этом 5000 запросов в месяц предоставляются бесплатно для всех моделей Gemini 3 и более новых версий. После этого стоимость составит **14 долларов США за 1000 поисковых запросов**. Один запрос к API может привести к тому, что модель выполнит несколько поисковых запросов, чтобы найти нужную информацию. Каждый из этих запросов считается платным использованием инструмента.
- **Gemini 2.5 и более ранние модели.** Оплата взимается за каждый поисковый запрос (25 долларов США за 1000 запросов с обоснованием). Плата за запрос взимается, только если в ответ на него возвращается хотя бы один результат, заземленный на Google Картах, независимо от того, сколько поисковых запросов выполнила модель, чтобы получить этот результат.

Квота на обоснование с Google Картами обычно соответствует ограничениям частоты запросов для базовой модели Gemini. Подробную информацию о ценах можно найти на [странице цен на API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=ru).

## Поддерживаемые модели

Обоснование с Google Картами поддерживают следующие модели:

| Модель | Обоснование с Google Картами |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=ru) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ru) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ru) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ru) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ru) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ru) | ✔️ |
| [Предварительная версия Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ru) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ru) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ru) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ru) | ✔️ |

## Поддерживаемые сочетания инструментов

Обоснование с Google Картами можно использовать с другими встроенными инструментами, например [обоснованием с Google Поиском](https://ai.google.dev/gemini-api/docs/google-search?hl=ru) (поддерживается в Gemini 3.5 Flash-Lite и более поздних моделях), чтобы решать более сложные задачи.
Модели Gemini 3 также поддерживают комбинирование этих встроенных инструментов с пользовательскими (вызов функций). Подробнее [о сочетаниях инструментов](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ru)…

## Дальнейшие действия

- Попробуйте [обоснование с Google Поиском в Gemini API Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ru).
- Подробнее [о других доступных инструментах](https://ai.google.dev/gemini-api/docs/tools?hl=ru)…
- Чтобы узнать больше о принципах ответственного использования ИИ и фильтрах безопасности Gemini API, ознакомьтесь с [руководством по настройкам безопасности](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ru).

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-15 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-15 UTC."],[],[]]
