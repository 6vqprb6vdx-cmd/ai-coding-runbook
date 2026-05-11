---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=pl
fetched_at: 2026-05-11T12:39:26.206967+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wyszukiwanie plików

Interfejs Gemini API umożliwia generowanie wspomagane wyszukiwaniem („RAG”) za pomocą narzędzia wyszukiwania plików. Wyszukiwarka plików importuje, dzieli na części i indeksuje dane, aby umożliwić szybkie wyszukiwanie odpowiednich informacji na podstawie podanego promptu. Te informacje są następnie wykorzystywane jako kontekst dla modelu, co pozwala mu udzielać dokładniejszych i trafniejszych odpowiedzi.

Aby wyszukiwanie plików było proste i przystępne cenowo dla deweloperów, udostępniamy bezpłatnie przechowywanie plików i generowanie osadzeń w momencie wysyłania zapytania. Płacisz tylko za tworzenie wektorów, gdy po raz pierwszy indeksujesz pliki (według obowiązującej ceny modelu wektorów) oraz za normalne tokeny wejściowe i wyjściowe modelu Gemini. Ten nowy model rozliczeń sprawia, że narzędzie do wyszukiwania plików jest łatwiejsze i bardziej opłacalne w budowie oraz skalowaniu.

## Bezpośrednie przesyłanie do sklepu wyszukiwarki plików

Ten przykład pokazuje, jak bezpośrednio przesłać plik do [sklepu z wyszukiwarką plików](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#method:-media.uploadtofilesearchstore):

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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
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

Więcej informacji znajdziesz w dokumentacji interfejsu API [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#method:-media.uploadtofilesearchstore).

## Importowanie plików

Możesz też przesłać istniejący plik i [zaimportować go do magazynu wyszukiwania plików](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#method:-filesearchstores.importfile):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
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
    model="gemini-3-flash-preview",
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
  // File name will be visible in citations
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
    model: "gemini-3-flash-preview",
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

Więcej informacji znajdziesz w dokumentacji interfejsu API [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#method:-filesearchstores.importfile).

## Konfiguracja dzielenia na części

Gdy zaimportujesz plik do sklepu File Search, zostanie on automatycznie podzielony na części, osadzony, zindeksowany i przesłany do sklepu File Search. Jeśli potrzebujesz większej kontroli nad strategią dzielenia na części, możesz określić ustawienie [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#request-body_5), aby ustawić maksymalną liczbę tokenów w części i maksymalną liczbę nakładających się tokenów.

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

Aby użyć sklepu File Search, przekaż go jako narzędzie do metody `interactions.create`, jak pokazano w przykładach [przesyłania](#upload) i [importowania](#importing-files).

## Jak to działa

Wyszukiwanie plików korzysta z techniki zwanej wyszukiwaniem semantycznym, aby znajdować informacje istotne dla promptu użytkownika. W przeciwieństwie do standardowego wyszukiwania opartego na słowach kluczowych wyszukiwanie semantyczne rozumie znaczenie i kontekst Twojego zapytania.

Podczas importowania pliku jest on przekształcany w reprezentacje numeryczne zwane [wektorami dystrybucyjnymi](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl), które odzwierciedlają znaczenie semantyczne tekstu. Te wektory są przechowywane w specjalistycznej bazie danych wyszukiwania plików.
Gdy wysyłasz zapytanie, jest ono również przekształcane w wektor. Następnie system przeprowadza wyszukiwanie plików, aby znaleźć najbardziej podobne i trafne fragmenty dokumentów w magazynie wyszukiwania plików.

Osadzenia i pliki nie mają czasu życia (TTL).
Są przechowywane do momentu ręcznego usunięcia lub wycofania modelu.

Oto opis procesu korzystania z interfejsu File Search
`uploadToFileSearchStore` API:

1. **Utwórz sklep wyszukiwania plików:** sklep wyszukiwania plików zawiera przetworzone dane z Twoich plików. Jest to trwały kontener na wektory dystrybucyjne, na których będzie działać wyszukiwanie semantyczne.
2. **Prześlij plik i zaimportuj go do sklepu wyszukiwania plików:** jednocześnie prześlij plik i zaimportuj wyniki do sklepu wyszukiwania plików. Spowoduje to utworzenie tymczasowego obiektu `File`, który jest odwołaniem do Twojego dokumentu w formacie nieprzetworzonym. Dane są następnie dzielone na części, konwertowane na wektory dystrybucyjne wyszukiwania plików i indeksowane. `File`Obiekt zostanie usunięty po 48 godzinach, a dane zaimportowane do magazynu wyszukiwania plików będą przechowywane bezterminowo, dopóki nie zdecydujesz się ich usunąć.
3. **Zapytanie za pomocą wyszukiwania plików:** na koniec używasz narzędzia `FileSearch` w wywołaniu `generateContent`. W konfiguracji narzędzia określasz `FileSearchRetrievalResource`, który wskazuje `FileSearchStore`, którego chcesz wyszukać. Dzięki temu model przeprowadzi wyszukiwanie semantyczne w tym konkretnym sklepie wyszukiwania plików, aby znaleźć odpowiednie informacje, na których będzie opierać swoją odpowiedź.

![Proces indeksowania i wyszukiwania w wyszukiwarce plików](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=pl)

Proces indeksowania i przesyłania zapytań w wyszukiwarce plików

Na tym diagramie linia przerywana od *Dokumentów* do *Modelu osadzania* (z użyciem [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl)) reprezentuje interfejs API `uploadToFileSearchStore` (z pominięciem *Pamięci plików*).
W przeciwnym razie użycie [interfejsu Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=pl) do oddzielnego tworzenia, a następnie importowania plików przenosi proces indeksowania z *Dokumentów* do *pamięci plików*, a potem do *modelu osadzania*.

## Sklepy wyszukiwania plików

Magazyn wyszukiwania plików to kontener na osadzenia dokumentów. Surowe pliki przesłane za pomocą interfejsu File API są usuwane po 48 godzinach, ale dane zaimportowane do sklepu wyszukiwania plików są przechowywane bezterminowo, dopóki nie usuniesz ich ręcznie. Możesz utworzyć kilka sklepów wyszukiwania plików, aby uporządkować dokumenty. Interfejs API `FileSearchStore` umożliwia tworzenie, wyświetlanie, pobieranie i usuwanie sklepów z wyszukiwarką plików. Nazwy sklepów w wyszukiwarce plików mają zasięg globalny.

Oto kilka przykładów zarządzania sklepami w wyszukiwarce plików:

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

## Dokumenty wyszukiwania plików

Poszczególnymi dokumentami w magazynach plików możesz zarządzać za pomocą interfejsu [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=pl) API, aby `list` każdy dokument w magazynie wyszukiwania plików, `get` informacje o dokumencie i `delete` dokument według nazwy.

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

## Metadane pliku

Możesz dodać do plików niestandardowe metadane, aby ułatwić ich filtrowanie lub zapewnić dodatkowy kontekst. Metadane to zbiór par klucz-wartość.

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

Jest to przydatne, gdy w magazynie wyszukiwania plików masz wiele dokumentów i chcesz przeszukiwać tylko ich podzbiór.

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
  model: "gemini-3-flash-preview",
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
    -X POST \
    -d '{
            "model": "gemini-3-flash-preview",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

Wskazówki dotyczące wdrażania składni filtra listy dla `metadata_filter` znajdziesz na stronie [google.aip.dev/160](https://google.aip.dev/160)

## Cytaty

Gdy używasz wyszukiwania plików, odpowiedź modelu może zawierać cytaty, które wskazują, które części przesłanych dokumentów zostały użyte do wygenerowania odpowiedzi. Ułatwia to weryfikację informacji.

Informacje o cytowaniu są dostępne w polu `annotations` w blokach treści na `model_output` etapie.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.annotations:
                print(content_block.annotations)
```

### JavaScript

```
for (const step of interaction.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.annotations) {
                console.log(contentBlock.annotations);
            }
        }
    }
}
```

Szczegółowe informacje o strukturze metadanych podstawowych znajdziesz w przykładach w [przewodniku po wyszukiwaniu plików](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb) lub w [sekcji dotyczącej podstaw w dokumentacji Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=pl#attributing_sources_with_inline_citations).

## Niestandardowe metadane w danych groundingu

Jeśli do plików dodano metadane niestandardowe, możesz uzyskać do nich dostęp w metadanych uzasadniających odpowiedź modelu. Jest to przydatne do przekazywania dodatkowego kontekstu (np. adresów URL, numerów stron lub autorów) z dokumentów źródłowych do logiki aplikacji. Każdy element `grounding_chunk` w `retrieved_context` zawiera te niestandardowe metadane.

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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

## Uporządkowane dane wyjściowe

W przypadku modeli Gemini 3 możesz połączyć narzędzie do wyszukiwania plików z [danymi strukturalnymi](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pl).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
result = Money.model_validate_json(interaction.steps[-1].content[0].text)
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
    model: "gemini-3-flash-preview",
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

  const result = moneySchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3-flash-preview",
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

## Obsługiwane modele

Wyszukiwanie plików jest obsługiwane przez te modele:

| Model | Wyszukiwanie plików |
| --- | --- |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite (wersja testowa)](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Obsługiwane kombinacje narzędzi

Modele Gemini 3 obsługują łączenie wbudowanych narzędzi (takich jak wyszukiwanie plików) z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na stronie [kombinacje narzędzi](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pl).

## Obsługiwane typy plików

Wyszukiwanie plików obsługuje szeroką gamę formatów plików, które są wymienione w kolejnych sekcjach.

### Typy plików aplikacji

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

### Typy plików tekstowych

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

## Ograniczenia

- **Interfejs Live API:** wyszukiwanie plików nie jest obsługiwane w [interfejsie Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).
- **Niezgodność narzędzi:** wyszukiwania plików nie można obecnie łączyć z innymi narzędziami, takimi jak [powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pl) czy [kontekst adresu URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pl).

### Ograniczenia liczby żądań

Aby zapewnić stabilność usługi, interfejs API wyszukiwania plików ma te limity:

- **Maksymalny rozmiar pliku / limit na dokument:** 100 MB
- **Całkowity rozmiar pamięci wyszukiwania plików w projekcie** (zależny od poziomu użytkownika):
  - **Bezpłatnie:** 1 GB
  - **Poziom 1:** 10 GB
  - **Poziom 2:** 100 GB
  - **Poziom 3:** 1 TB
- **Rekomendacja:** aby zapewnić optymalne opóźnienia pobierania, ogranicz rozmiar każdego sklepu wyszukiwania plików do poniżej 20 GB.

## Ceny

- Opłaty za umieszczanie są naliczane w momencie indeksowania na podstawie obowiązujących [cen umieszczania](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#gemini-embedding) (0,15 USD za 1 mln tokenów).
- Przechowywanie jest bezpłatne.
- Wektory dystrybucyjne podczas zapytań są bezpłatne.
- Pobrane tokeny dokumentu są rozliczane jako zwykłe [tokeny kontekstu](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=pl).

## Co dalej?

- Zapoznaj się z dokumentacją interfejsu API dotyczącą [magazynów wyszukiwania plików](https://ai.google.dev/api/file-search/file-search-stores?hl=pl) i [dokumentów](https://ai.google.dev/api/file-search/documents?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-09 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-09 UTC."],[],[]]
