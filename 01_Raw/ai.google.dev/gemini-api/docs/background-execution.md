---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=th
fetched_at: 2026-10-12T07:05:59.308401+00:00
title: "\u0e01\u0e32\u0e23\u0e14\u0e33\u0e40\u0e19\u0e34\u0e19\u0e01\u0e32\u0e23\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e2d\u0e22\u0e39\u0e48\u0e40\u0e1a\u0e37\u0e49\u0e2d\u0e07\u0e2b\u0e25\u0e31\u0e07 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การดำเนินการเมื่ออยู่เบื้องหลัง

สำหรับงานที่ใช้เวลานาน เช่น การค้นคว้าอย่างละเอียด การให้เหตุผลที่ซับซ้อน หรือการดำเนินการของเอเจนต์แบบหลายขั้นตอน การหมดเวลาการเชื่อมต่ออาจขัดขวางคำขอ HTTP มาตรฐาน (ซึ่งโดยปกติจะปิดหลังจาก 60 วินาที) [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) มี**การดำเนินการเบื้องหลัง**เพื่อเรียกใช้งานแบบไม่พร้อมกัน

หากต้องการให้การโต้ตอบทำงานจนกว่าจะทำงานบนเซิร์ฟเวอร์เสร็จสมบูรณ์ ให้ตั้งค่า `"background": true` เมื่อสร้างการโต้ตอบ API จะแสดงรหัสการโต้ตอบทันที ซึ่งแอปพลิเคชันไคลเอ็นต์สามารถใช้เพื่อสำรวจสถานะ ความคืบหน้าของสตรีม หรือเชื่อมต่อสตรีมที่ถูกตัดการเชื่อมต่ออีกครั้ง

ระบบรองรับการดำเนินการเมื่ออยู่เบื้องหลังสำหรับโมเดล Gemini มาตรฐาน (เช่น `gemini-3.8-flash` และ `gemini-3.1-pro-preview`) และ Agent ที่ได้รับการจัดการ (เช่น `antigravity-preview-09-2026`)

## สร้างการโต้ตอบในเบื้องหลัง

หากต้องการเริ่มการโต้ตอบในเบื้องหลัง ให้ตั้งค่าพารามิเตอร์ `background` เป็น `true` เมื่อสร้างทรัพยากร

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

### Go

```
package main

import (
    "context"
    "fmt"
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:      interactions.Model("gemini-3.8-flash"),
            Input:      interactions.NewInteractionsInput("Write a guide on space exploration."),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.ID != nil {
        fmt.Printf("Created background interaction ID: %s\n", *res.Interaction.ID)
    }
}
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

## วิธีการทำงานของการดำเนินการในเบื้องหลัง

เมื่อสร้างการโต้ตอบในเบื้องหลัง งานจะทำงานแบบไม่พร้อมกันในเซิร์ฟเวอร์ การโต้ตอบจะเปลี่ยนสถานะการดำเนินการต่างๆ ดังนี้

- `in_progress`: เซิร์ฟเวอร์กำลังดำเนินการโต้ตอบอยู่ (เช่น การเรียกใช้โค้ดหรือการค้นคว้า)
- `requires_action`: การโต้ตอบหยุดชั่วคราวและรอข้อมูลจากไคลเอ็นต์ (เช่น การยืนยันการเรียกใช้เครื่องมือหรือตอบคำถาม)
- `completed`: การโต้ตอบเสร็จสมบูรณ์และเอาต์พุตพร้อมใช้งานแล้ว
- `failed`: เกิดข้อผิดพลาดในระหว่างการดำเนินการ (เช่น เครื่องมือล้มเหลวหรือเกินขีดจำกัดอัตรา)
- `cancelled`: คำขอของไคลเอ็นต์หยุดการดำเนินการ

### กรณีการใช้งาน

ใช้การดำเนินการเมื่ออยู่เบื้องหลังสำหรับ

- **การดำเนินการของเอเจนต์:** งานที่ต้องมีการดำเนินการโค้ด การท่องเว็บ หรือการจัดระเบียบเอเจนต์ย่อย (เช่น `antigravity-preview-09-2026`)
- **Deep Research:** ทำงานโดยใช้ `deep-research-preview-04-2026` หรือ `deep-research-max-preview-04-2026` ซึ่งใช้เวลาหลายนาที
- **การให้เหตุผลแบบยาว:** งานที่ขั้นตอนการคิดของโมเดลเกินขีดจำกัดการเชื่อมต่อ HTTP มาตรฐาน

## เรียกดูผลลัพธ์

รับผลลัพธ์การโต้ตอบเบื้องหลังโดยใช้**การสำรวจ**หรือ**การสตรีม**

### รูปแบบการสำรวจ (ไม่บล็อก)

การสำรวจจะตรวจสอบสถานะการโต้ตอบเป็นระยะๆ โดยใช้คำขอ GET ที่ไม่บล็อกจนกว่าจะถึงสถานะสิ้นสุด

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    res, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
        ID: "YOUR_INTERACTION_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res.Interaction

    for interaction.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        res, err = client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = res.Interaction
    }

    if interaction.Status == interactions.InteractionStatusCompleted {
        if interaction.OutputText != nil {
            fmt.Println(*interaction.OutputText)
        }
    } else {
        fmt.Printf("Finished with status: %s\n", interaction.Status)
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### รูปแบบการสตรีม

หากเครือข่ายหยุดทำงานจนทำให้สตรีมถูกตัดขาด สตรีมมิงจะกลับมาทำงานต่อจากเหตุการณ์ล่าสุดที่ได้รับ โดยแต่ละเดลต้าจะมี `event_id` ที่ไม่ซ้ำกันในเพย์โหลด การส่งรหัสนี้เป็น `last_event_id` จะทำให้สตรีมเล่นต่อจากเหตุการณ์นั้น

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    interactionID := "YOUR_INTERACTION_ID"
    var lastEventID *string
    completed := false

    for !completed {
        res, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID:          interactionID,
            Stream:      genai.Ptr(true),
            LastEventID: lastEventID,
        })
        if err != nil {
            fmt.Printf("\n[Connection lost: %v. Reconnecting in 3s...]\n", err)
            time.Sleep(3 * time.Second)
            continue
        }

        stream := res.InteractionSSEStreamEvent
        for stream.Next() {
            event := stream.Value()
            if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
                if stepDelta.EventID != nil {
                    lastEventID = stepDelta.EventID
                }
                if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                    fmt.Print(textDelta.GetText())
                }
            } else if event.GetDataInteractionCompleted() != nil {
                completed = true
                break
            }
        }
        if err := stream.Err(); err != nil {
            fmt.Printf("\n[Stream error: %v. Reconnecting in 3s...]\n", err)
            _ = stream.Close()
            time.Sleep(3 * time.Second)
            continue
        }
        _ = stream.Close()
    }
}
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## การสนทนาไปมา

การโต้ตอบในภายหลังจะเชื่อมโยงกับการสนทนาในเบื้องหลังได้โดยใช้ `previous_interaction_id` โดยขึ้นอยู่กับข้อจำกัดต่อไปนี้

1. **การดำเนินการที่ใช้งานอยู่จะถูกบล็อก:** การเชื่อมต่อการโต้ตอบที่ตามมากับการโต้ตอบที่มี`in_progress`สถานะจะแสดงข้อผิดพลาด `400 Bad Request` รอให้การโต้ตอบถึงสถานะ `completed` ก่อนเริ่มการโต้ตอบถัดไป
2. **พารามิเตอร์สภาพแวดล้อมสำหรับ Agent ที่ได้รับการจัดการ:** เมื่อเชื่อมโยงการโต้ตอบสำหรับ Agent ที่ได้รับการจัดการ (เช่น `antigravity-preview-09-2026`) คำขอต้องมีทั้ง `previous_interaction_id` และ `environment`

ตัวอย่างต่อไปนี้แสดงวิธีเชื่อมโยงการโต้ตอบ

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

### Go

```
package main

import (
    "context"
    "log"
    "time"

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

    agentModel := interactions.Model("antigravity-preview-09-2026")
    remoteEnv := interactions.NewCreateModelInteractionEnvironment("remote")

    // First interaction: Provision sandbox environment and execute first instruction
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       agentModel,
            Input:       interactions.NewInteractionsInput("Create a folder named project/ and write hello.py inside."),
            Environment: &remoteEnv,
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Wait for completion
    for {
        check, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *res1.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        if check.Interaction.Status != interactions.InteractionStatusInProgress {
            break
        }
        time.Sleep(2 * time.Second)
    }

    // Second interaction: Chain using PreviousInteractionID and Environment
    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 agentModel,
            Input:                 interactions.NewInteractionsInput("List all files in the project/ directory."),
            PreviousInteractionID: res1.Interaction.ID,
            Environment:           &remoteEnv,
            Background:            genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
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

## การยกเลิกและการลบ

ควบคุมการดำเนินการที่กำลังทำงานและจัดการพื้นที่เก็บข้อมูลโดยใช้คำขอยกเลิกและลบ

- **ยกเลิก (`POST /interactions/{id}/cancel`):** หยุดงานที่กำลังทำงานอยู่ สถานะจะเปลี่ยนเป็น`cancelled` การดำเนินการล้างข้อมูลในเซิร์ฟเวอร์อาจทำให้เกิดความล่าช้าเล็กน้อยก่อนที่สถานะจะอัปเดตในคำขอ GET
- **ลบ (`DELETE /interactions/{id}`):** นำบันทึกการโต้ตอบออกจากเซิร์ฟเวอร์ คำขอ GET ที่ตามมาจะแสดงข้อผิดพลาด `404 Not Found`

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

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Cancel a running interaction
    _, err = client.Interactions.Cancel(ctx, operations.CancelInteractionByIDRequest{
        ID: "YOUR_INTERACTION_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    // Delete the interaction record entirely
    _, err = client.Interactions.Delete(ctx, operations.DeleteInteractionRequest{
        ID: "YOUR_INTERACTION_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
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

## ขั้นตอนถัดไป

- อ่าน[ภาพรวมของ Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) เพื่อทำความเข้าใจการจัดการเซสชันและสถานะ
- ดูรายละเอียดเกี่ยวกับการอัปเดตกิจกรรมแบบเรียลไทม์ได้ในคำแนะนำเกี่ยวกับ[การโต้ตอบในการสตรีม](https://ai.google.dev/gemini-api/docs/streaming?hl=th)
- สำรวจ[การเริ่มต้นใช้งานด่วนของ Agent ที่มีการจัดการ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th)เพื่อสร้าง Agent แบบหลายเทิร์นที่มีสถานะ

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
