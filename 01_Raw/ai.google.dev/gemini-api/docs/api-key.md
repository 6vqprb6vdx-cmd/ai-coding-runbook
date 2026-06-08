---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=zh-TW
fetched_at: 2026-06-08T15:08:34.532697+00:00
title: "\u4f7f\u7528 Gemini API \u91d1\u9470 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Gemini API 金鑰

如要使用 Gemini API，請取得 API 金鑰。本頁面說明如何在 Google AI Studio 中建立及管理金鑰，以及如何設定環境，以便在程式碼中使用金鑰。

[建立或查看 Gemini API 金鑰](https://aistudio.google.com/app/apikey?hl=zh-tw)

## API 金鑰

您可以在 [Google AI Studio](https://aistudio.google.com/app/apikey?hl=zh-tw) 的「API Keys」(API 金鑰) 頁面中，建立及管理所有 Gemini API 金鑰。

取得 API 金鑰後，您可以透過下列方式連線至 Gemini API：

- [將 API 金鑰設為環境變數](#set-api-env-var)
- [明確提供 API 金鑰](#provide-api-key-explicitly)

進行初步測試時，您可以將 API 金鑰寫死在程式碼中，但這只是暫時做法，因為並不安全。如需以硬式編碼方式提供 API 金鑰的範例，請參閱「[明確提供 API 金鑰](#provide-api-key-explicitly)」一節。

## Google Cloud 專案

[Google Cloud 專案](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=zh-tw)是使用 Google Cloud 服務 (例如 Gemini API)、管理帳單，以及控管協作者和權限的基本要件。Google AI Studio 提供 Google Cloud 專案的輕量型介面。

如果您尚未建立任何專案，必須建立新專案，或是從 Google Cloud 匯入專案至 Google AI Studio。Google AI Studio 的「專案」頁面會顯示所有有權使用 Gemini API 的金鑰。如需操作說明，請參閱「[匯入專案](#import-projects)」一節。

### 預設專案

新使用者接受服務條款後，Google AI Studio 會建立預設的 Google Cloud 專案和 API 金鑰，方便使用。如要在 Google AI Studio 中重新命名這個專案，請前往「資訊主頁」的「專案」檢視畫面，按一下專案旁邊的 3 點設定按鈕，然後選擇「重新命名專案」。現有使用者或已擁有 Google Cloud 帳戶的使用者，不會建立預設專案。

## 匯入專案

每個 Gemini API 金鑰都與 Google Cloud 專案相關聯。根據預設，Google AI Studio 不會顯示所有 Cloud 專案。您必須在「匯入專案」對話方塊中搜尋名稱或專案 ID，匯入所需專案。如要查看您有權存取的完整專案清單，請前往 Cloud Console。

如果尚未匯入任何專案，請按照下列步驟匯入 Google Cloud 專案並建立金鑰：

1. 前往 [Google AI Studio](https://aistudio.google.com?hl=zh-tw)。
2. 開啟左側面板中的「資訊主頁」。
3. 選取「專案」。
4. 在「專案」頁面中，選取「匯入專案」按鈕。
5. 搜尋並選取要匯入的 Google Cloud 雲端專案，然後選取「匯入」按鈕。

匯入專案後，請前往「資訊主頁」選單的「API 金鑰」頁面，在剛匯入的專案中建立 API 金鑰。

## 限制

在 Google AI Studio 中管理 API 金鑰和 Google Cloud 專案時，有以下限制。

- 您一次最多可以從 Google AI Studio 的「專案」頁面建立 10 個專案。
- 您可以命名及重新命名專案和金鑰。
- 「API 金鑰」和「專案」頁面最多會顯示 100 個金鑰和 50 個專案。
- 系統只會顯示未設限的 API 金鑰，或是僅限於 Generative Language API 的金鑰。

如要取得專案的額外管理存取權，包括修改及限制 API 金鑰，請前往 [Google Cloud 控制台憑證頁面](https://console.cloud.google.com/apis/credentials?hl=zh-tw)。
在 Cloud 控制台中，您可以選取專案、按一下現有 API 金鑰，然後將其限制為 **Generative Language API**。

## 將 API 金鑰設為環境變數

如果您設定環境變數 `GEMINI_API_KEY` 或 `GOOGLE_API_KEY`，使用 [Gemini API 程式庫](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)時，用戶端會自動擷取 API 金鑰。建議只設定其中一個變數，但如果兩個都設定，系統會優先採用 `GOOGLE_API_KEY`。

如果您使用 REST API 或瀏覽器上的 JavaScript，則需要明確提供 API 金鑰。

以下說明如何在不同作業系統中，將 API 金鑰在本機設為環境變數 `GEMINI_API_KEY`。

### Linux/macOS - Bash

Bash 是常見的 Linux 和 macOS 終端機設定。執行下列指令，即可檢查是否有設定檔：

```
~/.bashrc
```

如果回應為「No such file or directory」，您需要建立這個檔案，並執行下列指令來開啟檔案，或使用 `zsh`：

```
touch ~/.bashrc
open ~/.bashrc
```

接著，您需要新增下列匯出指令，設定 API 金鑰：

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

儲存檔案後，請執行下列指令來套用變更：

```
source ~/.bashrc
```

### macOS - Zsh

Zsh 是常見的 Linux 和 macOS 終端機設定。執行下列指令，即可檢查是否有設定檔：

```
~/.zshrc
```

如果回應為「No such file or directory」，您需要建立這個檔案，並執行下列指令來開啟檔案，或使用 `bash`：

```
touch ~/.zshrc
open ~/.zshrc
```

接著，您需要新增下列匯出指令，設定 API 金鑰：

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

儲存檔案後，請執行下列指令來套用變更：

```
source ~/.zshrc
```

### Windows

1. 在搜尋列中搜尋「環境變數」。
2. 選擇修改「系統設定」。你可能需要確認是否要執行這項操作。
3. 在系統設定對話方塊中，按一下標示為「環境變數」的按鈕。
4. 在「使用者變數」 (適用於目前使用者) 或「系統變數」 (適用於使用該機器的所有使用者) 下方，按一下「新增...」
5. 將變數名稱指定為 `GEMINI_API_KEY`。將 Gemini API 金鑰指定為變數值。
6. 按一下「確定」套用變更。
7. 開啟新的終端機工作階段 (cmd 或 Powershell)，取得新變數。

## 明確提供 API 金鑰

在某些情況下，您可能需要明確提供 API 金鑰。例如：

- 您要進行簡單的 API 呼叫，並偏好對 API 金鑰進行硬式編碼。
- 您想要明確控制，不必依賴 Gemini API 程式庫自動探索環境變數
- 您使用的環境不支援環境變數 (例如網頁)，或是您正在發出 REST 呼叫。

以下是明確提供 API 金鑰的範例：

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.5-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## 妥善保管 API 金鑰

請妥善保管 Gemini API 金鑰，如同密碼一般。如果遭到入侵，他人就能使用專案配額、產生費用 (如果已啟用帳單)，以及存取私人資料 (例如檔案)。

### 重大安全性規則

- **確保金鑰機密性**：Gemini 的 API 金鑰可能會存取應用程式所依附的機密資料。

  - **切勿將 API 金鑰提交至原始碼控管系統。**請勿在 Git 等版本管控系統中登錄 API 金鑰。
  - **請勿在用戶端公開 API 金鑰。**請勿直接在正式版網頁或行動應用程式中使用 API 金鑰。用戶端程式碼中的金鑰 (包括我們的 JavaScript/TypeScript 程式庫和 REST 呼叫) 可以擷取。
- **限制存取權**：盡可能將 API 金鑰的使用限制在特定 IP 位址、HTTP 參照網址或 Android/iOS 應用程式。
- **限制使用**：只為每個金鑰啟用必要的 API。
- **定期稽核**：定期稽核 API 金鑰，並定期輪替。

### 最佳做法

- **使用 API 金鑰進行伺服器端呼叫**：使用 API 金鑰最安全的方式，是從伺服器端應用程式呼叫 Gemini API，這樣金鑰就能保密。
- **使用臨時權杖進行用戶端存取 (僅限 Live API)：**如要直接從用戶端存取 Live API，可以使用臨時權杖。這些版本安全性風險較低，適合用於正式環境。詳情請參閱「[臨時權杖](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=zh-tw)」指南。
- **考慮為金鑰新增限制：**您可以新增 [API 金鑰限制](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=zh-tw#add-api-restrictions)，藉此限制金鑰的權限。這麼做可將金鑰外洩時的潛在損害降到最低。

如需一般最佳做法，請參閱這篇[說明文章](https://support.google.com/googleapi/answer/6310037?hl=zh-tw)。

## 保護未設限的 API 金鑰

未設限的 API 金鑰容易遭到惡意人士和未授權使用者濫用。為提升安全性，自 2026 年 6 月 19 日起，Gemini API 將停止支援無限制流量金鑰。

**也就是說，如果您未採取行動，Gemini API 要求就會失敗。**

如要繼續使用 Gemini API，請前往 [AI Studio](https://aistudio.google.com/api-keys?hl=zh-tw) 新增限制，確保流量金鑰安全無虞。

在 [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=zh-tw) 中，系統會在 API 金鑰未設限時顯示通知橫幅。您可以查看哪些金鑰不受限制，以及過去 90 天的服務用量。

如為不受限制的按鍵，請選擇下列其中一項：

- 金鑰只能用於 Gemini API。
- 將金鑰用於非 Gemini API。

### 將金鑰限制在僅限 Gemini API

如要將金鑰限制為僅適用於 Gemini API，請在 [AI Studio](https://aistudio.google.com/api-keys?hl=zh-tw) 中按一下「Restrict to Gemini API」(僅限 Gemini API) 按鈕，確保金鑰安全無虞。

### 限制金鑰只能用於非 Gemini API

如要限制金鑰，避免用於非 Gemini API：

1. 前往 [Google Cloud 控制台憑證頁面](https://console.cloud.google.com/apis/credentials?hl=zh-tw)。
2. 確認已選取正確的專案。
3. 選取 API 金鑰。
4. 展開「API 限制」下拉式選單，然後對 API 金鑰套用服務限制。

如要修改現有或新加入限制的金鑰，請前往 [Google Cloud 控制台](https://console.cloud.google.com/apis/credentials?hl=zh-tw)。

## 已封鎖的鍵

2026 年 5 月 7 日起，Gemini API 將封鎖長期閒置的無限制 API 金鑰。這些使用者會在 [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=zh-tw) 看到金鑰的「已封鎖」標記，必須產生新金鑰或使用其他受限金鑰，才能繼續使用 Gemini API。

## 排解 API 金鑰建立問題

在 Google AI Studio 中，「建立 API 金鑰」按鈕可能無法使用，並顯示「您沒有權限在這個專案中建立金鑰」訊息。

如果專案中的權限不足，無法產生新金鑰，就會發生這種情況：

- **`resourcemanager.projects.get`**：允許 AI Studio 驗證專案是否存在。
- **`apikeys.keys.create`**：允許產生 API 金鑰。
- **`serviceusage.services.enable`**：必須啟用這項服務，才能確保專案已啟用 Gemini API。
- **`iam.serviceAccounts.create`**：現在每個新的 API 金鑰都必須連結[服務帳戶](https://docs.cloud.google.com/docs/authentication/api-keys?hl=zh-tw#api-keys-bound-sa)，且該帳戶是在建立 API 金鑰時產生。
- **`iam.serviceAccountApiKeyBindings.create`**：必須將新建立的服務帳戶繫結至 API 金鑰。

如要修正權限，請要求專案管理員 (如果專案隸屬於[機構](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=zh-tw)，請要求機構管理員) 授予您具備上述權限的角色 (例如專案編輯者或自訂角色)。

如果您沒有專案的管理員存取權，可以建立不與機構相關聯的新專案，藉此產生金鑰。

如要查看所有 Google AI Studio 功能 (例如查看用量、頻率限制或帳單) 必須具備的 IAM 權限完整清單，請參閱 [AI Studio 疑難排解指南](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=zh-tw#iam-permissions)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-29 (世界標準時間)。"],[],[]]
