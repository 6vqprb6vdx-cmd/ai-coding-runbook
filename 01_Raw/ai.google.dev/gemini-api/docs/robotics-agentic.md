---
source_url: https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=vi
fetched_at: 2026-08-24T02:19:37.703890+00:00
title: "T\u1ea7m nh\u00ecn d\u1ef1a tr\u00ean t\u00e1c nh\u00e2n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tầm nhìn dựa trên tác nhân

Các mô hình Gemini Robotics ER có thể viết và thực thi mã Python để thao tác với hình ảnh và áp dụng logic trước khi trả lời. Trang này trình bày các ví dụ về việc thực thi mã: phát hiện đối tượng bằng cách thu phóng và cắt, đọc nhạc cụ, đo chất lỏng, đọc bảng mạch và chú thích hình ảnh.

Để điều chỉnh các ví dụ này cho trường hợp sử dụng của riêng bạn, hãy thay thế văn bản câu lệnh và tệp hình ảnh đã tải lên bằng văn bản và tệp hình ảnh của riêng bạn. Bạn cũng có thể điều chỉnh giản đồ JSON được yêu cầu trong câu lệnh để khớp với cấu trúc đầu ra mà ứng dụng của bạn cần, hoặc thêm `system_instruction` để thực thi định dạng và độ chính xác của đầu ra.

Để xem toàn bộ mã có thể chạy, hãy xem [Sổ tay về robot học](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Cấp độ tư duy

Bạn có thể kiểm soát mức độ tư duy của mô hình để đánh đổi độ trễ lấy độ chính xác. Các tác vụ không gian như phát hiện đối tượng hoạt động hiệu quả với mức độ tư duy thấp. Các nhiệm vụ phức tạp như đếm hoặc ước tính trọng lượng sẽ có lợi khi bạn có cấp độ tư duy cao hơn.

Ví dụ sau đây đặt cấp độ tư duy thành `high` cho một nhiệm vụ đếm phức tạp:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="scene.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": "Identify and count all objects on the table."}
    ],
    generation_config={
        "thinking_level": "high"  # Use "minimal" or "low" for faster spatial tasks
    }
)

print(interaction.output_text)
```

Hãy xem phần [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi) để biết thông tin chi tiết.

## Phát hiện đối tượng (Thu phóng và cắt)

Ví dụ sau đây sử dụng tính năng thực thi mã để phóng to và cắt một hình ảnh nhằm có chế độ xem rõ ràng hơn khi phát hiện các đối tượng và trả về các hộp giới hạn.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="sorting.jpeg")

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

Đầu ra của mô hình sẽ tương tự như phản hồi JSON sau:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

Hình ảnh sau đây cho thấy các hộp được trả về từ mô hình.

![Ví dụ minh hoạ các hộp giới hạn cho những đối tượng được tìm thấy](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=vi)

## Đọc đồng hồ đo analog và áp dụng logic

Ví dụ sau đây minh hoạ cách sử dụng mô hình để đọc đồng hồ đo tương tự và thực hiện các phép tính thời gian. Công cụ này sử dụng một chỉ dẫn hệ thống để thực thi đầu ra JSON.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="gauge.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

## Đo chất lỏng trong một hộp đựng

Ví dụ sau đây minh hoạ cách sử dụng tính năng thực thi mã để đo mức chất lỏng trong một hộp chứa.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="fluid.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

## Đọc các dấu hiệu trên bảng mạch

Ví dụ sau đây minh hoạ cách sử dụng tính năng thực thi mã để đọc các dấu hiệu trên bảng mạch.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="circuit_board.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

![Ví dụ minh hoạ các dấu hiệu trên bảng mạch](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=vi)

## Chú thích hình ảnh

Ví dụ sau đây minh hoạ cách sử dụng tính năng thực thi mã để chú thích một hình ảnh (ví dụ: vẽ mũi tên cho hướng dẫn xử lý) và trả về hình ảnh đã sửa đổi.

### Python

```
from google import genai

client = genai.Client()

# Load your image
uploaded_file = client.files.upload(file="sorting.jpeg")

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

Sau đây là một ví dụ về dữ liệu đầu vào hình ảnh.

![Ví dụ minh hoạ một chiếc đồng hồ để đọc](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=vi)

Đầu ra của mô hình sẽ tương tự như sau:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## Bước tiếp theo

- [Điều phối tác vụ](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=vi) – các tác vụ dài hạn bằng API robot tuỳ chỉnh.
- [Robot học có tính năng truyền trực tuyến](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=vi) – truyền trực tuyến hai chiều theo thời gian thực (chỉ Gemini Robotics ER 2).
- [Hiểu video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=vi) – tìm khoảnh khắc và phân loại tiến trình (chỉ Gemini Robotics ER 2).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-30 UTC."],[],[]]
