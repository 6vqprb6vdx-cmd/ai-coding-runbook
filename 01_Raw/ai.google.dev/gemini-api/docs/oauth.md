---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=id
fetched_at: 2026-10-19T05:42:58.881706+00:00
title: "Panduan memulai Authentication dengan OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Panduan memulai Authentication dengan OAuth

Cara termudah untuk mengautentikasi Gemini API adalah dengan mengonfigurasi kunci API, seperti yang dijelaskan dalam [panduan memulai Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=id). Jika memerlukan kontrol akses yang lebih ketat,
Anda dapat menggunakan OAuth. Panduan ini akan membantu
Anda menyiapkan autentikasi dengan OAuth.

Panduan ini menggunakan pendekatan autentikasi yang disederhanakan dan sesuai
untuk lingkungan pengujian. Untuk lingkungan produksi, pelajari
[autentikasi dan otorisasi](https://developers.google.com/workspace/guides/auth-overview?hl=id)
sebelum
[memilih kredensial akses](https://developers.google.com/workspace/guides/create-credentials?hl=id#choose_the_access_credential_that_is_right_for_you)
yang sesuai untuk aplikasi Anda.

## Tujuan

- Menyiapkan project cloud untuk OAuth
- Menyiapkan kredensial default aplikasi
- Mengelola kredensial dalam program Anda, bukan menggunakan `gcloud auth`

## Prasyarat

Untuk menjalankan quickstart ini, Anda memerlukan:

- [Project Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=id)
- [Penginstalan gcloud CLI lokal](https://cloud.google.com/sdk/docs/install?hl=id)

## Menyiapkan project cloud

Untuk menyelesaikan panduan memulai ini, Anda harus menyiapkan project Cloud terlebih dahulu.

### 1. Mengaktifkan API

Sebelum menggunakan Google API, Anda harus mengaktifkannya di project Google Cloud.

- Di Konsol Google Cloud, aktifkan Google Generative Language API.

  [Mengaktifkan API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=id)

### 2. Mengonfigurasi layar izin OAuth

Selanjutnya, konfigurasi layar izin OAuth project dan tambahkan diri Anda sebagai pengguna pengujian. Jika Anda telah menyelesaikan langkah ini untuk project Cloud, lewati ke bagian berikutnya.

1. Di Konsol Google Cloud, buka **Menu** >
   **Google Auth platform** > **Overview**.

   [Buka platform Google Auth](https://console.developers.google.com/auth/overview?hl=id)
2. Isi formulir konfigurasi project dan tetapkan jenis pengguna ke **Eksternal**
   di bagian **Audiens**.
3. Lengkapi formulir lainnya, setujui persyaratan Kebijakan Data Pengguna, lalu
   klik **Buat**.
4. Untuk saat ini, Anda dapat melewati penambahan cakupan dan mengklik **Simpan dan Lanjutkan**. Pada
   masa mendatang, saat membuat aplikasi untuk digunakan di luar organisasi Google Workspace, Anda harus menambahkan dan memverifikasi cakupan otorisasi yang diperlukan aplikasi Anda.
5. Tambahkan pengguna pengujian:

   1. Buka
      [halaman Audiens](https://console.developers.google.com/auth/audience?hl=id) di
      platform Google Auth.
   2. Di bagian **Pengguna pengujian**, klik **Tambahkan pengguna**.
   3. Masukkan alamat email Anda dan pengguna uji resmi lainnya, lalu
      klik **Simpan**.

### 3. Mengizinkan kredensial untuk aplikasi desktop

Untuk mengautentikasi sebagai pengguna akhir dan mengakses data pengguna di aplikasi Anda, Anda perlu membuat satu atau beberapa Client ID OAuth 2.0. Client ID digunakan untuk mengidentifikasi
satu aplikasi ke server OAuth Google. Jika aplikasi Anda berjalan di beberapa platform, Anda harus membuat ID klien terpisah untuk setiap platform.

1. Di Konsol Google Cloud, buka **Menu** > **Google Auth platform** >
   **Clients**.

   [Buka Kredensial](https://console.developers.google.com/auth/clients?hl=id)
2. Klik **Buat Klien**.
3. Klik **Jenis aplikasi** > **Aplikasi desktop**.
4. Di kolom **Name**, ketik nama untuk kredensial. Nama ini hanya
   ditampilkan di Konsol Google Cloud.
5. Klik **Buat**. Layar OAuth client created akan muncul, menampilkan Client ID dan Client secret baru Anda.
6. Klik **Oke**. Kredensial yang baru dibuat akan muncul di bagian **Client ID OAuth 2.0.**
7. Klik tombol download untuk menyimpan file JSON. File akan disimpan sebagai
   `client_secret_<identifier>.json`, lalu ganti namanya menjadi `client_secret.json`
   dan pindahkan ke direktori kerja Anda.

## Menyiapkan Kredensial Default Aplikasi

Untuk mengonversi file `client_secret.json` menjadi kredensial yang dapat digunakan, teruskan
lokasinya ke argumen
`--client-id-file` perintah `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

Penyiapan project yang disederhanakan dalam tutorial ini memicu dialog **"Google belum memverifikasi aplikasi ini"**. Hal ini normal, pilih **"continue"**.

Hal ini menempatkan token yang dihasilkan di lokasi yang sudah dikenal sehingga dapat diakses
oleh `gcloud` atau library klien.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

Setelah Anda menyetel Kredensial Default Aplikasi (ADC), library
klien dalam sebagian besar bahasa hanya memerlukan sedikit atau tidak memerlukan bantuan untuk menemukannya.

### Curl

Cara tercepat untuk menguji apakah ini berfungsi adalah dengan menggunakannya untuk mengakses REST API menggunakan curl:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

Di Python, library klien akan menemukannya secara otomatis:

```
pip install google-genai
```

Skrip minimal untuk mengujinya mungkin adalah:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## Mengelola kredensial sendiri [Python]

Dalam banyak kasus, Anda tidak akan memiliki perintah `gcloud` yang tersedia untuk membuat token akses dari ID Klien (`client_secret.json`). Google menyediakan library dalam banyak bahasa untuk memungkinkan Anda mengelola proses tersebut dalam aplikasi. Bagian ini menunjukkan prosesnya, dalam Python. Ada contoh prosedur serupa yang setara untuk bahasa lain, yang tersedia di [dokumentasi Drive API](https://developers.google.com/drive/api/quickstart/python?hl=id)

### 1. Instal library yang diperlukan

Instal library klien Google untuk Python, dan library klien Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. Menulis pengelola kredensial

Untuk meminimalkan jumlah klik yang harus Anda lakukan di layar otorisasi, buat file bernama `load_creds.py` di direktori kerja Anda untuk menyimpan file `token.json` yang dapat digunakan kembali nanti, atau diperbarui jika masa berlakunya habis.

Mulai dengan
kode berikut untuk mengonversi file `client_secret.json` menjadi token yang dapat digunakan dengan
`genai.configure`:

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. Menulis program Anda

Sekarang buat `script.py` Anda:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. Menjalankan program Anda

Di direktori kerja Anda, jalankan contoh:

```
python script.py
```

Saat pertama kali dijalankan, skrip akan membuka jendela browser dan meminta Anda
untuk mengizinkan akses.

1. Jika belum login ke Akun Google, Anda akan diminta untuk
   login. Jika Anda login ke beberapa akun, **pastikan untuk memilih
   akun yang Anda tetapkan sebagai "Akun Pengujian" saat mengonfigurasi project.**
2. Informasi otorisasi disimpan dalam sistem file, sehingga saat Anda menjalankan kode contoh pada lain waktu, Anda tidak akan dimintai otorisasi.

Anda telah berhasil menyiapkan autentikasi.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-10 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-10 UTC."],[],[]]
