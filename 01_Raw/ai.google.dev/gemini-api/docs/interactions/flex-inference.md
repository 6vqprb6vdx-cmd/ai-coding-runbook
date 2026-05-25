---
source_url: https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=zh-TW
fetched_at: 2026-05-25T12:57:22.063583+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 彈性推論

Gemini Flex API 是推論層級，與標準費率相比，可節省 50% 的成本，但延遲時間不固定，且僅盡力提供服務。這項 API 適用於可容許延遲的工作負載，需要同步處理，但不需要標準 API 的即時效能。

## 如何使用 Flex

如要使用 Flex 層級，請在要求中將 `service_tier` 指定為 `flex`。如果省略這個欄位，要求會預設使用標準層級。

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.output_text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: 'gemini-3.5-flash',
            input: 'Analyze this dataset for trends...',
            service_tier: 'flex'
        });
        console.log(interaction.output_text);
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Flex 推論的運作方式

Gemini Flex 推論可彌平標準 API 與 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw) 24 小時處理時間之間的落差。這項服務會利用離峰時段的「可卸除」運算容量，為背景任務和循序工作流程提供符合成本效益的解決方案。

| 功能 | Flex | 優先順序 | 標準 | 批次 |
| --- | --- | --- | --- | --- |
| **定價** | 50% 折扣 | 比 Standard 方案多 75% 至 100% | 全票 | 50% 折扣 |
| **延遲** | 分鐘 (目標：1 到 15 分鐘) | 低 (秒) | 秒到分鐘 | 長達 24 小時 |
| **穩定性** | 盡可能提供最佳服務 (可卸載) | 高 (不會脫落) | 高 / 中高 | 高 (處理量) |
| **介面** | 同步 | 同步 | 同步 | 非同步 |

### 主要優點

- **成本效益**：大幅節省非正式評估、背景代理程式和資料擴充的費用。
- **低摩擦**：只要在現有要求中加入單一參數即可。
- **同步工作流程**：適合用於連續 API 鏈，其中下一個要求取決於前一個要求的輸出內容，因此比 Batch 更適合代理功能工作流程。

### 用途

- **離線評估**：執行「LLM 做為評估者」迴歸測試或排行榜。
- **背景代理**：可接受延遲幾分鐘的循序工作，例如更新客戶關係管理系統、建立個人資料或內容審查。
- **預算不足的研究**：學術實驗需要在預算有限的情況下使用大量權杖。

### 頻率限制

彈性推論流量會計入一般[速率限制](https://aistudio.google.com/rate-limit?hl=zh-tw)，不會像 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw) 一樣提供擴展速率限制。

### 可卸除容量

彈性流量的優先順序較低，如果標準流量突然暴增，系統可能會搶先處理或清除 Flex 請求，確保高優先順序使用者有足夠的容量。如要瞭解高優先順序推論，請參閱「[優先推論](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=zh-tw)」一文。

### 錯誤代碼

如果彈性容量不足或系統壅塞，API 會傳回標準錯誤代碼：

- **503 Service Unavailable**：系統目前工作負載已達上限。
- **429 要求數量過多**：頻率限制或資源耗盡。

### 客戶責任

- **沒有伺服器端備用方案**：為避免產生非預期費用，如果彈性容量已滿，系統不會自動將彈性要求升級為標準層級。
- **重試**：您必須自行實作用戶端重試邏輯，並採用指數輪詢策略。
- **逾時**：由於 Flex 請求可能會排隊等候，建議將用戶端逾時時間延長至 10 分鐘以上，以免連線過早關閉。

## 調整逾時時間

您可以為 REST API 和用戶端程式庫設定個別要求的逾時。請務必確保用戶端逾時時間涵蓋預期的伺服器等待時間範圍 (例如 Flex 等待佇列為 600 秒以上)。SDK 預期的逾時值單位為毫秒。

### 每個要求的逾時時間

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="why is the sky blue?",
        service_tier="flex",
    )
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: "gemini-3.5-flash",
            input: "why is the sky blue?",
            service_tier: "flex",
        }, {timeout: 900000});
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}

await main();
```

## 實作重試機制

由於 Flex 可卸除，且會因 503 錯誤而失敗，因此以下範例說明如何選擇性地實作重試邏輯，以繼續處理失敗的要求：

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.5-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## 定價

彈性推論的價格為[標準 API](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw) 的 50%，並以權杖為單位計費。

## 支援的模型

下列模型支援 Flex 推論：

| 型號 | 彈性推論 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw) | ✔️ |
| [Gemini 3 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-tw) | ✔️ |

## 後續步驟

- [優先推論](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=zh-tw)，實現超低延遲。
- [權杖](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=zh-tw)：瞭解權杖。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-19 (世界標準時間)。"],[],[]]
