---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=pl
fetched_at: 2026-08-03T04:26:11.377757+00:00
title: "Kontekst adresu URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Kontekst adresu URL

Narzędzie kontekstu adresu URL umożliwia przekazywanie modelom dodatkowego kontekstu w
postaci adresów URL. Jeśli uwzględnisz adresy URL w żądaniu, model uzyska dostęp do
treści z tych stron (o ile nie jest to typ adresu URL wymieniony w sekcji
[ograniczeń](#limitations)), aby informować
i ulepszać swoją odpowiedź.

Narzędzie kontekstu adresu URL jest przydatne w przypadku takich zadań jak:

- **Wyodrębnianie danych**: pobieranie konkretnych informacji, takich jak ceny, nazwy lub kluczowe
  ustalenia, z wielu adresów URL.
- **Porównywanie dokumentów**: analizowanie wielu raportów, artykułów lub plików PDF w celu
  identyfikowania różnic i śledzenia trendów.
- **Synteza i tworzenie treści:** łączenie informacji z kilku źródłowych adresów URL w celu generowania dokładnych podsumowań, postów na blogu lub raportów.
- **Analizowanie kodu i dokumentów:** wskazywanie repozytorium GitHub lub dokumentacji technicznej w celu wyjaśnienia kodu, wygenerowania instrukcji konfiguracji lub udzielenia odpowiedzi na pytania.

Z przykładu poniżej dowiesz się, jak porównać 2 przepisy z różnych witryn.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Jak to działa

Narzędzie kontekstu adresu URL korzysta z 2-etapowego procesu pobierania, aby zachować równowagę między szybkością, kosztem a dostępem do aktualnych danych. Gdy podasz adres URL, narzędzie najpierw spróbuje pobrać treść z wewnętrznej pamięci podręcznej indeksu. Działa ona jak wysoce zoptymalizowana pamięć podręczna. Jeśli adres URL nie jest dostępny w indeksie (np. jeśli jest to bardzo nowa strona), narzędzie automatycznie przełączy się na pobieranie na żywo.
Dzięki temu uzyskuje bezpośredni dostęp do adresu URL, aby pobrać jego zawartość w czasie rzeczywistym.

## Łączenie z innymi narzędziami

Aby tworzyć bardziej zaawansowane przepływy pracy, możesz połączyć narzędzie kontekstu adresu URL z innymi narzędziami.

[Modele Gemini 3](#supported-models) obsługują łączenie wbudowanych narzędzi
(takich jak kontekst adresu URL) z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na
[stronie dotyczącej kombinacji narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

### Powiązanie ze źródłem informacji przy użyciu wyszukiwarki

Gdy włączone są zarówno kontekst adresu URL, jak i
[powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pl),
model może korzystać z funkcji wyszukiwania, aby znajdować
odpowiednie informacje w internecie, a następnie używać narzędzia kontekstu adresu URL, aby lepiej
zrozumieć znalezione strony. To podejście jest skuteczne w przypadku promptów, które wymagają zarówno szerokiego wyszukiwania, jak i szczegółowej analizy konkretnych stron.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Opis odpowiedzi

Gdy model używa narzędzia kontekstu adresu URL, jego odpowiedź tekstowa zawiera w tekście adnotacje `url_citation`. Każda adnotacja łączy segment tekstu odpowiedzi (za pomocą `start_index` i `end_index`) z adresem URL źródła, z którego pochodzi. Jest to podstawowy sposób wyświetlania cytatów w aplikacji
. Aby je wyodrębnić, zapoznaj się z [głównym przykładem powyżej](#get-started).

Odpowiedź zawiera też krok `url_context_result` z metadanymi dotyczącymi każdej próby pobrania adresu URL (stan, pobrany adres URL). Jest to przydatne głównie do debugowania.

### Testy zabezpieczeń

System przeprowadza sprawdzanie moderacji treści pod kątem adresów URL, aby potwierdzić, że spełniają one standardy bezpieczeństwa. Jeśli adres URL nie przejdzie tego testu, odpowiedni
`url_context_result` krok będzie miał `status` równy `"unsafe"`.

### Liczba tokenów

Treści pobrane z adresów URL podanych w prompcie są liczone jako część tokenów wejściowych. Liczbę tokenów możesz sprawdzić w obiekcie `usage` interakcji. Oto przykład:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

Cena za token zależy od używanego modelu. Więcej informacji znajdziesz na
[stronie cennika](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

| Model | Kontekst adresu URL |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pl) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Sprawdzone metody

- **Podawaj konkretne adresy URL**: aby uzyskać najlepsze wyniki, podaj bezpośrednie adresy URL do
  treści, które mają być analizowane przez model. Model będzie pobierać treści tylko z podanych adresów URL, a nie z linków zagnieżdżonych.
- **Sprawdzaj dostępność**: upewnij się, że podane adresy URL nie prowadzą do
  stron, które wymagają logowania lub są płatne.
- **Używaj pełnego adresu URL**: podaj pełny adres URL, w tym protokół
  (np. https://www.google.com zamiast google.com).

## Ograniczenia

- Limit żądań: narzędzie może przetwarzać maksymalnie 20 adresów URL na żądanie.
- Rozmiar treści adresu URL: maksymalny rozmiar treści pobranych z jednego adresu URL to 34 MB.
- Dostępność publiczna: adresy URL muszą być publicznie dostępne w internecie.
  Adresy localhost (np. localhost, 127.0.0.1), sieci prywatne i usługi tunelowania (np. ngrok, pinggy) nie są obsługiwane.

### Obsługiwane i nieobsługiwane typy treści

Narzędzie może wyodrębniać treści z adresów URL o tych typach:

- Tekst (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Obraz (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Te typy treści **nie są** obsługiwane:

- Treści płatne
- Filmy z YouTube (informacje o przetwarzaniu adresów URL z YouTube znajdziesz w artykule o
  [rozumieniu filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl#youtube))
- Pliki Google Workspace, takie jak dokumenty i arkusze Google
- Pliki audio i wideo

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-31 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-31 UTC."],[],[]]
