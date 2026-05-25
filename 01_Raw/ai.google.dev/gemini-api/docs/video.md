---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=tr
fetched_at: 2026-05-25T12:58:44.317461+00:00
title: "Gemini API'de Veo 3.1 ile video \u00fcretme \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API'de Veo 3.1 ile video üretme

> Video anlama hakkında bilgi edinmek için [Video anlama](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr) kılavuzuna bakın.

[Veo 3.1](https://deepmind.google/models/veo/?hl=tr), Google'ın yüksek kaliteli, 8 saniyelik 720p, 1080p veya 4K videolar oluşturmak için kullandığı son teknoloji modelidir. Bu videolar, çarpıcı gerçekçilik ve doğal olarak üretilmiş ses içerir. Bu modele Gemini API'yi kullanarak programatik olarak erişebilirsiniz. Mevcut Veo modeli varyantları hakkında daha fazla bilgi edinmek için [Model Sürümleri](#model-versions) bölümüne bakın.

Veo 3.1, çok çeşitli görsel ve sinematik stillerde üstün performans gösterir ve çeşitli yeni özellikler sunar:

- **Dikey videolar**: Yatay (`16:9`) ve dikey (`9:16`) videolar arasından seçim yapın.
- **Video uzatma**: Daha önce Veo kullanılarak oluşturulan videoları uzatın.
- **Kareye özgü üretim**: İlk ve son kareleri belirterek video oluşturun.
- **Resme dayalı yönlendirme**: Üretilen videonuzun içeriğini yönlendirmek için üç adede kadar referans resim kullanın.

Video oluşturmak için etkili metin istemleri yazma hakkında daha fazla bilgi edinmek için [Veo istem rehberini](#prompt-guide) inceleyin.

## Metinden video üretme

Diyalog, sinematik gerçekçilik veya yaratıcı animasyon içeren videolar oluşturmayı öğrenmek için bir örnek seçin:

Diyalog ve Ses Efektleri
Sinematik Gerçekçilik
Yaratıcı Animasyon

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
client.files.download(file=generated_video.video)
generated_video.video.save("dialogue_example.mp4")
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
import com.google.genai.types.Video;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class GenerateVideoFromText {
  public static void main(String[] args) throws Exception {
    Client client = new Client();

    String prompt = "A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.\n" +
"A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'";

    GenerateVideosOperation operation =
        client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

    // Poll the operation status until the video is ready.
    while (!operation.done().isPresent() || !operation.done().get()) {
      System.out.println("Waiting for video generation to complete...");
      Thread.sleep(10000);
      operation = client.operations.getVideosOperation(operation, null);
    }

    // Download the generated video.
    Video video = operation.response().get().generatedVideos().get().get(0).video().get();
    Path path = Paths.get("dialogue_example.mp4");
    client.files.download(video, path.toString(), null);
    if (video.videoBytes().isPresent()) {
      Files.write(path, video.videoBytes().get());
      System.out.println("Generated video saved to dialogue_example.mp4");
    }
  }
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

### En boy oranını kontrol etme

Veo 3.1 ile yatay (`16:9`, varsayılan ayar) veya dikey (`9:16`) videolar oluşturabilirsiniz. `aspect_ratio` parametresini kullanarak modele hangisini istediğinizi söyleyebilirsiniz:

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
client.files.download(file=generated_video.video)
generated_video.video.save("pizza_making.mp4")
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

### Çözünürlüğü kontrol etme

Veo 3.1, doğrudan 720p, 1080p veya 4K videolar da oluşturabilir (4K, Veo 3.1 Lite'ta kullanılamaz).

Çözünürlük ne kadar yüksek olursa gecikme süresinin de o kadar yüksek olacağını unutmayın. 4K videolar da daha pahalıdır (bkz. [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#veo-3.1)).

[Video uzantısı](#extending_veo_videos) da 720p videolarla sınırlıdır.

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
client.files.download(file=generated_video.video)
generated_video.video.save("4k_grand_canyon.mp4")
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

## Görüntüden video üretme

Aşağıdaki kod, [Gemini 3.1 Flash Image (Nano Banana 2)](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) kullanarak görüntü oluşturmayı ve ardından bu görüntüyü Veo 3.1 ile video oluşturmak için başlangıç karesi olarak kullanmayı gösterir.

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
client.files.download(file=video.video)
video.video.save("veo3_with_image_input.mp4")
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
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.Image;
import com.google.genai.types.Video;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class GenerateVideoFromImage {
  public static void main(String[] args) throws Exception {
    Client client = new Client();

    String prompt = "Panning wide shot of a calico kitten sleeping in the sunshine";

    // Step 1: Generate an image with Nano Banana 2:
    // Assume 'image' contains the generated image,
    // or is loaded from a file:
    Image image = Image.fromFile("path/to/your/image.png");

    // Step 2: Generate video with Veo 3.1 using the image.
    GenerateVideosOperation operation =
        client.models.generateVideos("veo-3.1-generate-preview", prompt, image, null);

    // Poll the operation status until the video is ready.
    while (!operation.done().isPresent() || !operation.done().get()) {
      System.out.println("Waiting for video generation to complete...");
      Thread.sleep(10000);
      operation = client.operations.getVideosOperation(operation, null);
    }

    // Download the video.
    Video video = operation.response().get().generatedVideos().get().get(0).video().get();
    Path path = Paths.get("veo3_with_image_input.mp4");
    client.files.download(video, path.toString(), null);
    if (video.videoBytes().isPresent()) {
      Files.write(path, video.videoBytes().get());
      System.out.println("Generated video saved to veo3_with_image_input.mp4");
    }
  }
}
```

### Referans resimleri kullanma

Veo 3.1, üretilen videonuzun içeriğine yön vermek için artık 3 adede kadar referans görseli kabul ediyor. Çıkış videosunda konuyla ilgili görünümü korumak için bir kişinin, karakterin veya ürünün resimlerini sağlayın.

Örneğin, [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) ile oluşturulan bu üç resmi [iyi yazılmış bir istemle](#use-reference-images) referans olarak kullanarak aşağıdaki video oluşturulur:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| Pembe ve fuşya tüylerden oluşan katmanlı, yüksek moda ürünü flamingo elbisesi | Koyu renk saçlı ve sıcak kahverengi gözlü güzel bir kadın | Kaprisli pembe, kalp şeklinde güneş gözlüğü |

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
client.files.download(file=video.video)
video.video.save("veo3.1_with_reference_images.mp4")
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

### İlk ve son kareyi kullanma

Veo 3.1, enterpolasyon kullanarak veya videonun ilk ve son karelerini belirterek video oluşturmanıza olanak tanır. Video üretimi için etkili metin istemleri yazma hakkında bilgi edinmek istiyorsanız [Veo istem rehberine](#use-reference-images) bakın.

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
client.files.download(file=video.video)
video.video.save("veo3.1_with_interpolation.mp4")
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
| Uzun beyaz saçlı ve akışkan bir elbise giymiş hayaletimsi bir kadın, halatlı salıncakta hafifçe sallanıyor. | Hayalet kadın salıncaktan kayboluyor | Sisli bir havada salıncakta oturan ürkütücü bir kadının kaybolduğu sinematik ve rahatsız edici video |

## Veo videolarını uzatma

Daha önce Veo ile oluşturduğunuz videoları 7 saniye ve 20 kata kadar uzatmak için Veo 3.1'i kullanın.

Giriş videosu sınırlamaları:

- Veo tarafından oluşturulan videolar en fazla 141 saniye uzunluğunda olabilir.
- Gemini API, yalnızca Veo ile üretilen videolar için video uzantılarını destekler.
- Video, `operation.response.generated_videos[0].video` gibi önceki nesillerden birine ait olmalıdır.
- Videolar 2 gün boyunca saklanır. Ancak bir video uzatma için referans olarak kullanılıyorsa 2 günlük saklama süresi sıfırlanır. Yalnızca son iki gün içinde oluşturulan veya referans verilen videoları uzatabilirsiniz.
- Giriş videolarının belirli bir uzunluğa, en boy oranına ve boyuta sahip olması beklenir:
  - En-boy oranı: 9:16 veya 16:9
  - Çözünürlük: 720p
  - Video uzunluğu: 141 saniye veya daha kısa

Uzantının çıktısı, kullanıcı giriş videosu ile oluşturulan genişletilmiş videoyu birleştiren ve 148 saniyeye kadar video içeren tek bir videodur.

Bu örnekte, orijinal istemiyle birlikte gösterilen Veo tarafından oluşturulmuş bir video, `video` parametresi ve yeni bir istem kullanılarak genişletiliyor:

| İstem | Çıkış: `butterfly_video` |
| --- | --- |
| Origami kelebek kanatlarını çırparak Fransız kapısından bahçeye uçuyor. | Origami kelebek kanatlarını çırparak Fransız kapıdan bahçeye doğru uçuyor. |

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
client.files.download(file=video.video)
video.video.save("veo3.1_extension.mp4")
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

Video üretimi için etkili metin istemleri yazma hakkında bilgi edinmek için [Veo istem rehberine](#extend-prompt) bakın.

## Eşzamansız işlemleri işleme

Video oluşturma, bilgi işlem açısından yoğun bir görevdir. API'ye istek gönderdiğinizde uzun süren bir iş başlatılır ve hemen bir `operation` nesnesi döndürülür. Ardından, `done` durumu doğru olana kadar video hazır olana kadar yoklama yapmanız gerekir.

Bu sürecin temelinde, işin durumunu düzenli olarak kontrol eden bir yoklama döngüsü bulunur.

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
import com.google.genai.types.Video;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class HandleAsync {
  public static void main(String[] args) throws Exception {
    Client client = new Client();

    // After starting the job, you get an operation object.
    GenerateVideosOperation operation =
        client.models.generateVideos(
            "veo-3.1-generate-preview",
            "A cinematic shot of a majestic lion in the savannah.",
            null,
            null);

    // This loop checks the job status every 10 seconds.
    while (!operation.done().isPresent() || !operation.done().get()) {
      Thread.sleep(10000);
      // Refresh the operation object to get the latest status.
      operation = client.operations.getVideosOperation(operation, null);
    }

    // Once done, the result is in operation.response.
    // Download the generated video.
    Video video = operation.response().get().generatedVideos().get().get(0).video().get();
    Path path = Paths.get("async_example.mp4");
    client.files.download(video, path.toString(), null);
    if (video.videoBytes().isPresent()) {
      Files.write(path, video.videoBytes().get());
      System.out.println("Generated video saved to async_example.mp4");
    }
  }
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

## Veo API parametreleri ve spesifikasyonları

Bunlar, video oluşturma sürecini kontrol etmek için API isteğinizde ayarlayabileceğiniz parametrelerdir.

| Parametre | Veo 3.1 ve Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 ve Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| Örnekler | | | | |
| `prompt`: Videonun metin açıklaması. Ses işaretlerini destekler. | `string` | `string` | `string` | `string` |
| `image`: Animasyon eklenecek ilk resim. | `Image` nesnesi | `Image` nesnesi | `Image` nesnesi | `Image` nesnesi |
| `lastFrame`: Geçiş yapılacak bir enterpolasyon videosunun son resmi. `image` parametresiyle birlikte kullanılmalıdır. | `Image` nesnesi | `Image` nesnesi | `Image` nesnesi | `Image` nesnesi |
| `referenceImages`: Stil ve içerik referansı olarak kullanılacak en fazla üç resim. | `VideoGenerationReferenceImage` nesnesi | `n/a` nesnesi | Yok | Yok |
| `video`: Video uzantısı için kullanılacak video. | Önceki nesilden `Video` nesne | Yok | Yok | Yok |
| Parametreler | | | | |
| `aspectRatio`: Videonun en boy oranı. | `"16:9"` (varsayılan), `"9:16"` | `"16:9"` (varsayılan), `"9:16"` | `"16:9"` (varsayılan), `"9:16"` | `"16:9"` (varsayılan), `"9:16"` |
| `durationSeconds`: Oluşturulan videonun uzunluğu. | `"4"`, `"6"`, `"8"`.   *Uzantı, referans resimler veya 1080p ve 4K çözünürlükler kullanılırken "8" olmalıdır.* | `"4"`, `"6"`, `"8"`.   *Referans resimler kullanılırken veya 1080p ile "8" olmalıdır* | `"4"`, `"6"`, `"8"`.   *Uzantı, referans resimler veya 1080p ve 4K çözünürlükler kullanılırken "8" olmalıdır.* | `"5"`, `"6"`, `"8"` |
| `personGeneration`: İnsanların üretilmesini kontrol eder. (Bölgesel kısıtlamalar için [Sınırlamalar](#limitations) bölümüne bakın) | Metinden videoya ve uzantı: `"allow_all"` yalnızca   Görüntüden videoya, ara görüntü ve referans resimler: `"allow_adult"` yalnızca | Metinden videoya: `"allow_all"` yalnızca   Görüntüden videoya, ara görüntü ve referans resimler: `"allow_adult"` yalnızca | Metinden videoya: `"allow_all"` yalnızca   Görüntüden videoya: `"allow_adult"` yalnızca | Metinden video:  `"allow_all"`, `"allow_adult"`, `"dont_allow"`   Resimden video:  `"allow_adult"` ve `"dont_allow"` |
| `resolution`: Videonun çözünürlüğü. | `"720p"` (varsayılan),  `"1080p"` (yalnızca 8 saniye süreyi destekler), `"4k"` (yalnızca 8 saniye süreyi destekler)   *`"720p"` yalnızca uzantı için* | `"720p"` (varsayılan),  `"1080p"` (yalnızca 8 saniyelik süreyi destekler) | `"720p"` (varsayılan),  `"1080p"` (yalnızca 8 saniye süreyi destekler), `"4k"` (yalnızca 8 saniye süreyi destekler)   *`"720p"` yalnızca uzantı için* | Desteklenmiyor |

`seed` parametresinin Veo 3 modellerinde de kullanılabildiğini unutmayın.
Bu, determinizmi garanti etmez ancak biraz iyileştirir.

## Model özellikleri

| Özellik | Veo 3.1 ve Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 ve Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **Ses:** Videoyla birlikte doğal ses üretir. | ✔️ Her zaman açık | ✔️ Her zaman açık | ✔️ Her zaman açık | ❌ Yalnızca sessiz |
| **Giriş biçimleri:** Üretim için kullanılan giriş türü. | Metinden videoya, görüntüden videoya, videodan videoya | Metinden videoya, görüntüden videoya | Metinden videoya, görüntüden videoya | Metinden videoya, görüntüden videoya |
| **Çözünürlük:** Videonun çıkış çözünürlüğü. | 720p, 1080p (yalnızca 8 saniye uzunluğunda), 4K (yalnızca 8 saniye uzunluğunda)  *Video uzantısı kullanılırken yalnızca 720p.* | 720p, 1080p (yalnızca 8 saniye uzunluğunda) | 720p ve 1080p (yalnızca 16:9) | 720p |
| **Kare hızı:** Videonun çıkış kare hızı. | 24 fps | 24 fps | 24 fps | 24 fps |
| **Video süresi:** Oluşturulan videonun uzunluğu. | 8 saniye, 6 saniye, 4 saniye  *Yalnızca 1080p veya 4K ise ya da referans resimler kullanılıyorsa 8 saniye* | 8 saniye, 6 saniye, 4 saniye  *Yalnızca 1080p ise veya referans resimler kullanılıyorsa 8 saniye* | 8 saniye | 5-8 saniye |
| **İstek başına video sayısı:** İstek başına oluşturulan video sayısı. | 1 | 1 | 1 | 1 veya 2 |
| **Durum:** Modelin kullanılabilirliği | [Önizleme](https://ai.google.dev/gemini-api/docs/models?hl=tr#preview) | [Önizleme](https://ai.google.dev/gemini-api/docs/models?hl=tr#preview) | [Kararlı](https://ai.google.dev/gemini-api/docs/models?hl=tr#stable) | [Kararlı](https://ai.google.dev/gemini-api/docs/models?hl=tr#latest-stable) |

## Sınırlamalar

- **İstek gecikmesi:** En az: 11 saniye; en fazla: 6 dakika (yoğun saatlerde).
- **Bölgesel sınırlamalar:** AB, Birleşik Krallık, İsviçre ve Orta Doğu ve Kuzey Afrika'daki konumlarda `personGeneration` için izin verilen değerler şunlardır:
  - Veo 3 ve 3.1: Yalnızca `allow_adult`.
  - Veo 2: `dont_allow` ve `allow_adult`. Varsayılan değer `dont_allow`'dır.
- **Video saklama:** Oluşturulan videolar 2 gün boyunca sunucuda saklanır ve ardından kaldırılır. Yerel bir kopya kaydetmek için videonuzu oluşturulduktan sonraki 2 gün içinde indirmeniz gerekir. Uzatılmış videolar, yeni oluşturulmuş videolar olarak kabul edilir.
- **Filigran:** Veo ile oluşturulan videolar, yapay zekayla üretilen içeriklere filigran ekleyip bu tür içerikleri tespit etmek için kullandığımız [SynthID](https://deepmind.google/technologies/synthid/?hl=tr) ile filigranlanır. Videolar, [SynthID](https://deepmind.google/science/synthid/?hl=tr) doğrulama platformu kullanılarak doğrulanabilir.
- **Güvenlik:** Oluşturulan videolar, gizlilik, telif hakkı ve önyargı risklerini azaltmaya yardımcı olan güvenlik filtrelerinden ve ezberleme kontrolü süreçlerinden geçirilir.
- **Ses hatası:** Veo 3.1, güvenlik filtreleri veya sesle ilgili diğer işleme sorunları nedeniyle bazen videonun oluşturulmasını engeller. Videonuzun oluşturulması engellenirse sizden ücret alınmaz.

## Veo istem rehberi

Bu bölümde, Veo kullanarak oluşturabileceğiniz videolara dair örnekler yer alır ve istemleri değiştirerek nasıl farklı sonuçlar elde edebileceğiniz gösterilir.

### Güvenlik filtreleri

Veo, üretilen videolarda ve yüklenen fotoğraflarda rahatsız edici içerik bulunmaması için Gemini'da güvenlik filtreleri uygular.
[Şartlarımızı ve kurallarımızı](https://ai.google.dev/gemini-api/docs/usage-policies?hl=tr#abuse-monitoring) ihlal eden istemler engellenir.

### İstem yazmayla ilgili temel bilgiler

İyi istemler açıklayıcı ve nettir. Veo'dan en iyi şekilde yararlanmak için temel fikrinizi belirleyerek başlayın, anahtar kelimeler ve değiştiriciler ekleyerek fikrinizi ayrıntılandırın ve istemlerinize videoya özgü terminolojiyi dahil edin.

İsteminizde aşağıdaki öğeler yer almalıdır:

- **Özne**: Videonuzda olmasını istediğiniz nesne, kişi, hayvan veya manzara (ör. *şehir manzarası*, *doğa*, *araçlar* veya *köpek yavruları*).
- **İşlem**: Öznenin yaptığı işlem (ör. *yürüme*, *koşma* veya *başını çevirme*).
- **Stil**: *Bilim kurgu*, *korku filmi*, *kara film* gibi belirli film stili anahtar kelimelerini veya *çizgi film* gibi animasyon stillerini kullanarak reklam öğesi yönünü belirtin.
- **Kamera konumlandırması ve hareketi**: [İsteğe bağlı] *Kuşbakışı*, *göz hizası*, *yukarıdan çekim*, *dolly çekimi* veya *solucan gözü* gibi terimleri kullanarak kameranın konumunu ve hareketini kontrol edin.
- **Kompozisyon**: [İsteğe bağlı] Çekimin nasıl kadraja alındığı (ör. *geniş çekim*, *yakın çekim*, *tek çekim* veya *iki kişilik çekim*).
- **Odak ve lens efektleri**: [İsteğe bağlı] Belirli görsel efektler elde etmek için *sığ odak*, *derin odak*, *Odağı Yumuşat*, *makro lens* ve *geniş açılı lens* gibi terimler kullanın.
- **Ortam**: [İsteğe bağlı] Renk ve ışığın sahneye katkısı (ör. *mavi tonlar*, *gece* veya *sıcak tonlar*).

#### İstem yazmayla ilgili diğer ipuçları

- **Açıklayıcı bir dil kullanın**: Veo'ya net bir resim sunmak için sıfatlar ve zarflar kullanın.
- **Yüz ayrıntılarını iyileştirin**: İstemde *portre* kelimesini kullanarak yüz ayrıntılarını fotoğrafın odak noktası olarak belirtin.

*Daha kapsamlı istem stratejileri için [İstem tasarımına giriş](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=tr) başlıklı makaleyi inceleyin.*

### Ses istemi

Veo'ya ses efektleri, ortam gürültüsü ve diyalog için istemler sağlayabilirsiniz.
Model, senkronize bir film müziği oluşturmak için bu ipuçlarının nüansını yakalar.

- **Diyalog:** Belirli bir konuşma için tırnak işareti kullanın. (Örnek: "Bu anahtar olmalı," diye mırıldandı.)
- **Ses efektleri:** Sesleri açıkça tanımlayın. (Örnek: lastiklerin
  gürültülü bir şekilde gıcırdaması, motorun kükremesi)
- **Ortam Gürültüsü:** Ortamın ses manzarasını açıklayın. (Örnek: Arka planda hafif ve ürkütücü bir uğultu duyuluyor.)

Bu videolarda, Veo 3'ün ses üretme özelliğine artan ayrıntı düzeylerinde istem girme gösterilmektedir.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| **Daha fazla ayrıntı (Diyalog ve ortam)** Sisli bir Pasifik Kuzeybatı ormanının geniş açılı çekimi. Yorgun iki yürüyüşçü (bir kadın ve bir erkek) eğrelti otları arasından geçerken erkek aniden durup bir ağaca bakıyor. Yakın çekim: Ağacın kabuğunda taze ve derin pençe izleri var. Adam: (Av bıçağını tutarak) "Bu sıradan bir ayı değil." Kadın: (Korkuyla sesi titreyerek, ormanı tarayarak) "Peki o zaman bu ne?" Pürüzlü bir kabuk, çıtırdayan dallar, nemli toprağın üzerindeki ayak izleri. Tek bir kuş cıvıldıyor. | Ormanda iki kişi ayı izleriyle karşılaşıyor. |
| **Daha az ayrıntı (Diyalog)** Kağıt kesme animasyonu. Yeni kütüphaneci: "Yasaklı kitapları nerede saklıyorsunuz?" Eski İçerik Seçici: "Hayır. Onlar bizi korur." | Yasaklı kitapları tartışan animasyonlu kütüphaneciler |

Sesi dinlemek için bu istemleri kendiniz deneyin.
[Veo'yu deneyin](https://deepmind.google/models/veo/?hl=tr)

### Referans resimlerle istem oluşturma

Veo'nun [görüntüden videoya](https://ai.google.dev/gemini-api/docs/video?hl=tr#generate-from-images) özelliklerini kullanarak oluşturulan videolarınıza yön vermek için bir veya daha fazla görüntüyü giriş olarak kullanabilirsiniz. Veo, giriş resmini ilk kare olarak kullanır. Günlük nesneleri hareketlendirmek, çizimlere ve tablolara hayat vermek, doğa manzaralarına hareket ve ses eklemek için videonuzun ilk sahnesi olarak düşündüğünüz görüntüye en yakın olanı seçin.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| **Giriş resmi (Nano Banana tarafından oluşturuldu)** Küçük, minyatür sörfçülerin rustik bir taş banyo lavabosunda okyanus dalgalarında sörf yaptığı hiper gerçekçi bir makro fotoğraf. Eski bir pirinç musluk, sürekli sörf sesi çıkararak akıyor. Sürreal, tuhaf, parlak doğal ışıklandırma. | Rustik taş banyo lavabosunda okyanus dalgalarında sörf yapan minik sörfçülerin minyatür görüntüsü. |
| **Çıkış videosu (Veo 3.1 tarafından oluşturuldu)** Sürrealist, sinematik bir makro video. Küçük sörfçüler, taş bir banyo lavabosunun içindeki sürekli yuvarlanan dalgalarda sörf yapıyor. Çalışan eski bir pirinç musluk, sonsuz sörf dalgaları oluşturuyor. Kamera, minyatür figürler turkuaz rengi suyu ustaca oyarken güneş ışığıyla aydınlatılmış, eğlenceli sahneyi yavaşça tarıyor. | Banyo lavabosundaki dalgaların etrafında dönen minik sörfçüler. |

Veo 3.1, üretilen videonuzun içeriğini yönlendirmek için [referans görseller](https://ai.google.dev/gemini-api/docs/video?hl=tr#reference-images) veya içerik öğeleri kullanmanıza olanak tanır. Tek bir kişiye, karaktere veya ürüne ait en fazla üç öğe resmi sağlayın. Veo, öznenin görünümünü çıkış videosunda korur.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| **Referans görsel (Nano Banana tarafından oluşturulmuştur)** Derin denizlerde yaşayan bir fenersiler balığı, dişleri açık ve yemi parlayarak karanlık sularda gizleniyor. | Karanlıkta parlayan bir fener balığı |
| **Referans görsel (Nano Banana tarafından oluşturuldu)** Düz bir ürün arka planı üzerinde, değnek ve taç ile tamamlanmış pembe bir çocuk prenses kostümü. | Çocuğun pembe prenses kostümü |
| **Çıkış videosu (Veo 3.1 tarafından oluşturuldu)** Kostümlü, yüzen ve asayı sallayan balığın komik bir çizgi film versiyonunu oluştur. | Prenses kostümü giymiş bir fener balığı |

Veo 3.1'i kullanarak videonun [ilk ve son karelerini](https://ai.google.dev/gemini-api/docs/video?hl=tr#using-first-and-last-video-frames) belirterek de video oluşturabilirsiniz.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| **İlk resim (Nano Banana tarafından üretildi)** Fransız Rivierası kıyısında kırmızı üstü açık yarış arabası kullanan bir zencefil kedinin yüksek kaliteli, fotoğraf gerçekliğinde ön görüntüsü. | Kırmızı üstü açık yarış arabası kullanan zencefil rengi bir kedi |
| **Son görüntü (Nano Banana tarafından oluşturuldu)** Araba bir uçurumdan kalktığında ne olduğunu göster. | Kırmızı üstü açık arabayı kullanan bir zencefil kedinin uçurumdan düşmesi |
| **Çıkış videosu (Veo 3.1 tarafından oluşturulur)** İsteğe bağlı | Bir kedi, uçurumdan aşağı araba sürüyor ve havalanıyor |

Bu özellik, başlangıç ve bitiş karesini tanımlamanıza olanak tanıyarak çekiminizin kompozisyonu üzerinde hassas kontrol sağlar. Sahnenizin tam olarak hayal ettiğiniz gibi başlayıp sona ermesini sağlamak için bir resim yükleyin veya önceki bir video oluşturma işleminden bir kare kullanın.

### Uzantı isteme

Veo 3.1 ile Veo tarafından oluşturulan videonuzu [uzatmak](https://ai.google.dev/gemini-api/docs/video?hl=tr#extending_veo_videos) için (Veo 3.1 Lite'ta kullanılamaz) videoyu isteğe bağlı bir metin istemiyle birlikte giriş olarak kullanın. Uzatma, videonuzun son 1-2 saniyesini veya 24 karesini tamamlar ve aksiyonu devam ettirir.

Ses, videonun son 1 saniyesinde yoksa etkili bir şekilde uzatılamaz.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| **Giriş videosu (Veo 3.1 tarafından oluşturuldu)** Yamaç paraşütçüsü dağın tepesinden kalkış yapıyor ve aşağıda çiçeklerle kaplı vadilere bakan dağlardan aşağı doğru süzülmeye başlıyor. | Bir yamaç paraşütçüsü dağın tepesinden kalkıyor |
| **Çıkış videosu (Veo 3.1 tarafından oluşturuldu)** Bu videoyu, yavaşça alçalan yamaç paraşütüyle uzat. | Bir yamaç paraşütü, dağın tepesinden kalkıyor ve yavaşça aşağı iniyor |

### Örnek istemler ve çıkış

Bu bölümde, açıklayıcı ayrıntıların her videonun sonucunu nasıl iyileştirebileceğini vurgulayan çeşitli istemler sunulmaktadır.

#### Buz Saçakları

Bu videoda, isteminizde [istem yazmayla ilgili temel bilgilerin](#basics) öğelerini nasıl kullanabileceğiniz gösterilmektedir.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| Donmuş bir kaya duvarında (bağlam) eriyen buz sarkıtlarının (özne) yakın çekim fotoğrafı (kompozisyon). Su damlalarının (eylem) yakın çekim ayrıntıları korunarak (kamera hareketi) mavi tonlarda (atmosfer) yakınlaştırılmış. | Mavi arka plan üzerinde damlayan buz sarkıtları. |

#### Telefonda konuşan adam

Bu videolarda, Veo'nun çıktıyı istediğiniz gibi iyileştirmesi için isteminizi giderek daha ayrıntılı bilgilerle nasıl revize edebileceğiniz gösterilmektedir.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| **Daha az ayrıntı** Kamera, yeşil trençkotlu çaresiz bir adamın yakın çekimini göstermek için hareket ediyor. Çevirmeli tarzda bir duvar telefonunda yeşil neon ışığıyla görüşme yapıyor. Film sahnesi gibi görünüyor. | Telefonda konuşan adam. |
| **Daha ayrıntılı açıklama** Yakın çekim sinematik bir sahnede, yıpranmış yeşil trençkotlu çaresiz bir adam, yeşil neon tabelanın ürkütücü ışığıyla aydınlatılmış, kirli bir tuğla duvara monte edilmiş çevirmeli bir telefonu çeviriyor. Kamera, adamın çenesindeki gerginliği ve telefonu açmaya çalışırken yüzüne yansıyan çaresizliği göstererek yakınlaşıyor. Alan derinliği düşük olduğu için arka plandaki neon renkler ve belirsiz gölgeler bulanık görünüyor. Bu durum, aciliyet ve yalnızlık hissi yaratıyor. | Telefonda konuşan adam |

#### Kar leoparı

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| **Basit istem:** Karda leopar benzeri tüyleri olan sevimli bir yaratık kış ormanında yürüyor, 3D çizgi film tarzında oluştur. | Kar leoparı uyuşuktur. |
| **Ayrıntılı istem:** Neşeli bir çizgi film tarzında kısa bir 3D animasyon sahnesi oluştur. Kar leoparı gibi tüyleri, büyük ve etkileyici gözleri olan sevimli bir yaratık, dost canlısı ve yuvarlak hatlarıyla kışın büyülü ormanında neşeyle dans ediyor. Sahne; yuvarlak, karla kaplı ağaçlar, yavaşça düşen kar taneleri ve dallar arasından süzülen sıcak güneş ışığı içermeli. Yaratığın zıplayan hareketleri ve kocaman gülümsemesi, saf bir keyif duygusu vermelidir. Parlak ve neşeli renkler ile eğlenceli animasyonlar kullanarak neşeli ve içten bir üslup kullanın. | Kar leoparı daha hızlı koşuyor. |

### Yazı öğelerine göre örnekler

Bu örneklerde, istemlerinizi her bir temel öğeye göre nasıl hassaslaştıracağınız gösterilmektedir.

#### Konu ve bağlam

Ana odak noktasını (konu) ve arka planı veya ortamı (bağlam) belirtin.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| Yemyeşil bitki örtüsü ve fütüristik öğelerle kusursuz bir şekilde harmanlanan, akışkan organik şekillere sahip beyaz beton bir apartman binasının mimari görseli | Yer tutucu. |
| Uzayda süzülen bir uydu. Arka planda ay ve bazı yıldızlar görünüyor. | Atmosferde süzülen uydu. |

#### İşlem

Öznenin ne yaptığını belirtin (ör. yürüyor, koşuyor veya başını çeviriyor).

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| Gün batımında ufka doğru mutlu ve rahat bir şekilde yürüyen kadının geniş açılı fotoğrafı. | Gün batımı kesinlikle çok güzel. |

#### Stil

Üretimi belirli bir estetiğe yönlendirmek için anahtar kelimeler ekleyin (ör. sürreal, vintage, fütüristik, film noir).

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| Kara film tarzında, sokakta yürüyen bir adam ve kadın, gizemli, sinematik, siyah beyaz. | Film noir tarzı kesinlikle çok güzel. |

#### Kamera hareketi ve kompozisyon

Kameranın nasıl hareket edeceğini (öznel çekim, kuşbakışı, takip eden drone görünümü) ve çekimin nasıl kadrajlanacağını (geniş çekim, yakın çekim, alçak açı) belirtin.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| Yağmurda giden bir vintage arabanın bakış açısı çekimi, Kanada'da gece, sinematik. | Gün batımı kesinlikle çok güzel. |
| Gözün, içinde şehir yansıması olan aşırı yakın çekimi. | Gün batımı kesinlikle çok güzel. |

#### Ortam

Renk paletleri ve aydınlatma, ruh halini etkiler. "Mat turuncu, sıcak tonlar", "doğal ışık", "gündoğumu" veya "soğuk mavi tonlar" gibi terimleri deneyin.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| Parkta sevimli bir golden retriever yavrusunu tutan kızın yakın çekimi, güneş ışığı. | Küçük bir kızın kollarında bir köpek yavrusu. |
| Yağmurda otobüste yolculuk eden üzgün bir kadının sinematik yakın çekimi, soğuk mavi tonlar, üzgün ruh hali. | Otobüste üzgün bir şekilde yolculuk yapan kadın. |

### En boy oranları

Veo, videonuzun en-boy oranını belirtmenize olanak tanır.

| **İstem** | **Üretilen çıkış** |
| --- | --- |
| **Geniş ekran (16:9)** 1970'lerde Palm Springs'te kırmızı üstü açık bir arabayı süren bir adamın takip eden drone görüntüsünü içeren bir video oluştur. Sıcak güneş ışığı, uzun gölgeler. | Palm Springs&#39;te 1970&#39;ler tarzında kırmızı bir üstü açık arabayı süren bir adam. |
| **Dikey (9:16)** Yemyeşil bir yağmur ormanındaki görkemli bir Hawaii şelalesinin akıcı hareketini vurgulayan bir video oluşturun. Sakinliği yansıtmak için gerçekçi su akışına, ayrıntılı yeşilliklere ve doğal ışıklandırmaya odaklan. Akan suyu, puslu atmosferi ve sık ağaçların arasından süzülen benekli güneş ışığını yakalayın. Şelaleyi ve çevresini göstermek için akıcı ve sinematik kamera hareketleri kullanın. İzleyiciyi Hawaii yağmur ormanının huzurlu güzelliğine götüren, sakin ve gerçekçi bir ton kullanın. | Yemyeşil bir yağmur ormanında muhteşem bir Hawaii şelalesi. |

## Model sürümleri

Veo modeline özgü kullanım ayrıntıları için [Fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#veo-3.1) sayfası ve [Hız sınırları](https://aistudio.google.com/rate-limit?hl=tr) bölümüne göz atın.

### Veo 3.1 Önizlemesi

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `veo-3.1-generate-preview` |
| saveDesteklenen veri türleri | **Giriş**  Metin, resim  **Çıkış**  Sesli video |
| token\_autoSınırlar | **Metin girişi**  1.024 jeton  **Çıkış videosu**  1 |
| calendar\_monthSon güncelleme | Ocak 2026 |

### Veo 3.1 Fast Önizlemesi

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `veo-3.1-fast-generate-preview` |
| saveDesteklenen veri türleri | **Giriş**  Metin, resim  **Çıkış**  Sesli video |
| token\_autoSınırlar | **Metin girişi**  1.024 jeton  **Çıkış videosu**  1 |
| calendar\_monthSon güncelleme | Ocak 2026 |

### Veo 3.1 Lite Önizlemesi

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `veo-3.1-lite-generate-preview` |
| saveDesteklenen veri türleri | **Giriş**  Metin, resim  **Çıkış**  Sesli video |
| token\_autoSınırlar | **Metin girişi**  1.024 jeton  **Çıkış videosu**  1 |
| calendar\_monthSon güncelleme | Mart 2026 |

### Veo 3

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `veo-3.0-generate-001` |
| saveDesteklenen veri türleri | **Giriş**  Metin, resim  **Çıkış**  Sesli video |
| token\_autoSınırlar | **Metin girişi**  1.024 jeton  **Çıkış videosu**  1 |
| calendar\_monthSon güncelleme | Temmuz 2025 |

### Veo 3 Fast

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `veo-3.0-fast-generate-001` |
| saveDesteklenen veri türleri | **Giriş**  Metin, resim  **Çıkış**  Sesli video |
| token\_autoSınırlar | **Metin girişi**  1.024 jeton  **Çıkış videosu**  1 |
| calendar\_monthSon güncelleme | Temmuz 2025 |

### Veo 2

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `veo-2.0-generate-001` |
| saveDesteklenen veri türleri | **Giriş**  Metin, resim  **Çıkış**  Video |
| token\_autoSınırlar | **Metin girişi**  Yok  **Resim girişi**  Dosya boyutu 20 MB'a kadar olan tüm görüntü çözünürlükleri ve en boy oranları  **Çıkış videosu**  2'ye kadar |
| calendar\_monthSon güncelleme | Nisan 2025 |

### Veo 2

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `veo-2.0-generate-001` |
| saveDesteklenen veri türleri | **Giriş**  Metin, resim  **Çıkış**  Video |
| token\_autoSınırlar | **Metin girişi**  Yok  **Resim girişi**  Dosya boyutu 20 MB'a kadar olan tüm görüntü çözünürlükleri ve en boy oranları  **Çıkış videosu**  2'ye kadar |
| calendar\_monthSon güncelleme | Nisan 2025 |

Veo Fast sürümleri, geliştiricilerin yüksek kaliteyi koruyarak ve hız ile iş kullanım alanları için optimize ederek sesli videolar oluşturmasına olanak tanır. Reklamları programatik olarak oluşturan arka uç hizmetleri, reklam öğesi konseptlerinin hızlı A/B testi için kullanılan araçlar veya sosyal medya içeriklerini hızlıca üretmesi gereken uygulamalar için idealdir.

## Sırada ne var?

- [Veo Quickstart Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=tr) ve [Veo 3.1 applet](https://aistudio.google.com/apps/bundled/veo_studio?hl=tr)'te denemeler yaparak Veo 3.1 API'yi kullanmaya başlayın.
- [İstem tasarımına giriş](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=tr) başlıklı makalemizle daha iyi istemler yazmayı öğrenin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-13 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-13 UTC."],[],[]]
