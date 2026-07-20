---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=vi
fetched_at: 2026-07-20T04:37:30.205304+00:00
title: "Tri\u1ec3n khai t\u1eeb Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Triển khai từ Google AI Studio

Google AI Studio cho phép bạn triển khai các ứng dụng full-stack ngay trong Chế độ tạo. Nhờ đó, bạn có thể nhanh chóng chuyển từ nguyên mẫu sang môi trường sản xuất có thể mở rộng và được quản lý.

## Các lựa chọn triển khai

Để triển khai ứng dụng trong Chế độ tạo của AI Studio, các yêu cầu sẽ phụ thuộc vào gói bạn sử dụng:

- [**Gói Starter của Google Cloud**](https://docs.cloud.google.com/docs/starter-tier?hl=vi):
  Cho phép bạn xuất bản tối đa 2 ứng dụng full-stack mà không cần thiết lập
  dự án Google Cloud hoặc tài khoản thanh toán.
- **Triển khai tiêu chuẩn**: Yêu cầu một dự án Google Cloud được liên kết với tài khoản
  AI Studio của bạn và tính năng thanh toán được bật trên dự án đó.

## Giới thiệu về Gói Starter

Gói Starter của Google Cloud cung cấp một quy trình hợp lý để triển khai ứng dụng lên Google Cloud ngay trong Google AI Studio mà không cần thiết lập môi trường Google Cloud đầy đủ hoặc tài khoản thanh toán.

Mỗi lượt triển khai trong Google AI Studio sẽ tạo một dịch vụ tương ứng trong Cloud Run. Đối với các dịch vụ được triển khai trong Google AI Studio bằng Gói Starter, các giới hạn sau đây sẽ áp dụng:

- Bạn có thể triển khai tối đa hai dịch vụ.
- Các dịch vụ của bạn được triển khai trong một
  [khu vực Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=vi).

## Các bước triển khai Gói Starter

Sau khi thiết kế ứng dụng ở Chế độ tạo, hãy triển khai ứng dụng đó bằng Gói Starter:

1. Nhấp vào nút **Xuất bản** ở góc trên cùng bên phải.
2. Hãy nhấp vào **Bắt đầu**.
3. Nhấp vào **Xuất bản ứng dụng**.

Sau khi quá trình triển khai hoàn tất, AI Studio sẽ cung cấp một URL Cloud Run để bạn có thể truy cập vào ứng dụng đang hoạt động của mình.

## URL tuỳ chỉnh cho AI Studio

Khi xuất bản ứng dụng trong Google AI Studio, bạn có thể đặt một miền phụ tuỳ chỉnh,
dễ nhớ trong `ai.studio` (ví dụ:
`https://your-app-name.ai.studio`).

Google AI Studio yêu cầu các miền phụ phải là duy nhất trên toàn cầu trong tất cả các dự án và chỉ định các miền phụ đó theo nguyên tắc ai đến trước được phục vụ trước. Nếu một dự án khác đã sử dụng tên, AI Studio sẽ nhắc bạn chọn một tên khác. Nếu bạn huỷ xuất bản hoặc xoá một ứng dụng, URL tuỳ chỉnh của ứng dụng đó sẽ được phát hành và người dùng khác có thể nhận URL đó.

### Đặt URL tuỳ chỉnh

Cách đặt hoặc cập nhật URL tuỳ chỉnh cho ứng dụng:

1. Mở ứng dụng trong Google AI Studio ở chế độ **Tạo**.
2. Nhấp vào **Xuất bản** ở góc trên cùng bên phải.
3. Trong cấu hình triển khai, hãy nhập miền phụ bạn muốn vào trường **URL tuỳ chỉnh** hoặc chấp nhận URL được đề xuất.
4. Nhấp vào **Xuất bản ứng dụng**.

Để chuyển một URL tuỳ chỉnh hiện có sang một ứng dụng khác, trước tiên, bạn phải huỷ xuất bản hoặc xoá ứng dụng được chỉ định URL tuỳ chỉnh đó, sau đó xuất bản ứng dụng mới bằng miền phụ đã chọn.

### Báo cáo vấn đề về nhãn hiệu hoặc bản quyền

Các miền phụ tuỳ chỉnh phải tuân thủ
[Điều khoản dịch vụ của Google](https://policies.google.com/terms?hl=vi). Nếu nhận thấy một
URL tuỳ chỉnh vi phạm nhãn hiệu hoặc sử dụng tên có bản quyền mà không được
phép, bạn có thể báo cáo URL đó bằng
[Trình khắc phục sự cố pháp lý của Google](https://support.google.com/legal/troubleshooter/1114905?hl=vi).

## Triển khai tiêu chuẩn

Khi các ứng dụng của bạn phát triển, bạn có thể cần các tính năng ngoài Gói Starter, chẳng hạn như hạn mức cao hơn hoặc tăng tài nguyên tính toán hoặc các sản phẩm khác của Google Cloud không có trong Gói Starter. Để khai thác các tính năng này, bạn có thể chuyển đổi dự án Gói Starter được quản lý hoàn toàn thành dự án Google Cloud tiêu chuẩn.

Điều này đảm bảo rằng bạn có thể mở rộng quy mô một cách liền mạch mà không làm mất tiến trình. Hãy làm theo các bước để
[tạo tài khoản Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=vi#create-new-billing-account),
chính thức chấp nhận Điều khoản dịch vụ tiêu chuẩn của Google Cloud và
[nâng cấp lên dự án Google Cloud tiêu chuẩn](https://docs.cloud.google.com/docs/starter-tier?hl=vi#upgradee).
Để biết thêm thông tin, hãy xem bài viết
[Thiết lập tài khoản trả phí](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=vi#paid-setup).

Để tìm hiểu thêm về các gói thanh toán, hãy xem bài viết [Thanh toán](https://ai.google.dev/gemini-api/docs/billing?hl=vi).

## Xoá ứng dụng

Nếu không còn cần ứng dụng nữa, bạn có thể xoá ứng dụng đó trong Google AI Studio bằng cách làm theo các hướng dẫn sau:

1. Trong Google AI Studio, hãy chuyển đến trang
   [Ứng dụng](https://aistudio.google.com/app/apps?hl=vi).
2. Ở trình đơn bên trái, hãy chọn **Ứng dụng**.
3. Di chuyển con trỏ qua ứng dụng bạn muốn xoá.
4. Nhấp vào biểu tượng thùng rác ở bên phải của hàng để xoá ứng dụng.

## Bước tiếp theo

- Tìm hiểu thêm về
  [Gói Starter của Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=vi).
- Đọc bài viết về [Thanh toán](https://ai.google.dev/gemini-api/docs/billing?hl=vi) trong Gemini API.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-10 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-10 UTC."],[],[]]
