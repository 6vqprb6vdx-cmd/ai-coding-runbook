---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=zh-CN
fetched_at: 2026-09-28T06:13:10.676575+00:00
title: "\u4f7f\u7528 OAuth \u8fdb\u884c\u8eab\u4efd\u9a8c\u8bc1\u7684\u5feb\u901f\u5165\u95e8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 使用 OAuth 进行身份验证的快速入门

对 Gemini API 进行身份验证的最简单方法是配置 API 密钥，如 [Gemini API 快速入门指南](https://ai.google.dev/gemini-api/docs/get-started?hl=zh-cn)中所述。如果您需要更严格的访问权限控制，可以改用 OAuth。本指南将帮助您设置 OAuth 身份验证。

本指南使用一种简化的身份验证方法，该方法适用于测试环境。对于生产环境，请先了解[身份验证和授权](https://developers.google.com/workspace/guides/auth-overview?hl=zh-cn)，然后再[选择适合您应用的访问凭据](https://developers.google.com/workspace/guides/create-credentials?hl=zh-cn#choose_the_access_credential_that_is_right_for_you)。

## 目标

- 为 OAuth 设置云项目
- 设置应用默认凭据
- 在您的计划中管理凭据，而不是使用 `gcloud auth`

## 前提条件

如需运行本快速入门，您需要满足以下条件：

- [Google Cloud 项目](https://developers.google.com/workspace/guides/create-project?hl=zh-cn)
- [本地安装的 gcloud CLI](https://cloud.google.com/sdk/docs/install?hl=zh-cn)

## 设置 Cloud 项目

如需完成本快速入门，您需要先设置云项目。

### 1. 启用 API

在使用 Google API 之前，您需要在 Google Cloud 项目中启用它们。

- 在 Google Cloud 控制台中，启用 Google Generative Language API。

  [启用 API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=zh-cn)

### 2. 配置 OAuth 权限请求页面

接下来，配置项目的 OAuth 权限请求页面，并将自己添加为测试用户。如果您已为 Cloud 项目完成此步骤，请跳至下一部分。

1. 在 Google Cloud 控制台中，依次前往**菜单** > **Google Auth 平台** > **概览**。

   [前往 Google Auth Platform](https://console.developers.google.com/auth/overview?hl=zh-cn)
2. 填写项目配置表单，并在**受众群体**部分将用户类型设置为**外部**。
3. 完成表单的其余部分，接受《用户数据政策》条款，然后点击**创建**。
4. 目前，您可以跳过添加范围的步骤，然后点击**保存并继续**。未来，当您创建供 Google Workspace 组织外部使用的应用时，必须添加并验证应用所需的授权范围。
5. 添加测试用户：

   1. 前往 Google Auth 平台的[受众群体页面](https://console.developers.google.com/auth/audience?hl=zh-cn)。
   2. 在**测试用户**下，点击**添加用户**。
   3. 输入您的电子邮件地址和任何其他已获授权的测试用户，然后点击**保存**。

### 3. 为桌面应用授权凭据

如需以最终用户身份进行身份验证并访问应用中的用户数据，您需要创建一个或多个 OAuth 2.0 客户端 ID。客户端 ID 用于向 Google 的 OAuth 服务器标识单个应用。如果您的应用在多个平台上运行，您必须为每个平台分别创建客户端 ID。

1. 在 Google Cloud 控制台中，依次前往**菜单** > **Google Auth Platform** > **客户端**。

   [进入“凭据”页面](https://console.developers.google.com/auth/clients?hl=zh-cn)
2. 点击**创建客户端**。
3. 依次点击**应用类型** > **桌面应用**。
4. 在**名称**字段中，输入凭据的名称。此名称仅在 Google Cloud 控制台中显示。
5. 点击**创建**。此时会显示“OAuth 客户端已创建”界面，其中显示您的新客户端 ID 和客户端密钥。
6. 点击**确定**。新创建的凭证会显示在 **OAuth 2.0 客户端 ID** 下。
7. 点击下载按钮以保存 JSON 文件。它将保存为 `client_secret_<identifier>.json`，然后将其重命名为 `client_secret.json` 并移至您的工作目录。

## 设置应用默认凭证

如需将 `client_secret.json` 文件转换为可用的凭据，请将该文件的位置传递给 `gcloud auth application-default login` 命令的 `--client-id-file` 实参。

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

本教程中简化的项目设置会触发**“Google 尚未验证此应用”**对话框。这是正常现象，请选择**“继续”**。

这会将生成的令牌放置在已知位置，以便 `gcloud` 或客户端库可以访问该令牌。

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

设置应用默认凭证 (ADC) 后，大多数语言的客户端库只需极少的帮助或无需任何帮助即可找到这些凭证。

### Curl

测试此功能是否正常运行的最快方法是使用它通过 curl 访问 REST API：

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

在 Python 中，客户端库应会自动找到这些凭据：

```
pip install google-genai
```

用于测试它的最简脚本可能如下所示：

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## 自行管理凭据 [Python]

在许多情况下，您无法使用 `gcloud` 命令从客户端 ID (`client_secret.json`) 创建访问令牌。Google 提供了多种语言的库，可让您在应用内管理该流程。本部分将以 Python 为例演示该流程。[Drive API 文档](https://developers.google.com/drive/api/quickstart/python?hl=zh-cn)中提供了其他语言的类似过程示例

### 1. 安装必要的库

安装 Python 版 Google 客户端库和 Gemini 客户端库。

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. 编写凭据管理器

为了尽量减少您必须点击授权屏幕的次数，请在工作目录中创建一个名为 `load_creds.py` 的文件，以缓存 `token.json` 文件，以便稍后重复使用，或者在过期时刷新。

首先使用以下代码将 `client_secret.json` 文件转换为可与 `genai.configure` 搭配使用的令牌：

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. 编写您的计划

现在创建 `script.py`：

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. 运行程序

在工作目录中，运行示例：

```
python script.py
```

首次运行脚本时，系统会打开一个浏览器窗口，并提示您授权访问。

1. 如果您尚未登录 Google 账号，系统会提示您登录。如果您登录了多个账号，**请务必选择在配置项目时设置为“测试账号”的账号。**
2. 授权信息存储在文件系统中，因此下次运行示例代码时，系统不会提示您进行授权。

您已成功设置身份验证。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-10。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-10。"],[],[]]
