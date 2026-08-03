---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=ja
fetched_at: 2026-08-03T04:35:47.992279+00:00
title: "\u30d5\u30a1\u30a4\u30eb\u691c\u7d22 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# ファイル検索

Gemini API では、ファイル検索ツールを使用して検索拡張生成（RAG）が可能です。ファイル検索は、プロンプトに基づいて関連情報を迅速に取得できるように、データをインポート、チャンク化、インデックス化します。取得した情報はモデルのコンテキストとして使用され、より正確で関連性の高い回答を提供できるようになります。ファイル検索では、`gemini-embedding-001` でサポートされているテキスト エンベディングと、`gemini-embedding-2` でサポートされている画像/マルチモーダル エンベディングを使用して、マルチモーダル機能を提供することもできます。

クエリ時のファイルの保存とエンベディングの生成は無料です。エンベディングの作成に対して料金が発生するのは、ファイルを初めてインデックス化するときと、通常の Gemini モデルの入力 / 出力トークンの費用のみです。この新しい課金パラダイムにより、ファイル検索ツールの構築とスケーリングが簡単かつ費用対効果の高いものになります。詳細については、
[料金](#pricing)セクションをご覧ください。

## ファイル検索ストアに直接アップロードする

この例では、ファイルを
[ファイル検索ストア](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#method:-media.uploadtofilesearchstore)に直接アップロードする方法を示します。

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
      "model": "gemini-3.6-flash",
      "input": "Can you tell me about [insert question]",
      "tools": [{
        "type": "file_search",
        "file_search_store_names": ["'"$FILE_SEARCH_STORE_NAME"'"]
      }]
    }'
```

詳細については、[`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#method:-media.uploadtofilesearchstore) の API リファレンスをご覧ください。

## ファイルのインポート

または、既存のファイルをアップロードして、[ファイル検索ストアにインポート](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#method:-filesearchstores.importfile)することもできます。

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
      "model": "gemini-3.6-flash",
      "input": "Can you tell me about [insert question]",
      "tools": [{
        "type": "file_search",
        "file_search_store_names": ["'"$FILE_SEARCH_STORE_NAME"'"]
      }]
    }'
```

詳細については、[`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#method:-filesearchstores.importfile) の API リファレンスをご覧ください。

## チャンク化の構成

ファイルをファイル検索ストアにインポートすると、自動的にチャンクに分割され、埋め込み、インデックス化されて、ファイル検索ストアにアップロードされます。チャンク化戦略をより細かく制御する必要がある場合は、
[`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=ja#request-body_5) 設定
を指定して、チャンクあたりのトークンの最大数と重複する
トークンの最大数を設定できます。

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

ファイル検索ストアを使用するには、`interactions.create`
メソッドにツールとして渡します。これは、[アップロード](#upload)と[インポート](#importing-files)の例に示されています。

## 仕組み

ファイル検索では、セマンティック検索と呼ばれる手法を使用して、ユーザー プロンプトに関連する情報を検索します。セマンティック検索は、標準のキーワード ベースの検索とは異なり、クエリの意味とコンテキストを理解します。

ファイルをインポートすると、アップロードされたコンテンツのセマンティックな意味を捉える
[エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)と呼ばれる数値表現に変換されます。これらのエンベディングは、専用のファイル検索データベースに保存されます。
クエリを実行すると、エンベディングに変換されます。次に、システムはファイル検索を実行して、ファイル検索ストアから最も類似した関連性の高いドキュメント チャンクを見つけます。

エンベディングには有効期間（TTL）はありません。手動で削除されるか、モデルが非推奨になるまで保持されます。ただし、ファイルは 48 時間後に削除されます。

ファイル検索 `uploadToFileSearchStore` API を使用するプロセスの内訳は次のとおりです。

1. **ファイル検索ストアを作成する**: ファイル検索ストアには、ファイルから処理された
   データが含まれます。これは、セマンティック検索が動作するエンベディングの永続的なコンテナです。
2. **ファイルをアップロードしてファイル検索ストアにインポートする**: ファイルをアップロードし、結果をファイル検索ストアにインポートします。これにより、元のドキュメントへの参照である一時的な `File` オブジェクトが作成されます。そのデータはチャンク化され、ファイル検索エンベディングに変換されてインデックス化されます。`File` オブジェクトは 48 時間後に削除されますが、ファイル検索ストアにインポートされたデータは、削除するまで無期限に保存されます。
3. **ファイル検索でクエリを実行する**: 最後に、`FileSearch` ツールを
   `generateContent` 呼び出しで使用します。ツール構成で、検索する `FileSearchStore` を指す `FileSearchRetrievalResource` を指定します。これにより、モデルは特定のファイル検索ストアでセマンティック検索を実行して、レスポンスのグラウンディングに関連する情報を検索します。

![ファイル検索のインデックス登録とクエリのプロセス](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=ja)

ファイル検索のインデックス作成とクエリのプロセス

この図では、[*ドキュメント*] から [*エンベディング モデル*]
（[`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja) を使用）への点線は、`uploadToFileSearchStore` API（[*ファイル ストレージ*] をバイパス）を表しています。
*それ以外の場合は、[[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja)] を使用して個別に作成
してからファイルをインポートすると、インデックス作成プロセスは [*ドキュメント*] から
[*ファイル ストレージ*]、[エンベディング モデル]* に移動します。

## ファイル検索ストア

ファイル検索ストアは、ドキュメント エンベディングのコンテナです。File API を使用してアップロードされた元のファイルは 48 時間後に削除されますが、ファイル検索ストアにインポートされたデータは、手動で削除するまで無期限に保存されます。複数のファイル検索ストアを作成して、ドキュメントを整理できます。`FileSearchStore` API を使用すると、ファイル検索ストアの作成、一覧表示、取得、削除を行って管理できます。ファイル検索ストア名はグローバル スコープです。

ファイル検索ストアを管理する方法の例を次に示します。

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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=${GEMINI_API_KEY}"
```

## ファイル検索ドキュメント

[ファイル検索ドキュメント](https://ai.google.dev/api/file-search/documents?hl=ja) API を使用すると、ファイルストア内の個々のドキュメントを管理できます。ファイル検索ストア内の各ドキュメントを `list` し、ドキュメントに関する情報を `get` し、名前でドキュメントを `delete` できます。

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

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=${GEMINI_API_KEY}&force=true"
```

## ファイルのメタデータ

ファイルにカスタム メタデータを追加して、フィルタリングや追加のコンテキストの提供に役立てることができます。メタデータは Key-Value ペアのセットです。

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

これは、ファイル検索ストアに複数のドキュメントがあり、そのサブセットのみを検索する場合に便利です。

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
            "model": "gemini-3.6-flash",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

`metadata_filter` のリストフィルタ構文の実装に関するガイダンスについては、[google.aip.dev/160](https://google.aip.dev/160) をご覧ください。

## マルチモーダル ファイル検索

マルチモーダル ファイル検索を使用すると、画像をネイティブに埋め込んで検索できるため、リッチなマルチモーダル RAG アプリケーションが可能になります。

### エンベディング モデルを構成する

`FileSearchStore` を作成する場合は、デフォルトのテキストのみのエンベディング モデルをオーバーライドして、マルチモーダル モデルを使用する必要があります。`models/gemini-embedding-2` を使用して、テキストと画像の両方を処理します。

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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "display_name": "Multimodal Catalog",
      "embedding_model": "models/gemini-embedding-2"
    }'
```

### 画像のアップロード

マルチモーダル エンベディング モデルを使用してストアを作成したら、
ファイル検索ストアに直接アップロードする[または](#upload)[ファイルのインポート](#importing-files)で説明されているのと同じアップロード API を使用して、画像ファイルを直接アップロードできます。

**画像ファイルの要件:**

- 画像ファイルの解像度は 4K x 4K ピクセル以下にする必要があります。
- サポートされている形式は PNG、JPEG です。

## 引用

ファイル検索を使用すると、モデルのレスポンスに、アップロードしたドキュメントのどの部分が回答の生成に使用されたかを指定する引用が含まれることがあります。これは、ファクト チェックと検証に役立ちます。

引用情報には、レスポンスの `model_output` ステップの `content` ブロック内の `annotations` 属性からアクセスできます。

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

引用の構造の詳細については、
[インタラクションの API リファレンスをご覧ください](https://ai.google.dev/api/interactions-api?hl=ja#Resource:FileCitation)。

### ページ番号

ページがあるドキュメント（PDF など）でファイル検索を使用すると、モデルのレスポンスに情報が見つかったページ番号が含まれることがあります。
この情報には、`file_citation` アノテーションの `page_number` 属性からアクセスできます。

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

### メディアの引用

生成中にモデルが画像チャンクを参照すると、API は `media_id` を含むアノテーションに `file_citation` 型のアノテーションを返します。この ID を使用すると、モデルが参照した正確な画像チャンクをダウンロードできます。この `media_id` は複数の検索呼び出しで永続的に保持されるため、同じ画像を確実に取得したり、ID を使用してキャッシュに保存したりできます。

次のスニペットは、REST レスポンス ステップの例です。

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

次のコード スニペットは、`media_id` を取得してメディアをダウンロードする方法を示しています。

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

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## カスタム メタデータ

ファイルにカスタム メタデータを追加した場合は、モデルのレスポンスのアノテーションでアクセスできます。これは、ソース ドキュメントからアプリケーション ロジックに追加のコンテキスト（URL、ページ番号、作成者など）を渡す場合に便利です。`file_citation` 型の各引用アノテーションには、このカスタム メタデータが含まれます。

### Python

```
interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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

## 構造化出力

Gemini 3 モデル以降では、ファイル検索ツールと
[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)を組み合わせることができます。

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
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

## サポートされているモデル

次のモデルはファイル検索をサポートしています。

| モデル | ファイル検索 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ja) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ja) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |

## サポートされているファイル形式

ファイル検索では、次のセクションに示すさまざまなファイル形式がサポートされています。

### アプリケーション ファイル形式

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

### テキスト ファイル形式

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

## 制限事項

- **Live API:** ファイル検索は
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja)ではサポートされていません。
- **ツールの非互換性:** 組み込みのグラウンディング ツールを組み合わせることはできません。
  たとえば、同じリクエストでファイル検索を [Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja) や
  [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja) と同時に使用することはできません。

### レート上限

サービスを安定させるため、ファイル検索 API には次の制限があります。

- **最大ファイルサイズ / ドキュメントあたりの上限**: 100 MB
- **プロジェクトのファイル検索ストアの合計サイズ** （ユーザー階層に基づく）:
  - **無料**: 1 GB
  - **Tier 1**: 10 GB
  - **Tier 2**: 100 GB
  - **Tier 3**: 1 TB
- **推奨事項**: 取得レイテンシを最適化するため、各ファイル検索ストアのサイズを 20 GB 未満に制限してください。

## 料金

- エンベディングの料金は、既存の
  [エンベディングの料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#gemini-embedding-2)に基づいてインデックス作成時に請求されます。
- ストレージは無料です。
- クエリ時のエンベディングは無料です。
- 取得したドキュメント トークンは、通常の
  [コンテキスト トークン](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)として課金されます。

## 次のステップ

- [ファイル検索ストア](https://ai.google.dev/api/file-search/file-search-stores?hl=ja)とファイル検索[ドキュメント](https://ai.google.dev/api/file-search/documents?hl=ja)の API リファレンスをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
