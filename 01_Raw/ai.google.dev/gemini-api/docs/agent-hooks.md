---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=vi
fetched_at: 2026-10-19T05:30:29.664733+00:00
title: "M\u00f3c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Móc

Các hook cho phép bạn chạy tập lệnh tuỳ chỉnh hoặc các yêu cầu HTTP bên ngoài ngay trước hoặc sau khi tác nhân thực thi mã hoặc sửa đổi tệp trong hộp cát từ xa. Sử dụng các hook để mở rộng vòng lặp của tác nhân bằng các quy trình công việc ở chế độ nền và hàng rào tự động, chẳng hạn như:

- **Thực thi các biện pháp bảo vệ an toàn và quyền truy cập** trước khi thực thi các lệnh shell có mức độ rủi ro cao hoặc các thao tác đọc tệp bị hạn chế.
- **Tự động hoá các hoạt động chuyển đổi quy trình dữ liệu** ngay sau khi một nhân viên tạo hoặc sửa đổi tệp.
- **Truyền trực tuyến dữ liệu đo từ xa kiểm tra doanh nghiệp** đến các hệ thống giám sát bên ngoài sau khi thực thi công cụ.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
            },
        ],
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
    },
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

String gateScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "cmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\n"
    + "if \"rm -rf\" in cmd:\n"
    + "    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\n"
    + "else:\n"
    + "    print(json.dumps({\"decision\": \"allow\"}))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/gate.py")
            .content(gateScript)
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run `rm -rf /tmp/forbidden` using code_execution."))
    .tools(List.of(CodeExecution.builder().build()))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    gateScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/gate.py"),
                Content: genai.Ptr(gateScript),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run `rm -rf /tmp/forbidden` using code_execution."),
            Tools:       []interactions.Tool{interactions.NewTool(interactions.CodeExecution{})},
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## Các sự kiện trong vòng đời được hỗ trợ

Các hook hỗ trợ 2 sự kiện trong hộp cát:

| Sự kiện | Thời điểm kích hoạt | Ý nghĩa |
| --- | --- | --- |
| `pre_tool_execution` | Ngay trước khi một công cụ chạy | Có thể phê duyệt (`allow`) hoặc chặn (`deny`) công cụ này trước khi công cụ thực thi. Khi bị chặn, mô hình sẽ thấy lý do bạn từ chối và điều chỉnh. |
| `post_tool_execution` | Ngay sau khi một công cụ hoàn tất | Chạy các tác vụ tiếp theo như định dạng mã, chạy kiểm thử đơn vị hoặc ghi nhật ký đo từ xa. Không thể chặn hoặc huỷ các thao tác đã hoàn tất. |

### `pre_tool_execution`

Kích hoạt ngay trước khi một công cụ thực thi. Tập lệnh của bạn đọc thông tin chi tiết về lệnh gọi công cụ từ `stdin` và xuất JSON quyết định (`allow` hoặc `deny`) sang `stdout`.

**Phần tải đầu vào (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**Phản hồi đầu ra (`stdout`):**

Cách phê duyệt lệnh gọi công cụ:

```
{
  "decision": "allow"
}
```

Để chặn lệnh gọi công cụ và trả về ý kiến phản hồi cho mô hình:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

Khi một lệnh từ chối lệnh, lệnh gọi công cụ sẽ bị bỏ qua ngay lập tức. Ngay trong lượt hiện tại, tác nhân sẽ thấy một kết quả lỗi có chứa lý do từ chối của bạn. Sau đó, mô hình có thể tự điều chỉnh bằng cách chọn một lệnh thay thế hoặc giải thích cho người dùng về khối này.

Nếu tập lệnh của bạn xuất ra JSON, văn bản thuần tuý hoặc bất kỳ nội dung nào khác ngoài `{"decision": "deny"}` mà không được nhận dạng, thì thời gian chạy sẽ coi phản hồi đó là một phản hồi phê duyệt (`allow`).

### `post_tool_execution`

Kích hoạt ngay sau khi một công cụ hoàn tất. Tập lệnh của bạn sẽ đọc thông tin chi tiết về quá trình thực thi và mọi trạng thái lỗi từ `stdin`.

**Phần tải đầu vào (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

Nếu một lệnh shell in lỗi ra lỗi chuẩn (`stderr`) hoặc một thao tác trên hệ thống tệp không thành công, thì một trường `"error"` chứa văn bản lỗi sẽ được đưa vào tải trọng. Khi lệnh thành công mà không có lỗi, trường `"error"` sẽ bị bỏ qua hoàn toàn.

**Phản hồi đầu ra (`stdout`):**

```
{}
```

Vì các lệnh gọi sau công cụ chỉ chạy cho các tác vụ trong nền như định dạng mã hoặc ghi nhật ký, nên thời gian chạy sẽ bỏ qua mọi giá trị quyết định được trả về trên `stdout`.

## Khám phá cấu hình

Thời gian chạy sẽ tự động phát hiện các định nghĩa về lệnh gọi từ `.agents/hooks.json` hoặc `/.agents/hooks.json` trong môi trường hộp cát. Bạn có thể cung cấp `hooks.json` cùng với các tập lệnh tuỳ chỉnh bằng cách sử dụng bất kỳ [nguồn môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#mount_from_a_source) nào được hỗ trợ:

- **Thư mục gốc của kho lưu trữ**: Kho lưu trữ Git chứa `.agents/hooks.json` cùng với `AGENTS.md`.
- **Cloud Storage (`gcs`)**: Bộ chứa GCS chứa `hooks.json` được sao chép vào môi trường.
- **Nguồn nội tuyến**: Chuỗi JSON thô và nội dung tập lệnh được truyền trong `environment.sources` khi gọi `client.interactions.create`.

### Lược đồ `hooks.json`

Tệp `hooks.json` nhóm các định nghĩa về sự kiện (`pre_tool_execution` hoặc `post_tool_execution`) theo tên tuỳ chỉnh. Bạn có thể bật hoặc tắt từng nhóm một cách độc lập:

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### Cú pháp và quy tắc của bộ so khớp

Mỗi nhóm quy tắc trong `hooks.json` xác định thời điểm và cách các trình xử lý kích hoạt bằng cách sử dụng các thuộc tính `matcher` và `hooks`:

| Trường | Loại | Mô tả |
| --- | --- | --- |
| `enabled` | `boolean` | Không bắt buộc. Đặt thành `false` để tắt nhóm (`true` theo mặc định). |
| `matcher` | `string` | Mẫu biểu thức chính quy so khớp tên công cụ mục tiêu bên trong vùng chứa. |
| `hooks` | `array` | Danh sách có thứ tự gồm các định nghĩa về trình xử lý (`command` hoặc `http`). Các trình xử lý chạy tuần tự theo thứ tự khai báo. |

#### Cách hoạt động của quy trình đánh giá biểu thức chính quy

Khi tác nhân gọi một công cụ bên trong hộp cát, thời gian chạy sẽ đánh giá tên vùng chứa của công cụ dựa trên mẫu `matcher` bằng cách sử dụng các biểu thức chính quy RE2 tiêu chuẩn. Nếu biểu thức chính quy khớp với tên công cụ, tất cả trình xử lý trong mảng `hooks` sẽ thực thi theo thứ tự. Nếu nhiều nhóm quy tắc khớp với cùng một công cụ, thì tất cả các mảng trình xử lý tương ứng sẽ chạy.

Bạn có thể nhắm đến bất kỳ tên công cụ vùng chứa tích hợp nào: thực thi mã (`code_execution`) hoặc các thao tác trên hệ thống tệp (`view_file`, `write_to_file`, `replace_file_content`, `list_dir` và `delete_file`).

#### Các biểu thức trình khớp thường dùng

- `"code_execution"`: So khớp chuỗi chính xác cho các lệnh shell và quá trình thực thi tập lệnh.
- `"write_to_file"`: So khớp chính xác cho hoạt động tạo tệp hệ thống tệp và ghi vào đĩa.
- `"view_file|write_to_file"`: Phân tách bằng dấu sổ dọc để so khớp nhiều tên công cụ cụ thể trong một quy tắc duy nhất.
- `".*_file"`: Biểu thức chính quy có ký tự đại diện khớp với mọi công cụ kết thúc bằng `_file` (chẳng hạn như `view_file`, `write_to_file` hoặc `delete_file`). Biểu thức này chỉ bao gồm một phần của bộ công cụ hệ thống tệp, `replace_file_content` và `list_dir` không kết thúc bằng `_file`, vì vậy, hãy đặt tên rõ ràng cho chúng khi bạn cần. Biểu thức chính quy RE2 tiêu chuẩn yêu cầu `.*`; các ký tự đại diện đơn giản của shell như `*_file` là cú pháp regex không hợp lệ và sẽ không khớp.
- `".*"` hoặc `"*"` hoặc `""`: Mẫu chung chặn mọi lệnh gọi công cụ trong vùng chứa.

## Các loại trình xử lý

### Lệnh hook

Lệnh hook thực thi một lệnh hoặc tập lệnh shell bên trong hộp cát. Tập lệnh này nhận JSON sự kiện trên `stdin` và xuất JSON quyết định trên `stdout`.

| Trường | Loại | Mô tả |
| --- | --- | --- |
| `type` | `string` | Phải là `"command"`. |
| `command` | `string` | Dòng lệnh để chạy trong hộp cát (ví dụ: `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | Thời gian chờ tính bằng giây. Mặc định: `30`. |

### Các lệnh gọi HTTP

Các lệnh gọi HTTP sẽ gửi JSON sự kiện dưới dạng yêu cầu POST đến một URL HTTPS bên ngoài ngay từ bên trong mạng hộp cát. Máy chủ mục tiêu trả về quyết định của mình trong nội dung phản hồi HTTP bằng chính xác định dạng JSON (`{"decision": "allow"}` hoặc `{"decision": "deny", "reason": "..."}`).

| Trường | Loại | Mô tả |
| --- | --- | --- |
| `type` | `string` | Phải là `"http"`. |
| `url` | `string` | Điểm cuối HTTPS bên ngoài để gửi tải trọng sự kiện đến. |
| `headers` | `object` | Các cặp khoá-giá trị không bắt buộc cho các tiêu đề tuỳ chỉnh không nhạy cảm (chẳng hạn như `{"X-Event-Source": "agent-sandbox"}`). Để xác thực, hãy dùng [credential](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=vi) (thông tin đăng nhập) trong danh sách cho phép của mạng thay thế. |
| `timeout` | `integer` | Thời gian chờ tính bằng giây. Mặc định: `30`. |

#### Uỷ quyền chuyển dữ liệu ra ngoài và chuyển đổi mã thông báo

Vì các lệnh gọi HTTP thực thi trực tiếp từ bên trong không gian tên mạng hộp cát, nên các yêu cầu đi ra sẽ đi qua proxy truyền tải minh bạch. Cấu trúc này mang lại cho bạn 2 lợi thế quan trọng về bảo mật:

- **Thêm mạng vào danh sách cho phép:** Bạn phải cho phép rõ ràng các điểm cuối mục tiêu trong `network.allowlist` của môi trường. Lưu lượng truy cập vòng lặp (`127.0.0.1` hoặc `localhost`) sẽ bị chặn bởi proxy; luôn nhắm đến các điểm cuối bên ngoài nằm trong danh sách cho phép.
- **Chèn thông tin xác thực:** Bạn không cần lưu trữ khoá API hoặc mã thông báo bí mật của người mang trong `.agents/hooks.json` hoặc gắn chúng vào vùng chứa. Lưu trữ khoá bí mật một lần dưới dạng [thông tin đăng nhập](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=vi) và tham chiếu khoá bí mật đó theo mã nhận dạng từ `network.allowlist` của môi trường. Proxy truyền dữ liệu ra sẽ tự động chặn lưu lượng truy cập hook HTTP đi và chèn tiêu đề xác thực thực vào đường truyền trước khi rời khỏi hộp cát. Các tiêu đề của bộ quy tắc `transform` nội tuyến được đặt theo cùng một cách trên đường truyền, thông tin đăng nhập là thông tin cần dùng khi bạn muốn sử dụng lại khoá bí mật trong dự án và xoay vòng khoá bí mật ở một nơi. Xem [cấu hình mạng](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#network-configuration).

## Cách thời gian chạy xử lý các quyết định và lỗi

- **Chờ đồng bộ:** Tác nhân tạm dừng và đợi các lệnh gọi của bạn hoàn tất rồi mới tiếp tục.
- **Chặn quá trình thực thi công cụ:** Nếu lệnh gọi trước công cụ trả về `{"decision": "deny", "reason": "<your reason>"}`, thì thời gian chạy sẽ huỷ ngay lệnh gọi công cụ. Mô hình sẽ thấy lý do bạn từ chối trong nhật ký trò chuyện và điều chỉnh bằng cách chọn một lựa chọn thay thế an toàn hoặc giải thích cho người dùng về việc bị chặn.
- **Xử lý sự cố tập lệnh, lỗi HTTP và hết thời gian chờ:** Nếu tập lệnh lệnh gặp sự cố (trạng thái thoát khác 0), một lệnh gọi HTTP trả về mã trạng thái không phải 2xx (chẳng hạn như lỗi máy chủ 4xx hoặc 5xx) hoặc một thao tác hết thời gian chờ hoặc trả về JSON không xác định, thì thời gian chạy sẽ coi đó là một lượt phê duyệt (`allow`). Quá trình thực thi công cụ vẫn diễn ra bình thường, vì vậy, một tập lệnh bị hỏng hoặc máy chủ đo từ xa không thể truy cập sẽ không bao giờ khiến ứng dụng của bạn bị bế tắc.

## Các trường hợp sử dụng phổ biến

### Khả năng khôi phục nhiều lượt cho quyền riêng tư đối với dữ liệu và việc tuân thủ

Khi một lệnh gọi chặn quyền truy cập vào các tài nguyên bị hạn chế (chẳng hạn như các thư mục chứa Thông tin nhận dạng cá nhân (PII) hoặc hồ sơ tài chính bí mật), bạn có thể truyền `previous_interaction_id` trong lệnh gọi tiếp theo để tiếp tục lượt trong cùng một môi trường. Tác nhân sẽ đọc nội dung giải thích về việc từ chối và tự động khôi phục bằng cách truy vấn các bảng công khai đã được phê duyệt.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "view_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "view_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
""";

String checkPrivacyScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "path = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\n"
    + "if \"/private/\" in path:\n"
    + "    resp = {\n"
    + "        \"decision\": \"deny\",\n"
    + "        \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"\n"
    + "    }\n"
    + "else:\n"
    + "    resp = {\"decision\": \"allow\"}\n"
    + "print(json.dumps(resp))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/check_privacy.py")
            .content(checkPrivacyScript)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/private/employees.json")
            .content("{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/public/summary.json")
            .content("{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}")
            .build()
    ))
    .build();

// Step 1: Agent attempts to read confidential PII records and is intercepted
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction int1 = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println(int1.outputText().orElse(""));

// Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."))
    .environment(CreateAgentInteractionEnvironment.of(int1.environmentId().orElse("")))
    .previousInteractionId(int1.id().orElse(""))
    .build();

Interaction int2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println(int2.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}`

    checkPrivacyScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))
if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential '/private/' records is blocked by PII compliance policy. Query approved '/public/' summary tables instead."
    }
else:
    resp = {"decision": "allow"}
print(json.dumps(resp))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/check_privacy.py"),
                Content: genai.Ptr(checkPrivacyScript),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/private/employees.json"),
                Content: genai.Ptr(`{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}`),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/public/summary.json"),
                Content: genai.Ptr(`{"department": "Engineering", "team_size": 42, "status": "active"}`),
            },
        },
    }

    // Step 1: Agent attempts to read confidential PII records and is intercepted
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    int1 := res1.Interaction
    if int1.OutputText != nil {
        fmt.Println(*int1.OutputText)
    }

    // Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*int1.EnvironmentID)),
            PreviousInteractionID: int1.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println(*res2.Interaction.OutputText)
    }
}
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"view_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-09-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### Ghi nhật ký kiểm tra và đo từ xa bên ngoài

Gửi các sự kiện kiểm tra theo thời gian thực từ bên trong hộp cát đến một máy chủ giám sát bên ngoài bất cứ khi nào tệp được đọc hoặc sửa đổi.

- **So khớp nhiều công cụ:** Vì trình so khớp sử dụng biểu thức chính quy tiêu chuẩn, nên bạn có thể kết hợp nhiều công cụ trong một quy tắc bằng cách sử dụng dấu gạch dọc (`view_file|write_to_file|replace_file_content`) hoặc ký tự đại diện (`.*_file`).
- **Không đưa các khoá bí mật vào cấu hình:** Lưu mã thông báo xác thực dưới dạng [thông tin đăng nhập](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=vi) và tham chiếu mã thông báo đó theo mã nhận dạng từ [cấu hình mạng](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#network-configuration) (`network.allowlist.credential`) của môi trường. Proxy truyền dữ liệu ra sẽ chèn mã thông báo thực tế vào các yêu cầu gửi đi. Thay vào đó, ví dụ này đặt tiêu đề cùng dòng với `transform`. Tiêu đề này được bảo vệ bằng cùng một proxy và phù hợp khi mã thông báo thuộc về một cấu hình này.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "view_file|write_to_file|replace_file_content",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
                {"domain": "*"},
            ]
        },
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "view_file|write_to_file|replace_file_content",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
    },
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// Define hook without secrets; the egress proxy injects headers dynamically
String hooksConfig = """
{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build()
    ))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("telemetry.example.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer telemetry_secret_token_123"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("*").build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Define hook without secrets; the egress proxy injects headers dynamically
    hooksConfig := `{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "telemetry.example.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer telemetry_secret_token_123",
                    })),
                },
                {
                    Domain: "*",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"view_file|write_to_file|replace_file_content\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## Các điểm hạn chế

- **Phạm vi của công cụ hộp cát:** Các lệnh gọi API chặn các công cụ tích hợp sẵn bên trong hộp cát: thực thi mã (`code_execution`) và các thao tác trên hệ thống tệp (`view_file`, `write_to_file`, `replace_file_content`, `list_dir` và `delete_file`). Các lệnh gọi API này không kích hoạt cho lệnh gọi hàm tuỳ chỉnh (`function`) hoặc các công cụ Giao thức ngữ cảnh mô hình (`mcp_server`) bên ngoài được xử lý bên ngoài vùng chứa.
- **Danh sách cho phép mạng:** Các lệnh gọi HTTP chạy trong mạng vùng chứa. Bạn phải cho phép rõ ràng các URL đích trong `network.allowlist` của môi trường. Địa chỉ Loopback (`localhost`, `127.0.0.1`) bị chặn bởi proxy.
- **Tự động phê duyệt khi có lỗi:** Nếu tập lệnh hook gặp sự cố (trạng thái thoát khác 0), hết thời gian chờ hoặc không thành công, thì thời gian chạy sẽ ghi nhật ký lỗi và cho phép lệnh gọi công cụ tiếp tục. Điều này đảm bảo các tập lệnh linter bị hỏng hoặc các quy trình treo không bao giờ làm ứng dụng của bạn bị tắc nghẽn.
- **Bảo vệ cấu hình hộp cát:** Vì các lệnh gọi thực thi bên trong hộp cát vùng chứa, nên các tác nhân có công cụ ghi hệ thống tệp hoặc quyền thực thi mã shell có thể sửa đổi `.agents/hooks.json` cục bộ hoặc các tập lệnh trong không gian làm việc có thể ghi. Sử dụng các lệnh gọi vùng chứa làm hướng dẫn tự động về chính sách và biện pháp bảo vệ hoạt động; nếu cần có khả năng chống giả mạo nghiêm ngặt đối với các hoạt động thực thi mô hình không đáng tin cậy, hãy gắn các nguồn cấu hình từ kho lưu trữ chỉ đọc.

## Bước tiếp theo

- Tìm hiểu cách định cấu hình [môi trường và hộp cát từ xa liên tục](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi).
- Khám phá các chức năng và công cụ tích hợp của [tác nhân Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi).
- Xem [Tổng quan về Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) cho các phiên nhiều lượt và truyền phát trực tuyến.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-07 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-07 UTC."],[],[]]
