---
source_url: https://ai.google.dev/gemini-api/docs/files?hl=zh-TW
fetched_at: 2026-10-26T06:04:31.871555+00:00
title: "Files API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Files API

Gemini 可同時處理多種輸入資料，包括文字、圖片和音訊。

本指南說明如何使用 Files API 處理媒體檔案。音訊檔案、圖片、影片、文件和其他支援的檔案類型，基本操作方式都相同。

如需檔案提示指南，請參閱「[檔案提示指南](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw#prompt-guide)」一節。

## 上傳檔案

您可以使用 Files API 上傳媒體檔案。如果要求總大小 (包括檔案、文字提示詞、系統指令等) 超過 100 MB，請一律使用 Files API。PDF 檔案大小上限為 50 MB。

下列程式碼會上傳檔案，然後在呼叫 `interactions.create` 時使用該檔案。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": myfile.uri, "mime_type": myfile.mime_type}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this audio clip" },
      { type: "audio", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

Content textContent = TextContent.builder().text("Describe this audio clip").build();
Content audioContent =
    AudioContent.builder()
        .uri(myFile.uri().orElse(""))
        .mimeType(AudioContentMimeType.of(myFile.mimeType().orElse("audio/mp3")))
        .build();

List<Content> contents = Arrays.asList(textContent, audioContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

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

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe this audio clip",
                }),
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(myFile.URI),
                    MimeType: interactions.AudioContentMimeType(myFile.MIMEType).ToPointer(),
                }),
            }),
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
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using the Interactions API
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## 取得檔案的中繼資料

您可以呼叫 `files.get`，確認 API 是否成功儲存上傳的檔案，並取得檔案的中繼資料。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await client.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

String fileName = myFile.name().orElse("");
File fileMetadata = client.files.get(fileName, null);
System.out.println(fileMetadata);
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    fileMetadata, err := client.Files.Get(ctx, myFile.Name, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(fileMetadata)
}
```

### REST

```
# file_info.json was created in the upload example
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
echo file_uri=$file_uri
```

## 列出上傳的檔案

下列程式碼會取得所有已上傳檔案的清單：

### Python

```
from google import genai

client = genai.Client()

print('My files:')
for f in client.files.list():
    print(' ', f.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const listResponse = await client.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;

Client client = new Client();

System.out.println("My files:");
for (File f : client.files.list(null)) {
  System.out.println("  " + f.name().orElse(""));
}
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("My files:")
    for f, err := range client.Files.All(ctx) {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(" ", f.Name)
    }
}
```

### REST

```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 刪除上傳的檔案

檔案會在 48 小時後自動刪除，您也可以手動刪除上傳的檔案：

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await client.files.delete({ name: fileName });
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File myFile =
    client.files.upload(
        new java.io.File("path/to/sample.mp3"),
        UploadFileConfig.builder().mimeType("audio/mp3").build());

client.files.delete(myFile.name().orElse(""), null);
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    myFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    if _, err := client.Files.Delete(ctx, myFile.Name, nil); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 使用資訊

您可以使用 Files API 上傳媒體檔案並與其互動。使用 Files API 時，每個專案最多可儲存 20 GB 的檔案，每個檔案的大小上限為 2 GB。檔案會保存 48 小時。

在這段期間，您可以使用 API 取得檔案的中繼資料。但無法下載使用者上傳的檔案。您可以使用 `files.download` 方法，下載模型生成的檔案，例如影片。在所有支援 Gemini API 的地區，都能免付費使用 Files API。

## 檔案提示策略

本節提供使用 Gemini API 提示搭配媒體檔案的指南和最佳做法。

提示中可使用多種資料類型，讓您能更彈性地運用 Gemini API 處理各種工作。例如，您可以向模型傳送美味餐點的相片，並要求模型撰寫關於該餐點的簡短網誌。

|  |  |
| --- | --- |
| **提示** | **回應** |
| 根據這張圖片，撰寫一篇簡短有趣的網誌文章。內容應包含相片中餐點的說明，並談談我的備餐歷程。   Cookie | 事先準備餐點不僅能節省時間和金錢，也有助於健康飲食。這道餐點不僅健康美味，而且可以提前準備，是絕佳的例子。  這道餐點包含糙米、烤蔬菜和照燒雞肉。 糙米是健康的複合碳水化合物，可提供持久能量。烤蔬菜富含每日所需的維生素和礦物質，照燒雞肉則美味可口，且含有豐富的蛋白質。  這道餐點的準備方式也很簡單。只要煮好糙米飯、烤蔬菜，以及烹調照燒雞肉，所有食材都煮熟後，分裝到備餐容器中，然後放入冰箱冷藏。這樣就能在忙碌的早晨隨時取用。  如果你想吃健康美味的餐點，又想提前準備，這道料理是絕佳選擇。這道料理營養豐富、美味可口，絕對能讓你飽足又滿意。  祝你備餐順利，吃得健康又美味！ |

如果使用媒體檔案的提示無法產生所需輸出內容，可以採取一些策略來取得所需結果。以下各節提供設計方法和疑難排解提示，協助您改善使用多模態輸入內容的提示。

如要改善多模態提示，請參考下列最佳做法：

- ### [提示設計基礎知識](#specific-instructions)

  - **提供明確的指示**：清楚簡潔地說明指示，盡量避免誤解。
  - **在提示中加入幾個範例：**使用實際的少量樣本範例，說明您想達成的目標。
  - **逐步分解**：將複雜任務分解為可管理的小目標，引導模型完成程序。
  - **指定輸出格式**：在提示中要求輸出內容採用所需格式，例如 Markdown、JSON、HTML 等。
  - **單一圖片提示詞請先放圖片**：Gemini 可以處理任何順序的圖片和文字輸入內容，但如果提示詞只包含一張圖片，將圖片 (或影片) 放在文字提示詞前面，可能會有較好的效果。不過，如果提示需要圖片和文字高度交錯才能有意義，請使用最自然的順序。
- ### [排解多模態提示詞問題](#troubleshooting)

  - **如果模型未從圖片的相關部分擷取資訊：**請在提示中加入提示，說明您希望提示從圖片的哪些部分擷取資訊。
  - **如果模型輸出內容太籠統 (未根據輸入的圖片/影片量身打造)：** 在提示詞開頭，先要求模型描述圖片或影片，再提供工作指示，或要求模型參考圖片內容。
  - **如要排解失敗的部分：**請模型描述圖片或說明推論過程，評估模型初步理解的程度。
  - **如果提示詞導致幻覺內容：**請嘗試調低溫度設定，或要求模型提供較短的說明，降低模型推斷額外細節的可能性。
  - **調整取樣參數：**嘗試不同的溫度設定和 Top-K 選項，調整模型的創意程度。

### 指令應明確具體

提示越清楚詳細，生成結果就越符合需求。如果您有特定的輸出內容，最好在提示中加入該要求，確保能取得想要的輸出內容。

如果要求模型「描述這張圖片」，模型可能會生成一般描述。如果需要模型從圖片中剖析時間和城市，可以直接在提示中加入這項要求。

| 提示詞 | 模型回應 |
| --- | --- |
| 描述這張圖片。 | 圖片：機場抵達與起飛時刻資訊看板。 |

| **更新提示** | **提升回應品質** |
| --- | --- |
| 旅遊時間表 Parse the time and city from the airport board shown in this image into a list. | - 10:50 莫斯科 - 11:05 愛丁堡 - 11:05 倫敦 - 11:10 布加勒斯特 - 基輔時間 11:30 - 11:35 都柏林 - 11:45 東密德蘭 - 12:15 Sofia - 12:30 倫敦 - 12:30 新堡 - 12:40 聖彼得堡 - 12:40 倫敦 - 12:45 曼徹斯特 |

### 新增幾個範例

Gemini 模型可接受多項輸入內容，並將其做為範例，瞭解您想要的輸出內容。加入這些範例有助於模型找出模式，並將指定圖片和回覆之間的關係套用至新範例。這也稱為「少量樣本」學習。

在下列範例中，初始輸出內容是以句子形式撰寫，且包含國家/地區 (巴西)。假設您希望輸出內容採用不同的格式或風格，且只要城市名稱，不要國家/地區名稱。在提示中加入少量樣本範例，可引導模型以您期望的方式回覆。

| **提示** | **模型回覆** |
| --- | --- |
| 旅遊時間表 判斷地標所在的城市。 | 這個地標是巴西里約熱內盧的救世基督像。 |

| **更新後的提示** | **改善回覆品質** |
| --- | --- |
| 判斷地標所在的城市。 羅馬競技場 | 城市：羅馬，地標：羅馬競技場。 |
| 紫禁城 | city: Beijing, landmark: Forbidden City |
| forbidden-city | 城市：里約熱內盧，地標：救世基督像 |

### 逐步分解

對於需要視覺理解和推論的複雜工作，建議將工作拆解成較小、較簡單的步驟。或者，您也可以直接在提示中要求模型「逐步思考」，這也是有效的方法。

| 提示詞 | 模型回應 |
| --- | --- |
| 衛生紙什麼時候會用完？ | 不久後，你只剩下 3 捲。 |

| **更新提示** | **改善回覆品質** |
| --- | --- |
| 1. 首先，請計算這張圖片中有多少捲衛生紙。 2. 接著，判斷一般人每天使用的衛生紙量。 3. 計算這些捲筒衛生紙可以使用多久。 | 1. 這張圖片中有 3 捲衛生紙。 2. 一般人每天會使用約 20 張衛生紙。 3. 如果每捲有 200 張，則每捲約可使用 10 天。因此，3 卷紙巾約可使用一個月。 |

數學問題或其他類型的文字題很適合要求模型逐步思考。

| **提示** | **回應** |
| --- | --- |
| 這個數列的第 4 項是什麼？ | -135 |

模型回覆的內容有誤。如要改善這項問題，可以要求模型先剖析問題，再回答提示。

| **提示** | **回應** |
| --- | --- |
| 請先剖析圖片中的公式。  然後根據公式回答「這個序列的第 4 個項是什麼？」。 | *按一下即可展開結果* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. 將 n = 4 代入公式： $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. 我們不知道 b(3) 的值，因此將 n = 3 代入公式： $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. 我們不知道 b(2) 的值，因此將 n = 2 代入公式： $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. 我們知道 b(1) 的值是 15，因此將其代入公式： $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. 現在我們知道 b(2) 的值，將其代入 b(3) 的公式： $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. 現在我們知道 b(3) 的值，因此可代入 b(4) 的公式： $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   因此，這個數列的第 4 項是 -405。 |

模型回覆正確。現在，為了讓回覆更精簡，您可以要求模型逐步思考。

| **更新提示** | **提升回應品質** |
| --- | --- |
| 這個數列的第 4 項為何？請逐步思考。 | 第一個詞是 15。  第二項是 b(1) \* (-3) = 15 \* (-3) = -45。  第三項是 b(2) \* (-3) = -45 \* (-3) = 135。  第四項是 b(3) \* (-3) = 135 \* (-3) = -405。 |

### 指定輸出格式

常見的問題是模型輸出內容必須採用特定格式 (例如 Markdown、JSON、HTML)，尤其是當模型輸出內容需要由下游工作擷取時。您可以指示模型在提示中以該格式輸出內容。以下是兩個例子：

| 提示詞 | 模型回應 |
| --- | --- |
| 將這張圖片中的表格剖析為 Markdown 格式 | ```none | Subject | Status | Time | Start date | Due on | | ------- | ------ | ---- | ---------- | ------ | | Math | Done | 1.5 hrs | 11/29/2023 | 12/1/2023 | | Geography | Done | 30 min | 12/2/2023 | 12/4/2023 | | Physics | In progress | 2 hrs | 12/3/2023 | 12/5/2023 | | Biology | Not started | 6 hrs | 11/2/2016 | 12/6/2023 | ``` |

| **提示** | **模型回覆** |
| --- | --- |
| 提供下列所有屬性的清單：  食材、菜餚類型、是否為素食，以 JSON 格式呈現 | ```json { "ingredients": [ "rice", "shrimp", "clams", "mussels", "peas", "tomatoes", "onions", "garlic", "olive oil", "paprika", "salt", "pepper" ], "type of cuisine": "Spanish", "vegetarian": false } ``` |

### 在單圖提示中，先提供圖片

雖然 Gemini 可以解讀提示中的圖片和文字，但將單一圖片放在文字提示詞之前，可能會得到更理想的結果。在下列範例中，您會發現每個提示中的圖片都排在文字前面。

### 排解多模態提示問題

如果回覆不符合需求，可能需要調整提示。你可以嘗試以下幾種策略。

#### 如果模型未從圖片的相關部分擷取資訊

如要取得更具體的回覆，可以指出您希望提示從圖片的哪些方面擷取資訊，以提供回覆。

| 提示詞 | 模型回應 |
| --- | --- |
| 這些尿布夠寶寶用幾天？ | 這些尿布可使用 198 天。 |

| **更新後的提示** | **提升回應品質** |
| --- | --- |
| 這些尿布可以用多久？  請根據外盒標示的重量判斷嬰兒年齡，並使用盒內尿布總數。  將總數除以孩子每天使用的尿布數量。 | 包裝盒內含 198 片尿布。包裝盒上註明尿布適合體重 22 至 37 磅的兒童。  這個體重範圍的兒童平均年齡可能介於 1 到 2 歲。  2 歲幼童通常每天會用掉 6 片尿布，因此 198 片尿布大約可用 33 天 (198/6)。 |

#### 模型輸出內容過於籠統，未針對輸入圖片調整

如要協助模型根據圖片調整回覆，請先要求模型描述圖片，再執行推論工作。

| 提示詞 | 模型回應 |
| --- | --- |
| 這些圖片有什麼共通點？ | 這四張圖片都是風景攝影範例。 |

| **更新提示** | **提升回應品質** |
| --- | --- |
| 首先，請詳細描述每張圖片的內容。這些圖片有什麼共通點？ | 第一張圖片顯示有人正在打包行李箱。第二張圖片顯示購物中心空無一人的走廊。第三張圖片顯示一捲衛生紙。第四張圖片顯示狂風暴雨中的大海。  這些圖片的共通點是，它們都是過渡空間的例子。過渡空間是指介於兩個地點或情境之間的地點或情境。通常會帶有不確定或模稜兩可的感覺。  第一張圖片顯示使用者在家和出遊時的狀態。第二張圖片顯示兩間商店之間的走廊。第三張圖片是衛生紙，代表浴室。浴室是私人和公共領域之間的過渡空間。我們在這裡準備進入或離開外部世界。  第四張圖片顯示海面介於平靜和暴風雨之間。  過渡空間既令人興奮，又令人不安。可以是新的開始，也可以是結束。可以是反思或行動的場所。 |

您也可以嘗試明確要求模型參考圖片中的內容。

| **更新提示** | **改善回覆品質** |
| --- | --- |
| 這些圖片有什麼共通點？在回覆中提及圖片內容。 | 所有圖片都與旅遊相關。第一張圖片顯示有人正在打包行李箱，第二張圖片顯示購物中心空蕩蕩的走廊，第三張圖片顯示一疊衛生紙，第四張圖片顯示黑暗且波濤洶湧的海面。  這些圖片都與旅遊相關，因為都是人們在旅遊時需要或使用的物品。第一張圖片顯示有人在打包行李箱，這是人們旅行時會做的事。第二張圖片顯示購物中心空蕩蕩的走廊，這是人們經常前往購買旅行用品的地方。第三張圖片顯示一疊衛生紙，這是人們旅行時經常使用的物品。第四張圖片顯示狂風暴雨的海面，這是人們旅行時經常會遇到的情況。 |

同樣的訣竅也適用於圖片的創意輸出內容。在以下兔子範例中，明確要求模型納入圖片中的元素，可以提升輸出結果。

| 提示詞 | 模型回應 |
| --- | --- |
| 可以根據這張圖片寫一首詩嗎？ | 小兔兔，柔軟又棕色，  在田野中跳躍，上上下下。  長長的耳朵，小小的尾巴，  你是最可愛的生物。  你啃著青草，又綠又甜，  一看到我就蹦蹦跳跳地跑開。  但我永遠是你的朋友，  小兔子，直到最後。 |

| **更新提示** | **改善回覆品質** |
| --- | --- |
| 請根據這張圖片撰寫一首描述性強烈且充滿戲劇性的詩，並加入地點。 | 綠地上的小兔，  耳朵又長又尖。  你看到什麼？  在遠處，你凝視的地方？  是海洋的藍色，  在陽光下閃閃發光？  還是海浪拍打的轟隆聲，  你最愛的節奏？  小兔兒，請告訴我，  是什麼吸引了你？  是鹹鹹的海風，  還是海鷗的叫聲？  或許是萬物浩瀚，  世界如此廣大，卻又如此渺小。  夢想在此自由翱翔，  冒險種子在此播撒。  小兔，我好奇你夢見了什麼，  你坐在草地上，如此寧靜。  你渴望探索深海，  還是想留在陸地，盡情跳躍？  無論如何，小兔子，  請讓好奇心持續閃耀。  在你的夢想和抱負中，  蘊藏著等待你創造的世界。 |

#### 疑難排解提示詞失敗的部分

如果提示失敗，很難判斷是因為模型一開始就**不理解圖片**，還是理解圖片但後續未執行正確的**推論步驟**。如要釐清原因，請要求模型描述圖像內容。

在以下範例中，如果模型回覆的點心與茶搭配起來很奇怪 (例如爆米花)，您可以先進行疑難排解，判斷模型是否正確辨識出圖片中含有茶。

| 提示詞 | 疑難排解提示 |
| --- | --- |
| 有什麼 1 分鐘內就能做好的點心，可以搭配這道料理？ | 描述這張圖片的內容。 |

另一種策略是要求模型說明推論過程。這有助於縮小範圍，找出推理過程中的問題 (如有)。

| 提示詞 | 疑難排解提示 |
| --- | --- |
| 有什麼點心可以在 1 分鐘內做好，而且適合搭配這道料理？ | 有什麼點心可以在 1 分鐘內做好，而且適合搭配這道菜？請說明原因。 |

## 後續步驟

- 使用 [Google AI Studio](http://aistudio.google.com?hl=zh-tw) 撰寫自己的多模態提示。
- 如要瞭解如何使用 Gemini Files API 上傳媒體檔案並加入提示，請參閱「[Vision](https://ai.google.dev/gemini-api/docs/vision?hl=zh-tw)」、「[音訊](https://ai.google.dev/gemini-api/docs/audio?hl=zh-tw)」和「[文件處理](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw)」指南。
- 如需更多提示設計指南 (例如調整取樣參數)，請參閱「[提示策略](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw)」頁面。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-14 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-14 (世界標準時間)。"],[],[]]
