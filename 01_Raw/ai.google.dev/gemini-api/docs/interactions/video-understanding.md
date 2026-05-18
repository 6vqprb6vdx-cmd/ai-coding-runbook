---
source_url: https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=vi
fetched_at: 2026-05-18T13:08:12.046362+00:00
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

# Hiểu video

> Để tìm hiểu về tính năng tạo video, hãy xem hướng dẫn về [Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi).

Các mô hình Gemini có thể xử lý video, cho phép nhiều trường hợp sử dụng của nhà phát triển tiên phong mà trước đây cần đến các mô hình dành riêng cho miền.
Một số khả năng thị giác của Gemini bao gồm: mô tả, phân đoạn và trích xuất thông tin từ video, trả lời câu hỏi về nội dung video và tham khảo dấu thời gian cụ thể trong video.

Bạn có thể cung cấp video làm dữ liệu đầu vào cho Gemini theo những cách sau:

| Phương thức nhập | Kích thước tối đa | Trường hợp sử dụng được đề xuất |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (có tính phí) / 2 GB (miễn phí) | Tệp lớn (từ 100 MB trở lên), video dài (từ 10 phút trở lên), tệp có thể dùng lại. |
| [Đăng ký Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi#registration) | 2 GB (mỗi tệp, không giới hạn bộ nhớ) | Tệp lớn (từ 100 MB trở lên), video dài (từ 10 phút trở lên), tệp cố định, có thể dùng lại. |
| [Dữ liệu nội tuyến](#inline-video) | < 100MB | Tệp nhỏ (<100 MB), thời lượng ngắn (<1 phút), dữ liệu đầu vào một lần. |
| [URL trên YouTube](#youtube) | Không áp dụng | Video công khai trên YouTube. |

> **Lưu ý:** Bạn nên dùng [File API](#upload-video) cho hầu hết các trường hợp sử dụng, đặc biệt là đối với những tệp có kích thước lớn hơn 100 MB hoặc khi bạn muốn dùng lại tệp trong nhiều yêu cầu.

Để tìm hiểu về các phương thức nhập tệp khác, chẳng hạn như sử dụng URL bên ngoài hoặc tệp được lưu trữ trong Google Cloud, hãy xem hướng dẫn [Phương thức nhập tệp](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=vi).

### Tải tệp video lên

Đoạn mã sau đây tải một video mẫu xuống, tải video đó lên bằng [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi), đợi video được xử lý, sau đó dùng thông tin tham chiếu về tệp đã tải lên để tóm tắt video.

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  // Wait for the file to be processed.
  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Luôn sử dụng Files API khi tổng kích thước yêu cầu (bao gồm cả tệp, câu lệnh văn bản, hướng dẫn hệ thống, v.v.) lớn hơn 20 MB, thời lượng video đáng kể hoặc nếu bạn dự định sử dụng cùng một video trong nhiều câu lệnh.
File API chấp nhận trực tiếp các định dạng tệp video.

Để tìm hiểu thêm về cách làm việc với tệp đa phương tiện, hãy xem [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi).

### Truyền dữ liệu video nội tuyến

Thay vì tải tệp video lên bằng File API, bạn có thể truyền trực tiếp các video nhỏ hơn trong yêu cầu. Phương thức này phù hợp với những video ngắn có tổng kích thước yêu cầu dưới 20 MB.

Dưới đây là ví dụ về cách cung cấp dữ liệu video nội tuyến:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### URL của YouTube

Bạn có thể truyền trực tiếp URL của YouTube đến Gemini API trong yêu cầu của mình như sau:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Các điểm hạn chế:**

- Đối với gói miễn phí, bạn không thể tải quá 8 giờ video trên YouTube lên mỗi ngày.
- Đối với gói có tính phí, không có giới hạn về thời lượng video.
- Đối với các mô hình trước Gemini 2.5, bạn chỉ có thể tải 1 video lên mỗi yêu cầu. Đối với Gemini 2.5 và các mô hình sau này, bạn có thể tải tối đa 10 video lên cho mỗi yêu cầu.
- Bạn chỉ có thể tải video công khai lên (không thể tải video riêng tư hoặc không công khai lên).

## Tham khảo dấu thời gian trong nội dung

Bạn có thể đặt câu hỏi về những thời điểm cụ thể trong video bằng cách sử dụng dấu thời gian có dạng `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Trích xuất thông tin chi tiết từ video

Các mô hình Gemini mang đến những khả năng mạnh mẽ để hiểu nội dung video bằng cách xử lý thông tin từ cả luồng **âm thanh và hình ảnh**. Nhờ đó, bạn có thể trích xuất một bộ thông tin chi tiết phong phú, bao gồm cả việc tạo nội dung mô tả về những gì đang diễn ra trong video và trả lời các câu hỏi về nội dung của video.

Đối với nội dung mô tả bằng hình ảnh, mô hình lấy mẫu video với tốc độ **1 khung hình/giây** (FPS). Tỷ lệ lấy mẫu mặc định này phù hợp với hầu hết nội dung, nhưng lưu ý rằng tỷ lệ này có thể bỏ lỡ các chi tiết trong video có chuyển động nhanh hoặc cảnh thay đổi nhanh.
Đối với nội dung có chuyển động nhanh như vậy, hãy cân nhắc [đặt tốc độ khung hình tuỳ chỉnh](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Định dạng video được hỗ trợ

Gemini hỗ trợ các loại MIME sau đây cho định dạng video:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Thông tin kỹ thuật về video

- **Các mô hình và ngữ cảnh được hỗ trợ**: Tất cả các mô hình Gemini đều có thể xử lý dữ liệu video.
  - Các mô hình có cửa sổ ngữ cảnh 1 triệu token có thể xử lý video dài tối đa 1 giờ ở độ phân giải mặc định hoặc video dài tối đa 3 giờ ở độ phân giải thấp.
- **Xử lý bằng File API**: Khi sử dụng File API, video được lưu trữ ở tốc độ 1 khung hình/giây (FPS) và âm thanh được xử lý ở tốc độ 1 Kbps (một kênh).
  Dấu thời gian được thêm vào mỗi giây.
  - Những tỷ lệ này có thể thay đổi trong tương lai để cải thiện khả năng suy luận.
- **Tính toán mã thông báo**: Mỗi giây video được mã hoá như sau:
  - Khung hình riêng lẻ (lấy mẫu ở tốc độ 1 khung hình/giây):
    - Nếu `media_resolution` được đặt thành thấp, các khung hình sẽ được mã hoá thành 66 mã thông báo cho mỗi khung hình.
    - Nếu không, các khung hình sẽ được mã hoá thành 258 mã thông báo cho mỗi khung hình.
  - Âm thanh: 32 mã thông báo mỗi giây.
  - Siêu dữ liệu cũng được đưa vào.
  - Tổng cộng: Khoảng 300 mã thông báo cho mỗi giây video ở độ phân giải mặc định của nội dung nghe nhìn hoặc 100 mã thông báo cho mỗi giây video ở độ phân giải thấp của nội dung nghe nhìn.
- **Độ phân giải trung bình**: Gemini 3 giới thiệu khả năng kiểm soát chi tiết đối với quá trình xử lý hình ảnh đa phương thức bằng tham số `media_resolution`. Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi khung hình đầu vào của hình ảnh hoặc video.**
  Độ phân giải cao hơn giúp cải thiện khả năng đọc văn bản nhỏ hoặc xác định các chi tiết nhỏ của mô hình, nhưng làm tăng mức sử dụng mã thông báo và độ trễ.

  tính toán, hãy xem hướng dẫn về [mã thông báo](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=vi).
- **Định dạng dấu thời gian**: Khi đề cập đến những khoảnh khắc cụ thể trong video trong câu lệnh, hãy sử dụng định dạng `MM:SS` (ví dụ: `01:15` cho 1 phút 15 giây).
- **Các phương pháp hay nhất**:

  - Chỉ sử dụng một video cho mỗi yêu cầu câu lệnh để có kết quả tối ưu.
  - Nếu kết hợp văn bản và một video, hãy đặt câu lệnh bằng văn bản *sau* phần video trong mảng `input`.
  - Xin lưu ý rằng các cảnh hành động nhanh có thể bị mất chi tiết do tốc độ lấy mẫu 1 khung hình/giây. Cân nhắc làm chậm những đoạn video như vậy nếu cần.

## Bước tiếp theo

Hướng dẫn này trình bày cách tải tệp video lên và tạo đầu ra văn bản từ đầu vào video. Để tìm hiểu thêm, hãy xem các tài nguyên sau:

- [Hướng dẫn hệ thống](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=vi#system-instructions): Hướng dẫn hệ thống giúp bạn điều hướng hành vi của mô hình dựa trên nhu cầu và trường hợp sử dụng cụ thể của bạn.
- [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi): Tìm hiểu thêm về cách tải lên và quản lý tệp để sử dụng với Gemini.
- [Chiến lược đặt câu lệnh cho tệp](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi#prompt-guide): Gemini API hỗ trợ đặt câu lệnh bằng dữ liệu văn bản, hình ảnh, âm thanh và video, còn được gọi là đặt câu lệnh đa phương thức.
- [Hướng dẫn về an toàn](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi): Đôi khi, các mô hình AI tạo sinh tạo ra kết quả không mong muốn, chẳng hạn như kết quả không chính xác, thiên vị hoặc phản cảm. Việc xử lý hậu kỳ và đánh giá của con người là điều cần thiết để hạn chế nguy cơ gây hại từ những kết quả như vậy.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-09 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-09 UTC."],[],[]]
