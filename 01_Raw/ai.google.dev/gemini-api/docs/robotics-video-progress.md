---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=tr
fetched_at: 2026-10-12T06:57:37.538889+00:00
title: "Video anlama \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Video anlama

Gemini Robotics ER 2, iki özelliği kullanarak sürekli video feed'lerinden görev ilerlemesini takip edebilir:

- An bulma: Önemli bir etkinliğin gerçekleştiği tam zaman damgasını belirler.
- Tamamlama sınıflandırması: Her videoyu beş tamamlama aralığından birine atar (%0-20, %20-40, %40-60, %60-80, %80-100).

## An bulma

An bulma özelliği, önemli bir olayın gerçekleştiği tam video karesini (ör. bir kupanın dolduğu veya bir düğümün bağlandığı an) belirler. Robotlar, başarıyı doğrulamak, adımları sıralamak ve düzeltmeleri tetiklemek için bunu kullanır.

Aşağıdaki örnek istemde modelden, videodaki belirli bir görevin tamamlanma anını belirlemesi isteniyor:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Aşağıda, bir an bulma videosundan örnek kareler gösterilmektedir. Model, görevin tamamlanma zaman damgasını tanımlamaktadır:

![Zaman damgası yerleşimiyle an bulma çıktısını gösteren örnek video kareleri](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=tr)

## İlerleme sınıflandırması

İlerleme sınıflandırması, bir videoyu beş tamamlama aralığından birine atar: 0-20%, 20-40%, 40-60%, 60-80% veya 80-100%. Bu sayede robotlar, tüm iş akışını yeniden başlatmadan eylemleri ayarlayabilir veya başarısız olan adımları yeniden deneyebilir.

Aşağıdaki örnek istemde modelden, bir videodaki mevcut ilerleme düzeyini sınıflandırması isteniyor:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Aşağıda, modelin ilerleme aralığı atadığı bir ilerleme sınıflandırması videosundan örnek kareler gösterilmektedir:

![İlerleme aralığı etiketiyle ilerleme sınıflandırma çıkışını gösteren örnek video kareleri](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=tr)

## Örnekler

Çok adımlı görev izleme de dahil olmak üzere tam olarak çalıştırılabilir örnekler için [Robotik çözüm kitabına](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb) bakın.

## Sırada ne var?

- [Robotik için Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr): Gerçek zamanlı çift yönlü yayın.
- [Görev düzenleme](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=tr): Uzamsal akıl yürütme içeren uzun vadeli görevler.
- [Gemini Robotics ER'ye genel bakış](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr): Model karşılaştırması ve özellikleri.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-08 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-08 UTC."],[],[]]
