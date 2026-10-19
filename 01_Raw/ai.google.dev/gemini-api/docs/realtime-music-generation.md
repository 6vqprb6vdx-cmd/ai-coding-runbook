---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=zh-CN
fetched_at: 2026-10-19T05:36:33.231205+00:00
title: "\u4f7f\u7528 Lyria RealTime \u5b9e\u65f6\u751f\u6210\u97f3\u4e50 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 Lyria RealTime 实时生成音乐

Gemini API 使用 [Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=zh-cn)，可提供对前沿的实时流式音乐生成模型的访问权限。它允许开发者构建应用，让用户能够以交互方式创作音乐、持续引导音乐创作，以及演奏乐器音乐。

Lyria RealTime 音乐创作功能使用 [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) 建立持久的双向低延迟流式传输连接。

如需体验使用 Lyria RealTime 可以构建哪些内容，请在 AI Studio 中使用 [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=zh-cn) 或 [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=zh-cn) 应用进行尝试。

## 生成和控制音乐

Lyria RealTime 的工作方式与 [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn) 类似，它使用 WebSocket 与模型保持实时通信。

以下代码演示了如何生成音乐：

### Python

此示例使用 `client.aio.live.music.connect()` 初始化 Lyria RealTime 会话，然后使用 `session.set_weighted_prompts()` 发送初始提示，同时使用 `session.set_music_generation_config` 发送初始配置，使用 `session.play()` 开始生成音乐，并设置 `receive_audio()` 来处理收到的音频块。

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1beta'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

此示例使用 `client.live.music.connect()` 初始化 Lyria RealTime 会话，然后使用 `session.setWeightedPrompts()` 发送初始提示，同时使用 `session.setMusicGenerationConfig` 发送初始配置，使用 `session.play()` 开始生成音乐，并设置 `onMessage` 回调来处理收到的音频块。

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1beta" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

然后，您可以使用 `session.play()`、`session.pause()`、`session.stop()` 和 `session.reset_context()` 来开始、暂停、停止或重置会话。

## 实时控制音乐

您可以发送提示并实时更新生成参数，从而实时控制音乐创作。

### 向 Lyria RealTime 发出提示

在直播期间，您可以随时发送新的 `WeightedPrompt` 消息来改变生成的音乐。模型将根据新输入内容平稳过渡。

提示需要采用正确的格式，包含 `text`（实际提示）和 `weight`。`weight` 可以采用除 `0` 之外的任何值。`1.0` 通常是一个不错的起点。

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

请注意，大幅更改提示时，模型过渡可能会有些突兀，因此建议通过向模型发送中间权重值来实现某种淡入淡出效果。

### 更新配置

您可以通过实时更新音乐创作参数来引导音乐创作。您不能只更新一个参数，而需要设置整个配置，否则其他字段将重置回其默认值。

由于更新每分钟节拍数或音阶对模型来说是一项重大更改，您还需要使用 `reset_context()` 指示模型重置其上下文，以便将新配置纳入考虑范围。这不会停止直播，但会造成硬切换。其他参数则无需执行此操作。

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## 为 Lyria RealTime 提供提示

Lyria RealTime 使用加权提示来动态融合音乐流派、乐器和情绪。如需探索提示引导策略、关键字标记词汇和完整提示示例，请参阅 [Lyria 提示指南](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=zh-cn#realtime-prompting)。

## 最佳做法

- 客户端应用必须实现强大的音频缓冲功能，以确保流畅播放。这有助于考虑网络抖动和生成延迟的细微变化。
- 有效的提示：
  - 描述要详实具体。使用描述曲调、流派和乐器的形容词。
  - 逐步迭代和调整。与其完全更改提示，不如尝试添加或修改元素，以便更顺畅地转换音乐。
  - 尝试调整 `WeightedPrompt` 的权重，以影响新提示对正在进行的生成过程的影响程度。

## 技术详情

本部分详细介绍了如何使用 Lyria RealTime 音乐生成功能。

### 规格

- 输出格式：原始 16 位 PCM 音频
- 采样率：48kHz
- 声道：2（立体声）

### 控件

通过发送包含以下内容的讯息，可以实时影响音乐生成：

- `WeightedPrompt`：描述音乐创意、流派、乐器、情绪或特征的文本字符串。您可以提供多个提示，以融合各种影响。如需详细了解如何以最佳方式提示 Lyria RealTime，请参阅[上文](#steer-music)。
- `MusicGenerationConfig`：音乐生成过程的配置，会影响输出音频的特征。参数包括：
  - `guidance`：（浮点数）范围：`[0.0, 6.0]`。默认值：`4.0`。
    控制模型遵循提示的严格程度。指导值越高，模型对提示的遵循程度就越高，但过渡会更突兀。
  - `bpm`：（整数）范围：`[60, 200]`。
    设置您希望生成的音乐达到的每分钟节拍数。您需要停止/播放或重置模型的上下文，以便模型将新的每分钟节拍数纳入考虑范围。
  - `density`：（浮点数）范围：`[0.0, 1.0]`。
    控制音符/声音的密度。值越低，生成的音乐越稀疏；值越高，生成的音乐越“繁忙”。
  - `brightness`：（浮点数）范围：`[0.0, 1.0]`。
    调整音调。值越高，音频听起来就越“明亮”，通常会强调高频。
  - `scale`：(Enum)
    设置生成音乐的音阶（调和模式）。使用 SDK 提供的 [`Scale` 枚举值](#scale-enum)。您需要停止/播放或重置模型的上下文，以便模型将新的比例纳入考虑范围。
  - `mute_bass`：（布尔值）默认值：`False`。
    控制模型是否降低输出的低音。
  - `mute_drums`：（布尔值）默认值：`False`。
    控制模型输出是否会减少输出的鼓声。
  - `only_bass_and_drums`：（布尔值）默认值：`False`。
    引导模型尝试仅输出贝斯和鼓。
  - `music_generation_mode`：（枚举）向模型指示它应侧重于音乐的 `QUALITY`（默认值）还是 `DIVERSITY`。也可以将其设置为 `VOCALIZATION`，让模型将发声作为另一种乐器生成（将其添加为新的提示）。
- `PlaybackControl`：用于控制播放方面的命令，例如播放、暂停、停止或重置上下文。

对于 `bpm`、`density`、`brightness` 和 `scale`，如果未提供值，模型将根据您的初始提示决定最佳值。

在 `MusicGenerationConfig` 中，您还可以自定义更多经典参数，例如 `temperature`（0.0 到 3.0，默认值为 1.1）、`top_k`（1 到 1000，默认值为 40）和 `seed`（0 到 2147483647，默认情况下随机选择）。

#### 缩放枚举值

以下是模型可以接受的所有缩放值：

| 枚举值 | 音阶 / 调 |
| --- | --- |
| `C_MAJOR_A_MINOR` | C 大调 / A 小调 |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | D♭ 大调 / B♭ 小调 |
| `D_MAJOR_B_MINOR` | D 大调 / B 小调 |
| `E_FLAT_MAJOR_C_MINOR` | E♭ 大调 / C 小调 |
| `E_MAJOR_D_FLAT_MINOR` | E 大调 / C♯/D♭ 小调 |
| `F_MAJOR_D_MINOR` | F 大调 / D 小调 |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | G♭ 大调 / E♭ 小调 |
| `G_MAJOR_E_MINOR` | G 大调 / E 小调 |
| `A_FLAT_MAJOR_F_MINOR` | A♭ 大调 / F 小调 |
| `A_MAJOR_G_FLAT_MINOR` | A 大调 / F♯/G♭ 小调 |
| `B_FLAT_MAJOR_G_MINOR` | 降 B 大调 / G 小调 |
| `B_MAJOR_A_FLAT_MINOR` | B 大调 / G♯/A♭ 小调 |
| `SCALE_UNSPECIFIED` | 默认值 / 由模型决定 |

该模型能够引导所演奏的音符，但无法区分相对调。因此，每个枚举都同时对应于相对主要版本和次要版本。例如，`C_MAJOR_A_MINOR` 对应于钢琴的所有白键，而 `F_MAJOR_D_MINOR` 对应于除降 B 之外的所有白键。

### 限制

- 仅乐器：模型仅生成乐器音乐。
- 安全性：提示会经过安全过滤器的检查。系统会忽略触发过滤条件的提示，在这种情况下，输出的 `filtered_prompt` 字段中会写入说明。
- 水印：输出音频始终会添加水印，以便根据我们的 [Responsible AI](https://ai.google/responsibility/principles/?hl=zh-cn) 原则进行识别。

## 后续步骤

- 使用 [Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-cn) 生成完整歌曲和人声轨道，
- 了解如何使用 [TTS 模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)生成多人对话，而不是生成音乐，
- 了解如何生成[图片](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)或[视频](https://ai.google.dev/gemini-api/docs/video?hl=zh-cn)，
- Gemini 不会生成音乐或音频，但可以[理解音频文件](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn)，
- 使用 [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn) 与 Gemini 进行实时对话。

如需查看更多代码示例和教程，请探索[食谱](https://github.com/google-gemini/cookbook)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-18。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-18。"],[],[]]
