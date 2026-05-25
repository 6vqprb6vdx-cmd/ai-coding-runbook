---
source_url: https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=id
fetched_at: 2026-05-25T13:03:49.029262+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Menggunakan kunci Gemini API

Untuk menggunakan Gemini API, Anda memerlukan kunci API. Halaman ini menguraikan cara membuat dan mengelola kunci di Google AI Studio serta cara menyiapkan lingkungan untuk menggunakannya dalam kode Anda.

[Membuat atau melihat Kunci Gemini API](https://aistudio.google.com/app/apikey?hl=id)

## Kunci API

Anda dapat membuat dan mengelola semua Kunci Gemini API dari halaman
[Google AI Studio](https://aistudio.google.com/app/apikey?hl=id) **Kunci API**.

Setelah memiliki kunci API, Anda memiliki opsi berikut untuk terhubung ke Gemini API:

- [Menetapkan kunci API sebagai variabel lingkungan](#set-api-env-var)
- [Memberikan kunci API secara eksplisit](#provide-api-key-explicitly)

Untuk pengujian awal, Anda dapat meng-hardcode kunci API, tetapi hal ini hanya boleh bersifat sementara karena tidak aman. Anda dapat menemukan contoh untuk meng-hardcode kunci API
di bagian [Memberikan kunci API secara eksplisit](#provide-api-key-explicitly).

## Project Google Cloud

[Project Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=id)
sangat penting untuk menggunakan layanan Google Cloud (seperti Gemini API),
mengelola penagihan, dan mengontrol kolaborator serta izin. Google AI Studio menyediakan antarmuka ringan ke project Google Cloud Anda.

Jika belum membuat project, Anda harus membuat project baru atau mengimpor project dari Google Cloud ke Google AI Studio. Halaman **Project** di Google AI Studio akan menampilkan semua kunci yang memiliki izin yang memadai untuk menggunakan Gemini API. Lihat bagian [mengimpor project](#import-projects) untuk mengetahui petunjuknya.

### Project default

Untuk pengguna baru, setelah menyetujui Persyaratan Layanan, Google AI Studio akan membuat Project Google Cloud dan Kunci API default, untuk kemudahan penggunaan. Anda dapat mengganti nama project ini di Google AI Studio dengan membuka tampilan **Project** di **Dasbor**, mengklik tombol setelan 3 titik di samping project, dan memilih **Ganti nama project**. Pengguna yang sudah ada, atau pengguna yang sudah memiliki Akun Google Cloud tidak akan memiliki project default yang dibuat.

## Mengimpor project

Setiap kunci Gemini API dikaitkan dengan project Google Cloud. Secara default, Google AI Studio tidak menampilkan semua Project Cloud Anda. Anda harus mengimpor project yang diinginkan dengan menelusuri nama atau project ID di dialog **Impor Project**. Untuk melihat daftar lengkap project yang dapat Anda akses, buka Konsol Cloud.

Jika belum mengimpor project, ikuti langkah-langkah berikut untuk mengimpor project Google Cloud dan membuat kunci:

1. Buka [Google AI Studio](https://aistudio.google.com?hl=id).
2. Buka **Dasbor** dari panel sisi kiri.
3. Pilih **Project**.
4. Pilih tombol **Impor project** di halaman **Project**.
5. Telusuri dan pilih project Google Cloud yang ingin Anda impor, lalu pilih tombol **Impor**.

Setelah project diimpor, buka halaman **Kunci API** dari menu **Dasbor** dan buat kunci API di project yang baru saja Anda impor.

## Batasan

Berikut adalah batasan pengelolaan kunci API dan project Google Cloud di Google AI Studio.

- Anda dapat membuat maksimum 10 project sekaligus dari halaman **Project** Google AI Studio.
- Anda dapat memberi nama dan mengganti nama project serta kunci.
- Halaman **Kunci API** dan **Project** menampilkan maksimum 100 kunci dan 50 project.
- Hanya kunci API yang tidak memiliki batasan, atau dibatasi ke Generative Language API yang ditampilkan.

Untuk akses pengelolaan tambahan ke project Anda, termasuk mengubah dan
membatasi kunci API, buka
[halaman kredensial Konsol Google Cloud](https://console.cloud.google.com/apis/credentials?hl=id).
Di Konsol Cloud, Anda dapat memilih project, mengklik kunci API yang ada, lalu membatasinya ke **Generative Language API**.

## Menetapkan kunci API sebagai variabel lingkungan

Jika Anda menetapkan variabel lingkungan `GEMINI_API_KEY` atau `GOOGLE_API_KEY`, kunci API akan otomatis diambil oleh klien saat menggunakan salah satu
[library Gemini API](https://ai.google.dev/gemini-api/docs/libraries?hl=id). Sebaiknya tetapkan hanya satu dari variabel tersebut, tetapi jika keduanya ditetapkan, `GOOGLE_API_KEY` akan diprioritaskan.

Jika menggunakan REST API, atau JavaScript di browser, Anda harus memberikan kunci API secara eksplisit.

Berikut cara menetapkan kunci API secara lokal sebagai variabel lingkungan `GEMINI_API_KEY` dengan sistem operasi yang berbeda.

### Linux/macOS - Bash

Bash adalah konfigurasi terminal Linux dan macOS yang umum. Anda dapat memeriksa apakah memiliki file konfigurasi untuknya dengan menjalankan perintah berikut:

```
~/.bashrc
```

Jika responsnya adalah "No such file or directory", Anda harus membuat file ini dan membukanya dengan menjalankan perintah berikut, atau menggunakan `zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

Selanjutnya, Anda harus menetapkan kunci API dengan menambahkan perintah ekspor berikut:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Setelah menyimpan file, terapkan perubahan dengan menjalankan:

```
source ~/.bashrc
```

### macOS - Zsh

Zsh adalah konfigurasi terminal Linux dan macOS yang umum. Anda dapat memeriksa apakah memiliki file konfigurasi untuknya dengan menjalankan perintah berikut:

```
~/.zshrc
```

Jika responsnya adalah "No such file or directory", Anda harus membuat file ini dan membukanya dengan menjalankan perintah berikut, atau menggunakan `bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

Selanjutnya, Anda harus menetapkan kunci API dengan menambahkan perintah ekspor berikut:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Setelah menyimpan file, terapkan perubahan dengan menjalankan:

```
source ~/.zshrc
```

### Windows

1. Telusuri "Environment Variables" di kotak penelusuran.
2. Pilih untuk mengubah **System Settings**. Anda mungkin harus mengonfirmasi bahwa Anda ingin melakukannya.
3. Dalam dialog setelan sistem, klik tombol berlabel **Environment Variables**.
4. Di bagian **User variables** (untuk pengguna saat ini) atau **System variables** (berlaku untuk semua pengguna yang menggunakan mesin), klik **New...**
5. Tentukan nama variabel sebagai `GEMINI_API_KEY`. Tentukan Kunci Gemini API Anda sebagai nilai variabel.
6. Klik **OK** untuk menerapkan perubahan.
7. Buka sesi terminal baru (cmd atau Powershell) untuk mendapatkan variabel baru.

## Memberikan kunci API secara eksplisit

Dalam beberapa kasus, Anda mungkin ingin memberikan kunci API secara eksplisit. Contoh:

- Anda melakukan panggilan API sederhana dan lebih suka meng-hardcode kunci API.
- Anda menginginkan kontrol eksplisit tanpa harus mengandalkan penemuan otomatis variabel lingkungan oleh library Gemini API
- Anda menggunakan lingkungan yang tidak mendukung variabel lingkungan (misalnya, web) atau Anda melakukan panggilan REST.

Di bawah ini adalah contoh cara memberikan kunci API secara eksplisit menggunakan Interactions API:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.5-flash", 
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Menjaga keamanan kunci API

Perlakukan kunci Gemini API Anda seperti sandi. Jika kunci tersebut disusupi, orang lain dapat menggunakan kuota project Anda, dikenai biaya (jika penagihan diaktifkan), dan mengakses data pribadi Anda, seperti file.

### Aturan keamanan penting

- **Jaga kerahasiaan kunci**: Kunci API untuk Gemini dapat mengakses data sensitif yang bergantung pada
  aplikasi Anda.

  - **Jangan pernah meng-commit kunci API ke kontrol sumber.** Jangan check in kunci API Anda ke sistem kontrol versi seperti Git.
  - **Jangan pernah menampilkan kunci API di sisi klien.** Jangan gunakan kunci API Anda secara langsung di aplikasi web atau seluler dalam produksi. Kunci dalam kode sisi klien (termasuk library JavaScript/TypeScript dan panggilan REST) dapat diekstrak.
- **Batasi akses**: Batasi penggunaan kunci API ke alamat IP, perujuk HTTP, atau aplikasi Android/iOS tertentu jika memungkinkan.
- **Batasi penggunaan**: Aktifkan hanya API yang diperlukan untuk setiap kunci.
- **Lakukan audit rutin**: Audit kunci API Anda secara rutin dan putar kunci tersebut
  secara berkala.

### Praktik terbaik

- **Gunakan panggilan sisi server dengan kunci API** Cara paling aman untuk menggunakan kunci API adalah dengan memanggil Gemini API dari aplikasi sisi server tempat kunci dapat dijaga kerahasiaannya.
- **Gunakan token sementara untuk akses sisi klien (khusus Live API):** Untuk akses sisi klien langsung ke Live API, Anda dapat menggunakan token sementara. Token ini memiliki risiko keamanan yang lebih rendah dan dapat cocok untuk penggunaan produksi. Tinjau
  [panduan token sementara](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=id) untuk mengetahui informasi selengkapnya.
- **Pertimbangkan untuk menambahkan batasan pada kunci Anda:** Anda dapat membatasi izin kunci
  dengan menambahkan [batasan kunci API](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=id#add-api-restrictions).
  Tindakan ini akan meminimalkan potensi kerusakan jika kunci bocor.

Untuk beberapa praktik terbaik umum, Anda juga dapat meninjau
[artikel dukungan ini](https://support.google.com/googleapi/answer/6310037?hl=id).

## Memecahkan masalah pembuatan kunci API

Di Google AI Studio, tombol **Buat kunci API** mungkin tampak tidak tersedia, dengan
pesan: "*Anda tidak memiliki izin untuk membuat kunci dalam project ini*".

Hal ini terjadi jika Anda tidak memiliki izin yang diperlukan dalam project untuk membuat kunci baru:

- **`resourcemanager.projects.get`**: Memungkinkan AI Studio memverifikasi keberadaan project.
- **`apikeys.keys.create`**: Memungkinkan pembuatan kunci API itu sendiri.
- **`serviceusage.services.enable`**: Diperlukan untuk memastikan Gemini API aktif di project.

Untuk memperbaiki izin Anda, minta admin project, atau admin organisasi Anda jika project tersebut milik [organisasi](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=id), untuk memberi Anda peran dengan izin yang tercantum di atas (seperti Editor Project atau peran kustom).

Jika tidak memiliki akses administratif ke project, Anda dapat membuat project baru yang tidak terkait dengan organisasi untuk membuat kunci.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
