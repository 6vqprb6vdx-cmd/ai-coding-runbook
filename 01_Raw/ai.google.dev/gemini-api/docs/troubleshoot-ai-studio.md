---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=ja
fetched_at: 2026-09-14T05:42:03.569519+00:00
title: "Google AI Studio \u306e\u30c8\u30e9\u30d6\u30eb\u30b7\u30e5\u30fc\u30c6\u30a3\u30f3\u30b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Google AI Studio のトラブルシューティング

このページでは、Google AI Studio で問題が発生した場合のトラブルシューティング方法について説明します。

## 403 アクセス制限エラーについて

[403 アクセス制限エラーが表示される場合は、
利用規約](https://ai.google.dev/terms?hl=ja)に準拠しない方法で Google AI Studio を使用しています。一般的な理由の 1 つは、
[サポートされているリージョン](https://ai.google.dev/available_regions?hl=ja)に居住していないことです。

## Google AI Studio でコンテンツなしのレスポンスを解決する

コンテンツが何らかの理由でブロックされると、warning **コンテンツなし** メッセージが
Google AI Studio に表示されます。詳細を確認するには、
[**コンテンツなし**] にポインタを合わせて、
warning [**安全性**] をクリックします。

[[[安全設定によりレスポンスがブロックされ、ユースケースの安全上のリスクを考慮した場合は、安全設定を変更して返されるレスポンスに影響を与えることができます。](https://ai.google.dev/docs/safety_setting?hl=ja)](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ja)](https://ai.google.dev/docs/safety_setting?hl=ja#safety_settings_in_makersuite)

レスポンスがブロックされたが、安全設定が原因ではない場合、クエリまたは
レスポンスが[利用規約](https://ai.google.dev/terms?hl=ja)に違反しているか、サポートされていない可能性があります。

## トークンの使用量と上限を確認する

プロンプトを開くと、画面下部の [**テキスト プレビュー**] ボタンに、プロンプトのコンテンツに使用されている現在のトークン数と、使用されているモデルの最大トークン数が表示されます。

## AI Studio の Google Cloud IAM 権限

Google Cloud プロジェクトのメンバーが Google AI Studio で操作を行うには、特定の Identity and Access Management（IAM）権限が必要です。これらの ID の詳細については、[IAM プリンシパルの概要](https://docs.cloud.google.com/iam/docs/principals-overview?hl=ja)をご覧ください。

関連付けられた Google Cloud プロジェクトで**編集者** または**オーナー** のロールを持つユーザーは、ダッシュボードを表示して Gemini API キーを管理するための完全な権限を持ちます。**閲覧者** のロールを持つユーザーは、ダッシュボードと API キーを表示できますが、作成、更新、削除はできません。

より詳細な制御を行うには、次の表で、AI Studio の各機能に必要な特定の権限を確認してください。これらの権限を付与する方法については、Google Cloud ドキュメントの[リソースへのアクセス権の付与、変更、取り消し](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=ja)をご覧ください。

| AI Studio の機能 | 必要な IAM 権限 | その他の要件 |
| --- | --- | --- |
| **プロジェクトを検索** （プロジェクトをインポート） | `resourcemanager.projects.get` |  |
| **プロジェクトの名前を変更** | `resourcemanager.projects.update` |  |
| **割り当て階層を表示** | なし |  |
| **API キーを作成** | **プロジェクトを検索** 権限があること、および  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **API キーを一覧表示** | **プロジェクトを検索** 権限があること、および  `apikeys.keys.list` `serviceusage.services.get` | Google Cloud プロジェクトで [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=ja) が有効になっている必要があります。 |
| **API キーの名前を変更** | `apikeys.keys.update` |  |
| **API キーを削除** | `apikeys.keys.delete` |  |
| **使用状況ダッシュボード** | **プロジェクトを検索** 権限があること、および  `monitoring.timeSeries.list` |  |
| **レート制限ダッシュボード** | **使用状況ダッシュボード** 権限があること、および  `cloudquotas.quotas.get` |  |
| **費用（請求上限）** | `billing.resourceCosts.get`（費用を表示） `billing.resourcebudgets.read`（上限を表示） `billing.resourcebudgets.write`（上限を設定） |  |
| **請求ダッシュボード** | `billing.accounts.get` |  |

### その他のアクセス チェック

Google Cloud IAM 権限に加えて、AI Studio ではセキュリティとコンプライアンスのチェックも行われます。次の要件を満たしていない場合、AI Studio インターフェースまたは API レスポンスで `PERMISSION_DENIED` エラーまたはアクセス制限エラーが発生することがあります。

- **セキュリティ チェック:** リクエストは自動セキュリティ チェックに合格する必要があります。
- **利用規約:** Google 利用規約と生成 AI の追加利用規約に同意する必要があります。
- **サポートされているリージョン:** サポートされている[リージョン](https://ai.google.dev/gemini-api/docs/available-regions?hl=ja)に居住している必要があります。
- **信頼と安全性:** Google Cloud プロジェクトに不正使用のフラグが設定されていない必要があります。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-12 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-12 UTC。"],[],[]]
