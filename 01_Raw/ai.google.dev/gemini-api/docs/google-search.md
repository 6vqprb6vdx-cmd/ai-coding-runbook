---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=ru
fetched_at: 2026-11-02T06:59:44.591422+00:00
title: "\u041e\u0431\u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441 Google \u041f\u043e\u0438\u0441\u043a\u043e\u043c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Обоснование с Google Поиском

Обоснование с Google Поиском позволяет модели Gemini получать доступ к веб-контенту в реальном времени и работает на всех доступных языках. Gemini может давать более точные ответы и ссылаться на проверенные источники, которые были опубликованы после даты актуальности данных.

Заземление помогает создавать приложения, которые могут:

- **Повышение фактической точности.** Снижение количества галлюцинаций модели за счет использования реальной информации.
- **Доступ к информации в реальном времени.** Отвечать на вопросы о недавних событиях и темах.
- **Добавляйте цитаты.** Повышайте доверие пользователей, показывая источники утверждений модели.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Проложить маршрут

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Как работает обоснование с Google Поиском

Если вы включите инструмент `google_search`, модель будет автоматически выполнять поиск, обработку и цитирование информации.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ru)

1. **Запрос пользователя.** Ваше приложение отправляет запрос пользователя в Gemini API с включенным инструментом `google_search`.
2. **Анализ запроса.** Модель анализирует запрос и определяет, может ли Google Поиск улучшить ответ.
3. **Google Поиск.** При необходимости модель автоматически генерирует один или несколько поисковых запросов и выполняет их.
4. **Обработка результатов поиска.** Модель обрабатывает результаты поиска, синтезирует информацию и формулирует ответ.
5. **Обоснованный ответ.** API возвращает окончательный, удобный для пользователя ответ, основанный на результатах поиска. Этот ответ включает текстовый ответ модели со встроенным объектом `annotations`, содержащим цитаты, а также шаги `google_search_call` и `google_search_result` с поисковыми запросами и подсказками.

## Как интерпретировать ответ с обоснованием

Если ответ успешно обоснован, текстовые выходные данные модели включают встроенные `annotations` непосредственно в блоке текстового контента. Эти аннотации содержат информацию о цитировании, связывающую части ответа с их источниками.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

Основные поля в ответе:

- `google_search_call` : содержит поисковый запрос `queries`, выполненный моделью.
- `google_search_result` – содержит `search_suggestions`, HTML-фрагмент для показа подсказок при поиске в интерфейсе. Полные требования к использованию приведены в [Условиях использования](https://ai.google.dev/gemini-api/terms?hl=ru#grounding-with-google-search).
- `text` с `annotations` : синтезированный ответ модели со встроенными цитатами. Каждая аннотация `url_citation` связывает сегмент текста (определяемый атрибутами `start_index` и `end_index`) с URL источника. Это ключ к
  созданию встроенных цитат.

Обоснование с Google Поиском можно использовать вместе с [инструментом URL-контекста](https://ai.google.dev/gemini-api/docs/url-context?hl=ru), чтобы обосновывать ответы как общедоступными данными из интернета, так и информацией с указанных вами URL.

## Указание источников с помощью встроенных цитат

API возвращает встроенные аннотации `url_citation` в блоке текстового контента, что дает вам полный контроль над тем, как источники отображаются в пользовательском интерфейсе.
Каждая аннотация содержит `start_index` и `end_index`, чтобы указать, какую часть текста она цитирует. Ниже рассказывается, как извлечь и показать их.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            String text = textContent.text().orElse("");
            System.out.println(text);
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nCitations:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof URLCitation) {
                  URLCitation citation = (URLCitation) annotation;
                  int start = citation.startIndex().orElse(0);
                  int end = citation.endIndex().orElse(0);
                  String citedText =
                      (start >= 0 && end <= text.length() && start <= end)
                          ? text.substring(start, end)
                          : "";
                  System.out.printf(
                      "  [%s](%s)%n", citation.title().orElse(""), citation.url().orElse(""));
                  System.out.printf("    Cited text: \"%s\"%n", citedText);
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Проложить маршрут

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    text := content.TextContent.Text
                    fmt.Println(text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nCitations:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                c := annotation.URLCitation
                                start := 0
                                if c.StartIndex != nil {
                                    start = *c.StartIndex
                                }
                                end := 0
                                if c.EndIndex != nil {
                                    end = *c.EndIndex
                                }
                                citedText := ""
                                if start >= 0 && end <= len(text) && start <= end {
                                    citedText = text[start:end]
                                }
                                title := ""
                                if c.Title != nil {
                                    title = *c.Title
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  [%s](%s)\n", title, url)
                                fmt.Printf("    Cited text: %q\n", citedText)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

В ответе будет текст и ссылки на источники:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Цены

Когда вы используете обоснование с Google Поиском в Gemini 3 и более новых моделях, с вашего проекта взимается плата за **каждый** поисковый запрос, который решает выполнить модель.
Эта модель оплаты за запрос включает 5000 бесплатных поисковых запросов в месяц, которые распределяются между всеми моделями Gemini 3 и более новыми. После этого стоимость составляет **14 долларов США за 1000 поисковых запросов**.

Например, если модель решает выполнить несколько поисковых запросов, чтобы ответить на одну подсказку (например, поиск `"UEFA Euro 2024 winner"` и `"Spain vs
England Euro 2024 final score"` в рамках одного вызова API), это считается двумя платными использованиями инструмента для этого запроса. При подсчете уникальных поисковых запросов для выставления счетов пустые запросы веб-поиска не учитываются.

При использовании обоснования в Google Поиске с Gemini 2.5 или более ранними моделями плата взимается за каждый запрос.

Подробную информацию о ценах можно найти на [странице цен Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ru).

## Поддерживаемые модели

Полный список возможностей можно найти на странице [Обзор модели](https://ai.google.dev/gemini-api/docs/models?hl=ru).

| Модель | Обоснование с Google Поиском |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Предварительная версия Gemini 3.1 Flash Image | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Предварительный просмотр изображений в Gemini 3 Pro | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Поддерживаемые комбинации инструментов

Обоснование с Google Поиском можно использовать с другими инструментами, такими как [выполнение кода](https://ai.google.dev/gemini-api/docs/code-execution?hl=ru), [URL-контекст](https://ai.google.dev/gemini-api/docs/url-context?hl=ru) и [обоснование с Google Картами](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ru) (поддерживается в Gemini 3.5 Flash-Lite и более поздних моделях), чтобы решать более сложные задачи.
Модели Gemini 3 также поддерживают комбинирование этих встроенных инструментов с пользовательскими (вызов функций). Подробнее [о сочетаниях инструментов](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ru)…

## Дальнейшие действия

- Узнайте о других доступных инструментах, например [вызове функций](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru).
- Узнайте, как дополнять запросы определенными URL с помощью [инструмента URL-контекста](https://ai.google.dev/gemini-api/docs/url-context?hl=ru).

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-29 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-29 UTC."],[],[]]
