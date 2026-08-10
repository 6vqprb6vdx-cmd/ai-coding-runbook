---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=hi
fetched_at: 2026-08-10T03:10:14.145931+00:00
title: "\u092e\u0948\u0928\u0947\u091c \u0915\u093f\u090f \u0917\u090f \u090f\u091c\u0947\u0902\u091f \u092c\u0928\u093e\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# मैनेज किए गए एजेंट बनाना

Gemini API से एजेंट बनाने और मैनेज करने की सुविधा की मदद से, Antigravity एजेंट को अपने निर्देशों, कौशल, और डेटा के साथ बढ़ाया जा सकता है. आपके पास इंटरैक्शन के दौरान, [एजेंट को इनलाइन तरीके से पसंद के मुताबिक बनाने](#customize-inline) का विकल्प होता है. इसके अलावा, [कॉन्फ़िगरेशन को सेव](#save-agent) करके, मैनेज किए गए एजेंट के तौर पर भी इस्तेमाल किया जा सकता है. इसके लिए, आपको आईडी का इस्तेमाल करना होगा.

## Antigravity एजेंट को पसंद के मुताबिक बनाना

कस्टम एजेंट बनाने का सबसे तेज़ तरीका यह है कि आप कॉन्फ़िगरेशन को इनलाइन पास करें. इसके लिए, आपको रजिस्ट्रेशन करने की ज़रूरत नहीं है. एजेंट को कई मुख्य तरीकों से बढ़ाया जा सकता है:

- **[मॉडल चुनना](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi#model-selection)**: `agent_config` की मदद से, Gemini का कोई मॉडल चुनें. डिफ़ॉल्ट रूप से, **Gemini 3.6 Flash** मॉडल चुना जाता है.
- **सिस्टम के निर्देश**: `system_instruction` के ज़रिए, इनलाइन टेक्स्ट को शेप के व्यवहार में पास करें.
- **टूल**: डिफ़ॉल्ट टूल (कोड एक्ज़ीक्यूशन, खोज, यूआरएल कॉन्टेक्स्ट) को बदलें, रिमोट एमसीपी सर्वर रजिस्टर करें या कस्टम फ़ंक्शन (फ़ंक्शन कॉलिंग) तय करें.
- **फ़ाइलें और स्किल**: `AGENTS.md` और `SKILL.md` जैसी फ़ाइलों को एनवायरमेंट में माउंट करें.

यहां तीनों को इनलाइन पास करने का उदाहरण दिया गया है:

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

इंटरैक्शन के समय ही सब कुछ तय किया जाता है. इसके लिए, आपको पहले कुछ भी रजिस्टर करने की ज़रूरत नहीं है. Antigravity एजेंट का हार्नेस, रनटाइम (कोड एक्ज़ीक्यूशन, फ़ाइल मैनेजमेंट, वेब ऐक्सेस) और आपकी कॉन्फ़िगरेशन लेयर उपलब्ध कराता है.

### टूल और सिस्टम के निर्देश

`system_instruction` और `tools` पैरामीटर का इस्तेमाल करके, किसी खास इंटरैक्शन के लिए एजेंट के व्यवहार और क्षमताओं को अपनी पसंद के मुताबिक बनाया जा सकता है.

- **सिस्टम के निर्देश**: एजेंट के व्यवहार को तय करने वाले इनलाइन टेक्स्ट को पास करने के लिए, `system_instruction` पैरामीटर का इस्तेमाल करें. यह सुविधा, उन बदलावों के लिए सबसे सही है जिन्हें आपको हर कॉल के हिसाब से बदलना है. `system_instruction` और `AGENTS.md`, दोनों को एक साथ इस्तेमाल किया जा सकता है. अगर ये दोनों मौजूद हैं, तो दोनों लागू होंगी.
- **टूल**: डिफ़ॉल्ट रूप से, Antigravity एजेंट के पास `code_execution`, `google_search`, और `url_context` का ऐक्सेस होता है. इंटरैक्शन के समय `tools` पैरामीटर पास करके, इस सूची को बदला जा सकता है. अपने एपीआई और डेटाबेस से एजेंट को कनेक्ट करने के लिए, [रिमोट एमसीपी सर्वर](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi#mcp-servers) भी रजिस्टर किए जा सकते हैं. इसके अलावा, [कस्टम फ़ंक्शन (फ़ंक्शन कॉलिंग)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi#function-calling) भी तय किए जा सकते हैं. उपलब्ध टूल के बारे में पूरी जानकारी के लिए, [Antigravity Agent: काम करने वाले टूल](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi#supported-tools) लेख पढ़ें.

### फ़ाइल के आधार पर मनमुताबिक बनाने की सुविधा

#### एजेंट डायरेक्ट्री स्ट्रक्चर

कॉन्फ़िगरेशन को इनलाइन पास किया जा सकता है. हालांकि, हमारा सुझाव है कि आप अपने एजेंट की फ़ाइलों को व्यवस्थित डायरेक्ट्री में सेव करें. इससे, एजेंट के एनवायरमेंट में फ़ाइलों को मैनेज करना, वर्शन कंट्रोल करना, और माउंट करना आसान हो जाता है.

किसी एजेंट प्रोजेक्ट की डायरेक्ट्री आम तौर पर ऐसी दिखती है:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Antigravity रनटाइम, इन फ़ाइलों के लिए `.agents/` (और एनवायरमेंट का रूट) स्कैन करता है.

#### AGENTS.md

स्टार्टअप पर एजेंट, सिस्टम के निर्देशों के तौर पर एनवायरमेंट से `.agents/AGENTS.md` (या `/.agents/AGENTS.md`) को अपने-आप लोड करता है. `AGENTS.md` का इस्तेमाल, पर्सोना की लंबी परिभाषाओं, दिशा-निर्देशों, और उन निर्देशों के लिए करें जिन्हें आपको अपने कोड के साथ वर्शन कंट्रोल करना है.

इनलाइन सोर्स का इस्तेमाल करके `AGENTS.md` को माउंट करें:

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

#### स्किल: SKILL.md

स्किल ऐसी फ़ाइलें होती हैं जो एजेंट की क्षमताओं को बढ़ाती हैं. उन्हें `.agents/skills/<skill-name>/SKILL.md` के नीचे रखें. इसके बाद, हार्नेस उन्हें अपने-आप ढूंढ लेगा और रजिस्टर कर देगा.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

इनलाइन सोर्स का इस्तेमाल करके किसी स्किल को माउंट करने के लिए:

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

`.agents/skills/` और `/.agents/skills/` से लोड की गई दोनों तरह की स्किल अपने-आप दिख जाती हैं.

## मैनेज किया गया एजेंट बनाना

कॉन्फ़िगरेशन को दोहराने के बाद, इसे `agents.create` की मदद से मैनेज किए जाने वाले एजेंट के तौर पर बनाया जा सकता है. इससे, हर बार कॉन्फ़िगरेशन को दोहराए बिना, आईडी के ज़रिए एजेंट को शुरू किया जा सकता है.

मैनेज किया जा रहा एजेंट बनाते समय, आपको एक `id` तय करना होता है.यह `id` आपके प्रोजेक्ट के लिए यूनीक होना चाहिए. साथ ही, यह रिज़र्व किए गए प्रीफ़िक्स (जैसे, `google-`, `gemini-`) से शुरू नहीं होना चाहिए. रिज़र्व किए गए प्रीफ़िक्स की पूरी सूची देखने के लिए, [एजेंट आईडी से जुड़ी पाबंदियां](#agent-id-restrictions) देखें.

### सोर्स से

सोर्स के साथ `base_agent`, `id`, `agent_config`, `system_instruction`, और `base_environment` की जानकारी दें. यह प्लैटफ़ॉर्म, हर बार आपकी फ़ाइलों के साथ एक नया सैंडबॉक्स उपलब्ध कराता है. उपलब्ध सोर्स टाइप (Git, GCS, इनलाइन) के लिए, [एनवायरमेंट](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi) देखें.

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.6-flash",
    },
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
    agent_config: {
        type: "antigravity",
        model: "gemini-3.6-flash",
    },
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
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.6-flash"
    },
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

### किसी मौजूदा एनवायरमेंट से (फ़ोर्क करना)

जब तक एनवायरमेंट सही न हो जाए (पैकेज इंस्टॉल हो जाएं, फ़ाइलें सही जगह पर हों), तब तक Antigravity के बेस एजेंट का इस्तेमाल करें. इसके बाद, इसे मैनेज किए जा सकने वाले एजेंट में फ़ोर्क करें.

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

### नेटवर्क के नियमों वाले ऑफ़र

मैनेज किए जा रहे एजेंट को सेव करते समय, आउटबाउंड ऐक्सेस को लॉक किया जा सकता है या क्रेडेंशियल डाले जा सकते हैं. अनुमति वाली सूची के पूरे स्कीमा, क्रेडेंशियल पैटर्न, और वाइल्डकार्ड के लिए, [एनवायरमेंट: नेटवर्क कॉन्फ़िगरेशन](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi#network-configuration) देखें.

यहां दिए गए उदाहरण में, एक `issue-resolver` एजेंट बनाया गया है. यह सिर्फ़ GitHub और PyPI को ऐक्सेस कर सकता है. साथ ही, इसमें GitHub के क्रेडेंशियल डाले गए हैं:

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

## एजेंट को शुरू करना

नया इंटरैक्शन बनाकर, अपने एजेंट आईडी से मैनेज किए जा रहे एजेंट को कॉल करें. हर इनवोकेशन, बेस एनवायरमेंट को फ़ोर्क करता है. इसलिए, हर रन क्लीन तरीके से शुरू होता है.

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

सिलसिलेवार बातचीत और स्ट्रीमिंग के लिए, [क्विकस्टार्ट](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=hi) देखें. मैनेज किए गए एजेंट पर भी `previous_interaction_id` और `environment` के यही पैटर्न लागू होते हैं.

मैनेज किए गए एजेंट, बैकग्राउंड में टास्क पूरा करने और उसे रद्द करने की सुविधा भी देते हैं. ज़्यादा जानकारी और कोड के उदाहरणों के लिए, [Antigravity Agent: Background execution](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi#background-execution) देखें.

## फ़ंक्शन को कॉल करते समय कॉन्फ़िगरेशन को बदलना

इंटरैक्शन बनाते समय, एजेंट के डिफ़ॉल्ट `system_instruction`, `tools`, और `environment` नेटवर्क कॉन्फ़िगरेशन को बदला जा सकता है. इससे, सेव की गई एजेंट की परिभाषा में बदलाव किए बिना, किसी खास रन के लिए एजेंट के व्यवहार, क्षमताओं या क्रेडेंशियल में बदलाव किया जा सकता है.

### सिस्टम के निर्देशों और टूल को बदलना

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

### नेटवर्क कॉन्फ़िगरेशन बदलना (क्रेडेंशियल रीफ़्रेश करना)

अगर आपके मैनेज किए जा रहे एजेंट में नेटवर्क क्रेडेंशियल पहले से मौजूद हैं, तो उन्हें कॉल करने के समय बदला जा सकता है. ऐसा इसलिए किया जाता है, ताकि खत्म हो चुके टोकन को रीफ़्रेश किया जा सके या एपीआई कुंजियों को रोटेट किया जा सके.`base_environment` नए `network` कॉन्फ़िगरेशन के साथ `environment` ऑब्जेक्ट पास करें. नए नेटवर्क नियमों के लागू होने के बाद, उस इंटरैक्शन के लिए पिछले नियम पूरी तरह से बदल जाते हैं. बेस एनवायरमेंट के सोर्स (फ़ाइलें, रिपॉज़िटरी) सुरक्षित रखे जाते हैं.

### Python

```
# Invoke the agent with a fresh token, overriding the base_environment credentials
result = client.interactions.create(
    agent="issue-resolver",
    input="Fix issue #42 and open a PR.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
// Invoke the agent with a fresh token, overriding the base_environment credentials
const result = await client.interactions.create({
    agent: "issue-resolver",
    input: "Fix issue #42 and open a PR.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        },
    },
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "issue-resolver",
      "input": "Fix issue #42 and open a PR.",
      "environment": {
          "type": "remote",
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## एजेंट मैनेज करें

आपके पास एजेंटों को सूची में शामिल करने, उन्हें पाने, और उन्हें मिटाने का विकल्प होता है.

### एजेंट की सूची बनाना

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

### कोई एजेंट पाना

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

### किसी एजेंट को मिटाना

मिटाने पर, कॉन्फ़िगरेशन हट जाता है. इससे, एजेंट के बनाए गए मौजूदा एनवायरमेंट और इंटरैक्शन पर कोई असर नहीं पड़ता.

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

## एजेंट की परिभाषा का रेफ़रंस

| फ़ील्ड | प्रकार | ज़रूरी है | ब्यौरा |
| --- | --- | --- | --- |
| `id` | स्ट्रिंग | हां | Google Cloud प्रोजेक्ट में एजेंट का यूनीक आइडेंटिफ़ायर. इसका इस्तेमाल एजेंट को शुरू करने के लिए किया जाता है. पहले से तय किए गए प्रीफ़िक्स का इस्तेमाल नहीं किया जाना चाहिए. [एजेंट आईडी से जुड़ी पाबंदियां](#agent-id-restrictions) देखें. |
| `description` | स्ट्रिंग | नहीं | इस फ़ील्ड में एजेंट के बारे में ऐसी जानकारी होती है जिसे कोई भी व्यक्ति आसानी से पढ़ सकता है. |
| `base_agent` | स्ट्रिंग | हां | बेस एजेंट का आईडी (जैसे, `antigravity-preview-05-2026`). |
| `agent_config` | ऑब्जेक्ट | नहीं | बेस एजेंट के लिए कॉन्फ़िगरेशन. इसमें मॉडल चुनने की सुविधा (`{"type": "antigravity", "model": "gemini-3.6-flash"}`) शामिल है. अगर इसे शामिल नहीं किया जाता है, तो डिफ़ॉल्ट रूप से `gemini-3.6-flash` का इस्तेमाल किया जाता है. नाम वाले एजेंट के लिए, इंटरैक्शन के दौरान इस सेटिंग को बदला नहीं जा सकता. |
| `system_instruction` | स्ट्रिंग | नहीं | सिस्टम प्रॉम्प्ट, जो व्यवहार और पर्सोना के बारे में बताता है. |
| `tools` | ऐरे | नहीं | ऐसे टूल जिनका इस्तेमाल एजेंट कर सकता है. अगर इसे शामिल नहीं किया जाता है, तो डिफ़ॉल्ट रूप से `code_execution`, `google_search`, और `url_context` पर सेट होता है. इन टूल का इस्तेमाल किया जा सकता है: `code_execution`, `google_search`, `url_context`, `mcp_server`, और कस्टम `function` डेफ़िनिशन. |
| `base_environment` | स्ट्रिंग या ऑब्जेक्ट | नहीं | `"remote"`, `environment_id` या `sources` और `network` वाला कॉन्फ़िगरेशन ऑब्जेक्ट. एनवायरमेंट देखें. |

### एजेंट आईडी से जुड़ी पाबंदियां

मैनेज किया गया एजेंट बनाते समय, आपके दिए गए `id` को इन नियमों का पालन करना होगा:

- यह आपके Google Cloud प्रोजेक्ट के लिए अलग होना चाहिए.
- यह इनमें से किसी भी रिज़र्व किए गए प्रीफ़िक्स (केस-इनसेंसिटिव) से शुरू **नहीं** होना चाहिए. ऐसा न होने पर, इसे नहीं बनाया जा सकेगा:
  - `antigravity-`
  - `veo-`
  - `omni-`
  - `lyria-`
  - `imagen-`
  - `gemma-`
  - `gemini-`
  - `google-`
  - `youtube-`
  - `android-`
  - `chrome-`
  - `pixel-`
  - `waze-`
  - `fitbit-`
  - `nest-`
  - `kaggle-`

## इटरेशन वर्कफ़्लो

1. Antigravity के बेसिक एजेंट के साथ **प्रोटोटाइप**. सिस्टम के निर्देश और एनवायरमेंट के सोर्स को इनलाइन पास करें. निर्देशों, कौशल, और एनवायरमेंट सेटअप की इंटरैक्टिव तरीके से जांच करें.
2. एनवायरमेंट को **स्थिर करें**. पैकेज इंस्टॉल करें, सोर्स माउंट करें, और पुष्टि करें कि सब कुछ काम कर रहा है.
3. सोर्स से या एनवायरमेंट को फ़ोर्क करके, नया एजेंट बनाकर मैनेज किए गए एजेंट के तौर पर **बने रहें**.
4. एजेंट की परिभाषा को **अपडेट करें**. सिस्टम के निर्देश बदलें, स्किल बदलें या सोर्स जोड़ें. अगला इनवोकेशन, नए कॉन्फ़िगरेशन को पिक अप करता है.

## सीमाएं

- **प्रीव्यू की स्थिति**: मैनेज किए गए एजेंट, प्रीव्यू में हैं. सुविधाओं और स्कीमा में बदलाव हो सकता है.
- **बेस एजेंट और मॉडल**: `base_agent` के तौर पर सिर्फ़ `antigravity-preview-05-2026` का इस्तेमाल किया जा सकता है. `agent_config` में काम करने वाले मॉडल के विकल्प ये हैं: `gemini-3.5-flash`, `gemini-3.6-flash` (डिफ़ॉल्ट), और `gemini-3.5-flash-lite`. नाम वाले एजेंट के लिए, इंटरैक्शन के समय मॉडल को ओवरराइड नहीं किया जा सकता.
- **वर्शनिंग की सुविधा उपलब्ध नहीं है**: एजेंट वर्शनिंग और रोलबैक की सुविधा फ़िलहाल उपलब्ध नहीं है.
- **सब-एजेंट नेस्टिंग की सुविधा उपलब्ध नहीं है**: फ़िलहाल, सब-एजेंट को डेलिगेट करने की सुविधा उपलब्ध नहीं है.
- आपके पास मैनेज किए जा रहे ज़्यादा से ज़्यादा 1,000 एजेंट हो सकते हैं.

## आगे क्या करना है

- [एजेंट की खास जानकारी](https://ai.google.dev/gemini-api/docs/agents?hl=hi): मैनेज किए जाने वाले एजेंट के मुख्य सिद्धांतों के बारे में जानें.
- [क्विकस्टार्ट](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=hi): सिलसिलेवार बातचीत और स्ट्रीमिंग की सुविधा का इस्तेमाल शुरू करें.
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi): डिफ़ॉल्ट एजेंट की सुविधाओं, टूल, और कीमत के बारे में जानें.
- [एजेंट एनवायरमेंट](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi): सैंडबॉक्स, सोर्स, और नेटवर्किंग कॉन्फ़िगर करें.
- [Agent Platform पर Managed Agents API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=hi): संगठन के लिए पहले से मौजूद गवर्नेंस के साथ एजेंट बनाने और मैनेज करने की सुविधा के लिए.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
