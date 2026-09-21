---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=id
fetched_at: 2026-09-21T06:00:17.058573+00:00
title: "Panduan perintah Lyria \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Panduan perintah Lyria

Gemini API menawarkan dua cara untuk membuat musik dengan Lyria:

- **Lyria 3.5 & Lyria 3 Clip**: Pembuatan non-streaming untuk klip berdurasi 30 detik atau lagu lengkap dengan lirik dan vokal. Lihat [Membuat musik dengan Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=id).
- **Lyria RealTime**: Streaming musik interaktif real-time dan pengarahan langsung melalui WebSockets. Lihat [Pembuatan musik real-time dengan Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=id).

Kedua model merespons perintah teks deskriptif, terminologi musik, dan petunjuk struktural. Panduan ini membahas cara menulis perintah yang efektif untuk pembuatan batch dan pengarahan real-time.

## Dasar-dasar perintah

Perintah Anda dapat berupa frasa pendek:

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

Atau deskripsi terstruktur dan mendetail:

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

Perintah singkat dan mendetail menghasilkan hasil yang kuat. Gunakan strategi berikut untuk memandu model menghasilkan suara yang persis seperti yang Anda inginkan.

## Genre dan gaya

Awali perintah Anda dengan genre utama. Anda dapat menggabungkan genre untuk menciptakan hibrida yang unik:

- Perpaduan metal dan hip-hop
- Death metal yang dipadukan dengan vokal opera
- Musik kamar klasik dengan elemen drone elektronik gelap
- Musik dance elektronik (EDM) modern yang dipadukan dengan Europop

Anda juga dapat menentukan era musik atau varian regional:

- Hip-hop boom-bap awal 1990-an
- Pop yé-yé Prancis tahun 1960-an
- Post-punk dan new wave tahun 1980-an
- R&B mainstream 2000-an
- Minimal techno Berlin atau hyphy Bay Area

### Kata kunci genre

Gunakan istilah genre yang diakui ini dalam perintah Anda untuk Lyria 3.5 dan Lyria RealTime:

- **Elektronik & Dance**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **Hip-Hop & R&B**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **Rock & Alternatif**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **Jazz, Soul & Funk**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **Folk & Tradisional**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **Klasik & Akustik**: `Baroque, Orchestral Score, Piano Ballad`

## Instrumen dan tekstur

Lyria secara otomatis memilih instrumentasi yang sesuai untuk genre yang diminta. Jika Anda menginginkan instrumen tertentu atau kombinasi yang tidak biasa, nyatakan secara eksplisit:

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

Jelaskan suara dan interaksi instrumen untuk mengatur mood dan tekstur:

- Garis bas 303 yang terdistorsi menembus hi-hat yang tajam dan rapat
- Pad synth analog yang hangat dan membesar di bawah gitar akustik yang jelas dan dekat
- Dinding suara yang dibangun dari beberapa lapisan gitar fuzz, dengan vokal yang jauh dan penuh reverb

### Kata kunci instrumen

- **Keyboard & Synthesizer**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **Bass & Drums**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **Gitar & Senar**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **Tiup & Logam**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **Perkusi**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## Struktur dan pengaturan waktu lagu

Untuk Lyria 3.5, tentukan progres lagu menggunakan tag atau panah:

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- Mulai dengan intro piano yang tenang, bangun menjadi bait yang energik, jeda sejenak, lalu meledak menjadi chorus.

Anda dapat mengarahkan dinamika dan transisi energi:

- Bangun ketegangan melalui pra-chorus, lalu turunkan ke keheningan sebelum chorus yang eksplosif
- Crescendo bertahap di sepanjang lagu, menambahkan satu instrumen per bagian
- Berhenti mendadak setelah jembatan, diikuti dengan chorus a cappella

Anda juga dapat meminta penanda waktu tertentu:

- Bangun hingga beat drop pada detik ke-12
- Contoh vokal berulang setiap 4 birama
- Bagian chorus dimulai pada detik ke-22

## Lirik dan vokal

Lyria 3.5 menghasilkan trek vokal dengan lirik secara default. Anda dapat memberikan lirik Anda sendiri, meminta model untuk membuatnya, atau meminta trek instrumental.

### Menggunakan lirik Anda sendiri

Sertakan lirik Anda langsung dalam perintah di bawah header `Lyrics:`. Beri tag pada setiap bagian untuk memandu penyampaian lisan:

```
Lyrics:

[Intro]
Ooooh, yeah

[Verse 1]
Early morning rain on the window pane
City lights wash away the pain
Walking down this empty street again

[Chorus]
We keep moving on (moving on)
Until the morning light
Everything will be alright
```

Gunakan tanda kurung untuk vokal latar, gema, atau ad-lib, seperti `(moving on)`.

### Mengarahkan lirik yang dihasilkan

Saat meminta Lyria 3.5 menulis lirik, buat garis besar narasi, emosi, atau frasa utama:

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

Untuk genre musik elektronik dan dance, minta hook vokal pendek yang berulang:

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### Penyampaian vokal dan profil penyanyi

Tentukan gender, rentang vokal, dan timbre untuk hasil yang akurat:

- **Soprano Wanita**: Timbre yang jernih dan seperti kristal dengan penyampaian yang lincah dan melambung. Nada cerah yang mampu menghasilkan tekstur lapang dan berhembus.
- **Alto Perempuan**: Rentang bawah yang kaya, hangat, dan serak. Timbre berasap dengan suara dada yang penuh jiwa dan beresonansi.
- **Tenor Pria**: Cerah, tajam, dan penuh semangat. Timbre muda dengan kekuatan vokal tinggi yang menembus campuran suara padat.
- **Bariton Pria**: Suara dada yang dalam, sehalus beludru dengan penyampaian yang hangat, menenangkan, dan merdu.
- **Weathered Rocker**: Timbre serak dan kasar yang mengingatkan pada rock alternatif tahun 1990-an. Intensitas emosional mentah dengan nada tinggi yang tegang.

### Efek vokal non-lirik

Anda juga dapat meminta dialog lisan, potongan vokal, dan efek sampling:

- Suara siaran radio vintage memperkenalkan lagu sebelum irama dimulai
- Suara yang diucapkan berbisik tepat sebelum drop, diikuti dengan synth yang bersemangat
- Sampel vokal yang dipotong dan diubah nada suaranya berputar sebagai elemen ritme instrumental

## Parameter musik

Sempurnakan perintah Anda dengan properti musik standar:

- **Tempo (BPM)**: Setel tempo secara langsung (misalnya, `120 BPM`, `slow tempo around 72 BPM`, `fast 160 BPM`).
- **Kunci dan Skala**: Tentukan kunci root dan tonalitas (misalnya, `in G major`, `in D minor`, `in C pentatonic`).
- **Suasana Hati dan Atmosfer**: Gunakan kata sifat emosional deskriptif:
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## Membuat perintah Lyria RealTime

Lyria RealTime menggunakan **prompt berbobot**, bukan string prompt monolitik tunggal. Hal ini memungkinkan Anda memadukan beberapa pengaruh musik secara dinamis dan mengarahkan musik secara berkelanjutan melalui koneksi WebSocket.

### Struktur perintah berbobot

Setiap perintah berbobot terdiri dari frasa teks deskriptif dan bobot floating point:

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### Strategi pengarahan real-time

- **Menggabungkan genre**: Gabungkan gaya yang berbeda dengan menetapkan bobot yang seimbang:
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **Transisi dinamis**: Untuk mentransisikan musik dengan lancar, sesuaikan bobot perintah dari waktu ke waktu:
  1. Diawali dengan `chill jazz piano (weight: 1.0)`.
  2. Tambahkan `electronic breakbeat (weight: 0.3)` secara bertahap.
  3. Tingkatkan `electronic breakbeat` menjadi `0.8` sambil menurunkan `chill jazz piano` menjadi `0.3`.
- **Mengatur elemen berlapis**: Pisahkan tag instrumen dan tag suasana hati agar Anda dapat menyesuaikannya secara terpisah:
  - Perintah 1: `bossa nova guitar (weight: 0.9)`
  - Perintah 2: `warm acoustic bass (weight: 0.7)`
  - Perintah 3: `subtle vinyl crackle (weight: 0.3)`

## Contoh perintah

### Contoh Lyria 3.5

- **Lo-Fi Study Beat**:
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **Pop Anthem**:
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **Cinematic Cyberpunk**:
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Setelan kemudi RealTime Lyria

```
# Initial high-energy groove
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="techno groove", weight=1.0),
        types.WeightedPrompt(text="acid 303 bass", weight=0.8),
    ]
)

# Transition to a melodic breakdown
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="ambient synth pads", weight=1.0),
        types.WeightedPrompt(text="subtle reverberant piano", weight=0.7),
        types.WeightedPrompt(text="techno groove", weight=0.2),
    ]
)
```

## Langkah berikutnya

- [Membuat musik dengan Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=id): Buat lagu lengkap dan klip berdurasi 30 detik menggunakan Interactions API.
- [Pembuatan musik real-time dengan Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=id): Buat aplikasi streaming musik interaktif real-time melalui WebSockets.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-18 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-18 UTC."],[],[]]
