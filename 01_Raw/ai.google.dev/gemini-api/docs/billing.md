---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=id
fetched_at: 2026-06-08T15:01:33.183333+00:00
title: "Penagihan \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Penagihan

Panduan ini memberikan ringkasan berbagai opsi penagihan Gemini API, menjelaskan cara mengaktifkan penagihan dan memantau penggunaan, serta memberikan jawaban atas pertanyaan umum (FAQ) tentang penagihan.

## Tentang penagihan dan tingkat

Penagihan untuk Gemini API didasarkan pada histori pembayaran Anda.

| Tingkat penggunaan | Kualifikasi | [Batas tingkat penagihan](#spend-caps) |
| --- | --- | --- |
| **Gratis** | [Project aktif](https://ai.google.dev/gemini-api/docs/api-key?hl=id#google-cloud-projects) atau uji coba gratis | T/A |
| **Tingkat 1** | [Menyiapkan dan menautkan akun penagihan yang aktif](#setup-billing) | $250 |
| **Tingkat 2** | Dibayar $100 + 3 hari sejak pembayaran pertama yang berhasil | $2.000 |
| **Tingkat 3** | Membayar $1.000 + 30 hari sejak pembayaran pertama yang berhasil | $20.000 - $100.000+ |

Akun baru dimulai dengan Paket Gratis, yang memungkinkan akses ke [model tertentu](https://ai.google.dev/gemini-api/docs/pricing?hl=id) di Gemini API dan AI Studio, hingga [batas kecepatan](https://aistudio.google.com/rate-limit?hl=id) paket gratis model.

Untuk men-deploy aplikasi langsung dari mode Build, Anda dapat menggunakan
**Paket Pemula Google Cloud**. Paket ini memungkinkan Anda memublikasikan hingga 2 aplikasi
full stack tanpa menyiapkan project Google Cloud atau akun penagihan.
Lihat [Men-deploy dari Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=id) untuk mengetahui
detailnya dan lihat [dokumentasi Paket Pemula Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=id) untuk mengetahui informasi selengkapnya.

Untuk mengakses batas frekuensi yang lebih tinggi, menggunakan model lanjutan, dan memastikan perintah dan respons Anda **tidak** digunakan untuk meningkatkan kualitas produk Google\*, Anda dapat [menautkan akun penagihan](#setup-billing) dan [Membayar di Muka](#prepay) untuk beralih ke Paket Berbayar.
Kemudian, Anda akan berpindah ke tingkat yang lebih tinggi berdasarkan pembelanjaan kumulatif dan usia akun. Di Tingkat 3, Anda mungkin memiliki opsi untuk beralih ke penagihan [pascabayar](#postpay).

Tingkatan, batas frekuensi, dan batas akun penagihan ditentukan di tingkat [akun
penagihan](#cloud-billing).

\* *Privasi data tingkat perusahaan: Untuk mengetahui informasi selengkapnya tentang penggunaan data untuk layanan berbayar, lihat [Persyaratan Layanan](https://ai.google.dev/gemini-api/terms?hl=id#data-use-paid).*

## Menyiapkan penagihan untuk mengakses Paket Berbayar

Anda dapat membuat project dan menyiapkan penagihan, atau mengimpor project yang ada, untuk mengupgrade ke Tingkat Berbayar di [Google AI Studio](https://aistudio.google.com/projects?hl=id).
Mengupgrade dari Tingkat Gratis ke Tingkat Berbayar berarti menautkan akun penagihan
dan [membayar di muka](#prepay) untuk menambahkan kredit minimal $10 (atau setara dalam mata uang lain) ke akun Anda.

1. Buka halaman [kunci API](https://aistudio.google.com/api-keys?hl=id) AI Studio, halaman
   [Project](https://aistudio.google.com/projects?hl=id), atau tempat mana pun Anda melihat tombol
   **Siapkan penagihan** di AI Studio.
   - Pengguna baru akan memiliki [project dan kunci API](https://ai.google.dev/gemini-api/docs/api-key?hl=id#google-cloud-projects) yang dibuat untuk mereka secara default.
   - Jika Anda memerlukan kunci baru, klik [**Buat kunci API**](https://aistudio.google.com/api-keys?hl=id)
     dan ikuti dialog untuk menambahkan pasangan kunci-project ke tabel.
2. Temukan project Tingkat Gratis yang ingin Anda upgrade ke Tingkat Berbayar, lalu klik
   **Siapkan penagihan** di kolom *Tingkat Penagihan*.
3. Jika Anda belum pernah menyiapkan akun penagihan Google sebelumnya:
   - Anda akan diminta untuk memilih negara Anda guna menyetujui Persyaratan Layanan.
   - Kemudian, isi atau konfirmasi informasi kontak dan metode pembayaran Anda untuk melanjutkan.
4. Jika Anda telah menyiapkan akun penagihan Google di masa lalu:
   - Anda akan diminta memilih dari akun penagihan yang sudah ada.
   - Jika Anda tidak ingin menggunakan salah satu akun yang ada, klik **Tambahkan akun penagihan baru**, lalu isi atau konfirmasi informasi kontak dan metode pembayaran Anda untuk melanjutkan.
5. Selanjutnya, Anda akan:
   - Diminta untuk membayar di muka minimal Rp100.000 untuk menyelesaikan penyiapan penagihan (artinya akun Anda ditetapkan secara otomatis ke paket penagihan [Prabayar](#prepay)),
   - Diberi pilihan antara paket penagihan [Prabayar](#prepay) dan [Pascabayar](#postpay)
     untuk akun Anda.
   - Ditetapkan ke paket penagihan [Pasca Bayar](#postpay) untuk periode sementara
     hingga sistem Prabayar baru diterapkan kepada semua pengguna (mulai 23 Maret 2026).
6. Setelah memilih Prabayar atau Pascabayar, penyiapan akun Anda selesai.

### Melakukan upgrade ke tingkat berbayar berikutnya

Jika Anda sudah menggunakan paket berbayar dan memenuhi [kriteria](#about-billing)
untuk perubahan paket, Anda akan otomatis diupgrade ke paket berikutnya
(tunduk pada [waktu pemrosesan](#processing-times)).

## Memverifikasi status penagihan

Setelah [menautkan akun penagihan](#setup-billing) ke project, Anda dapat memantau statusnya di [halaman Penagihan AI Studio](https://aistudio.google.com/billing?hl=id). Tidak seperti tingkat gratis, status tingkat berbayar bersifat dinamis; meskipun tingkat penggunaan Anda ditentukan oleh histori akun, Gemini API hanya akan melayani permintaan jika Anda memiliki saldo kredit [Prabayar](#prepay) yang positif.

Di halaman [Project](https://aistudio.google.com/projects?hl=id), Anda dapat
melihat tingkat dan paket penagihan project di kolom *Tingkat Penagihan*. Tindakan status penagihan yang mungkin perlu Anda lakukan untuk project ditampilkan di kolom *Tingkat Penagihan* atau *Status*:

- "***Siapkan penagihan***" jika project tidak memiliki akun penagihan yang terkait.
- "***Siapkan Prabayar***" jika project sudah memiliki akun penagihan yang terlampir, tetapi
  diwajibkan untuk menggunakan paket penagihan [Prabayar](#prepay) yang perlu disiapkan.
- "***Tidak ada kredit yang tersedia***" jika akun penagihan diwajibkan untuk membeli
  kredit, tetapi akun pembayaran Prabayar belum disiapkan atau saldo kredit
  yang tersedia telah habis.

Klik salah satu pesan untuk melanjutkan tindakan yang diperlukan.

## Memantau penggunaan

Anda dapat memantau penggunaan Gemini API di
[Google AI Studio](https://aistudio.google.com/usage?hl=id) di **Dasbor** >
**Penggunaan**.

## Paket penagihan

Paket penagihan untuk Gemini API dan AI Studio terbagi dalam dua kategori yang menentukan waktu pembayaran penggunaan: Prabayar dan Pascabayar. Anda dapat memeriksa paket penagihan yang ditetapkan dan mengelola metode pembayaran di halaman [Penagihan AI Studio](https://aistudio.google.com/billing?hl=id).

### Prabayar

Dalam paket penagihan Prabayar, Anda membeli kredit untuk saldo prabayar sebelum penggunaan Gemini API, dan biaya penggunaan API akan dipotong dari saldo kredit Prabayar [hampir secara real-time](#processing-times).
Anda dapat membayar di muka dengan [menambahkan kredit](#buy-credits) ke akun, atau menyiapkan [isi ulang otomatis](#auto-reload). Setelah kredit dibeli, kredit yang tidak digunakan akan berakhir setelah 12 bulan dan [tidak dapat dikembalikan dananya](#refunds), kecuali setelah [beralih ke akun Pascabayar](#postpay).

Saat saldo kredit Prabayar di akun penagihan Anda mencapai $0, semua kunci API di
semua project yang ditautkan ke akun penagihan tersebut akan berhenti berfungsi secara bersamaan.
Kredit prabayar hanya berlaku untuk biaya penggunaan Gemini API; Anda tidak dapat menggunakannya untuk membayar layanan Google Cloud lainnya.

Pengguna baru secara default menggunakan paket penagihan Prabayar. Project yang ada sebelum
pengenalan paket penagihan Prabayar dan Pascabayar mungkin perlu [memperbarui
detail penagihan project](#verify-billing) sebelum melanjutkan penggunaan Gemini
API.

*Perhatikan bahwa Prabayar tidak tersedia untuk akun [Dengan invoice (atau Offline)](https://docs.cloud.google.com/billing/docs/concepts?hl=id#billing_account_types)*.

#### Membeli kredit

Anda dapat membeli kredit secara manual sebelum penggunaan Gemini API untuk memuatnya ke saldo kredit akun Prabayar.

Untuk membeli poin, buka halaman [Penagihan AI Studio](https://aistudio.google.com/billing?hl=id), lalu pilih **Beli poin**.
Pembelian minimum adalah $10. Jumlah maksimum kredit yang dapat Anda bayar di muka adalah $5.000.

#### Muat ulang otomatis

Isi ulang otomatis adalah fitur opsional yang otomatis mengisi ulang saldo kredit Prabayar Anda saat saldo hampir habis. Hal ini berguna untuk mencegah gangguan layanan.

Anda dapat menyiapkan isi ulang otomatis dan melihat status isi ulang otomatis di kartu *Kredit tersedia* di halaman [Penagihan AI Studio](https://aistudio.google.com/billing?hl=id). Klik **Siapkan isi ulang otomatis** atau **Kelola isi ulang otomatis** untuk menetapkan metode pembayaran, jumlah isi ulang, dan saldo minimum yang memicu pembayaran isi ulang.

#### Batas pengisian otomatis bulanan

Batas isi ulang otomatis bulanan tersedia untuk pengguna Prabayar dan membantu mencegah biaya tak terduga dari isi ulang otomatis kredit yang sering.
Gunakan fitur ini untuk menetapkan batas maksimum pengisian ulang otomatis dalam satu siklus penagihan. Setelah jumlah total isi ulang otomatis dalam siklus penagihan mencapai batas ini, sistem akan menonaktifkan isi ulang otomatis hingga awal bulan berikutnya. Pembayaran satu kali yang Anda lakukan secara manual tidak mengurangi batas ini.

Untuk menetapkan batas pengisian otomatis bulanan saat isi ulang otomatis diaktifkan:

1. Buka halaman [Penagihan AI Studio](https://aistudio.google.com/billing?hl=id).
2. Klik **Kelola isi ulang otomatis**.
3. Perluas bagian **Batas Bulanan** dan masukkan batas bulanan maksimum untuk isi ulang otomatis.
4. Klik **Simpan**.

### Pascabayar

Dalam paket penagihan Pascabayar, akun Penagihan Cloud Anda mengakumulasi biaya dan Anda akan ditagih secara otomatis di akhir bulan, atau saat biaya Anda mencapai [batas pembelanjaan yang ditetapkan secara otomatis](#tier-spend-caps) berdasarkan tingkat akun Anda. Pembayaran ditagih ke metode pembayaran yang terlampir pada akun pembayaran Pascabayar Anda, yang dapat Anda kelola di halaman [Penagihan AI Studio](https://aistudio.google.com/billing?hl=id).

Setelah memenuhi [kriteria Tingkat 3](#about-billing), Anda dapat
beralih secara manual dari paket Prabayar ke Pascabayar. Untuk mengubah paket, Anda harus
mengklik tombol **Beralih ke pascabayar** yang muncul di kanan atas
halaman [Penagihan AI Studio](https://aistudio.google.com/billing?hl=id) saat akun Anda memenuhi syarat.

Kemudian, di halaman **Penagihan**, Anda dapat melihat saldo, tanggal jatuh tempo, dan pembayaran sebelumnya, serta melakukan pembayaran dan mengelola metode pembayaran.

Saat [menyiapkan penagihan](#setup-billing) untuk project baru, jika memenuhi syarat untuk Pascabayar, Anda akan memiliki opsi untuk memilih antara Prabayar dan Pascabayar dalam dialog [konfigurasi penagihan](#setup-billing).

Setelah Anda mengalihkan akun Penagihan Cloud untuk menggunakan paket penagihan Pasca Bayar, semua project yang ditautkan ke akun penagihan tersebut akan dialihkan ke paket Pasca Bayar. Anda
tidak dapat memindahkan akun penagihan tersebut kembali ke paket penagihan Prabayar. Anda dapat
memindahkan project ke akun penagihan dengan paket penagihan yang berbeda untuk mengubah
siklus penagihan untuk project tersebut; buka dokumentasi Cloud tentang [mengelola
penagihan untuk project](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=id).

Anda dapat mempelajari lebih lanjut siklus penagihan Pascabayar dalam [panduan Penagihan Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=id).

## Batas pembelanjaan

Gemini API mendukung batas pembelanjaan bulanan di tingkat project dan tingkat akun penagihan. Kontrol ini dirancang untuk melindungi akun Anda dari tagihan yang tidak terduga dan ekosistem untuk memastikan ketersediaan layanan.

*Perhatikan bahwa batas pembelanjaan tidak tersedia untuk akun [Dengan invoice (atau Offline)](https://docs.cloud.google.com/billing/docs/concepts?hl=id#billing_account_types).*

### Batas pembelanjaan project

Anda dapat menetapkan batas pembelanjaan [level project](https://ai.google.dev/gemini-api/docs/api-key?hl=id#google-cloud-projects) sendiri di AI Studio.
Hal ini berguna jika Anda memiliki beberapa project dalam akun penagihan yang sama dan ingin memastikan setiap project memiliki akses ke batas pembelanjaan kumulatif yang cukup.

Akun dengan [peran](https://docs.cloud.google.com/iam/docs/roles-overview?hl=id) editor, pemilik, atau admin project dapat menetapkan batas pembelanjaan per project di AI Studio pada halaman [Pembelanjaan](https://aistudio.google.com/spend?hl=id)
di bagian **Batas pembelanjaan bulanan** > **Edit batas pembelanjaan**.

Untuk mengetahui detail tentang izin IAM Google Cloud tertentu yang diperlukan untuk melihat atau mengedit batas pembelanjaan dan informasi penagihan di AI Studio, lihat [panduan pemecahan masalah AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=id#iam-permissions).

Jika Anda [memindahkan project ke akun penagihan lain](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=id#change_the_billing_account_for_a_project),
batas pembelanjaan yang telah Anda tetapkan untuk project tersebut akan tetap ada, tetapi pembelanjaan yang terakumulasi akan direset menjadi $0 untuk siklus penagihan baru.

Tugas yang berjalan lama seperti penyelesaian [mode batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=id) dan sesi agen dapat menimbulkan biaya tambahan di luar batas pembelanjaan project Anda.

Waktu pemrosesan data penagihan di AI Studio dapat tertunda hingga sekitar 10 menit. Anda mungkin mengalami penggunaan berlebih di luar batas project jika data penagihan belum diproses sebelum biaya lainnya terakumulasi.

### Batas pembelanjaan tingkat akun penagihan

Setiap [tingkatan](#about-billing) memiliki batas pembelanjaan bulanan maksimum:

| Tingkat penggunaan | Batas pembelanjaan |
| --- | --- |
| **Gratis** | T/A |
| **Tingkat 1** | $250 |
| **Tingkat 2** | $2.000 |
| **Tingkat 3** | $20.000 - $100.000 |

Batas penggunaan bulanan diterapkan untuk Gemini API di tingkat [akun penagihan](#cloud-billing). Meskipun batas default telah ditetapkan, Anda dapat [meminta
peningkatan](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=id)
untuk mengakomodasi penggunaan yang lebih tinggi. Total pembelanjaan digabungkan di semua project tertaut yang mengaktifkan layanan Gemini API. Setelah total akun kumulatif mencapai batas tingkat, layanan akan dijeda untuk semua project yang ditautkan ke akun penagihan tersebut hingga awal siklus penagihan berikutnya (tanggal 1 setiap bulan).

#### Mengevaluasi pembelanjaan akun penagihan Anda

Untuk mengevaluasi pembelanjaan bulanan historis Anda guna menentukan apakah [batas pembelanjaan tingkat Akun Penagihan](#tier-spend-caps) yang baru akan memengaruhi project yang sedang berjalan, ikuti langkah-langkah berikut:

1. Di konsol Google Cloud, lihat halaman [Laporan akun Penagihan Cloud](https://console.cloud.google.com/billing/reports?hl=id) Anda.
   - Jika Anda memiliki lebih dari satu akun penagihan, saat diminta, pilih akun Penagihan Cloud yang ingin Anda lihat laporan biayanya.
2. Secara default, laporan akan "Dikelompokkan menurut Layanan" pada "Bulan ini". Anda akan melihat **Gemini API** di kolom **Layanan** dan total pembelanjaan di kolom **Biaya penggunaan** dalam tabel.
3. Untuk melihat biaya terperinci yang terbatas pada penggunaan Gemini API, tetapkan filter **Kelompokkan menurut**
   untuk mengelompokkan menurut **SKU**, dan filter **Layanan** ke **Gemini API**.
4. Sesuaikan filter **Rentang waktu menurut tanggal penggunaan** ke rentang yang diinginkan untuk mengevaluasi pembelanjaan historis Anda dalam suatu periode.

## Waktu pemrosesan

Sinyal dan pembaruan penagihan tidak selalu terjadi secara real time.

- **Penggunaan kredit**: Biaya penggunaan biasanya ditarik dari saldo Anda dalam beberapa menit.
- **Konfirmasi pembayaran**: Meskipun sebagian besar pembayaran kartu dilakukan secara instan, beberapa metode pembayaran (seperti transfer bank) mungkin memerlukan waktu beberapa hari untuk diproses. Layanan hanya dilanjutkan atau di-upgrade setelah pembelian kredit dikonfirmasi secara resmi.
- **Upgrade tingkat**: Setelah pembayaran berhasil, atau saat Anda memenuhi
  [kriteria upgrade](#about-billing), upgrade tingkat biasanya akan ditampilkan dalam waktu 10
  menit.
- **Grafik perincian Total Biaya**: Grafik yang menampilkan perincian total biaya di halaman [Penagihan](https://aistudio.google.com/billing?hl=id) dan halaman [Pembelanjaan](https://aistudio.google.com/spend?hl=id) dapat memerlukan waktu hingga 24 jam untuk diperbarui.

Baca panduan Penagihan Cloud tentang [siklus penagihan](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=id#delayed-billing) dan latensi [transaksi](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=id#missing-transactions) untuk mempelajari lebih lanjut potensi keterlambatan penagihan.

## Pengembalian dana

Pengembalian dana tidak diizinkan untuk akun penagihan **Prabayar**, kecuali saat beralih jenis akun.

**Saat akun Prabayar beralih ke jenis akun Pascabayar** (setelah Anda
memenuhi [kriteria](#about-billing) dan [mengupgrade akun secara manual](#postpay)
Anda), akun Prabayar akan ditutup dan sisa kredit prabayar
akan otomatis dikembalikan dananya ke metode pembayaran yang tercatat.

Jika Anda [menutup](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=id#close-a-billing-account)
akun Prabayar karena alasan apa pun selain mengupgrade ke Pasca Bayar, sisa kredit prabayar akan hangus.

Masa berlaku kredit yang dibeli akan berakhir setelah 1 tahun. Setelah masa berlaku berakhir, kredit akan hangus dan tidak dapat diambil.

Akun **Pasca-bayar** mengikuti [kebijakan pengembalian dana Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=id#request_a_refund).

## Akun Penagihan Cloud

Gemini API menggunakan [akun Penagihan Cloud](https://cloud.google.com/billing/docs/concepts?hl=id) untuk layanan penagihan, yang dapat Anda [siapkan langsung di AI Studio](#setup-billing).
Anda dapat menggunakan AI Studio untuk melacak pembelanjaan, memahami biaya, dan melakukan pembayaran.

Tingkatan, batas frekuensi, dan batas akun penagihan ditentukan di tingkat akun penagihan.

### Project dan kunci API

Semua [project](https://ai.google.dev/gemini-api/docs/api-key?hl=id#google-cloud-projects) yang ditautkan ke akun Penagihan Cloud akan mewarisi tingkat penggunaan dan batas tarif serta batas akun yang terkait dengan akun penagihan tersebut. Jika Anda [mengubah project](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=id#change_the_billing_account_for_a_project)
dari satu akun penagihan ke akun penagihan lain, tingkatnya, dan selanjutnya batas kecepatan serta
batas akun, akan beralih ke tingkat akun penagihan baru.

Pembelanjaan kumulatif (untuk semua produk Google Cloud) dan usia akun di semua project yang terkait dengan akun penagihan dihitung untuk [kualifikasi tingkat](#about-billing) akun penagihan tersebut.

Anda dapat [membatalkan tautan project](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=id#disable_billing_for_a_project)
dari akun penagihannya untuk kembali ke paket gratis.

[Kunci API](https://ai.google.dev/gemini-api/docs/api-key?hl=id) adalah kredensial yang dibuat di dalam project.
Project ini tidak memiliki setelan penagihan independen; project ini mewarisi batas tingkat dan
status penagihan project. Penggunaan kumulatif dari semua kunci dalam project dihitung dalam batas pembelanjaan project tersebut dan total pembelanjaan akun penagihan.

## Pertanyaan umum (FAQ)

Bagian berikut memberikan jawaban atas pertanyaan umum (FAQ).

### Apa yang ditagih kepada saya?

Harga Gemini API didasarkan pada hal berikut:

- Jumlah token input
- Jumlah token output
- Jumlah token yang di-cache
- Durasi penyimpanan token yang di-cache

Untuk mengetahui informasi harga, lihat [Halaman harga](https://ai.google.dev/pricing?hl=id).

### Di mana saya dapat melihat kuota saya?

Anda dapat melihat kuota dan batas sistem di
[AI Studio](https://aistudio.google.com/usage?hl=id).

### Bagaimana cara beralih ke tingkat batas frekuensi panggilan yang lebih tinggi, atau meminta lebih banyak kuota?

Anda akan otomatis mendapatkan lebih banyak kuota saat akun Anda mencapai
[persyaratan tingkat](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id#usage-tiers) berikutnya.

### Dapatkah saya menggunakan Gemini API secara gratis di EEA (termasuk Uni Eropa), Inggris Raya, dan Swiss?

Ya, kami menyediakan paket gratis dan paket berbayar di [banyak region](https://ai.google.dev/gemini-api/docs/available-regions?hl=id).

### Jika saya menyiapkan penagihan dengan Gemini API, apakah saya akan ditagih untuk penggunaan Google AI Studio?

Penggunaan AI Studio tetap tanpa biaya kecuali jika pengguna menautkan kunci API berbayar untuk
mengakses fitur berbayar.
Setelah Anda menautkan kunci API berbayar sebagai bagian dari project berbayar di AI Studio, Anda akan ditagih untuk penggunaan AI Studio untuk kunci tersebut. Anda dapat beralih antara project Tingkat Berbayar dan project Tingkat Gratis sesuai kebutuhan dengan menggunakan kunci API masing-masing yang ditautkan ke setiap jenis.

### Jika saya menggunakan Paket Gratis, bagaimana cara mengupgrade ke paket yang lebih tinggi?

Untuk mengakses tingkat yang lebih tinggi, Anda harus menyiapkan penagihan di project Anda. Klik [**Siapkan
penagihan**](#setup-billing) di Google AI Studio. Tindakan ini akan memandu Anda memilih atau membuat akun Penagihan Cloud. Jika Anda diwajibkan menggunakan model penagihan prabayar, proses **Siapkan penagihan** akan memandu Anda melalui proses pembuatan akun Prabayar yang ditautkan ke akun Penagihan Cloud Anda.

### Dapatkah saya menggunakan 1 juta token dalam paket gratis?

Paket gratis untuk Gemini API berbeda-beda berdasarkan model yang dipilih. Untuk saat ini, Anda
dapat mencoba jendela konteks 1 juta token dengan cara berikut:

- Di Google AI Studio
- Dengan paket tanpa biaya untuk model tertentu
- Dengan paket pascabayar

### Dapatkah saya kembali ke Paket Gratis setelah melakukan upgrade ke paket yang lebih tinggi (berbayar)?

Untuk melakukan downgrade ke Paket Gratis, Anda dapat [menonaktifkan penagihan](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=id#disable_billing_for_a_project)
di setiap project yang ingin Anda downgrade.

### Bagaimana cara menghitung jumlah token yang saya gunakan?

Gunakan metode [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=id#count_tokens)
untuk menghitung jumlah token. Lihat [Panduan token](https://ai.google.dev/gemini-api/docs/tokens?hl=id) untuk mempelajari token lebih lanjut.

### Jika saya mendaftar ke akun Penagihan Cloud pertama saya melalui AI Studio, apakah saya tetap akan mendapatkan Uji Coba Gratis Google Cloud?

Saat Anda mendaftar ke akun Penagihan Cloud pertama Anda, [Uji Coba Gratis Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=id#free-trial) Anda akan dimulai dan Anda akan mendapatkan [Kredit selamat datang](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=id#welcome-credits) senilai $300.
Namun, kredit tersebut tidak dapat digunakan untuk membayar penggunaan AI Studio. Anda dapat menggunakan Kredit selamat datang untuk membayar layanan lain yang memenuhi syarat dalam Google Cloud (perhatikan bahwa setelah kredit tersebut digunakan atau habis masa berlakunya (dalam waktu 90 hari), biaya penggunaan tambahan akan otomatis ditagih ke metode pembayaran yang telah Anda tetapkan).

### Dapatkah saya menggunakan kredit Selamat Datang Google Cloud dengan Gemini API?

Tidak, [kredit Selamat datang](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=id#welcome-credits) Google Cloud atau kredit uji coba gratis tidak dapat digunakan untuk Gemini API atau AI Studio.

Jika Anda diberi kredit selamat datang Google Cloud sebelum kredit tersebut tidak memenuhi syarat, Anda diizinkan untuk membelanjakan sisa kredit Anda di Gemini API dan AI Studio hingga kredit tersebut berakhir (setelah 90 hari).

### Apakah Uji Coba Gratis Google Cloud berlaku untuk penggunaan Gemini API?

Tidak, mulai Maret 2026, biaya penggunaan Gemini API secara khusus tidak termasuk dalam program [Uji Coba Gratis Google Cloud senilai$300](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=id#free-trial).

### Bagaimana penagihan ditangani?

Penagihan untuk Gemini API ditangani oleh sistem [Penagihan Cloud](https://cloud.google.com/billing/docs/concepts?hl=id). Pelajari konfigurasi penagihan Cloud dalam produk di [dokumentasi Penagihan Cloud](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=id).

### Apakah saya dikenai biaya untuk permintaan yang gagal?

Jika permintaan Anda gagal dengan error 400 atau 500, Anda tidak akan ditagih untuk token yang digunakan. Namun, permintaan tersebut tetap akan mengurangi kuota Anda.

### Apakah `GetTokens` ditagih?

Permintaan ke API `GetTokens` tidak ditagih, dan tidak mengurangi kuota inferensi.

### Bagaimana penanganan data Google AI Studio saya jika saya memiliki akun API berbayar?

Lihat [Persyaratan layanan](https://ai.google.dev/gemini-api/terms?hl=id#paid-services) untuk mengetahui detail tentang cara data ditangani saat Penagihan Cloud diaktifkan (lihat "Cara Google Menggunakan Data Anda" di bagian "Layanan Berbayar"). Perhatikan bahwa perintah Google AI Studio Anda diperlakukan berdasarkan persyaratan "Layanan Berbayar" yang sama selama setidaknya 1 project API mengaktifkan penagihan, yang dapat Anda validasi di [halaman kunci API Gemini](https://aistudio.google.com/api-keys?hl=id) jika Anda melihat project yang ditandai sebagai "Berbayar" di bagian "Paket".

### Apa itu penagihan prabayar dan siapa yang wajib menggunakan model penagihan prabayar?

Penagihan prabayar memungkinkan pengguna Gemini API di AI Studio membeli kredit di muka.
Mulai 23 Maret 2026, pengguna baru AI Studio mungkin diwajibkan untuk menggunakan paket penagihan Prabayar. Selama proses [Siapkan Penagihan](#setup-billing) AI Studio, UI akan memandu Anda melalui alur penyiapan penagihan dan akan menunjukkan apakah Anda diwajibkan untuk melakukan prabayar.

### Bagaimana cara membeli kredit Prabayar, dan apakah ada jumlah minimum atau maksimum?

Anda dapat [membeli poin](#buy-credits) di halaman Penagihan AI Studio. Selama
proses pembelian, UI akan memberikan jumlah pembelian di muka minimum yang
diperlukan untuk wilayah dan tingkat Anda, serta jumlah maksimum yang dapat
ada di akun Anda dalam satu waktu.

### Dapatkah saya mengonfigurasi akun Prabayar untuk otomatis membeli lebih banyak kredit sesuai kebutuhan?

Ya, sebaiknya Anda mengonfigurasi [pemuatan ulang otomatis](#auto-reload) di setelan Penagihan AI Studio. Anda menentukan saldo kredit "pemicu" (misalnya, "jika saldo saya kurang dari Rp300.000") dan "nilai isi ulang" (misalnya, "tambahkan Rp1.000.000").

### Dapatkah saya membatasi jumlah pengisian ulang otomatis?

Ya, pengguna Prabayar dapat menetapkan [Batas Isi Ulang Otomatis Bulanan](#monthly-auto-charge-limit)
dalam widget **Isi Ulang Otomatis**. Jika total jumlah isi ulang otomatis dalam siklus penagihan mencapai batas ini, sistem akan menonaktifkan isi ulang otomatis hingga bulan berikutnya. Pembelian kredit manual tidak diperhitungkan dalam batas ini.

### Bisakah saya mendapatkan pengembalian dana untuk kredit yang tidak saya gunakan?

Semua kredit API prabayar akan habis masa berlakunya setelah 1 tahun dan tidak dapat dikembalikan. Baca
[kebijakan pengembalian dana untuk akun Prabayar](#refunds).

### Apakah masa berlaku kredit prabayar saya akan berakhir?

Ya, masa berlaku kredit akan berakhir 12 bulan setelah tanggal pembeliannya.

### Apa yang terjadi jika saldo kredit prabayar saya mencapai Rp0?

Semua layanan Gemini API di semua project yang dibayar oleh akun Prabayar Penagihan Cloud tersebut akan segera dihentikan untuk mencegah timbulnya biaya lebih lanjut. Project Anda tidak otomatis di-downgrade ke Tingkat Gratis.

Untuk memulihkan layanan di tingkat Berbayar saat ini, Anda harus [membeli
kredit tambahan](#buy-credits). Setelah membeli kredit, Anda akan dapat menggunakan Gemini API. Perhatikan bahwa mungkin ada [keterlambatan](#processing-times) saat sistem kami diperbarui untuk menampilkan saldo kredit Anda.

Jika ingin melakukan downgrade ke Paket Gratis, Anda dapat [menonaktifkan penagihan](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=id#disable_billing_for_a_project)
pada project yang ingin di-downgrade.

### Mengapa penggunaan saya berhenti meskipun saldo kredit Prabayar saya lebih besar dari Rp0?

Anda mungkin telah mencapai [batas penggunaan](#tier-spend-caps) untuk tingkat saat ini.
Batas penggunaan akan meningkat secara otomatis saat Anda naik ke tingkat yang lebih tinggi. Penggunaan Gemini API AI Studio Anda juga dapat terpengaruh karena [status akun Penagihan Cloud Anda](#missed-payment).

### Mengapa saldo kredit akun Prabayar saya negatif?

Karena kompleksitas sistem penagihan dan pemrosesan kami, mungkin ada [keterlambatan](#processing-times) dalam kemampuan kami untuk menghentikan penggunaan setelah Anda menggunakan semua kredit. Penggunaan berlebih ini mungkin muncul sebagai saldo kredit negatif di dasbor penagihan AI Studio. Jika hal ini terjadi, layanan Anda akan dijeda, dan saldo negatif Anda akan dipotong dari pembelian kredit berikutnya.

Untuk menghindari jeda pada layanan Gemini API, sebaiknya siapkan
[isi ulang otomatis](#auto-reload) untuk membeli lebih banyak kredit secara otomatis saat saldo kredit Anda kurang dari nilai yang Anda tentukan.

### Dapatkah saya menggunakan kredit Prabayar untuk layanan Google Cloud lainnya, seperti Gemini Enterprise Agent Platform?

Tidak, kredit Prabayar hanya dapat digunakan untuk penggunaan Gemini API. Layanan Google Cloud lainnya yang Anda gunakan (Compute, Storage, Gemini Enterprise Agent Platform) ditagih menggunakan [siklus penagihan Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=id) standar.

### Dapatkah saya beralih ke paket penagihan Pascabayar?

Saat Anda membuat histori pembayaran dan [mencapai tingkat yang memenuhi syarat](#about-billing) untuk paket penagihan Pasca Bayar, Anda dapat memilih untuk mentransisikan semua biaya penggunaan Gemini API di masa mendatang ke [siklus penagihan Pasca Bayar](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=id#view-your-charging-cycle) Google Cloud standar yang digabungkan.

### Apa yang terjadi pada kredit prabayar saya jika saya beralih ke Pascabayar?

Saat Anda mengupgrade ke [Pasca Bayar](#postpay), Penagihan Cloud akan menutup akun pembayaran Prabayar Anda, menonaktifkan [isi ulang otomatis](#auto-reload), dan secara otomatis mengembalikan dana kredit Prabayar yang tidak digunakan kepada Anda (tunduk pada waktu pemrosesan pengembalian dana standar).

### Di mana saya dapat melihat saldo kredit Prabayar dan histori transaksi saat ini?

Semua pengelolaan saldo dan histori transaksi untuk Gemini API harus dilakukan langsung di tab Penagihan Google AI Studio.

### Mengapa saya melihat pesan "Jenis akun penagihan tidak aktif atau tidak didukung"?

Interaksi pembayaran di [halaman Penagihan AI Studio](https://aistudio.google.com/billing?hl=id) dapat diblokir dan diganti dengan pesan "Jenis akun penagihan tidak aktif atau tidak didukung" jika jenis akun penagihan atau status akun penagihan yang Anda pilih tidak memenuhi syarat untuk Paket Berbayar di AI Studio.

Periksa [Konsol Cloud](https://console.cloud.google.com/billing/?hl=id) untuk melihat status akun penagihan Anda. Salah satu jenis yang tidak memenuhi syarat adalah *Akun uji coba gratis*. Dalam hal ini, Anda dapat [mengaktifkan penagihan](#setup-billing) di AI Studio agar memenuhi syarat. Salah satu status tidak aktif adalah *Ditutup*, dalam hal ini Anda dapat [membuka kembali akun](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=id).

### Apakah biaya penggunaan Gemini API saya akan muncul di konsol Google Cloud?

Ya, biaya Gemini API, beserta biaya yang terkait dengan layanan Google Cloud lainnya yang dibayar oleh akun Penagihan Cloud Anda, dapat dilihat di [halaman Pengelolaan biaya](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=id#cost-reports) di [konsol Penagihan Cloud](https://console.cloud.google.com/billing?hl=id). Perhatikan
bahwa Anda hanya dapat mengelola saldo kredit Prabayar di AI Studio.

### Mengapa Penggunaan Gemini API saya tidak muncul di Konsol Penagihan Cloud, padahal saya dapat melihatnya di Penagihan AI Studio, beserta penggunaan kredit saya?

Google Cloud dan AI Studio melaporkan data penggunaan ke Penagihan Cloud pada berbagai interval. Karena kompleksitas sistem penagihan dan pemrosesan kami, Anda mungkin melihat jeda antara penggunaan layanan dengan saat penggunaan dan biaya dapat dilihat di Penagihan Cloud. Biasanya, detail biaya Anda tersedia dalam satu hari, tetapi terkadang dapat memerlukan waktu lebih dari 24 jam.
Pelajari lebih lanjut penagihan tertunda di [dokumentasi Penagihan Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=id#delayed-billing).

### Jika saya menggunakan layanan Google Cloud lainnya dengan biaya yang tunduk pada siklus penagihan Pasca Bayar, apa yang terjadi jika saya terlambat membayar?

Keterlambatan pembayaran untuk layanan Google Cloud lainnya dapat menangguhkan akses Gemini API Anda di AI Studio, **terlepas dari jumlah kredit prabayar yang tersedia**. Penggunaan AI Studio didukung oleh akun Penagihan Google Cloud, yang dapat menggunakan penagihan Prabayar untuk AI Studio dan penagihan Pascabayar untuk layanan Cloud lainnya. Masalah pada saldo Pascabayar Anda menghentikan semua layanan yang terkait dengan akun tersebut. Penggunaan Gemini API Anda akan ditangguhkan jika akun Penagihan Cloud Anda ditandai karena masalah seperti:

- Saldo tunggakan atau terutang
- Pembayaran yang ditolak
- Metode pembayaran tidak valid atau sudah tidak berlaku

Untuk memulihkan layanan, Anda harus [menyelesaikan masalah akun Pasca Bayar](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=id#resolving-declined-payments) di konsol Penagihan Google Cloud. Setelah menyelesaikan masalah tersebut, Anda akan mendapatkan kembali akses ke kredit dan layanan Gemini API Prabayar.

### Di mana saya bisa mendapatkan bantuan terkait penagihan?

Untuk mendapatkan bantuan terkait penagihan, lihat
[Mendapatkan dukungan penagihan Cloud](https://cloud.google.com/support/billing?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-05 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-05 UTC."],[],[]]
