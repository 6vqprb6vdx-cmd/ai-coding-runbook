---
source_url: https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=hi
fetched_at: 2026-05-25T12:59:10.648299+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# वीडियो को समझना

> वीडियो जनरेट करने के बारे में जानने के लिए, [Veo](https://ai.google.dev/gemini-api/docs/video?hl=hi) गाइड देखें.

Gemini मॉडल, वीडियो प्रोसेस कर सकते हैं. इससे डेवलपर को इस्तेमाल के कई ऐसे उदाहरण मिलते हैं जिनके लिए पहले, डोमेन के हिसाब से मॉडल की ज़रूरत होती थी.
Gemini की विज़न से जुड़ी कुछ क्षमताओं में ये शामिल हैं: वीडियो से जानकारी निकालना, वीडियो के अलग-अलग हिस्सों के बारे में बताना, वीडियो के कॉन्टेंट से जुड़े सवालों के जवाब देना, और वीडियो में किसी खास टाइमस्टैंप का रेफ़रंस देना.

Gemini को इन तरीकों से वीडियो इनपुट के तौर पर दिए जा सकते हैं:

| इनपुट विधि | ज़्यादा से ज़्यादा साइज़ | इस्तेमाल का सुझाया गया उदाहरण |
| --- | --- | --- |
| [File API](#upload-video) | 20 जीबी (पैसे चुकाकर लिया गया) / 2 जीबी (बिना शुल्क वाला) | बड़ी फ़ाइलें (100 एमबी से ज़्यादा), लंबी अवधि के वीडियो (10 मिनट से ज़्यादा), और फिर से इस्तेमाल की जा सकने वाली फ़ाइलें. |
| [Cloud Storage रजिस्ट्रेशन](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi#registration) | 2 जीबी (हर फ़ाइल के लिए, स्टोरेज की कोई सीमा नहीं) | बड़ी फ़ाइलें (100 एमबी से ज़्यादा), लंबी अवधि के वीडियो (10 मिनट से ज़्यादा), लगातार इस्तेमाल की जा सकने वाली फ़ाइलें. |
| [इनलाइन डेटा](#inline-video) | < 100 एमबी | छोटी फ़ाइलें (<100 एमबी), कम अवधि (<1 मिनट), एक बार में इनपुट. |
| [YouTube के यूआरएल](#youtube) | लागू नहीं | सार्वजनिक तौर पर उपलब्ध YouTube वीडियो. |

> **ध्यान दें:** ज़्यादातर मामलों में, [File API](#upload-video) का इस्तेमाल करने का सुझाव दिया जाता है. खास तौर पर, 100 एमबी से ज़्यादा साइज़ वाली फ़ाइलों के लिए या जब आपको एक ही फ़ाइल का इस्तेमाल कई अनुरोधों में करना हो.

फ़ाइल इनपुट करने के अन्य तरीकों के बारे में जानने के लिए, [फ़ाइल इनपुट करने के तरीके](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=hi) गाइड देखें. जैसे, बाहरी यूआरएल या Google Cloud में सेव की गई फ़ाइलों का इस्तेमाल करना.

### वीडियो फ़ाइल अपलोड करना

नीचे दिए गए कोड में, एक सैंपल वीडियो डाउनलोड किया जाता है. इसके बाद, उसे [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=hi) का इस्तेमाल करके अपलोड किया जाता है. इसके बाद, वीडियो के प्रोसेस होने का इंतज़ार किया जाता है. इसके बाद, अपलोड की गई फ़ाइल के रेफ़रंस का इस्तेमाल करके वीडियो की खास जानकारी तैयार की जाती है.

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  // Wait for the file to be processed.
  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

जब अनुरोध का कुल साइज़ (इसमें फ़ाइल, टेक्स्ट प्रॉम्प्ट, सिस्टम के निर्देश वगैरह शामिल हैं) 20 एमबी से ज़्यादा हो, वीडियो की अवधि ज़्यादा हो या आपको एक ही वीडियो का इस्तेमाल कई प्रॉम्प्ट में करना हो, तो हमेशा Files API का इस्तेमाल करें.
File API, वीडियो फ़ाइल फ़ॉर्मैट को सीधे तौर पर स्वीकार करता है.

मीडिया फ़ाइलों के साथ काम करने के बारे में ज़्यादा जानने के लिए, [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=hi) देखें.

### वीडियो डेटा को इनलाइन पास करना

File API का इस्तेमाल करके वीडियो फ़ाइल अपलोड करने के बजाय, अनुरोध में सीधे तौर पर छोटे वीडियो पास किए जा सकते हैं. यह 20 एमबी से कम साइज़ वाले छोटे वीडियो के लिए सही है.

यहां इनलाइन वीडियो का डेटा देने का उदाहरण दिया गया है:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### YouTube वीडियो के यूआरएल पास करना

अपने अनुरोध के हिस्से के तौर पर, YouTube यूआरएल को सीधे Gemini API पर भेजा जा सकता है. इसके लिए, यह तरीका अपनाएं:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**सीमाएं:**

- मुफ़्त टियर के लिए, हर दिन आठ घंटे से ज़्यादा का YouTube वीडियो अपलोड नहीं किया जा सकता.
- पैसे चुकाकर ली जाने वाली सदस्यता के लिए, वीडियो की अवधि के हिसाब से कोई सीमा तय नहीं की गई है.
- Gemini 2.5 से पहले के मॉडल के लिए, हर अनुरोध में सिर्फ़ एक वीडियो अपलोड किया जा सकता है. Gemini 2.5 और इसके बाद के मॉडल के लिए, हर अनुरोध में ज़्यादा से ज़्यादा 10 वीडियो अपलोड किए जा सकते हैं.
- सिर्फ़ सार्वजनिक वीडियो अपलोड किए जा सकते हैं. निजी या 'सबके लिए मौजूद नहीं' के तौर पर उपलब्ध वीडियो अपलोड नहीं किए जा सकते.

## कॉन्टेंट में मौजूद टाइमस्टैंप देखें

वीडियो में किसी खास समय के बारे में सवाल पूछने के लिए, `MM:SS` फ़ॉर्मैट वाले टाइमस्टैंप का इस्तेमाल किया जा सकता है.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## वीडियो से अहम जानकारी निकालना

Gemini मॉडल, वीडियो कॉन्टेंट को समझने के लिए कई सुविधाएं देते हैं. इसके लिए, वे **ऑडियो और विज़ुअल**, दोनों स्ट्रीम से मिली जानकारी को प्रोसेस करते हैं. इसकी मदद से, आपको वीडियो के बारे में ज़्यादा जानकारी मिलती है. जैसे, वीडियो में क्या हो रहा है, इसके बारे में ब्यौरा जनरेट करना और वीडियो के कॉन्टेंट के बारे में सवालों के जवाब देना.

विज़ुअल के बारे में जानकारी देने के लिए, मॉडल वीडियो को **एक फ़्रेम प्रति सेकंड** (एफ़पीएस) की दर से सैंपल करता है. डिफ़ॉल्ट सैंपलिंग रेट, ज़्यादातर कॉन्टेंट के लिए सही होता है. हालांकि, ध्यान दें कि तेज़ी से चलने वाले वीडियो या सीन में तेज़ी से बदलाव होने वाले वीडियो में, यह कुछ जानकारी को छोड़ सकता है.
तेज़ी से चलने वाले ऐसे कॉन्टेंट के लिए, [कस्टम फ़्रेम रेट सेट करें](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## काम करने वाले वीडियो फ़ॉर्मैट

Gemini, इन वीडियो फ़ॉर्मैट के MIME टाइप के साथ काम करता है:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## वीडियो के बारे में तकनीकी जानकारी

- **इस्तेमाल किए जा सकने वाले मॉडल और कॉन्टेक्स्ट**: Gemini के सभी मॉडल, वीडियो डेटा को प्रोसेस कर सकते हैं.
  - 10 लाख कॉन्टेक्स्ट विंडो वाले मॉडल, डिफ़ॉल्ट मीडिया रिज़ॉल्यूशन पर एक घंटे तक के वीडियो प्रोसेस कर सकते हैं. वहीं, कम मीडिया रिज़ॉल्यूशन पर तीन घंटे तक के वीडियो प्रोसेस किए जा सकते हैं.
- **File API प्रोसेसिंग**: File API का इस्तेमाल करते समय, वीडियो को एक फ़्रेम प्रति सेकंड (एफ़पीएस) पर सेव किया जाता है. साथ ही, ऑडियो को 1Kbps (सिंगल चैनल) पर प्रोसेस किया जाता है.
  हर सेकंड टाइमस्टैंप जोड़े जाते हैं.
  - इन दरों में आने वाले समय में बदलाव हो सकता है, ताकि अनुमान लगाने की प्रोसेस को बेहतर बनाया जा सके.
- **टोकन की गिनती**: वीडियो के हर सेकंड को इस तरह टोकन में बदला जाता है:
  - अलग-अलग फ़्रेम (1 एफ़पीएस पर सैंपल किए गए):
    - अगर `media_resolution` को कम पर सेट किया जाता है, तो हर फ़्रेम को 66 टोकन में बदला जाता है.
    - अगर ऐसा नहीं है, तो हर फ़्रेम को 258 टोकन के हिसाब से टोकन में बदला जाता है.
  - ऑडियो: हर सेकंड 32 टोकन.
  - इसमें मेटाडेटा भी शामिल होता है.
  - कुल: डिफ़ॉल्ट मीडिया रिज़ॉल्यूशन पर, वीडियो के हर सेकंड के लिए करीब 300 टोकन या कम मीडिया रिज़ॉल्यूशन पर, वीडियो के हर सेकंड के लिए 100 टोकन.
- **मीडिया की क्वालिटी**: Gemini 3 में, `media_resolution` पैरामीटर की मदद से मल्टीमॉडल विज़न प्रोसेसिंग को ज़्यादा बारीकी से कंट्रोल करने की सुविधा मिलती है. `media_resolution` पैरामीटर से यह तय होता है कि **हर इनपुट इमेज या वीडियो फ़्रेम के लिए ज़्यादा से ज़्यादा कितने टोकन असाइन किए जाएं.**
  ज़्यादा रिज़ॉल्यूशन से, मॉडल को छोटे टेक्स्ट को पढ़ने या छोटी-छोटी बारीकियों को पहचानने में मदद मिलती है. हालांकि, इससे टोकन का इस्तेमाल और लेटेन्सी बढ़ जाती है.

  कैलकुलेशन के बारे में जानने के लिए, [टोकन](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=hi) गाइड देखें.
- **टाइमस्टैंप का फ़ॉर्मैट**: अगर आपको वीडियो के किसी खास हिस्से के बारे में बताना है, तो अपने प्रॉम्प्ट में `MM:SS` फ़ॉर्मैट का इस्तेमाल करें. उदाहरण के लिए, 1 मिनट और 15 सेकंड के लिए `01:15` का इस्तेमाल करें.
- **सबसे सही तरीके**:

  - बेहतर नतीजों के लिए, हर प्रॉम्प्ट के अनुरोध में सिर्फ़ एक वीडियो का इस्तेमाल करें.
  - अगर टेक्स्ट और एक वीडियो को साथ में इस्तेमाल किया जा रहा है, तो `input` ऐरे में वीडियो वाले हिस्से के *बाद* टेक्स्ट प्रॉम्प्ट डालें.
  - ध्यान दें कि 1 एफ़पीएस की सैंपलिंग दर की वजह से, तेज़ कार्रवाई वाले सीक्वेंस में जानकारी कम हो सकती है. अगर ज़रूरी हो, तो ऐसी क्लिप की स्पीड कम करें.

## आगे क्या करना है

इस गाइड में, वीडियो फ़ाइलें अपलोड करने और वीडियो इनपुट से टेक्स्ट आउटपुट जनरेट करने का तरीका बताया गया है. ज़्यादा जानने के लिए, यहां दिए गए संसाधन देखें:

- [सिस्टम के लिए निर्देश](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=hi#system-instructions):
  सिस्टम के लिए निर्देश देने की सुविधा की मदद से, अपनी खास ज़रूरतों और इस्तेमाल के उदाहरणों के आधार पर, मॉडल के व्यवहार को कंट्रोल किया जा सकता है.
- [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=hi): Gemini के साथ इस्तेमाल करने के लिए, फ़ाइलें अपलोड करने और मैनेज करने के बारे में ज़्यादा जानें.
- [फ़ाइल प्रॉम्प्ट करने की रणनीतियां](https://ai.google.dev/gemini-api/docs/interactions/files?hl=hi#prompt-guide): Gemini API में टेक्स्ट, इमेज, ऑडियो, और वीडियो डेटा के साथ प्रॉम्प्ट करने की सुविधा उपलब्ध है. इसे मल्टीमॉडल प्रॉम्प्टिंग भी कहा जाता है.
- [सुरक्षा से जुड़ी गाइडलाइन](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=hi): कभी-कभी जनरेटिव एआई मॉडल ऐसे आउटपुट जनरेट करते हैं जिनकी उम्मीद नहीं होती. जैसे, गलत, पक्षपात करने वाले या आपत्तिजनक आउटपुट. इस तरह के आउटपुट से होने वाले नुकसान के जोखिम को कम करने के लिए, पोस्ट-प्रोसेसिंग और मैन्युअल तरीके से आकलन करना ज़रूरी है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-09 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-09 (UTC) को अपडेट किया गया."],[],[]]
