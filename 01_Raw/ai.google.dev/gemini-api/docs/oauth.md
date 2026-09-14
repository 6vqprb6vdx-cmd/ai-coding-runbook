---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=vi
fetched_at: 2026-09-14T05:47:17.953444+00:00
title: "X\u00e1c th\u1ef1c b\u1eb1ng t\u00ednh n\u0103ng b\u1eaft \u0111\u1ea7u nhanh OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Xác thực bằng tính năng bắt đầu nhanh OAuth

Cách dễ nhất để xác thực với Gemini API là định cấu hình khoá API, như mô tả trong [hướng dẫn bắt đầu sử dụng Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=vi). Nếu cần biện pháp kiểm soát quyền truy cập nghiêm ngặt hơn, bạn có thể sử dụng OAuth. Hướng dẫn này sẽ giúp bạn thiết lập quy trình xác thực bằng OAuth.

Hướng dẫn này sử dụng phương pháp xác thực đơn giản, phù hợp với môi trường kiểm thử. Đối với môi trường thực tế, hãy tìm hiểu về [xác thực và uỷ quyền](https://developers.google.com/workspace/guides/auth-overview?hl=vi) trước khi [chọn thông tin đăng nhập để truy cập](https://developers.google.com/workspace/guides/create-credentials?hl=vi#choose_the_access_credential_that_is_right_for_you) phù hợp với ứng dụng của bạn.

## Mục tiêu

- Thiết lập dự án trên đám mây cho OAuth
- Thiết lập application-default-credentials
- Quản lý thông tin đăng nhập trong chương trình của bạn thay vì dùng `gcloud auth`

## Điều kiện tiên quyết

Để chạy hướng dẫn bắt đầu nhanh này, bạn cần:

- [Một dự án trên Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=vi)
- [Một bản cài đặt cục bộ của gcloud CLI](https://cloud.google.com/sdk/docs/install?hl=vi)

## Thiết lập dự án trên đám mây

Để hoàn tất hướng dẫn bắt đầu nhanh này, trước tiên bạn cần thiết lập dự án trên đám mây.

### 1. Bật API

Trước khi sử dụng API của Google, bạn cần bật các API đó trong một dự án trên Google Cloud.

- Trong Cloud Console, hãy bật Google Generative Language API.

  [Bật API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=vi)

### 2. Định cấu hình màn hình xin phép bằng OAuth

Tiếp theo, hãy định cấu hình màn hình xin phép OAuth của dự án và thêm chính bạn làm người dùng kiểm thử. Nếu bạn đã hoàn tất bước này cho dự án trên đám mây, hãy chuyển sang phần tiếp theo.

1. Trong Cloud Console của Google, hãy chuyển đến **Trình đơn** > **Nền tảng xác thực của Google** > **Tổng quan**.

   [Truy cập vào nền tảng Google Auth](https://console.developers.google.com/auth/overview?hl=vi)
2. Hoàn tất biểu mẫu định cấu hình dự án và đặt loại người dùng thành **Bên ngoài** trong mục **Đối tượng**.
3. Hoàn tất phần còn lại của biểu mẫu, chấp nhận các điều khoản trong Chính sách về dữ liệu người dùng, rồi nhấp vào **Tạo**.
4. Hiện tại, bạn có thể bỏ qua bước thêm phạm vi và nhấp vào **Lưu và tiếp tục**. Trong tương lai, khi tạo một ứng dụng để sử dụng bên ngoài tổ chức Google Workspace, bạn phải thêm và xác minh các phạm vi uỷ quyền mà ứng dụng của bạn yêu cầu.
5. Thêm người dùng thử nghiệm:

   1. Chuyển đến [trang Đối tượng](https://console.developers.google.com/auth/audience?hl=vi) của nền tảng Google Auth.
   2. Trong phần **Người dùng kiểm thử**, hãy nhấp vào **Thêm người dùng**.
   3. Nhập địa chỉ email của bạn và mọi người dùng kiểm thử được uỷ quyền khác, sau đó nhấp vào **Lưu**.

### 3. Uỷ quyền thông tin đăng nhập cho một ứng dụng dành cho máy tính

Để xác thực với tư cách là người dùng cuối và truy cập vào dữ liệu người dùng trong ứng dụng của mình, bạn cần tạo một hoặc nhiều Mã ứng dụng khách OAuth 2.0. Mã ứng dụng khách được dùng để xác định một ứng dụng duy nhất cho các máy chủ OAuth của Google. Nếu ứng dụng của bạn chạy trên nhiều nền tảng, bạn phải tạo một mã ứng dụng khách riêng cho mỗi nền tảng.

1. Trong Cloud Console, hãy chuyển đến **Trình đơn** > **Nền tảng xác thực của Google** > **Ứng dụng**.

   [Chuyển đến phần Thông tin đăng nhập](https://console.developers.google.com/auth/clients?hl=vi)
2. Nhấp vào **Tạo ứng dụng**.
3. Nhấp vào **Loại ứng dụng** > **Ứng dụng dành cho máy tính**.
4. Trong trường **Name** (Tên), hãy nhập tên cho thông tin đăng nhập. Tên này chỉ xuất hiện trong Cloud Console.
5. Nhấp vào **Tạo**. Màn hình ứng dụng OAuth đã tạo sẽ xuất hiện, cho biết Mã ứng dụng và Khoá bí mật của ứng dụng mới.
6. Nhấp vào **OK**. Thông tin xác thực mới tạo sẽ xuất hiện trong phần **Mã ứng dụng khách OAuth 2.0**.
7. Nhấp vào nút tải xuống để lưu tệp JSON. Tệp này sẽ được lưu dưới dạng `client_secret_<identifier>.json`, sau đó đổi tên thành `client_secret.json` và di chuyển tệp đó vào thư mục làm việc của bạn.

## Thiết lập thông tin xác thực mặc định của ứng dụng

Để chuyển đổi tệp `client_secret.json` thành thông tin đăng nhập có thể sử dụng, hãy truyền vị trí của tệp này vào đối số `--client-id-file` của lệnh `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

Quy trình thiết lập dự án đơn giản trong hướng dẫn này sẽ kích hoạt hộp thoại **"Google chưa xác minh ứng dụng này"**. Đây là điều bình thường, hãy chọn **"tiếp tục"**.

Thao tác này sẽ đặt mã thông báo kết quả ở một vị trí đã biết để `gcloud` hoặc các thư viện ứng dụng có thể truy cập vào mã thông báo đó.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

Sau khi bạn đặt Thông tin xác thực mặc định của ứng dụng (ADC), các thư viện ứng dụng bằng hầu hết các ngôn ngữ sẽ cần rất ít hoặc không cần sự trợ giúp để tìm thấy thông tin xác thực đó.

### Curl

Cách nhanh nhất để kiểm tra xem phương thức này có hoạt động hay không là sử dụng phương thức này để truy cập vào REST API bằng curl:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

Trong Python, các thư viện ứng dụng sẽ tự động tìm thấy các tệp này:

```
pip install google-genai
```

Một tập lệnh tối thiểu để kiểm thử có thể là:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## Tự quản lý thông tin xác thực [Python]

Trong nhiều trường hợp, bạn sẽ không có lệnh `gcloud` để tạo mã truy cập từ Mã ứng dụng (`client_secret.json`). Google cung cấp các thư viện bằng nhiều ngôn ngữ để cho phép bạn quản lý quy trình đó trong ứng dụng của mình. Phần này minh hoạ quy trình bằng Python. Bạn có thể xem các ví dụ tương đương về loại quy trình này cho các ngôn ngữ khác trong [tài liệu về API Drive](https://developers.google.com/drive/api/quickstart/python?hl=vi)

### 1. Cài đặt các thư viện cần thiết

Cài đặt thư viện ứng dụng Google cho Python và thư viện ứng dụng Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. Viết trình quản lý thông tin xác thực

Để giảm thiểu số lần bạn phải nhấp qua các màn hình uỷ quyền, hãy tạo một tệp có tên là `load_creds.py` trong thư mục làm việc để lưu vào bộ nhớ đệm một tệp `token.json` mà tệp này có thể sử dụng lại sau này hoặc làm mới nếu hết hạn.

Bắt đầu bằng đoạn mã sau để chuyển đổi tệp `client_secret.json` thành một mã thông báo có thể dùng với `genai.configure`:

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

### 3. Viết chương trình

Bây giờ, hãy tạo `script.py` của bạn:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. Chạy chương trình

Trong thư mục làm việc, hãy chạy mẫu:

```
python script.py
```

Trong lần đầu tiên bạn chạy tập lệnh, tập lệnh sẽ mở một cửa sổ trình duyệt và nhắc bạn uỷ quyền truy cập.

1. Nếu chưa đăng nhập vào Tài khoản Google, bạn sẽ được nhắc đăng nhập. Nếu bạn đăng nhập vào nhiều tài khoản, **hãy nhớ chọn tài khoản mà bạn đã đặt làm "Tài khoản thử nghiệm" khi định cấu hình dự án.**
2. Thông tin uỷ quyền được lưu trữ trong hệ thống tệp, vì vậy, vào lần tiếp theo chạy mã mẫu, bạn sẽ không được nhắc về việc uỷ quyền.

Bạn đã thiết lập thành công quy trình xác thực.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-10 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-10 UTC."],[],[]]
