---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi
fetched_at: 2026-07-27T04:36:29.617901+00:00
title: "\u092e\u0948\u0928\u0947\u091c \u0915\u093f\u090f \u091c\u093e \u0930\u0939\u0947 \u090f\u091c\u0947\u0902\u091f\u094b\u0902 \u092e\u0947\u0902 \u090f\u0928\u0935\u093e\u092f\u0930\u092e\u0947\u0902\u091f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# मैनेज किए जा रहे एजेंटों में एनवायरमेंट

एनवायरमेंट, मैनेज किए गए Linux सैंडबॉक्स होते हैं. इनसे एजेंट को कोड चलाने और फ़ाइलें सेव करने के लिए, अलग जगह मिलती है. ये इंटरैक्शन के कॉन्टेक्स्ट से अलग होते हैं. इसलिए, एक ही एनवायरमेंट को कई इंटरैक्शन में फिर से इस्तेमाल किया जा सकता है या किसी भी समय नया एनवायरमेंट बनाया जा सकता है.

यहां दिए गए उदाहरण में, रिमोट एनवायरमेंट बनाकर उसके साथ इंटरैक्शन करने और उसका आईडी पाने का तरीका बताया गया है:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas and matplotlib, verify the imports, and print the versions.",
    environment="remote",
)

print(f"Environment ID: {interaction.environment_id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas and matplotlib, verify the imports, and print the versions.",
    environment: "remote",
});

console.log(`Environment ID: ${interaction.environment_id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Install pandas and matplotlib, verify the imports, and print the versions.",
    "environment": "remote"
}'
```

## `environment` पैरामीटर

`environment` पैरामीटर के लिए, तीन फ़ॉर्मैट इस्तेमाल किए जा सकते हैं:

| फ़ॉर्म | उदाहरण | कब इस्तेमाल करें |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | नया सैंडबॉक्स बनाएं. |
| एनवायरमेंट आईडी | `environment="env_abc123"` | मौजूदा सैंडबॉक्स को उसकी सभी फ़ाइलों और पैकेज के साथ फिर से इस्तेमाल करें. |
| कॉन्फ़िगरेशन ऑब्जेक्ट | `environment={...}` | सोर्स, नेटवर्क के नियमों या दोनों के साथ नया सैंडबॉक्स बनाएं. |

यहां दिए गए उदाहरणों में, `environment` पैरामीटर का इस्तेमाल करने के तीन तरीके बताए गए हैं.

### Python

```
from google import genai

client = genai.Client()

# Fresh sandbox
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a hello world script.",
    environment="remote",
)

# Reuse an existing sandbox
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Modify the script to accept a name argument.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# New sandbox with sources
interaction_3 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List all files and summarize the project.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            }
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Fresh sandbox
const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a hello world script.",
    environment: "remote",
});

// Reuse an existing sandbox
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Modify the script to accept a name argument.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

// New sandbox with sources
const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "List all files and summarize the project.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
        ],
    },
});

console.log(interaction.output_text);
```

### REST

```
# Fresh sandbox
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a hello world script."}],
    "environment": "remote"
}'

# Reuse an existing sandbox (replace $ENV_ID and $INTERACTION_ID with values from the previous response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [{\"type\": \"text\", \"text\": \"Modify the script to accept a name argument.\"}],
    \"environment\": \"$ENV_ID\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
}"

# New sandbox with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "List all files and summarize the project."}],
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            }
        ]
    }
}'
```

## एनवायरमेंट कॉन्फ़िगर करना

एनवायरमेंट सेट अप करने का एक तरीका यह है कि एजेंट को बताया जाए कि आपको क्या इंस्टॉल करना है.
यह डिपेंडेंसी रिज़ॉल्यूशन और समस्या हल करने की प्रोसेस को मैनेज करता है. एनवायरमेंट तैयार होने के बाद, `environment_id` सेव करें और उसे फिर से इस्तेमाल करें.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment="remote",
)

# Reuse the configured environment
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# Reuse the configured environment
interaction_3 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Using the tools in /workspace/tools, list the files.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction_2.id,
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment: "remote",
});

const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Using the tools in /workspace/tools, list the files.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction2.id,
});
console.log(interaction.output_text);
```

### REST

```
# Create interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    "environment": "remote"
}'
```

### किसी सोर्स से माउंट करना

अगर आपको पता है कि एजेंट को किन फ़ाइलों की ज़रूरत है, तो उन्हें एक ही कॉल में माउंट करें. इसके लिए, बार-बार कॉल करने की ज़रूरत नहीं है. `environment` कॉन्फ़िगरेशन ऑब्जेक्ट, तीन टाइप वाले `sources` कलेक्शन को स्वीकार करता है:

| सोर्स टाइप | `type` की वैल्यू | ब्यौरा | सीमा |
| --- | --- | --- | --- |
| Git डेटा स्टोर करने की जगह | `repository` | किसी यूआरएल से, डेटा स्टोर करने की जगह को `target` पर मौजूद सैंडबॉक्स में क्लोन करता है. | 500 एमबी |
| Cloud Storage | `gcs` | Cloud Storage से किसी फ़ाइल या डायरेक्ट्री को कॉपी करके, `target` पर मौजूद सैंडबॉक्स में सेव करता है. | 2 GB |
| इनलाइन कॉन्टेंट | `inline` | रॉ टेक्स्ट कॉन्टेंट को, `target` पर मौजूद सैंडबॉक्स में किसी फ़ाइल में लिखता है. | हर फ़ाइल के लिए एक एमबी, कुल दो एमबी |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List all files under /workspace and describe what you find.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data",
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md",
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
    input: "List all files under /workspace and describe what you find.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
            {
                type: "gcs",
                source: "gs://cloud-samples-data/bigquery/us-states/",
                target: "/workspace/gcs-data",
            },
            {
                type: "inline",
                content: "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                target: "/workspace/notes/readme.md",
            },
        ],
    },
});

console.log(interaction.output_text);
```

### REST

```
# Create interaction with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "List all files under /workspace and describe what you find.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data"
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md"
            }
        ]
    }
}'
```

दोनों तरीकों को एक साथ इस्तेमाल किया जा सकता है: जाने-पहचाने सोर्स को डिक्लेरेटिव तरीके से माउंट करें. इसके बाद, पैकेज इंस्टॉल करने या सेटअप स्क्रिप्ट चलाने के लिए, फ़ॉलो-अप इंटरैक्शन के साथ दोहराएं. कस्टम सोर्स जोड़ते समय, रूट (`/`) को टारगेट के तौर पर सेट नहीं किया जा सकता. इसके लिए, हमेशा सब-डायरेक्ट्री तय करनी होगी.

### निजी सोर्स

नेटवर्क कॉन्फ़िगरेशन में क्रेडेंशियल जोड़कर, निजी GitHub रिपॉज़िटरी या निजी Cloud Storage बकेट से भी डाउनलोड किया जा सकता है:

**निजी Git रिपॉज़िटरी** के लिए, अपने
[GitHub Personal Access Token
(PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) के साथ `Basic` ऑथेंटिकेशन का इस्तेमाल करें.
टोकन को `x-oauth-basic` को उपयोगकर्ता नाम के तौर पर इस्तेमाल करके एनकोड करें:

```
echo -n "x-oauth-basic:ghp_YourPATHere" | base64
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run the test for my backend app and fix any issue.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run the test for my backend app and fix any issue.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app"
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Run the test for my backend app and fix any issue.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

**निजी Cloud Storage बकेट** के लिए, स्टैंडर्ड OAuth 2.0 Bearer टोकन का इस्तेमाल करें:

```
gcloud auth print-access-token
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the discrepancies across the data in workspace",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "*.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the discrepancies across the data in workspace",
    environment: {
        type: "remote",
        sources: [
            {
                type: "gcs",
                source: "gs://my-private-bucket/data",
                target: "/workspace",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the discrepancies across the data in workspace",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

## पहले से इंस्टॉल किया गया सॉफ़्टवेयर

सैंडबॉक्स, Ubuntu पर चलता है. इसमें रनटाइम और सामान्य पैकेज पहले से इंस्टॉल होते हैं. एजेंट, रनटाइम के दौरान `pip
install` या `npm install` का इस्तेमाल करके, अतिरिक्त पैकेज इंस्टॉल कर सकता है. किसी इंटरैक्शन के दौरान इंस्टॉल किए गए पैकेज, उसी `environment_id` को फिर से इस्तेमाल करने पर बने रहते हैं.

| कैटगरी | पहले से इंस्टॉल किए गए पैकेज |
| --- | --- |
| **UNIX टूल** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite`, `typescript` |

## नेटवर्क कॉन्फ़िगरेशन

डिफ़ॉल्ट रूप से, एनवायरमेंट में आउटबाउंड नेटवर्क ऐक्सेस पर कोई पाबंदी नहीं होती. आउटबाउंड ट्रैफ़िक को खास डोमेन तक सीमित करने के लिए, `network` फ़ील्ड का इस्तेमाल करें. हर नियम में, `domain` और मैचिंग अनुरोधों में हेडर इंजेक्ट करने के लिए, एक वैकल्पिक `transform` ऑब्जेक्ट तय किया जाता है. ये हेडर, हर इंटरैक्शन के लिए अलग-अलग हो सकते हैं. साथ ही, इन्हें एक ही एनवायरमेंट के लिए अपडेट किया जा सकता है.

| फ़ील्ड | टाइप | ब्यौरा |
| --- | --- | --- |
| `domain` | `string` | मैच करने के लिए डोमेन. सभी डोमेन के लिए, सटीक होस्टनेम या `*` का इस्तेमाल करें. |
| `transform` | `object` | ऑब्जेक्ट में फ़्लैट की-वैल्यू पेयर होते हैं.ये पेयर, मैचिंग अनुरोधों में इंजेक्ट किए जाने वाले हेडर को दिखाते हैं. जैसे, `{"Authorization": "Bearer ..."}`. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                {"domain": "pypi.org"},
                {"domain": "*"},
            ]
        },
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
    input: "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                { domain: "pypi.org" },
                { domain: "*" },
            ]
        }
    },
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Fetch the latest issues from the GitHub API for my-org/my-repo."}],
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    }
                },
                {"domain": "pypi.org"},
                {"domain": "*"}
            ]
        }
    }
}'
```

अनुमति वाली सूची सेट होने पर, सिर्फ़ सूची में शामिल डोमेन के अनुरोधों को अनुमति दी जाती है. सबडोमेन से मैच करने के लिए, वाइल्डकार्ड का इस्तेमाल किया जा सकता है. जैसे, `{"domain":
"*.example.com"}`. हालांकि, ध्यान दें कि इससे रूट डोमेन
`example.com` मैच नहीं होता. इसे अलग से जोड़ना होगा. अन्य सभी ट्रैफ़िक को अनुमति देने के लिए, जैसे
कि सूची में शामिल न किए गए डोमेन को बिना हेडर इंजेक्ट किए रूट करने के लिए, `{"domain": "*"}` को कैच-ऑल एंट्री के तौर पर
जोड़ें.

### क्रेडेंशियल

हेडर ट्रांसफ़ॉर्मेशन जोड़कर, अपने एजेंट के लिए क्रेडेंशियल जोड़े जा सकते हैं. क्रेडेंशियल को, संबंधित एचटीटीपी हेडर में इग्रेस प्रॉक्सी से इंजेक्ट किया जाता है. इन्हें एनवायरमेंट वैरिएबल या फ़ाइलों के तौर पर, सैंडबॉक्स में कभी भी नहीं दिखाया जाता.

### Python

```
import subprocess
from google import genai

# Fetch a short-lived access token from your local gcloud CLI
gcloud_token = subprocess.check_output(
    ["gcloud", "auth", "print-access-token"], text=True
).strip()

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": f"Bearer {gcloud_token}"
                    },
                }
            ]
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import { execSync } from "child_process";

const gcloudToken = execSync("gcloud auth print-access-token").toString().trim();

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": `Bearer ${gcloudToken}`
                    },
                }
            ]
        }
    },
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer <YOUR_GCLOUD_TOKEN>"
                    }
                }
            ]
        }
    }
}'
```

### नेटवर्क ऐक्सेस की सुविधा बंद करना

आउटबाउंड नेटवर्क ऐक्सेस को ब्लॉक करने के लिए, `network` को `disabled` पर सेट करें:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the local files only.",
    environment={
        "type": "remote",
        "network": "disabled",
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
    input: "Analyze the local files only.",
    environment: {
        type: "remote",
        network: "disabled",
    },
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the local files only.",
    "environment": {
        "type": "remote",
        "network": "disabled"
    }
}'
```

### क्रेडेंशियल रीफ़्रेश करना

ऐक्सेस टोकन और कम समय के लिए मान्य एपीआई कुंजियों जैसे क्रेडेंशियल की समयसीमा खत्म हो जाती है.
इन्हें रीफ़्रेश करने के लिए, अगले इंटरैक्शन में मौजूदा `environment_id` के साथ नया `network` कॉन्फ़िगरेशन पास करें. नए नेटवर्क के नियम, पुराने नियमों की जगह पूरी तरह से ले लेते हैं. वहीं, एनवायरमेंट के फ़ाइल सिस्टम की स्थिति (इंस्टॉल किए गए पैकेज, फ़ाइलें, रिपॉज़िटरी) बनी रहती है.

### Python

```
from google import genai

client = genai.Client()

# First interaction: use an initial token
first = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        },
    },
)

# Later: refresh the token on the same environment
result = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Now download the file reports/q1.csv from the same bucket.",
    environment={
        "type": "remote",
        "environment_id": first.environment_id,
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First interaction: use an initial token
const first = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        }
    },
});

// Later: refresh the token on the same environment
const result = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Now download the file reports/q1.csv from the same bucket.",
    environment: {
        type: "remote",
        environment_id: first.environment_id,
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        }
    },
});

console.log(result.output_text);
```

### REST

```
# Use the environment_id from a previous interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Now download the file reports/q1.csv from the same bucket.",
    "environment": {
        "type": "remote",
        "environment_id": "<ENVIRONMENT_ID_FROM_PREVIOUS_INTERACTION>",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    }
                }
            ]
        }
    }
}'
```

## एनवायरमेंट का लाइफ़साइकल

एनवायरमेंट का लाइफ़साइकल इस तरह होता है:

| राज्य | व्यवहार |
| --- | --- |
| **बनाया गया** | जब कोई इंटरैक्शन, `environment: "remote"` या कॉन्फ़िगरेशन ऑब्जेक्ट तय करता है, तब एनवायरमेंट बनाया जाता है. |
| **चालू है** | इंटरैक्शन के दौरान चालू रहता है. |
| **कुछ समय से इस्तेमाल में नहीं है** | 15 मिनट तक कोई गतिविधि न होने पर, इसका स्नैपशॉट अपने-आप ले लिया जाता है और यह बंद हो जाता है. |
| **ऑफ़लाइन** | पिछली बार चालू होने के बाद, सात दिनों तक बना रहता है. इसका आईडी पास करके, इसे फिर से चालू किया जा सकता है. |
| **मिटाया गया** | टीटीएल के सात दिनों की समयसीमा खत्म होने के बाद या मैन्युअल तरीके से मिटाने पर, इसे सिस्टम से अपने-आप हटा दिया जाता है. |

## Environments API

सैंडबॉक्स सेशन को प्रोग्राम के हिसाब से मैनेज करने के लिए, Environments API का इस्तेमाल किया जा सकता है.
एनवायरमेंट की सूची बनाने से, चालू सेशन के आईडी का पता लगाया जा सकता है. साथ ही, लंबे समय तक चलने वाले टास्क के दौरान, क्लाइंट कनेक्शन खत्म होने पर, स्थिति को वापस लाया जा सकता है. सेशन का मेटाडेटा भी देखा जा सकता है. साथ ही, वर्कफ़्लो खत्म होने पर, एनवायरमेंट को साफ़ तौर पर मिटाया जा सकता है. इसके लिए, टीटीएल की समयसीमा खत्म होने का इंतज़ार करने की ज़रूरत नहीं है.

### एनवायरमेंट की सूची बनाना

अपने प्रोजेक्ट से जुड़े चालू एनवायरमेंट की सूची बनाएं. जवाब के बैच का साइज़ कंट्रोल करने के लिए, पेज पर नंबर डालने वाले पैरामीटर का इस्तेमाल करें.

### Python

```
from google import genai

client = genai.Client()

for env in client.environments.list(page_size=10):
    print(f"Environment ID: {env.environment_id}, Type: {env.type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.list({ pageSize: 10 });
for (const env of response.environments) {
    console.log(`Environment ID: ${env.environment_id}, Type: ${env.type}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments?pageSize=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

जवाब, यहां दिए गए उदाहरण की तरह दिखता है:

```
{
  "environments": [
    {
      "environment_id": "140128b2a13c12c00a5a0d8cf7af9469",
      "type": "remote"
    },
    {
      "environment_id": "362b738275a1d74af6f1c62bc050da73",
      "type": "remote"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

### कोई एनवायरमेंट पाना

किसी खास एनवायरमेंट के लिए, उसके संसाधन के नाम के हिसाब से मेटाडेटा और कॉन्फ़िगरेशन की जानकारी पाएं.

### Python

```
from google import genai

client = genai.Client()

env = client.environments.get(name="environments/YOUR_ENVIRONMENT_ID")
print(f"Environment ID: {env.environment_id}, Type: {env.type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const env = await client.environments.get({ name: "environments/YOUR_ENVIRONMENT_ID" });
console.log(`Environment ID: ${env.environment_id}, Type: ${env.type}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

जवाब, यहां दिए गए उदाहरण की तरह दिखता है:

```
{
  "environment_id": "140128b2a13c12c00a5a0d8cf7af9469",
  "type": "remote",
  "sources": [
    {
      "type": "repository",
      "source": "https://github.com/octocat/Spoon-Knife",
      "target": "/workspace/spoon-knife"
    }
  ],
  "network": {
    "allowlist": [
      {
        "domain": "api.github.com"
      },
      {
        "domain": "github.com"
      }
    ]
  }
}
```

### कोई एनवायरमेंट मिटाना

अपने टास्क या पाइपलाइन खत्म होने पर, सैंडबॉक्स के संसाधनों को साफ़ करने के लिए, किसी एनवायरमेंट को साफ़ तौर पर खत्म करें और मिटाएं.

### Python

```
from google import genai

client = genai.Client()

client.environments.delete(name="environments/YOUR_ENVIRONMENT_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

await client.environments.delete({ name: "environments/YOUR_ENVIRONMENT_ID" });
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## एनवायरमेंट से फ़ाइलें डाउनलोड करना

एजेंट, एक्ज़ीक्यूशन के दौरान सैंडबॉक्स में फ़ाइलें बनाता है. Files API का इस्तेमाल करके, पूरे एनवायरमेंट के स्नैपशॉट को टार फ़ाइल के तौर पर डाउनलोड किया जा सकता है:

### Python

```
import os
import requests
import tarfile
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a file environments_test.txt with content 'Environments' inside the sandbox.",
    environment="remote",
)

env_id = interaction.environment_id
api_key = os.environ.get("GEMINI_API_KEY")

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot_env.tar", "wb") as f:
    f.write(response.content)

os.makedirs("extracted_env_snapshot", exist_ok=True)
with tarfile.open("snapshot_env.tar") as tar:
    tar.extractall(path="extracted_env_snapshot")

print(os.listdir("extracted_env_snapshot"))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { execSync } from "child_process";
import * as fs from "fs";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a file environments_test.txt with content 'Environments' inside the sandbox.",
    environment: "remote",
});

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot_env.tar", buffer);

if (!fs.existsSync("extracted_env_snapshot")) {
    fs.mkdirSync("extracted_env_snapshot");
}
execSync("tar -xf snapshot_env.tar -C extracted_env_snapshot");

console.log(fs.readdirSync("extracted_env_snapshot"));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a file environments_test.txt with content '\''Environments'\'' inside the sandbox.",
    "environment": "remote"
}'
# Step 2: Download snapshot (reusing environment ID from Step 1)
# curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
#   -H "x-goog-api-key: $API_KEY" \
#   -o snapshot.tar
```

## कीमत और संसाधन

हर एनवायरमेंट, तय किए गए संसाधन के साथ चलता है:

| संसाधन | मान |
| --- | --- |
| **सीपीयू** | चार कोर |
| **मेमोरी** | 16 जीबी |

प्रीव्यू की अवधि के दौरान, एनवायरमेंट के कंप्यूट (सीपीयू, मेमोरी, सैंडबॉक्स एक्ज़ीक्यूशन) के लिए **कोई शुल्क नहीं लिया जाता**. एजेंट टोकन की लागत के बारे में जानने के लिए,
[कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#pricing-for-agents) देखें.

## सीमाएं

- **प्रीव्यू की स्थिति:** एनवायरमेंट और मैनेज किए गए एजेंट, प्रीव्यू में हैं. इनकी सुविधाओं और स्कीमा में बदलाव हो सकता है.
- **इनलाइन सोर्स का साइज़:** इनलाइन सोर्स, हर फ़ाइल के लिए एक एमबी और सभी फ़ाइलों के लिए कुल दो एमबी तक सीमित हैं.
- **सोर्स का साइज़**: Git रिपॉज़िटरी 500 एमबी और Cloud Storage रिपॉज़िटरी दो जीबी तक सीमित हैं.
- **एनवायरमेंट का स्टार्टअप:** नया एनवायरमेंट बनाने में, करीब पांच सेकंड लगते हैं. बड़े सोर्स रिपॉज़िटरी की वजह से, इसमें ज़्यादा समय लग सकता है.
- **एनवायरमेंट की समयसीमा खत्म होना:** ऑफ़लाइन एनवायरमेंट, सात दिनों तक बने रहते हैं. इसके बाद, टीटीएल क्लीनअप की सुविधा से, इनकी समयसीमा अपने-आप खत्म हो जाती है. समयसीमा खत्म हो चुके या अमान्य एनवायरमेंट आईडी को पास करने पर, `404 Not Found` गड़बड़ी दिखती है.
- **फ़ाइल फ़ॉर्मैट के लिए सहायता:** फ़िलहाल, एजेंट सिर्फ़ टेक्स्ट और इमेज फ़ाइलें पढ़ सकता है. बाइनरी फ़ाइलें पढ़ने की सुविधा अभी उपलब्ध नहीं है.
- **रूट से माउंट करने की सुविधा नहीं है:** कस्टम सोर्स जोड़ते समय, रूट (`/`) को टारगेट के तौर पर सेट नहीं किया जा सकता. इसके लिए, हमेशा सब-डायरेक्ट्री तय करनी होगी.

## आगे क्या करना है

- [एजेंट की खास जानकारी](https://ai.google.dev/gemini-api/docs/agents?hl=hi): मैनेज किए गए एजेंट के मुख्य कॉन्सेप्ट के बारे में जानें.
- [क्विकस्टार्ट](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=hi): सिलसिलेवार बातचीत और स्ट्रीमिंग की सुविधा के साथ, एजेंट बनाना शुरू करें.
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi): डिफ़ॉल्ट एजेंट की क्षमताओं, टूल, मॉडल चुनने के तरीके, और कीमत के बारे में जानें.
- [कस्टम एजेंट बनाना](https://ai.google.dev/gemini-api/docs/custom-agents?hl=hi): `AGENTS.md` और `SKILL.md` का इस्तेमाल करके, अपने एजेंट तय करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-23 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-23 (UTC) को अपडेट किया गया."],[],[]]
