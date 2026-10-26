---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=vi
fetched_at: 2026-10-26T06:00:45.333335+00:00
title: "Suy lu\u1eadn m\u1ee9c \u0111\u1ed9 \u01b0u ti\u00ean \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Suy luận mức độ ưu tiên

Nội dung mô tả: Tìm hiểu cách tối ưu hoá độ trễ bằng Cấp suy luận ưu tiên

API Ưu tiên của Gemini là một cấp suy luận cao cấp được thiết kế cho các khối lượng công việc quan trọng đối với doanh nghiệp, đòi hỏi độ trễ thấp hơn và độ tin cậy cao nhất với mức giá cao cấp. Lưu lượng truy cập ở cấp ưu tiên được ưu tiên hơn lưu lượng truy cập ở API tiêu chuẩn và cấp linh hoạt.

Tính năng suy luận ưu tiên được cung cấp cho người dùng ở [Cấp 2 và Cấp 3](https://ai.google.dev/gemini-api/docs/billing?hl=vi#about-billing) trên các điểm cuối của API GenerateContent
và API Tương tác.

## Cách sử dụng Mức độ ưu tiên

Để sử dụng cấp Ưu tiên, hãy đặt trường `service_tier` trong nội dung yêu cầu thành `priority`. Cấp mặc định là tiêu chuẩn nếu bạn bỏ qua trường này.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.8-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Cách hoạt động của tính năng suy luận ưu tiên

Tính năng suy luận ưu tiên định tuyến các yêu cầu đến các hàng đợi tính toán có mức độ quan trọng cao, mang lại hiệu suất nhanh chóng và có thể dự đoán được cho các ứng dụng hướng đến người dùng. Cơ chế chính của tính năng này là hạ cấp một cách linh hoạt phía máy chủ xuống quy trình xử lý tiêu chuẩn đối với lưu lượng truy cập vượt quá các giới hạn linh động, đảm bảo tính ổn định của ứng dụng thay vì không thực hiện được yêu cầu.

| Tính năng | Mức độ ưu tiên | Chuẩn | Linh hoạt | Theo nhóm |
| --- | --- | --- | --- | --- |
| **Định giá** | Cao hơn 75 – 100% so với cấp Tiêu chuẩn | Giá đầy đủ | Chiết khấu 50% | Chiết khấu 50% |
| **Độ trễ** | Giây | Giây đến phút | Phút (mục tiêu 1 – 15 phút) | Tối đa 24 giờ |
| **Độ tin cậy** | Cao (Không thể loại bỏ) | Cao / Trung bình cao | Nỗ lực tối đa (Có thể loại bỏ) | Cao (đối với thông lượng) |
| **Giao diện** | Đồng bộ | Đồng bộ | Đồng bộ | Không đồng bộ |

### Lợi ích chính

- **Độ trễ thấp**: Được thiết kế để có thời gian phản hồi trong vài giây đối với các công cụ AI tương tác, dành cho người dùng.
- **Độ tin cậy cao**: Lưu lượng truy cập được xử lý với mức độ quan trọng cao nhất và
  hoàn toàn không thể loại bỏ.
- **Hạ cấp linh hoạt**: Các đợt tăng đột biến lưu lượng truy cập vượt quá giới hạn linh động sẽ
  tự động được hạ cấp xuống cấp Tiêu chuẩn để xử lý thay vì không thực hiện được,
  ngăn ngừa tình trạng ngừng dịch vụ.
- **Ít trở ngại**: Sử dụng cùng một phương thức đồng bộ `generateContent` như các cấp
  tiêu chuẩn và linh hoạt.

### Trường hợp sử dụng

Quy trình xử lý ưu tiên là lý tưởng cho các quy trình công việc quan trọng đối với doanh nghiệp, trong đó hiệu suất và độ tin cậy là tối quan trọng.

- **Ứng dụng AI tương tác**: Chatbot và trợ lý ảo dịch vụ khách hàng, trong đó
  người dùng trả phí cao cấp và mong đợi phản hồi nhanh chóng, nhất quán.
- **Công cụ đưa ra quyết định theo thời gian thực**: Các hệ thống yêu cầu yêu cầu về hệ thống có độ tin cậy cao và độ trễ thấp, chẳng hạn như phân loại phiếu yêu cầu hỗ trợ trực tiếp hoặc phát hiện gian lận.
- **Các tính năng cao cấp dành cho khách hàng**: Nhà phát triển cần đảm bảo các mục tiêu về mức độ cung cấp dịch vụ (SLO) cao hơn cho khách hàng trả phí.

### Giới hạn số lượng yêu cầu

Mức sử dụng ưu tiên có giới hạn số lượng yêu cầu riêng, mặc dù mức sử dụng được tính vào [giới hạn số lượng yêu cầu lưu lượng truy cập tương tác tổng thể](https://aistudio.google.com/rate-limit?hl=vi). Giới hạn số lượng yêu cầu mặc định cho tính năng suy luận ưu tiên là **0,3 lần giới hạn số lượng yêu cầu tiêu chuẩn cho Mô hình / Cấp**

### Logic hạ cấp linh hoạt

Nếu vượt quá giới hạn Mức độ ưu tiên do tắc nghẽn, các yêu cầu tràn sẽ được **tự động và linh hoạt** hạ cấp xuống quy trình xử lý Standard thay vì không thực hiện được với lỗi 503 hoặc 429. Các yêu cầu được hạ cấp sẽ được tính phí theo mức giá tiêu chuẩn, không phải mức giá cao cấp ưu tiên.

### Trách nhiệm của ứng dụng khách

- **Theo dõi phản hồi**: Nhà phát triển nên theo dõi `x-gemini-service-tier` tiêu đề trong phản hồi của API để phát hiện xem các yêu cầu có thường xuyên bị hạ cấp xuống `standard`.
- **Thử lại**: Ứng dụng khách phải triển khai logic thử lại/thuật toán thời gian đợi luỹ thừa đối với
  các lỗi tiêu chuẩn, chẳng hạn như `DEADLINE_EXCEEDED`.

## Định giá

Tính năng suy luận ưu tiên có giá cao hơn 75 – 100% so với [API tiêu chuẩn](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) và được tính phí theo mỗi mã thông báo.

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng suy luận ưu tiên:

| Mô hình | Suy luận ưu tiên |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=vi) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=vi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=vi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Bản xem trước Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Bản xem trước Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Bản xem trước hình ảnh Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Hình ảnh Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Bước tiếp theo

Đọc về các lựa chọn [suy luận và tối ưu hoá](https://ai.google.dev/gemini-api/docs/optimization?hl=vi) khác của Gemini:

- [Suy luận linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi) để giảm 50% chi phí.
- [API theo nhóm](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi) để xử lý không đồng bộ trong vòng 24 giờ.
- [Bộ nhớ đệm ngữ cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi) để giảm chi phí token đầu vào.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-13 UTC."],[],[]]
