---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=he
fetched_at: 2026-05-25T13:03:46.350363+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# שיטות קלט של קבצים

במדריך הזה מוסברות הדרכים השונות שבהן אפשר לכלול קובצי מדיה כמו תמונות, אודיו, וידאו ומסמכים כששולחים בקשות ל-Gemini API.
השיטות החדשות נתמכות בכל נקודות הקצה (endpoints) של Gemini API, כולל Batch, ‏ Interactions ו-Live API.
השיטה הנכונה תלויה בגודל הקובץ, במיקום שבו הנתונים מאוחסנים כרגע ובתדירות שבה אתם מתכננים להשתמש בקובץ.

הדרך הכי פשוטה לכלול קובץ כקלט היא לקרוא קובץ מקומי ולכלול אותו בהנחיה. בדוגמה הבאה אפשר לראות איך קוראים קובץ PDF מקומי. בשיטה הזו, גודל קובצי ה-PDF מוגבל ל-50MB. רשימה מלאה של סוגי קבצים ומגבלות מופיעה [בטבלת ההשוואה של שיטות הקלט](#method-comparison).

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const ai = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = path.join('content', 'my_local_file.pdf'); // Adjust path as needed

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: fs.readFileSync(filePath).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Summarize this document"}
        ]
      },
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "application/pdf",
              "data": "'"${B64_CONTENT}"'"
            }
          }
        ]
      }
    ]
  }'
```

## השוואה בין שיטות קלט

בטבלה הבאה מוצגת השוואה בין כל שיטות הקלט, עם מגבלות הקבצים והתרחישים המומלצים לשימוש. שימו לב שמגבלת גודל הקובץ עשויה להשתנות בהתאם לסוג הקובץ ולמודל או לטוקנייזר שמשמשים לעיבוד הקובץ.

| שיטה | הכי טוב עבור | גודל קובץ מקסימלי | התמדה |
| --- | --- | --- | --- |
| **נתונים מוטבעים** | בדיקה מהירה, קבצים קטנים, אפליקציות בזמן אמת. | ‫100MB לכל בקשה או מטען ייעודי (payload)   (**50MB לקובצי PDF**) | ללא (נשלח עם כל בקשה) |
| **העלאת קובץ דרך API** | קבצים גדולים, קבצים שנעשה בהם שימוש כמה פעמים. | ‫2GB לכל קובץ,   עד 20GB לכל פרויקט | 48 שעות |
| **רישום של URI של GCS ב-File API** | קבצים גדולים שכבר נמצאים ב-Google Cloud Storage, קבצים שנמצאים בשימוש כמה פעמים. | ‫2GB לכל קובץ, ללא מגבלות אחסון כוללות | ללא (מאוחזר לכל בקשה). רישום חד-פעמי יכול להעניק גישה למשך 30 יום לכל היותר. |
| **כתובות URL חיצוניות** | נתונים ציבוריים או נתונים בדליים בענן (AWS, ‏ Azure, ‏ GCS) בלי להעלות אותם מחדש. | ‫100MB לכל בקשה או מטען ייעודי (payload) | ללא (מאוחזר לפי בקשה) |

## נתונים מוטבעים

בקובצים קטנים יותר (עד 100MB, או עד 50MB בקובצי PDF), אפשר להעביר את הנתונים ישירות במטען הייעודי (payload) של הבקשה. זו השיטה הפשוטה ביותר לבדיקות מהירות או לאפליקציות שמטפלות בנתונים זמניים בזמן אמת. אפשר לספק נתונים כמחרוזות מקודדות ב-Base64 או על ידי קריאה ישירה של קבצים מקומיים.

דוגמה לקריאה מקובץ מקומי מופיעה בתחילת הדף הזה.

### אחזור מכתובת URL

אפשר גם לאחזר קובץ מכתובת URL, להמיר אותו לבייטים ולכלול אותו בקלט.

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=[
      types.Part.from_bytes(
        data=doc_data,
        mime_type='application/pdf',
      ),
      prompt
  ]
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl);
      .then((response) => response.arrayBuffer());

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Gemini File API

ממשק ה-API של הקבצים מיועד לקבצים גדולים יותר (עד 2GB) או לקבצים שרוצים להשתמש בהם בכמה בקשות.

### העלאה רגילה של קבצים

מעלים קובץ מקומי ל-Gemini API. קבצים שמועלים בדרך הזו מאוחסנים באופן זמני (למשך 48 שעות) ומעובדים כדי שהמודל יוכל לאחזר אותם ביעילות.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[prompt, audio_file]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const prompt = "Describe this audio clip";

async function main() {
  const filePath = "path/to/your/sample.mp3"; // Adjust path as needed

  const myfile = await ai.files.upload({
    file: filePath,
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(myfile.uri, myfile.mimeType),
    ]),
  });
  console.log(response.text);

}
await main();
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

### רישום קבצים ב-Google Cloud Storage

אם הנתונים שלכם כבר נמצאים ב-Google Cloud Storage, אתם לא צריכים להוריד אותם ולהעלות אותם מחדש. אפשר לרשום אותו ישירות באמצעות File API.

1. נותנים ל**סוכן השירות** גישה לכל קטגוריה

   1. מפעילים את Gemini API בפרויקט בענן ב-Google Cloud.
   2. יוצרים את סוכן השירות:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **נותנים לסוכן השירות של Gemini API הרשאות** לקריאה של קטגוריות האחסון.

      המשתמש צריך להקצות את `Storage Object Viewer`
      [תפקיד ה-IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=he#storage.objectViewer) לסוכן השירות הזה בקטגוריות האחסון הספציפיות שהוא מתכוון להשתמש בהן.

   הגישה הזו לא פגה כברירת מחדל, אבל אפשר לשנות את זה בכל שלב. אפשר גם להשתמש בפקודות של [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=he) כדי להעניק הרשאות.
2. אימות השירות

   **דרישות מוקדמות**

   - הפעלת ה-API
   - יוצרים חשבון שירות או סוכן עם ההרשאות המתאימות.

   קודם צריך לבצע אימות כשירות שיש לו הרשאות לצפייה באובייקט אחסון. אופן הפעולה תלוי בסביבה שבה יפעל קוד ניהול הקבצים.

   **מחוץ ל-Google Cloud**

   אם הקוד שלכם מורץ מחוץ ל-Google Cloud, למשל מהמחשב, אתם צריכים להוריד את פרטי הכניסה לחשבון מ-Google Cloud Console. כך עושים את זה:

   1. עוברים אל [מסוף חשבון השירות](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=he).
   2. בוחרים את חשבון השירות הרלוונטי.
   3. בוחרים בכרטיסייה **Keys** ואז באפשרות **Add key, Create new key**.
   4. בוחרים את סוג המפתח **JSON** ורושמים את המיקום במחשב שאליו הקובץ הורד.

   פרטים נוספים זמינים במאמרי העזרה הרשמיים של Google Cloud בנושא [ניהול מפתחות של חשבונות שירות](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=he).

   אחר כך משתמשים בפקודות הבאות כדי לבצע אימות. הפקודות האלה מניחות שקובץ חשבון השירות נמצא בספרייה הנוכחית ושמו `service-account.json`.

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **ב-Google Cloud**

   אם אתם מריצים את התהליך ישירות ב-Google Cloud, למשל באמצעות [פונקציות של Cloud Run](https://cloud.google.com/functions?hl=he) או [מכונה של Compute Engine](https://cloud.google.com/products/compute?hl=he), יהיו לכם פרטי כניסה מרומזים, אבל תצטרכו לבצע אימות מחדש כדי להעניק את ההיקפים המתאימים.

   ### Python

   הקוד הזה מניח שהשירות פועל בסביבה שבה אפשר לקבל אוטומטית [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=he), כמו Cloud Run או Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   הקוד הזה מניח שהשירות פועל בסביבה שבה אפשר לקבל אוטומטית [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=he), כמו Cloud Run או Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### CLI

   זוהי פקודה אינטראקטיבית. בשירותים כמו Compute Engine, אפשר לצרף היקפי הרשאות לשירות הפועל ברמת ההגדרה. דוגמה מופיעה ב[מסמכים בנושא שירותים בניהול המשתמשים](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=he#using).

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. רישום קבצים (Files API)

   משתמשים ב-Files API כדי לרשום קבצים וליצור נתיב Files API שאפשר להשתמש בו ישירות ב-Gemini API.

   ### Python

   ```
   from google import genai
   from google.genai.types import Part

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client()

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"],
       # Use the credentials obtained in the previous step.
       auth=credentials
   )
   prompt = "Summarize this file."

   # call generateContent for each file
   for f in registered_gcs_files.files:
     print(f.name)
     response = client.models.generate_content(
       model="gemini-3.5-flash",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
   ```

   ### CLI

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## כתובות URL חיצוניות מסוג HTTP / כתובות URL חתומות

אפשר להעביר כתובות URL מסוג HTTPS שנגישות לכולם או כתובות URL חתומות מראש (שמתאימות ל[כתובות URL חתומות מראש של S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) ול-Azure SAS) ישירות בבקשת היצירה. ‫Gemini API יאחזר את התוכן בצורה מאובטחת במהלך העיבוד. האפשרות הזו מתאימה לקבצים בגודל של עד 100MB שלא רוצים להעלות מחדש.

אתם יכולים להשתמש בכתובות URL ציבוריות או חתומות כקלט באמצעות כתובות ה-URL בשדה `file_uri`.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[
        Part.from_uri(
            file_uri=uri,
            mime_type="application/pdf",
        ),
        prompt
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: [
      // equivalent to Part.from_uri(file_uri=uri, mime_type="...")
      createPartFromUri(uri, "application/pdf"),
      "summarize this file",
    ],
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "contents":[
            {
              "parts":[
                {"text": "Summarize this pdf"},
                {
                  "file_data": {
                    "mime_type":"application/pdf",
                    "file_uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
                  }
                }
              ]
            }
          ]
        }'
```

### נגישות

מוודאים שכתובות ה-URL שציינתם לא מובילות לדפים שנדרשת בהם התחברות או לדפים שמוגנים על ידי חומת תשלום. במסדי נתונים פרטיים, חשוב לוודא שאתם יוצרים כתובת URL חתומה עם הרשאות הגישה ותאריך התפוגה הנכונים.

### בדיקות אבטחה

המערכת מבצעת בדיקה של ניהול התוכן בכתובת ה-URL כדי לוודא שהיא עומדת בתקני הבטיחות והמדיניות (למשל, תוכן שלא נחסם ושהגישה אליו היא בתשלום). אם כתובת ה-URL שסיפקתם לא תעבור את הבדיקה הזו, תקבלו הודעה `url_retrieval_status` על `URL_RETRIEVAL_STATUS_UNSAFE`.

### סוגי התוכן הנתמכים

הרשימה הזו של סוגי קבצים נתמכים ומגבלות נועדה לספק הנחיות ראשוניות, והיא לא מלאה. קבוצת הסוגים הנתמכים בפועל עשויה להשתנות, והיא תלויה במודל הספציפי ובגרסת הטוקנייזר שנמצאים בשימוש. סוגים שלא נתמכים יגרמו לשגיאה.
בנוסף, אחזור תוכן עבור סוגי הקבצים האלה תומך כרגע רק בכתובות URL שזמינות לכל.

#### סוגים של קובצי טקסט

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### סוגי קבצים של אפליקציות

- `application/json`
- `application/pdf`

#### סוגים של קובצי תמונות

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### סוגים של קובצי וידאו

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## שיטות מומלצות

- **בחירת השיטה הנכונה:** משתמשים בנתונים מוטבעים לקבצים קטנים וזמניים.
  כדאי להשתמש ב-File API לקבצים גדולים או לקבצים שמשתמשים בהם לעיתים קרובות. שימוש בכתובות URL חיצוניות
  לנתונים שכבר מתארחים אונליין.
- **מציינים סוגי MIME:** חשוב לספק תמיד את סוג ה-MIME הנכון לנתוני הקובץ כדי להבטיח עיבוד תקין.
- **טיפול בשגיאות:** כדאי להטמיע טיפול בשגיאות בקוד כדי לנהל בעיות פוטנציאליות כמו כשלים ברשת, בעיות בגישה לקבצים או שגיאות ב-API.
- **ניהול הרשאות GCS:** כשמשתמשים ברישום GCS, צריך להעניק לסוכן השירות של Gemini API רק את התפקיד `Storage Object Viewer` הנדרש בקטגוריות הספציפיות.
- **אבטחת כתובות URL חתומות:** מוודאים שלכתובות URL חתומות יש זמן תפוגה מתאים והרשאות מוגבלות.

## מגבלות

- מגבלות גודל הקובץ משתנות בהתאם לשיטה (ראו [טבלת השוואה](#method-comparison)) ולסוג הקובץ.
- נתונים מוטבעים מגדילים את גודל המטען הייעודי (payload) של הבקשה.
- העלאות באמצעות File API הן זמניות והתוקף שלהן פג אחרי 48 שעות.
- הגודל המקסימלי של מטען ייעודי (payload) שאפשר לאחזר מכתובת URL חיצונית הוא 100MB, ויש תמיכה בסוגי תוכן ספציפיים.
- כדי להירשם ל-Google Cloud Storage, צריך להגדיר את IAM בצורה נכונה ולנהל את אסימוני OAuth.

## המאמרים הבאים

- אתם יכולים לנסות לכתוב הנחיות מולטימודאליות משלכם באמצעות [Google AI Studio](http://aistudio.google.com/?hl=he).
- מידע על הכללת קבצים בהנחיות זמין במדריכים בנושא [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=he), [אודיו](https://ai.google.dev/gemini-api/docs/audio?hl=he) ו[עיבוד מסמכים](https://ai.google.dev/gemini-api/docs/document-processing?hl=he).
- הנחיות נוספות לעיצוב הנחיות, כמו כוונון פרמטרים של דגימה, זמינות במדריך [אסטרטגיות להנחיות](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-19 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-19 (שעון UTC)."],[],[]]
