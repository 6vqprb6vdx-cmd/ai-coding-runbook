---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=fa
fetched_at: 2026-10-19T05:34:25.143958+00:00
title: "\u062c\u0627\u0633\u0627\u0632\u06cc\u200c\u0647\u0627 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# جاسازی‌ها

‫Gemini API مدل‌های جاسازی را برای تولید جاسازی برای نوشتار، تصویر، ویدیو، و محتوای دیگر ارائه می‌دهد. سپس می‌توان از این جاسازی‌های حاصل برای کارهایی
مثل جستجوی معنایی، طبقه‌بندی، و دسته‌بندی استفاده کرد و نتایج دقیق‌تر و
آگاه به زمینه‌ای نسبت‌به رویکردهای مبتنی بر کلیدواژه ارائه داد.

جدیدترین مدل، `gemini-embedding-2`، اولین مدل جاسازی چندوجهی در Gemini API است. این مدل نوشتار، تصاویر، ویدیو، صدا، و اسناد را در فضای جاسازی یکپارچه نقشه‌برداری می‌کند و امکان جستجو، طبقه‌بندی، و خوشه‌بندی بین‌وجهی را در بیش‌از ۱۰۰ زبان فراهم می‌کند. برای اطلاعات بیشتر، به
[بخش جاسازی‌های چندوجهی](#multimodal) مراجعه کنید. برای موارد استفاده فقط نوشتاری،
`gemini-embedding-001` دردسترس باقی می‌ماند.

ساختن سیستم‌های «تولید با کمک بازیابی» (RAG) یک مورد استفاده رایج برای محصولات هوش مصنوعی است. جاسازی‌ها نقش کلیدی در بهبود قابل‌توجه بروندادهای مدل با دقت واقعی، انسجام، و غنای زمینه‌ای بهبودیافته دارند. اگر ترجیح می‌دهید از راهکار RAG مدیریت‌شده استفاده کنید، ابزار [جستجوی فایل](https://ai.google.dev/gemini-api/docs/file-search?hl=fa)
را ساخته‌ایم که مدیریت RAG را آسان‌تر و مقرون‌به‌صرفه‌تر می‌کند.

## درحال تولید جاسازی‌ها

از روش `embedContent` برای تولید جاسازی‌های نوشتاری استفاده کنید:

### Python

```
from google import genai

client = genai.Client()

result = client.models.embed_content(
        model="gemini-embedding-2",
        contents="What is the meaning of life?"
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {

    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
    });

    console.log(response.embeddings);
}

main();
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", "What is the meaning of life?", null);

System.out.println(response.embeddings().orElse(null));
```

### رفتن

```
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }
    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    embeddings, err := json.MarshalIndent(result.Embeddings, "", "  ")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(embeddings))
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "model": "models/gemini-embedding-2",
        "content": {
        "parts": [{
            "text": "What is the meaning of life?"
        }]
        }
    }'
```

## نوع تکلیف را مشخص کنید تا عملکرد بهبود یابد

می‌توانید از جاسازی‌ها برای طیف وسیعی از کارها، از طبقه‌بندی گرفته تا جستجوی سند، استفاده کنید. مشخص کردن نوع وظیفه صحیح به بهینه‌سازی جاسازی‌ها برای روابط موردنظر کمک می‌کند و دقت و کارایی را به حداکثر می‌رساند.

### انواع تکلیف با «جاسازی‌ها ۲»

برای تکالیف فقط نوشتاری با `gemini-embedding-2`، قویاً توصیه می‌کنیم
دستورالعمل تکلیف را به پیام‌واره‌تان اضافه کنید. این کار را می‌توان با قالب‌بندی کردن
پُرسمان و سند با پیشوند تکلیف صحیح انجام داد.

هنگام تولید [تک‌نهاد براساس ورودی چندوجهی](#embedding-aggregation)، معمولاً توصیه نمی‌کنیم بخش نوشتاری ورودی را با دستورالعمل تکلیف پیشوندگذاری کنید. در برخی موارد، عملکرد را بهبود می‌بخشد، اما در موارد دیگر، عملکرد را کاهش می‌دهد.

جدول‌های زیر نمونه‌هایی از نحوه قالب‌بندی پُرسمان‌ها و اسناد برای
موارد استفاده متقارن و نامتقارن بااستفاده از مدل `gemini-embedding-2` را نشان می‌دهد.

**کاربردهای بازیابی (قالب نامتقارن)**

در موارد استفاده نامتقارن، پیشوند تکلیف را به پُرسمان اضافه کنید و ساختار سند را برای محتوایی که می‌خواهید جاسازی و بازیابی کنید اعمال کنید.

| کاربرد | ساختار پُرسمان | ساختار سند |
| --- | --- | --- |
| درخواست جستجو | `task: search result | query: {content}` | `title: {title} | text: {content}` اگر عنوان وجود ندارد، از `title: none` استفاده کنید. |
| پاسخ به سؤال | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| راستی‌آزمایی خبر | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| بازیابی کد | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**مثال استفاده**

### Python

```
# Generate embedding for a task's query. Use your correct task here:
def prepare_query(query):
    # return f"task: question answering | query: {query}"
    # return f"task: fact checking | query: {query}"
    # return f"task: code retrieval | query: {query}"
    return f"task: search result | query: {query}"

# Generate embedding for document of an asymmetric retrieval task:
def prepare_document(content, title=None):
    if title is None:
        title = "none"
    return f"title: {title} | text: {content}"
```

**کاربردهای تک‌ورودی (قالب متقارن)**

در موارد استفاده متقارن، برای یک تکلیف یکسان، از قالب‌بندی یکسان برای پُرسمان و سند استفاده کنید.

| کاربرد | ساختار ورودی |
| --- | --- |
| رده‌بندی | `task: classification | query: {content}` |
| دسته‌بندی | `task: clustering | query: {content}` |
| تشابه معنایی | `task: sentence similarity | query: {content}` از این برای جستجو یا بازیابی استفاده نکنید. این مدل برای شباهت معنایی نوشتار درنظر گرفته شده است. |

**مثال استفاده**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

مهم است که تکلیف به‌طور مداوم استفاده شود. برای مثال، اگر اسناد با `f'task: classification | query: {content}'` جاسازی شده‌اند، پُرسمان نیز باید با پیروی از این قالب تکلیف جاسازی شود.

### انواع تکلیف با «جاسازی‌ها ۱»

برای `gemini-embedding-001`، می‌توانید `task_type` را در روش `embedContent`
مشخص کنید. برای فهرست کامل انواع تکلیف پشتیبانی‌شده، جدول [انواع تکلیف پشتیبانی‌شده](#supported-task-types) را ببینید.

مثال زیر نشان می‌دهد که چگونه می‌توانید از `SEMANTIC_SIMILARITY` برای بررسی میزان شباهت معنایی رشته‌های نوشتاری استفاده کنید.

### Python

```
from google import genai
from google.genai import types
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client()

texts = [
    "What is the meaning of life?",
    "What is the purpose of existence?",
    "How do I bake a cake?",
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

# Create a 3x3 table to show the similarity matrix
df = pd.DataFrame(
    cosine_similarity([e.values for e in result.embeddings]),
    index=texts,
    columns=texts,
)

print(df)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
// npm i compute-cosine-similarity
import * as cosineSimilarity from "compute-cosine-similarity";

async function main() {
    const ai = new GoogleGenAI({});

    const texts = [
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    ];

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-001',
        contents: texts,
        config: { taskType: 'SEMANTIC_SIMILARITY' },
    });

    const embeddings = response.embeddings.map(e => e.values);

    for (let i = 0; i < texts.length; i++) {
        for (let j = i + 1; j < texts.length; j++) {
            const text1 = texts[i];
            const text2 = texts[j];
            const similarity = cosineSimilarity(embeddings[i], embeddings[j]);
            console.log(`Similarity between '${text1}' and '${text2}': ${similarity.toFixed(4)}`);
        }
    }
}

main();
```

### جاوا

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentConfig;
import com.google.genai.types.EmbedContentResponse;
import java.util.List;

Client client = new Client();

List<String> texts =
    Arrays.asList(
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?");

EmbedContentConfig config =
    EmbedContentConfig.builder().taskType("SEMANTIC_SIMILARITY").build();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-001", texts, config);

List<ContentEmbedding> embeddings = response.embeddings().get();

for (int i = 0; i < texts.size(); i++) {
  for (int j = i + 1; j < texts.size(); j++) {
    List<Float> v1 = embeddings.get(i).values().get();
    List<Float> v2 = embeddings.get(j).values().get();
    double dotProduct = 0.0;
    double normA = 0.0;
    double normB = 0.0;
    for (int k = 0; k < v1.size(); k++) {
      dotProduct += v1.get(k) * v2.get(k);
      normA += v1.get(k) * v1.get(k);
      normB += v2.get(k) * v2.get(k);
    }
    double similarity = dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
    System.out.printf(
        "Similarity between '%s' and '%s': %.4f%n", texts.get(i), texts.get(j), similarity);
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
    "math"

    "google.golang.org/genai"
)

// cosineSimilarity calculates the similarity between two vectors.
func cosineSimilarity(a, b []float32) (float64, error) {
    if len(a) != len(b) {
        return 0, fmt.Errorf("vectors must have the same length")
    }

    var dotProduct, aMagnitude, bMagnitude float64
    for i := 0; i < len(a); i++ {
        dotProduct += float64(a[i] * b[i])
        aMagnitude += float64(a[i] * a[i])
        bMagnitude += float64(b[i] * b[i])
    }

    if aMagnitude == 0 || bMagnitude == 0 {
        return 0, nil
    }

    return dotProduct / (math.Sqrt(aMagnitude) * math.Sqrt(bMagnitude)), nil
}

func main() {
    ctx := context.Background()
    client, _ := genai.NewClient(ctx, nil)
    defer client.Close()

    texts := []string{
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    }

    var contents []*genai.Content
    for _, text := range texts {
        contents = append(contents, genai.NewContentFromText(text, genai.RoleUser))
    }

    result, _ := client.Models.EmbedContent(ctx,
        "gemini-embedding-001",
        contents,
        &genai.EmbedContentRequest{TaskType: genai.TaskTypeSemanticSimilarity},
    )

    embeddings := result.Embeddings

    for i := 0; i < len(texts); i++ {
        for j := i + 1; j < len(texts); j++ {
            similarity, _ := cosineSimilarity(embeddings[i].Values, embeddings[j].Values)
            fmt.Printf("Similarity between '%s' and '%s': %.4f\n", texts[i], texts[j], similarity)
        }
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
    "taskType": "SEMANTIC_SIMILARITY",
    "content": {
        "parts": [
        {
            "text": "What is the meaning of life?"
        },
        {
            "text": "How much wood would a woodchuck chuck?"
        },
        {
            "text": "How does the brain work?"
        }
        ]
    }
    }'
```

تکه‌کدهای نشان می‌دهد که بخش‌های مختلف نوشتار هنگام اجرا چقدر به یکدیگر شبیه‌اند.

#### انواع تکلیف پشتیبانی‌شده

انواع تکلیف پشتیبانی‌شده برای `gemini-embedding-001`:

| نوع تکلیف | شرح | مثال‌ها |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | جاسازی‌ها برای ارزیابی شباهت نوشتار بهینه‌سازی شده است. | سیستم‌های توصیه، تشخیص محتوای تکراری |
| **طبقه‌بندی** | جاسازی‌ها برای طبقه‌بندی نوشتارها براساس برچسب‌های پیش‌تنظیم‌شده بهینه‌سازی شده است. | تحلیل احساسات، تشخیص هرزنامه |
| **خوشه‌بندی** | جاسازی‌هایی که برای دسته‌بندی نوشتارها براساس شباهت‌هایشان بهینه‌سازی شده است. | سازمان‌دهی سند، پژوهش بازار، تشخیص ناهنجاری |
| **RETRIEVAL\_DOCUMENT** | جاسازی‌های بهینه‌سازی‌شده برای جستجوی سند. | نمایه‌گذاری مقاله‌ها، کتاب‌ها، یا صفحه‌های وب برای جستجو. |
| **RETRIEVAL\_QUERY** | جاسازی‌های بهینه‌سازی‌شده برای پُرسمان‌های جستجوی عمومی. از `RETRIEVAL_QUERY` برای پُرسمان‌ها؛ `RETRIEVAL_DOCUMENT` برای سندهایی که باید بازیابی شوند استفاده کنید. | جستجوی سفارشی |
| **CODE\_RETRIEVAL\_QUERY** | جاسازی‌های بهینه‌سازی‌شده برای بازیابی بلوک‌های کد براساس پُرسمان‌های زبان طبیعی. از `CODE_RETRIEVAL_QUERY` برای پُرسمان‌ها و از `RETRIEVAL_DOCUMENT` برای بلوک‌های کد بازیابی‌شده استفاده کنید. | پیشنهادها و جستجوی کد |
| **QUESTION\_ANSWERING** | جاسازی برای پرسش‌ها در سیستم پرسش و پاسخ، بهینه‌سازی‌شده برای یافتن اسنادی که به پرسش پاسخ می‌دهند. از `QUESTION_ANSWERING` برای سؤالات و از `RETRIEVAL_DOCUMENT` برای اسنادی که باید بازیابی شوند استفاده کنید. | کادر گپ |
| **FACT\_VERIFICATION** | جاسازی برای بیانیه‌هایی که باید درستی‌سنجی شوند، بهینه‌سازی‌شده برای بازیابی اسنادی که حاوی شواهدی برای تأیید یا رد بیانیه هستند. از `FACT_VERIFICATION` برای نوشتار هدف؛ `RETRIEVAL_DOCUMENT` برای اسنادی که باید بازیابی شوند استفاده کنید | سیستم‌های خودکار راستی‌آزمایی |

## کنترل اندازه جاسازی

هم `gemini-embedding-001` و هم `gemini-embedding-2` بااستفاده از
تکنیک «یادگیری نمایش ماتریوشکا» (MRL) آموزش داده می‌شوند که به مدل آموزش می‌دهد
تا جاسازی‌های با ابعاد بالا را یاد بگیرد که بخش‌های اولیه (یا پیشوندها) دارند که
نسخه‌های مفیدتر و ساده‌تر از همان داده‌ها هستند.

از پارامتر `output_dimensionality` برای کنترل اندازه
بردار جاسازی برونداد استفاده کنید. انتخاب بُعد خروجی کوچک‌تر می‌تواند فضای ذخیره‌سازی را ذخیره کند و کارایی محاسباتی را برای برنامه‌های پایین‌دستی افزایش دهد، درحالی‌که ازنظر کیفیت کمی فداکاری می‌کند. به‌طور پیش‌فرض، هر دو مدل جاسازی ۳۰۷۲ بُعدی تولید می‌کنند، اما می‌توانید آن را بدون ازدست دادن کیفیت به اندازه کوچکتری برش دهید تا فضای ذخیره‌سازی را ذخیره کنید. توصیه می‌کنیم از ابعاد خروجی ۷۶۸، ۱۵۳۶، یا ۳۰۷۲ استفاده کنید.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="What is the meaning of life?",
    config=types.EmbedContentConfig(output_dimensionality=768)
)

[embedding_obj] = result.embeddings
embedding_length = len(embedding_obj.values)

print(f"Length of embedding: {embedding_length}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
        config: { outputDimensionality: 768 },
    });

    const embeddingLength = response.embeddings[0].values.length;
    console.log(`Length of embedding: ${embeddingLength}`);
}

main();
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentConfig;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();

EmbedContentConfig config =
    EmbedContentConfig.builder().outputDimensionality(768).build();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", "What is the meaning of life?", config);

ContentEmbedding embeddingObj = response.embeddings().get().get(0);
int embeddingLength = embeddingObj.values().get().size();

System.out.println("Length of embedding: " + embeddingLength);
```

### رفتن

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client uses Application Default Credentials.
    // Authenticate with 'gcloud auth application-default login'.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }

    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        &genai.EmbedContentRequest{OutputDimensionality: 768},
    )
    if err != nil {
        log.Fatal(err)
    }

    embedding := result.Embeddings[0]
    embeddingLength := len(embedding.Values)
    fmt.Printf("Length of embedding: %d\n", embeddingLength)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H 'Content-Type: application/json' \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
        "content": {"parts":[{ "text": "What is the meaning of life?"}]},
        "output_dimensionality": 768
    }'
```

نمونه برونداد از تکه‌کد:

```
Length of embedding: 768
```

## تضمین کیفیت برای ابعاد کوچک‌تر

درحالی‌که جاسازی‌های پیش‌فرض ۳۰۷۲ بُعدی همیشه نرمال‌سازی می‌شوند، Gemini
Embedding 2 ابعاد کوتاه شده (مثلاً ۷۶۸، ۱۵۳۶) را نیز به‌طور خودکار نرمال‌سازی می‌کند. این کار تضمین می‌کند که شباهت معنایی ازطریق جهت بردار محاسبه شود نه
اندازه، و نتایج دقیق‌تری را به‌طور پیش‌فرض ارائه می‌دهد.

**مدل‌های قدیمی‌تر**: اگر از `gemini-embedding-001` استفاده می‌کنید، باید ابعاد غیر۳۰۷۲ را به‌صورت دستی و به روش زیر عادی‌سازی کنید:

### Python

```
import numpy as np
from numpy.linalg import norm

# Only for embeddings from `gemini-embedding-001`
embedding_values_np = np.array(embedding_obj.values)
normed_embedding = embedding_values_np / np.linalg.norm(embedding_values_np)

print(f"Normed embedding length: {len(normed_embedding)}")
print(f"Norm of normed embedding: {np.linalg.norm(normed_embedding):.6f}") # Should be very close to 1
```

نمونه برونداد از این تکه‌کد:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

جدول زیر نمره‌های MTEB را نشان می‌دهد که یک معیار رایج برای جاسازی‌ها در ابعاد مختلف است. به‌طور قابل‌توجهی، نتیجه نشان می‌دهد که عملکرد
به‌طور دقیق به اندازه بُعد جاسازی مرتبط نیست، به‌طوری‌که
ابعاد پایین‌تر به امتیازهایی قابل‌مقایسه با همتایان بُعد بالاتر خود دست می‌یابند.

| ابعاد MRL | امتیاز MTEB (Gemini Embedding 001) |
| --- | --- |
| ۲۰۴۸ | ۶۸.۱۶ |
| 1536 | ۶۸.۱۷ |
| 768 | ۶۷.۹۹ |
| 512 | ۶۷.۵۵ |
| 256 | ۶۶.۱۹ |
| 128 | ۶۳.۳۱ |

## جاسازی‌های چندحالته

مدل `gemini-embedding-2` از ورودی چندحالته پشتیبانی می‌کند و به شما امکان می‌دهد
محتوای تصویر، ویدیو، صدا، و سند را در کنار نوشتار جاسازی کنید. همه روش‌ها
در فضای جاسازی یکسانی نگاشت می‌شوند و جستجو و
مقایسه بین روش‌ها را ممکن می‌کنند.

### روش‌های پشتیبانی‌شده و محدودیت‌ها

حداکثر محدودیت کلی برای نشانه‌های ورودی ۸۱۹۲ نشانه است.

| ماهیت | مشخصات و محدودیت‌ها |
| --- | --- |
| **نوشتار** | تا ۸٬۱۹۲ واحد را پشتیبانی می‌کند. |
| **تصویر** | حداکثر ۶ تصویر در هر درخواست. قالب‌های پشتیبانی‌شده: PNG،‏ JPEG. |
| **صدا** | حداکثر مدت ۱۸۰ ثانیه. قالب‌های پشتیبانی‌شده: MP3،‏ WAV. |
| **ویدیو** | حداکثر مدت ۱۲۰ ثانیه. قالب‌های پشتیبانی‌شده: MP4،‏ MOV. کدک‌های پشتیبانی‌شده: H264،‏ H265،‏ AV1،‏ VP9.  سیستم حداکثر ۳۲ فریم در هر ویدیو را پردازش می‌کند: ویدیوهای کوتاه (≤۳۲ ثانیه) با نرخ ۱ فریم در ثانیه نمونه‌برداری می‌شوند، درحالی‌که ویدیوهای طولانی‌تر به‌طور یکنواخت تا ۳۲ فریم نمونه‌برداری می‌شوند. قطعه‌های صوتی در فایل‌های ویدیویی پردازش نمی‌شوند. |
| **سندها (PDF)** | حداکثر ۱ فایل در هر درخواست، حداکثر ۶ صفحه. |

### درحال جاسازی تصاویر

مثال زیر نحوه جاسازی تصویر بااستفاده از
`gemini-embedding-2` را نشان می‌دهد.

تصاویر را می‌توان به‌صورت داده‌های درون‌خطی یا به‌صورت فایل‌های بارگذاری‌شده ازطریق [میانای برنامه‌سازی کاربردی فایل‌ها](https://ai.google.dev/gemini-api/docs/files?hl=fa) ارائه کرد.

### Python

```
from google import genai
from google.genai import types

with open('example.png', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("example.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'image/png',
                data: imgBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("example.png"));

Content content = Content.fromParts(Part.fromBytes(imageBytes, "image/png"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
```

### REST

```
IMG_PATH="/path/to/your/image.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "image/png",
                    "data": "'"${IMG_BASE64}"'"
                }
            }]
        }
    }'
```

### انبوهش جاسازی

وقتی با محتوای چندوجهی کار می‌کنید، نحوه ساختاربندی ورودی شما بر
برونداد جاسازی تأثیر می‌گذارد:

- **چند بخش (تجمیع‌شده):** افزودن چندین ورودی مستقیماً به پارامتر
  `contents` یک جاسازی تجمیع‌شده برای همه ورودی‌ها تولید می‌کند.
- **چندین شیء `Content` (جداگانه):** پیچیدن هر ورودی در شیء `Content` و عبور دادن آن‌ها در پارامتر `contents` جاسازی‌های جداگانه برای هر ورودی برمی‌گرداند.
- **نمایش سطح پست:** برای اشیای پیچیده مثل پست‌های رسانه‌های اجتماعی با چندین عنصر رسانه‌ای، توصیه می‌کنیم جاسازی‌های جداگانه را با هم ترکیب کنید (برای مثال، با میانگین‌گیری) تا نمایش سطح پست منسجمی ایجاد کنید.

مثال زیر نحوه ایجاد یک جاسازی تجمیعی برای ورودی نوشتار و تصویر را نشان می‌دهد. به‌سادگی ورودی‌های متعددی را به پارامتر `contents` اضافه کنید:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        "An image of a dog",
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

# This produces one embedding
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            'An image of a dog',
            {
                inlineData: {
                    mimeType: 'image/png',
                    data: imgBase64,
                },
            },
        ],
    });

    // This produces one embedding
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("dog.png"));

Content content =
    Content.fromParts(
        Part.fromText("An image of a dog"),
        Part.fromBytes(imageBytes, "image/png"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

// This produces one embedding
for (ContentEmbedding embedding : response.embeddings().orElse(Collections.emptyList())) {
  System.out.println(embedding.values().orElse(Collections.emptyList()));
}
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [
                {"text": "An image of a dog"},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": "'"${IMG_BASE64}"'"
                    }
                }
            ]
        }
    }'
```

ازطرف دیگر، اگر از `Content` شیء در پارامتر `contents` استفاده کنید،
چند جاسازی جداگانه برمی‌گرداند. این مثال چندین جاسازی را در یک فراخوانی جاسازی ایجاد می‌کند:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents=[
        types.Content(parts=[types.Part.from_text(text="task: classification | query: An image of a dog")]),
        types.Content(
            parts=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png",
                ),
            ]
        ),
    ],
)

# This produces two embeddings
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            { parts: [{ text: 'task: classification | query: An image of a dog' }] },
            {
                parts: [{
                    inlineData: {
                        mimeType: 'image/png',
                        data: imgBase64,
                    },
                }],
            },
        ],
    });

    // This produces two embeddings
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### جاوا

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("dog.png"));

List<Content> contents =
    Arrays.asList(
        Content.fromParts(Part.fromText("task: classification | query: An image of a dog")),
        Content.fromParts(Part.fromBytes(imageBytes, "image/png")));

// Embed each Content object separately to produce separate embeddings
for (Content content : contents) {
  EmbedContentResponse response =
      client.models.embedContent("gemini-embedding-2", content, null);
  for (ContentEmbedding embedding : response.embeddings().orElse(Collections.emptyList())) {
    System.out.println(embedding.values().orElse(Collections.emptyList()));
  }
}
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:batchEmbedContents" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "requests": [
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"text": "task: classification | query: An image of a dog"}]}
            },
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"inline_data": {"mime_type": "image/png", "data": "'"${IMG_BASE64}"'"}}]}
            }
        ]
    }'
```

### درحال جاسازی صدا

مثال زیر نحوه جاسازی فایل صوتی بااستفاده از
`gemini-embedding-2` را نشان می‌دهد.

فایل‌های صوتی را می‌توان به‌صورت داده‌های درون‌خطی یا به‌صورت فایل‌های بارگذاری‌شده ازطریق [میانای برنامه‌سازی کاربردی فایل‌ها](https://ai.google.dev/gemini-api/docs/files?hl=fa) ارائه کرد.

### Python

```
from google import genai
from google.genai import types

with open('example.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=audio_bytes,
            mime_type='audio/mpeg',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const audioBase64 = fs.readFileSync("example.mp3", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'audio/mpeg',
                data: audioBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] audioBytes = Files.readAllBytes(Paths.get("example.mp3"));

Content content = Content.fromParts(Part.fromBytes(audioBytes, "audio/mpeg"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
```

### REST

```
AUDIO_PATH="/path/to/your/example.mp3"
AUDIO_BASE64=$(base64 -w0 "${AUDIO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "audio/mpeg",
                    "data": "'"${AUDIO_BASE64}"'"
                }
            }]
        }
    }'
```

### درحال جاسازی ویدیو

مثال زیر نحوه جاسازی ویدیو بااستفاده از
`gemini-embedding-2` را نشان می‌دهد.

ویدیوها را می‌توان به‌عنوان داده‌های درون‌خطی یا به‌عنوان فایل‌های بارگذاری‌شده ازطریق [Files API](https://ai.google.dev/gemini-api/docs/files?hl=fa) ارائه کرد.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('example.mp4', 'rb') as f:
    video_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=video_bytes,
            mime_type='video/mp4',
        ),
    ]
)

print(result.embeddings[0].values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const videoBase64 = fs.readFileSync("example.mp4", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'video/mp4',
                data: videoBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;

Client client = new Client();

byte[] videoBytes = Files.readAllBytes(Paths.get("example.mp4"));

Content content = Content.fromParts(Part.fromBytes(videoBytes, "video/mp4"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(
    response.embeddings().get().get(0).values().orElse(Collections.emptyList()));
```

### REST

```
VIDEO_PATH="/path/to/your/video.mp4"
VIDEO_BASE64=$(base64 -w0 "${VIDEO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "video/mp4",
                    "data": "'"${VIDEO_BASE64}"'"
                }
            }]
        }
    }'
```

اگر نیاز به جاسازی ویدیوهای >120 ثانیه دارید، می‌توانید ویدیو را به
بخش‌های هم‌پوشان تقسیم کنید و آن بخش‌ها را به‌صورت جداگانه جاسازی کنید.

### درحال جاسازی سندها

اسناد در قالب PDF را می‌توان مستقیماً جاسازی کرد. این مدل محتوای تصویری و نوشتاری هر صفحه را پردازش می‌کند.

فایل‌های PDF را می‌توان به‌عنوان داده‌های درون‌خطی یا به‌عنوان فایل‌های بارگذاری‌شده ازطریق [میانای برنامه‌سازی کاربردی فایل‌ها](https://ai.google.dev/gemini-api/docs/files?hl=fa) ارائه کرد.

#### نحوه پردازش فایل‌های PDF توسط مدل

وقتی فایل PDF را جاسازی می‌کنید، مدل سند را بااستفاده از ویژگی‌های دیداری و نوشتاری پردازش می‌کند:

- **نمایش تصویری:** مدل هر صفحه را به‌صورت تصویر پردازش می‌کند که در هر صفحه **۲۵۸ کد** مصرف می‌کند.
- **استخراج نوشتار:** مدل نوشتار را از سند استخراج می‌کند. برای **فایل‌های PDF بومی** (که حاوی نوشتار دیجیتال هستند)، مدل نوشتار را مستقیماً استخراج می‌کند. برای **فایل‌های PDF اسکن‌شده** (که حاوی تصاویر نوشتار هستند)، مدل به‌طور خودکار «تشخیص نویسه نوری» (OCR) را اجرا می‌کند تا نوشتار را استخراج کند.

برای محاسبه تعداد کل نشان‌ها برای یک PDF، نشان‌های تصویری (۲۵۸ نشان در هر صفحه) را به نشان‌های نوشتاری اضافه کنید. ورودی‌های شما باید در **حد مجاز ۸٬۱۹۲ واحد کد** مدل (که بین همه روش‌ها هم‌رسانی می‌شود) جای بگیرد. سیستم به‌طور بی‌صدا ورودی‌هایی را که از این حد فراتر می‌روند کوتاه می‌کند.

#### محدودیت‌های PDF

- **فایل‌ها در هر درخواست:** می‌توانید حداکثر ۱ فایل PDF ارسال کنید.
- **محدودیت صفحه:** می‌توانید حداکثر ۶ صفحه در هر فایل ارسال کنید. برای بهترین کیفیت، اکیداً توصیه می‌کنیم از ۱ صفحه در هر PDF استفاده کنید.

مثال زیر نحوه جاسازی PDF بااستفاده از `gemini-embedding-2` را نشان می‌دهد:

### Python

```
from google import genai
from google.genai import types

with open('example.pdf', 'rb') as f:
    pdf_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=pdf_bytes,
            mime_type='application/pdf',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const pdfBase64 = fs.readFileSync("example.pdf", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'application/pdf',
                data: pdfBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] pdfBytes = Files.readAllBytes(Paths.get("example.pdf"));

Content content = Content.fromParts(Part.fromBytes(pdfBytes, "application/pdf"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
```

### REST

```
PDF_PATH="/path/to/your/example.pdf"
PDF_BASE64=$(base64 -w0 "${PDF_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "application/pdf",
                    "data": "'"${PDF_BASE64}"'"
                }
            }]
        }
    }'
```

## موارد استفاده

جاسازی‌های متن برای انواع موارد استفاده رایج هوش مصنوعی، مانند موارد زیر، حیاتی است:

- **تولید با کمک بازیابی (RAG):** جاسازی‌ها با بازیابی و گنجاندن اطلاعات مرتبط در بافت مدل، کیفیت نوشتار تولیدشده را بهبود می‌بخشند.
- **بازیابی اطلاعات:** جستجوی متن یا
  اسناد با بیشترین شباهت معنایی با یک قطعه متن ورودی.

  [آموزش گام‌به‌گام جستجوی سندtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **رتبه‌بندی مجدد جستجو**: با امتیازدهی معنایی نتایج اولیه دربرابر پُرسمان، مرتبط‌ترین موارد را در اولویت قرار دهید.

  [آموزش گام‌به‌گام رتبه‌بندی مجدد جستجوtask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **تشخیص ناهنجاری:** مقایسه گروه‌های جاسازی می‌تواند به شناسایی گرایش‌های پنهان یا داده‌های دورافتاده کمک کند.

  [آموزش گام‌به‌گام تشخیص ناهنجاریbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **طبقه‌بندی:** نوشتار را براساس محتوایش به‌طور خودکار طبقه‌بندی کنید،
  برای نمونه، تحلیل احساسات یا تشخیص هرزنامه

  [آموزش طبقه‌بندیtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **خوشه‌بندی:** با ایجاد خوشه‌ها و دیداری‌سازی‌های جاسازی‌ها، روابط پیچیده را به‌طور مؤثر درک کنید.

  [آموزش گام‌به‌گام مصورسازی خوشه‌ایbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## ذخیره کردن جاسازی‌ها

وقتی جاسازی‌ها را به تولید می‌برید، معمولاً از **پایگاه‌های داده برداری** برای ذخیره، نمایه‌گذاری، و بازیابی کارآمد جاسازی‌های با ابعاد بالا استفاده می‌شود. ‫Google Cloud خدمات داده مدیریت‌شده‌ای ارائه می‌دهد که
می‌تواند برای این هدف استفاده شود، ازجمله
[جستجوی برداری پلاتفرم عامل Gemini Enterprise نسخه ۲.۰](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview?hl=fa)،
[BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=fa)،
[AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=fa)، و
[Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=fa).

آموزش‌های گام‌به‌گام زیر نحوه استفاده از پایگاه‌های داده برداری طرف سوم دیگر را
با «جاسازی Gemini» نشان می‌دهد.

- [آموزش‌های ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [آموزش‌های QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [آموزش‌های Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [آموزش‌های Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## نسخه‌های مدل

### Gemini Embedding 2

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | **Gemini API**  `gemini-embedding-2` |
| انواع داده‌های پشتیبانی‌شده برای ذخیره کردن | **ورودی**  نوشتار، تصویر، ویدیو، صدا، PDF  **برونداد**  جاسازی‌های نوشتاری |
| token\_autoمحدودیت‌های نشان[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) | **محدودیت داده‌واحد ورودی**  ۸٬۱۹۲  **اندازه بُعد برونداد**  انعطاف‌پذیر، پشتیبانی می‌کند: ۱۲۸ تا ۳۰۷۲، توصیه‌شده: ۷۶۸، ۱۵۳۶، ۳۰۷۲ |
| ‫۱۲۳نسخه | برای جزئیات بیشتر، [الگوهای نسخه مدل](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fa#model-versions) را بخوانید.  - پایدار: `gemini-embedding-2` |
| calendar\_monthآخرین به‌روزرسانی | آوریل ۲۰۲۶ |

### جاسازی Gemini

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | **Gemini API**  `gemini-embedding-001` |
| انواع داده‌های پشتیبانی‌شده برای ذخیره کردن | **ورودی**  نوشتار  **برونداد**  جاسازی‌های نوشتاری |
| token\_autoمحدودیت‌های نشان[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) | **محدودیت داده‌واحد ورودی**  ۲٬۰۴۸  **اندازه بُعد برونداد**  انعطاف‌پذیر، پشتیبانی می‌کند: ۱۲۸ تا ۳۰۷۲، توصیه‌شده: ۷۶۸، ۱۵۳۶، ۳۰۷۲ |
| ‫۱۲۳نسخه | برای جزئیات بیشتر، [الگوهای نسخه مدل](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fa#model-versions) را بخوانید.  - پایدار: `gemini-embedding-001` |
| calendar\_monthآخرین به‌روزرسانی | ژوئن ۲۰۲۵ |

برای مدل‌های «جاسازی» منسوخ‌شده، به صفحه
[منسوخ‌شده‌ها](https://ai.google.dev/gemini-api/docs/deprecations?hl=fa) مراجعه کنید

## انتقال از gemini-embedding-001

فضاهای جاسازی بین `gemini-embedding-001` و
`gemini-embedding-2` **ناسازگار** است. این یعنی نمی‌توانید جاسازی‌های تولیدشده توسط یک مدل را مستقیماً با جاسازی‌های تولیدشده توسط مدل دیگر مقایسه کنید. اگر به `gemini-embedding-2` ارتقا می‌دهید، باید
همه داده‌های موجودتان را دوباره جاسازی کنید.

علاوه‌بر ناسازگاری، تفاوت‌های قابل‌توجه دیگری بین این دو مدل وجود دارد:

- **مشخصات نوع تکلیف:** با `gemini-embedding-001`، نوع تکلیف را بااستفاده از پارامتر `task_type` مشخص می‌کنید (برای نمونه، `SEMANTIC_SIMILARITY`،
  `RETRIEVAL_DOCUMENT`). با `gemini-embedding-2`، پارامتر `task_type`
  پشتیبانی نمی‌شود. درعوض، باید دستورالعمل‌های تکلیف را
  مستقیماً در پیام‌واره تکلیف‌های فقط نوشتاری بگنجانید. برای جزئیات مربوط به نحوه قالب‌بندی پیام‌واره‌ها برای موارد استفاده مختلف، به
  [انواع تکلیف با «جاسازی‌های ۲»](#task-types-embeddings-2) مراجعه کنید.
- **انبوهش جاسازی:** `gemini-embedding-001` برای هر رشته در فهرست ورودی‌ها جاسازی‌های جداگانه تولید می‌کند. درمقابل،
  `gemini-embedding-2` وقتی چندین ورودی (مثل نوشتار و تصویر) مستقیماً در یک درخواست ارائه می‌شود، یک جاسازی تکی و تجمیعی تولید می‌کند. برای تولید جاسازی‌های جداگانه برای ورودی‌های فردی، هر ورودی را در یک
  `Content` شیء بپیچید، یا از
  [میانای برنامه‌سازی کاربردی دسته‌ای](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa#batch-embedding) استفاده کنید. برای اطلاعات بیشتر،
  [تجمیع جاسازی](#embedding-aggregation) را ببینید.
- **به‌هنجارسازی:** اگر از `output_dimensionality` برای درخواست جاسازی‌هایی با کمتر از ۳۰۷۲ بُعد استفاده می‌کنید، `gemini-embedding-2` به‌طور خودکار این جاسازی‌های کوتاه را به‌هنجار می‌کند. با `gemini-embedding-001`، باید
  برای ابعاد غیر از ۳۰۷۲، عادی‌سازی دستی انجام دهید. برای جزئیات، به
  [تضمین کیفیت برای ابعاد کوچک‌تر](#quality-for-smaller-dimensions)
  مراجعه کنید.

## جاسازی‌های گروهی

اگر تأخیر برایتان مهم نیست، از مدل‌های «جاسازی Gemini» با
[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa#batch-embedding) استفاده کنید. این کار
امکان می‌دهد توان عملیاتی بسیار بالاتری با ۵۰٪ قیمت پیش‌فرض «جاسازی» داشته باشید.
نمونه‌هایی از نحوه شروع کار در
[کتاب آشپزی Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb) پیدا کنید.

## اعلان استفاده مسئولانه

برخلاف مدل‌های هوش مصنوعی زایا که محتوای جدید ایجاد می‌کنند، مدل Gemini Embedding
فقط برای تبدیل قالب داده‌های ورودی شما به یک نمایش عددی درنظر گرفته شده است. درحالی‌که Google مسئول ارائه مدل جاسازی است که قالب داده‌های ورودی شما را به قالب عددی درخواستی تبدیل می‌کند، کاربران مسئولیت کامل داده‌هایی را که وارد می‌کنند و جاسازی‌های حاصل از آن را برعهده دارند. بااستفاده از مدل «جاسازی Gemini» تأیید می‌کنید که
حقوق لازم را برای هر محتوایی که بارگذاری می‌کنید دارید. محتوایی تولید نکنید که
حق نشر مالکیت فکری یا حقوق حریم خصوصی دیگران را نقض می‌کند. استفاده شما از این سرویس تابع [خط‌مشی کاربردهای غیرمجاز](https://policies.google.com/terms/generative-ai/use-policy?hl=fa) و [شرایط خدمات Google](https://ai.google.dev/gemini-api/terms?hl=fa) ما است.

## شروع ساختن با جاسازی‌ها

برای کاوش قابلیت‌های مدل و آشنایی با نحوه سفارشی‌سازی و
تصویرسازی جاسازی‌ها، [دفترچه شروع سریع جاسازی‌ها](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) را بررسی کنید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-09 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-09 به‌وقت ساعت هماهنگ جهانی."],[],[]]
