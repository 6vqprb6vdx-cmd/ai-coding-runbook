---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=fa
fetched_at: 2026-10-19T05:44:23.685835+00:00
title: "\u0631\u0627\u0647\u0646\u0645\u0627\u06cc \u062a\u0648\u0633\u0639\u0647\u200c\u062f\u0647\u0646\u062f\u06af\u0627\u0646 Gemini 3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)

ارسال بازخورد

# راهنمای توسعه‌دهندگان Gemini 3

‫Gemini 3 هوشمندترین خانواده مدل‌های ما تا به امروز است که بر پایه استدلال پیشرفته ساخته شده است. این مدل برای جان بخشیدن به هر ایده‌ای با تسلط بر گردش‌های کار عامل‌گرا، کدنویسی خودکار، و تکالیف پیچیده چندوجهی طراحی شده است.
این راهنما ویژگی‌های کلیدی خانواده مدل Gemini 3 و نحوه استفاده حداکثری از آن را پوشش می‌دهد.

[پیش‌نمایش Gemini 3.1 Pro را امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=fa)
[پیش‌نمایش Gemini 3 Flash را امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=fa)
[پیش‌نمایش Gemini 3.1 Flash-Lite را امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=fa)
[پیش‌نمایش Nano Banana 2 را امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=fa)

[مجموعه برنامه‌های Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=fa) ما را کاوش کنید تا ببینید این مدل چگونه از پس استدلال پیشرفته، کدنویسی خودکار، و وظایف پیچیده چندوجهی برمی‌آید.

با چند خط کد شروع کنید:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## با سری Gemini 3 آشنا شوید

‫Gemini 3.1 Pro برای تکالیف پیچیده‌ای که
به دانش جهانی گسترده و استدلال پیشرفته در حالت‌های مختلف نیاز دارند بهترین است.

‫Gemini 3 Flash جدیدترین مدل سری ۳ ما است که هوشمندی سطح Pro را با سرعت و قیمت Flash ارائه می‌دهد.

‫Nano Banana Pro (که با نام Gemini 3 Pro Image نیز شناخته می‌شود) باکیفیت‌ترین مدل تولید تصویر ما است و Nano Banana 2 (که با نام Gemini 3.1 Flash Image نیز شناخته می‌شود) معادل با حجم بالا، کارایی بالا، و قیمت پایین‌تر است.

‫Gemini 3.1 Flash-Lite مدل کارآمد ما است که برای مدل مقرون‌به‌صرفه و
کارهای با حجم بالا ساخته شده است.

| شناسه مدل | پنجره بافت (درون / بیرون) | تاریخ برش دانش | قیمت‌گذاری (ورودی / خروجی)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | ‫۱ میلیون / ۶۴ هزار | ژانویه ۲۰۲۵ | ۰٫۲۵ دلار (نوشتار، تصویر، ویدیو)، ۰٫۵۰ دلار (صوت) / ۱٫۵۰ دلار |
| **gemini-3.1-flash-image-preview** | ‫۱۲۸ هزار / ۳۲ هزار | ژانویه ۲۰۲۵ | ۰٫۲۵ دلار (ورودی نوشتار) / ۰٫۰۶۷ دلار (برونداد تصویر)\*\* |
| **gemini-3.1-pro-preview** | ‫۱ میلیون / ۶۴ هزار | ژانویه ۲۰۲۵ | ۲ دلار / ۱۲ دلار (<۲۰۰ هزار داده‌واحد)   ۴ دلار / ۱۸ دلار (>۲۰۰ هزار داده‌واحد) |
| **gemini-3-flash-preview** | ‫۱ میلیون / ۶۴ هزار | ژانویه ۲۰۲۵ | ۰.۵۰ دلار / ۳ دلار |
| **gemini-3-pro-image-preview** | ‫۶۵ هزار / ۳۲ هزار | ژانویه ۲۰۲۵ | ۲ دلار (ورودی نوشتار) / ۰٫۱۳۴ دلار (برونداد تصویر)\*\* |

*\* قیمت‌گذاری به‌ازای هر ۱ میلیون داده‌واحد است، مگر اینکه خلاف آن ذکر شده باشد.*
*\*\* قیمت‌گذاری تصویر براساس وضوح متفاوت است. برای جزئیات، [صفحه قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) را ببینید.*

برای اطلاع از حدود استفاده، قیمت‌گذاری، و اطلاعات تکمیلی، به
[صفحه مدل‌ها](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fa) مراجعه کنید.

## ویژگی‌های جدید API در Gemini 3

‫Gemini 3 پارامترهای جدیدی را معرفی می‌کند که برای دادن کنترل بیشتر به توسعه‌دهندگان بر
تأخیر، هزینه، و دقت چندوجهی طراحی شده‌اند.

### سطح «اندیشگر»

مدل‌های سری Gemini 3 به‌طور پیش‌فرض از اندیشیدن پویا برای استدلال کردن درباره پیام‌واره‌ها استفاده می‌کنند. می‌توانید از پارامتر `thinking_level` استفاده کنید که
**حداکثر** عمق فرایند استدلال داخلی مدل را قبل‌از تولید پاسخ کنترل می‌کند. ‫Gemini 3 این سطوح را به‌عنوان سهمیه‌های نسبی برای تفکر درنظر می‌گیرد
نه تضمین‌های دقیق برای تعداد نشان‌ها.

اگر `thinking_level` مشخص نشده باشد، Gemini 3 به‌طور پیش‌فرض روی `high` تنظیم می‌شود. برای
پاسخ‌های سریع‌تر و با تأخیر کمتر در مواقعی که استدلال پیچیده لازم نیست، می‌توانید
سطح تفکر مدل را به `low` محدود کنید.

| سطح اندیشگر | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | شرح |
| --- | --- | --- | --- | --- |
| **`minimal`** | پشتیبانی نمی‌شود | پشتیبانی‌شده (پیش‌فرض) | پشتیبانی‌شده | برای اکثر پُرسمان‌ها با تنظیم «بدون فکر کردن» مطابقت دارد. این مدل ممکن است برای تکالیف پیچیده کدنویسی بسیار کم فکر کند. تأخیر را برای گپ یا برنامه‌های با توان عملیاتی بالا به حداقل می‌رساند. توجه داشته باشید که `minimal` تضمین نمی‌کند که فکر کردن خاموش باشد. |
| **`low`** | پشتیبانی‌شده | پشتیبانی‌شده | پشتیبانی‌شده | تأخیر و هزینه را به حداقل می‌رساند. برای پیروی از دستورالعمل‌های ساده، گپ، یا برنامه‌های با توان عملیاتی بالا بهترین است. |
| **`medium`** | پشتیبانی‌شده | پشتیبانی‌شده | پشتیبانی‌شده | اندیشیدن متوازن برای اکثر تکالیف. |
| **`high`** | پشتیبانی‌شده (پیش‌فرض، پویا) | پشتیبانی‌شده (پویا) | پشتیبانی‌شده (پیش‌فرض، پویا) | عمق استدلال را به حداکثر می‌رساند. مدل ممکن است زمان بسیار بیشتری طول بکشد تا به اولین واحد خروجی (غیرفکر کردن) برسد، اما خروجی با دقت بیشتری استدلال خواهد شد. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### وضوح رسانه

‫Gemini 3 بااستفاده از پارامتر `media_resolution` کنترل دقیق‌تری بر پردازش دید چندحالته ارائه می‌دهد. وضوح بالاتر توانایی مدل را در
خواندن نوشتار ریز یا شناسایی جزئیات کوچک بهبود می‌بخشد، اما استفاده از نشان و تأخیر را افزایش می‌دهد.
پارامتر `media_resolution` **حداکثر تعداد نشانه‌ها
اختصاص‌داده‌شده به هر تصویر ورودی یا قاب ویدیو** را تعیین می‌کند.

اکنون می‌توانید وضوح را روی `media_resolution_low`،
`media_resolution_medium`، `media_resolution_high`، یا
`media_resolution_ultra_high` برای هر بخش رسانه به‌صورت جداگانه یا به‌صورت جهانی (ازطریق
`generation_config`، جهانی برای وضوح فوق‌العاده بالا دردسترس نیست) تنظیم کنید. اگر مشخص نشده باشد، مدل از پیش‌فرض‌های بهینه براساس نوع رسانه استفاده می‌کند.

**تنظیمات توصیه‌شده**

| نوع رسانه | تنظیمات توصیه‌شده | حداکثر داده‌واحد | راهنمای استفاده |
| --- | --- | --- | --- |
| **تصاویر** | `media_resolution_high` | 1120 | برای اکثر تکالیف تجزیه‌وتحلیل تصویر توصیه می‌شود تا حداکثر کیفیت تضمین شود. |
| **PDF** | `media_resolution_medium` | 560 | برای درک سند بهینه است؛ کیفیت معمولاً در `medium` به حد اشباع می‌رسد. افزایش به `high` به‌ندرت نتایج «تبدیل تصویر به نوشتار» را برای سندهای استاندارد بهبود می‌دهد. |
| **ویدیو** (عمومی) | `media_resolution_low` (یا `media_resolution_medium`) | ۷۰ (برای هر قاب) | **توجه:** برای ویدیو، تنظیمات `low` و `medium` به‌طور یکسان (۷۰ واحد) برای بهینه‌سازی استفاده از زمینه درنظر گرفته می‌شوند. این مقدار برای اکثر تکالیف تشخیص و شرح کنش کافی است. |
| **ویدیو** (نوشتار سنگین) | `media_resolution_high` | ۲۸۰ (برای هر قاب) | فقط زمانی لازم است که مورد استفاده شامل خواندن نوشتار فشرده (OCR) یا جزئیات کوچک در قاب‌های ویدیو باشد. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### دما

برای همه مدل‌های Gemini 3، اکیداً توصیه می‌کنیم پارامتر دما را روی مقدار پیش‌فرض `1.0` نگه دارید.

درحالی‌که مدل‌های قبلی اغلب از تنظیم دما برای کنترل خلاقیت دربرابر قطعیت بهره می‌بردند، قابلیت‌های استدلال Gemini 3 برای تنظیمات پیش‌فرض بهینه شده است. تغییر دما (تنظیم آن روی کمتر از ۱٫۰) ممکن است منجر به رفتار غیرمنتظره، مانند حلقه زدن یا عملکرد تنزل‌یافته، به‌ویژه در تکالیف پیچیده ریاضی یا استدلال شود.

### امضاهای فکری

‫Gemini 3 از [امضاهای فکری](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=fa) برای
حفظ زمینه استدلال در سراسر فراخوانی‌های API استفاده می‌کند. این امضاها نمایش‌های رمزگذاری‌شده از فرایند فکری داخلی مدل هستند. برای اطمینان از اینکه مدل
قابلیت‌های استدلال خود را حفظ می‌کند، باید این امضاها را دقیقاً همان‌گونه که دریافت شده‌اند به
مدل در درخواستتان برگردانید:

- **فراخوانی تابع (دقیق):** این API اعتبارسنجی دقیقی را روی
  «نوبت فعلی» اعمال می‌کند. درصورت نبودن امضا، خطای ۴۰۰ دریافت خواهید کرد.
- **نوشتار/گپ:** اعتبارسنجی به‌طور دقیق اجرا نمی‌شود، اما حذف امضاها باعث کاهش کیفیت استدلال و پاسخ مدل می‌شود.
- **تولید/ویرایش تصویر (سخت‌گیرانه)**: «میانای برنامه‌سازی کاربردی» در همه بخش‌های «مدل» ازجمله `thoughtSignature` اعتبارسنجی سخت‌گیرانه اعمال می‌کند. درصورت نبودن امضا، خطای ۴۰۰ دریافت خواهید کرد.

#### فراخوانی تابع (اعتبارسنجی دقیق)

وقتی Gemini `functionCall` تولید می‌کند، برای پردازش صحیح برونداد ابزار در نوبت بعدی، به `thoughtSignature` متکی است. «نوبت فعلی»
شامل همه مراحل «مدل» (`functionCall`) و «کاربر» (`functionResponse`) است که
از زمان آخرین پیام استاندارد **کاربر** `text` رخ داده است.

- **تماس با تابع واحد:** بخش `functionCall` حاوی امضا است. باید آن را برگردانید.
- **فراخوانی‌های تابع موازی:** فقط `functionCall` بخش اول در فهرست حاوی امضا خواهد بود. باید قطعات را دقیقاً به همان ترتیبی که دریافت کرده‌اید برگردانید.
- **چندمرحله‌ای (ترتیبی):** اگر مدل ابزاری را فراخوانی کند، نتیجه‌ای دریافت کند،
  و ابزار *دیگری* را (در همان نوبت) فراخوانی کند، **هر دو** فراخوانی تابع امضا دارند. باید **همه** امضاهای جمع‌آوری‌شده در سابقه را برگردانید.

#### نوشتار و جاری‌سازی

برای گپ استاندارد یا تولید نوشتار، وجود امضا تضمین نمی‌شود.

- **غیر جاری‌سازی**: بخش محتوای نهایی پاسخ ممکن است حاوی
  `thoughtSignature` باشد، اگرچه همیشه وجود ندارد. اگر یکی از آن‌ها برگشت داده شد،
  برای حفظ بهترین عملکرد باید آن را برگردانید.
- **جاری‌سازی**: اگر امضایی تولید شود، ممکن است در یک بخش نهایی که حاوی یک بخش نوشتاری خالی است، دریافت شود. مطمئن شوید که تجزیه‌گر جاری‌سازی شما
  امضاها را حتی اگر فیلد نوشتار خالی باشد بررسی می‌کند.

#### تولید و ویرایش تصویر

برای `gemini-3-pro-image-preview` و `gemini-3.1-flash-image-preview`، امضاهای فکری برای
ویرایش مکالمه‌ای حیاتی هستند. وقتی از مدل می‌خواهید تصویری را تغییر دهد، برای درک ترکیب و منطق تصویر اصلی، به `thoughtSignature` نوبت قبلی متکی است.

- **ویرایش:** امضاها در بخش اول پس‌از افکار پاسخ (`text` یا `inlineData`) و در هر بخش `inlineData`
  بعدی تضمین می‌شوند. برای جلوگیری از خطا، باید همه این امضاها را برگردانید.

#### نمونه‌های کد

#### فراخوانی تابع چندمرحله‌ای (متوالی)

کاربر در یک نوبت سؤالی می‌پرسد که به دو مرحله جداگانه نیاز دارد (بررسی پرواز -> رزرو تاکسی).   
  
**مرحله ۱: مدل «ابزار پرواز» را فرا می‌خواند.**‫  
مدل امضای `<Sig_A>` را برمی‌گرداند

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**مرحله ۲: کاربر «نتیجه پرواز» را ارسال می‌کند**  
برای حفظ روند فکری مدل، باید `<Sig_A>` را برگردانیم.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**مرحله ۳: مدل با «ابزار تاکسی» تماس می‌گیرد**  
مدل تأخیر پرواز را ازطریق `<Sig_A>` به‌خاطر می‌آورد و اکنون تصمیم می‌گیرد تاکسی رزرو کند. امضای *جدیدی* `<Sig_B>` تولید می‌کند.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**مرحله ۴: کاربر «نتیجه تاکسی» را ارسال می‌کند**  
برای تکمیل نوبت، باید کل زنجیره را برگردانید: `<Sig_A>` و `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### فراخوانی تابع موازی

کاربر می‌پرسد: «آب‌وهوای پاریس و لندن را بررسی کن.» مدل دو فراخوانی تابع را در یک پاسخ برمی‌گرداند.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### نوشتار/استدلال زمینه‌ای (بدون اعتبارسنجی)

کاربر سؤالی می‌پرسد که بدون ابزارهای خارجی به استدلال زمینه‌ای نیاز دارد. اگرچه امضا به‌طور دقیق درستی‌سنجی نمی‌شود، اما افزودن امضا به مدل کمک می‌کند تا زنجیره استدلال را برای سؤالات بعدی حفظ کند.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### تولید و ویرایش تصویر

برای تولید تصویر، امضاها به‌دقت اعتبارسنجی می‌شوند. این نشان‌ها در **بخش اول** (نوشتار یا تصویر) و **همه بخش‌های تصویری بعدی** ظاهر می‌شوند. همه باید در نوبت بعدی برگردانده شوند.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### انتقال از مدل‌های دیگر

اگر رد مکالمه‌ای را از مدل دیگری (مثلاً Gemini 2.5) منتقل می‌کنید یا فراخوانی تابع سفارشی را تزریق می‌کنید که توسط Gemini 3 تولید نشده است، امضای معتبری نخواهید داشت.

برای دور زدن اعتبارسنجی دقیق در این سناریوهای خاص، فیلد را با
این رشته ساختگی خاص پر کنید: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### بروندادهای ساختاریافته با ابزارها

مدل‌های Gemini 3 به شما امکان می‌دهند [بروندادهای ساختاریافته](https://ai.google.dev/gemini-api/docs/structured-output?hl=fa) را با ابزارهای داخلی، ازجمله
[زمینه‌سازی با «جستجوی Google»](https://ai.google.dev/gemini-api/docs/google-search?hl=fa)، [بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)، [اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)، و [فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa) ترکیب کنید.

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
      "responseFormat": {
        "text": {
          "mimeType": "APPLICATION_JSON",
          "schema": {
            "type": "object",
            "properties": {
              "winner": {"type": "string", "description": "The name of the winner."},
              "final_match_score": {"type": "string", "description": "The final score."},
              "scorers": {
                "type": "array",
                "items": {"type": "string"},
                "description": "The name of the scorer."
              }
            },
            "required": ["winner", "final_match_score", "scorers"]
          }
        }
      }
    }
  }'
```

### تولید تصویر

‫Gemini 3.1 Flash Image و Gemini 3 Pro Image به شما امکان می‌دهند تصاویر را از پیام‌واره‌های نوشتاری تولید و ویرایش کنید. این مدل از استدلال برای «فکر کردن» درباره پیام‌واره استفاده می‌کند و می‌تواند داده‌های بی‌درنگ—مثل پیش‌بینی‌های آب‌وهوا یا نمودارهای سهام—را قبل‌از استفاده از [جستجوی Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fa) برای زمینه‌سازی قبل‌از تولید تصاویر با کیفیت بالا بازیابی کند.

**قابلیت‌های جدید و بهبودیافته:**

- **پرداز کردن نوشتار و 4K:** نوشتار و نمودارهای واضح و خوانا با وضوح حداکثر 2K و 4K تولید کنید.
- **تولید مبتنی بر واقعیت:** از ابزار `google_search` برای درستی‌سنجی حقایق و
  تولید تصاویر براساس اطلاعات دنیای واقعی استفاده کنید. جستجوی زمینه‌سازی با Google *تصویر*
  برای Gemini 3.1 Flash Image دردسترس است.
- **ویرایش مکالمه‌ای:** ویرایش چندنوبتی تصویر با درخواست ساده برای تغییرات (برای نمونه، «پس‌زمینه را غروب آفتاب کن»). این گردش کار برای حفظ زمینه دیداری بین نوبت‌ها به
  **امضاهای فکری** متکی است.

برای جزئیات کامل درباره نسبت‌های ابعادی، گردش‌های کار ویرایش، و گزینه‌های پیکربندی، [راهنمای تولید تصویر](https://ai.google.dev/gemini-api/docs/image-generation?hl=fa) را ببینید.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="4K",
        ),
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      imageConfig: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
      "imageConfig": {
        "aspectRatio": "16:9",
        "imageSize": "4K"
      }
    }
  }'
```

**پاسخ نمونه**

![آب‌وهوای توکیو](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=fa)

### اجرای کد با تصاویر

‫Gemini 3 Flash می‌تواند دید را به‌عنوان یک بررسی فعال درنظر بگیرد، نه فقط یک نگاه
ایستا. با ترکیب استدلال با [اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)، مدل برنامه‌ای را فرموله می‌کند، سپس کد پایتون را برای بزرگ‌نمایی، برش، حاشیه‌نویسی، یا دستکاری تصاویر به‌صورت گام‌به‌گام می‌نویسد و اجرا می‌کند تا پاسخ‌هایش را به‌صورت بصری مستند کند.

**موارد استفاده:**

- **زوم‌پیش و بازرسی:** مدل به‌طور ضمنی تشخیص می‌دهد که جزئیات چقدر کوچک است (برای نمونه، خواندن درجه یا شماره سریال از دور) و کدی برای برش دادن و دوباره بررسی کردن ناحیه با وضوح بالاتر می‌نویسد.
- **ریاضیات و رسم نمودار دیداری:** این مدل می‌تواند محاسبات چندمرحله‌ای را بااستفاده از کد اجرا کند (برای مثال، جمع کردن ردیف‌های یک رسید، یا تولید نمودار Matplotlib از داده‌های استخراج‌شده).
- **گزارمان تصویر:** مدل می‌تواند برای پاسخ دادن به سؤالات فضایی مثل «این مورد کجا باید برود؟» مستقیماً روی تصاویر فلش، چارگوش محدودکننده، یا گزارشمان‌های دیگر بکشد.

برای فعال کردن تفکر تصویری، [اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa) را به‌عنوان ابزار پیکربندی کنید. این مدل درصورت نیاز به‌طور خودکار از
کد برای دستکاری تصاویر استفاده می‌کند.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

برای جزئیات بیشتر درباره اجرای کد با تصاویر، [اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa#images) را ببینید.

### پاسخ‌های عملکرد چندحالته

[فراخوانی تابع چندحالته](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa#multimodal)
به کاربران امکان می‌دهد پاسخ‌های تابع حاوی
اشیاء چندحالته داشته باشند که امکان استفاده بهتر از قابلیت‌های
فراخوانی تابع مدل را فراهم می‌کند. فراخوانی تابع استاندارد فقط از پاسخ‌های تابع نوشتاری پشتیبانی می‌کند:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### ترکیب ابزارهای داخلی و فراخوانی تابع

‫Gemini 3 امکان استفاده از ابزارهای داخلی (مثل «جستجوی Google»، بافت URL، و [موارد دیگر](https://ai.google.dev/gemini-api/docs/tools?hl=fa)) و ابزارهای سفارشی [فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa) را در همان فراخوانی API فراهم می‌کند و امکان گردش‌های کار پیچیده‌تر را فراهم می‌کند. در صفحه [ترکیب‌های ابزار](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fa) بیشتر بدانید.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### جاوا اسکریپت

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const response1 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });
}

run();
```

## درحال انتقال از Gemini 2.5

‫Gemini 3 توانمندترین خانواده مدل‌های ما تا به امروز است و نسبت به Gemini 2.5 بهبود گام‌به‌گام ارائه می‌دهد. هنگام انتقال، موارد زیر را درنظر بگیرید:

- **اندیشگر:** اگر قبلاً از مهندسی پیام‌واره پیچیده (مثل
  زنجیره فکر) برای مجبور کردن Gemini 2.5 به استدلال استفاده می‌کردید، Gemini 3 را با
  `thinking_level: "high"` و پیام‌واره‌های ساده‌شده امتحان کنید.
- **تنظیمات دما:** اگر کد موجودتان به‌طور صریح دما را تنظیم می‌کند
  (به‌ویژه روی مقادیر پایین برای بروندادهای قطعی)، توصیه می‌کنیم این
  پارامتر را بردارید و از مقدار پیش‌فرض ۱٫۰ در Gemini 3 استفاده کنید تا از مشکلات احتمالی حلقه
  یا افت عملکرد در کارهای پیچیده جلوگیری کنید.
- **درک سند و PDF:**
  اگر برای تجزیه اسناد متراکم به رفتار خاصی متکی بودید،
  تنظیم جدید `media_resolution_high` را آزمایش کنید تا از ادامه دقت مطمئن شوید.
- **مصرف داده‌واحد (توکن):** انتقال به پیش‌فرض‌های Gemini 3 ممکن است مصرف داده‌واحد (توکن) را برای فایل‌های PDF **افزایش** دهد اما مصرف داده‌واحد (توکن) را برای ویدیو **کاهش** دهد. اگر درخواست‌ها اکنون به‌دلیل وضوح پیش‌فرض بالاتر از پنجره بافت فراتر می‌روند، توصیه می‌کنیم وضوح رسانه را به‌طور صریح کاهش دهید.
- **تقسیم‌بندی تصویر:** قابلیت‌های تقسیم‌بندی تصویر (برگرداندن پوشش‌های سطح پیکسل برای اشیا) در Gemini 3 Pro یا Gemini 3 Flash پشتیبانی نمی‌شود. برای
  بارهای کاری که به تقسیم‌بندی تصویر بومی نیاز دارند، توصیه می‌کنیم
  به استفاده از Gemini 2.5 Flash با خاموش بودن تفکر ادامه دهید.
- **استفاده از رایانه:** Gemini 3 Pro و Gemini 3 Flash از [استفاده از رایانه](https://ai.google.dev/gemini-api/docs/computer-use?hl=fa) پشتیبانی می‌کنند. برخلاف سری ۲.۵، برای دسترسی به ابزار «استفاده از رایانه» نیازی به
  استفاده از مدل جداگانه ندارید.
- **پشتیبانی از ابزار**: [ترکیب ابزارهای داخلی با فراخوانی تابع](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fa) اکنون برای مدل‌های Gemini 3 پشتیبانی می‌شود. اکنون از [پایه Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fa) برای مدل‌های Gemini 3 نیز پشتیبانی می‌شود.
- **تعداد نامزدها**: مدل‌های Gemini 3 از `candidateCount > 1` پشتیبانی نمی‌کنند.
  اگر این پارامتر را روی مقداری بزرگ‌تر از `1` تنظیم کنید، خطای ۴۰۰ برمی‌گرداند.

## سازگاری با OpenAI

برای کاربرانی که از [لایه سازگاری OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fa) استفاده می‌کنند،
پارامترهای استاندارد (`reasoning_effort` در OpenAI) به‌طور خودکار به
معادل‌های Gemini (`thinking_level`) نگاشت می‌شوند.

## روال‌های مطلوب پیام‌واره

‫Gemini 3 مدل استدلالی است که نحوه پیام‌واره‌نویسی شما را تغییر می‌دهد.

- **دستورالعمل‌های دقیق:** در پیام‌واره‌های ورودی خود مختصر و مفید باشید. ‫Gemini 3 بهترین پاسخ را به دستورالعمل‌های مستقیم و واضح می‌دهد. ممکن است تکنیک‌های مهندسی پیام‌واره پرحرف یا بیش‌ازحد پیچیده را که برای مدل‌های قدیمی‌تر استفاده می‌شود بیش‌ازحد تجزیه‌وتحلیل کند.
- **پرگویی برونداد:** به‌طور پیش‌فرض، Gemini 3 کمتر پرگو است و ترجیح می‌دهد
  پاسخ‌های مستقیم و کارآمد ارائه دهد. اگر مورد استفاده شما به شخصیتی
  مکالمه‌ای‌تر یا «گپ‌زن» نیاز دارد، باید مدل را به‌طور صریح در پیام‌واره هدایت کنید (برای نمونه، «این را به‌عنوان دستیار دوستانه و گپ‌زن توضیح بده»).
- **مدیریت بافت:** هنگام کار با مجموعه داده‌های بزرگ (مثلاً کل کتاب‌ها، پایه‌های کد، یا ویدیوهای طولانی)، دستورالعمل‌ها یا پرسش‌های خاص خود را در انتهای پیام‌واره، پس‌از بافت داده‌ها، قرار دهید. با شروع کردن پرسش خود با عبارتی مثل «براساس اطلاعات بالا…»، استدلال مدل را به داده‌های ارائه‌شده متصل کنید.

درباره استراتژی‌های طراحی پیام‌واره در [راهنمای مهندسی پیام‌واره](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fa) بیشتر بدانید.

## پرسشگان

1. **«آستانه دانش» برای Gemini 3 چیست؟** مدل‌های Gemini 3 تا
   ژانویه ۲۰۲۵ اطلاعات دارند. برای اطلاعات جدیدتر، از ابزار
   [جستجوی زمینه‌ای](https://ai.google.dev/gemini-api/docs/google-search?hl=fa) استفاده کنید.
2. **محدودیت‌های پنجره زمینه‌ای چیست؟** مدل‌های Gemini 3 از پنجره زمینه‌ای ورودی ۱ میلیون داده‌واحد (توکن) و حداکثر ۶۴ هزار داده‌واحد (توکن) برونداد پشتیبانی می‌کنند.
3. **آیا سطح رایگانی برای Gemini 3 وجود دارد؟** ‫Gemini 3 Flash
   `gemini-3-flash-preview` و 3.1 Flash-Lite `gemini-3.1-flash-lite` در
   Gemini API سطوح رایگان دارند. می‌توانید Gemini 3.1 Pro و 3 Flash را به‌طور رایگان در
   Google AI Studio امتحان کنید، اما سطح رایگانی برای
   `gemini-3.1-pro-preview` در Gemini API دردسترس نیست.
4. **آیا کد قدیمی `thinking_budget` من همچنان کار خواهد کرد؟** بله، `thinking_budget` همچنان برای سازگاری با نسخه قدیمی پشتیبانی می‌شود، اما توصیه می‌کنیم برای عملکرد قابل‌پیش‌بینی‌تر به `thinking_level` انتقال دهید. از هر دو در یک درخواست استفاده نکنید.
5. **آیا Gemini 3 از Batch API پشتیبانی می‌کند؟** بله، Gemini 3 از
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa) پشتیبانی می‌کند.
6. **آیا «ذخیره کردن زمینه‌ای» پشتیبانی می‌شود؟** بله، [ذخیره کردن زمینه‌ای](https://ai.google.dev/gemini-api/docs/caching?hl=fa) برای Gemini 3 پشتیبانی می‌شود.
7. **کدام ابزارها در Gemini 3 پشتیبانی می‌شوند؟** ‫Gemini 3 از [جستجوی Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fa)، [پایه‌مندسازی با Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fa)، [جستجوی فایل](https://ai.google.dev/gemini-api/docs/file-search?hl=fa)،
   [اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)، و [زمینه نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa) پشتیبانی می‌کند. همچنین از [فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa) استاندارد برای ابزارهای سفارشی خودتان و در [ترکیب با ابزارهای داخلی](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fa) پشتیبانی می‌کند.
8. **‫`gemini-3.1-pro-preview-customtools` چیست؟** اگر از `gemini-3.1-pro-preview` استفاده می‌کنید و مدل ابزارهای سفارشی شما را نادیده می‌گیرد و از فرمان‌های bash استفاده می‌کند، مدل `gemini-3.1-pro-preview-customtools` را امتحان کنید. اطلاعات بیشتر در [اینجا](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fa#gemini-31-pro-preview-customtools).

## مراحل بعدی

- شروع به کار با [کتاب آشپزی Gemini 3](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=fa#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- راهنمای اختصاصی «کتاب آشپزی» درباره [سطوح تفکر](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=fa#gemini3) و نحوه انتقال از بودجه تفکر به سطوح تفکر را بررسی کنید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-19 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-19 به‌وقت ساعت هماهنگ جهانی."],[],[]]
