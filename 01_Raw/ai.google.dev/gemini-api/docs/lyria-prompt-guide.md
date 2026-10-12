---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=vi
fetched_at: 2026-10-12T06:47:47.158313+00:00
title: "H\u01b0\u1edbng d\u1eabn v\u1ec1 c\u00e2u l\u1ec7nh cho Lyria \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hướng dẫn về câu lệnh cho Lyria

Gemini API cung cấp 2 cách để tạo nhạc bằng Lyria:

- **Lyria 3.5 và Lyria 3 Clip**: Tạo nội dung không phát trực tuyến cho các đoạn video dài 30 giây hoặc bài hát trọn vẹn có lời bài hát và giọng hát. Xem phần [Tạo nhạc bằng Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=vi).
- **Lyria RealTime**: Phát nhạc trực tuyến và điều khiển trực tiếp theo thời gian thực qua WebSockets. Xem [Tính năng tạo nhạc theo thời gian thực bằng Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=vi).

Cả hai mô hình đều phản hồi các câu lệnh bằng văn bản mô tả, thuật ngữ âm nhạc và hướng dẫn về cấu trúc. Hướng dẫn này trình bày cách viết câu lệnh hiệu quả cho cả hoạt động tạo hàng loạt và điều hướng theo thời gian thực.

## Kiến thức cơ bản về câu lệnh

Câu lệnh của bạn có thể là một cụm từ ngắn:

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

Hoặc nội dung mô tả chi tiết có cấu trúc:

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

Cả câu lệnh ngắn và câu lệnh chi tiết đều mang lại kết quả tốt. Hãy sử dụng các chiến lược sau để hướng mô hình đến âm thanh chính xác mà bạn muốn.

## Thể loại và phong cách

Bắt đầu câu lệnh bằng thể loại chính. Bạn có thể kết hợp các thể loại để tạo ra những thể loại kết hợp độc đáo:

- Sự kết hợp giữa nhạc metal và hip-hop
- Nhạc death metal kết hợp với giọng hát opera
- Nhạc thính phòng cổ điển kết hợp với các yếu tố âm thanh điện tử tối
- Nhạc dance điện tử (EDM) hiện đại kết hợp với nhạc Europop

Bạn cũng có thể chỉ định một kỷ nguyên âm nhạc hoặc biến thể theo khu vực:

- Nhạc hip-hop boom-bap đầu thập niên 1990
- Nhạc pop yé-yé của Pháp những năm 1960
- Nhạc post-punk và new wave thập niên 1980
- Nhạc R&B phổ biến của những năm 2000
- Nhạc techno tối giản của Berlin hoặc nhạc hyphy của Vùng Vịnh

### Từ khoá theo thể loại

Hãy sử dụng những thuật ngữ thể loại được công nhận này trong câu lệnh của bạn cho Lyria 3.5 và Lyria RealTime:

- **Nhạc điện tử và nhạc nhảy**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **Hip-Hop và R&B**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **Rock và Alternative**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **Nhạc Jazz, Soul và Funk**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **Dân ca và nhạc cổ truyền**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **Nhạc cổ điển và nhạc mộc**: `Baroque, Orchestral Score, Piano Ballad`

## Nhạc cụ và kết cấu

Lyria tự động chọn nhạc cụ phù hợp cho thể loại được yêu cầu. Nếu bạn muốn nhạc cụ cụ thể hoặc tổ hợp nhạc cụ bất thường, hãy khai báo rõ ràng:

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

Mô tả âm thanh và cách các nhạc cụ tương tác với nhau để tạo ra tâm trạng và kết cấu:

- Một đường bass 303 méo mó xuyên qua tiếng hi-hat sắc nét, mạnh mẽ
- Tiếng synth analog ấm áp, vang vọng dưới tiếng guitar mộc mạc, gần gũi
- Một bức tường âm thanh được tạo nên từ nhiều lớp guitar fuzz, với giọng hát vang vọng từ xa

### Từ khoá về nhạc cụ

- **Bàn phím và đàn synthesizer**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **Bass & Drums**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **Đàn ghi-ta và dây đàn**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **Nhạc cụ hơi và nhạc cụ đồng**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **Nhạc cụ gõ**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## Cấu trúc và thời gian của bài hát

Đối với Lyria 3.5, hãy xác định tiến trình của bài hát bằng cách sử dụng thẻ hoặc mũi tên:

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- Bắt đầu bằng một đoạn nhạc piano nhẹ nhàng, chuyển sang một đoạn nhạc có nhịp điệu mạnh mẽ, tạm dừng một chút rồi bùng nổ ở đoạn điệp khúc.

Bạn có thể điều chỉnh động lực và quá trình chuyển đổi năng lượng:

- Tạo cao trào qua đoạn tiền điệp khúc, sau đó giảm âm lượng xuống mức im lặng trước khi điệp khúc bùng nổ
- Tăng dần âm lượng trong suốt bài hát, thêm một nhạc cụ cho mỗi phần
- Một đoạn nhạc đột ngột dừng lại sau đoạn chuyển, tiếp theo là một đoạn điệp khúc hát a cappella

Bạn cũng có thể nhắc các dấu thời gian cụ thể:

- Tạo hiệu ứng tăng dần đến khi nhịp điệu mạnh xuất hiện ở giây thứ 12
- Mẫu giọng hát lặp lại sau mỗi 4 ô nhịp
- Đoạn điệp khúc bắt đầu ở giây thứ 22

## Lời bài hát và giọng hát

Theo mặc định, Lyria 3.5 sẽ tạo các bản nhạc có giọng hát và lời bài hát. Bạn có thể cung cấp lời bài hát của riêng mình, yêu cầu mô hình tạo lời bài hát hoặc yêu cầu một bản nhạc không lời.

### Sử dụng lời bài hát của riêng bạn

Thêm lời bài hát trực tiếp vào câu lệnh bên dưới tiêu đề `Lyrics:`. Gắn thẻ cho từng phần để hướng dẫn cách truyền tải giọng nói:

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

Sử dụng dấu ngoặc đơn cho giọng hát bè, tiếng vọng hoặc câu ứng tác, chẳng hạn như `(moving on)`.

### Chỉ đạo lời bài hát được tạo

Khi yêu cầu Lyria 3.5 viết lời bài hát, hãy phác thảo cốt truyện, cảm xúc hoặc các cụm từ chính:

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

Đối với thể loại nhạc điện tử và nhạc dance, hãy yêu cầu đoạn hát trước khi vào điệp khúc ngắn lặp lại:

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### Cách thể hiện giọng hát và hồ sơ ca sĩ

Chỉ định giới tính, quãng giọng và âm sắc để có bản phối chính xác:

- **Nữ cao**: Âm sắc trong trẻo, tinh khiết, có khả năng truyền tải linh hoạt và cao vút. Âm sắc tươi sáng, có khả năng tạo ra những kết cấu thoáng đãng, có hơi thở.
- **Nữ trung**: Giọng trầm, ấm áp và khàn. Giọng khàn đặc trưng với giọng ngực vang vọng, đầy cảm xúc.
- **Nam cao**: Sáng, chói và tràn đầy năng lượng. Âm sắc trẻ trung với khả năng hát cao và vang, nổi bật trong các bản phối dày đặc.
- **Giọng nam trung**: Giọng ngực trầm, mượt mà như nhung, ấm áp, êm dịu và ngân nga.
- **Weathered Rocker** (Người chơi nhạc rock từng trải): Âm sắc khàn, thô ráp gợi nhớ đến nhạc rock thay thế của những năm 1990. Cường độ cảm xúc thô mộc với những nốt cao căng thẳng.

### Hiệu ứng giọng hát không lời

Bạn cũng có thể đưa ra câu lệnh cho đoạn hội thoại, đoạn nhạc có giọng hát và hiệu ứng lấy mẫu:

- Giọng nói của một chương trình phát thanh cổ điển giới thiệu bài hát trước khi nhịp điệu bắt đầu
- Một giọng nói thì thầm ngay trước đoạn nhạc cao trào, sau đó là những âm thanh điện tử sôi động
- Các mẫu giọng hát bị cắt và thay đổi cao độ lặp lại như một yếu tố nhịp điệu nhạc cụ

## Thông số âm nhạc

Tinh chỉnh câu lệnh bằng các thuộc tính âm nhạc tiêu chuẩn:

- **Nhịp độ (BPM)**: Đặt trực tiếp nhịp độ (ví dụ: `120 BPM`, `slow tempo around 72 BPM`, `fast 160 BPM`).
- **Khoá và điệu thức**: Chỉ định khoá gốc và điệu thức (ví dụ: `in G major`, `in D minor`, `in C pentatonic`).
- **Tâm trạng và bầu không khí**: Sử dụng các tính từ mô tả cảm xúc:
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## Sử dụng câu lệnh cho Lyria RealTime

Lyria RealTime sử dụng **câu lệnh có trọng số** thay vì một chuỗi câu lệnh nguyên khối duy nhất. Nhờ đó, bạn có thể kết hợp nhiều nguồn cảm hứng âm nhạc một cách linh hoạt và liên tục điều chỉnh nhạc thông qua kết nối WebSocket.

### Cấu trúc câu lệnh có trọng số

Mỗi câu lệnh có trọng số bao gồm một cụm từ văn bản mô tả và một trọng số dấu phẩy động:

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### Chiến lược điều hướng theo thời gian thực

- **Kết hợp các thể loại**: Kết hợp các phong cách riêng biệt bằng cách chỉ định trọng số cân bằng:
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **Chuyển cảnh linh hoạt**: Để chuyển nhạc một cách mượt mà, hãy điều chỉnh trọng số của câu lệnh theo thời gian:
  1. Bắt đầu với `chill jazz piano (weight: 1.0)`
  2. Thêm dần `electronic breakbeat (weight: 0.3)`.
  3. Tăng `electronic breakbeat` lên `0.8` trong khi giảm `chill jazz piano` xuống `0.3`.
- **Xếp lớp các phần tử**: Tách riêng thẻ nhạc cụ và thẻ tâm trạng để bạn có thể điều chỉnh từng thẻ một cách độc lập:
  - Câu lệnh 1: `bossa nova guitar (weight: 0.9)`
  - Câu lệnh 2: `warm acoustic bass (weight: 0.7)`
  - Câu lệnh 3: `subtle vinyl crackle (weight: 0.3)`

## Câu lệnh mẫu

### Ví dụ về Lyria 3.5

- **Lo-Fi Study Beat**:
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **Pop Anthem** (Bài hát pop truyền cảm hứng):
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **Cyberpunk điện ảnh**:
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Bộ điều khiển Lyria RealTime

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

## Bước tiếp theo

- [Tạo nhạc bằng Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=vi): Tạo các bài hát hoàn chỉnh và đoạn nhạc dài 30 giây bằng Interactions API.
- [Tạo nhạc theo thời gian thực bằng Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=vi): Tạo các ứng dụng phát nhạc trực tuyến, tương tác theo thời gian thực qua WebSockets.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-18 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-18 UTC."],[],[]]
