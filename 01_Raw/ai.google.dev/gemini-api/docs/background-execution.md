---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=de
fetched_at: 2026-10-05T06:35:08.667300+00:00
title: "Ausf\u00fchrung im Hintergrund \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Ausführung im Hintergrund

Bei zeitaufwendigen Aufgaben wie tiefgründigen Recherchen, komplexen Schlussfolgerungen oder Agentenausführungen mit mehreren Schritten können Verbindungszeitüberschreitungen standardmäßige HTTP-Anfragen unterbrechen, die normalerweise nach 60 Sekunden geschlossen werden. Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) bietet **Hintergrundausführung**, um diese Aufgaben asynchron auszuführen.

Wenn die Interaktion so lange laufen soll, bis die Aufgabe auf dem Server abgeschlossen ist, legen Sie beim Erstellen der Interaktion `"background": true` fest. Die API gibt sofort eine Interaktions-ID zurück, mit der Clientanwendungen den Status abrufen, den Fortschritt streamen oder die Verbindung zu einem getrennten Stream wiederherstellen können.

Die Ausführung im Hintergrund wird für Standard-Gemini-Modelle (z. B. `gemini-3.8-flash` und `gemini-3.1-pro-preview`) und Verwaltete KI-Agenten (z. B. `antigravity-preview-09-2026`) unterstützt.

## Hintergrundinteraktion erstellen

Wenn Sie eine Hintergrundinteraktion starten möchten, legen Sie beim Erstellen der Ressource den Parameter `background` auf `true` fest.

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

## So funktioniert die Ausführung im Hintergrund

Wenn Sie eine Hintergrundinteraktion erstellen, wird die Aufgabe asynchron auf dem Server ausgeführt. Die Interaktion durchläuft verschiedene Ausführungsstatus:

- `in_progress`: Der Server führt die Interaktion aktiv aus, z. B. durch Ausführen von Code oder durch Recherche.
- `requires_action`: Die Interaktion wurde pausiert und wartet auf eine Eingabe des Kunden, z. B. die Bestätigung der Ausführung eines Tools oder die Beantwortung einer Frage.
- `completed`: Die Interaktion wurde erfolgreich abgeschlossen und die Ausgabe ist verfügbar.
- `failed`: Bei der Ausführung ist ein Fehler aufgetreten (z. B. ein Toolfehler oder Ratenbeschränkungen).
- `cancelled`: Die Ausführung wurde durch eine Clientanfrage beendet.

### Anwendungsfälle

Ausführung im Hintergrund verwenden für:

- **Agent-Ausführungen**:Aufgaben, für die Codeausführung, Websuche oder die Orchestrierung von untergeordneten Agenten (z. B. `antigravity-preview-09-2026`) erforderlich ist.
- **Deep Research**:Läufe mit `deep-research-preview-04-2026` oder `deep-research-max-preview-04-2026`, die mehrere Minuten dauern.
- **Lange Begründung**:Aufgaben, bei denen die Denkprozesse des Modells die Standardlimits für HTTP-Verbindungen überschreiten.

## Ergebnisse abrufen

Ergebnisse von Hintergrundinteraktionen können entweder durch **Polling** oder **Streaming** abgerufen werden.

### Polling-Muster (nicht blockierend)

Beim Polling wird der Interaktionsstatus regelmäßig mithilfe von nicht blockierenden GET-Anfragen geprüft, bis ein Endstatus erreicht ist.

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

### Streamingmuster

Wenn ein Stream aufgrund einer Netzwerkunterbrechung getrennt wird, kann das Streaming ab dem letzten empfangenen Ereignis fortgesetzt werden. Jedes Delta enthält eine eindeutige `event_id` in seiner Nutzlast. Wenn Sie diese ID als `last_event_id` übergeben, wird der Stream ab diesem Ereignis fortgesetzt.

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

## Unterhaltungen über mehrere Themen

Nachfolgende Interaktionen können mit `previous_interaction_id` an eine Hintergrundunterhaltung angehängt werden. Dabei gelten die folgenden Einschränkungen:

1. **Aktive Ausführungen werden blockiert**:Wenn Sie eine nachfolgende Interaktion mit dem Status `in_progress` verketten, wird ein `400 Bad Request`-Fehler zurückgegeben. Warten Sie, bis die Interaktion den Status `completed` erreicht hat, bevor Sie die nächste starten.
2. **Umgebungsparameter für verwaltete KI-Agenten**:Wenn Sie Interaktionen für verwaltete KI-Agenten verketten (z. B. `antigravity-preview-09-2026`), müssen Anfragen sowohl `previous_interaction_id` als auch `environment` enthalten.

Die folgenden Beispiele zeigen, wie Sie Interaktionen verketten:

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

## Kündigung und Löschung

Laufende Ausführungen steuern und Speicher mit Abbrechen- und Löschanfragen verwalten:

- **Abbrechen (`POST /interactions/{id}/cancel`)**: Die laufende Aufgabe wird beendet. Der Status ändert sich in `cancelled`. Bereinigungsaktionen auf dem Server können zu einer leichten Verzögerung führen, bevor die Status in GET-Anfragen aktualisiert werden.
- **Löschen (`DELETE /interactions/{id}`)**: Entfernt die Interaktionsdatensätze vom Server. Nachfolgende GET-Anfragen geben den Fehler `404 Not Found` zurück.

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

## Nächste Schritte

- Lesen Sie die [Übersicht über die Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de), um mehr über die Sitzungs- und Statusverwaltung zu erfahren.
- Weitere Informationen zu Echtzeit-Event-Updates finden Sie im Leitfaden [Streaming-Interaktionen](https://ai.google.dev/gemini-api/docs/streaming?hl=de).
- In der [Kurzanleitung für verwaltete Agents](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de) erfahren Sie, wie Sie zustandsorientierte Mehrfachdialog-Agents erstellen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-24 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-24 (UTC)."],[],[]]
