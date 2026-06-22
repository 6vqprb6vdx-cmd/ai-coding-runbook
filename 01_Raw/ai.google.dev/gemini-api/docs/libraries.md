---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=vi
fetched_at: 2026-06-22T06:27:21.651000+00:00
title: "Th\u01b0 vi\u1ec7n Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Thư viện Gemini API

Khi xây dựng bằng Gemini API, bạn nên sử dụng **Google GenAI SDK**.
Đây là những thư viện chính thức, sẵn sàng cho hoạt động sản xuất mà chúng tôi phát triển và duy trì cho các ngôn ngữ phổ biến nhất. Các API này đang ở trạng thái [Được cung cấp công khai](https://ai.google.dev/gemini-api/docs/libraries?hl=vi#new-libraries) và được dùng trong tất cả tài liệu cũng như ví dụ chính thức của chúng tôi.

Nếu bạn mới làm quen với Gemini API, hãy làm theo [hướng dẫn bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi) của chúng tôi để bắt đầu.

## Hỗ trợ ngôn ngữ và cài đặt

Google GenAI SDK hiện hỗ trợ các ngôn ngữ Python, JavaScript/TypeScript, Go và Java. Bạn có thể cài đặt thư viện của từng ngôn ngữ bằng trình quản lý gói hoặc truy cập vào kho lưu trữ GitHub của các ngôn ngữ đó để tương tác thêm:

### Python

- Thư viện: [`google-genai`](https://pypi.org/project/google-genai)
- Kho lưu trữ GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Cài đặt: `pip install google-genai`

### JavaScript

- Thư viện: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- Kho lưu trữ GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Cài đặt: `npm install @google/genai`

### Go

- Thư viện: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- Kho lưu trữ GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Cài đặt: `go get google.golang.org/genai`

### Java

- Thư viện: `google-genai`
- Kho lưu trữ GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Cài đặt: Nếu bạn đang sử dụng Maven, hãy thêm nội dung sau vào các phần phụ thuộc:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Thư viện: `Google.GenAI`
- Kho lưu trữ GitHub: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Cài đặt: `dotnet add package Google.GenAI`

## Giai đoạn phát hành rộng rãi

Kể từ tháng 5 năm 2025, Google GenAI SDK đã đạt đến trạng thái Phát hành công khai (GA) trên tất cả các nền tảng được hỗ trợ và là các thư viện được đề xuất để truy cập vào Gemini API.
Các API này ổn định, được hỗ trợ đầy đủ cho việc sử dụng trong quá trình phát hành công khai và được duy trì liên tục.
Các mô hình này cung cấp quyền truy cập vào các tính năng mới nhất và mang lại hiệu suất tốt nhất khi hoạt động với Gemini.

Nếu đang dùng một trong các thư viện cũ của chúng tôi, bạn nên di chuyển để có thể sử dụng các tính năng mới nhất và đạt được hiệu suất tốt nhất khi làm việc với Gemini. Hãy xem phần [thư viện cũ](https://ai.google.dev/gemini-api/docs/libraries?hl=vi#previous-sdks) để biết thêm thông tin.

## Thư viện cũ và quá trình di chuyển

Nếu đang sử dụng một trong các thư viện cũ của chúng tôi, bạn nên [di chuyển sang các thư viện mới](https://ai.google.dev/gemini-api/docs/migrate?hl=vi).

Các thư viện cũ không cung cấp quyền truy cập vào các tính năng gần đây (chẳng hạn như [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi) và [Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi)) và sẽ ngừng hoạt động kể từ ngày 30 tháng 11 năm 2025.

Trạng thái hỗ trợ của mỗi thư viện cũ sẽ khác nhau, được nêu chi tiết trong bảng sau:

| Ngôn ngữ | Thư viện cũ | Trạng thái hỗ trợ | Thư viện đề xuất |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Không được duy trì thường xuyên | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Không được duy trì thường xuyên | `@google/genai` |
| **Bắt đầu** | `google.golang.org/generative-ai` | Không được duy trì thường xuyên | `google.golang.org/genai` |
| **Dart và Flutter** | `google_generative_ai` | Không được duy trì thường xuyên | Sử dụng [Genkit Dart](https://genkit.dev/docs/dart/get-started/) hoặc [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | Không được duy trì thường xuyên | Sử dụng [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=vi) |
| **Android** | `generative-ai-android` | Không được duy trì thường xuyên | Sử dụng [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=vi) |

**Lưu ý dành cho nhà phát triển Java:** Không có SDK Java cũ do Google cung cấp cho Gemini API, nên bạn không cần di chuyển từ một thư viện trước đây của Google. Bạn có thể bắt đầu ngay với thư viện mới trong phần [Hỗ trợ ngôn ngữ và cài đặt](#install).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-28 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-28 UTC."],[],[]]
