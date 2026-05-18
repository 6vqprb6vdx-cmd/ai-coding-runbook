---
source_url: https://ai.google.dev/gemini-api/docs/thought-signatures?hl=th
fetched_at: 2026-05-18T13:11:32.179471+00:00
title: "\u0e25\u0e32\u0e22\u0e40\u0e0b\u0e47\u0e19\u0e04\u0e27\u0e32\u0e21\u0e04\u0e34\u0e14 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ลายเซ็นความคิด

ลายเซ็นความคิดคือการแสดงความคิดภายในของโมเดลที่เข้ารหัสไว้
และใช้เพื่อรักษาบริบทการให้เหตุผลในการโต้ตอบแบบหลายขั้นตอน
เมื่อใช้โมเดลการคิด (เช่น Gemini 3 และซีรีส์ 2.5) API อาจ
แสดงผล`thoughtSignature`ฟิลด์ภายใน[ส่วนเนื้อหา](https://ai.google.dev/api/caching?hl=th#Part)
ของการตอบกลับ (เช่น ส่วน `text` หรือ `functionCall`)

โดยทั่วไปแล้ว หากคุณได้รับลายเซ็นความคิดในคำตอบของโมเดล คุณควรส่งลายเซ็นกลับไปตามที่ได้รับเมื่อส่งประวัติการสนทนาในรอบถัดไป
**เมื่อใช้โมเดล Gemini 3 คุณต้องส่งลายเซ็นความคิดกลับมาในระหว่างการเรียกใช้ฟังก์ชัน ไม่เช่นนั้นคุณจะได้รับข้อผิดพลาดในการตรวจสอบ** (รหัสสถานะ 4xx)
ซึ่งรวมถึงเมื่อใช้การตั้งค่า`minimal`
[ระดับการคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th#thinking-levels)สำหรับ Gemini 3
Flash

## วิธีการทำงาน

กราฟิกด้านล่างแสดงความหมายของ "เทิร์น" และ "ขั้นตอน" ที่เกี่ยวข้องกับ[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)ใน Gemini API "เทิร์น"
คือการแลกเปลี่ยนที่สมบูรณ์ครั้งเดียวในการสนทนาระหว่างผู้ใช้กับโมเดล "ขั้นตอน" คือการดำเนินการหรือการทำงานที่ละเอียดขึ้นซึ่งโมเดลดำเนินการ โดยมักเป็นส่วนหนึ่งของกระบวนการที่ใหญ่ขึ้นเพื่อดำเนินการให้เสร็จสมบูรณ์

![แผนภาพการเรียกใช้ฟังก์ชันและขั้นตอน](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=th)

*เอกสารนี้มุ่งเน้นที่การจัดการการเรียกใช้ฟังก์ชันสำหรับโมเดล Gemini 3 ดูส่วน[ลักษณะการทำงานของโมเดล](#model-behavior)สำหรับความคลาดเคลื่อนกับ 2.5*

Gemini 3 จะแสดงลายเซ็นความคิดสำหรับคำตอบของโมเดลทั้งหมด (คำตอบจาก API) พร้อมการเรียกใช้ฟังก์ชัน ลายเซ็นความคิดจะปรากฏในกรณีต่อไปนี้

- เมื่อมีการเรียกใช้[ฟังก์ชันแบบขนาน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#parallel_function_calling)
  ส่วนการเรียกใช้ฟังก์ชันแรกที่การตอบกลับของโมเดลส่งคืนจะมี
  ลายเซ็นความคิด
- เมื่อมีการเรียกใช้ฟังก์ชันตามลำดับ (หลายขั้นตอน) การเรียกใช้ฟังก์ชันแต่ละครั้งจะมี
  ลายเซ็น และคุณต้องส่งลายเซ็นทั้งหมดกลับ
- คำตอบของโมเดลที่ไม่มีการเรียกใช้ฟังก์ชันจะแสดงลายเซ็นความคิดภายใน
  ส่วนสุดท้ายที่โมเดลแสดง

ตารางต่อไปนี้แสดงภาพการเรียกใช้ฟังก์ชันแบบหลายขั้นตอน
โดยรวมคำจำกัดความของเทิร์นและขั้นตอนเข้ากับแนวคิดของลายเซ็น
ที่แนะนำไว้ข้างต้น

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **เลี้ยว** | **Step** | **คำขอของผู้ใช้** | **คำตอบของโมเดล** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | ไม่มี |

## ลายเซ็นในส่วนการเรียกใช้ฟังก์ชัน

เมื่อ Gemini สร้าง `functionCall` จะใช้ `thought_signature`
เพื่อประมวลผลเอาต์พุตของเครื่องมืออย่างถูกต้องในรอบถัดไป

- **พฤติกรรม**
  - **การเรียกฟังก์ชันเดียว**: ส่วน `functionCall` จะมี `thought_signature`
  - **การเรียกใช้ฟังก์ชันแบบขนาน**: หากโมเดลสร้างการเรียกใช้ฟังก์ชันแบบขนาน
    ในการตอบกลับ ระบบจะแนบ `thought_signature` **เฉพาะกับส่วนแรก**
    `functionCall` ส่วน `functionCall` ที่ตามมาในการตอบกลับเดียวกันจะ**ไม่มี**ลายเซ็น
- **ข้อกำหนด**: คุณ**ต้อง**ส่งคืนลายเซ็นนี้ในส่วนที่ได้รับเมื่อส่งประวัติการสนทนากลับ
- **การตรวจสอบ**: มีการบังคับใช้การตรวจสอบอย่างเข้มงวดสำหรับการเรียกใช้ฟังก์ชันทั้งหมดภายใน
  เทิร์นปัจจุบัน (ต้องเป็นเทิร์นปัจจุบันเท่านั้น เราไม่ตรวจสอบเทิร์นก่อนหน้า)
  - API จะย้อนกลับไปในประวัติ (ใหม่สุดไปเก่าสุด) เพื่อค้นหาข้อความ**ผู้ใช้**ล่าสุดที่มีเนื้อหามาตรฐาน (เช่น `text`) ( ซึ่งจะเป็นจุดเริ่มต้นของเทิร์นปัจจุบัน) การดำเนินการนี้จะไม่**be**`functionResponse`
  - **การตอบกลับ**ของโมเดล`functionCall`ทั้งหมดที่เกิดขึ้นหลังจากข้อความการใช้งานเฉพาะนั้นจะถือเป็นส่วนหนึ่งของการตอบกลับ
  - ส่วน`functionCall`**แรก**ใน**แต่ละขั้นตอน**ของเทิร์นปัจจุบัน**ต้อง**มี`thought_signature`ของส่วนนั้น
  - หากคุณละเว้น `thought_signature` สำหรับส่วน `functionCall` แรกในขั้นตอนใดก็ตามของเทิร์นปัจจุบัน คำขอจะล้มเหลวพร้อมข้อผิดพลาด 400
- **หากไม่ได้รับลายเซ็นที่ถูกต้อง คุณจะได้รับข้อผิดพลาดดังนี้**
  - โมเดล Gemini 3: การไม่ใส่ลายเซ็นจะทำให้เกิดข้อผิดพลาด 400 ข้อความจะมีรูปแบบดังนี้
    - การเรียกใช้ฟังก์ชัน `<Function Call>` ในบล็อกเนื้อหา `<index of contents array>`
      ไม่มี `thought_signature` เช่น *Function
      call `FC1` ในบล็อกเนื้อหา `1.` ไม่มี `thought_signature`*

### ตัวอย่างการเรียกใช้ฟังก์ชันแบบต่อเนื่อง

ส่วนนี้แสดงตัวอย่างการเรียกใช้ฟังก์ชันหลายรายการที่ผู้ใช้ถาม
คำถามที่ซับซ้อนซึ่งต้องใช้หลายงาน

มาดูตัวอย่างการเรียกใช้ฟังก์ชันแบบหลายรอบที่ผู้ใช้ถามคำถามที่ซับซ้อนซึ่งต้องทำหลายอย่างกัน `"Check flight status for AA100 and
book a taxi if delayed"`

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **เลี้ยว** | **Step** | **คำขอของผู้ใช้** | **คำตอบของโมเดล** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

โค้ดต่อไปนี้แสดงลำดับในตารางด้านบน

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำขอของผู้ใช้)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "check_flight",
          "description": "Gets the current status of a flight",
          "parameters": {
            "type": "object",
            "properties": {
              "flight": {
                "type": "string",
                "description": "The flight number to check"
              }
            },
            "required": [
              "flight"
            ]
          }
        },
        {
          "name": "book_taxi",
          "description": "Book a taxi",
          "parameters": {
            "type": "object",
            "properties": {
              "time": {
                "type": "string",
                "description": "time to book the taxi"
              }
            },
            "required": [
              "time"
            ]
          }
        }
      ]
    }
  ]
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำตอบของโมเดล)**

```
{
"content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>"
          }
        ]
  }
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 2 (การตอบกลับของผู้ใช้ - การส่งเอาต์พุตของเครื่องมือ)** เนื่องจากเทิร์นของผู้ใช้รายนี้มีเพียง `functionResponse` (ไม่มีข้อความใหม่) เราจึงยังอยู่ในเทิร์นที่ 1 เราต้องอนุรักษ์`<Signature_A>`

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
                }
              }
            }
        ]
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 2 (โมเดล)** ตอนนี้โมเดลตัดสินใจจองแท็กซี่ตาม
เอาต์พุตของเครื่องมือก่อนหน้า

```
{
      "content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>"
          }
        ]
      }
}
```

**Turn 1, Step 3 (User - Sending tool output)** หากต้องการส่งการยืนยันการจองแท็กซี่
เราต้องใส่ลายเซ็นสำหรับการเรียกใช้ฟังก์ชัน**ทั้งหมด**ในลูปนี้
(`<Signature A>` + `<Signature B>`)

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
              }
              }
            }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "book_taxi",
              "response": {
                "booking_status": "success"
              }
              }
            }
        ]
    }
}
```

### ตัวอย่างการเรียกใช้ฟังก์ชันแบบขนาน

มาดูตัวอย่างการเรียกใช้ฟังก์ชันแบบขนานที่ผู้ใช้ขอ
`"Check weather in Paris and London"` เพื่อดูว่าโมเดลทําการตรวจสอบที่ใด

| **เลี้ยว** | **Step** | **คำขอของผู้ใช้** | **คำตอบของโมเดล** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("ปารีส") + ลายเซ็น  FC2 ("ลอนดอน") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (ไม่มี FC) | ไม่มี |

โค้ดต่อไปนี้แสดงลำดับในตารางด้านบน

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำขอของผู้ใช้)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำตอบของโมเดล)**

```
{
  "content": {
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "Paris"
          }
        },
        "thoughtSignature": "<Signature_A>"// INCLUDED on First FC
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "London"
          }// NO signature on subsequent parallel FCs
        }
      }
    ]
  }
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 2 (การตอบกลับของผู้ใช้ - การส่งเอาต์พุตของเครื่องมือ)** เราต้องเก็บรักษา
`<Signature_A>` ส่วนแรกไว้ตามที่ได้รับ

```
[
  {
    "role": "user",
    "parts": [
      {
        "text": "Check the weather in Paris and London."
      }
    ]
  },
  {
    "role": "model",
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "Paris"
          }
        },
        "thought_signature": "<Signature_A>" // MUST BE INCLUDED
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "London"
          }
        }
      } // NO SIGNATURE FIELD
    ]
  },
  {
    "role": "user",
    "parts": [
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "15C"
          }
        }
      },
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "12C"
          }
        }
      }
    ]
  }
]
```

## ลายเซ็นในส่วนที่ไม่ใช่ `functionCall`

นอกจากนี้ Gemini ยังอาจแสดง `thought_signatures` ในส่วนสุดท้ายของคำตอบ
ในส่วนที่ไม่ได้เรียกใช้ฟังก์ชันด้วย

- **ลักษณะการทำงาน**: ส่วนเนื้อหาสุดท้าย (`text, inlineData…`) ที่โมเดลส่งคืนอาจมี `thought_signature`
- **คำแนะนำ**: **ขอแนะนำ**ให้ส่งคืนลายเซ็นเหล่านี้เพื่อให้มั่นใจว่าโมเดลจะยังคงให้เหตุผลคุณภาพสูง โดยเฉพาะอย่างยิ่งสำหรับการปฏิบัติตามคำสั่งที่ซับซ้อน หรือเวิร์กโฟลว์ของเอเจนต์จำลอง
- **การตรวจสอบ**: API **ไม่ได้**บังคับใช้การตรวจสอบอย่างเคร่งครัด คุณจะไม่ได้รับข้อผิดพลาดเกี่ยวกับการบล็อกหากละเว้นการระบุ แต่ประสิทธิภาพอาจลดลง

### การให้เหตุผลตามข้อความ/ในบริบท (ไม่มีการตรวจสอบ)

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำตอบของโมเดล)**

```
{
  "role": "model",
  "parts": [
    {
      "text": "I need to calculate the risk. Let me think step-by-step...",
      "thought_signature": "<Signature_C>" // OPTIONAL (Recommended)
    }
  ]
}
```

**เทิร์นที่ 2 ขั้นตอนที่ 1 (ผู้ใช้)**

```
[
  { "role": "user", "parts": [{ "text": "What is the risk?" }] },
  {
    "role": "model", 
    "parts": [
      {
        "text": "I need to calculate the risk. Let me think step-by-step...",
        // If you omit <Signature_C> here, no error will occur.
      }
    ]
  },
  { "role": "user", "parts": [{ "text": "Summarize it." }] }
]
```

## ลายเซ็นเพื่อความเข้ากันได้กับ OpenAI

ตัวอย่างต่อไปนี้แสดงวิธีจัดการลายเซ็นความคิดสำหรับ API การเติมข้อความแชทโดยใช้[ความเข้ากันได้ของ OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=th)

### ตัวอย่างการเรียกใช้ฟังก์ชันแบบต่อเนื่อง

นี่คือตัวอย่างการเรียกใช้ฟังก์ชันหลายรายการที่ผู้ใช้ถามคำถามที่ซับซ้อน
ซึ่งต้องใช้หลายงาน

มาดูตัวอย่างการเรียกใช้ฟังก์ชันแบบหลายรอบที่ผู้ใช้ถามว่า
`Check flight status for AA100 and book a taxi if delayed` และคุณจะเห็นว่า
เกิดอะไรขึ้นเมื่อผู้ใช้ถามคำถามที่ซับซ้อนซึ่งต้องใช้หลายงาน

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **เลี้ยว** | **Step** | **คำขอของผู้ใช้** | **คำตอบของโมเดล** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

โค้ดต่อไปนี้จะแสดงลำดับที่ระบุ

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำขอของผู้ใช้)**

```
{
  "model": "google/gemini-3.1-pro-preview",
  "messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "check_flight",
        "description": "Gets the current status of a flight",
        "parameters": {
          "type": "object",
          "properties": {
            "flight": {
              "type": "string",
              "description": "The flight number to check."
            }
          },
          "required": [
            "flight"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "book_taxi",
        "description": "Book a taxi",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "time to book the taxi"
            }
          },
          "required": [
            "time"
          ]
        }
      }
    }
  ]
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำตอบของโมเดล)**

```
{
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>"
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    }
```

**เทิร์นที่ 1 ขั้นตอนที่ 2 (การตอบกลับของผู้ใช้ - การส่งเอาต์พุตของเครื่องมือ)**

เนื่องจากเทิร์นของผู้ใช้นี้มีเพียง `functionResponse` (ไม่มีข้อความใหม่) เราจึงยังอยู่ในเทิร์นที่ 1 และต้องเก็บ `<Signature_A>` ไว้

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    }
  ]
```

**เทิร์นที่ 1 ขั้นตอนที่ 2 (โมเดล)**

ตอนนี้โมเดลจะตัดสินใจจองแท็กซี่โดยอิงตามเอาต์พุตของเครื่องมือก่อนหน้า

```
{
"role": "model",
"tool_calls": [
{
"extra_content": {
"google": {
"thought_signature": "<Signature B>"
}
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-2",
            "type": "function"
          }
       ]
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 3 (ผู้ใช้ - ส่งเอาต์พุตของเครื่องมือ)**

หากต้องการส่งการยืนยันการจองแท็กซี่ เราต้องใส่ลายเซ็นสำหรับการเรียกใช้ฟังก์ชันทั้งหมดในลูปนี้ (`<Signature A>` + `<Signature B>`)

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature B>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "book_taxi",
      "tool_call_id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
      "content": "{\"booking_status\":\"success\"}"
    }
  ]
```

### ตัวอย่างการเรียกใช้ฟังก์ชันแบบขนาน

มาดูตัวอย่างการเรียกใช้ฟังก์ชันแบบขนานที่ผู้ใช้ถามว่า
`"Check weather in Paris and London"` และคุณจะเห็นว่าโมเดลทำการตรวจสอบ
ที่ใด

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **เลี้ยว** | **Step** | **คำขอของผู้ใช้** | **คำตอบของโมเดล** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

นี่คือโค้ดที่จะใช้เพื่อดูข้อมูลในลำดับที่ระบุ

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำขอของผู้ใช้)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 1 (คำตอบของโมเดล)**

```
{
"role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Signature returned
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": {
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function" // No signature on Parallel FC
          }
        ]
}
```

**เทิร์นที่ 1 ขั้นตอนที่ 2 (การตอบกลับของผู้ใช้ - การส่งเอาต์พุตของเครื่องมือ)**

คุณต้องเก็บรักษา `<Signature_A>` ในส่วนแรกให้ตรงตามที่ได้รับ

```
"messages": [
    {
      "role": "user",
      "content": "Check the weather in Paris and London."
    },
    {
      "role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": { //No Signature
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function"
          }
        ]
    },
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
      "content": "{\"temp\":\"15C\"}"
    },    
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
      "content": "{\"temp\":\"12C\"}"
    }
  ]
```

## คำถามที่พบบ่อย

1. **ฉันจะโอนประวัติจากโมเดลอื่นไปยัง Gemini 3 โดยมีส่วนการเรียกใช้ฟังก์ชันในเทิร์นและขั้นตอนปัจจุบันได้อย่างไร ฉันต้องระบุส่วนการเรียกใช้ฟังก์ชัน
   ที่ API ไม่ได้สร้างขึ้นและจึงไม่มีลายเซ็นความคิดที่เชื่อมโยงใช่ไหม**

   แม้ว่าเราจะไม่แนะนำอย่างยิ่งให้แทรกบล็อกการเรียกใช้ฟังก์ชันที่กำหนดเองลงในคำขอ แต่ในกรณีที่หลีกเลี่ยงไม่ได้ เช่น การให้ข้อมูลแก่โมเดลเกี่ยวกับการเรียกใช้ฟังก์ชันและการตอบกลับที่ไคลเอ็นต์ดำเนินการอย่างแน่นอน หรือการโอนการติดตามจากโมเดลอื่นที่ไม่มีลายเซ็นความคิด คุณสามารถตั้งค่าลายเซ็นจำลองต่อไปนี้ของ `"context_engineering_is_the_way_to_go"` หรือ `"skip_thought_signature_validator"` ในช่องลายเซ็นความคิดเพื่อข้ามการตรวจสอบได้
2. **ฉันส่งการเรียกใช้ฟังก์ชันและการตอบกลับแบบขนานที่สลับกัน และ
   API แสดงผล 400 ทำไมจึงเป็นเช่นนั้น**

   เมื่อ API แสดงผลการเรียกใช้ฟังก์ชันแบบขนาน "FC1 + ลายเซ็น, FC2" การตอบกลับจากผู้ใช้ที่คาดหวังคือ "FC1 + ลายเซ็น, FC2, FR1, FR2" หากคุณมีข้อมูลที่
   สลับกันเป็น "FC1 + ลายเซ็น, FR1, FC2, FR2" API จะแสดงข้อผิดพลาด 400
3. **เมื่อสตรีมและโมเดลไม่แสดงผลการเรียกใช้ฟังก์ชัน ฉันจะหาลายเซ็นความคิดไม่เจอ**

   ในระหว่างการตอบกลับของโมเดลที่ไม่มี FC พร้อมคำขอสตรีม โมเดลอาจแสดงลายเซ็นความคิดในส่วนที่มีเนื้อหาข้อความว่างเปล่า ขอแนะนำให้แยกวิเคราะห์คำขอทั้งหมดจนกว่าโมเดลจะส่งคืน `finish_reason`

## ลายเซ็นความคิดสำหรับโมเดลต่างๆ

[โมเดล Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=th#gemini-3) และโมเดล Gemini 2.5
จะทำงานแตกต่างกันเมื่อมีการลงนามความคิดในการเรียกใช้ฟังก์ชัน

- หากมีการเรียกใช้ฟังก์ชันในการตอบกลับ
  - Gemini 3 จะมีลายเซ็นในส่วนการเรียกใช้ฟังก์ชันแรกเสมอ
    คุณ**ต้อง**ส่งคืนชิ้นส่วนดังกล่าว
  - Gemini 2.5 จะมีลายเซ็นในส่วนแรก (ไม่ว่าจะเป็น
    ประเภทใดก็ตาม) คุณ**ไม่จำเป็น**ต้องส่งคืนชิ้นส่วนดังกล่าว
- หากไม่มีการเรียกใช้ฟังก์ชันในการตอบกลับ
  - Gemini 3 จะมีลายเซ็นในส่วนสุดท้ายหากโมเดลสร้างความคิด
  - Gemini 2.5 จะไม่มีลายเซ็นในส่วนใดๆ

ดูรายละเอียดการเปรียบเทียบเพิ่มเติมได้ที่หน้า[การคิด](https://ai.google.dev/gemini-api/docs/thinking?hl=th#signatures)
สำหรับโมเดลรูปภาพ Gemini 3 โปรดดูส่วนกระบวนการคิดของคู่มือ[การสร้างรูปภาพ](https://ai.google.dev/gemini-api/docs/image-generation?hl=th#thinking-process)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-08 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-08 UTC"],[],[]]
