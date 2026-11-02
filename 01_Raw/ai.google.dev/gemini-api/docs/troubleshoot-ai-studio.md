---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=zh-TW
fetched_at: 2026-11-02T07:04:34.326893+00:00
title: "\u6392\u89e3 Google AI Studio \u554f\u984c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 排解 Google AI Studio 問題

本頁提供 Google AI Studio 疑難排解建議，協助您解決問題。

## 瞭解 403 存取受限錯誤

如果看到 403 存取受限錯誤，代表您使用 Google AI Studio 的方式不符合《[服務條款](https://ai.google.dev/terms?hl=zh-tw)》。常見原因之一是您不在[支援的地區](https://ai.google.dev/available_regions?hl=zh-tw)。

## 驗證 Google 帳戶的年齡規定

必須年滿 18 歲才能使用 Google AI Studio。嘗試開啟 [Google AI Studio](https://aistudio.google.com/?hl=zh-tw) 時，系統可能會將您重新導向至這個部分。如果是，請確認您的 Google 帳戶符合年齡規定：

- **檢查生日：**確認[生日設定](https://myaccount.google.com/birthday?hl=zh-tw)中的出生日期顯示你已年滿 18 歲。
- **驗證年齡：**在 Google 帳戶完成[年齡驗證](https://myaccount.google.com/age-verification?hl=zh-tw)。如要瞭解驗證選項，請參閱「[驗證 Google 帳戶中的年齡](https://support.google.com/accounts/answer/10071085?hl=zh-tw)」。
- **與身分證件上的出生日期相符：**如果您使用身分證件驗證年齡，請檢查帳戶設定。確認[生日](https://myaccount.google.com/birthday?hl=zh-tw)與身分證件上的日期一致。
- **Google Workspace 帳戶：**如果是 Google Workspace for Education 帳戶，請與管理員聯絡。他們可以確認你的帳戶是否已指定為 18 歲以上。詳情請參閱「[使用 Workspace 帳戶存取 Google AI Studio](https://ai.google.dev/gemini-api/docs/workspace?hl=zh-tw)」。

## 解決 Google AI Studio 的「無內容」回應

如果內容因任何原因遭到封鎖，Google AI Studio 會顯示 warning **No Content** 訊息。如要查看更多詳細資料，請將指標懸停在「No Content」(無內容) 上，然後按一下 warning「Safety」(安全性)。

如果回覆因[安全設定](https://ai.google.dev/docs/safety_setting?hl=zh-tw)而遭到封鎖，且您已考量用途的[安全風險](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-tw)，可以修改[安全設定](https://ai.google.dev/docs/safety_setting?hl=zh-tw#safety_settings_in_makersuite)，影響傳回的回覆。

如果回覆遭到封鎖，但不是因為安全設定，則查詢或回覆可能違反《[服務條款](https://ai.google.dev/terms?hl=zh-tw)》，或是不支援。

## 查看權杖用量和限制

開啟提示時，畫面底部的「Text Preview」(文字預覽) 按鈕會顯示提示內容目前使用的權杖，以及所用模型的權杖數量上限。

## AI Studio 的 Google Cloud IAM 權限

Google Cloud 專案成員必須具備特定 Identity and Access Management (IAM) 權限，才能在 Google AI Studio 執行動作。如要進一步瞭解這些身分，請參閱「[IAM 主體總覽](https://docs.cloud.google.com/iam/docs/principals-overview?hl=zh-tw)」。

在相關聯 Google Cloud 雲端專案中，具備**編輯者**或**擁有者**角色的使用者，擁有查看資訊主頁和管理 Gemini API 金鑰的完整權限。具備「檢視者」角色的使用者可以查看資訊主頁和 API 金鑰，但無法建立、更新或刪除。

如要更精細地控管，請參閱下表，瞭解各項 AI Studio 功能所需的特定權限。如要瞭解如何授予這些權限，請參閱 Google Cloud 說明文件中的「[授予、變更及撤銷資源存取權](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=zh-tw)」。

| AI Studio 功能 | 必要 IAM 權限 | 額外規定 |
| --- | --- | --- |
| **搜尋專案** (匯入專案) | `resourcemanager.projects.get` |  |
| **重新命名專案** | `resourcemanager.projects.update` |  |
| **顯示配額級別** | 不適用 |  |
| **建立 API 金鑰** | 具備**搜尋專案**權限，且：  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **列出 API 金鑰** | 具備**搜尋專案**權限，且：  `apikeys.keys.list` `serviceusage.services.get` | Google Cloud 雲端專案必須啟用 [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=zh-tw)。 |
| **重新命名 API 金鑰** | `apikeys.keys.update` |  |
| **刪除 API 金鑰** | `apikeys.keys.delete` |  |
| **用量資訊主頁** | 具備**搜尋專案**權限，且：  `monitoring.timeSeries.list` |  |
| **頻率限制資訊主頁** | 具備**用量資訊主頁**權限，且：  `cloudquotas.quotas.get` |  |
| **支出 (帳單費用上限)** | `billing.resourceCosts.get` (查看支出) `billing.resourcebudgets.read` (查看上限) `billing.resourcebudgets.write` (設定上限) |  |
| **帳單資訊主頁** | `billing.accounts.get` |  |

### 其他存取權檢查

除了 Google Cloud IAM 權限外，AI Studio 也會執行安全性和法規遵循檢查。如果不符合下列要求，AI Studio 介面或 API 回應可能會顯示 `PERMISSION_DENIED` 或存取限制錯誤：

- **安全性檢查：**您的要求必須通過自動安全性檢查。
- **服務條款：**您必須接受《Google 服務條款》和《生成式 AI 附加服務條款》。
- **支援的地區：**必須位於[支援的地區](https://ai.google.dev/gemini-api/docs/available-regions?hl=zh-tw)。
- **年齡規定：**Google 帳戶必須符合[年齡規定](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=zh-tw#age-requirements) (年滿 18 歲)。
- **信任與安全：**Google Cloud 雲端專案不得標記為濫用。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-22 (世界標準時間)。"],[],[]]
