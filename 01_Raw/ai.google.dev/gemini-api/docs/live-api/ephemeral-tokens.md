---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=id
fetched_at: 2026-05-25T12:57:08.284758+00:00
title: "Ephemeral tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Ephemeral tokens

Token sementara adalah token autentikasi dengan masa berlaku singkat untuk mengakses Gemini
API melalui [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Kredensial ini dirancang untuk meningkatkan keamanan saat Anda terhubung langsung dari perangkat pengguna ke API (implementasi [klien ke server](https://ai.google.dev/gemini-api/docs/live?hl=id#implementation-approach)). Seperti kunci API standar, token sementara dapat diekstrak dari aplikasi sisi klien seperti browser web atau aplikasi seluler. Namun, karena token sementara cepat habis masa berlakunya dan dapat dibatasi, token ini secara signifikan mengurangi risiko keamanan di lingkungan produksi. Anda harus menggunakannya saat mengakses Live API langsung dari aplikasi sisi klien untuk meningkatkan keamanan kunci API.

## Cara kerja token sementara

Berikut cara kerja token sementara secara umum:

1. Klien Anda (misalnya, aplikasi web) melakukan autentikasi dengan backend Anda.
2. Backend Anda meminta token sementara dari layanan penyediaan Gemini API.
3. Gemini API mengeluarkan token yang memiliki masa aktif singkat.
4. Backend Anda mengirimkan token ke klien untuk koneksi WebSocket ke Live
   API. Anda dapat melakukannya dengan menukar kunci API Anda dengan token sementara.
5. Kemudian, klien menggunakan token seolah-olah itu adalah kunci API.

![Ringkasan token sementara](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=id)

Hal ini meningkatkan keamanan karena meskipun diekstrak, token hanya berlaku dalam waktu singkat,
tidak seperti kunci API yang berlaku dalam waktu lama yang di-deploy di sisi klien. Karena klien mengirim data langsung ke Gemini, hal ini juga meningkatkan latensi dan menghindari backend Anda perlu mem-proxy data real time.

## Membuat token sementara

Berikut adalah contoh sederhana cara mendapatkan token sementara dari Gemini.
Secara default, Anda akan memiliki waktu 1 menit untuk memulai sesi Live API baru menggunakan token
dari permintaan ini (`newSessionExpireTime`), dan 30 menit untuk mengirim pesan melalui
koneksi tersebut (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

Untuk batasan nilai `expireTime`, default, dan spesifikasi kolom lainnya, lihat
[referensi API](https://ai.google.dev/api/live?hl=id#ephemeral-auth-tokens).
Dalam jangka waktu `expireTime`, Anda harus
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=id#session-resumption) untuk
menghubungkan kembali panggilan setiap 10 menit (hal ini dapat dilakukan dengan token yang sama meskipun
`uses: 1`).

Anda juga dapat mengunci token sementara ke serangkaian konfigurasi. Hal ini
mungkin berguna untuk lebih meningkatkan keamanan aplikasi Anda dan menyimpan
petunjuk sistem di sisi server.

### Python

```
from google import genai

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

Anda juga dapat mengunci subset kolom, lihat [dokumentasi SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
untuk mengetahui info selengkapnya.

## Menghubungkan ke Live API dengan token sementara

Setelah memiliki token sementara, Anda dapat menggunakannya seolah-olah itu adalah kunci API (tetapi
ingat, token tersebut hanya berfungsi untuk live API, dan hanya dengan API versi `v1alpha`).

Penggunaan token sementara hanya menambah nilai saat men-deploy aplikasi yang mengikuti pendekatan [implementasi client-to-server](https://ai.google.dev/gemini-api/docs/live?hl=id#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Lihat [Mulai menggunakan Live API](https://ai.google.dev/gemini-api/docs/live?hl=id) untuk contoh lainnya.

## Praktik terbaik

- Tetapkan durasi habis masa berlaku yang singkat menggunakan parameter `expire_time`.
- Masa berlaku token akan berakhir, sehingga memerlukan inisiasi ulang proses penyediaan.
- Verifikasi autentikasi yang aman untuk backend Anda sendiri. Token sementara hanya akan seaman metode autentikasi backend Anda.
- Secara umum, hindari penggunaan token sementara untuk koneksi backend-ke-Gemini,
  karena jalur ini biasanya dianggap aman.

## Batasan

Token sementara hanya kompatibel dengan [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id) saat ini.

## Langkah berikutnya

- Baca [referensi](https://ai.google.dev/api/live?hl=id#ephemeral-auth-tokens) Live API tentang token sementara untuk mengetahui informasi selengkapnya.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-25 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-25 UTC."],[],[]]
