---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=th
fetched_at: 2026-11-02T07:28:07.954048+00:00
title: "\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e2a\u0e34\u0e17\u0e18\u0e34\u0e4c\u0e14\u0e49\u0e27\u0e22\u0e01\u0e32\u0e23\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 OAuth \u0e2d\u0e22\u0e48\u0e32\u0e07\u0e23\u0e27\u0e14\u0e40\u0e23\u0e47\u0e27 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การตรวจสอบสิทธิ์ด้วยการเริ่มต้นใช้งาน OAuth อย่างรวดเร็ว

วิธีที่ง่ายที่สุดในการตรวจสอบสิทธิ์ไปยัง Gemini API คือการกำหนดค่าคีย์ API
ตามที่อธิบายไว้ใน [คู่มือเริ่มต้นใช้งาน Gemini API](https://ai.google.dev/gemini-api/docs/get-started?hl=th) หากต้องการการควบคุมการเข้าถึงที่เข้มงวดมากขึ้น คุณสามารถใช้ OAuth แทนได้ คู่มือนี้จะช่วยคุณตั้งค่าการตรวจสอบสิทธิ์ด้วย OAuth

คู่มือนี้ใช้วิธีการตรวจสอบสิทธิ์แบบง่าย ซึ่งเหมาะกับสภาพแวดล้อมการทดสอบ สำหรับสภาพแวดล้อมฮาร์ดแวร์และซอฟต์แวร์ โปรดดูข้อมูล
เกี่ยวกับ
[การตรวจสอบสิทธิ์และการให้สิทธิ์](https://developers.google.com/workspace/guides/auth-overview?hl=th)
ก่อน
[เลือกข้อมูลเข้าสู่ระบบ](https://developers.google.com/workspace/guides/create-credentials?hl=th#choose_the_access_credential_that_is_right_for_you)
ที่เหมาะสมกับแอป

## วัตถุประสงค์

- ตั้งค่าโปรเจ็กต์ที่อยู่ในระบบคลาวด์สำหรับ OAuth
- ตั้งค่าข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน
- จัดการข้อมูลเข้าสู่ระบบในโปรแกรมแทนการใช้ `gcloud auth`

## ข้อกำหนดเบื้องต้น

คุณต้องมีสิ่งต่อไปนี้จึงจะเรียกใช้การเริ่มต้นใช้งานฉบับย่อนี้ได้

- [โปรเจ็กต์ Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=th)
- [gcloud CLI ที่ติดตั้งในเครื่อง](https://cloud.google.com/sdk/docs/install?hl=th)

## ตั้งค่าโปรเจ็กต์ที่อยู่ในระบบคลาวด์

คุณต้องตั้งค่าโปรเจ็กต์ที่อยู่ในระบบคลาวด์ก่อนจึงจะทำการเริ่มต้นใช้งานฉบับย่อนี้ให้เสร็จสมบูรณ์ได้

### 1. เปิดใช้ API

ก่อนใช้ Google API คุณต้องเปิด API เหล่านั้นในโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google

- ในคอนโซล Google Cloud ให้เปิดใช้ Google Generative Language API

  [เปิดใช้ API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=th)

### 2. กำหนดค่าหน้าจอขอความยินยอม OAuth

จากนั้นกำหนดค่าหน้าจอขอความยินยอม OAuth ของโปรเจ็กต์และเพิ่มตัวคุณเองเป็นผู้ใช้ทดสอบ หากดำเนินการขั้นตอนนี้สำหรับโปรเจ็กต์ที่อยู่ในระบบคลาวด์แล้ว ให้ข้ามไปยังส่วนถัดไป

1. ในคอนโซล Google Cloud ให้ไปที่**เมนู** > **แพลตฟอร์มการตรวจสอบสิทธิ์ของ Google** > **ภาพรวม**

   [ไปที่แพลตฟอร์มการตรวจสอบสิทธิ์ของ Google](https://console.developers.google.com/auth/overview?hl=th)
2. กรอกแบบฟอร์มการกำหนดค่าโปรเจ็กต์และตั้งค่าประเภทผู้ใช้เป็น**ภายนอก** ในส่วน**กลุ่มเป้าหมาย**
3. กรอกข้อมูลในแบบฟอร์มส่วนที่เหลือ ยอมรับข้อกำหนดของนโยบายข้อมูลผู้ใช้ แล้วคลิก**สร้าง**
4. ตอนนี้คุณสามารถข้ามการเพิ่มขอบเขตและคลิก**บันทึกและดำเนินการต่อ** ในอนาคต เมื่อสร้างแอปเพื่อใช้ภายนอกองค์กร Google Workspace คุณต้องเพิ่มและยืนยันขอบเขตการให้สิทธิ์ที่แอปต้องใช้
5. เพิ่มผู้ใช้ทดสอบโดยทำดังนี้

   1. ไปที่
      [หน้ากลุ่มเป้าหมาย](https://console.developers.google.com/auth/audience?hl=th)ของ
      แพลตฟอร์มการตรวจสอบสิทธิ์ของ Google
   2. ในส่วน**ผู้ใช้ทดสอบ** ให้คลิก**เพิ่มผู้ใช้**
   3. ป้อนอีเมลของคุณและอีเมลของผู้ใช้ทดสอบที่ได้รับอนุญาตรายอื่นๆ แล้วคลิก**บันทึก**

### 3. ให้สิทธิ์ข้อมูลเข้าสู่ระบบสำหรับแอปพลิเคชันบนเดสก์ท็อป

หากต้องการตรวจสอบสิทธิ์ในฐานะผู้ใช้ปลายทางและเข้าถึงข้อมูลผู้ใช้ในแอป คุณต้องสร้างรหัสไคลเอ็นต์ OAuth 2.0 อย่างน้อย 1 รายการ รหัสไคลเอ็นต์ใช้เพื่อระบุแอปเดี่ยวไปยังเซิร์ฟเวอร์ OAuth ของ Google หากแอปทำงานบนหลายแพลตฟอร์ม คุณต้องสร้างรหัสไคลเอ็นต์แยกต่างหากสำหรับแต่ละแพลตฟอร์ม

1. ในคอนโซล Google Cloud ให้ไปที่**เมนู** > **แพลตฟอร์มการตรวจสอบสิทธิ์ของ Google** > **ไคลเอ็นต์**

   [ไปที่ข้อมูลเข้าสู่ระบบ](https://console.developers.google.com/auth/clients?hl=th)
2. คลิก**สร้างไคลเอ็นต์**
3. คลิก**ประเภทแอปพลิเคชัน** > **แอปบนเดสก์ท็อป**
4. พิมพ์ชื่อของข้อมูลเข้าสู่ระบบในช่อง**ชื่อ** ชื่อนี้จะแสดงในคอนโซล Google Cloud เท่านั้น
5. คลิก**สร้าง** หน้าจอไคลเอ็นต์ OAuth ที่สร้างขึ้นจะปรากฏขึ้น โดยแสดงรหัสไคลเอ็นต์และรหัสลับไคลเอ็นต์ใหม่
6. คลิก**ตกลง** ข้อมูลเข้าสู่ระบบที่สร้างขึ้นใหม่จะปรากฏในส่วน**รหัสไคลเอ็นต์ OAuth 2.0**
7. คลิกปุ่มดาวน์โหลดเพื่อบันทึกไฟล์ JSON ระบบจะบันทึกไฟล์เป็น
   `client_secret_<identifier>.json` จากนั้นเปลี่ยนชื่อเป็น `client_secret.json`
   และย้ายไฟล์ไปยังไดเรกทอรีงาน

## ตั้งค่าข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน

หากต้องการแปลงไฟล์ `client_secret.json` เป็นข้อมูลเข้าสู่ระบบที่ใช้ได้ ให้ส่งตำแหน่งของไฟล์ไปยังอาร์กิวเมนต์ `--client-id-file` ของคำสั่ง `gcloud auth application-default login`

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

การตั้งค่าโปรเจ็กต์แบบง่ายในบทแนะนำนี้จะทริกเกอร์กล่องโต้ตอบ **"Google ยังไม่ได้
ยืนยันแอปนี้"** ซึ่งเป็นเรื่องปกติ ให้เลือก **"ดำเนินการต่อ"**

การดำเนินการนี้จะวางโทเค็นที่ได้ไว้ในตำแหน่งที่รู้จักกันดีเพื่อให้ `gcloud` หรือไลบรารีของไคลเอ็นต์เข้าถึงได้

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

เมื่อตั้งค่าข้อมูลรับรองเริ่มต้นของแอปพลิเคชัน (ADC) แล้ว ไลบรารีของไคลเอ็นต์ในภาษาต่างๆ ส่วนใหญ่จะค้นหาข้อมูลเข้าสู่ระบบเหล่านี้ได้โดยไม่ต้องอาศัยความช่วยเหลือหรืออาศัยความช่วยเหลือน้อยมาก

### Curl

วิธีที่รวดเร็วที่สุดในการทดสอบว่าการดำเนินการนี้ได้ผลคือการใช้เพื่อเข้าถึง REST API โดยใช้ curl ดังนี้

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

ใน Python ไลบรารีของไคลเอ็นต์ควรค้นหาข้อมูลเข้าสู่ระบบเหล่านี้ได้โดยอัตโนมัติ

```
pip install google-genai
```

สคริปต์อย่างง่ายสำหรับการทดสอบอาจมีลักษณะดังนี้

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## จัดการข้อมูลเข้าสู่ระบบด้วยตนเอง [Python]

ในหลายๆ กรณี คุณจะไม่มีคำสั่ง `gcloud` ให้ใช้เพื่อสร้างโทเค็นเพื่อการเข้าถึงจากรหัสไคลเอ็นต์ (`client_secret.json`) Google มีไลบรารีในหลายภาษาเพื่อให้คุณจัดการกระบวนการดังกล่าวภายในแอปได้ ส่วนนี้จะแสดงกระบวนการใน Python นอกจากนี้ยังมีตัวอย่างที่เทียบเท่าของขั้นตอนประเภทนี้
สำหรับภาษาอื่นๆ ใน
[เอกสารประกอบของ Drive API](https://developers.google.com/drive/api/quickstart/python?hl=th)

### 1. ติดตั้งไลบรารีที่จำเป็น

ติดตั้งไลบรารีของไคลเอ็นต์ Google สำหรับ Python และไลบรารีของไคลเอ็นต์ Gemini

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. เขียนตัวจัดการข้อมูลเข้าสู่ระบบ

หากต้องการลดจำนวนครั้งที่คุณต้องคลิกผ่านหน้าจอการให้สิทธิ์ ให้สร้างไฟล์ชื่อ `load_creds.py` ในไดเรกทอรีงานเพื่อแคชไฟล์ `token.json` ที่ไฟล์นี้จะนำกลับมาใช้ใหม่ได้ในภายหลัง หรือรีเฟรชหากไฟล์หมดอายุ

เริ่มต้นด้วยโค้ดต่อไปนี้เพื่อแปลงไฟล์ `client_secret.json` เป็นโทเค็นที่ใช้ได้กับ `genai.configure`

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

### 3. เขียนโปรแกรม

ตอนนี้ให้สร้าง `script.py` ดังนี้

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. เรียกใช้โปรแกรม

เรียกใช้ตัวอย่างในไดเรกทอรีงานโดยใช้คำสั่งต่อไปนี้

```
python script.py
```

เมื่อเรียกใช้สคริปต์เป็นครั้งแรก สคริปต์จะเปิดหน้าต่างเบราว์เซอร์และแจ้งให้คุณให้สิทธิ์เข้าถึง

1. หากยังไม่ได้ลงชื่อเข้าใช้บัญชี Google ระบบจะแจ้งให้คุณลงชื่อเข้าใช้ หากลงชื่อเข้าใช้ไว้หลายบัญชี **โปรดเลือกบัญชีที่คุณตั้งค่าเป็น "บัญชีทดสอบ" เมื่อกำหนดค่าโปรเจ็กต์**
2. ระบบจะจัดเก็บข้อมูลการให้สิทธิ์ไว้ในระบบไฟล์ ดังนั้นครั้งถัดไปที่คุณเรียกใช้โค้ดตัวอย่าง ระบบจะไม่แจ้งให้คุณให้สิทธิ์

คุณตั้งค่าการตรวจสอบสิทธิ์เรียบร้อยแล้ว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-10 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-10 UTC"],[],[]]
