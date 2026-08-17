---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=hi
fetched_at: 2026-08-17T02:16:32.274148+00:00
title: "\u0932\u093f\u0916\u0947 \u0917\u090f \u0936\u092c\u094d\u0926\u094b\u0902 \u0915\u094b \u0938\u0941\u0928\u0928\u0947 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e (\u091f\u0940\u091f\u0940\u090f\u0938) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# लिखे गए शब्दों को सुनने की सुविधा (टीटीएस)

Gemini API, टेक्स्ट इनपुट को एक या एक से ज़्यादा स्पीकर वाले ऑडियो में बदल सकता है. इसके लिए, Gemini की टेक्स्ट को बोली में बदलने (टीटीएस) की सुविधा का इस्तेमाल किया जाता है.
लिखे गए शब्दों को सुनने की सुविधा (टीटीएस) को *[कंट्रोल किया जा सकता है](#controllable)*. इसका मतलब है कि बातचीत को स्ट्रक्चर करने और ऑडियो की *स्टाइल*, *उच्चारण*, *रफ़्तार*, और *टोन* को गाइड करने के लिए, नैचुरल लैंग्वेज का इस्तेमाल किया जा सकता है.

[Google AI Studio में आज़माएं](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=hi)

टीटीएस की सुविधा, [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) के ज़रिए उपलब्ध कराई गई स्पीच जनरेशन की सुविधा से अलग है. इसे इंटरैक्टिव, अनस्ट्रक्चर्ड ऑडियो, और मल्टीमॉडल इनपुट और आउटपुट के लिए डिज़ाइन किया गया है. लाइव एपीआई, बातचीत के कॉन्टेक्स्ट को डाइनैमिक तरीके से समझने में बेहतर है. वहीं, Gemini API के ज़रिए टीटीएस की सुविधा, उन स्थितियों के लिए तैयार की गई है जिनमें स्टाइल और आवाज़ पर बारीकी से कंट्रोल करने के साथ-साथ, सटीक टेक्स्ट सुनाने की ज़रूरत होती है. जैसे, पॉडकास्ट या ऑडियो बुक जनरेट करना.

इस गाइड में, टेक्स्ट से एक स्पीकर और एक से ज़्यादा स्पीकर वाला ऑडियो जनरेट करने का तरीका बताया गया है.

## शुरू करने से पहले

पक्का करें कि आपने Gemini के ऐसे मॉडल का इस्तेमाल किया हो जिसमें Gemini की लिखाई को बोली में बदलने (टीटीएस) की सुविधा उपलब्ध हो. इसके बारे में [साथ काम करने वाले मॉडल](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#supported-models) सेक्शन में बताया गया है. सबसे अच्छे नतीजे पाने के लिए, यह तय करें कि आपके इस्तेमाल के हिसाब से कौनसा मॉडल सबसे सही है.

ऐप्लिकेशन बनाना शुरू करने से पहले, [AI Studio में Gemini के टीटीएस मॉडल को टेस्ट करना](https://aistudio.google.com/generate-speech?hl=hi) आपके लिए फ़ायदेमंद हो सकता है.

## एक व्यक्ति की आवाज़ में टीटीएस

टेक्स्ट को एक स्पीकर वाले ऑडियो में बदलने के लिए, रिस्पॉन्स मोड को "ऑडियो" पर सेट करें. इसके बाद, `VoiceConfig` सेट किए गए `SpeechConfig` ऑब्जेक्ट को पास करें.
आपको पहले से मौजूद [आउटपुट की आवाज़ों](#voices) में से किसी एक को चुनना होगा.

इस उदाहरण में, मॉडल से मिले आउटपुट ऑडियो को वेव फ़ाइल में सेव किया गया है:

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        },
        "model": "gemini-3.1-flash-tts-preview",
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode >out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## एक से ज़्यादा लोगों की आवाज़ में टीटीएस

एक से ज़्यादा स्पीकर से ऑडियो चलाने के लिए, आपको `MultiSpeakerVoiceConfig` ऑब्जेक्ट की ज़रूरत होगी. इसमें हर स्पीकर (दो तक) को `SpeakerVoiceConfig` के तौर पर कॉन्फ़िगर किया गया हो.
आपको हर `speaker` को उन नामों से तय करना होगा जिनका इस्तेमाल [प्रॉम्प्ट](#controllable) में किया गया है:

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: prompt }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                        {
                           speaker: 'Joe',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Kore' }
                           }
                        },
                        {
                           speaker: 'Jane',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Puck' }
                           }
                        }
                  ]
               }
            }
      }
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [{
    "parts":[{
      "text": "TTS the following conversation between Joe and Jane:
                Joe: Hows it going today Jane?
                Jane: Not too bad, how about you?"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [{
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }, {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }]
      }
    }
  },
  "model": "gemini-3.1-flash-tts-preview",
}' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
    base64 --decode > out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## प्रॉम्प्ट की मदद से, बोलने के तरीके को कंट्रोल करना

एक या एक से ज़्यादा स्पीकर के लिए, टीटीएस की स्टाइल, टोन, लहजे, और गति को कंट्रोल किया जा सकता है. इसके लिए, नैचुरल लैंग्वेज प्रॉम्प्ट
या [ऑडियो टैग](#transcript-tags) का इस्तेमाल करें.
उदाहरण के लिए, एक स्पीकर वाले प्रॉम्प्ट में, यह कहा जा सकता है:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

एक से ज़्यादा स्पीकर वाले प्रॉम्प्ट में, मॉडल को हर स्पीकर का नाम और उससे जुड़ी ट्रांसक्रिप्ट दें. हर स्पीकर के लिए अलग-अलग निर्देश भी दिए जा सकते हैं:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

अपनी बात को ज़्यादा असरदार बनाने के लिए, [आवाज़ का ऐसा विकल्प](#voices) इस्तेमाल करें जो आपकी स्टाइल या भावना के मुताबिक हो. उदाहरण के लिए, पिछले प्रॉम्प्ट में *एन्सेलडस* की सांस लेने की आवाज़ से "थका हुआ" और "उबाऊ" पर ज़ोर दिया जा सकता है. वहीं, *पक* की तेज़ आवाज़ से "उत्साहित" और "खुश" पर ज़ोर दिया जा सकता है.

## ऑडियो में बदलने के लिए प्रॉम्प्ट जनरेट किया जा रहा है

टीटीएस मॉडल सिर्फ़ ऑडियो आउटपुट देते हैं. हालांकि, पहले ट्रांसक्रिप्ट जनरेट करने के लिए [अन्य मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi) का इस्तेमाल किया जा सकता है. इसके बाद, उस ट्रांसक्रिप्ट को टीटीएस मॉडल को पढ़कर सुनाने के लिए भेजा जा सकता है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3.6-flash",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to handle audio output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

const transcript = await ai.models.generateContent({
   model: "gemini-3.6-flash",
   contents: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const response = await ai.models.generateContent({
   model: "gemini-3.1-flash-tts-preview",
   contents: transcript,
   config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
         multiSpeakerVoiceConfig: {
            speakerVoiceConfigs: [
                   {
                     speaker: "Dr. Anya",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Kore"},
                     }
                  },
                  {
                     speaker: "Liam",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Puck"},
                    }
                  }
                ]
              }
            }
      }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## आवाज़ के विकल्प

TTS मॉडल, `voice_name` फ़ील्ड में आवाज़ के इन 30 विकल्पों के साथ काम करते हैं:

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | **Charon** -- *Informative* |
| **Kore** -- *Firm* | **Fenrir** -- *Excitable* | **Leda** -- *यूथफ़ुल* |
| **Orus** -- *फ़र्म* | **Aoede** -- *Breezy* | **Callirrhoe** -- *ईज़ी-गोइंग* |
| **ऑटोनो** -- *तेज रोशनी* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *शांत स्वभाव वाला* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| **एरिनोमे** -- *हटाएं* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *Informative* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *Mature* | **Pulcherrima** -- *Forward* |
| **Achird** -- *Friendly* | **Zubenelgenubi** -- *कैज़ुअल* | **Vindemiatrix** -- *जेंटल* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Knowledgeable* | **Sulafat** -- *Warm* |

[AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में जाकर, आवाज़ के सभी विकल्प सुने जा सकते हैं.

## इस्तेमाल की जा सकने वाली भाषाएं

टीटीएस मॉडल, इनपुट की भाषा का पता अपने-आप लगा लेते हैं. इन भाषाओं में यह सुविधा इस्तेमाल की जा सकती है:

| भाषा | BCP-47 कोड | भाषा | BCP-47 कोड |
| --- | --- | --- | --- |
| अरबी | ar | फ़िलिपीनी | fil |
| बांग्ला | bn | फ़िनिश | fi |
| डच | nl | गैलिशियन | gl |
| अंग्रेज़ी | en | जॉर्जियन | ka |
| फ़्रांसीसी | fr | ग्रीक | el |
| जर्मन | de | गुजराती | gu |
| हिन्दी | hi | हैतियन क्रिओल | ht |
| इंडोनेशियन | आईडी | हीब्रू | वह |
| इटैलियन | it | हंगेरियन | hu |
| जैपनीज़ | ja | आइसलैंडिक | है |
| कोरियन | ko | जावानीज़ | jv |
| मराठी | mr | कन्नड़ | kn |
| पोलिश | pl | कोंकणी | kok |
| पॉर्चुगीज़ | pt | लाओ | lo |
| रोमेनियन | ro | लैटिन | la |
| रशियन | ru | लातवियन | lv |
| स्पेनिश | es | लिथुएनियन | lt |
| तमिल | ta | लक्ज़मबर्गिश | lb |
| तेलुगु | te | मैसेडोनियन | mk |
| थाई | th | मैथिली | mai |
| टर्किश | tr | मैलगासी | mg |
| यूक्रेनियन | uk | मलय | ms |
| वियतनामीज़ | vi | मलयालम | ml |
| अफ़्रीकान्स | af | मंगोलियन | mn |
| अल्बेनियन | sq | नेपाली | ne |
| अमहैरिक | am | नॉर्वीजन, बुकमॉल | nb |
| आर्मीनियन | hy | नॉर्वेजियन, नायनॉर्स्क | nn |
| अज़रबैजानी | az | ओड़िया | या |
| बॉस्क | eu | पश्तो | ps |
| बेलारूसी | be | फ़ारसी | fa |
| बल्गैरियन | bg | पंजाबी | pa |
| बर्मीज़ | my | सर्बियन | sr |
| कैटलैन | ca | सिंधी | sd |
| सेबुआनो | ceb | सिंहली | si |
| चाइनीज़, मैंडरिन | cmn | स्लोवाक | sk |
| क्रोएशियन | घंटा | स्लोवेनियन | sl |
| चेक | cs | स्वाहिली | sw |
| डेनिश | da | स्वीडिश | sv |
| एस्टोनियन | et | उर्दू | ur |

## इन मॉडल के साथ काम करता है

| मॉडल | एक व्यक्ति बोल रहा है | मल्टीस्पीकर |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=hi) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=hi) | ✔️ | ✔️ |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=hi) | ✔️ | ✔️ |

## प्रॉम्प्ट से जुड़ी गाइड

**Gemini Native Audio Generation Text-to-Speech (TTS)** मॉडल, पारंपरिक टीटीएस मॉडल से अलग है. यह एक लार्ज लैंग्वेज मॉडल का इस्तेमाल करता है. इस मॉडल को ***यह न सिर्फ़ पता होता है कि क्या बोलना है, बल्कि यह भी पता होता है कि कैसे बोलना है***.

मॉडल, ट्रांसक्रिप्ट को अपने-आप समझ लेगा और यह तय करेगा कि आपके शब्दों को कैसे डिलीवर किया जाना चाहिए. सामान्य ट्रांसक्रिप्ट, बिना किसी अतिरिक्त प्रॉम्प्ट के स्वाभाविक लगती हैं. हालांकि, Gemini के टीटीएस में ऐसे टूल भी शामिल हैं जिनका इस्तेमाल करके, इसे कंट्रोल किया जा सकता है.

इस गाइड का मकसद, ऑडियो अनुभव को बेहतर बनाने के लिए बुनियादी दिशा-निर्देश देना और नए आइडिया देना है. हम **टैग** से शुरुआत करेंगे, ताकि आपको तुरंत इनलाइन कंट्रोल मिल सके. इसके बाद, हम बेहतर परफ़ॉर्मेंस के लिए **प्रॉम्प्ट स्ट्रक्चर** के बारे में जानेंगे.

### ऑडियो टैग

टैग, इनलाइन मॉडिफ़ायर होते हैं. जैसे, `[whispers]` या `[laughs]`. इनसे आपको डिलीवरी पर ज़्यादा कंट्रोल मिलता है. इनका इस्तेमाल करके, ट्रांसक्रिप्ट की किसी लाइन या सेक्शन की टोन, गति, और भावनात्मक स्थिति में बदलाव किया जा सकता है. इनका इस्तेमाल, परफ़ॉर्मेंस में
अचानक बोले जाने वाले शब्द और कुछ अन्य बिना बोले जाने वाले साउंड जोड़ने के लिए भी किया जा सकता है. जैसे,
`[cough]`, `[sighs]` या `[gasp]`.

इस बारे में कोई पूरी सूची नहीं है कि कौनसे टैग काम करते हैं और कौनसे नहीं. हमारा सुझाव है कि अलग-अलग भावनाओं और एक्सप्रेशन के साथ एक्सपेरिमेंट करें, ताकि यह देखा जा सके कि आउटपुट में क्या बदलाव होता है.

अगर आपकी ट्रांसक्रिप्ट अंग्रेज़ी में नहीं है, तो हमारा सुझाव है कि आप बेहतर नतीजों के लिए, अंग्रेज़ी ऑडियो टैग का इस्तेमाल करें.

**ऑडियो टैग का क्रिएटिव तरीके से इस्तेमाल करना**

ऑडियो टैग की मदद से, अलग-अलग तरह के बदलाव किए जा सकते हैं. यहां कुछ उदाहरण दिए गए हैं. इनमें एक ही बात कही गई है, लेकिन इस्तेमाल किए गए टैग के आधार पर डिलीवरी में बदलाव किया गया है.

किसी लाइन की शुरुआत में टैग जोड़कर, डिलीवरी के लहजे में बदलाव किया जा सकता है. इससे स्पीकर को उत्साहित, ऊब या अनिच्छुक दिखाया जा सकता है:

- `[excitedly]` नमस्ते, मैं टेक्स्ट को स्पीच में बदलने वाला नया मॉडल हूं. मैं किसी भी बात को कई अलग-अलग तरीकों से कह सकता हूं. आज मैं आपकी किस तरह मदद कर सकता हूं?
- `[bored]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…
- `[reluctantly]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…

टैग का इस्तेमाल, डिलीवरी की स्पीड को बदलने के लिए भी किया जा सकता है. इसके अलावा, स्पीड को किसी शब्द पर ज़ोर देने के साथ भी जोड़ा जा सकता है:

- `[very fast]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…
- `[very slow]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…
- `[sarcastically, one painfully slow word at a time]` नमस्ते, मैं टेक्स्ट को
  बोली में बदलने वाला नया मॉडल हूँ…

आपके पास खास सेक्शन पर भी सटीक कंट्रोल होता है. इसका मतलब है कि आप एक हिस्से को धीरे से और दूसरे हिस्से को ज़ोर से बोल सकते हैं.

- `[whispers]` नमस्ते, मैं लिखाई को बोली में बदलने वाला नया मॉडल हूं. `[shouting]` मैं कई अलग-अलग तरीकों से बोल सकता हूं. `[whispers]` आज मैं आपकी किस तरह मदद कर सकता हूं

इसके अलावा, आपके पास अपनी पसंद के किसी भी क्रिएटिव आइडिया को आज़माने का विकल्प होता है:

- `[like a cartoon dog]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…
- `[like dracula]` नमस्ते, मैं लिखाई को बोली में बदलने वाला एक नया मॉडल हूँ…

आम तौर पर इस्तेमाल किए जाने वाले टैग में ये शामिल हैं:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

टैग की मदद से, ट्रांसक्रिप्ट को आसानी से और तुरंत कंट्रोल किया जा सकता है. ज़्यादा कंट्रोल के लिए, इन्हें कॉन्टेक्स्ट प्रॉम्प्ट के साथ मिलाकर इस्तेमाल किया जा सकता है. इससे परफ़ॉर्मेंस की टोन और वाइब सेट की जा सकती है.

### ऐडवांस प्रॉम्प्टिंग

ऐडवांस प्रॉम्प्ट को, मॉडल के लिए सिस्टम के निर्देश के तौर पर माना जा सकता है. इससे मॉडल को ज़्यादा कॉन्टेक्स्ट मिलता है और परफ़ॉर्मेंस को कंट्रोल करने में मदद मिलती है.

एक अच्छे प्रॉम्प्ट में ये एलिमेंट शामिल होने चाहिए, ताकि आपको बेहतर परफ़ॉर्मेंस मिल सके:

- **ऑडियो प्रोफ़ाइल** - इससे आवाज़ की पहचान तय होती है. इसमें किरदार की पहचान, मूल रूप, और उम्र, बैकग्राउंड वगैरह जैसी अन्य विशेषताएं शामिल होती हैं.
- **सीन** - इससे कहानी की शुरुआत होती है. इसमें आस-पास के माहौल और "वाइब", दोनों के बारे में बताया गया है.
- **डायरेक्टर के नोट** - परफ़ॉर्मेंस से जुड़ी गाइडेंस. इसमें यह बताया जा सकता है कि आपके वर्चुअल टैलेंट के लिए किन निर्देशों पर ध्यान देना ज़रूरी है. उदाहरण के लिए, स्टाइल, सांस लेने का तरीका, गति, शब्दों का उच्चारण, और लहजा.
- **कॉन्टेक्स्ट का सैंपल** - इससे मॉडल को कॉन्टेक्स्ट के हिसाब से शुरुआती जानकारी मिलती है, ताकि आपका वर्चुअल ऐक्टर, आपके सेट अप किए गए सीन में नैचुरल तरीके से एंट्री कर सके.
- **ट्रांसक्रिप्ट** - वह टेक्स्ट जिसे मॉडल बोलेगा. बेहतर परफ़ॉर्मेंस के लिए, ध्यान रखें कि ट्रांसक्रिप्ट का विषय और लिखने का तरीका, आपके दिए गए निर्देशों से मेल खाना चाहिए.
- **ऑडियो टैग** - ये ऐसे मॉडिफ़ायर होते हैं जिन्हें ट्रांसक्रिप्ट में डाला जा सकता है. इनसे यह तय किया जाता है कि टेक्स्ट का वह हिस्सा कैसे डिलीवर किया जाएगा. जैसे, `[whispers]` या `[shouting]`.

पूरे प्रॉम्प्ट का उदाहरण:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
```

### ज़्यादा जानकारी देने वाली प्रॉम्प्टिंग की रणनीतियां

आइए, प्रॉम्प्ट के हर एलिमेंट को समझते हैं.

#### ऑडियो प्रोफ़ाइल

कैरेक्टर के बारे में कम शब्दों में जानकारी दें.

- **नाम.** अपने किरदार को नाम देने से, मॉडल को बेहतर तरीके से काम करने में मदद मिलती है. सीन और कॉन्टेक्स्ट सेट करते समय, किरदार का नाम इस्तेमाल करें
- **भूमिका.** सीन में किरदार की मुख्य पहचान और टाइप. जैसे, रेडियो डीजे, पॉडकास्टर, न्यूज़ रिपोर्टर वगैरह.

उदाहरण:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### दृश्य

सीन के लिए कॉन्टेक्स्ट सेट करें. इसमें लोकेशन, मूड, और माहौल की जानकारी शामिल करें, ताकि टोन और वाइब तय की जा सके. बताओ कि किरदार के आस-पास क्या हो रहा है और इसका उस पर क्या असर पड़ रहा है. सीन से, पूरे इंटरैक्शन के लिए एनवायरमेंटल कॉन्टेक्स्ट मिलता है. साथ ही, यह ऐक्टिंग परफ़ॉर्मेंस को हल्के और स्वाभाविक तरीके से गाइड करता है.

उदाहरण:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### डायरेक्टर के नोट

इस ज़रूरी सेक्शन में, परफ़ॉर्मेंस से जुड़े खास दिशा-निर्देश शामिल होते हैं. आपके पास अन्य सभी एलिमेंट को छोड़ने का विकल्प होता है. हालांकि, हमारा सुझाव है कि आप इस एलिमेंट को शामिल करें.

सिर्फ़ उन चीज़ों को तय करें जो परफ़ॉर्मेंस के लिए ज़रूरी हैं. साथ ही, यह ध्यान रखें कि ज़रूरत से ज़्यादा जानकारी न दी गई हो. बहुत ज़्यादा सख्त नियम लागू करने से, मॉडल की क्रिएटिविटी सीमित हो जाएगी. साथ ही, इससे परफ़ॉर्मेंस खराब हो सकती है. भूमिका और सीन की जानकारी के साथ-साथ, परफ़ॉर्मेंस से जुड़े खास नियमों का भी ध्यान रखें.

आम तौर पर, **स्टाइल, पेसिंग, और ऐक्सेंट** के बारे में निर्देश दिए जाते हैं. हालांकि, मॉडल को सिर्फ़ इन्हीं निर्देशों के हिसाब से काम करने की ज़रूरत नहीं होती. अपनी परफ़ॉर्मेंस के लिए ज़रूरी किसी भी अन्य जानकारी को शामिल करने के लिए, कस्टम निर्देश जोड़ें. साथ ही, ज़रूरत के हिसाब से ज़्यादा या कम जानकारी दें.

उदाहरण के लिए:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**स्टाइल:**

इससे जनरेट की गई स्पीच का टोन और स्टाइल सेट किया जाता है. परफ़ॉर्मेंस को बेहतर बनाने के लिए, इसमें उत्साहित, ऊर्जावान, शांत, बोर वगैरह जैसे शब्द शामिल करें. ज़्यादा से ज़्यादा जानकारी दें: *"Infectious enthusiasm. *"ऊर्जावान और उत्साही"* कहने के बजाय,*�

इसके अलावा, वॉइसओवर इंडस्ट्री में लोकप्रिय शब्दों का भी इस्तेमाल किया जा सकता है. जैसे, "वोकल स्माइल". स्टाइल की जितनी चाहें उतनी विशेषताएं जोड़ी जा सकती हैं.

उदाहरण:

सिंपल इमोशन

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

ज़्यादा गहराई

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

पेचीदा लेवल

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**एक्सेंट:**

बताएं कि आपको किस ऐक्सेंट में ऑडियो चाहिए. प्रॉम्प्ट में जितनी ज़्यादा जानकारी दी जाएगी, नतीजे उतने ही बेहतर होंगे. उदाहरण के लिए, "*ब्रिटिश लहजा*" के बजाय "*क्रॉयडन, इंग्लैंड में बोले जाने वाले ब्रिटिश लहजे*" का इस्तेमाल करें.

उदाहरण:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a DJ from Brixton, London
...
```

**पेसिंग:**

पूरे लेख में पेसिंग और पेस में बदलाव.

उदाहरण:

सिंपल

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

ज़्यादा गहराई

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

पेचीदा लेवल

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### ट्रांसक्रिप्ट और ऑडियो टैग

ट्रांसक्रिप्ट में वे शब्द होते हैं जिन्हें मॉडल बोलेगा. ऑडियो टैग, स्क्वेयर ब्रैकेट में मौजूद एक शब्द होता है. इससे यह पता चलता है कि किसी शब्द को कैसे बोला जाना चाहिए, टोन में बदलाव कैसे किया जाना चाहिए या किसी शब्द को कैसे शामिल किया जाना चाहिए.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**इसे आज़माएं**

इन उदाहरणों को [AI Studio](https://aistudio.google.com/generate-speech?hl=hi) पर खुद आज़माएं. हमारे [TTS ऐप्लिकेशन](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=hi) का इस्तेमाल करें और Gemini को डायरेक्टर की कुर्सी पर बैठने दें. बेहतरीन परफ़ॉर्मेंस देने के लिए, इन बातों का ध्यान रखें:

- ध्यान रखें कि पूरा प्रॉम्प्ट एक जैसा हो. स्क्रिप्ट और निर्देश, दोनों एक साथ मिलकर अच्छी परफ़ॉर्मेंस देते हैं.
- आपको हर चीज़ के बारे में बताने की ज़रूरत नहीं है. कभी-कभी, मॉडल को कुछ जानकारी अपने हिसाब से भरने देने से, जवाब ज़्यादा स्वाभाविक लगता है. (ठीक वैसे ही जैसे कोई टैलेंटेड ऐक्टर)
- अगर आपको कभी भी कोई परेशानी हो, तो Gemini से अपनी स्क्रिप्ट या परफ़ॉर्मेंस को बेहतर बनाने में मदद लें.

## स्ट्रीमिंग के दौरान स्पीच जनरेट करना

मॉडल से ऑडियो जनरेट होने के दौरान ही, उसे स्ट्रीम किया जा सकता है. इससे, इंतज़ार के समय को कम करने में मदद मिलती है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response_stream = client.models.generate_content_stream(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

for chunk in response_stream:
   try:
      data = chunk.candidates[0].content.parts[0].inline_data.data
      # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
      # Process the audio chunk (e.g., play it or write to a file)
   except (IndexError, AttributeError):
      pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        }
    }'
```

## सीमाएं

- टीटीएस मॉडल, सिर्फ़ टेक्स्ट इनपुट ले सकते हैं और ऑडियो आउटपुट जनरेट कर सकते हैं.
- टीटीएस सेशन के लिए, [कॉन्टेक्स्ट विंडो](https://ai.google.dev/gemini-api/docs/long-context?hl=hi) की सीमा 32 हज़ार टोकन होती है.
- भाषा से जुड़ी सहायता के लिए, [भाषाएं](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#languages) सेक्शन देखें.
- टीटीएस की सुविधा, 3.1 से पहले के वर्शन वाले मॉडल के लिए स्ट्रीमिंग की सुविधा के साथ काम नहीं करती. हालांकि, यह सुविधा `gemini-3.1-flash-tts-preview` और उसके बाद के वर्शन के साथ काम करती है.

Gemini 3.1 Flash के टीटीएस प्रीव्यू मॉडल का इस्तेमाल करके स्पीच जनरेट करने पर, ये पाबंदियां लागू होती हैं:

- **प्रॉम्प्ट में दिए गए निर्देशों के हिसाब से आवाज़ न होना:** ऐसा हो सकता है कि मॉडल का आउटपुट, चुनी गई आवाज़ से हमेशा मेल न खाए. इस वजह से, ऑडियो आपकी उम्मीद के मुताबिक नहीं लगता. आवाज़ की टोन में अंतर होने से बचने के लिए (जैसे, किसी पुरुष की भारी आवाज़ में किसी छोटी लड़की की तरह बोलने की कोशिश करना), पक्का करें कि आपके प्रॉम्प्ट में लिखी गई टोन और कॉन्टेक्स्ट, चुने गए स्पीकर की प्रोफ़ाइल के हिसाब से हो.
- **लंबे आउटपुट की क्वालिटी:** कुछ मिनट से ज़्यादा लंबे जनरेट किए गए आउटपुट में, आवाज़ की क्वालिटी और एकरूपता में अंतर आ सकता है. हमारा सुझाव है कि आप अपनी ट्रांसक्रिप्ट को छोटे-छोटे हिस्सों में बांट लें.
- **कभी-कभी टेक्स्ट टोकन मिलते हैं:** मॉडल कभी-कभी ऑडियो टोकन के बजाय टेक्स्ट टोकन देता है. इस वजह से, सर्वर अनुरोध को पूरा नहीं कर पाता और `500` गड़बड़ी का मैसेज दिखाता है. ऐसा बहुत कम अनुरोधों में होता है. इसलिए, आपको अपने ऐप्लिकेशन में, अपने-आप फिर से कोशिश करने का लॉजिक लागू करना चाहिए, ताकि इन अनुरोधों को हैंडल किया जा सके.
- **प्रॉम्प्ट क्लासिफ़ायर के ज़रिए प्रॉम्प्ट को गलत तरीके से अस्वीकार करना:** अस्पष्ट प्रॉम्प्ट, स्पीच सिंथेसिस क्लासिफ़ायर को ट्रिगर नहीं कर पाते हैं. इस वजह से, अनुरोध अस्वीकार कर दिया जाता है (`PROHIBITED_CONTENT`) या मॉडल, स्टाइल से जुड़े निर्देशों और डायरेक्टर के नोट को पढ़कर सुनाता है. अपने प्रॉम्प्ट की पुष्टि करें. इसके लिए, एक साफ़ तौर पर प्रीऐंबल जोड़ें. इसमें मॉडल को स्पीच सिंथेसाइज़ करने के निर्देश दिए गए हों. साथ ही, इसमें साफ़ तौर पर यह बताया गया हो कि बोली गई बातों का ट्रांसक्रिप्ट कहां से शुरू होता है.

## आगे क्या करना है

- [ऑडियो जनरेट करने से जुड़ी कुकबुक](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=hi) आज़माएं.
- Gemini के [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) में, इंटरैक्टिव ऑडियो जनरेट करने के विकल्प मिलते हैं. इन्हें अन्य मोड के साथ इंटरलीव किया जा सकता है.
- ऑडियो *इनपुट* के साथ काम करने के लिए, [ऑडियो समझने](https://ai.google.dev/gemini-api/docs/audio?hl=hi) से जुड़ी गाइड पढ़ें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-30 (UTC) को अपडेट किया गया."],[],[]]
