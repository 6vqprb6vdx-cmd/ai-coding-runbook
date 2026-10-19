---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-input-methods?hl=ja
fetched_at: 2026-10-19T05:46:17.315640+00:00
title: "\u30d5\u30a1\u30a4\u30eb\u5165\u529b\u30e1\u30bd\u30c3\u30c9 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# ファイル入力メソッド

このガイドでは、Gemini API にリクエストを行う際に、画像、音声、動画、ドキュメントなどのメディア ファイルを含めるさまざまな方法について説明します。新しいメソッドは、Batch API、Interactions API、Live API など、すべての Gemini API エンドポイントでサポートされています。適切な方法を選択するには、ファイルのサイズ、データの現在の保存場所、ファイルの使用頻度を考慮する必要があります。

ファイルを入力として含める最も簡単な方法は、ローカル ファイルを読み取ってプロンプトに含めることです。次の例は、ローカルの PDF ファイルを読み取る方法を示しています。このメソッドでは、PDF は 50 MB に制限されています。ファイル入力の種類と上限の完全なリストについては、[入力方法の比較表](#method-comparison)をご覧ください。

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const ai = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = path.join('content', 'my_local_file.pdf'); // Adjust path as needed

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: fs.readFileSync(filePath).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.8-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Summarize this document"}
        ]
      },
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "application/pdf",
              "data": "'"${B64_CONTENT}"'"
            }
          }
        ]
      }
    ]
  }'
```

## 入力方法の比較

次の表は、各入力方法とファイルの上限、最適なユースケースを比較したものです。ファイルサイズの制限は、ファイルの種類と、ファイルの処理に使用されるモデル/トークナイザーによって異なる場合があります。

| メソッド | 最適な用途 | 最大ファイルサイズ | 永続性 |
| --- | --- | --- | --- |
| **インライン データ** | 迅速なテスト、小規模なファイル、リアルタイム アプリケーション。 | リクエスト/ペイロードあたり 100 MB  （**PDF の場合は 50 MB**） | なし（すべてのリクエストで送信） |
| **File API アップロード** | 大きなファイル、複数回使用されるファイル。 | ファイルあたり 2 GB、  プロジェクトあたり最大 20 GB | 48 時間 |
| **File API GCS URI の登録** | Google Cloud Storage にすでに保存されている大きなファイル、複数回使用されるファイル。 | 1 ファイルあたり 2 GB、保存容量の上限なし | なし（リクエストごとに取得）。1 回の登録で最大 30 日間アクセスできます。 |
| **外部 URL** | パブリック データまたはクラウド バケット（AWS、Azure、GCS）内のデータを再アップロードせずに使用できます。 | 1 ファイルあたり 15 MB | なし（リクエストごとに取得） |

## インライン データ

小さいファイル（100 MB 未満、PDF の場合は 50 MB）の場合は、リクエスト ペイロードでデータを直接渡すことができます。これは、リアルタイムの一時データを処理するクイック テストやアプリケーションに最適な最も簡単な方法です。データは、Base64 でエンコードされた文字列として提供するか、ローカル ファイルを直接読み取って提供できます。

ローカル ファイルから読み取る例については、このページの冒頭の例をご覧ください。

### URL から取得する

URL からファイルを取得し、バイトに変換して入力に含めることもできます。

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=[
      types.Part.from_bytes(
        data=doc_data,
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.8-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Gemini File API

File API は、大きなファイル（最大 2 GB）や複数のリクエストで使用するファイルを対象としています。

### 標準のファイル アップロード

ローカル ファイルを Gemini API にアップロードします。この方法でアップロードされたファイルは一時的に（48 時間）保存され、モデルによる効率的な取得のために処理されます。

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[prompt, audio_file]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const prompt = "Describe this audio clip";

async function main() {
  const filePath = "path/to/your/sample.mp3"; // Adjust path as needed

  const myfile = await ai.files.upload({
    file: filePath,
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(myfile.uri, myfile.mimeType),
    ]),
  });
  console.log(response.text);

}
await main();
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

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

### Google Cloud Storage ファイルを登録する

データがすでに Google Cloud Storage にある場合は、ダウンロードして再アップロードする必要はありません。File API に直接登録できます。

1. 各バケットへの **サービス エージェント** アクセス権を付与する

   1. Google Cloud プロジェクトで Gemini API を有効にします。
   2. サービス エージェントを作成します。

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. ストレージ バケットを読み取るための **Gemini API サービス エージェントの権限を付与**します。

      ユーザーは、使用する特定のストレージ バケットで、このサービス エージェントに `Storage Object Viewer`
      [IAM ロール](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=ja#storage.objectViewer)を割り当てる必要があります。

   このアクセス権はデフォルトでは期限切れになりませんが、いつでも変更できます。[Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=ja) コマンドを使用して権限を付与することもできます。
2. サービスを認証する

   **前提条件**

   - API を有効にする
   - 適切な権限が付与されたサービス アカウント/エージェントを作成します。

   まず、ストレージ オブジェクト閲覧者の権限を持つサービスとして認証する必要があります。この処理は、ファイル管理コードが実行される環境によって異なります。

   **Google Cloud の外部**

   コードが Google Cloud の外部（デスクトップなど）から実行されている場合は、次の手順で Google Cloud コンソールからアカウント認証情報をダウンロードします。

   1. [サービス アカウント コンソール](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=ja)に移動します。
   2. 関連するサービス アカウントを選択する
   3. [**鍵**] タブを選択し、[**鍵を追加、新しい鍵を作成**] を選択します。
   4. 鍵のタイプとして [**JSON**] を選択し、ファイルがマシン上のどこにダウンロードされたかを確認します。

   詳細については、[サービス アカウント キーの管理](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=ja)に関する Google Cloud の公式ドキュメントをご覧ください。

   次に、次のコマンドを使用して認証します。これらのコマンドは、サービス アカウント ファイルが現在のディレクトリにあり、名前が `service-account.json` であることを前提としています。

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **Google Cloud**

   [Cloud Run 関数](https://cloud.google.com/functions?hl=ja)や [Compute Engine インスタンス](https://cloud.google.com/products/compute?hl=ja)を使用して Google Cloud で直接実行している場合は、暗黙的な認証情報がありますが、適切なスコープを付与するために再認証する必要があります。

   ### Python

   このコードは、Cloud Run や Compute Engine など、[アプリケーションのデフォルト認証情報](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ja)を自動的に取得できる環境でサービスが実行されていることを想定しています。

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   このコードは、Cloud Run や Compute Engine など、[アプリケーションのデフォルト認証情報](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=ja)を自動的に取得できる環境でサービスが実行されていることを想定しています。

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   これはインタラクティブなコマンドです。Compute Engine などのサービスでは、構成レベルで実行中のサービスにスコープを関連付けることができます。例については、[ユーザー管理サービスに関するドキュメント](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=ja#using)をご覧ください。

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. ファイル登録（Files API）

   Files API を使用してファイルを登録し、Gemini API で直接使用できる Files API パスを生成します。

   ### Python

   ```
   from google import genai
   from google.genai.types import Part

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client()

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"],
       # Use the credentials obtained in the previous step.
       auth=credentials
   )
   prompt = "Summarize this file."

   # call generateContent for each file
   for f in registered_gcs_files.files:
     print(f.name)
     response = client.models.generate_content(
       model="gemini-3.8-flash",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
   ```

   ### CLI

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## 外部 HTTP / 署名付き URL

一般公開されている HTTPS URL または事前署名付き URL（[S3 事前署名付き URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) および Azure SAS と互換性あり）は、生成リクエストで直接渡すことができます。Gemini API は、処理中にコンテンツを安全に取得します。これは、再アップロードしたくないファイルに最適です。各ファイルの最大サイズは 15 MB です。大きなファイルの場合は、[File API](#file-api) を使用します。

`file_uri` フィールドの URL を使用して、公開 URL または署名付き URL を入力として使用できます。

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        Part.from_uri(
            file_uri=uri,
            mime_type="application/pdf",
        ),
        prompt
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3.8-flash',
    contents: [
      // equivalent to Part.from_uri(file_uri=uri, mime_type="...")
      createPartFromUri(uri, "application/pdf"),
      "summarize this file",
    ],
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "contents":[
            {
              "parts":[
                {"text": "Summarize this pdf"},
                {
                  "file_data": {
                    "mime_type":"application/pdf",
                    "file_uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
                  }
                }
              ]
            }
          ]
        }'
```

### ユーザー補助

指定した URL が、ログインが必要なページや有料コンテンツのページにリンクしていないことを確認します。非公開データベースの場合は、適切なアクセス権限と有効期限で署名付き URL を作成してください。

### 安全チェック

システムは、URL が安全基準とポリシー基準（オプトアウトされていないコンテンツやペイウォールで保護されたコンテンツなど）を満たしていることを確認するため、URL に対してコンテンツ モデレーション チェックを実行します。指定した URL がこのチェックに失敗すると、`url_retrieval_status` は `URL_RETRIEVAL_STATUS_UNSAFE` になります。

### サポートされているコンテンツの種類

サポートされているファイル形式と制限事項のこのリストは、初期のガイダンスとして提供されるものであり、包括的なものではありません。サポートされている型の有効なセットは変更される可能性があり、使用中の特定のモデルとトークナイザーのバージョンによって異なる場合があります。サポートされていない型を使用すると、エラーが発生します。また、これらのファイル形式のコンテンツ取得は、現在一般公開されている URL のみをサポートしています。

#### テキスト ファイルの種類

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### アプリケーション ファイル形式

- `application/json`
- `application/pdf`

#### 画像ファイル形式

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### 動画ファイル形式

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## ベスト プラクティス

- **適切な方法を選択する:** 小さな一時ファイルにはインライン データを使用します。サイズが大きいファイルや頻繁に使用するファイルには、File API を使用します。すでにオンラインでホストされているデータには、外部 URL を使用します。
- **MIME タイプを指定する:** ファイルデータを正しく処理するために、常に正しい MIME タイプを指定します。
- **エラーを処理する:** ネットワーク障害、ファイル アクセスの問題、API エラーなどの潜在的な問題を管理するために、コードにエラー処理を実装します。
- **GCS 権限を管理する:** GCS 登録を使用する場合は、Gemini API サービス エージェントに特定のバケットに対する必要な `Storage Object Viewer` ロールのみを付与します。
- **署名付き URL のセキュリティ:** 署名付き URL に適切な有効期限と制限付きの権限が設定されていることを確認します。

## 制限事項

- ファイルサイズの上限は、メソッド（[比較表](#method-comparison)を参照）とファイル形式によって異なります。
- インライン データはリクエスト ペイロード サイズを増やします。
- File API のアップロードは一時的なもので、48 時間後に期限切れになります。
- 外部 URL の取得は、ファイルあたり 15 MB に制限され、特定のコンテンツ タイプがサポートされます。
- Google Cloud Storage の登録には、適切な IAM 設定と OAuth トークン管理が必要です。

## 次のステップ

- [Google AI Studio](http://aistudio.google.com/?hl=ja) を使用して、独自のマルチモーダル プロンプトを作成してみてください。
- プロンプトにファイルを含める方法については、[Vision](https://ai.google.dev/gemini-api/docs/vision?hl=ja)、[音声](https://ai.google.dev/gemini-api/docs/audio?hl=ja)、[ドキュメント処理](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja)のガイドをご覧ください。
- サンプリング パラメータのチューニングなど、プロンプト設計に関するガイダンスについては、[プロンプト戦略](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)ガイドをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-07 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-07 UTC。"],[],[]]
