---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=fa
fetched_at: 2026-10-19T05:39:47.087929+00:00
title: "\u067e\u0627\u06cc\u0647\u200c\u0645\u0646\u062f\u0633\u0627\u0632\u06cc \u0628\u0627 \u00ab\u062c\u0633\u062a\u062c\u0648\u06cc Google\u00bb \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# پایه‌مندسازی با «جستجوی Google»

«پایه‌گذاری با جستجوی Google» مدل Gemini را به محتوای وب هم‌زمان متصل می‌کند
و با همه زبان‌های دردسترس کار می‌کند. این کار به Gemini امکان می‌دهد پاسخ‌های دقیق‌تری ارائه دهد و منابع قابل‌تأیید را فراتر از تاریخ برش دانش خود نقل کند.

زمینه‌سازی به شما کمک می‌کند برنامه‌هایی بسازید که می‌توانند:

- **افزایش دقت واقعی:** با قرار دادن اطلاعات دنیای واقعی به‌عنوان مبنای پاسخ‌ها، توهمات مدل را کاهش دهید.
- **دسترسی به اطلاعات هم‌زمان:** به سؤالات مربوط به رویدادها و موضوعات اخیر پاسخ دهید.
- **ارائه استناد:** با نشان دادن منابع ادعاهای مدل، اعتماد کاربر را جلب کنید.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## نحوه عملکرد پایه‌مندسازی با «جستجوی Google»

وقتی ابزار `google_search` را فعال می‌کنید، مدل کل گردش کار جستجو، پردازش، و استناد به اطلاعات را به‌طور خودکار انجام می‌دهد.

![نمای کلی پایه‌مندسازی](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=fa)

1. **پیام‌واره کاربر:** برنامه شما پیام‌واره کاربر را به Gemini API
   با ابزار `google_search` فعال ارسال می‌کند.
2. **تحلیل پیام‌واره:** مدل پیام‌واره را تحلیل می‌کند و تعیین می‌کند که آیا «جستجوی Google» می‌تواند پاسخ را بهبود بخشد یا نه.
3. **جستجوی Google:** درصورت نیاز، مدل به‌طور خودکار یک یا چند پرسمان جستجو تولید و اجرا می‌کند.
4. **پردازش نتایج جستجو:** مدل نتایج جستجو را پردازش می‌کند،
   اطلاعات را ترکیب می‌کند، و پاسخی را فرمول‌بندی می‌کند.
5. **پاسخ پایه‌مند:** میانای برنامه‌سازی کاربردی پاسخ نهایی کاربرپسندی را برمی‌گرداند که
   بر نتایج جستجو پایه‌مند شده است. این پاسخ شامل پاسخ نوشتاری مدل با `annotations` درون‌خطی حاوی استنادها، و همچنین `google_search_call` و `google_search_result` مرحله با پُرسمان‌های جستجو و پیشنهادهای جستجو است.

## آشنایی با پاسخ مستندسازی

وقتی پاسخ باموفقیت زمینه‌دار می‌شود، برونداد نوشتاری مدل شامل
`annotations` به‌خط مستقیم در بلوک محتوای نوشتاری است. این گزارمان‌ها
اطلاعات استنادی ارائه می‌دهند که بخش‌های پاسخ را به منابع آن‌ها پیوند می‌دهد.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

فیلدهای کلیدی در پاسخ:

- ‫`google_search_call` : شامل جستجویی است که مدل `queries` اجرا کرده است.
- `google_search_result` : حاوی `search_suggestions`، یک قطعه HTML
  برای ارائه پیشنهادهای جستجو در واسط کاربر شما. جزئیات کامل شرایط استفاده در [شرایط خدمات](https://ai.google.dev/gemini-api/terms?hl=fa#grounding-with-google-search) آمده است.
- `text` با `annotations` : پاسخ ترکیبی مدل با استنادهای درون‌خطی. هر حاشیه‌نویسی `url_citation` یک بخش نوشتار (تعریف‌شده
  توسط `start_index` و `end_index`) را به نشانی وب منبع پیوند می‌دهد. این کلید ساختن
  نقل‌قول‌های درون‌خطی است.

از «پایه‌مندسازی با جستجوی Google» می‌توان در ترکیب با [ابزار بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa) نیز استفاده کرد تا پاسخ‌ها هم براساس داده‌های وب عمومی و هم براساس نشانی‌های وب خاصی که ارائه می‌دهید پایه‌مندسازی شوند.

## نسبت دادن منابع با استنادهای به‌خط

این API حاشیه‌نویسی‌های `url_citation` درون‌خطی را در بلوک محتوای نوشتاری برمی‌گرداند،
و به شما کنترل کامل بر نحوه نمایش منابع در میانای کاربر می‌دهد.
هر گل‌نویسی شامل `start_index` و `end_index` است تا مشخص کند به کدام بخش از نوشتار ارجاع می‌دهد. در اینجا نحوه استخراج و نمایش آن‌ها آورده شده است.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            String text = textContent.text().orElse("");
            System.out.println(text);
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nCitations:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof URLCitation) {
                  URLCitation citation = (URLCitation) annotation;
                  int start = citation.startIndex().orElse(0);
                  int end = citation.endIndex().orElse(0);
                  String citedText =
                      (start >= 0 && end <= text.length() && start <= end)
                          ? text.substring(start, end)
                          : "";
                  System.out.printf(
                      "  [%s](%s)%n", citation.title().orElse(""), citation.url().orElse(""));
                  System.out.printf("    Cited text: \"%s\"%n", citedText);
                }
              }
            }
          }
        }
      }
    }
  }
}
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    text := content.TextContent.Text
                    fmt.Println(text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nCitations:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                c := annotation.URLCitation
                                start := 0
                                if c.StartIndex != nil {
                                    start = *c.StartIndex
                                }
                                end := 0
                                if c.EndIndex != nil {
                                    end = *c.EndIndex
                                }
                                citedText := ""
                                if start >= 0 && end <= len(text) && start <= end {
                                    citedText = text[start:end]
                                }
                                title := ""
                                if c.Title != nil {
                                    title = *c.Title
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  [%s](%s)\n", title, url)
                                fmt.Printf("    Cited text: %q\n", citedText)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

برونداد نوشتار را به‌همراه فهرست منابع آن نشان می‌دهد:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## قیمت‌گذاری

وقتی از «پایه‌مندسازی با جستجوی Google» با Gemini 3 و مدل‌های جدیدتر استفاده می‌کنید،
پروژه شما برای **هر** پرسمان جستجویی که مدل تصمیم به اجرای آن می‌گیرد صورت‌حساب دریافت می‌کند.
این مدل صورت‌حساب براساس پُرسمان شامل ۵٬۰۰۰ درخواست جستجوی رایگان در ماه است که بین همه مدل‌های Gemini 3 و جدیدتر مشترک است و سپس هزینه آن **۱۴ دلار به‌ازای هر ۱٬۰۰۰ درخواست جستجو** است.

برای مثال، اگر مدل تصمیم بگیرد برای پاسخ دادن به یک پیام‌واره واحد، چندین پُرسمان جستجو اجرا کند (برای نمونه، جستجوی `"UEFA Euro 2024 winner"` و `"Spain vs
England Euro 2024 final score"` در همان فراخوانی API)، این به‌عنوان دو استفاده صورت‌حساب‌پذیر از ابزار برای آن درخواست محاسبه می‌شود. برای اهداف صورت‌حساب،
پرسمان‌های جستجوی وب خالی را هنگام شمارش پرسمان‌های یکتا نادیده می‌گیریم.

وقتی از «پایه جستجو» با Gemini 2.5 یا مدل‌های قدیمی‌تر استفاده می‌کنید، هزینه پروژه شما براساس هر پیام‌واره محاسبه می‌شود.

برای اطلاعات دقیق درباره قیمت‌گذاری، به [صفحه قیمت‌گذاری Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) مراجعه کنید.

## مدل‌های پشتیبانی‌شده

می‌توانید قابلیت‌های کامل را در صفحه [نمای کلی
مدل](https://ai.google.dev/gemini-api/docs/models?hl=fa) پیدا کنید.

| مدل | پایه‌مندسازی با جستجوی Google |
| --- | --- |
| ‫Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| پیش‌نمایش تصویر Gemini 3.1 Flash | ✔️ |
| پیش‌نمایش Gemini 3.1 Pro | ✔️ |
| پیش‌نمایش تصویر Gemini 3 Pro | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| ‫Gemini 2.5 Pro | ✔️ |
| ‫Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## ترکیب‌های ابزار پشتیبانی‌شده

می‌توانید از «پایه با جستجوی Google» با ابزارهای دیگر مثل
[اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)،
[زمینه نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)، و
[پایه با Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fa) (پشتیبانی‌شده در
Gemini 3.5 Flash-Lite و مدل‌های جدیدتر) برای تقویت موارد استفاده پیچیده‌تر استفاده کنید.
مدل‌های Gemini 3 همچنین از ترکیب این ابزارهای داخلی با ابزارهای سفارشی (فراخوانی تابع) پشتیبانی می‌کنند. در صفحه
[ترکیب‌های ابزار](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fa) بیشتر بدانید.

## قدم بعدی چیست

- با ابزارهای دردسترس دیگر، مثل [فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa)، آشنا شوید.
- با نحوه تقویت پیام‌واره‌ها با نشانی‌های وب خاص بااستفاده از [ابزار بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa) آشنا شوید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-13 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-13 به‌وقت ساعت هماهنگ جهانی."],[],[]]
