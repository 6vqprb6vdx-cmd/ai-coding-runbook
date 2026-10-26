---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-input-methods?hl=pt-BR
fetched_at: 2026-10-26T05:56:12.258047+00:00
title: "M\u00e9todos de entrada de arquivo \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

Envie comentários

# Métodos de entrada de arquivo

Este guia explica as diferentes maneiras de incluir arquivos de mídia, como imagens, áudio, vídeo e documentos, ao fazer solicitações para a API Gemini.
Os novos métodos são compatíveis com todos os endpoints da API Gemini, incluindo as APIs Batch, Interactions e Live.
A escolha do método certo depende do tamanho do arquivo, de onde os dados estão armazenados e da frequência com que você planeja usar o arquivo.

A maneira mais simples de incluir um arquivo como entrada é ler um arquivo local e
incluí-lo em um comando. O exemplo a seguir mostra como ler um arquivo PDF local. Os PDFs estão limitados a 50 MB para esse método. Consulte a
[tabela de comparação de métodos de entrada](#method-comparison) para ver uma lista completa de tipos e limites de entrada de arquivos.

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.8-flash",
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
        model: "gemini-3.8-flash",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## Comparação de métodos de entrada

A tabela a seguir compara cada método de entrada com limites de arquivos e casos de uso ideais. O limite de tamanho do arquivo pode variar dependendo do tipo de arquivo e do modelo/tokenizer usado para processá-lo.

| Método | Ideal para | Tamanho máximo do arquivo | Persistência |
| --- | --- | --- | --- |
| **Dados inline** | Testes rápidos, arquivos pequenos, aplicativos em tempo real. | 100 MB por solicitação/payload   (**50 MB para PDFs**) | Nenhum (enviado com todas as solicitações) |
| **Upload da API File** | Arquivos grandes, arquivos usados várias vezes. | 2 GB por arquivo,   até 20 GB por projeto | 48 horas |
| **Registro de URI do GCS da API File** | Arquivos grandes já no Google Cloud Storage, arquivos usados várias vezes. | 2 GB por arquivo, sem limites gerais de armazenamento | Nenhum (buscado por solicitação). O registro único pode dar acesso por até 30 dias. |
| **URLs externos** | Dados públicos ou em buckets da nuvem (AWS, Azure, GCS) sem fazer upload novamente. | 15 MB por arquivo | Nenhum (buscado por solicitação) |

## Dados inline

Para arquivos menores (menos de 100 MB ou 50 MB para PDFs), você pode transmitir os dados diretamente no payload da solicitação. Esse é o método mais simples para testes rápidos ou
aplicativos que processam dados transitórios em tempo real. É possível fornecer dados como strings codificadas em base64 ou lendo arquivos locais diretamente.

Para ver um exemplo de leitura de um arquivo local, consulte o exemplo no início
desta página.

### Buscar de um URL

Também é possível buscar um arquivo de um URL, convertê-lo em bytes e incluí-lo na entrada.

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
  model="gemini-3.8-flash",
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
    const pdfResp = await fetch(docUrl)
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
        model: "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## API Gemini File

A API File foi projetada para arquivos maiores (até 2 GB) ou arquivos que você pretende usar em várias solicitações.

### Upload de arquivo padrão

Faça upload de um arquivo local para a API Gemini. Os arquivos enviados dessa forma são armazenados temporariamente (48 horas) e processados para recuperação eficiente pelo modelo.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

### Registrar arquivos do Google Cloud Storage

Se os dados já estiverem no Google Cloud Storage, não será necessário fazer o download e o upload novamente. É possível registrar diretamente com a API File.

1. Conceda acesso do **agente de serviço** a cada bucket

   1. Ative a API Gemini no seu projeto do Google Cloud.
   2. Crie o agente de serviço:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Conceda ao agente de serviço da API Gemini permissões** para ler seus buckets de armazenamento.

      O usuário precisa atribuir o [papel do IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=pt-br#storage.objectViewer) `Storage Object Viewer` a esse agente de serviço nos buckets de armazenamento específicos que pretende usar.

   Esse acesso não expira por padrão, mas pode ser alterado a qualquer momento. Também é possível usar os comandos do [SDK do IAM do Google Cloud Storage](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=pt-br) para conceder permissões.
2. Autenticar seu serviço

   **Pré-requisitos**

   - Ativar API
   - Crie uma conta de serviço/agente com as permissões adequadas.

   Primeiro, você precisa se autenticar como o serviço que tem permissões de leitor de objetos do Storage. Isso depende do ambiente em que o código de gerenciamento de arquivos será executado.

   **Fora do Google Cloud**

   Se o código estiver sendo executado fora do Google Cloud, como no seu computador,
   faça o download das credenciais da conta no console do Google Cloud seguindo estas etapas:

   1. Acesse o [console de contas de serviço](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=pt-br).
   2. Selecione a conta de serviço relevante
   3. Selecione a guia **Chaves** e escolha **Adicionar chave, Criar nova chave**.
   4. Escolha o tipo de chave **JSON** e observe onde o arquivo foi baixado na sua máquina.

   Para mais detalhes, consulte a documentação oficial do Google Cloud sobre [gerenciamento de chaves de conta de serviço](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=pt-br).

   Em seguida, use os comandos abaixo para fazer a autenticação. Esses comandos pressupõem que o arquivo da conta de serviço esteja no diretório atual, chamado `service-account.json`.

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

   **No Google Cloud**

   Se você estiver executando diretamente no Google Cloud, por exemplo, usando [funções do Cloud Run](https://cloud.google.com/functions?hl=pt-br) ou uma [instância do Compute Engine](https://cloud.google.com/products/compute?hl=pt-br), terá credenciais implícitas, mas precisará se autenticar novamente para conceder os escopos apropriados.

   ### Python

   Esse código espera que o serviço esteja sendo executado em um ambiente em que as [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=pt-br) podem ser obtidas automaticamente, como o Cloud Run ou o Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Esse código espera que o serviço esteja sendo executado em um ambiente em que as [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=pt-br) podem ser obtidas automaticamente, como o Cloud Run ou o Compute Engine.

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

   Este é um comando interativo. Para serviços como o Compute Engine, é possível anexar escopos ao
   serviço em execução no nível da configuração. Consulte a [documentação do serviço gerenciado pelo usuário](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=pt-br#using) para conferir um exemplo.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Registro de arquivos (API Files)

   Use a API Files para registrar arquivos e produzir um caminho da API Files que pode
   ser usado diretamente na API Gemini.

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
       model="gemini-3.8-flash",
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

## HTTP externo / URLs assinados

É possível transmitir URLs HTTPS acessíveis publicamente ou pré-assinados (compatíveis com [URLs pré-assinados do S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) e SAS do Azure) diretamente na solicitação de geração. A API Gemini vai buscar
o conteúdo com segurança durante o processamento. Isso é ideal para arquivos que você não quer enviar novamente. Cada arquivo pode ter até 15 MB. Para arquivos maiores, use a
[API File](#file-api).

É possível usar URLs públicos ou assinados como entrada usando os URLs no campo `file_uri`.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
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
    model: 'gemini-3.8-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent \
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

### Acessibilidade

Verifique se os URLs fornecidos não levam a páginas que exigem login ou estão atrás de um paywall. Para bancos de dados particulares, crie um URL assinado
com as permissões de acesso e o vencimento corretos.

### Confirmações de segurança

O sistema realiza uma verificação de moderação de conteúdo no URL para confirmar se ele atende aos padrões de segurança e política (por exemplo, conteúdo não desativado e pago). Se o URL fornecido não passar nessa verificação, você vai receber um
`url_retrieval_status` de `URL_RETRIEVAL_STATUS_UNSAFE`.

### Tipos de conteúdo compatíveis

Esta lista de tipos de arquivo aceitos e limitações é apenas uma orientação inicial e não é abrangente. O conjunto efetivo de tipos compatíveis está sujeito a mudanças e pode variar de acordo com o modelo específico e a versão do tokenizador em uso. Tipos sem suporte vão resultar em um erro.
Além disso, a recuperação de conteúdo para esses tipos de arquivo
atualmente só é compatível com URLs de acesso público.

#### Tipos de arquivo de texto

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Tipos de arquivo de aplicativo

- `application/json`
- `application/pdf`

#### Tipos de arquivo de imagem

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Tipos de arquivo de vídeo

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Práticas recomendadas

- **Escolha o método certo**:use dados inline para arquivos pequenos e temporários.
  Use a API File para arquivos maiores ou usados com frequência. Use URLs externos
  para dados já hospedados on-line.
- **Especifique tipos MIME**:sempre forneça o tipo MIME correto para os dados do arquivo para garantir o processamento adequado.
- **Tratar erros**:implemente o tratamento de erros no seu código para gerenciar
  possíveis problemas, como falhas de rede, problemas de acesso a arquivos ou erros
  de API.
- **Gerenciar permissões do GCS**:ao usar o registro do GCS, conceda ao agente de serviço da API Gemini apenas a função `Storage Object Viewer` necessária nos buckets específicos.
- **Segurança de URL assinado**:verifique se os URLs assinados têm um tempo de expiração adequado e permissões limitadas.

## Limitações

- Os limites de tamanho de arquivo variam de acordo com o método (consulte a [tabela de comparação](#method-comparison)) e o tipo de arquivo.
- Os dados inline aumentam o tamanho do payload da solicitação.
- Os uploads da API File são temporários e expiram após 48 horas.
- A busca de URLs externos é limitada a 15 MB por arquivo e oferece suporte a tipos de conteúdo específicos.
- O registro do Google Cloud Storage exige a configuração adequada do IAM e o gerenciamento de tokens
  do OAuth.

## A seguir

- Escreva seus próprios comandos multimodais usando o [Google AI Studio](http://aistudio.google.com/?hl=pt-br).
- Para saber como incluir arquivos nos comandos, consulte os guias de
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=pt-br),
  [Áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br) e
  [Processamento de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br).
- Para mais orientações sobre design de comandos, como ajuste de parâmetros de amostragem, consulte o
  guia [Estratégias de comandos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-07 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-07 UTC."],[],[]]
