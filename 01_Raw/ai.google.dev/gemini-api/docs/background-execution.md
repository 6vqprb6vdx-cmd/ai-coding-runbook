---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=hi
fetched_at: 2026-09-21T05:56:26.030997+00:00
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

डीप रिसर्च, जटिल तर्क या कई चरणों वाले एजेंट एक्ज़ीक्यूशन जैसे लंबे समय तक चलने वाले टास्क के लिए, कनेक्शन टाइमआउट की वजह से स्टैंडर्ड एचटीटीपी अनुरोधों में रुकावट आ सकती है. ये अनुरोध आम तौर पर 60 सेकंड के बाद बंद हो जाते हैं. [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi), इन टास्क को एसिंक्रोनस तरीके से चलाने के लिए **बैकग्राउंड में प्रोसेस करने की सुविधा** देता है.

इंटरैक्शन को तब तक चलने दें, जब तक कि वह सर्वर पर टास्क पूरा न कर ले. इसके लिए, इंटरैक्शन बनाते समय `"background": true` सेट करें. एपीआई तुरंत इंटरैक्शन आईडी दिखाता है. क्लाइंट ऐप्लिकेशन, इस आईडी का इस्तेमाल करके स्टेटस, स्ट्रीम की प्रोग्रेस या डिस्कनेक्ट की गई स्ट्रीम से फिर से कनेक्ट करने के लिए पोल कर सकते हैं.

बैकग्राउंड में प्रोग्राम चलाने की सुविधा, Gemini के स्टैंडर्ड मॉडल (जैसे कि `gemini-3.8-flash` और `gemini-3.1-pro-preview`) और एजेंट बनाने और मैनेज करने की सुविधा (जैसे कि `antigravity-preview-09-2026`) के लिए उपलब्ध है.

## बैकग्राउंड इंटरैक्शन बनाना

बैकग्राउंड इंटरैक्शन शुरू करने के लिए, संसाधन बनाते समय `background` पैरामीटर को `true` पर सेट करें.

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
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Write a guide on space exploration."))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Created background interaction ID: " + interaction.id().orElse(""));
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

बैकग्राउंड इंटरैक्शन बनाने पर, टास्क सर्वर पर एसिंक्रोनस तरीके से चलता है. इंटरैक्शन, एक्ज़ीक्यूशन की अलग-अलग स्थितियों से गुज़रता है:

- `in_progress`: सर्वर, इंटरैक्शन को चालू तौर पर लागू कर रहा है. जैसे, कोड चलाना या रिसर्च करना.
- `requires_action`: इंटरैक्शन को रोक दिया गया है और क्लाइंट के इनपुट का इंतज़ार किया जा रहा है. जैसे, टूल के इस्तेमाल की पुष्टि करना या किसी सवाल का जवाब देना.
- `completed`: इंटरैक्शन पूरा हो गया है और आउटपुट उपलब्ध है.
- `failed`: स्क्रिप्ट चलाने के दौरान कोई गड़बड़ी हुई. जैसे, टूल काम नहीं कर रहा है या दर की सीमाएं पूरी हो गई हैं.
- `cancelled`: क्लाइंट के अनुरोध पर, एक्ज़ीक्यूशन रोक दिया गया है.

### उपयोग के उदाहरण

बैकग्राउंड में कोड एक्ज़ीक्यूट होने की सुविधा का इस्तेमाल इन कामों के लिए किया जा सकता है:

- **एजेंट के ज़रिए की जाने वाली कार्रवाइयां:** ऐसे टास्क जिनके लिए कोड को लागू करना, वेब ब्राउज़ करना या सब-एजेंट को व्यवस्थित करना ज़रूरी होता है. जैसे, `antigravity-preview-09-2026`.
- **Deep Research:** यह `deep-research-preview-04-2026` या `deep-research-max-preview-04-2026` का इस्तेमाल करके काम करता है. इसमें कई मिनट लगते हैं.
- **गहराई से विश्लेषण में ज़्यादा समय लगना:** ऐसे टास्क जिनमें मॉडल के गहराई से विचार करने के चरण, स्टैंडर्ड एचटीटीपी कनेक्शन की सीमाओं से ज़्यादा होते हैं.

## नतीजे वापस पाना

**पोलिंग** या **स्ट्रीमिंग** का इस्तेमाल करके, बैकग्राउंड इंटरैक्शन के नतीजे पाएं.

### पोलिंग पैटर्न (नॉन-ब्लॉकिंग)

पोलिंग, इंटरैक्शन की स्थिति की समय-समय पर जांच करती है. इसके लिए, नॉन-ब्लॉकिंग GET अनुरोधों का इस्तेमाल किया जाता है. यह तब तक किया जाता है, जब तक कि इंटरैक्शन की स्थिति आखिरी स्थिति तक न पहुंच जाए.

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
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

Interaction interaction =
    client.interactions
        .get(GetInteractionByIdRequest.builder().id("YOUR_INTERACTION_ID").build())
        .interaction()
        .get();

while (InteractionStatus.IN_PROGRESS.equals(interaction.status().orElse(null))) {
  Thread.sleep(5000);
  interaction =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
}

if (InteractionStatus.COMPLETED.equals(interaction.status().orElse(null))) {
  System.out.println(interaction.outputText().orElse(""));
} else {
  System.out.println(
      "Finished with status: " + interaction.status().map(InteractionStatus::value).orElse(""));
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### स्ट्रीमिंग पैटर्न

अगर नेटवर्क में रुकावट आने की वजह से कोई स्ट्रीम बंद हो जाती है, तो स्ट्रीमिंग को आखिरी बार मिले इवेंट से फिर से शुरू किया जा सकता है. हर डेल्टा के पेलोड में एक यूनीक `event_id` होता है. इस आईडी को `last_event_id` के तौर पर पास करने से, स्ट्रीम उस इवेंट से फिर से शुरू हो जाती है.

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
import com.google.genai.gaos.models.interactions.InteractionCompletedEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();
String interactionId = "YOUR_INTERACTION_ID";
String lastEventId = null;
boolean completed = false;

while (!completed) {
  try (EventStream<InteractionSSEStreamEvent> stream =
      client.interactions
          .get(
              GetInteractionByIdRequest.builder()
                  .id(interactionId)
                  .stream(true)
                  .lastEventId(lastEventId)
                  .build())
          .events()) {
    for (InteractionSSEStreamEvent streamEvent : stream) {
      InteractionSSEEvent event = streamEvent.data().orElse(null);
      if (event instanceof StepDelta) {
        StepDelta stepDelta = (StepDelta) event;
        if (stepDelta.eventId().isPresent()) {
          lastEventId = stepDelta.eventId().get();
        }
        if (stepDelta.delta().isPresent() && stepDelta.delta().get() instanceof TextDelta) {
          System.out.print(((TextDelta) stepDelta.delta().get()).text().orElse(""));
          System.out.flush();
        }
      } else if (event instanceof InteractionCompletedEvent) {
        completed = true;
        break;
      }
    }
  } catch (Exception e) {
    System.out.println("\n[Connection lost: " + e.getMessage() + ". Reconnecting in 3s...]");
    Thread.sleep(3000);
  }
}
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## सिलसिलेवार बातचीत

इसके बाद के इंटरैक्शन को, `previous_interaction_id` का इस्तेमाल करके बैकग्राउंड बातचीत से जोड़ा जा सकता है. हालांकि, इसके लिए ये शर्तें पूरी होनी चाहिए:

1. **चालू किए गए एक्ज़ीक्यूशन ब्लॉक कर दिए जाते हैं:** `in_progress` स्टेटस वाले इंटरैक्शन के बाद, किसी अन्य इंटरैक्शन को चेन करने पर `400 Bad Request` गड़बड़ी दिखती है. अगला इंटरैक्शन शुरू करने से पहले, इंटरैक्शन के `completed` स्थिति में पहुँचने का इंतज़ार करें.
2. **एजेंट बनाने और मैनेज करने की सुविधा के लिए एनवायरमेंट पैरामीटर:** एजेंट बनाने और मैनेज करने की सुविधा (जैसे कि `antigravity-preview-09-2026`) के लिए इंटरैक्शन को चेन करते समय, अनुरोधों में `previous_interaction_id` और `environment`, दोनों शामिल होने चाहिए.

यहां दिए गए उदाहरणों में, इंटरैक्शन को एक साथ जोड़ने का तरीका बताया गया है:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-09-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    agent=agent_model,
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
    agent=agent_model,
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
const agentModel = "antigravity-preview-09-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    agent: agentModel,
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
    agent: agentModel,
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
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();
String agentModel = "antigravity-preview-09-2026";

// First interaction: Provision sandbox environment and execute first instruction
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(agentModel)
        .input(InteractionsInput.of("Create a folder named project/ and write hello.py inside."))
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .background(true)
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Wait for completion
while (true) {
  Interaction check =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction1.id().get()).build())
          .interaction()
          .get();
  if (!InteractionStatus.IN_PROGRESS.equals(check.status().orElse(null))) {
    break;
  }
  Thread.sleep(2000);
}

// Second interaction: Chain using previousInteractionId and environment
CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(agentModel)
        .input(InteractionsInput.of("List all files in the project/ directory."))
        .previousInteractionId(interaction1.id().get())
        .environment(CreateModelInteractionEnvironment.of("remote"))
        .background(true)
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## रद्द करना और मिटाना

अनुरोध रद्द करने और मिटाने की सुविधा का इस्तेमाल करके, चल रहे एक्ज़ीक्यूशन को कंट्रोल करें और स्टोरेज को मैनेज करें:

- **रद्द करें (`POST /interactions/{id}/cancel`):** इससे चल रहा टास्क बंद हो जाता है. इसके बाद, स्टेटस `cancelled` में बदल जाता है. सर्वर पर क्लीन-अप की कार्रवाइयों की वजह से, GET अनुरोधों में स्थिति अपडेट होने में थोड़ा समय लग सकता है.
- **मिटाएं (`DELETE /interactions/{id}`):** इससे इंटरैक्शन रिकॉर्ड, सर्वर से हट जाते हैं. इसके बाद, GET अनुरोधों से `404 Not Found` गड़बड़ी का मैसेज मिलता है.

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

Client client = new Client();

// Cancel a running interaction
client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
client.interactions.delete("YOUR_INTERACTION_ID");
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

- सेशन और स्टेट मैनेजमेंट को समझने के लिए, [Interactions API की खास जानकारी](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) पढ़ें.
- रीयल-टाइम में इवेंट के अपडेट के बारे में जानने के लिए, [स्ट्रीमिंग के दौरान दर्शकों से इंटरैक्ट करना](https://ai.google.dev/gemini-api/docs/streaming?hl=hi) गाइड देखें.
- स्टेटफ़ुल सिलसिलेवार बातचीत वाले एजेंट बनाने के लिए, [मैनेज किए गए एजेंट के लिए क्विकस्टार्ट गाइड](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया."],[],[]]
