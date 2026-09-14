---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=hi
fetched_at: 2026-09-14T05:50:21.171256+00:00
title: "\u0935\u0940\u0921\u093f\u092f\u094b \u0915\u0940 \u092c\u093e\u0930\u0940\u0915\u093c\u0940 \u0938\u0947 \u092a\u0939\u091a\u093e\u0928 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# वीडियो की बारीक़ी से पहचान करना

> वीडियो जनरेट करने के बारे में जानने के लिए, [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=hi) गाइड देखें.

Gemini मॉडल, वीडियो प्रोसेस कर सकते हैं. इससे डेवलपर को कई ऐसे मामलों में मदद मिलती है जिनमें पहले, डोमेन के हिसाब से मॉडल की ज़रूरत होती थी.
Gemini की विज़न क्षमताओं में ये शामिल हैं: वीडियो के बारे में जानकारी देना, वीडियो को सेगमेंट में बांटना, वीडियो से जानकारी निकालना, वीडियो के कॉन्टेंट के बारे में सवालों के जवाब देना, और वीडियो में किसी खास टाइमस्टैंप का रेफ़रंस देना.

Gemini को वीडियो इनपुट के तौर पर देने के लिए, इन तरीकों का इस्तेमाल किया जा सकता है:

| इनपुट विधि | ज़्यादा से ज़्यादा साइज़ | इस्तेमाल का सुझाया गया उदाहरण |
| --- | --- | --- |
| [File API](#upload-video) | 20 जीबी (पैसे चुकाकर लिया गया) / 2 जीबी (बिना शुल्क वाला) | बड़ी फ़ाइलें (100 एमबी से ज़्यादा), लंबी अवधि के वीडियो (10 मिनट से ज़्यादा), और फिर से इस्तेमाल की जा सकने वाली फ़ाइलें. |
| [Cloud Storage रजिस्ट्रेशन](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi#registration) | 2 जीबी (हर फ़ाइल के लिए, स्टोरेज की कोई सीमा नहीं) | बड़ी फ़ाइलें (100 एमबी से ज़्यादा), लंबी अवधि के वीडियो (10 मिनट से ज़्यादा), लगातार इस्तेमाल की जा सकने वाली फ़ाइलें. |
| [इनलाइन डेटा](#inline-video) | < 100 एमबी | छोटी फ़ाइलें (<100 एमबी), कम अवधि (<1 मिनट), एक बार में इनपुट. |
| [YouTube के यूआरएल](#youtube) | लागू नहीं | सार्वजनिक YouTube वीडियो. |

> **ध्यान दें:** ज़्यादातर मामलों में, [File API](#upload-video) का इस्तेमाल करने का सुझाव दिया जाता है. खास तौर पर, 100 एमबी से ज़्यादा साइज़ वाली फ़ाइलों के लिए या जब आपको एक ही फ़ाइल का इस्तेमाल कई अनुरोधों में करना हो.

फ़ाइल इनपुट करने के अन्य तरीकों के बारे में जानने के लिए, [फ़ाइल इनपुट करने के तरीके](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi) गाइड देखें. जैसे, बाहरी यूआरएल या Google Cloud में सेव की गई फ़ाइलों का इस्तेमाल करना.

### वीडियो फ़ाइल अपलोड करना

नीचे दिए गए कोड में, एक सैंपल वीडियो डाउनलोड किया जाता है. इसके बाद, उसे [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) का इस्तेमाल करके अपलोड किया जाता है. इसके बाद, वीडियो के प्रोसेस होने का इंतज़ार किया जाता है. इसके बाद, अपलोड की गई फ़ाइल के रेफ़रंस का इस्तेमाल करके वीडियो की खास जानकारी तैयार की जाती है.

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
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
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

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
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

टोकन की परफ़ॉर्मेंस और इस्तेमाल को ऑप्टिमाइज़ करने के लिए, [एजेंटिक वीडियो प्रोसेसिंग](#agentic-video-understanding) का इस्तेमाल करें.

जब अनुरोध का कुल साइज़ (इसमें फ़ाइल, टेक्स्ट प्रॉम्प्ट, सिस्टम के निर्देश वगैरह शामिल हैं) 20 एमबी से ज़्यादा हो, वीडियो की अवधि ज़्यादा हो या आपको एक ही वीडियो का इस्तेमाल कई प्रॉम्प्ट में करना हो, तो हमेशा Files API का इस्तेमाल करें.
File API, वीडियो फ़ाइल फ़ॉर्मैट को सीधे तौर पर स्वीकार करता है.

मीडिया फ़ाइलों के साथ काम करने के बारे में ज़्यादा जानने के लिए, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) देखें.

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
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
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
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
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

YouTube के यूआरएल को सीधे Gemini API पर पास किया जा सकता है. इसके लिए, आपको अपने अनुरोध में इन यूआरएल को इस तरह शामिल करना होगा:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
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

## एजेंट की मदद से वीडियो को समझना

डिफ़ॉल्ट रूप से, वीडियो इनपुट के लिए स्टैटिक प्रोसेसिंग का इस्तेमाल किया जाता है. इसमें 1 एफ़पीएस पर फ़्रेम निकाले जाते हैं.
Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, और 3.5 Flash Lite मॉडल भी **एजेंटिक वीडियो अंडरस्टैंडिंग** की सुविधा के साथ काम करते हैं. इसमें मॉडल, वीडियो की टाइमलाइन को डाइनैमिक तरीके से एक्सप्लोर करता है. साथ ही, ट्रांसक्रिप्ट की चुनिंदा तौर पर जांच करता है. इसके अलावा, प्रॉम्प्ट के आधार पर फ़्रेम रेट और रिज़ॉल्यूशन को तुरंत अडजस्ट करता है.

| **मोड** | **ब्यौरा** | **इन मॉडल के साथ काम करता है** |
| --- | --- | --- |
| **स्टैटिक** (डिफ़ॉल्ट) | यह फ़्रेम को एक तय दर (1 FPS) पर निकालता है और उन्हें एक ही पास में कॉन्टेक्स्ट में रखता है. यह छोटी क्लिप के लिए बेहतर तरीके से काम करता है. | Gemini के सभी मॉडल |
| **एजेंटिक** | यह मॉडल, वीडियो की टाइमलाइन पर डाइनैमिक तरीके से नेविगेट करता है. साथ ही, सिर्फ़ उस कॉन्टेंट को लोड करता है जिसकी उसे प्रॉम्प्ट के आधार पर ज़रूरत होती है. यह लंबी अवधि वाले वीडियो के लिए, 88% तक ज़्यादा टोकन-इफ़िशिएंट है और इसकी क्वालिटी ~7% बेहतर है. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite |

### प्रोसेसिंग का कोई मोड चुनना

सामान्य दिशा-निर्देश के तौर पर, **एजेंटिक** मोड से शुरुआत करें. खास तौर पर, जवाब की क्वालिटी या टोकन की क्षमता को ऑप्टिमाइज़ करते समय ऐसा करें.

- **एजेंटिक:** लंबी अवधि के वीडियो या किसी खास पल को टारगेट करने वाली क्वेरी. यह मॉडल, टाइमलाइन में डाइनैमिक तरीके से नेविगेट करता है, ताकि कॉन्टेक्स्ट के हिसाब से काम की जानकारी को टारगेट किया जा सके. इसके लिए, कॉन्टेक्स्ट विंडो को भरने की ज़रूरत नहीं होती.
- **स्टैटिक:** कम समय की क्लिप (पांच मिनट से कम) पर इंतज़ार के समय के हिसाब से संवेदनशील क्वेरी या ऐसे मामले जहां पूरी क्लिप में फ़्रेम-लेवल की सटीक जानकारी की ज़रूरत होती है.

> **ध्यान दें:** लंबी अवधि के वीडियो या मुश्किल प्रॉम्प्ट के लिए, स्ट्रीमिंग (`stream=True`) या बैकग्राउंड में प्रोसेस करने (`background=True`) की सुविधा का इस्तेमाल करें. इससे कनेक्शन ऐक्टिव रहता है, बीच-बीच में तर्क देने के चरण दिखते हैं, और कनेक्शन या पुष्टि करने के लिए तय समय खत्म नहीं होता.

### प्रोसेसिंग मोड सेट करना

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ]
  }' 2> /dev/null
```

> **ध्यान दें:** यह पुष्टि करने के लिए कि एजेंट की मदद से प्रोसेसिंग की गई है, `interaction.steps` की जांच करें. `processing_call` और `processing_result` की मौजूदगी से पता चलता है कि मॉडल ने वीडियो को डाइनैमिक तरीके से नेविगेट किया है.

### जवाब देने के चरण

एजेंटिक प्रोसेसिंग, `steps` ऐरे में दो नए तरह के चरण जोड़ती है:

- `processing_call`: मॉडल ने वीडियो सेगमेंट या ऑडियो ट्रांसक्रिप्ट का अनुरोध किया है. इसकी पहचान `id` से होती है.
- `processing_result`: लोड करने का नतीजा, जिसे `call_id` ने लिंक किया है.

ये `thought` चरणों के बीच में दिखते हैं. ऐसा तब होता है, जब खास जानकारी देने की सुविधा चालू होती है. साथ ही, ये आखिरी `model_output` चरण से पहले दिखते हैं. इनका इस्तेमाल, आपके यूज़र इंटरफ़ेस (यूआई) में प्रोग्रेस ट्रेस दिखाने के लिए किया जा सकता है. हालांकि, इनके लिए जवाब की ज़रूरत नहीं होती.

यहां दिए गए उदाहरण में, इंटरलीव किए गए प्रोसेसिंग चरणों के साथ जवाब का पेलोड दिखाया गया है:

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### अलग-अलग वीडियो के लिए, प्रोसेसिंग के अलग-अलग मोड का इस्तेमाल करना

एक ही अनुरोध में, हर वीडियो के लिए अलग-अलग प्रोसेसिंग मोड सेट किए जा सकते हैं:

### Python

```
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
  }' 2> /dev/null
```

### वीडियो के बारे में सिलसिलेवार बातचीत

बातचीत के दौरान, वीडियो का कॉन्टेक्स्ट बनाए रखा जाता है. एजेंटिक प्रोसेसिंग का इस्तेमाल करते समय:

- **स्टेटफ़ुल मोड** (`previous_interaction_id` का इस्तेमाल करके): सर्वर, वीडियो के कॉन्टेक्स्ट को बनाए रखता है. इसके लिए, किसी अन्य कार्रवाई की ज़रूरत नहीं है.
- **स्टेटलेस मोड** (`step_list` का इस्तेमाल करके): स्टेटलेस मोड में, जवाब में `processing_call` और `processing_result` चरण शामिल होते हैं. ये चरण, वीडियो के कॉन्टेक्स्ट को एन्कोड करते हैं. वीडियो के कॉन्टेक्स्ट को बनाए रखने के लिए, आपको जवाब में बताए गए सभी चरणों को अपनी अगली `step_list` में शामिल करना होगा. फ़िलहाल, इन्हें शामिल न करने पर एपीआई से जुड़ी कोई गड़बड़ी नहीं होती. हालांकि, वीडियो का कॉन्टेक्स्ट खो जाता है. इससे, फ़ॉलो-अप सवालों के जवाब की क्वालिटी काफ़ी कम हो जाती है. ध्यान दें कि बाद के अनुरोधों में भेजे गए जवाबों में मौजूद चरणों की वजह से, इनपुट टोकन की संख्या बढ़ जाती है.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## वीडियो से ज़्यादा जानकारी पाना

Gemini मॉडल, वीडियो कॉन्टेंट को समझने के लिए बेहतरीन सुविधाएँ देते हैं. इसके लिए, वे **ऑडियो और विज़ुअल**, दोनों स्ट्रीम से जानकारी प्रोसेस करते हैं. इसकी मदद से, वीडियो के बारे में ज़्यादा जानकारी निकाली जा सकती है. जैसे, वीडियो में क्या हो रहा है, इसका ब्यौरा जनरेट करना और वीडियो के कॉन्टेंट के बारे में सवालों के जवाब देना.

विज़ुअल के बारे में जानकारी देने के लिए, मॉडल वीडियो को **हर सेकंड में एक फ़्रेम** (एफ़पीएस) की दर से सैंपल करता है. डिफ़ॉल्ट सैंपलिंग रेट, ज़्यादातर कॉन्टेंट के लिए सही होता है. हालांकि, ध्यान दें कि तेज़ गति वाले वीडियो या सीन में तेज़ी से बदलाव होने वाले वीडियो में, यह कुछ जानकारी को छोड़ सकता है.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Summarize the key events in this video.").build();
Content videoContent =
    VideoContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/video/pixel8.mp4")
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## वीडियो प्रोसेसिंग को पसंद के मुताबिक बनाना

Gemini API में वीडियो प्रोसेसिंग को अपनी पसंद के मुताबिक बनाया जा सकता है. इसके लिए, क्लिप करने के इंटरवल सेट करें या फ़्रेम रेट की सैंपलिंग को अपनी पसंद के मुताबिक बनाएं. कस्टमाइज़ेशन के ये विकल्प, सिर्फ़ `"static"` मोड में वीडियो प्रोसेस करते समय काम करते हैं.

### क्लिपिंग इंटरवल सेट करना

`processing` कॉन्फ़िगरेशन ऑब्जेक्ट में `start_offset` और `end_offset` तय करके, वीडियो को क्लिप किया जा सकता है.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### कस्टम फ़्रेम रेट सेट करना

`processing` कॉन्फ़िगरेशन ऑब्जेक्ट में `fps` आर्ग्युमेंट पास करके, फ़्रेम रेट की कस्टम सैंपलिंग सेट की जा सकती है.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## काम करने वाले वीडियो फ़ॉर्मैट

Gemini, वीडियो फ़ॉर्मैट के इन MIME टाइप के साथ काम करता है:

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

- **इस्तेमाल किए जा सकने वाले मॉडल और कॉन्टेक्स्ट**: सभी Gemini मॉडल, वीडियो डेटा को प्रोसेस कर सकते हैं.
  - 10 लाख टोकन वाली कॉन्टेक्स्ट विंडो वाले मॉडल, डिफ़ॉल्ट रूप से तीन घंटे तक के वीडियो प्रोसेस कर सकते हैं. हालांकि, ऐसा कम मीडिया रिज़ॉल्यूशन पर होता है. वहीं, ज़्यादा मीडिया रिज़ॉल्यूशन पर, ये मॉडल एक घंटे तक के वीडियो प्रोसेस कर सकते हैं.
- **प्रोसेसिंग मोड**: Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite, और इसके बाद के मॉडल में, वीडियो प्रोसेसिंग के दो मोड काम करते हैं:
  - **स्टैटिक**: फ़्रेम, 1 एफ़पीएस पर निकाले जाते हैं और उन्हें कॉन्टेक्स्ट में रखा जाता है. यह सभी मॉडल के लिए डिफ़ॉल्ट रूप से उपलब्ध होता है. ऑडियो को 1 केबीपीएस (सिंगल चैनल) पर प्रोसेस किया जाता है.
    टाइमस्टैंप हर सेकंड जोड़े जाते हैं. यह छोटी क्लिप के लिए सबसे अच्छा है. इसके अलावा, यह तब भी सबसे अच्छा है, जब हर फ़्रेम मायने रखता हो. जैसे, फ़्रेम-बाय-फ़्रेम जांच करना. ध्यान दें कि 1 एफ़पीएस की सैंपलिंग दर की वजह से, फ़ास्ट ऐक्शन सीक्वेंस में जानकारी कम हो सकती है.
  - **एजेंटिक**: यह मॉडल, वीडियो में डाइनैमिक तरीके से नेविगेट करता है. साथ ही, मांग पर ट्रांसक्रिप्ट और/या फ़्रेम और/या ऑडियो लोड करता है. यह लंबी अवधि के कॉन्टेंट के लिए, 88% तक कम टोकन का इस्तेमाल करता है. हालांकि, जनरेटिव एआई के काम करने के तरीके और जनरेट होने से पहले टूल के राउंड-ट्रिप की वजह से, छोटी क्लिप (<5 मिनट) पर नेविगेशन के लिए, पहले टोकन के लिए समय (टीटीएफटी) थोड़ा बढ़ सकता है. यह लंबी अवधि के वीडियो के लिए सबसे अच्छा है. इससे टोकन की लागत और जवाब की क्वालिटी को ऑप्टिमाइज़ किया जा सकता है.
    यह सुविधा, Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, और 3.5 Flash Lite पर काम करती है.
    ज़्यादा जानकारी के लिए, [एजेंटिक वीडियो अंडरस्टैंडिंग](#agentic-video-understanding) देखें.
- **टोकन कैलकुलेशन (स्टैटिक मोड)**: वीडियो के हर सेकंड को इस तरह टोकन में बदला जाता है:
  - अलग-अलग फ़्रेम (1 एफ़पीएस पर सैंपल किए गए):
    - अगर `media_resolution` को कम पर सेट किया जाता है, तो फ़्रेम को 66 टोकन प्रति फ़्रेम पर टोकन में बदला जाता है.
    - अगर ऐसा नहीं है, तो हर फ़्रेम के लिए 258 टोकन इस्तेमाल किए जाते हैं.
  - ऑडियो: हर सेकंड 32 टोकन.
  - इसमें मेटाडेटा भी शामिल होता है.
  - कुल: डिफ़ॉल्ट (कम) मीडिया रिज़ॉल्यूशन पर, वीडियो के हर सेकंड के लिए करीब 100 टोकन या हाई मीडिया रिज़ॉल्यूशन पर, वीडियो के हर सेकंड के लिए करीब 300 टोकन.
- **टोकन की गिनती (एजेंटिक मोड)**: टोकन का इस्तेमाल, कॉन्टेंट की जटिलता और मॉडल की नेविगेशन रणनीति के आधार पर अलग-अलग होता है. वीडियो एक्सप्लोर करने के दौरान जनरेट किए गए नेविगेशन रीज़निंग टोकन को **थॉट टोकन** (`total_thought_tokens`) के तौर पर गिना जाता है. वहीं, मांग पर लोड किए गए फ़्रेम, ऑडियो, और ट्रांसक्रिप्ट को टूल इस्तेमाल करने वाले टोकन (`total_tool_use_tokens`) के तौर पर गिना जाता है. आम तौर पर, एजेंटिक प्रोसेसिंग में स्टैटिक प्रोसेसिंग की तुलना में, लंबी अवधि के कॉन्टेंट के लिए कुल 88% कम टोकन इस्तेमाल होते हैं. ऐसा इसलिए होता है, क्योंकि मॉडल सिर्फ़ उस ट्रांसक्रिप्ट और/या फ़्रेम और/या ऑडियो को लोड करता है जिसकी उसे प्रॉम्प्ट का जवाब देने के लिए ज़रूरत होती है. ज़्यादा जानकारी के लिए, [टोकन गाइड](https://ai.google.dev/gemini-api/docs/tokens?hl=hi#video-token-usage) देखें.
- **मीडिया रिज़ॉल्यूशन**: Gemini 3 में, `media_resolution` पैरामीटर की मदद से मल्टीमॉडल विज़न प्रोसेसिंग को ज़्यादा बारीकी से कंट्रोल करने की सुविधा मिलती है. `media_resolution` पैरामीटर से यह तय होता है कि **हर इनपुट इमेज या वीडियो फ़्रेम के लिए, ज़्यादा से ज़्यादा कितने टोकन
  मिलेंगे.** ज़्यादा रिज़ॉल्यूशन से, मॉडल को छोटे टेक्स्ट को पढ़ने या छोटी-छोटी बारीकियों को पहचानने में मदद मिलती है. हालांकि, इससे टोकन का इस्तेमाल और लेटेन्सी बढ़ जाती है. `media_resolution` और `processing` पैरामीटर एक-दूसरे से अलग हैं: दोनों को एक ही वीडियो इनपुट पर सेट किया जा सकता है.

टोकन की गिनती के बारे में ज़्यादा जानने के लिए, [टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) गाइड देखें.

- **टाइमस्टैंप का फ़ॉर्मैट**: अपने प्रॉम्प्ट में किसी वीडियो के खास पलों के बारे में बताते समय, `MM:SS` फ़ॉर्मैट का इस्तेमाल करें. उदाहरण के लिए, 1 मिनट और 15 सेकंड के लिए `01:15`.
- **प्रॉम्प्ट का प्लेसमेंट**: अगर टेक्स्ट और एक वीडियो को साथ में इस्तेमाल किया जा रहा है, तो `input` ऐरे में वीडियो के बाद टेक्स्ट प्रॉम्प्ट को *रखें*.
- **लंबे अनुरोधों के लिए टाइमआउट**: ऐसे वीडियो के लिए स्ट्रीमिंग (`stream=True`) या बैकग्राउंड में प्रोसेस करने (`background=True`) की सुविधा का इस्तेमाल करें जिन्हें प्रोसेस करने में ज़्यादा समय लगता है या जिनमें कई चरणों में जटिल तर्क शामिल होते हैं.
  सिंक्रोनस, नॉन-स्ट्रीमिंग अनुरोधों के लिए, ज़्यादा मांग होने पर बैकएंड से फिर से कोशिश की जाती है. इससे कनेक्शन या पुष्टि करने वाले टोकन की वैधता की अवधि खत्म हो सकती है. ऐसा होने पर, `401 Unauthorized` या टाइमआउट से जुड़ी गड़बड़ियां दिख सकती हैं.
  स्ट्रीमिंग से, कनेक्शन चालू रहता है. साथ ही, इससे बीच-बीच में तर्क और टूल कॉल की प्रोग्रेस दिखती है.

## आगे क्या करना है

- [मीडिया रिज़ॉल्यूशन](https://ai.google.dev/gemini-api/docs/media-resolution?hl=hi): क्वालिटी और टोकन के इस्तेमाल को बैलेंस करने के लिए, वीडियो फ़्रेम के रिज़ॉल्यूशन को कंट्रोल करें.
- [टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi): जानें कि स्टैटिक और एजेंटिक, दोनों प्रोसेसिंग मोड में वीडियो कॉन्टेंट को कैसे टोकनाइज़ किया जाता है.
- [सिस्टम के लिए निर्देश](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#system-instructions):
  सिस्टम के लिए निर्देश देने की सुविधा की मदद से, अपनी खास ज़रूरतों और इस्तेमाल के उदाहरणों के आधार पर, मॉडल के व्यवहार को कंट्रोल किया जा सकता है.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi): Gemini के साथ इस्तेमाल करने के लिए, फ़ाइलें अपलोड करने और उन्हें मैनेज करने के बारे में ज़्यादा जानें.
- [फ़ाइल प्रॉम्प्ट करने की रणनीतियां](https://ai.google.dev/gemini-api/docs/files?hl=hi#prompt-guide): Gemini API, टेक्स्ट, इमेज, ऑडियो, और वीडियो डेटा के साथ प्रॉम्प्ट करने की सुविधा देता है. इसे मल्टीमॉडल प्रॉम्प्टिंग भी कहा जाता है.
- [सुरक्षा से जुड़ी गाइडलाइन](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=hi): कभी-कभी जनरेटिव एआई मॉडल ऐसे आउटपुट जनरेट करते हैं जिनकी उम्मीद नहीं होती. जैसे, गलत, पक्षपात वाले या आपत्तिजनक आउटपुट. इस तरह के आउटपुट से होने वाले नुकसान के जोखिम को कम करने के लिए, पोस्ट-प्रोसेसिंग और मैन्युअल तरीके से आकलन करना ज़रूरी है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया."],[],[]]
