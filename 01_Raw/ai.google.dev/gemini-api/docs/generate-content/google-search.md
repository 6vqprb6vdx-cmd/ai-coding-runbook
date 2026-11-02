---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=ja
fetched_at: 2026-11-02T07:30:25.317658+00:00
title: "Google \u691c\u7d22\u306b\u3088\u308b\u30b0\u30e9\u30a6\u30f3\u30c7\u30a3\u30f3\u30b0 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# Google 検索によるグラウンディング

Google 検索によるグラウンディングは、Gemini モデルをリアルタイムのウェブ コンテンツに接続し、利用可能なすべての言語で機能します。これで、Gemini はより正確な回答を提供して、ナレッジ カットオフ以降の検証可能な情報源を引用することができます。

グラウンディングを使用すると、次のようなアプリケーションを構築できます。

- **事実の正確性を高める:** 実世界の情報に基づいて回答を生成することで、モデルのハルシネーションを軽減します。
- **リアルタイムの情報にアクセスする:** 最近の出来事やトピックに関する質問に答えます。
- **引用を提供する:** モデルの主張のソースを示すことで、ユーザーの信頼を構築します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

詳しくは、[検索ツール ノートブック](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ja)をお試しください。

## Google 検索によるグラウンディングの仕組み

`google_search` ツールを有効にすると、モデルは情報の検索、処理、引用のワークフロー全体を自動的に処理します。

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ja)

1. **ユーザー プロンプト:** アプリケーションは、`google_search` ツールを有効にして、ユーザーのプロンプトを Gemini API に送信します。
2. **プロンプト分析:** モデルはプロンプトを分析し、Google 検索で回答を改善できるかどうかを判断します。
3. **Google 検索:** 必要に応じて、モデルは 1 つまたは複数の検索クエリを自動的に生成して実行します。
4. **検索結果の処理:** モデルは検索結果を処理し、情報を合成して、回答を作成します。
5. **グラウンディングされたレスポンス:** API は、検索結果に基づいてグラウンディングされた、ユーザー フレンドリーな最終レスポンスを返します。このレスポンスには、モデルのテキスト回答と、検索クエリ、ウェブ検索結果、引用を含む `groundingMetadata` が含まれます。

## グラウンディング レスポンスについて

レスポンスが正常にグラウンディングされると、レスポンスに `groundingMetadata` フィールドが含まれます。この構造化データは、アプリケーションで主張を検証し、豊富な引用エクスペリエンスを構築するために不可欠です。

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Gemini API は、`groundingMetadata` とともに次の情報を返します。

- `webSearchQueries` : 使用された検索クエリの配列。これは、モデルの推論プロセスのデバッグと理解に役立ちます。
- `searchEntryPoint` : 必要な検索候補をレンダリングするための HTML と CSS が含まれています。使用要件の詳細については、[利用規約](https://ai.google.dev/gemini-api/terms?hl=ja#grounding-with-google-search)をご覧ください。
- `groundingChunks` : ウェブソース（`uri` と `title`）を含むオブジェクトの配列。
- `groundingSupports` : モデル レスポンス `text` を `groundingChunks` のソースに接続するチャンクの配列。各チャンクは、テキスト `segment`（`startIndex` と `endIndex` で定義）を 1 つ以上の `groundingChunkIndices` にリンクします。これは、インライン引用を構築するための鍵となります。

Google 検索によるグラウンディングは、[URL コンテキスト ツール](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)と組み合わせて使用することもできます。これにより、一般公開されているウェブデータと、指定した特定の URL の両方でレスポンスをグラウンディングできます。

## インライン引用によるソースの帰属

API は構造化された引用データを返すため、ユーザー インターフェースでソースを表示する方法を完全に制御できます。`groundingSupports` フィールドと `groundingChunks` フィールドを使用すると、モデルのステートメントをソースに直接リンクできます。以下は、メタデータを処理して、クリック可能なインライン引用を含むレスポンスを作成する一般的なパターンです。

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

インライン引用を含む新しい回答は、たとえば次のようになります。

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## 料金

Gemini 3 以降のモデルで Google 検索によるグラウンディングを使用すると、モデルが実行を決定した検索クエリごとにプロジェクトに課金されます。このクエリごとの課金モデルには、すべての Gemini 3 以降のモデルで共有される 1 か月あたり 5,000 件の無料検索リクエストが含まれています。その後、**1,000 件の検索リクエストあたり $14** の費用がかかります。

たとえば、モデルが 1 つのプロンプトに回答するために複数の検索クエリを実行することを決定した場合（同じ API 呼び出し内で `"UEFA Euro 2024 winner"` と `"Spain vs
England Euro 2024 final score"` を検索するなど）、そのリクエストに対してツールの課金対象の使用が 2 回カウントされます。請求目的で、一意のクエリをカウントする際に、空のウェブ検索クエリは無視されます。

Gemini 2.5 以前のモデルで検索グラウンディングを使用すると、プロジェクトはプロンプトごとに課金されます。

詳しい料金情報については、[Gemini API の料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)をご覧ください。

## サポートされているモデル

完全な機能については、[モデルの概要](https://ai.google.dev/gemini-api/docs/models?hl=ja)ページをご覧ください。

| モデル | Google 検索によるグラウンディング |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image プレビュー版 | ✔️ |
| Gemini 3.1 Pro プレビュー版 | ✔️ |
| Gemini 3 Pro Image プレビュー | ✔️ |
| Gemini 3 Flash プレビュー | ✔️ |
| Gemini 3.1 Flash-Lite プレビュー版 | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## サポートされているツールの組み合わせ

Google 検索によるグラウンディングを、[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)、[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)、[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)（Gemini 3.5 Flash-Lite 以降のモデルでサポート）などの他のツールと組み合わせて使用することで、より複雑なユースケースに対応できます。Gemini 3 モデルは、これらの組み込みツールとカスタムツール（関数呼び出し）の組み合わせもサポートしています。詳しくは、[ツールの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)のページをご覧ください。

## 次のステップ

- [Gemini API クックブックの Google 検索によるグラウンディング](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ja)を試す。
- [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)など、利用可能な他のツールについて学習する。
- [URL コンテキスト ツール](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)を使用して、特定の URL でプロンプトを拡張する方法を学習する。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-29 UTC。"],[],[]]
