---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=id
fetched_at: 2026-06-08T15:01:51.319588+00:00
title: "Membangun Agen Terkelola \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Membangun Agen Terkelola

Agen terkelola di Gemini API memungkinkan Anda memperluas agen Antigravity dengan petunjuk, kemampuan, dan data Anda sendiri. Anda dapat [menyesuaikan agen secara inline](#customize-inline) pada waktu interaksi, atau [menyimpan konfigurasi](#save-agent) sebagai agen terkelola yang Anda panggil berdasarkan ID.

## Menyesuaikan agen Antigravitasi

Cara tercepat untuk membuat agen kustom adalah dengan meneruskan konfigurasi inline saat membuat interaksi baru tanpa memerlukan langkah pendaftaran. Anda dapat memperluas kemampuan agen dengan tiga cara:

- **Petunjuk sistem**: Teruskan teks inline melalui `system_instruction` untuk membentuk perilaku.
- **Alat**: Mengganti alat default (Eksekusi Kode, Penelusuran, Konteks URL).
- **File dan keterampilan**: Pasang file seperti `AGENTS.md` dan `SKILL.md` ke dalam lingkungan.

Berikut adalah contoh meneruskan ketiga parameter secara inline:

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

Semuanya ditentukan pada waktu interaksi. Tidak perlu mendaftarkan apa pun terlebih dahulu. Harness agen Antigravity menyediakan runtime (eksekusi kode, pengelolaan file, akses web) dan lapisan konfigurasi Anda di atasnya.

### Alat dan petunjuk sistem

Anda dapat menyesuaikan perilaku dan kemampuan agen untuk interaksi tertentu menggunakan parameter `system_instruction` dan `tools`.

- **Petunjuk sistem**: Gunakan parameter `system_instruction` untuk meneruskan teks inline yang membentuk perilaku agen. Opsi ini ideal untuk penyesuaian cepat yang ingin Anda ubah per panggilan. `system_instruction` dan `AGENTS.md` bersifat aditif; keduanya berlaku jika ada.
- **Alat**: Secara default, agen Antigravity memiliki akses ke `code_execution`, `google_search`, dan `url_context`. Anda dapat mengganti daftar ini dengan meneruskan parameter `tools` pada waktu interaksi. Untuk mengetahui detail lengkap tentang alat yang tersedia dan cara menggunakannya, lihat [Agen Antigravity: Alat yang didukung](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id#supported-tools).

### Penyesuaian berbasis file

#### Struktur direktori agen

Meskipun Anda dapat meneruskan konfigurasi sebaris, sebaiknya susun file agen Anda dalam direktori terstruktur. Hal ini mempermudah pengelolaan, kontrol versi, dan pemasangan ke lingkungan agen.

Direktori project agen standar terlihat seperti ini:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Runtime Antigravity memindai `.agents/` (dan root lingkungan) untuk mencari file ini.

#### AGENTS.md

Agen otomatis memuat `.agents/AGENTS.md` (atau `/.agents/AGENTS.md`) dari lingkungan sebagai petunjuk sistem saat memulai. Gunakan `AGENTS.md` untuk definisi persona panjang, panduan mendetail, dan petunjuk yang ingin Anda kontrol versinya bersama kode Anda.

Pasang `AGENTS.md` menggunakan sumber inline:

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

#### Keterampilan: SKILL.md

Keterampilan adalah file yang memperluas kemampuan agen. Tempatkan di bawah `.agents/skills/<skill-name>/SKILL.md` dan harness akan otomatis menemukan serta mendaftarkannya.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Pasang keterampilan menggunakan sumber inline:

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

Keterampilan yang dimuat dari `.agents/skills/` dan `/.agents/skills/` akan otomatis ditemukan.

## Membuat agen terkelola

Setelah melakukan iterasi pada konfigurasi, Anda dapat membuatnya sebagai agen terkelola dengan `agents.create`. Dengan begitu, Anda dapat memanggil agen berdasarkan ID tanpa mengulangi konfigurasi setiap saat.

### Dari sumber

Tentukan `base_agent`, `id`, `system_instruction`, dan `base_environment` dengan sumber. Platform ini menyediakan sandbox baru dengan file Anda pada setiap pemanggilan. Lihat [Lingkungan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id) untuk jenis sumber yang tersedia (Git, GCS, inline).

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

### Dari lingkungan yang ada (fork)

Lakukan iterasi dengan agen Antigravity dasar hingga lingkungan sudah tepat (paket diinstal, file sudah ada), lalu buat fork menjadi agen terkelola.

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

### Dengan aturan jaringan

Anda dapat mengunci akses keluar atau menyuntikkan kredensial saat menyimpan agen terkelola. Untuk mengetahui skema daftar yang diizinkan, pola kredensial, dan karakter pengganti selengkapnya, lihat [Lingkungan: Konfigurasi jaringan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#network-configuration).

Contoh berikut membuat agen `issue-resolver` yang hanya dapat mengakses GitHub dan PyPI, dengan kredensial yang dimasukkan untuk GitHub:

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

## Memanggil agen

Panggil agen terkelola Anda dengan ID agen Anda dengan membuat interaksi baru. Setiap pemanggilan membuat cabang lingkungan dasar, sehingga setiap proses dimulai dengan bersih.

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

Untuk percakapan multi-turn dan streaming, lihat [Panduan memulai](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id). Pola `previous_interaction_id` dan `environment` yang sama berlaku untuk agen terkelola.

## Mengganti konfigurasi saat pemanggilan

Anda dapat mengganti `system_instruction` dan `tools` default agen saat membuat interaksi. Hal ini memungkinkan Anda mengubah perilaku atau kemampuan agen untuk satu kali proses tertentu tanpa mengubah definisi agen yang disimpan.

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

## Kelola agen

Anda dapat mencantumkan, mendapatkan, dan menghapus agen.

### Mencantumkan agen

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

### Mendapatkan agen

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

### Menghapus agen

Menghapus akan menghapus konfigurasi. Lingkungan dan interaksi yang sudah ada yang dibuat oleh agen tidak terpengaruh.

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

## Referensi definisi agen

| Kolom | Jenis | Wajib diisi | Deskripsi |
| --- | --- | --- | --- |
| `id` | string | Ya | ID agen unik. Digunakan untuk memanggil agen. |
| `description` | string | Tidak | Deskripsi agen yang dapat dibaca manusia. |
| `base_agent` | string | Ya | ID agen dasar (misalnya, `antigravity-preview-05-2026`). |
| `system_instruction` | string | Tidak | Perintah sistem yang menentukan perilaku dan persona. |
| `tools` | string atau objek | Tidak | Alat yang dapat digunakan agen, yang tidak disertakan akan memiliki akses ke `code_execution`, `google_search`, dan `url_context`. |
| `base_environment` | string atau objek | Tidak | `"remote"`, `environment_id`, atau objek konfigurasi dengan `sources` dan `network`. Lihat Lingkungan. |

## Alur kerja iterasi

1. **Buat prototipe** dengan agen Antigravity dasar. Teruskan petunjuk sistem dan sumber lingkungan secara inline. Uji petunjuk, keterampilan, dan penyiapan lingkungan secara interaktif.
2. **Stabilkan** lingkungan. Instal paket, pasang sumber, verifikasi semuanya berfungsi.
3. **Persist** sebagai agen terkelola dengan membuat agen baru, baik dari sumber maupun dengan membuat cabang lingkungan.
4. **Perbarui** definisi agen. Ubah petunjuk sistem, ganti keterampilan, atau tambahkan sumber. Pemanggilan berikutnya akan mengambil konfigurasi baru.

## Batasan

- **Status pratinjau**: Agen terkelola dalam pratinjau. Fitur dan skema dapat berubah.
- **Agen dasar**: Hanya `antigravity-preview-05-2026` yang didukung sebagai `base_agent`.
- **Tanpa pembuatan versi**: Pembuatan versi dan rollback agen belum tersedia.
- **Tidak ada penyusunan sub-agen**: Delegasi sub-agen belum didukung.
- Anda dapat memiliki hingga 1.000 agen terkelola.

## Langkah berikutnya

- [Ringkasan Agen](https://ai.google.dev/gemini-api/docs/agents?hl=id): Pelajari konsep inti agen terkelola.
- [Panduan memulai](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=id): Mulai membangun dengan percakapan multi-turn dan streaming.
- [Agen Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id): Pelajari kemampuan, alat, dan harga untuk agen default.
- [Lingkungan Agen](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id): Mengonfigurasi sandbox, sumber, dan jaringan.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-01 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-01 UTC."],[],[]]
