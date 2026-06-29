---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl
fetched_at: 2026-06-29T05:33:44.124454+00:00
title: "Grounding z u\u017cyciem Map Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Grounding z użyciem Map Google

Powiązanie ze źródłami informacji przy użyciu Map Google łączy możliwości generatywne Gemini z bogatymi, aktualnymi i opartymi na faktach danymi z Map Google. Dzięki tej funkcji deweloperzy mogą łatwo wprowadzać w swoich aplikacjach funkcje uwzględniające lokalizację. Gdy zapytanie użytkownika ma kontekst związany z danymi z Map, model Gemini korzysta z Map Google, aby udzielać dokładnych i aktualnych odpowiedzi, które są odpowiednie dla określonej przez użytkownika lokalizacji lub ogólnego obszaru.

- **Dokładne odpowiedzi uwzględniające lokalizację:** wykorzystuj obszerne i aktualne dane z Map Google w przypadku zapytań dotyczących konkretnych lokalizacji.
- **Ulepszona personalizacja:** dostosowuj rekomendacje i informacje na podstawie lokalizacji podanych przez użytkownika.

## Rozpocznij

Ten przykład pokazuje, jak zintegrować powiązanie ze źródłami informacji przy użyciu Map Google z aplikacją, aby udzielać dokładnych odpowiedzi uwzględniających lokalizację. Prompt prosi o lokalne rekomendacje z opcjonalną lokalizacją użytkownika, co umożliwia modelowi Gemini korzystanie z danych z Map Google.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Jak działa powiązanie ze źródłami informacji przy użyciu Map Google

Powiązanie ze źródłami informacji przy użyciu Map Google integruje interfejs Gemini API z ekosystemem Google Geo, używając interfejsu API Map Google jako źródła informacji. Gdy zapytanie użytkownika zawiera kontekst geograficzny, model Gemini może wywołać narzędzie powiązania ze źródłami informacji przy użyciu Map Google. Model może wtedy generować odpowiedzi na podstawie danych z Map Google dotyczących podanej lokalizacji.

Proces ten zwykle obejmuje te etapy:

1. **Zapytanie użytkownika:** użytkownik przesyła zapytanie do Twojej aplikacji, które może zawierać kontekst geograficzny (np. „kawiarnie w pobliżu”, „muzea w San Francisco”).
2. **Wywołanie narzędzia:** model Gemini, rozpoznając intencję geograficzną, wywołuje narzędzie powiązania ze źródłami informacji przy użyciu Map Google. To narzędzie może opcjonalnie otrzymać współrzędne geograficzne użytkownika (`latitude` i `longitude`). Narzędzie to jest narzędziem do wyszukiwania tekstowego i działa podobnie do wyszukiwania w Mapach. Zapytania lokalne („w pobliżu”) będą używać współrzędnych, a zapytania konkretne lub nielokalne raczej nie będą uwzględniać lokalizacji.
3. **Pobieranie danych:** usługa powiązania ze źródłami informacji przy użyciu Map Google wysyła zapytania do Map Google, aby uzyskać odpowiednie informacje (np. miejsca, opinie, zdjęcia, adresy, godziny otwarcia).
4. **Generowanie na podstawie danych:** pobrane dane z Map są używane do informowania odpowiedzi modelu Gemini, co zapewnia dokładność i trafność.
5. **Odpowiedź i adnotacje:** model zwraca odpowiedź tekstową z adnotacjami w tekście, które zawierają linki do źródeł w Mapach Google, co umożliwia deweloperom wyświetlanie cytatów.

## Kiedy i dlaczego warto używać powiązania ze źródłami informacji przy użyciu Map Google

Powiązanie ze źródłami informacji przy użyciu Map Google jest idealne w przypadku aplikacji, które wymagają dokładnych, aktualnych i specyficznych dla lokalizacji informacji. Ulepsza ono wrażenia użytkownika, udostępniając trafne i spersonalizowane treści oparte na obszernej bazie danych Map Google, która zawiera ponad 250 milionów miejsc na całym świecie.

Powiązania ze źródłami informacji przy użyciu Map Google należy używać, gdy aplikacja musi:

- udzielać pełnych i dokładnych odpowiedzi na pytania dotyczące konkretnych lokalizacji;
- tworzyć konwersacyjne plany podróży i przewodniki lokalne;
- rekomendować ciekawe miejsca na podstawie lokalizacji i preferencji użytkownika, np. restauracje lub sklepy;
- tworzyć funkcje uwzględniające lokalizację w przypadku usług społecznościowych, handlowych lub dostawy jedzenia.

Powiązanie ze źródłami informacji przy użyciu Map Google sprawdza się w przypadkach użycia, w których kluczowe są bliskość i aktualne dane, np. w przypadku wyszukiwania „najlepszej kawiarni w pobliżu” lub wyznaczania trasy.

## Przypadki użycia

Powiązanie ze źródłami informacji przy użyciu Map Google obsługuje różne przypadki użycia uwzględniające lokalizację.

### Obsługa pytań dotyczących konkretnych miejsc

Zadawaj szczegółowe pytania o konkretne miejsce, aby uzyskać odpowiedzi na podstawie opinii użytkowników Google i innych danych z Map.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
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
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
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
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Personalizacja na podstawie lokalizacji

Uzyskuj rekomendacje dostosowane do preferencji użytkownika i konkretnego obszaru geograficznego.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
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
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
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
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Pomoc w planowaniu planu podróży

Generuj plany na wiele dni z informacjami o trasach i różnych lokalizacjach, które są idealne w przypadku aplikacji podróżniczych.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Wymagania dotyczące korzystania z usługi

Ta sekcja zawiera opis wymagań dotyczących korzystania z usługi powiązania ze źródłami informacji przy użyciu Map Google.

### Informowanie użytkownika o korzystaniu ze źródeł z Map Google

W przypadku każdego wyniku powiązanego z Mapami Google otrzymasz adnotacje źródłowe w blokach treści kroku `model_output`, które obsługują każdą odpowiedź. Zwracane są te metadane:

- adres URL źródła
- nazwa

Podczas prezentowania wyników powiązania ze źródłami informacji przy użyciu Map Google musisz określić powiązane źródła z Map Google i poinformować użytkowników o tych kwestiach:

- Źródła z Map Google muszą znajdować się bezpośrednio po wygenerowanej treści, którą obsługują. Ta wygenerowana treść jest też nazywana wynikiem powiązanym z Mapami Google.
- Źródła z Map Google muszą być widoczne w ramach jednej interakcji z użytkownikiem.

### Wyświetlanie źródeł z Map Google z linkami do Map Google

W przypadku każdej adnotacji źródłowej należy wygenerować podgląd linku zgodnie z tymi wymaganiami:

- Przypisz każde źródło do Map Google zgodnie ze wskazówkami dotyczącymi atrybucji tekstowej w Mapach Google
  .
- Wyświetl nazwę źródła podaną w odpowiedzi.
- Utwórz link do źródła za pomocą `url` z adnotacji.

### Wskazówki dotyczące atrybucji tekstowej w Mapach Google

Gdy przypisujesz źródła do Map Google w tekście, postępuj zgodnie z tymi wskazówkami:

- Nie modyfikuj w żaden sposób tekstu Mapy Google:
  - Nie zmieniaj wielkości liter w nazwie Mapy Google.
  - Nie dziel nazwy Mapy Google na kilka wierszy.
  - Nie tłumacz nazwy Mapy Google na inny język.
  - Uniemożliwiaj przeglądarkom tłumaczenie nazwy Mapy Google, używając atrybutu HTML translate="no".

Więcej informacji o niektórych dostawcach danych do Map Google i ich
warunkach licencji znajdziesz w [informacjach prawnych dotyczących Map Google i Google Earth](https://www.google.com/help/legalnotices_maps/?hl=pl).

## Sprawdzone metody

- **Podaj lokalizację użytkownika:** aby uzyskać najbardziej trafne i spersonalizowane odpowiedzi, zawsze uwzględniaj współrzędne geograficzne (`latitude` i `longitude`) w konfiguracji narzędzia `google_maps`, gdy znasz lokalizację użytkownika.
- **Informuj użytkowników:** wyraźnie informuj użytkowników, że do odpowiadania na ich zapytania używane są dane z Map Google, zwłaszcza gdy narzędzie jest włączone.
- **Wyłączaj, gdy nie jest potrzebne:** powiązanie ze źródłami informacji przy użyciu Map Google jest domyślnie wyłączone. Aby zoptymalizować wydajność i koszty, włączaj je (`"tools": [{"type": "google_maps"}]`) tylko wtedy, gdy zapytanie ma
  wyraźny kontekst geograficzny.

## Ograniczenia

- Powiązanie ze źródłami informacji przy użyciu Map Google obsługuje obecnie tylko prompty i odpowiedzi w języku angielskim.
- Narzędzie może być niedostępne w niektórych regionach.
- Wyniki mogą się różnić w zależności od dokładności lokalizacji i dostępnych danych z Map.
- **Zasięg geograficzny:** powiązanie ze źródłami informacji przy użyciu Map Google jest dostępne na całym świecie.
- **Stan domyślny:** narzędzie powiązania ze źródłami informacji przy użyciu Map Google jest domyślnie wyłączone.
  Musisz je wyraźnie włączyć w żądaniach do interfejsu API.

## Ceny i limity zapytań

Ceny powiązania ze źródłami informacji przy użyciu Map Google różnią się w zależności od generowania modelu:

- **Modele Gemini 3:** Twój projekt jest obciążany za każde **zapytanie wyszukiwania** , które model zdecyduje się wykonać. Pojedynczy **prompt wyszukiwania** (żądanie do interfejsu API wysłane do modelu) może spowodować, że model wykona wiele zapytań wyszukiwania, aby znaleźć potrzebne informacje. Każde z tych zapytań jest liczone jako płatne użycie narzędzia.
- **Modele Gemini 2.5 i starsze:** Twój projekt jest obciążany za każdy **prompt wyszukiwania**.
  Żądanie jest rozliczane tylko wtedy, gdy prompt zwróci co najmniej 1 wynik powiązany z Mapami Google, niezależnie od tego, ile pojedynczych zapytań wyszukiwania model wykonał wewnętrznie, aby uzyskać ten wynik.

Szczegółowe informacje o cenach znajdziesz na stronie cennika interfejsu [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).

## Obsługiwane modele

Powiązanie ze źródłami informacji przy użyciu Map Google jest obsługiwane przez te modele:

| Model | Powiązanie ze źródłami informacji przy użyciu Map Google |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Obsługiwane kombinacje narzędzi

Modele Gemini 3 obsługują łączenie wbudowanych narzędzi (takich jak powiązanie ze źródłami informacji przy użyciu Map Google) z narzędziami niestandardowymi (wywoływanie funkcji). Więcej informacji znajdziesz na
[stronie kombinacji narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

## Co dalej?

- Dowiedz się więcej o innych [dostępnych narzędziach](https://ai.google.dev/gemini-api/docs/tools?hl=pl).
- Więcej informacji o sprawdzonych metodach dotyczących odpowiedzialnej AI i filtrach bezpieczeństwa interfejsu Gemini API znajdziesz w [przewodniku po ustawieniach bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-24 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-24 UTC."],[],[]]
