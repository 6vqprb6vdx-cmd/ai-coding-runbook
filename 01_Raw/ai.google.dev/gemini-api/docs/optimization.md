---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=vi
fetched_at: 2026-07-20T04:39:40.770251+00:00
title: "T\u1ed1i \u01b0u ho\u00e1 v\u00e0 suy lu\u1eadn Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tối ưu hoá và suy luận Gemini API

Gemini API cung cấp nhiều cơ chế tối ưu hoá để giúp bạn cân bằng tốc độ, chi phí và độ tin cậy dựa trên nhu cầu cụ thể về khối lượng công việc.
Cho dù bạn đang xây dựng bot trò chuyện theo thời gian thực hay chạy các pipeline xử lý dữ liệu ngoại tuyến nặng, việc chọn đúng mô hình có thể giúp bạn giảm đáng kể chi phí hoặc tăng hiệu suất.

| Tính năng | Tiêu chuẩn | Linh hoạt | Mức độ ưu tiên | Theo nhóm | Lưu vào bộ nhớ đệm |
| --- | --- | --- | --- | --- | --- |
| **Định giá** | Giá đầy đủ | Chiết khấu 50% | Cao hơn từ 75% đến 100% so với mức tiêu chuẩn | Chiết khấu 50% | Chiết khấu 90% + Dung lượng lưu trữ mã thông báo theo tỷ lệ |
| **Độ trễ** | Từ vài giây đến vài phút | Phút (mục tiêu từ 1 đến 15 phút) | Giây | Tối đa 24 giờ | Thời gian hiển thị mã thông báo đầu tiên nhanh hơn |
| **Độ tin cậy** | Cao / Trung bình cao | Trong khả năng tốt nhất có thể (Có thể loại bỏ) | Cao (Không thể loại bỏ) | Cao (đối với thông lượng) | Không áp dụng |
| **Giao diện** | Đồng bộ | Đồng bộ | Đồng bộ | Không đồng bộ | Trạng thái đã lưu |
| **Trường hợp sử dụng phù hợp nhất** | Quy trình công việc chung của ứng dụng | Các chuỗi tuần tự không khẩn cấp | Ứng dụng sản xuất, ứng dụng dành cho người dùng | Tập dữ liệu lớn, đánh giá ngoại tuyến | Các truy vấn lặp lại trên cùng một tệp |

## Cấp dịch vụ suy luận (Đồng bộ)

Bạn có thể chuyển đổi giữa lưu lượng truy cập đồng bộ được tối ưu hoá về độ tin cậy và lưu lượng truy cập đồng bộ được tối ưu hoá về chi phí bằng cách truyền tham số `service_tier` trong các lệnh gọi tạo tiêu chuẩn.

### Suy luận tiêu chuẩn (Mặc định)

Cấp tiêu chuẩn là lựa chọn mặc định để tạo nội dung tuần tự.
Cấp này cung cấp thời gian phản hồi bình thường mà không có phí bảo hiểm bổ sung hoặc hàng đợi lớn.

- **Độ tin cậy:** Mức độ quan trọng tiêu chuẩn
- **Giá:** Giá tiêu chuẩn.
- **Phù hợp nhất với:** Hầu hết các ứng dụng tương tác hằng ngày.

### Suy luận ưu tiên (Tối ưu hoá độ trễ)

[Quy trình xử lý](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi)ưu tiên sẽ chuyển các yêu cầu của bạn
đến hàng đợi điện toán có mức độ quan trọng cao.
Lưu lượng truy cập này hoàn toàn không thể loại bỏ (không bao giờ bị các cấp khác ưu tiên) và mang lại độ tin cậy cao nhất. Nếu bạn vượt quá giới hạn Ưu tiên động, hệ thống sẽ tự động hạ cấp yêu cầu xuống quy trình xử lý Tiêu chuẩn thay vì báo lỗi.

- **Độ tin cậy:** Mức độ quan trọng cao nhất
- **Giá:** Cao hơn từ 75% đến 100% so với mức Tiêu chuẩn.
- **Phù hợp nhất với:** Chatbot dành cho khách hàng, tính năng phát hiện gian lận theo thời gian thực và trợ lý ảo quan trọng đối với doanh nghiệp.

### Suy luận linh hoạt (Tối ưu hoá chi phí)

[Suy luận linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi) giúp bạn tiết kiệm 50% so với mức giá tiêu chuẩn bằng cách tận dụng
công suất điện toán không cao điểm. Các yêu cầu được xử lý đồng bộ, nghĩa là bạn không cần viết lại mã để quản lý các đối tượng theo nhóm.
Vì đây là lưu lượng truy cập "có thể loại bỏ", nên các yêu cầu có thể bị ưu tiên nếu hệ thống gặp phải tình trạng tăng đột biến lưu lượng truy cập tiêu chuẩn.

- **Độ tin cậy:** Không được đảm bảo, mức độ quan trọng có thể loại bỏ
- **Giá:** 50% giá Tiêu chuẩn (tính phí theo mã thông báo).
- **Phù hợp nhất với:** Quy trình công việc nhiều bước của tác nhân mà lệnh gọi N+1 phụ thuộc vào kết quả của lệnh gọi N, các bản cập nhật CRM ở chế độ nền và các đánh giá ngoại tuyến.

## API theo nhóm (Hàng loạt, không đồng bộ)

[API theo nhóm](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi) được thiết kế để xử lý không đồng bộ một lượng lớn
yêu cầu với
chi phí bằng 50% chi phí tiêu chuẩn. Bạn có thể gửi yêu cầu dưới dạng từ điển nội tuyến hoặc sử dụng tệp đầu vào JSONL (tối đa 2 GB). API này xử lý các yêu cầu bằng cách sử dụng hàng đợi thông lượng ở chế độ nền với thời gian hoàn thành mục tiêu là 24 giờ.

- **Độ tin cậy:** Có thể loại bỏ nhưng có hệ thống tự động thử lại và xếp hàng đợi trong 24 giờ
- **Giá:** 50% giá Tiêu chuẩn.
- **Phù hợp nhất với:** Xử lý trước các tập dữ liệu lớn, chạy các bộ kiểm thử hồi quy định kỳ và tạo hình ảnh hoặc nội dung nhúng với số lượng lớn.

## Lưu vào bộ nhớ đệm theo ngữ cảnh (Tiết kiệm dữ liệu đầu vào)

[Tính năng lưu vào bộ nhớ đệm theo ngữ cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi) được sử dụng khi một ngữ cảnh ban đầu đáng kể
được các yêu cầu ngắn hơn tham chiếu nhiều lần.

- **Lưu vào bộ nhớ đệm ngầm ẩn:** Tự động bật trên Gemini 2.5 và các mô hình mới hơn.
  Hệ thống sẽ chuyển khoản tiết kiệm chi phí nếu yêu cầu của bạn khớp với các bộ nhớ đệm hiện có dựa trên các tiền tố lời nhắc phổ biến.
- **Lưu vào bộ nhớ đệm rõ ràng:** Bạn có thể tạo đối tượng bộ nhớ đệm theo cách thủ công với một Thời gian tồn tại (TTL) cụ thể. Sau khi tạo, bạn có thể tham khảo các mã thông báo được lưu vào bộ nhớ đệm cho các yêu cầu tiếp theo để tránh việc truyền tải cùng một tải trọng văn bản nhiều lần.
- **Giá:** Tính phí dựa trên số lượng mã thông báo trong bộ nhớ đệm và thời gian lưu trữ (TTL).
- **Phù hợp nhất với:** Chatbot có hướng dẫn hệ thống mở rộng, phân tích lặp lại các tệp video dài hoặc truy vấn đối với các tập tài liệu lớn.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
