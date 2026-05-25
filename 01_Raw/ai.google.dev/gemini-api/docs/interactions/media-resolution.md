---
source_url: https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=pl
fetched_at: 2026-05-25T13:03:24.803955+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozdzielczość multimediów

Parametr `media_resolution` określa, jak interfejs Gemini API przetwarza dane wejściowe multimediów, takie jak obrazy, filmy i dokumenty PDF, poprzez określenie **maksymalnej liczby tokenów** przydzielonych do danych wejściowych multimediów. Umożliwia to zrównoważenie jakości odpowiedzi z opóźnieniem i kosztem. Więcej informacji o różnych ustawieniach, wartościach domyślnych i ich odpowiednikach w postaci tokenów znajdziesz w sekcji [Liczba tokenów](#token-counts).

Możesz skonfigurować rozdzielczość multimediów dla poszczególnych obiektów multimedialnych (elementów treści) w swojej prośbie (tylko Gemini 3).

## Rozdzielczość multimediów dla poszczególnych elementów treści (tylko Gemini 3)

Gemini 3 umożliwia ustawienie rozdzielczości multimediów dla poszczególnych obiektów multimedialnych w żądaniu, co pozwala na precyzyjną optymalizację wykorzystania tokenów. W jednym żądaniu możesz łączyć różne poziomy rozdzielczości. Na przykład możesz użyć wysokiej rozdzielczości w przypadku złożonego diagramu, a niskiej w przypadku prostego obrazu kontekstowego.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Dostępne wartości rozdzielczości

Interfejs Gemini API określa te poziomy rozdzielczości multimediów:

- `unspecified`: ustawienie domyślne. Liczba tokenów na tym poziomie znacznie różni się w przypadku Gemini 3 i starszych modeli Gemini.
- `low`: mniejsza liczba tokenów, co skutkuje szybszym przetwarzaniem i niższymi kosztami, ale mniejszą ilością szczegółów.
- `medium`: równowaga między szczegółowością, kosztem i opóźnieniem.
- `high`: większa liczba tokenów, która zapewnia modelowi więcej szczegółów do pracy, ale wiąże się z większym czasem oczekiwania i kosztem.
- `ultra_high` (Tylko w przypadku poszczególnych elementów treści): najwyższa liczba tokenów, wymagana w określonych przypadkach użycia, np. w przypadku [korzystania z komputera](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=pl).

Pamiętaj, że `high` zapewnia optymalną wydajność w większości przypadków użycia.

Dokładna liczba tokenów wygenerowanych na każdym z tych poziomów zależy zarówno od **typu multimediów** (obraz, film, PDF), jak i od **wersji modelu**.

## Liczba tokenów

W tabelach poniżej znajdziesz podsumowanie przybliżonej liczby tokenów dla każdej wartości `media_resolution` i każdego typu multimediów w poszczególnych rodzinach modeli.

**Modele Gemini 3**

| MediaResolution | Obraz | Wideo | PDF |
| --- | --- | --- | --- |
| `unspecified` (wartość domyślna) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 znaków + tekst natywny |
| `medium` | 560 | 70 | 560 + tekst natywny |
| `high` | 1120 | 280 | 1120 + tekst natywny |
| `ultra_high` | 2240 | Nie dotyczy | Nie dotyczy |

## Wybór odpowiedniej rozdzielczości

- **Domyślna (`unspecified`):** zacznij od domyślnej. Jest on dostosowany do większości typowych przypadków użycia, aby zapewnić dobrą równowagę między jakością, opóźnieniem i kosztem.
- **`low`:** używaj w sytuacjach, w których najważniejsze są koszty i czas oczekiwania, a szczegółowość ma mniejsze znaczenie.
- **`medium` / `high`:** zwiększ rozdzielczość, gdy zadanie wymaga zrozumienia skomplikowanych szczegółów w multimediach. Jest to często potrzebne w przypadku złożonej analizy wizualnej, odczytywania wykresów lub zrozumienia gęstych dokumentów.
- **`ultra_high`** – dostępny tylko w przypadku ustawienia dotyczącego poszczególnych elementów treści. Zalecany w przypadku konkretnych zastosowań, takich jak korzystanie z komputera, lub gdy testy wykazują wyraźną poprawę w porównaniu z `high`.
- **Sterowanie poszczególnymi elementami treści (Gemini 3):** optymalizuje wykorzystanie tokenów. Na przykład w prompcie z wieloma obrazami użyj elementu `high` w przypadku złożonego diagramu, a elementu `low` lub `medium` w przypadku prostszych obrazów kontekstowych.

**Zalecane ustawienia**

Poniżej znajdziesz listę zalecanych ustawień rozdzielczości multimediów dla każdego obsługiwanego typu multimediów.

| Typ mediów | Zalecane ustawienie | Maksymalna liczba tokenów | Wytyczne dotyczące użytkowania |
| --- | --- | --- | --- |
| **Obrazy** | `high` | 1120 | Zalecane w przypadku większości zadań związanych z analizą obrazów, aby zapewnić maksymalną jakość. |
| **PDF** | `medium` | 560 | Optymalne do analizy dokumentów; jakość zwykle osiąga maksymalny poziom przy wartości `medium`. Zwiększenie do `high` rzadko poprawia wyniki OCR w przypadku standardowych dokumentów. |
| **Wideo** (ogólne) | `low` (lub `medium`) | 70 (na klatkę) | **Uwaga:** w przypadku filmów ustawienia `low` i `medium` są traktowane identycznie (70 tokenów), aby zoptymalizować wykorzystanie kontekstu. Jest to wystarczające w przypadku większości zadań związanych z rozpoznawaniem i opisywaniem działań. |
| **Film** (z dużą ilością tekstu) | `high` | 280 (na klatkę) | Wymagane tylko wtedy, gdy przypadek użycia obejmuje odczytywanie gęstego tekstu (OCR) lub drobnych szczegółów w klatkach wideo. |

Zawsze testuj i oceniaj wpływ różnych ustawień rozdzielczości na aplikację, aby znaleźć najlepszy kompromis między jakością, opóźnieniem i kosztem.

## Podsumowanie zgodności wersji

- Ustawianie `resolution` w przypadku poszczególnych elementów treści jest **dostępne tylko w modelach Gemini 3**.

## Dalsze kroki

- Więcej informacji o możliwościach multimodalnych interfejsu Gemini API znajdziesz w przewodnikach dotyczących [rozpoznawania obrazów](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=pl), [rozumienia filmów](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=pl) i [rozumienia dokumentów](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-19 UTC."],[],[]]
