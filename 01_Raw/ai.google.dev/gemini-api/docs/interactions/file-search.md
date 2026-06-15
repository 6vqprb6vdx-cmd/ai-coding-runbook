---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=pt-BR
fetched_at: 2026-06-15T06:20:13.266001+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Pesquisa de arquivos

A API Gemini permite a geração aumentada por recuperação (RAG) com a ferramenta de pesquisa de arquivos. A Pesquisa de arquivos importa, divide e indexa seus dados para permitir a recuperação rápida de informações relevantes com base em um comando fornecido. Essas informações recuperadas são usadas como contexto para o modelo, permitindo que ele forneça respostas mais precisas e relevantes. A pesquisa de arquivos também pode oferecer recursos multimodais com embeddings de texto compatíveis com `gemini-embedding-001` e embeddings de imagem/multimodais compatíveis com `gemini-embedding-2`.

O armazenamento de arquivos e a geração de embeddings no momento da consulta são sem custo financeiro. Você só paga pela criação de embeddings quando indexa seus arquivos pela primeira vez e pelo custo normal dos tokens de entrada / saída do modelo do Gemini. Esse novo paradigma de faturamento torna a ferramenta de pesquisa de arquivos mais fácil e econômica de criar e dimensionar. Consulte a seção de [preços](#pricing) para detalhes.

## Fazer upload diretamente para o repositório da Pesquisa de arquivos

Este exemplo mostra como fazer upload direto de um arquivo para o
[repositório de pesquisa de arquivos](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#method:-media.uploadtofilesearchstore):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.upload_to_file_search_store(
  file='sample.txt',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'display-file-name',
  }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "file_citation":
                            print(f"  - {annotation.file_name}: {annotation.source}")
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.uploadToFileSearchStore({
    file: 'file.txt',
    fileSearchStoreName: fileSearchStore.name,
    config: {
      displayName: 'file-name',
    }
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation });
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'file_citation') {
                console.log(`  - ${annotation.file_name}: ${annotation.source}`);
              }
            }
          }
        }
      }
    }
  }
}

run();
```

Consulte a referência da API para [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#method:-media.uploadtofilesearchstore) para mais informações.

## Como importar arquivos

Como alternativa, você pode fazer upload de um arquivo e [importar para o repositório de pesquisa de arquivos](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#method:-filesearchstores.importfile):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

sample_file = client.files.upload(file='sample.txt', config={'display_name': 'display_file_name'})

file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { displayName: 'file-name' }
  });

  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.importFile({
    fileSearchStoreName: fileSearchStore.name,
    fileName: sampleFile.name
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation: operation });
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
        }
      }
    }
  }
}

run();
```

Consulte a referência da API para [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#method:-filesearchstores.importfile) para mais informações.

## Configuração de divisão

Quando você importa um arquivo para um repositório de pesquisa de arquivos, ele é automaticamente dividido em partes, incorporado, indexado e enviado para o repositório de pesquisa de arquivos. Se você precisar de mais controle sobre a estratégia de divisão em partes, especifique uma configuração [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#request-body_5) para definir um número máximo de tokens por parte e um número máximo de tokens sobrepostos.

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file='sample.txt',
    config={
        'chunking_config': {
          'white_space_config': {
            'max_tokens_per_chunk': 200,
            'max_overlap_tokens': 20
          }
        }
    }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

print("Custom chunking complete.")
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

let operation = await ai.fileSearchStores.uploadToFileSearchStore({
  file: 'file.txt',
  fileSearchStoreName: fileSearchStore.name,
  config: {
    displayName: 'file-name',
    chunkingConfig: {
      whiteSpaceConfig: {
        maxTokensPerChunk: 200,
        maxOverlapTokens: 20
      }
    }
  }
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 5000));
  operation = await ai.operations.get({ operation });
}
console.log("Custom chunking complete.");
```

Para usar o armazenamento da Pesquisa de arquivos, transmita-o como uma ferramenta para o método `interactions.create`, conforme mostrado nos exemplos de [Upload](#upload) e [Importação](#importing-files).

## Como funciona

A Pesquisa de arquivos usa uma técnica chamada pesquisa semântica para encontrar informações relevantes para o comando do usuário. Ao contrário da pesquisa padrão baseada em palavras-chave, a pesquisa semântica entende o significado e o contexto da sua consulta.

Quando você importa um arquivo, ele é convertido em representações numéricas chamadas [embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=pt-br), que capturam o significado semântico do conteúdo enviado. Esses embeddings são armazenados em um banco de dados especializado da Pesquisa de arquivos.
Quando você faz uma consulta, ela também é convertida em um embedding. Em seguida, o sistema realiza uma pesquisa de arquivos para encontrar os trechos de documentos mais semelhantes e relevantes no repositório de pesquisa de arquivos.

Não há um Time To Live (TTL) para incorporações. Elas persistem até serem excluídas manualmente ou quando o modelo é descontinuado. No entanto, os arquivos são excluídos após 48 horas.

Confira um detalhamento do processo para usar a API File Search
`uploadToFileSearchStore`:

1. **Crie um repositório de pesquisa de arquivos**: um repositório de pesquisa de arquivos contém os dados processados dos seus arquivos. É o contêiner persistente para os embeddings em que a pesquisa semântica vai operar.
2. **Fazer upload de um arquivo e importar para um repositório da Pesquisa de arquivos**: faça upload de um arquivo e importe os resultados para o repositório da Pesquisa de arquivos ao mesmo tempo. Isso cria um objeto `File` temporário, que é uma referência ao seu documento bruto. Esses dados são divididos em partes, convertidos em embeddings da pesquisa de arquivos e indexados. O objeto `File`
   é excluído após 48 horas, enquanto os dados importados para o repositório
   da Pesquisa de arquivos são armazenados indefinidamente até que você os exclua.
3. **Consulta com a Pesquisa de arquivos**: por fim, use a ferramenta `FileSearch` em uma chamada `generateContent`. Na configuração da ferramenta, especifique um
   `FileSearchRetrievalResource`, que aponta para o `FileSearchStore` que você quer
   pesquisar. Isso instrui o modelo a realizar uma pesquisa semântica no repositório específico da Pesquisa de arquivos para encontrar informações relevantes e embasar a resposta.

![O processo de indexação e consulta da Pesquisa de arquivos](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=pt-br)

O processo de indexação e consulta da Pesquisa de arquivos

Neste diagrama, a linha pontilhada de *Documentos* para *Modelo de incorporação* (usando [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=pt-br)) representa a API `uploadToFileSearchStore` (ignorando *Armazenamento de arquivos*). Caso contrário, usar a [API Files](https://ai.google.dev/gemini-api/docs/interactions/files?hl=pt-br) para criar e importar arquivos separadamente move o processo de indexação de *Documentos* para *Armazenamento de arquivos* e, em seguida, para *Modelo de incorporação*.

## Armazenamentos da Pesquisa de arquivos

Um repositório de pesquisa de arquivos é um contêiner para seus embeddings de documentos. Embora os arquivos brutos enviados pela API File sejam excluídos após 48 horas, os dados importados para um repositório de pesquisa de arquivos são armazenados indefinidamente até que você os exclua manualmente. É possível criar vários repositórios de pesquisa de arquivos para organizar seus documentos. A API `FileSearchStore` permite criar, listar, receber e excluir para gerenciar seus repositórios de pesquisa de arquivos. Os nomes dos repositórios de pesquisa de arquivos têm escopo global.

Confira alguns exemplos de como gerenciar suas lojas de pesquisa de arquivos:

### Python

```
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'my-file_search-store-123',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

for file_search_store in client.file_search_stores.list():
    print(file_search_store)

my_file_search_store = client.file_search_stores.get(name='fileSearchStores/my-file_search-store-123')

client.file_search_stores.delete(name='fileSearchStores/my-file_search-store-123', config={'force': True})
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: 'my-file_search-store-123',
    embeddingModel: 'models/gemini-embedding-2'
  }
});

const fileSearchStores = await ai.fileSearchStores.list();
for await (const store of fileSearchStores) {
  console.log(store);
}

const myFileSearchStore = await ai.fileSearchStores.get({
  name: 'fileSearchStores/my-file_search-store-123'
});

await ai.fileSearchStores.delete({
  name: 'fileSearchStores/my-file_search-store-123',
  config: { force: true }
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"
```

## Documentos da pesquisa de arquivos

É possível gerenciar documentos individuais nos seus repositórios de arquivos com a
API [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=pt-br) para `list` cada documento
em um repositório de pesquisa de arquivos, `get` informações sobre um documento e `delete` um
documento por nome.

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc', config={'force': True})
```

### JavaScript

```
const documents = await ai.fileSearchStores.documents.list({
  parent: 'fileSearchStores/my-file_search-store-123'
});
for await (const doc of documents) {
  console.log(doc);
}

const fileSearchDocument = await ai.fileSearchStores.documents.get({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}&force=true"
```

## Metadados do arquivo

É possível adicionar metadados personalizados aos arquivos para ajudar a filtrá-los ou fornecer mais contexto. Os metadados são um conjunto de pares de chave-valor.

### Python

```
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    config={
        'custom_metadata': [
            {"key": "author", "string_value": "Robert Graves"},
            {"key": "year", "numeric_value": 1934}
        ]
    }
)
```

### JavaScript

```
let operation = await ai.fileSearchStores.importFile({
  fileSearchStoreName: fileSearchStore.name,
  fileName: sampleFile.name,
  config: {
    customMetadata: [
      { key: "author", stringValue: "Robert Graves" },
      { key: "year", numericValue: 1934 }
    ]
  }
});
```

Isso é útil quando você tem vários documentos em um repositório da Pesquisa de arquivos e quer pesquisar apenas um subconjunto deles.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me about the book 'I, Claudius'",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name],
        "metadata_filter": 'author="Robert Graves"',
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: "Tell me about the book 'I, Claudius'",
  tools: [{
    type: "file_search",
    file_search_store_names: [fileSearchStore.name],
    metadata_filter: 'author="Robert Graves"',
  }]
});

for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
      }
    }
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -X POST \
    -d '{
            "model": "gemini-3.5-flash",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

As orientações sobre a implementação da sintaxe de filtro de lista para `metadata_filter` podem ser encontradas em [google.aip.dev/160](https://google.aip.dev/160).

## Pesquisa de arquivos multimodal

Com a pesquisa de arquivos multimodal, é possível incorporar e pesquisar imagens de forma nativa, o que permite aplicativos de RAG multimodais e avançados.

### Configurar o modelo de embedding

Ao criar um `FileSearchStore`, é necessário substituir o modelo de embedding padrão somente de texto para usar um modelo multimodal. Use `models/gemini-embedding-2` para
processar textos e imagens.

### Python

```
store = client.file_search_stores.create(
    config={
        "display_name": "Multimodal Catalog",
        "embedding_model": "models/gemini-embedding-2",
    }
)
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: "Multimodal Catalog",
    embeddingModel: "models/gemini-embedding-2",
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "display_name": "Multimodal Catalog",
      "embedding_model": "models/gemini-embedding-2"
    }'
```

### Fazer upload de imagens

Depois de criar o repositório com um modelo de incorporação multimodal, você pode fazer upload de arquivos de imagem diretamente usando as mesmas APIs de upload descritas em [Fazer upload diretamente para o repositório da Pesquisa de arquivos](#upload) ou [Importar arquivos](#importing-files).

**Requisitos de arquivo de imagem:**

- Os arquivos de imagem precisam ter resolução de até 4K x 4K pixels.
- Os formatos aceitos são PNG e JPEG.

## Citações

Ao usar a Pesquisa de arquivos, a resposta do modelo pode incluir citações que especificam quais partes dos documentos enviados foram usadas para gerar a resposta. Isso ajuda na checagem de fatos e na verificação.

Você pode acessar as informações de citação pelo atributo `annotations` nos blocos `content` da etapa `model_output` da resposta.

### Python

```
for step in interaction.steps:
    if step.type == 'model_output':
        for content in step.content:
            if content.type == 'text' and content.annotations:
                print(content.annotations)
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text' && contentBlock.annotations) {
        console.log(JSON.stringify(contentBlock.annotations, null, 2));
      }
    }
  }
}
```

Para informações detalhadas sobre a estrutura das citações, consulte a
[referência da API Interactions](https://ai.google.dev/api/interactions-api?hl=pt-br#Resource:FileCitation).

### Números de página

Quando você usa a Pesquisa de arquivos com documentos que têm páginas (como PDFs), a resposta do modelo pode incluir o número da página em que as informações foram encontradas.
É possível acessar essas informações usando o atributo `page_number` de uma anotação `file_citation`.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.page_number:
                        print(f"Cited Page: {annotation.page_number}")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.pageNumber) {
            console.log(`Cited Page: ${annotation.pageNumber}`);
          }
        }
      }
    }
  }
}
```

### Citações de mídia

Quando o modelo faz referência a um trecho de imagem durante a geração, a API retorna uma anotação do tipo `file_citation` nas anotações que incluem um `media_id`. Use esse ID para baixar o trecho de imagem exato a que o modelo fez referência. Esse `media_id` é persistente em várias chamadas de pesquisa, o que permite recuperar de forma confiável a mesma imagem ou armazená-la em cache usando o ID.

O snippet a seguir é um exemplo de etapa de resposta REST:

```
{
  "type": "model_output",
  "content": [
    {
      "type": "text",
      "text": "...",
      "annotations": [
        {
          "type": "file_citation",
          "file_name": "product_image",
          "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
        }
      ]
    }
  ]
}
```

Os snippets de código a seguir demonstram como recuperar o `media_id` e
baixar a mídia:

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.media_id:
                        print(f"Cited Media ID: {annotation.media_id}")
                        blob_content = client.file_search_stores.download_media(
                            media_id=annotation.media_id
                        )
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.mediaId) {
            console.log(`Cited Media ID: ${annotation.mediaId}`);
            const blobContent = await ai.fileSearchStores.downloadMedia(annotation.mediaId);
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Metadados personalizados

Se você adicionou metadados personalizados aos seus arquivos, é possível acessá-los nas anotações da resposta do modelo. Isso é útil para transmitir contexto adicional (como URLs, números de página ou autores) dos documentos de origem para a lógica do aplicativo. Cada anotação de citação do tipo `file_citation`
contém esses metadados personalizados.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.annotations:
                for annotation in content_block.annotations:
                    print(annotation)
```

### JavaScript

```
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.annotations) {
          contentBlock.annotations.forEach((annotation) => {
            console.log(annotation);
          });
        }
      }
    }
  }
```

### REST

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "...",
          "annotations": [
            {
              "file_name": "...",
              "source": "...",
              "custom_metadata": [
                {
                  "key": "author",
                  "string_value": "Robert Graves"
                },
                {
                  "key": "year",
                  "numeric_value": 1934
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## Resposta estruturada

A partir dos modelos do Gemini 3, é possível combinar a ferramenta de pesquisa de arquivos com [saídas estruturadas](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pt-br).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the minimum hourly wage in Tokyo right now?",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Money.model_json_schema()
    },
)
result = Money.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { z } from "zod";

const moneyJsonSchema = {
  type: "object",
  properties: {
    amount: { type: "string", description: "The numerical part of the amount." },
    currency: { type: "string", description: "The currency of amount." }
  },
  required: ["amount", "currency"]
};

const moneySchema = z.fromJSONSchema(moneyJsonSchema);

async function run() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the minimum hourly wage in Tokyo right now?",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name],
    }],
    response_format: {
      type: 'text',
      mime_type: 'application/json',
      schema: moneyJsonSchema
    },
  });

  const result = moneySchema.parse(JSON.parse(interaction.output_text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the minimum hourly wage in Tokyo right now?",
    "tools": [{
      "type": "file_search",
      "file_search_store_names": ["$FILE_SEARCH_STORE_NAME"]
    }],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "amount": {"type": "string", "description": "The numerical part of the amount."},
          "currency": {"type": "string", "description": "The currency of amount."}
        },
        "required": ["amount", "currency"]
      }
    }
  }'
```

## Modelos compatíveis

Os seguintes modelos são compatíveis com a Pesquisa de arquivos:

| Modelo | Pesquisa de arquivos |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pt-br) | ✔️ |

## Combinações de ferramentas compatíveis

Os modelos do Gemini 3 permitem combinar ferramentas integradas (como a Pesquisa de arquivos) com ferramentas personalizadas (chamada de função). Saiba mais na página de
[combinações de ferramentas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).

## Tipos de arquivo compatíveis

A Pesquisa de arquivos é compatível com vários formatos de arquivo, listados nas seções a seguir.

### Tipos de arquivo de aplicativo

- `application/dart`
- `application/ecmascript`
- `application/json`
- `application/ms-java`
- `application/msword`
- `application/pdf`
- `application/sql`
- `application/typescript`
- `application/vnd.curl`
- `application/vnd.dart`
- `application/vnd.ibm.secure-container`
- `application/vnd.jupyter`
- `application/vnd.ms-excel`
- `application/vnd.oasis.opendocument.text`
- `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.template`
- `application/x-csh`
- `application/x-hwp`
- `application/x-hwp-v5`
- `application/x-latex`
- `application/x-php`
- `application/x-powershell`
- `application/x-sh`
- `application/x-shellscript`
- `application/x-tex`
- `application/x-zsh`
- `application/xml`
- `application/zip`

### Tipos de arquivos de texto

- `text/1d-interleaved-parityfec`
- `text/RED`
- `text/SGML`
- `text/cache-manifest`
- `text/calendar`
- `text/cql`
- `text/cql-extension`
- `text/cql-identifier`
- `text/css`
- `text/csv`
- `text/csv-schema`
- `text/dns`
- `text/encaprtp`
- `text/enriched`
- `text/example`
- `text/fhirpath`
- `text/flexfec`
- `text/fwdred`
- `text/gff3`
- `text/grammar-ref-list`
- `text/hl7v2`
- `text/html`
- `text/javascript`
- `text/jcr-cnd`
- `text/jsx`
- `text/markdown`
- `text/mizar`
- `text/n3`
- `text/parameters`
- `text/parityfec`
- `text/php`
- `text/plain`
- `text/provenance-notation`
- `text/prs.fallenstein.rst`
- `text/prs.lines.tag`
- `text/prs.prop.logic`
- `text/raptorfec`
- `text/rfc822-headers`
- `text/rtf`
- `text/rtp-enc-aescm128`
- `text/rtploopback`
- `text/rtx`
- `text/sgml`
- `text/shaclc`
- `text/shex`
- `text/spdx`
- `text/strings`
- `text/t140`
- `text/tab-separated-values`
- `text/texmacs`
- `text/troff`
- `text/tsv`
- `text/tsx`
- `text/turtle`
- `text/ulpfec`
- `text/uri-list`
- `text/vcard`
- `text/vnd.DMClientScript`
- `text/vnd.IPTC.NITF`
- `text/vnd.IPTC.NewsML`
- `text/vnd.a`
- `text/vnd.abc`
- `text/vnd.ascii-art`
- `text/vnd.curl`
- `text/vnd.debian.copyright`
- `text/vnd.dvb.subtitle`
- `text/vnd.esmertec.theme-descriptor`
- `text/vnd.exchangeable`
- `text/vnd.familysearch.gedcom`
- `text/vnd.ficlab.flt`
- `text/vnd.fly`
- `text/vnd.fmi.flexstor`
- `text/vnd.gml`
- `text/vnd.graphviz`
- `text/vnd.hans`
- `text/vnd.hgl`
- `text/vnd.in3d.3dml`
- `text/vnd.in3d.spot`
- `text/vnd.latex-z`
- `text/vnd.motorola.reflex`
- `text/vnd.ms-mediapackage`
- `text/vnd.net2phone.commcenter.command`
- `text/vnd.radisys.msml-basic-layout`
- `text/vnd.senx.warpscript`
- `text/vnd.sosi`
- `text/vnd.sun.j2me.app-descriptor`
- `text/vnd.trolltech.linguist`
- `text/vnd.wap.si`
- `text/vnd.wap.sl`
- `text/vnd.wap.wml`
- `text/vnd.wap.wmlscript`
- `text/vtt`
- `text/wgsl`
- `text/x-asm`
- `text/x-bibtex`
- `text/x-boo`
- `text/x-c`
- `text/x-c++hdr`
- `text/x-c++src`
- `text/x-cassandra`
- `text/x-chdr`
- `text/x-coffeescript`
- `text/x-component`
- `text/x-csh`
- `text/x-csharp`
- `text/x-csrc`
- `text/x-cuda`
- `text/x-d`
- `text/x-diff`
- `text/x-dsrc`
- `text/x-emacs-lisp`
- `text/x-erlang`
- `text/x-gff3`
- `text/x-go`
- `text/x-haskell`
- `text/x-java`
- `text/x-java-properties`
- `text/x-java-source`
- `text/x-kotlin`
- `text/x-lilypond`
- `text/x-lisp`
- `text/x-literate-haskell`
- `text/x-lua`
- `text/x-moc`
- `text/x-objcsrc`
- `text/x-pascal`
- `text/x-pcs-gcd`
- `text/x-perl`
- `text/x-perl-script`
- `text/x-python`
- `text/x-python-script`
- `text/x-r-markdown`
- `text/x-rsrc`
- `text/x-rst`
- `text/x-ruby-script`
- `text/x-rust`
- `text/x-sass`
- `text/x-scala`
- `text/x-scheme`
- `text/x-script.python`
- `text/x-scss`
- `text/x-setext`
- `text/x-sfv`
- `text/x-sh`
- `text/x-siesta`
- `text/x-sos`
- `text/x-sql`
- `text/x-swift`
- `text/x-tcl`
- `text/x-tex`
- `text/x-vbasic`
- `text/x-vcalendar`
- `text/xml`
- `text/xml-dtd`
- `text/xml-external-parsed-entity`
- `text/yaml`

## Limitações

- **API Live**:a Pesquisa de arquivos não é compatível com a [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br).
- **Incompatibilidade de ferramentas**:no momento, a Pesquisa de arquivos não pode ser combinada com outras ferramentas, como [Embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br), [Contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br) etc.

### Limites de taxas

A API File Search tem os seguintes limites para garantir a estabilidade do serviço:

- **Tamanho máximo do arquivo / limite por documento**: 100 MB
- **Tamanho total dos armazenamentos da Pesquisa de arquivos do projeto** (com base no nível do usuário):
  - **Sem custo financeiro**: 1 GB
  - **Nível 1**: 10 GB
  - **Nível 2**: 100 GB
  - **Nível 3**: 1 TB
- **Recomendação**: limite o tamanho de cada repositório de pesquisa de arquivos para menos de 20 GB e garanta latências de recuperação ideais.

## Preços

- Você recebe uma cobrança por incorporações no momento da indexação com base nos [preços de incorporação](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-embedding-2) atuais.
- O armazenamento não tem custo financeiro.
- Os embeddings de tempo de consulta não têm custo financeiro.
- Os tokens de documentos recuperados são cobrados como [tokens de contexto](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=pt-br) normais.

## A seguir

- Acesse a referência da API para [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br) e [Documents](https://ai.google.dev/api/file-search/documents?hl=pt-br) da Pesquisa de arquivos.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-05 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-05 UTC."],[],[]]
