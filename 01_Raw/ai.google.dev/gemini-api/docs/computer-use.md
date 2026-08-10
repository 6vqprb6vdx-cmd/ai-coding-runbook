---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=vi
fetched_at: 2026-08-10T03:21:53.905493+00:00
title: "S\u1eed d\u1ee5ng m\u00e1y t\u00ednh \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Sử dụng máy tính

Công cụ Sử dụng máy tính cho phép bạn tạo các tác nhân kiểm soát trình duyệt, thiết bị di động và máy tính để bàn tương tác và tự động hoá các tác vụ. Bằng cách sử dụng ảnh chụp màn hình, mô hình này có thể "nhìn thấy" màn hình máy tính và "hành động" bằng cách tạo các thao tác cụ thể trên giao diện người dùng, chẳng hạn như nhấp chuột và nhập dữ liệu bằng bàn phím. Tương tự như việc gọi hàm, bạn sẽ cần triển khai môi trường thực thi phía máy khách để nhận và thực thi các thao tác Sử dụng máy tính.

Để xem danh sách các mô hình được hỗ trợ, hãy xem phần [Các phiên bản mô hình](#model-versions). Các mô hình Gemini 3.x hỗ trợ một số tính năng nâng cao:

- **Hỗ trợ nhiều môi trường:** tạo các tác nhân cho môi trường [trình duyệt, thiết bị di động và máy tính](#supported-environments).
- **Các hành động tinh giản bằng ý định:** các hành động bao gồm một trường `intent` giải thích lý do của mô hình đằng sau mỗi bước.
- **Chính sách an toàn có thể định cấu hình:** tinh chỉnh [hành vi an toàn](#safety-policies) bằng các danh mục chính sách và chế độ ghi đè được tích hợp sẵn.
- **Phát hiện tiêm câu lệnh (prompt injection):** chọn sử dụng tính năng [quét ảnh chụp màn hình](#prompt-injection) để phát hiện các câu lệnh đối nghịch bị ẩn.

Với tính năng Sử dụng máy tính, bạn có thể tạo các tác nhân có khả năng:

- Tự động hoá việc nhập dữ liệu hoặc điền biểu mẫu lặp đi lặp lại trên các trang web.
- Thực hiện kiểm thử tự động các ứng dụng web và quy trình của người dùng
- Nghiên cứu trên nhiều trang web (ví dụ: thu thập thông tin sản phẩm, giá cả và bài đánh giá từ các trang web thương mại điện tử để đưa ra quyết định mua hàng)

Dưới đây là một ví dụ tối giản về việc khởi chạy ứng dụng và gửi một câu lệnh cho mô hình khi công cụ `computer_use` được bật cho môi trường trình duyệt:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Search for 'Gemini API' on Google.",
    tools=[{"type": "computer_use", "environment": "browser"}]
)

print(interaction)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  input: "Search for 'Gemini API' on Google.",
  tools: [{ type: "computer_use", environment: "browser" }]
});

console.log(interaction);
```

## Cách hoạt động của tính năng Sử dụng máy tính

Để tạo một tác nhân bằng mô hình Sử dụng máy tính, bạn cần thiết lập một vòng lặp liên tục giữa ứng dụng và API. Sau đây là những việc mà mã của bạn sẽ làm ở mỗi bước:

1. [**Gửi yêu cầu đến mô hình**](#send-request)
   - Ứng dụng của bạn gửi một yêu cầu API có chứa công cụ Sử dụng máy tính, chế độ cài đặt cấu hình (chẳng hạn như môi trường mục tiêu), câu lệnh của người dùng và ảnh chụp màn hình hiện tại.
2. [**Nhận câu trả lời của mô hình**](#model-response)
   - Mô hình này phân tích màn hình và câu lệnh, trả về một phản hồi bao gồm `function_call` được đề xuất, đại diện cho một thao tác trên giao diện người dùng (chẳng hạn như lượt nhấp, lượt di chuyển hoặc lượt nhấn phím).
   - Đối với **các mô hình Gemini 3.x**, câu trả lời cũng bao gồm một suy luận `intent` giải thích tại sao mô hình chọn hành động đó.
   - Phản hồi cũng có thể bao gồm một `safety_decision` từ hệ thống an toàn nội bộ phân loại hành động là thông thường/được phép, `require_confirmation` (yêu cầu người dùng phê duyệt) hoặc bị chặn.
3. [**Thực thi hành động đã nhận**](#execute-actions)
   - Nếu hành động được cho phép (hoặc người dùng xác nhận hành động đó), thì mã phía máy khách của bạn sẽ phân tích cú pháp `function_call`, điều chỉnh tỷ lệ các toạ độ được chuẩn hoá cho phù hợp với khung hiển thị và thực thi hành động trong môi trường mục tiêu bằng các công cụ tự động hoá (chẳng hạn như Playwright). Nếu thao tác bị chặn, ứng dụng của bạn sẽ phải dừng thực thi hoặc xử lý gián đoạn.
4. [**Chụp trạng thái môi trường mới**](#capture-state)
   - Sau khi thao tác hoàn tất, ứng dụng của bạn sẽ chụp một ảnh chụp màn hình mới và gửi lại cho mô hình trong `function_result` để yêu cầu bước tiếp theo.

Sau đó, quy trình này lặp lại từ bước 2, liên tục yêu cầu mô hình thực hiện hành động tiếp theo cho đến khi tác vụ hoàn tất hoặc kết thúc.

![Tổng quan về việc sử dụng máy tính](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=vi)

## Cách triển khai tính năng Sử dụng máy tính

Trước khi tạo bằng công cụ Sử dụng máy tính, bạn cần thiết lập:

- **Môi trường thực thi an toàn:** Chạy tác nhân của bạn trong một VM hoặc vùng chứa được đưa vào hộp cát để tách tác nhân đó khỏi hệ thống lưu trữ và hạn chế tác động tiềm ẩn của tác nhân.
  [Triển khai tham chiếu](https://github.com/google/computer-use-preview/) bao gồm một hộp cát dựa trên Docker mà bạn có thể sử dụng ngay làm điểm xuất phát.
- **Trình xử lý thao tác phía máy khách:** Triển khai logic phía máy khách để thực thi toạ độ, nhập văn bản và chụp ảnh màn hình.

Các ví dụ bên dưới sử dụng trình duyệt web làm môi trường thực thi và [Playwright](https://playwright.dev/) làm trình xử lý phía máy khách.

### 0. Thiết lập Playwright

Trước tiên, hãy cài đặt các gói bắt buộc:

```
pip install google-genai playwright
playwright install chromium
```

Sau đó, hãy khởi chạy một phiên bản trình duyệt Playwright để sử dụng cho quá trình thực thi:

```
from playwright.sync_api import sync_playwright

# 1. Configure screen dimensions for the target environment
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# 2. Start the Playwright browser
# In production, utilize a sandboxed environment.
playwright = sync_playwright().start()
# Set headless=False to see the actions performed on your screen
browser = playwright.chromium.launch(headless=False)

# 3. Create a context and page with the specified dimensions
context = browser.new_context(
    viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
)
page = context.new_page()

# 4. Navigate to an initial page to start the task
page.goto("https://www.google.com")

# The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
# will be used in the steps below.
```

### 1. Gửi yêu cầu đến mô hình

Khởi chạy thư viện ứng dụng và định cấu hình công cụ Sử dụng máy tính. Xin lưu ý rằng bạn không cần chỉ định kích thước màn hình khi đưa ra yêu cầu; mô hình sẽ dự đoán toạ độ pixel được điều chỉnh theo chiều cao và chiều rộng của màn hình.

### Gemini 3.x

### Python

Sử dụng `google-genai` Python SDK (phiên bản `2.7.0` trở lên) để định cấu hình một yêu cầu nhắm đến môi trường trình duyệt:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input="Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "enable_prompt_injection_detection": True
        }
    ]
)

print(interaction)
```

### JavaScript

Sử dụng SDK `@google/genai` Node.js để định cấu hình một yêu cầu nhắm đến môi trường trình duyệt:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.6-flash',
  input: "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th",
  tools: [
    {
      type: "computer_use",
      environment: "browser",
      enable_prompt_injection_detection: true
    }
  ]
});

console.log(interaction);
```

### REST

Sử dụng curl để gửi yêu cầu:

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Find me a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th. Start by navigating directly to flights.google.com",
    "tools": [
      {
        "type": "computer_use",
        "environment": "browser",
        "enable_prompt_injection_detection": true
      }
    ]
  }'
```

### Gemini 2.5 (Phiên bản cũ)

### Python

```
from google import genai

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Search for highly rated smart fridges on Google Shopping.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        }
    ]
)

print(interaction)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Specify predefined functions to exclude (optional)
const excludedFunctions = ["drag_and_drop"];

const interaction = await ai.interactions.create({
  model: 'gemini-2.5-computer-use-preview-10-2025',
  input: "Search for highly rated smart fridges on Google Shopping.",
  tools: [
    {
      type: "computer_use",
      environment: "browser",
      excluded_predefined_functions: excludedFunctions
    }
  ]
});

console.log(interaction);
```

### 2. Nhận câu trả lời của mô hình

Mô hình phản hồi đề xuất một lệnh gọi hàm. Đối với **các mô hình Gemini 3.x**, phản hồi chứa ý định suy luận phù hợp cùng với toạ độ. Sau đây là ví dụ về cả hai phản hồi:

### Gemini 3.x

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click",
      "arguments": {
        "x": 450,
        "y": 120,
        "intent": "Click the search box to type the destination."
      }
    }
  ]
}
```

### Gemini 2.5 (Phiên bản cũ)

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I will type the search query into the search bar."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "type_text_at",
      "arguments": {
        "x": 371,
        "y": 470,
        "text": "highly rated smart fridges",
        "press_enter": true
      }
    }
  ]
}
```

### 3. Thực thi các hành động đã nhận

Ứng dụng của bạn phải phân tích cú pháp toạ độ phản hồi, thực thi thao tác và điều chỉnh tỷ lệ các toạ độ đó từ toạ độ 1000x1000 được chuẩn hoá.

Đoạn mã dưới đây xử lý cả lệnh của công cụ cũ (`click_at`, `type_text_at`) và lệnh hiện đại được tinh giản (`click`, `type`).

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(interaction, page, screen_width, screen_height):
    results = []
    function_calls = [
        step for step in interaction.steps if step.type == "function_call"
    ]

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.arguments
        print(f"  -> Executing: {fname} (Intent: {args.get('intent', 'N/A')})")

        try:
            if fname in ("open_web_browser", "open_app"):
                pass # Handled / already open
            elif fname in ("click", "click_at", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"):
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)

                if fname in ("click", "click_at"):
                    page.mouse.click(actual_x, actual_y)
                elif fname == "double_click":
                    page.mouse.dblclick(actual_x, actual_y)
                elif fname == "right_click":
                    page.mouse.click(actual_x, actual_y, button="right")
                elif fname == "middle_click":
                    page.mouse.click(actual_x, actual_y, button="middle")
                elif fname == "move":
                    page.mouse.move(actual_x, actual_y)
            elif fname in ("type", "type_text_at"):
                actual_x = denormalize_x(args["x"], screen_width) if "x" in args else None
                actual_y = denormalize_y(args["y"], screen_height) if "y" in args else None
                text = args["text"]
                press_enter = args.get("press_enter", False)

                if actual_x is not None and actual_y is not None:
                    page.mouse.click(actual_x, actual_y)
                # Clear field first
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            elif fname == "navigate":
                page.goto(args["url"])
            elif fname == "go_back":
                page.go_back()
            elif fname == "go_forward":
                page.go_forward()
            elif fname == "wait":
                time.sleep(args.get("seconds", 1))
            else:
                print(f"Warning: Custom or unhandled function {fname}")

            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### JavaScript

```
function denormalizeX(x, screenWidth) {
    // Convert normalized x coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((x / 1000) * screenWidth);
}

function denormalizeY(y, screenHeight) {
    // Convert normalized y coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((y / 1000) * screenHeight);
}

async function executeFunctionCalls(interaction, page, screenWidth, screenHeight) {
    const results = [];
    const functionCalls = interaction.steps.filter(step => step.type === "function_call");

    for (const functionCall of functionCalls) {
        const actionResult = {};
        const fname = functionCall.name;
        const args = functionCall.arguments;
        console.log(`  -> Executing: ${fname} (Intent: ${args.intent || 'N/A'})`);

        try {
            if (fname === "open_web_browser" || fname === "open_app") {
                // Handled / already open
            } else if (["click", "click_at", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"].includes(fname)) {
                const actualX = denormalizeX(args.x, screenWidth);
                const actualY = denormalizeY(args.y, screenHeight);

                if (fname === "click" || fname === "click_at") {
                    await page.mouse.click(actualX, actualY);
                } else if (fname === "double_click") {
                    await page.mouse.dblclick(actualX, actualY);
                } else if (fname === "right_click") {
                    await page.mouse.click(actualX, actualY, { button: "right" });
                } else if (fname === "middle_click") {
                    await page.mouse.click(actualX, actualY, { button: "middle" });
                } else if (fname === "move") {
                    await page.mouse.move(actualX, actualY);
                }
            } else if (fname === "type" || fname === "type_text_at") {
                const actualX = args.x !== undefined ? denormalizeX(args.x, screenWidth) : null;
                const actualY = args.y !== undefined ? denormalizeY(args.y, screenHeight) : null;
                const text = args.text;
                const pressEnter = args.press_enter || false;

                if (actualX !== null && actualY !== null) {
                    await page.mouse.click(actualX, actualY);
                }
                // Clear field first
                await page.keyboard.press("Meta+A");
                await page.keyboard.press("Backspace");
                await page.keyboard.type(text);
                if (pressEnter) {
                    await page.keyboard.press("Enter");
                }
            } else if (fname === "navigate") {
                await page.goto(args.url);
            } else if (fname === "go_back") {
                await page.goBack();
            } else if (fname === "go_forward") {
                await page.goForward();
            } else if (fname === "wait") {
                await new Promise(resolve => setTimeout(resolve, (args.seconds || 1) * 1000));
            } else {
                console.log(`Warning: Custom or unhandled function ${fname}`);
            }

            await page.waitForLoadState('load', { timeout: 5000 }).catch(() => {});
            await new Promise(resolve => setTimeout(resolve, 1000));
        } catch (e) {
            console.log(`Error executing ${fname}: ${e}`);
            actionResult.error = e.message;
        }

        results.push([fname, functionCall.id, actionResult]);
    }

    return results;
}
```

### 4. Ghi lại trạng thái môi trường mới

Sau khi thực hiện các hành động, hãy gửi kết quả thực thi hàm trở lại mô hình để mô hình có thể sử dụng thông tin này để tạo hành động tiếp theo. Nếu thực hiện nhiều thao tác (cuộc gọi song song), bạn phải gửi một `function_result` cho từng thao tác trong lượt tương tác tiếp theo của người dùng.

### Python

```
import json
import base64

def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, call_id, result in results:
        function_responses.append({
            "type": "function_result",
            "name": name,
            "call_id": call_id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps({"url": current_url, **result})
                },
                {
                    "type": "image",
                    "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
                    "mime_type": "image/png"
                }
            ]
        })
    return function_responses
```

### JavaScript

```
async function getFunctionResponses(page, results) {
    const screenshotBuffer = await page.screenshot({ type: 'png' });
    const screenshotBase64 = screenshotBuffer.toString('base64');
    const currentUrl = page.url();
    const functionResponses = [];

    for (const [name, callId, result] of results) {
        functionResponses.push({
            type: "function_result",
            name: name,
            call_id: callId,
            result: [
                {
                    type: "text",
                    text: JSON.stringify({ url: currentUrl, ...result })
                },
                {
                    type: "image",
                    data: screenshotBase64,
                    mime_type: "image/png"
                }
            ]
        });
    }
    return functionResponses;
}
```

Sau khi xác định cách ghi lại và định dạng trạng thái môi trường, bạn có thể kết hợp tất cả các bước này thành một vòng lặp thực thi liên tục.

## Tạo vòng lặp tác nhân

Để bật các lượt tương tác nhiều bước, hãy kết hợp 4 bước trong phần [Cách triển khai việc sử dụng máy tính](#implement-computer-use) thành một vòng lặp duy nhất.
Vòng lặp này tiếp tục yêu cầu các hành động và truyền kết quả trở lại mô hình cho đến khi tác vụ hoàn tất.

Hãy nhớ quản lý lịch sử cuộc trò chuyện một cách chính xác bằng cách thêm cả câu trả lời của mô hình và câu trả lời của hàm vào lịch sử ở mỗi bước.

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Take initial screenshot
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    # First interaction
    interaction = client.interactions.create(
        model='gemini-3.6-flash',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser",
            "enable_prompt_injection_detection": True
        }]
    )

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")

        has_function_calls = any(
            step.type == "function_call"
            for step in interaction.steps
        )
        if not has_function_calls:
            text_response = " ".join([
                content_block.text for step in interaction.steps if step.type == "model_output"
                for content_block in step.content if content_block.type == "text"
            ])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        # Continue conversation with function responses
        interaction = client.interactions.create(
            model='gemini-3.6-flash',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser",
                "enable_prompt_injection_detection": True
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

### JavaScript

```
import { chromium } from 'playwright';
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Constants for screen dimensions
const SCREEN_WIDTH = 1440;
const SCREEN_HEIGHT = 900;

console.log("Initializing browser...");
const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({
    viewport: { width: SCREEN_WIDTH, height: SCREEN_HEIGHT }
});
const page = await context.newPage();

// Define helper functions. Copy/paste from steps 3 and 4:
// function denormalizeX(...)
// function denormalizeY(...)
// async function executeFunctionCalls(...)
// async function getFunctionResponses(...)

try {
    // Go to initial page
    await page.goto("https://ai.google.dev/gemini-api/docs");

    // Take initial screenshot
    const initialScreenshotBuffer = await page.screenshot({ type: 'png' });
    const initialScreenshotBase64 = initialScreenshotBuffer.toString('base64');
    const USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
    console.log(`Goal: ${USER_PROMPT}`);

    // First interaction
    let interaction = await ai.interactions.create({
        model: 'gemini-3.6-flash',
        input: [
            { type: 'text', text: USER_PROMPT },
            { type: 'image', data: initialScreenshotBase64, mime_type: 'image/png' }
        ],
        tools: [{
            type: 'computer_use',
            environment: 'browser',
            enable_prompt_injection_detection: true
        }]
    });

    // Agent Loop
    const turnLimit = 5;
    for (let i = 0; i < turnLimit; i++) {
        console.log(`\n--- Turn ${i + 1} ---`);

        const hasFunctionCalls = interaction.steps.some(step => step.type === "function_call");
        if (!hasFunctionCalls) {
            const textResponses = [];
            for (const step of interaction.steps) {
                if (step.type === "model_output") {
                    for (const contentBlock of step.content || []) {
                        if (contentBlock.type === "text") {
                            textResponses.push(contentBlock.text);
                        }
                    }
                }
            }
            console.log("Agent finished:", textResponses.join(" "));
            break;
        }

        console.log("Executing actions...");
        const results = await executeFunctionCalls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT);

        console.log("Capturing state...");
        const functionResponses = await getFunctionResponses(page, results);

        // Continue conversation with function responses
        interaction = await ai.interactions.create({
            model: 'gemini-3.6-flash',
            previous_interaction_id: interaction.id,
            input: functionResponses,
            tools: [{
                type: 'computer_use',
                environment: 'browser',
                enable_prompt_injection_detection: true
            }]
        });
    }
} finally {
    // Cleanup
    console.log("\nClosing browser...");
    await browser.close();
}
```

## Các môi trường được hỗ trợ (Gemini 3.x)

Các mô hình Gemini 3.x hỗ trợ 3 môi trường được chỉ định trong cấu hình `computer_use`:

### Môi trường trình duyệt (`ENVIRONMENT_BROWSER`)

Các thao tác có thể thực hiện trong công cụ trình duyệt:

| Tên lệnh | Mô tả | Đối số (trong lệnh gọi hàm) |
| --- | --- | --- |
| **click** | Nhấp chuột trái vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Nhấp đúp vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Nhấp ba lần vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Nhấp chuột giữa vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Nhấp chuột phải vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Nhấn và giữ nút chuột tại toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Nhả nút chuột tại toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **move** | Di chuyển con trỏ đến vị trí đã chỉ định. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | Nhập văn bản. | `text`: str `press_enter`: bool (Không bắt buộc, mặc định là `false`) `intent`: str |
| **drag\_and\_drop** | Kéo một mục từ toạ độ bắt đầu đến toạ độ kết thúc. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | Tạm dừng thực thi trong một số giây được chỉ định. | `seconds`: int (Không bắt buộc, mặc định là `1`) `intent`: str |
| **press\_key** | Nhấn phím đã chỉ định rồi thả ra. | `key`: str `intent`: str |
| **key\_down** | Nhấn và giữ phím đã chỉ định. | `key`: str `intent`: str |
| **key\_up** | Nhả khoá đã chỉ định. | `key`: str `intent`: str |
| **phím tắt** | Nhấn tổ hợp phím đã chỉ định. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Trả về ảnh chụp màn hình hiện tại. | `intent`: str |
| **scroll** | Cuộn lên, xuống, sang trái hoặc sang phải tại một toạ độ theo khoảng cách pixel. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, Không bắt buộc, mặc định là `300`) `intent`: str |
| **go\_back** | Quay lại trang web trước đó trong nhật ký trình duyệt. | `intent`: str |
| **navigate** | Điều hướng trực tiếp đến một URL cụ thể. | `url`: str `intent`: str |
| **go\_forward** | Chuyển tiếp đến trang web tiếp theo trong nhật ký duyệt web. | `intent`: str |

### Môi trường di động (`ENVIRONMENT_MOBILE`)

Các thao tác trong môi trường được tối ưu hoá cho Android:

| Tên lệnh | Mô tả | Đối số (trong lệnh gọi hàm) |
| --- | --- | --- |
| **open\_app** | Mở một ứng dụng theo tên. | `app_name`: str `intent`: str |
| **click** | Nhấp chuột trái vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | Liệt kê các ứng dụng có trên thiết bị, trả về tên và tên gói của các ứng dụng đó. | `intent`: str |
| **wait** | Tạm dừng thực thi trong một số giây được chỉ định. | `seconds`: int (Không bắt buộc, mặc định là `1`) `intent`: str |
| **go\_back** | Quay lại màn hình hoặc trang web trước đó. | `intent`: str |
| **type** | Nhập văn bản. | `text`: str `press_enter`: bool (Không bắt buộc, mặc định là `false`) `intent`: str |
| **drag\_and\_drop** | Kéo một mục từ toạ độ bắt đầu đến toạ độ kết thúc. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | Thực hiện thao tác nhấn và giữ tại một toạ độ trên màn hình. | `y`: int (0-999) `x`: int (0-999) `seconds`: int (Không bắt buộc, mặc định là `2`) `intent`: str |
| **press\_key** | Nhấn phím đã chỉ định rồi thả ra. | `key`: str `intent`: str |
| **take\_screenshot** | Trả về ảnh chụp màn hình hiện tại. | `intent`: str |

### Môi trường máy tính (`ENVIRONMENT_DESKTOP`)

Các lệnh con trỏ ở cấp hệ điều hành của môi trường máy tính:

| Tên lệnh | Mô tả | Đối số (trong lệnh gọi hàm) |
| --- | --- | --- |
| **click** | Nhấp chuột trái vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Nhấp đúp vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Nhấp ba lần vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Nhấp chuột giữa vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Nhấp chuột phải vào toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Nhấn và giữ nút chuột tại toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Nhả nút chuột tại toạ độ. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **move** | Di chuyển con trỏ đến vị trí đã chỉ định. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **type** | Nhập văn bản. | `text`: str `press_enter`: bool (Không bắt buộc, mặc định là `false`) `intent`: str |
| **drag\_and\_drop** | Kéo một mục từ toạ độ bắt đầu đến toạ độ kết thúc. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **wait** | Tạm dừng thực thi trong một số giây được chỉ định. | `seconds`: int (Không bắt buộc, mặc định là `1`) `intent`: str |
| **press\_key** | Nhấn phím đã chỉ định rồi thả ra. | `key`: str `intent`: str |
| **key\_down** | Nhấn và giữ phím đã chỉ định. | `key`: str `intent`: str |
| **key\_up** | Nhả khoá đã chỉ định. | `key`: str `intent`: str |
| **phím tắt** | Nhấn tổ hợp phím đã chỉ định. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Trả về ảnh chụp màn hình hiện tại. | `intent`: str |
| **scroll** | Cuộn lên, xuống, sang trái hoặc sang phải tại một toạ độ theo khoảng cách pixel. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, Không bắt buộc, mặc định là `300`) `intent`: str |

## Các thao tác trên giao diện người dùng cũ được hỗ trợ (Gemini 2.5)

Đối với các mô hình cũ (`gemini-2.5-computer-use-preview-10-2025`), các thao tác sau được hỗ trợ:

| Tên lệnh | Mô tả | Đối số (trong lệnh gọi hàm) | Ví dụ về lệnh gọi hàm |
| --- | --- | --- | --- |
| **open\_web\_browser** | Mở trình duyệt web. | Không có | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | Tạm dừng thực thi trong 5 giây. | Không có | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | Chuyển đến trang trước trong nhật ký. | Không có | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | Chuyển đến trang tiếp theo trong nhật ký. | Không có | `{"name": "go_forward", "arguments": {}}` |
| **search** | Chuyển đến công cụ tìm kiếm mặc định. | Không có | `{"name": "search", "arguments": {}}` |
| **navigate** | Điều hướng trình duyệt trực tiếp đến URL đã chỉ định. | `url`: str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Nhấp vào một toạ độ cụ thể. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | Di chuột đến một toạ độ cụ thể. | `y`: int (0-999), `x`: int (0-999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Nhập văn bản tại một toạ độ. | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (Không bắt buộc, mặc định là True), `clear_before_typing`: bool (Không bắt buộc, mặc định là True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search", "press_enter": false}}` |
| **key\_combination** | Nhấn các phím hoặc tổ hợp phím. | `keys`: str | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | Cuộn toàn bộ trang web. | `direction`: str | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | Cuộn tại toạ độ (x,y). | `y`: int, `x`: int, `direction`: str, `magnitude`: int (Không bắt buộc, mặc định là 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down"}}` |
| **drag\_and\_drop** | Kéo giữa hai toạ độ. | `y`: int, `x`: int, `destination_y`: int, `destination_x`: int | `{"name": "drag_and_drop", "arguments": {"y": 100, "destination_y": 500, "destination_x": 500, "x": 100}}` |

## Hàm tuỳ chỉnh do người dùng xác định

Bạn có thể mở rộng chức năng của mô hình bằng cách thêm các hàm tuỳ chỉnh do người dùng xác định. Ví dụ: trong các trường hợp có sự tham gia của con người (HITL), bạn có thể loại trừ các thao tác được xác định trước theo mặc định và đăng ký các thao tác tuỳ chỉnh.

#### Công cụ tuỳ chỉnh Gemini 3.x

### Python

Loại trừ các thao tác tiêu chuẩn được xác định trước trên trình duyệt (chẳng hạn như `click`) và đăng ký một công cụ `yield_to_user` tuỳ chỉnh:

```
from google import genai

client = genai.Client()

yield_to_user_tool = {
    "type": "function",
    "name": "yield_to_user",
    "description": "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    "parameters": {
        "type": "object",
        "properties": {
            "reason": {
                "type": "string",
                "description": "The reason why the agent is yielding control to the human."
            }
        },
        "required": ["reason"]
    }
}

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Click the submit button. If you need a second factor authentication code, ask me.",
    tools=[
        {
            "type": "computer_use",
            "environment": "mobile",
            "excluded_predefined_functions": ["click"]
        },
        yield_to_user_tool
    ]
)
```

### JavaScript

Loại trừ các thao tác tiêu chuẩn được xác định trước trên trình duyệt (chẳng hạn như `click`) và đăng ký một công cụ `yield_to_user` tuỳ chỉnh:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const yieldToUserTool = {
    type: "function",
    name: "yield_to_user",
    description: "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    parameters: {
        type: "object",
        properties: {
            reason: {
                type: "string",
                description: "The reason why the agent is yielding control to the human."
            }
        },
        required: ["reason"]
    }
};

const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Click the submit button. If you need a second factor authentication code, ask me.",
    tools: [
        {
            type: "computer_use",
            environment: "mobile",
            excluded_predefined_functions: ["click"]
        },
        yieldToUserTool
    ]
});
```

#### Công cụ tuỳ chỉnh Gemini 2.5 (Phiên bản cũ)

### Python

```
from google import genai

client = genai.Client()

# Define custom tools here
custom_functions = [...]  # Describe parameters as function declarations

excluded_functions = [
    "open_web_browser",
    "wait_5_seconds",
    "go_back",
    "go_forward",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "key_combination",
    "drag_and_drop",
]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Open Chrome, then long-press at 200,400.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        },
        *custom_functions
    ]
)

print(interaction)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Define custom tools here
const customFunctions = [...]; // Describe parameters as function declarations

const excludedFunctions = [
    "open_web_browser",
    "wait_5_seconds",
    "go_back",
    "go_forward",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "key_combination",
    "drag_and_drop",
];

const interaction = await ai.interactions.create({
    model: 'gemini-2.5-computer-use-preview-10-2025',
    input: "Open Chrome, then long-press at 200,400.",
    tools: [
        {
            type: "computer_use",
            environment: "browser",
            excluded_predefined_functions: excludedFunctions
        },
        ...customFunctions
    ]
});

console.log(interaction);
```

## Quản lý cấp độ tư duy (Gemini 3.x)

Đối với các tác nhân sử dụng máy tính, bạn có thể định cấu hình các cấp độ tư duy khác nhau để cân bằng chất lượng hành động và tốc độ thực thi. Các cấp độ tư duy thấp hơn thường đạt được sự cân bằng tốt cho các tác vụ tự động hoá tiêu chuẩn.

## An toàn và bảo mật

### Định cấu hình chính sách an toàn (Gemini 3.x)

Các mô hình Gemini 3.x có các danh mục dịch vụ an toàn tích hợp sẵn để tự động xác định xem có cần người dùng xác nhận hay không.

| Danh mục chính sách an toàn | Mô tả |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | Chặn hoặc kích hoạt bước xác nhận cho các hành động liên quan đến khoản thanh toán, quy trình thanh toán bán lẻ hoặc hàng hoá thuộc diện quản lý. |
| `SENSITIVE_DATA_MODIFICATION` | Bảo vệ hồ sơ sức khoẻ, tài chính hoặc hồ sơ của chính phủ khỏi bị sửa đổi trái phép. |
| `COMMUNICATION_TOOL` | Hạn chế tác nhân tự động gửi email, tin nhắn trò chuyện hoặc bản nháp. |
| `ACCOUNT_CREATION` | Hạn chế tác nhân tự động đăng ký tài khoản mới trên các trang web. |
| `DATA_MODIFICATION` | Điều chỉnh các hoạt động sửa đổi hệ thống tệp tổng thể, chia sẻ dữ liệu và xoá bộ nhớ. |
| `USER_CONSENT_MANAGEMENT` | Yêu cầu người dùng tiếp quản biểu ngữ yêu cầu đồng ý sử dụng cookie và lời nhắc về quyền riêng tư. |
| `LEGAL_TERMS_AND_AGREEMENTS` | Ngăn mô hình tự động chấp nhận Điều khoản dịch vụ hoặc các hợp đồng ràng buộc pháp lý. |

#### Chế độ ghi đè an toàn

Bạn có thể ghi đè một số chính sách bằng cách truyền các giá trị ghi đè:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Clean up the local folder by archiving old logs.",
    tools=[
        {
            "type": "computer_use",
            "environment": "desktop",
            "disabled_safety_policies": [
                "data_modification"
            ]
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Clean up the local folder by archiving old logs.",
    tools: [
        {
            type: "computer_use",
            environment: "desktop",
            disabled_safety_policies: [
                "data_modification"
            ]
        }
    ]
});
```

### Phát hiện kỹ thuật tấn công "tiêm câu lệnh" (Gemini 3.x)

Cơ chế an toàn chọn tham gia quét các pixel ảnh chụp màn hình để tìm hướng dẫn ẩn của câu lệnh đối nghịch (ví dụ: "Bỏ qua các lệnh trước đó") và chặn thực thi khi phát hiện.

### Xác nhận quyết định về an toàn

Phản hồi có thể bao gồm một tham số `safety_decision` trong các đối số của lệnh gọi hàm:

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click_at",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "Must check check-box",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

Nếu `safety_decision` là `require_confirmation`, hãy nhắc người dùng cuối. Nếu người dùng xác nhận, hãy đặt `safety_acknowledgement` thành `function_result`.

### Python

```
def get_safety_confirmation(safety_decision):
    # Prompt user for confirmation
    print(f"Safety confirmation required: {safety_decision.get('explanation', '')}")
    return "CONTINUE" # Or TERMINATE

# Inside execute_function_calls, check for safety_decision:
if 'safety_decision' in function_call.arguments:
    decision = get_safety_confirmation(function_call.arguments['safety_decision'])
    if decision == "TERMINATE":
        break
    # Include safety_acknowledgement inside the action result
    action_result["safety_acknowledgement"] = True
```

### Các phương pháp hay nhất về an toàn

Việc sử dụng máy tính có thể gây ra những rủi ro riêng về bảo mật và hoạt động, vì một mô hình hành động thay cho người dùng có thể gặp phải nội dung không đáng tin cậy trên màn hình hoặc mắc lỗi khi thực hiện các hành động. Hãy triển khai các phương pháp hay nhất sau đây để bảo vệ dữ liệu và hệ thống của người dùng:

1. **Con người tham gia vào quy trình (HITL):**

   - **Thực thi xác nhận của người dùng:** Khi phản hồi về sự an toàn cho biết `require_confirmation` (hoặc quyết định an toàn cũ yêu cầu), hãy nhắc người dùng phê duyệt.
   - **Cung cấp hướng dẫn an toàn tuỳ chỉnh:** Triển khai một chỉ dẫn tuỳ chỉnh cho hệ thống để xác định và thực thi ranh giới an toàn của riêng bạn. Ví dụ:

     ### Python

     ```
     from google import genai

     client = genai.Client()

     system_instruction = """
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Completing any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     """

     interaction = client.interactions.create(
         model="gemini-3.6-flash",
         system_instruction=system_instruction,
         input="Prepare a draft but do not send.",
         tools=[{
             "type": "computer_use",
             "environment": "browser"
         }]
     )
     ```

     ### JavaScript

     ```
     import { GoogleGenAI } from '@google/genai';

     const ai = new GoogleGenAI();

     const systemInstruction = `
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Completing any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     `;

     const interaction = await ai.interactions.create({
         model: "gemini-3.6-flash",
         system_instruction: systemInstruction,
         input: "Prepare a draft but do not send.",
         tools: [{
             type: "computer_use",
             environment: "browser"
         }]
     });
     ```
2. **Môi trường thực thi an toàn:** Chạy tác nhân của bạn trong một môi trường an toàn, được đưa vào hộp cát để hạn chế tác động tiềm ẩn của tác nhân. Đây có thể là một máy ảo (VM) được cách ly, một vùng chứa (ví dụ: Docker) hoặc một hồ sơ trình duyệt chuyên dụng có quyền hạn chế. Hãy xem [hoạt động triển khai tham chiếu trên GitHub](https://github.com/google/computer-use-preview/) để biết hướng dẫn thiết lập hộp cát bằng Docker.
3. **Làm sạch dữ liệu đầu vào:** Làm sạch tất cả văn bản do người dùng tạo trong câu lệnh để giảm thiểu nguy cơ vô tình đưa ra hướng dẫn hoặc tiêm câu lệnh (prompt injection). Đây là một lớp bảo mật hữu ích, nhưng không thay thế được môi trường thực thi an toàn.
4. **Quy định hạn chế về nội dung:** Sử dụng các quy định hạn chế và API An toàn nội dung để đánh giá tính phù hợp của thông tin đầu vào của người dùng, thông tin đầu vào và đầu ra của công cụ, cũng như các câu trả lời của tác nhân, đồng thời phát hiện hành vi tiêm câu lệnh (prompt injection) và vượt qua các quy định hạn chế.
5. **Danh sách cho phép và danh sách chặn:** Triển khai cơ chế lọc để kiểm soát vị trí mà mô hình có thể điều hướng và những việc mà mô hình có thể làm. Danh sách chặn các trang web bị cấm là một điểm xuất phát tốt, trong khi danh sách cho phép hạn chế hơn sẽ an toàn hơn nữa.
6. **Khả năng quan sát và ghi nhật ký:** Duy trì nhật ký chi tiết để gỡ lỗi, kiểm tra và xử lý sự cố. Ứng dụng của bạn nên ghi lại các câu lệnh, ảnh chụp màn hình, hành động do mô hình đề xuất (`function_call`), phản hồi an toàn và tất cả các hành động mà cuối cùng ứng dụng thực hiện.
7. **Quản lý môi trường:** Đảm bảo môi trường GUI nhất quán.
   Cửa sổ bật lên, thông báo hoặc thay đổi bố cục không mong muốn có thể khiến mô hình bị nhầm lẫn. Nếu có thể, hãy bắt đầu từ một trạng thái sạch, đã biết cho mỗi tác vụ mới.

## Phiên bản mô hình

Bạn có thể sử dụng tính năng Sử dụng máy tính với các mẫu sau:

- [**Gemini 3.6 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=vi) (`gemini-3.6-flash`): Mô hình được đề xuất để sử dụng trên máy tính, có các hành động tinh giản theo ý định, hỗ trợ môi trường trình duyệt, thiết bị di động và máy tính, chính sách an toàn có thể định cấu hình và tính năng phát hiện hành vi chèn câu lệnh.
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=vi) (`gemini-3.5-flash-lite`): Một mô hình có độ trễ thấp, tiết kiệm chi phí và hỗ trợ việc sử dụng máy tính.
- [**Gemini 3.5 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) (`gemini-3.5-flash`): Mô hình ổn định trước đây hỗ trợ việc sử dụng máy tính.
- [**Bản dùng thử Gemini 3 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) (`gemini-3-flash-preview`): Mô hình dùng thử hỗ trợ việc sử dụng máy tính.
- [**Gemini 2.5 (Bản dùng thử cũ)**](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025?hl=vi) (`gemini-2.5-computer-use-preview-10-2025`): Mô hình dùng thử cũ được tối ưu hoá để sử dụng trên máy tính dựa trên trình duyệt.

## Bước tiếp theo

- Thử nghiệm với việc sử dụng máy tính trong [môi trường minh hoạ Browserbase](http://gemini.browserbase.com).
- Hãy xem [Triển khai tham chiếu](https://github.com/google/computer-use-preview) để biết mã ví dụ.
- Tìm hiểu về các công cụ khác của Gemini API:
  - [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)
  - [Neo bám vào Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-30 UTC."],[],[]]
