---
source_url: https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=ja
fetched_at: 2026-06-15T06:24:54.505230+00:00
title: "Gemini API \u30ad\u30fc\u3092\u4f7f\u7528\u3059\u308b \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API キーを使用する

Gemini API を使用するには、リクエストを認証する必要があります。標準 API キーまたは認可 API キーを使用して認証できます。

[Gemini API キーを作成または表示する](https://aistudio.google.com/apikey?hl=ja)

## API キーの種類: 標準と認可

API キーを使用すると Gemini API にアクセスできますが、セキュリティ特性は異なります。セキュリティを強化するため、Gemini API は標準 API キーから認可キーに移行しています。

- **標準 API キー**: 課金と割り当てを目的として、リクエストを Google Cloud プロジェクトに関連付けます。標準キーは呼び出し元を識別しないため、サポートできる権限とアクセス制御の粒度が制限されます。
- **認可（auth）キー**: Google Cloud サービス
  アカウントに直接バインドされます。認可キーを使用すると、バインドされたサービス アカウントの ID でリクエストが処理され、きめ細かいアクセス制御が可能になります。認可キーはデフォルトで Generative Language API（Gemini API）に制限されており、システムで検出された漏洩キーの使用を迅速に停止する、漏洩キーの迅速な適用を実現します。

安全な使用を確保するため、Gemini API は標準キーから認可キーに移行します。

- **認可キーがデフォルト**: Google AI Studio で作成された新しい API キーはすべて、
  認可キーとして自動的に作成されます。
- **2026 年 6 月 19 日**: Gemini API は、リクエストを拒否します
  **制限のない標準キー**から。明示的な制限が適用された標準 API キーは引き続き機能します。この制限により、一般公開されているキーや他のサービスにリンクされているキーの不正使用を防ぐことができます。
- **2026 年 9 月**: Gemini API は、**標準
  キー** からのリクエストを拒否します。サービスの停止を回避するため、この日付より前に[認可キーに移行する](#migrate-to-auth-key)
  必要があります。2026 年 9 月までに認可キーに移行してください。

## Google AI Studio で API キーを管理する

プロジェクトとキーは [Google AI Studio](https://aistudio.google.com/apikey?hl=ja) で直接管理できます。

### Google Cloud プロジェクト

すべての Gemini API キーは [Google Cloud プロジェクト](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ja) に関連付けられています。
Google Cloud プロジェクトは、課金、共同編集者、権限を管理します。Google AI Studio には、これらのプロジェクトにアクセスするための軽量インターフェースが用意されています。

- **デフォルト プロジェクト**: 新規ユーザーの場合、利用規約に同意すると、Google AI Studio によってデフォルトの Google Cloud プロジェクトと API キーが自動的に
  作成されます。このプロジェクトの名前を変更するには、ダッシュボードの [**Projects**] ビューに移動します。
- **既存のプロジェクト**: Google Cloud アカウントをすでにお持ちの場合、AI
  Studio はデフォルト プロジェクトを作成しません。代わりに、既存のプロジェクトをインポートする必要があります。

### プロジェクトをインポートする

デフォルトでは、Google AI Studio にはすべての Google Cloud プロジェクトが表示されません。使用するプロジェクトをインポートする必要があります。

1. [Google AI Studio](https://aistudio.google.com?hl=ja) に移動します。
2. 左側のパネルから [**Dashboard**] を開き、[**Projects**] を選択します。
3. [**Import projects**] ボタンをクリックします。
4. インポートする Google Cloud プロジェクトを検索して選択し、[**Import**] をクリックします。
5. インポートしたら、ダッシュボードの [**API Keys**] ページに移動して、そのプロジェクトにキーを作成します。

### キー作成権限のトラブルシューティング

If the [**Create API key**] button is unavailable and displays the message:
*"You do not have permission to create a key in this project"*, you lack the
required IAM permissions.

Google Cloud プロジェクトまたは組織の管理者に、次の権限を含むロール（プロジェクト編集者など）の付与を依頼してください。

- `resourcemanager.projects.get`: AI Studio がプロジェクトを検証できるようにします。
- `apikeys.keys.create`: キーの生成を許可します。
- `serviceusage.services.enable`: Generative Language API が有効になっていることを確認します。
- `iam.serviceAccounts.create`: リンクされたサービス アカウントを作成するために必要です。
- `iam.serviceAccountApiKeyBindings.create`: サービス アカウントを API キーにバインドします。

管理アクセス権を取得できない場合は、組織に関連付けられていない新しい Google Cloud プロジェクトを作成して、キーを生成できます。

## 環境設定

キーを取得したら、アプリケーションで安全に使用できるように環境を構成します。

### 方法 1: 環境変数を使用する（推奨）

環境変数 `GEMINI_API_KEY` または `GOOGLE_API_KEY` を設定します。Gemini API クライアント ライブラリは、これらの変数を自動的に検出して使用します。両方が設定されている場合は、`GOOGLE_API_KEY` が優先されます。

オペレーティング システムを選択して変数を設定します。

### Linux/macOS - Bash

Bash 構成ファイルがあるかどうかを確認します。

```
~/.bashrc
```

ない場合は、作成して開きます。

```
touch ~/.bashrc && open ~/.bashrc
```

ファイルの末尾に export コマンドを追加します。

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

ファイルを保存して変更を適用します。

```
source ~/.bashrc
```

### macOS - Zsh

zsh 構成ファイルがあるかどうかを確認します。

```
~/.zshrc
```

ない場合は、作成して開きます。

```
touch ~/.zshrc && open ~/.zshrc
```

export コマンドを追加します。

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

ファイルを保存して変更を適用します。

```
source ~/.zshrc
```

### Windows

1. Windows の検索バーで「環境変数」を検索します。
2. [システムのプロパティ] ダイアログで [**環境変数**] をクリックします。
3. [**ユーザー環境変数**] または [**システム環境変数**] で [**新規...**] をクリックします。
4. 変数名を `GEMINI_API_KEY` に設定し、値を API キーに設定します。
5. [**OK**] をクリックして保存します。新しいターミナル セッションを開いて変数を読み込みます。

### 方法 2: コードで API キーを明示的に指定する

クライアントの初期化時に API キーを明示的に渡すことができます。これは、環境変数を使用できない場合にのみ行ってください。

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
    "google.golang.org/genai/interactions"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction, err := client.Interactions.NewModel(ctx, interactions.NewModelParams{
        Model: "gemini-3.5-flash",
        Input: interactions.Input{
            String: "Explain how AI works in a few words",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range interaction.Steps {
        if step.ModelOutput != nil {
            for _, content := range step.ModelOutput.Content {
                if content.Text != nil {
                    fmt.Println(content.Text.Text)
                }
            }
        }
    }
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.interactions.models.interactions.CreateModelInteractionParams;
import com.google.genai.interactions.models.interactions.Interaction;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    CreateModelInteractionParams params =
        CreateModelInteractionParams.builder()
            .input("Explain how AI works in a few words")
            .model("gemini-3.5-flash")
            .build();

    Interaction interaction = client.interactions.create(params);

    interaction.steps().forEach(step -> {
      if (step.isModelOutput()) {
        step.asModelOutput().content().ifPresent(contents -> {
          contents.forEach(content -> {
            content.text().ifPresent(text -> System.out.println(text.text()));
          });
        });
      }
    });
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## セキュリティとシークレットの管理

Gemini API キーはパスワードと同様に扱います。侵害されると、プロジェクトの割り当てが消費され、予期しない請求が発生し、非公開リソースにアクセスされる可能性があります。

### 重要なセキュリティ ルール

- **キーを機密情報として保持する**: Git などのソース管理システム
  に API キーをチェックインしないでください。
- **本番環境でクライアントサイドでキーを公開しない**: ウェブアプリやモバイルアプリに API キーを
  直接ハードコードしないでください。クライアントサイドコードでコンパイルされたキーは、ユーザーが抽出できます。クライアントサイド アプリを保護するには、バックエンド プロキシ サーバーを実行して実際の API 呼び出しを行います。

### シークレット管理のベスト プラクティス

- **環境変数**: 構成ファイルではなく環境変数からキーを読み取ります。
- [**Secret Manager**: 本番環境では、Google Cloud Secret Manager などの安全なシークレット ストアにキーを保存します。](https://cloud.google.com/secret-manager?hl=ja)
- **請求アラート**: Google Cloud コンソールで請求アラートを設定して、使用量や費用が急増した場合に
  通知を受け取ります。

### 漏洩対応チェックリスト

API キーが漏洩した疑いがある場合は、次の手順を行います。

1. **新しいキーを生成する**: Google AI Studio または
   Cloud Console で代替キーを作成します。
2. **アプリケーションを更新する**: 新しいキーを使用してコードをデプロイします。
3. **侵害されたキーを無効にするか削除する**: 新しいキーが検証されたら、
   Cloud Console で漏洩したキーを無効にします。アプリケーションのダウンタイムを回避するため、新しいキーが完全に有効になるまで古いキーを削除しないでください。
4. **使用状況を監査する**: Google Cloud
   コンソールで請求ログと API 使用状況を確認して、不正なアクティビティを特定します。

## キーを制限して保護する

API キーに制限を追加すると、キーが侵害された場合の潜在的な損害を最小限に抑えることができます。

### リクエスト元の制限を適用する

オリジン制限により、キーを使用できる IP アドレス、ウェブサイト、アプリケーションが制限されます。

1. [[Google Cloud コンソール認証情報] ページに移動します。](https://console.cloud.google.com/apis/credentials?hl=ja)
2. プロジェクトを選択し、制限する API キーの名前をクリックします。
3. [**アプリケーションの制限**] で [**IP アドレス**]（または環境に適した制限タイプ）を選択します。
4. 許可する IP アドレスまたは範囲を指定して、[**保存**] をクリックします。

### 制限のない標準 API キーを保護する

2026 年 6 月 19 日以降も Gemini API を使用するには、制限のないキーを保護する必要があります。

#### 方法 A: キーを Gemini API のみに制限する（AI Studio）

Gemini API にのみキーを使用する場合は、AI Studio で直接保護します。

1. [**API Keys**] ページ（[Google AI Studio](https://aistudio.google.com/api-keys?hl=ja) 内）で、
   [**Unrestricted**] ラベルが付いたキーを見つけます。
2. ラベルにカーソルを合わせ、ダイアログで [**Add restrictions**] をクリックします。
3. [**Restrict to Gemini API only**] を選択します。
4. [**Restrict key**] をクリックして確定します。

#### 方法 B: 他のサービスのキーを制限する（Google Cloud コンソール）

キーが他の Google API と共有されている場合は（推奨されません）、Cloud Console で制限します。**注: このキーを使用する Gemini API リクエストは、これらの制限が適用されると失敗します。**

1. [[Google Cloud コンソール認証情報] ページに移動します。](https://console.cloud.google.com/apis/credentials?hl=ja)
2. プロジェクトと API キーを選択します。
3. [**API の制限**] で [**キーを制限**] を選択します。
4. プルダウンから、このキーでアクセスする API を選択します。[**Generative Language API**] は選択しないでください。
5. [**保存**] をクリックします。Gemini API を引き続き使用するには、AI Studio で別の制限付きキーを作成します。

### ブロックされた休止中のキー

2026 年 5 月 7 日より、Gemini API は長期間休止している制限のない API キーをブロックします。これらのキーには、AI Studio に [**Blocked**] タグが表示されます。続行するには、新しいキーを生成するか、既存の制限付きキーを使用する必要があります。

## 認可キーに移行する

新しい認可 API キーを作成してアプリケーションを更新する手順は次のとおりです。

1. [[AI Studio API Keys] ページに移動します。](https://aistudio.google.com/api-keys?hl=ja)
2. [**Key Type**] 列で、[**Standard**] と表示されているキーを確認します。
3. [**Create API key**] をクリックして新しいキーを生成します。AI Studio で作成された新しいキーはすべて、認可キーとして自動的に作成されます。
4. 新しい認可 API キーをコピーします。
5. 新しい認可 API キーを使用するように、アプリケーション コード、環境変数、デプロイ構成を更新します。
6. アプリケーションをテストして、新しいキーで正しく動作することを確認します。
7. 確認したら、古いトラフィック キーを削除または取り消して、不正使用を防ぎます。

## 制限事項

Google AI Studio には、プロジェクトとキーの管理に関する次の制限があります。

- Google AI Studio の [**Projects**] ページから一度に作成できるプロジェクトは最大 10 個です。
- [**API keys**] ページと [**Projects**] ページには、最大 100 個のキーと 50 個のプロジェクトが表示されます。
- 制限のない API キー、または Generative Language API（Gemini API）にのみ制限されている API キーのみが表示されます。

高度なプロジェクト管理を行う場合や、他の制限があるキーを変更する場合は、
[[Google Cloud コンソールの認証情報ページ](https://console.cloud.google.com/apis/credentials?hl=ja)]を使用します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-11 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-11 UTC。"],[],[]]
