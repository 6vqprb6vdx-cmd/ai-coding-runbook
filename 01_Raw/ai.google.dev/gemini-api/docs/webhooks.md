---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=de
fetched_at: 2026-07-20T04:42:39.839764+00:00
title: "Webhooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Webhooks

Mit Webhooks kann die Gemini API Echtzeitbenachrichtigungen an Ihren Server senden, wenn asynchrone oder lang andauernde Vorgänge (Long-Running Operations, LROs) abgeschlossen sind. Dadurch ist es nicht mehr erforderlich, die API nach Statusaktualisierungen abzufragen, was die Latenz und den Aufwand reduziert.

Webhooks sind für Vorgänge wie [Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=de) jobs,
[Interaktionen](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) und [Videogenerierung](https://ai.google.dev/gemini-api/docs/video?hl=de) verfügbar.

## Funktionsweise

Anstatt `GET /operations` wiederholt abzufragen, um zu prüfen, ob ein Job abgeschlossen ist, können Sie Gemini API-Webhooks so konfigurieren, dass sofort nach einem Ereignistrigger eine HTTP-POST-Anfrage an Ihre Listener-URL gesendet wird.

Die Gemini API unterstützt zwei Möglichkeiten zum Konfigurieren von Webhooks:

- [**Statische Webhooks**](#static-webhooks): Endpunkte auf Projektebene, die mit der Gemini [WebhookService API](https://ai.google.dev/api?hl=de) konfiguriert wurden. Gut für globale Integrationen (z.B. Benachrichtigung von Slack, Synchronisierung einer Datenbank usw.).
- [**Dynamische Webhooks**](#dynamic-webhooks): Überschreibungen auf Anfrageebene, bei denen eine
  Webhook-URL in der Konfigurationsnutzlast eines bestimmten Jobaufrufs übergeben wird. Ideal, um bestimmte Jobs an dedizierte Endpunkte weiterzuleiten.

## Statische Webhooks

Statische Webhooks werden für ein ganzes [Projekt](https://ai.google.dev/gemini-api/docs/api-key?hl=de#google-cloud-projects) registriert und werden für jedes übereinstimmende
Ereignis ausgelöst.

### Webhook erstellen

Sie können Endpunkte mit dem SDK oder der REST API erstellen.

**WICHTIG**: Beim Erstellen eines Webhooks gibt die API
**nur einmal** ein **Signatur-Secret** zurück. Sie müssen dieses Secret sicher speichern (z.B. in Ihren Umgebungsvariablen), um Signaturen später zu überprüfen. Wenn Sie das Signatur-Secret verlieren, müssen Sie es
[rotieren](#rotate-signing-secret)

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

# Store webhook.new_signing_secret securely
webhook_secret = webhook.new_signing_secret
print(f"Created webhook: {webhook.name}, {webhook.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  // Store webhook.signingSecret securely
  const webhookSecret = webhook.new_signing_secret;
  console.log(`Created webhook: ${webhook.name}, ${webhook.id}`);
}

createWebhook();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "name": "MyBatchWebhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

Weitere Informationen zum Einrichten Ihres Servers für den Empfang von Daten finden Sie im
[Abschnitt Webhook-Anfragen verarbeiten](#handle-webhook-requests).

### Webhook abrufen

Rufen Sie Details zu einem bestimmten Webhook anhand seines Ressourcennamens ab.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.get(id="<your_webhook_id>")

print(f"Webhook: {webhook.name}")
print(f"URI: {webhook.uri}")
print(f"Events: {webhook.subscribed_events}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI(); // Assumes process.env.GEMINI_API_KEY is set

async function getWebhook() {
  const webhook = await client.webhooks.get("<your_webhook_id>");

  console.log(`Webhook: ${webhook.name}`);
  console.log(`URI: ${webhook.uri}`);
  console.log(`Events: ${webhook.subscribed_events}`);
}

getWebhook();
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Webhooks auflisten

Listen Sie alle konfigurierten Webhooks für das aktuelle Projekt auf, optional mit Paginierung.

### Python

```
from google import genai

client = genai.Client()

webhooks = client.webhooks.list()

for wh in webhooks:
    print(f"{wh.id}: {wh.name} -> {wh.uri}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function listWebhooks() {
  const webhooks = await client.webhooks.list();

  for (const wh of webhooks) {
    console.log(`${wh.id}: ${wh.name} -> ${wh.uri}`);
  }
}

listWebhooks();
```

### REST

```
curl -X GET \
  "https://generativelanguage.googleapis.com/v1/webhooks" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Webhook aktualisieren

Aktualisieren Sie die Eigenschaften eines vorhandenen Webhooks, z. B. den Anzeigenamen, die Ziel-URI oder die abonnierten Ereignisse.

### Python

```
from google import genai

client = genai.Client()

updated_webhook = client.webhooks.update(
    id="<your_webhook_id>",
    subscribed_events=["batch.succeeded", "batch.failed", "batch.cancelled"],
)

print(f"Updated webhook: {updated_webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function updateWebhook() {
  const updatedWebhook = await client.webhooks.update(
    "<your_webhook_id>",
    {
      subscribed_events: ["batch.succeeded", "batch.failed", "batch.cancelled"],
    }
  );

  console.log(`Updated webhook: ${updatedWebhook.name}`);
}

updateWebhook();
```

### REST

```
curl -X PATCH \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "subscribed_events": ["batch.succeeded", "batch.failed", "batch.cancelled"]
  }'
```

### Webhook löschen

Entfernen Sie einen Webhook-Endpunkt aus dem Projekt. Dadurch werden zukünftige Ereignisse nicht mehr an diesen Endpunkt gesendet.

### Python

```
from google import genai

client = genai.Client()

client.webhooks.delete(id="<your_webhook_id>")

print("Webhook deleted.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function deleteWebhook() {
  await client.webhooks.delete("<your_webhook_id>");

  console.log("Webhook deleted.");
}

deleteWebhook();
```

### REST

```
curl -X DELETE \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Signatur-Secret rotieren

Rotieren Sie das Signatur-Secret für einen Webhook. Sie können konfigurieren, ob zuvor aktive Secrets sofort oder nach einer Kulanzfrist von 24 Stunden widerrufen werden.

**WICHTIG**: Das neue Signatur-Secret wird **nur einmal** zum Zeitpunkt der Rotation
zurückgegeben. Speichern Sie es sicher, bevor Sie Ihre Überprüfungslogik aktualisieren.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.webhooks.rotate_signing_secret(
    id="<your_webhook_id>",
    revocation_behavior="REVOKE_PREVIOUS_SECRETS_AFTER_H24",
)

# Store response.secret securely, then update your server's verification config
print("New signing secret generated. Update your server configuration.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function rotateSigningSecret() {
  const response = await client.webhooks.rotateSigningSecret(
    "<your_webhook_id>",
    {
      revocation_behavior: "REVOKE_PREVIOUS_SECRETS_AFTER_H24",
    }
  );

  // Store response.secret securely, then update your server's verification config
  console.log("New signing secret generated. Update your server configuration.");
}

rotateSigningSecret();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks/<your_webhook_id>/rotate_secret" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "revocation_behavior": "REVOKE_PREVIOUS_SECRETS_AFTER_H24"
  }'
```

### Webhook-Anfragen auf einem Server verarbeiten

Wenn ein Ereignis eintritt, für das Sie sich angemeldet haben, empfängt Ihre Webhook-URL eine HTTP-POST-Anfrage. Ihr Endpunkt muss innerhalb weniger Sekunden mit einem 2xx-Statuscode antworten, um einen Wiederholungsversuch zu vermeiden. Um die Zustellung zu gewährleisten, wiederholt die Gemini API fehlgeschlagene Anfragen 24 Stunden lang automatisch mit exponentiellem Backoff.

Gemini folgt strikt der [Spezifikation für Standard-Webhooks](https://github.com/standard-webhooks/standard-webhooks) für
Sicherheitsheader. Überprüfen Sie die Nutzlast auf Ihrem Server mit den signierten Headersignaturen und Ihrem gespeicherten statischen Signatur-Secret. Informationen zur Nutzlast finden Sie im Abschnitt [Webhook-Umschlag](#webhook-envelope).

Hier ist ein Beispiel mit Flask für den HTTP-Listener:

### Python

```
# pip install flask standardwebhooks
import os
from flask import Flask, request, jsonify
# Standard verification wrapper for Standard Webhook Headers
from standardwebhooks.webhooks import Webhook, WebhookVerificationError

app = Flask(__name__)

SIGNING_SECRET = os.environ.get('WEBHOOK_SIGNING_SECRET')

@app.route('/gemini-callback', methods=['POST'])
def gemini_callback():
    payload = request.get_data(as_text=True)
    headers = request.headers

    try:
        wh = Webhook(SIGNING_SECRET)
        event = wh.verify(payload, headers)
    except WebhookVerificationError as e:
        return jsonify({"error": "Signature invalid"}), 400

    # Process thin payload contents
    if event.get("type") == "batch.succeeded":
        print(f"Batch completed! ID: {event['data']['id']}")
        if event["data"].get("output_file_uri"):
            # For batch jobs with input file
            print(f"Batch file: {event['data']['output_file_uri']}")
    elif event.get("type") == "interaction.completed":
        print(f"Interaction completed! ID: {event['data']['id']}")
    elif event.get("type") == "video.generated":
        print(f"Video generated! URI: {event['data']['output_file_uri']}")

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=8000)
```

### JavaScript

```
// npm install standardwebhooks
import { Webhook } from "standardwebhooks";
import express from "express";

const app = express();
const client = new GoogleGenAI({ webhookSecret: process.env.WEBHOOK_SIGNING_SECRET });

// Don't use express.json() because signature verification needs the raw text body
app.use(express.text({ type: "application/json" }));

app.post("/gemini-callback", async (req, res) => {
  const payload = await req.text();
        const headers: Record<string, string> = {};
        req.headers.forEach((value, key) => {
            headers[key] = value;
        });

        try {
            const wh = new Webhook(process.env.WEBHOOK_SIGNING_SECRET);
            const event = wh.verify(payload, headers) as Record<string, any>;
    console.log(`Event type: ${event.type}, data: ${JSON.stringify(event.data)}`);

            // Process thin payload contents
            if (event.type === "batch.succeeded") {
                console.log(`Batch completed! ID: ${event.data.id}`);
                if (event.data.output_file_uri) {
                    // For batch jobs with input file
                    console.log(`Batch file: ${event.data.output_file_uri}`);
                }
            } else if (event.type === "interaction.completed") {
                console.log(`Interaction completed! ID: ${event.data.id}`);
            } else if (event.type === "video.generated") {
                console.log(`Video generated! URI: ${event.data.output_file_uri}`);
            }

            res.status(200).json({ status: "received" });
        } catch (e) {
            console.error("Webhook verification failed:", e);
            res.status(400).send("Invalid signature");
        }
});

app.listen(8000, () => {
  console.log("Webhook server is running on port 8000");
});
```

## Dynamische Webhooks

Mit dynamischen Webhooks können Sie einen Webhook-Endpunkt an eine **bestimmte Anfrage
konfiguration** binden, was ideal für Agent-Orchestrierungs-Warteschlangen ist. Dynamische Webhooks verwenden asymmetrische JWKS-Signaturen mit öffentlichen Schlüsseln anstelle von symmetrischen Secrets.

### Dynamische Anfrage senden

Fügen Sie eine `webhook_config` hinzu, wenn Sie einen asynchronen Job auslösen (z.B. einen Batch erstellen).

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

response = client.interactions.create(
    model='gemini-3.5-flash',
    input='Tell me a short joke about programming.',
    background=True, # Required when webhook_config is specified
    webhook_config={
        'uris': ["https://my-api.com/gemini-webhook-dynamic"],
        'user_metadata': {"job_group": "nightly-eval", "priority": "high"}
    }
)

print(f"Interaction created! ID: {response.id}")
print(f"Status: {response.status}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createInteractionWithWebhook() {
  const response = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Tell me a short joke about programming.",
    background: true, // Required when webhook_config is specified
    webhook_config: {
      uris: ["https://my-api.com/gemini-webhook-dynamic"],
      user_metadata: { job_group: "nightly-eval", priority: "high" },
    },
  });

  console.log(`Interaction created! ID: ${response.id}`);
  console.log(`Status: ${response.status}`);
}

createInteractionWithWebhook();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a short joke about programming.",
    "background": true,
    "webhook_config": {
      "uris": ["https://my-api.com/gemini-webhook-dynamic"],
      "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
    }
  }'
```

### Dynamische Signaturen (JWKS) überprüfen

Dynamische Webhook-Anfragen geben eine JWT-Signatur (JSON Web Token) aus. Ihr Listener
muss die Signatur extrahieren und mit den [öffentlichen Zertifikat
Endpunkten](https://www.googleapis.com/oauth2/v3/certs) von Google überprüfen.

### Python

```
import jwt
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Google public cert list endpoint
JWKS_URI = "https://generativelanguage.googleapis.com/.well-known/jwks.json"

def load_google_public_key(kid):
    response = requests.get(JWKS_URI).json()
    for key_item in response.get('keys', []):
        if key_item.get('kid') == kid:
            # Convert JWK to Cert wrapper
            return jwt.algorithms.RSAAlgorithm.from_jwk(key_item)
    return None

@app.route('/gemini-webhook-dynamic', methods=['POST'])
def dynamic_handler():
    payload = request.get_data(as_text=True)
    headers = request.headers

    token = headers.get('Webhook-Signature')
    if not token:
        return jsonify({"error": "No signature header"}), 400

    try:
        # Extract kid from JWT header
        unverified_headers = jwt.get_unverified_header(token)
        pub_key = load_google_public_key(unverified_headers.get('kid'))

        if not pub_key:
            return jsonify({"error": "Key cert not found"}), 400

        # Verify Signature against expected audience (e.g., your project client ID)
        event = jwt.decode(
            token,
            pub_key,
            algorithms=["RS256"],
            audience="your-configured-audience"
        )
    except Exception as e:
        return jsonify({"error": "Invalid Dynamic signature", "details": str(e)}), 400

    print("Verified Dynamic payload success.")
    return jsonify({"status": "received"}), 200
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import express from "express";
import jwt from "jsonwebtoken";
import jwksClient from "jwks-rsa";

const app = express();
app.use(express.text({ type: 'application/json' }));

const client = jwksClient({
  jwksUri: "https://generativelanguage.googleapis.com/.well-known/jwks.json"
});

function getKey(header, callback) {
  client.getSigningKey(header.kid, (err, key) => {
    const signingKey = key.getPublicKey();
    callback(null, signingKey);
  });
}

app.post('/gemini-webhook-dynamic', (req, res) => {
  const token = req.headers['webhook-signature'];

  if (!token) {
    return res.status(400).json({ error: "No signature header" });
  }

  jwt.verify(
    token,
    getKey,
    {
      algorithms: ["RS256"],
      audience: "your-configured-audience"
    },
    (err, decoded) => {
      if (err) {
        return res.status(400).json({ error: "Invalid Dynamic signature", details: err.message });
      }

      console.log("Verified Dynamic payload success.");
      res.status(200).json({ status: "received" });
    }
  );
});
```

## Webhook-Umschlag

Um eine Überlastung der Bandbreite zu vermeiden, verwenden Gemini-Webhooks ein Modell mit **geringer Nutzlast** , um Daten zu liefern. Bei Zustellungen wird ein Snapshot mit Statusdetails und Verweisen auf die Ergebnisse gesendet, nicht die Rohausgabedatei selbst.

Hier ist ein Beispiel für das Nutzlastformat:

```
{
  "type": "batch.succeeded",
  "version": "v1",
  "timestamp": "2026-01-22T12:00:00Z",
  "data": {
    "id": "batch_123456",
    "output_file_uri": "gs://my-bucket/results.jsonl"
  }
}
```

## Referenz zum Ereigniskatalog

Die folgenden Ereignisse werden für unterstützende Jobs ausgelöst:

| Ereignistyp | Trigger | Nutzlastelement (`data`) |
| --- | --- | --- |
| `batch.succeeded` | Die Verarbeitung wurde erfolgreich abgeschlossen. | `id`, `output_file_uri` |
| `batch.cancelled` | Nutzer hat die Anfrage abgebrochen | `id` |
| `batch.expired` | Batch wurde nicht innerhalb von 24 Stunden verarbeitet (abgeschlossen) | `id` |
| `batch.failed` | Batchjob ist fehlgeschlagen (System- oder Validierungsfehler). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Funktionsaufruf, Nutzer muss etwas tun | `id` |
| `interaction.completed` | LRO in der Interactions API erfolgreich | `id` |
| `interaction.failed` | LRO in der Interactions API ist fehlgeschlagen (System- oder Validierungsfehler). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | LRO in der Interactions API abgebrochen | `id` |
| `video.generated` | LRO für die Videogenerierung abgeschlossen. | `id`, `output_file_uri`, `file_name` |

## Best Practices

So sorgen Sie für einen zuverlässigen und skalierbaren Betrieb:

- **Strenge Überprüfung zum Schutz vor Replay-Angriffen**: Alle Anfragen enthalten einen `webhook-timestamp`
  Header. Überprüfen Sie diesen Zeitstempel immer auf der Konfigurationsebene Ihres Servers, um Nutzlasten abzulehnen, die älter als **5 Minuten** sind (um Replay-Angriffe zu verhindern).
- **Asynchron verarbeiten**: Antworten Sie sofort mit `2xx OK`, wenn eine gültige
  Signatur erkannt wird, und stellen Sie Parsing-Vorgänge intern in die Warteschlange. Längere Wartezeiten für Listener lösen einen Wiederholungszyklus für die Zustellung aus.
- **Deduplizierung**: Standard-Webhooks liefern mindestens einmal. Verwenden Sie den einheitlichen `webhook-id`-Header, um potenzielle Duplikate bei höherer Überlastung zu verarbeiten.

## Nächste Schritte

- [Batch API](https://ai.google.dev/gemini-api/docs/batch?hl=de): Nutzen Sie Webhooks, um Endpunkte mit hohem Volumen zu automatisieren.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-06 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-06 (UTC)."],[],[]]
