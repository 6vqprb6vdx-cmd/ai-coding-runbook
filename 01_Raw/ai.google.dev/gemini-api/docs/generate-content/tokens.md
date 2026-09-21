---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=fr
fetched_at: 2026-09-21T05:46:30.569989+00:00
title: "Comprendre et compter les jetons \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Comprendre et compter les jetons

Gemini et d'autres modèles d'IA générative traitent les entrées et les sorties avec une granularité appelée *jeton*.

**Pour les modèles Gemini, un jeton équivaut à environ quatre caractères.
100 jetons correspondent à environ 60 à 80 mots en anglais.**

## À propos des jetons

Les jetons peuvent être des caractères uniques comme `z` ou des mots entiers comme `cat`. Les mots longs sont divisés en plusieurs jetons. L'ensemble de tous les jetons utilisés par le modèle est appelé vocabulaire, et le processus de fractionnement du texte en jetons est appelé *tokenisation*.

Lorsque la facturation est activée, le [coût d'un appel à l'API Gemini](https://ai.google.dev/pricing?hl=fr) est déterminé en partie par le nombre de jetons d'entrée et de sortie. Il peut donc être utile de savoir comment compter les jetons.

Vous pouvez essayer de compter les jetons dans notre Colab.

|  |  |  |
| --- | --- | --- |
| [Afficher sur ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=fr) | [Essayer un notebook Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=fr) | [Afficher le notebook sur GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=fr) |

## Compter les jetons

Toutes les entrées et sorties de l'API Gemini sont tokenisées, y compris le texte, les fichiers image et les autres modalités non textuelles.

Vous pouvez compter les jetons de différentes manières :

- **Appelez [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=fr) avec l'entrée de la requête.**  
   : renvoie le nombre total de jetons dans *l'entrée uniquement*. Vous pouvez effectuer cet appel avant d'envoyer l'entrée au modèle pour vérifier la taille de vos requêtes.
- **Utilisez l'attribut `usage_metadata` sur l'objet `response` après avoir appelé `generate_content`.**  
   renvoie le nombre total de jetons dans *l'entrée et la sortie* : `total_token_count`.  
   Il renvoie également le nombre de jetons d'entrée et de sortie séparément : `prompt_token_count` (jetons d'entrée) et `candidates_token_count` (jetons de sortie).

  Si vous utilisez un [modèle de réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr), les jetons utilisés lors du processus de réflexion sont renvoyés dans `thoughts_token_count`. Si vous utilisez la [mise en cache du contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr), le nombre de jetons mis en cache se trouve dans `cached_content_token_count`.

### Compter les jetons de texte

Si vous appelez `count_tokens` avec une entrée en texte brut, il renvoie le nombre de jetons du texte *dans l'entrée uniquement* (`total_tokens`). Vous pouvez effectuer cet appel avant d'appeler `generate_content` pour vérifier la taille de vos requêtes.

Une autre option consiste à appeler `generate_content`, puis à utiliser l'attribut `usage_metadata` sur l'objet `response` pour obtenir les éléments suivants :

- Nombre de jetons distincts pour l'entrée (`prompt_token_count`), le contenu mis en cache (`cached_content_token_count`) et la sortie (`candidates_token_count`)
- Nombre de jetons pour le processus de réflexion (`thoughts_token_count`)
- Nombre total de jetons *dans l'entrée et la sortie* (`total_token_count`)

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

### Go

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

### Compter les jetons multitours (chat)

Si vous appelez `count_tokens` avec l'historique des discussions, il renvoie le nombre total de jetons du texte de chaque rôle dans la discussion (`total_tokens`).

Une autre option consiste à appeler `send_message`, puis à utiliser l'attribut `usage_metadata` sur l'objet `response` pour obtenir les éléments suivants :

- Nombre de jetons distincts pour l'entrée (`prompt_token_count`), le contenu mis en cache (`cached_content_token_count`) et la sortie (`candidates_token_count`)
- Nombre de jetons pour le processus de réflexion (`thoughts_token_count`)
- Nombre total de jetons *dans l'entrée et la sortie* (`total_token_count`)

Pour comprendre l'ampleur de votre prochaine réponse conversationnelle, vous devez l'ajouter à l'historique lorsque vous appelez `count_tokens`.

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

### Go

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

### Compter les jetons multimodaux

Toutes les entrées de l'API Gemini sont tokenisées, y compris le texte, les fichiers image et les autres modalités non textuelles. Voici les principaux points à retenir concernant la tokenisation des entrées multimodales lors du traitement par l'API Gemini :

- Les entrées d'image dont les deux dimensions sont inférieures ou égales à 384 pixels sont comptabilisées comme 258 jetons. Les images dont l'une ou les deux dimensions sont supérieures sont recadrées et mises à l'échelle si nécessaire en vignettes de 768 x 768 pixels, chacune comptant pour 258 jetons.
- Les fichiers vidéo et audio sont convertis en jetons aux taux fixes suivants : 263 jetons par seconde pour les vidéos et 32 jetons par seconde pour les fichiers audio.

#### Résolutions des contenus multimédias

Les [modèles Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-3) offrent un contrôle précis sur le traitement de la vision multimodale grâce au paramètre `media_resolution`. Le paramètre `media_resolution` détermine le **nombre maximal de jetons alloués par image ou frame vidéo en entrée**.
Les résolutions plus élevées améliorent la capacité du modèle à lire du texte fin ou à identifier de petits détails, mais augmentent l'utilisation de jetons et la latence.

Pour en savoir plus sur le paramètre et son impact sur le calcul des jetons, consultez le guide sur la [résolution du contenu multimédia](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=fr).

#### Fichiers image

Si vous appelez `count_tokens` avec une entrée de texte et d'image, il renvoie le nombre total de jetons du texte et de l'image *dans l'entrée uniquement* (`total_tokens`). Vous pouvez effectuer cet appel avant d'appeler `generate_content` pour vérifier la taille de vos requêtes. Vous pouvez également appeler `count_tokens` sur le texte et le fichier séparément.

Une autre option consiste à appeler `generate_content`, puis à utiliser l'attribut `usage_metadata` sur l'objet `response` pour obtenir les éléments suivants :

- Nombre de jetons distincts pour l'entrée (`prompt_token_count`), le contenu mis en cache (`cached_content_token_count`) et la sortie (`candidates_token_count`)
- Nombre de jetons pour le processus de réflexion (`thoughts_token_count`)
- Nombre total de jetons *dans l'entrée et la sortie* (`total_token_count`)

Exemple utilisant une image importée à partir de l'API File :

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

Exemple qui fournit l'image en tant que données intégrées :

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

#### Fichiers audio ou vidéo

L'audio et la vidéo sont convertis en jetons aux taux fixes suivants :

- Vidéo : 263 jetons par seconde
- Audio : 32 jetons par seconde

Si vous appelez `count_tokens` avec une entrée texte et vidéo/audio, il renvoie le nombre combiné de jetons du texte et du fichier vidéo/audio *dans l'entrée uniquement* (`total_tokens`). Vous pouvez effectuer cet appel avant d'appeler `generate_content` pour vérifier la taille de vos requêtes. Vous pouvez également appeler `count_tokens` sur le texte et le fichier séparément.

Une autre option consiste à appeler `generate_content`, puis à utiliser l'attribut `usage_metadata` sur l'objet `response` pour obtenir les éléments suivants :

- Nombre de jetons distincts pour l'entrée (`prompt_token_count`), le contenu mis en cache (`cached_content_token_count`) et la sortie (`candidates_token_count`)
- Nombre de jetons pour le processus de réflexion (`thoughts_token_count`)
- Nombre total de jetons *d'entrée et de sortie* (`total_token_count`).

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

### Compter les jetons de réflexion

Lorsque vous activez la réflexion, le prix de la réponse correspond à la somme des jetons de sortie et des jetons de réflexion. Vous pouvez récupérer le nombre total de jetons de réflexion générés à partir du champ `thoughtsTokenCount` (ou de l'équivalent SDK).

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

Les modèles à raisonnement génèrent des pensées complètes pour améliorer la qualité de la réponse finale, puis produisent des [résumés](https://ai.google.dev/gemini-api/docs/thinking?hl=fr#summaries) pour donner un aperçu du processus de réflexion. Par conséquent, l'API base la tarification sur les jetons de pensée complets que le modèle génère pour créer un résumé, même si l'API ne génère que le résumé.

Pour savoir comment configurer la réflexion, consultez le guide [Réflexion de Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).

## Fenêtres de contexte

Les modèles disponibles via l'API Gemini disposent de fenêtres de contexte mesurées en jetons. La fenêtre de contexte définit la quantité d'entrée que vous pouvez fournir et la quantité de sortie que le modèle peut générer. Vous pouvez déterminer la taille de la fenêtre de contexte en appelant le [point de terminaison `models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=fr) ou en consultant la [documentation sur les modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr).

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

### Go

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

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/12 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/12 (UTC)."],[],[]]
