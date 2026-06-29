---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=vi
fetched_at: 2026-06-29T05:31:22.579540+00:00
title: "Kh\u1eafc ph\u1ee5c s\u1ef1 c\u1ed1 li\u00ean quan \u0111\u1ebfn Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Khắc phục sự cố liên quan đến Google AI Studio

Trang này đưa ra các đề xuất khắc phục sự cố Google AI Studio nếu bạn gặp vấn đề.

## Tìm hiểu về lỗi 403 Access Restricted (Quyền truy cập bị hạn chế)

Nếu thấy lỗi 403 Access Restricted (Truy cập bị hạn chế), tức là bạn đang sử dụng Google AI Studio theo cách không tuân thủ [Điều khoản dịch vụ](https://ai.google.dev/terms?hl=vi). Một lý do thường gặp là bạn không ở trong một [khu vực được hỗ trợ](https://ai.google.dev/available_regions?hl=vi).

## Giải quyết các phản hồi Không có nội dung trên Google AI Studio

Thông báo warning **Không có nội dung** sẽ xuất hiện trên Google AI Studio nếu nội dung bị chặn vì bất kỳ lý do nào. Để xem thêm thông tin chi tiết, hãy di chuyển con trỏ lên **Không có nội dung** rồi nhấp vào warning **An toàn**.

Nếu câu trả lời bị chặn do [chế độ cài đặt an toàn](https://ai.google.dev/docs/safety_setting?hl=vi) và bạn đã cân nhắc [các rủi ro về an toàn](https://ai.google.dev/docs/safety_guidance?hl=vi) cho trường hợp sử dụng của mình, thì bạn có thể sửa đổi [chế độ cài đặt an toàn](https://ai.google.dev/docs/safety_setting?hl=vi#safety_settings_in_makersuite) để ảnh hưởng đến câu trả lời được trả về.

Nếu câu trả lời bị chặn nhưng không phải do chế độ cài đặt an toàn, thì có thể cụm từ tìm kiếm hoặc câu trả lời đó vi phạm [Điều khoản dịch vụ](https://ai.google.dev/terms?hl=vi) hoặc không được hỗ trợ.

## Kiểm tra mức sử dụng và giới hạn mã thông báo

Khi bạn mở một câu lệnh, nút **Xem trước văn bản** ở cuối màn hình sẽ cho biết số lượng mã thông báo hiện tại được dùng cho nội dung của câu lệnh và số lượng mã thông báo tối đa cho mô hình đang được dùng.

## Quyền Cloud IAM của Google Cloud đối với AI Studio

Các thành viên của một dự án trên đám mây của Google cần có các quyền Quản lý danh tính và quyền truy cập (IAM) cụ thể để thực hiện các thao tác trong Google AI Studio. Để biết thêm thông tin về các danh tính này, hãy xem bài viết [Tổng quan về các thực thể IAM](https://cloud.google.com/iam/docs/principals?hl=vi).

Người dùng có vai trò **Người chỉnh sửa** hoặc **Chủ sở hữu** trong dự án trên đám mây Google được liên kết có đầy đủ quyền xem trang tổng quan và quản lý khoá Gemini API. Người dùng có vai trò **Người xem** có thể xem trang tổng quan và khoá API, nhưng không thể tạo, cập nhật hoặc xoá các mục này.

Để có quyền kiểm soát chi tiết hơn, hãy tham khảo bảng sau để biết các quyền cụ thể cần thiết cho từng tính năng của AI Studio. Để biết hướng dẫn về cách cấp các quyền này, hãy xem bài viết [Cấp, thay đổi và thu hồi quyền truy cập vào tài nguyên](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=vi) trong tài liệu của Google Cloud.

| Tính năng AI Studio | Các quyền IAM bắt buộc | Yêu cầu khác |
| --- | --- | --- |
| **Tìm dự án** (nhập dự án) | `resourcemanager.projects.get` |  |
| **Đổi tên dự án** | `resourcemanager.projects.update` |  |
| **Hiển thị cấp hạn mức** | Không áp dụng |  |
| **Tạo khoá API** | Có quyền **Tìm kiếm dự án** và:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **Liệt kê khoá API** | Có quyền **Tìm kiếm dự án** và:  `apikeys.keys.list` `serviceusage.services.get` | Dự án trên đám mây của Google Cloud phải bật [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=vi). |
| **Đổi tên khoá API** | `apikeys.keys.update` |  |
| **Xoá khoá API** | `apikeys.keys.delete` |  |
| **Trang tổng quan về mức sử dụng** | Có quyền **Tìm kiếm dự án** và:  `monitoring.timeSeries.list` |  |
| **Trang tổng quan về hạn mức yêu cầu** | Có quyền truy cập vào **Trang tổng quan về việc sử dụng** và:  `cloudquotas.quotas.get` |  |
| **Mức chi tiêu (Giới hạn thanh toán)** | `billing.resourceCosts.get` (để xem mức chi tiêu) `billing.resourcebudgets.read` (để xem hạn mức) `billing.resourcebudgets.write` (để đặt hạn mức) |  |
| **Trang tổng quan về hoạt động thanh toán** | `billing.accounts.get` |  |

### Các bước kiểm tra quyền truy cập khác

Ngoài các quyền Cloud IAM của Google Cloud, AI Studio cũng thực hiện các quy trình kiểm tra bảo mật và tuân thủ. Bạn có thể gặp lỗi `PERMISSION_DENIED` hoặc lỗi hạn chế quyền truy cập trong giao diện AI Studio hoặc trong các phản hồi của API nếu không đáp ứng các yêu cầu sau:

- **Kiểm tra bảo mật:** Yêu cầu của bạn phải vượt qua quy trình kiểm tra bảo mật tự động.
- **Điều khoản dịch vụ:** Bạn phải chấp nhận Điều khoản dịch vụ của Google và Điều khoản dịch vụ bổ sung của AI tạo sinh.
- **Khu vực được hỗ trợ:** Bạn phải ở một [khu vực được hỗ trợ](https://ai.google.dev/gemini-api/docs/available-regions?hl=vi).
- **Độ tin cậy và an toàn:** Dự án trên đám mây của Google Cloud không được bị gắn cờ là có hành vi sai trái.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-29 UTC."],[],[]]
