---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=zh-TW
fetched_at: 2026-06-29T05:31:04.131253+00:00
title: "\u5efa\u69cb\u4ee3\u7ba1\u4ee3\u7406\u7a0b\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 建構代管代理程式

透過 Gemini API 中的受管理代理程式，您可以運用自己的指令、技能和資料擴充 Antigravity 代理程式。您可以在互動時[自訂代理程式內嵌](#customize-inline)，或[將設定儲存](#save-agent)為您透過 ID 叫用的受管理代理程式。

## 自訂 Antigravity 代理程式

如要快速建構自訂代理程式，最簡單的方式就是在建立新互動時，直接傳遞設定，不需要註冊步驟。您可以透過三種方式擴充代理程式：

- **系統指令**：透過 `system_instruction` 傳遞內嵌文字，以塑造行為。
- **工具**：覆寫預設工具 (程式碼執行、搜尋、網址內容)、註冊遠端 MCP 伺服器，或定義自訂函式 (函式呼叫)。
- **檔案和技能**：將 `AGENTS.md` 和 `SKILL.md` 等檔案掛載到環境中。

以下是內嵌傳遞所有三個項目的範例：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a slide deck.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",        
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the Q1 revenue data and create a slide deck.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",        
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the Q1 revenue data and create a slide deck.",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            }
        ]
    }
}'
```

所有項目都是在互動時定義。不必事先註冊任何項目，Antigravity 代理程式安全帶提供執行階段 (程式碼執行、檔案管理、網路存取)，以及頂層的設定層。

### 工具和系統指令

您可以使用 `system_instruction` 和 `tools` 參數，自訂特定互動的代理程式行為和功能。

- **系統指令**：使用 `system_instruction` 參數傳遞內嵌文字，以塑造代理程式的行為。非常適合在每次通話時快速調整設定。《`system_instruction`》和《`AGENTS.md`》是加成效果，如果兩者都存在，則會同時套用。
- **工具**：根據預設，Antigravity 代理程式可存取 `code_execution`、`google_search` 和 `url_context`。您可以在互動時傳遞 `tools` 參數，覆寫這份清單。您也可以註冊[遠端 MCP 伺服器](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw#mcp-servers)，或定義[自訂函式 (函式呼叫)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw#function-calling)，將代理程式連結至您自己的 API 和資料庫。如要瞭解可用的完整工具，請參閱「[Antigravity Agent：支援的工具](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw#supported-tools)」。

### 以檔案為基礎的自訂

#### 代理程式目錄結構

雖然您可以內嵌傳遞設定，但我們建議您在結構化目錄中整理代理程式的檔案。方便管理、版本管控，以及掛接到代理程式環境。

典型的代理程式專案目錄如下所示：

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Antigravity 執行階段會掃描 `.agents/` (和環境的根目錄) 是否有這些檔案。

#### AGENTS.md

代理程式會在啟動時，從環境中自動載入 `.agents/AGENTS.md` (或 `/.agents/AGENTS.md`) 做為系統指令。使用 `AGENTS.md` 進行長篇角色定義、詳細規範和說明，並與程式碼一起進行版本管控。

使用內嵌來源掛接 `AGENTS.md`：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a report.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the Q1 revenue data and create a report.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Analyze the Q1 revenue data and create a report.",
      "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/AGENTS.md",
                  "content": "Always use matplotlib for charts. Include a summary table in every report."
              }
          ]
      }
  }'
```

#### 技能：SKILL.md

技能是擴充代理功能的檔案。將它們放在 `.agents/skills/<skill-name>/SKILL.md` 下方，安全帶就會自動探索並註冊。

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

使用內嵌來源掛接技能：

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Create a presentation about our Q1 results.",
    system_instruction="You create presentations from data.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Create a presentation about our Q1 results.",
    system_instruction: "You create presentations from data.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Create a presentation about our Q1 results.",
      "system_instruction": "You create presentations from data.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/skills/slide-maker/SKILL.md",
                  "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html"
              }
          ]
      }
  }'
```

系統會自動探索從 `.agents/skills/` 和 `/.agents/skills/` 載入的技能。

## 建立代管代理程式

完成設定的疊代作業後，您可以使用 `agents.create` 將設定建立為受管理代理程式。這樣一來，您就能透過 ID 叫用代理程式，不必每次都重複設定。

### 來自來源

使用來源指定 `base_agent`、`id`、`system_instruction` 和 `base_environment`。平台會在每次叫用時，使用您的檔案佈建新的沙箱。如要瞭解可用的來源類型 (Git、GCS、內嵌)，請參閱「[環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw)」。

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates",
            },
        ],
    },
)

print(f"Created agent: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "data-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                type: "repository",
                source: "https://github.com/my-org/analysis-templates",
                target: "/workspace/templates",
            },
        ],
    },
});

console.log(`Created agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates"
            }
        ]
    }
}'
```

### 從現有環境 (分叉)

使用基礎 Antigravity 代理程式進行疊代，直到環境正確為止 (已安裝套件、檔案就位)，然後將其分叉到受管理代理程式。

### Python

```
from google import genai

client = genai.Client()

# Step 1: set up the environment interactively
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment="remote",
)

# Step 2: fork that environment into a managed agent

agent = client.agents.create(
    id="my-data-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment=interaction.environment_id,
)

print(f"Forked agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment: "remote",
}, { timeout: 300000 });

const agent = await client.agents.create({
    id: "my-data-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment: interaction.environment_id,
});

console.log(`Forked agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### 使用網路規則

儲存受管理代理程式時，您可以鎖定輸出存取權或插入憑證。如需完整的許可清單結構定義、憑證模式和萬用字元，請參閱「[環境：網路設定](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#network-configuration)」。

以下範例會建立只能存取 GitHub 和 PyPI 的 `issue-resolver` 代理程式，並為 GitHub 插入憑證：

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="issue-resolver",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/my-org/backend",
                "target": "/workspace/repo",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(f"Created issue-resolver agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "issue-resolver",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/my-org/backend",
                target: "/workspace/repo",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        }
    },
});

console.log(`Created issue-resolver agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "id": "issue-resolver",
      "base_agent": "antigravity-preview-05-2026",
      "system_instruction": "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
      "base_environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "repository",
                  "source": "https://github.com/my-org/backend",
                  "target": "/workspace/repo"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Basic YOUR_BASE64_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## 叫用代理程式

建立新的互動，並使用代理程式 ID 呼叫受管理代理程式。每次叫用都會分叉基本環境，因此每次執行都會從乾淨的狀態開始。

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

如要瞭解多輪對話和串流，請參閱[快速入門導覽課程](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-tw)。受管理代理程式也適用相同的 `previous_interaction_id` 和 `environment` 模式。

代管代理程式也支援背景執行和取消作業。如需詳細資料和程式碼範例，請參閱「[Antigravity Agent：背景執行](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw#background-execution)」。

## 在叫用時覆寫設定

建立互動時，您可以覆寫代理程式的預設 `system_instruction` 和 `tools`。這樣一來，您就能在特定執行作業中修改代理程式的行為或功能，而不必變更儲存的代理程式定義。

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction="You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools=[{"type": "code_execution"}], # Override to only use code execution
    environment="remote",
)
print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction: "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools: [{ type: "code_execution" }], // Override to only use code execution
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

## 管理代理

您可以列出、取得及刪除代理程式。

### 列出代理程式

### Python

```
agents = client.agents.list()
for a in agents.agents:
    print(f"{a.id}: {a.description}")
```

### JavaScript

```
const agents = await client.agents.list();
if (agents.agents) {
    for (const a of agents.agents) {
        console.log(`${a.id}: ${a.description}`);
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 取得代理程式

### Python

```
agent = client.agents.get(id="data-analyst")
print(agent)
```

### JavaScript

```
const agent = await client.agents.get("data-analyst");
console.log(agent);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 刪除代理程式

刪除後，系統會移除設定。代理程式建立的現有環境和互動不會受到影響。

### Python

```
client.agents.delete(id="data-analyst")
```

### JavaScript

```
await client.agents.delete("data-analyst");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 代理定義參考資料

| 欄位 | 類型 | 必要 | 說明 |
| --- | --- | --- | --- |
| `id` | 字串 | 是 | 專屬代理程式 ID。用於呼叫代理程式。 |
| `description` | 字串 | 否 | 人類可讀的代理說明。 |
| `base_agent` | 字串 | 是 | 基本代理 ID (例如 `antigravity-preview-05-2026`)。 |
| `system_instruction` | 字串 | 否 | 定義行為和角色的系統提示。 |
| `tools` | 陣列 | 否 | 代理可用的工具。如果省略此屬性，系統會預設為 `code_execution`、`google_search` 和 `url_context`。支援的工具包括 `code_execution`、`google_search`、`url_context`、`mcp_server` 和自訂 `function` 定義。 |
| `base_environment` | 字串或物件 | 否 | `"remote"`、`environment_id`，或是包含 `sources` 和 `network` 的設定物件。請參閱「環境」。 |

## 疊代工作流程

1. 使用基礎 Antigravity 代理**原型**。內嵌傳遞系統指令和環境來源。以互動方式測試指令、技能和環境設定。
2. **穩定**環境。安裝套件、掛接來源，並確認一切正常運作。
3. 建立新代理程式 (可從來源建立，或透過分叉環境建立)，以**保留**為受管理代理程式。
4. **更新**代理程式定義。變更系統指令、更換技能或新增來源。下次叫用時，系統就會採用新設定。

## 限制

- **預覽狀態**：受管理代理程式目前為預覽版。功能和結構定義可能會有所異動。
- **基礎代理程式**：僅支援 `antigravity-preview-05-2026` 做為 `base_agent`。
- **不支援版本管理**：目前不支援代理程式版本管理和復原。
- **不支援子代理巢狀結構**：目前不支援子代理委派。
- 最多可有 1000 個受管理代理程式。

## 後續步驟

- [代理程式總覽](https://ai.google.dev/gemini-api/docs/agents?hl=zh-tw)：瞭解受管理代理程式的核心概念。
- [快速入門導覽課程](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=zh-tw)：開始建構多輪對話和串流。
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw)：瞭解預設代理的功能、工具和價格。
- [代理程式環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw)：設定沙箱、來源和網路。
- [Agent Platform 的 Managed Agents API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=zh-tw)：用於建立內建機構治理功能的代理。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-26 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-26 (世界標準時間)。"],[],[]]
