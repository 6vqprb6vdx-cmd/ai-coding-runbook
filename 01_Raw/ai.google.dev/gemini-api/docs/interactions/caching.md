---
source_url: https://ai.google.dev/gemini-api/docs/interactions/caching?hl=vi
fetched_at: 2026-05-18T13:06:54.789886+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Lưu ngữ cảnh vào bộ nhớ đệm

Trong quy trình làm việc điển hình của AI, bạn có thể truyền đi truyền lại cùng một mã thông báo đầu vào cho một mô hình. Gemini API cung cấp tính năng lưu vào bộ nhớ đệm ngầm để tối ưu hoá hiệu suất và chi phí.

## Lưu vào bộ nhớ đệm ngầm

Tính năng lưu vào bộ nhớ đệm ngầm định được bật theo mặc định cho tất cả các mô hình Gemini 2.5 trở lên. Chúng tôi tự động chuyển các khoản tiết kiệm chi phí nếu yêu cầu của bạn truy cập vào bộ nhớ đệm. Bạn không cần làm gì để bật tính năng này. Số lượng mã thông báo đầu vào tối thiểu để lưu vào bộ nhớ đệm ngữ cảnh được liệt kê trong bảng sau cho từng mô hình:

| Mô hình | Giới hạn mã thông báo tối thiểu |
| --- | --- |
| Bản xem trước Gemini 3 Flash | 1024 |
| Bản dùng thử Gemini 3 Pro | 4096 |
| Gemini 2.5 Flash | 1024 |
| Gemini 2.5 Pro | 4096 |

Để tăng cơ hội đạt được kết quả tìm kiếm trong bộ nhớ cache ngầm ẩn:

- Hãy thử đặt nội dung lớn và phổ biến ở đầu câu lệnh
- Hãy thử gửi các yêu cầu có tiền tố tương tự trong một khoảng thời gian ngắn

Bạn có thể xem số lượng mã thông báo là lượt truy cập vào bộ nhớ đệm trong trường `usage_metadata` (Python) hoặc `usageMetadata` (JavaScript) của đối tượng phản hồi.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-07 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-07 UTC."],[],[]]
