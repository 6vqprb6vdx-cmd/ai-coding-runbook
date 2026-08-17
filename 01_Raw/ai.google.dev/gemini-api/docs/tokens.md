---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=th
fetched_at: 2026-08-17T02:27:20.946549+00:00
title: "\u0e17\u0e4d\u0e32\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e41\u0e25\u0e30\u0e19\u0e31\u0e1a\u0e42\u0e17\u0e40\u0e04\u0e47\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ทําความเข้าใจและนับโทเค็น

Gemini และโมเดล Generative AI อื่นๆ จะประมวลผลอินพุตและเอาต์พุตที่ระดับความละเอียดที่เรียกว่า *โทเค็น*

**สำหรับโมเดล Gemini โทเค็น 1 รายการจะเทียบเท่ากับอักขระประมาณ 4 ตัว
และโทเค็น 100 รายการจะเทียบเท่ากับคำภาษาอังกฤษประมาณ 60-80 คำ**

## เกี่ยวกับโทเค็น

โทเค็นอาจเป็นอักขระเดียว เช่น `z` หรือคำทั้งคำ เช่น `cat` โดยคำยาวๆ จะถูกแบ่งออกเป็นโทเค็นหลายรายการ ชุดโทเค็นทั้งหมดที่โมเดลใช้เรียกว่าคำศัพท์ และกระบวนการแยกข้อความออกเป็นโทเค็นเรียกว่า *การทำโทเค็น*

เมื่อเปิดใช้การเรียกเก็บเงินแล้ว [ต้นทุนของการเรียกใช้ Gemini API](https://ai.google.dev/pricing?hl=th) จะ
พิจารณาจากจำนวนโทเค็นอินพุตและเอาต์พุตเป็นส่วนหนึ่ง ดังนั้นการรู้วิธี
นับโทเค็นจึงอาจเป็นประโยชน์

## นับโทเค็น

ระบบจะทำโทเค็นอินพุตและเอาต์พุตทั้งหมดของ Gemini API รวมถึงข้อความ ไฟล์รูปภาพ และรูปแบบอื่นๆ ที่ไม่ใช่ข้อความ

คุณนับโทเค็นได้ด้วยวิธีต่อไปนี้

- **เรียกใช้ `count_tokens` ด้วยอินพุตของคำขอ** ซึ่งจะแสดงผลจำนวนโทเค็นทั้งหมดใน *อินพุตเท่านั้น* โดยให้เรียกใช้ฟังก์ชันนี้ก่อนส่งอินพุตเพื่อตรวจสอบขนาดของคำขอ
- **ใช้ `usage` ในการตอบกลับการโต้ตอบ** ซึ่งจะแสดงผลจำนวนโทเค็นสำหรับอินพุต (`total_input_tokens`), เอาต์พุต (`total_output_tokens`), การประมวลผล (`total_thought_tokens`), เนื้อหาที่แคชไว้ (`total_cached_tokens`), การใช้เครื่องมือ (`total_tool_use_tokens`) และทั้งหมด (`total_tokens`)

### นับโทเค็นข้อความ

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.6-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### นับโทเค็นการสนทนาไปมา

นับโทเค็นในประวัติการสนทนาโดยใช้ `previous_interaction_id` ดังนี้

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### นับโทเค็นหลายรูปแบบ

ระบบจะทำโทเค็นอินพุตทั้งหมดของ Gemini API รวมถึงรูปภาพ วิดีโอ และเสียง
โดยมีประเด็นสำคัญเกี่ยวกับการทำโทเค็นดังนี้

- **รูปภาพ**: รูปภาพที่มีขนาด ≤384 พิกเซลในทั้ง 2 มิติจะนับเป็น 258 โทเค็น ส่วนรูปภาพที่ใหญ่กว่าจะถูกแบ่งออกเป็นรูปภาพขนาด 768x768 พิกเซล ซึ่งแต่ละรูปภาพจะนับเป็น 258 โทเค็น
- **วิดีโอ**: 263 โทเค็นต่อวินาที
- **เสียง**: 32 โทเค็นต่อวินาที

#### โทเค็นรูปภาพ

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.6-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**ตัวอย่างข้อมูลแบบอินไลน์**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### โทเค็นวิดีโอ

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### โทเค็นเสียง

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.6-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### นับโทเค็นคำแนะนำของระบบ

คำแนะนำของระบบจะนับเป็นส่วนหนึ่งของโทเค็นอินพุต

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### นับโทเค็นเครื่องมือ

ระบบจะนับเครื่องมือ (ฟังก์ชัน การเรียกใช้โค้ด Google Search) ด้วย

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## หน้าต่างบริบท

โมเดล Gemini แต่ละโมเดลมีจำนวนโทเค็นสูงสุดที่จัดการได้ โดยหน้าต่างบริบทจะกำหนดขีดจำกัดรวมของโทเค็นอินพุตและเอาต์พุต

### รับขนาดหน้าต่างบริบทแบบเป็นโปรแกรม

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.6-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.6-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

ดูขนาดหน้าต่างบริบทได้ในหน้า[โมเดล](https://ai.google.dev/gemini-api/docs/models?hl=th)

## ขั้นตอนถัดไป

- [การสร้างข้อความ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th): ข้อมูลพื้นฐานเกี่ยวกับการสร้าง
- [การแคช](https://ai.google.dev/gemini-api/docs/caching?hl=th): ลดค่าใช้จ่ายด้วยการแคช
- [การตั้งราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th): ทำความเข้าใจค่าใช้จ่าย

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
