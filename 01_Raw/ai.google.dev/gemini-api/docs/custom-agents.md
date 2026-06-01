---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko
fetched_at: 2026-06-01T19:46:54.686381+00:00
title: "\uad00\ub9ac \uc5d0\uc774\uc804\ud2b8 \ube4c\ub4dc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 관리 에이전트 빌드

Gemini API의 관리형 에이전트를 사용하면 자체 요청 사항, 기술, 데이터로 Antigravity 에이전트를 확장할 수 있습니다. 상호작용 시점에 에이전트를 [인라인으로 맞춤설정](#customize-inline)하거나 구성을 [ID로 호출하는 관리형 에이전트로 저장](#save-agent)할 수 있습니다.

## Antigravity 에이전트 맞춤설정

맞춤 에이전트를 빌드하는 가장 빠른 방법은 등록 단계 없이 새 상호작용을 만드는 동안 구성을 인라인으로 전달하는 것입니다. 다음 세 가지 방법으로 에이전트를 확장할 수 있습니다.

- **시스템 요청 사항**: 인라인 텍스트를 `system_instruction`을 통해 전달하여 동작을 형성합니다.
- **도구**: 기본 도구 (코드 실행, 검색, URL 컨텍스트)를 재정의합니다.
- **파일 및 기술**: `AGENTS.md` 및 `SKILL.md`와 같은 파일을 환경에 마운트합니다.

다음은 세 가지 모두를 인라인으로 전달하는 예입니다.

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
-H "Api-Revision: 2026-05-20" \
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

모든 항목은 상호작용 시점에 정의됩니다. 먼저 등록할 필요가 없습니다. Antigravity 에이전트 하네스는 런타임 (코드 실행, 파일 관리, 웹 액세스)과 구성 레이어를 제공합니다.

### 도구 및 시스템 요청 사항

`system_instruction` 및 `tools` 매개변수를 사용하여 특정 상호작용에 맞게 에이전트의 동작과 기능을 맞춤설정할 수 있습니다.

- **시스템 요청 사항**: `system_instruction` 매개변수를 사용하여 에이전트의 동작을 형성하는 인라인 텍스트를 전달합니다. 이는 호출당 변경하려는 빠른 조정을 위해 이상적입니다. `system_instruction` 및 `AGENTS.md`는 추가적입니다. 둘 다 있는 경우 적용됩니다.
- **도구**: 기본적으로 Antigravity 에이전트는 `code_execution`, `google_search`, `url_context`에 액세스할 수 있습니다. 상호작용 시점에 `tools` 매개변수를 전달하여 이 목록을 재정의할 수 있습니다. 사용 가능한 도구 및 사용 방법에 관한 자세한 내용은 [Antigravity 에이전트: 지원되는 도구](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko#supported-tools)를 참고하세요.

### 파일 기반 맞춤설정

#### 에이전트 디렉터리 구조

구성을 인라인으로 전달할 수 있지만 구조화된 디렉터리에 에이전트의 파일을 구성하는 것이 좋습니다. 이렇게 하면 에이전트의 환경에서 더 쉽게 관리하고, 버전 제어하고, 마운트할 수 있습니다.

일반적인 에이전트 프로젝트 디렉터리는 다음과 같습니다.

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Antigravity 런타임은 이러한 파일에 대해 `.agents/` (및 환경의 루트)를 검사합니다.

#### AGENTS.md

에이전트는 시작 시 환경에서 `.agents/AGENTS.md` (또는 `/.agents/AGENTS.md`)를 시스템 요청 사항으로 자동 로드합니다. 코드와 함께 버전 제어하려는 긴 형식의 페르소나 정의, 자세한 가이드라인, 요청 사항에 `AGENTS.md`를 사용합니다.

인라인 소스를 사용하여 `AGENTS.md`를 마운트합니다.

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
  -H "Api-Revision: 2026-05-20" \
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

#### 기술: SKILL.md

기술은 에이전트의 기능을 확장하는 파일입니다. `.agents/skills/<skill-name>/SKILL.md` 아래에 배치하면 하네스가 자동으로 검색하고 등록합니다.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

인라인 소스를 사용하여 기능을 마운트합니다.

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
  -H "Api-Revision: 2026-05-20" \
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

`.agents/skills/` 및 `/.agents/skills/`에서 로드된 기술은 모두 자동으로 검색됩니다.

## 관리형 에이전트 만들기

구성을 반복한 후 `agents.create`를 사용하여 관리형 에이전트로 만들 수 있습니다. 이렇게 하면 매번 구성을 반복하지 않고도 ID로 에이전트를 호출할 수 있습니다.

### 소스에서

소스와 함께 `base_agent`, `id`, `system_instruction`, `base_environment`를 지정합니다. 플랫폼은 호출할 때마다 파일이 포함된 새로운 샌드박스를 프로비저닝합니다. 사용 가능한 소스 유형 (Git, GCS, 인라인)은 [환경](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko)을 참고하세요.

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
-H "Api-Revision: 2026-05-20" \
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

### 기존 환경에서 (포크)

환경이 올바를 때까지 (패키지 설치, 파일 배치) 기본 Antigravity 에이전트를 반복한 다음 관리형 에이전트로 포크합니다.

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### 네트워크 규칙 사용

관리형 에이전트를 저장할 때 아웃바운드 액세스를 잠그거나 사용자 인증 정보를 삽입할 수 있습니다. 허용 목록 스키마, 사용자 인증 정보 패턴, 와일드카드에 관한 자세한 내용은 [환경: 네트워크 구성](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#network-configuration)을 참고하세요.

다음 예에서는 GitHub에 사용자 인증 정보가 삽입된 상태로 GitHub 및 PyPI에만 액세스할 수 있는 `issue-resolver` 에이전트를 만듭니다.

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
  -H "Api-Revision: 2026-05-20" \
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

## 에이전트 호출

새 상호작용을 만들어 에이전트 ID로 관리형 에이전트를 호출합니다. 각 호출은 기본 환경을 포크하므로 모든 실행이 깨끗하게 시작됩니다.

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

다중 턴 대화 및 스트리밍은 [빠른 시작](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko)을 참고하세요. 동일한 `previous_interaction_id` 및 `environment` 패턴이 관리형 에이전트에 적용됩니다.

## 호출 시 구성 재정의

상호작용을 만들 때 에이전트의 기본 `system_instruction` 및 `tools`를 재정의할 수 있습니다. 이렇게 하면 저장된 에이전트 정의를 변경하지 않고도 특정 실행에 맞게 에이전트의 동작 또는 기능을 수정할 수 있습니다.

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

## 에이전트 관리

에이전트를 나열, 가져오기, 삭제할 수 있습니다.

### 에이전트 나열

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

### 에이전트 가져오기

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

### 에이전트 삭제

삭제하면 구성이 삭제됩니다. 에이전트가 만든 기존 환경과 상호작용은 영향을 받지 않습니다.

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

## 에이전트 정의 참조

| 필드 | 유형 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | 문자열 | 예 | 고유 에이전트 식별자입니다. 에이전트를 호출하는 데 사용됩니다. |
| `description` | 문자열 | 아니요 | 인간이 읽을 수 있는 에이전트 설명입니다. |
| `base_agent` | 문자열 | 예 | 기본 에이전트 ID (예: `antigravity-preview-05-2026`). |
| `system_instruction` | 문자열 | 아니요 | 동작과 페르소나를 정의하는 시스템 프롬프트입니다. |
| `tools` | 문자열 또는 객체 | 아니요 | 에이전트가 사용할 수 있는 도구입니다. 생략하면 `code_execution`, `google_search`, `url_context`에 액세스할 수 있습니다. |
| `base_environment` | 문자열 또는 객체 | 아니요 | `"remote"`, `environment_id` 또는 `sources` 및 `network`가 포함된 구성 객체입니다. 환경을 참고하세요. |

## 반복 워크플로

1. 기본 Antigravity 에이전트로 **프로토타입** 을 만듭니다. 시스템 요청 사항 및 환경 소스를 인라인으로 전달합니다. 요청 사항, 기술, 환경 설정을 대화형으로 테스트합니다.
2. 환경을 **안정화** 합니다. 패키지를 설치하고, 소스를 마운트하고, 모든 항목이 작동하는지 확인합니다.
3. 소스를 사용하거나 환경을 포크하여 새 에이전트를 만들어 관리형 에이전트로 **유지** 합니다.
4. 에이전트 정의를 **업데이트** 합니다. 시스템 요청 사항을 변경하거나, 기술을 교체하거나, 소스를 추가합니다. 다음 호출은 새 구성을 선택합니다.

## 제한사항

- **미리보기 상태**: 관리형 에이전트는 미리보기 상태입니다. 기능과 스키마는 변경될 수 있습니다.
- **기본 에이전트**: `antigravity-preview-05-2026`만 `base_agent`로 지원됩니다.
- **버전 관리 없음**: 에이전트 버전 관리 및 롤백은 아직 사용할 수 없습니다.
- **하위 에이전트 중첩 없음**: 하위 에이전트 위임은 아직 지원되지 않습니다.
- 관리형 에이전트는 최대 1,000개까지 사용할 수 있습니다.

## 다음 단계

- [에이전트 개요](https://ai.google.dev/gemini-api/docs/agents?hl=ko): 관리형 에이전트의 핵심 개념에 대해 알아봅니다.
- [빠른 시작](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ko): 다중 턴 대화 및 스트리밍으로 빌드를 시작합니다.
- [Antigravity 에이전트](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko): 기본 에이전트의 기능, 도구, 가격 책정을 살펴봅니다.
- [에이전트 환경](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko): 샌드박스, 소스, 네트워킹을 구성합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-06-01(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-06-01(UTC)"],[],[]]
