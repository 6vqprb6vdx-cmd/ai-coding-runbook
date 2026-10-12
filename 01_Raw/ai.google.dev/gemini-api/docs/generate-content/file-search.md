---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-search?hl=id
fetched_at: 2026-10-12T07:02:48.619294+00:00
title: "Penelusuran file \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Penelusuran file

Gemini API memungkinkan Retrieval-Augmented Generation ("RAG") melalui alat Penelusuran File. Penelusuran File mengimpor, membagi, dan mengindeks data Anda untuk memungkinkan pengambilan informasi yang relevan dengan cepat berdasarkan perintah yang diberikan. Informasi yang diambil ini kemudian digunakan sebagai konteks untuk model, sehingga model dapat memberikan jawaban yang lebih akurat dan relevan. Penelusuran file juga dapat
memberikan kemampuan multimodal dengan embedding teks yang didukung oleh
`gemini-embedding-001`, dan embedding gambar/multimodal yang didukung oleh `gemini-embedding-2`.

Penyimpanan file dan pembuatan sematan pada waktu kueri gratis, dan Anda hanya akan membayar
pembuatan sematan saat pertama kali mengindeks file dan biaya token input / output model Gemini
yang normal. Paradigma penagihan baru ini membuat Alat Penelusuran File lebih mudah dan hemat biaya untuk dibangun dan diskalakan. Lihat bagian
[harga](#pricing) untuk mengetahui detailnya.

## Mengupload langsung ke penyimpanan Penelusuran File

Contoh ini menunjukkan cara mengupload file secara langsung ke [penyimpanan penelusuran file](https://ai.google.dev/api/file-search/file-search-stores?hl=id#method:-media.uploadtofilesearchstore):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.upload_to_file_search_store(
  file='sample.txt',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'display-file-name',
  }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.uploadToFileSearchStore({
    file: 'file.txt',
    fileSearchStoreName: fileSearchStore.name,
    config: {
      displayName: 'file-name',
    }
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation });
  }

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Can you tell me about [insert question]",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [fileSearchStore.name]
          }
        }
      ]
    }
  });

  console.log(response.text);
}

run();
```

Periksa referensi API untuk [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=id#method:-media.uploadtofilesearchstore) untuk mengetahui informasi selengkapnya.

## Mengimpor file

Atau, Anda dapat mengupload file yang ada dan [mengimpornya ke penyimpanan penelusuran file Anda](https://ai.google.dev/api/file-search/file-search-stores?hl=id#method:-filesearchstores.importfile):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'name': 'display_file_name'})

file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { name: 'file-name' }
  });

  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.importFile({
    fileSearchStoreName: fileSearchStore.name,
    fileName: sampleFile.name
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation: operation });
  }

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Can you tell me about [insert question]",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [fileSearchStore.name]
          }
        }
      ]
    }
  });

  console.log(response.text);
}

run();
```

Periksa referensi API untuk [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=id#method:-filesearchstores.importfile) untuk mengetahui informasi selengkapnya.

## Konfigurasi pemotongan

Saat Anda mengimpor file ke penyimpanan Penelusuran File, file tersebut akan otomatis dipecah menjadi beberapa bagian, disematkan, diindeks, dan diupload ke penyimpanan Penelusuran File Anda. Jika Anda
membutuhkan kontrol yang lebih besar atas strategi chunking, Anda dapat menentukan setelan
[`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=id#request-body_5)
untuk menetapkan jumlah maksimum token per chunk dan jumlah maksimum token yang tumpang-tindih.

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    config={
        'chunking_config': {
          'white_space_config': {
            'max_tokens_per_chunk': 200,
            'max_overlap_tokens': 20
          }
        }
    }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

print("Custom chunking complete.")
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

let operation = await ai.fileSearchStores.uploadToFileSearchStore({
  file: 'file.txt',
  fileSearchStoreName: fileSearchStore.name,
  config: {
    displayName: 'file-name',
    chunkingConfig: {
      whiteSpaceConfig: {
        maxTokensPerChunk: 200,
        maxOverlapTokens: 20
      }
    }
  }
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 5000));
  operation = await ai.operations.get({ operation });
}
console.log("Custom chunking complete.");
```

Untuk menggunakan penyimpanan Penelusuran File, teruskan sebagai alat ke metode `generateContent`, seperti yang ditunjukkan dalam contoh [Upload](#upload) dan [Impor](#importing-files).

## Cara kerjanya

Penelusuran File menggunakan teknik yang disebut penelusuran semantik untuk menemukan informasi yang relevan dengan perintah pengguna. Tidak seperti penelusuran berbasis kata kunci standar, penelusuran semantik memahami makna dan konteks kueri Anda.

Saat Anda mengimpor file, file tersebut akan dikonversi menjadi representasi numerik yang disebut
[embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=id), yang menangkap makna semantik
konten yang diupload. Embedding ini disimpan dalam database Penelusuran File khusus.
Saat Anda membuat kueri, kueri tersebut juga dikonversi menjadi embedding. Kemudian, sistem
melakukan Penelusuran File untuk menemukan potongan dokumen yang paling mirip dan relevan
dari penyimpanan Penelusuran File.

Tidak ada Time To Live (TTL) untuk sematan;
sematan akan tetap ada hingga dihapus secara manual, atau saat model tidak digunakan lagi. Namun, file akan dihapus setelah 48 jam.

Berikut perincian proses penggunaan File Search
`uploadToFileSearchStore` API:

1. **Membuat penyimpanan Penelusuran File**: Penyimpanan Penelusuran File berisi data yang diproses dari file Anda. Ini adalah penampung persisten untuk embedding yang akan digunakan oleh penelusuran semantik.
2. **Mengupload file dan mengimpor ke penyimpanan Penelusuran File**: Mengupload file dan mengimpor hasil ke penyimpanan Penelusuran File secara bersamaan. Tindakan ini akan membuat objek `File` sementara, yang merupakan referensi ke dokumen mentah Anda. Data tersebut kemudian dibagi-bagi, diubah menjadi embedding Penelusuran File, dan diindeks. Objek `File`
   dihapus setelah 48 jam, sedangkan data yang diimpor ke penyimpanan Penelusuran File
   akan disimpan tanpa batas waktu hingga Anda memilih untuk menghapusnya.
3. **Kueri dengan Penelusuran File**: Terakhir, Anda menggunakan alat `FileSearch` dalam panggilan `generateContent`. Dalam konfigurasi alat, Anda menentukan
   `FileSearchRetrievalResource`, yang mengarah ke `FileSearchStore` yang ingin
   Anda telusuri. Hal ini memberi tahu model untuk melakukan penelusuran semantik di penyimpanan Penelusuran File tertentu tersebut guna menemukan informasi yang relevan untuk mendasari responsnya.

![Proses pengindeksan dan pembuatan kueri Penelusuran File](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=id)

Proses pengindeksan dan pembuatan kueri Penelusuran File

Dalam diagram ini, garis putus-putus dari *Documents* ke *Embedding model*
(menggunakan [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=id))
merepresentasikan `uploadToFileSearchStore` API (melewati *File storage*).
Jika tidak, menggunakan [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id) untuk membuat
dan mengimpor file secara terpisah akan memindahkan proses pengindeksan dari *Dokumen* ke
*Penyimpanan file*, lalu ke *Model sematan*.

## Menyimpan Penelusuran File

Penyimpanan Penelusuran File adalah container untuk embedding dokumen Anda. Meskipun file mentah yang diupload melalui File API akan dihapus setelah 48 jam, data yang diimpor ke penyimpanan Penelusuran File akan disimpan tanpa batas waktu hingga Anda menghapusnya secara manual. Anda dapat membuat beberapa penyimpanan Penelusuran File untuk mengatur dokumen Anda. `FileSearchStore` API memungkinkan Anda membuat, mencantumkan, mendapatkan, dan menghapus untuk mengelola penyimpanan penelusuran file Anda. Nama toko Penelusuran File memiliki cakupan global.

Berikut beberapa contoh cara mengelola toko Penelusuran File Anda:

### Python

```
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'my-file_search-store-123',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

for file_search_store in client.file_search_stores.list():
    print(file_search_store)

my_file_search_store = client.file_search_stores.get(name='fileSearchStores/my-file_search-store-123')

client.file_search_stores.delete(name='fileSearchStores/my-file_search-store-123', config={'force': True})
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: 'my-file_search-store-123',
    embeddingModel: 'models/gemini-embedding-2'
  }
});

const fileSearchStores = await ai.fileSearchStores.list();
for await (const store of fileSearchStores) {
  console.log(store);
}

const myFileSearchStore = await ai.fileSearchStores.get({
  name: 'fileSearchStores/my-file_search-store-123'
});

await ai.fileSearchStores.delete({
  name: 'fileSearchStores/my-file_search-store-123',
  config: { force: true }
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"
```

## Dokumen Penelusuran File

Anda dapat mengelola setiap dokumen di penyimpanan file dengan API
[File Search Documents](https://ai.google.dev/api/file-search/documents?hl=id) untuk `list` setiap dokumen
di penyimpanan penelusuran file, `get` informasi tentang dokumen, dan `delete`
dokumen menurut nama.

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
```

### JavaScript

```
const documents = await ai.fileSearchStores.documents.list({
  parent: 'fileSearchStores/my-file_search-store-123'
});
for await (const doc of documents) {
  console.log(doc);
}

const fileSearchDocument = await ai.fileSearchStores.documents.get({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc',
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"
```

## Metadata file

Anda dapat menambahkan metadata kustom ke file untuk membantu memfilter atau memberikan
konteks tambahan. Metadata adalah sekumpulan key-value pair.

### Python

```
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    custom_metadata=[
        {"key": "author", "string_value": "Robert Graves"},
        {"key": "year", "numeric_value": 1934}
    ]
)
```

### JavaScript

```
let operation = await ai.fileSearchStores.importFile({
  fileSearchStoreName: fileSearchStore.name,
  fileName: sampleFile.name,
  config: {
    customMetadata: [
      { key: "author", stringValue: "Robert Graves" },
      { key: "year", numericValue: 1934 }
    ]
  }
});
```

Hal ini berguna jika Anda memiliki beberapa dokumen di penyimpanan Penelusuran File dan ingin
menelusuri hanya sebagian dokumen tersebut.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Tell me about the book 'I, Claudius'",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name],
                    metadata_filter="author=Robert Graves",
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Tell me about the book 'I, Claudius'",
  config: {
    tools: [
      {
        fileSearch: {
          fileSearchStoreNames: [fileSearchStore.name],
          metadataFilter: 'author="Robert Graves"',
        }
      }
    ]
  }
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=${GEMINI_API_KEY}" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
            "contents": [{
                "parts":[{"text": "Tell me about the book I, Claudius"}]
            }],
            "tools": [{
                "file_search": {
                    "file_search_store_names":["'$STORE_NAME'"],
                    "metadata_filter": "author = \"Robert Graves\""
                }
            }]
        }' 2> /dev/null > response.json

cat response.json
```

Panduan tentang penerapan sintaksis filter daftar untuk `metadata_filter` dapat ditemukan
di [google.aip.dev/160](https://google.aip.dev/160)

## Penelusuran File Multimodal

Penelusuran File Multimodal memungkinkan Anda menyematkan dan menelusuri gambar secara native, sehingga memungkinkan aplikasi RAG multimodal yang kaya.

### Mengonfigurasi model embedding

Saat membuat `FileSearchStore`, Anda harus mengganti model embedding default khusus teks untuk menggunakan model multimodal. Gunakan `models/gemini-embedding-2` untuk memproses teks dan gambar.

### Python

```
store = client.file_search_stores.create(
    config={
        "display_name": "Multimodal Catalog",
        "embedding_model": "models/gemini-embedding-2",
    }
)
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: "Multimodal Catalog",
    embeddingModel: "models/gemini-embedding-2",
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "display_name": "Multimodal Catalog",
      "embedding_model": "models/gemini-embedding-2"
    }'
```

### Upload gambar

Setelah membuat toko dengan model penyematan multimodal, Anda dapat mengupload
file gambar secara langsung menggunakan API upload yang sama seperti yang dijelaskan dalam
[Mengupload langsung ke toko Penelusuran File](#upload) atau [Mengimpor file](#importing-files).

**Persyaratan file gambar:**

- File gambar harus memiliki resolusi maksimal 4K x 4K piksel.
- Format yang didukung adalah PNG, JPEG.

## Kutipan

Saat Anda menggunakan Penelusuran File, respons model dapat menyertakan kutipan yang menentukan bagian dokumen yang Anda upload yang digunakan untuk membuat jawaban. Hal ini membantu dalam pemeriksaan fakta dan verifikasi.

Anda dapat mengakses informasi kutipan melalui atribut `grounding_metadata`
respons.

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

Untuk mengetahui informasi mendetail tentang struktur metadata perujukan, lihat contoh dalam [File Search
cookbook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb)
atau [bagian perujukan dalam dokumentasi Grounding dengan Google
Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id#attributing_sources_with_inline_citations).

### Nomor halaman

Saat Anda menggunakan Penelusuran File dengan dokumen yang memiliki halaman (seperti PDF), respons model dapat menyertakan nomor halaman tempat informasi ditemukan.
Anda dapat mengakses informasi ini melalui atribut `page_number` dari
`retrieved_context`.

### Python

```
# Iterate through citations and check for page numbers
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.page_number:
       print(f"Cited Page: {chunk.retrieved_context.page_number}")
```

### JavaScript

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.pageNumber) {
    console.log(`Cited Page: ${chunk.retrievedContext.pageNumber}`);
  }
}
```

### Kutipan media

Saat model mereferensikan potongan gambar selama pembuatan, API akan menampilkan kutipan dalam metadata perujukan yang menyertakan `media_id`. Anda dapat menggunakan ID ini untuk mendownload potongan gambar persis yang dirujuk model. `media_id` ini bersifat persisten di beberapa panggilan penelusuran, sehingga Anda dapat mengambil gambar yang sama atau menyimpannya dalam cache menggunakan ID dengan andal.

Cuplikan berikut adalah contoh respons REST:

```
"groundingMetadata": {
  "groundingChunks": [
    {
      "retrievedContext": {
        "title": "product_image",
        "fileSearchStore": "fileSearchStores/my-store-123",
        "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
      }
    }
  ]
}
```

Cuplikan kode berikut menunjukkan cara mengambil `media_id` dan
mendownload media:

### Python

```
# Iterate through citations and download media if present
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.media_id:
       print(f"Cited Media ID: {chunk.retrieved_context.media_id}")
       # Download the blob using the SDK
       blob_content = client.file_search_stores.download_media(
           media_id=chunk.retrieved_context.media_id
       )
       # Save blob_content to file...
```

### JavaScript

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.mediaId) {
    console.log(`Cited Media ID: ${chunk.retrievedContext.mediaId}`);
    const blobContent = await ai.fileSearchStores.downloadMedia(chunk.retrievedContext.mediaId);
    // Save blobContent to file...
  }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Metadata kustom dalam data perujukan

Jika telah menambahkan metadata kustom ke file, Anda dapat mengaksesnya di metadata perujukan respons model. Hal ini berguna untuk meneruskan
konteks tambahan (seperti URL, nomor halaman, atau penulis) dari dokumen sumber
ke logika aplikasi Anda. Setiap `grounding_chunk` di
`retrieved_context` berisi metadata kustom ini.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Tell me about [insert question]",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

for chunk in response.candidates[0].grounding_metadata.grounding_chunks:
    if chunk.retrieved_context:
        print(f"Text: {chunk.retrieved_context.text}")
        if chunk.retrieved_context.custom_metadata:
            for metadata in chunk.retrieved_context.custom_metadata:
                print(f"Metadata Key: {metadata.key}")
                print(f"Value: {metadata.string_value or metadata.numeric_value}")
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Tell me about [insert question]",
  config: {
    tools: [
      {
        fileSearch: {
          fileSearchStoreNames: [fileSearchStore.name]
        }
      }
    ]
  }
});

const groundingMetadata = response.candidates[0].groundingMetadata;
groundingMetadata.groundingChunks.forEach((chunk) => {
  if (chunk.retrievedContext) {
    console.log(`Text: ${chunk.retrievedContext.text}`);
    if (chunk.retrievedContext.customMetadata) {
      chunk.retrievedContext.customMetadata.forEach((metadata) => {
        console.log(`Metadata Key: ${metadata.key}`);
        console.log(`Value: ${metadata.stringValue || metadata.numericValue}`);
      });
    }
  }
});
```

### REST

```
{
  "candidates": [
    {
      "content": { ... },
      "grounding_metadata": {
        "grounding_chunks": [
          {
            "retrieved_context": {
              "text": "...",
              "title": "...",
              "uri": "...",
              "custom_metadata": [
                {
                  "key": "author",
                  "string_value": "Robert Graves"
                },
                {
                  "key": "year",
                  "numeric_value": 1934
                }
              ]
            }
          }
        ],
        "grounding_supports": [ ... ]
      }
    }
  ]
}
```

## Output terstruktur

Mulai dari model Gemini 3, Anda dapat menggabungkan alat penelusuran file dengan
[output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is the minimum hourly wage in Tokyo right now?",
    config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[file_search_store.name]
                        )
                    )
                ],
                response_format={"text": {"mime_type": "application/json", "schema": Money.model_json_schema()}}
      )
)
result = Money.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { z } from "zod";

const moneySchema = z.object({
  amount: z.string().describe("The numerical part of the amount."),
  currency: z.string().describe("The currency of amount."),
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the minimum hourly wage in Tokyo right now?",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [file_search_store.name],
          },
        },
      ],
      responseFormat: { text: { mimeType: "application/json", schema: z.toJSONSchema(moneySchema) } },
    },
  });

  const result = moneySchema.parse(JSON.parse(response.text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "What is the minimum hourly wage in Tokyo right now?"}]
    }],
    "tools": [
      {
        "fileSearch": {
          "fileSearchStoreNames": ["$FILE_SEARCH_STORE_NAME"]
        }
      }
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "amount": {"type": "string", "description": "The numerical part of the amount."},
                "currency": {"type": "string", "description": "The currency of amount."}
  }
}
},
            "required": ["amount", "currency"]
        }
    }
  }'
```

## Model yang didukung

Model berikut mendukung Penelusuran File:

| Model | Penelusuran File |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=id) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id) | ✔️ |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ |
| [Pratinjau Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ |

## Kombinasi alat yang didukung

Model Gemini 3 mendukung penggabungan alat bawaan (seperti Penelusuran File) dengan alat kustom (panggilan fungsi). Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).

## Jenis file yang didukung

Penelusuran File mendukung berbagai format file, yang tercantum di bagian berikut.

### Jenis file aplikasi

- `application/dart`
- `application/ecmascript`
- `application/json`
- `application/ms-java`
- `application/msword`
- `application/pdf`
- `application/sql`
- `application/typescript`
- `application/vnd.curl`
- `application/vnd.dart`
- `application/vnd.ibm.secure-container`
- `application/vnd.jupyter`
- `application/vnd.ms-excel`
- `application/vnd.oasis.opendocument.text`
- `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.template`
- `application/x-csh`
- `application/x-hwp`
- `application/x-hwp-v5`
- `application/x-latex`
- `application/x-php`
- `application/x-powershell`
- `application/x-sh`
- `application/x-shellscript`
- `application/x-tex`
- `application/x-zsh`
- `application/xml`
- `application/zip`

### Jenis file teks

- `text/1d-interleaved-parityfec`
- `text/RED`
- `text/SGML`
- `text/cache-manifest`
- `text/calendar`
- `text/cql`
- `text/cql-extension`
- `text/cql-identifier`
- `text/css`
- `text/csv`
- `text/csv-schema`
- `text/dns`
- `text/encaprtp`
- `text/enriched`
- `text/example`
- `text/fhirpath`
- `text/flexfec`
- `text/fwdred`
- `text/gff3`
- `text/grammar-ref-list`
- `text/hl7v2`
- `text/html`
- `text/javascript`
- `text/jcr-cnd`
- `text/jsx`
- `text/markdown`
- `text/mizar`
- `text/n3`
- `text/parameters`
- `text/parityfec`
- `text/php`
- `text/plain`
- `text/provenance-notation`
- `text/prs.fallenstein.rst`
- `text/prs.lines.tag`
- `text/prs.prop.logic`
- `text/raptorfec`
- `text/rfc822-headers`
- `text/rtf`
- `text/rtp-enc-aescm128`
- `text/rtploopback`
- `text/rtx`
- `text/sgml`
- `text/shaclc`
- `text/shex`
- `text/spdx`
- `text/strings`
- `text/t140`
- `text/tab-separated-values`
- `text/texmacs`
- `text/troff`
- `text/tsv`
- `text/tsx`
- `text/turtle`
- `text/ulpfec`
- `text/uri-list`
- `text/vcard`
- `text/vnd.DMClientScript`
- `text/vnd.IPTC.NITF`
- `text/vnd.IPTC.NewsML`
- `text/vnd.a`
- `text/vnd.abc`
- `text/vnd.ascii-art`
- `text/vnd.curl`
- `text/vnd.debian.copyright`
- `text/vnd.dvb.subtitle`
- `text/vnd.esmertec.theme-descriptor`
- `text/vnd.exchangeable`
- `text/vnd.familysearch.gedcom`
- `text/vnd.ficlab.flt`
- `text/vnd.fly`
- `text/vnd.fmi.flexstor`
- `text/vnd.gml`
- `text/vnd.graphviz`
- `text/vnd.hans`
- `text/vnd.hgl`
- `text/vnd.in3d.3dml`
- `text/vnd.in3d.spot`
- `text/vnd.latex-z`
- `text/vnd.motorola.reflex`
- `text/vnd.ms-mediapackage`
- `text/vnd.net2phone.commcenter.command`
- `text/vnd.radisys.msml-basic-layout`
- `text/vnd.senx.warpscript`
- `text/vnd.sosi`
- `text/vnd.sun.j2me.app-descriptor`
- `text/vnd.trolltech.linguist`
- `text/vnd.wap.si`
- `text/vnd.wap.sl`
- `text/vnd.wap.wml`
- `text/vnd.wap.wmlscript`
- `text/vtt`
- `text/wgsl`
- `text/x-asm`
- `text/x-bibtex`
- `text/x-boo`
- `text/x-c`
- `text/x-c++hdr`
- `text/x-c++src`
- `text/x-cassandra`
- `text/x-chdr`
- `text/x-coffeescript`
- `text/x-component`
- `text/x-csh`
- `text/x-csharp`
- `text/x-csrc`
- `text/x-cuda`
- `text/x-d`
- `text/x-diff`
- `text/x-dsrc`
- `text/x-emacs-lisp`
- `text/x-erlang`
- `text/x-gff3`
- `text/x-go`
- `text/x-haskell`
- `text/x-java`
- `text/x-java-properties`
- `text/x-java-source`
- `text/x-kotlin`
- `text/x-lilypond`
- `text/x-lisp`
- `text/x-literate-haskell`
- `text/x-lua`
- `text/x-moc`
- `text/x-objcsrc`
- `text/x-pascal`
- `text/x-pcs-gcd`
- `text/x-perl`
- `text/x-perl-script`
- `text/x-python`
- `text/x-python-script`
- `text/x-r-markdown`
- `text/x-rsrc`
- `text/x-rst`
- `text/x-ruby-script`
- `text/x-rust`
- `text/x-sass`
- `text/x-scala`
- `text/x-scheme`
- `text/x-script.python`
- `text/x-scss`
- `text/x-setext`
- `text/x-sfv`
- `text/x-sh`
- `text/x-siesta`
- `text/x-sos`
- `text/x-sql`
- `text/x-swift`
- `text/x-tcl`
- `text/x-tex`
- `text/x-vbasic`
- `text/x-vcalendar`
- `text/xml`
- `text/xml-dtd`
- `text/xml-external-parsed-entity`
- `text/yaml`

## Batasan

- **Live API:** Penelusuran File tidak didukung di
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id).
- **Ketidakcocokan alat:** Penelusuran File tidak dapat digabungkan dengan alat lain seperti [Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id), [Konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id), dll. saat ini.

### Batas kapasitas

File Search API memiliki batas berikut untuk memastikan stabilitas layanan:

- **Ukuran file maksimum / batas per dokumen**: 100 MB
- **Total ukuran penyimpanan Penelusuran File project** (berdasarkan tingkat pengguna):
  - **Gratis**: 1 GB
  - **Tingkat 1**: 10 GB
  - **Tingkat 2**: 100 GB
  - **Tingkat 3**: 1 TB
- **Rekomendasi**: Batasi ukuran setiap penyimpanan Penelusuran File hingga di bawah 20 GB untuk memastikan latensi pengambilan yang optimal.

## Harga

- Anda akan ditagih untuk penyematan pada waktu pengindeksan berdasarkan [harga penyematan](https://ai.google.dev/gemini-api/docs/pricing?hl=id#gemini-embedding-2) yang ada.
- Penyimpanan tidak dikenai biaya.
- Embedding waktu kueri tidak dikenai biaya.
- Token dokumen yang diambil dikenai biaya sebagai [token konteks](https://ai.google.dev/gemini-api/docs/tokens?hl=id) reguler.

## Langkah berikutnya

- Baca referensi API untuk [Penyimpanan Penelusuran File](https://ai.google.dev/api/file-search/file-search-stores?hl=id) dan [Dokumen](https://ai.google.dev/api/file-search/documents?hl=id) Penelusuran File.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-09 UTC."],[],[]]
