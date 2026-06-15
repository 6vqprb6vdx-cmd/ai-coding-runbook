---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi
fetched_at: 2026-06-15T06:18:45.844454+00:00
title: "H\u01b0\u1edbng d\u1eabn nhanh v\u1ec1 Managed Agents \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hướng dẫn nhanh về Managed Agents

Hướng dẫn này sẽ hướng dẫn bạn cách tạo và sử dụng Tác nhân được quản lý trên Gemini API, bằng cách sử dụng [tác nhân Antigravity](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=vi). Bạn sẽ thực hiện cuộc gọi đầu tiên cho trợ lý, tiếp tục cuộc trò chuyện nhiều lượt, truyền trực tuyến phản hồi, tải tệp xuống từ hộp cát và làm việc với trợ lý được quản lý Antigravity.

## Chạy lượt tương tác đầu tiên với nhân viên hỗ trợ

Một lệnh gọi duy nhất đến [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi) sẽ cung cấp một hộp cát Linux, chạy vòng lặp tác nhân và trả về kết quả. Bạn sẽ xác định 3 tham số:

- Truyền `agent` dưới dạng `"antigravity-preview-05-2026",`. Đây là phiên bản hiện tại của tác nhân được quản lý đa năng và xác định trước của chúng tôi.
- Xác định `environment="remote"` để cung cấp một môi trường hộp cát mới và sạch.
- Tạo một đầu vào, xác định những việc bạn muốn tác nhân thực hiện.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

Phản hồi trả về một đối tượng `Interaction`. Lưu trữ `interaction.id` và `interaction.environment_id` để tiếp tục cuộc trò chuyện trong cùng một hộp cát. Sử dụng `interaction.output_text` để truy cập vào câu trả lời cuối cùng của trợ lý. `interaction.steps` liệt kê từng bước mà tác nhân đã thực hiện (suy luận, lệnh gọi công cụ, thực thi mã).

## Tiếp tục cuộc trò chuyện (nhiều lượt)

API này theo dõi 2 phương diện trạng thái độc lập:

- **Bối cảnh cuộc trò chuyện:** nhật ký trò chuyện, dấu vết suy luận, việc sử dụng công cụ, sử dụng `previous_interaction_id`.
- [**Trạng thái môi trường:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi) tệp, các gói đã cài đặt và trạng thái hộp cát, bằng cách sử dụng `environment`.

Truyền cả hai vào vị trí tương ứng để tiếp tục:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

Các tệp từ lượt 1 (`fibonacci.txt`) vẫn tồn tại trong lượt 2. Tác nhân cũng lưu giữ bối cảnh trò chuyện.

Bạn có thể kết hợp các thành phần này một cách độc lập:

- **Xoá cuộc trò chuyện, giữ lại tệp:** Bỏ qua `previous_interaction_id`, chỉ truyền mã nhận dạng môi trường bằng `environment` để bắt đầu một cuộc trò chuyện mới trong cùng một không gian làm việc.
- **Giữ lại cuộc trò chuyện, không gian làm việc mới:** Truyền `previous_interaction_id`, đặt `environment="remote"` cho một hộp cát mới.

### Tự động nén bối cảnh

Trong các cuộc trò chuyện kéo dài nhiều lượt, nhật ký thô về các bước suy luận, lệnh gọi công cụ và nội dung tệp lớn có thể nhanh chóng tăng lên và chiếm một lượng lớn không gian bối cảnh. Để ngăn lỗi vượt quá giới hạn mã thông báo và duy trì sự tập trung của tác nhân (ngăn chặn "sự suy giảm ngữ cảnh"), Managed Agents API có một bước nén ngữ cảnh gốc ở khoảng 135.000 mã thông báo. Quy trình này diễn ra tự động.

## Hiện câu trả lời theo thời gian thực

Đối với các tác vụ chạy trong thời gian dài, bạn có thể truyền trực tuyến phản hồi để xem tác nhân hoạt động theo thời gian thực:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

Truyền trực tuyến trả về một đối tượng có thể lặp lại gồm các delta bước, là văn bản gia tăng, mã thông báo suy luận và thông tin cập nhật về lệnh gọi công cụ. Tìm hiểu thêm về cách truyền trực tuyến các câu trả lời trong [Hướng dẫn truyền trực tuyến](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=vi).

## Tải tệp xuống từ môi trường

Khi tác nhân tạo tệp bên trong hộp cát. Tải các tệp này xuống bằng Files API thông qua yêu cầu HTTP trực tiếp (chưa có phương thức SDK):

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## Lưu tác nhân được quản lý

Trong các bước trước, chúng ta đã sử dụng tác nhân Antigravity mặc định và tuỳ chỉnh tác nhân này theo dòng. Sau khi lặp lại cấu hình (hướng dẫn, kỹ năng và môi trường), bạn có thể lưu cấu hình đó dưới dạng một tác nhân được quản lý. Điều này cho phép bạn gọi nó theo mã nhận dạng mà không cần lặp lại cấu hình.

Khi lưu một tác nhân, bạn sẽ xác định một `base_environment` (từ các nguồn hoặc bằng cách phân nhánh một môi trường hiện có). Nhân viên hỗ trợ sẽ sử dụng môi trường này cho mọi lượt tương tác mới.

**Từ các nguồn:** Xác định các nguồn nội tuyến hoặc từ các nguồn khác như GitHub hoặc Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Gọi tác nhân được quản lý

Sau khi lưu một tác nhân được quản lý, bạn có thể gọi tác nhân đó theo mã nhận dạng. Mỗi lệnh gọi sẽ phân nhánh môi trường cơ sở, vì vậy, mọi lượt chạy đều bắt đầu từ đầu:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## Bước tiếp theo

- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi): các chức năng, công cụ được hỗ trợ, dữ liệu đầu vào đa phương thức, giá và các hạn chế.
- [Tạo tác nhân được quản lý](https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi): mở rộng Antigravity bằng các hướng dẫn, kỹ năng và dữ liệu của riêng bạn.
- [Môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi): nguồn, mạng, vòng đời, giới hạn tài nguyên.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi): API cơ bản cho các mô hình và tác nhân.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-20 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-20 UTC."],[],[]]
