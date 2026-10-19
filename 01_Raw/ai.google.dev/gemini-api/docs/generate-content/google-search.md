---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=hi
fetched_at: 2026-10-19T05:44:02.229506+00:00
title: "Google Search \u0915\u0947 \u0906\u0927\u093e\u0930 \u092a\u0930 \u091c\u093e\u0928\u0915\u093e\u0930\u0940 \u0926\u0947\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# Google Search के आधार पर जानकारी देना

Google Search से सटीक जानकारी पाने की सुविधा, Gemini मॉडल को रीयल-टाइम में वेब कॉन्टेंट से कनेक्ट करती है और सभी उपलब्ध भाषाओं में काम करती है. इससे Gemini, जानकारी न मिलने की स्थिति के दायरे से बाहर निकलकर ज़्यादा सटीक जवाब और भरोसेमंद सोर्स के रेफ़रंस दे पाता है.

Google Search से सटीक जानकारी पाने की सुविधा की मदद से, ऐसे ऐप्लिकेशन बनाए जा सकते हैं जो:

- **तथ्यों के हिसाब से ज़्यादा सटीक जवाब दे सकते हैं:** असल दुनिया की जानकारी के आधार पर जवाब देकर, मॉडल के गलत जवाब देने की संभावना को कम किया जा सकता है.
- **रीयल-टाइम में जानकारी ऐक्सेस कर सकते हैं:** हाल ही में हुई घटनाओं और विषयों के बारे में सवालों के जवाब दे सकते हैं.
- **रेफ़रंस दे सकते हैं:** मॉडल के दावों के सोर्स दिखाकर, उपयोगकर्ता का भरोसा जीता जा सकता है.

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

[Search टूल
नोटबुक](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=hi) आज़माकर, ज़्यादा जानकारी पाई जा सकती है.

## Google Search से सटीक जानकारी पाने की सुविधा कैसे काम करती है

`google_search` टूल चालू करने पर, मॉडल, जानकारी खोजने, उसे प्रोसेस करने, और रेफ़रंस देने का पूरा वर्कफ़्लो अपने-आप मैनेज करता है.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=hi)

1. **उपयोगकर्ता का प्रॉम्प्ट:** आपका ऐप्लिकेशन, `google_search` टूल चालू होने पर, उपयोगकर्ता का प्रॉम्प्ट Gemini API को भेजता है.
2. **प्रॉम्प्ट का विश्लेषण:** मॉडल, प्रॉम्प्ट का विश्लेषण करता है और यह तय करता है कि Google Search की मदद से जवाब को बेहतर बनाया जा सकता है या नहीं.
3. **Google Search:** ज़रूरत पड़ने पर, मॉडल अपने-आप एक या एक से ज़्यादा सर्च क्वेरी जनरेट करता है और उन्हें एक्ज़ीक्यूट करता है.
4. **सर्च के नतीजों को प्रोसेस करना:** मॉडल, सर्च के नतीजों को प्रोसेस करता है, जानकारी को सिंथेसाइज़ करता है, और जवाब तैयार करता है.
5. **भरोसेमंद सोर्स से मिला जवाब:** एपीआई, सर्च के नतीजों के आधार पर, उपयोगकर्ता के लिए फ़ाइनल और आसान जवाब देता है. इस जवाब में, मॉडल का टेक्स्ट जवाब और `groundingMetadata` शामिल होता है. इसमें सर्च क्वेरी, वेब के नतीजे, और रेफ़रंस भी शामिल होते हैं.

## भरोसेमंद स्रोतों से मिले जवाब को समझना

जब कोई जवाब, भरोसेमंद सोर्स से मिलता है, तो उसमें `groundingMetadata` फ़ील्ड शामिल होता है. यह स्ट्रक्चर्ड डेटा, दावों की पुष्टि करने और आपके ऐप्लिकेशन में रेफ़रंस देने की बेहतर सुविधा बनाने के लिए ज़रूरी है.

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

Gemini API, `groundingMetadata` के साथ यह जानकारी दिखाता है:

- `webSearchQueries` : इस्तेमाल की गई सर्च क्वेरी का कलेक्शन. यह डीबग करने और मॉडल की तर्क देने की प्रोसेस को समझने के लिए काम का है.
- `searchEntryPoint` : इसमें, ज़रूरी Search के सुझावों को रेंडर करने के लिए, एचटीएमएल और सीएसएस शामिल होता है. इस्तेमाल से जुड़ी पूरी ज़रूरी शर्तें, [सेवा की
  शर्तों](https://ai.google.dev/gemini-api/terms?hl=hi#grounding-with-google-search) में बताई गई हैं.
- `groundingChunks` : ऑब्जेक्ट का कलेक्शन. इसमें वेब सोर्स (`uri` और `title`) शामिल होते हैं.
- `groundingSupports` : कलेक्शन. इसमें मॉडल के जवाब `text` को `groundingChunks` में मौजूद सोर्स से कनेक्ट करने के लिए, चंक शामिल होते हैं. हर चंक, `segment` (जो `startIndex` और `endIndex` से तय होता है) को एक या एक से ज़्यादा `groundingChunkIndices` से लिंक करता है. यह इनलाइन रेफ़रंस बनाने के लिए ज़रूरी है.

Google Search से सटीक जानकारी पाने की सुविधा को, [यूआरएल
कॉन्टेक्स्ट टूल](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) के साथ भी इस्तेमाल किया जा सकता है. इससे, सार्वजनिक
वेब डेटा और आपके दिए गए खास यूआरएल, दोनों के आधार पर जवाब दिए जा सकते हैं.

## इनलाइन रेफ़रंस की मदद से सोर्स एट्रिब्यूट करना

एपीआई, रेफ़रंस का स्ट्रक्चर्ड डेटा दिखाता है. इससे आपको यह तय करने का पूरा कंट्रोल मिलता है कि अपने यूज़र इंटरफ़ेस में सोर्स कैसे दिखाए जाएं. मॉडल के स्टेटमेंट को सीधे उनके सोर्स से लिंक करने के लिए, `groundingSupports` और `groundingChunks` फ़ील्ड का इस्तेमाल किया जा सकता है. यहां, मेटाडेटा को प्रोसेस करके, इनलाइन और क्लिक किए जा सकने वाले रेफ़रंस के साथ जवाब बनाने का सामान्य तरीका बताया गया है.

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

इनलाइन रेफ़रंस वाला नया जवाब ऐसा दिखेगा:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## कीमत

Gemini 3 और उसके बाद के मॉडल के साथ, Google Search से सटीक जानकारी पाने की सुविधा का इस्तेमाल करने पर, आपके प्रोजेक्ट के लिए **हर** उस सर्च क्वेरी का शुल्क लिया जाता है जिसे मॉडल एक्ज़ीक्यूट करता है.
क्वेरी के हिसाब से बिलिंग वाले इस मॉडल में, हर महीने 5,000 मुफ़्त सर्च अनुरोध शामिल होते हैं. ये अनुरोध, Gemini 3 और उसके बाद के सभी मॉडल के साथ शेयर किए जाते हैं. इसके बाद, **1,000 सर्च अनुरोधों के लिए 14 डॉलर** का शुल्क लिया जाता है.

उदाहरण के लिए, अगर मॉडल, किसी एक प्रॉम्प्ट का जवाब देने के लिए, एक से ज़्यादा सर्च क्वेरी एक्ज़ीक्यूट करता है (जैसे, एक ही एपीआई कॉल में `"UEFA Euro 2024 winner"` और `"Spain vs
England Euro 2024 final score"` के लिए खोज करना), तो इस अनुरोध के लिए, टूल के दो बार इस्तेमाल का शुल्क लिया जाएगा. बिलिंग के लिए, यूनीक क्वेरी की गिनती करते समय, हम खाली वेब सर्च क्वेरी को अनदेखा करते हैं.

Gemini 2.5 या उससे पुराने मॉडल के साथ, सर्च से सटीक जानकारी पाने की सुविधा का इस्तेमाल करने पर, आपके प्रोजेक्ट के लिए हर प्रॉम्प्ट का शुल्क लिया जाता है.

कीमत की ज़्यादा जानकारी के लिए, [Gemini API की कीमत
वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.

## इस्तेमाल किए जा सकने वाले मॉडल

मॉडल की सभी क्षमताओं के बारे में जानकारी, मॉडल की [खास जानकारी
वाले पेज](https://ai.google.dev/gemini-api/docs/models?hl=hi) पर देखी जा सकती है.

| मॉडल | Google Search से सटीक जानकारी पाने की सुविधा |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image Preview | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3 Pro Image Preview | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| Gemini 3.1 Flash-Lite Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## टूल के इस्तेमाल के लिए उपलब्ध कॉम्बिनेशन

ज़्यादा मुश्किल इस्तेमाल के मामलों के लिए, Google Search से सटीक जानकारी पाने की सुविधा को अन्य टूल के साथ इस्तेमाल किया जा सकता है. जैसे,
[कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi),
[यूआरएल कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi), और
[Google Maps से सटीक जानकारी पाने की सुविधा](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi). Google Maps से सटीक जानकारी पाने की सुविधा,
Gemini 3.5 Flash-Lite और उसके बाद के मॉडल पर उपलब्ध है.
Gemini 3 मॉडल में, इन बिल्ट-इन टूल को कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ भी इस्तेमाल किया जा सकता है. ज़्यादा जानकारी के लिए,
[टूल के इस्तेमाल के लिए उपलब्ध कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) वाला पेज देखें.

## आगे क्या करना है

- [Gemini API की
  कुकबुक](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=hi) में, Google Search से सटीक जानकारी पाने की सुविधा को आज़माएं.
- उपलब्ध अन्य टूल के बारे में जानें. जैसे, [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi).
- [यूआरएल कॉन्टेक्स्ट
  टूल](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) का इस्तेमाल करके, खास यूआरएल की मदद से प्रॉम्प्ट को बेहतर बनाने का तरीका जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया."],[],[]]
