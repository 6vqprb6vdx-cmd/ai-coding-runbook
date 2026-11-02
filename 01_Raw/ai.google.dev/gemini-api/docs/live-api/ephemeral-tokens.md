---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=es-419
fetched_at: 2026-11-02T07:01:08.917416+00:00
title: "Tokens ef\u00edmeros \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Tokens efímeros

Los tokens efímeros son tokens de autenticación de corta duración para acceder a la API de Gemini
a través de [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Están diseñados para mejorar la seguridad cuando
te conectas directamente desde el dispositivo de un usuario a la API (una
[implementación de cliente a servidor](https://ai.google.dev/gemini-api/docs/live?hl=es-419#implementation-approach)
). Al igual que las claves de API estándar, los tokens efímeros se pueden extraer de aplicaciones del cliente, como navegadores web o apps para dispositivos móviles. Sin embargo, debido a que los tokens efímeros vencen rápidamente y se pueden restringir, reducen significativamente los riesgos de seguridad en un entorno de producción. Debes usarlos cuando accedas a la API de Live directamente desde aplicaciones del cliente para mejorar la seguridad de la clave de API.

## Cómo funcionan los tokens efímeros

A continuación, se explica cómo funcionan los tokens efímeros en un nivel general:

1. Tu cliente (p.ej., una app web) se autentica con tu backend.
2. Tu backend solicita un token efímero al servicio de aprovisionamiento de la API de Gemini.
3. La API de Gemini emite un token de corta duración.
4. Tu backend envía el token al cliente para las conexiones WebSocket a la API de Live. Para ello, puedes intercambiar tu clave de API por un token efímero.
5. Luego, el cliente usa el token como si fuera una clave de API.

![Descripción general de los tokens efímeros](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=es-419)

Esto mejora la seguridad porque, incluso si se extrae, el token es de corta duración, a diferencia de una clave de API de larga duración implementada en el cliente. Dado que el cliente envía datos directamente a Gemini, esto también mejora la latencia y evita que tus backends necesiten proxy de los datos en tiempo real.

## Cómo crear un token efímero

Este es un ejemplo simplificado de cómo obtener un token efímero de Gemini.
De forma predeterminada, tendrás 1 minuto para iniciar sesiones nuevas de la API de Live con el token de esta solicitud (`newSessionExpireTime`) y 30 minutos para enviar mensajes a través de esa conexión (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
    },
  });
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

Para conocer las restricciones de valores, los valores predeterminados y otras especificaciones de campos de `expireTime`, consulta la
[referencia de la API](https://ai.google.dev/api/live?hl=es-419#ephemeral-auth-tokens).
Dentro del período `expireTime`, necesitarás
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=es-419#session-resumption) para
volver a conectar la llamada cada 10 minutos (esto se puede hacer con el mismo token, incluso
si `uses: 1`).

También es posible bloquear un token efímero en un conjunto de configuraciones. Esto puede ser útil para mejorar aún más la seguridad de tu aplicación y mantener las instrucciones del sistema en el servidor.

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.8-live',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.8-live',
            config: {
                sessionResumption: {},
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.8-live",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

También puedes bloquear un subconjunto de campos. Consulta la [documentación del SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
para obtener más información.

## Cómo conectarse a la API de Live con un token efímero

Una vez que tengas un token efímero, úsalo como si fuera una clave de API (pero recuerda que solo funciona para la API de Live y solo con la versión `v1beta` de la API).

El uso de tokens efímeros solo agrega valor cuando se implementan aplicaciones
que siguen el enfoque de implementación [de cliente a servidor](https://ai.google.dev/gemini-api/docs/live?hl=es-419#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Consulta [Comienza a usar la API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419) para obtener más ejemplos.

## Prácticas recomendadas

- Establece una duración de vencimiento corta con el parámetro `expire_time`.
- Los tokens vencen, lo que requiere que se vuelva a iniciar el proceso de aprovisionamiento.
- Verifica la autenticación segura para tu propio backend. Los tokens efímeros solo serán tan seguros como tu método de autenticación de backend.
- En general, evita usar tokens efímeros para las conexiones de backend a Gemini, ya que, por lo general, esta ruta se considera segura.

## Limitaciones

Por el momento, los tokens efímeros solo son compatibles con la [API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419).

## ¿Qué sigue?

- Lee la referencia de la API de Live [sobre los tokens efímeros](https://ai.google.dev/api/live?hl=es-419#ephemeral-auth-tokens)
  para obtener más información.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-17 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-17 (UTC)"],[],[]]
