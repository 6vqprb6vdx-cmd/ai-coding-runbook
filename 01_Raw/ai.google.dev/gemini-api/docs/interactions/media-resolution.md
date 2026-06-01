---
source_url: https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=ko
fetched_at: 2026-06-01T19:49:00.244775+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 미디어 해상도

`media_resolution` 매개변수는 미디어 입력에 할당된 **최대 토큰 수** 를 결정하여 이미지, 동영상, PDF 문서와 같은 미디어 입력을 Gemini API가 처리하는 방식을 제어하므로 응답 품질과 지연 시간 및 비용 간의 균형을 맞출 수 있습니다. 다양한 설정, 기본값, 토큰과의 상호 관계는 [토큰 수](#token-counts) 섹션을 참고하세요.

요청 내에서 개별 미디어 객체 (콘텐츠 항목)의 미디어 해상도를 구성할 수 있습니다 (Gemini 3만 해당).

## 콘텐츠 항목별 미디어 해상도 (Gemini 3만 해당)

Gemini 3을 사용하면 요청 내에서 개별 미디어 객체의 미디어 해상도를 설정하여 토큰 사용을 세부적으로 최적화할 수 있습니다. 단일 요청에서 해상도 수준을 혼합할 수 있습니다. 예를 들어 복잡한 다이어그램에는 고해상도를 사용하고 간단한 컨텍스트 이미지에는 저해상도를 사용합니다.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## 사용 가능한 해상도 값

Gemini API는 미디어 해상도에 대해 다음 수준을 정의합니다.

- `unspecified`: 기본 설정입니다. 이 수준의 토큰 수는 Gemini 3과 이전 Gemini 모델 간에 크게 다릅니다.
- `low`: 토큰 수가 적어 처리 속도가 빠르고 비용이 저렴하지만 세부정보가 적습니다.
- `medium`: 세부정보, 비용, 지연 시간 간의 균형입니다.
- `high`: 토큰 수가 많아 모델이 사용할 수 있는 세부정보가 많지만 지연 시간과 비용이 증가합니다.
- `ultra_high` (콘텐츠 항목당만 해당): 토큰 수가 가장 많으며 [컴퓨터 사용](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=ko)과 같은 특정 사용 사례에 필요합니다.

`high`는 대부분의 사용 사례에서 최적의 성능을 제공합니다.

이러한 각 수준에 대해 생성되는 정확한 토큰 수는 **미디어 유형** (이미지, 동영상, PDF)과 **모델 버전** 에 따라 다릅니다.

## 토큰 수

아래 표에는 모델 계열별로 각 `media_resolution` 값과 미디어 유형에 대한 대략적인 토큰 수가 요약되어 있습니다.

**Gemini 3 모델**

| MediaResolution | 이미지 | 동영상 | PDF |
| --- | --- | --- | --- |
| `unspecified` (기본값) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + 기본 텍스트 |
| `medium` | 560 | 70 | 560 + 기본 텍스트 |
| `high` | 1120 | 280 | 1,120 + 기본 텍스트 |
| `ultra_high` | 2240 | 해당 사항 없음 | 해당 사항 없음 |

## 적합한 해상도 선택하기

- **기본값 (`unspecified`):** 기본값으로 시작합니다. 가장 일반적인 사용 사례에서 품질, 지연 시간, 비용 간의 균형을 맞추도록 조정됩니다.
- **`low`:** 비용과 지연 시간이 가장 중요하고 세부정보가 덜 중요한 시나리오에 사용합니다.
- **`medium` / `high`:** 태스크에서 미디어 내의 복잡한 세부정보를 이해해야 하는 경우 해상도를 높입니다. 이는 복잡한 시각적 분석, 차트 읽기 또는 밀도 높은 문서 이해에 필요한 경우가 많습니다.
- **`ultra_high`** - 콘텐츠 항목별 설정에만 사용할 수 있습니다. 컴퓨터 사용과 같은 특정 사용 사례 또는 테스트에서 `high`보다 명확한 개선이 확인되는 경우에 권장됩니다.
- **콘텐츠 항목별 제어 (Gemini 3):** 토큰 사용을 최적화합니다. 예를 들어 이미지가 여러 개 포함된 프롬프트에서 복잡한 다이어그램에는 `high`를 사용하고 더 간단한 컨텍스트 이미지에는 `low` 또는 `medium`을 사용합니다.

**권장 설정**

다음은 지원되는 각 미디어 유형에 권장되는 미디어 해상도 설정을 나열한 것입니다.

| 미디어 유형 | 권장 설정 | 최대 토큰 수 | 사용 안내 |
| --- | --- | --- | --- |
| **이미지** | `high` | 1120 | 최대 품질을 보장하기 위해 대부분의 이미지 분석 작업에 권장됩니다. |
| **PDF** | `medium` | 560 | 문서 이해에 최적입니다. 품질은 일반적으로 `medium`에서 포화됩니다. `high`로 늘려도 표준 문서의 OCR 결과가 개선되는 경우는 거의 없습니다. |
| **동영상** (일반) | `low` (또는 `medium`) | 70 (프레임당) | **참고:** 동영상의 경우 컨텍스트 사용을 최적화하기 위해 `low` 및 `medium` 설정이 동일하게 처리됩니다 (70개 토큰). 이는 대부분의 동작 인식 및 설명 작업에 충분합니다. |
| **동영상** (텍스트가 많은 경우) | `high` | 280 (프레임당) | 사용 사례에 밀도 높은 텍스트 (OCR) 또는 동영상 프레임 내의 작은 세부정보를 읽는 것이 포함되는 경우에만 필요합니다. |

항상 다양한 해상도 설정이 애플리케이션에 미치는 영향을 테스트하고 평가하여 품질, 지연 시간, 비용 간의 최적의 절충점을 찾으세요.

## 버전 호환성 요약

- 개별 콘텐츠 항목에 `resolution`을 설정하는 것은 **Gemini 3 모델에만 해당** 됩니다.

## 다음 단계

- [이미지 이해](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=ko), [동영상 이해](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ko), [문서 이해](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=ko) 가이드에서 Gemini API의 멀티모달 기능에 대해 자세히 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-28(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-28(UTC)"],[],[]]
