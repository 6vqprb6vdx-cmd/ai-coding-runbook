---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=de
fetched_at: 2026-08-03T04:31:48.723729+00:00
title: "Tokens verstehen und z\u00e4hlen \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Tokens verstehen und zählen

Gemini und andere generative KI-Modelle verarbeiten Eingaben und Ausgaben mit einer Granularität, die als *Token* bezeichnet wird.

**Bei Gemini-Modellen entspricht ein Token etwa 4 Zeichen.
100 Tokens entsprechen etwa 60–80 englischen Wörtern.**

## Informationen zu Tokens

Tokens können einzelne Zeichen wie `z` oder ganze Wörter wie `cat` sein. Lange Wörter werden in mehrere Tokens aufgeteilt. Die Menge aller vom Modell verwendeten Tokens wird als Vokabular bezeichnet und der Vorgang, Text in Tokens aufzuteilen, als *Tokenisierung*.

Wenn die Abrechnung aktiviert ist, werden die [Kosten für einen Aufruf der Gemini API](https://ai.google.dev/pricing?hl=de) teilweise durch die Anzahl der Eingabe- und Ausgabetokens bestimmt. Daher kann es hilfreich sein, zu wissen, wie Tokens gezählt werden.

Sie können das Zählen von Tokens in unserem Colab ausprobieren.

|  |  |  |
| --- | --- | --- |
| [Auf ai.google.dev ansehen](https://ai.google.dev/gemini-api/docs/tokens?hl=de) | [Colab-Notebook ausprobieren](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=de) | [Notebook auf GitHub ansehen](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=de) |

## Tokens zählen

Alle Eingaben und Ausgaben der Gemini API werden tokenisiert, einschließlich Text, Bilddateien und anderer nicht textbasierter Modalitäten.

Sie können Tokens auf folgende Arten zählen:

- **Rufen Sie [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=de) mit der Eingabe
  der Anfrage auf.**  
   Dadurch wird die Gesamtzahl der Tokens *nur in der Eingabe* zurückgegeben. Sie können diesen Aufruf vor dem Senden der Eingabe an das Modell ausführen, um die Größe Ihrer Anfragen zu prüfen.
- **Verwenden Sie das Attribut `usage_metadata` für das Objekt `response`, nachdem Sie `generate_content` aufgerufen haben.**  
   Dadurch wird die Gesamtzahl der
  Tokens in *der Eingabe und in der Ausgabe* zurückgegeben: `total_token_count`.  
   Außerdem werden die Tokenanzahlen der Eingabe und Ausgabe separat zurückgegeben: `prompt_token_count` (Eingabetokens) und `candidates_token_count` (Ausgabetokens).

  Wenn Sie ein [Thinking
  Modell](https://ai.google.dev/gemini-api/docs/thinking?hl=de) verwenden, werden die während des Denk
  Prozesses verwendeten Tokens in `thoughts_token_count` zurückgegeben. Wenn Sie
  [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) verwenden, wird die Anzahl der im Cache gespeicherten Tokens in `cached_content_token_count` angegeben.

### Texttokens zählen

Wenn Sie `count_tokens` mit einer reinen Texteingabe aufrufen, wird die Anzahl der Tokens des Texts *nur in der Eingabe* zurückgegeben (`total_tokens`). Sie können diesen Aufruf vor dem Aufruf von `generate_content` ausführen, um die Größe Ihrer Anfragen zu prüfen.

Eine weitere Möglichkeit ist, `generate_content` aufzurufen und dann das Attribut `usage_metadata` für das Objekt `response` zu verwenden, um Folgendes abzurufen:

- Die separaten Tokenanzahlen der Eingabe (`prompt_token_count`), der im Cache gespeicherten Inhalte (`cached_content_token_count`) und der Ausgabe (`candidates_token_count`)
- Die Tokenanzahl für den Denkprozess (`thoughts_token_count`)
- Die Gesamtzahl der Tokens *in der Eingabe und in der Ausgabe* (`total_token_count`)

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=prompt
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
    model: "gemini-3.6-flash",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: prompt,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Ok

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

// Convert prompt to a slice of *genai.Content using the helper.
contents := []*genai.Content{
  genai.NewContentFromText(prompt, genai.RoleUser),
}
countResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", contents, nil)
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

### Tokens für Unterhaltungen mit mehreren Antworten (Chat) zählen

Wenn Sie `count_tokens` mit dem Chatverlauf aufrufen, wird die Gesamtzahl der Tokens des Texts für jede Rolle im Chat zurückgegeben (`total_tokens`).

Eine weitere Möglichkeit ist, `send_message` aufzurufen und dann das Attribut `usage_metadata` für das Objekt `response` zu verwenden, um Folgendes abzurufen:

- Die separaten Tokenanzahlen der Eingabe (`prompt_token_count`), der im Cache gespeicherten Inhalte (`cached_content_token_count`) und der Ausgabe (`candidates_token_count`)
- Die Tokenanzahl für den Denkprozess (`thoughts_token_count`)
- Die Gesamtzahl der Tokens *in der Eingabe und in der Ausgabe* (`total_token_count`)

Wenn Sie wissen möchten, wie groß Ihre nächste Unterhaltung sein wird, müssen Sie sie beim Aufruf von `count_tokens` an den Verlauf anhängen.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.6-flash",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3.6-flash", contents=chat.get_history()
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
print(client.models.count_tokens(model="gemini-3.6-flash", contents=history))
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
    model: "gemini-3.6-flash",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
    contents: combinedHistory,
  });
  console.log(
    "Combined history token count:",
    combinedCountTokensResponse.totalTokens,
  );
}

await main();
```

### Ok

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

history := []*genai.Content{
  {Role: genai.RoleUser, Parts: []*genai.Part({Text: "Hi my name is Bob"})},
  {Role: genai.RoleModel, Parts: []*genai.Part({Text: "Hi Bob!"})},
}
chat, err := client.Chats.Create(ctx, "gemini-3.6-flash", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", chat.History(false), nil)
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

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### Multimodale Tokens zählen

Alle Eingaben der Gemini API werden tokenisiert, einschließlich Text, Bilddateien und anderer nicht textbasierter Modalitäten. Beachten Sie die folgenden allgemeinen Punkte zur Tokenisierung multimodaler Eingaben während der Verarbeitung durch die Gemini API:

- Bildeingaben mit beiden Dimensionen <= 384 Pixel werden als 258 Tokens gezählt. Bilder, die in einer oder beiden Dimensionen größer sind, werden nach Bedarf zugeschnitten und auf 768 × 768 Pixel große Kacheln skaliert. Jede Kachel wird als 258 Tokens gezählt.
- Video- und Audiodateien werden mit den folgenden festen Raten in Tokens umgewandelt: Video mit 263 Tokens pro Sekunde und Audio mit 32 Tokens pro Sekunde.

#### Auflösungen von Medien

[Mit den Gemini 3-Modellen](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-3) wird mit dem `media_resolution` Parameter eine detaillierte Steuerung der
multimodalen Bildverarbeitung eingeführt. Der Parameter `media_resolution` bestimmt die **maximale Anzahl der Tokens, die pro Eingabebild oder Videoframe zugewiesen werden**.
Höhere Auflösungen verbessern die Fähigkeit des Modells, kleinen Text zu lesen oder kleine Details zu erkennen, erhöhen aber die Tokennutzung und die Latenz.

Weitere Informationen zum Parameter und zu seinen Auswirkungen auf die Tokenberechnungen finden Sie im Leitfaden zur Auflösung von Medien.
Siehe den [Leitfaden zur Auflösung von Medien](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=de).

#### Bilddateien

Wenn Sie `count_tokens` mit einer Text- und Bildeingabe aufrufen, wird die kombinierte Tokenanzahl des Texts und des Bilds *nur in der Eingabe* zurückgegeben (`total_tokens`). Sie können diesen Aufruf vor dem Aufruf von `generate_content` ausführen, um die Größe Ihrer Anfragen zu prüfen. Optional können Sie `count_tokens` auch separat für den Text und die Datei aufrufen.

Eine weitere Möglichkeit ist, `generate_content` aufzurufen und dann das Attribut `usage_metadata` für das Objekt `response` zu verwenden, um Folgendes abzurufen:

- Die separaten Tokenanzahlen der Eingabe (`prompt_token_count`), der im Cache gespeicherten Inhalte (`cached_content_token_count`) und der Ausgabe (`candidates_token_count`)
- Die Tokenanzahl für den Denkprozess (`thoughts_token_count`)
- Die Gesamtzahl der Tokens *in der Eingabe und in der Ausgabe* (`total_token_count`)

Beispiel mit einem hochgeladenen Bild aus der File API:

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.6-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.6-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Ok

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx, 
  filepath.Join(getMedia(), "organ.jpg&q&uot;), 
  genai.UploadFileConfig{
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

Beispiel, bei dem das Bild als Inline-Daten bereitgestellt wird:

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3.6-flash", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[prompt, your_image_file]
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
    model: "gemini-3.6-flash",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: contents,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Ok

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

imageBytes, err := os.ReadFile("organ.jpg")
if err != nil {
    log.Fatalf("Failed to read image file: %v", err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image&qu&ot;),
  {
        InlineData: genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imageBytes,
        },
  },
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "&quot;, "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### Video- oder Audiodateien

Audio und Video werden jeweils mit den folgenden festen Raten in Tokens umgewandelt:

- Video: 263 Tokens pro Sekunde
- Audio: 32 Tokens pro Sekunde

Wenn Sie `count_tokens` mit einer Text- und Video-/Audioeingabe aufrufen, wird die kombinierte Tokenanzahl des Texts und der Video-/Audiodatei *nur in der Eingabe* zurückgegeben (`total_tokens`). Sie können diesen Aufruf vor dem Aufruf von `generate_content` ausführen, um die Größe Ihrer Anfragen zu prüfen. Optional können Sie `count_tokens` auch separat für den Text und die Datei aufrufen.

Eine weitere Möglichkeit ist, `generate_content` aufzurufen und dann das Attribut `usage_metadata` für das Objekt `response` zu verwenden, um Folgendes abzurufen:

- Die separaten Tokenanzahlen der Eingabe (`prompt_token_count`), der im Cache gespeicherten Inhalte (`cached_content_token_count`) und der Ausgabe (`candidates_token_count`)
- Die Tokenanzahl für den Denkprozess (`thoughts_token_count`)
- Die Gesamtzahl der Tokens *in der Eingabe und in der Ausgabe* (`total_token_count`).

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
        model="gemini-3.6-flash", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[prompt, your_file]
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
    model: "gemini-3.6-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Ok

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx,
  filepath.Join(getMedia(), "Big_Buck_Bunny.mp4&&quot;),
  genai.UploadFileConfig{
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

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3.6-flash", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

### Tokens für Gedanken zählen

Wenn Sie Thinking aktivieren, setzen sich die Kosten für die Antwort aus der Anzahl der Ausgabetokens und der Anzahl der Thinking-Tokens zusammen. Sie können die Gesamtzahl der generierten Thinking-Tokens aus dem Feld `thoughtsTokenCount` (oder dem entsprechenden SDK-Feld) abrufen.

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

### Ok

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Thinking-Modelle generieren vollständige Gedanken, um die Qualität der endgültigen Antwort zu verbessern, und geben dann [Zusammenfassungen](https://ai.google.dev/gemini-api/docs/thinking?hl=de#summaries) aus, um Einblicke in den Denkprozess zu geben. Daher basiert die Abrechnung der API auf den vollständigen Thinking-Tokens, die das Modell zum Erstellen einer Zusammenfassung generiert, obwohl die API nur die Zusammenfassung ausgibt.

Weitere Informationen zum Konfigurieren von Thinking finden Sie im Leitfaden zu [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=de).

## Kontextfenster

Die über die Gemini API verfügbaren Modelle haben Kontextfenster, die in Tokens gemessen werden. Das Kontextfenster definiert, wie viele Eingaben Sie bereitstellen können und wie viele Ausgaben das Modell generieren kann. Sie können die Größe des
Kontextfensters ermitteln, indem Sie den [`models.get` Endpunkt](https://ai.google.dev/api/rest/v1/models/get?hl=de)
aufrufen oder in der [Dokumentation zu den Modellen](https://ai.google.dev/gemini-api/docs/models?hl=de)nachsehen.

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3.6-flash")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3.6-flash'});
  console.log(modelInfo.inputTokenLimit);
  console.log(modelInfo.outputTokenLimit);
}

await main();
```

### Ok

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
  log.Fatal(err)
}
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3.6-flash")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
