---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=it
fetched_at: 2026-10-19T05:35:01.523322+00:00
title: "Comprendi e conteggia i token \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Comprendi e conteggia i token

Gemini e altri modelli di AI generativa elaborano input e output con una granularità chiamata *token*.

**Per i modelli Gemini, un token equivale a circa 4 caratteri.
100 token equivalgono a circa 60-80 parole in inglese.**

## Informazioni sui token

I token possono essere singoli caratteri come `z` o intere parole come `cat`. Le parole lunghe vengono suddivise in più token. L'insieme di tutti i token utilizzati dal modello è chiamato vocabolario e il processo di suddivisione del testo in token è chiamato *tokenizzazione*.

Quando la fatturazione è abilitata, il [costo di una chiamata all'API Gemini](https://ai.google.dev/pricing?hl=it) è
determinato in parte dal numero di token di input e output, quindi sapere come
contare i token può essere utile.

Puoi provare a contare i token nel nostro Colab.

|  |  |  |
| --- | --- | --- |
| [Visualizza su ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | [Prova un notebook di Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=it) | [Visualizza il notebook su GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=it) |

## Contare i token

Tutti gli input e gli output dell'API Gemini vengono tokenizzati, inclusi testo, file immagine e altre modalità non testuali.

Puoi contare i token nei seguenti modi:

- **Chiama [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=it) con l'input
  della richiesta.**  
   Viene restituito il numero totale di token *solo nell'input*. Puoi effettuare questa chiamata prima di inviare l'input al modello per verificare le dimensioni delle richieste.
- **Utilizza l'attributo `usage_metadata` dell'oggetto `response` dopo
  aver chiamato `generate_content`.**  
   Viene restituito il numero totale di
  token *sia nell'input che nell'output*: `total_token_count`.  
   Vengono restituiti anche i conteggi dei token di input e output separatamente: `prompt_token_count` (token di input) e `candidates_token_count` (token di output).

  Se utilizzi un [modello di ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it), i token utilizzati durante il processo di ragionamento vengono restituiti in `thoughts_token_count`. Se utilizzi
  [la memorizzazione nella cache del contesto](https://ai.google.dev/gemini-api/docs/caching?hl=it), il conteggio dei token memorizzati nella cache
  sarà in `cached_content_token_count`.

### Contare i token di testo

Se chiami `count_tokens` con un input di solo testo, viene restituito il conteggio dei token del testo *solo nell'input* (`total_tokens`). Puoi effettuare questa chiamata prima di chiamare `generate_content` per verificare le dimensioni delle richieste.

Un'altra opzione è chiamare `generate_content` e poi utilizzare l'attributo `usage_metadata` dell'oggetto `response` per ottenere quanto segue:

- I conteggi dei token separati dell'input (`prompt_token_count`), dei contenuti memorizzati nella cache (`cached_content_token_count`) e dell'output (`candidates_token_count`)
- Il conteggio dei token per il processo di ragionamento (`thoughts_token_count`)
- Il numero totale di token *sia nell'input che nell'output* (`total_token_count`)

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

### Vai

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

### Contare i token di chat a più turni

Se chiami `count_tokens` con la cronologia chat, viene restituito il conteggio totale dei token del testo di ogni ruolo nella chat (`total_tokens`).

Un'altra opzione è chiamare `send_message` e poi utilizzare l'attributo `usage_metadata` dell'oggetto `response` per ottenere quanto segue:

- I conteggi dei token separati dell'input (`prompt_token_count`), dei contenuti memorizzati nella cache (`cached_content_token_count`) e dell'output (`candidates_token_count`)
- Il conteggio dei token per il processo di ragionamento (`thoughts_token_count`)
- Il numero totale di token *sia nell'input che nell'output* (`total_token_count`)

Per capire quanto sarà grande il prossimo turno di conversazione, devi aggiungerlo alla cronologia quando chiami `count_tokens`.

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

### Vai

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

### Contare i token multimodali

Tutti gli input dell'API Gemini vengono tokenizzati, inclusi testo, file immagine e altre modalità non testuali. Tieni presente i seguenti punti chiave di alto livello sulla tokenizzazione dell'input multimodale durante l'elaborazione da parte dell'API Gemini:

- Gli input immagine con entrambe le dimensioni <= 384 pixel vengono conteggiati come 258 token. Le immagini più grandi in una o entrambe le dimensioni vengono ritagliate e scalate in base alle esigenze in riquadri di 768 x 768 pixel, ognuno conteggiato come 258 token.
- I file audio e video vengono convertiti in token alle seguenti tariffe fisse: video a 263 token al secondo e audio a 32 token al secondo. Questa tariffa si applica all'elaborazione statica (impostazione predefinita). Per l'elaborazione agentica, l'utilizzo dei token varia. Consulta [Utilizzo dei token video per modalità di elaborazione](#video-token-usage).

#### Risoluzioni dei contenuti multimediali

[I modelli Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=it#gemini-3) introducono un controllo granulare sull'
elaborazione della visione multimodale con il parametro `media_resolution`. Il parametro `media_resolution` determina il **numero massimo di token allocati per ogni immagine di input o fotogramma video**.
Le risoluzioni più elevate migliorano la capacità del modello di leggere il testo fine o identificare piccoli dettagli, ma aumentano l'utilizzo dei token e la latenza.

Per maggiori dettagli sul parametro e su come può influire sui calcoli dei token,
consulta la [guida alla risoluzione dei contenuti multimediali](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=it).

#### File immagine

Se chiami `count_tokens` con un input di testo e immagine, viene restituito il conteggio combinato dei token del testo e dell'immagine *solo nell'input* (`total_tokens`). Puoi effettuare questa chiamata prima di chiamare `generate_content` per verificare le dimensioni delle richieste. Puoi anche chiamare facoltativamente `count_tokens` sul testo e sul file separatamente.

Un'altra opzione è chiamare `generate_content` e poi utilizzare l'attributo `usage_metadata` dell'oggetto `response` per ottenere quanto segue:

- I conteggi dei token separati dell'input (`prompt_token_count`), dei contenuti memorizzati nella cache (`cached_content_token_count`) e dell'output (`candidates_token_count`)
- Il conteggio dei token per il processo di ragionamento (`thoughts_token_count`)
- Il numero totale di token *sia nell'input che nell'output* (`total_token_count`)

Esempio che utilizza un'immagine caricata dall'API File:

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

### Vai

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

Esempio che fornisce l'immagine come dati in linea:

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

### Vai

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

#### File audio o video

L'audio e il video vengono convertiti in token alle seguenti tariffe fisse:

- Video: 263 token al secondo
- Audio: 32 token al secondo

Se chiami `count_tokens` con un input di testo e video/audio, viene restituito il conteggio combinato dei token del testo e del file video/audio *solo nell'input* (`total_tokens`). Puoi effettuare questa chiamata prima di chiamare `generate_content` per verificare le dimensioni delle richieste. Puoi anche chiamare facoltativamente `count_tokens` sul testo e sul file separatamente.

Un'altra opzione è chiamare `generate_content` e poi utilizzare l'attributo `usage_metadata` dell'oggetto `response` per ottenere quanto segue:

- I conteggi dei token separati dell'input (`prompt_token_count`), dei contenuti memorizzati nella cache (`cached_content_token_count`) e dell'output (`candidates_token_count`)
- Il conteggio dei token per il processo di ragionamento (`thoughts_token_count`)
- Il numero totale di token *sia nell'input che nell'output* (`total_token_count`).

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

### Vai

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

#### Utilizzo dei token video per modalità di elaborazione

L'utilizzo dei token per i video dipende dalla modalità di elaborazione:

| **Modalità di elaborazione** | **Calcolo dei token** | **Utilizzo tipico** |
| --- | --- | --- |
| **Statica** (impostazione predefinita) | ~100 token/secondo per impostazione predefinita (bassa risoluzione) o ~300 token/secondo (alta risoluzione). Tutti i fotogrammi campionati a 1 FPS. | Prevedibile, proporzionale alla durata del video. |
| **Agentica** | Varia in base alla complessità dei contenuti. Il modello carica solo la trascrizione e/o i fotogrammi e/o l'audio necessari per rispondere al prompt. | Fino all'88% in meno di token per i contenuti in formato lungo. |

Con l'elaborazione agentica, una lezione di 1 ora che utilizzerebbe ~1,08 milioni di token in modalità statica potrebbe utilizzare ~108.000 token, a seconda del prompt e dei contenuti.

Per verificare l'utilizzo effettivo dei token per una richiesta, utilizza il campo `usage_metadata` nella risposta. In `UsageMetadata`, i token video agentici vengono segnalati nei seguenti campi:

- **Prompt iniziale** (riferimento video + prompt utente): `prompt_token_count`
- **Ragionamento di navigazione**: `thoughts_token_count`
- **Trascrizione, fotogrammi e audio caricati on demand**: `tool_use_prompt_token_count`
- **Risposta finale**: `candidates_token_count`

### Contare i token di ragionamento

Quando attivi il ragionamento, il prezzo della risposta è la somma dei token di output e dei token di ragionamento. Puoi recuperare il numero totale di token di ragionamento generati dal campo `thoughtsTokenCount` (o dall'equivalente SDK).

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

### Vai

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

I modelli di ragionamento generano ragionamenti completi per migliorare la qualità della risposta finale e poi restituiscono [riepiloghi](https://ai.google.dev/gemini-api/docs/thinking?hl=it#summaries) per fornire informazioni sul processo di ragionamento. Pertanto, l'API basa i prezzi sui token di ragionamento completi che il modello genera per creare un riepilogo, anche se l'API restituisce solo il riepilogo.

Puoi scoprire di più su come configurare il ragionamento nella guida al ragionamento di [Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=it).

## Finestre contestuali

I modelli disponibili tramite l'API Gemini hanno finestre contestuali misurate in token. La finestra contestuale definisce la quantità di input che puoi fornire e la quantità di output che il modello può generare. Puoi determinare le dimensioni della
finestra contestuale chiamando l'endpoint [`models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=it)
o consultando la [documentazione dei modelli](https://ai.google.dev/gemini-api/docs/models?hl=it).

- **Modelli Gemini 4 (`gemini-4-argon`):** condividono una singola finestra contestuale di 1 milione di token (`1,048,576` token) tra token di input, ragionamento e output. Le singole richieste sono limitate a `65,536` token di output per lo streaming (`streamGenerateContent`) e `32,768` token di output per il non streaming (`generateContent`), oppure puoi generare fino a `1,048,576` token utilizzando [la decodifica lunga](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=it). Se i token di input più `max_output_tokens` superano 1.048.576 token, l'API limita automaticamente l'output allo spazio rimanente nella finestra contestuale (`1,048,576` meno i token di input).
- **Modelli Gemini 3 e 2.5:** utilizzano budget di input (`1,048,576` token) e output (`65,536` token) separati.

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

### Vai

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

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-13 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-13 UTC."],[],[]]
