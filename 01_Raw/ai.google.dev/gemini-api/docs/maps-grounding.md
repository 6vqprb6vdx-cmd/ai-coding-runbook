---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi
fetched_at: 2026-07-27T04:39:05.150905+00:00
title: "C\u0103n c\u1ee9 v\u00e0o Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Căn cứ vào Google Maps

Tính năng Bám sát nguồn bằng Google Maps kết hợp các khả năng tạo sinh của Gemini với dữ liệu phong phú, thực tế và mới nhất của Google Maps. Tính năng này giúp nhà phát triển dễ dàng tích hợp chức năng nhận biết vị trí vào ứng dụng của họ. Khi truy vấn của người dùng có bối cảnh liên quan đến dữ liệu Maps, mô hình Gemini sẽ tận dụng Google Maps để cung cấp câu trả lời chính xác và mới nhất, phù hợp với vị trí cụ thể hoặc khu vực chung mà người dùng chỉ định.

- **Câu trả lời chính xác, nhận biết vị trí:** Tận dụng dữ liệu phong phú và hiện tại của Google Maps cho các truy vấn theo vị trí địa lý.
- **Cá nhân hoá nâng cao:** Điều chỉnh đề xuất và thông tin dựa trên vị trí do người dùng cung cấp.

## Bắt đầu

Ví dụ này minh hoạ cách tích hợp tính năng Bám sát nguồn bằng Google Maps vào ứng dụng của bạn để cung cấp câu trả lời chính xác, nhận biết vị trí cho các truy vấn của người dùng. Lời nhắc yêu cầu các đề xuất tại địa phương kèm theo vị trí không bắt buộc của người dùng, cho phép mô hình Gemini sử dụng dữ liệu của Google Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Cách hoạt động của tính năng Bám sát nguồn bằng Google Maps

Tính năng Bám sát nguồn bằng Google Maps tích hợp Gemini API với hệ sinh thái Google Geo bằng cách sử dụng Maps API làm nguồn bám sát nguồn. Khi truy vấn của người dùng chứa bối cảnh địa lý, mô hình Gemini có thể gọi công cụ Bám sát nguồn bằng Google Maps. Sau đó, mô hình này có thể tạo câu trả lời dựa trên dữ liệu của Google Maps liên quan đến vị trí được cung cấp.

Quá trình này thường bao gồm:

1. **Truy vấn của người dùng:** Người dùng gửi một truy vấn đến ứng dụng của bạn, có thể bao gồm bối cảnh địa lý (ví dụ: "quán cà phê gần tôi", "bảo tàng ở San Francisco").
2. **Gọi công cụ:** Mô hình Gemini nhận ra ý định địa lý, gọi công cụ Bám sát nguồn bằng Google Maps. Bạn có thể cung cấp `latitude` và `longitude` của người dùng cho công cụ này. Công cụ này là một công cụ tìm kiếm bằng văn bản và hoạt động tương tự như tìm kiếm trên Maps, trong đó các truy vấn tại địa phương ("gần tôi") sẽ sử dụng toạ độ, trong khi các truy vấn cụ thể hoặc không tại địa phương sẽ không bị ảnh hưởng bởi vị trí rõ ràng.
3. **Truy xuất dữ liệu:** Dịch vụ Bám sát nguồn bằng Google Maps truy vấn Google Maps để tìm thông tin liên quan (ví dụ: địa điểm, bài đánh giá, ảnh, địa chỉ, giờ mở cửa).
4. **Tạo sinh dựa trên nguồn:** Dữ liệu Maps đã truy xuất được dùng để cung cấp thông tin cho câu trả lời của mô hình Gemini, đảm bảo tính chính xác và mức độ liên quan.
5. **Câu trả lời và chú thích:** Mô hình này trả về câu trả lời bằng văn bản kèm theo chú thích nội tuyến liên kết đến các nguồn trên Google Maps, cho phép nhà phát triển hiển thị trích dẫn.

## Lý do và thời điểm sử dụng tính năng Bám sát nguồn bằng Google Maps

Tính năng Bám sát nguồn bằng Google Maps là lựa chọn lý tưởng cho các ứng dụng yêu cầu thông tin chính xác, mới nhất và theo vị trí. Tính năng này giúp nâng cao trải nghiệm người dùng bằng cách cung cấp nội dung phù hợp và được cá nhân hoá dựa trên cơ sở dữ liệu phong phú của Google Maps về hơn 250 triệu địa điểm trên toàn thế giới.

Bạn nên sử dụng tính năng Bám sát nguồn bằng Google Maps khi ứng dụng của bạn cần:

- Cung cấp câu trả lời đầy đủ và chính xác cho các câu hỏi theo vị trí địa lý.
- Xây dựng công cụ lập kế hoạch chuyến đi và hướng dẫn viên địa phương dựa trên cuộc trò chuyện.
- Đề xuất các địa điểm yêu thích dựa trên vị trí và lựa chọn ưu tiên của người dùng, chẳng hạn như nhà hàng hoặc cửa hàng.
- Tạo trải nghiệm nhận biết vị trí cho các dịch vụ xã hội, bán lẻ hoặc giao đồ ăn.

Tính năng Bám sát nguồn bằng Google Maps vượt trội trong các trường hợp sử dụng mà khoảng cách và dữ liệu thực tế hiện tại là rất quan trọng, chẳng hạn như tìm "quán cà phê ngon nhất gần tôi" hoặc nhận chỉ đường.

## Trường hợp sử dụng

Tính năng Bám sát nguồn bằng Google Maps hỗ trợ nhiều trường hợp sử dụng nhận biết vị trí.

### Xử lý các câu hỏi cụ thể về địa điểm

Đặt câu hỏi chi tiết về một địa điểm cụ thể để nhận câu trả lời dựa trên bài đánh giá của người dùng Google và các dữ liệu khác trên Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Cung cấp tính năng cá nhân hoá dựa trên vị trí

Nhận các đề xuất phù hợp với lựa chọn ưu tiên của người dùng và một khu vực địa lý cụ thể.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Hỗ trợ lập kế hoạch hành trình

Tạo kế hoạch nhiều ngày kèm theo chỉ đường và thông tin về nhiều địa điểm, phù hợp với các ứng dụng du lịch.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Yêu cầu về việc sử dụng dịch vụ

Phần này mô tả các yêu cầu về việc sử dụng dịch vụ đối với tính năng Bám sát nguồn bằng Google Maps.

### Thông báo cho người dùng về việc sử dụng các nguồn trên Google Maps

Với mỗi kết quả Bám sát nguồn bằng Google Maps, bạn sẽ nhận được chú thích nguồn trên các khối nội dung của bước `model_output` hỗ trợ từng câu trả lời. Siêu dữ liệu sau đây sẽ được trả về:

- URL nguồn
- tên

Khi trình bày kết quả từ tính năng Bám sát nguồn bằng Google Maps, bạn phải chỉ định các nguồn liên kết trên Google Maps và thông báo cho người dùng của bạn về những điều sau:

- Các nguồn trên Google Maps phải xuất hiện ngay sau nội dung được tạo mà các nguồn đó hỗ trợ. Nội dung được tạo này còn được gọi là Kết quả Bám sát nguồn bằng Google Maps.
- Các nguồn trên Google Maps phải có thể xem được trong một lượt tương tác của người dùng.

### Hiển thị các nguồn trên Google Maps kèm theo đường liên kết trên Google Maps

Đối với mỗi chú thích nguồn, bạn phải tạo bản xem trước đường liên kết theo các yêu cầu sau:

- Ghi công từng nguồn cho Google Maps theo nguyên tắc ghi công văn bản của Google Maps
  .
- Hiển thị tên nguồn được cung cấp trong câu trả lời.
- Liên kết đến nguồn bằng `url` từ chú thích.

### Nguyên tắc ghi công văn bản của Google Maps

Khi bạn ghi công các nguồn cho Google Maps bằng văn bản, hãy tuân theo các nguyên tắc sau:

- Không sửa đổi văn bản Google Maps theo bất kỳ cách nào:
  - Không thay đổi cách viết hoa của Google Maps.
  - Không chuyển Google Maps sang nhiều dòng.
  - Không bản địa hoá Google Maps sang ngôn ngữ khác.
  - Ngăn trình duyệt dịch Google Maps bằng cách sử dụng thuộc tính HTML translate="no".

Để biết thêm thông tin về một số nhà cung cấp dữ liệu của Google Maps và điều khoản cấp phép của họ, hãy xem [thông báo pháp lý của Google Maps và Google Earth](https://www.google.com/help/legalnotices_maps/?hl=vi).

## Các phương pháp hay nhất

- **Cung cấp vị trí của người dùng:** Để có câu trả lời phù hợp và được cá nhân hoá nhất, hãy luôn thêm `latitude` và `longitude` vào cấu hình công cụ `google_maps` khi bạn biết vị trí của người dùng.
- **Thông báo cho người dùng cuối:** Thông báo rõ ràng cho người dùng cuối rằng dữ liệu của Google Maps đang được sử dụng để trả lời các truy vấn của họ, đặc biệt là khi công cụ này được bật.
- **Tắt khi không cần:** Tính năng Bám sát nguồn bằng Google Maps được tắt theo mặc định. Chỉ bật tính năng này (`"tools": [{"type": "google_maps"}]`) khi truy vấn có
  bối cảnh địa lý rõ ràng để tối ưu hoá hiệu suất và chi phí.

## Các điểm hạn chế

- Tính năng Bám sát nguồn bằng Google Maps hiện chỉ hỗ trợ lời nhắc và câu trả lời bằng tiếng Anh.
- Công cụ này có thể không dùng được ở một số khu vực.
- Kết quả có thể khác nhau dựa trên độ chính xác của vị trí và dữ liệu Maps hiện có.
- **Phạm vi địa lý:** Tính năng Bám sát nguồn bằng Google Maps có trên toàn cầu.
- **Trạng thái mặc định:** Công cụ Bám sát nguồn bằng Google Maps được tắt theo mặc định.
  Bạn phải bật công cụ này một cách rõ ràng trong các yêu cầu API.

## Giá và hạn mức về giá

Giá của tính năng Bám sát nguồn bằng Google Maps sẽ khác nhau tuỳ thuộc vào thế hệ mô hình:

- **Mô hình Gemini 3:** Dự án của bạn sẽ bị tính phí cho mỗi **truy vấn tìm kiếm** mà mô hình quyết định thực thi. Một **lời nhắc tìm kiếm** (yêu cầu API của bạn đối với mô hình) có thể khiến mô hình thực thi nhiều truy vấn tìm kiếm để tìm thông tin cần thiết. Mỗi truy vấn này được tính là một lần sử dụng công cụ có tính phí.
- **Mô hình Gemini 2.5 và các mô hình cũ hơn:** Dự án của bạn sẽ bị tính phí cho mỗi **lời nhắc tìm kiếm**.
  Yêu cầu chỉ bị tính phí nếu lời nhắc trả về thành công ít nhất một kết quả bám sát nguồn bằng Google Maps, bất kể mô hình đã thực hiện bao nhiêu truy vấn tìm kiếm riêng lẻ ở nội bộ để nhận được kết quả đó.

Để biết thông tin chi tiết về giá, hãy xem [trang giá của Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng Bám sát nguồn bằng Google Maps:

| Mô hình | Bám sát nguồn bằng Google Maps |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ |
| [Gemini 3.1 Pro Bản dùng thử](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Gemini 3 Flash Bản dùng thử](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Các cách kết hợp công cụ được hỗ trợ

Mô hình Gemini 3 hỗ trợ kết hợp các công cụ tích hợp (như Bám sát nguồn bằng Google Maps) với các công cụ tuỳ chỉnh (gọi hàm). Tìm hiểu thêm trên trang các cách kết hợp công cụ
.

## Bước tiếp theo

- Tìm hiểu về các [công cụ khác hiện có](https://ai.google.dev/gemini-api/docs/tools?hl=vi).
- Để tìm hiểu thêm về các phương pháp hay nhất về AI có trách nhiệm và bộ lọc an toàn của Gemini API, hãy xem [hướng dẫn về chế độ cài đặt An toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-06 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-06 UTC."],[],[]]
