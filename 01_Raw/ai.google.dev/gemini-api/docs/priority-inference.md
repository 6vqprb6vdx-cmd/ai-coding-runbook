---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi
fetched_at: 2026-11-02T07:24:53.051606+00:00
title: "Suy lu\u1eadn m\u1ee9c \u0111\u1ed9 \u01b0u ti\u00ean \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Suy luận mức độ ưu tiên

Nội dung mô tả: Tìm hiểu cách tối ưu hoá độ trễ bằng cấp suy luận Ưu tiên trong Interactions API

Gemini Priority API là một cấp suy luận cao cấp được thiết kế cho
khối lượng công việc quan trọng của doanh nghiệp, đòi hỏi độ trễ thấp hơn và
độ tin cậy cao nhất với mức giá cao. Lưu lượng truy cập theo cấp ưu tiên được ưu tiên hơn lưu lượng truy cập theo API tiêu chuẩn và cấp linh hoạt.

Bạn có thể suy luận mức độ ưu tiên trên các điểm cuối Interactions API.

## Cách sử dụng Mức độ ưu tiên

Để sử dụng Cấp ưu tiên, hãy đặt trường `service_tier` trong yêu cầu thành `priority`. Cấp mặc định là cấp tiêu chuẩn nếu bạn bỏ qua trường này.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Perform a priority inference task."))
        .serviceTier(ServiceTier.PRIORITY)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Perform a priority inference task."),
            ServiceTier: interactions.ServiceTierPriority.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Cách hoạt động của tính năng suy luận mức độ ưu tiên

Tính năng suy luận ưu tiên sẽ định tuyến các yêu cầu đến hàng đợi điện toán có mức độ nghiêm trọng cao, mang lại hiệu suất nhanh và dễ dự đoán cho các ứng dụng mà người dùng sử dụng. Cơ chế chính của tính năng này là hạ cấp nhẹ nhàng phía máy chủ xuống quy trình xử lý tiêu chuẩn cho lưu lượng truy cập vượt quá giới hạn động, đảm bảo độ ổn định của ứng dụng thay vì không thực hiện được yêu cầu.

| Tính năng | Mức độ ưu tiên | Chuẩn | Gập | Theo nhóm |
| --- | --- | --- | --- | --- |
| **Định giá** | Cao hơn 75 – 100% so với gói Standard | Giá đầy đủ | Giảm giá 50% | Giảm giá 50% |
| **Độ trễ** | Giây | Giây sang phút | Phút (mục tiêu từ 1 đến 15 phút) | Tối đa 24 giờ |
| **Độ tin cậy** | Cao (Không thể giảm tải) | Cao / Trung bình cao | Nỗ lực tối đa (Có thể loại bỏ) | Cao (cho thông lượng) |
| **Giao diện** | Đồng bộ | Đồng bộ | Đồng bộ | Không đồng bộ |

### Lợi ích chính

- **Độ trễ thấp**: Được thiết kế để phản hồi trong vài giây cho các công cụ AI tương tác, dành cho người dùng.
- **Độ tin cậy cao**: Lưu lượng truy cập được xử lý với mức độ quan trọng cao nhất và
  hoàn toàn không thể bị loại bỏ.
- **Giảm hiệu suất một cách từ từ**: Các đợt tăng đột biến lưu lượng truy cập vượt quá hạn mức linh hoạt sẽ tự động được hạ cấp xuống cấp độ Tiêu chuẩn để xử lý thay vì thất bại, ngăn chặn tình trạng ngừng dịch vụ.
- **Ít rắc rối**: Sử dụng cùng phương thức `create` đồng bộ như các cấp tiêu chuẩn và linh hoạt.

### Trường hợp sử dụng

Xử lý ưu tiên là lựa chọn lý tưởng cho những quy trình quan trọng đối với hoạt động kinh doanh, trong đó hiệu suất và độ tin cậy là yếu tố tối quan trọng.

- **Ứng dụng AI tương tác**: Chatbot và trợ lý dịch vụ khách hàng, nơi người dùng trả phí cao và mong đợi phản hồi nhanh, nhất quán.
- **Công cụ đưa ra quyết định theo thời gian thực**: Hệ thống yêu cầu về hệ thống có độ tin cậy cao và độ trễ thấp, chẳng hạn như phân loại phiếu yêu cầu hỗ trợ trực tiếp hoặc phát hiện hành vi gian lận.
- **Các tính năng dành cho khách hàng cao cấp**: Nhà phát triển cần đảm bảo mục tiêu mức độ dịch vụ (SLO) cao hơn cho khách hàng trả phí.

### Giới hạn số lượng yêu cầu

Mức sử dụng ưu tiên có giới hạn tốc độ riêng, mặc dù mức sử dụng được tính vào [giới hạn tốc độ lưu lượng truy cập tương tác tổng thể](https://aistudio.google.com/rate-limit?hl=vi). Hạn mức mặc định
cho tính năng Suy luận ưu tiên là **0,3 lần hạn mức tiêu chuẩn cho Mô hình / Cấp**

### Logic hạ cấp từng bước

Nếu vượt quá hạn mức của dịch vụ Ưu tiên do tắc nghẽn, các yêu cầu vượt quá hạn mức sẽ được **tự động và nhẹ nhàng** hạ cấp xuống dịch vụ xử lý Tiêu chuẩn thay vì không thực hiện được và trả về lỗi 503 hoặc 429. Các yêu cầu bị hạ cấp sẽ được tính phí theo mức giá tiêu chuẩn, chứ không phải mức giá cao cấp của dịch vụ Ưu tiên.

### Trách nhiệm của khách hàng

- **Giám sát phản hồi**: Nhà phát triển nên giám sát tiêu đề `x-gemini-service-tier` trong phản hồi của API để phát hiện xem các yêu cầu có thường xuyên bị hạ cấp xuống `standard` hay không.
- **Thử lại**: Ứng dụng phải triển khai logic thử lại/thuật toán đợi luỹ tiến cho các lỗi tiêu chuẩn, chẳng hạn như `DEADLINE_EXCEEDED`.

## Giá

Dịch vụ suy luận ưu tiên có giá cao hơn từ 75% đến 100% so với [API tiêu chuẩn](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) và được tính phí theo mã thông báo.

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ suy luận Ưu tiên:

| Mô hình | Suy luận ưu tiên |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=vi) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=vi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=vi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Bước tiếp theo

- [Suy luận linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi) để giảm chi phí.
- [Mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi): Tìm hiểu về mã thông báo.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-13 UTC."],[],[]]
