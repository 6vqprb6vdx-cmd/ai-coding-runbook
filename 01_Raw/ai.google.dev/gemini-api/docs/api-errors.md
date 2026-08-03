---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=vi
fetched_at: 2026-08-03T04:34:38.109323+00:00
title: "L\u1ed7i API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Lỗi API

Trang này cung cấp thông tin tham khảo về tất cả mã lỗi của Interactions API, mô tả định dạng phản hồi lỗi và giải thích cách API gửi lỗi cho các loại yêu cầu khác nhau.

## Mã lỗi API tiêu chuẩn

Các mã lỗi chung ở cấp yêu cầu này tương ứng với mã trạng thái HTTP tiêu chuẩn.
Sử dụng trường `code` trong logic ứng dụng để xử lý lỗi theo phương thức lập trình.

| Mã | Trạng thái HTTP | Mô tả | Hành động được đề xuất |
| --- | --- | --- | --- |
| `invalid_request` | 400 Yêu cầu không hợp lệ | Yêu cầu sai định dạng hoặc chứa các tham số không hợp lệ. | Kiểm tra dữ liệu đầu vào dựa trên [tài liệu tham khảo API](https://ai.google.dev/api/interactions-api?hl=vi). |
| `parameter_unknown` | 400 Yêu cầu không hợp lệ | Yêu cầu chứa một tham số không xác định. | Xoá tham số không nhận dạng được rồi thử lại. |
| `authentication` | 401 Không được phép | Khoá API bị thiếu hoặc không hợp lệ. | Xác minh [khoá API](https://ai.google.dev/gemini-api/docs/api-key?hl=vi). |
| `permission_denied` | 403 Bị cấm | Khoá API của bạn không có quyền truy cập vào tài nguyên này. | Kiểm tra quyền khoá API và quyền truy cập vào dự án. |
| `not_found` | 404 Không tìm thấy | Không tìm thấy tài nguyên được yêu cầu. | Xác minh đường dẫn tài nguyên và các tham số. |
| `model_not_found` | 404 Không tìm thấy | Không tìm thấy mô hình được chỉ định. | Xác minh tên mô hình hoặc chuyển sang một mô hình khác. |
| `rate_limit_exceeded` | 429 Quá nhiều yêu cầu | Bạn đã vượt quá giới hạn yêu cầu hoặc mã thông báo mỗi phút hoặc mỗi giây. | Hãy đợi rồi thử lại với thời gian đợi luỹ thừa. |
| `quota_exceeded` | 429 Quá nhiều yêu cầu | Bạn đã vượt quá hạn mức hằng ngày. | Đợi đến khi hạn mức được đặt lại hoặc yêu cầu tăng hạn mức. |
| `cancelled` | 499 Ứng dụng đã đóng yêu cầu | Ứng dụng khách đã huỷ yêu cầu trước khi yêu cầu hoàn tất. | Bạn không cần làm gì cả. Điều này thường có nghĩa là ứng dụng đã ngắt kết nối. |
| `api_error` | 500 Lỗi máy chủ nội bộ | Đã xảy ra lỗi không mong muốn trên máy chủ. | Thử gửi lại yêu cầu. Nếu vấn đề vẫn tiếp diễn, hãy liên hệ với nhóm hỗ trợ. |
| `service_unavailable` | 503 Không có dịch vụ | Dịch vụ tạm thời bị quá tải hoặc không hoạt động. | Hãy đợi rồi thử lại với thời gian đợi luỹ thừa. |

## Mã bị chặn tạo

Các mã lỗi này cho biết rằng các hạn chế về chính sách, an toàn hoặc nội dung đã chặn đầu ra của mô hình. Khi bạn nhận được một trong những mã này, hãy sửa đổi nội dung nhập rồi thử lại.

| Mã | Mô tả |
| --- | --- |
| `safety` | Lỗi vi phạm về an toàn (nội dung gây hại) đã chặn yêu cầu. |
| `recitation` | Yêu cầu bị chặn do quy định hạn chế về bản quyền hoặc việc trích dẫn. |
| `language` | Ngôn ngữ không được hỗ trợ đã chặn yêu cầu. |
| `prohibited_content` | Nguyên tắc đối với nội dung bị cấm đã chặn yêu cầu này. |
| `spii` | Các quy định hạn chế về Thông tin nhạy cảm có thể nhận dạng cá nhân đã chặn yêu cầu. |
| `blocklist` | Các cụm từ bị cấm trong danh sách chặn đã chặn yêu cầu. |
| `image_safety` | Lỗi vi phạm về an toàn đã chặn quá trình tạo hình ảnh. |
| `image_prohibited_content` | Nguyên tắc đối với nội dung bị cấm đã chặn việc tạo hình ảnh. |
| `image_recitation` | Quy định hạn chế về bản quyền hoặc việc trích dẫn đã chặn quá trình tạo hình ảnh. |
| `image_other` | Quá trình tạo hình ảnh bị chặn vì những lý do không xác định. |
| `content_blocked` | Một lý do không xác định về chính sách đã chặn yêu cầu. |

## Mã lỗi tạo

Các mã lỗi này cho biết có vấn đề về cấu trúc với đầu ra do mô hình tạo (chẳng hạn như lệnh gọi hàm bị lỗi hoặc lệnh gọi công cụ chưa khai báo).

| Mã | Mô tả |
| --- | --- |
| `malformed_function_call` | Mô hình đã tạo ra một lệnh gọi hàm không phân tích cú pháp được. |
| `malformed_tool_call` | Mô hình đã tạo một lệnh gọi công cụ không thể phân tích cú pháp. |
| `unexpected_tool_call` | Mô hình đã gọi một công cụ không được khai báo trong yêu cầu. |
| `no_image` | Mô hình không tạo được hình ảnh. |
| `too_many_tool_calls` | Mô hình đã tạo ra nhiều lệnh gọi công cụ hơn mức cho phép. |
| `missing_thought_signature` | Phản hồi thiếu chữ ký bắt buộc. |

## Định dạng phản hồi lỗi

Tất cả lỗi từ Interactions API đều trả về một đối tượng `error` chứa `code` và `message`. Ví dụ: việc truyền một loại công cụ không được hỗ trợ sẽ trả về:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Trường | Loại | Mô tả |
| --- | --- | --- |
| `code` | chuỗi | Mã lỗi mà máy có thể đọc được trong `snake_case`. |
| `message` | chuỗi | Nội dung mô tả mà con người đọc được về vấn đề đã xảy ra. |

## Cách gửi lỗi

API gửi lỗi theo cách khác nhau tuỳ thuộc vào việc bạn đưa ra yêu cầu HTTP tiêu chuẩn hay yêu cầu truyền trực tuyến (SSE).

### Yêu cầu HTTP tiêu chuẩn

Đối với các yêu cầu tiêu chuẩn (không truyền trực tuyến), API sẽ đặt mã trạng thái phản hồi HTTP (chẳng hạn như `400 Bad Request`, `401 Unauthorized` hoặc `429 Too Many Requests`) và trả về một đối tượng `error` trong phần nội dung phản hồi JSON:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Yêu cầu truyền trực tuyến (SSE)

Đối với các yêu cầu phát trực tuyến (`stream: true`), API sẽ gửi các sự kiện lỗi qua luồng Sự kiện do máy chủ gửi (SSE) với `event_type` được đặt thành `"error"`. Trường `error` chứa cấu trúc `code` và `message` tương tự:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Để biết giản đồ sự kiện SSE đầy đủ, hãy xem [Tài liệu tham khảo về Interactions API](https://ai.google.dev/api/interactions-api?hl=vi).

## Bước tiếp theo

- [Khắc phục sự cố về API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=vi): Giải quyết các vấn đề thường gặp và các trường hợp lỗi.
- [Hạn mức về tốc độ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi): Tìm hiểu về hạn mức yêu cầu và cách xử lý hạn mức.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-30 UTC."],[],[]]
