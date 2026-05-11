---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja
fetched_at: 2026-05-11T12:38:08.078093+00:00
title: "\u30ec\u30fc\u30c8\u5236\u9650 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# レート制限

レート制限は、特定の期間内に Gemini API に送信できるリクエスト数を規制します。この制限は、公正な使用を維持し、不正使用を防ぎ、すべてのユーザーのシステム パフォーマンスを維持するのに役立ちます。

[AI Studio で有効なレート制限を確認する](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=ja)

## レート制限の仕組み

レート制限は通常、次の 3 つのディメンションで測定されます。

- 1 分あたりのリクエスト数（**RPM**）
- 1 分あたりのトークン数（入力）（**TPM**）
- 1 日あたりのリクエスト数（**RPD**）

使用量は各上限と比較され、いずれかを超えるとレート制限エラーがトリガーされます。たとえば、RPM 上限が 20 の場合、1 分以内に 21 件のリクエストを行うと、TPM やその他の上限を超えていなくてもエラーが発生します。

レート制限は、API キーごとではなく、プロジェクトごとに適用されます。1 日あたりのリクエスト数（**RPD**）の割り当ては、午前 0 時（太平洋時間）にリセットされます。

上限は使用する特定のモデルによって異なり、一部の上限は特定のモデルにのみ適用されます。たとえば、1 分あたりの画像数（IPM）は、画像を生成できるモデル（Nano Banana）でのみ計算されますが、概念的には TPM と似ています。他のモデルでは、1 日あたりのトークン数（TPD）の上限が設定されている場合があります。

試験運用版モデルとプレビュー版モデルでは、レート制限が厳しくなっています。

## 使用量ティア

レート制限は、プロジェクトの使用量ティアに関連付けられています。API の使用量と費用が増加すると、レート制限が引き上げられた上位のティアに自動的にアップグレードされます。

Tier 2 と Tier 3 の資格は、プロジェクトにリンクされた請求先アカウントの Google Cloud サービス（Gemini API 以下を含みます（ただしこれらに限定されません））の合計累積費用に基づいています。

| 使用量ティア | 予選 | [請求先アカウント枠の上限](https://ai.google.dev/gemini-api/docs/billing?hl=ja#tier-spend-caps) |
| --- | --- | --- |
| **無料** | [有効なプロジェクト](https://ai.google.dev/gemini-api/docs/api-key?hl=ja#google-cloud-projects)または無料トライアル | なし |
| **Tier 1** | [有効な請求先アカウントを設定してリンクしている](https://ai.google.dev/gemini-api/docs/billing?hl=ja#setup-billing) | $250 |
| **Tier 2** | 最初の支払いが完了してから 3 日以上経過し、$100 以上を支払っている | $2,000 |
| **Tier 3** | 最初の支払いが完了してから 30 日以上経過し、$1,000 以上を支払っている | $20,000 ～$100,000 以上 |

通常、記載されている資格要件を満たしていれば承認されますが、審査プロセスで特定された他の要因に基づいて、アップグレード リクエストが拒否される場合があります。

このシステムは、すべてのユーザーに対して Gemini API プラットフォームのセキュリティと整合性を維持するのに役立ちます。

## Gemini API のレート制限

レート制限は、使用量ティアなどのさまざまな要因によって異なり、Google AI Studio で確認できます。ティアとアカウントのステータスが時間とともに変化すると、レート制限は自動的に更新されます。

[AI Studio で有効なレート制限を確認する](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=ja)

指定されたレート制限は保証されるものではなく、実際の容量は異なる場合があります。

## 優先推論のレート制限

[優先](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)消費量は、消費量が全体的なインタラクティブ トラフィックの
レート制限にカウントされる場合でも、独自のレート
制限を保持します。**デフォルトのレート制限は、モデルとティアごとに[標準レート制限](https://aistudio.google.com/rate-limit?hl=ja)の 0.3 倍です。**

## Batch API のレート制限

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja) リクエストには、非バッチ API 呼び出しとは別に、独自のレート
制限が適用されます。

- **同時実行バッチ リクエスト:** 100
- **入力ファイルサイズの制限:** 2 GB
- **ファイル ストレージの上限:** 20 GB
- **モデルごとにキューに追加できるトークン数:** [**キューに追加できるバッチトークン**] 表に、特定のモデルのアクティブなバッチジョブ全体でバッチ処理用にキューに追加できるトークンの最大数が表示されます。

### Tier 1

| モデル | キューに追加できるバッチトークン |
| --- | --- |
| テキスト出力モデル | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro プレビュー版 | 5,000,000 |
| Gemini 3.1 Flash-Lite | 10,000,000 |
| Gemini 3.1 Flash-Lite プレビュー版 | 10,000,000 |
| Gemini 3 Flash プレビュー | 3,000,000 |
| Gemini 2.5 Pro | 5,000,000 |
| Gemini 2.5 Pro TTS | 25,000 |
| Gemini 2.5 Flash | 3,000,000 |
| Gemini 2.5 Flash プレビュー | 3,000,000 |
| Gemini 2.5 Flash 画像プレビュー | 3,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash-Lite | 10,000,000 |
| Gemini 2.5 Flash-Lite プレビュー版 | 10,000,000 |
| Gemini 2.0 Flash | 10,000,000 |
| Gemini 2.0 Flash 画像 | 3,000,000 |
| Gemini 2.0 Flash-Lite | 10,000,000 |
| マルチモーダル生成モデル | | | | |
| Gemini 3.1 Flash 画像プレビュー 🍌 | 1,000,000 |
| Gemini 3 Pro 画像プレビュー 🍌 | 2,000,000 |
| エンベディング モデル | | | | |
| Gemini エンベディング | 500,000 |

### Tier 2

| モデル | キューに追加できるバッチトークン |
| --- | --- |
| テキスト出力モデル | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro プレビュー版 | 500,000,000 |
| Gemini 3.1 Flash-Lite | 500,000,000 |
| Gemini 3.1 Flash-Lite プレビュー版 | 500,000,000 |
| Gemini 3.1 Flash プレビュー | 400,000,000 |
| Gemini 2.5 Pro | 500,000,000 |
| Gemini 2.5 Pro TTS | 100,000 |
| Gemini 2.5 Flash | 400,000,000 |
| Gemini 2.5 Flash プレビュー | 400,000,000 |
| Gemini 2.5 Flash 画像プレビュー | 400,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash-Lite | 500,000,000 |
| Gemini 2.5 Flash-Lite プレビュー版 | 500,000,000 |
| Gemini 2.0 Flash | 1,000,000,000 |
| Gemini 2.0 Flash 画像 | 400,000,000 |
| Gemini 2.0 Flash-Lite | 1,000,000,000 |
| マルチモーダル生成モデル | | | | |
| Gemini 3.1 Flash 画像プレビュー 🍌 | 250,000,000 |
| Gemini 3 Pro 画像プレビュー 🍌 | 270,000,000 |
| エンベディング モデル | | | | |
| Gemini エンベディング | 5,000,000 |

### Tier 3

| モデル | キューに追加できるバッチトークン |
| --- | --- |
| テキスト出力モデル | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro プレビュー版 | 1,000,000,000 |
| Gemini 3.1 Flash-Lite | 1,000,000,000 |
| Gemini 3.1 Flash-Lite プレビュー版 | 1,000,000,000 |
| Gemini 3.1 Flash プレビュー | 1,000,000,000 |
| Gemini 2.5 Pro | 1,000,000,000 |
| Gemini 2.5 Pro TTS | 1,000,000 |
| Gemini 2.5 Flash | 1,000,000,000 |
| Gemini 2.5 Flash プレビュー | 1,000,000,000 |
| Gemini 2.5 Flash 画像プレビュー | 1,000,000,000 |
| Gemini 2.5 Flash TTS | 4,000,000 |
| Gemini 2.5 Flash-Lite | 1,000,000,000 |
| Gemini 2.5 Flash-Lite プレビュー版 | 1,000,000,000 |
| Gemini 2.0 Flash | 5,000,000,000 |
| Gemini 2.0 Flash 画像 | 1,000,000,000 |
| Gemini 2.0 Flash-Lite | 5,000,000,000 |
| マルチモーダル生成モデル | | | | |
| Gemini 3.1 Flash 画像プレビュー 🍌 | 750,000,000 |
| Gemini 3 Pro 画像プレビュー 🍌 | 1,000,000,000 |
| エンベディング モデル | | | | |
| Gemini エンベディング | 10,000,000 |

## 次のティアにアップグレードする方法

無料ティアから有料ティアに移行するには、まず
[AI Studio で課金を設定する必要があります](https://ai.google.dev/gemini-api/docs/billing?hl=ja)。

プロジェクトが[指定された条件](#usage-tiers)を満たすと、
自動的に次のティアにアップグレードされます。無料ティアから Tier 1 へのティアのアップグレードは通常、すぐに有効になり、それ以降のティアのアップグレードは 10 分以内に有効になります。AI Studio の [[プロジェクト] ページ](https://aistudio.google.com/projects?hl=ja)に移動して、ティアを確認します。

## レート制限の引き上げをリクエストする

モデル バリエーションごとに、関連付けられたレート制限（1 分あたりのリクエスト数、RPM）があります。
これらのレート制限の詳細については、
[AI Studio のレート制限](https://aistudio.google.com/rate-limit?hl=ja)のページをご覧ください。

[有料ティアのレート制限の引き上げをリクエストする](https://forms.gle/ETzX94k8jf7iSotH9)

レート制限の引き上げを保証するものではありませんが、リクエストの審査に最善を尽くします。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-07 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-07 UTC。"],[],[]]
