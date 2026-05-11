---
source_url: https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=ja
fetched_at: 2026-05-11T12:35:22.948165+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API キーを使用する

Gemini API を使用するには、API キーが必要です。このページでは、Google AI Studio でキーを作成して管理する方法と、コードで使用するための環境を設定する方法について説明します。

[Gemini API キーを作成または表示する](https://aistudio.google.com/app/apikey?hl=ja)

## API キー

[Google AI Studio](https://aistudio.google.com/app/apikey?hl=ja) の **API キー**ページで、すべての Gemini API キーを作成して管理できます。

API キーを取得したら、次のオプションを使用して Gemini API に接続できます。

- [API キーを環境変数として設定する](#set-api-env-var)
- [API キーを明示的に指定する](#provide-api-key-explicitly)

初期テストでは API キーをハードコードできますが、これは安全ではなく、一時的なものにすぎません。API キーをハードコードする例については、[API キーを明示的に指定する](#provide-api-key-explicitly)をご覧ください。

## Google Cloud プロジェクト

[Google Cloud プロジェクト](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ja)は、Google Cloud サービス（Gemini API など）の使用、課金の管理、共同編集者と権限の制御に不可欠です。Google AI Studio は、Google Cloud プロジェクトへの軽量インターフェースを提供します。

まだプロジェクトを作成していない場合は、新しいプロジェクトを作成するか、Google Cloud から Google AI Studio にプロジェクトをインポートする必要があります。Google AI Studio の [**プロジェクト**] ページには、Gemini API を使用するのに十分な権限を持つすべてのキーが表示されます。手順については、[プロジェクトをインポートする](#import-projects)セクションをご覧ください。

### デフォルトのプロジェクト

初めてご利用になる場合は、利用規約に同意すると、Google AI Studio によってデフォルトの Google Cloud プロジェクトと API キーが作成され、すぐに使用を開始できます。このプロジェクトの名前を変更するには、Google AI Studio の**ダッシュボード**の [**プロジェクト**] ビューに移動し、プロジェクトの横にある 3 つのドットの設定ボタンをクリックして、[**プロジェクトの名前を変更**] を選択します。既存のユーザー、またはすでに Google Cloud アカウントをお持ちのユーザーには、デフォルト プロジェクトは作成されません。

## プロジェクトをインポートする

Gemini API キーはそれぞれ Google Cloud プロジェクトに関連付けられています。デフォルトでは、Google AI Studio にすべての Cloud プロジェクトが表示されるわけではありません。必要なプロジェクトは、[**プロジェクトのインポート**] ダイアログで名前またはプロジェクト ID を検索してインポートする必要があります。アクセス権のあるプロジェクトの一覧を表示するには、Cloud Console にアクセスします。

まだプロジェクトをインポートしていない場合は、次の手順で Google Cloud プロジェクトをインポートして鍵を作成します。

1. [Google AI Studio](https://aistudio.google.com?hl=ja) に移動します。
2. 左側のサイドパネルから [**ダッシュボード**] を開きます。
3. [**プロジェクト**] を選択します。
4. [**プロジェクト**] ページで [**プロジェクトをインポート**] ボタンを選択します。
5. インポートする Google Cloud プロジェクトを検索して選択し、[**インポート**] ボタンを選択します。

プロジェクトをインポートしたら、**ダッシュボード** メニューから **API キー**ページに移動し、インポートしたプロジェクトで API キーを作成します。

## 制限事項

Google AI Studio での API キーと Google Cloud プロジェクトの管理には、次の制限があります。

- Google AI Studio の [**プロジェクト**] ページから、一度に最大 10 個のプロジェクトを作成できます。
- プロジェクトと鍵の名前を設定したり、変更したりできます。
- [**API キー**] ページと [**プロジェクト**] ページには、最大 100 個のキーと 50 個のプロジェクトが表示されます。
- 制限がない API キー、または Generative Language API に制限されている API キーのみが表示されます。

API キーの変更や制限など、プロジェクトへの追加の管理アクセスについては、[Google Cloud コンソールの認証情報ページ](https://console.cloud.google.com/apis/credentials?hl=ja)をご覧ください。Cloud コンソールで、プロジェクトを選択し、既存の API キーをクリックして、**Generative Language API** に制限できます。

## API キーを環境変数として設定する

環境変数 `GEMINI_API_KEY` または `GOOGLE_API_KEY` を設定すると、[Gemini API ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)のいずれかを使用するときに、API キーがクライアントによって自動的に取得されます。これらの変数のいずれか 1 つのみを設定することをおすすめしますが、両方が設定されている場合は `GOOGLE_API_KEY` が優先されます。

REST API またはブラウザの JavaScript を使用している場合は、API キーを明示的に指定する必要があります。

さまざまなオペレーティング システムで API キーをローカルで環境変数 `GEMINI_API_KEY` として設定する方法は次のとおりです。

### Linux/macOS - Bash

Bash は、Linux と macOS の一般的なターミナル構成です。次のコマンドを実行すると、構成ファイルがあるかどうかを確認できます。

```
~/.bashrc
```

「No such file or directory」という応答が返された場合は、次のコマンドを実行してこのファイルを作成して開くか、`zsh` を使用する必要があります。

```
touch ~/.bashrc
open ~/.bashrc
```

次に、次のエクスポート コマンドを追加して API キーを設定する必要があります。

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

ファイルを保存したら、次のコマンドを実行して変更を適用します。

```
source ~/.bashrc
```

### macOS - Zsh

Zsh は、Linux と macOS で一般的なターミナル構成です。次のコマンドを実行すると、構成ファイルがあるかどうかを確認できます。

```
~/.zshrc
```

「No such file or directory」という応答が返された場合は、次のコマンドを実行してこのファイルを作成して開くか、`bash` を使用する必要があります。

```
touch ~/.zshrc
open ~/.zshrc
```

次に、次のエクスポート コマンドを追加して API キーを設定する必要があります。

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

ファイルを保存したら、次のコマンドを実行して変更を適用します。

```
source ~/.zshrc
```

### Windows

1. 検索バーで「環境変数」を検索します。
2. [**システム設定**] を変更します。この操作を行うことを確認するメッセージが表示されることがあります。
3. [システム設定] ダイアログで、[**環境変数**] というラベルのボタンをクリックします。
4. [**ユーザー環境変数**]（現在のユーザーの場合）または [**システム環境変数**]（マシンを使用するすべてのユーザーに適用）のいずれかで、[**新規...**] をクリックします。
5. 変数名を `GEMINI_API_KEY` として指定します。Gemini API キーを変数値として指定します。
6. [**OK**] をクリックして変更を適用します。
7. 新しいターミナル セッション（cmd または Powershell）を開いて、新しい変数を確認します。

## API キーを明示的に指定する

場合によっては、API キーを明示的に指定する必要があります。次に例を示します。

- 単純な API 呼び出しを行っており、API キーをハードコードすることを希望している。
- Gemini API ライブラリによる環境変数の自動検出に依存せずに、明示的な制御を行いたい
- 環境変数がサポートされていない環境（ウェブなど）を使用しているか、REST 呼び出しを行っている。

以下に、Interactions API を使用して API キーを明示的に指定する方法の例を示します。

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3-flash-preview", 
    input="Explain how AI works in a few words"
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works in a few words"
  }'
```

## API キーを安全に保護する

Gemini API キーはパスワードと同様に扱ってください。漏洩した場合、他のユーザーがプロジェクトの割り当てを使用したり、料金が発生したり（課金が有効になっている場合）、ファイルなどのプライベート データにアクセスしたりする可能性があります。

### 重大なセキュリティ ルール

- **キーの機密性を維持する**: Gemini の API キーは、アプリケーションが依存するセンシティブ データにアクセスする可能性があります。

  - **API キーをソース コントロールに commit しないでください。**API キーを Git などのバージョン管理システムにチェックインしないでください。
  - **クライアントサイドで API キーを公開しないでください。**本番環境のウェブアプリやモバイルアプリで API キーを直接使用しないでください。クライアントサイド コード（JavaScript/TypeScript ライブラリや REST 呼び出しなど）のキーは抽出できます。
- **アクセスを制限する**: 可能であれば、API キーの使用を特定の IP アドレス、HTTP リファラー、Android/iOS アプリに制限します。
- **使用を制限する**: 各キーに必要な API のみを有効にします。
- **定期的な監査を実施する**: API キーを定期的に監査し、定期的にローテーションします。

### ベスト プラクティス

- **API キーを使用してサーバーサイド呼び出しを行う**: API キーを使用する最も安全な方法は、キーを機密情報として保持できるサーバーサイド アプリケーションから Gemini API を呼び出すことです。
- **クライアントサイド アクセスにエフェメラル トークンを使用する（Live API のみ）:** Live API に直接クライアントサイド アクセスする場合は、エフェメラル トークンを使用できます。セキュリティ リスクが低く、本番環境での使用に適しています。詳しくは、[エフェメラル トークン](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ja)のガイドをご覧ください。
- **キーに制限を追加することを検討する:** [API キー制限](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=ja#add-api-restrictions)を追加することで、キーの権限を制限できます。これにより、鍵が漏洩した場合の潜在的な被害を最小限に抑えることができます。

一般的なベスト プラクティスについては、こちらの[サポート記事](https://support.google.com/googleapi/answer/6310037?hl=ja)もご覧ください。

## API キーの作成に関するトラブルシューティング

Google AI Studio で、[**API キーを作成**] ボタンが使用できない状態になり、「*このプロジェクトでキーを作成する権限がありません*」というメッセージが表示されることがあります。

これは、新しい鍵を生成するために必要な権限がプロジェクト内にない場合に発生します。

- **`resourcemanager.projects.get`**: AI Studio がプロジェクトの存在を確認できるようにします。
- **`apikeys.keys.create`**: API キー自体の生成を許可します。
- **`serviceusage.services.enable`**: プロジェクトで Gemini API が有効になっていることを確認するために必要です。

権限を修正するには、プロジェクト管理者に依頼して、上記の権限（プロジェクト編集者やカスタムロールなど）を持つロールを付与してもらいます。プロジェクトが[組織](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=ja)に属している場合は、組織の管理者に依頼します。

プロジェクトに対する管理者権限がない場合は、組織に関連付けられていない新しいプロジェクトを作成して、キーを生成できます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-07 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-07 UTC。"],[],[]]
