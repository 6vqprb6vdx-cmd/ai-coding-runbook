---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=vi
fetched_at: 2026-09-07T05:31:09.101872+00:00
title: "Gi\u1ea3i th\u00edch v\u1ec1 c\u00e1c phi\u00ean b\u1ea3n API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu tham khảo API](https://ai.google.dev/api?hl=vi)

Gửi ý kiến phản hồi

# Giải thích về các phiên bản API

Tài liệu này cung cấp thông tin tổng quan cấp cao về sự khác biệt giữa phiên bản `v1` và `v1beta` của Gemini API.

- **v1**: Phiên bản ổn định của API. Các tính năng trong phiên bản ổn định được hỗ trợ đầy đủ trong suốt thời gian tồn tại của phiên bản lớn. Nếu có bất kỳ thay đổi có thể gây lỗi nào, một phiên bản lớn mới của API sẽ được tạo và phiên bản hiện có sẽ bị ngừng hoạt động sau một khoảng thời gian hợp lý.
  Bạn có thể giới thiệu các thay đổi không làm gián đoạn API mà không cần thay đổi phiên bản lớn. **Interactions API** và các tính năng cốt lõi của API này thường có trong `v1`.
- **v1beta**: Phiên bản này bao gồm các tính năng và chức năng ban đầu đang được phát triển tích cực. Mặc dù các tính năng trong `v1beta` có thể thay đổi khi chúng tôi tinh chỉnh dựa trên ý kiến phản hồi, nhưng bạn có thể dùng thử các tính năng mới trước khi chúng được chuyển sang phiên bản ổn định.

## Khả năng và phạm vi hỗ trợ tính năng

Bảng sau đây trình bày chi tiết về khả năng sử dụng các tính năng trên `v1` (GA) và `v1beta` (Beta). Các chức năng và công cụ API cốt lõi áp dụng cho cả API Tương tác và `generateContent`, trừ phi có quy định khác:

| Tính năng | v1 | v1beta |
| --- | --- | --- |
| **Các chức năng chính của API** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=vi) |  |  |
| [Lệnh gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) |  |  |
| [Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi) |  |  |
| [Tư duy / Suy luận](https://ai.google.dev/gemini-api/docs/thinking?hl=vi) |  |  |
| [Hướng dẫn về hệ thống](https://ai.google.dev/gemini-api/docs/system-instructions?hl=vi) |  |  |
| [Đầu ra âm thanh (Cấu hình lời nói)](https://ai.google.dev/gemini-api/docs/audio?hl=vi) |  |  |
| [Cấp dịch vụ (Ưu tiên / Linh hoạt)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi) |  |  |
| **Công cụ** |  |  |
| [Công cụ thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) |  |  |
| [Cơ sở dữ liệu của Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) |  |  |
| [Cơ sở dữ liệu địa lý của Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi) |  |  |
| [Công cụ Bối cảnh từ URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) |  |  |
| [Công cụ tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi) |  |  |
| [Công cụ sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi) |  |  |
| [Công cụ máy chủ MCP](https://ai.google.dev/gemini-api/docs/eap/remote_mcp?hl=vi) |  |  |
| **Realtime APIs** |  |  |
| [Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=vi) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=vi) |  |  |
| [Mã thông báo tạm thời (Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=vi) |  |  |
| **Platform API** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=vi) |  |  |
| [Files Service Route](https://ai.google.dev/gemini-api/docs/files?hl=vi) |  |  |
| [File Search Stores Route](https://ai.google.dev/gemini-api/docs/file-search?hl=vi) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=vi) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=vi) |  |  |
| [Lưu ngữ cảnh vào bộ nhớ đệm](https://ai.google.dev/gemini-api/docs/caching?hl=vi) |  |  |

- – Được hỗ trợ

## Định cấu hình phiên bản API trong SDK

Các SDK của Gemini API mặc định là `v1beta`, nhưng bạn có thể chỉ định rõ ràng các phiên bản bằng cách đặt phiên bản API như trong mẫu mã sau:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.7-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.7-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client = Client.builder()
    .httpOptions(HttpOptions.builder().apiVersion("v1").build())
    .build();

CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.6-flash"))
    .input(InteractionsInput.of("Explain how AI works"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.7-flash",
    "input": "Explain how AI works",
  }'
```

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-01 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-01 UTC."],[],[]]
