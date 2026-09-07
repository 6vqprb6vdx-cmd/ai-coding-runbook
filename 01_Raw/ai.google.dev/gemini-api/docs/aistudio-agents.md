---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=vi
fetched_at: 2026-09-07T05:40:14.292487+00:00
title: "T\u00e1c nh\u00e2n trong AI Studio Playground \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tác nhân trong AI Studio Playground

Google AI Studio Playground cung cấp một giao diện trực quan để tạo nguyên mẫu và tìm hiểu cách xây dựng các tác nhân được quản lý mà không cần phải tạo và viết lệnh gọi API.

Để bắt đầu, hãy chuyển đến thẻ **Playground** (Sân chơi) trong bảng điều hướng của Google AI Studio, rồi chuyển nút bật/tắt sang **Agents** (Trợ lý AI).

## Mẫu tạo sẵn

Thẻ **Agents** (Tác nhân) có một loạt mẫu định cấu hình sẵn Antigravity Agent cơ bản bằng cách thiết lập cấu hình công cụ và môi trường. Tất cả các mẫu đều là nguồn mở và được xuất bản trong kho lưu trữ [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/). Khám phá những mẫu này là một cách tuyệt vời để tìm hiểu cách xây dựng và cấu trúc tác nhân được quản lý của riêng bạn.

Ví dụ: khi bạn chọn mẫu AI Radio, mẫu này sẽ bật tất cả các công cụ được phép và liên kết một tệp `AGENTS.md` chuyên dụng cùng các kỹ năng để sản xuất chương trình phát thanh. Bạn có thể xem các chế độ cài đặt này trên giao diện người dùng Sân chơi trong mục **Môi trường** bằng cách nhấp vào nút **Nguồn**.

## Cấu hình công cụ

Trong phần Cài đặt tác nhân của Sân chơi, bạn có thể bật/tắt quyền truy cập vào các công cụ tích hợp sau đây:

- **Google Tìm kiếm:** Truy cập vào web mở để có thông tin theo thời gian thực.
- **Ngữ cảnh URL:** Tìm nạp và phân tích nội dung văn bản của các URL trang web cụ thể.
- **Thực thi mã:** Chạy các lệnh Bash và Python ngay trong môi trường hộp cát biệt lập.
- **Công cụ hệ thống tệp:** Đọc, ghi, liệt kê và xoá các tệp trong không gian làm việc.

## Cấu hình môi trường

Các tác nhân được quản lý chạy trong một hộp cát Linux tạm thời, bảo mật (môi trường) cung cấp không gian làm việc và các công cụ cần thiết để hoạt động. Để tìm hiểu thêm, hãy xem hướng dẫn về [môi trường tác nhân được quản lý](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi).

### Kiểm soát hành vi của tác nhân

Hành vi, tính cách và khả năng của tác nhân chủ yếu được xác định bởi các tệp có trong môi trường của tác nhân. Tác nhân này tự động phát hiện và tải các cấu hình từ một thư mục `.agents` đặc biệt:

- **`AGENTS.md`**: Được tải sẵn vào ngữ cảnh của tác nhân để xác định hướng dẫn và tính cách của hệ thống.
- **`SKILL.md`**: Nằm trong các thư mục kỹ năng tương ứng (ví dụ: `.agents/skills/my-skill/SKILL.md`) để xác định các chức năng và quy trình cụ thể.

### Cung cấp môi trường

Bạn có thể định cấu hình môi trường mà tác nhân sẽ sử dụng bằng cách gắn các tệp vào môi trường trước khi bắt đầu một phiên. Bạn có thể tạo một môi trường mới bằng cách gắn các nguồn hoặc khôi phục một môi trường trước đó:

- **Để tạo một môi trường mới**, hãy nhấp vào **Thêm nguồn** trong bảng điều khiển Cài đặt môi trường rồi chọn một trong các loại nguồn sau:

| Loại nguồn | Mô tả | Đường dẫn gắn kết |
| --- | --- | --- |
| **Tệp nội tuyến** | Viết hoặc dán tệp cấu hình, tập dữ liệu mô phỏng hoặc tập lệnh tiện ích (tối đa 100 KB) trực tiếp vào giao diện người dùng Playground. | Đường dẫn đích do người dùng xác định (ví dụ: `/workspace/scripts/parser.py`). |
| **Google Cloud Storage** | Gắn một bộ chứa Cloud Storage công khai hoặc riêng tư.  Bộ chứa riêng tư yêu cầu mã thông báo Bearer OAuth 2.0 tiêu chuẩn. Để biết thêm thông tin, hãy xem phần [Nguồn riêng tư](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#private-sources). | Liên kết một đường dẫn bộ chứa GCS (ví dụ: `gs://your-bucket-name/data/`) với một thư mục không gian làm việc (ví dụ: `/workspace/data/`). |
| **Kho lưu trữ GitHub** | Sao chép cơ sở mã công khai hoặc riêng tư.  Kho lưu trữ riêng tư yêu cầu xác thực cơ bản bằng Mã truy cập cá nhân (PAT) của bạn trên GitHub. Để biết thêm thông tin, hãy xem phần [Nguồn riêng tư](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#private-sources). | Được sao chép trực tiếp vào `/workspace/` (thường là trong `/workspace/<repo-name>`). |

- **Để khôi phục một môi trường trước đó**, bạn có thể [sử dụng lại một mã môi trường hiện có](#reusing-an-existing-environment-id) để sao chép và phân nhánh trạng thái chính xác của môi trường đó.

### Sử dụng lại mã môi trường hiện có

Nếu đã dành thời gian thiết lập một môi trường hộp cát, bạn không cần phải bắt đầu lại từ đầu. Cách sử dụng một môi trường hiện có:

1. Chuyển đến bảng điều khiển Environments (Môi trường) trong AI Studio rồi chuyển **Type** (Loại) thành **Existing** (Hiện có)
2. Nhập **Mã môi trường** (ví dụ: `env_abc123`)

Để biết thêm thông tin, hãy xem phần [Định cấu hình môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#configure-an-environment). Bạn cũng có thể truy xuất Mã nhận dạng môi trường của phiên hiện tại trong thẻ Môi trường của giao diện người dùng.

Sau khi bạn gửi tin nhắn đầu tiên cho nhân viên hỗ trợ, cấu hình môi trường sẽ cố định cho phiên đó. Bạn không thể gắn các nguồn mới hoặc sửa đổi danh sách cho phép mạng trong khi hoạt động tương tác đang chạy.

## Tải môi trường xuống

Sau khi tạo một môi trường, bạn có thể tải ảnh chụp nhanh môi trường xuống bất cứ lúc nào bằng cách sử dụng nút **Tải xuống** trong phần Cài đặt môi trường của AI Studio Playground để truy xuất các tệp môi trường dưới dạng một tệp tar.

## Quản lý chi phí và an toàn

### Quản lý việc sử dụng mã thông báo

Không giống như yêu cầu trò chuyện tiêu chuẩn chỉ tạo ra một đầu ra, Antigravity Agent thực thi một quy trình công việc tự động. Nó lên kế hoạch, chạy mã, quan sát kết quả và lặp lại. Điều này có nghĩa là một câu lệnh duy nhất có thể dẫn đến mức tiêu thụ mã thông báo không giới hạn.

Để quản lý chi phí, hãy **cung cấp tiêu chí chấm dứt rõ ràng trong câu lệnh và thu hẹp phạm vi nhiệm vụ cho tác nhân**. Một ví dụ hay có thể là câu lệnh như *Xem xét yêu cầu kéo và dừng lại sau khi bạn đã tạo bản tóm tắt bằng markdown.
Đừng tự mình tìm cách khắc phục*.

### Chi phí bổ sung

Theo mặc định, tất cả các mẫu tác nhân trên Playground đều có quyền truy cập vào dịch vụ Gemini API và có thể thực hiện các lệnh gọi API từ môi trường để thực hiện các yêu cầu. Những thao tác này có thể phát sinh thêm chi phí và sẽ không được phản ánh trong mức tiêu thụ mã thông báo.

Tương tự, nếu bạn thêm các dịch vụ bên ngoài khác, thì tác nhân có thể phát sinh thêm chi phí khi gọi các dịch vụ này thay cho bạn.

### Danh sách mạng được phép

Theo mặc định, trên AI Studio, tất cả các yêu cầu mạng gửi đi từ môi trường hộp cát của tác nhân đều được kiểm soát chặt chẽ và hạn chế để đảm bảo an toàn. Để cấp cho tác nhân của bạn khả năng truy cập vào các API bên ngoài, dịch vụ web hoặc trình quản lý gói, bạn phải khai báo rõ ràng các API đó:

1. Chuyển đến bảng điều khiển Environments (Môi trường) trong AI Studio.
2. Chọn nút **quy tắc** bên cạnh **Mạng**.
3. Trong bảng điều khiển **Cấu hình mạng**, hãy nhấp vào **Thêm vào danh sách cho phép** rồi điền thông tin chi tiết có liên quan:
   - **Hạn chế về miền:** Chỉ những miền cụ thể hoặc mẫu ký tự đại diện được thêm vào danh sách mới có thể truy cập vào máy ảo của tác nhân. Ví dụ: bạn có thể nhập các miền chính xác như `api.github.com` hoặc các mẫu rộng như `*.googleapis.com`.
   - **Thêm tiêu đề HTTP và chèn mã thông báo:** Sử dụng lựa chọn **Thêm tiêu đề HTTP** để chèn thông tin đăng nhập bắt buộc (chẳng hạn như mã thông báo API) một cách an toàn cho một miền cụ thể. Những thông tin đăng nhập này được truyền an toàn thông qua một proxy xuất và không bao giờ bị lộ trực tiếp dưới dạng văn bản thô bên trong hộp cát của tác nhân.

Luôn thận trọng khi thêm miền vào danh sách cho phép. Việc cấp cho tác nhân quyền truy cập vào các dịch vụ đã xác thực có nghĩa là tác nhân có thể thay mặt bạn hành động, điều này có thể dẫn đến những hành động ngoài ý muốn nếu bạn không giám sát cẩn thận.

### Các phương pháp hay nhất về thông tin đăng nhập

Nếu quy trình làm việc của bạn yêu cầu tác nhân xác thực bằng các dịch vụ bên ngoài, thì bạn chịu trách nhiệm cung cấp và xác định phạm vi cho những thông tin đăng nhập đó. Hãy làm theo các nguyên tắc sau để giảm rủi ro:

- **Sử dụng thông tin đăng nhập có ít đặc quyền nhất:** Tạo tài khoản dịch vụ hoặc khoá API chỉ có các quyền mà tác nhân của bạn cần. Tránh truyền thông tin đăng nhập có quyền truy cập rộng hoặc quyền quản trị.
- **Ưu tiên mã thông báo ngắn hạn:** Nếu có thể, hãy sử dụng thông tin đăng nhập hoặc mã thông báo có giới hạn thời gian và hết hạn thay vì khoá API dài hạn.
- **Giả định có toàn quyền truy cập:** Tác nhân có thể sử dụng mọi thông tin đăng nhập mà tác nhân có quyền truy cập để hoàn thành nhiệm vụ mà bạn đã giao. Chỉ cung cấp thông tin đăng nhập mà bạn sẵn sàng cấp toàn bộ phạm vi quyền truy cập.
- **Thường xuyên xoay vòng thông tin đăng nhập:** Xử lý thông tin đăng nhập được chia sẻ với tác nhân theo cách tương tự như cách bạn xử lý mọi thông tin đăng nhập có lập trình; xoay vòng thông tin đăng nhập theo lịch trình thường xuyên.

### Kết nối các công cụ và API bên ngoài

Bạn có thể kết nối các công cụ và API bên ngoài (chẳng hạn như máy chủ Giao thức ngữ cảnh mô hình / MCP) để mở rộng các chức năng của tác nhân. Khi làm như vậy:

- Chỉ kết nối các công cụ từ những nguồn mà bạn tin tưởng. Một công cụ độc hại hoặc được viết kém có thể làm lộ dữ liệu hoặc thực hiện các hành động không mong muốn.
- Định cấu hình các công cụ với quyền tối thiểu cần thiết cho trường hợp sử dụng của bạn. Nếu một công cụ hỗ trợ chế độ chỉ có thể đọc, hãy ưu tiên chế độ đó trừ phi bạn thực sự cần ghi.
- Trước khi kết nối một công cụ với nguồn dữ liệu sản xuất, hãy kiểm thử công cụ đó dựa trên dữ liệu mẫu hoặc dữ liệu tổng hợp để xác minh rằng tác nhân sử dụng công cụ đó như dự kiến.

### Sự giám sát của con người

Các tác nhân có thể suy luận, lập kế hoạch và thực thi quy trình làm việc nhiều bước với mức độ tự chủ cao. Mặc dù có nhiều tính năng, nhưng điều này cũng có nghĩa là bạn nên áp dụng chế độ giám sát thích hợp; đặc biệt là đối với những tác vụ sửa đổi dữ liệu hoặc tương tác với các hệ thống bên ngoài.

Luôn xác minh các kết quả đầu ra quan trọng như mã được tạo, quá trình chuyển đổi dữ liệu hoặc các thay đổi về cấu hình trước khi triển khai.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-08-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-08-19 UTC."],[],[]]
