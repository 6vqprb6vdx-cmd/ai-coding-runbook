---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=vi
fetched_at: 2026-08-31T06:28:31.797572+00:00
title: "T\u00ecm hi\u1ec3u th\u00f4ng tin c\u01a1 b\u1ea3n tr\u00ean Google T\u00ecm ki\u1ebfm \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tìm hiểu thông tin cơ bản trên Google Tìm kiếm

Tính năng Bám sát nguồn bằng Google Tìm kiếm kết nối mô hình Gemini với nội dung trên web theo thời gian thực và hỗ trợ tất cả các ngôn ngữ hiện có. Nhờ đó, Gemini có thể đưa ra câu trả lời chính xác hơn và trích dẫn các nguồn có thể xác minh ngoài điểm cắt kiến thức.

Cơ sở kiến thức giúp bạn xây dựng các ứng dụng có thể:

- **Tăng độ chính xác về thông tin thực tế:** Giảm tình trạng ảo tưởng của mô hình bằng cách dựa vào thông tin thực tế để đưa ra câu trả lời.
- **Truy cập thông tin theo thời gian thực:** Trả lời các câu hỏi về những sự kiện và chủ đề gần đây.
- **Cung cấp thông tin trích dẫn:** Xây dựng lòng tin của người dùng bằng cách cho thấy nguồn của các tuyên bố của mô hình.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.7-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.7-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Cách hoạt động của tính năng neo bám vào Google Tìm kiếm

Khi bạn bật công cụ `google_search`, mô hình sẽ tự động xử lý toàn bộ quy trình tìm kiếm, xử lý và trích dẫn thông tin.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=vi)

1. **Câu lệnh của người dùng:** Ứng dụng của bạn gửi câu lệnh của người dùng đến Gemini API khi bật công cụ `google_search`.
2. **Phân tích câu lệnh:** Mô hình phân tích câu lệnh và xác định xem Google Tìm kiếm có thể cải thiện câu trả lời hay không.
3. **Google Tìm kiếm:** Nếu cần, mô hình sẽ tự động tạo một hoặc nhiều cụm từ tìm kiếm và thực hiện các cụm từ đó.
4. **Xử lý kết quả tìm kiếm:** Mô hình xử lý kết quả tìm kiếm, tổng hợp thông tin và đưa ra câu trả lời.
5. **Câu trả lời bám sát nguồn:** API trả về một câu trả lời cuối cùng, thân thiện với người dùng và bám sát nguồn là các kết quả tìm kiếm. Phản hồi này bao gồm câu trả lời bằng văn bản của mô hình có `annotations` nội tuyến chứa các trích dẫn, cũng như các bước `google_search_call` và `google_search_result` với cụm từ tìm kiếm và đề xuất tìm kiếm.

## Tìm hiểu về câu trả lời dựa trên thông tin thực tế

Khi một câu trả lời được căn cứ thành công, đầu ra văn bản của mô hình sẽ bao gồm `annotations` nội tuyến ngay trên khối nội dung văn bản. Những chú thích này cung cấp thông tin trích dẫn, liên kết các phần của câu trả lời với nguồn của chúng.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

Các trường khoá trong phản hồi:

- `google_search_call` : Chứa cụm từ tìm kiếm `queries` mà mô hình đã thực thi.
- `google_search_result` : Chứa `search_suggestions`, một đoạn mã HTML để hiển thị các đề xuất tìm kiếm trong giao diện người dùng của bạn. Các yêu cầu đầy đủ về việc sử dụng được nêu chi tiết trong [Điều khoản dịch vụ](https://ai.google.dev/gemini-api/terms?hl=vi#grounding-with-google-search).
- `text` có `annotations` : Câu trả lời do mô hình tổng hợp có trích dẫn nội dòng. Mỗi chú thích `url_citation` liên kết một đoạn văn bản (do `start_index` và `end_index` xác định) với một URL nguồn. Đây là chìa khoá để tạo trích dẫn nội dòng.

Bạn cũng có thể sử dụng tính năng Neo bám vào Google Tìm kiếm kết hợp với [công cụ ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) để neo bám các câu trả lời bằng cả dữ liệu trên web công khai và các URL cụ thể mà bạn cung cấp.

## Phân bổ nguồn bằng trích dẫn ngay trong văn bản

API này trả về chú thích `url_citation` nội tuyến trên khối nội dung văn bản, giúp bạn hoàn toàn kiểm soát cách hiển thị nguồn trong giao diện người dùng.
Mỗi chú thích đều có `start_index` và `end_index` để xác định phần văn bản mà chú thích trích dẫn. Sau đây là cách trích xuất và hiển thị các giá trị này.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

Đầu ra sẽ cho thấy văn bản, theo sau là các trích dẫn:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Giá

Khi bạn sử dụng tính năng Neo bám vào Google Tìm kiếm với Gemini 3, dự án của bạn sẽ bị tính phí cho mỗi cụm từ tìm kiếm mà mô hình quyết định thực hiện. Nếu mô hình quyết định thực hiện nhiều cụm từ tìm kiếm để trả lời một câu lệnh duy nhất (ví dụ: tìm kiếm `"UEFA Euro 2024 winner"` và `"Spain vs England Euro 2024 final
score"` trong cùng một lệnh gọi API), thì điều này được tính là hai lần sử dụng công cụ có tính phí cho yêu cầu đó. Để tính phí, chúng tôi bỏ qua các cụm từ tìm kiếm trống trên web khi tính số lượng cụm từ tìm kiếm riêng biệt. Mô hình tính phí này chỉ áp dụng cho các mô hình Gemini 3; khi bạn sử dụng tính năng tìm kiếm thông tin cơ sở với các mô hình Gemini 2.5 trở xuống, dự án của bạn sẽ được tính phí theo từng câu lệnh.

Để biết thông tin chi tiết về giá, hãy xem [trang định giá Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Mô hình được hỗ trợ

Bạn có thể xem toàn bộ các chức năng trên trang [tổng quan về mô hình](https://ai.google.dev/gemini-api/docs/models?hl=vi).

| Mô hình | Bám sát nguồn bằng Google Tìm kiếm |
| --- | --- |
| Gemini 3.7 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Bản xem trước hình ảnh Gemini 3.1 Flash | ✔️ |
| Gemini 3.1 Pro (Bản xem trước) | ✔️ |
| Bản xem trước hình ảnh của Gemini 3 Pro | ✔️ |
| Bản xem trước Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Các tổ hợp công cụ được hỗ trợ

Bạn có thể sử dụng tính năng Neo bám vào Google Tìm kiếm với các công cụ khác như [thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi), [Bối cảnh từ URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) và [Neo bám vào Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi) (được hỗ trợ trên Gemini 3.5 Flash và các mô hình sau này) để hỗ trợ các trường hợp sử dụng phức tạp hơn. Các mô hình Gemini 3 cũng hỗ trợ kết hợp những công cụ tích hợp này với các công cụ tuỳ chỉnh (gọi hàm). Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

## Bước tiếp theo

- Tìm hiểu về các công cụ khác hiện có, chẳng hạn như [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).
- Tìm hiểu cách tăng cường câu lệnh bằng các URL cụ thể bằng [công cụ bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-08-20 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-08-20 UTC."],[],[]]
