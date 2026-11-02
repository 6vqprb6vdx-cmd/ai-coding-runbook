---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru
fetched_at: 2026-11-02T07:19:52.370590+00:00
title: "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0430\u0433\u0435\u043d\u0442\u0430 \u0434\u043b\u044f \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043a\u043e\u0434\u0430 \u0438 \u0440\u0435\u0441\u0443\u0440\u0441\u044b \u0434\u043b\u044f \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u043e\u0432 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Настройка агента для написания кода и ресурсы для разработчиков

ИИ-агенты для программирования используют данные для обучения, которые ограничены определенной датой. Поэтому агенты часто предлагают устаревшие модели (`gemini-1.5`), старые SDK (`google-generativeai`) или устаревшие шаблоны кода.

Подключив агента к официальным ресурсам для разработчиков Gemini, вы поможете ему писать точный код с использованием текущих моделей, `google-genai` SDK и [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru).

Подключить агента к документации, правилам и инструментам CLI Gemini можно пятью способами:

## Сводка ресурсов агента

| Ресурс | Что он дает | Доступность |
| --- | --- | --- |
| **[Навыки агента Gemini](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru#available-skills)** | Пошаговые инструкции, шаблоны SDK и вспомогательные скрипты для определенных функций (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`). | Предустановлен в [AI Studio Build](https://ai.studio/build). Установите с помощью `skills.sh`, Context7 или Managed Agents. |
| **[Gemini Docs MCP Server](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru#mcp-setup)** | Поиск в реальном времени (`gemini_search_docs`) и чтение всей страницы (`gemini_get_doc`) во всей документации. | Поддерживается в Claude Code, Cursor, OpenAI Codex и VS Code. |
| **[Плагин Gemini API](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru#gemini-api-plugin)** | Пакет с официальными навыками Gemini, MCP-сервером Документов и инструментами для ключей API. | Antigravity. |
| **[Документы, предназначенные для компьютеров](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru#machine-readable-docs)** | Очистите страницы Markdown и индексы `llms.txt`. | Все страницы документации на сайте `ai.google.dev/gemini-api/docs`. |
| **[Gemini API CLI](https://ai.google.dev/gemini-api/docs/cli?hl=ru)** | Интерфейс командной строки без сохранения состояния (`gemini-api`) для генерации медиаконтента, анализа файлов и запуска управляемых агентов из оболочки без написания кода SDK. | Установите на macOS, Linux или Windows с помощью скрипта установки, Go или готовых двоичных файлов. |

## Установите навыки агента Gemini

Навыки агента предоставляют вашему агенту программирования процедурные правила, текущие названия моделей и шаблоны кода SDK. Вместо того чтобы добавлять длинные инструкции в запрос, агент загружает каждый навык только по мере необходимости. Это поможет агенту избегать устаревших SDK и использовать современные шаблоны Gemini.

Навыки работают вместе с MCP-сервером Gemini для Документов. Если на вашем агенте не установлен сервер MCP, навык возвращается к [`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=ru). Подробнее о том, как работают навыки, рассказывается в [руководстве по навыкам Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=ru).

### Установка с помощью CLI (`skills.sh` или Context7)

Установите навыки с помощью [skills.sh](https://skills.sh) (рекомендуется) или [Context7](https://context7.com).

```
# List all available skills in the repository
npx skills add google-gemini/gemini-skills --list

# Install a specific skill globally with skills.sh
npx skills add google-gemini/gemini-skills --skill <skill-name> --global

# Or install with Context7
npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
```

### Доступные навыки

#### `gemini-api-dev`

Навык создания приложений с помощью [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru) и официальных SDK Gemini API (`google-genai` для Python и `@google/genai` для TypeScript). Этот навык
включает:

- Генерация текста, многоэтапный чат, потоковая передача, структурированные выходные данные и вызов функций.
- Генерация изображений, преобразование текста в речь и мультимодальные запросы
- Управление состоянием чата на стороне сервера, выполнение в фоновом режиме, Deep Research и управляемые агенты
- Названия текущих моделей и перенос устаревшего кода `generateContent` или `google-generativeai`

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### `gemini-live-api-dev`

Навык создания приложений для потоковой передачи аудио и видео в реальном времени с помощью [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ru). Этот навык включает:

- Управление сеансами WebSocket, временные токены клиентов и возобновление сеансов.
- Потоковая передача аудио, видео и текста с поддержкой обнаружения голосовой активности и прерывания.
- Рассуждения в фоновом режиме (расширенное мышление), неблокирующие асинхронные вызовы инструментов, расшифровка и перевод устной речи в реальном времени.

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### `gemini-omni-flash-api`

Навык для создания и редактирования видео с помощью Gemini Omni Flash и Interactions API. Включает вспомогательные скрипты (`upload_file.py`, `generate_video.py`, `prep_video.py`, `inspect_video.py`) и охватывает:

- Генерация видео по тексту и составление запросов
- Переходы между первым и последним кадрами и создание видео на основе референса
- Расширения для видео и рабочие процессы предварительной обработки медиаконтента

```
npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
```

### Как подключить навыки в управляемых агентах

При запуске удаленных управляемых агентов с помощью Interactions API вы можете подключить хранилище `google-gemini/gemini-skills` к рабочей области агента. Подробную информацию вы найдете в [руководстве по навыкам Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=ru).

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build a script that generates a 5-second video of a neon cityscape.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/google-gemini/gemini-skills",
                "target": ".agents",
            }
        ],
    },
)
```

## Подключите MCP-сервер Gemini Docs

Общедоступный **MCP-сервер Gemini Docs** (`https://gemini-api-docs-mcp.dev`) предоставляет агенту доступ ко всему сайту с документацией в реальном времени. Агент может искать и читать страницы документации, чтобы проверять схемы запросов, ограничения моделей и новые функции.

- `gemini_search_docs` – поиск по теме или запросу в документации Gemini API.
- `gemini_get_doc`: читает весь контент Markdown на определенной странице документации.

### Быстрая настройка

Чтобы автоматически настроить обнаруженных агентов программирования, выполните в терминале или корневом каталоге проекта следующую команду:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

### Конфигурация по среде

### Claude Code

Выполните в терминале следующую команду:

```
$ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
```

### Курсор

Добавьте в `~/.cursor/mcp.json` (глобальный) или `.cursor/mcp.json` (проект):

```
{
  "mcpServers": {
    "geminiDocs": {
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

### OpenAI Codex

Выполните в терминале следующую команду:

```
$ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
```

Или добавьте в `~/.codex/config.toml`:

```
[mcp_servers.geminiDocs]
url = "https://gemini-api-docs-mcp.dev"
```

### VS Code (Copilot)

Добавьте в `.vscode/mcp.json` в рабочей области:

```
{
  "servers": {
    "geminiDocs": {
      "type": "http",
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

## Плагин Gemini API

Если вы используете **Antigravity**, **плагин Gemini API** – это самый быстрый способ настроить рабочую область. Он включает MCP-сервер Gemini Docs, все официальные навыки Gemini (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) и инструменты для работы с ключами API в одном скачиваемом пакете.

- **Установка в Antigravity (UI).** Перейдите в **Settings (Настройки) > Customizations (Настройки) > Build with Google Plugins (Плагины Build with Google)** и скачайте **Gemini API**.
- **Установите с помощью CLI:**
  `bash
  agy plugin install https://github.com/google-gemini/gemini-skills`

## Машиночитаемая документация

Стандартные веб-страницы содержат HTML-теги, панели навигации и скрипты, которые занимают место в окне контекста. `ai.google.dev` предоставляет машиночитаемые конечные точки, чтобы агенты и скрипты могли получать чистый Markdown напрямую:

- **Индекс `llms.txt`** ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=ru)). Список всех страниц документации Gemini API со ссылками на каждую из них.
- **Прямые URL Markdown (`.md.txt`).** Добавьте `.md.txt` к любому URL документации на сайте `ai.google.dev` (например, [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt?hl=ru)), чтобы получить чистый исходный код Markdown для сохраненных запросов, правил `AGENTS.md` или автоматизированных скриптов.

## Рекомендуемые правила проекта (`AGENTS.md`)

Файл правил проекта (`AGENTS.md`, `.cursorrules` или `CLAUDE.md`) задает базовые правила, которые загружаются в начале каждого сеанса агента. Добавьте эти рекомендации в корень проекта, чтобы агенты программирования по умолчанию использовали текущие модели и SDK:

```
# Gemini API Guidelines

- Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
- Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
- Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
- Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
```

## Проверка и устранение неполадок

### Проверка правильности настроек

Чтобы проверить настройки, спросите у агента программирования:

```
Look up the request schema for the Gemini Interactions API in the documentation.
```

Настроенный агент будет использовать `gemini_search_docs` на сервере MCP `geminiDocs` и писать код с помощью `client.interactions.create` и SDK `google-genai` или `@google/genai`.

### Команды статуса

| Среда | Проверка MCP | Проверка навыков |
| --- | --- | --- |
| **Claude Code** | Запуск по расписанию: `/mcp` | Запуск по расписанию: `/skills` |
| **Курсор** | Откройте **Settings > Features > MCP (Настройки > Функции > MCP)**. | Откройте **Настройки > Правила**. |
| **OpenAI Codex** | Запуск по расписанию: `codex mcp list` | Проверьте `.codex/skills/` или `~/.codex/skills/` |
| **Antigravity** | Выберите **Customizations (Настройки) > Connections (Подключения)**. | Откройте **Customizations (Настройки) > Rules (Правила)** или выполните команду `/skills list`. |
| **VS Code (Copilot)** | Откройте **Расширения > MCP** или панель вывода. | В Copilot Chat нажмите **Select Tools (Выбрать инструменты)**. |

### Устранение неполадок

- **Навык или MCP-сервер не обнаружен.** Перезапустите редактор (Cursor или VS Code) или сеанс терминала (Claude Code или Codex). Большинство агентов загружают MCP-серверы и навыки только при запуске.
- **Конфликт с глобально установленным навыком.** Если агент игнорирует глобально установленный навык, установите его в корневой папке проекта без `--global`:
  `bash
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
- **Правила игнорируются.** Убедитесь, что файл `AGENTS.md`, `.cursorrules` или `CLAUDE.md` находится в корневом каталоге проекта.

## Дальнейшие действия

- [Gemini API CLI](https://ai.google.dev/gemini-api/docs/cli?hl=ru)
- [Руководство по навыкам Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=ru)
- [Навыки Gemini API на GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru)
- [Доступные модели](https://ai.google.dev/gemini-api/docs/models?hl=ru)
- [Библиотеки и SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ru)

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-28 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-28 UTC."],[],[]]
