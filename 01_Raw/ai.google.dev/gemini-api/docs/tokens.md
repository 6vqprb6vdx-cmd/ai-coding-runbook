---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=pt-BR
fetched_at: 2026-05-25T13:04:17.453834+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Entender e contar tokens

O Gemini e outros modelos de IA generativa processam entradas e saídas em uma granularidade chamada *token*.

**Para modelos do Gemini, um token equivale a cerca de quatro caracteres.
100 tokens equivalem a cerca de 60 a 80 palavras em inglês.**

## Sobre tokens

Os tokens podem ser caracteres únicos, como `z`, ou palavras inteiras, como `cat`. Palavras longas são divididas em vários tokens. O conjunto de todos os tokens usados pelo modelo é chamado de vocabulário, e o processo de dividir o texto em tokens é chamado de *tokenização*.

Quando o faturamento está ativado, o [custo de uma chamada para a API Gemini](https://ai.google.dev/pricing?hl=pt-br) é determinado em parte pelo número de tokens de entrada e saída. Por isso, saber como contar tokens pode ser útil.

Você pode testar a contagem de tokens no nosso Colab.

|  |  |  |
| --- | --- | --- |
| [Ver em ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) | [Testar um notebook do Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=pt-br) | [Conferir o notebook no GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=pt-br) |

## Contar tokens

Todas as entradas e saídas da API Gemini são tokenizadas, incluindo texto, arquivos de imagem e outras modalidades que não são de texto.

É possível contar tokens das seguintes maneiras:

- **Chame [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=pt-br) com a entrada da solicitação.**  
   Isso retorna o número total de tokens *apenas na entrada*. Você pode fazer essa chamada antes de enviar a entrada para o modelo e verificar o tamanho das solicitações.
- **Use o atributo `usage_metadata` no objeto `response` depois de
  chamar `generate_content`.**  
   Isso retorna o número total de tokens em *entrada e saída*: `total_token_count`.  
   Ele
  também retorna as contagens de tokens da entrada e da saída separadamente: `prompt_token_count` (tokens de entrada) e `candidates_token_count`
  (tokens de saída).

  Se você estiver usando um [modelo de raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br), os tokens usados durante o processo de raciocínio serão retornados em `thoughts_token_count`. Se você estiver usando o [armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br), a contagem de tokens armazenados em cache estará em `cached_content_token_count`.

### Contar tokens de texto

Se você chamar `count_tokens` com uma entrada somente de texto, ele vai retornar a contagem de tokens do texto *apenas na entrada* (`total_tokens`). É possível fazer essa chamada antes de chamar `generate_content` para verificar o tamanho das solicitações.

Outra opção é chamar `generate_content` e usar o atributo `usage_metadata`
no objeto `response` para receber o seguinte:

- As contagens de tokens separadas da entrada (`prompt_token_count`), do conteúdo em cache (`cached_content_token_count`) e da saída (`candidates_token_count`).
- A contagem de tokens para o processo de raciocínio (`thoughts_token_count`)
- O número total de tokens *na entrada e na saída*
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

### Contar tokens multiturno (chat)

Se você chamar `count_tokens` com o histórico de chat, ele vai retornar a contagem total de tokens do texto de cada função no chat (`total_tokens`).

Outra opção é chamar `send_message` e usar o atributo `usage_metadata`
no objeto `response` para receber o seguinte:

- As contagens separadas de tokens da entrada (`prompt_token_count`), do conteúdo
  em cache (`cached_content_token_count`) e da saída
  (`candidates_token_count`)
- A contagem de tokens para o processo de raciocínio (`thoughts_token_count`)
- O número total de tokens *na entrada e na saída*
  (`total_token_count`)

Para entender o tamanho da sua próxima conversa, adicione-a ao histórico ao chamar `count_tokens`.

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

### Contar tokens multimodais

Todas as entradas da API Gemini são tokenizadas, incluindo texto, arquivos de imagem e outras modalidades não textuais. Confira os principais pontos sobre a tokenização de entradas multimodais durante o processamento pela API Gemini:

- Entradas de imagem com ambas as dimensões <=384 pixels são contadas como
  258 tokens. Imagens maiores em uma ou ambas as dimensões são cortadas e dimensionadas conforme
  necessário em blocos de 768 x 768 pixels, cada um contado como 258 tokens.
- Os arquivos de vídeo e áudio são convertidos em tokens nas seguintes taxas fixas: vídeo a 263 tokens por segundo e áudio a 32 tokens por segundo.

#### Resoluções de mídia

Os [modelos do Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#gemini-3) introduzem um controle granular sobre o processamento de visão multimodal com o parâmetro `media_resolution`. O parâmetro
`media_resolution` determina o
**número máximo de tokens alocados por imagem de entrada ou frame de vídeo**.
Resoluções mais altas melhoram a capacidade do modelo de ler textos pequenos ou identificar detalhes, mas aumentam o uso de tokens e a latência.

Para mais detalhes sobre o parâmetro e como ele pode afetar os cálculos de token, consulte o guia de [resolução de mídia](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pt-br).

#### Arquivos de imagem

Se você chamar `count_tokens` com uma entrada de texto e imagem, ele vai retornar a contagem combinada de tokens do texto e da imagem *apenas na entrada* (`total_tokens`). Você pode fazer essa chamada antes de chamar `generate_content` para verificar o tamanho das suas solicitações. Você também pode chamar `count_tokens` no texto e no arquivo separadamente.

Outra opção é chamar `generate_content` e usar o atributo `usage_metadata`
no objeto `response` para receber o seguinte:

- As contagens de tokens separadas da entrada (`prompt_token_count`), do conteúdo em cache (`cached_content_token_count`) e da saída (`candidates_token_count`).
- A contagem de tokens para o processo de raciocínio (`thoughts_token_count`)
- O número total de tokens *na entrada e na saída*
  (`total_token_count`)

Exemplo que usa uma imagem enviada da API File:

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

Exemplo que fornece a imagem como dados inline:

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

#### Arquivos de vídeo ou áudio

O áudio e o vídeo são convertidos em tokens nas seguintes taxas fixas:

- Vídeo: 263 tokens por segundo
- Áudio: 32 tokens por segundo

Se você chamar `count_tokens` com uma entrada de texto e vídeo/áudio, ele vai retornar a contagem combinada de tokens do texto e do arquivo de vídeo/áudio *apenas na entrada* (`total_tokens`). Você pode fazer essa chamada antes de chamar `generate_content` para verificar o tamanho das suas solicitações. Também é possível chamar `count_tokens` no texto e no arquivo separadamente.

Outra opção é chamar `generate_content` e usar o atributo `usage_metadata`
no objeto `response` para receber o seguinte:

- As contagens de tokens separadas da entrada (`prompt_token_count`), do conteúdo em cache (`cached_content_token_count`) e da saída (`candidates_token_count`).
- A contagem de tokens para o processo de raciocínio (`thoughts_token_count`)
- O número total de tokens *na entrada e na saída* (`total_token_count`).

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

## Janelas de contexto

Os modelos disponíveis na API Gemini têm janelas de contexto medidas em tokens. A janela de contexto define a quantidade de entrada que você pode fornecer e a quantidade de saída que o modelo pode gerar. Para determinar o tamanho da janela de contexto, chame o [endpoint `models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=pt-br) ou consulte a [documentação de modelos](https://ai.google.dev/gemini-api/docs/models?hl=pt-br).

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

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-19 UTC."],[],[]]
