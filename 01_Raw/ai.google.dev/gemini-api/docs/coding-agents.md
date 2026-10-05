---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja
fetched_at: 2026-10-05T06:32:24.634544+00:00
title: "Gemini MCP \u3068\u30b9\u30ad\u30eb\u3092\u4f7f\u7528\u3057\u3066\u30b3\u30fc\u30c7\u30a3\u30f3\u30b0 \u30a2\u30b7\u30b9\u30bf\u30f3\u30c8\u3092\u8a2d\u5b9a\u3059\u308b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini MCP とスキルを使用してコーディング アシスタントを設定する

AI コーディング アシスタントは強力ですが、制限があります。トレーニング データは特定の日付でカットオフされ、新しい API 機能や変更が欠落しています。Gemini 固有のドキュメントにアクセスできない場合、エージェントは最適化されたアプローチではなく、一般的なパターンを提案する可能性があります。

進化する Gemini API とその推奨される使用方法に合わせてコーディング アシスタントを最新の状態に保つには、**Gemini Docs MCP** を設定し、**Gemini API Skills** で環境を強化することをおすすめします。これらのツールは単独で使用できますが、完全なカバレッジを提供するために連携して動作するように設計されています。

## Gemini Docs MCP を接続する

Gemini は、`https://gemini-api-docs-mcp.dev` でパブリック Model Context Protocol（MCP）サーバーをホストします。コーディング エージェントをこのサーバーに接続すると、すべてのクエリが最新の API、コード アップデート、最適な構成例にアクセスできるようになります。

エージェントのターミナルまたはプロジェクト ルートで次のコマンドを実行して、サーバーをインストールします。

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

このサーバーは、エージェントが公式の Gemini ドキュメント ファイルからリアルタイムの API 定義と統合パターンを取得するために使用できる `search_documentation` 関数を追加します。

## API 開発スキルを追加する

スキルは、アシスタントのコンテキストに直接 **組み込みのルールとベスト プラクティス**（正しい SDK と現在のモデル バージョンの適用など）を提供します。このスキルは Gemini Docs MCP サービスと連携します。両方がインストールされている場合、このスキルはドキュメントに MCP サービスを使用します。MCP がインストールされていない場合でも、フォールバックとして `ai.google.dev` から [`/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=ja) を取得します（個々のページは、`.md.txt` を追加して未加工の Markdown として取得することもできます（例: `https://ai.google.dev/gemini-api/docs/speech-generation.md.txt`））。

これらのスキルをインストールするには、次のいずれかのサポートされているツールを使用します。両方のインストール手順は、各スキル モジュールの下に記載されています。

- **[skills.sh](https://skills.sh)**: 推奨。ポータブル エージェントの動作に関するオープン標準。
- **[Context7](https://context7.com)**: Context7 エコシステムをすでに利用しているユーザーが対象です。

### gemini-api-dev

[Gemini API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja)（Interactions API）を使用してアプリを構築するためのスキル。Interactions API は、Gemini モデルとエージェントを使用して構築する最もシンプルで最適な方法です。このスキルでは、次のことを学びます。

- テキスト生成、マルチターン チャット、ストリーミング
- 関数呼び出し、構造化された出力、画像生成
- バックグラウンド実行と Deep Research エージェント
- サーバーサイドの会話状態の管理
- 現在のモデルへのプロンプトのルーティングと非推奨モデルの回避
- Python と TypeScript の SDK パターン

#### skills.sh を使用してインストールする

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Context7 を使用してインストールする

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Gemini Live API を使用してリアルタイムの会話型 AI アプリケーションを構築するスキル。このスキルでは、次の項目に関するドキュメントとベスト プラクティスを提供します。

- 低レイテンシ ストリーミング用の WebSocket 接続
- 音声、動画、テキストのストリーミング
- 音声検出と割り込みのサポート

#### skills.sh を使用してインストールする

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Context7 を使用してインストールする

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

## インストールを確認する

インストール後、コーディング アシスタントが Gemini Docs MCP サーバーに接続し、インストールしたスキルを使用できることを確認します。

### 1. エージェントの動作を確認する

最も確実な方法は、Gemini API に関する技術的な質問をエージェントにすることです。

**プロンプト:** 「Gemini API でコンテキスト キャッシュ保存機能を使用するにはどうすればよいですか？」

セットアップが正常に完了すると、次のようになります。

- **正確なコードを提供する**: 最新のエンドポイントから `cacheContent` や `cachedContents.create` などの特定の Gemini メソッドを参照します。
- **MCP ツールを使用する**: **Gemini Docs MCP サーバー**に接続されていること、または `search_documentation` ツールを使用してデータを取得していることを示します。
- **読み込まれたスキルを呼び出す**: 「スキル: gemini-api-dev を使用中」というインジケーターを表示します（セカンダリ ラッパーに依存している場合）。

### 2. マニフェストとツールを確認する

エージェントが一般的な回答をした場合は、環境固有の Discovery コマンドまたは Status コマンドを使用して、Docs MCP またはスキルがメモリに読み込まれていることを確認します。

| 環境 | MCP の確認 | スキル検証 |
| --- | --- | --- |
| **Claude Code** | ターミナルに「`/mcp`」と入力して、アクティブなサーバーと `search_documentation` ツールを表示します。 | ターミナルで「`/skills`」と入力して、アクティブなすべてのマニフェストを一覧表示します。 |
| **Cursor** | **[設定] > [機能] > [MCP]** に移動します。サーバーが [接続済み] になっていることを確認します。 | [**設定] > [**ルール] を開きます。スキルが [Agent Decides] に表示されていることを確認します。 |
| **Antigravity** | [**カスタマイズ > 接続**] サイドバーで MCP のステータスを確認します。 | `/skills list` と入力するか、[**カスタマイズ**] > [ルール] サイドバーを確認します。 |
| **Gemini CLI** | `gemini mcp list` を実行するか、`/mcp list` を使用します。 | `gemini skills list` を実行するか、セッション内で `/skills` スラッシュ コマンドを使用します。 |
| **Copilot** | `@gemini /mcp` と入力して、アクティブなデータコネクタを一覧表示します。 | `@gemini /skills`（または `/skills`）と入力すると、有効な拡張機能が表示されます。 |

## トラブルシューティング

エージェントが一般的な情報しか提供しない場合や、Gemini 固有のメソッドを認識しない場合は、次のことを確認します。

### エージェントがスキルを検出できなかった

ほとんどのエージェントは、起動時にのみスキルをインデックス登録します。

**修正:** IDE（Cursor/VS Code）を完全に再起動するか、ターミナルベースのエージェント（Claude Code）を終了して再度開きます。

### グローバルな競合とローカルな競合

`--global` フラグを使用してインストールした場合、エージェントはプロジェクト固有のルールを優先して、このフラグを無視している可能性があります。

**修正:** グローバル フラグなしで、スキルをプロジェクト ルートに直接インストールしてみてください。

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## リソース

- [GitHub の Gemini API スキル](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja)
- [使ってみる](https://ai.google.dev/gemini-api/docs/get-started?hl=ja)
- [ライブラリ](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-24 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-24 UTC。"],[],[]]
