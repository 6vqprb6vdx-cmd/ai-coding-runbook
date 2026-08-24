---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=id
fetched_at: 2026-08-24T02:27:19.581466+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Hooks

Hook memungkinkan Anda menjalankan skrip kustom atau permintaan HTTP eksternal tepat sebelum atau setelah agen menjalankan kode atau mengubah file di dalam sandbox jarak jauhnya. Gunakan hook untuk memperluas loop agen dengan batasan otomatis dan alur kerja latar belakang, seperti:

- **Menerapkan batasan keamanan dan akses** sebelum perintah shell berisiko tinggi atau pembacaan file terbatas dijalankan.
- **Mengotomatiskan transformasi pipeline data** tepat setelah agen membuat atau mengubah file.
- **Streaming telemetri audit perusahaan** ke sistem pemantauan eksternal setelah eksekusi alat.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
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

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
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
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## Peristiwa siklus proses yang didukung

Hook mendukung 2 peristiwa di dalam sandbox:

| Peristiwa | Waktu diaktifkan | Fungsinya |
| --- | --- | --- |
| `pre_tool_execution` | Tepat sebelum alat dijalankan | Dapat menyetujui (`allow`) atau memblokir (`deny`) alat sebelum dijalankan. Saat diblokir, model akan melihat alasan penolakan Anda dan menyesuaikannya. |
| `post_tool_execution` | Tepat setelah alat selesai | Menjalankan tugas lanjutan seperti memformat kode, menjalankan pengujian unit, atau mencatat telemetri. Tidak dapat memblokir atau mengurungkan tindakan yang telah selesai. |

### `pre_tool_execution`

Diaktifkan tepat sebelum alat dijalankan. Skrip Anda membaca detail panggilan alat dari `stdin` dan menampilkan JSON keputusannya (`allow` atau `deny`) ke `stdout`.

**Payload input (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**Respons output (`stdout`):**

Untuk menyetujui panggilan alat:

```
{
  "decision": "allow"
}
```

Untuk memblokir panggilan alat dan menampilkan masukan ke model:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

Jika hook menolak perintah, panggilan alat akan segera dilewati. Agen akan melihat hasil error yang berisi alasan penolakan Anda tepat di dalam giliran saat ini. Model kemudian dapat mengoreksi diri sendiri dengan memilih perintah alternatif atau menjelaskan blokir kepada pengguna.

Jika skrip Anda menampilkan JSON yang tidak dikenali, teks biasa, atau apa pun selain `{"decision": "deny"}`, runtime akan memperlakukan respons sebagai persetujuan (`allow`).

### `post_tool_execution`

Diaktifkan tepat setelah alat selesai. Skrip Anda membaca detail eksekusi dan status error dari `stdin`.

**Payload input (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

Jika perintah shell mencetak error ke error standar (`stderr`) atau operasi sistem file gagal, kolom `"error"` yang berisi teks error akan disertakan dalam payload. Jika perintah berhasil tanpa error, kolom `"error"` akan dihilangkan sepenuhnya.

**Respons output (`stdout`):**

```
{}
```

Karena hook pasca-alat berjalan secara ketat untuk tugas latar belakang seperti pemformatan kode atau logging, runtime akan mengabaikan nilai keputusan apa pun yang ditampilkan di `stdout`.

## Penemuan konfigurasi

Runtime otomatis menemukan definisi hook dari `.agents/hooks.json` atau `/.agents/hooks.json` di dalam lingkungan sandbox. Anda dapat menyediakan `hooks.json` bersama skrip kustom menggunakan sumber [lingkungan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#mount_from_a_source) yang didukung:

- **Pemasangan repositori**: Repositori Git yang berisi `.agents/hooks.json` bersama `AGENTS.md`.
- **Cloud Storage (`gcs`)**: Bucket GCS yang berisi `hooks.json` yang disalin ke lingkungan.
- **Sumber inline**: String JSON mentah dan konten skrip yang diteruskan di `environment.sources` saat memanggil `client.interactions.create`.

### Skema `hooks.json`

File `hooks.json` mengelompokkan definisi peristiwa (`pre_tool_execution` atau `post_tool_execution`) dengan nama kustom. Anda dapat mengaktifkan atau menonaktifkan setiap grup secara terpisah:

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### Sintaksis dan aturan pencocok

Setiap grup aturan di `hooks.json` menentukan kapan dan bagaimana pengendali diaktifkan menggunakan properti `matcher` dan `hooks`:

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `enabled` | `boolean` | Opsional. Tetapkan ke `false` untuk menonaktifkan grup (`true` secara default). |
| `matcher` | `string` | Pola ekspresi reguler yang cocok dengan nama alat target di dalam penampung. |
| `hooks` | `array` | Daftar definisi pengendali yang diurutkan (`command` atau `http`). Pengendali berjalan secara berurutan dalam urutan deklarasi. |

#### Cara kerja evaluasi ekspresi reguler

Saat agen memanggil alat di dalam sandbox, runtime akan mengevaluasi nama penampung alat terhadap pola `matcher` Anda menggunakan ekspresi reguler RE2 standar. Jika ekspresi reguler cocok dengan nama alat, semua pengendali dalam array `hooks` akan dijalankan secara berurutan. Jika beberapa grup aturan cocok dengan alat yang sama, semua array pengendali yang sesuai akan dijalankan.

Anda dapat menargetkan nama alat penampung bawaan: eksekusi kode (`code_execution`) atau operasi sistem file (`read_file`, `write_file`, `list_files`, dan `delete_file`).

#### Ekspresi pencocok umum

- `"code_execution"`: Pencocokan string yang tepat untuk perintah shell dan eksekusi skrip.
- `"write_file"`: Pencocokan yang tepat untuk pembuatan file sistem file dan penulisan disk.
- `"read_file|write_file"`: Pemisahan pipa cocok dengan beberapa nama alat tertentu dalam satu aturan.
- `".*_file"`: Karakter pengganti ekspresi reguler yang cocok dengan alat apa pun yang diakhiri dengan `_file` (seperti `read_file`, `write_file`, atau `delete_file`). Ekspresi reguler RE2 standar memerlukan `.*`; glob shell sederhana seperti `*_file` adalah sintaksis ekspresi reguler yang tidak valid dan akan gagal dicocokkan.
- `".*"` atau `"*"` atau `""`: Pola catch-all yang mencegat setiap panggilan alat di dalam penampung.

## Jenis pengendali

### Hook perintah

Hook perintah menjalankan perintah atau skrip shell di dalam sandbox. Skrip menerima JSON peristiwa di `stdin` dan menampilkan JSON keputusannya di `stdout`.

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `type` | `string` | Harus berupa `"command"`. |
| `command` | `string` | Baris perintah yang akan dijalankan di dalam sandbox (misalnya, `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | Batas waktu dalam detik. Default: `30`. |

### Hook HTTP

Hook HTTP mengirim JSON peristiwa sebagai permintaan POST ke URL HTTPS eksternal langsung dari dalam jaringan sandbox. Server target menampilkan keputusannya di isi respons HTTP menggunakan format JSON yang sama persis (`{"decision": "allow"}` atau `{"decision": "deny", "reason": "..."}`).

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `type` | `string` | Harus berupa `"http"`. |
| `url` | `string` | Endpoint HTTPS eksternal untuk mem-POST payload peristiwa. |
| `headers` | `object` | Pasangan nilai kunci opsional untuk header kustom non-sensitif (seperti `{"X-Event-Source": "agent-sandbox"}`). Untuk kredensial autentikasi, gunakan proxy jaringan. |
| `timeout` | `integer` | Batas waktu dalam detik. Default: `30`. |

#### Proxy keluar dan transformasi token

Karena hook HTTP dijalankan langsung dari dalam namespace jaringan sandbox, permintaan keluar akan diteruskan melalui proxy keluar transparan. Arsitektur ini memberi Anda 2 keuntungan keamanan penting:

- **Daftar yang diizinkan jaringan:** Endpoint target harus diizinkan secara eksplisit di `network.allowlist` lingkungan Anda. Traffic loopback (`127.0.0.1` atau `localhost`) diblokir oleh proxy; selalu targetkan endpoint eksternal yang diizinkan.
- **Transformasi token:** Anda tidak perlu menyimpan kunci API atau token pembawa rahasia di dalam `.agents/hooks.json` atau memasangnya ke dalam penampung. Sebagai gantinya, konfigurasi aturan transformasi token di [konfigurasi jaringan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#network-configuration) Anda (`network.allowlist.transform`). Proxy keluar akan otomatis mencegat traffic hook HTTP keluar dan menyisipkan header autentikasi Anda yang sebenarnya di jaringan sebelum keluar dari sandbox.

## Cara runtime menangani keputusan dan kegagalan

- **Menunggu sinkron:** Agen akan berhenti dan menunggu hook Anda selesai sebelum melanjutkan.
- **Memblokir eksekusi alat:** Jika hook pra-alat Anda menampilkan `{"decision": "deny", "reason": "<your reason>"}`, runtime akan segera membatalkan panggilan alat. Model akan melihat alasan penolakan Anda di histori percakapannya dan menyesuaikan dengan memilih alternatif yang aman atau menjelaskan blokir kepada pengguna.
- **Menangani error skrip, error HTTP, dan batas waktu:** Jika skrip perintah mengalami error (status keluar bukan nol), hook HTTP menampilkan kode status non-2xx (seperti error server 4xx atau 5xx), atau operasi mencapai batas waktu atau menampilkan JSON yang tidak dikenali, runtime akan memperlakukannya sebagai persetujuan (`allow`). Eksekusi alat akan terus berjalan secara normal sehingga skrip yang rusak atau server telemetri yang tidak dapat dijangkau tidak akan pernah menyebabkan aplikasi Anda mengalami deadlock.

## Kasus penggunaan umum

### Pemulihan multi-giliran untuk privasi dan kepatuhan data

Jika hook memblokir akses ke resource terbatas—seperti direktori yang berisi Informasi Identitas Pribadi (PII) atau catatan keuangan rahasia—Anda dapat meneruskan `previous_interaction_id` pada panggilan berikutnya untuk melanjutkan giliran di lingkungan yang sama. Agen akan membaca penjelasan penolakan dan otomatis memulihkan dengan membuat kueri tabel publik yang disetujui.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "read_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "read_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"read_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-05-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### Telemetri dan logging audit eksternal

Kirim peristiwa audit real-time dari dalam sandbox ke server pemantauan eksternal setiap kali file dibaca atau diubah.

- **Cocokkan beberapa alat:** Karena pencocok menggunakan ekspresi reguler standar, Anda dapat menggabungkan beberapa alat dalam satu aturan menggunakan pipa (`read_file|write_file`) atau karakter pengganti (`.*_file`).
- **Jaga kerahasiaan informasi di luar konfigurasi Anda:** Tentukan token autentikasi di [konfigurasi jaringan](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id#network-configuration) lingkungan Anda (`network.allowlist.transform`). Proxy keluar akan otomatis menyisipkan token pembawa Anda yang sebenarnya pada permintaan keluar.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "read_file|write_file",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
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

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "read_file|write_file",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
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
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"read_file|write_file\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## Batasan

- **Cakupan alat sandbox:** Hook mencegat alat bawaan di dalam sandbox: eksekusi kode (`code_execution`) dan operasi sistem file (`read_file`, `write_file`, `list_files`, dan `delete_file`). Hook tidak diaktifkan untuk panggilan fungsi kustom (`function`) atau alat Model Context Protocol (`mcp_server`) eksternal yang ditangani di luar penampung.
- **Daftar yang diizinkan jaringan:** Hook HTTP berjalan di dalam jaringan penampung. Anda harus mengizinkan URL target secara eksplisit di `network.allowlist` lingkungan Anda. Alamat loopback (`localhost`, `127.0.0.1`) diblokir oleh proxy.
- **Persetujuan otomatis saat terjadi error:** Jika skrip hook mengalami error (status keluar bukan nol), mencapai batas waktu, atau gagal, runtime akan mencatat kegagalan dan mengizinkan panggilan alat untuk dilanjutkan. Hal ini memastikan skrip linter yang rusak atau proses yang terhenti tidak akan pernah menyebabkan aplikasi Anda mengalami deadlock.
- **Perlindungan konfigurasi sandbox:** Karena hook dijalankan di dalam sandbox penampung, agen dengan alat tulis sistem file atau izin eksekusi kode shell dapat mengubah `.agents/hooks.json` atau skrip lokal di dalam ruang kerja yang dapat ditulis. Gunakan hook penampung sebagai panduan kebijakan otomatis dan batasan operasional; jika ketahanan terhadap gangguan yang ketat diperlukan terhadap eksekusi model yang tidak tepercaya, pasang sumber konfigurasi dari repositori hanya baca.

## Langkah berikutnya

- [Pelajari cara mengonfigurasi sandbox dan lingkungan jarak jauh yang persisten.](https://ai.google.dev/gemini-api/docs/agent-environment?hl=id)
- Pelajari kemampuan dan alat bawaan agen [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=id).
- Tinjau [ringkasan Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) untuk sesi multi-giliran dan streaming.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
