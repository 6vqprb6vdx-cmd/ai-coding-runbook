---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=ar
fetched_at: 2026-10-05T06:28:22.707351+00:00
title: "\u0627\u0644\u0628\u062d\u062b \u0639\u0646 \u0645\u0644\u0641 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البحث عن ملف

تتيح Gemini API ميزة "التوليد المعزّز بالاسترجاع" من خلال أداة "البحث في الملفات". تستورد ميزة "البحث في الملفات" بياناتك وتقسّمها وتفهرسها
لإتاحة استرجاع المعلومات ذات الصلة بسرعة استنادًا إلى طلب مقدَّم. يتم بعد ذلك استخدام هذه المعلومات المسترجَعة كسياق للنموذج، ما يتيح له تقديم إجابات أكثر دقة وملاءمةً. تتوفّر أيضًا إمكانات البحث المتعدد الوسائط في &quot;بحث الملفات&quot;، وذلك من خلال تضمين النصوص باستخدام `gemini-embedding-001`، وتضمين الصور والوسائط المتعددة باستخدام `gemini-embedding-2`.

تكون عملية تخزين الملفات وإنشاء عمليات التضمين مجانية عند وقت طلب البحث، ولن تدفع إلا مقابل إنشاء عمليات التضمين عند فهرسة ملفاتك لأول مرة، بالإضافة إلى التكلفة العادية لرموز الإدخال والإخراج في نموذج Gemini. يساهم نموذج الفوترة الجديد هذا في تسهيل عملية إنشاء &quot;أداة البحث عن الملفات&quot; وتوسيع نطاقها، كما يقلّل من تكلفتها. راجِع قسم [الأسعار](#pricing) لمعرفة التفاصيل.

## التحميل مباشرةً إلى "متجر البحث عن الملفات"

يوضّح المثال التالي كيفية تحميل ملف مباشرةً إلى
[مخزن البحث عن الملفات](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-media.uploadtofilesearchstore):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.upload_to_file_search_store(
  file='sample.txt',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'display-file-name',
  }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "file_citation":
                            print(f"  - {annotation.file_name}: {annotation.source}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.uploadToFileSearchStore({
    file: 'file.txt',
    fileSearchStoreName: fileSearchStore.name,
    config: {
      displayName: 'file-name',
    }
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation });
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'file_citation') {
                console.log(`  - ${annotation.file_name}: ${annotation.source}`);
              }
            }
          }
        }
      }
    }
  }
}

run();
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileCitation;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.types.FileSearchStore;
import com.google.genai.types.UploadToFileSearchStoreConfig;
import com.google.genai.types.UploadToFileSearchStoreOperation;
import java.util.Arrays;

Client client = new Client();

FileSearchStore fileSearchStore =
    client.fileSearchStores.create(
        CreateFileSearchStoreConfig.builder()
            .displayName("your-fileSearchStore-name")
            .embeddingModel("models/gemini-embedding-2")
            .build());

UploadToFileSearchStoreOperation operation =
    client.fileSearchStores.uploadToFileSearchStore(
        fileSearchStore.name().get(),
        "sample.txt",
        UploadToFileSearchStoreConfig.builder().displayName("display-file-name").build());

while (!operation.done().orElse(false)) {
  Thread.sleep(5000);
  operation = client.operations.get(operation, null);
}

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList(fileSearchStore.name().get()))
                    .build()))
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
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof FileCitation) {
                  FileCitation citation = (FileCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n",
                      citation.fileName().orElse(""), citation.source().orElse(""));
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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    fileSearchStore, err := client.FileSearchStores.Create(ctx, &genai.CreateFileSearchStoreConfig{
        DisplayName:    "your-fileSearchStore-name",
        EmbeddingModel: "models/gemini-embedding-2",
    })
    if err != nil {
        log.Fatal(err)
    }

    operation, err := client.FileSearchStores.UploadToFileSearchStoreFromPath(
        ctx,
        "sample.txt",
        fileSearchStore.Name,
        &genai.UploadToFileSearchStoreConfig{
            DisplayName: "display-file-name",
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    for !operation.Done {
        time.Sleep(5 * time.Second)
        operation, err = client.Operations.GetUploadToFileSearchStoreOperation(ctx, operation, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{fileSearchStore.Name},
                    }),
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
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.FileCitation != nil {
                                c := annotation.FileCitation
                                fileName := ""
                                if c.FileName != nil {
                                    fileName = *c.FileName
                                }
                                source := ""
                                if c.Source != nil {
                                    source = *c.Source
                                }
                                fmt.Printf("  - %s: %s\n", fileName, source)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# 1. Create a File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "displayName": "your-file-search-store-name",
      "embeddingModel": "models/gemini-embedding-2"
    }' > store_res.json

FILE_SEARCH_STORE_NAME=$(jq -r ".name" store_res.json)

# 2. Upload directly to File Search store using resumable upload
NUM_BYTES=$(wc -c < "sample.txt")
curl "https://generativelanguage.googleapis.com/upload/v1beta/fileSearchStores/$FILE_SEARCH_STORE_NAME:uploadToFileSearchStore?key=$GEMINI_API_KEY" \
    -D upload-header.tmp \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Header-Content-Type: text/plain" \
    -H "Content-Type: application/json" \
    -d '{"displayName": "sample.txt"}' 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " upload-header.tmp | cut -d" " -f2 | tr -d "\r")
rm upload-header.tmp

curl "${upload_url}" \
    -H "Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@sample.txt" 2> /dev/null > upload_response.json

cat upload_response.json

# 3. Query using the File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "gemini-3.8-flash",
      "input": "Can you tell me about [insert question]",
      "tools": [{
        "type": "file_search",
        "file_search_store_names": ["'"$FILE_SEARCH_STORE_NAME"'"]
      }]
    }'
```

راجِع مرجع واجهة برمجة التطبيقات [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-media.uploadtofilesearchstore) للحصول على مزيد من المعلومات.

## استيراد الملفات

بدلاً من ذلك، يمكنك تحميل ملف حالي و[استيراده إلى متجر البحث عن الملفات](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-filesearchstores.importfile) باتّباع الخطوات التالية:

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

sample_file = client.files.upload(file='sample.txt', config={'display_name': 'display_file_name'})

file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { displayName: 'file-name' }
  });

  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.importFile({
    fileSearchStoreName: fileSearchStore.name,
    fileName: sampleFile.name
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation: operation });
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
        }
      }
    }
  }
}

run();
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.types.File;
import com.google.genai.types.FileSearchStore;
import com.google.genai.types.ImportFileOperation;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;

Client client = new Client();

File sampleFile =
    client.files.upload(
        "sample.txt", UploadFileConfig.builder().displayName("display_file_name").build());

FileSearchStore fileSearchStore =
    client.fileSearchStores.create(
        CreateFileSearchStoreConfig.builder()
            .displayName("your-fileSearchStore-name")
            .embeddingModel("models/gemini-embedding-2")
            .build());

ImportFileOperation operation =
    client.fileSearchStores.importFile(
        fileSearchStore.name().get(), sampleFile.name().get(), null);

while (!operation.done().orElse(false)) {
  Thread.sleep(5000);
  operation = client.operations.get(operation, null);
}

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList(fileSearchStore.name().get()))
                    .build()))
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
            System.out.println(textContent.text().orElse(""));
          }
        }
      }
    }
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
    "time"

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

    sampleFile, err := client.Files.UploadFromPath(ctx, "sample.txt", &genai.UploadFileConfig{
        DisplayName: "display_file_name",
    })
    if err != nil {
        log.Fatal(err)
    }

    fileSearchStore, err := client.FileSearchStores.Create(ctx, &genai.CreateFileSearchStoreConfig{
        DisplayName:    "your-fileSearchStore-name",
        EmbeddingModel: "models/gemini-embedding-2",
    })
    if err != nil {
        log.Fatal(err)
    }

    operation, err := client.FileSearchStores.ImportFile(ctx, fileSearchStore.Name, sampleFile.Name, nil)
    if err != nil {
        log.Fatal(err)
    }

    for !operation.Done {
        time.Sleep(5 * time.Second)
        operation, err = client.Operations.GetImportFileOperation(ctx, operation, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{fileSearchStore.Name},
                    }),
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
                    fmt.Println(content.TextContent.Text)
                }
            }
        }
    }
}
```

### REST

```
# 1. Upload file using the Files API
NUM_BYTES=$(wc -c < "sample.txt")
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=$GEMINI_API_KEY" \
    -D upload-header.tmp \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Header-Content-Type: text/plain" \
    -H "Content-Type: application/json" \
    -d '{"file": {"displayName": "sample.txt"}}' 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " upload-header.tmp | cut -d" " -f2 | tr -d "\r")
rm upload-header.tmp

curl "${upload_url}" \
    -H "Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@sample.txt" 2> /dev/null > file_info.json

FILE_NAME=$(jq -r ".file.name" file_info.json)

# 2. Create a File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "displayName": "your-file-search-store-name",
      "embeddingModel": "models/gemini-embedding-2"
    }' > store_res.json

FILE_SEARCH_STORE_NAME=$(jq -r ".name" store_res.json)

# 3. Import the file into the File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/$FILE_SEARCH_STORE_NAME:importFile?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"fileName": "'"$FILE_NAME"'"}'

# 4. Query using the File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "gemini-3.8-flash",
      "input": "Can you tell me about [insert question]",
      "tools": [{
        "type": "file_search",
        "file_search_store_names": ["'"$FILE_SEARCH_STORE_NAME"'"]
      }]
    }'
```

راجِع مرجع واجهة برمجة التطبيقات [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#method:-filesearchstores.importfile) للحصول على مزيد من المعلومات.

## إعدادات التقسيم

عند استيراد ملف إلى مستودع &quot;البحث عن الملفات&quot;، يتم تقسيمه تلقائيًا إلى أجزاء صغيرة، وتضمينه، وفهرسته، وتحميله إلى مستودع &quot;البحث عن الملفات&quot;. إذا كنت بحاجة إلى المزيد من التحكّم في استراتيجية التقسيم، يمكنك تحديد إعداد [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=ar#request-body_5) لضبط الحد الأقصى لعدد الرموز المميزة لكل جزء والحد الأقصى لعدد الرموز المميزة المتداخلة.

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file='sample.txt',
    config={
        'chunking_config': {
          'white_space_config': {
            'max_tokens_per_chunk': 200,
            'max_overlap_tokens': 20
          }
        }
    }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

print("Custom chunking complete.")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

let operation = await ai.fileSearchStores.uploadToFileSearchStore({
  file: 'file.txt',
  fileSearchStoreName: fileSearchStore.name,
  config: {
    displayName: 'file-name',
    chunkingConfig: {
      whiteSpaceConfig: {
        maxTokensPerChunk: 200,
        maxOverlapTokens: 20
      }
    }
  }
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 5000));
  operation = await ai.operations.get({ operation });
}
console.log("Custom chunking complete.");
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.types.ChunkingConfig;
import com.google.genai.types.UploadToFileSearchStoreConfig;
import com.google.genai.types.UploadToFileSearchStoreOperation;
import com.google.genai.types.WhiteSpaceConfig;

Client client = new Client();

UploadToFileSearchStoreOperation operation =
    client.fileSearchStores.uploadToFileSearchStore(
        "fileSearchStores/my-file-search-store",
        "sample.txt",
        UploadToFileSearchStoreConfig.builder()
            .displayName("file-name")
            .chunkingConfig(
                ChunkingConfig.builder()
                    .whiteSpaceConfig(
                        WhiteSpaceConfig.builder()
                            .maxTokensPerChunk(200)
                            .maxOverlapTokens(20)
                            .build())
                    .build())
            .build());

while (!operation.done().orElse(false)) {
  Thread.sleep(5000);
  operation = client.operations.get(operation, null);
}

System.out.println("Custom chunking complete.");
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    operation, err := client.FileSearchStores.UploadToFileSearchStoreFromPath(
        ctx,
        "sample.txt",
        "fileSearchStores/my-file-search-store",
        &genai.UploadToFileSearchStoreConfig{
            DisplayName: "file-name",
            ChunkingConfig: &genai.ChunkingConfig{
                WhiteSpaceConfig: &genai.WhiteSpaceConfig{
                    MaxTokensPerChunk: genai.Ptr(int32(200)),
                    MaxOverlapTokens:  genai.Ptr(int32(20)),
                },
            },
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    for !operation.Done {
        time.Sleep(5 * time.Second)
        operation, err = client.Operations.GetUploadToFileSearchStoreOperation(ctx, operation, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    fmt.Println("Custom chunking complete.")
}
```

### REST

```
NUM_BYTES=$(wc -c < "sample.txt")
curl "https://generativelanguage.googleapis.com/upload/v1beta/fileSearchStores/$FILE_SEARCH_STORE_NAME:uploadToFileSearchStore?key=$GEMINI_API_KEY" \
    -D upload-header.tmp \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Header-Content-Type: text/plain" \
    -H "Content-Type: application/json" \
    -d '{
      "displayName": "sample.txt",
      "chunkingConfig": {
        "whiteSpaceConfig": {
          "maxTokensPerChunk": 200,
          "maxOverlapTokens": 20
        }
      }
    }' 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " upload-header.tmp | cut -d" " -f2 | tr -d "\r")
rm upload-header.tmp

curl "${upload_url}" \
    -H "Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@sample.txt" 2> /dev/null > upload_response.json

cat upload_response.json
```

لاستخدام متجر "بحث الملفات"، مرِّره كأداة إلى طريقة `interactions.create`، كما هو موضّح في المثالَين [تحميل](#upload) و[استيراد](#importing-files).

## آلية العمل

تستخدم ميزة "البحث عن الملفات" أسلوبًا يُعرف باسم البحث الدلالي للعثور على معلومات ذات صلة بطلب المستخدم. على عكس البحث العادي المستند إلى الكلمات الرئيسية، يفهم البحث الدلالي المعنى والسياق الخاصين بطلب البحث.

عند استيراد ملف، يتم تحويله إلى تمثيلات رقمية تُعرف باسم
[التضمينات](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar)، والتي تسجّل المعنى الدلالي للمحتوى الذي تم تحميله. يتم تخزين هذه التضمينات في قاعدة بيانات متخصّصة في "البحث عن الملفات".
عندما تُجري طلب بحث، يتم أيضًا تحويله إلى تضمين. بعد ذلك، يجري النظام عملية &quot;البحث في الملفات&quot; للعثور على أجزاء المستندات الأكثر تشابهًا وملاءمةً من مستودع &quot;البحث في الملفات&quot;.

لا تتوفّر مدة بقاء (TTL) للتضمينات، بل تبقى متاحة إلى أن يتم حذفها يدويًا أو عند إيقاف النموذج نهائيًا. أما الملفات، فيتم حذفها بعد 48 ساعة.

في ما يلي تفصيل لعملية استخدام واجهة برمجة التطبيقات File Search
`uploadToFileSearchStore`:

1. **إنشاء مستودع بحث في الملفات**: يحتوي مستودع بحث في الملفات على البيانات المعالَجة من ملفاتك. وهي الحاوية الدائمة لعمليات التضمين التي سيتم إجراء البحث الدلالي عليها.
2. **تحميل ملف واستيراده إلى مستودع "البحث في الملفات"**: يمكنك تحميل ملف واستيراد النتائج إلى مستودع "البحث في الملفات" في الوقت نفسه. يؤدي ذلك إلى إنشاء كائن `File` مؤقت، وهو مرجع إلى المستند الأولي. بعد ذلك، يتم تقسيم هذه البيانات إلى أجزاء، وتحويلها إلى تضمينات &quot;بحث الملفات&quot;، وفهرستها. يتم حذف عنصر `File` بعد 48 ساعة، بينما يتم تخزين البيانات التي تم استيرادها إلى مساحة تخزين &quot;البحث عن الملفات&quot; إلى أجل غير مسمى إلى أن تختار حذفها.
3. **طلب البحث باستخدام "البحث عن ملف"**: أخيرًا، يمكنك استخدام أداة `FileSearch` في مكالمة `generateContent`. في إعدادات الأداة، عليك تحديد `FileSearchRetrievalResource`، يشير إلى `FileSearchStore` الذي تريد البحث فيه. يطلب هذا الإجراء من النموذج إجراء بحث دلالي في مخزن &quot;بحث الملفات&quot; المحدّد للعثور على المعلومات ذات الصلة التي يمكنه الاستناد إليها في رده.

![عملية الفهرسة وطلب البحث في &quot;بحث الملفات&quot;](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=ar)

عملية الفهرسة والاستعلام في &quot;بحث الملفات&quot;

في هذا المخطط، يمثّل الخط المتقطّع من *المستندات* إلى *نموذج التضمين*
(باستخدام [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=ar))
واجهة برمجة التطبيقات `uploadToFileSearchStore` (مع تجاوز *تخزين الملفات*).
في حال عدم توفّر ذلك، يؤدي استخدام [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar) لإنشاء الملفات بشكل منفصل ثم استيرادها إلى نقل عملية الفهرسة من *المستندات* إلى *مساحة تخزين الملفات* ثم إلى *نموذج التضمين*.

## متاجر "بحث الملفات"

مستودع "البحث عن الملفات" هو حاوية لتضمينات المستندات. في حين يتم حذف الملفات الأولية التي تم تحميلها من خلال File API بعد 48 ساعة، يتم تخزين البيانات التي تم استيرادها إلى متجر "بحث الملفات" إلى أجل غير مسمى إلى أن تحذفها يدويًا. يمكنك إنشاء عدة مستودعات بحث في الملفات لتنظيم مستنداتك. تتيح لك واجهة برمجة التطبيقات
`FileSearchStore` إنشاء قوائم وعرضها والحصول عليها وحذفها لإدارة
متاجر البحث عن الملفات. يتم تحديد نطاق أسماء متاجر "البحث عن الملفات" على مستوى العالم.

في ما يلي بعض الأمثلة على كيفية إدارة متاجر "بحث الملفات":

### Python

```
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'myfilesearchstore123',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

for store in client.file_search_stores.list():
    print(store)

my_file_search_store = client.file_search_stores.get(name=file_search_store.name)

client.file_search_stores.delete(name=file_search_store.name, config={'force': True})
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: 'myfilesearchstore123',
    embeddingModel: 'models/gemini-embedding-2'
  }
});

const fileSearchStores = await ai.fileSearchStores.list();
for await (const store of fileSearchStores) {
  console.log(store);
}

const myFileSearchStore = await ai.fileSearchStores.get({
  name: fileSearchStore.name
});

await ai.fileSearchStores.delete({
  name: fileSearchStore.name,
  config: { force: true }
});
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.types.DeleteFileSearchStoreConfig;
import com.google.genai.types.FileSearchStore;

Client client = new Client();

FileSearchStore fileSearchStore =
    client.fileSearchStores.create(
        CreateFileSearchStoreConfig.builder()
            .displayName("myfilesearchstore123")
            .embeddingModel("models/gemini-embedding-2")
            .build());

for (FileSearchStore store : client.fileSearchStores.list(null)) {
  System.out.println(store);
}

FileSearchStore myFileSearchStore =
    client.fileSearchStores.get(fileSearchStore.name().get(), null);

client.fileSearchStores.delete(
    fileSearchStore.name().get(), DeleteFileSearchStoreConfig.builder().force(true).build());
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

    fileSearchStore, err := client.FileSearchStores.Create(ctx, &genai.CreateFileSearchStoreConfig{
        DisplayName:    "myfilesearchstore123",
        EmbeddingModel: "models/gemini-embedding-2",
    })
    if err != nil {
        log.Fatal(err)
    }

    for store, err := range client.FileSearchStores.All(ctx) {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(store)
    }

    myFileSearchStore, err := client.FileSearchStores.Get(ctx, fileSearchStore.Name, nil)
    if err != nil {
        log.Fatal(err)
    }
    _ = myFileSearchStore

    err = client.FileSearchStores.Delete(ctx, fileSearchStore.Name, &genai.DeleteFileSearchStoreConfig{
        Force: genai.Ptr(true),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=${GEMINI_API_KEY}"
```

## مستندات "البحث في الملفات"

يمكنك إدارة المستندات الفردية في مخازن الملفات باستخدام واجهة برمجة التطبيقات
[File Search Documents](https://ai.google.dev/api/file-search/documents?hl=ar) من أجل `list` كل مستند
في مخزن بحث الملفات، و`get` معلومات حول مستند، و`delete` مستند
حسب الاسم.

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/myfilesearchstore123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/myfilesearchstore123/documents/sampletxt123')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/myfilesearchstore123/documents/sampletxt123', config={'force': True})
```

### JavaScript

```
const documents = await ai.fileSearchStores.documents.list({
  parent: 'fileSearchStores/myfilesearchstore123'
});
for await (const doc of documents) {
  console.log(doc);
}

const fileSearchDocument = await ai.fileSearchStores.documents.get({
  name: 'fileSearchStores/myfilesearchstore123/documents/sampletxt123'
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/myfilesearchstore123/documents/sampletxt123',
  config: { force: true }
});
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.types.DeleteDocumentConfig;
import com.google.genai.types.Document;

Client client = new Client();

for (Document documentInStore :
    client.fileSearchStores.documents.list("fileSearchStores/myfilesearchstore123", null)) {
  System.out.println(documentInStore);
}

Document fileSearchDocument =
    client.fileSearchStores.documents.get(
        "fileSearchStores/myfilesearchstore123/documents/sampletxt123", null);
System.out.println(fileSearchDocument);

client.fileSearchStores.documents.delete(
    "fileSearchStores/myfilesearchstore123/documents/sampletxt123",
    DeleteDocumentConfig.builder().force(true).build());
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

    for documentInStore, err := range client.FileSearchStores.Documents.All(ctx, "fileSearchStores/myfilesearchstore123") {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(documentInStore)
    }

    fileSearchDocument, err := client.FileSearchStores.Documents.Get(ctx, "fileSearchStores/myfilesearchstore123/documents/sampletxt123", nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(fileSearchDocument)

    err = client.FileSearchStores.Documents.Delete(ctx, "fileSearchStores/myfilesearchstore123/documents/sampletxt123", &genai.DeleteDocumentConfig{
        Force: genai.Ptr(true),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=${GEMINI_API_KEY}&force=true"
```

## البيانات الوصفية للملف

يمكنك إضافة بيانات وصفية مخصّصة إلى ملفاتك للمساعدة في فلترتها أو تقديم سياق إضافي. بيانات التعريف هي مجموعة من أزواج المفاتيح والقيم.

### Python

```
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    config={
        'custom_metadata': [
            {"key": "author", "string_value": "Robert Graves"},
            {"key": "year", "numeric_value": 1934}
        ]
    }
)
```

### JavaScript

```
let operation = await ai.fileSearchStores.importFile({
  fileSearchStoreName: fileSearchStore.name,
  fileName: sampleFile.name,
  config: {
    customMetadata: [
      { key: "author", stringValue: "Robert Graves" },
      { key: "year", numericValue: 1934 }
    ]
  }
});
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.types.CustomMetadata;
import com.google.genai.types.ImportFileConfig;
import com.google.genai.types.ImportFileOperation;
import java.util.Arrays;

Client client = new Client();

ImportFileOperation op =
    client.fileSearchStores.importFile(
        "fileSearchStores/myfilesearchstore123",
        "files/samplefile123",
        ImportFileConfig.builder()
            .customMetadata(
                Arrays.asList(
                    CustomMetadata.builder().key("author").stringValue("Robert Graves").build(),
                    CustomMetadata.builder().key("year").numericValue(1934f).build()))
            .build());
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

    op, err := client.FileSearchStores.ImportFile(
        ctx,
        "fileSearchStores/myfilesearchstore123",
        "files/samplefile123",
        &genai.ImportFileConfig{
            CustomMetadata: []*genai.CustomMetadata{
                {Key: "author", StringValue: "Robert Graves"},
                {Key: "year", NumericValue: genai.Ptr(float32(1934))},
            },
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    _ = op
}
```

يكون ذلك مفيدًا عندما يكون لديك مستندات متعددة في متجر &quot;بحث الملفات&quot; وتريد البحث في مجموعة فرعية منها فقط.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me about the book 'I, Claudius'",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name],
        "metadata_filter": 'author="Robert Graves"',
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me about the book 'I, Claudius'",
  tools: [{
    type: "file_search",
    file_search_store_names: [fileSearchStore.name],
    metadata_filter: 'author="Robert Graves"',
  }]
});

for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
      }
    }
  }
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me about the book 'I, Claudius'"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .metadataFilter("author=\"Robert Graves\"")
                    .build()))
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
            System.out.println(textContent.text().orElse(""));
          }
        }
      }
    }
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
                Input: interactions.NewInteractionsInput("Tell me about the book 'I, Claudius'"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                        MetadataFilter:       genai.Ptr(`author="Robert Graves"`),
                    }),
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
                    fmt.Println(content.TextContent.Text)
                }
            }
        }
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
            "model": "gemini-3.8-flash",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

يمكنك الاطّلاع على إرشادات حول تنفيذ بنية فلتر القائمة الخاصة بـ `metadata_filter` على الرابط [google.aip.dev/160](https://google.aip.dev/160).

## البحث المتعدد الوسائط في الملفات

تتيح لك ميزة "البحث المتعدد الوسائط في الملفات" تضمين الصور والبحث فيها بشكلٍ مدمج، ما يتيح إنشاء تطبيقات غنية ومتعددة الوسائط تستخدم التوليد المعزّز بالاسترجاع (RAG).

### ضبط نموذج التضمين

عند إنشاء `FileSearchStore`، عليك تجاهل نموذج التضمين التلقائي النصي فقط واستخدام نموذج متعدد الوسائط. استخدِم `models/gemini-embedding-2` لمعالجة كل من النص والصور.

### Python

```
store = client.file_search_stores.create(
    config={
        "display_name": "Multimodal Catalog",
        "embedding_model": "models/gemini-embedding-2",
    }
)
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: "Multimodal Catalog",
    embeddingModel: "models/gemini-embedding-2",
  },
});
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.types.FileSearchStore;

Client client = new Client();

FileSearchStore store =
    client.fileSearchStores.create(
        CreateFileSearchStoreConfig.builder()
            .displayName("Multimodal Catalog")
            .embeddingModel("models/gemini-embedding-2")
            .build());
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

    store, err := client.FileSearchStores.Create(ctx, &genai.CreateFileSearchStoreConfig{
        DisplayName:    "Multimodal Catalog",
        EmbeddingModel: "models/gemini-embedding-2",
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = store
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "display_name": "Multimodal Catalog",
      "embedding_model": "models/gemini-embedding-2"
    }'
```

### تحميل صور

بعد إنشاء المتجر باستخدام نموذج التضمين المتعدّد الوسائط، يمكنك تحميل ملفات الصور مباشرةً باستخدام واجهات برمجة التطبيقات نفسها الخاصة بالتحميل والموضّحة في [التحميل مباشرةً إلى متجر "بحث الملفات"](#upload) أو [استيراد الملفات](#importing-files).

**متطلبات ملف الصورة:**

- يجب ألا تزيد دقة ملفات الصور عن 4K x 4K بكسل.
- التنسيقات المتوافقة هي PNG وJPEG.

## الاقتباسات

عند استخدام "البحث في الملفات"، قد يتضمّن ردّ النموذج اقتباسات تحدّد الأجزاء التي تم استخدامها من المستندات التي حمّلتها لإنشاء الإجابة. ويساعد ذلك في التحقّق من صحة المعلومات.

يمكنك الوصول إلى معلومات الاقتباس من خلال السمة `annotations` داخل مربّعات `content` في خطوة `model_output` من الردّ.

### Python

```
for step in interaction.steps:
    if step.type == 'model_output':
        for content in step.content:
            if content.type == 'text' and content.annotations:
                print(content.annotations)
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text' && contentBlock.annotations) {
        console.log(JSON.stringify(contentBlock.annotations, null, 2));
      }
    }
  }
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content content : outputStep.content().get()) {
          if (content instanceof TextContent) {
            TextContent textContent = (TextContent) content;
            if (textContent.annotations().isPresent()) {
              System.out.println(textContent.annotations().get());
            }
          }
        }
      }
    }
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
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
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
                if content.TextContent != nil && len(content.TextContent.Annotations) > 0 {
                    fmt.Println(content.TextContent.Annotations)
                }
            }
        }
    }
}
```

### REST

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "...",
          "annotations": [
            {
              "type": "file_citation",
              "file_name": "sample.txt",
              "source": "..."
            }
          ]
        }
      ]
    }
  ]
}
```

للحصول على معلومات تفصيلية حول بنية الاقتباسات، يُرجى الاطّلاع على
[مرجع واجهة برمجة التطبيقات للتفاعلات](https://ai.google.dev/api/interactions-api?hl=ar#Resource:FileCitation).

### أرقام الصفحات

عند استخدام ميزة "البحث في الملفات" مع المستندات التي تتضمّن صفحات (مثل ملفات PDF)، قد يتضمّن ردّ النموذج رقم الصفحة التي تم العثور على المعلومات فيها.
يمكنك الوصول إلى هذه المعلومات من خلال السمة `page_number` الخاصة بالتعليق التوضيحي `file_citation`.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.page_number:
                        print(f"Cited Page: {annotation.page_number}")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.pageNumber) {
            console.log(`Cited Page: ${annotation.pageNumber}`);
          }
        }
      }
    }
  }
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileCitation;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content content : outputStep.content().get()) {
          if (content instanceof TextContent) {
            TextContent textContent = (TextContent) content;
            if (textContent.annotations().isPresent()) {
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof FileCitation) {
                  FileCitation citation = (FileCitation) annotation;
                  if (citation.pageNumber().isPresent()) {
                    System.out.println("Cited Page: " + citation.pageNumber().get());
                  }
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
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
                    for _, annotation := range content.TextContent.Annotations {
                        if annotation.FileCitation != nil && annotation.FileCitation.PageNumber != nil {
                            fmt.Println("Cited Page:", *annotation.FileCitation.PageNumber)
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "...",
          "annotations": [
            {
              "type": "file_citation",
              "file_name": "document.pdf",
              "page_number": 1,
              "source": "..."
            }
          ]
        }
      ]
    }
  ]
}
```

### اقتباسات من الوسائط

عندما يشير النموذج إلى جزء من صورة أثناء عملية الإنشاء، تعرض واجهة برمجة التطبيقات تعليقًا توضيحيًا من النوع `file_citation` في التعليقات التوضيحية يتضمّن `media_id`. يمكنك استخدام هذا المعرّف لتنزيل جزء الصورة الذي أشار إليه النموذج. يكون هذا `media_id` ثابتًا في طلبات البحث المتعددة، ما يتيح لك استرداد الصورة نفسها أو تخزينها مؤقتًا باستخدام المعرّف بشكل موثوق.

المقتطف التالي هو مثال على خطوة استجابة REST:

```
{
  "type": "model_output",
  "content": [
    {
      "type": "text",
      "text": "...",
      "annotations": [
        {
          "type": "file_citation",
          "file_name": "product_image",
          "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
        }
      ]
    }
  ]
}
```

توضّح مقتطفات الرمز البرمجي التالية كيفية استرداد `media_id` وتنزيل الوسائط:

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.media_id:
                        print(f"Cited Media ID: {annotation.media_id}")
                        blob_content = client.file_search_stores.download_media(
                            media_id=annotation.media_id
                        )
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.mediaId) {
            console.log(`Cited Media ID: ${annotation.mediaId}`);
            const blobContent = await ai.fileSearchStores.downloadMedia(annotation.mediaId);
          }
        }
      }
    }
  }
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileCitation;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content content : outputStep.content().get()) {
          if (content instanceof TextContent) {
            TextContent textContent = (TextContent) content;
            if (textContent.annotations().isPresent()) {
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof FileCitation) {
                  FileCitation citation = (FileCitation) annotation;
                  if (citation.mediaId().isPresent()) {
                    System.out.println("Cited Media ID: " + citation.mediaId().get());
                    byte[] blobContent =
                        client.fileSearchStores.downloadMedia(citation.mediaId().get(), null);
                  }
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
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
                    for _, annotation := range content.TextContent.Annotations {
                        if annotation.FileCitation != nil && annotation.FileCitation.MediaID != nil {
                            fmt.Println("Cited Media ID:", *annotation.FileCitation.MediaID)
                            blobContent, err := client.FileSearchStores.DownloadMedia(ctx, *annotation.FileCitation.MediaID, nil)
                            if err != nil {
                                log.Fatal(err)
                            }
                            _ = blobContent
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## البيانات الوصفية المخصّصة

إذا أضفت بيانات وصفية مخصّصة إلى ملفاتك، يمكنك الوصول إليها في التعليقات التوضيحية الخاصة برد النموذج. ويكون ذلك مفيدًا في تمرير سياق إضافي (مثل عناوين URL أو أرقام الصفحات أو المؤلّفين) من المستندات المصدر إلى منطق التطبيق. يحتوي كل تعليق توضيحي للاقتباس من النوع `file_citation` على هذه البيانات الوصفية المخصّصة.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.annotations:
                for annotation in content_block.annotations:
                    print(annotation)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me about [insert question]",
  tools: [{
    type: "file_search",
    file_search_store_names: [fileSearchStore.name]
  }]
});

for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.annotations) {
        contentBlock.annotations.forEach((annotation) => {
          console.log(annotation);
        });
      }
    }
  }
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
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
            if (textContent.annotations().isPresent()) {
              for (Annotation annotation : textContent.annotations().get()) {
                System.out.println(annotation);
              }
            }
          }
        }
      }
    }
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
                Input: interactions.NewInteractionsInput("Tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
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
                    for _, annotation := range content.TextContent.Annotations {
                        fmt.Println(annotation)
                    }
                }
            }
        }
    }
}
```

### REST

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "...",
          "annotations": [
            {
              "file_name": "...",
              "source": "...",
              "custom_metadata": [
                {
                  "key": "author",
                  "string_value": "Robert Graves"
                },
                {
                  "key": "year",
                  "numeric_value": 1934
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## الناتج المنظَّم

بدءًا من نماذج Gemini 3، يمكنك دمج أداة البحث عن الملفات مع [النتائج المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the minimum hourly wage in Tokyo right now?",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Money.model_json_schema()
    },
)
result = Money.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { z } from "zod";

const moneyJsonSchema = {
  type: "object",
  properties: {
    amount: { type: "string", description: "The numerical part of the amount." },
    currency: { type: "string", description: "The currency of amount." }
  },
  required: ["amount", "currency"]
};

const moneySchema = z.fromJSONSchema(moneyJsonSchema);

async function run() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the minimum hourly wage in Tokyo right now?",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name],
    }],
    response_format: {
      type: 'text',
      mime_type: 'application/json',
      schema: moneyJsonSchema
    },
  });

  const result = moneySchema.parse(JSON.parse(interaction.output_text));
  console.log(result);
}

run();
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();

Map<String, Object> amountProp = new HashMap<>();
amountProp.put("type", "string");
amountProp.put("description", "The numerical part of the amount.");
properties.put("amount", amountProp);

Map<String, Object> currencyProp = new HashMap<>();
currencyProp.put("type", "string");
currencyProp.put("description", "The currency of amount.");
properties.put("currency", currencyProp);

Map<String, Object> moneyJsonSchema = new HashMap<>();
moneyJsonSchema.put("type", "object");
moneyJsonSchema.put("properties", properties);
moneyJsonSchema.put("required", Arrays.asList("amount", "currency"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(moneyJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the minimum hourly wage in Tokyo right now?"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
        .responseFormat(format)
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

    moneyJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "amount": map[string]any{
                "type":        "string",
                "description": "The numerical part of the amount.",
            },
            "currency": map[string]any{
                "type":        "string",
                "description": "The currency of amount.",
            },
        },
        "required": []string{"amount", "currency"},
    }

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   moneyJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("What is the minimum hourly wage in Tokyo right now?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
                },
                ResponseFormat: &format,
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
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the minimum hourly wage in Tokyo right now?",
    "tools": [{
      "type": "file_search",
      "file_search_store_names": ["$FILE_SEARCH_STORE_NAME"]
    }],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "amount": {"type": "string", "description": "The numerical part of the amount."},
          "currency": {"type": "string", "description": "The currency of amount."}
        },
        "required": ["amount", "currency"]
      }
    }
  }'
```

## النماذج المتوافقة

تتيح الطُرز التالية استخدام ميزة "البحث عن الملفات":

| الطراز | البحث عن الملفات |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=ar) | ✔️ |
| [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=ar) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |

## أنواع الملفات المعتمدة

يتيح &quot;بحث الملفات&quot; استخدام مجموعة كبيرة من تنسيقات الملفات، كما هو موضّح في الأقسام التالية.

### أنواع ملفات التطبيقات

- `application/dart`
- `application/ecmascript`
- `application/json`
- `application/ms-java`
- `application/msword`
- `application/pdf`
- `application/sql`
- `application/typescript`
- `application/vnd.curl`
- `application/vnd.dart`
- `application/vnd.ibm.secure-container`
- `application/vnd.jupyter`
- `application/vnd.ms-excel`
- `application/vnd.oasis.opendocument.text`
- `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.template`
- `application/x-csh`
- `application/x-hwp`
- `application/x-hwp-v5`
- `application/x-latex`
- `application/x-php`
- `application/x-powershell`
- `application/x-sh`
- `application/x-shellscript`
- `application/x-tex`
- `application/x-zsh`
- `application/xml`
- `application/zip`

### أنواع الملفات النصية

- `text/1d-interleaved-parityfec`
- `text/RED`
- `text/SGML`
- `text/cache-manifest`
- `text/calendar`
- `text/cql`
- `text/cql-extension`
- `text/cql-identifier`
- `text/css`
- `text/csv`
- `text/csv-schema`
- `text/dns`
- `text/encaprtp`
- `text/enriched`
- `text/example`
- `text/fhirpath`
- `text/flexfec`
- `text/fwdred`
- `text/gff3`
- `text/grammar-ref-list`
- `text/hl7v2`
- `text/html`
- `text/javascript`
- `text/jcr-cnd`
- `text/jsx`
- `text/markdown`
- `text/mizar`
- `text/n3`
- `text/parameters`
- `text/parityfec`
- `text/php`
- `text/plain`
- `text/provenance-notation`
- `text/prs.fallenstein.rst`
- `text/prs.lines.tag`
- `text/prs.prop.logic`
- `text/raptorfec`
- `text/rfc822-headers`
- `text/rtf`
- `text/rtp-enc-aescm128`
- `text/rtploopback`
- `text/rtx`
- `text/sgml`
- `text/shaclc`
- `text/shex`
- `text/spdx`
- `text/strings`
- `text/t140`
- `text/tab-separated-values`
- `text/texmacs`
- `text/troff`
- `text/tsv`
- `text/tsx`
- `text/turtle`
- `text/ulpfec`
- `text/uri-list`
- `text/vcard`
- `text/vnd.DMClientScript`
- `text/vnd.IPTC.NITF`
- `text/vnd.IPTC.NewsML`
- `text/vnd.a`
- `text/vnd.abc`
- `text/vnd.ascii-art`
- `text/vnd.curl`
- `text/vnd.debian.copyright`
- `text/vnd.dvb.subtitle`
- `text/vnd.esmertec.theme-descriptor`
- `text/vnd.exchangeable`
- `text/vnd.familysearch.gedcom`
- `text/vnd.ficlab.flt`
- `text/vnd.fly`
- `text/vnd.fmi.flexstor`
- `text/vnd.gml`
- `text/vnd.graphviz`
- `text/vnd.hans`
- `text/vnd.hgl`
- `text/vnd.in3d.3dml`
- `text/vnd.in3d.spot`
- `text/vnd.latex-z`
- `text/vnd.motorola.reflex`
- `text/vnd.ms-mediapackage`
- `text/vnd.net2phone.commcenter.command`
- `text/vnd.radisys.msml-basic-layout`
- `text/vnd.senx.warpscript`
- `text/vnd.sosi`
- `text/vnd.sun.j2me.app-descriptor`
- `text/vnd.trolltech.linguist`
- `text/vnd.wap.si`
- `text/vnd.wap.sl`
- `text/vnd.wap.wml`
- `text/vnd.wap.wmlscript`
- `text/vtt`
- `text/wgsl`
- `text/x-asm`
- `text/x-bibtex`
- `text/x-boo`
- `text/x-c`
- `text/x-c++hdr`
- `text/x-c++src`
- `text/x-cassandra`
- `text/x-chdr`
- `text/x-coffeescript`
- `text/x-component`
- `text/x-csh`
- `text/x-csharp`
- `text/x-csrc`
- `text/x-cuda`
- `text/x-d`
- `text/x-diff`
- `text/x-dsrc`
- `text/x-emacs-lisp`
- `text/x-erlang`
- `text/x-gff3`
- `text/x-go`
- `text/x-haskell`
- `text/x-java`
- `text/x-java-properties`
- `text/x-java-source`
- `text/x-kotlin`
- `text/x-lilypond`
- `text/x-lisp`
- `text/x-literate-haskell`
- `text/x-lua`
- `text/x-moc`
- `text/x-objcsrc`
- `text/x-pascal`
- `text/x-pcs-gcd`
- `text/x-perl`
- `text/x-perl-script`
- `text/x-python`
- `text/x-python-script`
- `text/x-r-markdown`
- `text/x-rsrc`
- `text/x-rst`
- `text/x-ruby-script`
- `text/x-rust`
- `text/x-sass`
- `text/x-scala`
- `text/x-scheme`
- `text/x-script.python`
- `text/x-scss`
- `text/x-setext`
- `text/x-sfv`
- `text/x-sh`
- `text/x-siesta`
- `text/x-sos`
- `text/x-sql`
- `text/x-swift`
- `text/x-tcl`
- `text/x-tex`
- `text/x-vbasic`
- `text/x-vcalendar`
- `text/xml`
- `text/xml-dtd`
- `text/xml-external-parsed-entity`
- `text/yaml`

## القيود

- **Live API:** لا تتوافق ميزة &quot;البحث عن الملفات&quot; مع [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar).
- **عدم توافق الأدوات:** لا يمكن دمج أدوات تحديد المصدر المضمّنة مع بعضها البعض،
  على سبيل المثال، لا يمكن استخدام "البحث عن الملفات" في الوقت نفسه مع [تحديد المصدر من خلال "بحث Search"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) أو
  [سياق عناوين URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) في الطلب نفسه.

### حدود معدّل الاستخدام

تفرض واجهة برمجة التطبيقات File Search API الحدود التالية لضمان ثبات الخدمة:

- **الحدّ الأقصى لحجم الملف / الحدّ الأقصى لكل مستند**: 100 ميغابايت
- **إجمالي حجم مساحات تخزين "البحث عن الملفات" في المشروع** (استنادًا إلى مستوى المستخدم):
  - **الخطة المجانية**: 1 غيغابايت
  - **المستوى 1**: 10 غيغابايت
  - **المستوى 2**: ‏100 غيغابايت
  - **المستوى 3**: 1 تيرابايت
- **اقتراح**: يجب ألا يتجاوز حجم كل مستودع بيانات في "بحث الملفات" 20 غيغابايت لضمان أفضل أوقات استجابة ممكنة.

## الأسعار

- يتم تحصيل رسوم منك مقابل التضمينات في وقت الفهرسة استنادًا إلى [أسعار التضمينات](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#gemini-embedding-2) الحالية.
- تتوفر خدمة تخزين الأمتعة مجانًا.
- تكون تضمينات وقت طلب البحث مجانية.
- يتم تحصيل رسوم من الرموز المميزة للمستندات التي تم استرجاعها باعتبارها
  [رموزًا مميزة للسياق](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) عادية.

## الخطوات التالية

- انتقِل إلى مرجع واجهة برمجة التطبيقات [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=ar) و[Documents](https://ai.google.dev/api/file-search/documents?hl=ar) في File Search.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
