---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ja
fetched_at: 2026-09-14T05:52:08.835588+00:00
title: "\u30c8\u30e9\u30d6\u30eb\u30b7\u30e5\u30fc\u30c6\u30a3\u30f3\u30b0 \u30ac\u30a4\u30c9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# トラブルシューティング ガイド

このガイドでは、Gemini API の呼び出し時に発生する一般的な問題の診断と解決に役立つ情報を説明します。Gemini API バックエンド サービスまたはクライアント SDK のいずれかで問題が発生する可能性があります。Google のクライアント SDK は、次のリポジトリでオープンソース化されています。

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

API キーに関する問題が発生した場合は、[API キーの設定ガイド](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)に沿って
API キーが正しく設定されていることを確認してください。

## エラーコード

HTTP ステータス コード、
生成ブロック コード、コンテンツ エラーコードなど、すべてのエラーコードのリファレンスについては、
[API エラー](https://ai.google.dev/gemini-api/docs/api-errors?hl=ja)のページをご覧ください。

## 再試行方法

リクエストを再試行する必要があることを示すエラー（`429 RESOURCE_EXHAUSTED` や `503 UNAVAILABLE` など）を受け取った場合は、指数バックオフ戦略を実装することをおすすめします。つまり、最初の再試行の前に短い時間待機し、以降の再試行の間隔を徐々に長くします。

[Python SDK](https://github.com/googleapis/python-genai) などの Gemini API の公式クライアント SDK には、タイムアウト、ネットワークの問題、レート制限（`429` と `5xx` のステータス コード）など、一時的なエラーを処理するための指数バックオフによる自動再試行ロジックがデフォルトで含まれています。たとえば、Python SDK は、一時的なエラーを最大 4 回再試行します。最初の遅延は約 1 秒、最大遅延は 60 秒です。

REST API リクエストを直接行う場合や、再試行ロジックをカスタマイズする場合は、次のベスト プラクティスに沿って、リクエストが成功する可能性を高め、サービスに過負荷がかからないようにしてください。

- **指数バックオフを使用する:** 最初の再試行の前に短い時間（1 秒など）待機し、遅延を指数関数的に増やします（2 秒、4 秒、8 秒など）。
- **ジッターを追加する:** 遅延にランダムな「ジッター」を追加して、すべてのクライアントが同時に再試行しないようにします。
- **特定のエラーで再試行する:** 一時的なエラー（`429`、`408`、`5xx` など）でのみ再試行します。クライアント エラー（`400`、`403` など）は、無効な API キーや不正な構文などの問題を示しているため、再試行しないでください。
- **最大再試行回数を設定する:** 無限ループを防ぐため、再試行回数の上限を定義します。

## API 呼び出しでモデル パラメータのエラーを確認する

モデル パラメータが次の値の範囲内にあることを確認します。

|  |  |
| --- | --- |
| **モデル パラメータ** | **値（範囲）** |
| 候補数 | 1 ～ 8（整数） |
| 温度 | 0.0 ～ 1.0 |
| 最大出力トークン | 使用しているモデルの最大トークン数を[モデルページ](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja) で確認します。 |
| TopP | 0.0 ～ 1.0 |

パラメータ値を確認するだけでなく、必要な機能をサポートする正しい
[API バージョン](https://ai.google.dev/gemini-api/docs/api-versions?hl=ja)（`/v1`、`/v1beta` など）と
モデルを使用していることを確認してください。たとえば、機能がベータ版の場合、`/v1beta` API バージョンでのみ使用できます。

## 適切なモデルを使用していることを確認する

モデル[ページ
に記載されているサポート対象モデルを使用していることを確認します](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)。

## 2.5 モデルでのレイテンシの増加またはトークン使用量の増加

2.5 Flash モデルと Pro モデルでレイテンシやトークン使用量が増加している場合は、品質向上のために**思考がデフォルトで有効になっている** ことが原因である可能性があります。速度を優先する場合や、費用を最小限に抑える必要がある場合は、思考を調整または無効にできます。

ガイダンスとサンプルコードについては、[思考のページ](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#set-budget)を
ご覧ください。

## 安全性に関する問題

API 呼び出しの安全設定によりプロンプトがブロックされた場合は、API 呼び出しで設定したフィルタに関してプロンプトを確認してください。

`BlockedReason.OTHER` が表示された場合、クエリまたはレスポンスが [利用規約](https://ai.google.dev/terms?hl=ja) に違反しているか、サポートされていない可能性があります。

## 暗唱の問題

RECITATION という理由でモデルの出力生成が停止した場合は、モデル出力が特定のデータに似ている可能性があります。この問題を解決するには、プロンプト / コンテキストをできるだけ一意にし、Temperature を高くしてみてください。

## トークンの繰り返しに関する問題

出力トークンが繰り返される場合は、次の方法を試して、トークンを減らすか削除してください。

| 説明 | 原因 | 推奨される回避策 |
| --- | --- | --- |
| Markdown テーブルでハイフンが繰り返される | モデルが視覚的に整列された Markdown テーブルを作成しようとすると、テーブルの内容が長くなる場合に発生することがあります。ただし、正しいレンダリングには Markdown の配置は必要ありません。 | プロンプトに指示を追加して、Markdown テーブルを生成するための具体的なガイドライン をモデルに提供します。これらのガイドラインに沿った例を示します。 温度を調整することもできます。コードや Markdown テーブルなどの構造化された出力を生成する場合、Temperature（>= 0.8）の方が効果的であることがわかっています。  この問題を回避するためにプロンプトに追加できるガイドラインの例を次に示します。     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Markdown テーブルでトークンが繰り返される | ハイフンの繰り返しと同様に、モデルがテーブルの内容を 視覚的に整列しようとすると発生します。正しいレンダリングには Markdown の配置は 必要ありません。 | - 次のような指示をシステム プロンプトに追加してみてください。      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - 温度を調整してみてください。一般に、温度が高いほど（>= 0.8）   出力の繰り返しや重複を解消できます。 |
| 構造化出力で改行（`\n`）が繰り返される | モデルの入力に Unicode やエスケープ シーケンス（ `\u`、`\t` など）が含まれていると、改行が繰り返されることがあります。 | - プロンプトで禁止されているエスケープ シーケンスを確認し、UTF-8 文字に置き換えます。   たとえば、JSON の例で `\u`   エスケープ シーケンスを使用すると、モデルがそのエスケープ シーケンスを出力で使用する可能性があります。 - 許可されているエスケープについてモデルに指示します。次のようなシステム指示を追加します。   これ:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| 構造化出力を使用してテキストが繰り返される | モデル出力でフィールドの順序が定義された構造化スキーマと異なる場合、テキストが繰り返されることがあります。 | - プロンプトでフィールドの順序を指定しないでください。 - すべての出力フィールドを必須にします。 |
| ツール呼び出しの繰り返し | モデルが以前の思考のコンテキストを失った場合や、強制的に使用できないエンドポイントを呼び出した場合に発生することがあります。 | 思考プロセス内で状態を維持するようにモデルに指示します。 システム指示の末尾に以下を追加します。    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| 構造化出力の一部ではないテキストの繰り返し | モデルが解決できないリクエストでスタックした場合に発生することがあります。 | - 思考がオンになっている場合は、手順で問題の解決方法を   明示的に指示しないでください。最終的な   出力のみをリクエストします。 - 温度を 0.8 以上にしてみてください。 - 「簡潔にしてください」、「繰り返さないでください」、「回答は 1 回のみ提供してください」などの指示を追加します。 |

## ブロックされた API キーまたは機能しない API キー

このセクションでは、Gemini API キーがブロックされているかどうかを確認する方法と、その対処方法について説明します。

### キーがブロックされる理由を理解する

一部の API キーが一般公開されている可能性がある脆弱性が特定されました。データを保護し、不正アクセスを防ぐため、既知の漏洩したキーが Gemini API にアクセスできないように事前にブロックしました。

### キーが影響を受けているかどうかを確認する

キーが漏洩していることが判明した場合、Gemini API でそのキーを使用することはできません。[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ja) を使用すると、Gemini API の呼び出しがブロックされている API キーがあるかどうかを確認し、新しい
キーを生成できます。これらのキーを使用しようとすると、次のエラーが返されることもあります。

```
Your API key was reported as leaked. Please use another API key.
```

### ブロックされた API キーに対するアクション

[Google
AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ja) を使用して、Gemini API 統合用の新しい API キーを生成する必要があります。新しいキーが安全に保管され、一般公開されないように、API キーの管理方法を見直すことを強くおすすめします。

### 脆弱性による予期しない請求

[課金サポートケースを送信してください](https://console.cloud.google.com/support/chat?hl=ja)。
課金チームが対応を進めており、最新情報をできるだけ早くお知らせいたします。

### 漏洩したキーに対する Google のセキュリティ対策

**API キーが漏洩した場合、Google は費用超過や不正使用からアカウントを保護するためにどのような対策を講じますか？**

- Google AI Studio を使用して新しいキーをリクエストすると、API キーが発行されるようになります。デフォルトでは、
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ja) のみに制限され、他のサービスからのキーは受け付けられません。
  これにより、意図しないキーのクロス使用を防ぐことができます。
- Gemini API で漏洩して使用されている API キーはデフォルトでブロックされ、費用やアプリケーション データの不正使用を防ぐことができます。
- [Google AI
  Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=ja) で API キーのステータスを確認できます。API キーが漏洩していることが判明した場合は、迅速な対応を促すため、積極的に通知いたします。

## モデル出力を改善する

モデルの出力を高品質にするには、構造化されたプロンプトの作成を検討してください。
[プロンプト エンジニアリング ガイド](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)のページ
では、基本的なコンセプト、戦略、ベスト プラクティスについて説明しています。

## トークンの上限について

[トークン ガイド](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)を読んで、トークンのカウント方法と上限について理解を深めてください。

## 既知の問題

- この API は、一部の言語のみをサポートしています。サポートされていない言語でプロンプトを送信すると、予期しないレスポンスやブロックされたレスポンスが生成される可能性があります。最新情報については、
  [対応言語](https://ai.google.dev/gemini-api/docs/models?hl=ja#supported-languages)をご覧ください。

## バグを報告する

ご不明な点がございましたら、
[Google AI デベロッパー フォーラム](https://discuss.ai.google.dev?hl=ja)
のディスカッションにご参加ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-11 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-11 UTC。"],[],[]]
