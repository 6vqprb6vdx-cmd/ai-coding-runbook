---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=es-419
fetched_at: 2026-11-02T07:30:59.220012+00:00
title: "Comprender y contar tokens \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

Enviar comentarios

# Comprender y contar tokens

Gemini y otros modelos de IA generativa procesan la entrada y la salida con una granularidad llamada *token*.

**En el caso de los modelos de Gemini, un token equivale a aproximadamente 4 caracteres.
100 tokens equivalen a aproximadamente 60 a 80 palabras en inglés.**

## Acerca de los tokens

Los tokens pueden ser caracteres únicos, como `z`, o palabras completas, como `cat`. Las palabras largas se dividen en varios tokens. El conjunto de todos los tokens que usa el modelo se denomina vocabulario, y el proceso de dividir el texto en tokens se denomina *tokenización*.

Cuando la facturación está habilitada, el [costo de una llamada a la API de Gemini](https://ai.google.dev/pricing?hl=es-419) se
determina, en parte, por la cantidad de tokens de entrada y salida, por lo que puede ser útil saber cómo
contarlos.

Puedes probar el recuento de tokens en nuestro Colab.

|  |  |  |
| --- | --- | --- |
| [Ver en ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | [Probar un notebook de Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=es-419) | [Ver el notebook en GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=es-419) |

## Cuenta tokens

Toda la entrada y la salida de la API de Gemini se tokenizan, incluido el texto, los archivos de imagen y otras modalidades que no son de texto.

Puedes contar tokens de las siguientes maneras:

- **Llama a [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=es-419) con la entrada
  de la solicitud.**  
   Esto devuelve la cantidad total de tokens *solo en la entrada*. Puedes realizar esta llamada antes de enviar la entrada al modelo para verificar el tamaño de tus solicitudes.
- **Usa el atributo `usage_metadata` en el objeto `response` después de
  llamar a `generate_content`.**  
   Esto devuelve la cantidad total de
  tokens *tanto en la entrada como en la salida*: `total_token_count`.  
   También devuelve los recuentos de tokens de la entrada y la salida por separado: `prompt_token_count` (tokens de entrada) y `candidates_token_count` (tokens de salida).

  Si usas un modelo de [razonamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419), los tokens que se usan durante el proceso de razonamiento
  se muestran en `thoughts_token_count`. Y si usas el
  [almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419), el recuento de tokens
  almacenados en caché estará en `cached_content_token_count`.

### Cuenta tokens de texto

Si llamas a `count_tokens` con una entrada solo de texto, se muestra el recuento de tokens del texto en *la entrada solamente* (`total_tokens`). Puedes realizar esta llamada antes de llamar a `generate_content` para verificar el tamaño de tus solicitudes.

Otra opción es llamar a `generate_content` y, luego, usar el atributo `usage_metadata` en el objeto `response` para obtener lo siguiente:

- Los recuentos de tokens separados de la entrada (`prompt_token_count`), el contenido almacenado en caché (`cached_content_token_count`) y la salida (`candidates_token_count`)
- El recuento de tokens para el proceso de razonamiento (`thoughts_token_count`)
- La cantidad total de tokens *tanto en la entrada como en la salida* (`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=prompt
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
    model: "gemini-3.8-flash",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
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
countResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
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

### Cuenta tokens de varios turnos (chat)

Si llamas a `count_tokens` con el historial de chat, se muestra el recuento total de tokens del texto de cada rol en el chat (`total_tokens`).

Otra opción es llamar a `send_message` y, luego, usar el atributo `usage_metadata` en el objeto `response` para obtener lo siguiente:

- Los recuentos de tokens separados de la entrada (`prompt_token_count`), el contenido almacenado en caché (`cached_content_token_count`) y la salida (`candidates_token_count`)
- El recuento de tokens para el proceso de razonamiento (`thoughts_token_count`)
- La cantidad total de tokens *tanto en la entrada como en la salida* (`total_token_count`)

Para comprender el tamaño de tu próximo turno conversacional, debes agregarlo al historial cuando llames a `count_tokens`.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.8-flash",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=chat.get_history()
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
print(client.models.count_tokens(model="gemini-3.8-flash", contents=history))
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
    model: "gemini-3.8-flash",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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
chat, err := client.Chats.Create(ctx, "gemini-3.8-flash", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", chat.History(false), nil)
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

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### Cuenta tokens multimodales

Toda la entrada a la API de Gemini se tokeniza, incluido el texto, los archivos de imagen y otras modalidades que no son de texto. Ten en cuenta los siguientes puntos clave de alto nivel sobre la tokenización de la entrada multimodal durante el procesamiento de la API de Gemini:

- Las entradas de imágenes con ambas dimensiones <=384 píxeles se cuentan como 258 tokens. Las imágenes más grandes en una o ambas dimensiones se cortan y se ajustan según sea necesario en mosaicos de 768 x 768 píxeles, cada uno contado como 258 tokens.
- Los archivos de audio y video se convierten en tokens a las siguientes tasas fijas: video a 263 tokens por segundo y audio a 32 tokens por segundo. Esta tasa se aplica al procesamiento estático (predeterminado). Para el procesamiento mediante agentes, el uso de tokens varía. Consulta [Uso de tokens de video por modo de procesamiento](#video-token-usage).

#### Resoluciones de contenido multimedia

[Los modelos de Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=es-419#gemini-3) introducen un control detallado sobre el
procesamiento de visión multimodal con el `media_resolution` parámetro. El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.**
Las resoluciones más altas mejoran la capacidad del modelo para leer texto fino o identificar detalles pequeños, pero aumentan el uso de tokens y la latencia.

Para obtener más detalles sobre el parámetro y cómo puede afectar los cálculos de tokens,
consulta la [guía de resolución de contenido multimedia](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=es-419).

#### Archivos de imagen

Si llamas a `count_tokens` con una entrada de texto e imagen, se muestra el recuento de tokens combinado del texto y la imagen en *la entrada solamente* (`total_tokens`). Puedes realizar esta llamada antes de llamar a `generate_content` para verificar el tamaño de tus solicitudes. También puedes llamar a `count_tokens` de forma opcional en el texto y el archivo por separado.

Otra opción es llamar a `generate_content` y, luego, usar el atributo `usage_metadata` en el objeto `response` para obtener lo siguiente:

- Los recuentos de tokens separados de la entrada (`prompt_token_count`), el contenido almacenado en caché (`cached_content_token_count`) y la salida (`candidates_token_count`)
- El recuento de tokens para el proceso de razonamiento (`thoughts_token_count`)
- La cantidad total de tokens *tanto en la entrada como en la salida* (`total_token_count`)

Ejemplo que usa una imagen subida desde la API de File:

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.8-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
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
        model="gemini-3.8-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.8-flash",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
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

Si llamas a `count_tokens` con una entrada de texto y video o audio, se muestra el recuento de tokens combinado del texto y el archivo de video o audio en *la entrada solamente* (`total_tokens`). Puedes realizar esta llamada antes de llamar a `generate_content` para verificar el tamaño de tus solicitudes. También puedes llamar a `count_tokens` de forma opcional en el texto y el archivo por separado.

Otra opción es llamar a `generate_content` y, luego, usar el atributo `usage_metadata` en el objeto `response` para obtener lo siguiente:

- Los recuentos de tokens separados de la entrada (`prompt_token_count`), el contenido almacenado en caché (`cached_content_token_count`) y la salida (`candidates_token_count`)
- El recuento de tokens para el proceso de razonamiento (`thoughts_token_count`)
- La cantidad total de tokens *tanto en la entrada como en la salida* (`total_token_count`).

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
        model="gemini-3.8-flash", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[prompt, your_file]
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
    model: "gemini-3.8-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.8-flash",
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### Uso de tokens de video por modo de procesamiento

El uso de tokens para video depende del modo de procesamiento:

| **Modo de procesamiento** | **Cálculo de tokens** | **Uso común** |
| --- | --- | --- |
| **Estático** (predeterminado) | ~100 tokens/segundo de forma predeterminada (baja resolución) o ~300 tokens/segundo (alta resolución). Todos los fotogramas se muestrean a 1 FPS. | Predecible, proporcional a la duración del video. |
| **Agentes** | Varía según la complejidad del contenido. El modelo carga solo la transcripción o los fotogramas o el audio necesarios para responder la instrucción. | Hasta un 88% menos de tokens para contenido de larga duración. |

Con el procesamiento mediante agentes, una conferencia de 1 hora que usaría ~1.08 millones de tokens en modo estático podría usar ~108,000 tokens, según la instrucción y el contenido.

Para verificar el uso real de tokens de una solicitud, usa el campo `usage_metadata` en la respuesta. En `UsageMetadata`, los tokens de video de agentes se informan en los siguientes campos:

- **Instrucción inicial** (referencia de video + instrucción del usuario): `prompt_token_count`
- **Razonamiento de navegación**: `thoughts_token_count`
- **Transcripción, fotogramas y audio cargados a pedido**: `tool_use_prompt_token_count`
- **Respuesta final**: `candidates_token_count`

### Cuenta tokens de razonamiento

Cuando activas el razonamiento, el precio de la respuesta es la suma de los tokens de salida y los tokens de razonamiento. Puedes recuperar la cantidad total de tokens de razonamiento generados del campo `thoughtsTokenCount` (o su equivalente en el SDK).

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

Los modelos de razonamiento generan razonamientos completos para mejorar la calidad de la respuesta final y, luego, generan [resúmenes](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419#summaries) para proporcionar información sobre el proceso de razonamiento. Por lo tanto, la API basa los precios en los tokens de razonamiento completos que genera el modelo para crear un resumen, aunque la API solo genera el resumen.

Puedes obtener más información para configurar el razonamiento en la [guía de razonamiento de Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419).

## Ventanas de contexto

Los modelos disponibles a través de la API de Gemini tienen ventanas de contexto que se miden en tokens. La ventana de contexto define cuánta entrada puedes proporcionar y cuánta salida puede generar el modelo. Puedes determinar el tamaño de la
ventana de contexto llamando al extremo [`models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=es-419)
o consultando la [documentación de los modelos](https://ai.google.dev/gemini-api/docs/models?hl=es-419).

- **Modelos de Gemini 4 (`gemini-4-argon`):** Comparten una sola ventana de contexto de 1 millón de tokens (`1,048,576` tokens) en los tokens de entrada, razonamiento y salida. Las solicitudes únicas tienen un límite de `65,536` tokens de salida para la transmisión (`streamGenerateContent`) y `32,768` tokens de salida para la no transmisión (`generateContent`), o puedes generar hasta `1,048,576` tokens con la [decodificación larga](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=es-419). Si tus tokens de entrada más `max_output_tokens` superan los 1,048,576 tokens, la API limita automáticamente el límite de salida al espacio restante en la ventana de contexto (`1,048,576` menos tus tokens de entrada).
- **Modelos de Gemini 3 y 2.5:** Usan presupuestos de entrada (`1,048,576` tokens) y salida (`65,536` tokens) separados.

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3.8-flash")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3.8-flash'});
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
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3.8-flash")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-13 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-13 (UTC)"],[],[]]
