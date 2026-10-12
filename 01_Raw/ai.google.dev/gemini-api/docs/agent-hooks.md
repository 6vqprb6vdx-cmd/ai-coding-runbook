---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=fa
fetched_at: 2026-10-12T07:15:08.580977+00:00
title: "\u0642\u0644\u0627\u0628\u200c\u0647\u0627 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash اکنون در دسترس است. [آن را امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fa) .

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# قلاب‌ها

قلاب‌ها به شما امکان می‌دهند درست قبل یا بعداز اینکه کارگزار کد را اجرا می‌کند یا فایل‌ها را در جعبه امن از دور اصلاح می‌کند، پلاتین‌های سفارشی یا درخواست‌های HTTP خارجی را اجرا کنید. از قلاب‌ها برای گسترش حلقه عامل با نرده‌های محافظ خودکار و گردش‌های کار پس‌زمینه‌ای استفاده کنید، مثلاً:

- **اجرای محافظ‌های ایمنی و دسترسی** قبل‌از اجرای دستورات پوسته پرخطر یا خواندن فایل‌های محدودشده.
- **خودکارسازی تبدیل‌های خط لوله داده** بلافاصله پس‌از اینکه کارگزاری فایل‌ها را ایجاد یا اصلاح می‌کند.
- **جاری‌سازی داده‌های تله‌متری ممیزی سازمانی** به سیستم‌های پایش خارجی پس‌از اجرای ابزار.

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
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "security-gate": {
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
  }
}
""";

String gateScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "cmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\n"
    + "if \"rm -rf\" in cmd:\n"
    + "    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\n"
    + "else:\n"
    + "    print(json.dumps({\"decision\": \"allow\"}))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/gate.py")
            .content(gateScript)
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run `rm -rf /tmp/forbidden` using code_execution."))
    .tools(List.of(CodeExecution.builder().build()))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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

    hooksConfig := `{
  "security-gate": {
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
  }
}`

    gateScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/gate.py"),
                Content: genai.Ptr(gateScript),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run `rm -rf /tmp/forbidden` using code_execution."),
            Tools:       []interactions.Tool{interactions.NewTool(interactions.CodeExecution{})},
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
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

## رویدادهای چرخه حیات پشتیبانی‌شده

قلاب‌ها از ۲ رویداد در جعبه شنی پشتیبانی می‌کنند:

| رویداد | وقتی فعال می‌شود | کارکرد |
| --- | --- | --- |
| `pre_tool_execution` | درست قبل‌از اجرای ابزار | می‌تواند ابزار را قبل‌از اجرا تأیید (`allow`) یا مسدود (`deny`) کند. وقتی مسدود شود، مدل دلیل رد کردن شما را می‌بیند و خود را تطبیق می‌دهد. |
| `post_tool_execution` | بلافاصله پس‌از پایان ابزار | تکالیف پیگیری مانند قالب‌بندی کد، اجرای آزمون‌های واحد، یا ثبت تله‌متری را اجرا می‌کند. نمی‌توانید کنش‌های تکمیل‌شده را مسدود یا واگرد کنید. |

### `pre_tool_execution`

درست قبل‌از اجرای ابزار فعال می‌شود. نوشتار شما جزئیات تماس ابزار را از `stdin` می‌خواند و تصمیم JSON آن (`allow` یا `deny`) را در `stdout` برونداد می‌کند.

**واحد داده ورودی (`stdin`):**

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

**پاسخ برونداد (`stdout`):**

برای تأیید فراخوانی ابزار:

```
{
  "decision": "allow"
}
```

برای مسدود کردن فراخوانی ابزار و برگرداندن بازخورد به مدل:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

وقتی قلابی فرمانی را رد می‌کند، تماس ابزار بلافاصله رد می‌شود. عامل نتیجه خطایی را که حاوی دلیل رد شما است درست در نوبت فعلی‌اش می‌بیند. سپس مدل می‌تواند با انتخاب فرمان جایگزین یا توضیح دادن مسدودسازی به کاربر، خود را اصلاح کند.

اگر دستورگان شما JSON ناشناخته، نوشتار ساده، یا هر چیزی به‌جز `{"decision": "deny"}` را برون‌برد کند، زمان اجرا پاسخ را به‌عنوان تأیید (`allow`) درنظر می‌گیرد.

### `post_tool_execution`

بلافاصله پس‌از تکمیل ابزار اجرا می‌شود. نوشتار شما جزئیات اجرا و وضعیت خطا را از `stdin` می‌خواند.

**واحد داده ورودی (`stdin`):**

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

اگر فرمان پوسته خطاها را در خطای استاندارد (`stderr`) چاپ کند یا عملیات سیستم فایل ناموفق باشد، فیلد `"error"` حاوی نوشتار خطا در بار گنجانده می‌شود. وقتی فرمان بدون خطا موفقیت‌آمیز باشد، فیلد `"error"` به‌طور کامل حذف می‌شود.

**پاسخ برونداد (`stdout`):**

```
{}
```

ازآنجایی‌که قلاب‌های پس‌ابزار فقط برای کارهای پس‌زمینه‌ای مثل قالب‌بندی کد یا ثبت گزارش اجرا می‌شوند، زمان اجرا هر مقدار تصمیم برگشتی در `stdout` را نادیده می‌گیرد.

## کاوش پیکربندی

زمان اجرا به‌طور خودکار تعریف‌های قلاب را از `.agents/hooks.json` یا `/.agents/hooks.json` در محیط جعبه شنی پیدا می‌کند. می‌توانید `hooks.json` را درکنار دستورگان‌های سفارشی‌تان بااستفاده از هر [منبع محیط](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa#mount_from_a_source) پشتیبانی‌شده‌ای ارائه دهید:

- **نصب مخزن**: مخزن Git حاوی `.agents/hooks.json` در کنار `AGENTS.md`.
- **Cloud Storage‏ (`gcs`)**: مخزن GCS حاوی `hooks.json` که در محیط کپی شده است.
- **منابع درون‌خطی**: رشته JSON خام و محتوای دستورگان که هنگام فراخوانی `client.interactions.create` در `environment.sources` ارسال می‌شود.

### ‫`hooks.json` طرح‌واره

فایل `hooks.json` تعاریف رویداد (`pre_tool_execution` یا `post_tool_execution`) را تحت نام‌های سفارشی گروه‌بندی می‌کند. می‌توانید هر گروه را به‌طور مستقل فعال یا غیرفعال کنید:

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

### قواعد و نحو تطبیق‌دهنده

هر گروه قانون در `hooks.json` تعریف می‌کند که کنترل‌کننده‌ها بااستفاده از ویژگی‌های `matcher` و `hooks` چه زمانی و چگونه فعال شوند:

| فیلد | نوع | شرح |
| --- | --- | --- |
| `enabled` | `boolean` | اختیاری. برای غیرفعال کردن گروه، روی `false` تنظیم کنید (به‌طور پیش‌فرض `true` است). |
| `matcher` | `string` | الگوی عبارت باقاعده که با نام‌های ابزار هدف در داخل محتوی مطابقت دارد. |
| `hooks` | `array` | فهرست مرتب‌شده تعریف‌های کنترل‌کننده (`command` یا `http`). کنترل‌کننده‌ها به‌ترتیب در ترتیب بیانیه اجرا می‌شوند. |

#### نحوه عملکرد ارزیابی عبارت باقاعده

وقتی عامل ابزاری را در محیط امن فراخوانی می‌کند، زمان اجرا نام ظرف ابزار را با الگوی `matcher` شما بااستفاده از عبارات منظم استاندارد RE2 ارزیابی می‌کند. اگر عبارت باقاعده با نام ابزار مطابقت داشته باشد، همه کنترل‌کننده‌های موجود در آرایه `hooks` به‌ترتیب اجرا می‌شوند. اگر چند گروه قانون با ابزار یکسانی مطابقت داشته باشند، همه آرایه‌های گرداننده مربوطه اجرا می‌شوند.

می‌توانید هر نام ابزار داخلی ظرف را هدف‌یابی کنید: اجرای کد (`code_execution`) یا عملیات سیستم فایل (`view_file`،‏ `write_to_file`،‏ `replace_file_content`،‏ `list_dir`، و `delete_file`).

#### عبارت‌های تطبیق‌دهنده رایج

- `"code_execution"`: مطابقت دقیق رشته برای دستورات پوسته و اجرای دستورگان.
- ‫`"write_to_file"`: مطابقت دقیق برای ایجاد فایل سیستم فایل و نوشتن روی دیسک.
- ‫`"view_file|write_to_file"`: جداسازی با خط لوله با چندین نام ابزار خاص در یک قانون مطابقت دارد.
- ‫`".*_file"`: مطابقت گل‌دار Regex با هر ابزاری که به `_file` ختم می‌شود (مثل `view_file`،‏ `write_to_file`، یا `delete_file`). این فقط بخشی از مجموعه ابزار سیستم فایل را پوشش می‌دهد، `replace_file_content` و `list_dir` به `_file` ختم نمی‌شوند، بنابراین وقتی به آن‌ها نیاز دارید، نامشان را به‌طور صریح ذکر کنید. عبارت‌های باقاعده RE2 استاندارد به `.*` نیاز دارند؛ globهای پوسته ساده مثل `*_file` ساختار عبارت باقاعده نامعتبر هستند و مطابقت پیدا نمی‌کنند.
- `".*"` یا `"*"` یا `""`: الگوی فراگیری که هر تماس ابزاری را در محتوی رهگیری می‌کند.

## انواع مدیریت‌کننده

### قلاب‌های فرمان

قلاب‌های فرمان، فرمان یا متن پوسته‌ای را در محیط امن اجرا می‌کنند. نوشتار JSON رویداد را در `stdin` دریافت می‌کند و JSON تصمیم خود را در `stdout` برون‌برد می‌کند.

| فیلد | نوع | شرح |
| --- | --- | --- |
| `type` | `string` | باید `"command"` باشد. |
| `command` | `string` | خط فرمان برای اجرا در جعبه شنی (برای مثال، `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | مهلت زمانی برحسب ثانیه. پیش‌فرض: `30`. |

### قلاب‌های HTTP

قلاب‌های HTTP رویداد JSON را به‌عنوان درخواست POST مستقیماً از داخل شبکه sandbox به نشانی وب HTTPS خارجی ارسال می‌کنند. کارساز هدف تصمیم خود را در بدنه پاسخ HTTP بااستفاده از همان قالب JSON (`{"decision": "allow"}` یا `{"decision": "deny", "reason": "..."}`) برمی‌گرداند.

| فیلد | نوع | شرح |
| --- | --- | --- |
| `type` | `string` | باید `"http"` باشد. |
| `url` | `string` | نقطه پایانی HTTPS خارجی برای ارسال محتوای رویداد. |
| `headers` | `object` | جفت‌های کلید-مقدار اختیاری برای سرایندهای سفارشی غیرحساس (مثل `{"X-Event-Source": "agent-sandbox"}`). برای اصالت‌سنجی، به‌جای آن از [اطلاعات اعتباری](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) در فهرست مجاز شبکه استفاده کنید. |
| `timeout` | `integer` | مهلت زمانی برحسب ثانیه. پیش‌فرض: `30`. |

#### پراکسی خروجی و تبدیل کد

ازآنجایی‌که قلاب‌های HTTP مستقیماً از داخل فضای نام شبکه sandbox اجرا می‌شوند، درخواست‌های خروجی ازطریق پراکسی خروجی شفاف ارسال می‌شوند. این معماری ۲ مزیت امنیتی مهم به شما می‌دهد:

- **فهرست مجاز شبکه:** نقاط پایانی هدف باید به‌طور صریح در `network.allowlist` محیط شما مجاز باشند. ترافیک حلقه برگشتی (`127.0.0.1` یا `localhost`) توسط پراکسی مسدود شده است؛ همیشه نقطه‌های پایانی خارجی فهرست مجازها را هدف‌یابی کنید.
- **تزریق اطلاعات اعتباری:** نیازی نیست کلیدهای میانای برنامه‌سازی کاربردی یا کد حامل مخفی را در `.agents/hooks.json` ذخیره کنید یا آن‌ها را در محتوی نصب کنید. رمز را یک‌بار به‌عنوان [اطلاعات اعتباری](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) ذخیره کنید و بااستفاده از شناسه آن در `network.allowlist` محیطتان به آن ارجاع دهید. کارگزار خروجی به‌طور خودکار ترافیک قلاب HTTP خروجی را رهگیری می‌کند و سرصفحه اصالت‌سنجی واقعی را قبل‌از خروج از محیط آزمایشی به سیم تزریق می‌کند. قوانین `transform` درون‌خطی سرصفحه‌ها را به همان روش در سیم تنظیم می‌کند، اعتبارنامه‌ای که باید هنگام استفاده مجدد از رمز در سراسر پروژه و چرخش آن در یک مکان استفاده کنید. به [پیکربندی شبکه](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa#network-configuration) مراجعه کنید.

## نحوه مدیریت تصمیمات و خطاها توسط زمان اجرا

- **انتظار هم‌زمان:** نماینده متوقف می‌شود و منتظر می‌ماند تا قلاب‌های شما تمام شود و سپس ادامه می‌دهد.
- **مسدود کردن اجرای ابزار:** اگر قلاب پیش‌ابزار شما `{"decision": "deny", "reason": "<your reason>"}` برگرداند، زمان اجرا بلافاصله تماس ابزار را لغو می‌کند. مدل دلیل رد کردن شما را در سابقه مکالمه‌اش می‌بیند و با انتخاب جایگزین ایمن یا توضیح دادن مسدود شدن به کاربر، خود را تطبیق می‌دهد.
- **مدیریت خرابی‌های دستورگان، خطاهای HTTP، و زمان‌های اتمام:** اگر دستورگان فرمان خراب شود (وضعیت خروج غیرصفر)، قلاب HTTP کد وضعیت غیر2xx (مثل خطای سرور 4xx یا 5xx) برگرداند، یا عملیات زمان اتمام داشته باشد یا JSON غیرقابل‌تشخیص برگرداند، زمان اجرا آن را به‌عنوان تأیید درنظر می‌گیرد (`allow`). اجرای ابزار به‌طور عادی ادامه می‌یابد، بنابراین دستورگان خراب یا سرور تله‌متری غیرقابل‌دسترس هرگز باعث توقف برنامه شما نمی‌شود.

## موارد استفاده رایج

### بازیابی چند مرحله‌ای برای حریم خصوصی داده‌ها و رعایت استانداردها

وقتی قلابی دسترسی به منابع محدودشده را مسدود می‌کند—مثلاً فهرستگان حاوی «اطلاعات شناساننده شخصی» (PII) یا سوابق مالی محرمانه—می‌توانید `previous_interaction_id` را در تماس بعدی ارسال کنید تا چرخش در همان محیط ادامه یابد. کارگزار توضیح رد را می‌خواند و به‌جای آن با پُرسمان کردن از جدول‌های عمومی تأییدشده به‌طور خودکار بازیابی می‌کند.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "view_file",
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
    agent="antigravity-preview-09-2026",
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
    agent="antigravity-preview-09-2026",
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
                matcher: "view_file",
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
    agent: "antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
""";

String checkPrivacyScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "path = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\n"
    + "if \"/private/\" in path:\n"
    + "    resp = {\n"
    + "        \"decision\": \"deny\",\n"
    + "        \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"\n"
    + "    }\n"
    + "else:\n"
    + "    resp = {\"decision\": \"allow\"}\n"
    + "print(json.dumps(resp))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/check_privacy.py")
            .content(checkPrivacyScript)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/private/employees.json")
            .content("{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/public/summary.json")
            .content("{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}")
            .build()
    ))
    .build();

// Step 1: Agent attempts to read confidential PII records and is intercepted
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction int1 = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println(int1.outputText().orElse(""));

// Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."))
    .environment(CreateAgentInteractionEnvironment.of(int1.environmentId().orElse("")))
    .previousInteractionId(int1.id().orElse(""))
    .build();

Interaction int2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println(int2.outputText().orElse(""));
```

### رفتن

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

    hooksConfig := `{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}`

    checkPrivacyScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))
if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential '/private/' records is blocked by PII compliance policy. Query approved '/public/' summary tables instead."
    }
else:
    resp = {"decision": "allow"}
print(json.dumps(resp))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/check_privacy.py"),
                Content: genai.Ptr(checkPrivacyScript),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/private/employees.json"),
                Content: genai.Ptr(`{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}`),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/public/summary.json"),
                Content: genai.Ptr(`{"department": "Engineering", "team_size": 42, "status": "active"}`),
            },
        },
    }

    // Step 1: Agent attempts to read confidential PII records and is intercepted
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    int1 := res1.Interaction
    if int1.OutputText != nil {
        fmt.Println(*int1.OutputText)
    }

    // Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*int1.EnvironmentID)),
            PreviousInteractionID: int1.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println(*res2.Interaction.OutputText)
    }
}
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"view_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
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
#       "agent": "antigravity-preview-09-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### گزارش‌گیری و تله‌متری ممیزی خارجی

هرگاه فایل‌ها خوانده یا اصلاح می‌شوند، رویدادهای ممیزی هم‌زمان را از داخل محیط آزمایشی به سرور پایش خارجی ارسال کنید.

- **مطابقت با چندین ابزار:** ازآنجایی‌که مطابقت‌دهنده‌ها از عبارت باقاعده استاندارد استفاده می‌کنند، می‌توانید چندین ابزار را بااستفاده از خط لوله (`view_file|write_to_file|replace_file_content`) یا نویسه‌های عام (`.*_file`) در یک قانون ترکیب کنید.
- **رمزها را از پیکربندی‌تان خارج کنید:** نشان اصالت‌سنجی را به‌عنوان [اطلاعات اعتباری](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) ذخیره کنید و آن را با شناسه از [پیکربندی شبکه](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa#network-configuration) محیطتان (`network.allowlist.credential`) ارجاع دهید. کارگزار خروجی نشان حامل واقعی را در درخواست‌های خروجی تزریق می‌کند. این مثال سرایند را به‌جای آن با `transform` درخط تنظیم می‌کند که با همان پراکسی محافظت می‌شود و وقتی که نشان به این پیکربندی تعلق داشته باشد، مناسب است.

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
                "matcher": "view_file|write_to_file|replace_file_content",
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
    agent="antigravity-preview-09-2026",
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
                matcher: "view_file|write_to_file|replace_file_content",
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
    agent: "antigravity-preview-09-2026",
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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// Define hook without secrets; the egress proxy injects headers dynamically
String hooksConfig = """
{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build()
    ))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("telemetry.example.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer telemetry_secret_token_123"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("*").build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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

    // Define hook without secrets; the egress proxy injects headers dynamically
    hooksConfig := `{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "telemetry.example.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer telemetry_secret_token_123",
                    })),
                },
                {
                    Domain: "*",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"view_file|write_to_file|replace_file_content\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
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

## محدودیت‌ها

- **محدوده ابزار جعبه امن:** قلاب‌ها ابزارهای داخلی را در جعبه امن رهگیری می‌کنند: اجرای کد (`code_execution`) و عملیات سیستم فایل (`view_file`،‏ `write_to_file`،‏ `replace_file_content`،‏ `list_dir`، و `delete_file`). این قلاب‌ها برای فراخوانی تابع سفارشی (`function`) یا ابزارهای خارجی «پروتکل بافتار مدل» (`mcp_server`) که در خارج از محتوی مدیریت می‌شوند فعال نمی‌شوند.
- **فهرست‌های مجاز شبکه:** قلاب‌های HTTP در شبکه محتوی اجرا می‌شوند. باید نشانی‌های وب هدف را به‌طور صریح در `network.allowlist` محیطتان مجاز کنید. نشانی‌های مسیریابی بازگشتی (`localhost`، `127.0.0.1`) توسط پراکسی مسدود شده است.
- **تأیید خودکار درصورت بروز خطا:** اگر یک دستورگان قلاب ازکار بیفتد (وضعیت خروجی غیرصفر)، زمان آن تمام شود، یا ناموفق باشد، زمان اجرا این خرابی را ثبت می‌کند و به تماس ابزار اجازه می‌دهد ادامه یابد. این کار تضمین می‌کند که برنامه‌های شما هرگز به‌دلیل خراب شدن دستورگان‌های linter یا فرایندهای معلق دچار بن‌بست نمی‌شوند.
- **محافظت از پیکربندی جعبه امن:** ازآنجایی‌که قلاب‌ها در جعبه امن محتوی اجرا می‌شوند، کارگزاران دارای ابزارهای نوشتن سیستم فایل یا اجازه‌های اجرای کد پوسته می‌توانند `.agents/hooks.json` محلی یا دستورگان‌های موجود در فضای کاری نوشتنی را تغییر دهند. از قلاب‌های محتوی به‌عنوان راهنمایی خودکارسازی‌شده خط‌مشی و نرده‌های محافظ عملیاتی استفاده کنید؛ اگر مقاومت دربرابر دستکاری سخت دربرابر اجرای مدل‌های غیرقابل‌اعتماد لازم است، منابع پیکربندی را از مخازن فقط‌خواندنی نصب کنید.

## قدم بعدی چیست

- با نحوه پیکربندی [محیط‌ها و جعبه‌های ایمنی از راه دور](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa) ماندگار آشنا شوید.
- توانمندی‌ها و ابزارهای داخلی [عامل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fa) را کاوش کنید.
- برای جلسات چند نوبتی و جاری‌سازی، [نمای کلی «میانای برنامه‌سازی کاربردی تعامل‌ها»](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fa) را مرور کنید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-07 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-07 به‌وقت ساعت هماهنگ جهانی."],[],[]]
