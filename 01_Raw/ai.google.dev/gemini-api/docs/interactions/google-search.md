---
source_url: https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ko
fetched_at: 2026-05-11T12:33:40.587398+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Google 검색을 사용한 그라운딩

Google 검색을 사용한 그라운딩은 Gemini 모델을 실시간 웹 콘텐츠에 연결하며 사용 가능한 모든 언어로 작동합니다. 이를 통해 Gemini는 지식 단절 시점 이후에 더 정확한 답변을 제공하고 검증 가능한 출처를 인용할 수 있습니다.

그라운딩을 사용하면 다음 작업을 할 수 있는 애플리케이션을 빌드할 수 있습니다.

- **사실에 기반한 정확성 향상:** 실제 정보를 기반으로 대답하여 모델 할루시네이션을 줄입니다.
- **실시간 정보 액세스:** 최근 이벤트 및 주제에 관한 질문에 대답합니다.
- **인용 제공:** 모델의 주장에 대한 출처를 표시하여 사용자 신뢰를 구축합니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

const modelStep = interaction.steps.find(s => s.type === 'model_output');
if (modelStep) {
  for (const contentBlock of modelStep.content) {
    if (contentBlock.type === 'text') console.log(contentBlock.text);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Google 검색을 사용한 그라운딩 작동 방식

`google_search` 도구를 사용 설정하면 모델이 정보 검색, 처리, 인용의 전체 워크플로를 자동으로 처리합니다.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ko)

1. **사용자 프롬프트:** 애플리케이션이 `google_search` 도구가 사용 설정된 상태로 사용자의 프롬프트를 Gemini API로 전송합니다.
2. **프롬프트 분석:** 모델이 프롬프트를 분석하고 Google 검색으로 대답을 개선할 수 있는지 확인합니다.
3. **Google 검색:** 필요한 경우 모델이 하나 이상의 검색어를 자동으로 생성하고 실행합니다.
4. **검색 결과 처리:** 모델이 검색 결과를 처리하고 정보를 합성하여 대답을 구성합니다.
5. **그라운딩된 대답:** API가 검색 결과에 그라운딩된 최종적인 사용자 친화적인 대답을 반환합니다. 이 대답에는 인용이 포함된 인라인 `annotations`가 있는 모델의 텍스트 대답과 검색어 및 추천 검색어가 있는 `google_search_call` 및 `google_search_result` 단계가 포함됩니다.

## 그라운딩 대답 이해

대답이 성공적으로 그라운딩되면 모델의 텍스트 출력에 텍스트 콘텐츠 블록에 직접 인라인 `annotations`가 포함됩니다. 이러한 주석은 대답의 일부를 출처에 연결하는 인용 정보를 제공합니다.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

대답의 주요 필드는 다음과 같습니다.

- `google_search_call` : 모델이 실행한 검색 `queries`를 포함합니다.
- `google_search_result` : UI에서 추천 검색어를 렌더링하기 위한 HTML 스니펫인 `search_suggestions`를 포함합니다. 전체 사용 요구사항은
  [서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko#grounding-with-google-search)에 자세히 설명되어 있습니다.
- `annotations`가 있는 `text` : 인라인 인용이 포함된 모델의 합성된 대답입니다. 각 `url_citation` 주석은 텍스트 세그먼트 (`start_index` 및 `end_index`로 정의됨)를 출처 URL에 연결합니다. 이는 인라인 인용을 빌드하는 데 핵심적인 요소입니다.

Google 검색을 사용한 그라운딩은 [URL
컨텍스트 도구](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ko)와 함께 사용하여
공개 웹 데이터와 제공하는 특정 URL 모두에서 대답을 그라운딩할 수도 있습니다.

## 인라인 인용으로 출처 기여 분석

API는 텍스트 콘텐츠 블록에 인라인 `url_citation` 주석을 반환하므로 사용자 인터페이스에서 출처를 표시하는 방식을 완전히 제어할 수 있습니다.
각 주석에는 텍스트의 어느 부분을 인용하는지 식별하는 `start_index`와 `end_index`가 포함됩니다. 이를 추출하고 표시하는 방법은 다음과 같습니다.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

출력에는 텍스트와 그 인용이 표시됩니다.

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## 가격 책정

Gemini 3에서 Google 검색을 사용한 그라운딩을 사용하면 모델이 실행하기로 결정한 각 검색어에 대해 프로젝트에 요금이 청구됩니다. 모델이 단일 프롬프트에 대답하기 위해
여러 검색어를 실행하기로 결정하는 경우 (예:
`"UEFA Euro 2024 winner"` 및 `"Spain vs England Euro 2024 final
score"`를 동일한 API 호출 내에서 검색) 이 요청에 대해 도구의 청구 가능한 사용 2회로 계산됩니다. 청구 목적으로 고유한 검색어를 계산할 때 빈 웹 검색어는 무시됩니다. 이 청구 모델은 Gemini 3 모델에만 적용됩니다. Gemini 2.5 또는 이전 모델에서 검색 그라운딩을 사용하면 프롬프트당 프로젝트에 요금이 청구됩니다.

자세한 가격 책정 정보는 [Gemini API 가격 책정
페이지](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)를 참고하세요.

## 지원되는 모델

모델 [개요](https://ai.google.dev/gemini-api/docs/models?hl=ko) 페이지에서 전체 기능을 확인할 수 있습니다.

| 모델 | Google 검색을 사용한 그라운딩 |
| --- | --- |
| Gemini 3.1 Flash Image 프리뷰 | ✔️ |
| Gemini 3.1 Pro 프리뷰 | ✔️ |
| Gemini 3 Pro Image 프리뷰 | ✔️ |
| Gemini 3 Flash 프리뷰 | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## 지원되는 도구 조합

[코드 실행](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=ko) 및
[URL 컨텍스트](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ko)와 같은 다른 도구와 함께 Google 검색을 사용한 그라운딩을 사용하여 더 복잡한
사용 사례를 지원할 수 있습니다.

Gemini 3 모델은 기본 제공 도구 (예: Google 검색을 사용한 그라운딩)와 커스텀 도구 (함수 호출)의 조합을 지원합니다. 도구 조합
 페이지에서 자세히 알아보세요.

## 다음 단계

- [함수 호출과 같은 사용 가능한 다른 도구에 대해 알아보세요.](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ko)
- [URL 컨텍스트 도구를 사용하여 특정 URL로 프롬프트를 보강하는 방법을 알아보세요.](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-07(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-07(UTC)"],[],[]]
