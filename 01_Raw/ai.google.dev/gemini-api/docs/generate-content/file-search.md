---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-search?hl=es-419
fetched_at: 2026-11-02T07:05:08.968601+00:00
title: "B\u00fasqueda de archivos \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

Enviar comentarios

# Búsqueda de archivos

La API de Gemini habilita la generación mejorada por recuperación ("RAG") a través de la herramienta de búsqueda de archivos. La Búsqueda de archivos importa, divide en fragmentos y crea un índice de tus datos para permitir la recuperación rápida de información pertinente según una instrucción proporcionada. Luego, esta información recuperada se usa como contexto para el modelo, lo que le permite proporcionar respuestas más precisas y pertinentes. La búsqueda de archivos también puede proporcionar capacidades multimodales con embedding de texto compatibles con `gemini-embedding-001` y con incorporaciones de imágenes o multimodales compatibles con `gemini-embedding-2`.

El almacenamiento de archivos y la generación de embeddings en el momento de la consulta son gratuitos, y solo pagarás
por crear embeddings cuando indexes tus archivos por primera vez y por el costo normal de los tokens de entrada y salida del modelo de
Gemini. Este nuevo paradigma de facturación hace que la herramienta de búsqueda de archivos sea más fácil y rentable de compilar y escalar. Consulta
la sección [Precios](#pricing) para obtener más información.

## Sube directamente al almacén de File Search

En este ejemplo, se muestra cómo subir un archivo directamente al [almacén de búsqueda de archivos](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#method:-media.uploadtofilesearchstore):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
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

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
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

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Can you tell me about [insert question]",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [fileSearchStore.name]
          }
        }
      ]
    }
  });

  console.log(response.text);
}

run();
```

Consulta la referencia de la API de [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#method:-media.uploadtofilesearchstore) para obtener más información.

## Importación de archivos

También puedes subir un archivo existente y [importarlo a tu tienda de búsqueda de archivos](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#method:-filesearchstores.importfile):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'name': 'display_file_name'})

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

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { name: 'file-name' }
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

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Can you tell me about [insert question]",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [fileSearchStore.name]
          }
        }
      ]
    }
  });

  console.log(response.text);
}

run();
```

Consulta la referencia de la API de [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#method:-filesearchstores.importfile) para obtener más información.

## Configuración de fragmentación

Cuando importas un archivo a un almacén de File Search, se divide automáticamente
en fragmentos, se incorpora, se indexa y se sube a tu almacén de File Search. Si
necesitas más control sobre la estrategia de fragmentación, puedes especificar un
parámetro de configuración [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#request-body_5)
para establecer una cantidad máxima de tokens por fragmento y una cantidad máxima de tokens
superpuestos.

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
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

Para usar tu almacén de File Search, pásalo como una herramienta al método `generateContent`, como se muestra en los ejemplos de [carga](#upload) y de [importación](#importing-files).

## Cómo funciona

La Búsqueda de archivos usa una técnica llamada búsqueda semántica para encontrar información pertinente para la instrucción del usuario. A diferencia de la búsqueda estándar basada en palabras clave, la búsqueda semántica
comprende el significado y el contexto de tu consulta.

Cuando importas un archivo, se convierte en representaciones numéricas llamadas
[embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419), que capturan el significado semántico del
contenido subido. Estos embeddings se almacenan en una base de datos especializada de File Search.
Cuando realizas una consulta, esta también se convierte en un embedding. Luego, el sistema realiza una búsqueda de archivos para encontrar los fragmentos de documentos más similares y relevantes del almacén de búsqueda de archivos.

No hay un tiempo de actividad (TTL) para los embeddings;
persisten hasta que se borran de forma manual o cuando el modelo deja de estar disponible. Sin embargo, los archivos se borran después de 48 horas.

A continuación, se detalla el proceso para usar la API de File Search `uploadToFileSearchStore`:

1. **Crea un almacén de File Search**: Un almacén de File Search contiene los datos procesados de tus archivos. Es el contenedor persistente para los embeddings en los que operará
   la búsqueda semántica.
2. **Sube un archivo y, luego, impórtalo a un almacén de File Search**: Sube un archivo
   y, al mismo tiempo, importa los resultados a tu almacén de File Search. Esto crea un objeto `File` temporal, que es una referencia a tu documento sin procesar. Luego, esos datos se dividen en fragmentos, se convierten en embeddings de la Búsqueda de archivos y se indexan. El objeto `File` se borra después de 48 horas, mientras que los datos importados en el almacén de la Búsqueda de archivos se almacenarán de forma indefinida hasta que decidas borrarlos.
3. **Realiza consultas con File Search**: Por último, usa la herramienta `FileSearch` en una llamada a `generateContent`. En la configuración de la herramienta, especificas un
   `FileSearchRetrievalResource`, que apunta al `FileSearchStore` que deseas
   buscar. Esto le indica al modelo que realice una búsqueda semántica en ese almacén específico de File Search para encontrar información pertinente que fundamente su respuesta.

![El proceso de indexación y consulta de File Search](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=es-419)

El proceso de indexación y consulta de la Búsqueda de archivos

En este diagrama, la línea punteada de *Documentos* a *Modelo de incorporación*
(con [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419))
representa la API de `uploadToFileSearchStore` (omitiendo el *Almacenamiento de archivos*).
De lo contrario, usar la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419) para crear
y, luego, importar archivos por separado mueve el proceso de indexación de *Documentos* a
*Almacenamiento de archivos* y, luego, al *Modelo de incorporación*.

## Almacenes de búsqueda de archivos

Un almacén de búsqueda de archivos es un contenedor para tus embeddings de documentos. Si bien los archivos sin procesar
subidos a través de la API de File se borran después de 48 horas, los datos importados a
un almacén de File Search se almacenan de forma indefinida hasta que los borres manualmente. Puedes
crear varios almacenes de File Search para organizar tus documentos. La
API de `FileSearchStore` te permite crear, enumerar, obtener y borrar para administrar tus almacenes de búsqueda de
archivos. Los nombres de la tienda de la Búsqueda de archivos tienen un alcance global.

Estos son algunos ejemplos de cómo administrar tus tiendas de Búsqueda de archivos:

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

## Documentos de File Search

Puedes administrar documentos individuales en tus almacenes de archivos con la API de [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=es-419) para `list` cada documento en un almacén de búsqueda de archivos, `get` información sobre un documento y `delete` un documento por nombre.

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
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
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc',
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"
```

## Metadatos de archivos

Puedes agregar metadatos personalizados a tus archivos para filtrarlos o proporcionar contexto adicional. Los metadatos son un conjunto de pares clave-valor.

### Python

```
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    custom_metadata=[
        {"key": "author", "string_value": "Robert Graves"},
        {"key": "year", "numeric_value": 1934}
    ]
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

Esto es útil cuando tienes varios documentos en un almacén de File Search y quieres
buscar solo un subconjunto de ellos.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Tell me about the book 'I, Claudius'",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name],
                    metadata_filter="author=Robert Graves",
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Tell me about the book 'I, Claudius'",
  config: {
    tools: [
      {
        fileSearch: {
          fileSearchStoreNames: [fileSearchStore.name],
          metadataFilter: 'author="Robert Graves"',
        }
      }
    ]
  }
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=${GEMINI_API_KEY}" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
            "contents": [{
                "parts":[{"text": "Tell me about the book I, Claudius"}]
            }],
            "tools": [{
                "file_search": {
                    "file_search_store_names":["'$STORE_NAME'"],
                    "metadata_filter": "author = \"Robert Graves\""
                }
            }]
        }' 2> /dev/null > response.json

cat response.json
```

Puedes encontrar orientación sobre cómo implementar la sintaxis de filtro de listas para `metadata_filter`
en [google.aip.dev/160](https://google.aip.dev/160)

## Búsqueda de archivos multimodal

La búsqueda de archivos multimodal te permite incorporar imágenes y realizar búsquedas en ellas de forma nativa,
lo que habilita aplicaciones de RAG multimodales y enriquecidas.

### Configura el modelo de embedding

Cuando creas un `FileSearchStore`, debes anular el modelo de incorporación predeterminado solo de texto para usar un modelo multimodal. Usa `models/gemini-embedding-2` para
procesar texto e imágenes.

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

### Sube imágenes

Después de crear el almacén con un modelo de embeddings multimodal, puedes subir
archivos de imagen directamente con las mismas APIs de carga que se describen en
[Sube directamente al almacén de File Search](#upload) o [Importa archivos](#importing-files).

**Requisitos de los archivos de imagen:**

- Los archivos de imagen deben tener una resolución máxima de 4K x 4K píxeles.
- Los formatos admitidos son PNG y JPEG.

## Citas

Cuando usas la Búsqueda de archivos, la respuesta del modelo puede incluir citas que especifican qué partes de los documentos que subiste se usaron para generar la respuesta. Esto ayuda con la verificación de datos.

Puedes acceder a la información de citas a través del atributo `grounding_metadata`
de la respuesta.

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

Para obtener información detallada sobre la estructura de los metadatos de fundamentación, consulta los ejemplos en el [recetario de File Search](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb) o [la sección de fundamentación de la documentación de Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419#attributing_sources_with_inline_citations).

### Números de página

Cuando usas la Búsqueda de archivos con documentos que tienen páginas (como archivos PDF), la
respuesta del modelo puede incluir el número de página en el que se encontró la información.
Puedes acceder a esta información a través del atributo `page_number` de `retrieved_context`.

### Python

```
# Iterate through citations and check for page numbers
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.page_number:
       print(f"Cited Page: {chunk.retrieved_context.page_number}")
```

### JavaScript

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.pageNumber) {
    console.log(`Cited Page: ${chunk.retrievedContext.pageNumber}`);
  }
}
```

### Citas de medios

Cuando el modelo hace referencia a un fragmento de imagen durante la generación, la API devuelve una
cita en los metadatos de fundamentación que incluye un `media_id`. Puedes usar este ID para descargar el fragmento de imagen exacto al que hizo referencia el modelo. Este `media_id` es
persistente en varias llamadas de búsqueda, lo que te permite recuperar de forma confiable
la misma imagen o almacenarla en caché con el ID.

El siguiente fragmento es un ejemplo de respuesta de REST:

```
"groundingMetadata": {
  "groundingChunks": [
    {
      "retrievedContext": {
        "title": "product_image",
        "fileSearchStore": "fileSearchStores/my-store-123",
        "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
      }
    }
  ]
}
```

En los siguientes fragmentos de código, se muestra cómo recuperar el objeto `media_id` y descargar el contenido multimedia:

### Python

```
# Iterate through citations and download media if present
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.media_id:
       print(f"Cited Media ID: {chunk.retrieved_context.media_id}")
       # Download the blob using the SDK
       blob_content = client.file_search_stores.download_media(
           media_id=chunk.retrieved_context.media_id
       )
       # Save blob_content to file...
```

### JavaScript

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.mediaId) {
    console.log(`Cited Media ID: ${chunk.retrievedContext.mediaId}`);
    const blobContent = await ai.fileSearchStores.downloadMedia(chunk.retrievedContext.mediaId);
    // Save blobContent to file...
  }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Metadatos personalizados en los datos de fundamentación

Si agregaste metadatos personalizados a tus archivos, puedes acceder a ellos en los
metadatos de fundamentación de la respuesta del modelo. Esto es útil para pasar
contexto adicional (como URLs, números de página o autores) de tus documentos de origen
a la lógica de tu aplicación. Cada `grounding_chunk` en el
`retrieved_context` contiene estos metadatos personalizados.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Tell me about [insert question]",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

for chunk in response.candidates[0].grounding_metadata.grounding_chunks:
    if chunk.retrieved_context:
        print(f"Text: {chunk.retrieved_context.text}")
        if chunk.retrieved_context.custom_metadata:
            for metadata in chunk.retrieved_context.custom_metadata:
                print(f"Metadata Key: {metadata.key}")
                print(f"Value: {metadata.string_value or metadata.numeric_value}")
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Tell me about [insert question]",
  config: {
    tools: [
      {
        fileSearch: {
          fileSearchStoreNames: [fileSearchStore.name]
        }
      }
    ]
  }
});

const groundingMetadata = response.candidates[0].groundingMetadata;
groundingMetadata.groundingChunks.forEach((chunk) => {
  if (chunk.retrievedContext) {
    console.log(`Text: ${chunk.retrievedContext.text}`);
    if (chunk.retrievedContext.customMetadata) {
      chunk.retrievedContext.customMetadata.forEach((metadata) => {
        console.log(`Metadata Key: ${metadata.key}`);
        console.log(`Value: ${metadata.stringValue || metadata.numericValue}`);
      });
    }
  }
});
```

### REST

```
{
  "candidates": [
    {
      "content": { ... },
      "grounding_metadata": {
        "grounding_chunks": [
          {
            "retrieved_context": {
              "text": "...",
              "title": "...",
              "uri": "...",
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
          }
        ],
        "grounding_supports": [ ... ]
      }
    }
  ]
}
```

## Resultados estructurados

A partir de los modelos de Gemini 3, puedes combinar la herramienta de búsqueda de archivos con
[resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is the minimum hourly wage in Tokyo right now?",
    config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[file_search_store.name]
                        )
                    )
                ],
                response_mime_type="application/json",
                response_json_schema=Money.model_json_schema()
      )
)
result = Money.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { z } from "zod";

const moneySchema = z.object({
  amount: z.string().describe("The numerical part of the amount."),
  currency: z.string().describe("The currency of amount."),
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the minimum hourly wage in Tokyo right now?",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [file_search_store.name],
          },
        },
      ],
      responseMimeType: "application/json",
      responseJsonSchema: z.toJSONSchema(moneySchema),
    },
  });

  const result = moneySchema.parse(JSON.parse(response.text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "What is the minimum hourly wage in Tokyo right now?"}]
    }],
    "tools": [
      {
        "fileSearch": {
          "fileSearchStoreNames": ["$FILE_SEARCH_STORE_NAME"]
        }
      }
    ],
    "generationConfig": {
      "responseFormat": {
        "text": {
          "mimeType": "APPLICATION_JSON",
          "schema": {
            "type": "object",
            "properties": {
              "amount": {"type": "string", "description": "The numerical part of the amount."},
              "currency": {"type": "string", "description": "The currency of amount."}
            },
            "required": ["amount", "currency"]
          }
        }
      }
    }
  }'
```

## Modelos compatibles

Los siguientes modelos admiten la Búsqueda de archivos:

| Modelo | Búsqueda de archivos |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=es-419) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=es-419) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=es-419) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=es-419) | ✔️ |

## Combinaciones de herramientas compatibles

Los modelos Gemini 4 y Gemini 3 admiten la combinación de herramientas integradas (como la búsqueda de archivos) con herramientas personalizadas (llamada a funciones). Obtén más información en la página
[Combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

## Tipos de archivos admitidos

La Búsqueda de archivos admite una amplia variedad de formatos de archivo, que se indican en las siguientes secciones.

### Tipos de archivos de la aplicación

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

### Tipos de archivos de texto

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

## Limitaciones

- **API en vivo:** La búsqueda de archivos no es compatible con la [API en vivo](https://ai.google.dev/gemini-api/docs/live?hl=es-419).
- **Incompatibilidad de herramientas:** Por el momento, la búsqueda de archivos no se puede combinar con otras herramientas, como la [Fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419), el [contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419), etcétera.

### Límites de frecuencia

La API de File Search tiene los siguientes límites para garantizar la estabilidad del servicio:

- **Tamaño máximo de archivo / límite por documento**: 100 MB
- **Tamaño total de los almacenes de File Search del proyecto** (según el nivel del usuario):
  - **Gratis**: 1 GB
  - **Nivel 1**: 10 GB
  - **Nivel 2**: 100 GB
  - **Nivel 3**: 1 TB
- **Recomendación**: Limita el tamaño de cada almacén de File Search a menos de 20 GB para garantizar latencias de recuperación óptimas.

## Precios

- Se te cobrarán las incorporaciones en el momento de la indexación según los [precios de las incorporaciones](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#gemini-embedding-2) existentes.
- El almacenamiento no tiene costo.
- Los embeddings de tiempo de consulta no tienen costo.
- Los tokens de documentos recuperados se cobran como [tokens de contexto](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) normales.

## ¿Qué sigue?

- Visita la referencia de la API para [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419) y File Search [Documents](https://ai.google.dev/api/file-search/documents?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-19 (UTC)"],[],[]]
