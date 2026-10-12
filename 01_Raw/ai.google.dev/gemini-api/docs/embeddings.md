---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-TW
fetched_at: 2026-10-12T07:17:00.331404+00:00
title: "\u5d4c\u5165 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 嵌入

Gemini API 提供嵌入模型，可為文字、圖片、影片和其他內容生成嵌入內容。這些產生的嵌入內容可用於語意搜尋、分類和叢集等工作，提供比關鍵字方法更準確、情境感知的結果。

最新模型 `gemini-embedding-2` 是 Gemini API 中第一個多模態嵌入模型。可將文字、圖片、影片、音訊和文件對應至統一的嵌入空間，以 100 多種語言進行跨模式搜尋、分類和叢集。詳情請參閱[多模態嵌入部分](#multimodal)。如要處理純文字內容，仍可使用 `gemini-embedding-001`。

建構檢索增強生成 (RAG) 系統是 AI 產品的常見用途。嵌入在大幅提升模型輸出內容方面扮演關鍵角色，可提高事實準確度、連貫性和情境豐富度。如果偏好使用代管 RAG 解決方案，我們打造的[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)工具可讓您更輕鬆地管理 RAG，並提高成本效益。

## 生成嵌入

使用 `embedContent` 方法生成文字嵌入：

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

### Java

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

## 指定工作類型以提升效能

從分類到文件搜尋，您可以使用嵌入項目執行各種工作。指定正確的任務類型有助於針對預期關係最佳化嵌入項目，進而提高準確度和效率。

### 使用 Embeddings 2 的工作類型

如果工作僅包含文字，且使用 `gemini-embedding-2`，強烈建議您在提示中加入工作指令。方法是使用正確的任務前置字串，設定查詢和文件的格式。

根據[多模態輸入內容產生單一嵌入內容](#embedding-aggregation)時，我們通常不建議在輸入內容的文字部分加上工作指令前置字元。有時可提升成效，有時則會降低成效。

下表提供範例，說明如何使用 `gemini-embedding-2` 模型，為對稱和非對稱用途格式化查詢和文件。

**擷取用途 (非對稱格式)**

在非對稱用途中，請在查詢中加入工作前置字元，並套用要嵌入及擷取內容的文件結構。

| 用途 | 查詢結構 | 文件結構 |
| --- | --- | --- |
| 搜尋查詢 | `task: search result | query: {content}` | `title: {title} | text: {content}` 如果沒有標題，請使用 `title: none`。 |
| 問題回答 | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| 事實查核 | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| 程式碼擷取 | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**使用範例**

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

**單一輸入內容的用途 (對稱格式)**

在對稱用途中，針對相同工作，查詢和文件使用相同的格式。

| 用途 | 輸入結構 |
| --- | --- |
| 分類 | `task: classification | query: {content}` |
| 分群 | `task: clustering | query: {content}` |
| Semantic similarity (語意相似度) | `task: sentence similarity | query: {content}` 請勿使用這項功能進行搜尋或擷取。適用於語意文字相似度。 |

**使用範例**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

請務必持續使用這項工作。舉例來說，如果文件內嵌 `f'task: classification | query: {content}'`，查詢也應按照這項工作格式內嵌。

### 使用 Embeddings 1 的工作類型

如要使用 `gemini-embedding-001`，可以在 `embedContent` 方法中指定 `task_type`。如需支援的完整工作類型清單，請參閱「[支援的工作類型](#supported-task-types)」表格。

以下範例說明如何使用 `SEMANTIC_SIMILARITY` 檢查文字字串的意義相似程度。

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

### Java

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

執行程式碼片段後，即可查看不同文字區塊的相似程度。

#### 支援的工作類型

`gemini-embedding-001`支援的任務類型：

| 工作類型 | 說明 | 範例 |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | 經過最佳化處理的嵌入，可評估文字相似度。 | 推薦系統、重複內容偵測 |
| **分類** | 經過最佳化處理的嵌入模型，可根據預設標籤分類文字。 | 情緒分析、垃圾訊息偵測 |
| **分群** | 經過最佳化，可根據相似度將文字分群。 | 文件整理、市場調查、異常偵測 |
| **RETRIEVAL\_DOCUMENT** | 專為文件搜尋最佳化的嵌入內容。 | 為搜尋功能建立文章、書籍或網頁的索引。 |
| **RETRIEVAL\_QUERY** | 針對一般搜尋查詢最佳化的嵌入內容。 使用 `RETRIEVAL_QUERY` 進行查詢；使用 `RETRIEVAL_DOCUMENT` 擷取文件。 | 自訂搜尋 |
| **CODE\_RETRIEVAL\_QUERY** | 經過最佳化處理的嵌入，可根據自然語言查詢擷取程式碼區塊。 使用 `CODE_RETRIEVAL_QUERY` 查詢；使用 `RETRIEVAL_DOCUMENT` 擷取程式碼區塊。 | 程式碼建議和搜尋 |
| **QUESTION\_ANSWERING** | 問答系統中的問題嵌入，經過最佳化處理，可找出回答問題的文件。 使用 `QUESTION_ANSWERING` 提問；使用 `RETRIEVAL_DOCUMENT` 擷取文件。 | Chatbox |
| **FACT\_VERIFICATION** | 需要驗證的陳述內容的嵌入內容，經過最佳化處理，可擷取含有佐證或反駁陳述內容的文件。 使用 `FACT_VERIFICATION` 做為目標文字；使用 `RETRIEVAL_DOCUMENT` 做為要擷取的檔案 | 自動事實查核系統 |

## 控制嵌入大小

`gemini-embedding-001`和 `gemini-embedding-2` 都是使用 Matryoshka 表徵學習 (MRL) 技術訓練而成，這項技術會教導模型學習高維度嵌入，這些嵌入具有初始區段 (或前置字元)，也是相同資料的實用簡化版本。

使用 `output_dimensionality` 參數控制輸出嵌入向量的大小。選取較小的輸出維度可節省儲存空間，並提高下游應用程式的運算效率，同時不會犧牲太多品質。這兩個模型預設都會輸出 3072 維度的嵌入內容，但您可以將其截斷為較小的尺寸，以節省儲存空間，且不會降低品質。建議使用 768、1536 或 3072 的輸出尺寸。

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

### Java

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

程式碼片段的輸出範例如下：

```
Length of embedding: 768
```

## 確保較小尺寸的品質

雖然預設的 3072 維度嵌入內容一律會經過正規化，但 Gemini Embedding 2 也會自動正規化截斷的維度 (例如 768、1536)。這可確保系統透過向量方向而非大小計算語意相似度，提供更準確的結果。

**舊版模型**：如果您使用 `gemini-embedding-001`，必須手動將非 3072 維度標準化，方法如下：

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

這個程式碼片段的輸出範例如下：

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

下表顯示不同維度的 MTEB 分數，這是評估嵌入內容時常用的基準。值得注意的是，結果顯示效能並非與嵌入維度大小嚴格相關，較低的維度可達到與較高維度對應項目相當的分數。

| MRL 維度 | MTEB 分數 (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## 多模態嵌入

`gemini-embedding-2` 模型支援多模態輸入，可讓您在文字中嵌入圖片、影片、音訊和文件內容。所有模態都會對應到相同的嵌入空間，方便進行跨模態搜尋和比較。

### 支援的模態和限制

輸入權杖總數上限為 8192 個。

| 模態 | 規格和限制 |
| --- | --- |
| **文字** | 最多支援 8,192 個權杖。 |
| **圖片** | 每項要求最多可上傳 6 張圖片。支援的格式：PNG、JPEG。 |
| **音訊** | 時間長度上限為 180 秒。支援的格式：MP3、WAV。 |
| **影片** | 時間長度上限為 120 秒。支援的格式：MP4、MOV。支援的轉碼器：H264、H265、AV1、VP9。  系統最多會處理每部影片的 32 個影格：短片 (≤32 秒) 的取樣率為每秒 1 個影格，較長的影片則會均勻取樣至 32 個影格。影片檔案中的音軌不會經過處理。 |
| **文件 (PDF)** | 每項要求最多可上傳 1 個檔案，最多 6 頁。 |

### 嵌入圖片

以下範例說明如何使用 `gemini-embedding-2` 嵌入圖片。

圖片可以內嵌資料的形式提供，也可以透過 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw) 上傳檔案。

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

### Java

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

### 嵌入匯總

處理多模態內容時，輸入內容的結構會影響嵌入輸出內容：

- **多個部分 (匯總)：**直接在 `contents` 參數中新增多項輸入內容，即可為所有輸入內容產生一個匯總的嵌入。
- **多個 `Content` 物件 (分開)：**將每個輸入內容包裝在 `Content` 物件中，並在 `contents` 參數中傳遞這些物件，即可為每個項目傳回個別的嵌入內容。
- **貼文層級表示法：**如果是社群媒體貼文等複雜物件，且包含多個媒體項目，建議匯總個別嵌入 (例如取平均值)，建立連貫的貼文層級表示法。

以下範例說明如何為文字和圖片輸入內容建立一個匯總嵌入。只要在 `contents` 參數中新增多個輸入內容即可：

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

### Java

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

另一方面，如果您在 `contents` 參數中使用 `Content` 物件，則會傳回個別的嵌入內容。這個範例會在一次嵌入呼叫中建立多個嵌入：

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

### Java

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

### 嵌入音訊

以下範例說明如何使用 `gemini-embedding-2` 嵌入音訊檔案。

音訊檔案可以內嵌資料形式提供，也可以透過 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw) 上傳。

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

### Java

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

### 嵌入影片

以下範例說明如何使用 `gemini-embedding-2` 嵌入影片。

影片可以內嵌資料的形式提供，也可以透過 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw) 上傳檔案。

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

### Java

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

如要嵌入長度超過 120 秒的影片，可以將影片分成重疊的片段，然後個別嵌入這些片段。

### 嵌入文件

您可以直接嵌入 PDF 格式的文件。模型會處理每個網頁的視覺和文字內容。

你可以透過 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw)，以內嵌資料或上傳檔案的形式提供 PDF。

#### 模型如何處理 PDF

嵌入 PDF 時，模型會同時使用視覺和文字功能處理文件：

- **視覺化呈現：**模型會將每個網頁算繪為圖片，每個網頁會消耗 **258 個權杖**。
- **文字擷取：**模型會從文件中擷取文字。如果是**原生 PDF** (內含數位文字)，模型會直接擷取文字。如果是**掃描的 PDF** (內含文字圖片)，模型會自動執行光學字元辨識 (OCR) 來擷取文字。

如要計算 PDF 的詞元總數，請將視覺詞元 (每頁 258 個) 加到文字詞元。輸入內容必須符合模型的**8,192 個權杖限制** (所有模態共用)。如果輸入內容超過這個上限，系統會自動截斷。

#### PDF 限制

- **每個要求可提交的檔案數：**最多可提交 1 個 PDF 檔案。
- **頁面限制：**每個檔案最多可提交 6 個頁面。為確保最佳品質，我們強烈建議每個 PDF 檔案只包含 1 頁。

以下範例說明如何使用 `gemini-embedding-2` 嵌入 PDF：

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

### Java

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

## 用途

文字嵌入對於各種常見的 AI 用途至關重要，例如：

- **檢索增強生成 (RAG)：**嵌入項目可擷取相關資訊並納入模型背景脈絡，提升生成文字的品質。
- **資訊檢索：**根據輸入文字，搜尋語意最相似的文字或文件。

  [文件搜尋教學課程task](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **搜尋結果重新排序**：根據查詢對初始結果進行語意評分，優先顯示最相關的項目。

  [搜尋結果重新排序教學課程task](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **異常偵測：**比較嵌入群組有助於找出隱藏的趨勢或離群值。

  [異常偵測教學課程bubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **分類：**根據內容自動分類文字，例如情緒分析或垃圾訊息偵測

  [分類教學課程token](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **分群：**建立嵌入的叢集和視覺化圖表，有效掌握複雜關係。

  [叢集視覺化教學課程bubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## 儲存嵌入

將嵌入投入實際應用時，通常會使用**向量資料庫**，有效率地儲存、建立索引及擷取高維度嵌入。Google Cloud 提供可達成此目的的受管理資料服務，包括 [Gemini Enterprise Agent Platform 向量搜尋 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview?hl=zh-tw)、[BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=zh-tw)、[AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=zh-tw) 和 [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=zh-tw)。

下列教學課程說明如何搭配 Gemini Embedding 使用其他第三方向量資料庫。

- [ChromaDB 教學課程bolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [QDrant 教學課程bolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Weaviate 教學課程bolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Pinecone 教學課程bolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## 模型版本

### Gemini Embedding 2

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `gemini-embedding-2` |
| 儲存支援的資料類型 | **輸入功率**  文字、圖片、影片、音訊、PDF  **輸出內容**  文字嵌入 |
| token\_auto 代幣限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw) | **輸入權杖限制**  8,192  **輸出維度大小**  彈性，支援：128 - 3072，建議：768、1536、3072 |
| 123 個版本 | 如要瞭解詳情，請參閱[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#model-versions)。  - 穩定：`gemini-embedding-2` |
| calendar\_month最新更新 | 2026 年 4 月 |

### Gemini Embedding

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `gemini-embedding-001` |
| 儲存支援的資料類型 | **輸入功率**  文字  **輸出內容**  文字嵌入 |
| token\_auto 代幣限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw) | **輸入權杖限制**  2,048  **輸出維度大小**  彈性，支援：128 - 3072，建議：768、1536、3072 |
| 123 個版本 | 如要瞭解詳情，請參閱[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#model-versions)。  - 穩定：`gemini-embedding-001` |
| calendar\_month最新更新 | 2025 年 6 月 |

如要瞭解已淘汰的 Embeddings 模型，請前往「[淘汰項目](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-tw)」頁面。

## 從 gemini-embedding-001 遷移

`gemini-embedding-001` 和 `gemini-embedding-2` 之間的嵌入空間**不相容**。也就是說，您無法直接比較一個模型產生的嵌入內容與另一個模型產生的嵌入內容。如要升級至 `gemini-embedding-2`，請務必重新嵌入所有現有資料。

除了不相容之外，這兩款機型還有其他幾項顯著差異：

- **工作類型規格：**使用 `gemini-embedding-001` 時，您可以使用 `task_type` 參數指定工作類型 (例如 `SEMANTIC_SIMILARITY`、`RETRIEVAL_DOCUMENT`)。使用 `gemini-embedding-2` 時，系統不支援 `task_type` 參數。請改為在純文字工作的提示中直接加入工作指示。如要瞭解如何針對不同用途設定提示格式，請參閱「[使用 Embeddings 2 的工作類型](#task-types-embeddings-2)」。
- **嵌入匯總：** `gemini-embedding-001`為輸入清單中的每個字串產生個別的嵌入。相反地，如果直接在一個要求中提供多個輸入內容 (例如文字和圖片)，`gemini-embedding-2` 會產生單一的匯總嵌入。如要為個別輸入內容產生不同的嵌入內容，請將每個輸入內容包裝在 `Content` 物件中，或使用 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw#batch-embedding)。詳情請參閱「[嵌入式匯總](#embedding-aggregation)」。
- **正規化：**如果您使用 `output_dimensionality` 要求維度少於 3072 的嵌入，`gemini-embedding-2` 會自動正規化這些截斷的嵌入。使用 `gemini-embedding-001` 時，您需要手動將 3072 以外的維度正規化。詳情請參閱「[確保較小尺寸的品質](#quality-for-smaller-dimensions)」。

## 批次嵌入

如果延遲不是問題，請嘗試搭配 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw#batch-embedding) 使用 Gemini Embeddings 模型。這項模型可讓您以預設嵌入價格的 50% 價格，獲得高出許多的高輸送量。如需入門範例，請參閱 [Batch API 食譜](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)。

## 負責任的使用方式通知

Gemini Embedding 模型與生成新內容的生成式 AI 模型不同，只會將輸入資料的格式轉換為數字表示法。Google 負責提供嵌入模型，將輸入資料的格式轉換為要求的數字格式，但使用者仍須全權負責輸入的資料和產生的嵌入內容。使用 Gemini Embedding 模型即代表您確認自己具備必要權限，可使用上傳的一切內容。請勿生成會侵害他人智慧財產或隱私權的內容。使用這項服務時，請務必遵守《[使用限制政策](https://policies.google.com/terms/generative-ai/use-policy?hl=zh-tw)》和《[Google 服務條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw)》。

## 開始使用嵌入建構內容

請參閱[嵌入快速入門筆記本](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)，瞭解模型功能，以及如何自訂和視覺化呈現嵌入。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-09 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-09 (世界標準時間)。"],[],[]]
