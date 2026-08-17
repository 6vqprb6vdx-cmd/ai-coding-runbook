---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=ko
fetched_at: 2026-08-17T02:19:04.801559+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

이제 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)가 정식 버전으로 출시되었습니다. 이 API를 사용하여 모든 최신 기능과 모델에 액세스하는 것이 좋습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini Robotics ER

Gemini Robotics ER (embodied reasoning) 모델은 로봇이 실제 세계를 인식하고 상호작용할 수 있도록 지원하는 비전 언어 모델(VLM)입니다. 시각적 데이터를 해석하고, 공간 및 시간 추론을 수행하고, 다단계 작업을 계획하고, 로봇과 도구를 조정합니다.

## 모델

Gemini Robotics ER 2 모델은 Gemini Robotics의 최신 모델입니다.
로봇이 환경을 정확하게 이해할 수 있도록 지원하는 업데이트된 추론 모델입니다. 이 모델은 로봇의 에이전트 오케스트레이션 (예: VLA 사용), 진행 상황 이해 및 성공 감지를 비롯한 로봇 동영상 이해, 계기판 읽기, 가리키기, 공간 추론과 같은 체화된 추론 기능에 특화되어 있습니다.

Gemini Robotics ER 2 모델에는 다음과 같은 두 가지 모델 엔드포인트가 도입되었습니다.

- **`gemini-robotics-er-2-preview`**: 표준 ER 2 모델입니다. 향상된 공간 추론, 동영상 순간 찾기, 동영상 진행 상황 분류, 다중 로봇 오케스트레이션, 다단계 도구 사용을 통해 Gemini 3.5 Flash를 기반으로 합니다.
- **`gemini-robotics-er-2-streaming-preview`**: [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ko)를 통한 실시간 스트리밍에 최적화되어 있습니다. 연속 오디오 및 동영상 입력을 처리하는 짧은 지연 시간 로봇 에이전트에 이 모델을 사용합니다.

Gemini Robotics ER 1.6을 사용하는 경우 API 호출에서 `model="gemini-robotics-er-1.6-preview"`을 `model="gemini-robotics-er-2-preview"` 또는 `model="gemini-robotics-er-2-streaming-preview"`로 대체하여 Gemini Robotics ER 2로 업그레이드하세요. Gemini Robotics ER 1.6 모델은 [8월 말](https://ai.google.dev/gemini-api/docs/deprecations?hl=ko#robotics-models)에 종료됩니다.

[Google AI Studio에서 Gemini Robotics ER 2 사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=ko)

## 로봇 기능

Gemini Robotics ER은 다양한 체화된 추론 기능을 지원합니다.
기능을 선택하여 자세히 알아보세요.

| 기능 | 설명 | 가이드 |
| --- | --- | --- |
| 공간 추론 | 객체를 가리키고, 동영상에서 추적하고, 경계 상자로 감지하고, 궤적을 계획합니다. | [공간 추론](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=ko) |
| 에이전트형 비전 | 코드 실행을 사용하여 이미지 조작 도구를 활용하여 다른 기능을 개선합니다. | [에이전트형 비전](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=ko) |
| 태스크 조정 | 공간 추론을 맞춤 로봇 API와 결합하여 장기 작업을 완료합니다. | [작업 조정](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=ko) |
| 스트리밍 (Gemini Robotics ER 2 스트리밍 엔드포인트만 해당) | 지연 시간이 짧은 함수 호출을 사용하는 실시간 로봇 에이전트를 위한 양방향 스트리밍 | [로봇 공학 스트리밍](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ko) |
| 동영상 진행률 (Gemini Robotics ER 2만 해당) | 연속 동영상 피드에서 순간 찾기 및 진행 상황 분류 | [동영상 이해](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=ko) |

## 시작하기

다음 예에서는 이미지에서 객체를 찾아 정규화된 2D 좌표와 라벨을 반환합니다. 이 출력을 로봇 공학 API나 VLA 모델에 직접 전달하여 로봇 작업을 생성할 수 있습니다.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

출력은 객체를 포함하는 JSON 배열이며, 각 객체에는 `point`(정규화된 `[y, x]` 좌표)와 객체를 식별하는 `label`가 있습니다.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

다음 이미지는 이러한 포인트를 표시하는 방법을 보여주는 예입니다.

![이미지에서 객체의 점을 표시하는 예](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=ko)

## 작동 방식

Gemini Robotics ER은 자연어 프롬프트로 이미지, 동영상 또는 오디오 입력을 받습니다. 객체를 식별하고, 장면 컨텍스트와 공간 관계를 추론하며, 좌표나 경계 상자와 같은 구조화된 출력을 반환합니다.

Gemini Robotics ER은 에이전트 기능도 제공합니다. 복잡한 작업을 하위 작업으로 나누고 로봇 함수를 호출하거나 생성된 코드를 실행하여 작업을 실행합니다. 예를 들어 '사과를 그릇에 넣어'는 찾기, 잡기, 놓기 단계의 시퀀스가 됩니다.

Gemini가 도구 호출을 실행하는 방법에 관한 자세한 내용은 [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ko#how-it-works)을 참고하세요.

## 안전

Gemini Robotics ER은 안전을 고려하여 제작되었지만 로봇 주변의 안전한 환경을 유지하는 것은 사용자의 책임입니다. 생성형 AI 모델은 실수를 할 수 있으며, 물리적 로봇은 손상을 일으킬 수 있습니다. 자세한 내용은 [Google DeepMind 로봇 공학 안전 페이지](https://deepmind.google/models/gemini-robotics/safety?hl=ko)를 참고하세요.

## 권장사항

1. 간단하고 자연스러운 언어를 사용하세요. 사람에게 말하듯이 로봇이 수행할 작업을 설명하세요. 용어가 작동하지 않으면 일반적인 동의어를 사용해 보세요.
2. 시각적 입력 최적화 이미지를 보내기 전에 작거나 불분명한 객체를 자르거나 확대합니다. 조명과 낮은 색상 대비는 감지에 영향을 미칠 수 있습니다.
3. 복잡한 작업을 단계별로 나눕니다. 모델이 집중하고 정확도를 높일 수 있도록 각 단계를 별도의 프롬프트로 전송하세요.
4. 고정밀 작업의 경우 여러 번 쿼리하고 결과를 평균화합니다. 이 컨센서스 접근 방식은 공간 출력의 분산을 줄입니다.

## 제한사항

Gemini Robotics ER로 개발할 때는 다음 제한사항을 고려하세요.

- **API 키 제한:** Gemini API는 제한되지 않은 API 키의 요청을 허용하지 않으며 `403 Forbidden` 오류를 반환합니다. [AI Studio](https://aistudio.google.com/api-keys?hl=ko)에서 제한사항을 추가하여 API 키를 보호하세요.
  자세한 내용은 [제한되지 않은 API 키 보안](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#secure-unrestricted-keys)을 참고하세요.
- **지연 시간과 성능:** 복잡한 질문, 고해상도 입력 또는 높은 사고 수준은 처리 시간을 늘릴 수 있습니다. 사고 수준의 경우 지연 시간과 성능 간의 균형을 맞추려면 중간을 사용하세요.
- **할루시네이션:** 모든 대규모 언어 모델과 마찬가지로 Gemini Robotics ER 모델도 때때로 '할루시네이션'을 일으키거나 잘못된 정보를 제공할 수 있습니다. 특히 모호한 프롬프트나 분포 외 입력의 경우에 그렇습니다.
- **프롬프트 품질에 대한 의존성:** 출력 품질은 입력 프롬프트의 명확성에 따라 달라집니다. 구체적이고 잘 구성된 프롬프트를 사용하세요.
- **계산 비용:** 특히 동영상 입력 또는 높은 `thinking_budget`로 모델을 실행하면 컴퓨팅 리소스가 소비되고 비용이 발생합니다.
  자세한 내용은 [생각하기](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ko) 페이지를 참고하세요.
- **입력 유형:** 각 모드의 제한사항에 관한 자세한 내용은 다음 주제를 참고하세요.
  - [이미지 입력](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=ko#technical-details-image)
  - [동영상 입력](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ko#supported-formats)
  - [오디오 입력](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ko#supported-formats)

## 개인정보처리방침

귀하는 이 문서에 언급된 모델('로봇 공학 모델')이 귀하의 지시에 따라 하드웨어를 작동하고 이동하기 위해 동영상 및 오디오 데이터를 활용한다는 점을 인정합니다. 따라서 음성, 이미지, 유사성 데이터 ('개인 정보')와 같은 식별 가능한 개인의 데이터가 로봇 모델에 의해 수집되도록 로봇 모델을 작동할 수 있습니다. 귀하가 개인 정보를 수집하는 방식으로 로봇 모델을 운영하기로 선택한 경우, 식별 가능한 개인이 [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=ko)에 있는 Gemini API 추가 서비스 약관('약관')에 설명된 대로, 'Google에서 데이터를 사용하는 방식' 섹션에 따라 Google에 개인 정보가 제공되고 사용될 수 있다는 사실을 충분히 통지받고 이에 동의하지 않는 한, 식별 가능한 개인이 로봇 모델과 상호작용하거나 로봇 모델 주변에 있는 것을 허용하지 않는 데 동의합니다. 귀하는 이러한 알림이 '약관'에 명시된 대로 '개인 정보'의 수집 및 사용을 허용하도록 보장하며, 얼굴 흐리게 처리와 같이 식별 가능한 사람이 포함되지 않은 영역에서 '로봇 모델'을 운영하는 등의 기법을 사용하여 '개인 정보'의 수집 및 배포를 최소화하기 위해 상업적으로 합당한 노력을 기울입니다.

## 가격 책정

가격 및 사용 가능한 지역에 관한 자세한 내용은 [가격](https://ai.google.dev/gemini-api/docs/pricing?hl=ko) 페이지를 참고하세요.

## 모델 엔드포인트

### Gemini Robotics ER 2 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | `gemini-robotics-er-2-preview` |
| save지원되는 데이터 유형 | **입력**  텍스트, 이미지, 동영상, 오디오  **출력**  텍스트 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  131,072  **출력 토큰 한도**  65,536 |
| handyman기능 | **[오디오 생성](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)**  지원되지 않음  **[캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)**  지원됨  **[코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)**  지원됨  **[컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)**  지원됨  **[파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)**  지원됨  **[함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)**  지원됨  **[Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)**  지원됨  **[이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)**  지원되지 않음  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ko)**  지원되지 않음  **[검색 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)**  지원됨  **[구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)**  지원됨  **[사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)**  지원됨  **[URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)**  지원됨 |
| speed소비 옵션 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)**  지원됨  **[유연한 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)**  지원되지 않음  **[우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)**  지원되지 않음 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 미리보기: `gemini-robotics-er-2-preview` |
| calendar\_month최신 업데이트 | 2026년 7월 |
| id\_card모델 카드 | [모델 카드](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ko) |

### Gemini Robotics ER 2 스트리밍 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | `gemini-robotics-er-2-streaming-preview` |
| save지원되는 데이터 유형 | **입력**  텍스트, 이미지, 동영상, 오디오  **출력**  텍스트 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  131,072  **출력 토큰 한도**  65,536 |
| handyman기능 | **[오디오 생성](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)**  지원되지 않음  **[캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)**  지원되지 않음  **[코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)**  지원되지 않음  **[컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)**  지원되지 않음  **[파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)**  지원되지 않음  **[함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)**  지원됨  **[Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)**  지원되지 않음  **[이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)**  지원되지 않음  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ko)**  지원됨  **[검색 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)**  지원됨  **[구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)**  지원되지 않음  **[사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)**  지원됨  **[URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)**  지원되지 않음 |
| speed소비 옵션 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)**  지원되지 않음  **[유연한 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)**  지원되지 않음  **[우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)**  지원되지 않음 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 미리보기: `gemini-robotics-er-2-streaming-preview` |
| calendar\_month최신 업데이트 | 2026년 7월 |
| id\_card모델 카드 | [모델 카드](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ko) |

### Gemini Robotics ER 1.6 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | `gemini-robotics-er-1.6-preview` |
| save지원되는 데이터 유형 | **입력**  텍스트, 이미지, 동영상, 오디오  **출력**  텍스트 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  131,072  **출력 토큰 한도**  65,536 |
| handyman기능 | **[오디오 생성](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)**  지원되지 않음  **[캐싱](https://ai.google.dev/gemini-api/docs/caching?hl=ko)**  지원됨  **[코드 실행](https://ai.google.dev/gemini-api/docs/code-execution?hl=ko)**  지원됨  **[컴퓨터 사용](https://ai.google.dev/gemini-api/docs/computer-use?hl=ko)**  지원됨  **[파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko)**  지원됨  **[함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)**  지원됨  **[Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ko)**  지원됨  **[이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)**  지원되지 않음  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ko)**  지원되지 않음  **[검색 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)**  지원됨  **[구조화된 출력](https://ai.google.dev/gemini-api/docs/structured-output?hl=ko)**  지원됨  **[사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)**  지원됨  **[URL 컨텍스트](https://ai.google.dev/gemini-api/docs/url-context?hl=ko)**  지원됨 |
| speed소비 옵션 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko)**  지원됨  **[유연한 추론](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ko)**  지원되지 않음  **[우선순위 추론](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ko)**  지원되지 않음 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 미리보기: `gemini-robotics-er-1.6-preview` |
| calendar\_month최신 업데이트 | 2025년 12월 |
| cognition\_2지식 단절 | 2025년 1월 |

## 다음 단계

- [공간 추론](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=ko): 가리키기, 추적, 경계 상자, 궤적
- [에이전트 기능](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=ko): 코드 실행, 계측기 읽기, 이미지 주석
- [작업 조정](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=ko): 맞춤 로봇 API를 사용하는 장기 작업
- [스트리밍을 사용하는 로봇 공학](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ko): 실시간 양방향 스트리밍 (Gemini Robotics ER 2만 해당)
- [동영상 이해](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=ko): 순간 찾기 및 진행 상황 분류 (Gemini Robotics ER 2만 해당)
- [Google DeepMind 로봇공학 안전](https://deepmind.google/models/gemini-robotics/safety?hl=ko) - 모델 제품군의 안전 연구

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-07-30(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-07-30(UTC)"],[],[]]
