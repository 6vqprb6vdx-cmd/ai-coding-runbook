---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=id
fetched_at: 2026-06-29T05:37:56.399719+00:00
title: "Memahami dan menghitung token \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Memahami dan menghitung token

Gemini dan model AI generatif lainnya memproses input dan output pada granularitas yang disebut *token*.

**Untuk model Gemini, token setara dengan sekitar 4 karakter.
100 token setara dengan sekitar 60-80 kata dalam bahasa Inggris.**

## Tentang token

Token dapat berupa karakter tunggal seperti `z` atau seluruh kata seperti `cat`. Kata-kata panjang dipecah menjadi beberapa token. Kumpulan semua token yang digunakan oleh model disebut kosakata, dan proses pemisahan teks menjadi token disebut *tokenisasi*.

Jika penagihan diaktifkan, [biaya panggilan ke Gemini API](https://ai.google.dev/pricing?hl=id)
ditentukan sebagian oleh jumlah token input dan output, sehingga mengetahui cara
menghitung token dapat bermanfaat.

Anda dapat mencoba menghitung token di Colab kami.

|  |  |  |
| --- | --- | --- |
| [Lihat di ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=id) | [Coba notebook Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=id) | [Lihat notebook di GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=id) |

## Menghitung token

Semua input ke dan output dari Gemini API di-tokenisasi, termasuk teks, file gambar, dan modalitas non-teks lainnya.

Anda dapat menghitung token dengan cara berikut:

- **Panggil [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=id) dengan input
  permintaan.**  
   Tindakan ini akan menampilkan jumlah total token di *input saja*. Anda dapat melakukan panggilan ini sebelum mengirim input ke model untuk memeriksa ukuran permintaan.
- **Gunakan atribut `usage_metadata` pada objek `response` setelah
  memanggil `generate_content`.**  
   Tindakan ini akan menampilkan jumlah total
  token di *input dan output*: `total_token_count`.  
   Tindakan ini juga menampilkan jumlah token input dan output secara terpisah: `prompt_token_count` (token input) dan `candidates_token_count` (token output).

  Jika Anda menggunakan model [penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id), token yang digunakan selama proses penalaran akan ditampilkan di `thoughts_token_count`. Dan jika Anda menggunakan
  [Context caching](https://ai.google.dev/gemini-api/docs/caching?hl=id), jumlah token yang di-cache akan berada di `cached_content_token_count`.

### Menghitung token teks

Jika Anda memanggil `count_tokens` dengan input khusus teks, tindakan ini akan menampilkan jumlah token teks di *input saja* (`total_tokens`). Anda dapat melakukan panggilan ini sebelum memanggil `generate_content` untuk memeriksa ukuran permintaan.

Opsi lainnya adalah memanggil `generate_content`, lalu menggunakan atribut `usage_metadata` pada objek `response` untuk mendapatkan hal berikut:

- Jumlah token input (`prompt_token_count`), konten yang di-cache (`cached_content_token_count`), dan output (`candidates_token_count`) secara terpisah
- Jumlah token untuk proses penalaran (`thoughts_token_count`)
- Jumlah total token di *input dan output* (`total_token_count`)

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

### Menghitung token multi-turn (chat)

Jika Anda memanggil `count_tokens` dengan histori chat, tindakan ini akan menampilkan jumlah total token teks dari setiap peran dalam chat (`total_tokens`).

Opsi lainnya adalah memanggil `send_message`, lalu menggunakan atribut `usage_metadata` pada objek `response` untuk mendapatkan hal berikut:

- Jumlah token input (`prompt_token_count`), konten yang di-cache (`cached_content_token_count`), dan output (`candidates_token_count`) secara terpisah
- Jumlah token untuk proses penalaran (`thoughts_token_count`)
- Jumlah total token di *input dan output* (`total_token_count`)

Untuk memahami seberapa besar giliran percakapan berikutnya, Anda harus menambahkannya ke histori saat memanggil `count_tokens`.

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

### Menghitung token multimodal

Semua input ke Gemini API di-tokenisasi, termasuk teks, file gambar, dan modalitas non-teks lainnya. Perhatikan poin-poin utama tingkat tinggi berikut tentang tokenisasi input multimodal selama pemrosesan oleh Gemini API:

- Input gambar dengan kedua dimensi <=384 piksel dihitung sebagai 258 token. Gambar yang lebih besar dalam satu atau kedua dimensi akan dipangkas dan diskalakan sesuai kebutuhan menjadi petak 768x768 piksel, yang masing-masing dihitung sebagai 258 token.
- File video dan audio dikonversi menjadi token dengan tarif tetap berikut: video dengan 263 token per detik dan audio dengan 32 token per detik.

#### Resolusi media

[Model Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-3) memperkenalkan kontrol terperinci atas
pemrosesan visi multimodal dengan parameter `media_resolution`. Parameter `media_resolution` menentukan **jumlah maksimum token yang dialokasikan per gambar input atau frame video.**
Resolusi yang lebih tinggi meningkatkan kemampuan model untuk membaca teks halus atau mengidentifikasi detail kecil, tetapi meningkatkan penggunaan token dan latensi.

Untuk mengetahui detail selengkapnya tentang parameter dan pengaruhnya terhadap penghitungan token,
lihat panduan [resolusi media](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=id).

#### File gambar

Jika Anda memanggil `count_tokens` dengan input teks dan gambar, tindakan ini akan menampilkan jumlah token gabungan teks dan gambar di *input saja* (`total_tokens`). Anda dapat melakukan panggilan ini sebelum memanggil `generate_content` untuk memeriksa ukuran permintaan. Anda juga dapat secara opsional memanggil `count_tokens` pada teks dan file secara terpisah.

Opsi lainnya adalah memanggil `generate_content`, lalu menggunakan atribut `usage_metadata` pada objek `response` untuk mendapatkan hal berikut:

- Jumlah token input (`prompt_token_count`), konten yang di-cache (`cached_content_token_count`), dan output (`candidates_token_count`) secara terpisah
- Jumlah token untuk proses penalaran (`thoughts_token_count`)
- Jumlah total token di *input dan output* (`total_token_count`)

Contoh yang menggunakan gambar yang diupload dari File API:

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

Contoh yang menyediakan gambar sebagai data inline:

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

#### File video atau audio

Audio dan video masing-masing dikonversi menjadi token dengan tarif tetap berikut:

- Video: 263 token per detik
- Audio: 32 token per detik

Jika Anda memanggil `count_tokens` dengan input teks dan video/audio, tindakan ini akan menampilkan jumlah token gabungan teks dan file video/audio di *input saja* (`total_tokens`). Anda dapat melakukan panggilan ini sebelum memanggil `generate_content` untuk memeriksa ukuran permintaan. Anda juga dapat secara opsional memanggil `count_tokens` pada teks dan file secara terpisah.

Opsi lainnya adalah memanggil `generate_content`, lalu menggunakan atribut `usage_metadata` pada objek `response` untuk mendapatkan hal berikut:

- Jumlah token input (`prompt_token_count`), konten yang di-cache (`cached_content_token_count`), dan output (`candidates_token_count`) secara terpisah
- Jumlah token untuk proses penalaran (`thoughts_token_count`)
- Jumlah total token di *input dan output* (`total_token_count`).

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

### Menghitung token penalaran

Saat Anda mengaktifkan penalaran, harga respons adalah jumlah token output dan token penalaran. Anda dapat mengambil jumlah total token penalaran yang dihasilkan dari kolom `thoughtsTokenCount` (atau SDK yang setara).

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

Model penalaran menghasilkan penalaran lengkap untuk meningkatkan kualitas respons akhir, lalu menghasilkan [ringkasan](https://ai.google.dev/gemini-api/docs/thinking?hl=id#summaries) output untuk memberikan insight tentang proses penalaran. Jadi, API mendasarkan harga pada token penalaran lengkap yang dihasilkan model untuk membuat ringkasan, meskipun API hanya menampilkan ringkasan.

Anda dapat mempelajari lebih lanjut cara mengonfigurasi penalaran di panduan [penalaran Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=id).

## Jendela konteks

Model yang tersedia melalui Gemini API memiliki jendela konteks yang diukur dalam token. Jendela konteks menentukan jumlah input yang dapat Anda berikan dan jumlah output yang dapat dihasilkan model. Anda dapat menentukan ukuran jendela konteks dengan memanggil endpoint [`models.get`](https://ai.google.dev/api/rest/v1/models/get?hl=id)atau dengan melihat [dokumentasi model](https://ai.google.dev/gemini-api/docs/models?hl=id).

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

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-24 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-24 UTC."],[],[]]
