---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=hi
fetched_at: 2026-10-26T06:05:54.661118+00:00
title: "\u092b\u093c\u093e\u0907\u0932 \u0916\u094b\u091c\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# फ़ाइल खोजना

Gemini API, फ़ाइल सर्च टूल के ज़रिए Retrieval Augmented Generation ("RAG") की सुविधा देता है. File Search, आपके डेटा को इंपोर्ट करता है, उसे छोटे-छोटे हिस्सों में बांटता है, और इंडेक्स करता है. इससे, दिए गए प्रॉम्प्ट के आधार पर काम की जानकारी को तेज़ी से वापस पाने में मदद मिलती है. इसके बाद, इस जानकारी का इस्तेमाल मॉडल के लिए कॉन्टेक्स्ट के तौर पर किया जाता है. इससे मॉडल को ज़्यादा सटीक और काम के जवाब देने में मदद मिलती है. फ़ाइल खोजने की सुविधा, टेक्स्ट एम्बेडिंग के साथ-साथ टेक्स्ट, इमेज, और वीडियो वगैरह का इस्तेमाल करके की गई क्वेरी के जवाब देने की सुविधा भी दे सकती है. टेक्स्ट एम्बेडिंग की सुविधा `gemini-embedding-001` के साथ काम करती है. वहीं, इमेज/टेक्स्ट, इमेज, और वीडियो वगैरह का इस्तेमाल करके की गई क्वेरी के जवाब देने की सुविधा `gemini-embedding-2` के साथ काम करती है.

फ़ाइल स्टोरेज और क्वेरी के समय एम्बेडिंग जनरेट करने की सुविधा बिना किसी शुल्क के उपलब्ध है. आपको सिर्फ़ तब शुल्क देना होगा, जब पहली बार अपनी फ़ाइलों को इंडेक्स किया जाएगा और Gemini मॉडल के सामान्य इनपुट / आउटपुट टोकन का शुल्क देना होगा. बिलिंग के इस नए मॉडल की मदद से, फ़ाइल सर्च टूल को बनाना और उसे बड़े पैमाने पर इस्तेमाल करना आसान और किफ़ायती हो जाता है. ज़्यादा जानकारी के लिए, [कीमत](#pricing) सेक्शन देखें.

## फ़ाइल खोज स्टोर में सीधे तौर पर अपलोड करना

इस उदाहरण में, [फ़ाइल सर्च स्टोर](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#method:-media.uploadtofilesearchstore) में सीधे तौर पर फ़ाइल अपलोड करने का तरीका बताया गया है:

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

### Java

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

### ऐप पर जाएं

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

### आराम का समय

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

ज़्यादा जानकारी के लिए, [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#method:-media.uploadtofilesearchstore) के लिए एपीआई का संदर्भ देखें.

## फ़ाइलें इंपोर्ट करना

इसके अलावा, कोई मौजूदा फ़ाइल अपलोड करके, [उसे फ़ाइल सर्च स्टोर में इंपोर्ट](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#method:-filesearchstores.importfile) किया जा सकता है:

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

### Java

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

### ऐप पर जाएं

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

### आराम का समय

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

ज़्यादा जानकारी के लिए, [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#method:-filesearchstores.importfile) के लिए एपीआई का संदर्भ देखें.

## चंकिंग कॉन्फ़िगरेशन

जब किसी फ़ाइल को File Search स्टोर में इंपोर्ट किया जाता है, तो वह अपने-आप छोटे-छोटे हिस्सों में बंट जाती है. इसके बाद, उसे एंबेड और इंडेक्स किया जाता है. साथ ही, File Search स्टोर में अपलोड किया जाता है. अगर आपको चंकिंग की रणनीति पर ज़्यादा कंट्रोल चाहिए, तो [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=hi#request-body_5) सेटिंग का इस्तेमाल करें. इससे, हर चंक के लिए ज़्यादा से ज़्यादा टोकन और ओवरलैप होने वाले टोकन की ज़्यादा से ज़्यादा संख्या सेट की जा सकती है.

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

### Java

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

### ऐप पर जाएं

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

फ़ाइल खोजने की सुविधा वाले स्टोर का इस्तेमाल करने के लिए, इसे `interactions.create`
तरीके में टूल के तौर पर पास करें. इसके लिए, [अपलोड करें](#upload) और [इंपोर्ट करें](#importing-files) के उदाहरण देखें.

## यह कैसे काम करता है

File Search, उपयोगकर्ता के प्रॉम्प्ट से जुड़ी जानकारी ढूंढने के लिए, सिमैंटिक सर्च नाम की तकनीक का इस्तेमाल करता है. स्टैंडर्ड कीवर्ड-आधारित खोज के उलट, सिमैंटिक सर्च आपकी क्वेरी के मतलब और संदर्भ को समझती है.

जब कोई फ़ाइल इंपोर्ट की जाती है, तो उसे संख्याओं में बदल दिया जाता है. इन्हें [एम्बेडिंग](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi) कहा जाता है. इनसे अपलोड किए गए कॉन्टेंट का सिमैंटिक मतलब पता चलता है. इन एम्बेडिंग को, फ़ाइल खोजने के लिए खास तौर पर बनाए गए डेटाबेस में सेव किया जाता है.
जब कोई क्वेरी की जाती है, तो उसे भी एंबेडिंग में बदल दिया जाता है. इसके बाद, सिस्टम फ़ाइल खोज की सुविधा का इस्तेमाल करके, फ़ाइल खोज के स्टोर से मिलते-जुलते और काम के दस्तावेज़ के हिस्सों को ढूंढता है.

एम्बेडिंग के लिए, टाइम टू लिव (टीटीएल) की कोई सीमा नहीं होती. ये तब तक मौजूद रहते हैं, जब तक इन्हें मैन्युअल तरीके से मिटाया नहीं जाता या मॉडल को बंद नहीं किया जाता. हालांकि, फ़ाइलें 48 घंटों के बाद मिटा दी जाती हैं.

फ़ाइल खोजने की सुविधा वाले `uploadToFileSearchStore` एपीआई का इस्तेमाल करने की प्रोसेस के बारे में यहां बताया गया है:

1. **फ़ाइल खोज का स्टोर बनाएं**: फ़ाइल खोज के स्टोर में, आपकी फ़ाइलों से प्रोसेस किया गया डेटा होता है. यह एम्बेडिंग के लिए स्थायी कंटेनर है, जिस पर सिमैंटिक सर्च काम करेगा.
2. **कोई फ़ाइल अपलोड करना और उसे File Search स्टोर में इंपोर्ट करना**: एक साथ कोई फ़ाइल अपलोड करें और नतीजों को अपने File Search स्टोर में इंपोर्ट करें. इससे एक अस्थायी `File` ऑब्जेक्ट बनता है, जो आपके ओरिजनल दस्तावेज़ का रेफ़रंस होता है. इसके बाद, उस डेटा को छोटे-छोटे हिस्सों में बांटा जाता है, फ़ाइल सर्च एंबेडिंग में बदला जाता है, और इंडेक्स किया जाता है. `File` ऑब्जेक्ट 48 घंटों के बाद मिट जाता है. हालांकि, File Search स्टोर में इंपोर्ट किया गया डेटा तब तक सेव रहेगा, जब तक उसे मिटाया नहीं जाता.
3. **फ़ाइल सर्च टूल की मदद से क्वेरी करना**: आखिर में, `FileSearch` टूल का इस्तेमाल `generateContent` कॉल में किया जाता है. टूल कॉन्फ़िगरेशन में, आपको एक `FileSearchRetrievalResource` तय करना होता है. यह `FileSearchStore` की ओर इशारा करता है, जिसे आपको खोजना है. इससे मॉडल को उस खास File Search स्टोर में सिमैंटिक सर्च करने का निर्देश मिलता है, ताकि वह अपने जवाब को बेहतर बनाने के लिए काम की जानकारी ढूंढ सके.

![फ़ाइल खोजने की सुविधा के लिए इंडेक्स करने और क्वेरी करने की प्रोसेस](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=hi)

फ़ाइल खोजने की सुविधा के लिए, इंडेक्स करने और क्वेरी करने की प्रोसेस

इस डायग्राम में, *दस्तावेज़* से *एम्बेडिंग मॉडल* तक की बिंदु वाली लाइन ([`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=hi) का इस्तेमाल करके), `uploadToFileSearchStore` एपीआई को दिखाती है. यह *फ़ाइल स्टोरेज* को बायपास करती है.
इसके अलावा, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) का इस्तेमाल करके, अलग से फ़ाइलें बनाई जा सकती हैं और फिर उन्हें इंपोर्ट किया जा सकता है. इससे इंडेक्स करने की प्रोसेस, *दस्तावेज़* से *फ़ाइल स्टोरेज* और फिर *एम्बेडिंग मॉडल* पर शिफ़्ट हो जाती है.

## फ़ाइल खोजने की सुविधा देने वाले ऐप्लिकेशन

फ़ाइल खोजने की सुविधा वाला स्टोर, आपके दस्तावेज़ों के एम्बेड किए गए वर्शन के लिए कंटेनर होता है. File API के ज़रिए अपलोड की गई रॉ फ़ाइलें, 48 घंटे बाद मिट जाती हैं. हालांकि, फ़ाइल सर्च स्टोर में इंपोर्ट किया गया डेटा तब तक सेव रहता है, जब तक उसे मैन्युअल तरीके से नहीं मिटाया जाता. अपने दस्तावेज़ों को व्यवस्थित करने के लिए, एक से ज़्यादा फ़ाइल खोज स्टोर बनाए जा सकते हैं. `FileSearchStore` एपीआई की मदद से, फ़ाइल खोज स्टोर को मैनेज करने के लिए, उन्हें बनाया, लिस्ट किया, पाया, और मिटाया जा सकता है. फ़ाइल खोज में स्टोर के नाम, दुनिया भर में उपलब्ध होते हैं.

यहां File Search स्टोर मैनेज करने के कुछ उदाहरण दिए गए हैं:

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

### Java

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

### ऐप पर जाएं

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

### आराम का समय

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=${GEMINI_API_KEY}"
```

## फ़ाइल खोजने से जुड़े दस्तावेज़

[File Search Documents](https://ai.google.dev/api/file-search/documents?hl=hi) API की मदद से, फ़ाइल स्टोर में मौजूद अलग-अलग दस्तावेज़ों को मैनेज किया जा सकता है. इससे, फ़ाइल सर्च स्टोर में मौजूद हर दस्तावेज़ को `list` किया जा सकता है, किसी दस्तावेज़ की जानकारी `get` की जा सकती है, और नाम के हिसाब से दस्तावेज़ को `delete` किया जा सकता है.

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

### Java

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

### ऐप पर जाएं

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

## फ़ाइल का मेटाडेटा

अपनी फ़ाइलों में कस्टम मेटाडेटा जोड़ा जा सकता है, ताकि उन्हें फ़िल्टर करने या ज़्यादा जानकारी देने में मदद मिल सके. मेटाडेटा, की-वैल्यू पेयर का एक सेट होता है.

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

### Java

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

### ऐप पर जाएं

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

यह तब काम आता है, जब आपके पास File Search स्टोर में कई दस्तावेज़ हों और आपको उनमें से सिर्फ़ कुछ दस्तावेज़ खोजने हों.

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

### Java

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

### ऐप पर जाएं

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

### आराम का समय

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

`metadata_filter` के लिए, सूची को फ़िल्टर करने वाले सिंटैक्स को लागू करने के बारे में जानकारी, [google.aip.dev/160](https://google.aip.dev/160) पर देखी जा सकती है

## मल्टीमॉडल फ़ाइल सर्च

मल्टीमोडल फ़ाइल सर्च की सुविधा से, इमेज को नेटिव तौर पर एम्बेड किया जा सकता है और उन्हें खोजा जा सकता है. इससे, बेहतर और मल्टीमोडल आरएजी ऐप्लिकेशन बनाए जा सकते हैं.

### एंबेड करने वाले मॉडल को कॉन्फ़िगर करना

`FileSearchStore` बनाते समय, आपको मल्टीमॉडल का इस्तेमाल करने के लिए, सिर्फ़ टेक्स्ट वाले डिफ़ॉल्ट एंबेडिंग मॉडल को बदलना होगा. टेक्स्ट और इमेज, दोनों को प्रोसेस करने के लिए `models/gemini-embedding-2` का इस्तेमाल करें.

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

### Java

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

### ऐप पर जाएं

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

### आराम का समय

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "display_name": "Multimodal Catalog",
      "embedding_model": "models/gemini-embedding-2"
    }'
```

### इमेज अपलोड करें

मल्टीमोडल एंबेडिंग मॉडल की मदद से स्टोर बनाने के बाद, इमेज फ़ाइलें सीधे अपलोड की जा सकती हैं. इसके लिए, अपलोड करने वाले उन्हीं एपीआई का इस्तेमाल करें जिनके बारे में [फ़ाइल सर्च स्टोर पर सीधे अपलोड करना](#upload) या [फ़ाइलें इंपोर्ट करना](#importing-files) में बताया गया है.

**इमेज फ़ाइल से जुड़ी ज़रूरी शर्तें:**

- इमेज फ़ाइलों का रिज़ॉल्यूशन 4K x 4K पिक्सल से ज़्यादा नहीं होना चाहिए.
- PNG और JPEG फ़ॉर्मैट का इस्तेमाल किया जा सकता है.

## उद्धरण

फ़ाइल खोज की सुविधा का इस्तेमाल करने पर, मॉडल के जवाब में उद्धरण शामिल हो सकते हैं. इनसे पता चलता है कि जवाब जनरेट करने के लिए, आपके अपलोड किए गए दस्तावेज़ों के किन हिस्सों का इस्तेमाल किया गया. इससे तथ्यों की जांच करने और पुष्टि करने में मदद मिलती है.

जवाब के `model_output` चरण के `content` ब्लॉक में मौजूद `annotations` एट्रिब्यूट की मदद से, उद्धरण की जानकारी ऐक्सेस की जा सकती है.

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

### Java

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

### ऐप पर जाएं

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

### आराम का समय

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

उद्धरणों के स्ट्रक्चर के बारे में ज़्यादा जानकारी के लिए, [इंटरैक्शन के लिए एपीआई का संदर्भ](https://ai.google.dev/api/interactions-api?hl=hi#Resource:FileCitation) देखें.

### पेज नंबर

पेज वाले दस्तावेज़ों (जैसे कि PDF) में फ़ाइल खोजने की सुविधा का इस्तेमाल करने पर, मॉडल के जवाब में वह पेज नंबर शामिल हो सकता है जहां जानकारी मिली थी.
इस जानकारी को `file_citation` एनोटेशन के `page_number` एट्रिब्यूट की मदद से ऐक्सेस किया जा सकता है.

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

### Java

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

### ऐप पर जाएं

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

### मीडिया साइटेशन

जब मॉडल, इमेज जनरेट करते समय किसी इमेज के हिस्से का रेफ़रंस देता है, तब एपीआई एनोटेशन में `file_citation` टाइप का एनोटेशन दिखाता है. इसमें `media_id` शामिल होता है. इस आईडी का इस्तेमाल करके, इमेज का वह हिस्सा डाउनलोड किया जा सकता है जिसका रेफ़रंस मॉडल ने दिया है. यह `media_id`, खोज के लिए किए गए कई कॉल के दौरान एक जैसा रहता है. इससे, आपको एक ही इमेज को भरोसेमंद तरीके से वापस पाने या आईडी का इस्तेमाल करके उसे कैश मेमोरी में सेव करने की सुविधा मिलती है.

यहां दिया गया स्निपेट, REST रिस्पॉन्स के चरण का एक उदाहरण है:

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

यहां दिए गए कोड स्निपेट में, `media_id` को वापस पाने और मीडिया को डाउनलोड करने का तरीका बताया गया है:

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

### Java

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

### ऐप पर जाएं

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

## कस्टम मेटाडेटा

अगर आपने अपनी फ़ाइलों में कस्टम मेटाडेटा जोड़ा है, तो उसे मॉडल के जवाब के एनोटेशन में ऐक्सेस किया जा सकता है. यह आपके सोर्स दस्तावेज़ों से, ऐप्लिकेशन लॉजिक में अतिरिक्त कॉन्टेक्स्ट (जैसे कि यूआरएल, पेज नंबर या लेखक) पास करने के लिए काम का है. `file_citation` टाइप के हर उद्धरण एनोटेशन में, यह कस्टम मेटाडेटा शामिल होता है.

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

### Java

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

### ऐप पर जाएं

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

## स्ट्रक्चर्ड आउटपुट

Gemini 3 मॉडल से शुरू करके, फ़ाइल खोजने वाले टूल को [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) के साथ इस्तेमाल किया जा सकता है.

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

### Java

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

### ऐप पर जाएं

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

### आराम का समय

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

## इन मॉडल के साथ काम करता है

फ़ाइल खोजने की सुविधा के साथ ये मॉडल काम करते हैं:

| मॉडल | फ़ाइलें खोजना |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=hi) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=hi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |

## एक साथ इस्तेमाल किए जा सकने वाले टूल

Gemini 4 और Gemini 3 मॉडल, पहले से मौजूद टूल (जैसे, फ़ाइल सर्च) को कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ इस्तेमाल करने की सुविधा देते हैं. [टूल कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) पेज पर जाकर ज़्यादा जानें.

## इस्तेमाल किए जा सकने वाले फ़ाइल टाइप

फ़ाइल खोजने की सुविधा, अलग-अलग तरह के फ़ाइल फ़ॉर्मैट के साथ काम करती है. इनकी जानकारी यहां दी गई है.

### ऐप्लिकेशन की फ़ाइल के टाइप

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

### टेक्स्ट फ़ाइल टाइप

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

## सीमाएं

- **Live API:** [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) में, फ़ाइल खोजने की सुविधा काम नहीं करती.
- **टूल के साथ काम न करना:** बिल्ट-इन ग्राउंडिंग टूल को एक साथ इस्तेमाल नहीं किया जा सकता;
  उदाहरण के लिए, एक ही अनुरोध में फ़ाइल खोजने की सुविधा को [Google Search से मिली जानकारी का इस्तेमाल करके जवाब देने की सुविधा](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) या [यूआरएल के कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) के साथ एक साथ इस्तेमाल नहीं किया जा सकता.

### अनुरोधों की संख्या की सीमाएं

सेवा को बेहतर तरीके से उपलब्ध कराने के लिए, File Search API पर ये सीमाएं लागू होती हैं:

- **फ़ाइल का ज़्यादा से ज़्यादा साइज़ / हर दस्तावेज़ के लिए तय सीमा**: 100 एमबी
- **प्रोजेक्ट के File Search स्टोर का कुल साइज़** (उपयोगकर्ता के टियर के आधार पर):
  - **बिना किसी शुल्क के**: 1 जीबी
  - **टियर 1**: 10 जीबी
  - **दूसरा टियर**: 100 जीबी
  - **टियर 3**: 1 टीबी
- **सुझाव**: हर फ़ाइल खोज स्टोर का साइज़ 20 जीबी से कम रखें, ताकि डेटा को तेज़ी से वापस पाया जा सके.

## कीमत

- इंडेक्स करने के समय, एंबेडिंग के लिए आपसे शुल्क लिया जाता है. यह शुल्क, [एंबेडिंग की मौजूदा कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#gemini-embedding-2) के आधार पर तय होता है.
- स्टोरेज की सुविधा बिना किसी शुल्क के उपलब्ध है.
- क्वेरी के समय एम्बेड करने की सुविधा बिना किसी शुल्क के उपलब्ध है.
- वापस लाए गए दस्तावेज़ के टोकन के लिए, सामान्य [कॉन्टेक्स्ट टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) की तरह ही शुल्क लिया जाता है.

## आगे क्या करना है

- [फ़ाइल खोजने की सुविधा देने वाले स्टोर](https://ai.google.dev/api/file-search/file-search-stores?hl=hi) और फ़ाइल खोजने की सुविधा देने वाले [दस्तावेज़ों](https://ai.google.dev/api/file-search/documents?hl=hi) के लिए, एपीआई रेफ़रंस पर जाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया."],[],[]]
