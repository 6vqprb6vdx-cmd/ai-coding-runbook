---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=hi
fetched_at: 2026-06-15T06:25:33.207912+00:00
title: "Gemini Developer API \u092c\u0928\u093e\u092e Gemini Enterprise Agent Platform \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini Developer API बनाम Gemini Enterprise Agent Platform

Gemini की मदद से जनरेटिव एआई के समाधान डेवलप करने के लिए, Google दो एपीआई प्रॉडक्ट उपलब्ध कराता है:
[Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=hi) और [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=hi).

Gemini Developer API की मदद से, Gemini की सुविधाओं वाले ऐप्लिकेशन को तेज़ी से बनाया, प्रोडक्शन में लाया, और स्केल किया जा सकता है. ज़्यादातर डेवलपर को Gemini Developer API का इस्तेमाल करना चाहिए. हालांकि, अगर एंटरप्राइज़ के लिए खास कंट्रोल की ज़रूरत हो, तो Gemini Enterprise Agent Platform API का इस्तेमाल किया जा सकता है.

Gemini Enterprise Agent Platform, एंटरप्राइज़ के लिए तैयार सुविधाओं और सेवाओं का एक पूरा इकोसिस्टम उपलब्ध कराता है. इसकी मदद से, Google Cloud Platform पर जनरेटिव एआई के ऐप्लिकेशन बनाए और डिप्लॉय किए जा सकते हैं.

हमने हाल ही में इन सेवाओं के बीच माइग्रेट करने की प्रोसेस को आसान बनाया है. अब Gemini
Developer API और Gemini Enterprise Agent Platform API, दोनों को unified
[Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=hi) की मदद से ऐक्सेस किया जा सकता है.

## कोड की तुलना

इस पेज पर, टेक्स्ट जनरेट करने के लिए Gemini Developer API और Gemini Enterprise Agent Platform के क्विकस्टार्ट के कोड की तुलना की गई है.

### Python

`google-genai` लाइब्रेरी की मदद से, Gemini Developer API और Gemini Enterprise Agent Platform, दोनों की सेवाओं को ऐक्सेस किया जा सकता है. [लाइब्रेरीज़](https://ai.google.dev/gemini-api/docs/libraries?hl=hi) पेज पर
`google-genai` इंस्टॉल करने के निर्देशों के लिए, देखें.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript और TypeScript

`@google/genai` लाइब्रेरी की मदद से, Gemini Developer API और Gemini Enterprise Agent Platform, दोनों की सेवाओं को ऐक्सेस किया जा सकता है. [लाइब्रेरीज़](https://ai.google.dev/gemini-api/docs/libraries?hl=hi) पेज पर, `@google/genai` इंस्टॉल करने के निर्देशों के लिए देखें.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

`google.golang.org/genai` लाइब्रेरी की मदद से, Gemini Developer API और Gemini Enterprise Agent Platform, दोनों की सेवाओं को ऐक्सेस किया जा सकता है. [लाइब्रेरीज़](https://ai.google.dev/gemini-api/docs/libraries?hl=hi) पेज पर
इंस्टॉल करने के निर्देशों के लिए, `google.golang.org/genai` देखें.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### इस्तेमाल के अन्य उदाहरण और प्लैटफ़ॉर्म

अन्य प्लैटफ़ॉर्म और इस्तेमाल के उदाहरणों के लिए, [Gemini Developer API के दस्तावेज़](https://ai.google.dev/gemini-api/docs?hl=hi)
और [Gemini Enterprise Agent Platform के दस्तावेज़](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=hi)
में, इस्तेमाल के उदाहरणों से जुड़े गाइड देखें.

## माइग्रेशन से जुड़ी ज़रूरी बातें

माइग्रेट करने पर:

- आपको पुष्टि करने के लिए, Google Cloud के सेवा खातों का इस्तेमाल करना होगा. ज़्यादा जानकारी के लिए, [Gemini Enterprise Agent Platform का दस्तावेज़](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=hi)
  देखें.
- [आपके पास, मौजूदा Google Cloud प्रोजेक्ट
  (वही प्रोजेक्ट जिसका इस्तेमाल आपने एपीआई पासकोड जनरेट करने के लिए किया था) का इस्तेमाल करने या नया Google Cloud प्रोजेक्ट](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=hi)बनाने का विकल्प होता है.
- Gemini Developer API और Gemini Enterprise Agent Platform API के लिए, काम करने वाले इलाकों में फ़र्क़ हो सकता है. Google Cloud पर जनरेटिव एआई के लिए, काम करने वाले इलाकों की सूची देखें
  .
- Google AI Studio में बनाए गए सभी मॉडल को, Gemini Enterprise Agent Platform में फिर से ट्रेन करना होगा.

अगर आपको Gemini Developer API के लिए, Gemini API पासकोड का इस्तेमाल नहीं करना है, तो सुरक्षा से जुड़े सबसे सही तरीके अपनाएं और उसे मिटा दें.

एपीआई पासकोड मिटाने के लिए:

1. [Google Cloud के एपीआई क्रेडेंशियल वाला पेज खोलें.](https://console.cloud.google.com/apis/credentials?hl=hi)
2. वह एपीआई पासकोड ढूंढें जिसे आपको मिटाना है. इसके बाद, **कार्रवाइयां** आइकॉन पर क्लिक करें.
3. **एपीआई पासकोड मिटाएं** को चुनें.
4. **क्रेडेंशियल मिटाएं** वाले मॉडल में, **मिटाएं** को चुनें.

   एपीआई पासकोड मिटाने के बाद, इसे सभी जगह से हटाने में कुछ मिनट लगते हैं. सभी जगह से हटाने की प्रोसेस पूरी होने के बाद, मिटाए गए एपीआई पासकोड का इस्तेमाल करने वाले किसी भी ट्रैफ़िक को अस्वीकार कर दिया जाता है.

## अगले चरण

- Gemini Enterprise Agent Platform पर जनरेटिव एआई के समाधानों के बारे में ज़्यादा जानने के लिए,
  [Gemini Enterprise Agent Platform पर जनरेटिव एआई की खास जानकारी](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/multimodal/overview?hl=hi)
  देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-19 (UTC) को अपडेट किया गया."],[],[]]
