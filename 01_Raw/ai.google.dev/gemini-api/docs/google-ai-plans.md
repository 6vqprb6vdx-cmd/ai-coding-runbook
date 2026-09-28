---
source_url: https://ai.google.dev/gemini-api/docs/google-ai-plans?hl=vi
fetched_at: 2026-09-28T06:18:59.846944+00:00
title: "C\u00e1c g\u00f3i AI c\u1ee7a Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Các gói AI của Google

Sử dụng gói thuê bao AI của Google trong AI Studio.

Các gói thuê bao Google AI Pro và Ultra cung cấp quyền truy cập rộng hơn vào mô hình và tăng hạn mức tốc độ để tạo nguyên mẫu và phát triển trong AI Studio so với gói miễn phí.

Để đăng ký gói AI của Google, bạn có thể nâng cấp trực tiếp trong Google AI Studio bằng cách nhấp vào nút **Nâng cấp** trong trình đơn điều hướng bên trái. Ngoài ra, bạn có thể đăng ký bằng cách truy cập vào [trang Các gói Google AI](https://one.google.com/about/google-ai-plans/?hl=vi).

## Tổng quan

Các gói thuê bao Google AI Pro và Ultra giúp nhà phát triển khai thác các mô hình có tính phí và hạn mức cao hơn trong Google AI Studio Playground cũng như các tính năng như Trợ lý lập trình ở [Chế độ tạo](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=vi) để lập trình theo cảm hứng. Người đăng ký sẽ nhận được hạn mức cơ bản hằng ngày cao hơn so với hạn mức của gói miễn phí để sử dụng trên các giao diện [Playground](https://aistudio.google.com/prompts/new_chat?hl=vi) và [Build](https://aistudio.google.com/apps?hl=vi). Giới hạn hằng ngày được thực thi bằng cách sử dụng các lần đặt lại thay vì khoảng thời gian cố định, đảm bảo trải nghiệm phát triển suôn sẻ trước khi chuyển sang phát triển ở quy mô sản xuất bằng Cloud Billing.

| Lập kế hoạch | Mức sử dụng AI Studio | Quyền sử dụng mô hình và các lợi ích |
| --- | --- | --- |
| **Free** | Hạn mức vừa phải | Hạn mức và quyền truy cập cơ bản, có thể nâng cấp để có thêm hạn mức và quyền truy cập. |
| **AI Pro** | Hạn mức cao hơn | Quyền truy cập vào các mô hình cao cấp như Gemini Pro, Nano Banana và Lyria. |
| **AI Ultra** | Hạn mức cao nhất | Hạn mức cao nhất để tạo nguyên mẫu, phát triển và sử dụng các mô hình tiên tiến. |

## Sử dụng Gemini API

Khi hết hạn mức cơ bản hằng ngày của gói thuê bao trong AI Studio, bạn có thể tiếp tục quy trình làm việc bằng cách sử dụng khoá Gemini API có bật tính năng Thanh toán trên đám mây để sử dụng Gemini API trực tiếp theo mức trả phí cho mỗi yêu cầu.
Bạn có thể theo dõi mức sử dụng Gemini API cho các dự án và khoá API trong [Trang tổng quan của AI Studio](https://aistudio.google.com/projects?hl=vi).

Những người đăng ký có dự án trên Google Cloud Platform (GCP) và đã bật Cloud Billing đều đủ điều kiện nhận tín dụng Cloud hằng tháng từ [Google Developer Program](https://developers.google.com/program?hl=vi) cho các dịch vụ Cloud, bao gồm cả Gemini API. Việc sử dụng và thanh toán trả trước và trả sau vẫn không thay đổi. Đối với người dùng sử dụng phương thức thanh toán trả trước, bạn cần có số dư lớn hơn 0 USD trong AI Studio để kích hoạt tín dụng khuyến mãi. Khoản tín dụng Google Cloud đủ điều kiện (nếu có) sẽ được áp dụng trước.
[Tìm hiểu thêm](https://ai.google.dev/gemini-api/docs/billing?hl=vi#billing-plans).

Việc tích hợp gói thuê bao AI của Google giúp giảm bớt rào cản đối với hoạt động thử nghiệm và phát triển nâng cao. Tuy nhiên, đối với các hoạt động triển khai quy mô lớn trong môi trường sản xuất, dự án Google Cloud, [Google Cloud Starter Tier](https://cloud.google.com/blog/topics/developers-practitioners/the-starter-tier-for-google-ai-studio-explained?hl=vi) và khoá Gemini API là những lựa chọn được đề xuất.

## Hạn chế và khả năng tương thích

- **Chỉ có giao diện người dùng AI Studio:** Các lợi ích của gói AI của Google dành cho mục đích sử dụng của nhà phát triển chỉ áp dụng trong giao diện web của Google AI Studio. Việc sử dụng trực tiếp Gemini API (chẳng hạn như sử dụng khoá API hoặc các ứng dụng bên ngoài) sẽ được tính phí và quản lý riêng. Tuy nhiên, bạn có thể sử dụng gói thuê bao này trên các sản phẩm khác của Google (xem [Các gói AI của Google](https://one.google.com/about/google-ai-plans/?hl=vi)).
- **Khác với phí sử dụng API:** Các gói AI của Google dành cho AI Studio tách biệt với [các bậc sử dụng Gemini API](https://ai.google.dev/gemini-api/docs/billing?hl=vi). Các bậc này bao gồm việc sử dụng API trong quá trình phát triển và sản xuất.
- **Tín dụng Google One:** [Tín dụng AI của Google One](https://support.google.com/googleone/answer/16287445?hl=vi) là một hệ thống tín dụng riêng biệt không được hỗ trợ trong AI Studio và không trùng lặp với tín dụng Google Cloud.
- **Quyền truy cập vào các tác nhân:** Các gói Google AI không bao gồm quyền truy cập vào các tác nhân (Deep Research và Antigravity Preview) trong AI Studio và yêu cầu phải có [khoá API trả phí](https://ai.google.dev/gemini-api/docs/billing?hl=vi#setup-billing).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-08-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-08-19 UTC."],[],[]]
