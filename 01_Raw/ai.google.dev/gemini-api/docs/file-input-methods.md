---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de
fetched_at: 2026-08-03T04:30:05.133307+00:00
title: "Methoden zur Dateieingabe \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Methoden zur Dateieingabe

In diesem Leitfaden werden die verschiedenen Möglichkeiten erläutert, wie Sie Mediendateien wie Bilder, Audio, Video und Dokumente in Anfragen an die Gemini API einfügen können.
Die neuen Methoden werden in allen Gemini API-Endpunkten unterstützt, einschließlich Batch, Interactions und Live API.
Die Wahl der richtigen Methode hängt von der Größe der Datei, dem Speicherort der Daten und der Häufigkeit ab, mit der Sie die Datei verwenden möchten.

Die einfachste Möglichkeit, eine Datei als Eingabe zu verwenden, besteht darin, eine lokale Datei zu lesen und sie in einen Prompt einzufügen. Im folgenden Beispiel wird gezeigt, wie eine lokale PDF-Datei gelesen wird. Bei dieser Methode sind PDFs auf 50 MB begrenzt. Eine vollständige Liste der Dateieingabetypen und ‑beschränkungen finden Sie in der
[Vergleichstabelle für Eingabemethoden](#method-comparison).

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## Vergleich der Eingabemethoden

In der folgenden Tabelle werden die einzelnen Eingabemethoden mit Dateibeschränkungen und optimalen Anwendungsfällen verglichen. Die Dateigrößenbeschränkung kann je nach Dateityp und Modell oder Tokenizer variieren, der zum Verarbeiten der Datei verwendet wird.

| Methode | Optimal für | Maximale Dateigröße | Persistenz |
| --- | --- | --- | --- |
| **Inlinedaten** | Schnelle Tests, kleine Dateien, Echtzeitanwendungen. | 100 MB pro Anfrage oder Nutzlast   (**50 MB für PDFs**) | Keine (wird mit jeder Anfrage gesendet) |
| **Dateiupload über die File API** | Große Dateien, Dateien, die mehrmals verwendet werden. | 2 GB pro Datei,   bis zu 20 GB pro Projekt | 48 Stunden |
| **Registrierung der GCS-URI über die File API** | Große Dateien, die sich bereits in Google Cloud Storage befinden, Dateien, die mehrmals verwendet werden. | 2 GB pro Datei, keine Beschränkungen für den Gesamtspeicher | Keine (wird pro Anfrage abgerufen). Durch eine einmalige Registrierung kann der Zugriff für bis zu 30 Tage gewährt werden. |
| **Externe URLs** | Öffentliche Daten oder Daten in Cloud-Buckets (AWS, Azure, GCS) ohne erneuten Upload. | 100 MB pro Anfrage/Nutzlast | Keine (wird pro Anfrage abgerufen) |

## Inlinedaten

Bei kleineren Dateien (unter 100 MB oder 50 MB für PDFs) können Sie die Daten direkt in der Anfrage-Nutzlast übergeben. Dies ist die einfachste Methode für schnelle Tests oder Anwendungen, die Echtzeitdaten verarbeiten. Sie können Daten als Base64-codierte Strings bereitstellen oder lokale Dateien direkt lesen.

Ein Beispiel für das Lesen aus einer lokalen Datei finden Sie am Anfang dieser Seite.

### Von einer URL abrufen

Sie können eine Datei auch von einer URL abrufen, sie in Byte umwandeln und in die Eingabe einfügen.

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
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

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.6-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Gemini File API

Die File API ist für größere Dateien (bis zu 2 GB) oder Dateien konzipiert, die Sie in mehreren Anfragen verwenden möchten.

### Standardmäßiger Dateiupload

Laden Sie eine lokale Datei in die Gemini API hoch. Auf diese Weise hochgeladene Dateien werden vorübergehend (48 Stunden) gespeichert und für den effizienten Abruf durch das Modell verarbeitet.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Google Cloud Storage-Dateien registrieren

Wenn sich Ihre Daten bereits in Google Cloud Storage befinden, müssen Sie sie nicht herunterladen und noch einmal hochladen. Sie können sie direkt bei der File API registrieren.

1. Gewähren Sie dem **Dienst-Agent** Zugriff auf jeden Bucket.

   1. Aktivieren Sie die Gemini API in Ihrem Google Cloud-Projekt.
   2. Erstellen Sie den Dienst-Agent:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Gewähren Sie dem Gemini API-Dienst-Agent Berechtigungen** zum Lesen Ihrer Speicher-Buckets.

      Der Nutzer muss diesem Dienst-Agent die `Storage Object Viewer`
      [IAM-Rolle](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=de#storage.objectViewer)
      für die jeweiligen Speicher-Buckets zuweisen, die er verwenden möchte.

   Dieser Zugriff läuft standardmäßig nicht ab, kann aber jederzeit geändert werden. Sie können
   auch die
   [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=de)
   -Befehle verwenden, um Berechtigungen zu gewähren.
2. Authentifizieren Sie Ihren Dienst.

   **Voraussetzungen**

   - API aktivieren
   - Erstellen Sie ein Dienstkonto oder einen Dienst-Agent mit den entsprechenden Berechtigungen.

   Sie müssen sich zuerst als der Dienst authentifizieren, der Berechtigungen für den Storage-Objekt-Betrachter hat. Wie das geschieht, hängt von der Umgebung ab, in der Ihr Dateiverwaltungscode ausgeführt wird.

   **Außerhalb von Google Cloud**

   Wenn Ihr Code außerhalb von Google Cloud ausgeführt wird, z. B. auf Ihrem Computer, laden Sie die Kontoberechtigungen mit den folgenden Schritten aus der Google Cloud Console herunter:

   1. Rufen Sie die [Dienstkonto-Konsole](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=de) auf.
   2. Wählen Sie das entsprechende Dienstkonto aus.
   3. Wählen Sie den Tab **Schlüssel** aus und klicken Sie auf **Schlüssel hinzufügen, Neuen Schlüssel erstellen**.
   4. Wählen Sie den Schlüsseltyp **JSON** aus und notieren Sie sich, wohin die Datei auf Ihrem Computer heruntergeladen wurde.

   Weitere Informationen finden Sie in der offiziellen Google Cloud-Dokumentation zur
   [Verwaltung von Dienstkontoschlüsseln](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=de).

   Verwenden Sie dann die folgenden Befehle, um sich zu authentifizieren. Bei diesen Befehlen wird davon ausgegangen, dass sich die Dienstkontodatei im aktuellen Verzeichnis befindet und den Namen `service-account.json` hat.

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

   **Mit Google Cloud**

   Wenn Sie direkt in Google Cloud ausgeführt werden, z. B. mit [Cloud
   Run-Funktionen](https://cloud.google.com/functions?hl=de) oder einer
   [Compute Engine-Instanz](https://cloud.google.com/products/compute?hl=de), haben Sie
   implizite Anmeldedaten, müssen sich aber noch einmal authentifizieren, um die
   entsprechenden Bereiche zu gewähren.

   ### Python

   Dieser Code geht davon aus, dass der Dienst in einer Umgebung ausgeführt wird, in der
   [Standardanmeldedaten für Anwendungen](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=de)
   automatisch abgerufen werden können, z. B. Cloud Run oder Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Dieser Code geht davon aus, dass der Dienst in einer Umgebung ausgeführt wird, in der
   [Standardanmeldedaten für Anwendungen](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=de)
   automatisch abgerufen werden können, z. B. Cloud Run oder Compute Engine.

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

   Dies ist ein interaktiver Befehl. Bei Diensten wie Compute Engine können Sie Bereiche auf Konfigurationsebene an den ausgeführten Dienst anhängen. Ein Beispiel finden Sie in der Dokumentation zu [nutzerverwalteten Diensten
   docs](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=de#using).

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Dateiregistrierung (Files API)

   Verwenden Sie die Files API, um Dateien zu registrieren und einen Files API-Pfad zu erstellen, der direkt in der Gemini API verwendet werden kann.

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.6-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.6-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
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

## Externe HTTP- / signierte URLs

Sie können öffentlich zugängliche HTTPS-URLs oder vorab signierte URLs direkt in Ihrer Anfrage übergeben. Die Gemini API ruft die Inhalte während der Verarbeitung sicher ab.
Dies ist ideal für Dateien mit bis zu 100 MB, die Sie nicht noch einmal hochladen möchten.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.6-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### Bedienungshilfen

Prüfen Sie, ob die von Ihnen angegebenen URLs nicht zu Seiten führen, für die eine Anmeldung erforderlich ist oder die sich hinter einer Paywall befinden. Erstellen Sie für private Datenbanken eine signierte URL mit den richtigen Zugriffsberechtigungen und dem richtigen Ablaufdatum.

### Sicherheitsprüfungen

Das System führt eine Inhaltsmoderationsprüfung für die URL durch, um zu bestätigen, dass sie den Sicherheits- und Richtlinienstandards entspricht. Wenn die URL diese Prüfung nicht besteht, erhalten Sie für `url_retrieval_status` den Wert `URL_RETRIEVAL_STATUS_UNSAFE`.

### Unterstützte Inhaltstypen

Diese Liste der unterstützten Dateitypen und ‑beschränkungen dient als erste Orientierung und ist nicht vollständig. Die tatsächliche Menge der unterstützten Typen kann sich ändern und je nach verwendetem Modell und Tokenizer variieren. Nicht unterstützte Typen führen zu einem Fehler.
Außerdem wird der Abruf von Inhalten für diese Dateitypen nur für öffentlich zugängliche URLs unterstützt.

#### Textdateitypen

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Anwendungsdateitypen

- `application/json`
- `application/pdf`

#### Bilddateitypen

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Videodateitypen

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Best Practices

- **Die richtige Methode auswählen**:Verwenden Sie Inlinedaten für kleine, temporäre Dateien.
  Verwenden Sie die File API für größere oder häufig verwendete Dateien. Verwenden Sie externe URLs für Daten, die bereits online gehostet werden.
- **MIME-Typen angeben**:Geben Sie immer den richtigen MIME-Typ für die Dateidaten an, um eine ordnungsgemäße Verarbeitung zu gewährleisten.
- **Fehlerbehandlung**:Implementieren Sie eine Fehlerbehandlung in Ihrem Code, um potenzielle Probleme wie Netzwerkausfälle, Probleme beim Dateizugriff oder API-Fehler zu beheben.

## Beschränkungen

- Die Dateigrößenbeschränkungen variieren je nach Methode (siehe [Vergleichstabelle](#method-comparison))
  und Dateityp.
- Inlinedaten erhöhen die Größe der Anfrage-Nutzlast.
- Dateiuploads über die File API sind temporär und laufen nach 48 Stunden ab.
- Der Abruf externer URLs ist auf 100 MB pro Nutzlast begrenzt und unterstützt bestimmte Inhaltstypen.

## Nächste Schritte

- Versuchen Sie, eigene multimodale Prompts mit
  [Google AI Studio](http://aistudio.google.com/?hl=de) zu erstellen.
- Informationen zum Einfügen von Dateien in Ihre Prompts finden Sie in den
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=de),
  [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=de)- und
  [Dokumentverarbeitung](https://ai.google.dev/gemini-api/docs/document-processing?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
