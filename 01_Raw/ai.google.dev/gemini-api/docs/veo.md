---
source_url: https://ai.google.dev/gemini-api/docs/veo?hl=zh-TW
fetched_at: 2026-10-26T05:57:17.500382+00:00
title: "\u5728 Gemini API \u4e2d\u4f7f\u7528 Veo 3.1 \u751f\u6210\u5f71\u7247 \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 在 Gemini API 中使用 Veo 3.1 生成影片

> 如要瞭解影片理解功能，請參閱[影片理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-tw)指南。

[Veo 3.1](https://deepmind.google/models/veo/?hl=zh-tw) 模型可生成 8 秒影片 (720p、1080p 或 4k)，並原生生成音訊。您可以使用 Gemini API，透過程式輔助方式存取這個模型。如要進一步瞭解可用的 Veo 模型變化版本，請參閱「[模型版本](#model-versions)」一節。

Veo 3.1 擅長處理各種視覺和電影風格，並推出多項新功能：

- **直式影片**：選擇橫向 (`16:9`) 或直式 (`9:16`) 影片。
- **影片擴充**：擴充先前使用 Veo 生成的影片。
- **指定影格生成**：指定第一個和最後一個影格來生成影片。
- **圖像引導**：最多可使用三張參考圖像，引導生成影片的內容。

如要進一步瞭解如何撰寫有效的文字提示詞來生成影片，請參閱 [Veo 提示詞指南](#prompt-guide)。

## 文字轉影片生成

以下範例說明如何生成[對話](#dialogue)、[電影寫實](#realism)或[創意動畫](#style)影片：

### 對話和音效

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

prompt = """A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'"""

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video, destination="dialogue_example.mp4")
print("Generated video saved to dialogue_example.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'`;

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "dialogue_example.mp4",
});
console.log(`Generated video saved to dialogue_example.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
    A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'`

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        nil,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "dialogue_example.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.GeneratedVideo;

Client client = new Client();

String prompt =
    "A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.\n"
        + "A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'";

GenerateVideosOperation operation =
    client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

// Poll the operation status until the video is ready.
while (!operation.done().orElse(false)) {
  System.out.println("Waiting for video generation to complete...");
  Thread.sleep(10000);
  operation = client.operations.getVideosOperation(operation, null);
}

// Download the generated video.
GeneratedVideo generatedVideo = operation.response().get().generatedVideos().get().get(0);
client.files.download(generatedVideo, "dialogue_example.mp4", null);
System.out.println("Generated video saved to dialogue_example.mp4");
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A close up of two people staring at a cryptic drawing on a wall, torchlight flickering. A man murmurs, \"This must be it. That'\''s the secret code.\" The woman looks at him and whispering excitedly, \"What did you find?\""
      }
    ]
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o dialogue_example.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

### 電影寫實風格

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

prompt = """Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.
The convertible accelerates fast and the engine roars loudly."""

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video, destination="realism_example.mp4")
print("Generated video saved to realism_example.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.
The convertible accelerates fast and the engine roars loudly.`;

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "realism_example.mp4",
});
console.log(`Generated video saved to realism_example.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.
  The convertible accelerates fast and the engine roars loudly.`

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        nil,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "realism_example.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.GeneratedVideo;

Client client = new Client();

String prompt =
    "Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.\n"
        + "The convertible accelerates fast and the engine roars loudly.";

GenerateVideosOperation operation =
    client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

// Poll the operation status until the video is ready.
while (!operation.done().orElse(false)) {
  System.out.println("Waiting for video generation to complete...");
  Thread.sleep(10000);
  operation = client.operations.getVideosOperation(operation, null);
}

// Download the generated video.
GeneratedVideo generatedVideo = operation.response().get().generatedVideos().get().get(0);
client.files.download(generatedVideo, "realism_example.mp4", null);
System.out.println("Generated video saved to realism_example.mp4");
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below. The convertible accelerates fast and the engine roars loudly."
      }
    ]
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o realism_example.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

### 創意動畫

### Python

```
import time
from google import genai

client = genai.Client()
prompt = "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet."

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video, destination="style_example.mp4")
print("Generated video saved to style_example.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet.";

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "style_example.mp4",
});
console.log(`Generated video saved to style_example.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet.`

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        nil,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "style_example.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.GeneratedVideo;

Client client = new Client();

String prompt =
    "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet.";

GenerateVideosOperation operation =
    client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

// Poll the operation status until the video is ready.
while (!operation.done().orElse(false)) {
  System.out.println("Waiting for video generation to complete...");
  Thread.sleep(10000);
  operation = client.operations.getVideosOperation(operation, null);
}

// Download the generated video.
GeneratedVideo generatedVideo = operation.response().get().generatedVideos().get().get(0);
client.files.download(generatedVideo, "style_example.mp4", null);
System.out.println("Generated video saved to style_example.mp4");
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet."
      }
    ]
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o style_example.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

## 控制顯示比例

Veo 3.1 可讓您建立橫向 (`16:9`，預設設定) 或直向 (`9:16`) 影片。您可以使用 `aspect_ratio` 參數，告訴模型要使用哪一個：

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

prompt = """A montage of pizza making: a chef tossing and flattening the floury dough, ladling rich red tomato sauce in a spiral, sprinkling mozzarella cheese and pepperoni, and a final shot of the bubbling golden-brown pizza, upbeat electronic music with a rhythmical beat is playing, high energy professional video."""

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    config=types.GenerateVideosConfig(
      aspect_ratio="9:16",
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video, destination="pizza_making.mp4")
print("Generated video saved to pizza_making.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `A montage of pizza making: a chef tossing and flattening the floury dough, ladling rich red tomato sauce in a spiral, sprinkling mozzarella cheese and pepperoni, and a final shot of the bubbling golden-brown pizza, upbeat electronic music with a rhythmical beat is playing, high energy professional video.`;

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
    config: {
      aspectRatio: "9:16",
    },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "pizza_making.mp4",
});
console.log(`Generated video saved to pizza_making.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `A montage of pizza making: a chef tossing and flattening the floury dough, ladling rich red tomato sauce in a spiral, sprinkling mozzarella cheese and pepperoni, and a final shot of the bubbling golden-brown pizza, upbeat electronic music with a rhythmical beat is playing, high energy professional video.`

  videoConfig := &genai.GenerateVideosConfig{
      AspectRatio: "9:16",
  }

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        videoConfig,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "pizza_making.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A montage of pizza making: a chef tossing and flattening the floury dough, ladling rich red tomato sauce in a spiral, sprinkling mozzarella cheese and pepperoni, and a final shot of the bubbling golden-brown pizza, upbeat electronic music with a rhythmical beat is playing, high energy professional video."
      }
    ],
    "parameters": {
      "aspectRatio": "9:16"
    }
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o pizza_making.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

## 控制解析度

Veo 3.1 也能直接生成 720p、1080p 或 4k 影片 (Veo 3.1 Lite 不支援 4k)。

請注意，解析度越高，延遲時間就越長。4K 影片的費用也較高 (請參閱[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw))。

[影片擴充功能](#extending-veo-videos)也僅限 720p 影片。

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

prompt = """A stunning drone view of the Grand Canyon during a flamboyant sunset that highlights the canyon's colors. The drone slowly flies towards the sun then accelerates, dives and flies inside the canyon."""

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    config=types.GenerateVideosConfig(
      resolution="4k",
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video, destination="4k_grand_canyon.mp4")
print("Generated video saved to 4k_grand_canyon.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `A stunning drone view of the Grand Canyon during a flamboyant sunset that highlights the canyon's colors. The drone slowly flies towards the sun then accelerates, dives and flies inside the canyon.`;

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
    config: {
      resolution: "4k",
    },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "4k_grand_canyon.mp4",
});
console.log(`Generated video saved to 4k_grand_canyon.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `A stunning drone view of the Grand Canyon during a flamboyant sunset that highlights the canyon's colors. The drone slowly flies towards the sun then accelerates, dives and flies inside the canyon.`

  videoConfig := &genai.GenerateVideosConfig{
      Resolution: "4k",
  }

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        videoConfig,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "4k_grand_canyon.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A stunning drone view of the Grand Canyon during a flamboyant sunset that highlights the canyon'\''s colors. The drone slowly flies towards the sun then accelerates, dives and flies inside the canyon."
      }
    ],
    "parameters": {
      "resolution": "4k"
    }
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o 4k_grand_canyon.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

## 以圖片生成影片

下列程式碼示範如何使用 [Gemini 3.1 Flash Image (又稱 Nano Banana 2)](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw) 生成圖片，然後將該圖片做為起始影格，使用 Veo 3.1 生成影片。

### Python

```
import time
from google import genai

client = genai.Client()

prompt = "Panning wide shot of a calico kitten sleeping in the sunshine"

# Step 1: Generate an image with Nano Banana 2.
image = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents=prompt,
    config={"response_modalities":['IMAGE']}
)

# Step 2: Generate video with Veo 3.1 using the image.
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    image=image.parts[0].as_image(),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video.
video = operation.response.generated_videos[0]
client.files.download(file=video.video, destination="veo3_with_image_input.mp4")
print("Generated video saved to veo3_with_image_input.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "Panning wide shot of a calico kitten sleeping in the sunshine";

// Step 1: Generate an image with Nano Banana 2.
const imageResponse = await ai.models.generateContent({
  model: "gemini-3.1-flash-image-preview",
  prompt: prompt,
});

// Step 2: Generate video with Veo 3.1 using the image.
let operation = await ai.models.generateVideos({
  model: "veo-3.1-generate-preview",
  prompt: prompt,
  image: {
    imageBytes: imageResponse.generatedImages[0].image.imageBytes,
    mimeType: "image/png",
  },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
  console.log("Waiting for video generation to complete...")
  await new Promise((resolve) => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({
    operation: operation,
  });
}

// Download the video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "veo3_with_image_input.mp4",
});
console.log(`Generated video saved to veo3_with_image_input.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Panning wide shot of a calico kitten sleeping in the sunshine"

    // Step 1: Generate an image with Nano Banana 2.
    imageResponse, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.1-flash-image-preview",
        prompt,
        nil, // GenerateImagesConfig
    )
    if err != nil {
        log.Fatal(err)
    }

    // Step 2: Generate video with Veo 3.1 using the image.
    operation, err := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        imageResponse.GeneratedImages[0].Image,
        nil, // GenerateVideosConfig
    )
    if err != nil {
        log.Fatal(err)
    }

    // Poll the operation status until the video is ready.
    for !operation.Done {
        log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "veo3_with_image_input.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Blob;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.GeneratedVideo;
import com.google.genai.types.Image;

Client client = new Client();

String prompt = "Panning wide shot of a calico kitten sleeping in the sunshine";

// Step 1: Generate an image with Nano Banana 2.
GenerateContentResponse imageResponse =
    client.models.generateContent(
        "gemini-3.1-flash-image-preview",
        prompt,
        GenerateContentConfig.builder().responseModalities("IMAGE").build());

Blob inlineData = imageResponse.parts().get(0).inlineData().get();
Image image =
    Image.builder()
        .imageBytes(inlineData.data().get())
        .mimeType(inlineData.mimeType().orElse("image/png"))
        .build();

// Step 2: Generate video with Veo 3.1 using the image.
GenerateVideosOperation operation =
    client.models.generateVideos("veo-3.1-generate-preview", prompt, image, null);

// Poll the operation status until the video is ready.
while (!operation.done().orElse(false)) {
  System.out.println("Waiting for video generation to complete...");
  Thread.sleep(10000);
  operation = client.operations.getVideosOperation(operation, null);
}

// Download the video.
GeneratedVideo video = operation.response().get().generatedVideos().get().get(0);
client.files.download(video, "veo3_with_image_input.mp4", null);
System.out.println("Generated video saved to veo3_with_image_input.mp4");
```

### 使用參考圖像

Veo 3.1 現在最多可接受 3 張參考圖像，引導生成影片的內容。提供人物、角色或產品的圖片，在輸出影片中保留主體的外觀。

舉例來說，使用 [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw) 生成的三張圖片做為參考，並搭配[精心撰寫的提示](#use-reference-images)，即可生成下列影片：

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| 時尚紅鶴洋裝，有多層粉紅色和紫紅色羽毛 | 美麗的女子，有著深色頭髮和暖棕色眼睛 | 奇幻粉紅色心形太陽眼鏡 |

### Python

```
import time
from google import genai

client = genai.Client()

prompt = "The video opens with a medium, eye-level shot of a beautiful woman with dark hair and warm brown eyes. She wears a magnificent, high-fashion flamingo dress with layers of pink and fuchsia feathers, complemented by whimsical pink, heart-shaped sunglasses. She walks with serene confidence through the crystal-clear, shallow turquoise water of a sun-drenched lagoon. The camera slowly pulls back to a medium-wide shot, revealing the breathtaking scene as the dress's long train glides and floats gracefully on the water's surface behind her. The cinematic, dreamlike atmosphere is enhanced by the vibrant colors of the dress against the serene, minimalist landscape, capturing a moment of pure elegance and high-fashion fantasy."

dress_reference = types.VideoGenerationReferenceImage(
  image=dress_image, # Generated separately with Nano Banana
  reference_type="asset"
)

sunglasses_reference = types.VideoGenerationReferenceImage(
  image=glasses_image, # Generated separately with Nano Banana
  reference_type="asset"
)

woman_reference = types.VideoGenerationReferenceImage(
  image=woman_image, # Generated separately with Nano Banana
  reference_type="asset"
)

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    config=types.GenerateVideosConfig(
      reference_images=[dress_reference, glasses_reference, woman_reference],
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video.
video = operation.response.generated_videos[0]
client.files.download(file=video.video, destination="veo3.1_with_reference_images.mp4")
print("Generated video saved to veo3.1_with_reference_images.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "The video opens with a medium, eye-level shot of a beautiful woman with dark hair and warm brown eyes. She wears a magnificent, high-fashion flamingo dress with layers of pink and fuchsia feathers, complemented by whimsical pink, heart-shaped sunglasses. She walks with serene confidence through the crystal-clear, shallow turquoise water of a sun-drenched lagoon. The camera slowly pulls back to a medium-wide shot, revealing the breathtaking scene as the dress's long train glides and floats gracefully on the water's surface behind her. The cinematic, dreamlike atmosphere is enhanced by the vibrant colors of the dress against the serene, minimalist landscape, capturing a moment of pure elegance and high-fashion fantasy.";

// dressImage, glassesImage, womanImage generated separately with Nano Banana
// and available as objects like { imageBytes: "...", mimeType: "image/png" }
const dressReference = {
  image: dressImage,
  referenceType: "asset",
};
const sunglassesReference = {
  image: glassesImage,
  referenceType: "asset",
};
const womanReference = {
  image: womanImage,
  referenceType: "asset",
};

let operation = await ai.models.generateVideos({
  model: "veo-3.1-generate-preview",
  prompt: prompt,
  config: {
    referenceImages: [
      dressReference,
      sunglassesReference,
      womanReference,
    ],
  },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
  console.log("Waiting for video generation to complete...");
  await new Promise((resolve) => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({
    operation: operation,
  });
}

// Download the video.
ai.files.download({
  file: operation.response.generatedVideos[0].video,
  downloadPath: "veo3.1_with_reference_images.mp4",
});
console.log(`Generated video saved to veo3.1_with_reference_images.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

  prompt := `The video opens with a medium, eye-level shot of a beautiful woman with dark hair and warm brown eyes. She wears a magnificent, high-fashion flamingo dress with layers of pink and fuchsia feathers, complemented by whimsical pink, heart-shaped sunglasses. She walks with serene confidence through the crystal-clear, shallow turquoise water of a sun-drenched lagoon. The camera slowly pulls back to a medium-wide shot, revealing the breathtaking scene as the dress's long train glides and floats gracefully on the water's surface behind her. The cinematic, dreamlike atmosphere is enhanced by the vibrant colors of the dress against the serene, minimalist landscape, capturing a moment of pure elegance and high-fashion fantasy.`

  // dressImage, glassesImage, womanImage generated separately with Nano Banana
  // and available as *genai.Image objects.
  var dressImage, glassesImage, womanImage *genai.Image

  dressReference := &genai.VideoGenerationReferenceImage{
    Image: dressImage,
    ReferenceType: "asset",
  }
  sunglassesReference := &genai.VideoGenerationReferenceImage{
    Image: glassesImage,
    ReferenceType: "asset",
  }
  womanReference := &genai.VideoGenerationReferenceImage{
    Image: womanImage,
    ReferenceType: "asset",
  }

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
    nil, // image
        &genai.GenerateVideosConfig{
      ReferenceImages: []*genai.VideoGenerationReferenceImage{
        dressReference,
        sunglassesReference,
        womanReference,
      },
    },
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
        log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "veo3.1_with_reference_images.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# It assumes dress_image_base64, glasses_image_base64, and woman_image_base64
# contain base64-encoded image data.

# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
      "prompt": "The video opens with a medium, eye-level shot of a beautiful woman with dark hair and warm brown eyes. She wears a magnificent, high-fashion flamingo dress with layers of pink and fuchsia feathers, complemented by whimsical pink, heart-shaped sunglasses. She walks with serene confidence through the crystal-clear, shallow turquoise water of a sun-drenched lagoon. The camera slowly pulls back to a medium-wide shot, revealing the breathtaking scene as the dress'\''s long train glides and floats gracefully on the water'\''s surface behind her. The cinematic, dreamlike atmosphere is enhanced by the vibrant colors of the dress against the serene, minimalist landscape, capturing a moment of pure elegance and high-fashion fantasy.",
      "referenceImages": [
        {
          "image": {"inlineData": {"mimeType": "image/png", "data": "'"$dress_image_base64"'"}},
          "referenceType": "asset"
        },
        {
          "image": {"inlineData": {"mimeType": "image/png", "data": "'"$glasses_image_base64"'"}},
          "referenceType": "asset"
        },
        {
          "image": {"inlineData": {"mimeType": "image/png", "data": "'"$woman_image_base64"'"}},
          "referenceType": "asset"
        }
      ]
    }],
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o veo3.1_with_reference_images.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 10 seconds before checking again.
  sleep 10
done
```

### 使用初始和結束影格

Veo 3.1 可讓您使用內插法，或指定影片的第一個和最後一個影格，來建立影片。如要瞭解如何撰寫有效的文字提示詞來生成影片，請參閱 [Veo 提示詞指南](#use-reference-images)。

### Python

```
import time
from google import genai

client = genai.Client()

prompt = "A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence."

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    image=first_image, # The starting frame is passed as a primary input
    config=types.GenerateVideosConfig(
      last_frame=last_image # The ending frame is passed as a generation constraint in the config
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video.
video = operation.response.generated_videos[0]
client.files.download(file=video.video, destination="veo3.1_with_interpolation.mp4")
print("Generated video saved to veo3.1_with_interpolation.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence.";

// firstImage and lastImage generated separately with Nano Banana
// and available as objects like { imageBytes: "...", mimeType: "image/png" }
let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
    image: firstImage, // The starting frame is passed as a primary input
    config: {
      lastFrame: lastImage, // The ending frame is passed as a generation constraint in the config
    },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "veo3.1_with_interpolation.mp4",
});
console.log(`Generated video saved to veo3.1_with_interpolation.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

  prompt := `A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence.`

  // firstImage and lastImage generated separately with Nano Banana
  // and available as *genai.Image objects.
  var firstImage, lastImage *genai.Image

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
    firstImage, // The starting frame is passed as a primary input
        &genai.GenerateVideosConfig{
      LastFrame: lastImage, // The ending frame is passed as a generation constraint in the config
    },
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
        log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "veo3.1_with_interpolation.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# It assumes first_image_base64 and last_image_base64
# contain base64-encoded image data.

# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
# The starting frame is passed as a primary input
# The ending frame is passed as a generation constraint in the config
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
      "prompt": "A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence.",
      "image": {"inlineData": {"mimeType": "image/png", "data": "'"$first_image_base64"'"}},
      "lastFrame": {"inlineData": {"mimeType": "image/png", "data": "'"$last_image_base64"'"}}
    }],
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o veo3.1_with_interpolation.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 10 seconds before checking again.
  sleep 10
done
```

| `` `first_image` `` | `` `last_image` `` | *veo3.1\_with\_interpolation.mp4* |
| --- | --- | --- |
| 一位留著白色長髮、身穿飄逸洋裝的幽靈女子，輕輕地在繩索鞦韆上搖擺 | 女鬼從鞦韆上消失 | 電影風格的驚悚影片，一名詭異女子在霧中從鞦韆上消失 |

## 延長 Veo 影片

使用 Veo 3.1，可將先前用 Veo 生成的影片延長 7 秒，最多可延長 20 次。

輸入影片限制：

- Veo 生成的影片長度上限為 141 秒。
- Gemini API 僅支援 Veo 生成影片的影片擴充功能。
- 影片應來自上一代，例如
  `operation.response.generated_videos[0].video`
- 影片會儲存 2 天，但如果影片用於擴充，2 天的儲存計時器會重設。只能延長過去兩天內生成或參考的影片。
- 輸入影片應符合特定長度、顯示比例和尺寸：
  - 顯示比例：9:16 或 16:9
  - 解析度：720p
  - 影片長度：141 秒以下

擴充功能的輸出內容是單一影片，結合了使用者輸入的影片和生成的擴充影片，長度最多 148 秒。

以下範例使用 Veo 生成的影片 (此處顯示原始提示)，並使用 `video` 參數和新提示擴充影片：

| 提示詞 | 輸出：`butterfly_video` |
| --- | --- |
| 一隻摺紙蝴蝶拍動翅膀，飛出落地門，進入花園。 | 摺紙蝴蝶拍動翅膀，飛出落地窗進入花園。 |

### Python

```
import time
from google import genai

client = genai.Client()

prompt = "Track the butterfly into the garden as it lands on an orange origami flower. A fluffy white puppy runs up and gently pats the flower."

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    video=operation.response.generated_videos[0].video, # This must be a video from a previous generation
    prompt=prompt,
    config=types.GenerateVideosConfig(
        number_of_videos=1,
        resolution="720p"
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video.
video = operation.response.generated_videos[0]
client.files.download(file=video.video, destination="veo3.1_extension.mp4")
print("Generated video saved to veo3.1_extension.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "Track the butterfly into the garden as it lands on an orange origami flower. A fluffy white puppy runs up and gently pats the flower.";

// butterflyVideo must be a video from a previous generation
// available as an object like { videoBytes: "...", mimeType: "video/mp4" }
let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    video: butterflyVideo,
    prompt: prompt,
    config: {
        numberOfVideos: 1,
        resolution: "720p",
    },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "veo3.1_extension.mp4",
});
console.log(`Generated video saved to veo3.1_extension.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

  prompt := `Track the butterfly into the garden as it lands on an orange origami flower. A fluffy white puppy runs up and gently pats the flower.`

  // butterflyVideo must be a video from a previous generation
  // available as a *genai.Video object.
  var butterflyVideo *genai.Video

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
    nil, // image
    butterflyVideo,
        &genai.GenerateVideosConfig{
      NumberOfVideos: 1,
      Resolution: "720p",
    },
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
        log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "veo3.1_extension.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# It assumes butterfly_video_base64 contains base64-encoded
# video data from a previous generation.

# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
      "prompt": "Track the butterfly into the garden as it lands on an orange origami flower. A fluffy white puppy runs up and gently pats the flower.",
      "video": {"inlineData": {"mimeType": "video/mp4", "data": "'"$butterfly_video_base64"'"}}
    }],
    "parameters": {
      "numberOfVideos": 1,
      "resolution": "720p"
    }
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o veo3.1_extension.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 10 seconds before checking again.
  sleep 10
done
```

如要瞭解如何撰寫有效的文字提示詞來生成影片，請參閱 [Veo 提示詞指南](#extend-prompt)。

## 處理非同步作業

影片生成需要大量運算資源。向 API 傳送要求時，API 會啟動長時間執行的工作，並立即傳回 `operation` 物件。接著，您必須輪詢，直到影片準備就緒 (`done` 狀態為 true)。

這項程序的核心是輪詢迴圈，會定期檢查工作狀態。

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

# After starting the job, you get an operation object.
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="A cinematic shot of a majestic lion in the savannah.",
)

# Alternatively, you can use operation.name to get the operation.
operation = types.GenerateVideosOperation(name=operation.name)

# This loop checks the job status every 10 seconds.
while not operation.done:
    time.sleep(10)
    # Refresh the operation object to get the latest status.
    operation = client.operations.get(operation)

# Once done, the result is in operation.response.
# ... process and download your video ...
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// After starting the job, you get an operation object.
let operation = await ai.models.generateVideos({
  model: "veo-3.1-generate-preview",
  prompt: "A cinematic shot of a majestic lion in the savannah.",
});

// Alternatively, you can use operation.name to get the operation.
// operation = types.GenerateVideosOperation(name=operation.name)

// This loop checks the job status every 10 seconds.
while (!operation.done) {
    await new Promise((resolve) => setTimeout(resolve, 1000));
    // Refresh the operation object to get the latest status.
    operation = await ai.operations.getVideosOperation({ operation });
}

// Once done, the result is in operation.response.
// ... process and download your video ...
```

### Go

```
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // After starting the job, you get an operation object.
    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        "A cinematic shot of a majestic lion in the savannah.",
        nil,
        nil,
    )

    // This loop checks the job status every 10 seconds.
    for !operation.Done {
        time.Sleep(10 * time.Second)
        // Refresh the operation object to get the latest status.
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Once done, the result is in operation.Response.
    // ... process and download your video ...
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;

Client client = new Client();

// After starting the job, you get an operation object.
GenerateVideosOperation operation =
    client.models.generateVideos(
        "veo-3.1-generate-preview",
        "A cinematic shot of a majestic lion in the savannah.",
        null,
        null);

// Alternatively, you can use operation.name to construct the operation.
operation = GenerateVideosOperation.builder().name(operation.name().get()).build();

// This loop checks the job status every 10 seconds.
while (!operation.done().orElse(false)) {
  Thread.sleep(10000);
  // Refresh the operation object to get the latest status.
  operation = client.operations.getVideosOperation(operation, null);
}

// Once done, the result is in operation.response().
// ... process and download your video ...
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A cinematic shot of a majestic lion in the savannah."
      }
    ]
  }' | jq -r .name)

# This loop checks the job status every 10 seconds.
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Once done, the result is in status_response.
    # ... process and download your video ...
    echo "Video generation complete."
    break
  fi
  # Wait for 10 seconds before checking again.
  echo "Waiting for video generation to complete..."
  sleep 10
done
```

## Veo API 參數和規格

您可以在 API 要求中設定這些參數，控管影片生成程序。

| 參數 | Veo 3.1 和 Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 和 Veo 3 Fast |
| --- | --- | --- | --- |
| 執行個體 | | | |
| `prompt`： 影片的文字說明。支援音訊提示。 | `string` | `string` | `string` |
| `image`： 要製作動畫的初始圖片。 | `Image` 個物件 | `Image` 個物件 | `Image` 個物件 |
| `lastFrame`： 插補影片轉換的最終圖片。必須與 `image` 參數搭配使用。 | `Image` 個物件 | `Image` 個物件 | `Image` 個物件 |
| `referenceImages`： 最多可提供三張圖片，做為風格和內容參考。 | `VideoGenerationReferenceImage` 個物件 | `n/a` 個物件 | 不適用 |
| `video`： 用於影片額外資訊的影片。 | `Video` 個舊版物件 | 不適用 | 不適用 |
| 參數 | | | |
| `aspectRatio`： 影片的顯示比例。 | `"16:9"` (預設)、 `"9:16"` | `"16:9"` (預設)、 `"9:16"` | `"16:9"` (預設)、 `"9:16"` |
| `durationSeconds`： 生成影片的長度。 | `"4"`，`"6"`，`"8"`。   *使用擴充功能、參考圖像或 1080p 和 4k 解析度時，必須為「8」* | `"4"`，`"6"`，`"8"`。   *使用參考圖像或 1080p 時，必須設為「8」* | `"4"`，`"6"`，`"8"`。   *使用擴充功能、參考圖像或 1080p 和 4k 解析度時，必須為「8」* |
| `personGeneration`： 控制人物生成。(如要瞭解區域限制，請參閱「[限制](#limitations)」一節) | 文字轉影片和擴展： `"allow_all"`僅限   圖片轉影片、插值和參考圖像： `"allow_adult"`僅限 | 文字轉影片：僅限  `"allow_all"`   圖像轉影片、插值和參考圖像：僅限  `"allow_adult"` | 文字轉影片：僅限  `"allow_all"`   圖像轉影片：僅限  `"allow_adult"` |
| `resolution`： 影片解析度。 | `"720p"` (預設)、 `"1080p"` (僅支援 8 秒長度)、 `"4k"` (僅支援 8 秒長度)   *`"720p"` 僅適用於擴充功能* | `"720p"` (預設)、 `"1080p"` (僅支援 8 秒) | `"720p"` (預設)、 `"1080p"` (僅支援 8 秒長度)、 `"4k"` (僅支援 8 秒長度)   *`"720p"` 僅適用於擴充功能* |

請注意，`seed` 參數也適用於 Veo 3 模型。這項設定無法保證確定性，但能稍微提升。

## 模型功能

| 功能 | Veo 3.1 和 Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 和 Veo 3 Fast |
| --- | --- | --- | --- |
| **音訊：** 原生生成影片音訊。 | ✔️ 一律開啟 | ✔️ 一律開啟 | ✔️ 一律開啟 |
| **輸入模態：** 用於生成的輸入類型。 | 文字轉影片、圖像轉影片、影片轉影片 | 文字轉影片、圖像轉影片 | 文字轉影片、圖像轉影片 |
| **解析度：** 影片的輸出解析度。 | 720p、1080p (僅限 8 秒長度)、4k (僅限 8 秒長度)  *使用影片增補功能時，僅限 720p。* | 720p、1080p (僅限 8 秒長度) | 720p 和 1080p (僅限 16:9) |
| **影格率：** 影片的輸出影格率。 | 24fps | 24fps | 24fps |
| **影片長度：** 生成的影片長度。 | 8 秒、6 秒、4 秒  *只有在 1080p 或 4k 或使用參考圖像時，才能選擇 8 秒* | 8 秒、6 秒、4 秒  *只有 1080p 或使用參考圖像時，才能生成 8 秒影片* | 8 秒 |
| **每次要求的影片數量：** 每次要求生成的影片數量。 | 1 | 1 | 1 |
| **狀態：** 模型可用性 | [預覽](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#preview) | [預覽](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#preview) | [穩定](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#stable) |

## 限制

- **多影片提示：**目前不支援參照或推論多部影片。如果嘗試使用多部影片提示，可能會導致模型效能降低或輸出非預期內容。
- **語言支援：**完整支援英文 (EN)，但尚未評估其他語言，因此可能可以使用，但結果可能不盡相同。
- **要求延遲時間：**最短 11 秒，最長 6 分鐘 (尖峰時段)。
- **區域限制：**在歐盟、英國、瑞士、中東與北非地區，`personGeneration` 只能使用 `allow_adult` 值。
- **影片保留：**生成的影片會在伺服器上保留 2 天，之後就會移除。如要儲存本機副本，請在影片生成後 2 天內下載。延長的影片會視為新生成的影片。
- **浮水印：**Veo 製作的影片會使用 [SynthID](https://deepmind.google/technologies/synthid/?hl=zh-tw) 加上浮水印，這是我們用於辨識 AI 生成內容並加上浮水印的工具。您可以使用 [SynthID](https://deepmind.google/science/synthid/?hl=zh-tw) 驗證平台驗證影片。
- **安全性：**生成的影片會經過安全篩選器和記憶檢查程序，有助於降低隱私、著作權和偏誤風險。
- **音訊錯誤：**Veo 3.1 有時會因安全篩選器或其他音訊處理問題，而無法生成影片。如果影片無法生成，我們不會向你收費。

## Veo 提示詞指南

本節提供 Veo 製作的影片範例，並說明如何修改提示來產生不同結果。

### 安全篩選機制

Veo 會在 Gemini 中套用安全篩選器，確保生成的影片和上傳的相片不含令人反感的內容。違反[條款和規範](https://ai.google.dev/gemini-api/docs/usage-policies?hl=zh-tw#abuse-monitoring)的提示會遭到封鎖。

### 提示詞撰寫基本概念

好的提示詞應清楚明確，如要充分發揮 Veo 的效益，請先找出核心構想，然後加入關鍵字和修飾詞來精進構想，並在提示中加入影片專屬術語。

提示應包含下列元素：

- **主體**：影片中要呈現的物體、人物、動物或風景，例如*城市景觀*、*自然*、*車輛*或*小狗*。
- **動作**：主體正在做什麼 (例如*走路*、*跑步*或*轉頭*)。
- **風格**：使用特定電影風格關鍵字指定廣告素材方向，例如*科幻*、*恐怖電影*、*黑色電影*，或*卡通*等動畫風格。
- **攝影機位置和動作**：[選用] 使用「鳥瞰圖」、「平視」、「俯拍」、「推軌鏡頭」或「仰拍」等字詞，控制攝影機的位置和動作。
- **構圖**：[選用] 取景方式，例如*廣角*、*特寫*、*單人鏡頭*或*雙人鏡頭*。
- **對焦和鏡頭效果**：[選用] 使用*淺景深*、*深景深*、*柔焦*、*微距鏡頭*和*廣角鏡頭*等字詞，達到特定視覺效果。
- **環境光源**：[選用] 色彩和光線如何營造場景氣氛，例如*藍色調*、*夜晚*或*暖色調*。

#### 更多撰寫提示的訣竅

- **使用描述性語言**：使用形容詞和副詞，為 Veo 描繪清晰的畫面。
- **強化臉部細節**：在提示中使用「*肖像*」等字詞，指定臉部細節為相片焦點。

*如需更全面的提示策略，請參閱「[提示設計簡介](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-tw)」。*

### 提示音訊

你可以提供 Veo 音效、環境噪音和對話的提示。
模型會擷取這些線索的細微差異，生成同步的音軌。

- **對話：**使用引號標示特定語音。(例如：他喃喃自語：「這一定是鑰匙。」)
- **音效 (SFX)：**明確描述音效。(例如：輪胎發出刺耳的摩擦聲、引擎轟鳴聲)。
- **環境噪音：**描述環境的音景。(範例：背景傳來微弱、詭異的嗡嗡聲。)

這些影片示範如何使用 Veo 3 的音訊生成功能，逐步增加提示的詳細程度。

| **提示詞** | **生成的內容** |
| --- | --- |
| **更多細節 (對話和環境音)** 遠景鏡頭，呈現霧氣繚繞的美國西北太平洋森林。一對男女登山客疲憊地穿過蕨類植物，男子突然停下腳步，盯著一棵樹。特寫：樹皮上有新鮮、深陷的爪痕。男子：(手放在獵刀上)「那不是普通的熊。」女子：(聲音因恐懼而緊繃，掃視著樹林)「那是什麼？」粗糙的樹皮、折斷的樹枝、踩在潮濕泥土上的腳步聲。一隻鳥在鳴叫。 | 兩人在林中發現熊的蹤跡。 |
| **細節較少 (對話)** 剪紙動畫。新圖書館員：「禁書放在哪裡？」老館長：「我們不這麼做。他們會留住我們。」 | 動畫：圖書館員討論禁書 |

歡迎親自試試這些提示詞，聆聽生成的音訊！
[試用 Veo](https://deepmind.google/models/veo/?hl=zh-tw)

### 使用參考圖像提示

您可以使用 Veo 的[圖片轉影片](https://ai.google.dev/gemini-api/docs/veo?hl=zh-tw#generate-from-images)功能，輸入一或多張圖片，引導生成影片。Veo 會將輸入的圖片當做初始影格。選取最接近您構想的圖片，做為影片的第一個場景，為日常物品加上動畫、讓繪畫和畫作栩栩如生，並為自然場景加入動作和音效。

| **提示詞** | **生成的內容** |
| --- | --- |
| **輸入圖像 (由 Nano Banana 生成)** 一張超逼真的微距相片，呈現迷你衝浪者在古樸石製浴室洗手台內衝浪。復古黃銅水龍頭流出水，形成永不停止的海浪。超現實、異想天開、明亮的自然光。 | 在質樸的石製浴室洗手台內，有微型衝浪者在海浪中衝浪。 |
| **輸出影片 (由 Veo 3.1 生成)** 超現實的電影級微距影片。石製浴室洗手台內，小小的衝浪者在不斷翻滾的波浪中衝浪。復古黃銅水龍頭流出的水，形成無盡的海浪。攝影機緩慢平移，捕捉陽光普照的奇幻場景，微型人物則熟練地在碧綠的海水中衝浪。 | 在浴室洗手台裡，小小的衝浪者在波浪中穿梭。 |

Veo 3.1 可讓您[參考圖像](https://ai.google.dev/gemini-api/docs/veo?hl=zh-tw#reference-images)或材料，引導生成影片的內容。最多提供三張素材圖片，呈現同一個人、角色或產品。Veo 會在輸出影片中保留主體的外觀。

| **提示詞** | **生成的內容** |
| --- | --- |
| **參考圖像 (由 Nano Banana 生成)** 一隻深海鮟鱇魚潛伏在黑暗的深水中，露出牙齒，發光的誘餌。 | 發光的深色鮟鱇魚 |
| **參考圖像 (由 Nano Banana 生成)** 粉紅色兒童公主服裝，附有魔杖和皇冠，背景為素色產品背景。 | 兒童粉紅色公主服裝 |
| **輸出影片 (由 Veo 3.1 生成)** 製作一個搞笑的卡通版本，呈現魚穿著服裝、游泳並揮舞魔杖的畫面。 | 穿著公主服裝的鮟鱇魚 |

使用 Veo 3.1 時，您也可以指定影片的[第一和最後一個影格](https://ai.google.dev/gemini-api/docs/veo?hl=zh-tw#using-first-and-last-video-frames)來生成影片。

| **提示詞** | **生成的內容** |
| --- | --- |
| **第一張圖片 (由 Nano Banana 生成)** 一張高畫質的寫實正面圖片，呈現一隻橘貓在法國蔚藍海岸駕駛紅色敞篷賽車。 | 一隻橘貓駕駛紅色敞篷賽車 |
| **最後一張圖片 (由 Nano Banana 生成)** 呈現車子從懸崖飛出的畫面。 | 一隻橘貓開著紅色敞篷車衝下懸崖 |
| **輸出影片 (由 Veo 3.1 生成)** 選用 | 貓咪開車衝下懸崖，飛向天空 |

這項功能可讓你定義起始和結束影格，精確控制鏡頭構圖。上傳圖片或使用先前生成的影片影格，確保場景的開頭和結尾完全符合您的構想。

### 提示擴充

如要使用 Veo 3.1 [延長](https://ai.google.dev/gemini-api/docs/veo?hl=zh-tw#extending-veo-videos) Veo 生成的影片 (不適用於 Veo 3.1 Lite)，請將影片做為輸入內容，並視需要加入文字提示詞。「延伸」會完成影片的最後一秒或 24 個影格，並繼續動作。

請注意，如果影片最後 1 秒沒有語音，就無法有效延續語音。

| **提示詞** | **生成的內容** |
| --- | --- |
| **輸入影片 (由 Veo 3.1 生成)** 滑翔傘從山頂起飛，開始滑翔下山，俯瞰下方開滿鮮花的山谷。 | 滑翔傘從山頂起飛 |
| **輸出影片 (由 Veo 3.1 生成)** 延伸這部影片，讓滑翔傘緩緩降落。 | 滑翔傘從山頂起飛，然後緩緩降落 |

### 提示詞和輸出內容範例

本節提供幾個提示，說明如何透過描述性細節提升每部影片的成果。

#### 冰柱

這部影片示範如何在提示中使用[提示撰寫基本概念](#basics)的元素。

| **提示詞** | **生成的內容** |
| --- | --- |
| 冰凍岩壁 (背景) 上融化冰柱 (主體) 的特寫鏡頭 (構圖)，冷色調藍色 (氛圍)，放大 (相機動作) 保持水滴的特寫細節 (動作)。 | 藍色背景，有滴水的冰柱。 |

#### 男子講電話

這些影片示範如何逐步加入更具體的細節，修改提示詞，讓 Veo 根據你的喜好調整輸出內容。

| **提示詞** | **生成的內容** |
| --- | --- |
| **減少細節** 鏡頭推近，特寫一名身穿綠色風衣的絕望男子。他正在使用綠色霓虹燈光的旋轉撥號壁掛式電話。看起來就像電影場景。 | 男子正在講電話。 |
| **更多細節** 電影風格的特寫鏡頭跟著一名身穿破舊綠色風衣的絕望男子，他正在撥打掛在粗糙磚牆上的轉盤電話，沐浴在綠色霓虹燈招牌的詭異光芒中。攝影機向前推軌，呈現他緊繃的下巴和絕望的神情，凸顯他撥打電話時的掙扎。淺景深效果聚焦於他緊皺的眉頭和黑色轉盤電話，背景模糊成一片霓虹色彩和模糊陰影，營造出緊迫感和孤立感。 | 男子講電話 |

#### 雪豹

| **提示詞** | **生成的內容** |
| --- | --- |
| **簡單提示：** 一隻可愛的生物，身上有雪豹般的毛皮，在冬天的森林中行走，3D 卡通風格渲染。 | 雪豹無精打采。 |
| **詳細提示：** 製作一部 3D 動畫短片，風格為歡樂的卡通風。一隻可愛的生物，有著雪豹般的毛皮、大而有神的眼睛，以及友善圓潤的身形，在奇幻的冬季森林中快樂地蹦蹦跳跳。場景應包含圓潤的積雪樹木、輕柔飄落的雪花，以及穿透樹枝的溫暖陽光。生物的彈跳動作和燦爛笑容應傳達純粹的喜悅。語氣應歡快溫馨，並搭配明亮愉悅的色彩和俏皮的動畫。 | 雪豹跑得更快了。 |

### 寫作元素範例

以下範例說明如何根據各項基本元素調整提示。

#### 主旨和背景資訊

指定主要焦點 (主體) 和背景或環境 (情境)。

| **提示詞** | **生成的內容** |
| --- | --- |
| 白色混凝土公寓大樓的建築渲染圖，流暢的有機形狀與綠意盎然的植物和未來感元素完美融合 | 預留位置。 |
| 衛星漂浮在外太空，背景是月亮和一些星星。 | 漂浮在大氣層中的衛星。 |

#### 動作

指定主體正在做什麼 (例如走路、跑步或轉頭)。

| **提示詞** | **生成的內容** |
| --- | --- |
| 一名女子沿著海灘漫步，在日落時分望向地平線，神情滿足而放鬆。 | 日落景色美極了。 |

#### 樣式

加入關鍵字，引導生成特定美學風格 (例如超現實、復古、未來主義、黑色電影)。

| **提示詞** | **生成的內容** |
| --- | --- |
| 黑色電影風格，一男一女走在街上，神祕、電影感、黑白。 | 黑色電影風格絕對是美不勝收。 |

#### 攝影機動作和構圖

指定攝影機移動方式 (第一視角、鳥瞰圖、追蹤無人機視角) 和畫面構圖 (遠景、特寫、低角度)。

| **提示詞** | **生成的內容** |
| --- | --- |
| 雨中行駛的復古車輛第一視角鏡頭，加拿大夜晚，電影風格。 | 日落景色美極了。 |
| 眼睛的極特寫鏡頭，眼中有城市的倒影。 | 日落景色美極了。 |

#### 類別

配色和光線會影響氛圍。試試「柔和橘色暖色調」、「自然光」、「日出」或「冷藍色調」等字詞。

| **提示詞** | **生成的內容** |
| --- | --- |
| 特寫鏡頭：陽光灑落的公園中，一名女孩抱著可愛的黃金獵犬幼犬。 | 小女孩抱著小狗。 |
| 電影風格特寫鏡頭，一名悲傷的女子在雨中搭乘公車，冷藍色調，悲傷氛圍。 | 一名女子搭乘公車，看起來很悲傷。 |

### 顯示比例

Veo 可讓您指定影片的顯示比例。

| **提示詞** | **生成的內容** |
| --- | --- |
| **橫向 (16:9)** 生成影片，內容為無人機追蹤拍攝一名男子在 1970 年代的棕櫚泉駕駛紅色敞篷車，陽光溫暖，影子很長。 | 一名男子在棕櫚泉駕駛紅色敞篷車，1970 年代風格。 |
| **直向 (9:16)** 製作影片精華片段，呈現夏威夷壯麗瀑布在茂密雨林中流動的流暢畫面。著重於逼真的水流、細緻的樹葉和自然光線，傳達寧靜感。捕捉奔騰的水流、霧氣繚繞的氛圍，以及穿透茂密樹冠的斑駁陽光。運用流暢、電影般的運鏡手法，呈現瀑布和周遭環境。請盡量營造平靜、寫實的氛圍，讓觀眾彷彿置身於夏威夷雨林的寧靜美景中。 | 茂密雨林中壯麗的夏威夷瀑布。 |

## 模型版本

如要進一步瞭解 Veo 模型的使用詳情，請參閱[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)頁面和[頻率限制](https://aistudio.google.com/rate-limit?hl=zh-tw)。

### Veo 3.1 預先發布版 (已淘汰)

| 屬性 | 說明 |
| --- | --- |
| id\_card模型代碼 | **Gemini API**  `veo-3.1-generate-preview` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto限制 | **文字輸入**  1,024 個詞元  **輸出影片**  1 |
| calendar\_month最新更新 | 2026 年 1 月 |

### Veo 3.1 Fast 預先發布版 (已淘汰)

| 屬性 | 說明 |
| --- | --- |
| id\_card模型代碼 | **Gemini API**  `veo-3.1-fast-generate-preview` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto限制 | **文字輸入**  1,024 個詞元  **輸出影片**  1 |
| calendar\_month最新更新 | 2026 年 1 月 |

### Veo 3.1 Lite 預先發布版 (已淘汰)

| 屬性 | 說明 |
| --- | --- |
| id\_card模型代碼 | **Gemini API**  `veo-3.1-lite-generate-preview` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto限制 | **文字輸入**  1,024 個詞元  **輸出影片**  1 |
| calendar\_month最新更新 | 2026 年 3 月 |

### Veo 3 (已淘汰)

| 屬性 | 說明 |
| --- | --- |
| id\_card模型代碼 | **Gemini API**  `veo-3.0-generate-001` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto限制 | **文字輸入**  1,024 個詞元  **輸出影片**  1 |
| calendar\_month最新更新 | 2025 年 7 月 |

### Veo 3 Fast (已淘汰)

| 屬性 | 說明 |
| --- | --- |
| id\_card模型代碼 | **Gemini API**  `veo-3.0-fast-generate-001` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto限制 | **文字輸入**  1,024 個詞元  **輸出影片**  1 |
| calendar\_month最新更新 | 2025 年 7 月 |

Veo Fast 版本可讓開發人員製作有聲影片，兼顧高畫質、速度和商業用途。這類模型適合用於以程式輔助方式生成廣告的後端服務、快速 A/B 測試廣告素材概念的工具，或需要快速製作社群媒體內容的應用程式。

## 後續步驟

- 如要開始使用 Veo 3.1 API，請在 [Veo 快速入門導覽課程 Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=zh-tw) 和 [Veo 3.1 小工具](https://aistudio.google.com/apps/bundled/veo_studio?hl=zh-tw)中進行實驗。
- 請參閱[提示設計簡介](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-tw)，瞭解如何撰寫更有效的提示。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-22 (世界標準時間)。"],[],[]]
