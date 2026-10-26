---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ja
fetched_at: 2026-10-26T05:53:56.246341+00:00
title: "\u30c8\u30e9\u30d6\u30eb\u30b7\u30e5\u30fc\u30c6\u30a3\u30f3\u30b0 \u30ac\u30a4\u30c9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# トラブルシューティング ガイド

このガイドでは、Gemini API の呼び出し時に発生する一般的な問題の診断と解決に役立つ情報を説明します。Gemini API バックエンド サービスまたはクライアント SDK で問題が発生することがあります。クライアント SDK は、次のリポジトリでオープンソース化されています。

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

API キーの問題が発生した場合は、[API キーの設定ガイド](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)に沿って API キーが正しく設定されていることを確認してください。

## エラーコード

HTTP ステータス コード、生成ブロックコード、コンテンツ エラーコードなど、すべてのエラーコードの完全なリファレンスについては、[API エラー](https://ai.google.dev/gemini-api/docs/api-errors?hl=ja)のページをご覧ください。

## 再試行方法

リクエストを再試行する必要があることを示すエラー（`429 RESOURCE_EXHAUSTED` や `503 UNAVAILABLE` など）を受け取った場合は、指数バックオフ戦略を実装することをおすすめします。つまり、最初の再試行の前に少し待機し、その後、再試行間の待機時間を徐々に増やしていきます。

Gemini API の公式クライアント SDK（[Python SDK](https://github.com/googleapis/python-genai) など）には、タイムアウト、ネットワークの問題、レート制限（`429` ステータス コードと `5xx` ステータス コード）などの一時的なエラーを処理するために、デフォルトで指数バックオフを使用した自動再試行ロジックが含まれています。たとえば、Python SDK は、一時的なエラーを最大 4 回自動的に再試行します。最初の遅延は約 1 秒で、最大遅延は 60 秒です。

REST API リクエストを直接作成する場合や、再試行ロジックをカスタマイズする場合は、次のベスト プラクティスに沿って、リクエストが成功する可能性を高め、サービスに過剰な負荷がかからないようにします。

- **指数バックオフを使用する:** 最初の再試行の前に短い時間（1 秒など）待機し、その後、遅延を指数関数的に増やします（2 秒、4 秒、8 秒など）。
- **ジッターを追加する:** 遅延にランダムな「ジッター」を追加して、すべてのクライアントが同時に再試行しないようにします。
- **特定のエラーで再試行する:** 一時的なエラー（`429`、`408`、`5xx` など）でのみ再試行します。クライアント エラー（`400`、`402`、`403` など）では再試行しないでください。これらのエラーは、API キーが無効である、前払いクレジットが不足している、構文が正しくないなどの問題を示しています。
- **最大再試行回数を設定する:** 無限ループを回避するために、再試行の最大回数を定義します。

## API 呼び出しでモデル パラメータのエラーを確認する

モデル パラメータが次の値の範囲内であることを確認します。

|  |  |
| --- | --- |
| **モデル パラメータ** | **値（範囲）** |
| 候補数 | 1 ～ 8（整数） |
| 温度 | 0.0 ～ 1.0 |
| 最大出力トークン数 | [モデルページ](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)を使用して、使用しているモデルのトークンの最大数を決定します。 |
| TopP | 0.0 ～ 1.0 |

パラメータ値を確認するだけでなく、必要な機能をサポートする正しい [API バージョン](https://ai.google.dev/gemini-api/docs/api-versions?hl=ja)（`/v1` や `/v1beta` など）とモデルを使用していることを確認してください。たとえば、機能がベータ版リリースの場合、`/v1beta` API バージョンでのみ使用できます。

## モデルが正しいかどうかを確認する

[モデルページ](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)に記載されているサポート対象のモデルを使用していることを確認します。

## 思考モデルでのレイテンシまたはトークン使用量の増加

レイテンシやトークンの使用量が増加するのは、Gemini 3.x モデルで思考がデフォルトで有効になっていることが原因です。非推奨の Gemini 2.5 モデルもデフォルトの思考を使用します。

思考モデルは、品質を向上させるために内部推論トークンを生成します。この推論プロセスにより、レスポンスのレイテンシとトークンの総消費量の両方が増加します。

レイテンシの短縮を優先する場合や、費用を最小限に抑える必要がある場合は、思考レベルを下げるか、思考をオフにできます。

構成の詳細とコードサンプルについては、[思考ガイド](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#thinking-levels)をご覧ください。

## 安全性に関する問題

API 呼び出しの安全設定が原因でプロンプトがブロックされた場合は、API 呼び出しで設定したフィルタに照らしてプロンプトを確認します。

`BlockedReason.OTHER` が表示された場合、クエリまたはレスポンスが[利用規約](https://ai.google.dev/terms?hl=ja)に違反しているか、サポートされていない可能性があります。

## 列挙の問題

RECITATION の理由でモデルが出力の生成を停止した場合は、モデル出力が特定のデータに類似している可能性があります。これを修正するには、プロンプト / コンテキストをできるだけ一意にし、温度を高くします。

## トークンの繰り返しに関する問題

出力トークンが繰り返し表示される場合は、次の方法を試して、繰り返しを減らすか、なくしてください。

| 説明 | 原因 | 推奨される回避策 |
| --- | --- | --- |
| Markdown テーブル内の繰り返しのハイフン | これは、モデルが視覚的に整列されたマークダウン テーブルを作成しようとしたときに、テーブルの内容が長い場合に発生することがあります。ただし、Markdown の配置は、正しいレンダリングに必要ありません。 | プロンプトに指示を追加して、Markdown テーブルを生成するための具体的なガイドラインをモデルに提供します。これらのガイドラインに沿った例を提示します。温度を調整してみることもできます。コードや Markdown テーブルなどの構造化された出力を生成する場合は、高い温度（0.8 以上）の方が効果的であることがわかっています。  この問題を回避するためにプロンプトに追加できるガイドラインの例を次に示します。     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| マークダウン テーブル内の繰り返しトークン | 繰り返されるハイフンと同様に、これはモデルがテーブルの内容を視覚的に揃えようとしたときに発生します。Markdown の配置は、正しいレンダリングには必要ありません。 | - システム プロンプトに次のような指示を追加してみてください。      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - 温度を調整してみてください。温度を高く（0.8 以上）すると、通常、出力の繰り返しや重複を排除できます。 |
| 構造化出力で改行（`\n`）が繰り返される | モデル入力に `\u` や `\t` などの Unicode またはエスケープ シーケンスが含まれていると、改行が繰り返されることがあります。 | - プロンプトで禁止されているエスケープ シーケンスを確認し、UTF-8 文字に置き換えます。たとえば、JSON の例で `\u` エスケープ シーケンスを使用すると、モデルが出力でもそれを使用する可能性があります。 - 許可されるエスケープについてモデルに指示します。次のようなシステム指示を追加します。      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| 構造化出力の使用でテキストが繰り返される | モデル出力のフィールドの順序が、定義された構造化スキーマと異なる場合、テキストが繰り返されることがあります。 | - プロンプトでフィールドの順序を指定しないでください。 - すべての出力フィールドを必須にします。 |
| 繰り返しのツール呼び出し | これは、モデルが以前の思考のコンテキストを失った場合や、利用できないエンドポイントを呼び出すように強制された場合に発生する可能性があります。 | 思考プロセス内で状態を維持するようにモデルに指示します。 システム指示の末尾に次の指示を追加します。    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| 構造化出力の一部ではない繰り返しテキスト | これは、モデルが解決できないリクエストでスタックした場合に発生することがあります。 | - 思考が有効になっている場合は、指示で問題の思考方法を明示的に指示しないでください。最終的な出力をリクエストするだけです。 - 温度を 0.8 以上に上げてみてください。 - 「簡潔に」、「同じことを繰り返さない」、「回答は 1 回だけ」などの指示を追加します。 |

## プロジェクトが制限されているか、利用できません

API リクエストが `403 PERMISSION_DENIED`（「プロジェクトへのアクセスが拒否されました」）を返す場合、またはプロジェクトのステータスが [Google AI Studio](https://aistudio.google.com/?hl=ja) で [**制限付き**]、[**無料枠は利用できません**]、[**お支払いが必要です**]、[**利用できません**] と表示される場合は、プロジェクトに該当するセクションを確認してください。

### Gemini API の無料枠が利用できない

すべての Google Cloud プロジェクトまたはアカウントが Gemini API の無料枠の対象となるわけではありません。プロジェクトで無料枠の使用が制限されている場合:

- **同じプロジェクトで新しい API キーを作成しても、エラーは解決しません。**Google は、Google Cloud プロジェクト レベルで利用資格を評価します。
- **このプロジェクトで Gemini API を使用するには、有効な
  [Cloud 請求先アカウント](https://aistudio.google.com/billing?hl=ja)をリンクして、有料
  ティアにアップグレードする必要があります**。
- 注: プロジェクトを有料ティアにアップグレードしても、無料ティアの割り当ては解除されません。Google は、[Gemini API の料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)に従って有料ティアの使用量を請求するか、対象となる Google Cloud クレジットから差し引きます。

### Cloud 請求先アカウントのお支払いが必要です

プロジェクトがすでに Cloud 請求先アカウントにリンクされていて、[**お支払いが必要です**] と表示されている場合（または、未払い残高を示す `403 PERMISSION_DENIED` が返される場合）:

- [AI Studio のお支払いページ](https://aistudio.google.com/billing?hl=ja)または [Google Cloud Billing コンソール](https://console.cloud.google.com/billing?hl=ja)にアクセスして、未払い残高を解決するか、お支払い方法を更新してください。
- 請求先アカウントが良好な状態に戻ると、プロジェクトは API アクセスを自動的に回復します。

### 漏洩した API キーまたはブロックされた API キー

`403 PERMISSION_DENIED` エラーで、API キーが漏洩またはブロックされたと報告されている場合:

- [AI Studio の API キーページ](https://aistudio.google.com/apikeys?hl=ja)に移動して、新しい API キーを生成し、アプリケーションの認証情報を更新します。
- API キーをクライアントサイドのコードや公開リポジトリに直接埋め込むことは絶対に避けてください。

### ポリシーに基づくプロジェクトまたは請求先アカウントの停止

ポリシー違反により Google Cloud プロジェクトまたは Cloud 請求先アカウントが停止された場合は、関連付けられているメールアドレスを確認してください。[Google Cloud コンソール](https://console.cloud.google.com/?hl=ja)にアクセスして、停止通知を確認し、[プロジェクト停止ガイドライン](https://cloud.google.com/resource-manager/docs/project-suspension-guidelines?hl=ja)に沿って対応してください。

## ブロックされている、または機能していない API キー

このセクションでは、Gemini API キーがブロックされているかどうかを確認する方法と、その対処方法について説明します。

### 鍵がブロックされる理由を理解する

一部の API キーが一般公開されている可能性がある脆弱性が特定されました。データを保護し、不正アクセスを防止するため、Google は、これらの既知の漏洩したキーが Gemini API にアクセスできないように事前にブロックしました。

### 鍵が影響を受けるかどうかを確認する

キーが漏洩していることが判明した場合、そのキーを Gemini API で使用することはできなくなります。[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=ja) を使用して、API キーが Gemini API の呼び出しをブロックされているかどうかを確認し、新しいキーを生成できます。これらのキーを使用しようとすると、次のエラーが返されることもあります。

```
Your API key was reported as leaked. Please use another API key.
```

### ブロックされた API キーに対するアクション

Gemini API 統合用の新しい API キーは、[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=ja) を使用して生成する必要があります。新しいキーが安全に保管され、公開されないように、API キーの管理方法を見直すことを強くおすすめします。

### 脆弱性による予期しない請求

[課金サポートケースを送信する](https://console.cloud.google.com/support/chat?hl=ja)。請求チームがこの問題に取り組んでおり、できるだけ早く最新情報をお知らせします。

### 漏洩した鍵に対する Google のセキュリティ対策

**API キーが漏洩した場合、Google はどのようにしてアカウントを費用超過や不正使用から保護しますか？**

- [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=ja) を使用して新しいキーをリクエストすると、デフォルトで Google AI Studio のみに制限され、他のサービスからのキーを受け入れない API キーが発行されるようになります。これにより、意図しないクロスキーの使用を防ぐことができます。
- Gemini API で漏洩して使用された API キーは、デフォルトでブロックされます。これにより、費用やアプリケーション データの不正使用を防ぐことができます。
- API キーのステータスは [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=ja) で確認できます。また、API キーの漏洩が検出された場合は、迅速な対応のために積極的な通知を行います。

## モデル出力を改善する

モデル出力の品質を高めるには、より構造化されたプロンプトを作成することを検討してください。[プロンプト エンジニアリング ガイド](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)のページでは、プロンプトの設計を開始するための基本的なコンセプト、戦略、ベスト プラクティスについて説明します。

## トークンの上限について

トークンのカウント方法と上限について詳しくは、[トークンガイド](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)をご覧ください。

## 既知の問題

- この API は、一部の言語のみをサポートしています。サポートされていない言語でプロンプトを送信すると、予期しないレスポンスが生成されたり、レスポンスがブロックされたりすることがあります。最新情報については、[利用可能な言語](https://ai.google.dev/gemini-api/docs/models?hl=ja#supported-languages)をご覧ください。

## バグを報告する

ご不明な点がございましたら、[Google AI デベロッパー フォーラム](https://discuss.ai.google.dev?hl=ja)のディスカッションにご参加ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-23 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-23 UTC。"],[],[]]
