---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=vi
fetched_at: 2026-11-02T07:23:14.031070+00:00
title: "Ch\u1ea1y \u1edf ch\u1ebf \u0111\u1ed9 n\u1ec1n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Chạy ở chế độ nền

Đối với các tác vụ chạy trong thời gian dài như Deep Research, suy luận phức tạp hoặc thực thi tác nhân nhiều bước, thời gian chờ kết nối có thể làm gián đoạn các yêu cầu HTTP tiêu chuẩn (thường đóng sau 60 giây). [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) cung cấp tính năng **thực thi trong nền** để chạy các tác vụ này một cách không đồng bộ.

Để cho phép hoạt động tương tác chạy cho đến khi hoàn tất tác vụ trên máy chủ, hãy đặt `"background": true` khi tạo hoạt động tương tác. API này ngay lập tức trả về một mã nhận dạng tương tác mà các ứng dụng khách có thể dùng để thăm dò trạng thái, tiến trình phát trực tuyến hoặc kết nối lại với một luồng bị ngắt kết nối.

Tính năng thực thi trong nền được hỗ trợ cho các mô hình Gemini tiêu chuẩn (chẳng hạn như `gemini-4-argon` và `gemini-3.8-flash`) và Tác nhân được quản lý (chẳng hạn như `antigravity-preview-09-2026`).

## Tạo một hoạt động tương tác trong nền

Để bắt đầu một hoạt động tương tác trong nền, hãy đặt tham số `background` thành `true` khi tạo tài nguyên.

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

## Cách hoạt động của tính năng thực thi trong nền

Khi bạn tạo một hoạt động tương tác trong nền, tác vụ sẽ chạy không đồng bộ trên máy chủ. Hoạt động tương tác chuyển đổi qua nhiều trạng thái thực thi:

- `in_progress`: Máy chủ đang tích cực thực hiện hoạt động tương tác (chẳng hạn như chạy mã hoặc nghiên cứu).
- `requires_action`: Lượt tương tác đã tạm dừng và đang chờ thông tin đầu vào của ứng dụng (chẳng hạn như xác nhận việc thực thi công cụ hoặc trả lời câu hỏi).
- `completed`: Hoạt động tương tác đã hoàn tất thành công và có kết quả.
- `failed`: Đã xảy ra lỗi trong quá trình thực thi (chẳng hạn như lỗi công cụ hoặc giới hạn số lượng yêu cầu).
- `cancelled`: Một yêu cầu của ứng dụng đã dừng quá trình thực thi.

### Trường hợp sử dụng

Sử dụng chế độ thực thi trong nền cho:

- **Thực thi tác nhân:** Các tác vụ yêu cầu thực thi mã, duyệt web hoặc điều phối tác nhân phụ (chẳng hạn như `antigravity-preview-09-2026`).
- **Deep Research:** Chạy bằng `deep-research-preview-04-2026` hoặc `deep-research-max-preview-04-2026`, mất vài phút.
- **Suy luận dài:** Những nhiệm vụ mà các bước suy nghĩ mở rộng của mô hình vượt quá giới hạn kết nối HTTP tiêu chuẩn.
- **Giải mã dài (Gemini 4):** Các tác vụ tạo ra kết quả hoàn thành mở rộng vượt quá `65,536` mã thông báo. Trên `gemini-4-argon`, bạn có thể đặt tối đa `1,048,576` mã thông báo `max_output_tokens` bằng cách sử dụng tính năng [giải mã dài](https://ai.google.dev/gemini-api/docs/long-decode?hl=vi).

### Giữ lại dữ liệu cho quá trình thực thi trong nền

Quá trình thực thi trong nền (`background=True`) yêu cầu `store=True` (mặc định) để máy chủ có thể lưu trữ hoạt động tương tác trong khi bạn thăm dò ý kiến hoặc truyền trực tuyến kết quả. Việc truyền `background=True` bằng `store=False` sẽ trả về lỗi `400`.

Các hoạt động tương tác được lưu trữ ở chế độ nền tuân theo chính sách [lưu trữ và giữ lại dữ liệu tiêu chuẩn của Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi#data-storage-retention):

- **Cấp có tính phí:** Được giữ lại trong **55 ngày** (có thể định cấu hình thành 7, 14, 28 hoặc 55 ngày trong [Google AI Studio](https://aistudio.google.com/logs?hl=vi)).
- **Bậc miễn phí:** Được giữ lại trong **1 ngày**.

Để xoá một hoạt động tương tác trong nền sớm hơn, hãy [xoá hoạt động tương tác](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi#cancellation-and-deletion) sau khi truy xuất kết quả.

## Truy xuất kết quả

Nhận kết quả tương tác trong nền bằng cách sử dụng tính năng **thăm dò ý kiến** hoặc **truyền trực tuyến**.

### Mẫu thăm dò ý kiến (không chặn)

Tính năng thăm dò ý kiến sẽ kiểm tra trạng thái tương tác theo định kỳ bằng cách sử dụng các yêu cầu GET không chặn cho đến khi đạt đến trạng thái kết thúc.

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

### Mẫu hình truyền trực tuyến

Nếu sự cố mạng làm gián đoạn một luồng, thì quá trình truyền trực tuyến có thể tiếp tục từ sự kiện nhận được gần đây nhất. Mỗi delta chứa một `event_id` duy nhất trong tải trọng của nó. Việc truyền mã nhận dạng này dưới dạng `last_event_id` sẽ tiếp tục luồng từ sự kiện đó.

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

## Cuộc trò chuyện nhiều lượt

Các lượt tương tác tiếp theo có thể liên kết với một cuộc trò chuyện ở chế độ nền bằng cách sử dụng `previous_interaction_id`, tuỳ thuộc vào các quy tắc ràng buộc sau:

1. **Các lượt thực thi đang hoạt động bị chặn:** Việc liên kết một lượt tương tác tiếp theo với một lượt tương tác có trạng thái `in_progress` sẽ trả về lỗi `400 Bad Request`. Chờ cho đến khi hoạt động tương tác đạt đến trạng thái `completed` trước khi bắt đầu hoạt động tiếp theo.
2. **Tham số môi trường cho tác nhân được quản lý:** Khi liên kết các lượt tương tác cho tác nhân được quản lý (chẳng hạn như `antigravity-preview-09-2026`), các yêu cầu phải bao gồm cả `previous_interaction_id` và `environment`.

Các ví dụ sau đây cho thấy cách liên kết các hoạt động tương tác:

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

## Huỷ và xoá

Kiểm soát các lần thực thi đang chạy và quản lý bộ nhớ bằng cách sử dụng yêu cầu huỷ và xoá:

- **Cancel (`POST /interactions/{id}/cancel`):** Dừng tác vụ đang chạy. Trạng thái chuyển sang `cancelled`. Các thao tác dọn dẹp trên máy chủ có thể gây ra độ trễ nhỏ trước khi trạng thái cập nhật trong yêu cầu GET.
- **Xoá (`DELETE /interactions/{id}`):** Xoá các bản ghi tương tác khỏi máy chủ. Các yêu cầu GET tiếp theo sẽ trả về lỗi `404 Not Found`.

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

## Các bước tiếp theo

- Đọc [Tổng quan về Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) để tìm hiểu về cách quản lý phiên và trạng thái.
- Xem hướng dẫn về [Tương tác trực tuyến](https://ai.google.dev/gemini-api/docs/streaming?hl=vi) để biết thông tin chi tiết về nội dung cập nhật sự kiện theo thời gian thực.
- Khám phá [hướng dẫn bắt đầu nhanh về tác nhân được quản lý](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi) để xây dựng các tác nhân nhiều lượt có trạng thái.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-21 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-21 UTC."],[],[]]
