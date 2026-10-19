---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=ru
fetched_at: 2026-10-19T05:30:36.082045+00:00
title: "\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Библиотеки Gemini API

При работе с Gemini API мы рекомендуем использовать **Google GenAI SDK**.
Это официальные готовые к использованию библиотеки, которые мы разрабатываем и поддерживаем для самых популярных языков. Они находятся в [общей доступности](https://ai.google.dev/gemini-api/docs/libraries?hl=ru#new-libraries) и используются во всей нашей официальной документации и примерах.

Если вы ещё не работали с Gemini API, ознакомьтесь с [руководством по началу работы](https://ai.google.dev/gemini-api/docs/get-started?hl=ru).

## Поддержка языков и установка

Google GenAI SDK доступен для языков Python, JavaScript/TypeScript, Go и Java. Вы можете установить библиотеку для каждого языка с помощью менеджеров пакетов или посетить их репозитории GitHub для дальнейшего взаимодействия:

### Python

- Библиотека: [`google-genai`](https://pypi.org/project/google-genai)
- Репозиторий GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Установка: `pip install google-genai`

### JavaScript

- Библиотека: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- Репозиторий GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Установка: `npm install @google/genai`

### Проложить маршрут

- Библиотека: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- Репозиторий GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Установка: `go get google.golang.org/genai`

### Java

- Библиотека: `google-genai`
- Репозиторий GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Установка. Если вы используете Maven, добавьте в зависимости следующее:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Библиотека: `Google.GenAI`
- Репозиторий GitHub: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Установка: `dotnet add package Google.GenAI`

## Общая доступность

С мая 2025 г. Google GenAI SDK достигли общей доступности (GA) на всех поддерживаемых платформах и являются рекомендуемыми библиотеками для доступа к Gemini API.
Они стабильны, полностью поддерживаются для использования в рабочей среде и активно обслуживаются.
Они обеспечивают доступ к новейшим функциям и оптимальную производительность при работе с Gemini.

Если вы используете одну из наших устаревших библиотек, настоятельно рекомендуем перейти на новую, чтобы получить доступ к последним функциям и обеспечить наилучшую производительность при работе с Gemini. Подробнее [о библиотеках устаревшей версии](https://ai.google.dev/gemini-api/docs/libraries?hl=ru#previous-sdks)…

## Устаревшие библиотеки и перенос данных

Если вы используете одну из устаревших библиотек, рекомендуем [перейти на новые](https://ai.google.dev/gemini-api/docs/migrate?hl=ru).

Устаревшие библиотеки не предоставляют доступ к новым функциям, таким как [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ru) и [Veo](https://ai.google.dev/gemini-api/docs/video?hl=ru), и будут отключены 30 ноября 2025 года.

Статус поддержки каждой устаревшей библиотеки различается, как описано в следующей таблице:

| Язык | Устаревшая библиотека | Статус поддержки | Рекомендуемая библиотека |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Не поддерживается | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Не поддерживается | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | Не поддерживается | `google.golang.org/genai` |
| **Dart и Flutter** | `google_generative_ai` | Не поддерживается | Используйте [Genkit Dart](https://genkit.dev/docs/dart/get-started/) или [Firebase AI Logic](https://pub.dev/packages/firebase_ai). |
| **Swift** | `generative-ai-swift` | Не поддерживается активно | Используйте [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=ru) |
| **Android** | `generative-ai-android` | Не поддерживается активно | Используйте [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=ru) |

**Примечание для разработчиков на Java.** Устаревшего Java SDK для Gemini API, предоставленного Google, не было, поэтому переходить с предыдущей библиотеки Google не требуется. Вы можете сразу перейти к новой библиотеке в разделе [Поддержка языков и установка](https://ai.google.dev/gemini-api/docs/libraries?hl=ru#install).

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-15 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-15 UTC."],[],[]]
