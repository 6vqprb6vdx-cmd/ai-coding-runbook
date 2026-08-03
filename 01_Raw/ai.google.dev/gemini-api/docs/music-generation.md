---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=tr
fetched_at: 2026-08-03T04:35:13.293886+00:00
title: "Lyria 3 ile m\u00fczik \u00fcretme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Lyria 3 ile müzik üretme

Lyria 3, Gemini API üzerinden kullanılabilen Google'ın müzik üretme modeli ailesidir. Lyria 3 ile metin istemlerinden veya resimlerden yüksek kaliteli, 44, 1 kHz stereo sesler üretebilirsiniz. Bu modeller, vokaller, zamanlanmış şarkı sözleri ve tam enstrümantal düzenlemeler dahil olmak üzere yapısal tutarlılık sağlar.

Lyria 3 ailesinde iki model bulunur:

| Model | Model Kimliği | En uygun olduğu durumlar | Süre | Çıkış |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Kısa klipler, döngüler, önizlemeler | 30 saniye | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Dizeler, nakaratlar ve köprüler içeren tam uzunlukta şarkılar | Birkaç dakika (istem kullanılarak kontrol edilebilir) | MP3 |

Her iki model de çok formatlı girişleri (metin ve resimler) destekleyen yeni [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) kullanılarak kullanılabilir ve **44,1 kHz yüksek kaliteli stereo** ses üretir.

## Müzik klibi oluşturma

Lyria 3 Clip modeli her zaman **30 saniyelik** bir klip oluşturur. Klip oluşturmak için `interactions.create` yöntemini metin istemiyle çağırın. Yanıtta, `steps` şemasındaki sesin yanı sıra her zaman oluşturulan şarkı sözleri ve şarkı yapısı yer alır.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

Oluşturulan son ses bloğunu döndüren `interaction.output_audio` özelliğini kullanarak oluşturulan müzik verilerini alabilirsiniz. Ayrıca, `interaction.output_text` özelliğini kullanarak şarkı sözlerini ve yapısını da alabilirsiniz. Kolaylık özellikleri hakkında ayrıntılı bilgi için [Etkileşimlere genel bakış](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr#convenience-properties) başlıklı makaleyi inceleyin.

## Tam uzunlukta şarkı oluşturma

Birkaç dakika süren tam uzunlukta şarkılar oluşturmak için `lyria-3-pro-preview` modelini kullanın. Pro modeli, müzikal yapıyı anlar ve farklı kıtalar, nakaratlar ve köprüler içeren kompozisyonlar oluşturabilir. İsteminizde süreyi belirterek (ör. "2 dakikalık bir şarkı oluştur") veya yapıyı tanımlamak için [zaman damgalarını](#timing) kullanarak süreyi etkileyebilirsiniz.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## Çıkış biçimini seçin

Lyria 3 modelleri varsayılan olarak **MP3** biçiminde ses üretir. Lyria 3 Pro'da, `response_format` ayarını yaparak çıktının **WAV** biçiminde olmasını da isteyebilirsiniz.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Yanıtı ayrıştırma

Lyria 3'ün yanıtı, `steps` şemasında birden fazla içerik bloğu içeriyor.
Etkileşimler, `model_output` adımlarının oluşturulan içeriği içerdiği bir adım dizisi döndürür.
Metin içerik bloklarında, üretilen şarkı sözleri veya şarkı yapısının JSON açıklaması yer alır.
`audio` türündeki içerik blokları, Base64 kodlu ses verilerini içerir.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### Şarkı sözleri ve müzik arasında geçiş yapma

Lyria 3'ün çıktısı karmaşıktır. Oluşturulan şarkı sözleri (metin) ve şarkının kendisi (ses) için ayrı adımlar ve bloklar içerir. Bu nedenle, kolaylık özellikleri hızlı ve önerilen bir kısayol sunar.

Ancak sunucu tarafından döndürülen adımların ham zaman çizelgesi üzerinde tam ve programatik kontrol sahibi olmak istiyorsanız (ör. tek tek içerik bloklarını alındıkları sırada günlüğe kaydetmek) bunun yerine `steps` üzerinde manuel olarak yineleme yapabilirsiniz:

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

## Resimlerden müzik oluşturma

Lyria 3, çok formatlı girişleri destekler. `input` listesinde metin isteminizle birlikte **10 adede kadar resim** sağlayabilirsiniz. Model, görsel içerikten ilham alarak müzik oluşturur.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3-pro-preview",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## Özel şarkı sözleri sağlama

Kendi şarkı sözlerinizi yazıp isteme ekleyebilirsiniz. Modelin şarkı yapısını anlamasına yardımcı olmak için `[Verse]`, `[Chorus]` ve `[Bridge]` gibi bölüm etiketlerini kullanın:

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## Zamanlamayı ve yapıyı kontrol etme

Zaman damgalarını kullanarak şarkının belirli anlarında tam olarak ne olacağını belirtebilirsiniz. Bu özellik, enstrümanların ne zaman devreye gireceğini, şarkı sözlerinin ne zaman sunulacağını ve şarkının nasıl ilerleyeceğini kontrol etmek için kullanışlıdır:

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Enstrümantal parçalar oluşturma

Arka plan müziği, oyun müzikleri veya vokallerin gerekli olmadığı tüm kullanım alanlarında, modelden yalnızca enstrümantal parçalar üretmesini isteyebilirsiniz:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Farklı dillerde müzik üretme

Lyria 3, isteminizin dilinde şarkı sözleri oluşturur. Fransızca sözler içeren bir şarkı oluşturmak için isteminizi Fransızca yazın. Model, ses stilini ve telaffuzunu dile uyacak şekilde ayarlar.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Model zekası

Lyria 3, isteminizi analiz eder. Bu süreçte model, isteminize göre müzikal yapı (giriş, kıta, nakarat, köprü vb.) üzerinden akıl yürütür.
Bu işlem, ses oluşturulmadan önce gerçekleşir ve yapısal tutarlılık ile müzikalite sağlar.

## İstem yazma kılavuzu

İsteminiz ne kadar ayrıntılı olursa sonuçlar o kadar iyi olur. Üretimi yönlendirmek için şunları ekleyebilirsiniz:

- **Tür**: Bir tür veya tür karışımı belirtin (ör. "lo-fi hip hop", "jazz fusion", "sinematik orkestra").
- **Enstrümanlar**: Belirli enstrümanların adını belirtin (ör. "Fender Rhodes piyano", "slide gitar", "TR-808 davul makinesi").
- **BPM**: Tempoyu ayarlayın (ör. "120 BPM", "70 BPM civarında yavaş tempo").
- **Ton/Ölçek**: Müzik tonunu belirtin (ör. "Sol majör", "Re minör").
- **Ruh hali ve atmosfer**: Açıklayıcı sıfatlar kullanın (ör. "nostaljik", "agresif", "göklerde", "hayalperest").
- **Yapı**: Şarkının ilerlemesini kontrol etmek için `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`, `[Outro]` gibi etiketler veya zaman damgaları kullanın.
- **Süre**: Klip modeli her zaman 30 saniyelik klipler üretir. Pro modelinde, isteminizde amaçlanan uzunluğu belirtin (ör. "2 dakikalık bir şarkı oluştur") veya süreyi kontrol etmek için zaman damgalarını kullanın.

### Örnek istemler

Etkili istemlere ilişkin bazı örnekler:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## En iyi uygulamalar

- **Önce Clip ile yineleyin.** `lyria-3-clip-preview` ile tam uzunlukta bir üretim yapmadan önce istemlerle deneme yapmak için daha hızlı olan `lyria-3-clip-preview` modelini kullanın.`lyria-3-pro-preview`
- **Net olun.** Net olmayan istemler, genel sonuçlar üretir. En iyi sonucu elde etmek için enstrümanları, tempoyu, anahtarı, ruh halini ve yapıyı belirtin.
- **Dilinizi eşleştirin.** Şarkı sözlerinin hangi dilde olmasını istiyorsanız o dilde istem girin.
- **Bölüm etiketlerini kullanın.** `[Verse]`, `[Chorus]`, `[Bridge]` etiketleri, modele izleyeceği net bir yapı sunar.
- **Şarkı sözlerini talimatlardan ayırın.** Özel şarkı sözleri sağlarken bunları müzikal yönlendirme talimatlarınızdan net bir şekilde ayırın.

## Sınırlamalar

- **Güvenlik**: Tüm istemler güvenlik filtreleriyle kontrol edilir. Filtreleri tetikleyen istemler engellenir. Belirli sanatçıların seslerini veya telif hakkıyla korunan şarkı sözlerinin oluşturulmasını isteyen istemler de bu kapsamdadır.
- **Filigran**: Üretilen tüm seslerde tanımlama için [SynthID ses filigranı](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=tr) bulunur. Bu filigran, insan kulağıyla fark edilemez ve dinleme deneyimini etkilemez.
- **Çok adımlı düzenleme**: Müzik üretimi tek adımlı bir süreçtir.
  Oluşturulan bir klibin birden fazla istemle yinelenerek düzenlenmesi veya iyileştirilmesi, Lyria 3'ün mevcut sürümünde desteklenmemektedir.
- **Uzunluk**: Klip modeli her zaman 30 saniyelik klipler oluşturur. Pro modeli, birkaç dakika süren şarkılar oluşturur. Tam süre, isteminizle belirlenebilir.
- **Belirlenimcilik**: Aynı istemle bile olsa sonuçlar görüşmeler arasında farklılık gösterebilir.

## Sırada ne var?

- Lyria 3 modellerinin [fiyatlandırmasını](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) inceleyin.
- Lyria RealTime ile [anlık, akışlı müzik üretmeyi](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=tr) deneyin.
- [TTS modelleri](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) ile birden fazla konuşmacının yer aldığı görüşmeler oluşturun.
- [Resim](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) veya [video](https://ai.google.dev/gemini-api/docs/video?hl=tr) oluşturmayı öğrenin.
- Gemini'ın [ses dosyalarını nasıl anlayabileceğini](https://ai.google.dev/gemini-api/docs/audio?hl=tr) öğrenin.
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr)'yi kullanarak Gemini ile anlık sohbet edin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
