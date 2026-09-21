---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=ja
fetched_at: 2026-09-21T05:43:02.591502+00:00
title: "Gemini API \u30ad\u30fc\u3092\u4f7f\u7528\u3059\u308b \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API キーを使用する

Gemini API を使用するには、リクエストを認証する必要があります。認証には、標準または認可 API キーを使用できます。

[Gemini API キーを作成または表示する](https://aistudio.google.com/apikey?hl=ja)

## API キーのタイプ: 標準と認可

API キーは Gemini API へのアクセスを提供しますが、セキュリティ特性は異なります。Gemini API は、セキュリティを強化するために標準 API キーから認可キーに移行しています。

- **標準 API キー**: 課金と割り当てを目的として、リクエストを Google Cloud プロジェクトに関連付けます。標準キーは呼び出し元を識別しないため、サポートできる権限とアクセス制御の粒度が制限されます。
- **認可（auth）キー**: Google Cloud サービス アカウントに直接バインドされます。認可キーを使用すると、リクエストはバインドされたサービス アカウントの ID で処理され、きめ細かいアクセス制御が可能になります。認証キーはデフォルトで Generative Language API（Gemini API）に制限されており、漏洩したキーの迅速な適用により、Google のシステムで検出された漏洩したキーの使用を迅速に停止します。

安全な使用を確保するため、Gemini API は標準キーから認証キーに移行します。

- **認証キーのデフォルト**: 2026 年 5 月 28 日以降、Google AI Studio で作成されたすべての新しい API キーは、認証キーとして自動的に作成されます。
- **制限のないキーが拒否された**: Gemini API は、**制限のない標準キー**からのリクエストを拒否します。明示的な制限が適用されている標準 API キーは引き続き機能します。この制限により、一般公開されている可能性のあるキーや、他のサービスにリンクされている可能性のあるキーの不正使用を防ぐことができます。
- **2026 年 9 月**: Gemini API は**標準キー**からのリクエストを拒否します。サービスの中断を避けるため、この日付より前に[認証キーに移行](#migrate-to-auth-key)する必要があります。2026 年 9 月までに認証鍵に移行してください。

## Google AI Studio で API キーを管理する

プロジェクトとキーは [Google AI Studio](https://aistudio.google.com/apikey?hl=ja) で直接管理できます。

### Google Cloud プロジェクト

すべての Gemini API キーは [Google Cloud プロジェクト](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ja)に関連付けられています。Google Cloud プロジェクトでは、課金、共同編集者、権限を管理します。Google AI Studio には、これらのプロジェクトにアクセスするための軽量インターフェースが用意されています。

- **デフォルト プロジェクト**: 新規ユーザーの場合は、利用規約に同意すると、Google AI Studio によってデフォルトの Google Cloud プロジェクトと API キーが自動的に作成されます。このプロジェクトの名前を変更するには、ダッシュボードの [**プロジェクト**] ビューに移動します。
- **既存のプロジェクト**: Google Cloud アカウントをすでに所有している場合、AI Studio はデフォルト プロジェクトを作成しません。代わりに、既存のプロジェクトをインポートする必要があります。

### プロジェクトのインポート

デフォルトでは、Google AI Studio にすべての Google Cloud プロジェクトが表示されるわけではありません。使用するプロジェクトをインポートする必要があります。

1. [Google AI Studio](https://aistudio.google.com?hl=ja) に移動します。
2. 左側のパネルから [**Dashboard**] を開き、[**Projects**] を選択します。
3. [**プロジェクトをインポート**] ボタンをクリックします。
4. インポートする Google Cloud プロジェクトを検索して選択し、[**インポート**] をクリックします。
5. インポートしたら、ダッシュボードの [**API キー**] ページに移動して、そのプロジェクトにキーを作成します。

### 鍵の作成権限のトラブルシューティング

[**API キーを作成**] ボタンが使用できず、「このプロジェクトでキーを作成する権限がありません」というメッセージが表示される場合は、必要な IAM 権限がありません。

Google Cloud プロジェクトまたは組織の管理者に、次の権限を含むロール（プロジェクト編集者など）の付与を依頼します。

- `resourcemanager.projects.get`: AI Studio がプロジェクトを検証できるようにします。
- `apikeys.keys.create`: 鍵の生成を許可します。
- `serviceusage.services.enable`: Generative Language API が有効になっていることを確認します。
- `iam.serviceAccounts.create`: リンクされたサービス アカウントの作成に必要です。
- `iam.serviceAccountApiKeyBindings.create`: サービス アカウントを API キーにバインドします。

管理者権限を取得できない場合は、組織に関連付けられていない新しい Google Cloud プロジェクトを作成して、鍵を生成できます。

## 環境設定

キーを取得したら、アプリケーションで安全に使用できるように環境を構成します。

### オプション 1: 環境変数を使用する（推奨）

環境変数 `GEMINI_API_KEY` または `GOOGLE_API_KEY` を設定します。Gemini API クライアント ライブラリは、これらの変数を自動的に検出して使用します。両方を設定した場合は、`GOOGLE_API_KEY` が優先されます。

オペレーティング システムを選択して変数を設定します。

### Linux/macOS - Bash

bash 構成ファイルがあるかどうかを確認します。

```
~/.bashrc
```

存在しない場合は、作成して開きます。

```
touch ~/.bashrc && open ~/.bashrc
```

ファイルの末尾にエクスポート コマンドを追加します。

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

ファイルを保存し、変更を適用します。

```
source ~/.bashrc
```

### macOS - Zsh

zsh 構成ファイルがあるかどうかを確認します。

```
~/.zshrc
```

存在しない場合は、作成して開きます。

```
touch ~/.zshrc && open ~/.zshrc
```

エクスポート コマンドを追加します。

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

ファイルを保存し、変更を適用します。

```
source ~/.zshrc
```

### Windows

1. Windows の検索バーで「環境変数」を検索します。
2. [システムのプロパティ] ダイアログで [**環境変数**] をクリックします。
3. [**ユーザー環境変数**] または [**システム環境変数**] で [**新規...**] をクリックします。
4. 変数名を `GEMINI_API_KEY` に設定し、値を API キーに設定します。
5. [**OK**] をクリックして保存します。新しいターミナル セッションを開いて変数を読み込みます。

### オプション 2: コードで API キーを明示的に指定する

クライアントを初期化するときに、API キーを明示的に渡すことができます。環境変数を使用できない場合にのみ、これを行います。

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = Client.builder().apiKey("YOUR_API_KEY").build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few sentences."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## セキュリティとシークレットの管理

Gemini API キーはパスワードと同様に扱ってください。不正使用されると、他のユーザーがプロジェクトの割り当てを消費し、予期しない請求が発生し、プライベート リソースにアクセスする可能性があります。

### 重大なセキュリティ ルール

- **キーを機密情報として扱う**: API キーを Git などのソース コントロール システムにチェックインしないでください。
- **本番環境でクライアントサイドの鍵を公開しない**: ウェブアプリやモバイルアプリに API キーを直接ハードコードしないでください。クライアントサイド コードにコンパイルされたキーは、ユーザーが抽出できます。クライアントサイド アプリを保護するには、バックエンド プロキシ サーバーを実行して実際の API 呼び出しを行います。

### シークレット管理のベスト プラクティス

- **環境変数**: 構成ファイルではなく環境変数からキーを読み取ります。
- **Secret Manager**: 本番環境では、[Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=ja) などの安全なシークレット ストアに鍵を保存します。
- **課金アラート**: Google Cloud コンソールで課金アラートを設定して、使用量や費用が急増した場合に通知を受け取ります。

### リーク対応チェックリスト

API キーが漏洩した疑いがある場合:

1. **新しい鍵を生成する**: Google AI Studio または Cloud コンソールで代替鍵を作成します。
2. **アプリケーションを更新する**: 新しいキーを使用してコードをデプロイします。
3. **不正使用された鍵を無効にするか削除する**: 新しい鍵が確認されたら、Cloud Console で漏洩した鍵を無効にします。アプリケーションのダウンタイムを回避するため、新しいキーが完全に有効になるまで古いキーを削除しないでください。
4. **使用状況の監査**: Google Cloud コンソールで請求ログと API 使用状況を確認して、不正なアクティビティを特定します。

## キーの制限と保護

API キーに制限を追加すると、キーが不正使用された場合の影響を最小限に抑えることができます。

### リクエストのオリジン制限を適用する

オリジンの制限は、キーを使用できる IP アドレス、ウェブサイト、アプリケーションを制限します。

1. [Google Cloud コンソールの [認証情報] ページ](https://console.cloud.google.com/apis/credentials?hl=ja)に移動します。
2. プロジェクトを選択し、制限する API キーの名前をクリックします。
3. [**アプリケーションの制限**] で、[**IP アドレス**]（または環境に適した制限タイプ）を選択します。
4. 許可する IP アドレスまたは範囲を指定して、[**保存**] をクリックします。

### 制限のない標準 API キーを保護する

Gemini API を引き続き使用するには、制限のないキーを保護する必要があります。

#### 方法 A: キーを Gemini API のみに制限する（AI Studio）

Gemini API にのみキーを使用する場合は、AI Studio で直接保護します。

1. [Google AI Studio](https://aistudio.google.com/api-keys?hl=ja) の [**API キー**] ページで、[**制限なし**] ラベルが付いているキーを探します。
2. ラベルにカーソルを合わせ、ダイアログで [**制限を追加**] をクリックします。
3. [**Gemini API のみに制限**] を選択します。
4. [**キーを制限**] をクリックして確定します。

#### 方法 B: 他のサービスのキーを制限する（Google Cloud コンソール）

キーが他の Google API と共有されている場合は（推奨されません）、Cloud コンソールで制限します。**注: これらの制限が適用されると、このキーを使用する Gemini API リクエストは失敗します。**

1. [Google Cloud コンソールの [認証情報] ページ](https://console.cloud.google.com/apis/credentials?hl=ja)に移動します。
2. プロジェクトと API キーを選択します。
3. [**API の制限**] で、[**API の制限を選択**] プルダウンを使用して、このキーでアクセスする API を選択します。[**Generative Language API**] は選択しないでください。
4. [**保存**] をクリックします。Gemini API を引き続き使用するには、AI Studio で制限付きの個別のキーを作成します。

### 休眠中のキーをブロックする

2026 年 5 月 7 日より、Gemini API は長期間使用されていない制限のない API キーをブロックします。これらのキーは、AI Studio で [**ブロック済み**] タグを表示します。続行するには、新しい鍵を生成するか、既存の制限付き鍵を使用する必要があります。

## 認証キーに移行する

新しい認証 API キーを作成してアプリケーションを更新する手順は次のとおりです。

1. [AI Studio の [API キー] ページ](https://aistudio.google.com/api-keys?hl=ja)に移動します。
2. [**Key Type**] 列で、[**Standard**] と表示されているキーを確認します。
3. [**API キーを作成**] をクリックして、新しいキーを生成します。AI Studio で作成された新しいキーはすべて、認証キーとして自動的に作成されます。
4. 新しい認証 API キーをコピーします。
5. 新しい認証 API キーを使用するように、アプリケーション コード、環境変数、デプロイ構成を更新します。
6. アプリケーションをテストして、新しいキーで正しく動作することを確認します。
7. 確認が済んだら、古いトラフィック キーを削除または取り消して、不正使用を防ぎます。

## 制限事項

Google AI Studio には、プロジェクトとキーの管理に関する次の制限があります。

- Google AI Studio の [**プロジェクト**] ページから、一度に最大 10 個のプロジェクトを作成できます。
- [**API キー**] ページと [**プロジェクト**] ページには、最大 100 個のキーと 50 個のプロジェクトが表示されます。
- 制限がない API キー、または Generative Language API（Gemini API）に特に制限されている API キーのみが表示されます。

高度なプロジェクト管理を行う場合や、他の制限付きで鍵を変更する場合は、[Google Cloud コンソールの [認証情報] ページ](https://console.cloud.google.com/apis/credentials?hl=ja)を使用します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-17 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-17 UTC。"],[],[]]
