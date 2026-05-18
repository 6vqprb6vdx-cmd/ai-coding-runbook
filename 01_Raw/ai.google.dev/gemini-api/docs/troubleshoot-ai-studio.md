---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=ja
fetched_at: 2026-05-18T13:11:26.672693+00:00
title: "Google AI Studio \u306e\u30c8\u30e9\u30d6\u30eb\u30b7\u30e5\u30fc\u30c6\u30a3\u30f3\u30b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Google AI Studio のトラブルシューティング

このページでは、Google AI Studio で問題が発生した場合のトラブルシューティングのヒントを紹介します。

## 403 アクセス制限エラーについて

[403 アクセス制限エラーが表示される場合は、
利用規約](https://ai.google.dev/terms?hl=ja)に準拠しない方法で Google AI Studio を使用しています。一般的な理由の一つに、
サポートされている[リージョン](https://ai.google.dev/available_regions?hl=ja)にいないことが挙げられます。

## Google AI Studio で「コンテンツなし」というレスポンスを解決する

コンテンツが何らかの理由でブロックされると、warning **コンテンツなし** メッセージが
Google AI Studio に表示されます。詳細を確認するには、
[**コンテンツなし**] にポインタを合わせて、
warning [**安全性**] をクリックします。

[[[安全設定が原因でレスポンスがブロックされ、ユースケースの安全上のリスクを考慮した場合は、安全設定を変更して返されるレスポンスに影響を与えることができます。](https://ai.google.dev/docs/safety_setting?hl=ja)](https://ai.google.dev/docs/safety_guidance?hl=ja)](https://ai.google.dev/docs/safety_setting?hl=ja#safety_settings_in_makersuite)

安全設定が原因でレスポンスがブロックされなかった場合、クエリまたは
レスポンスが[利用規約](https://ai.google.dev/terms?hl=ja)に違反しているか、サポートされていない可能性があります。

## トークンの使用量と上限を確認する

プロンプトを開くと、画面下部の [**テキスト プレビュー**] ボタンに、プロンプトのコンテンツに使用されている現在のトークン数と、使用されているモデルの最大トークン数が表示されます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
