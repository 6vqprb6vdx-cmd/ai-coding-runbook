---
source_url: https://ai.google.dev/gemini-api/docs/webhooks?hl=es-419
fetched_at: 2026-05-11T12:41:44.024172+00:00
title: "Webhooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Webhooks

Los webhooks permiten que la API de Gemini envíe notificaciones en tiempo real a tu servidor cuando se completan las operaciones asíncronas o de larga duración (LRO). Esto reemplaza la necesidad de sondear la API para obtener actualizaciones de estado, lo que reduce la latencia y la sobrecarga.

Los webhooks están disponibles para operaciones como [trabajos por lotes](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419),
[interacciones](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419) y [generación de video](https://ai.google.dev/gemini-api/docs/video?hl=es-419).

## Cómo funciona

En lugar de sondear `GET /operations` de forma repetida para verificar si se completó un trabajo, puedes configurar los webhooks de la API de Gemini para enviar una solicitud HTTP POST a la URL del objeto de escucha inmediatamente después de que se active un evento.

La API de Gemini admite dos formas de configurar webhooks:

- [**Webhooks estáticos**](#static-webhooks): Son extremos a nivel del proyecto configurados
  con la API de Gemini [WebhookService](https://ai.google.dev/api?hl=es-419). Son adecuados para integraciones globales (p. ej., notificar a Slack, sincronizar una base de datos, etcétera).
- [**Webhooks dinámicos**](#dynamic-webhooks): Son anulaciones a nivel de la solicitud que pasan una
  URL de webhook en la carga útil de configuración de una llamada de trabajos específica. Son ideales para enrutar trabajos específicos a extremos dedicados.

## Webhooks estáticos

Los webhooks estáticos se registran para todo un [proyecto](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#google-cloud-projects) y se activan para cualquier evento
coincidente.

### Crea un webhook

Puedes crear extremos con el SDK o la API de REST.

**IMPORTANTE**: Cuando se crea un webhook, la API muestra un **secreto de firma**
**solo una vez**. Debes almacenarlo de forma segura (p.ej., en tus variables de entorno) para verificar las firmas más adelante. Si pierdes el secreto de firma, deberás
[rotarlo](#rotate-signing-secret).

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

Para obtener detalles sobre cómo configurar tu servidor para recibir datos, consulta la
[sección Controla solicitudes de webhook](#handle-webhook-requests).

### Obtén un webhook

Recupera detalles sobre un webhook específico por su nombre de recurso.

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

### Enumera webhooks

Enumera todos los webhooks configurados para el proyecto actual, con paginación opcional.

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

### Actualiza un webhook

Actualiza las propiedades de un webhook existente, como el nombre visible, el URI de destino o los eventos suscritos.

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

### Borra un webhook

Quita un extremo de webhook del proyecto. De este modo, se detienen las entregas de eventos futuros a ese extremo.

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

### Rota un secreto de firma

Rota el secreto de firma de un webhook. Puedes configurar si los secretos activos anteriormente se revocan de inmediato o después de un período de gracia de 24 horas.

**IMPORTANTE**: El nuevo secreto de firma se muestra **solo una vez** en el momento de la rotación. Almacénalo de forma segura antes de actualizar tu lógica de verificación.

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

### Controla solicitudes de webhook en un servidor

Cuando ocurre un evento al que te suscribiste, la URL de tu webhook recibirá una solicitud HTTP POST. Tu extremo debe responder con un código de estado 2xx en unos segundos para evitar un reintento. Para garantizar la entrega, la API de Gemini vuelve a intentar automáticamente las solicitudes fallidas durante 24 horas con una retirada exponencial.

Gemini sigue estrictamente la especificación de [webhooks estándar](https://github.com/standard-webhooks/standard-webhooks) para los
encabezados de seguridad. Verifica la carga útil en tu servidor con las firmas de encabezado firmadas y tu secreto de firma estático almacenado. Consulta la sección [Sobre de webhook](#webhook-envelope) para obtener información sobre la carga útil.

Este es un ejemplo con Flask para el objeto de escucha HTTP:

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
        print(f"Batch completed! ID: {event["data"]["id"]}")
        if event["data"].get("output_file_uri"):
            # For batch jobs with input file
            print(f"Batch file: {event["data"]["output_file_uri"]}")
    elif (event.type == "video.generated"):
        print(f"Video generated! URI: {event["data"]["output_file_uri"]}")

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

## Webhooks dinámicos

Los webhooks dinámicos te permiten vincular un extremo de webhook a una **configuración de solicitud
específica**, ideal para colas de orquestación de agentes. Los webhooks dinámicos aprovechan las firmas JWKS de clave pública asimétrica en lugar de secretos simétricos.

### Envía una solicitud dinámica

Agrega un `webhook_config` cuando actives un trabajo asíncrono (p.ej., crear un lote).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

file_batch_job = client.batches.create(
    model="gemini-3-flash-preview",
    src="files/uploaded_file_id",
    config={
        "display_name": "My Setup",
        "webhook_config": {
            "uris": ["https://my-api.com/gemini-webhook-dynamic"],
            "user_metadata":{"job_group": "nightly-eval", "priority": "high"}
        }
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createBatchWithWebhook() {
  const fileBatchJob = await client.batches.create({
    model: "gemini-3-flash-preview",
    src: "files/uploaded_file_id",
    config: {
      displayName: "My Setup",
      webhookConfig: {
        uris: ["https://my-api.com/gemini-webhook-dynamic"],
        user_metadata: {"job_group": "nightly-eval", "priority": "high"}
      },
    },
  });
}
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview:batchCreate" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "src": "files/uploaded_file_id",
    "config": {
      "display_name": "My Setup",
      "webhook_config": {
        "uris": ["https://my-api.com/gemini-webhook-dynamic"],
        "user_metadata": {"job_group": "nightly-eval", "priority": "high"}
      }
    }
  }'
```

### Verifica firmas dinámicas (JWKS)

Las solicitudes de webhook dinámicas emiten una firma de token web JSON (JWT). Tu objeto de escucha
debe extraer la firma y verificarla con los extremos de certificado público de [Google](https://www.googleapis.com/oauth2/v3/certs).

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

## Sobre de webhook

Para evitar la congestión del ancho de banda, los webhooks de Gemini usan un modelo de **carga útil delgada** para entregar datos. Las entregas envían una instantánea que contiene detalles de estado y punteros a los resultados, en lugar del archivo de salida sin procesar.

Este es un ejemplo del formato de carga útil:

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

## Referencia del catálogo de eventos

Los siguientes eventos se activan para trabajos compatibles:

| Tipo de evento | Activador | Elemento de carga útil (`data`) |
| --- | --- | --- |
| `batch.succeeded` | El procesamiento finalizó correctamente. | `id`, `output_file_uri` |
| `batch.cancelled` | El usuario canceló la solicitud | `id` |
| `batch.expired` | El lote no se procesó (finalizó) en un período de 24 horas | `id` |
| `batch.failed` | No se pudo realizar el trabajo por lotes (error del sistema o de validación). | `id`, `error_code`, `error_message` |
| `interaction.requires_action` | Llamada a función, el usuario debe hacer algo | `id` |
| `interaction.completed` | Se completó la LRO en la API de Interactions | `id` |
| `interaction.failed` | No se pudo realizar la LRO en la API de Interactions (error del sistema o de validación). | `id`, `error_code`, `error_message` |
| `interaction.cancelled` | Se canceló la LRO en la API de Interactions | `id` |
| `video.generated` | Se completó la LRO de generación de video. | `id`, `output_file_uri`, `file_name` |

## Prácticas recomendadas

Para garantizar una operación confiable y escalable, haz lo siguiente:

- **Verificación estricta de protección de reproducción**: Todas las solicitudes tienen un `webhook-timestamp`
  encabezado. Siempre valida esta marca de tiempo en la capa de configuración del servidor para rechazar cargas útiles de más de **5 minutos** (para mitigar los ataques de reproducción).
- **Procesa de forma asíncrona**: Responde con `2xx OK` inmediatamente después de la detección de una firma válida
  y pon en cola las operaciones de análisis de forma interna. Los tiempos de espera prolongados del objeto de escucha activarán un ciclo de reintento de entrega.
- **Control de deduplicación**: Los webhooks estándar entregan "al menos una vez". Usa el encabezado `webhook-id` coherente para controlar posibles duplicados en flujos de mayor congestión.

## Próximos pasos

- [API de Batch](https://ai.google.dev/gemini-api/docs/batch?hl=es-419): Utiliza webhooks para automatizar extremos de gran volumen.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-08 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-08 (UTC)"],[],[]]
