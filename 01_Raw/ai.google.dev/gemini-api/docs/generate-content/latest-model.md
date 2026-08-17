---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=zh-TW
fetched_at: 2026-08-17T02:20:12.114824+00:00
title: "\u4f7f\u7528\u6700\u65b0 Gemini \u6a21\u578b \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用最新 Gemini 模型

[本頁](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=zh-tw)

Gemini 3.6 Flash (`gemini-3.6-flash`) 和 Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) 正式發布，可供正式版使用。

- **Gemini 3.6 Flash**：在複雜的代理式和多模態任務中展現更強大的效能，同時減少權杖用量，價格也比 3.5 Flash 更低。
- **Gemini 3.5 Flash-Lite**：3.5 系列中速度最快、成本最低的模型。執行高輸送量作業時，效能優於先前的 Flash-Lite 版本。

本指南將說明各模型的新功能、影響程式碼的 API 變更，以及如何遷移。

### Gemini 3.6 Flash

1. 安裝技能：

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 套用技能：

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. 安裝技能：

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 套用技能：

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## 全新模型

| 模型 | 模型 ID | 預設思考程度 | 定價 | 說明 |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 每 100 萬個輸入權杖 $1.50 美元，每 100 萬個輸出權杖 $7.50 美元 | 兼顧速度與智慧，適用於代理式和多模態工作。 |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 每 100 萬個輸入詞元 $0.30，每 100 萬個輸出詞元 $2.50 | 速度最快、成本最低的 3.5 模型，適合執行高輸送量作業。 |

這兩款模型都支援 100 萬個詞元的脈絡窗口、最多 64,000 個輸出詞元、思考功能，以及全套內建工具，包括[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)。

如需完整規格，請參閱以下型號頁面：

- [Gemini 3.6 Flash 模型頁面](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-tw)
- [Gemini 3.5 Flash-Lite 模型頁面](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-tw)

如需詳細定價資訊，請參閱[定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。

## 快速入門導覽課程

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## Gemini 3.6 Flash 的新功能

- **減少詞元和對話回合：**完成多步驟工作流程時，所需的推論步驟、對話回合和工具呼叫次數，都比 Gemini 3.5 少。這項功能也能減少執行迴圈螺旋。
- **提升程式碼生成品質：**生成可直接用於正式環境的程式碼，減少不必要的編輯和偵錯迴圈。
- **更準確地遵循指令**：減少診斷工作期間不必要的檔案變更。
- **強大的多模態和空間推論能力：**提升圖表解讀、視覺藍圖轉換和多元素網頁版面配置生成方面的效能。
- **預先進行程式輔助檢查：**相較於 Gemini 3.5 Flash，Gemini 1.0 Pro 更常在進行變更前執行診斷程式碼指令碼。這項功能可提高複雜工作的準確度，但可能會在簡單的前端工作中增加額外的探索步驟。
- **支援電腦使用：**支援做為代理 UI 自動化的原生工具。
- **UI 樣式偏好**：更擅長建立實用程式碼，但人類評估人員偏好先前模型產生的視覺版面配置和樣式。您可以提供明確的設計規範，藉此減輕這個問題。
- **預設思考程度 (中)：**與 Gemini 3.5 Flash 使用相同的 `medium` 預設思考程度。
- **價格更低**：輸出權杖費用較低 (每 100 萬個權杖 $7.50 美元，3.5 Flash 則為每 100 萬個權杖 $9.00 美元)。輸入權杖的價格仍為每 100 萬個 $1.50 美元。

## Gemini 3.5 Flash-Lite 最新消息

- **縮短工作執行延遲時間：**在 3.5 系列中，這是處理大量資料剖析和文件擷取作業時，總處理量最高的模型。
- **更強大的推論和多模態效能：**從 Gemini 2.5 Flash 順利遷移，在 HLE (18.0% vs. 11.0%) 等推論任務和 CharXIV (74.5% vs. 63.7%) 等多模態基準測試中，獲得更高的分數。
- **子代理程式自動化調度管理和工具可靠性：**提升執行程式碼、搜尋和 MCP 工作流程的工具執行可靠性。提高自主規劃和複雜子代理程式任務的思考層次。
- **提升文件理解能力：**提高文件剖析和結構化資料擷取的準確度。視文件複雜度，嘗試使用最低和最高思考程度。
- **互動式網頁程式碼編寫和表格資料處理：**透過輕量型執行程式碼作業進行規劃，在前端 JavaScript 和表格資料處理方面表現出色。
- **聊天機器人和角色設定持續性：**相較於 Gemini 3.1 Flash-Lite，Gemini 1.5 Pro 在多輪對話中能更準確地遵循指令，並維持角色設定一致性。
- **支援電腦使用：**支援做為代理 UI 自動化的原生工具。

## 選擇合適的 Flash 或 Flash-Lite 模型

請參閱下表，為工作負載選擇合適的模型和遷移路徑。

這兩個模型都必須移除已淘汰的取樣參數 (`temperature`、`top_p`、`top_k`) 和預先填入的模型輪流。詳情請參閱「[API 變更](#api-changes-and-parameter-updates)」。

| 模型 | 主要應用實例 | 建議的遷移目標 |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | 程式碼生成、空間/多模態推論、多步驟代理工作流程 | **Gemini 3.5 Flash**、**Gemini 3 Flash (預先發布版)** 或 **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | 自主執行子代理程式、大量資料分析和文件擷取、結構化 JSON 剖析 | **Gemini 3.1 Flash-Lite** 或 **Gemini 2.5 Flash** |

## 更新 Antigravity 代理程式

由於效能提升，Gemini 3.6 Flash 現在是 Gemini Managed Agents 中 [Antigravity 代理程式](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=zh-tw)的全新預設模型。如要變更這項設定，請在 API 中設定新欄位。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## API 變更和參數更新

從 Gemini 3.6 Flash 和 Gemini 3.5 Flash-Lite 開始，下列 API 變更會套用至這些模型和日後發布的所有 Gemini 模型。

- **淘汰取樣參數**：`temperature`、`top_p` 和 `top_k` 已淘汰。API 會忽略這些參數，並在日後的模型生成作業中傳回錯誤。
- **預先填入模型輪次驗證**：系統不再支援預先填入模型輪次。如果要求中最後一個非空白的輪流是 `model` 輪流，API 會傳回 `400` 錯誤。

以下是各項 API 變更的詳細說明和程式碼範例。

### 1. 取樣參數已淘汰 (`temperature`、`top_p`、`top_k`)

`temperature`、`top_p` 和 `top_k` 已淘汰並遭到忽略。在日後的模型版本中，提供這些參數會傳回 HTTP 400 錯誤。**從所有要求中移除這些參數。**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

如要提升確定性，請為特定用途定義系統指令，並明確指定規則。

### 2. 預先填入模型回合驗證

如果 API 要求以非空白的模型角色回合結尾，系統會禁止這類要求，並傳回 **HTTP 400 錯誤**。

#### ⚠️ 避免

在舊版 `generateContent` 或原始 REST 酬載中，現在不允許以模型角色回合結尾：

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ 建議遷移

如果應用程式先前預先填寫模型回合，以抑制前言或強制使用 JSON 格式，請改用 `system_instruction` 或[結構化輸出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)。

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## 遷移檢查清單

### Gemini 3.6 Flash

1. 安裝技能：

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 套用技能：

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. 安裝技能：

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. 套用技能：

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### 遷移至 gemini-3.6-flash

- **更新模型 ID：**將目標模型字串變更為 `gemini-3.6-flash`。
- **移除已淘汰的取樣參數：**
  - 從生成設定中移除 `temperature`、`top_p` 和 `top_k`。
  - 將 `thinking_budget` 替換為設為 `"medium"` 或 `"high"` 的字串列舉 `thinking_level`。
  - 移除 `candidate_count` (Gemini 3.x 不支援)。
- **強制執行回合驗證規則：**
  - 移除預先填入的模型回合。
  - 確認最終使用者輪流輸入的內容包含非空白文字。
- **稽核函式呼叫：**
  - 確認所有 `FunctionResponse` 物件都包含 `call_id` 和 `name`。
  - 將多模態素材資源放在回應酬載中。
  - 使用 `\\n\\n` 格式設定內嵌指令。
  - 如果看到與前置工具文字相關的 `Malformed_Function_Call` 錯誤，請參閱「[前置工具文字規定解決方法](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=zh-tw#workarounds-for-pre-tool-text-requirements)」。
- **Gemini 3.x 基準需求：**如要瞭解 SDK 更新和想法簽章保留作業，請參閱 [Gemini 3.5 遷移檢查清單](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=zh-tw#migration)。

### 遷移至 gemini-3.5-flash-lite

- **更新模型 ID：**將目標模型字串變更為 `gemini-3.5-flash-lite`。
- **設定思考程度：**
  - 如要大量擷取、轉送或分類：請保留 `thinking_level` 的預設值 `"minimal"`，以達到最大處理量。
  - 如果是具有工具呼叫、執行程式碼或多步驟推論功能的自主子代理程式，請將 `thinking_level` 設為 `"medium"` 或 `"high"`，避免工具過早終止。
- **移除已淘汰的參數並驗證函式呼叫：**套用[與 3.6 Flash 相同的規則](#migrate-to-gemini-3-6-flash)。
- **Gemini 3.x 基準需求：**請參閱 [Gemini 3.5 遷移檢查清單](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=zh-tw#migration)。

## 後續步驟

- 在「模型總覽」中查看 API 規格。
- 請參閱[互動 API 指南](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw)，瞭解多代理自動化調度管理機制。
- 在 [Google AI Studio](https://aistudio.google.com/?hl=zh-tw) 中測試及調整提示。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-30 (世界標準時間)。"],[],[]]
