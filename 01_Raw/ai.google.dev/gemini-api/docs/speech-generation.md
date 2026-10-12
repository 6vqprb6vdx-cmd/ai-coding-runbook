---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi
fetched_at: 2026-10-12T07:01:42.243501+00:00
title: "\u0932\u093f\u0916\u0947 \u0917\u090f \u0936\u092c\u094d\u0926\u094b\u0902 \u0915\u094b \u0938\u0941\u0928\u0928\u0947 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e (\u091f\u0940\u091f\u0940\u090f\u0938) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# लिखे गए शब्दों को सुनने की सुविधा (टीटीएस)

Gemini API, टेक्स्ट इनपुट को एक या एक से ज़्यादा स्पीकर वाले ऑडियो में बदल सकता है. इसके लिए, Gemini की लिखाई को बोली में बदलने (टीटीएस) की सुविधा का इस्तेमाल किया जाता है.
टेक्स्ट को स्पीच में बदलने की सुविधा को *[कंट्रोल किया जा सकता है](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#controllable)*. इसका मतलब है कि ऑडियो की *स्टाइल*, *एसेंट*, *रफ़्तार*, और *टोन* को कंट्रोल करने के लिए, स्ट्रक्चर्ड टर्न मेटाडेटा (`speech_metadata`) और इनलाइन वोकल टैग को एक साथ इस्तेमाल किया जा सकता है.

टीटीएस की सुविधा, [लाइव एपीआई](https://ai.google.dev/gemini-api/docs/live?hl=hi) के ज़रिए उपलब्ध कराई गई स्पीच जनरेशन की सुविधा से अलग है. इसे इंटरैक्टिव, अनस्ट्रक्चर्ड ऑडियो, और मल्टीमॉडल इनपुट और आउटपुट के लिए डिज़ाइन किया गया है. लाइव एपीआई, बातचीत के कॉन्टेक्स्ट को डाइनैमिक तरीके से समझने में बेहतर है. वहीं, Gemini API के ज़रिए टीटीएस की सुविधा, उन स्थितियों के लिए तैयार की गई है जिनमें स्टाइल और आवाज़ पर बारीकी से कंट्रोल के साथ, सटीक टेक्स्ट सुनाने की ज़रूरत होती है. जैसे, पॉडकास्ट या ऑडियो बुक जनरेट करना.

इस गाइड में बताया गया है कि [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) (`gemini-3.8-flash-tts`) और [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) (`gemini-3.8-flash-lite-tts`) का इस्तेमाल करके, टेक्स्ट से एक या एक से ज़्यादा स्पीकर की आवाज़ में ऑडियो कैसे जनरेट करें.

## शुरू करने से पहले

पक्का करें कि आपने [साथ काम करने वाले मॉडल](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#supported-models) सेक्शन में दिए गए Gemini TTS मॉडल का इस्तेमाल किया हो. साथ ही, Google GenAI SDK के सबसे नए वर्शन (Python के लिए `google-genai >= 2.25.0` या JavaScript/TypeScript के लिए `@google/genai >= 2.24.0`) पर अपग्रेड करें या REST API का इस्तेमाल करें.
बेहतर नतीजों के लिए, [किस मॉडल का इस्तेमाल कब करना चाहिए](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#when-to-use-which-model) लेख पढ़ें. इससे आपको अपने वर्कलोड के लिए सबसे सही मॉडल चुनने में मदद मिलेगी.

ऐप्लिकेशन बनाना शुरू करने से पहले, [AI Studio में Gemini के टीटीएस मॉडल को टेस्ट करना](https://aistudio.google.com/generate-speech?hl=hi) आपके लिए फ़ायदेमंद हो सकता है.

## एक ही आवाज़ में टीटीएस की सुविधा

Gemini 3.8 के टीटीएस मॉडल का इस्तेमाल करके, टेक्स्ट को एक स्पीकर वाले ऑडियो में बदलने के लिए, `input` में शब्दशः ट्रांसक्रिप्ट पास करें. साथ ही, `speech_metadata` एनोटेशन का इस्तेमाल करके, टर्न-लेवल स्टाइलिंग अटैच करें और `generation_config.speech_config` में अपनी आवाज़ कॉन्फ़िगर करें. आपके पास पहले से मौजूद [आवाज़ के विकल्प](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#voices), एक्सटेंडेड वॉइस लाइब्रेरी (`GET /v1beta/voices`), कस्टम [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) आईडी (`voice_...`), [वॉइस रेप्लिकेशन](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi) आईडी (`voice_...` या बिना स्थिति वाली वैकल्पिक `voicekey_...`) में से कोई एक आवाज़ चुनने का विकल्प होता है.

इस उदाहरण में, मॉडल से मिले डिफ़ॉल्ट WAV आउटपुट ऑडियो (`audio/wav`) को सीधे किसी फ़ाइल में सेव किया गया है:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

Python और JavaScript SDK में, जनरेट किए गए ऑडियो डेटा को वापस पाने के लिए, `interaction.output_audio` सुविधा प्रॉपर्टी का इस्तेमाल किया जा सकता है. यह प्रॉपर्टी, जनरेट किए गए आखिरी ऑडियो ब्लॉक को दिखाती है. रॉ REST JSON रिस्पॉन्स में, base64-encoded ऑडियो को `steps[].content[].data` में सेव किया जाता है. सुविधा प्रॉपर्टी के बारे में ज़्यादा जानने के लिए, [इंटरैक्शन की खास जानकारी](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi#convenience-properties) देखें.

## एक से ज़्यादा लोगों की आवाज़ में टीटीएस

एक से ज़्यादा स्पीकर वाले डायलॉग के लिए, `speech_config.speakers` में दो स्पीकर कॉन्फ़िगर करें. इसके बाद, हर टर्न को अलग-अलग टेक्स्ट आइटम के तौर पर पास करें. साथ ही, `speech_metadata` एनोटेशन में `speaker` और टर्न-लेवल का `style` बताएं. ध्यान दें कि `speech_config`, एक स्पीकर के लिए जनरेट करने के लिए एक ऐरे (`[{"voice": "..."}]`) और एक से ज़्यादा स्पीकर के लिए जनरेट करने के लिए एक ऑब्जेक्ट (`{"speakers": [...]}`) स्वीकार करता है:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "How's it going today Jane?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                }],
            },
            {
                "type": "text",
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Joe", "voice": "Puck"},
                {"speaker": "Jane", "voice": "Kore"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: "How's it going today Jane?",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               }],
            },
            {
               type: 'text',
               text: 'Not too bad, how about you? Ready to test these new voices?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Joe', voice: 'Puck' },
               { speaker: 'Jane', voice: 'Kore' },
            ],
         },
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "TTS the following conversation between Joe and Jane:\n" +
        "Joe: How's it going today Jane?\n" +
        "Jane: Not too bad, how about you?"

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Joe"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Jane"), Voice: genai.Ptr("Puck")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput(prompt),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "How'\''s it going today Jane?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }]
        },
        {
          "type": "text",
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Jane",
            "style": "calm and relaxed"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "mode": "conversational",
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## मेटाडेटा और टैग की मदद से, बोलने के तरीके को कंट्रोल करना

Gemini 3.8 TTS, `text` फ़ील्ड को हूबहू ट्रांसक्रिप्ट के तौर पर इस्तेमाल करता है. स्टेज के निर्देशों को तेज़ आवाज़ में सुने बिना डिलीवरी को कंट्रोल करने के लिए, अपने निर्देशों को स्कोप के हिसाब से बांटें:

- **पूरे टर्न के लिए एक जैसी डिलीवरी (`speech_metadata.style`):** `style` फ़ील्ड में, पूरे टर्न के लिए एक जैसी भावनाएं, डिलीवरी स्टाइल, उतार-चढ़ाव, गति, और आवाज़ का इस्तेमाल करें. उदाहरण के लिए, `"style": "whispered urgently"`, `"style": "out of breath"` या `"style": "warm and enthusiastic"`.
- **किसी समय पर होने वाले इवेंट (इनलाइन टैग):** कुछ समय के लिए बिना बोले आवाज़ में होने वाले बदलाव या पॉज़ को सीधे तौर पर ट्रांसक्रिप्ट में ऐंगल ब्रैकेट का इस्तेमाल करके डालें. उदाहरण के लिए, `"Wait... <short pause> did you hear that? <sigh>"` या `"Excuse me <cough> as I was saying..."`.

सबसे सही तरीकों के बारे में पूरी जानकारी के लिए, [प्रॉम्प्ट के लिए गाइड](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#prompting-guide) देखें.

### ऐप पर जाएं

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    transcriptRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                "Generate a short transcript around 100 words that reads " +
                    "like it was clipped from a podcast by excited herpetologists. " +
                    "The hosts names are Dr. Anya and Liam.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var transcript string
    if transcriptRes.Interaction.OutputText != nil {
        transcript = *transcriptRes.Interaction.OutputText
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Dr. Anya"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Liam"), Voice: genai.Ptr("Puck")},
        })),
    }

    ttsRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput(transcript),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = ttsRes
}
```

## बोलकर जवाब देने की सुविधा

`stream: true` को सेट करके, जनरेट किए जा रहे ऑडियो को स्ट्रीम किया जा सकता है. यूनरी अनुरोधों के उलट, **स्ट्रीमिंग अनुरोधों में डिफ़ॉल्ट रूप से हेडरलेस रॉ 16-बिट साइंड लिटिल-एंडियन लीनियर पीसीएम (`audio/l16`, 24 kHz, मोनो) चंक मिलते हैं**. यूनरी अनुरोधों में, RIFF हेडर के साथ पूरी WAV फ़ाइल मिलती है. इसलिए, ऑडियो चंक को कंटेनर हेडर के बिना लगातार चलाया या जोड़ा जा सकता है.

### Python

```
import base64
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
      stream: true,
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## ऑडियो आउटपुट के फ़ॉर्मैट

Gemini 3.8 के टीटीएस मॉडल, अलग-अलग डिफ़ॉल्ट ऑडियो फ़ॉर्मैट का इस्तेमाल करते हैं. यह इस बात पर निर्भर करता है कि अनुरोध यूनरी है या स्ट्रीमिंग:

- **यूनरी अनुरोध (`stream=False`):** स्टैंडर्ड RIFF हेडर (24 किलोहर्ट्ज़, मोनो, 16-बिट साइंड लिटिल-एंडियन पीसीएम) के साथ पूरा **WAV (`audio/wav`)** ऑडियो वापस पाएं. डिकोड किए गए ऑडियो बाइट को सीधे `.wav` फ़ाइल में सेव किया जा सकता है. इसके लिए, WAV हेडर को मैन्युअल तरीके से जोड़ने की ज़रूरत नहीं होती.
- **स्ट्रीमिंग के अनुरोध (`stream=True`):** डिफ़ॉल्ट रूप से, **हेडरलेस रॉ लीनियर पीसीएम (`audio/l16`)** के चंक (24 किलोहर्ट्ज़, मोनो, 16-बिट साइंड लिटिल-एंडियन पीसीएम) दिखाएं, ताकि हर चंक पर कंटेनर हेडर के बिना चंक को लगातार स्ट्रीम या जोड़ा जा सके.

ऑडियो को कोड में बदलने या सैंपलिंग रेट के लिए कोई दूसरा अनुरोध करने के लिए, `response_format` में `mime_type` और `sample_rate` को कॉन्फ़िगर करें.
को कॉन्फ़िगर करना ज़रूरी नहीं है:

| फ़ॉर्मैट | `mime_type` की कीमत का | ब्यौरा |
| --- | --- | --- |
| **WAV** *(unary default)* | `"audio/wav"` | बिना कंप्रेस की गई WAV फ़ाइल, जिसमें RIFF हेडर हो (16-बिट साइंड लिटिल-एंडियन पीसीएम, मोनो, 24 किलोहर्ट्ज़ डिफ़ॉल्ट). यह यूनेरी अनुरोधों के लिए डिफ़ॉल्ट वैल्यू है. |
| **Raw PCM (L16)** *(स्ट्रीमिंग के लिए डिफ़ॉल्ट)* | `"audio/l16"` | बिना कंप्रेस किया गया, हेडर रहित 16-बिट साइंड लिटिल-एंडियन लीनियर पीसीएम ऑडियो (24 kHz, मोनो). स्ट्रीमिंग के अनुरोधों के लिए डिफ़ॉल्ट. |
| **Mu-law** | `"audio/mulaw"` | 8-बिट G.711 mu-law एन्कोड किया गया ऑडियो. इसका इस्तेमाल आम तौर पर, उत्तरी अमेरिका और जापान के टेलीफ़ोनी/आईवीआर सिस्टम में किया जाता है. |
| **A-law** | `"audio/alaw"` | 8-बिट G.711 A-लॉ एन्कोड किया गया ऑडियो. इसका इस्तेमाल आम तौर पर, यूरोप और अंतरराष्ट्रीय टेलीफ़ोनी सिस्टम में किया जाता है. |

हर्ट्ज़ में `sample_rate` भी तय किया जा सकता है. उदाहरण के लिए, `24000`, `16000` या `8000`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={
        "type": "audio",
        "mime_type": "audio/l16",  # "audio/wav" (default), "audio/l16", "audio/mulaw", or "audio/alaw"
        "sample_rate": 24000,
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.pcm", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: {
         type: 'audio',
         mime_type: 'audio/l16', // 'audio/wav' (default), 'audio/l16', 'audio/mulaw', or 'audio/alaw'
         sample_rate: 24000,
      },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### ऐप पर जाएं

```
package main

import (
    "context"
    "encoding/base64"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
            Stream:           genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if audioDelta := stepDelta.GetDeltaAudio(); audioDelta != nil && audioDelta.Data != nil {
                audioData, err := base64.StdEncoding.DecodeString(*audioDelta.Data)
                if err != nil {
                    log.Fatal(err)
                }
                // Process the audio chunk (e.g. play it or write to a file)
                _ = audioData
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio",
      "mime_type": "audio/l16",
      "sample_rate": 24000
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## बोलकर लिखवाने के विकल्प

Gemini 3.8 में टीटीएस की सुविधा, चार तरीकों से आवाज़ें चुनने या बनाने की सुविधा देती है:

1. **स्टूडियो की पहले से तैयार की गई आवाज़ें:** यहां दी गई टेबल में 30 आवाज़ें दी गई हैं.
2. **एक्सटेंडेड वॉइस लाइब्रेरी:** इसमें अलग-अलग भाषाओं, लहज़ों, और किरदारों के हिसाब से सैकड़ों अतिरिक्त आवाज़ें उपलब्ध हैं. इन्हें `client.voices.list()` (`GET /v1beta/voices`) का इस्तेमाल करके ऐक्सेस किया जा सकता है.
3. **[आवाज़ का डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi):** [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में, सामान्य भाषा में दिए गए ब्यौरे से, अपनी पसंद के मुताबिक आवाज़ जनरेट करें. इसके अलावा, `POST /v1beta/voices` (`type="prompted"`, जो `voice_...` आईडी और  WAV प्रीव्यू को  और `GetVoice` में दिखाता है) का इस्तेमाल करके भी ऐसा किया जा सकता है.`sample_audio``CreateVoice`
4. **[आवाज़ की नकल करना](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi):** [Google AI Studio](https://aistudio.google.com/generate-speech?hl=hi) में, रेफ़रंस और सहमति वाले ऑडियो का इस्तेमाल करके किसी स्पीकर की आवाज़ की नकल करें. इसके अलावा, `POST /v1beta/voices` (`type="replicated"`, डिफ़ॉल्ट रूप से लगातार `store=True` या बिना स्थिति के वैकल्पिक `store=False`) का इस्तेमाल करके भी ऐसा किया जा सकता है.

### कस्टम वॉइस की सीमाएं और टीटीएल

| बोलकर लिखवाएँ | स्टोरेज मोड | कोटा / सीमा | डेटा का रखरखाव (टीटीएल) |
| --- | --- | --- | --- |
| **स्टेटफ़ुल आवाज़ें** (`voice_...`, प्रॉम्प्ट की गई या कॉपी की गई) | `store=True` | **हर प्रोजेक्ट के लिए 200 आवाज़ें** (इन्हें प्रॉम्प्ट की गई और रेप्लिका की गई आवाज़ों के साथ शेयर किया जाता है) | **आखिरी बार इस्तेमाल करने के एक साल बाद\*** |
| **स्टेटलेस वॉइस की** (`voicekey_...`, रेप्लिका) | `store=False` | क्लाइंट के ज़रिए मैनेज किया गया | **सात दिन** |

\* **टीटीएल का बढ़ना:** आवाज़ का इस्तेमाल करने पर, डेटा को सेव रखने की एक साल की अवधि रीसेट हो जाती है. आवाज़ का इस्तेमाल, स्पीच को सिंथेसाइज़ करने या रीमिक्स करने के लिए किया जा सकता है. जिन आवाज़ों का इस्तेमाल एक साल तक नहीं किया जाता उन्हें अपने-आप मिटा दिया जाता है.

### पहले से मौजूद आवाज़ें

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | **Charon** -- *Informative* |
| **Kore** -- *Firm* | **Fenrir** -- *Excitable* | **Leda** -- *Youthful* |
| **Orus** -- *कंपनी* | **Aoede** -- *Breezy* | **Callirrhoe** -- *ईज़ी-गोइंग* |
| **ऑटोनो** -- *ब्राइट* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *आसानी से काम करने वाला* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| **Erinome** -- *Clear* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *Informative* |
| **Laomedeia** -- *अपबीट* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
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
| `type` (`type_` in Python) | `list[str]` | आवाज़ के सोर्स के हिसाब से फ़िल्टर करें: `"prebuilt"`, `"prompted"` ([आवाज़ का डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi)) या `"replicated"` ([आवाज़ की नकल](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi)). |
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
| Belarusian | ✔️ | ✔️ |
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
| Hindi | ✔️ | ✔️ |
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
| Polish | ✔️ | ✔️ |
| Portuguese | ✔️ | ✔️ |
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
| Turkish | ✔️ | ✔️ |
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

अगर आपको `gemini-3.1-flash-tts-preview` या उससे पहले के Gemini TTS मॉडल से Gemini 3.8 TTS पर माइग्रेट करना है, तो:

1. **मोड़ के हिसाब से दिए गए निर्देशों को `speech_metadata` में ले जाएं:** Gemini 3.8 टीटीएस, इनपुट टेक्स्ट को हूबहू ट्रांसक्रिप्ट के तौर पर लेता है. स्टेज के निर्देशों को ट्रांसक्रिप्ट के टेक्स्ट में एम्बेड करने के बजाय, लगातार डिलीवरी के निर्देशों (`style`—जैसे कि `"whispering"`, `"out of breath"` या `"speaking slowly"`) और स्पीकर लेबल (`speaker`) को स्ट्रक्चर्ड `speech_metadata` एनोटेशन में ले जाएं.
2. **सिर्फ़ कुछ समय के लिए होने वाली आवाज़ों के लिए, ऐंगल-ब्रैकेट वाले इनलाइन टैग इस्तेमाल करें:** ट्रांसक्रिप्ट में, कुछ समय के लिए होने वाली आवाज़ों और रुकने के समय को इनलाइन रखने के लिए, ऐंगल ब्रैकेट (जैसे कि `<laugh>`, `<sigh>`, `<cough>`, `<breath>` या `<short pause>`) का इस्तेमाल करें. साउंड इफ़ेक्ट वाले टैग (जैसे कि तालियां या धमक) का इस्तेमाल न करें और डिलीवरी स्टाइल को `speech_metadata.style` में रखें.
3. **एक से ज़्यादा स्पीकर वाले अनुरोधों में, हर बार `speaker` तय करें:** एक से ज़्यादा स्पीकर वाले अनुरोध में, हर बार
   `speech_metadata` के अंदर `speaker` को साफ़ तौर पर शामिल किया जाना चाहिए. यह, कॉन्फ़िगर किए गए किसी स्पीकर से मेल खाना चाहिए.
4. **वॉइस डिज़ाइन की मदद से, पहले से ही पर्सोना डिज़ाइन करना:** मल्टी-पैराग्राफ़ `"Audio Profile"` या `"Director's Notes"` ब्लॉक को [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) में बनाई गई कस्टम आवाज़ से बदलें. इसके बाद, उस `voice_...` आईडी को अपने टीटीएस अनुरोधों में कम से कम या खाली `style` स्ट्रिंग के साथ ले जाएं.
5. **एकल अनुरोधों पर डिफ़ॉल्ट WAV (`audio/wav`) आउटपुट के लिए खाता:** `gemini-3.1-flash-tts-preview` और टीटीएस के पुराने मॉडल (जो डिफ़ॉल्ट रूप से हेडरलेस रॉ पीसीएम `audio/l16` दिखाते थे) के उलट, Gemini 3.8 टीटीएस, एकल अनुरोधों के लिए डिफ़ॉल्ट रूप से स्टैंडर्ड RIFF हेडर के साथ WAV ऑडियो (`audio/wav`) दिखाता है.
   - अगर आपके कोड में पहले रॉ पीसीएम बाइट को WAV हेडर में रैप किया गया था (उदाहरण के लिए, Python के `wave` मॉड्यूल या `ffmpeg` का इस्तेमाल करके), तो मैन्युअल हेडर रैपर को हटा दें. साथ ही, लौटाए गए बाइट को सीधे `.wav` फ़ाइल में लिखें.
   - अगर आपकी पाइपलाइन को हेडरलेस रॉ पीसीएम, म्यू-लॉ या ए-लॉ ऑडियो की ज़रूरत है, तो `response_format.mime_type` को `"audio/l16"`, `"audio/mulaw"` या `"audio/alaw"` पर सेट करें. उदाहरण के लिए, Interactions API में `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` या `generateContent` में `AUDIO_L16`. [ऑडियो आउटपुट फ़ॉर्मैट](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#audio-output-formats) देखें.

## प्रॉम्प्ट से जुड़ी गाइड

Gemini 3.8 के टीटीएस मॉडल, इनपुट टेक्स्ट को सिर्फ़ **शब्दशः ट्रांसक्रिप्ट** के तौर पर लेते हैं.
पहले के प्रीव्यू मॉडल में, स्टेज के बारे में निर्देश सादे टेक्स्ट में एम्बेड किए जाते थे. हालांकि, Gemini 3.8 टीटीएस में, लगातार टर्न-लेवल के निर्देशों (`speech_metadata`) को, पॉइंट-इन-टाइम इनलाइन वोकल टैग से अलग किया जाता है.

### स्टाइल फ़ील्ड बनाम इनलाइन टैग

परफ़ॉर्मेंस के निर्देशों को स्कोप के हिसाब से बांटें:

- **टर्न-लेवल डिलीवरी (`speech_metadata.style`):** डिलीवरी की लगातार बनी रहने वाली एट्रिब्यूट वैल्यू—जैसे कि भावना, उतार-चढ़ाव, बोलने की कुल गति या डिलीवरी स्टाइल (जैसे कि `"whispering"`, `"out of breath"`, `"muttering"` या `"sarcastic"`)—को `speech_metadata` के `style` फ़ील्ड में डालें. हर बार एक जैसा किरदार और परफ़ॉर्मेंस पाने के लिए, [आवाज़ का डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) सेक्शन में जाकर, पहले से ही पर्सोना डिज़ाइन करें. साथ ही, `style` का इस्तेमाल सिर्फ़ उन बदलावों के लिए करें जो हर बार किए जा सकते हैं.
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

एक से ज़्यादा स्पीकर वाली बातचीत में, सुनने वाले की प्रतिक्रियाओं को पाइप कैरेक्टर (`|reaction|`) में रैप करें. ऐसा स्पीकर के टर्न के दौरान किया जाता है, ताकि नैचुरल बैकचैनल या ओवरलैपिंग स्पीच बनाई जा सके. इससे हर प्रतिक्रिया के लिए अलग टर्न नहीं लेना पड़ता.

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
  [वॉइस डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) में, अपनी क्रिएटिव सोच का इस्तेमाल करके एक स्थायी कस्टम `voice_...` पर्सोना जनरेट करें. इसके बाद, टीटीएस कॉल के दौरान उस वॉइस आईडी का इस्तेमाल करें.
- **आवाज़ को स्थिर रखने के लिए, आवाज़ के रेफ़रंस पर भरोसा करें (मेटा-निर्देश शामिल न करें):**
  Gemini 3.8 के टीटीएस मॉडल को, सबसे पहले ऑडियो रेफ़रंस पर फ़ोकस करने के लिए ट्रेन किया गया है.
  मॉडल को आवाज़ स्थिर रखने के निर्देश शामिल न करें. जैसे, `"do not switch speaker identity"` या `"maintain identical timbre"`. प्रॉम्प्ट में ज़्यादा टेक्स्ट शामिल करने से, आवाज़ में बदलाव होने की संभावना बढ़ जाती है. स्टाइल से जुड़े गैर-ज़रूरी निर्देश हटा दें. साथ ही, मॉडल को आवाज़ के रेफ़रंस के हिसाब से, नैचुरल तरीके से अलग-अलग आवाज़ों में बोलने दें.
- **`style` में स्पीकर की ऐसी विशेषताओं को बदलने की कोशिश न करें जिन्हें बदला नहीं जा सकता:** `speech_metadata.style` में उम्र, लिंग, नाम या स्थायी लहजे में बदलाव न करें.
  इसके बजाय, Extended Voice Library से किसी क्षेत्र के हिसाब से आवाज़ चुनें या [आवाज़ डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) की मदद से कोई आवाज़ बनाएं.

### सुझाया गया वर्कफ़्लो

1. **एक बार में ही किरदार तैयार करें:** [आवाज़ डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) में अपना किरदार बनाएं या एक्सटेंडेड वॉइस लाइब्रेरी से ऐसी क्षेत्रीय आवाज़ चुनें जो आपकी टारगेट की गई भाषा और पर्सोना से मेल खाती हो.
2. **बोलचाल की भाषा में ट्रांसक्रिप्ट लिखें:** `text` को ज़्यादा से ज़्यादा नैचुरल बनाने के लिए, इसे बोलचाल की भाषा में ट्रांसक्रिप्ट के तौर पर लिखें. इसमें बातचीत के दौरान होने वाली रुकावटें और हिचकिचाहट भी शामिल करें. उदाहरण के लिए, `"Oh uh yeah I think... hm, so that's interesting"`.
3. **सबसे पहले, सामान्य टीटीएस को आज़माएं:** सबसे पहले, अपनी ट्रांसक्रिप्ट को खाली `style` फ़ील्ड के साथ सिंथेसाइज़ करें. ज़्यादातर अनुरोधों के लिए, `style` निर्देश की ज़रूरत नहीं होती.
4. **सिर्फ़ बदलावों के लिए छोटे `style` प्रॉम्प्ट जोड़ें:** सिर्फ़ उन टर्न के लिए छोटे `style` स्ट्रिंग (जैसे, `"casual, friendly"` या `"muttering, then reassuring"`) जोड़ें जिनमें डिलीवरी में खास बदलाव करने की ज़रूरत हो. साथ ही, जब आपको एक जैसा बेसलाइन चाहिए, तब सभी टर्न में उसी छोटे स्ट्रिंग का फिर से इस्तेमाल करें.

### सिलसिलेवार बातचीत और वॉइस एजेंट

रीयल-टाइम में बातचीत करने वाले वॉइस एजेंट या सिलसिलेवार बातचीत वाले ऐप्लिकेशन बनाते समय:

- एलएलएम से टेक्स्ट के हिस्से मिलने पर, **हर बार एक टीटीएस कॉल करें**.
- कॉन्फ़िगर किए गए `voice` (पहले से बने, डिज़ाइन किए गए `voice_...` या डुप्लीकेट किए गए `voice_...` / `voicekey_...`) को हर बार स्पीकर की पहचान करने दें. हर बार लंबी अवधि के किरदार की पर्सोना को फिर से न भेजें.
- हर बातचीत के लिए `style` फ़ील्ड को खाली छोड़ दें या पूरी बातचीत के लिए एक छोटी सी स्ट्रिंग (जैसे कि `"casual, friendly"`) भेजें.
- एजेंट के लंबे जवाबों को छोटे-छोटे हिस्सों में बांटें. इसके लिए, स्टाइल से जुड़े ज़्यादा बेहतर प्रॉम्प्ट का इस्तेमाल न करें.

## सीमाएं

- टीटीएस मॉडल, सिर्फ़ टेक्स्ट वाले इनपुट स्वीकार करते हैं और सिर्फ़ ऑडियो वाले आउटपुट जनरेट करते हैं.
- एक ही अनुरोध में कई स्पीकर की आवाज़ जनरेट करने की सुविधा (`speech_config.speakers`) के तहत, पहले से मौजूद आवाज़ों का इस्तेमाल करके ज़्यादा से ज़्यादा दो स्पीकर की आवाज़ जनरेट की जा सकती है. एक से ज़्यादा किरदार वाले डायलॉग में, कस्टम डिज़ाइन की गई (`voice_...`) या कॉपी की गई (`voice_...` / `voicekey_...`) आवाज़ों को एक साथ इस्तेमाल करने के लिए, हर किरदार के डायलॉग को अलग-अलग सिंथेसाइज़ करें.
  यूनरी अनुरोधों में डिफ़ॉल्ट रूप से, 44 बाइट का RIFF हेडर वाला `audio/wav` मिलता है. इसलिए, रॉ पीसीएम (`{"type": "audio", "mime_type": "audio/l16"}`) का अनुरोध करें या 24 किलोहर्ट्ज़ पीसीएम ऑडियो फ़्रेम को जोड़ने से पहले, हर टर्न से WAV हेडर हटाएं.
- **कस्टम वॉइस के स्टोरेज की सीमाएं और टीटीएल:**
  - **स्टेटफ़ुल आवाज़ें (`store=True`, प्रॉम्प्ट की गई या डुप्लीकेट की गई):** **हर प्रोजेक्ट के लिए ज़्यादा से ज़्यादा 200 आवाज़ें**. इनका **टीटीएल (टाइम-टू-लाइव) एक साल** होता है.
  - **स्टेटलेस वॉइस की (`store=False`, `voicekey_...`):** **सात दिनों का टीटीएल**
    (टाइम-टू-लिव).
- भाषा कवरेज के लिए, [उपलब्ध भाषाएं](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi#languages) सेक्शन देखें.

## आगे क्या करना है

- [आवाज़ के डिज़ाइन](https://ai.google.dev/gemini-api/docs/voice-design?hl=hi) की मदद से, नैचुरल लैंग्वेज से अपनी पसंद के मुताबिक़ आवाज़ें बनाएं.
- [वॉइस रेप्लिकेशन](https://ai.google.dev/gemini-api/docs/voice-replication?hl=hi) की मदद से, किसी मौजूदा स्पीकर की आवाज़ को रेप्लिकेट करना.
- [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=hi) और [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=hi) मॉडल के पेजों पर जाकर, मॉडल की खास बातों की तुलना करें.
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) की मदद से, दोनों भाषाओं में इंटरैक्टिव ऑडियो की सुविधा का इस्तेमाल करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-02 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-02 (UTC) को अपडेट किया गया."],[],[]]
