---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=ar
fetched_at: 2026-10-05T06:38:13.050458+00:00
title: "\u0627\u0644\u062a\u0636\u0645\u064a\u0646\u0627\u062a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# التضمينات

توفّر Gemini API نماذج تضمين لإنشاء تضمينات للنصوص والصور والفيديوهات والمحتوى الآخر. يمكن بعد ذلك استخدام التضمينات الناتجة في مهام مثل البحث الدلالي والتصنيف والتجميع، ما يوفّر نتائج أكثر دقة ومراعية للسياق مقارنةً بالطرق المستندة إلى الكلمات الرئيسية.

أحدث نموذج، `gemini-embedding-2`، هو أول نموذج متعدد الوسائط
لإنشاء تضمينات في Gemini API. يعمل هذا النموذج على ربط النصوص والصور والفيديوهات والمقاطع الصوتية والمستندات بمساحة تضمين موحّدة، ما يتيح البحث والتصنيف والتجميع المتعدّد الوسائط بأكثر من 100 لغة. يمكنك الاطّلاع على [قسم "التضمينات المتعدّدة الوسائط"](#multimodal) لمعرفة المزيد. بالنسبة إلى حالات الاستخدام النصية فقط، سيظل `gemini-embedding-001` متاحًا.

إنشاء أنظمة التوليد المعزّز بالاسترجاع (RAG) هو حالة استخدام شائعة لمنتجات الذكاء الاصطناعي. تؤدي التضمينات دورًا رئيسيًا في تحسين مخرجات النماذج بشكل كبير،
من خلال تعزيز دقتها الوقائعية وتماسكها وثراء سياقها. إذا كنت تفضّل استخدام حلّ مُدار للتوليد المعزّز بالاسترجاع، أنشأنا أداة [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar) التي تسهّل إدارة عملية التوليد المعزّز بالاسترجاع وتجعلها أكثر فعالية من حيث التكلفة.

## إنشاء التضمينات

استخدِم طريقة `embedContent` لإنشاء تضمينات نصية:

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

### جافا

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", "What is the meaning of life?", null);

System.out.println(response.embeddings().orElse(null));
```

### Go

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

## تحديد نوع المهمة لتحسين الأداء

يمكنك استخدام التضمينات في مجموعة كبيرة من المهام، بدءًا من التصنيف وصولاً إلى البحث عن المستندات. يساعد تحديد نوع المهمة المناسب في تحسين عمليات التضمين للعلاقات المقصودة، ما يؤدي إلى زيادة الدقة والفعالية إلى أقصى حد.

### أنواع المهام التي يمكن تنفيذها باستخدام Embeddings 2

بالنسبة إلى المهام النصية فقط التي تتضمّن `gemini-embedding-2`، ننصحك بشدة بإضافة تعليمات المهمة في طلبك. ويمكن إجراء ذلك من خلال تنسيق طلب البحث والمستند باستخدام بادئة المهمة الصحيحة.

عند إنشاء [تضمين واحد استنادًا إلى إدخال متعدد الوسائط](#embedding-aggregation)، لا ننصح عمومًا بإضافة بادئة إلى جزء النص من الإدخال تتضمّن تعليمات المهمة. وفي بعض الحالات، يؤدي ذلك إلى تحسين الأداء، ولكن في حالات أخرى، يؤدي إلى خفضه.

تعرض الجداول التالية أمثلة على كيفية تنسيق طلبات البحث والمستندات لحالات الاستخدام المتماثلة وغير المتماثلة باستخدام نموذج `gemini-embedding-2`.

**حالات استخدام الاسترجاع (تنسيق غير متماثل)**

في حالات الاستخدام غير المتماثل، أضِف بادئة المهمة إلى طلب البحث وطبِّق بنية المستند على المحتوى الذي تريد تضمينه واسترداده.

| حالة الاستخدام | بنية طلب البحث | بنية المستند |
| --- | --- | --- |
| طلب البحث | `task: search result | query: {content}` | `title: {title} | text: {content}` في حال عدم توفّر عنوان، استخدِم `title: none`. |
| الإجابة عن الأسئلة | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| التحقّق من صحة الأخبار | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| استرداد الرمز | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**مثال على الاستخدام**

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

**حالات استخدام الإدخال الفردي (التنسيق المتماثل)**

في حالات الاستخدام المتماثلة، استخدِم التنسيق نفسه للاستعلام والمستند في المهمة نفسها.

| حالة الاستخدام | بنية الإدخال |
| --- | --- |
| التصنيف | `task: classification | query: {content}` |
| التجميع | `task: clustering | query: {content}` |
| التشابه الدلالي | `task: sentence similarity | query: {content}` لا تستخدِم هذه الميزة للبحث أو الاسترجاع. وهي مخصّصة للتشابه الدلالي النصي. |

**مثال على الاستخدام**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

من المهم استخدام المهمة بشكلٍ متّسق. على سبيل المثال، إذا كانت المستندات مضمّنة مع `f'task: classification | query: {content}'`، يجب أن يكون طلب البحث مضمّنًا أيضًا باتّباع تنسيق المهمة هذا.

### أنواع المهام التي تتضمّن Embeddings 1

بالنسبة إلى `gemini-embedding-001`، يمكنك تحديد `task_type` في طريقة `embedContent`. للحصول على قائمة كاملة بأنواع المهام المتوافقة، راجِع جدول [أنواع المهام المتوافقة](#supported-task-types).

يوضّح المثال التالي كيفية استخدام `SEMANTIC_SIMILARITY` للتحقّق من مدى تشابه معاني سلاسل النصوص.

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

### جافا

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

### Go

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

ستوضّح مقتطفات الرموز مدى تشابه مقاطع النص المختلفة مع بعضها البعض عند تشغيلها.

#### أنواع المهام المتوافقة

أنواع المهام المتوافقة مع `gemini-embedding-001`:

| نوع المهمة | الوصف | أمثلة |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | تضمينات محسّنة لتقييم التشابه بين النصوص | أنظمة الاقتراح، رصد المحتوى المكرّر |
| **التصنيف** | تضمينات محسَّنة لتصنيف النصوص وفقًا لتصنيفات محدَّدة مسبقًا | تحليل المشاعر ورصد الرسائل غير المرغوب فيها |
| **التجميع** | تكون عمليات التضمين محسّنة لتجميع النصوص استنادًا إلى أوجه التشابه بينها. | تنظيم المستندات وأبحاث السوق ورصد القيم الشاذة |
| **RETRIEVAL\_DOCUMENT** | تضمينات محسّنة للبحث عن المستندات | فهرسة المقالات أو الكتب أو صفحات الويب لتسهيل البحث فيها |
| **RETRIEVAL\_QUERY** | تضمينات محسّنة لطلبات البحث العامة استخدِم `RETRIEVAL_QUERY` للاستعلامات و`RETRIEVAL_DOCUMENT` للمستندات التي سيتم استرجاعها. | تجربة مخصّصة على شبكة البحث |
| **CODE\_RETRIEVAL\_QUERY** | تضمينات محسَّنة لاسترداد مجموعات الرموز استنادًا إلى طلبات البحث باللغة الطبيعية استخدِم `CODE_RETRIEVAL_QUERY` لطلبات البحث و`RETRIEVAL_DOCUMENT` لكتل الرموز البرمجية التي سيتم استردادها. | اقتراحات الرموز البرمجية والبحث |
| **QUESTION\_ANSWERING** | تضمينات للأسئلة في نظام الإجابة عن الأسئلة، تم تحسينها للعثور على المستندات التي تجيب عن السؤال استخدِم `QUESTION_ANSWERING` لطرح الأسئلة و`RETRIEVAL_DOCUMENT` لاسترداد المستندات. | مربّع الدردشة |
| **FACT\_VERIFICATION** | تضمين عبارات تحتاج إلى التحقّق، وتم تحسينها لاسترداد المستندات التي تتضمّن أدلة تؤيّد العبارة أو تدحضها استخدِم `FACT_VERIFICATION` للنص المستهدَف و`RETRIEVAL_DOCUMENT` للمستندات المطلوب استرجاعها | أنظمة التحقّق الآلي من صحة الأخبار |

## التحكّم في حجم التضمين

يتم تدريب كل من `gemini-embedding-001` و`gemini-embedding-2` باستخدام تقنية Matryoshka Representation Learning (MRL) التي تعلّم النموذج كيفية التعرّف على عمليات التضمين العالية الأبعاد التي تتضمّن مقاطع أولية (أو بادئات) مفيدة أيضًا، وهي عبارة عن إصدارات أبسط من البيانات نفسها.

استخدِم المَعلمة `output_dimensionality` للتحكّم في حجم
متّجه التضمين الناتج. يمكن أن يؤدي اختيار عدد أصغر من الأبعاد الناتجة إلى توفير مساحة التخزين وزيادة كفاءة الحوسبة للتطبيقات اللاحقة، مع التضحية بالقليل من حيث الجودة. بشكل تلقائي، ينتج كلا النموذجين تضمينًا
بـ 3072 بُعدًا، ولكن يمكنك تقصيره إلى حجم أصغر بدون
فقدان الجودة لتوفير مساحة التخزين. ننصحك باستخدام أبعاد الإخراج 768 أو 1536 أو 3072.

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

### جافا

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

### Go

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

مثال على الناتج من مقتطف الرمز:

```
Length of embedding: 768
```

## ضمان الجودة للأبعاد الأصغر

في حين يتم دائمًا تسوية عمليات التضمين التلقائية ذات 3072 بُعدًا، تعمل Gemini
Embedding 2 أيضًا على تسوية الأبعاد المقتطعة تلقائيًا (مثل 768 و1536). يضمن ذلك احتساب التشابه الدلالي من خلال اتجاه المتّجه بدلاً من حجمه، ما يوفّر نتائج أكثر دقة بدون الحاجة إلى إجراء أي تعديلات.

**الطُرز القديمة**: إذا كنت تستخدم `gemini-embedding-001`، عليك تسوية الأبعاد غير 3072 يدويًا باتّباع الخطوات التالية:

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

مثال على الناتج من مقتطف الرمز هذا:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

يعرض الجدول التالي نتائج MTEB، وهو مقياس أداء شائع الاستخدام لعمليات التضمين، وذلك لمختلف السمات. والجدير بالذكر أنّ النتيجة توضّح أنّ الأداء
لا يرتبط بشكل صارم بحجم سمة التضمين، إذ حقّقت السمات ذات الأبعاد المنخفضة نتائج مماثلة للسمات ذات الأبعاد الأعلى.

| سمة MRL | نتيجة MTEB (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## التضمينات المتعددة الوسائط

يتيح نموذج `gemini-embedding-2` إدخال محتوى متعدّد الوسائط، ما يسمح لك بتضمين صور وفيديوهات ومقاطع صوتية ومستندات إلى جانب النصوص. يتم ربط جميع الوسائط بمساحة التضمين نفسها، ما يتيح البحث والمقارنة بين الوسائط المختلفة.

### الوسائط المتوافقة والحدود

الحد الأقصى العام لعدد الرموز المميزة المُدخلة هو 8192 رمزًا مميزًا.

| نمط البيانات | المواصفات والحدود |
| --- | --- |
| **Text** | يمكنه التعامل مع ما يصل إلى 8,192 رمزًا مميزًا. |
| **صورة** | يمكن إرسال 6 صور كحد أقصى لكل طلب. التنسيقات المتوافقة: PNG وJPEG |
| **الصوت** | الحدّ الأقصى للمدة هو 180 ثانية. التنسيقات المتوافقة: MP3 وWAV |
| **الفيديو** | المدة القصوى هي 120 ثانية. التنسيقات المتوافقة: MP4 وMOV برامج الترميز المتوافقة: H264 وH265 وAV1 وVP9  يعالج النظام 32 لقطة كحدّ أقصى لكل فيديو: يتم أخذ عيّنات من الفيديوهات القصيرة (≤32 ثانية) بمعدّل لقطة واحدة في الثانية، بينما يتم أخذ عيّنات من الفيديوهات الأطول بشكل موحّد بمعدّل 32 لقطة. لا تتم معالجة المقاطع الصوتية في ملفات الفيديو. |
| **المستندات (ملف PDF)** | يمكن إرسال ملف واحد كحد أقصى لكل طلب، على ألا يزيد عدد الصفحات عن 6. |

### تضمين الصور

يوضّح المثال التالي كيفية تضمين صورة باستخدام `gemini-embedding-2`.

يمكن تقديم الصور كبيانات مضمّنة أو كملفات تم تحميلها
من خلال [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar).

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

### جافا

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

### تجميع التضمين

عند العمل على محتوى متعدد الوسائط، تؤثر طريقة تنظيم الإدخال في
مخرجات التضمين:

- **أجزاء متعددة (مجمّعة):** تؤدي إضافة مدخلات متعددة مباشرةً إلى المَعلمة
  `contents` إلى إنشاء عملية تضمين مجمّعة واحدة لجميع المدخلات.
- **عناصر `Content` متعددة (منفصلة):** يؤدي تضمين كل إدخال في عنصر `Content`
  وتمريرها في المَعلمة `contents` إلى عرض
  تضمينات منفصلة لكل إدخال.
- **التمثيل على مستوى المنشور:** بالنسبة إلى الكائنات المعقّدة، مثل المشاركات على وسائل التواصل الاجتماعي التي تتضمّن عناصر وسائط متعدّدة، ننصح بتجميع التضمينات المنفصلة (على سبيل المثال، عن طريق حساب المتوسط) لإنشاء تمثيل متماسك على مستوى المنشور.

يوضّح المثال التالي كيفية إنشاء عملية تضمين مجمّعة واحدة لكل من النص والصورة. ما عليك سوى إضافة مدخلات متعدّدة إلى المَعلمة `contents`:

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

### جافا

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

من ناحية أخرى، إذا كنت تستخدم عناصر `Content` داخل المَعلمة `contents`، سيعرض ذلك تضمينات منفصلة. ينشئ هذا المثال عدة تضمينات في طلب تضمين واحد:

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

### جافا

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

### تضمين الصوت

يوضّح المثال التالي كيفية تضمين ملف صوتي باستخدام `gemini-embedding-2`.

يمكن تقديم ملفات الصوت كبيانات مضمّنة أو كملفات تم تحميلها
من خلال [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar).

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

### جافا

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

### تضمين فيديو

يوضّح المثال التالي كيفية تضمين فيديو باستخدام `gemini-embedding-2`.

يمكن تقديم الفيديوهات كبيانات مضمّنة أو كملفات تم تحميلها
من خلال [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar).

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

### جافا

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

إذا كنت بحاجة إلى تضمين فيديوهات تزيد مدتها عن 120 ثانية، يمكنك تقسيم الفيديو إلى مقاطع متداخلة وتضمين هذه المقاطع بشكل فردي.

### تضمين المستندات

يمكن تضمين المستندات بتنسيق PDF مباشرةً. يعالج النموذج المحتوى المرئي والنصي لكل صفحة.

يمكن تقديم ملفات PDF كبيانات مضمّنة أو كملفات تم تحميلها
من خلال [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar).

#### طريقة معالجة النموذج لملفات PDF

عند تضمين ملف PDF، يعالج النموذج المستند باستخدام ميزات مرئية ونصية:

- **التمثيل المرئي:** يعرض النموذج كل صفحة كصورة، ما يستهلك **258 رمزًا مميزًا** لكل صفحة.
- **استخراج النص:** يستخرج النموذج النص من المستند. بالنسبة إلى **ملفات PDF الأصلية** (التي تحتوي على نص رقمي)، يستخرج النموذج النص مباشرةً. بالنسبة إلى **ملفات PDF الممسوحة ضوئيًا** (التي تحتوي على صور للنص)، يشغّل النموذج تلقائيًا تقنية التعرّف البصري على الأحرف (OCR) لاستخراج النص.

لاحتساب إجمالي عدد الرموز المميزة في ملف PDF، أضِف الرموز المميزة المرئية (258 رمزًا مميزًا لكل صفحة) إلى الرموز المميزة النصية. يجب أن تتناسب مدخلاتك مع **الحد الأقصى البالغ 8,192 رمزًا مميزًا** في النموذج (يتم مشاركته بين جميع الوسائط). يقتطع النظام تلقائيًا المدخلات التي تتجاوز هذا الحد.

#### حدود ملفات PDF

- **الملفات لكل طلب:** يمكنك إرسال ملف PDF واحد كحدّ أقصى.
- **الحدّ الأقصى لعدد الصفحات:** يمكنك إرسال 6 صفحات كحدّ أقصى لكل ملف. للحصول على أفضل جودة، ننصحك بشدة باستخدام صفحة واحدة لكل ملف PDF.

يوضّح المثال التالي كيفية تضمين ملف PDF باستخدام `gemini-embedding-2`:

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

### جافا

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

## حالات الاستخدام

تُعدّ تضمينات النصوص ضرورية لمجموعة متنوّعة من حالات الاستخدام الشائعة للذكاء الاصطناعي، مثل:

- **التوليد المعزّز بالاسترجاع (RAG):** تعمل التضمينات على تحسين جودة النص الذي يتم إنشاؤه من خلال استرجاع المعلومات ذات الصلة ودمجها في سياق النموذج.
- **استرجاع المعلومات:** البحث عن النص أو المستندات الأكثر تشابهًا من الناحية الدلالية، وذلك بالاستناد إلى جزء من النص المدخل

  [برنامج تعليمي حول البحث عن المستنداتtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **إعادة ترتيب نتائج البحث**: إعطاء الأولوية للعناصر الأكثر صلة من خلال تقييم النتائج الأولية دلاليًا مقارنةً بطلب البحث.

  [البرنامج التعليمي لإعادة ترتيب نتائج البحثtask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **رصد القيم الشاذة:** يمكن أن تساعد مقارنة مجموعات التضمينات في تحديد المؤشرات المخفية أو القيم الشاذة.

  [برنامج تعليمي حول رصد القيم الشاذةbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **التصنيف:** تصنيف النصوص تلقائيًا استنادًا إلى محتواها، مثل تحليل المشاعر أو رصد الرسائل غير المرغوب فيها

  [البرنامج التعليمي للتصنيفtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **التجميع:** يمكنك فهم العلاقات المعقّدة بشكل فعّال من خلال إنشاء مجموعات وتصوّرات لعمليات التضمين.

  [برنامج تعليمي حول العرض المرئي للتجميعbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## تخزين التضمينات

عند نقل عمليات التضمين إلى مرحلة الإنتاج، من الشائع استخدام **قواعد بيانات المتّجهات** لتخزين عمليات التضمين العالية الأبعاد وفهرستها واسترجاعها بكفاءة. تقدّم Google Cloud خدمات بيانات مُدارة يمكن استخدامها لهذا الغرض، بما في ذلك [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview?hl=ar) و[BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=ar) و[AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=ar) و[Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=ar).

توضّح البرامج التعليمية التالية كيفية استخدام قواعد بيانات متجهات تابعة لجهات خارجية أخرى مع Gemini Embedding.

- [برامج تعليمية حول ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [برامج QDrant التعليميةbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [برامج Weaviate التعليميةbolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [برامج Pinecone التعليميةbolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## إصدارات النموذج

### Gemini Embedding 2

| الموقع | الوصف |
| --- | --- |
| رمز النموذج id\_card | **Gemini API**  `gemini-embedding-2` |
| saveأنواع البيانات المتوافقة | **الإدخال**  النصوص والصور والفيديوهات والملفات الصوتية وملفات PDF  **الناتج**  تضمينات النص |
| token\_autoحدود الرموز المميزة[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) | **الحدّ الأقصى لعدد الرموز المميزة التي يمكن إدخالها**  8,192  **حجم سمة الإخراج**  مرن، ويتوافق مع: 128 - 3072، الحجم المقترَح: 768 و1536 و3072 |
| 123الإصدارات | يمكنك الاطّلاع على [أنماط إصدارات النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#model-versions) لمزيد من التفاصيل.  - إصدار ثابت: `gemini-embedding-2` |
| calendar\_monthآخر تعديل | أبريل 2026 |

### تضمين Gemini

| الموقع | الوصف |
| --- | --- |
| رمز النموذج id\_card | **Gemini API**  `gemini-embedding-001` |
| saveأنواع البيانات المتوافقة | **الإدخال**  نص  **الناتج**  تضمينات النص |
| token\_autoحدود الرموز المميزة[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) | **الحدّ الأقصى لعدد الرموز المميزة التي يمكن إدخالها**  2,048  **حجم سمة الإخراج**  مرن، ويتوافق مع: 128 - 3072، الحجم المقترَح: 768 و1536 و3072 |
| 123الإصدارات | يمكنك الاطّلاع على [أنماط إصدارات النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#model-versions) لمزيد من التفاصيل.  - إصدار ثابت: `gemini-embedding-001` |
| calendar\_monthآخر تعديل | يونيو 2025 |

بالنسبة إلى نماذج Embeddings المتوقّفة نهائيًا، يُرجى الانتقال إلى صفحة [الإيقافات النهائية](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar).

## نقل البيانات من gemini-embedding-001

مساحات التضمين بين `gemini-embedding-001` و`gemini-embedding-2` **غير متوافقة**. وهذا يعني أنّه لا يمكنك مقارنة التضمينات التي تم إنشاؤها بواسطة نموذج معيّن بالتضمينات التي تم إنشاؤها بواسطة نموذج آخر بشكل مباشر. إذا كنت بصدد الترقية إلى `gemini-embedding-2`، عليك إعادة تضمين جميع بياناتك الحالية.

بالإضافة إلى عدم التوافق، هناك العديد من الاختلافات الأخرى بين النموذجين، وهي:

- **تحديد نوع المهمة:** باستخدام `gemini-embedding-001`، يمكنك تحديد نوع المهمة باستخدام المَعلمة `task_type` (مثل `SEMANTIC_SIMILARITY` و`RETRIEVAL_DOCUMENT`). أما باستخدام `gemini-embedding-2`، فلا تتوفّر المَعلمة `task_type`. بدلاً من ذلك، عليك تضمين تعليمات المهمة مباشرةً في الطلب الخاص بالمهام التي تتضمّن نصًا فقط. راجِع مقالة
  [أنواع المهام التي تستخدم Embeddings 2](#task-types-embeddings-2) للحصول على تفاصيل حول كيفية
  تنسيق الطلبات لحالات الاستخدام المختلفة.
- **تجميع التضمينات:** تنشئ `gemini-embedding-001` تضمينات فردية لكل سلسلة في قائمة من المدخلات. في المقابل،
  تنتج `gemini-embedding-2` تضمينًا واحدًا مجمّعًا عند تقديم مدخلات متعددة (مثل النصوص والصور) مباشرةً في طلب واحد. لإنشاء تضمينات منفصلة لكل إدخال على حدة، عليك تضمين كل إدخال في عنصر `Content`، أو استخدام [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar#batch-embedding). لمزيد من المعلومات، اطّلِع على مقالة [تضمين التجميع](#embedding-aggregation).
- **التسوية:** إذا كنت تستخدم `output_dimensionality` لطلب تضمينات بأقل من 3072 سمة، ستعمل `gemini-embedding-2` تلقائيًا على تسوية هذه التضمينات المقتطعة. باستخدام `gemini-embedding-001`، عليك إجراء تسوية يدوية للسمات التي تختلف عن 3072. لمزيد من التفاصيل، يُرجى الاطّلاع على مقالة [ضمان الجودة للأبعاد الأصغر](#quality-for-smaller-dimensions).

## التضمينات المجمّعة

إذا لم يكن وقت الاستجابة مصدر قلق، جرِّب استخدام نماذج Gemini Embeddings مع [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar#batch-embedding). يتيح ذلك سرعة معالجة بيانات أعلى بكثير بنسبة% 50 من سعر Embedding التلقائي.
يمكنك العثور على أمثلة حول كيفية البدء في [كتاب وصفات Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## إشعار الاستخدام المسؤول

على عكس نماذج الذكاء الاصطناعي التوليدي التي تنشئ محتوًى جديدًا، يهدف نموذج Gemini Embedding إلى تحويل تنسيق بيانات الإدخال إلى تمثيل رقمي فقط. في حين أنّ Google مسؤولة عن توفير نموذج تضمين
يحوّل تنسيق بيانات الإدخال إلى التنسيق الرقمي المطلوب،
يحتفظ المستخدمون بالمسؤولية الكاملة عن البيانات التي يدخلونها وعمليات التضمين الناتجة. يشير استخدامك لنموذج Gemini Embedding إلى تأكيدك على امتلاك الحقوق اللازمة لأي محتوى يتم تحميله. ويجب عدم إنشاء محتوى ينتهك حقوق الملكية الفكرية أو حقوق الخصوصية للآخرين. يخضع استخدامك لهذه الخدمة [لسياسة الاستخدام المحظور](https://policies.google.com/terms/generative-ai/use-policy?hl=ar) و[بنود خدمة Google](https://ai.google.dev/gemini-api/terms?hl=ar).

## بدء التطوير باستخدام عمليات التضمين

اطّلِع على [دفتر ملاحظات البدء السريع الخاص بالتضمينات](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) لاستكشاف إمكانات النموذج والتعرّف على كيفية تخصيص التضمينات وعرضها بشكل مرئي.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-18 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-18 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
