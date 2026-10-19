---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=ja
fetched_at: 2026-10-19T05:45:07.199150+00:00
title: "API \u30a8\u30e9\u30fc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# API エラー

このページでは、すべての Interactions API エラーコードのリファレンス、エラー レスポンスの形式、さまざまなリクエスト タイプに対して API がエラーを返す方法について説明します。

## 標準 API エラーコード

これらの一般的なリクエストレベルのエラーコードは、標準の HTTP ステータス コードに対応しています。アプリケーション ロジックの `code` フィールドを使用して、エラーをプログラムで処理します。

| コード | HTTP ステータス | 説明 | 推奨される対処方法 |
| --- | --- | --- | --- |
| `invalid_request` | 400 無効なリクエスト | リクエスト ペイロードの形式が正しくないか、無効なパラメータが含まれています。 | [API リファレンス](https://ai.google.dev/api/interactions-api?hl=ja)でリクエストの構文とパラメータを確認します。 |
| `failed_precondition` | 400 無効なリクエスト | 前提条件（課金が無効になっているなど）が満たされていないため、リクエストを処理できません。 | プロジェクトの課金ステータスまたはアカウントの前提条件を確認します。 |
| `out_of_range` | 416 リクエストされた範囲内にありません | リクエスト パラメータが有効な範囲外です。 | パラメータ値と上限を確認します。 |
| `parameter_unknown` | 400 無効なリクエスト | リクエストに不明なパラメータが含まれています。 | 認識されないパラメータを削除して、もう一度お試しください。 |
| `authentication` | 401 未認証 | API キーがない、無効である、または期限切れです。 | [API キー](https://ai.google.dev/gemini-api/docs/api-key?hl=ja)を確認します。 |
| `payment_required` | 402 支払いが必要です | 前払いクレジットの残高がなくなりました。 | 請求先アカウントに[クレジットを追加](https://ai.google.dev/gemini-api/docs/billing?hl=ja#buy-credits)するか、[オートチャージ](https://ai.google.dev/gemini-api/docs/billing?hl=ja#auto-reload)をオンにします。再試行しない: クレジットが追加されるまでリクエストは成功しません。 |
| `permission_denied` | 403 禁止 | API キーにこのリソースに対する権限がありません。 | API キーの権限とプロジェクトへのアクセス権を確認します。 |
| `not_found` | 404 見つかりません | リクエストされたリソースが見つかりませんでした。 | リソースパスとパラメータを確認します。 |
| `model_not_found` | 404 見つかりません | 指定されたモデルが見つかりませんでした。 | モデル名を確認するか、別のモデルにフォールバックします。 |
| `already_exists` | 409 競合しています。 | 作成しようとしたエンティティはすでに存在します。 | リソースを再作成する前に、リソースがすでに存在するかどうかを確認します。 |
| `aborted` | 409 競合しています。 | 競合または同時実行チェックの失敗により、オペレーションが中止されました。 | より高いアプリケーション レベルでリクエストを再試行します。 |
| `rate_limit_exceeded` | 429 Too Many Requests（リクエスト数が多すぎる） | 1 分あたりまたは 1 秒あたりのリクエスト数またはトークンの上限を超えています。 | 指数バックオフを利用して、待機と再試行を繰り返してください。 |
| `quota_exceeded` | 429 Too Many Requests（リクエスト数が多すぎる） | 1 日の割り当てを超過しました。 | 割り当てがリセットされるまで待つか、割り当ての増加をリクエストします。 |
| `too_many_requests` | 429 Too Many Requests（リクエスト数が多すぎる） | 短時間にリクエストが多すぎます。 | 指数バックオフを利用して、待機と再試行を繰り返してください。 |
| `cancelled` | 499 クライアントがリクエストをクローズしました | クライアントがリクエストの完了前にキャンセルしました。 | 何もする必要はない。通常、これはクライアントが切断されたことを意味します。 |
| `api_error` | 500 Internal Server Error（内部サーバーエラー） | サーバーで予期しないエラーが発生しました。 | リクエストを再試行します。問題が解決しない場合は、サポートにお問い合わせください。 |
| `unimplemented` | 501 実装されていません | オペレーションまたは機能が実装されていないか、サポートされていません。 | API の機能を確認するか、サポートされている機能に切り替えます。 |
| `service_unavailable` | 503 Service Unavailable（サービス利用不可） | サービスが一時的に過負荷状態になっているか、ダウンしています。 | 指数バックオフを利用して、待機と再試行を繰り返してください。 |
| `deadline_exceeded` | 504 Gateway Timeout（ゲートウェイ タイムアウト） | 期限内にリクエストが完了しませんでした。 | クライアントの期限設定を削除または延長して、サーバーのデフォルトを使用します。 |

## 生成がブロックされたコード

これらのエラーコードは、ポリシー、安全性、コンテンツの制限によりモデルの出力がブロックされたことを示します。これらのコードを受け取った場合は、入力を変更して再試行してください。

| コード | 説明 |
| --- | --- |
| `safety` | 安全性違反（有害なコンテンツ）によりリクエストがブロックされました。 |
| `recitation` | 著作権または朗読の制限によりリクエストがブロックされました。 |
| `language` | サポートされていない言語のため、リクエストがブロックされました。 |
| `prohibited_content` | 禁止コンテンツに関するガイドラインにより、リクエストがブロックされました。 |
| `spii` | 個人を特定できる機密情報の制限により、リクエストがブロックされました。 |
| `blocklist` | ブロックリストの禁止用語によりリクエストがブロックされました。 |
| `image_safety` | 安全性の違反により、画像の生成がブロックされました。 |
| `image_prohibited_content` | 禁止コンテンツに関するガイドラインにより、画像の生成がブロックされました。 |
| `image_recitation` | 著作権または朗読の制限により、画像の生成がブロックされました。 |
| `image_other` | 不明な理由で画像の生成がブロックされました。 |
| `content_blocked` | 指定されていないポリシーの理由により、リクエストがブロックされました。 |

## 生成エラーコード

これらのエラーコードは、モデルの生成された出力の構造上の問題（形式が正しくない関数呼び出しや未宣言のツール呼び出しなど）を示します。

| コード | 説明 |
| --- | --- |
| `malformed_function_call` | モデルが解析できない関数呼び出しを生成しました。 |
| `malformed_tool_call` | モデルが解析できないツール呼び出しを生成しました。 |
| `unexpected_tool_call` | モデルが、リクエストで宣言されていないツールを呼び出しました。 |
| `no_image` | モデルで画像を生成できませんでした。 |
| `too_many_tool_calls` | モデルが許可されている数を超えるツール呼び出しを生成しました。 |
| `missing_thought_signature` | レスポンスに必須の思考署名がありません。 |

## エラー レスポンスの形式

Interactions API からのエラーはすべて、`code` と `message` を含む `error` オブジェクトを返します。たとえば、サポートされていないツールタイプを渡すと、次の値が返されます。

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| フィールド | タイプ | 説明 |
| --- | --- | --- |
| `code` | 文字列 | `snake_case` の機械可読エラーコード。 |
| `message` | 文字列 | 何が問題だったのかを人が読める形式で説明します。 |

## エラーの配信方法

API は、標準の HTTP リクエストを行うか、ストリーミング（SSE）リクエストを行うかによって、エラーの配信方法が異なります。

### 標準 HTTP リクエスト

標準（ストリーミング以外）のリクエストの場合、API は HTTP レスポンス ステータス コード（`400 Bad Request`、`401 Unauthorized`、`429 Too Many Requests` など）を設定し、JSON レスポンス本文で `error` オブジェクトを返します。

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### ストリーミング（SSE）リクエスト

ストリーミング リクエスト（`stream: true`）の場合、API は `event_type` が `"error"` に設定されたサーバー送信イベント（SSE）ストリームを介してエラー イベントを送信します。`error` フィールドには、同じ `code` 構造と `message` 構造が含まれます。

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

SSE イベント スキーマの詳細については、[Interactions API リファレンス](https://ai.google.dev/api/interactions-api?hl=ja)をご覧ください。

## 次のステップ

- [API のトラブルシューティング](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=ja): 一般的な問題とエラー シナリオを解決します。
- [レート制限](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja): リクエストの上限と割り当ての処理について学習します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-20 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-20 UTC。"],[],[]]
