---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=es-419
fetched_at: 2026-07-20T04:41:15.835127+00:00
title: "Comprender y contar tokens \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comprender y contar tokens

Gemini y otros modelos de IA generativa procesan la entrada y la salida con una granularidad llamada *token*.

**En el caso de los modelos de Gemini, un token equivale a alrededor de 4 caracteres.
100 tokens equivalen a entre 60 y 80 palabras en inglés.**

## Acerca de los tokens

Los tokens pueden ser caracteres únicos, como `z`, o palabras completas, como `cat`. Las palabras largas se dividen en varios tokens. El conjunto de todos los tokens que usa el modelo se denomina vocabulario, y el proceso de dividir el texto en tokens se denomina *tokenización*.

Cuando la facturación está habilitada, el [costo de una llamada a la API de Gemini](https://ai.google.dev/pricing?hl=es-419) se determina, en parte, por la cantidad de tokens de entrada y salida, por lo que saber cómo contarlos puede ser útil.

Puedes probar a contar tokens en nuestro Colab.

|  |  |  |
| --- | --- | --- |
| [Ver en ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | [Probar un notebook de Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=es-419) | [Ver el notebook en GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=es-419) |

## Cuenta tokens

Todas las entradas y salidas de la API de Gemini se tokenizan, incluidos los archivos de texto, imagen y otras modalidades que no son de texto.

Puedes contar tokens de las siguientes maneras:

- **Llama a [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=es-419) con la entrada de la solicitud.**  
   Devuelve la cantidad total de tokens en *solo la entrada*. Puedes hacer esta llamada antes de enviar la entrada al modelo para verificar el tamaño de tus solicitudes.
- **Usa el atributo `usage_metadata` en el objeto `response` después de llamar a `generate_content`.**  
   Esto devuelve la cantidad total de tokens en *la entrada y la salida*: `total_token_count`.  
   También devuelve los recuentos de tokens de entrada y salida por separado: `prompt_token_count` (tokens de entrada) y `candidates_token_count` (tokens de salida).

  Si usas un [modelo de pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419), los tokens que se usan durante el proceso de pensamiento se devuelven en `thoughts_token_count`. Además, si usas el [almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419), el recuento de tokens almacenados en caché estará en `cached_content_token_count`.

### Cómo contar tokens de texto

Si llamas a `count_tokens` con una entrada solo de texto, se devuelve el recuento de tokens del texto *solo en la entrada* (`total_tokens`). Puedes realizar esta llamada antes de llamar a `generate_content` para verificar el tamaño de tus solicitudes.

Otra opción es llamar a `generate_content` y, luego, usar el atributo `usage_metadata` en el objeto `response` para obtener lo siguiente:

- Las cantidades de tokens independientes de la entrada (`prompt_token_count`), el contenido almacenado en caché (`cached_content_token_count`) y la salida (`candidates_token_count`)
- Recuento de tokens para el proceso de pensamiento (`thoughts_token_count`)
- La cantidad total de tokens en *la entrada y la salida*
  (`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3.5-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=prompt
)

print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.5-flash",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: prompt,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

// Convert prompt to a slice of *genai.Content using the helper.
contents := []*genai.Content{
  genai.NewContentFromText(prompt, genai.RoleUser),
}
countResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
    ```
```

### Cómo contar tokens de varios turnos (chat)

Si llamas a `count_tokens` con el historial de chat, se muestra el recuento total de tokens del texto de cada rol en el chat (`total_tokens`).

Otra opción es llamar a `send_message` y, luego, usar el atributo `usage_metadata` en el objeto `response` para obtener lo siguiente:

- Las cantidades de tokens independientes de la entrada (`prompt_token_count`), el contenido almacenado en caché (`cached_content_token_count`) y la salida (`candidates_token_count`)
- Recuento de tokens para el proceso de pensamiento (`thoughts_token_count`)
- La cantidad total de tokens en *la entrada y la salida*
  (`total_token_count`)

Para comprender qué tan grande será tu próximo turno de conversación, debes agregarlo al historial cuando llames a `count_tokens`.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=chat.get_history()
    )
)

response = chat.send_message(
    message="In one sentence, explain how a computer works to a young child."
)
print(response.usage_metadata)

extra = types.UserContent(
    parts=[
        types.Part(
            text="What is the meaning of life?",
        )
    ]
)
history = [*chat.get_history(), extra]
print(client.models.count_tokens(model="gemini-3.5-flash", contents=history))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    { role: "user", parts: [{ text: "Hi my name is Bob" }] },
    { role: "model", parts: [{ text: "Hi Bob!" }] },
  ];
  const chat = ai.chats.create({
    model: "gemini-3.5-flash",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.5-flash",
    contents: chat.getHistory(),
  });
  console.log(countTokensResponse.totalTokens);

  const chatResponse = await chat.sendMessage({
    message: "In one sentence, explain how a computer works to a young child.",
  });
  console.log(chatResponse.usageMetadata);

  const extraMessage = {
    role: "user",
    parts: [{ text: "What is the meaning of life?" }],
  };
  const combinedHistory = [...chat.getHistory(), extraMessage];
  const combinedCountTokensResponse = await ai.models.countTokens({
    model: "gemini-3.5-flash",
    contents: combinedHistory,
  });
  console.log(
    "Combined history token count:",
    combinedCountTokensResponse.totalTokens,
  );
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

history := []*genai.Content{
  {Role: genai.RoleUser, Parts: []*genai.Part({Text: "Hi my name is Bob"})},
  {Role: genai.RoleModel, Parts: []*genai.Part({Text: "Hi Bob!"})},
}
chat, err := client.Chats.Create(ctx, "gemini-3.5-flash", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", chat.History(false), nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(firstTokenResp.TotalTokens)

resp, err := chat.SendMessage(ctx, genai.NewPartFromText("In one sentence, explain how a computer works to a young child."))
if err != nil {
  log.Fatal(err)
}
fmt.Printf("%#v\n", resp.UsageMetadata)

extra := genai.NewContentFromText("What is the meaning of life?", genai.RoleUser)
hist := chat.History(false)
hist = append(hist, extra)

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### Cómo contar tokens multimodales

Todas las entradas a la API de Gemini se tokenizan, incluidos el texto, los archivos de imágenes y otras modalidades que no son de texto. Ten en cuenta los siguientes puntos clave generales sobre la tokenización de la entrada multimodal durante el procesamiento de la API de Gemini:

- Las entradas de imágenes con ambas dimensiones menores o iguales a 384 píxeles se cuentan como 258 tokens. Las imágenes más grandes en una o ambas dimensiones se recortan y se ajustan según sea necesario en mosaicos de 768 × 768 píxeles, y cada uno se cuenta como 258 tokens.
- Los archivos de audio y video se convierten en tokens a las siguientes tasas fijas: video a 263 tokens por segundo y audio a 32 tokens por segundo.

#### Resoluciones de contenido multimedia

Los [modelos de Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-3) introducen un control detallado sobre el procesamiento de visión multimodal con el parámetro `media_resolution`. El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.**
Las resoluciones más altas mejoran la capacidad del modelo para leer texto pequeño o identificar detalles, pero aumentan el uso de tokens y la latencia.

Para obtener más detalles sobre el parámetro y cómo puede afectar los cálculos de tokens, consulta la guía de [resolución de medios](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=es-419).

#### Archivos de imagen

Si llamas a `count_tokens` con una entrada de texto y una imagen, se devuelve el recuento combinado de tokens del texto y la imagen *solo en la entrada* (`total_tokens`). Puedes realizar esta llamada antes de llamar a `generate_content` para verificar el tamaño de tus solicitudes. También puedes llamar a `count_tokens` en el texto y el archivo por separado.

Otra opción es llamar a `generate_content` y, luego, usar el atributo `usage_metadata` en el objeto `response` para obtener lo siguiente:

- Las cantidades de tokens independientes de la entrada (`prompt_token_count`), el contenido almacenado en caché (`cached_content_token_count`) y la salida (`candidates_token_count`)
- Recuento de tokens para el proceso de pensamiento (`thoughts_token_count`)
- La cantidad total de tokens en *la entrada y la salida*
  (`total_token_count`)

Ejemplo que usa una imagen subida desde la API de File:

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this image";

async function main() {
  const organ = await ai.files.upload({
    file: path.join(media, "organ.jpg"),
    config: { mimeType: "image/jpeg" },
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx, 
  filepath.Join(getMedia(), "organ.jpg"), 
  &genai.UploadFileConfig{
    MIMEType : "image/jpeg",
  },
)
if err != nil {
  log.Fatal(err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image"),
  genai.NewPartFromURI(file.URI, file.MIMEType),
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

Ejemplo que proporciona la imagen como datos intercalados:

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this image";
const imageBuffer = fs.readFileSync(path.join(media, "organ.jpg"));

const imageBase64 = imageBuffer.toString("base64");

const contents = createUserContent([
  prompt,
  createPartFromBase64(imageBase64, "image/jpeg"),
]);

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.5-flash",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: contents,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

imageBytes, err := os.ReadFile("organ.jpg")
if err != nil {
    log.Fatalf("Failed to read image file: %v", err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image"),
  {
        InlineData: &genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imageBytes,
        },
  },
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### Archivos de audio o video

El audio y el video se convierten en tokens a las siguientes tasas fijas:

- Video: 263 tokens por segundo
- Audio: 32 tokens por segundo

Si llamas a `count_tokens` con una entrada de texto y video o audio, se devuelve el recuento combinado de tokens del texto y el archivo de video o audio *solo en la entrada* (`total_tokens`). Puedes realizar esta llamada antes de llamar a `generate_content` para verificar el tamaño de tus solicitudes. También puedes llamar a `count_tokens` en el texto y el archivo por separado de forma opcional.

Otra opción es llamar a `generate_content` y, luego, usar el atributo `usage_metadata` en el objeto `response` para obtener lo siguiente:

- Las cantidades de tokens independientes de la entrada (`prompt_token_count`), el contenido almacenado en caché (`cached_content_token_count`) y la salida (`candidates_token_count`)
- Recuento de tokens para el proceso de pensamiento (`thoughts_token_count`)
- Es la cantidad total de tokens en *la entrada y la salida* (`total_token_count`).

### Python

```
from google import genai
import time

client = genai.Client()
prompt = "Tell me about this video"
your_file = client.files.upload(file=media / "Big_Buck_Bunny.mp4")

while not your_file.state or your_file.state.name != "ACTIVE":
    print("Processing video...")
    print("File state:", your_file.state)
    time.sleep(5)
    your_file = client.files.get(name=your_file.name)

print(
    client.models.count_tokens(
        model="gemini-3.5-flash", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[prompt, your_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this video";

async function main() {
  let videoFile = await ai.files.upload({
    file: path.join(media, "Big_Buck_Bunny.mp4"),
    config: { mimeType: "video/mp4" },
  });

  while (!videoFile.state || videoFile.state.toString() !== "ACTIVE") {
    console.log("Processing video...");
    console.log("File state: ", videoFile.state);
    await sleep(5000);
    videoFile = await ai.files.get({ name: videoFile.name });
  }

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx,
  filepath.Join(getMedia(), "Big_Buck_Bunny.mp4"),
  &genai.UploadFileConfig{
    MIMEType : "video/mp4",
  },
)
if err != nil {
  log.Fatal(err)
}

for file.State == genai.FileStateUnspecified || file.State != genai.FileStateActive {
  fmt.Println("Processing video...")
  fmt.Println("File state:", file.State)
  time.Sleep(5 * time.Second)

  file, err = client.Files.Get(ctx, file.Name, nil)
  if err != nil {
    log.Fatal(err)
  }
}

parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this video"),
  genai.NewPartFromURI(file.URI, file.MIMEType),
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

### Cómo contar tokens de pensamiento

Cuando activas el razonamiento, el precio de la respuesta es la suma de los tokens de salida y los tokens de razonamiento. Puedes recuperar la cantidad total de tokens de pensamiento generados desde el campo `thoughtsTokenCount` (o su equivalente en el SDK).

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Los modelos de pensamiento generan pensamientos completos para mejorar la calidad de la respuesta final y, luego, generan [resúmenes](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419#summaries) para proporcionar información sobre el proceso de pensamiento. Por lo tanto, la API basa los precios en los tokens de pensamiento completos que genera el modelo para crear un resumen, aunque la API solo genere el resumen.

Puedes obtener más información para configurar el pensamiento en la guía [Pensamiento de Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).

## Ventanas de contexto

Los modelos disponibles a través de la API de Gemini tienen ventanas de contexto que se miden en tokens. La ventana de contexto define la cantidad de entrada que puedes proporcionar y la cantidad de salida que puede generar el modelo. Puedes determinar el tamaño de la ventana de contexto llamando al [extremo `models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=es-419) o consultando la [documentación de los modelos](https://ai.google.dev/gemini-api/docs/models?hl=es-419).

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3.5-flash")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3.5-flash'});
  console.log(modelInfo.inputTokenLimit);
  console.log(modelInfo.outputTokenLimit);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
  log.Fatal(err)
}
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3.5-flash")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-24 (UTC)"],[],[]]
