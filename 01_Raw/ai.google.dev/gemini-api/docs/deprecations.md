---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=ja
fetched_at: 2026-10-26T05:48:31.963975+00:00
title: "Gemini \u306e\u975e\u63a8\u5968 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini の非推奨

このページでは、[安定版（GA）](https://ai.google.dev/gemini-api/docs/models?hl=ja#stable)モデルと[プレビュー](https://ai.google.dev/gemini-api/docs/models?hl=ja#preview) モデル、および Gemini API のマネージド エージェントの既知の非推奨スケジュールについて説明します。「**非推奨**」とは、モデルのサポートが終了し、近い将来に「**シャットダウン**」されるというお知らせです。モデルが「**シャットダウン**」されると、完全にオフになり、エンドポイントは使用できなくなります。

サポート終了のお知らせは[リリースノート](https://ai.google.dev/gemini-api/docs/changelog?hl=ja)のページに掲載されます。また、お知らせに記載されている最も早いシャットダウン日は、このページで追跡されます。すでにシャットダウンされているモデルは、グレーの背景で表示されます。

## Gemini 3 モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替手段** |
| --- | --- | --- | --- |
| `gemini-3.8-flash-tts` | 2026 年 9 月 22 日 | 提供終了日は未発表 |  |
| `gemini-3.8-flash-lite-tts` | 2026 年 9 月 22 日 | 提供終了日は未発表 |  |
| `gemini-3.8-live` | 2026 年 9 月 15 日 | 提供終了日は未発表 |  |
| `gemini-3.8-live-extended-thinking` | 2026 年 9 月 15 日 | 提供終了日は未発表 |  |
| `gemini-3.8-flash` | 2026 年 9 月 2 日 | 提供終了日は未発表 |  |
| `gemini-3.7-flash` | 2026 年 8 月 13 日 | なし | `gemini-3.8-flash`（Google AI Studio では選択できません。エンドポイントはシャットダウンされず、API リクエストは自動的に `gemini-3.8-flash` にルーティングされます） |
| `gemini-3.6-flash` | 2026 年 7 月 21 日 | 提供終了日は未発表 |  |
| `gemini-3.5-flash-lite` | 2026 年 7 月 21 日 | 提供終了日は未発表 |  |
| `gemini-3.5-flash` | 2026 年 5 月 19 日 | なし | `gemini-3.6-flash`（Google AI Studio では選択できません。エンドポイントはシャットダウンされず、API リクエストは自動的に `gemini-3.6-flash` にルーティングされます） |
| `gemini-3.1-flash-lite` | 2026 年 5 月 7 日 | 2027 年 5 月 7 日 | `gemini-3.5-flash-lite` |
| モデルをプレビュー | | | |
| `gemini-3.1-flash-tts-preview` | 2026 年 2 月 26 日 | 2026 年 11 月 17 日 | `gemini-3.8-flash-tts` または `gemini-3.8-flash-lite-tts` |
| `gemini-3.1-pro-preview` | 2026 年 2 月 19 日 | 提供終了日は未発表 |  |
| `gemini-3-flash-preview` | 2025 年 12 月 17 日 | 提供終了日は未発表 | `gemini-3.6-flash` |
| `gemini-3-pro-preview` | 2025 年 11 月 18 日 | 2026 年 3 月 9 日 | `gemini-3.1-pro-preview` |
| `gemini-3.1-flash-lite-preview` | 2026 年 3 月 3 日 | 2026 年 5 月 25 日 | `gemini-3.1-flash-lite` |

## Gemini 2.5 Pro モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | 2025 年 6 月 17 日 | 提供終了日は未発表 |  |
| モデルをプレビュー | | | |
| `gemini-2.5-computer-use-preview-10-2025` | 2025 年 10 月 7 日 | 2026 年 7 月 28 日 | `gemini-3.8-flash` |
| `gemini-2.5-pro-preview-03-25` | 2025 年 3 月 3 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | 2025 年 5 月 6 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | 2025 年 6 月 5 日 | 2025 年 12 月 2 日 | `gemini-3.1-pro-preview` |

## Gemini 2.5 Flash モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | 2025 年 6 月 17 日 | 提供終了日は未発表 |  |
| `gemini-2.5-flash-lite` | 2025 年 7 月 22 日 | 提供終了日は未発表 |  |
| モデルをプレビュー | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | 2025 年 9 月 25 日 | 2026 年 3 月 31 日 | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | 2025 年 5 月 20 日 | 2025 年 11 月 18 日 | `gemini-3.6-flash` |
| `gemini-2.5-flash-preview-09-25` | 2025 年 9 月 25 日 | 2026 年 2 月 17 日 | `gemini-3.6-flash` |

## Gemini 2.0 モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | 2025 年 2 月 5 日 | 2026 年 6 月 1 日 | `gemini-3.6-flash` |
| `gemini-2.0-flash-001` | 2025 年 2 月 5 日 | 2026 年 6 月 1 日 | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` | 2025 年 2 月 25 日 | 2026 年 6 月 1 日 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-001` | 2025 年 2 月 25 日 | 2026 年 6 月 1 日 | `gemini-3.1-flash-lite` |
| モデルをプレビュー | | | |
| `gemini-2.0-flash-lite-preview` | 2025 年 2 月 5 日 | 2025 年 12 月 9 日 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | 2025 年 2 月 5 日 | 2025 年 12 月 9 日 | `gemini-3.1-flash-lite` |

## Live API モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `gemini-3.8-live` | 2026 年 9 月 15 日 | 提供終了日は未発表 |  |
| `gemini-3.8-live-extended-thinking` | 2026 年 9 月 15 日 | 提供終了日は未発表 |  |
| `gemini-3.5-transcribe-live` | 2026 年 8 月 | 提供終了日は未発表 |  |
| `gemini-2.0-flash-live-001` | 2025 年 4 月 9 日 | 2025 年 12 月 9 日 | `gemini-3.8-live` |
| モデルをプレビュー | | | |
| `gemini-3.5-live-translate-preview` | 2026 年 6 月 | 提供終了日は未発表 |  |
| `gemini-3.1-flash-live-preview` | 2026 年 3 月 11 日 | 2026 年 11 月 17 日 | `gemini-3.8-live` |
| `gemini-2.5-flash-native-audio-preview-12-2025` | 2025 年 12 月 12 日 | 2026 年 11 月 17 日 | `gemini-3.8-live` |
| `gemini-live-2.5-flash-preview` | 2025 年 6 月 17 日 | 2025 年 12 月 9 日 | `gemini-3.8-live` |

## 音声モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `gemini-3.5-transcribe` | 2026 年 8 月 | 提供終了日は未発表 |  |
| モデルをプレビュー | | | |
| `gemini-2.5-flash-preview-tts` | 2025 年 5 月 20 日 | 2026 年 11 月 17 日 | `gemini-3.8-flash-tts` または `gemini-3.8-flash-lite-tts` |
| `gemini-2.5-pro-preview-tts` | 2025 年 5 月 20 日 | 2026 年 11 月 17 日 | `gemini-3.8-flash-tts` または `gemini-3.8-flash-lite-tts` |

## エンベディング モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `gemini-embedding-2` | 2026 年 4 月 22 日 | 提供終了日は未発表 |  |
| `gemini-embedding-001` | 2025 年 7 月 14 日 | 2028 年 5 月 14 日 | `gemini-embedding-2` |
| `text-embedding-004` | 2024 年 4 月 9 日 | 2026 年 1 月 14 日 | `gemini-embedding-2` |
| モデルをプレビュー | | | |
| `embedding-2-preview` | 2026 年 3 月 10 日 | 2026 年 8 月 10 日 | `gemini-embedding-2` |
| `embedding-001` | 2024 年 4 月 9 日 | 2025 年 10 月 30 日 | `gemini-embedding-2` |
| `embedding-gecko-001` |  | 2025 年 10 月 30 日 | `gemini-embedding-2` |
| `gemini-embedding-exp` |  | 2025 年 10 月 30 日 | `gemini-embedding-2` |
| `gemini-embedding-exp-03-07` |  | 2025 年 10 月 30 日 | `gemini-embedding-2` |

## Nano Banana モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `gemini-nano-banana-2.1` | 2026 年 10 月 6 日 | 提供終了日は未発表 |  |
| `gemini-3.1-flash-lite-image` | 2026 年 6 月 30 日 | 提供終了日は未発表 |  |
| `gemini-3.1-flash-image` | 2026 年 5 月 28 日 | 提供終了日は未発表 | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image` | 2026 年 5 月 28 日 | 提供終了日は未発表 |  |
| `gemini-2.5-flash-image` | 2025 年 10 月 2 日 | 2027 年 3 月 15 日 | `gemini-3.1-flash-lite-image` |
| モデルをプレビュー | | | |
| `gemini-3.1-flash-image-preview` | 2026 年 2 月 26 日 | 2026 年 6 月 25 日 | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image-preview` | 2025 年 11 月 20 日 | 2026 年 6 月 25 日 | `gemini-3-pro-image` |
| `gemini-2.5-flash-image-preview` | 2025 年 5 月 7 日 | 2026 年 1 月 15 日 | `gemini-nano-banana-2.1` |
| `gemini-2.0-flash-preview-image-generation` | 2025 年 5 月 7 日 | 2025 年 11 月 14 日 | `gemini-nano-banana-2.1` |

## Imagen モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替手段** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | 2025 年 6 月 24 日 | 2026 年 8 月 17 日 | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-001` | 2025 年 6 月 24 日 | 2026 年 8 月 17 日 | `gemini-nano-banana-2.1` |
| `imagen-4.0-fast-generate-001` | 2025 年 6 月 24 日 | 2026 年 8 月 17 日 | `gemini-nano-banana-2.1` |
| `imagen-3.0-generate-002` | 2025 年 2 月 6 日 | 2025 年 11 月 10 日 | `gemini-nano-banana-2.1` |
| モデルをプレビュー | | | |
| `imagen-4.0-generate-preview-06-06` | 2025 年 6 月 24 日 | 2026 年 2 月 17 日 | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-preview-06-06` | 2025 年 6 月 24 日 | 2026 年 2 月 17 日 | `gemini-nano-banana-2.1` |

## Veo モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | 2025 年 9 月 9 日 | 2026 年 6 月 30 日 | `gemini-omni-1.1-flash` または [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=ja) の GA モデル |
| `veo-3.0-fast-generate-001` | 2025 年 9 月 9 日 | 2026 年 6 月 30 日 | `gemini-omni-1.1-flash` または [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=ja) の GA モデル |
| `veo-2.0-generate-001` | 2025 年 4 月 9 日 | 2026 年 6 月 30 日 | `gemini-omni-1.1-flash` または [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=ja) の GA モデル |
| モデルをプレビュー | | | |
| `veo-3.1-lite-generate-preview` | 2026 年 3 月 31 日 | 2026 年 10 月 22 日 | `gemini-omni-1.1-flash` |
| `veo-3.1-generate-preview` | 2025 年 10 月 15 日 | 2026 年 10 月 22 日 | `gemini-omni-1.1-flash` |
| `veo-3.1-fast-generate-preview` | 2025 年 10 月 15 日 | 2026 年 10 月 22 日 | `gemini-omni-1.1-flash` |
| `veo-3.0-generate-preview` | 2025 年 7 月 31 日 | 2025 年 11 月 12 日 | `gemini-omni-1.1-flash` |
| `veo-3.0-fast-generate-preview` | 2025 年 7 月 31 日 | 2025 年 11 月 12 日 | `gemini-omni-1.1-flash` |

## Gemini Omni Flash モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `gemini-omni-1.1-flash` | 2026 年 8 月 27 日 | 提供終了日は未発表 |  |
| モデルをプレビュー | | | |
| `gemini-omni-flash-preview` | 2026 年 6 月 30 日 | 2026 年 10 月 22 日 | `gemini-omni-1.1-flash` |

## Lyria モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| `lyria-3.5` | 2026 年 9 月 3 日 | 提供終了日は未発表 |  |
| モデルをプレビュー | | | |
| `lyria-3-clip-preview` | 2026 年 3 月 25 日 | 提供終了日は未発表 |  |
| `lyria-3-pro-preview` | 2026 年 3 月 25 日 | 提供終了日は未発表 | `lyria-3.5` |
| `lyria-realtime-exp` | 2025 年 5 月 20 日 | 提供終了日は未発表 |  |

## ロボティクス モデル

| **モデル** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| モデルをプレビュー | | | |
| `gemini-robotics-er-2-preview` | 2026 年 7 月 30 日 | 提供終了日は未発表 |  |
| `gemini-robotics-er-2-streaming-preview` | 2026 年 7 月 30 日 | 提供終了日は未発表 |  |
| `gemini-robotics-er-1.6-preview` | 2026 年 4 月 14 日 | 2026 年 8 月 31 日 | `gemini-robotics-er-2-preview` |
| `gemini-robotics-er-1.5-preview` | 2025 年 9 月 25 日 | 2026 年 4 月 30 日 | `gemini-robotics-er-2-preview` |

## マネージド エージェント

| **エージェント** | **リリース日** | **提供終了日** | **推奨される代替サービス** |
| --- | --- | --- | --- |
| エージェントのプレビュー | | | |
| `antigravity-preview-09-2026` | 2026 年 9 月 17 日 | 提供終了日は未発表 |  |
| `deep-research-preview-04-2026` | 2026 年 4 月 21 日 | 提供終了日は未発表 |  |
| `deep-research-max-preview-04-2026` | 2026 年 4 月 21 日 | 提供終了日は未発表 |  |
| `deep-research-pro-preview-12-2025` | 2025 年 12 月 11 日 | 2026 年 10 月 23 日 | `deep-research-preview-04-2026` |
| `antigravity-preview-05-2026` | 2026 年 5 月 19 日 | 2026 年 10 月 5 日 | `antigravity-preview-09-2026` |

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-22 UTC。"],[],[]]
