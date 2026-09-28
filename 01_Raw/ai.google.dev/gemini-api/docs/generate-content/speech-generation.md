---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi
fetched_at: 2026-09-28T06:08:14.494144+00:00
title: "\u0932\u093f\u0916\u0947 \u0917\u090f \u0936\u092c\u094d\u0926\u094b\u0902 \u0915\u094b \u0938\u0941\u0928\u0928\u0947 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e (\u091f\u0940\u091f\u0940\u090f\u0938) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# लिखे गए शब्दों को सुनने की सुविधा (टीटीएस)

Gemini API, टेक्स्ट इनपुट को एक या एक से ज़्यादा स्पीकर वाले ऑडियो में बदल सकता है. इसके लिए, Gemini की लिखाई को बोली में बदलने (टीटीएस) की सुविधा का इस्तेमाल किया जाता है.
लिखे हुए शब्दों को बोली में बदलने की सुविधा को *[कंट्रोल किया जा सकता है](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi#controllable)*. इसका मतलब है कि ऑडियो की *स्टाइल*, *एक्सेंट*, *रफ़्तार*, और *टोन* को कंट्रोल करने के लिए, स्ट्रक्चर्ड टर्न मेटाडेटा (`speech_metadata`) और इनलाइन वोकल टैग को एक साथ इस्तेमाल किया जा सकता है.

[Google AI Studio में आज़माएं](https://aistudio.google.com/generate-speech?hl=hi)

टीटीएस की सुविधा, [लाइव एपीआई](https://ai.google.dev/gemini-api/docs/live?hl=hi) के ज़रिए उपलब्ध कराई गई स्पीच जनरेशन की सुविधा से अलग है. इसे इंटरैक्टिव, अनस्ट्रक्चर्ड ऑडियो, और मल्टीमॉडल इनपुट और आउटपुट के लिए डिज़ाइन किया गया है. लाइव एपीआई, बातचीत के कॉन्टेक्स्ट को डाइनैमिक तरीके से समझने में बेहतर है. वहीं, Gemini API के ज़रिए टीटीएस की सुविधा, उन स्थितियों के लिए तैयार की गई है जिनमें स्टाइल और आवाज़ पर बारीकी से कंट्रोल के साथ, सटीक टेक्स्ट सुनाने की ज़रूरत होती है. जैसे, पॉडकास्ट या ऑडियो बुक जनरेट करना.

इस गाइड में बताया गया है कि [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) (`gemini-3.8-flash-tts`) और [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) (`gemini-3.8-flash-lite-tts`) का इस्तेमाल करके, टेक्स्ट से एक या एक से ज़्यादा स्पीकर की आवाज़ में ऑडियो कैसे जनरेट करें.

## शुरू करने से पहले

पक्का करें कि आपने [साथ काम करने वाले मॉडल](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi#supported-models) सेक्शन में दिए गए Gemini के टीटीएस मॉडल का इस्तेमाल किया हो. बेहतर नतीजों के लिए, [किस मॉडल का इस्तेमाल कब करना चाहिए](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi#when-to-use-which-model) लेख पढ़ें. इससे आपको अपने वर्कलोड के लिए सबसे सही मॉडल चुनने में मदद मिलेगी.

ऐप्लिकेशन बनाना शुरू करने से पहले, [AI Studio में Gemini के टीटीएस मॉडल को टेस्ट करना](https://aistudio.google.com/generate-speech?hl=hi) आपके लिए फ़ायदेमंद हो सकता है.

## एक ही आवाज़ में टीटीएस की सुविधा

Gemini 3.8 के टीटीएस मॉडल की मदद से, टेक्स्ट को एक स्पीकर वाले ऑडियो में बदलने के लिए, `parts[].text` में हूबहू ट्रांसक्रिप्ट पास करें, `parts[].speech_metadata` में टर्न-लेवल की स्टाइलिंग अटैच करें, और `speechConfig.voiceConfig` में अपनी आवाज़ कॉन्फ़िगर करें. प्रीबिल्ट वॉइस नेम, Extended Voice Library का आईडी, कस्टम [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi) का आईडी (`voice_...`) या [वॉइस रेप्लिकेशन](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=hi) का आईडी (`voice_...` या बिना स्थिति वाली वैकल्पिक `voicekey_...`) पास किया जा सकता है.

इस उदाहरण में, मॉडल से मिले आउटपुट ऑडियो को WAV फ़ाइल में सेव किया गया है:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speech_metadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.wav
```

## एक से ज़्यादा लोगों की आवाज़ में टीटीएस

एक से ज़्यादा स्पीकर के बीच बातचीत के लिए, `prebuiltVoiceConfig` का इस्तेमाल करके `multiSpeakerVoiceConfig.speakerVoiceConfigs` में दो स्पीकर कॉन्फ़िगर करें. साथ ही, बातचीत के हर टर्न को अलग `part` के तौर पर पास करें. इसमें `speech_metadata` में `speaker` और टर्न-लेवल का वैकल्पिक `style`, दोनों की जानकारी दें:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [
            {
                "text": "How's it going today Jane?",
                "speech_metadata": {
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                },
            },
            {
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "speech_metadata": {
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                },
            },
        ],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "multi_speaker_voice_config": {
                "speaker_voice_configs": [
                    {
                        "speaker": "Joe",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Puck"}
                        },
                    },
                    {
                        "speaker": "Jane",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Kore"}
                        },
                    },
                ]
            }
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [
            {
               text: "How's it going today Jane?",
               speech_metadata: {
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               },
            },
            {
               text: 'Not too bad, how about you? Ready to test these new voices?',
               speech_metadata: {
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               },
            },
         ],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            multiSpeakerVoiceConfig: {
               speakerVoiceConfigs: [
                  {
                     speaker: 'Joe',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Puck' },
                     },
                  },
                  {
                     speaker: 'Jane',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Kore' },
                     },
                  },
               ],
            },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {
          "text": "How'\''s it going today Jane?",
          "speech_metadata": {
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }
        },
        {
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "speech_metadata": {
            "speaker": "Jane",
            "style": "calm and relaxed"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {
              "speaker": "Joe",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Puck" }
              }
            },
            {
              "speaker": "Jane",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Kore" }
              }
            }
          ]
        }
      }
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
      base64 --decode > out.wav
```

## मेटाडेटा और टैग की मदद से, बोलने के तरीके को कंट्रोल करना

Gemini 3.8 TTS, `text` फ़ील्ड को हूबहू ट्रांसक्रिप्ट के तौर पर इस्तेमाल करता है. स्टेज के निर्देशों को तेज़ आवाज़ में सुने बिना डिलीवरी को कंट्रोल करने के लिए, अपने निर्देशों को स्कोप के हिसाब से बांटें:

- **लगातार एक ही तरह से जवाब देना (`speech_metadata.style`):** `speech_metadata.style` में, पूरे टर्न के दौरान एक ही तरह की भावनाएं, जवाब देने का तरीका, उतार-चढ़ाव, गति, और आवाज़ का इस्तेमाल करें. उदाहरण के लिए, `"style": "whispered urgently"`, `"style": "out of breath"` या `"style": "warm and enthusiastic"`.
- **किसी समय पर होने वाले इवेंट (इनलाइन टैग):** कुछ समय के लिए बिना बोले आवाज़ में होने वाले बदलाव या पॉज़ को सीधे तौर पर ट्रांसक्रिप्ट में ऐंगल ब्रैकेट का इस्तेमाल करके डालें. उदाहरण के लिए, `"Wait... <short pause> did you hear that? <sigh>"` या `"Excuse me <cough> as I was saying..."`.

सबसे सही तरीकों के बारे में पूरी जानकारी पाने के लिए, [प्रॉम्प्ट के लिए गाइड](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi#prompting-guide) देखें.

## आवाज़ के विकल्प

Gemini 3.8 में टीटीएस की सुविधा, चार तरीकों से आवाज़ें चुनने या बनाने की सुविधा देती है:

1. **स्टूडियो की पहले से तैयार की गई आवाज़ें:** यहां दी गई टेबल में 30 आवाज़ें दी गई हैं.
2. **एक्सटेंडेड वॉइस लाइब्रेरी:** इसमें अलग-अलग भाषाओं, लहज़ों, और किरदारों के हिसाब से सैकड़ों अतिरिक्त आवाज़ें उपलब्ध हैं. इन्हें `client.voices.list()` (`GET /v1beta/voices`) का इस्तेमाल करके ऐक्सेस किया जा सकता है.
3. **[आवाज़ का डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi):** [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में, सामान्य भाषा में दिए गए ब्यौरे से, अपनी पसंद के मुताबिक आवाज़ जनरेट करें. इसके लिए, `POST /v1beta/voices` (`type="prompted"` का इस्तेमाल करें. यह `voice_...` आईडी और `sample_audio` WAV फ़ाइल की झलक दिखाता है. यह `CreateVoice` और `GetVoice` में उपलब्ध है).
4. **[आवाज़ की नकल करना](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=hi):**
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में, किसी स्पीकर की आवाज़ की नकल करने के लिए, रेफ़रंस और सहमति वाला ऑडियो इस्तेमाल करें. इसके अलावा, `POST /v1beta/voices` (`type="replicated"`, डिफ़ॉल्ट रूप से लगातार `store=True` या बिना स्थिति के वैकल्पिक `store=False`) का इस्तेमाल करके भी ऐसा किया जा सकता है.

### कस्टम वॉइस की सीमाएं और टीटीएल

| बोलकर लिखवाएँ | स्टोरेज मोड | कोटा / सीमा | डेटा का रखरखाव (टीटीएल) |
| --- | --- | --- | --- |
| **स्टेटफ़ुल आवाज़ें** (`voice_...`, प्रॉम्प्ट की गई या कॉपी की गई) | `store=True` | **हर प्रोजेक्ट के लिए 200 आवाज़ें** (इन्हें प्रॉम्प्ट की गई और रेप्लिका की गई आवाज़ों के साथ शेयर किया जाता है) | **एक साल** |
| **स्टेटलेस वॉइस की** (`voicekey_...`, रेप्लिका) | `store=False` | क्लाइंट की ओर से मैनेज किया गया | **सात दिन** |

### पहले से मौजूद आवाज़ें

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | **Charon** -- *Informative* |
| **Kore** -- *Firm* | **Fenrir** -- *Excitable* | **Leda** -- *यूथफ़ुल* |
| **Orus** -- *कंपनी* | **Aoede** -- *Breezy* | **Callirrhoe** -- *ईज़ी-गोइंग* |
| **ऑटोनो** -- *ब्राइट* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *शांत स्वभाव वाला* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| **Erinome** -- *Clear* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *Informative* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *मैच्योर* | **Pulcherrima** -- *Forward* |
| **Achird** -- *Friendly* | **Zubenelgenubi** -- *कैज़ुअल* | **Vindemiatrix** -- *जेंटल* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Knowledgeable* | **Sulafat** -- *Warm* |

### वॉइस लाइब्रेरी और फ़िल्टर करने की सुविधा को बेहतर बनाया गया

ऊपर दी गई टेबल में, स्टूडियो में उपलब्ध 30 आवाज़ों के अलावा, **आवाज़ों की बड़ी लाइब्रेरी** में कई और आवाज़ें उपलब्ध हैं. ये आवाज़ें अलग-अलग भाषाओं, क्षेत्रीय लहज़ों, किरदार के पर्सोना, और डोमेन के हिसाब से उपलब्ध हैं. [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में, वॉइस लाइब्रेरी को ब्राउज़ किया जा सकता है. साथ ही, इसे फ़िल्टर किया जा सकता है और इसकी पूरी झलक देखी जा सकती है. इसके अलावा, `client.voices.list()` (`GET /v1beta/voices`, `google-genai` 2.25.0+ / `@google/genai` 2.24.0+ का इस्तेमाल करके) का इस्तेमाल करके, प्रोग्राम के हिसाब से इससे क्वेरी की जा सकती है.

`ListVoices` से, सेव की गई आपकी कस्टम आवाज़ें (सबसे नई आवाज़ें पहले दिखती हैं) दिखती हैं. इसके बाद, फ़िल्टर के लिए तय की गई शर्तों से मेल खाने वाली, पहले से मौजूद कैटलॉग की आवाज़ें दिखती हैं. जब सूची वाले फ़िल्टर के लिए एक से ज़्यादा वैल्यू पास की जाती हैं, तो उस फ़िल्टर में मौजूद **किसी भी** वैल्यू से मेल खाने वाली आवाज़ें दिखाई जाती हैं (`OR`). वहीं, अलग-अलग फ़िल्टर पैरामीटर `AND` के साथ जुड़ जाते हैं:

| पैरामीटर | टाइप | ब्यौरा |
| --- | --- | --- |
| `language_code` | `list[str]` | BCP-47 भाषा के टैग (उदाहरण के लिए, `["en-US", "en-GB"]`). केस-इनसेंसिटिव एग्ज़ैक्ट मैच. |
| `region_code` | `list[str]` | ISO 3166-1 ऐल्फ़ा-2 या UN M.49 क्षेत्र का कोड (उदाहरण के लिए, `["US", "GB"]`). |
| `accent` | `list[str]` | क्षेत्रीय लहज़े के बारे में बताने वाले डिस्क्रिप्टर (उदाहरण के लिए, `["American", "British"]`). |
| `gender` | `list[str]` | लिंग की पहचान (`"female"`, `"male"` या `"neutral"`). |
| `pitch` | `list[str]` | आवाज़ की पिच का क्लासिफ़िकेशन (`"low"`, `"medium"` या `"high"`). |
| `persona` | `list[str]` | आवाज़ देने वाले का पर्सोना या किरदार (उदाहरण के लिए, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (REST में `context`) | `list[str]` | इस्तेमाल के लिए सबसे सही डोमेन (उदाहरण के लिए, `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` in Python) | `list[str]` | आवाज़ के सोर्स के हिसाब से फ़िल्टर करें: `"prebuilt"`, `"prompted"` ([आवाज़ का डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi)) या `"replicated"` ([आवाज़ की नकल](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=hi)). |
| `search` | `str` | फ़्री-टेक्स्ट सबस्ट्रिंग खोज, `display_name` और `description`, दोनों के साथ केस-इनसेंसिटिव तरीके से मैच हुई. |
| `page_size` | `int` | हर पेज पर दिखाई जाने वाली आवाज़ों की ज़्यादा से ज़्यादा संख्या (डिफ़ॉल्ट `50`, ज़्यादा से ज़्यादा `1000`). |
| `page_token` | `str` | `response.next_page_token` से मिला टोकन, जिसका इस्तेमाल नतीजों का अगला पेज फ़ेच करने के लिए किया जाता है. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## इस्तेमाल की जा सकने वाली भाषाएं

टीटीएस मॉडल, इनपुट की भाषा का पता अपने-आप लगा लेते हैं.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi)
(`gemini-3.8-flash-tts`) **130 से ज़्यादा भाषाओं** में काम करता है. वहीं, [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi)
(`gemini-3.8-flash-lite-tts`) **100 से ज़्यादा भाषाओं** में काम करता है:

| भाषा | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| एचनीज़ (अरबी स्क्रिप्ट) | ✔️ | ✔️ |
| अफ़्रीकान्स | ✔️ | ✔️ |
| आकान | ✔️ | ✔️ |
| अमहैरिक | ✔️ | ✔️ |
| आर्मीनियन | ✔️ | ✔️ |
| असमिया | ✔️ | ✔️ |
| अवधी | ✔️ | ✔️ |
| बालीनीज़ | ✔️ | ✔️ |
| बांग्ला | ✔️ | ✔️ |
| बंजार (अरबी लिपि) | ✔️ | — |
| बंजार (लैटिन स्क्रिप्ट) | ✔️ | ✔️ |
| बाश्कियर | ✔️ | — |
| बॉस्क | ✔️ | ✔️ |
| बेलारूसी | ✔️ | ✔️ |
| बेंबा | ✔️ | — |
| भोजपुरी | ✔️ | ✔️ |
| बोस्नियन | ✔️ | ✔️ |
| ब्‍यूगिनी | ✔️ | ✔️ |
| बल्गैरियन | ✔️ | ✔️ |
| बर्मीज़ | ✔️ | — |
| कैंटोनीज़ | ✔️ | ✔️ |
| कैटलैन | ✔️ | ✔️ |
| सेबुआनो | ✔️ | ✔️ |
| सेंट्रल कुर्दिश | ✔️ | ✔️ |
| छत्तीसगढ़ी | ✔️ | ✔️ |
| चाइनीज़ (हंस स्क्रिप्ट) | ✔️ | ✔️ |
| चाइनीज़ (हंत स्क्रिप्ट) | ✔️ | ✔️ |
| क्राइमियन टाटर | ✔️ | — |
| क्रोएशियन | ✔️ | ✔️ |
| चेक | ✔️ | ✔️ |
| डैनिश | ✔️ | ✔️ |
| डच | ✔️ | ✔️ |
| ड्यूला | ✔️ | — |
| जोंगखा | ✔️ | — |
| मिस्री अरबी | ✔️ | ✔️ |
| अंग्रेज़ी | ✔️ | ✔️ |
| एस्टोनियन | ✔️ | ✔️ |
| फ़िलिपीनी | ✔️ | ✔️ |
| फ़िनिश | ✔️ | — |
| फ़्रांसीसी | ✔️ | ✔️ |
| गैलिशियन | ✔️ | ✔️ |
| गांदा | ✔️ | ✔️ |
| जॉर्जियन | ✔️ | ✔️ |
| जर्मन | ✔️ | ✔️ |
| ग्रीक | ✔️ | ✔️ |
| गुअरानी | ✔️ | — |
| गुजराती | ✔️ | ✔️ |
| हैतियन क्रिओल | ✔️ | ✔️ |
| हलह मंगोलियन | ✔️ | ✔️ |
| हौसा | ✔️ | ✔️ |
| हिब्रू | ✔️ | ✔️ |
| हिन्दी | ✔️ | ✔️ |
| हंगेरियन | ✔️ | ✔️ |
| आइसलैंडिक | ✔️ | ✔️ |
| इग्बो | ✔️ | — |
| ईलोको | ✔️ | ✔️ |
| इंडोनेशियन | ✔️ | ✔️ |
| ईरानी फ़ारसी | ✔️ | ✔️ |
| इटैलियन | ✔️ | ✔️ |
| जापानी | ✔️ | ✔️ |
| जावानीज़ | ✔️ | ✔️ |
| कबाइल | ✔️ | — |
| कांबा | ✔️ | ✔️ |
| कन्नड़ | ✔️ | ✔️ |
| कश्मीरी (अरबी लिपि) | ✔️ | ✔️ |
| कश्मीरी (देव स्क्रिप्ट) | ✔️ | ✔️ |
| कज़ाक | ✔️ | ✔️ |
| ख्मेर | ✔️ | ✔️ |
| किकुयू | ✔️ | ✔️ |
| किनयारवांडा | ✔️ | ✔️ |
| कॉन्गो | ✔️ | ✔️ |
| कोरियन | ✔️ | ✔️ |
| किर्गिज़ | ✔️ | ✔️ |
| लाओ | ✔️ | ✔️ |
| लैजालियन | ✔️ | — |
| लिंगाला | ✔️ | ✔️ |
| लिथुएनियन | ✔️ | — |
| लक्ज़मबर्गिश | ✔️ | — |
| मैसेडोनियन | ✔️ | ✔️ |
| मगही | ✔️ | ✔️ |
| मैथिली | ✔️ | ✔️ |
| मलयालम | ✔️ | ✔️ |
| मोल्टीज़ | ✔️ | ✔️ |
| मणिपुरी | ✔️ | ✔️ |
| मराठी | ✔️ | ✔️ |
| मिनांग्काबाउ (अरबी लिपि) | ✔️ | ✔️ |
| मिनांग्काबाउ (लैटिन स्क्रिप्ट) | ✔️ | — |
| मिज़ो | ✔️ | ✔️ |
| नेपाली (अलग भाषा) | ✔️ | ✔️ |
| नाइजीरिया की फु़लफु़लदे | ✔️ | ✔️ |
| उत्तरी अज़रबैजान | ✔️ | ✔️ |
| नॉर्दर्न सोथो | ✔️ | ✔️ |
| नॉर्दर्न उज़्बेक | ✔️ | ✔️ |
| नॉर्वेजियन बोकमाल | ✔️ | ✔️ |
| नार्वेजियन नॉर्स्क | ✔️ | ✔️ |
| न्यान्जा | ✔️ | ✔️ |
| ओसीटन | ✔️ | — |
| ओड़िया (अलग भाषा) | ✔️ | ✔️ |
| पंगासिनान | ✔️ | — |
| पर्शन (अफ़ग़ानिस्तान) | ✔️ | ✔️ |
| पोलिश | ✔️ | ✔️ |
| पॉर्चुगीज़ | ✔️ | ✔️ |
| पंजाबी | ✔️ | ✔️ |
| रोमानियन | ✔️ | ✔️ |
| रूसी | ✔️ | ✔️ |
| संथाली | ✔️ | ✔️ |
| सर्बियन | ✔️ | ✔️ |
| सिंधी | ✔️ | — |
| सिंहला | ✔️ | ✔️ |
| स्लोवाक | ✔️ | ✔️ |
| स्लोवेनियन | ✔️ | — |
| सोमाली | ✔️ | — |
| दक्षिणी अज़रबैजानी | ✔️ | ✔️ |
| दक्षिणी पश्तो | ✔️ | ✔️ |
| सदर्न सुटू | ✔️ | — |
| स्पैनिश | ✔️ | ✔️ |
| स्टैंडर्ड ऐरेबिक (अरबी लिपि) | ✔️ | ✔️ |
| स्टैंडर्ड ऐरेबिक (लैटिन स्क्रिप्ट) | ✔️ | ✔️ |
| स्टैंडर्ड लातवियन | ✔️ | ✔️ |
| स्टैंडर्ड मलय | ✔️ | ✔️ |
| स्वाहीली (अलग भाषा) | ✔️ | — |
| स्वाटी | ✔️ | — |
| स्वीडिश | ✔️ | — |
| ताजिक | ✔️ | — |
| तमिल | ✔️ | ✔️ |
| तेलुगु | ✔️ | ✔️ |
| थाई | ✔️ | — |
| तिग्रिन्या | ✔️ | — |
| टॉस्क अल्बानियन | ✔️ | — |
| टर्किश | ✔️ | ✔️ |
| विगर | ✔️ | — |
| वियतनामीज़ | ✔️ | ✔️ |

## इन मॉडल के साथ काम करता है

| मॉडल | एक व्यक्ति बोल रहा है | एक से ज़्यादा स्पीकर | आवाज़ का डिज़ाइन | वॉइस रेप्लिकेशन |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash TTS की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=hi) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=hi) | ✔️ | ✔️ | — | — |

### किस मॉडल का इस्तेमाल कब करना चाहिए

Gemini 3.8 के दोनों टीटीएस मॉडल, एक ही एपीआई स्कीमा और प्रॉम्प्ट फ़ॉर्मैट का इस्तेमाल करते हैं. इसलिए, एक पैरामीटर में बदलाव करके, इन दोनों मॉडल के बीच स्विच किया जा सकता है:

- **[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi)
  (`gemini-3.8-flash-tts`)** का इस्तेमाल तब करें, जब आपको सबसे ज़्यादा एकॉस्टिक फ़िडेलिटी, बारीकी से ऐक्टिंग, और एक्सप्रेशन पर कंट्रोल चाहिए हो. यह मॉडल, स्टूडियो-ग्रेड क्रिएटिव काम, कई स्पीकर वाले मुश्किल डायलॉग, तेज़ आवाज़ वाले टैग, मुश्किल उच्चारण, क्षेत्रीय या अल्पसंख्यक बोलियों, और लंबी अवधि के ऐसे नैरेशन के लिए सबसे सही है जिनमें आवाज़ और रूम-टोन की स्थिरता बहुत ज़रूरी होती है.
- `gemini-3.1-flash-tts-preview` की जगह, **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi)
  (`gemini-3.8-flash-lite-tts`)** का इस्तेमाल करें. यह मॉडल, कम लागत में तेज़ी से काम करता है. इसे इन कामों के लिए ऑप्टिमाइज़ किया गया है: एक साथ कई ऑडियो बनाना, बातचीत करने वाले वॉइस एजेंट के लिए कैस्केड बनाना, पढ़कर सुनाने की सुविधा, भरोसेमंद तरीके से आवाज़ की नकल करना, और रोज़मर्रा की बातचीत में एक ही स्पीकर की आवाज़ को मुख्य भाषाओं में इस्तेमाल करना.

### माइग्रेशन गाइड

अगर आपको झलक के तौर पर उपलब्ध कराए गए पुराने मॉडल (`gemini-3.1-flash-tts-preview` या
`gemini-2.5-pro-preview-tts`) से Gemini 3.8 टीटीएस (`gemini-3.8-flash-tts` या
`gemini-3.8-flash-lite-tts`) पर अपग्रेड करना है, तो इन पांच मुख्य बदलावों के बारे में जान लें:

1. **स्टाइल को ट्रांसक्रिप्ट से अलग करना:** एक्टिंग, टोन, प्रॉसोडी, और पेसिंग से जुड़े निर्देशों (जैसे कि `"whispering"`, `"out of breath"` या `"speaking slowly"`) को सामान्य टेक्स्ट से हटाकर `speech_metadata.style` में ले जाएं.
   `text` को, शब्दशः ट्रांसक्रिप्ट के साथ-साथ इनलाइन वोकल टैग के तौर पर ही रखें.
2. **वॉइस डिज़ाइन की मदद से, पर्सोना को पहले से डिज़ाइन करें:** एक से ज़्यादा पैराग्राफ़ वाले `"Audio Profile"` या `"Director's Notes"` ब्लॉक को [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi) में बनाई गई कस्टम आवाज़ से बदलें. इसके बाद, टीटीएस के अनुरोधों में उस `voice_...` आईडी का इस्तेमाल करें. साथ ही, `style` स्ट्रिंग को कम से कम या खाली रखें.
3. **स्ट्रक्चर्ड डायलॉग टर्न का इस्तेमाल करें:** एक से ज़्यादा स्पीकर वाले डायलॉग के लिए, एक ही टेक्स्ट ब्लॉक में `Speaker: ...` प्रीफ़िक्स एम्बेड करने के बजाय, हर स्पीकर के टर्न के लिए `speech_metadata.speaker` के साथ एक `part` पास करें.
4. **इनलाइन वोकल टैग के लिए ऐंगल ब्रैकेट का इस्तेमाल करें:** किसी समय पर की गई मानवीय आवाज़ और ठहराव के लिए, ऐंगल ब्रैकेट (`<laugh>`, `<sigh>`, `<cough>`, `<breath>`, `<short pause>`) का इस्तेमाल करें. बिना आवाज़ वाले साउंड इफ़ेक्ट टैग (जैसे, तालियां या धमक) का इस्तेमाल न करें.
5. **एकल अनुरोधों पर डिफ़ॉल्ट WAV (`AUDIO_WAV`) आउटपुट का हिसाब रखें:**
   `gemini-3.1-flash-tts-preview` के उलट, Gemini 3.8 के टीटीएस मॉडल, एकल अनुरोधों
   पर RIFF हेडर (24 किलोहर्ट्ज़, मोनो, 16-बिट पीसीएम) के साथ पूरा **WAV
   (`AUDIO_WAV`)** ऑडियो देते हैं. डिफ़ॉल्ट रूप से हेडरलेस रॉ पीसीएम
   `AUDIO_L16` देता है. डिकोड किए गए ऑडियो बाइट को सीधे `.wav` फ़ाइल में लिखा जा सकता है. इसके लिए, उन्हें Python के `wave` मॉड्यूल या Node के `wav` पैकेज के साथ मैन्युअल तरीके से रैप करने की ज़रूरत नहीं होती. अगर आपकी मौजूदा पाइपलाइन को हेडरलेस रॉ पीसीएम की ज़रूरत है, तो `response_format` को `{"audio": {"mime_type": "AUDIO_L16"}}` पर सेट करें ([ऑडियो आउटपुट फ़ॉर्मैट](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi#audio-output-formats) देखें).

## प्रॉम्प्ट से जुड़ी गाइड

Gemini 3.8 के टीटीएस मॉडल, इनपुट टेक्स्ट को सिर्फ़ **शब्दशः ट्रांसक्रिप्ट** के तौर पर लेते हैं.
पहले के प्रीव्यू मॉडल में, स्टेज के बारे में निर्देश सादे टेक्स्ट में एम्बेड किए जाते थे. हालांकि, Gemini 3.8 टीटीएस में, लगातार टर्न-लेवल के निर्देशों (`speech_metadata`) को, पॉइंट-इन-टाइम इनलाइन वोकल टैग से अलग किया जाता है.

### स्टाइल फ़ील्ड बनाम इनलाइन टैग

परफ़ॉर्मेंस के निर्देशों को स्कोप के हिसाब से बांटें:

- **टर्न-लेवल डिलीवरी (`speech_metadata.style`):** डिलीवरी की लगातार बनी रहने वाली एट्रिब्यूट वैल्यू—जैसे कि भावना, उतार-चढ़ाव, बोलने की कुल गति या डिलीवरी स्टाइल (जैसे कि `"whispering"`, `"out of breath"`, `"muttering"` या `"sarcastic"`)—को `speech_metadata` के `style` फ़ील्ड में डालें. हर बार एक जैसा किरदार और परफ़ॉर्मेंस पाने के लिए, [आवाज़ का डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi) में जाकर, पहले से ही पर्सोना डिज़ाइन करें. साथ ही, `style` का इस्तेमाल सिर्फ़ टर्न-लेवल में किए जाने वाले ज़रूरी बदलावों के लिए करें.
- **किसी समय पर होने वाले इवेंट (इनलाइन टैग):** ट्रांसक्रिप्ट में कुछ समय के लिए बोले गए शब्दों के अलावा अन्य आवाज़ें, सांस लेने की आवाज़ या कुछ देर के लिए रुकने की आवाज़ को ऐंगल ब्रैकेट (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`) का इस्तेमाल करके इनलाइन में डालें. सबसे अच्छी ऑडियो क्वालिटी के लिए, ऐंगल ब्रैकेट (`<...>`) का इस्तेमाल करें. साथ ही, आवाज़ के अलावा अन्य साउंड इफ़ेक्ट के बजाय, सिर्फ़ आवाज़ों का इस्तेमाल करें.

| दायरा | कहां जोड़ें | उदाहरण |
| --- | --- | --- |
| **टर्न-लेवल** (टर्न के दौरान जारी रहता है) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **पॉइंट-इन-टाइम** (किसी खास शब्द पर होता है) | `text` (`<...>`) में इनलाइन | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### गति और ठहराव

रिदम और साइलेंस को तीन लेवल पर कंट्रोल किया जा सकता है:

- **विराम चिह्न और एलिप्सिस:** बातचीत में स्वाभाविक रूप से हिचकिचाहट दिखाने के लिए, कॉमा, डैश (`--`), और एलिप्सिस (`...`) का इस्तेमाल करें.
- **इनलाइन पॉज़ टैग:** स्क्रिप्ट में उन जगहों पर `<short pause>` या `<long pause>` डालें जहां स्पीकर को रुकना चाहिए:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **टर्न-लेवल की स्पीड:** पूरे टर्न के दौरान बोलने की स्पीड को कंट्रोल करने के लिए, `speech_metadata` में `"style": "speaking rapidly"` या `"style": "speaking slowly"` सेट करें.

### सुर और पिच

किसी टर्न में उतार-चढ़ाव, पिच, और इन्फ़्लेक्शन को कंट्रोल करने के लिए, **`speech_metadata.style`** का इस्तेमाल करें. उदाहरण के लिए, `"style": "high pitch, cheerful and excited inflection"` या `"style": "monotone and flat"`. अगर बातचीत के बीच में भावना या उतार-चढ़ाव बदलता है, तो स्क्रिप्ट को अलग-अलग टर्न में बांटें. साथ ही, हर टर्न के लिए अलग-अलग `style` वैल्यू का इस्तेमाल करें.

### हाइलाइट करना

ट्रांसक्रिप्ट में कुछ शब्दों को कैपिटल लेटर में लिखें. साथ ही, विराम चिह्न और इनलाइन वोकल टैग का इस्तेमाल करें, ताकि मुख्य शब्दों पर नैचुरल वोकल स्ट्रेस डाला जा सके:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### बोलने में रुकावट और बोली के अलावा अन्य आवाज़ें

आवाज़ के अलावा अन्य मानवीय आवाज़ों को, ऐंगल ब्रैकेट (`<...>`) का इस्तेमाल करके, उसी जगह पर रखें जहां आवाज़ आनी चाहिए. सुझाए गए वोकल टैग में ये शामिल हैं:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>` / `<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>` / `<laughter>` | `<moan>` | `<pant>` | `<pff>` / `<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>` / `<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>` / `<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### बैकचैनल और एक साथ कई लोगों के बोलने की सुविधा

एक से ज़्यादा लोगों के बीच बातचीत में, सुनने वाले की प्रतिक्रियाओं को पाइप कैरेक्टर (`|reaction|`) में रैप करें. ऐसा स्पीकर की बारी में किया जाता है, ताकि प्रतिक्रिया के लिए अलग से बारी न लेनी पड़े और बातचीत स्वाभाविक तरीके से जारी रहे.

- **बैकचैनल पर की गई छोटी बातचीत:** बोलने वाले व्यक्ति के बोलने के दौरान, सुनने वाले लोगों की छोटी प्रतिक्रियाएं (`|oh hmm|`,
  `|oh really?|`, `|absolutely|`) दिखाएं:
  - **पहला टर्न (स्पीकर A):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **दूसरी बारी (स्पीकर B):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **तीसरी बारी (स्पीकर A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **एक साथ बोली गई और बीच-बीच में बोली गई आवाज़:** एक साथ या बीच-बीच में बोली गई आवाज़ को सिम्युलेट करने के लिए, एक से ज़्यादा पाइप सेगमेंट का इस्तेमाल करें. यह सुविधा, दो लोगों के बीच की बातचीत के लिए सबसे अच्छी तरह काम करती है (`gemini-3.8-flash-tts` के साथ सबसे अच्छी तरह काम करती है):
  - **एक साथ काउंटडाउन/कोरस:** `"Let's surprise him on three |ok| ready?"` इसके बाद `"one. two. three. |happy| happy |birthday| birthday!"`
  - **स्पीकर की आवाज़ पूरी तरह से ओवरलैप हो रही है:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### जनरेट किए गए कॉन्टेंट में एकरूपता बनाए रखना और क्या नहीं करना चाहिए

अपनी आवाज़ की पहचान को हर बार एक जैसा रखने के लिए, इन दिशा-निर्देशों का पालन करें:

- **वॉइस डिज़ाइन में, स्टाइल ब्लॉक के बजाय पहले से ही पर्सोना डिज़ाइन करें:**
  पहले के मॉडल से लिए गए लंबे-चौड़े `"Audio Profile"` पैराग्राफ़ और कई बुलेट पॉइंट `"Director's Notes"`, आवाज़ में बदलाव होने की सबसे आम वजह है.
  [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi) में, क्रिएटिविटी का इस्तेमाल करके एक स्थायी कस्टम `voice_...` पर्सोना जनरेट करें. इसके बाद, टीटीएस कॉल के दौरान उस वॉइस आईडी का इस्तेमाल करें.
- **आवाज़ को स्थिर रखने के लिए, आवाज़ के रेफ़रंस पर भरोसा करें (मेटा-निर्देश शामिल न करें):**
  Gemini 3.8 के टीटीएस मॉडल को, सबसे पहले ऑडियो रेफ़रंस पर फ़ोकस करने के लिए ट्रेन किया गया है.
  मॉडल को आवाज़ स्थिर रखने के निर्देश शामिल न करें. जैसे, `"do not switch speaker identity"` या `"maintain identical timbre"`. प्रॉम्प्ट में ज़्यादा टेक्स्ट शामिल करने से, आवाज़ में बदलाव होने की संभावना बढ़ जाती है. स्टाइल से जुड़े गैर-ज़रूरी निर्देश हटा दें. साथ ही, मॉडल को आवाज़ के रेफ़रंस के हिसाब से, नैचुरल तरीके से अलग-अलग आवाज़ों में बोलने दें.
- **`style` में स्पीकर की ऐसी विशेषताओं को बदलने की कोशिश न करें जिन्हें बदला नहीं जा सकता:** `speech_metadata.style` में उम्र, लिंग, नाम या स्थायी लहजे में बदलाव न करें.
  इसके बजाय, Extended Voice Library से किसी क्षेत्र के हिसाब से आवाज़ चुनें या [आवाज़ डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi) की मदद से कोई आवाज़ बनाएं.

### सुझाया गया वर्कफ़्लो

1. **एक बार में ही किरदार तैयार करें:** [आवाज़ डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi) में जाकर अपना किरदार बनाएं. इसके अलावा, एक्सटेंडेड वॉइस लाइब्रेरी से ऐसी क्षेत्रीय आवाज़ चुनें जो आपकी टारगेट भाषा और पर्सोना से मेल खाती हो.
2. **बोलचाल की भाषा में ट्रांसक्रिप्ट लिखें:** `text` को ज़्यादा से ज़्यादा नैचुरल बनाने के लिए, इसे बोलचाल की भाषा में ट्रांसक्रिप्ट के तौर पर लिखें. इसमें बातचीत के दौरान होने वाली रुकावटें और हिचकिचाहट भी शामिल करें. उदाहरण के लिए, `"Oh uh yeah I think... hm, so that's interesting"`.
3. **सबसे पहले, सामान्य टीटीएस को आज़माएं:** सबसे पहले, अपनी ट्रांसक्रिप्ट को खाली `style` फ़ील्ड के साथ सिंथेसाइज़ करें. ज़्यादातर अनुरोधों के लिए, `style` निर्देश की ज़रूरत नहीं होती.
4. **सिर्फ़ बदलावों के लिए छोटे `style` प्रॉम्प्ट जोड़ें:** सिर्फ़ उन टर्न के लिए छोटे `style` स्ट्रिंग (जैसे, `"casual, friendly"` या `"muttering, then reassuring"`) जोड़ें जिनमें डिलीवरी में खास बदलाव करने की ज़रूरत हो. साथ ही, जब आपको एक जैसा बेसलाइन चाहिए, तब सभी टर्न में उसी छोटे स्ट्रिंग का फिर से इस्तेमाल करें.

### सिलसिलेवार बातचीत और वॉइस एजेंट

रीयल-टाइम में बातचीत करने वाले वॉइस एजेंट या सिलसिलेवार बातचीत वाले ऐप्लिकेशन बनाते समय:

- एलएलएम से टेक्स्ट के हिस्से मिलने पर, **हर बार एक टीटीएस कॉल करें**.
- कॉन्फ़िगर किए गए `voice` (पहले से बने, डिज़ाइन किए गए `voice_...` या डुप्लीकेट किए गए `voice_...` / `voicekey_...`) को हर बार स्पीकर की पहचान करने दें. हर बार लंबी अवधि के किरदार की पर्सोना को फिर से न भेजें.
- हर बातचीत के लिए `style` फ़ील्ड को खाली छोड़ दें या पूरी बातचीत के लिए एक छोटी सी स्ट्रिंग (जैसे कि `"casual, friendly"`) भेजें.
- एजेंट के लंबे जवाबों को छोटे-छोटे हिस्सों में बांटें. इसके लिए, स्टाइल से जुड़े ज़्यादा बेहतर प्रॉम्प्ट का इस्तेमाल न करें.

## स्ट्रीमिंग के दौरान बोली जनरेट करना

मॉडल के ऑडियो जनरेट करने के दौरान ही, उसे स्ट्रीम किया जा सकता है. यूनरी अनुरोधों के उलट (ये RIFF हेडर वाली पूरी WAV फ़ाइल दिखाते हैं), **स्ट्रीमिंग अनुरोध, डिफ़ॉल्ट रूप से हेडरलेस रॉ 16-बिट साइंड लिटिल-एंडियन लीनियर पीसीएम (`AUDIO_L16` / `audio/L16;codec=pcm;rate=24000`, 24 kHz, मोनो) चंक दिखाते हैं**. इसलिए, कंटेनर हेडर के बिना ऑडियो चंक को लगातार चलाया या जोड़ा जा सकता है:

### Python

```
from google import genai

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

for chunk in response_stream:
    try:
        data = chunk.candidates[0].content.parts[0].inline_data.data
        # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
    except (IndexError, AttributeError):
        pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speech_metadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }'
```

## ऑडियो आउटपुट के फ़ॉर्मैट

Gemini 3.8 के टीटीएस मॉडल, अलग-अलग डिफ़ॉल्ट ऑडियो फ़ॉर्मैट का इस्तेमाल करते हैं. यह इस बात पर निर्भर करता है कि अनुरोध यूनरी है या स्ट्रीमिंग:

- **यूनरी अनुरोध (`models.generate_content`):** पूरा **WAV
  (`AUDIO_WAV`)** ऑडियो, RIFF हेडर (24 किलोहर्ट्ज़, मोनो, 16-बिट साइंड
  लिटिल-एंडियन पीसीएम) के साथ वापस भेजें. डिकोड किए गए ऑडियो बाइट को सीधे `.wav` फ़ाइल में लिखा जा सकता है. इसके लिए, WAV कंटेनर को मैन्युअल तरीके से जोड़ने की ज़रूरत नहीं होती.
- **स्ट्रीमिंग के अनुरोध (`models.generate_content_stream` / `streamGenerateContent`):**
  डिफ़ॉल्ट रूप से, **हेडरलेस रॉ लीनियर पीसीएम (`AUDIO_L16`)** चंक (24 किलोहर्ट्ज़, मोनो, 16-बिट साइंड लिटिल-एंडियन पीसीएम) दिखाएं, ताकि चंक को स्ट्रीम किया जा सके या हर चंक पर कंटेनर हेडर के बिना लगातार जोड़ा जा सके.

`generationConfig.responseFormat.audio` का इस्तेमाल करके, आउटपुट ऑडियो एन्कोडिंग और सैंपल रेट को बदला जा सकता है:

| `mimeType` की कीमत का | फ़ॉर्मैट | ब्यौरा |
| --- | --- | --- |
| `"AUDIO_WAV"` *(यूनरी डिफ़ॉल्ट)* | WAV (`audio/wav`) | RIFF हेडर वाली पूरी WAV फ़ाइल (24 किलोहर्ट्ज़, मोनो, 16-बिट पीसीएम). |
| `"AUDIO_L16"` *(स्ट्रीमिंग के लिए डिफ़ॉल्ट)* | लीनियर पीसीएम (`audio/l16`) | हेडरलेस रॉ 16-बिट साइंड लिटिल-एंडियन लीनियर पीसीएम. यह मॉडल, स्ट्रीमिंग, कस्टम ऑडियो पाइपलाइन या सिलसिलेवार बातचीत की क्लिप को जोड़ने के लिए सबसे सही है. |
| `"AUDIO_MULAW"` | μ-लॉ (`audio/basic` / `audio/mulaw`) | G.711 μ-लॉ कंपैंडेड ऑडियो. इसका इस्तेमाल आम तौर पर, उत्तरी अमेरिका और जापान में टेलीफ़ोनी के लिए किया जाता है (8 किलोहर्ट्ज़). |
| `"AUDIO_ALAW"` | A-law (`audio/alaw`) | G.711 A-law कंपैंडेड ऑडियो. आम तौर पर, इसका इस्तेमाल यूरोप और अंतरराष्ट्रीय टेलीफ़ोनी (8 किलोहर्ट्ज़) में किया जाता है. |

इसके अलावा, `sampleRate` (उदाहरण के लिए, `24000`, `16000` या `8000` हर्ट्ज़; डिफ़ॉल्ट रूप से `24000` हर्ट्ज़ पर सेट होता है) भी तय किया जा सकता है.

यहां दिए गए उदाहरण में, 24 किलोहर्ट्ज़ पर हेडरलेस रॉ 16-बिट पीसीएम (`AUDIO_L16`) का अनुरोध किया गया है:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "response_format": {
            "audio": {
                "mime_type": "AUDIO_L16",
                "sample_rate": 24000,
            }
        },
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.pcm", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speech_metadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         responseFormat: {
            audio: {
               mimeType: 'AUDIO_L16',
               sampleRate: 24000,
            },
         },
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "responseFormat": {
            "audio": {
              "mimeType": "AUDIO_L16",
              "sampleRate": 24000
            }
          },
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.pcm
```

## सीमाएं

- टीटीएस मॉडल, सिर्फ़ टेक्स्ट वाले इनपुट स्वीकार करते हैं और सिर्फ़ ऑडियो वाले आउटपुट जनरेट करते हैं.
- एक ही अनुरोध में कई स्पीकर की आवाज़ जनरेट करने की सुविधा (`multiSpeakerVoiceConfig`) के तहत, पहले से मौजूद आवाज़ों का इस्तेमाल करके ज़्यादा से ज़्यादा दो स्पीकर की आवाज़ जनरेट की जा सकती है. एक से ज़्यादा किरदार वाले डायलॉग में, कस्टम डिज़ाइन की गई (`voice_...`) या कॉपी की गई (`voice_...` / `voicekey_...`) आवाज़ों को एक साथ इस्तेमाल करने के लिए, हर किरदार के डायलॉग को अलग-अलग सिंथेसाइज़ करें.
  यूनरी अनुरोधों में डिफ़ॉल्ट रूप से 44 बाइट का RIFF हेडर होता है. इसलिए, रॉ पीसीएम (`AUDIO_L16`) का अनुरोध करें या 24 किलोहर्ट्ज़ पीसीएम ऑडियो फ़्रेम को एक साथ जोड़ने से पहले, हर टर्न से WAV हेडर हटाएं.`audio/wav`
- **कस्टम वॉइस के स्टोरेज की सीमाएं और टीटीएल:**
  - **स्टेटफ़ुल आवाज़ें (`store=True`, प्रॉम्प्ट की गई या डुप्लीकेट की गई):** **हर प्रोजेक्ट के लिए ज़्यादा से ज़्यादा 200 आवाज़ें**. इनका **टीटीएल (टाइम-टू-लाइव) एक साल** होता है.
  - **स्टेटलेस वॉइस की (`store=False`, `voicekey_...`):** **सात दिनों का टीटीएल**
    (टाइम-टू-लिव).
- भाषा कवरेज के लिए, [उपलब्ध भाषाएं](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi#languages) सेक्शन देखें.

## आगे क्या करना है

- [आवाज़ के डिज़ाइन](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=hi) की मदद से, नैचुरल लैंग्वेज से अपनी पसंद के मुताबिक़ आवाज़ें बनाएं.
- [वॉइस रेप्लिकेशन](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=hi) की मदद से, किसी मौजूदा स्पीकर की आवाज़ को कॉपी करें.
- [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) और [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) मॉडल के पेजों पर जाकर, मॉडल की खास बातों की तुलना करें.
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) की मदद से, दोनों ओर से ऑडियो के साथ इंटरैक्टिव बातचीत की सुविधा का इस्तेमाल करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-24 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-24 (UTC) को अपडेट किया गया."],[],[]]
