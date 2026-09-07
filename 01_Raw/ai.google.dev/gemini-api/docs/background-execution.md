---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=hi
fetched_at: 2026-09-07T05:44:57.505078+00:00
title: "\u092c\u0948\u0915\u0917\u094d\u0930\u093e\u0909\u0902\u0921 \u092e\u0947\u0902 \u0915\u094b\u0921 \u090f\u0915\u094d\u091c\u093c\u0940\u0915\u094d\u092f\u0942\u091f \u0939\u094b\u0928\u0947 \u0915\u0940 \u0938\u0941\u0935\u093f\u0927\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# बैकग्राउंड में कोड एक्ज़ीक्यूट होने की सुविधा

डीप रिसर्च, मुश्किल तर्क-वितर्क या कई चरणों वाले एजेंट के एक्ज़ीक्यूशन जैसे लंबे समय तक चलने वाले टास्क के लिए, कनेक्शन टाइमआउट की वजह से स्टैंडर्ड एचटीटीपी अनुरोधों में रुकावट आ सकती है. आम तौर पर, ये अनुरोध 60 सेकंड बाद बंद हो जाते हैं. [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi), इन टास्क को एसिंक्रोनस तरीके से चलाने के लिए, **बैकग्राउंड में कोड एक्ज़ीक्यूट होने की सुविधा** देता है.

इंटरैक्शन को सर्वर पर टास्क पूरा होने तक चलाने के लिए, इंटरैक्शन बनाते समय `"background": true` सेट करें. एपीआई तुरंत एक इंटरैक्शन आईडी दिखाता है. क्लाइंट ऐप्लिकेशन, इस आईडी का इस्तेमाल करके, स्टेटस के लिए पोल कर सकते हैं, प्रोग्रेस को स्ट्रीम कर सकते हैं या डिसकनेक्ट हुई स्ट्रीम से फिर से कनेक्ट हो सकते हैं.

बैकग्राउंड में कोड एक्ज़ीक्यूट होने की सुविधा, Gemini के स्टैंडर्ड मॉडल (जैसे, `gemini-3.8-flash` और `gemini-3.1-pro-preview`) और एजेंट बनाने और मैनेज करने की सुविधा (जैसे, `antigravity-preview-05-2026`) के लिए उपलब्ध है.

## बैकग्राउंड में इंटरैक्शन बनाना

बैकग्राउंड में इंटरैक्शन शुरू करने के लिए, संसाधन बनाते समय `background` पैरामीटर को `true` पर सेट करें.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## बैकग्राउंड में कोड एक्ज़ीक्यूट होने की सुविधा कैसे काम करती है

बैकग्राउंड में इंटरैक्शन बनाने पर, टास्क सर्वर पर एसिंक्रोनस तरीके से चलता है. इंटरैक्शन, एक्ज़ीक्यूशन की अलग-अलग स्थितियों से गुज़रता है:

- `in_progress`: सर्वर, इंटरैक्शन को ऐक्टिव तौर पर एक्ज़ीक्यूट कर रहा है. जैसे, कोड चलाना या रिसर्च करना.
- `requires_action`: इंटरैक्शन रुक गया है और क्लाइंट के इनपुट का इंतज़ार कर रहा है. जैसे, किसी टूल के एक्ज़ीक्यूशन की पुष्टि करना या किसी सवाल का जवाब देना.
- `completed`: इंटरैक्शन, सफलतापूर्वक पूरा हो गया है और आउटपुट उपलब्ध है.
- `failed`: एक्ज़ीक्यूशन के दौरान कोई गड़बड़ी हुई. जैसे, टूल में गड़बड़ी या रेट लिमिट.
- `cancelled`: क्लाइंट के अनुरोध की वजह से, एक्ज़ीक्यूशन रुक गया.

### इस्तेमाल के उदाहरण

बैकग्राउंड में कोड एक्ज़ीक्यूट होने की सुविधा का इस्तेमाल इन कामों के लिए करें:

- **एजेंट के एक्ज़ीक्यूशन:** ऐसे टास्क जिनके लिए कोड एक्ज़ीक्यूट करना, वेब ब्राउज़ करना या सब-एजेंट ऑर्केस्ट्रेशन करना ज़रूरी है. जैसे, `antigravity-preview-05-2026`.
- **डीप रिसर्च:** `deep-research-preview-04-2026` या `deep-research-max-preview-04-2026` का इस्तेमाल करके की जाने वाली रिसर्च, जिसमें कई मिनट लगते हैं.
- **लंबे तर्क-वितर्क:** ऐसे टास्क जिनमें मॉडल के सोचने के चरण, स्टैंडर्ड एचटीटीपी कनेक्शन की सीमाओं से ज़्यादा होते हैं.

## नतीजे पाना

**पोलिंग** या **स्ट्रीमिंग** का इस्तेमाल करके, बैकग्राउंड में किए गए इंटरैक्शन के नतीजे पाएं.

### पोलिंग पैटर्न (नॉन-ब्लॉकिंग)

पोलिंग, इंटरैक्शन के स्टेटस की समय-समय पर जांच करता है. इसके लिए, नॉन-ब्लॉकिंग जीईटी अनुरोधों का इस्तेमाल किया जाता है. यह तब तक जारी रहता है, जब तक इंटरैक्शन, टर्मिनल स्थिति में न पहुंच जाए.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### स्ट्रीमिंग पैटर्न

अगर नेटवर्क में रुकावट की वजह से कोई स्ट्रीम डिसकनेक्ट हो जाती है, तो स्ट्रीमिंग को आखिरी बार मिले इवेंट से फिर से शुरू किया जा सकता है. हर डेल्टा के पेलोड में एक यूनीक `event_id` होता है. इस आईडी को `last_event_id` के तौर पर पास करने से, स्ट्रीम उस इवेंट से फिर से शुरू हो जाती है.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## सिलसिलेवार बातचीत

`previous_interaction_id` का इस्तेमाल करके, बाद के इंटरैक्शन को बैकग्राउंड में की गई बातचीत से जोड़ा जा सकता है. हालांकि, इसके लिए ये शर्तें पूरी होनी चाहिए:

1. **ऐक्टिव एक्ज़ीक्यूशन ब्लॉक किए जाते हैं:** `in_progress` स्टेटस वाले इंटरैक्शन से, बाद के इंटरैक्शन को जोड़ने पर, `400 Bad Request` गड़बड़ी दिखती है. अगला इंटरैक्शन शुरू करने से पहले, पहले इंटरैक्शन के `completed` स्थिति में पहुंचने का इंतज़ार करें.
2. **एजेंट बनाने और मैनेज करने की सुविधा के लिए एनवायरमेंट पैरामीटर:** एजेंट बनाने और मैनेज करने की सुविधा (जैसे, `antigravity-preview-05-2026`) के लिए इंटरैक्शन को जोड़ते समय, अनुरोधों में `previous_interaction_id` और `environment`, दोनों शामिल होने चाहिए.

यहां दिए गए उदाहरणों में, इंटरैक्शन को जोड़ने का तरीका बताया गया है:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## रद्द करना और मिटाना

रद्द करने और मिटाने के अनुरोधों का इस्तेमाल करके, चल रहे एक्ज़ीक्यूशन को कंट्रोल करें और स्टोरेज को मैनेज करें:

- **रद्द करें (`POST /interactions/{id}/cancel`):** चल रहे टास्क को रोकता है. स्टेटस बदलकर `cancelled` हो जाता है. सर्वर पर क्लीन-अप की कार्रवाइयों की वजह से, जीईटी अनुरोधों में स्टेटस अपडेट होने में थोड़ी देरी हो सकती है.
- **मिटाएं (`DELETE /interactions/{id}`):** सर्वर से इंटरैक्शन के रिकॉर्ड मिटाता है. इसके बाद के जीईटी अनुरोधों में, `404 Not Found` गड़बड़ी दिखती है.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.operations.GetInteractionByIdResponse;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Execute this background task."))
        .background(true)
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");

// Poll status using GetInteractionByIdRequest
GetInteractionByIdResponse getResponse =
    client.interactions.get(new GetInteractionByIdRequest(interactionId));
Interaction polled = getResponse.interaction().get();
System.out.println("Status: " + polled.status().orElse(null));
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## अगले चरण

- सेशन और स्टेटस मैनेजमेंट को समझने के लिए, [Interactions API की खास जानकारी](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) पढ़ें.
- रीयल-टाइम इवेंट अपडेट के बारे में ज़्यादा जानने के लिए, [स्ट्रीमिंग इंटरैक्शन](https://ai.google.dev/gemini-api/docs/streaming?hl=hi) से जुड़ी गाइड देखें.
- स्टेटफ़ुल सिलसिलेवार बातचीत वाले एजेंट बनाने के लिए, [मैनेज किए जाने वाले एजेंट का क्विकस्टार्ट](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-04 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-04 (UTC) को अपडेट किया गया."],[],[]]
