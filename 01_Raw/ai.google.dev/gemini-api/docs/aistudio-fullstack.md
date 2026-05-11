---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=vi
fetched_at: 2026-05-11T12:31:31.384174+00:00
title: "Ph\u00e1t tri\u1ec3n \u1ee9ng d\u1ee5ng Full-Stack trong Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Phát triển ứng dụng Full-Stack trong Google AI Studio

Google AI Studio hiện hỗ trợ phát triển toàn ngăn xếp, cho phép bạn tạo các ứng dụng vượt xa nguyên mẫu phía máy khách. Với thời gian chạy phía máy chủ, bạn có thể quản lý bí mật, kết nối với các API bên ngoài và tạo trải nghiệm nhiều người chơi theo thời gian thực.

## Thời gian chạy phía máy chủ

Giờ đây, các ứng dụng Google AI Studio có thể bao gồm một thành phần phía máy chủ (Node.js).
Điều này cho phép bạn:

- **Thực thi logic phía máy chủ**: Chạy mã không được hiển thị cho máy
  khách.
- **Truy cập vào các gói npm**: [Tác nhân Antigravity](https://antigravity.google/docs/agent?hl=vi)
  có thể cài đặt và sử dụng các gói từ hệ sinh thái npm rộng lớn.
- **Xử lý bí mật**: Sử dụng khoá API và thông tin đăng nhập một cách an toàn.

### Sử dụng các gói npm

Bạn không cần chạy `npm install` theo cách thủ công. Chỉ cần yêu cầu Tác nhân thêm chức năng yêu cầu một gói, và tác nhân này sẽ xử lý quá trình cài đặt và nhập.

**Ví dụ**: > "Sử dụng `axios` để tìm nạp dữ liệu từ API bên ngoài."

## Quản lý bí mật một cách an toàn

Với mã phía máy chủ và tính năng quản lý bí mật, giờ đây, bạn có thể tạo các ứng dụng tương tác với thế giới.

- **API của bên thứ ba**: Kết nối với các dịch vụ như Stripe, SendGrid hoặc các API REST tuỳ chỉnh.
- **Cơ sở dữ liệu**: Kết nối với các cơ sở dữ liệu bên ngoài (ví dụ: thông qua Supabase, Firebase,
  hoặc MongoDB Atlas) để lưu giữ dữ liệu ngoài phiên.

Khi tạo các ứng dụng trong thế giới thực, bạn thường cần kết nối với các dịch vụ bên thứ ba (như Twilio, Slack hoặc cơ sở dữ liệu) yêu cầu khoá API. Bạn có thể thêm khoá theo cách thủ công bằng các bước sau:

1. **Thêm bí mật**: Chuyển đến trình đơn **Cài đặt** trong Google AI Studio và tìm
   phần Bí mật.
2. **Lưu trữ khoá**: Thêm khoá API hoặc mã thông báo bí mật của bạn vào đây.
3. **Truy cập vào mã**: Tác nhân có thể viết mã phía máy chủ để truy cập vào các
   bí mật này một cách an toàn (thường là thông qua các biến môi trường), đảm bảo rằng các bí mật này không bao giờ được hiển thị cho trình duyệt phía máy khách.

Khi cần, tác nhân cũng sẽ hiển thị một thẻ trong cuộc trò chuyện nhắc bạn thêm khoá bất cứ khi nào cần một bí mật mới hoặc khi một khoá mới được phát hiện trong các biến môi trường của dự án.

### Tích hợp Firebase cho cơ sở dữ liệu và xác thực

[Giờ đây, Google AI Studio giúp bạn dễ dàng thêm cơ sở dữ liệu hoặc xác thực vào ứng dụng thông qua quá trình tích hợp Firebase.](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=vi)
Tác nhân Antigravity có thể tự động cung cấp và thiết lập các dịch vụ sau cho bạn:

- **Cơ sở dữ liệu Firestore**: một cơ sở dữ liệu đám mây NoSQL linh hoạt, có thể mở rộng để lưu trữ
  và đồng bộ hoá dữ liệu cho quá trình phát triển phía máy khách và máy chủ.
- **Xác thực Firebase**: cho phép người dùng đăng nhập vào
  ứng dụng của bạn một cách an toàn bằng quy trình "Đăng nhập bằng Google".

Chỉ cần yêu cầu tác nhân "thêm cơ sở dữ liệu vào ứng dụng của tôi" hoặc "thiết lập tính năng Đăng nhập bằng Google", và tác nhân này sẽ xử lý cấu hình cần thiết và tạo mã cho bạn.

Firebase cho phép bạn bắt đầu miễn phí và tuỳ ý mở rộng bằng tài khoản trả phí bất cứ khi nào bạn sẵn sàng sử dụng thêm hạn mức hoặc các tính năng trả phí.

### Thiết lập OAuth

Một trường hợp sử dụng chính để quản lý bí mật là thiết lập OAuth để kết nối với các trang web hoặc ứng dụng khác. Khi lời nhắc của bạn bao gồm hướng dẫn về cách kết nối với một ứng dụng bên thứ ba yêu cầu xác thực OAuth, tác nhân sẽ cung cấp hướng dẫn về cách thiết lập OAuth cho ứng dụng đó. Các hướng dẫn này sẽ bao gồm các URL gọi lại cần thiết để định cấu hình Ứng dụng OAuth.
Bạn cũng có thể tìm thấy các URL gọi lại trong phần **Tích hợp** trên bảng điều khiển Cài đặt.

## Tạo trải nghiệm nhiều người chơi

Thời gian chạy toàn ngăn xếp cho phép các tính năng cộng tác theo thời gian thực.

- **Trạng thái theo thời gian thực**: Bạn có thể yêu cầu Tác nhân tạo các tính năng như "trò chuyện trực tiếp
  ," "bảng trắng cộng tác" hoặc "trò chơi nhiều người chơi."
- **Phiên được đồng bộ hoá**: Máy chủ quản lý trạng thái, cho phép nhiều người dùng
  tương tác với cùng một thực thể ứng dụng theo thời gian thực.

**Ví dụ về lời nhắc**: > "Tạo trò chơi nhiều người chơi, trong đó người chơi có thể nhìn thấy con trỏ của nhau."

### Mẹo kiểm thử ứng dụng nhiều người chơi

Bạn có thể kiểm thử chế độ nhiều người chơi theo 2 cách trước khi triển khai ứng dụng.

1. Mở ứng dụng của bạn ở chế độ Tạo trong Google AI Studio trên nhiều thẻ. Khi phát triển ở chế độ Tạo, ứng dụng của bạn sẽ nằm trong một vùng chứa dành cho nhà phát triển. Việc mở ứng dụng trên nhiều thẻ sẽ cho phép bạn mô phỏng nhiều người chơi sử dụng ứng dụng của mình.
2. Chia sẻ ứng dụng với người khác bằng trình đơn **Chia sẻ** ở trên cùng bên phải. sau đó sử dụng **URL được chia sẻ** trong thẻ **Tích hợp** của trình đơn **Chia sẻ** để sử dụng ứng dụng với những người chơi mà bạn đã chia sẻ ứng dụng.

## Các phương pháp hay nhất

- **Bảo mật bí mật**: Luôn sử dụng Trình quản lý bí mật cho các khoá nhạy cảm.
  Không bao giờ mã hoá cứng các khoá này trong tệp của bạn.
- **Phân tách mối quan tâm**: Giữ logic giao diện người dùng trong khung phía máy khách
  (React/Angular) và logic nghiệp vụ/xử lý dữ liệu ở phía máy chủ.
- **Xử lý lỗi**: Đảm bảo mã phía máy chủ của bạn xử lý lỗi một cách mạnh mẽ
  từ các lệnh gọi API bên ngoài để ngăn ứng dụng gặp sự cố.

## Tiếp theo là gì?

- [Tạo ứng dụng trong Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=vi)
- [Thư viện ứng dụng](https://aistudio.google.com/apps?source=showcase&hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
