---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=zh-TW
fetched_at: 2026-07-06T05:07:59.050954+00:00
title: "\u601d\u60f3\u7279\u5fb5 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 思想特徵

想法簽章是模型內部思考過程的加密表示法，用於在多步驟互動中保留推理背景資訊。使用思考模型 (例如 Gemini 3 和 2.5 系列) 時，API 可能會在回應的[內容部分](https://ai.google.dev/api/caching?hl=zh-tw#Part)中傳回 `thoughtSignature` 欄位 (例如 `text` 或 `functionCall` 部分)。

一般來說，如果模型回覆中包含思維簽章，您應該在下一個回合傳送對話記錄時，完全按照收到的內容傳回該簽章。**使用 Gemini 3 模型時，您必須在函式呼叫期間傳回思維簽章，否則會收到驗證錯誤** (4xx 狀態碼)。包括使用 Gemini 3 Flash 的`minimal`
[思考程度](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw#thinking-levels)設定時。

## 運作方式

下圖以視覺化方式呈現「回合」和「步驟」的意義，與 Gemini API 中的[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)相關。「回合」是指使用者與模型之間一次完整的對話。「步驟」是指模型執行的更精細動作或作業，通常是完成回合的較大程序之一。

![函式呼叫回合和步驟圖](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=zh-tw)

*本文著重於處理 Gemini 3 模型的函式呼叫。如要瞭解與 2.5 的差異，請參閱「[模型行為](#model-behavior)」一節。*

Gemini 3 會針對所有模型回覆 (API 回覆) 傳回思維簽章，並呼叫函式。在下列情況中會顯示想法簽名：

- 如果出現[平行函式](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#parallel_function_calling)呼叫，模型回應傳回的第一個函式呼叫部分會包含想法簽章。
- 如果有多個連續函式呼叫 (多步驟)，每個函式呼叫都會有簽章，您必須將所有簽章傳回。
- 如果模型回應未呼叫函式，模型傳回的最後一部分會包含思維簽章。

下表以視覺化方式呈現多步驟函式呼叫，並結合回合和步驟的定義，以及上述簽章的概念：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **開啟** | **Step** | **使用者要求** | **模型回應** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | 無 |

## 函式呼叫部分的簽章

Gemini 生成 `functionCall` 時，會依據 `thought_signature` 在下一個回合中正確處理工具的輸出內容。

- **行為**：
  - **單一函式呼叫**：`functionCall` 部分會包含 `thought_signature`。
  - **平行函式呼叫**：如果模型在回覆中生成平行函式呼叫，`thought_signature` 只會附加至**第一個**
    `functionCall` 部分。同一回應中的後續 `functionCall` 部分**不會**包含簽章。
- **必要條件**：傳回對話記錄時，您**必須**在收到簽章的確切位置傳回簽章。
- **驗證**：系統會對目前回合內的所有函式呼叫強制執行嚴格驗證。(只需要目前輪次，我們不會驗證先前的輪次)
  - API 會回溯記錄 (從最新到最舊)，找出包含標準內容 (例如 `text`) 的最新**使用者**訊息 (這會是目前回合的開頭)。這不會**be** `functionResponse`。
  - 在該特定使用訊息之後發生的**所有**模型 `functionCall` 回合，都視為該回合的一部分。
  - 目前回合**每個步驟**的**第一個** `functionCall` 部分**必須**包含 `thought_signature`。
  - 如果在目前回合的任何步驟中，省略第一個 `functionCall` 部分的 `thought_signature`，要求就會失敗並顯示 400 錯誤。
- **如果未傳回正確簽章，您會收到以下錯誤訊息**：
  - Gemini 3 模型：如未加入簽章，就會發生 400 錯誤。文字格式如下：
    - `<index of contents array>` 內容區塊中的函式呼叫 `<Function Call>` 缺少 `thought_signature`。舉例來說，*`1.` 內容區塊中的函式呼叫 `FC1` 缺少 `thought_signature`。*

### 循序函式呼叫範例

這個部分會顯示多個函式呼叫的範例，使用者提出需要多項工作的複雜問題。

我們來逐步瞭解多輪函式呼叫範例，使用者提出需要多項工作的複雜問題：`"Check flight status for AA100 and
book a taxi if delayed"`。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **開啟** | **Step** | **使用者要求** | **模型回應** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

下列程式碼說明上表中的序列。

**第 1 輪，步驟 1 (使用者要求)**

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

**第 1 回合第 1 步 (模型回覆)**

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

**第 1 輪第 2 步 (使用者回覆 - 傳送工具輸出內容)**由於這個使用者回合只包含 `functionResponse` (沒有新文字)，我們仍處於第 1 輪。我們必須保留 `<Signature_A>`。

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

**第 1 輪，步驟 2 (模型)**：模型現在會根據先前的工具輸出內容，決定是否預約計程車。

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

**第 1 輪，步驟 3 (使用者 - 傳送工具輸出內容)**：如要傳送計程車預約確認訊息，我們必須在這個迴圈中加入**所有**函式呼叫的簽章 (`<Signature A>` + `<Signature B>`)。

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

### 平行函式呼叫範例

我們來看看平行函式呼叫的範例，使用者要求 `"Check weather in Paris and London"` 查看模型驗證的位置。

| **開啟** | **Step** | **使用者要求** | **模型回應** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 (「巴黎」) + 簽名  FC2 (「倫敦」) | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (no FCs) | 無 |

下列程式碼說明上表中的序列。

**第 1 輪，步驟 1 (使用者要求)**

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

**第 1 回合，步驟 1 (模型回覆)**

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

**第 1 輪，步驟 2 (使用者回應 - 傳送工具輸出內容)** 我們必須保留第一部分，`<Signature_A>`與收到的內容完全一致。

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

## 非 `functionCall` 部分的簽章

在非函式呼叫的部分，Gemini 也可能會在回覆的最後部分傳回 `thought_signatures`。

- **行為**：模型傳回的最終內容部分 (`text, inlineData…`) 可能包含 `thought_signature`。
- **建議**：**建議**傳回這些簽章，確保模型維持高品質的推論能力，特別是複雜的指令遵循或模擬 Agentic Workflows。
- **驗證**：API「不會」嚴格執行驗證。如果省略這些屬性，您不會收到封鎖錯誤，但效能可能會降低。

### 文字/情境推論 (無驗證)

**第 1 回合，步驟 1 (模型回覆)**

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

**第 2 回合，步驟 1 (使用者)**

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

## OpenAI 相容性簽章

以下範例說明如何使用 [OpenAI 相容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw)，處理聊天完成 API 的想法簽章。

### 循序函式呼叫範例

以下範例說明如何多次呼叫函式。使用者提出複雜問題，需要執行多項工作。

讓我們逐步瞭解多輪函式呼叫的範例，使用者會提出`Check flight status for AA100 and book a taxi if delayed`，您可以查看使用者提出需要多項工作的複雜問題時，會發生什麼情況。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **開啟** | **Step** | **使用者要求** | **模型回應** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

下列程式碼會逐步說明指定序列。

**第 1 輪，步驟 1 (使用者要求)**

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

**第 1 輪，步驟 1 (模型回應)**

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

**第 1 回合，步驟 2 (使用者回應 - 傳送工具輸出內容)**

由於這個使用者回合只包含 `functionResponse` (沒有新文字)，我們仍處於回合 1，因此必須保留 `<Signature_A>`。

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

**第 1 輪，步驟 2 (模型)**

模型現在會根據先前的工具輸出內容，決定是否預約計程車。

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

**第 1 輪，步驟 3 (使用者 - 傳送工具輸出內容)**

如要傳送計程車預約確認訊息，我們必須在這個迴圈中加入所有函式呼叫的簽章 (`<Signature A>` + `<Signature B>`)。

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

### 平行函式呼叫範例

我們來看看平行函式呼叫的範例，使用者會提出`"Check weather in Paris and London"`，您可以看到模型進行驗證的位置。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **開啟** | **Step** | **使用者要求** | **模型回應** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

以下是逐步瞭解指定序列的程式碼。

**第 1 輪，步驟 1 (使用者要求)**

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

**第 1 輪，步驟 1 (模型回應)**

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

**第 1 回合，步驟 2 (使用者回應 - 傳送工具輸出內容)**

您必須保留第一部分的 `<Signature_A>`，與收到的內容完全一致。

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

## 常見問題

1. **如何將其他模型的記錄轉移至 Gemini 3，並在目前的輪次和步驟中加入函式呼叫部分？我需要提供 API 未生成的函式呼叫部分，因此沒有相關聯的思維簽章嗎？**

   強烈建議不要將自訂函式呼叫區塊插入要求中，但如果無法避免，例如向模型提供由用戶端確定執行的函式呼叫和回應資訊，或是從不含想法簽章的其他模型轉移追蹤記錄，您可以在想法簽章欄位中設定 `"context_engineering_is_the_way_to_go"` 或 `"skip_thought_signature_validator"` 的虛擬簽章，略過驗證。
2. **我傳回交錯的平行函式呼叫和回應，但 API 傳回 400。為什麼？**

   如果 API 傳回平行函式呼叫「FC1 + 簽章、FC2」，預期使用者回應為「FC1 + 簽章、FC2、FR1、FR2」。如果交錯排列為「FC1 + 簽章、FR1、FC2、FR2」，API 會傳回 400 錯誤。
3. **串流時，如果模型未傳回函式呼叫，我找不到想法簽章**

   在模型回覆期間，如果串流要求不含 FC，模型可能會在文字內容空白的部分傳回想法簽章。建議您剖析整個要求，直到模型傳回 `finish_reason` 為止。

## 不同模型的想法簽名

[Gemini 3 模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#gemini-3)和 Gemini 2.5 模型在函式呼叫中，會以不同方式處理思考簽章：

- 如果回覆中包含函式呼叫，
  - Gemini 3 一律會在第一個函式呼叫部分加上簽章。
    **必須**退回該零件。
  - Gemini 2.5 會在第一部分加上簽名 (無論類型為何)。**選填**：退回該部分。
- 如果回覆中沒有函式呼叫，- 如果模型生成想法，Gemini 3 會在最後一部分加上簽名。
  - Gemini 2.5 不會在任何部分加上簽名。

如需比較詳細資料，請參閱「[Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw#signatures)」頁面。如要瞭解 Gemini 3 Image 模型的思考過程，請參閱「[圖片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw#thinking-process)」指南的思考過程部分。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-22 (世界標準時間)。"],[],[]]
