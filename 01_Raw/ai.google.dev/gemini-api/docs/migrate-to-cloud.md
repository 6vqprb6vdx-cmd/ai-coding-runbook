---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=ru
fetched_at: 2026-10-12T07:10:18.771873+00:00
title: "Gemini Developer API \u0438 \u043f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0430 Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Флэш-память Gemini 3.8 теперь доступна. [Попробуйте!](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Gemini Developer API и платформа Gemini

При разработке решений на основе генеративного искусственного интеллекта с помощью Gemini Google предлагает два API-продукта: [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=ru) и [Gemini platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ru).

Gemini Developer API – это самый быстрый способ создавать, запускать и масштабировать приложения на основе Gemini. Большинству разработчиков следует использовать Gemini Developer API, если только им не нужны специальные корпоративные средства управления.

Платформа Gemini предлагает комплексную экосистему готовых к использованию в корпоративной среде функций и сервисов для создания и развертывания приложений на основе генеративного искусственного интеллекта с поддержкой Google Cloud.

Недавно мы упростили перенос данных между этими сервисами. Теперь Gemini Developer API и Gemini Platform API доступны через единый [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ru) и [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru).

## Сравнение кода: API взаимодействий (рекомендуется)

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru) – это рекомендуемый способ создания приложений с использованием моделей и агентов Gemini. В приведенных ниже примерах сравнивается генерация текста с помощью Gemini Developer API и платформы Gemini.

### Python

Вы можете получить доступ к Gemini Developer API и сервисам платформы Gemini через библиотеку `google-genai` (`>= 2.3.0`). Инструкции по установке `google-genai` приведены на странице [библиотек](https://ai.google.dev/gemini-api/docs/libraries?hl=ru).

### Gemini Developer API

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### Gemini platform API

```
from google import genai

client = genai.Client(
    enterprise=True, project="your-project-id", location="global"
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### JavaScript и TypeScript

Вы можете получить доступ к Gemini Developer API и сервисам платформы Gemini через библиотеку `@google/genai` (`>= 2.3.0`). Инструкции по установке `@google/genai` приведены на странице [библиотек](https://ai.google.dev/gemini-api/docs/libraries?hl=ru).

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### Gemini platform API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  enterprise: true,
  project: "your_project",
  location: "global",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

## Сравнение кода: API generateContent

Мы рекомендуем использовать Interactions API для новых проектов, но API `generateContent` по-прежнему поддерживается.

### Python

Вы можете получить доступ к Gemini Developer API и сервисам платформы Gemini с помощью библиотеки `google-genai`. Инструкции по установке `google-genai` приведены на странице [библиотек](https://ai.google.dev/gemini-api/docs/libraries?hl=ru).

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript и TypeScript

Вы можете получить доступ к Gemini Developer API и сервисам платформы Gemini с помощью библиотеки `@google/genai`. Инструкции по установке `@google/genai` приведены на странице [библиотек](https://ai.google.dev/gemini-api/docs/libraries?hl=ru).

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Проложить маршрут

Вы можете получить доступ к Gemini Developer API и сервисам платформы Gemini с помощью библиотеки `google.golang.org/genai`. Инструкции по установке `google.golang.org/genai` приведены на странице [библиотек](https://ai.google.dev/gemini-api/docs/libraries?hl=ru).

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google Cloud project
const project = "your-project"

// A Google Cloud location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Другие варианты использования и платформы

Информацию о других платформах и примерах использования можно найти в [документации по Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=ru) и [документации по платформе Gemini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ru).

## Что нужно учитывать при переносе

При переносе:

- Для аутентификации необходимо использовать сервисные аккаунты Google Cloud. Дополнительную информацию можно найти в [документации по платформе Gemini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ru).
- Вы можете использовать существующий облачный проект Google Cloud (тот же, который вы использовали для создания ключа API) или [создать новый облачный проект Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ru).
- Поддерживаемые регионы могут различаться для Gemini Developer API и Gemini Platform API. В предварительной версии [Interactions API на платформе Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=ru) поддерживается только конечная точка `global` (`location="global"`). Ознакомьтесь со списком [поддерживаемых регионов для генеративного искусственного интеллекта в Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=ru).
- Все модели, созданные в Google AI Studio, необходимо переобучить на платформе Gemini.

Если вам больше не нужен ключ Gemini API для Gemini Developer API, удалите его в соответствии с рекомендациями по обеспечению безопасности.

Чтобы удалить ключ API, выполните следующие действия:

1. Откройте страницу [Google Cloud API Credentials (Учетные данные API Google Cloud)](https://console.cloud.google.com/apis/credentials?hl=ru).
2. Найдите ключ API, который хотите удалить, и нажмите на значок **Действия**.
3. Выберите **Удалить ключ API**.
4. В модальном окне **Delete credential (Удаление учетных данных)** выберите **Delete (Удалить)**.

   После удаления ключа API может пройти несколько минут, прежде чем изменение распространится в системе. Когда процесс завершится, трафик, использующий удаленный ключ API, будет отклоняться.

## Дальнейшие действия

- Изучите [руководство для разработчиков по Interactions API на платформе Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=ru).
- Подробнее [о решениях на основе генеративного искусственного интеллекта на платформе Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ru)…

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-08 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-08 UTC."],[],[]]
