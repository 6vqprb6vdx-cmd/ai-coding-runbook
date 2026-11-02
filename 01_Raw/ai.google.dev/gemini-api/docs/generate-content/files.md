---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/files?hl=id
fetched_at: 2026-11-02T07:30:32.785573+00:00
title: "API File \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# API File

Gemini dapat menangani berbagai jenis data input, termasuk teks, gambar, dan
audio, secara bersamaan.

Panduan ini menunjukkan cara menggunakan file media dengan Files API. Operasi dasarnya sama untuk file audio, gambar, video, dokumen, dan jenis file lain yang didukung.

Untuk panduan perintah file, lihat bagian
[Panduan perintah file](https://ai.google.dev/gemini-api/docs/files?hl=id#prompt-guide).

## Upload file

Anda dapat menggunakan Files API untuk mengupload file media. Selalu gunakan Files API jika
ukuran total permintaan (termasuk file, perintah teks, petunjuk sistem,
dll.) lebih besar dari 100 MB. Untuk file PDF, batasnya adalah 50 MB.

Kode berikut mengupload file, lalu menggunakan file tersebut dalam panggilan ke
`generateContent`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=["Describe this audio clip", myfile]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
defer client.Files.Delete(ctx, file.Name)

resp, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", []*genai.Content{
  {
    Parts: []*genai.Part{
      genai.NewPartFromFile(*file),
      genai.NewPartFromText("Describe this audio clip"),
    },
  },
}, nil)

if err != nil {
    log.Fatal(err)
}

printResponse(resp)
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Mendapatkan metadata untuk file

Anda dapat memverifikasi bahwa API berhasil menyimpan file yang diupload dan mendapatkan metadatanya dengan memanggil `files.get`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await ai.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}

gotFile, err := client.Files.Get(ctx, file.Name)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Got file:", gotFile.Name)
```

### REST

```
# file_info.json was created in the upload example
name=$(jq ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/files/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri
```

## Mencantumkan file yang diupload

Kode berikut mendapatkan daftar semua file yang diupload:

### Python

```
from google import genai

client = genai.Client()

print('My files:')
for f in client.files.list():
    print(' ', f.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const listResponse = await ai.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Go

```
for file, err := range client.Files.All(ctx) {
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(file.Name)
}
```

### REST

```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Menghapus file yang diupload

File akan otomatis dihapus setelah 48 jam. Anda juga dapat menghapus file yang diupload secara manual:

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await ai.files.delete({ name: fileName });
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
client.Files.Delete(ctx, file.Name)
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/files/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Informasi penggunaan

Anda dapat menggunakan Files API untuk mengupload dan berinteraksi dengan file media. Files API memungkinkan Anda menyimpan file hingga 20 GB per project, dengan ukuran maksimum per file sebesar 2 GB. File disimpan selama 48 jam.

Selama waktu tersebut, Anda dapat menggunakan API untuk mendapatkan metadata tentang file. Namun,
Anda tidak dapat mendownload file yang diupload pengguna. Anda dapat mendownload file yang dihasilkan oleh model, seperti video, menggunakan metode `files.download`. Files API tersedia tanpa biaya di semua wilayah tempat Gemini API tersedia.

## Strategi penulisan perintah file

Bagian ini memberikan panduan dan praktik terbaik untuk menggunakan file media dengan
perintah untuk Gemini API.

Kemampuan untuk menggunakan berbagai jenis data dalam perintah memberi Anda lebih banyak
fleksibilitas dalam hal tugas yang dapat Anda selesaikan dengan Gemini API. Misalnya, Anda dapat mengirimkan foto makanan lezat ke model dan memintanya untuk menulis
blog singkat tentang makanan tersebut.

|  |  |
| --- | --- |
| **Perintah** | **Respons** |
| Tulis postingan blog yang singkat dan menarik berdasarkan gambar ini. Postingan ini harus menyertakan deskripsi makanan dalam foto dan menceritakan perjalanan saya dalam menyiapkan makanan.   Cookie | Menyiapkan makanan adalah cara yang bagus untuk menghemat waktu dan uang, serta dapat membantu Anda makan lebih sehat. Makanan ini adalah contoh yang bagus untuk makanan sehat dan lezat yang dapat disiapkan dengan mudah sebelumnya.  Hidangan ini menyajikan nasi merah, sayuran panggang, dan ayam teriyaki. Beras merah adalah karbohidrat kompleks dan sehat yang akan memberi Anda energi berkelanjutan. Sayuran panggang adalah cara yang bagus untuk mendapatkan asupan vitamin dan mineral harian, dan ayam teriyaki adalah pilihan yang lezat dan kaya protein.  Makanan ini juga sangat mudah disiapkan. Cukup masak beras merah, panggang sayuran, dan masak ayam teriyaki. Setelah semuanya matang, bagi menjadi beberapa wadah penyiapan makanan dan simpan di dalam kulkas. Anda bisa mengambil wadah dan pergi di pagi hari yang sibuk!  Jika Anda mencari makanan sehat dan lezat yang dapat disiapkan dengan mudah sebelumnya, makanan ini adalah pilihan yang bagus. Sup ini kaya akan nutrisi dan rasa, serta pasti akan membuat Anda merasa kenyang dan puas.  Selamat menyiapkan makanan yang sehat dan lezat. |

Jika Anda mengalami kesulitan mendapatkan output yang diinginkan dari perintah yang menggunakan
file media, ada beberapa strategi yang dapat membantu Anda mendapatkan hasil yang
diinginkan. Bagian berikut memberikan pendekatan desain dan tips pemecahan masalah untuk meningkatkan kualitas perintah yang menggunakan input multimodal.

Anda dapat meningkatkan kualitas perintah multimodal dengan mengikuti praktik terbaik berikut:

- ### [Dasar-dasar desain perintah](#specific-instructions)

  - **Berikan petunjuk yang spesifik**: Buat petunjuk yang jelas dan ringkas untuk meminimalkan kemungkinan salah tafsir.
  - **Tambahkan beberapa contoh ke perintah Anda:** Gunakan contoh few-shot yang realistis untuk mengilustrasikan hal yang ingin Anda capai.
  - **Uraikan langkah demi langkah**: Bagi tugas yang kompleks menjadi sub-sasaran yang mudah dikelola, sehingga memandu model melalui prosesnya.
  - **Tentukan format output**: Dalam perintah Anda, minta output dalam format yang Anda inginkan, seperti markdown, JSON, HTML, dan lainnya.
  - **Tempatkan gambar Anda terlebih dahulu untuk perintah satu gambar**: Meskipun Gemini dapat menangani input gambar dan teks dalam urutan apa pun, untuk perintah yang berisi satu gambar, Gemini mungkin akan berperforma lebih baik jika gambar (atau video) tersebut ditempatkan sebelum perintah teks. Namun, untuk perintah yang memerlukan gambar yang sangat disisipkan dengan teks agar masuk akal, gunakan urutan yang paling alami.
- ### [Memecahkan masalah perintah multimodal](#troubleshooting)

  - **Jika model tidak mengambil informasi dari bagian gambar yang relevan:** Berikan petunjuk tentang aspek gambar yang Anda inginkan untuk diambil informasinya oleh perintah.
  - **Jika output model terlalu umum (tidak cukup disesuaikan dengan input gambar/video):** Di awal perintah, coba minta model untuk mendeskripsikan gambar atau video sebelum memberikan petunjuk tugas, atau coba minta model untuk merujuk pada apa yang ada dalam gambar.
  - **Untuk memecahkan masalah bagian mana yang gagal:** Minta model untuk mendeskripsikan gambar, atau minta model untuk menjelaskan penalarannya, guna mengukur pemahaman awal model.
  - **Jika perintah Anda menghasilkan konten halusinasi:** Coba turunkan setelan temperature atau minta model memberikan deskripsi yang lebih singkat agar model tidak terlalu banyak mengekstrapolasi detail tambahan.
  - **Menyesuaikan parameter sampling:** Bereksperimenlah dengan berbagai setelan temperature dan pilihan top-k untuk menyesuaikan kreativitas model.

### Berikan petunjuk yang spesifik

Perintah akan memberikan hasil terbaik jika jelas dan mendetail. Jika Anda memiliki
output tertentu, sebaiknya sertakan persyaratan tersebut dalam perintah
untuk memastikan Anda mendapatkan output yang diinginkan.

Untuk gambar papan bandara ini, meminta model untuk sekadar "mendeskripsikan gambar ini" dapat menghasilkan deskripsi umum. Jika Anda memerlukan model untuk mengurai waktu dan kota dari gambar, Anda dapat menyertakan permintaan tersebut langsung dalam prompt.

| Perintah | Respons model |
| --- | --- |
| Jelaskan gambar ini. | Gambar menampilkan papan kedatangan dan keberangkatan bandara. |

| **Perintah yang diperbarui** | **Respons yang lebih baik** |
| --- | --- |
| Jadwal perjalanan Parse the time and city from the airport board shown in this image into a list. | - 10.50 Moskow - 11.05 Edinburgh - 11.05 London - 11.10 Bucharest - 11.30 Kiev - 11.35 Dublin - 11.45 East Midlands - 12.15 Sofia - 12.30 London - 12.30 Newcastle - 12.40 St Petersburg - 12.40 London - 12.45 Manchester |

### Tambahkan beberapa contoh

Model Gemini dapat menerima beberapa input yang dapat digunakan sebagai contoh untuk memahami output yang Anda inginkan. Menambahkan contoh ini dapat membantu model mengidentifikasi pola dan menerapkan
hubungan antara gambar dan respons yang diberikan ke contoh baru. Hal ini juga disebut
pembelajaran "few-shot".

Dalam contoh di bawah, output awal ditulis dalam bentuk kalimat, dan juga berisi
negara (Brasil). Misalnya, Anda menginginkan output dalam format atau gaya yang berbeda, dan Anda hanya menginginkan kota, bukan negara. Menambahkan contoh few-shot ke perintah Anda dapat mengarahkan model
untuk merespons sesuai keinginan Anda.

| **Perintah** | **Respons model** |
| --- | --- |
| Jadwal perjalanan Tentukan kota beserta tempat terkenalnya. | Tempat terkenal ini adalah patung Kristus Penebus di Rio de Janeiro, Brasil. |

| **Perintah yang diperbarui** | **Respons yang lebih baik** |
| --- | --- |
| Tentukan kota beserta tempat terkenalnya. colosseum | kota: Roma, tempat terkenal: Colosseum. |
| Kota Terlarang | kota: Beijing, bangunan terkenal: Kota Terlarang |
| forbidden-city | kota: Rio de Janeiro, tempat terkenal: Patung Kristus Penebus |

### Uraikan langkah demi langkah

Untuk tugas kompleks seperti yang memerlukan pemahaman dan penalaran visual, sebaiknya bagi tugas menjadi langkah-langkah yang lebih kecil dan lebih mudah. Atau, Anda juga dapat langsung meminta model untuk “berpikir langkah demi langkah” dalam perintah Anda.

| Perintah | Respons model |
| --- | --- |
| Kapan tisu toilet saya akan habis? | Segera, Anda hanya memiliki sisa 3 rol. |

| **Perintah yang diperbarui** | **Respons yang lebih baik** |
| --- | --- |
| 1. Pertama, hitung berapa banyak gulungan tisu toilet dalam gambar ini.  2. Kemudian, tentukan berapa banyak tisu toilet yang digunakan orang pada umumnya per hari.  3. Hitung berapa lama tisu toilet ini akan bertahan. | 1. Ada 3 rol tisu toilet dalam gambar ini.  2. Seseorang biasanya menggunakan sekitar 20 lembar tisu toilet per hari.  3. Jika setiap rol berisi 200 lembar, setiap rol akan bertahan selama sekitar 10 hari. Jadi, 3 rol akan bertahan selama sekitar satu bulan. |

Soal matematika atau jenis soal cerita lainnya adalah kandidat yang bagus untuk meminta
model berpikir langkah demi langkah.

| **Perintah** | **Respons** |
| --- | --- |
| Berapa suku ke-4 dalam deret tersebut? | -135 |

Respons dari model salah. Beberapa cara untuk meningkatkan kualitasnya adalah dengan meminta
model mengurai masalah sebelum menjawab perintah.

| **Perintah** | **Respons** |
| --- | --- |
| Uraikan formula dalam gambar terlebih dahulu.  Kemudian, berdasarkan rumus tersebut, jawab "apa suku ke-4 dalam deret tersebut?". | *Klik untuk meluaskan hasil* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. Masukkan n = 4 ke dalam rumus:  $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. Kita tidak tahu nilai b(3), jadi substitusikan n = 3 ke dalam rumus:  $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. Kita tidak tahu nilai b(2), jadi substitusikan n = 2 ke dalam rumus:  $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. Kita tahu nilai b(1) adalah 15, jadi masukkan ke dalam rumus:  $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. Setelah mengetahui nilai b(2), substitusikan ke dalam formula untuk b(3):  $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. Setelah kita mengetahui nilai b(3), substitusikan ke dalam rumus untuk b(4):  $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Oleh karena itu, suku ke-4 dalam deret ini adalah -405. |

Respons model ini sudah benar. Sekarang, untuk membuat responsnya lebih efisien,
Anda dapat meminta model untuk berpikir langkah demi langkah.

| **Perintah yang diperbarui** | **Respons yang lebih baik** |
| --- | --- |
| Berapa suku ke-4 dalam deret tersebut? Berpikirlah secara berurutan. | Suku pertama adalah 15.  Suku kedua adalah b(1) \* (-3) = 15 \* (-3) = -45.  Suku ketiga adalah b(2) \* (-3) = -45 \* (-3) = 135.  Suku keempat adalah b(3) \* (-3) = 135 \* (-3) = -405. |

### Menentukan format output

Masalah umum adalah perlunya output model dalam format tertentu
(misalnya, markdown, JSON, HTML), terutama jika output model perlu
diserap oleh tugas downstream. Anda dapat mencoba menghasilkan output dalam format tersebut
dengan menginstruksikan model untuk melakukannya dalam prompt. Berikut adalah dua contoh:

| Perintah | Respons model |
| --- | --- |
| Uraikan tabel dalam gambar ini ke dalam format markdown | | Subject | Status | Time | Start date | Due on |  | ------- | ------ | ---- | ---------- | ------ |  | Matematika | Selesai | 1,5 jam | 29/11/2023 | 1/12/2023 |  | Geografi | Selesai | 30 mnt | 2/12/2023 | 4/12/2023 |  | Physics | In progress | 2 hrs | 12/3/2023 | 12/5/2023 |  | Biology | Not started | 6 hrs | 11/2/2016 | 12/6/2023 | |

| **Perintah** | **Respons model** |
| --- | --- |
| Berikan daftar semua atribut berikut:  bahan, jenis masakan, vegetarian atau tidak, dalam format JSON | ```` ```json ````  `{`  `"ingredients": [`  `"rice",`  `"shrimp",`  `"clams",`  `"mussels",`  `"peas",`  `"tomatoes",`  `"onions",`  `"garlic",`  `"olive oil",`  `"paprika",`  `"salt",`  `"pepper"`  `],`  `"type of cuisine": "Spanish",`  `"vegetarian": false`  `}`  ```` ``` ```` |

### Letakkan gambar Anda terlebih dahulu untuk perintah satu gambar

Meskipun Gemini dapat menafsirkan gambar dan teks dalam urutan apa pun dalam perintah, menempatkan
satu gambar sebelum perintah teks dapat memberikan hasil yang lebih baik.
Dalam contoh berikut, Anda akan melihat gambar muncul sebelum teks di
setiap perintah.

### Memecahkan masalah perintah multimodal

Anda mungkin perlu memecahkan masalah perintah jika tidak mendapatkan respons yang bermanfaat. Berikut beberapa strategi yang dapat Anda coba.

#### Jika model tidak mengambil informasi dari bagian gambar yang relevan

Untuk mendapatkan respons yang lebih spesifik, Anda dapat menunjukkan aspek gambar mana yang Anda inginkan untuk diambil informasinya oleh perintah guna memberikan respons.

| Perintah | Respons model |
| --- | --- |
| Berapa hari popok ini akan bertahan untuk bayi? | Popok akan bertahan selama 198 hari sebelum habis. |

| **Perintah yang diperbarui** | **Respons yang lebih baik** |
| --- | --- |
| Berapa lama popok ini akan bertahan sebelum habis?  Gunakan berat yang ditampilkan pada kotak untuk menentukan usia anak, dan gunakan jumlah total popok dalam kotak.  Bagi jumlah total dengan jumlah popok yang digunakan anak per hari. | Kotak berisi 198 popok. Kotak tersebut menyatakan bahwa popok tersebut ditujukan untuk anak dengan berat 10-17 kg.  Anak-anak dalam rentang berat ini rata-rata berusia antara 1 dan 2 tahun.  Anak berusia 2 tahun biasanya menggunakan 6 popok per hari, sehingga popok akan bertahan sekitar 33 hari (198/6). |

#### Jika output model terlalu umum dan tidak cukup disesuaikan dengan input gambar

Untuk membantu model menyesuaikan responsnya dengan gambar, coba minta model untuk mendeskripsikan
gambar sebelum melakukan tugas penalarannya.

| Perintah | Respons model |
| --- | --- |
| Apa kesamaan di antara gambar-gambar ini? | Keempat gambar tersebut adalah contoh fotografi lanskap. |

| **Perintah yang diperbarui** | **Respons yang lebih baik** |
| --- | --- |
| Pertama, jelaskan isi setiap gambar secara mendetail. Apa kesamaan di antara gambar-gambar ini? | Gambar pertama menunjukkan seseorang sedang mengemas koper. Gambar kedua menunjukkan lorong kosong di pusat perbelanjaan. Gambar ketiga menampilkan gulungan tisu toilet. Gambar keempat menunjukkan laut yang gelap dan berbadai.  Kesamaan di antara gambar-gambar ini adalah semuanya merupakan contoh ruang liminal. Ruang liminal adalah tempat atau situasi yang berada di antara dua tempat atau situasi lainnya. Masalah ini sering kali ditandai dengan rasa ketidakpastian atau ambiguitas.  Gambar pertama menunjukkan orang tersebut berada di antara rumah dan perjalanan. Gambar kedua menunjukkan lorong di antara dua toko. Gambar ketiga adalah tisu toilet, yang dapat mewakili kamar mandi. Kamar mandi adalah ruang transisi antara ranah pribadi dan publik. Ini adalah tempat kita mempersiapkan diri untuk memasuki atau meninggalkan dunia luar.  Gambar keempat menunjukkan laut yang berada di antara kondisi tenang dan badai.  Ruang liminal bisa terasa menarik sekaligus meresahkan. Stasiun bisa menjadi tempat awal yang baru atau tempat akhir. Taman bisa menjadi tempat untuk merenung atau tempat untuk beraktivitas. |

Anda juga dapat mencoba meminta model secara eksplisit untuk merujuk pada apa yang ada dalam gambar.

| **Perintah yang diperbarui** | **Respons yang lebih baik** |
| --- | --- |
| Apa kesamaan di antara gambar-gambar ini? Refer to what's in the images in your response. | Semua gambar terkait dengan perjalanan. Gambar pertama menunjukkan seseorang sedang mengemas koper, gambar kedua menunjukkan lorong kosong di pusat perbelanjaan, gambar ketiga menunjukkan tumpukan tisu toilet, dan gambar keempat menunjukkan laut yang gelap dan berbadai.  Gambar-gambar ini semuanya terkait dengan perjalanan karena semuanya adalah hal yang dibutuhkan atau digunakan orang saat bepergian. Gambar pertama menunjukkan seseorang sedang mengemas koper, yang merupakan sesuatu yang dilakukan orang saat mereka akan melakukan perjalanan. Gambar kedua menunjukkan lorong kosong di pusat perbelanjaan, yang merupakan tempat orang sering pergi untuk membeli barang untuk perjalanan mereka. Gambar ketiga menunjukkan tumpukan tisu toilet, yang sering digunakan orang saat bepergian. Gambar keempat menunjukkan laut yang gelap dan berbadai, yang sering ditemui orang saat bepergian. |

Tips yang sama berlaku untuk output kreatif dari gambar. Dalam contoh berikut dengan
kelinci, meminta model secara eksplisit untuk menyertakan aspek dari gambar dapat
meningkatkan output.

| Perintah | Respons model |
| --- | --- |
| Bisakah Anda menulis puisi tentang gambar ini? | Kelinci kecil, lembut dan cokelat,  Melompat-lompat di ladang, naik dan turun.  Telingamu panjang, ekormu kecil,  Kamu makhluk paling lucu di antara semuanya.  Kau mengunyah rumput, hijau dan manis,  Dan melompat pergi saat melihatku.  Tapi aku akan selalu jadi temanmu,  Kelinci kecil, sampai akhir. |

| **Perintah yang diperbarui** | **Respons yang lebih baik** |
| --- | --- |
| Bisakah Anda menulis puisi deskriptif dan dramatis tentang gambar ini dan menyertakan lokasinya? | Kelinci kecil di padang rumput,  Telinganya panjang, sangat tajam.  Apa yang kau lihat di sana,  Di kejauhan, tempat kau menatap?  Apakah itu biru laut,  Berkilau dalam rona matahari?  Atau deburan ombak yang menderu,  Irama yang Anda sukai?  Kelinci kecil, katakan padaku,  Apa yang membuatmu begitu tertarik?  Apakah angin laut yang asin,  Atau jeritan burung camar yang menyenangkan?  Mungkin karena luasnya,  Dunia yang begitu besar dan kecil.  Tempat impian dapat berkeliaran,  Dan petualangan dapat disemai.  Kelinci kecil, aku ingin tahu apa mimpimu,  Saat kamu duduk di rumput, begitu tenang.  Apakah Anda ingin menjelajahi laut dalam,  Atau tetap di darat, tempat Anda bisa melompat?  Apa pun itu, kelinci kecil,  Pertahankan percikan keajaiban itu agar tetap menyala terang.  Karena dalam mimpi dan aspirasimu,  Ada dunia yang menunggu kreasimu. |

#### Memecahkan masalah bagian perintah yang gagal

Mungkin sulit untuk mengetahui apakah perintah gagal karena model
tidak **memahami gambar** sejak awal, atau apakah model memahami gambar
tetapi tidak melakukan **langkah-langkah penalaran** yang benar setelahnya.
Untuk memperjelas alasan tersebut, minta model untuk mendeskripsikan apa yang ada dalam gambar.

Dalam contoh berikut, jika model merespons dengan camilan yang tampaknya mengejutkan
saat dipasangkan dengan teh (misalnya, popcorn), Anda dapat memecahkan masalah terlebih dahulu untuk menentukan
apakah model mengenali dengan benar bahwa gambar tersebut berisi teh.

| Perintah | Perintah untuk pemecahan masalah |
| --- | --- |
| Apa camilan yang bisa saya buat dalam 1 menit yang cocok dengan ini? | Jelaskan apa yang ada dalam gambar ini. |

Strategi lainnya adalah meminta model untuk menjelaskan penalarannya. Hal ini dapat membantu Anda
mempersempit bagian penalaran mana yang rusak, jika ada.

| Perintah | Perintah untuk pemecahan masalah |
| --- | --- |
| Apa camilan yang bisa saya buat dalam 1 menit yang cocok dengan ini? | Apa camilan yang bisa saya buat dalam 1 menit yang cocok dengan ini? Harap jelaskan alasannya. |

## Langkah berikutnya

- Coba tulis perintah multimodal Anda sendiri menggunakan [Google AI
  Studio](http://aistudio.google.com?hl=id).
- Untuk mengetahui informasi tentang cara menggunakan Gemini Files API untuk
  mengupload file media dan menyertakannya dalam perintah Anda, lihat
  panduan [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=id), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=id), dan
  [Pemrosesan dokumen](https://ai.google.dev/gemini-api/docs/document-processing?hl=id).
- Untuk panduan selengkapnya tentang desain prompt, seperti menyesuaikan parameter pengambilan sampel, lihat halaman [Strategi prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-26 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-26 UTC."],[],[]]
