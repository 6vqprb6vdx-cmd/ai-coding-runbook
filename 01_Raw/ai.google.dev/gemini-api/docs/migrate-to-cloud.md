---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=fa
fetched_at: 2026-11-02T07:24:27.801358+00:00
title: "\u0645\u0642\u0627\u06cc\u0633\u0647 Gemini Developer API \u0648 \u067e\u0644\u0627\u062a\u0641\u0631\u0645 Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# مقایسه Gemini Developer API و پلاتفرم Gemini

هنگام توسعه راه‌حل‌های هوش مصنوعی زایا با Gemini،‏ Google دو محصول API ارائه می‌دهد: [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=fa) و [Gemini platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=fa).

‫Gemini Developer API سریع‌ترین مسیر را برای ساختن، تولید کردن، و
مقیاس‌بندی برنامه‌های با بهره‌گیری از Gemini فراهم می‌کند. اکثر توسعه‌دهندگان باید از «میانای برنامه‌سازی کاربردی توسعه‌دهندگان Gemini» استفاده کنند، مگراینکه نیاز به کنترل‌های سازمانی خاصی باشد.

پلاتفرم Gemini اکوسیستم جامعی از ویژگی‌ها و سرویس‌های آماده برای شرکت‌ها
برای ساختن و استقرار دادن برنامه‌های هوش مصنوعی زایا با پشتیبانی
Google Cloud ارائه می‌دهد.

اخیراً انتقال بین این سرویس‌ها را ساده‌تر کرده‌ایم. اکنون هم Gemini
Developer API و هم Gemini platform API ازطریق [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=fa) یکپارچه و
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fa) دردسترس هستند.

## مقایسه کد: Interactions API (توصیه‌شده)

[میانای برنامه‌سازی کاربردی تعاملات](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fa) روش توصیه‌شده برای ساختن با مدل‌ها و نمایندگان Gemini است. مثال‌های زیر
تولید نوشتار را بین Gemini Developer API و پلاتفرم Gemini مقایسه می‌کند.

### Python

می‌توانید ازطریق کتابخانه `google-genai` (`>= 2.3.0`) به Gemini Developer API و خدمات پلاتفرم Gemini دسترسی پیدا کنید.
برای دستورالعمل‌های نصب `google-genai`، به صفحه
[کتابخانه‌ها](https://ai.google.dev/gemini-api/docs/libraries?hl=fa) مراجعه کنید.

### Gemini Developer API

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### Gemini platform API

```
from google import genai

client = genai.Client(
    enterprise=True, project="your-project-id", location="global"
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### جاوا اسکریپت و تایپ‌اسکریپت

می‌توانید ازطریق کتابخانه `@google/genai` (`>= 2.3.0`) به Gemini Developer API و خدمات پلاتفرم Gemini دسترسی داشته باشید.
برای دستورالعمل‌های نصب `@google/genai`، صفحه [کتابخانه‌ها](https://ai.google.dev/gemini-api/docs/libraries?hl=fa) را ببینید.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### Gemini platform API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  enterprise: true,
  project: "your_project",
  location: "global",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

## مقایسه کد: generateContent API

اگرچه «میانای برنامه‌سازی کاربردی تعامل‌ها» برای پروژه‌های جدید توصیه می‌شود،
`generateContent` API همچنان پشتیبانی می‌شود.

### Python

ازطریق کتابخانه `google-genai` می‌توانید به Gemini Developer API و سرویس‌های پلاتفرم Gemini دسترسی داشته باشید. برای دریافت دستورالعمل‌های مربوط به نحوه نصب
`google-genai`، صفحه
[کتابخانه‌ها](https://ai.google.dev/gemini-api/docs/libraries?hl=fa) را ببینید.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### جاوا اسکریپت و تایپ‌اسکریپت

می‌توانید ازطریق کتابخانه `@google/genai` به هر دو سرویس Gemini Developer API و پلاتفرم Gemini دسترسی داشته باشید. برای دریافت دستورالعمل‌های مربوط به نحوه نصب
`@google/genai`، به صفحه
[کتابخانه‌ها](https://ai.google.dev/gemini-api/docs/libraries?hl=fa) مراجعه کنید.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### رفتن

می‌توانید ازطریق کتابخانه `google.golang.org/genai` به هر دو سرویس Gemini Developer API و پلاتفرم Gemini دسترسی داشته باشید. برای دریافت دستورالعمل‌های مربوط به نحوه نصب
`google.golang.org/genai`، به صفحه
[کتابخانه‌ها](https://ai.google.dev/gemini-api/docs/libraries?hl=fa) مراجعه کنید.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google Cloud project
const project = "your-project"

// A Google Cloud location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### سایر موارد استفاده و پلاتفرم‌ها

برای پلاتفرم‌ها و موارد استفاده دیگر، به راهنماهای ویژه مورد استفاده در [اسناد Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=fa)
و [اسناد پلاتفرم Gemini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=fa)
مراجعه کنید.

## ملاحظات انتقال

وقتی انتقال می‌دهید:

- برای اصالت‌سنجی باید از حساب‌های خدمات Google Cloud استفاده کنید. برای اطلاعات بیشتر،
  [مستندات پلاتفرم Gemini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=fa)
  را ببینید.
- می‌توانید از پروژه Google Cloud موجودتان (همان پروژه‌ای که برای تولید کلید API استفاده کردید) استفاده کنید یا می‌توانید [پروژه Google Cloud جدیدی ایجاد کنید](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=fa).
- مناطق پشتیبانی‌شده ممکن است بین Gemini Developer API و
  Gemini platform API متفاوت باشد. درطول «پیش‌نمایش»،
  [میانای برنامه‌سازی کاربردی «تعاملات» در پلاتفرم Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=fa)
  فقط از نقطه پایانی `global` (`location="global"`) پشتیبانی می‌کند. فهرست
  [مناطق پشتیبانی‌شده برای هوش مصنوعی زایا در Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=fa) را ببینید.
- هر مدلی که در Google AI Studio ساخته‌اید باید در پلاتفرم Gemini بازآموزی شود.

اگر دیگر نیازی به استفاده از کلید Gemini API برای Gemini Developer API ندارید،
روال‌های مطلوب امنیتی را دنبال کنید و آن را حذف کنید.

برای حذف کلید میانای API:

1. صفحه
   [اطلاعات اعتباری Google Cloud API](https://console.cloud.google.com/apis/credentials?hl=fa)
   را باز کنید.
2. کلید API موردنظر برای حذف را پیدا کنید و روی نماد **کنش‌ها** کلیک کنید.
3. **حذف کلید API** را انتخاب کنید.
4. در مدال **حذف اطلاعات اعتباری**، **حذف** را انتخاب کنید.

   حذف کلید API چند دقیقه طول می‌کشد تا منتشر شود. پس‌از تکمیل
   انتشار، هرگونه ترافیک که از کلید API حذف‌شده استفاده کند رد می‌شود.

## مراحل بعدی

- راهنمای توسعه‌دهندگان
  [میانای برنامه‌سازی کاربردی تعاملات در پلاتفرم Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=fa)
  را کاوش کنید.
- برای کسب اطلاعات بیشتر درباره راه‌حل‌های هوش مصنوعی زایا در پلاتفرم Gemini،
  [نمای کلی هوش مصنوعی زایا در پلاتفرم Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=fa)
  را ببینید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-08 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-08 به‌وقت ساعت هماهنگ جهانی."],[],[]]
