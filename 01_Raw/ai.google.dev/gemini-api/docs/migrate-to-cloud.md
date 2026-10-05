---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=es-419
fetched_at: 2026-10-05T06:30:47.167051+00:00
title: "Comparaci\u00f3n entre la API de Gemini Developer y Agent Platform de Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comparación entre la API de Gemini Developer y Agent Platform de Gemini Enterprise

Cuando desarrollas soluciones de IA generativa con Gemini, Google ofrece dos productos de API: la [API de Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=es-419) y la [API de Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=es-419).

La API para desarrolladores de Gemini proporciona la ruta más rápida para compilar, llevar a producción y escalar aplicaciones potenciadas por Gemini. La mayoría de los desarrolladores deberían usar la API de Gemini Developer, a menos que necesiten controles empresariales específicos.

Gemini Enterprise Agent Platform ofrece un ecosistema integral de funciones y servicios listos para empresas para crear e implementar aplicaciones de IA generativa respaldadas por Google Cloud Platform.

Recientemente, simplificamos la migración entre estos servicios. Ahora se puede acceder a la API de Gemini Developer y a la API de Gemini Enterprise Agent Platform a través del [SDK de GenAI de Google](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) unificado y la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419).

## Comparación de código: API de Interactions (recomendada)

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) es la forma recomendada de crear soluciones con modelos y agentes de Gemini. En los siguientes ejemplos, se compara la generación de texto entre la API de Gemini Developer y Gemini Enterprise Agent Platform.

### Python

Puedes acceder a los servicios de la API de Gemini Developer y de Gemini Enterprise Agent Platform a través de la biblioteca `google-genai` (`>= 2.3.0`). Consulta la página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) para obtener instrucciones sobre cómo instalar `google-genai`.

### API de Gemini Developer

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### API de Gemini Enterprise Agent Platform

```
from google import genai

client = genai.Client(
    enterprise=True, project="your-project-id", location="global"
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### JavaScript y TypeScript

Puedes acceder a los servicios de la API de Gemini Developer y de Gemini Enterprise Agent Platform a través de la biblioteca `@google/genai` (`>= 2.3.0`). Consulta la página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) para obtener instrucciones sobre cómo instalar `@google/genai`.

### API de Gemini Developer

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### API de Gemini Enterprise Agent Platform

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  enterprise: true,
  project: "your_project",
  location: "global",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

## Comparación de código: API de generateContent

Si bien se recomienda la API de Interactions para proyectos nuevos, la API de `generateContent` sigue siendo compatible.

### Python

Puedes acceder a los servicios de la API de Gemini Developer y de Gemini Enterprise Agent Platform a través de la biblioteca de `google-genai`. Consulta la página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) para obtener instrucciones sobre cómo instalar `google-genai`.

### API de Gemini Developer

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### API de Gemini Enterprise Agent Platform

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript y TypeScript

Puedes acceder a los servicios de la API de Gemini Developer y de Gemini Enterprise Agent Platform a través de la biblioteca de `@google/genai`. Consulta la página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) para obtener instrucciones sobre cómo instalar `@google/genai`.

### API de Gemini Developer

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### API de Gemini Enterprise Agent Platform

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

Puedes acceder a los servicios de la API de Gemini Developer y de Gemini Enterprise Agent Platform a través de la biblioteca de `google.golang.org/genai`. Consulta la página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) para obtener instrucciones sobre cómo instalar `google.golang.org/genai`.

### API de Gemini Developer

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### API de Gemini Enterprise Agent Platform

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google Cloud project
const project = "your-project"

// A Google Cloud location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Otros casos de uso y plataformas

Consulta las guías específicas de casos de uso en la [documentación de la API de Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=es-419) y la [documentación de Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=es-419) para otras plataformas y casos de uso.

## Consideraciones sobre la migración

Cuando migres, ocurrirá lo siguiente:

- Deberás usar cuentas de servicio de Google Cloud para autenticarte. Consulta la [documentación de Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=es-419) para obtener más información.
- Puedes usar tu proyecto existente de Google Cloud
  (el mismo que usaste para generar tu clave de API) o puedes
  [crear un proyecto nuevo de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=es-419).
- Las regiones admitidas pueden diferir entre la API de Gemini Developer y la API de Gemini Enterprise Agent Platform. Durante la versión preliminar, la [API de Interactions en Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=es-419) solo admite el endpoint `global` (`location="global"`). Consulta la lista de [regiones compatibles con la IA generativa en Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=es-419).
- Todos los modelos que creaste en Google AI Studio deben volver a entrenarse en Gemini Enterprise Agent Platform.

Si ya no necesitas usar tu clave de la API de Gemini para la API para desarrolladores de Gemini, sigue las prácticas recomendadas de seguridad y bórrala.

Para borrar una clave de API, haz lo siguiente:

1. Abre la página [Credenciales de la API de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
2. Busca la clave de API que deseas borrar y haz clic en el ícono **Acciones**.
3. Selecciona **Borrar clave de API**.
4. En la ventana modal **Borrar credencial**, selecciona **Borrar**.

   Borrar una clave de API por completo demora algunos minutos. Una vez que finalice este proceso, el tráfico que use la clave de API borrada se rechazará.

## Próximos pasos

- Explora la guía para desarrolladores de la [API de Interactions en Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=es-419).
- Consulta la [descripción general de la IA generativa en Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=es-419) para obtener más información sobre las soluciones de IA generativa en Gemini Enterprise Agent Platform.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-30 (UTC)"],[],[]]
