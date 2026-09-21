---
source_url: https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-BR
fetched_at: 2026-09-21T05:47:16.183683+00:00
title: "API Batch \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# API Batch

A API Gemini Batch foi projetada para processar grandes volumes de solicitações
de forma assíncrona com [50% do custo padrão](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).
O tempo de resposta esperado é de 24 horas, mas, na maioria dos casos, é muito mais rápido.

Use a API Batch para tarefas não urgentes em grande escala, como pré-processamento de dados ou execução de avaliações em que uma resposta imediata não é necessária.

## Como criar um job em lote

Há duas maneiras de enviar solicitações na API Batch:

- **[Solicitações inline](#inline-requests):** uma lista de objetos
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=pt-br#GenerateContentRequest) incluídos diretamente na solicitação de criação em lote. Isso é adequado para lotes menores que mantêm o tamanho total da solicitação abaixo de 20 MB. A **saída** retornada do modelo é uma lista de objetos `inlineResponse`.
- **[Arquivo de entrada](#input-file):** um arquivo [JSON Lines (JSONL)](https://jsonlines.org/)
  em que cada linha contém um objeto
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=pt-br#GenerateContentRequest) completo.
  Esse método é recomendado para solicitações maiores. A **saída** retornada do modelo é um arquivo JSONL em que cada linha é um objeto `GenerateContentResponse` ou de status.

### Solicitações inline

Para um pequeno número de solicitações, é possível incorporar diretamente os
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=pt-br#GenerateContentRequest) objetos
no [`BatchGenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=pt-br#request-body). O
exemplo a seguir chama o
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=pt-br#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
método com solicitações inline:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'Tell me a one-sentence joke.'}],
            'role': 'user'
        }]
    },
    {
        'contents': [{
            'parts': [{'text': 'Why is the sky blue?'}],
            'role': 'user'
        }]
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=inline_requests,
    config={
        'display_name': "inlined-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'Tell me a one-sentence joke.'}],
            role: 'user'
        }]
    },
    {
        contents: [{
            parts: [{'text': 'Why is the sky blue?'}],
            role: 'user'
        }]
    }
]

const response = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});

console.log(response);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import java.util.List;

Client client = new Client();

// A list of InlinedRequest objects
List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(Arrays.asList(Part.fromText("Tell me a one-sentence joke.")))
                        .build()))
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(Arrays.asList(Part.fromText("Why is the sky blue?")))
                        .build()))
            .build());

BatchJobSource src = BatchJobSource.builder().inlinedRequests(inlineRequests).build();
CreateBatchJobConfig config =
    CreateBatchJobConfig.builder().displayName("inlined-requests-job-1").build();

BatchJob inlineBatchJob = client.batches.create("gemini-3.8-flash", src, config);

System.out.println("Created batch job: " + inlineBatchJob.name().orElse(""));
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:batchGenerateContent \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-X POST \
-H "Content-Type:application/json" \
-d '{
    "batch": {
        "display_name": "my-batch-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-1"
                        }
                    },
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-2"
                        }
                    }
                ]
            }
        }
    }
}'
```

### Arquivo de entrada

Para conjuntos maiores de solicitações, prepare um arquivo JSON Lines (JSONL). Cada linha desse arquivo precisa ser um objeto JSON que contenha uma chave definida pelo usuário e um objeto de solicitação, em que a solicitação seja um objeto válido
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=pt-br#GenerateContentRequest). A chave definida pelo usuário é usada na resposta para indicar qual saída é o resultado de qual solicitação. Por exemplo, a solicitação com a chave definida como `request-1` terá a resposta anotada com o mesmo nome de chave.

Esse arquivo é enviado usando a [API File](https://ai.google.dev/gemini-api/docs/files?hl=pt-br). O tamanho máximo permitido para um arquivo de entrada é de 2 GB.

Confira abaixo um exemplo de arquivo JSONL. É possível salvá-lo em um arquivo chamado `my-batch-requests.json`:

```
{"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generation_config": {"temperature": 0.7}}}
{"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
```

Assim como nas solicitações inline, é possível especificar outros parâmetros, como instruções do sistema, ferramentas ou outras configurações em cada JSON de solicitação.

É possível fazer upload desse arquivo usando a [API File](https://ai.google.dev/gemini-api/docs/files?hl=pt-br), conforme
mostrado no exemplo a seguir. Se você estiver trabalhando com entrada multimodal, poderá referenciar outros arquivos enviados no arquivo JSONL.

### Python

```
import json
from google import genai
from google.genai import types

client = genai.Client()

# Create a sample JSONL file
with open("my-batch-requests.jsonl", "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

# Upload the file to the File API
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

print(f"Uploaded file: {uploaded_file.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});
const fileName = "my-batch-requests.jsonl";

// Define the requests
const requests = [
    { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "Describe the process of photosynthesis." }] }] } },
    { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "What are the main ingredients in a Margherita pizza?" }] }] } }
];

// Construct the full path to file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.join(__dirname, fileName); // __dirname is the directory of the current script

async function writeBatchRequestsToFile(requests, filePath) {
    try {
        // Use a writable stream for efficiency, especially with larger files.
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });

        writeStream.on('error', (err) => {
            console.error(`Error writing to file ${filePath}:`, err);
        });

        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }

        writeStream.end();

        console.log(`Successfully wrote batch requests to ${filePath}`);

    } catch (error) {
        // This catch block is for errors that might occur before stream setup,
        // stream errors are handled by the 'error' event.
        console.error(`An unexpected error occurred:`, error);
    }
}

// Write to a file.
writeBatchRequestsToFile(requests, filePath);

// Upload the file to the File API.
const uploadedFile = await ai.files.upload({file: 'my-batch-requests.jsonl', config: {
    mimeType: 'jsonl',
}});
console.log(uploadedFile.name);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

Client client = new Client();

// Create a sample JSONL file
List<String> requests =
    Arrays.asList(
        "{\"key\": \"request-1\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"Describe the process of photosynthesis.\"}]}]}}",
        "{\"key\": \"request-2\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"What are the main ingredients in a Margherita pizza?\"}]}]}}");
Files.write(Paths.get("my-batch-requests.jsonl"), requests);

// Upload the file to the File API
UploadFileConfig uploadConfig =
    UploadFileConfig.builder()
        .displayName("my-batch-requests")
        .mimeType("jsonl")
        .build();
File uploadedFile = client.files.upload("my-batch-requests.jsonl", uploadConfig);

System.out.println("Uploaded file: " + uploadedFile.name().orElse(""));
```

### REST

```
tmp_batch_input_file=batch_input.tmp
echo -e '{"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generationConfig": {"temperature": 0.7}}\n{"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}' > batch_input.tmp
MIME_TYPE=$(file -b --mime-type "${tmp_batch_input_file}")
NUM_BYTES=$(wc -c < "${tmp_batch_input_file}")
DISPLAY_NAME=BatchInput

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
-D "${tmp_header_file}" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "X-Goog-Upload-Protocol: resumable" \
-H "X-Goog-Upload-Command: start" \
-H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
-H "Content-Type: application/jsonl" \
-d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
-H "Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Offset: 0" \
-H "X-Goog-Upload-Command: upload, finalize" \
--data-binary "@${tmp_batch_input_file}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
```

O exemplo a seguir chama o
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=pt-br#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
método com o arquivo de entrada enviado usando a API File:

### Python

```
from google import genai

# Assumes `uploaded_file` is the file object from the previous step
client = genai.Client()
file_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=uploaded_file.name,
    config={
        'display_name': "file-upload-job-1",
    },
)

print(f"Created batch job: {file_batch_job.name}")
```

### JavaScript

```
// Assumes `uploadedFile` is the file object from the previous step
const fileBatchJob = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: uploadedFile.name,
    config: {
        displayName: 'file-upload-job-1',
    }
});

console.log(fileBatchJob);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.CreateBatchJobConfig;

Client client = new Client();

// Assumes `uploadedFileName` is the file name from the previous step
String uploadedFileName = "files/my-batch-requests-id";

BatchJobSource src = BatchJobSource.builder().fileName(uploadedFileName).build();
CreateBatchJobConfig config =
    CreateBatchJobConfig.builder().displayName("file-upload-job-1").build();

BatchJob fileBatchJob = client.batches.create("gemini-3.8-flash", src, config);

System.out.println("Created batch job: " + fileBatchJob.name().orElse(""));
```

### REST

```
# Set the File ID taken from the upload response.
BATCH_INPUT_FILE='files/123456'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:batchGenerateContent \
-X POST \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" \
-d "{
    'batch': {
        'display_name': 'my-batch-requests',
        'input_config': {
            'file_name': '${BATCH_INPUT_FILE}'
        }
    }
}"
```

Ao criar um job em lote, você vai receber um nome de job retornado. Use esse nome
para [monitorar](#batch-job-status) o status do job e
[recuperar os resultados](#retrieve-batch-results) quando ele for concluído.

Confira abaixo um exemplo de saída que contém um nome de job:

```
Created batch job from file: batches/123456789
```

### Suporte a embedding em lote

É possível usar a API Batch para interagir com o
[modelo Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=pt-br) para maior capacidade.
Para criar um job em lote de embeddings com [solicitações inline](#inline-requests)
ou [arquivos de entrada](#input-file), use a API `batches.create_embeddings` e
especifique o modelo de embeddings.

### Python

```
from google import genai

client = genai.Client()

# Creating an embeddings batch job with an input file request:
file_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    src={'file_name': uploaded_batch_requests.name},
    config={'display_name': "Input embeddings batch"},
)

# Creating an embeddings batch job with an inline request:
batch_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    # For a predefined list of requests `inlined_requests`
    src={'inlined_requests': inlined_requests},
    config={'display_name': "Inlined embeddings batch"},
)
```

### JavaScript

```
// Creating an embeddings batch job with an input file request:
let fileJob;
fileJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    src: {fileName: uploadedBatchRequests.name},
    config: {displayName: 'Input embeddings batch'},
});
console.log(`Created batch job: ${fileJob.name}`);

// Creating an embeddings batch job with an inline request:
let batchJob;
batchJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    // For a predefined a list of requests `inlinedRequests`
    src: {inlinedRequests: inlinedRequests},
    config: {displayName: 'Inlined embeddings batch'},
});
console.log(`Created batch job: ${batchJob.name}`);
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.Content;
import com.google.genai.types.CreateEmbeddingsBatchJobConfig;
import com.google.genai.types.EmbedContentBatch;
import com.google.genai.types.EmbeddingsBatchJobSource;
import com.google.genai.types.Part;
import java.util.List;

Client client = new Client();

String uploadedFileName = "files/my-embedding-requests-id";

// Creating an embeddings batch job with an input file request:
BatchJob fileJob =
    client.batches.createEmbeddings(
        "gemini-embedding-2",
        EmbeddingsBatchJobSource.builder().fileName(uploadedFileName).build(),
        CreateEmbeddingsBatchJobConfig.builder().displayName("Input embeddings batch").build());
System.out.println("Created batch job: " + fileJob.name().orElse(""));

// Creating an embeddings batch job with an inline request:
EmbedContentBatch inlinedRequests =
    EmbedContentBatch.builder()
        .contents(Arrays.asList(Content.fromParts(Part.fromText("What is the meaning of life?"))))
        .build();
BatchJob batchJob =
    client.batches.createEmbeddings(
        "gemini-embedding-2",
        EmbeddingsBatchJobSource.builder().inlinedRequests(inlinedRequests).build(),
        CreateEmbeddingsBatchJobConfig.builder().displayName("Inlined embeddings batch").build());
System.out.println("Created batch job: " + batchJob.name().orElse(""));
```

Leia a seção Embeddings no [manual da API Batch](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)
para mais exemplos.

### Configuração das solicitações

É possível incluir todas as configurações de solicitação que você usaria em uma solicitação padrão não em lote. Por exemplo, você pode especificar a temperatura, as instruções do sistema ou até mesmo transmitir outras modalidades. O exemplo a seguir mostra uma solicitação inline que contém uma instrução do sistema para uma das solicitações:

### Python

```
inline_requests_list = [
    {'contents': [{'parts': [{'text': 'Write a short poem about a cloud.'}]}]},
    {'contents': [{
        'parts': [{
            'text': 'Write a short poem about a cat.'
            }]
        }],
    'config': {
        'system_instruction': {'parts': [{'text': 'You are a cat. Your name is Neko.'}]}}
    }
]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Write a short poem about a cloud.'}]}]},
    {contents: [{parts: [{text: 'Write a short poem about a cat.'}]}],
     config: {systemInstruction: {parts: [{text: 'You are a cat. Your name is Neko.'}]}}}
]
```

### Java

```
import java.util.Arrays;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import java.util.List;

List<InlinedRequest> inlineRequestsList =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Write a short poem about a cloud."))))
            .build(),
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Write a short poem about a cat."))))
            .config(
                GenerateContentConfig.builder()
                    .systemInstruction(
                        Content.fromParts(Part.fromText("You are a cat. Your name is Neko.")))
                    .build())
            .build());
```

Da mesma forma, é possível especificar as ferramentas a serem usadas para uma solicitação. O exemplo a seguir
mostra uma solicitação que ativa a ferramenta [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br):

### Python

```
inlined_requests = [
{'contents': [{'parts': [{'text': 'Who won the euro 1998?'}]}]},
{'contents': [{'parts': [{'text': 'Who won the euro 2025?'}]}],
 'config':{'tools': [{'google_search': {}}]}}]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Who won the euro 1998?'}]}]},
    {contents: [{parts: [{text: 'Who won the euro 2025?'}]}],
     config: {tools: [{googleSearch: {}}]}}
]
```

### Java

```
import java.util.Arrays;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GoogleSearch;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.Part;
import com.google.genai.types.Tool;
import java.util.List;

List<InlinedRequest> inlinedRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Who won the euro 1998?"))))
            .build(),
        InlinedRequest.builder()
            .contents(Arrays.asList(Content.fromParts(Part.fromText("Who won the euro 2025?"))))
            .config(
                GenerateContentConfig.builder()
                    .tools(Tool.builder().googleSearch(GoogleSearch.builder().build()).build())
                    .build())
            .build());
```

Também é possível especificar a saída [estruturada](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br).
O exemplo a seguir mostra como especificar para suas solicitações em lote.

### Python

```
import time
from google import genai
from pydantic import BaseModel, TypeAdapter

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    },
    {
        'contents': [{
            'parts': [{'text': 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.8-flash",
    src=inline_requests,
    config={
        'display_name': "structured-output-job-1"
    },
)

# wait for the job to finish
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

while True:
    batch_job_inline = client.batches.get(name=job_name)
    if batch_job_inline.state.name in ('JOB_STATE_SUCCEEDED', 'JOB_STATE_FAILED', 'JOB_STATE_CANCELLED', 'JOB_STATE_EXPIRED'):
        break
    print(f"Job not finished. Current state: {batch_job_inline.state.name}. Waiting 30 seconds...")
    time.sleep(30)

print(f"Job finished with state: {batch_job_inline.state.name}")

# print the response
for i, inline_response in enumerate(batch_job_inline.dest.inlined_responses, start=1):
    print(f"\n--- Response {i} ---")

    # Check for a successful response
    if inline_response.response:
        # The .text property is a shortcut to the generated text.
        print(inline_response.response.text)
```

### JavaScript

```
import {GoogleGenAI, Type} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    },
    {
        contents: [{
            parts: [{text: 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    }
]

const inlinedBatchJob = await ai.batches.create({
    model: 'gemini-3.8-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});
```

### Java

```
import java.util.HashMap;
import java.util.HashSet;
import java.util.Arrays;
import java.util.Collections;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import com.google.genai.types.Part;
import com.google.genai.types.Schema;
import com.google.genai.types.Type;
import java.util.List;
import java.util.Map;
import java.util.Set;

Client client = new Client();

Map<String, Schema> properties = new HashMap<>();
properties.put("recipeName", Schema.builder().type(Type.Known.STRING).build());
properties.put(
    "ingredients",
    Schema.builder()
        .type(Type.Known.ARRAY)
        .items(Schema.builder().type(Type.Known.STRING).build())
        .build());

Schema recipeSchema =
    Schema.builder()
        .type(Type.Known.ARRAY)
        .items(
            Schema.builder()
                .type(Type.Known.OBJECT)
                .properties(
properties)
                .required("recipeName")
                .build())
        .build();

GenerateContentConfig jsonConfig =
    GenerateContentConfig.builder()
        .responseMimeType("application/json")
        .responseSchema(recipeSchema)
        .build();

List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(
                            Arrays.asList(
                                Part.fromText(
                                    "List a few popular cookie recipes, and include the amounts of ingredients.")))
                        .build()))
            .config(jsonConfig)
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.builder()
                        .role("user")
                        .parts(
                            Arrays.asList(
                                Part.fromText(
                                    "List a few popular gluten free cookie recipes, and include the amounts of ingredients.")))
                        .build()))
            .config(jsonConfig)
            .build());

BatchJob inlineBatchJob =
    client.batches.create(
        "gemini-3.8-flash",
        BatchJobSource.builder().inlinedRequests(inlineRequests).build(),
        CreateBatchJobConfig.builder().displayName("structured-output-job-1").build());

// Wait for the job to finish
String jobName = inlineBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJobInline = client.batches.get(jobName, null);
while (!completedStates.contains(batchJobInline.state().get().knownEnum())) {
  System.out.println(
      "Job not finished. Current state: " + batchJobInline.state().get() + ". Waiting 30 seconds...");
  Thread.sleep(30000);
  batchJobInline = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJobInline.state().get());

// Print the response
List<InlinedResponse> responses = batchJobInline.dest().get().inlinedResponses().orElse(Collections.emptyList());
for (int i = 0; i < responses.size(); i++) {
  System.out.println("\n--- Response " + (i + 1) + " ---");
  InlinedResponse inlineResponse = responses.get(i);
  if (inlineResponse.response().isPresent()) {
    System.out.println(inlineResponse.response().get().text());
  }
}
```

Confira abaixo um exemplo de saída desse job:

```
--- Response 1 ---
[
  {
    "recipe_name": "Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 1/4 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Oatmeal Raisin Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 cup packed light brown sugar",
      "1/2 cup granulated sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "1 1/2 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1 teaspoon ground cinnamon",
      "1/2 teaspoon salt",
      "3 cups old-fashioned rolled oats",
      "1 cup raisins"
    ]
  },
  {
    "recipe_name": "Sugar Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 1/2 cups granulated sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 3/4 cups all-purpose flour",
      "1 teaspoon baking powder",
      "1/2 teaspoon salt"
    ]
  }
]

--- Response 2 ---
[
  {
    "recipe_name": "Gluten-Free Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "2 1/4 cups gluten-free all-purpose flour blend (with xanthan gum)",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Gluten-Free Peanut Butter Cookies",
    "ingredients": [
      "1 cup (250g) creamy peanut butter",
      "1/2 cup (100g) granulated sugar",
      "1/2 cup (100g) packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1/2 teaspoon baking soda",
      "1/4 teaspoon salt"
    ]
  },
  {
    "recipe_name": "Gluten-Free Oatmeal Raisin Cookies",
    "ingredients": [
      "1/2 cup (1 stick) unsalted butter, softened",
      "1/2 cup granulated sugar",
      "1/2 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1 cup gluten-free all-purpose flour blend",
      "1/2 teaspoon baking soda",
      "1/2 teaspoon ground cinnamon",
      "1/4 teaspoon salt",
      "1 1/2 cups gluten-free rolled oats",
      "1/2 cup raisins"
    ]
  }
]
```

## Como monitorar o status do job

Use o nome da operação recebido ao criar o job em lote para pesquisar o status dele.
O campo de estado do job em lote vai indicar o status atual. Um job em lote pode estar em um dos seguintes estados:

- `JOB_STATE_PENDING`: o job foi criado e está aguardando o processamento pelo serviço.
- `JOB_STATE_RUNNING`: o job está em andamento.
- `JOB_STATE_SUCCEEDED`: o job foi concluído. Agora é possível recuperar os resultados.
- `JOB_STATE_FAILED`: o job falhou. Confira os detalhes do erro para mais informações.
- `JOB_STATE_CANCELLED`: o job foi cancelado pelo usuário.
- `JOB_STATE_EXPIRED`: o job expirou porque estava em execução ou pendente por mais de 48 horas. O job não terá resultados para recuperar.
  Tente enviar o job novamente ou dividir as solicitações em lotes menores.

É possível pesquisar o status do job periodicamente para verificar a conclusão.

### Python

```
import time
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"  # (e.g. 'batches/your-batch-id')
batch_job = client.batches.get(name=job_name)

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

print(f"Polling status for job: {job_name}")
batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(30) # Wait for 30 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")
if batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
let batchJob;
const completedStates = new Set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
]);

try {
    batchJob = await ai.batches.get({name: inlinedBatchJob.name});
    while (!completedStates.has(batchJob.state)) {
        console.log(`Current state: ${batchJob.state}`);
        // Wait for 30 seconds before polling again
        await new Promise(resolve => setTimeout(resolve, 30000));
        batchJob = await client.batches.get({ name: batchJob.name });
    }
    console.log(`Job finished with state: ${batchJob.state}`);
    if (batchJob.state === 'JOB_STATE_FAILED') {
        // The exact structure of `error` might vary depending on the SDK
        // This assumes `error` is an object with a `message` property.
        console.error(`Error: ${batchJob.state}`);
    }
} catch (error) {
    console.error(`An error occurred while polling job ${batchJob.name}:`, error);
}
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.JobState;
import java.util.Set;

Client client = new Client();

// Use the name of the job you want to check
String jobName = "batches/your-batch-id";

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

System.out.println("Polling status for job: " + jobName);
BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(30000); // Wait for 30 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### Pesquisa e webhooks

**Cansou de pesquisar?** O Gemini agora oferece suporte a
[webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=pt-br) para processar conclusões de forma assíncrona.
Em vez de chamar continuamente `GET / operations`, inscreva-se em `batch.succeeded` diretamente para permitir que a API Gemini envie notificações em tempo real ao seu servidor quando operações assíncronas ou de longa duração forem concluídas.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

print(f"Created webhook: {webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  console.log(`Created webhook: ${webhook.name}`);
}

createWebhook();
```

### Java

```
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.gaos.models.webhooks.Webhook;
import com.google.genai.gaos.models.webhooks.WebhookInput;
import com.google.genai.gaos.models.webhooks.WebhookSubscribedEvent;
import java.util.List;

Client client = new Client();

WebhookInput input =
    WebhookInput.builder()
        .name("MyBatchWebhook")
        .subscribedEvents(
            Arrays.asList(
                WebhookSubscribedEvent.BATCH_SUCCEEDED,
                WebhookSubscribedEvent.BATCH_FAILED))
        .uri("https://my-api.com/gemini-callback")
        .build();

Webhook webhook = client.webhooks.create(input).webhook().get();
System.out.println("Created webhook: " + webhook.name().orElse(""));
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks?webhook_id=my-example-webhook-123" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "name": "My Example Webhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

## Como recuperar resultados

Quando o status do job indicar que o job em lote foi concluído, os resultados estarão disponíveis no campo `response`.
Por padrão, os resultados do job em lote são armazenados e ficam disponíveis para download por seis semanas antes de serem excluídos permanentemente.

### Python

```
import json
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"
batch_job = client.batches.get(name=job_name)

if batch_job.state.name == 'JOB_STATE_SUCCEEDED':

    # If batch job was created with a file
    if batch_job.dest and batch_job.dest.file_name:
        # Results are in a file
        result_file_name = batch_job.dest.file_name
        print(f"Results are in file: {result_file_name}")

        print("Downloading result file content...")
        file_content = client.files.download(file=result_file_name)
        # Process file_content (bytes) as needed
        print(file_content.decode('utf-8'))

    # If batch job was created with inline request
    # (for embeddings, use batch_job.dest.inlined_embed_content_responses)
    elif batch_job.dest and batch_job.dest.inlined_responses:
        # Results are inline
        print("Results are inline:")
        for i, inline_response in enumerate(batch_job.dest.inlined_responses):
            print(f"Response {i+1}:")
            if inline_response.response:
                # Accessing response, structure may vary.
                try:
                    print(inline_response.response.text)
                except AttributeError:
                    print(inline_response.response) # Fallback
            elif inline_response.error:
                print(f"Error: {inline_response.error}")
    else:
        print("No results found (neither file nor inline).")
else:
    print(f"Job did not succeed. Final state: {batch_job.state.name}")
    if batch_job.error:
        print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
const jobName = "YOUR_BATCH_JOB_NAME";

try {
    const batchJob = await ai.batches.get({ name: jobName });

    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        console.log('Found completed batch:', batchJob.displayName);
        console.log(batchJob);

        // If batch job was created with a file destination
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);

            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });

            // Process fileContentBuffer (Buffer) as needed
            console.log(fileContentBuffer.toString('utf-8'));
        }

        // If batch job was created with inline responses
        else if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    // Accessing response, structure may vary.
                    if (inlineResponse.response.text !== undefined) {
                        console.log(inlineResponse.response.text);
                    } else {
                        console.log(inlineResponse.response); // Fallback
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        }

        // If batch job was an embedding batch with inline responses
        else if (batchJob.dest?.inlinedEmbedContentResponses) {
            console.log("Embedding results found inline:");
            for (let i = 0; i < batchJob.dest.inlinedEmbedContentResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedEmbedContentResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    console.log(inlineResponse.response);
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No results found (neither file nor inline).");
        }
    } else {
        console.log(`Job did not succeed. Final state: ${batchJob.state}`);
        if (batchJob.error) {
            console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
        }
    }
} catch (error) {
    console.error(`An error occurred while processing job ${jobName}:`, error);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobDestination;
import com.google.genai.types.InlinedEmbedContentResponse;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

Client client = new Client();

// Use the name of the job you want to check
String jobName = "batches/your-batch-id";
BatchJob batchJob = client.batches.get(jobName, null);

if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  BatchJobDestination dest = batchJob.dest().orElse(null);

  // If batch job was created with a file destination
  if (dest != null && dest.fileName().isPresent()) {
    String resultFileName = dest.fileName().get();
    System.out.println("Results are in file: " + resultFileName);

    System.out.println("Downloading result file content...");
    client.files.download(resultFileName, "batch_results.jsonl", null);
    String fileContent = Files.readString(Paths.get("batch_results.jsonl"));
    System.out.println(fileContent);
  }
  // If batch job was created with inline requests
  else if (dest != null && dest.inlinedResponses().isPresent()) {
    System.out.println("Results are inline:");
    List<InlinedResponse> responses = dest.inlinedResponses().get();
    for (int i = 0; i < responses.size(); i++) {
      System.out.println("Response " + (i + 1) + ":");
      InlinedResponse inlineResponse = responses.get(i);
      if (inlineResponse.response().isPresent()) {
        System.out.println(inlineResponse.response().get().text());
      } else if (inlineResponse.error().isPresent()) {
        System.out.println("Error: " + inlineResponse.error().get());
      }
    }
  }
  // If batch job was an embedding batch with inline responses
  else if (dest != null && dest.inlinedEmbedContentResponses().isPresent()) {
    System.out.println("Embedding results found inline:");
    List<InlinedEmbedContentResponse> responses = dest.inlinedEmbedContentResponses().get();
    for (int i = 0; i < responses.size(); i++) {
      System.out.println("Response " + (i + 1) + ":");
      InlinedEmbedContentResponse inlineResponse = responses.get(i);
      if (inlineResponse.response().isPresent()) {
        System.out.println(inlineResponse.response().get());
      } else if (inlineResponse.error().isPresent()) {
        System.out.println("Error: " + inlineResponse.error().get());
      }
    }
  } else {
    System.out.println("No results found (neither file nor inline).");
  }
} else {
  System.out.println("Job did not succeed. Final state: " + batchJob.state().get());
  batchJob.error().ifPresent(err -> System.out.println("Error: " + err));
}
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null > batch_status.json

if jq -r '.done' batch_status.json | grep -q "false"; then
    echo "Batch has not finished processing"
fi

batch_state=$(jq -r '.metadata.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    if [[ $(jq '.response | has("inlinedResponses")' batch_status.json) = "true" ]]; then
        jq -r '.response.inlinedResponses' batch_status.json
        exit
    fi
    responses_file_name=$(jq -r '.response.responsesFile' batch_status.json)
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
    -H "x-goog-api-key: $GEMINI_API_KEY" 2> /dev/null
elif [[ $batch_state = "JOB_STATE_FAILED" ]]; then
    jq '.error' batch_status.json
elif [[ $batch_state == "JOB_STATE_CANCELLED" ]]; then
    echo "Batch was cancelled by the user"
elif [[ $batch_state == "JOB_STATE_EXPIRED" ]]; then
    echo "Batch expired after 48 hours"
fi
```

## Como listar jobs em lote

É possível listar seus jobs em lote recentes.

### Python

```
batch_jobs = client.batches.list()

# Optional query config:
# batch_jobs = client.batches.list(config={'page_size': 5})

for batch_job in batch_jobs:
    print(batch_job)
```

### JavaScript

```
const batchJobs = await ai.batches.list();

// Optional query config:
// const batchJobs = await ai.batches.list({config: {'pageSize': 5}});

for await (const batchJob of batchJobs) {
    console.log(batchJob);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.Pager;
import com.google.genai.types.BatchJob;
import com.google.genai.types.ListBatchJobsConfig;

Client client = new Client();

Pager<BatchJob> batchJobs = client.batches.list(null);

// Optional query config:
// Pager<BatchJob> batchJobs = client.batches.list(ListBatchJobsConfig.builder().pageSize(5).build());

for (BatchJob batchJob : batchJobs) {
  System.out.println(batchJob);
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/batches \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Como cancelar um job em lote

É possível cancelar um job em lote em andamento usando o nome dele. Quando um job é cancelado, ele para de processar novas solicitações.

### Python

```
client.batches.cancel(name=batch_job_to_cancel.name)
```

### JavaScript

```
await ai.batches.cancel({name: batchJobToCancel.name});
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

String batchJobToCancelName = "batches/your-batch-id";
client.batches.cancel(batchJobToCancelName, null);
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Cancel the batch
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME:cancel \
-H "x-goog-api-key: $GEMINI_API_KEY" \

# Confirm that the status of the batch after cancellation is JOB_STATE_CANCELLED
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null | jq -r '.metadata.state'
```

## Como excluir um job em lote

É possível excluir um job em lote usando o nome dele. Quando um job é excluído, ele para de processar novas solicitações e é removido da lista de jobs em lote.

### Python

```
client.batches.delete(name=batch_job_to_delete.name)
```

### JavaScript

```
await ai.batches.delete({name: batchJobToDelete.name});
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

String batchJobToDeleteName = "batches/your-batch-id";
client.batches.delete(batchJobToDeleteName, null);
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Delete the batch job
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Como gerar imagens em lote

Se você estiver usando [Gemini Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) e precisar gerar muitas
imagens, use a API Batch para receber limites de taxa
[mais altos](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br) em troca de um tempo de resposta de até
24 horas.

É possível usar [solicitações inline](#inline-requests-images) para pequenos lotes de solicitações (abaixo de 20 MB) ou
um [arquivo de entrada JSONL](#input-file-images) para lotes grandes (recomendado para geração de imagens):

### Solicitações inline para imagens

### Python

```
import time
import base64
import json
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create batch job with inline requests
inline_requests = [
    {
        'contents': [{'parts': [{'text': 'A big letter A surrounded by animals starting with the A letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    },
    {
        'contents': [{'parts': [{'text': 'A big letter B surrounded by animals starting with the B letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=inline_requests,
    config={
        'display_name': "inlined-image-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")

# 2. Monitor job status
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 3. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    print("Results are inline:")
    for i, inline_response in enumerate(batch_job.dest.inlined_responses):
        print(f"Response {i+1}:")
        if inline_response.response:
            for part in inline_response.response.candidates[0].content.parts:
                if part.text:
                    print(part.text)
                elif part.inline_data:
                    print(f"Image mime type: {part.inline_data.mime_type}")
                    image = part.as_image()
                    image.save(f"image_{i+1}.png")
        elif inline_response.error:
            print(f"Error: {inline_response.error}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create batch job with inline requests
    const inlinedRequests = [
        {
            contents: [{parts: [{text: 'A big letter A surrounded by animals starting with the A letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        },
        {
            contents: [{parts: [{text: 'A big letter B surrounded by animals starting with the B letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        }
    ]

    const inlineBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: inlinedRequests,
        config: {
            displayName: 'inlined-image-requests-job-1',
        }
    });

    console.log(inlineBatchJob);

    // 2. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: inlineBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${inlineBatchJob.name}:`, error);
        return;
    }

    // 3. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    for (const part of inlineResponse.response.candidates[0].content.parts) {
                        if (part.text) {
                            console.log(part.text);
                        } else if (part.inlineData) {
                            console.log(`Image mime type: ${part.inlineData.mimeType}`);
                        }
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No inline results found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import java.util.Collections;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.Content;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.InlinedRequest;
import com.google.genai.types.InlinedResponse;
import com.google.genai.types.JobState;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

Client client = new Client();

// 1. Create batch job with inline requests
GenerateContentConfig imageConfig =
    GenerateContentConfig.builder().responseModalities("TEXT", "IMAGE").build();

List<InlinedRequest> inlineRequests =
    Arrays.asList(
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromText(
                            "A big letter A surrounded by animals starting with the A letter"))))
            .config(imageConfig)
            .build(),
        InlinedRequest.builder()
            .contents(
                Arrays.asList(
                    Content.fromParts(
                        Part.fromText(
                            "A big letter B surrounded by animals starting with the B letter"))))
            .config(imageConfig)
            .build());

BatchJob inlineBatchJob =
    client.batches.create(
        "gemini-3-pro-image-preview",
        BatchJobSource.builder().inlinedRequests(inlineRequests).build(),
        CreateBatchJobConfig.builder().displayName("inlined-image-requests-job-1").build());

System.out.println("Created batch job: " + inlineBatchJob.name().orElse(""));

// 2. Monitor job status
String jobName = inlineBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(10000); // Wait for 10 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());

// 3. Retrieve results
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  System.out.println("Results are inline:");
  List<InlinedResponse> responses = batchJob.dest().get().inlinedResponses().orElse(Collections.emptyList());
  for (int i = 0; i < responses.size(); i++) {
    System.out.println("Response " + (i + 1) + ":");
    InlinedResponse inlineResponse = responses.get(i);
    if (inlineResponse.response().isPresent()) {
      for (Part part : inlineResponse.response().get().parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          System.out.println("Image mime type: " + part.inlineData().get().mimeType().orElse(""));
          Files.write(
              Paths.get("image_" + (i + 1) + ".png"),
              part.inlineData().get().data().get());
        }
      }
    } else if (inlineResponse.error().isPresent()) {
      System.out.println("Error: " + inlineResponse.error().get());
    }
  }
} else if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### REST

```
# 1. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-image-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-1" }
                    },
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-2" }
                    }
                ]
            }
        }
    }
}'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 2. Poll job status until completion by repeating the following command
# Replace $BATCH_NAME with the name returned above.
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 3. If state is JOB_STATE_SUCCEEDED, retrieve results from batch_status.json
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    echo "Job succeeded. Results:"
    jq -r '.dest.inlinedResponses' batch_status.json
fi
```

### Arquivo de entrada para imagens

### Python

```
import json
import time
import base64
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create and upload file
file_name = "my-batch-image-requests.jsonl"
with open(file_name, "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

uploaded_file = client.files.upload(
    file=file_name,
    config=types.UploadFileConfig(display_name='my-batch-image-requests', mime_type='jsonl')
)
print(f"Uploaded file: {uploaded_file.name}")

# 2. Create batch job
file_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=uploaded_file.name,
    config={
        'display_name': "file-image-upload-job-1",
    },
)
print(f"Created batch job: {file_batch_job.name}")

# 3. Monitor job status
job_name = file_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 4. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    result_file_name = batch_job.dest.file_name
    print(f"Results are in file: {result_file_name}")
    print("Downloading result file content...")
    file_content_bytes = client.files.download(file=result_file_name)
    file_content = file_content_bytes.decode('utf-8')
    # The result file is also a JSONL file. Parse and print each line.
    for line in file_content.splitlines():
      if line:
        parsed_response = json.loads(line)
        if 'response' in parsed_response and parsed_response['response']:
            for part in parsed_response['response']['candidates'][0]['content']['parts']:
              if part.get('text'):
                print(part['text'])
              elif part.get('inlineData'):
                print(f"Image mime type: {part['inlineData']['mimeType']}")
                data = base64.b64decode(part['inlineData']['data'])
        elif 'error' in parsed_response:
            print(f"Error: {parsed_response['error']}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create and upload file
    const fileName = "my-batch-image-requests.jsonl";
    const requests = [
        { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "A big letter A surrounded by animals starting with the A letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } },
        { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "A big letter B surrounded by animals starting with the B letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } }
    ];
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    const filePath = path.join(__dirname, fileName);

    try {
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });
        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }
        writeStream.end();
        console.log(`Successfully wrote batch requests to ${filePath}`);
    } catch (error) {
        console.error(`An unexpected error occurred writing file:`, error);
        return;
    }

    const uploadedFile = await ai.files.upload({file: fileName, config: { mimeType: 'jsonl' }});
    console.log(`Uploaded file: ${uploadedFile.name}`);

    // 2. Create batch job
    const fileBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: uploadedFile.name,
        config: {
            displayName: 'file-image-upload-job-1',
        }
    });
    console.log(fileBatchJob);

    // 3. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: fileBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${fileBatchJob.name}:`, error);
        return;
    }

    // 4. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);
            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });
            const fileContent = fileContentBuffer.toString('utf-8');
            for (const line of fileContent.split('\n')) {
                if (line) {
                    const parsedResponse = JSON.parse(line);
                    if (parsedResponse.response) {
                        for (const part of parsedResponse.response.candidates[0].content.parts) {
                            if (part.text) {
                                console.log(part.text);
                            } else if (part.inlineData) {
                                console.log(`Image mime type: ${part.inlineData.mimeType}`);
                            }
                        }
                    } else if (parsedResponse.error) {
                        console.error(`Error: ${parsedResponse.error}`);
                    }
                }
            }
        } else {
            console.log("No result file found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### Java

```
import java.util.HashSet;
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.BatchJob;
import com.google.genai.types.BatchJobSource;
import com.google.genai.types.CreateBatchJobConfig;
import com.google.genai.types.File;
import com.google.genai.types.JobState;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

Client client = new Client();

// 1. Create and upload file
String fileName = "my-batch-image-requests.jsonl";
List<String> requests =
    Arrays.asList(
        "{\"key\": \"request-1\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"A big letter A surrounded by animals starting with the A letter\"}]}], \"generation_config\": {\"responseModalities\": [\"TEXT\", \"IMAGE\"]}}}",
        "{\"key\": \"request-2\", \"request\": {\"contents\": [{\"parts\": [{\"text\": \"A big letter B surrounded by animals starting with the B letter\"}]}], \"generation_config\": {\"responseModalities\": [\"TEXT\", \"IMAGE\"]}}}");
Files.write(Paths.get(fileName), requests);

File uploadedFile =
    client.files.upload(
        fileName,
        UploadFileConfig.builder()
            .displayName("my-batch-image-requests")
            .mimeType("jsonl")
            .build());
System.out.println("Uploaded file: " + uploadedFile.name().orElse(""));

// 2. Create batch job
BatchJob fileBatchJob =
    client.batches.create(
        "gemini-3-pro-image-preview",
        BatchJobSource.builder().fileName(uploadedFile.name().get()).build(),
        CreateBatchJobConfig.builder().displayName("file-image-upload-job-1").build());
System.out.println("Created batch job: " + fileBatchJob.name().orElse(""));

// 3. Monitor job status
String jobName = fileBatchJob.name().get();
System.out.println("Polling status for job: " + jobName);

Set<JobState.Known> completedStates =
    new HashSet<>(Arrays.asList(
        JobState.Known.JOB_STATE_SUCCEEDED,
        JobState.Known.JOB_STATE_FAILED,
        JobState.Known.JOB_STATE_CANCELLED,
        JobState.Known.JOB_STATE_EXPIRED));

BatchJob batchJob = client.batches.get(jobName, null);
while (!completedStates.contains(batchJob.state().get().knownEnum())) {
  System.out.println("Current state: " + batchJob.state().get());
  Thread.sleep(10000); // Wait for 10 seconds before polling again
  batchJob = client.batches.get(jobName, null);
}

System.out.println("Job finished with state: " + batchJob.state().get());

// 4. Retrieve results
if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_SUCCEEDED) {
  String resultFileName = batchJob.dest().get().fileName().get();
  System.out.println("Results are in file: " + resultFileName);
  System.out.println("Downloading result file content...");
  client.files.download(resultFileName, "batch_image_results.jsonl", null);
  for (String line : Files.readAllLines(Paths.get("batch_image_results.jsonl"))) {
    if (!line.isEmpty()) {
      System.out.println(line);
    }
  }
} else if (batchJob.state().get().knownEnum() == JobState.Known.JOB_STATE_FAILED) {
  System.out.println("Error: " + batchJob.error().orElse(null));
}
```

### REST

```
# 1. Create and upload file
echo '{"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' > my-batch-image-requests.jsonl
echo '{"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' >> my-batch-image-requests.jsonl

# Follow File API guide to upload: https://ai.google.dev/gemini-api/docs/files#upload_a_file
# This example assumes you have uploaded the file and set BATCH_INPUT_FILE to its name (e.g., files/abcdef123)
BATCH_INPUT_FILE="files/your-uploaded-file-name"

# 2. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-file-image-requests",
        "input_config": { "file_name": "%s" }
    }
}' "$BATCH_INPUT_FILE"
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -X POST \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 3. Poll job status until completion by repeating the following command:
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 4. If state is JOB_STATE_SUCCEEDED, download results file
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    responses_file_name=$(jq -r '.dest.fileName' batch_status.json)
    echo "Job succeeded. Downloading results from $responses_file_name..."
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
      -H "x-goog-api-key: $GEMINI_API_KEY" > batch_results.jsonl
    echo "Results saved to batch_results.jsonl"
fi
```

## Detalhes técnicos

- **Modelos compatíveis**:a API Batch oferece suporte a uma variedade de modelos do Gemini.
  Consulte a [página Modelos](https://ai.google.dev/gemini-api/docs/models?hl=pt-br) para saber mais sobre o suporte
  da API Batch para cada modelo. As modalidades compatíveis com a API Batch são as mesmas que têm suporte na API interativa (ou não em lote).
- **Preços**:o uso da API Batch tem um preço de 50% do custo padrão da API interativa para o modelo equivalente. Consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br)
  para mais detalhes. Consulte a [página de limites de taxa](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br#batch-mode)
  para mais detalhes sobre os limites de taxa desse recurso.
- **Objetivo de nível de serviço (SLO)** : os jobs em lote são projetados para serem concluídos em um tempo de resposta de 24 horas. Muitos jobs podem ser concluídos muito mais rápido, dependendo do tamanho e da carga atual do sistema.
- **Armazenamento em cache:** [o armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) é compatível
  com solicitações em lote. Reutilize o conteúdo armazenado em cache especificando o nome do recurso `cached_content` na configuração de solicitações individuais no lote.
  Se uma solicitação no lote resultar em uma ocorrência em cache, você pagará as
  [taxas padrão de armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).

## Práticas recomendadas

- **Usar arquivos de entrada para solicitações grandes:** Para um grande número de solicitações,
  sempre use o método de entrada de arquivo
  para melhor gerenciamento e para evitar atingir os limites de tamanho da solicitação para
  a chamada [`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=pt-br#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent). Há um limite de tamanho de arquivo de 2 GB por arquivo de entrada.
- **Tratamento de erros**:verifique o `batchStats` para `failedRequestCount` após a conclusão de um job. Se você estiver usando a saída de arquivo, analise cada linha para verificar se ela é um objeto `GenerateContentResponse` ou de status que indica um erro para essa solicitação específica. Consulte o [guia
  de solução de problemas](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pt-br#error-codes) para ver um conjunto completo de
  códigos de erro.
- **Enviar jobs uma vez**:a criação de um job em lote não é idempotente.
  Se você enviar a mesma solicitação de criação duas vezes, dois jobs em lote separados serão criados.
- **Dividir lotes muito grandes**:embora o tempo de resposta esperado seja de 24 horas, o tempo de processamento real pode variar com base na carga do sistema e no tamanho do job.
  Para jobs grandes, considere dividi-los em lotes menores se os resultados intermediários forem necessários mais cedo.

## A seguir

- Confira o [notebook da API Batch](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb?hl=pt-br)
  para mais exemplos.
- A camada de compatibilidade com a OpenAI oferece suporte à API Batch. Leia os exemplos na
  [página de compatibilidade do OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br#batch).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-18 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-18 UTC."],[],[]]
