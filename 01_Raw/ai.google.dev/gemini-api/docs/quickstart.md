---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=ko
fetched_at: 2026-05-11T12:35:40.749138+00:00
title: "Gemini API \ube60\ub978 \uc2dc\uc791 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API 빠른 시작

이 빠른 시작에서는 [라이브러리](https://ai.google.dev/gemini-api/docs/libraries?hl=ko)
를 설치하고 첫 번째 Gemini API 요청을 만드는 방법을 보여줍니다.

## 시작하기 전에

Gemini API를 사용하려면 API 키가 필요합니다. 무료로 API 키를 만들어 시작할 수 있습니다.

[Gemini API 키 만들기](https://aistudio.google.com/app/apikey?hl=ko)

## Google GenAI SDK 설치

### Python

[Python 3.9+](https://www.python.org/downloads/) 이상을 사용하여 다음
[pip 명령어](https://packaging.python.org/en/latest/tutorials/installing-packages/)를 사용하여
[`google-genai` 패키지](https://pypi.org/project/google-genai/)를 설치합니다.

```
pip install -q -U google-genai
```

### JavaScript

[Node.js v18+](https://nodejs.org/en/download/package-manager)을 사용하여 다음
[npm 명령어](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)를 사용하여
[TypeScript 및 JavaScript용 Google 생성형 AI SDK](https://www.npmjs.com/package/@google/genai)를 설치합니다.

```
npm install @google/genai
```

### Go

[go get 명령어를 사용하여 모듈 디렉터리에
[google.golang.org/genai](https://pkg.go.dev/google.golang.org/genai)를 설치합니다
:](https://go.dev/doc/code)

```
go get google.golang.org/genai
```

### Java

Maven을 사용하는 경우 종속 항목에 다음을 추가하여
[google-genai](https://github.com/googleapis/java-genai)를 설치할 수 있습니다.

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

[googleapis/go-genai](https://googleapis.github.io/dotnet-genai/)를 모듈 디렉터리에 [dotnet add 명령어를](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add) 사용하여 설치합니다.

```
dotnet add package Google.GenAI
```

### Apps Script

1. 새 Apps Script 프로젝트를 만들려면
   [script.new](https://script.google.com/u/0/home/projects/create?hl=ko)로 이동합니다.
2. **제목 없는 프로젝트** 를 클릭합니다.
3. Apps Script 프로젝트의 이름을 **AI Studio** 로 바꾸고 **이름 바꾸기** 를 클릭합니다.
4. [API 키](https://developers.google.com/apps-script/guides/properties?hl=ko#manage_script_properties_manually) 설정
   1. 왼쪽에서 **프로젝트 설정** ![프로젝트 설정 아이콘](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg)을 클릭합니다.
   2. **스크립트 속성** 에서 **스크립트 속성 추가** 를 클릭합니다.
   3. **\*\*속성\*\* 에 키 이름 `GEMINI_API_KEY`를 입력합니다.**
   4. **값**에 API 키의 값을 입력합니다.
   5. **스크립트 속성 저장** 을 클릭합니다.
5. `Code.gs` 파일 콘텐츠를 다음 코드로 바꿉니다.

## 첫 번째 요청하기

다음은 Gemini 2.5 Flash 모델을 사용하여 Gemini API에 요청을 전송하는
[`generateContent`](https://ai.google.dev/api/generate-content?hl=ko#method:-models.generatecontent) 메서드
를 사용하는 예입니다.

API 키를 [환경 변수 `GEMINI_API_KEY`로](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#set-api-env-var)설정하면
Gemini API 라이브러리를 사용할 때 [클라이언트에서 자동으로 선택합니다](https://ai.google.dev/gemini-api/docs/libraries?hl=ko).
그렇지 않으면 클라이언트를 초기화할 때 [API 키를](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#provide-api-key-explicitly)
인수로 전달해야 합니다.

Gemini API 문서의 모든 코드 샘플은 환경 변수 `GEMINI_API_KEY`를 설정했다고 가정합니다.

### Python

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    // The client gets the API key from the environment variable `GOOGLE_API_KEY`.
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## 다음 단계

이제 첫 번째 API 요청을 만들었으므로 Gemini가 작동하는 모습을 보여주는 다음 가이드를 살펴보는 것이 좋습니다.

- [텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation?hl=ko)
- [이미지 생성](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)
- [이미지 이해](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ko)
- [사고](https://ai.google.dev/gemini-api/docs/thinking?hl=ko)
- [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)
- [긴 컨텍스트](https://ai.google.dev/gemini-api/docs/long-context?hl=ko)
- [임베딩](https://ai.google.dev/gemini-api/docs/embeddings?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-07(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-07(UTC)"],[],[]]
