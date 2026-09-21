---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl
fetched_at: 2026-09-21T05:54:26.724546+00:00
title: "Rozdzielczo\u015b\u0107 multimedi\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozdzielczość multimediów

Parametr `media_resolution` określa sposób przetwarzania przez Gemini API danych wejściowych w postaci multimediów, takich jak obrazy, filmy, dźwięk i dokumenty PDF, poprzez określenie **maksymalnej liczby tokenów** przydzielonych do danych wejściowych w postaci multimediów. Umożliwia to zrównoważenie jakości odpowiedzi z opóźnieniem i kosztem. W przypadku danych wejściowych w postaci obrazów i dokumentów przydział tokenów jest skalowany na podstawie ustawienia rozdzielczości, natomiast w przypadku danych wejściowych w postaci dźwięku tokeny są generowane ze stałą szybkością na sekundę na wszystkich poziomach rozdzielczości. Informacje o różnych ustawieniach, wartościach domyślnych i ich odpowiednikach w postaci tokenów znajdziesz w sekcji [Liczba tokenów](#token-counts).

Możesz skonfigurować rozdzielczość multimediów dla poszczególnych obiektów multimedialnych (elementów treści) w swoim żądaniu (tylko Gemini 3).

## Rozdzielczość multimediów dla poszczególnych elementów treści (tylko Gemini 3)

Gemini 3 umożliwia ustawienie rozdzielczości multimediów dla poszczególnych obiektów multimedialnych w żądaniu, co pozwala na precyzyjną optymalizację wykorzystania tokenów. W ramach jednego żądania możesz łączyć różne poziomy rozdzielczości. Na przykład używaj wysokiej rozdzielczości w przypadku złożonego diagramu, a niskiej w przypadku prostego obrazu kontekstowego.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
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
- `high`: większa liczba tokenów, która zapewnia modelowi więcej szczegółów, ale wiąże się z większym czasem oczekiwania i kosztem.
- `ultra_high` (Tylko w przypadku poszczególnych elementów treści): najwyższa liczba tokenów, wymagana w określonych przypadkach użycia, np. w [przypadku korzystania z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl).

Pamiętaj, że `high` zapewnia optymalną wydajność w większości przypadków.

Dokładna liczba tokenów wygenerowanych na każdym z tych poziomów zależy zarówno od **typu multimediów** (obraz, film, dźwięk, PDF), jak i od **wersji modelu**.

## Liczba tokenów

W tabelach poniżej znajdziesz podsumowanie przybliżonej liczby tokenów dla każdej wartości `media_resolution` i każdego typu multimediów w poszczególnych rodzinach modeli.

**Modele Gemini 3**

| MediaResolution | Obraz | Wideo | Audio | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (wartość domyślna) | 1120 | 70 | 25 (na sekundę) | 560 |
| `low` | 280 | 70 | 25 (na sekundę) | 280 znaków + tekst natywny |
| `medium` | 560 | 70 | 25 (na sekundę) | 560 + tekst natywny |
| `high` | 1120 | 280 | 25 (na sekundę) | 1120 + Native Text |
| `ultra_high` | 2240 | Nie dotyczy | Nie dotyczy | Nie dotyczy |

## Wybór odpowiedniej rozdzielczości

- **Domyślna (`unspecified`):** zacznij od domyślnej. Jest on dostosowany do większości typowych przypadków użycia, aby zapewnić dobrą równowagę między jakością, opóźnieniem i kosztem.
- **`low`:** używaj w sytuacjach, w których najważniejsze są koszty i czas oczekiwania, a szczegółowość ma mniejsze znaczenie.
- **`medium` / `high`:** zwiększ rozdzielczość, gdy zadanie wymaga zrozumienia skomplikowanych szczegółów w multimediach. Jest to często potrzebne w przypadku złożonej analizy wizualnej, odczytywania wykresów lub zrozumienia gęstych dokumentów.
- **`ultra_high`** – dostępne tylko w przypadku ustawienia dotyczącego poszczególnych elementów treści. Zalecane w przypadku konkretnych zastosowań, takich jak korzystanie z komputera, lub gdy testy wykazują wyraźną poprawę w porównaniu z `high`.
- **Sterowanie poszczególnymi elementami treści (Gemini 3):** optymalizuje wykorzystanie tokenów. Na przykład w prompcie z wieloma obrazami użyj elementu `high` w przypadku złożonego diagramu, a elementów `low` lub `medium` w przypadku prostszych obrazów kontekstowych.

**Zalecane ustawienia**

Poniżej znajdziesz listę zalecanych ustawień rozdzielczości multimediów dla każdego obsługiwanego typu multimediów.

| Typ mediów | Zalecane ustawienie | Maksymalna liczba tokenów | Wytyczne dotyczące użytkowania |
| --- | --- | --- | --- |
| **Obrazy** | `high` | 1120 | Zalecane w przypadku większości zadań związanych z analizą obrazów, aby zapewnić najwyższą jakość. |
| **Pliki PDF** | `medium` | 560 | Optymalne do analizy dokumentów; jakość zwykle osiąga maksymalny poziom przy wartości `medium`. Zwiększenie do `high` rzadko poprawia wyniki OCR w przypadku standardowych dokumentów. |
| **Wideo** (ogólne) | `low` (lub `medium`) | 70 (na klatkę) | **Uwaga:** w przypadku filmów ustawienia `low` i `medium` są traktowane identycznie (70 tokenów), aby zoptymalizować wykorzystanie kontekstu. Jest to wystarczające w przypadku większości zadań związanych z rozpoznawaniem i opisywaniem działań. |
| **Film** (z dużą ilością tekstu) | `high` | 280 (na klatkę) | Wymagane tylko wtedy, gdy przypadek użycia obejmuje odczytywanie gęstego tekstu (OCR) lub drobnych szczegółów w klatkach wideo. |
| **Dźwięk** | `unspecified` (wartość domyślna) | 25 (na sekundę) | Dźwięk jest tokenizowany ze stałą szybkością 25 tokenów na sekundę we wszystkich obsługiwanych ustawieniach rozdzielczości (`unspecified`, `low`, `medium` i `high`). |

Zawsze testuj i oceniaj wpływ różnych ustawień rozdzielczości na aplikację, aby znaleźć najlepszy kompromis między jakością, opóźnieniem i kosztem.

## Związek z trybami przetwarzania filmów

Parametry `media_resolution` i przetwarzania kontrolują różne aspekty danych wejściowych wideo:

- `media_resolution` określa **rozdzielczość** każdej klatki (liczbę tokenów na klatkę).
- Elementy sterujące `processing` / `media_processing` określają, **które treści z filmu** są wczytywane do kontekstu.

Oba ustawienia możesz zastosować do tego samego wejścia wideo. Możesz na przykład użyć przetwarzania agentowego z niską rozdzielczością multimediów, aby zminimalizować całkowite zużycie tokenów w przypadku długiego filmu.

Szczegółowe informacje o trybach przetwarzania filmów znajdziesz w przewodniku [Analizowanie filmów przez agenta](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl#agentic-video-understanding).

## Podsumowanie zgodności wersji

- Ustawianie `resolution` w przypadku poszczególnych elementów treści jest **dostępne tylko w modelach Gemini 3**.

## Dalsze kroki

- Więcej informacji o możliwościach multimodalnych interfejsu Gemini API znajdziesz w przewodnikach dotyczących [rozpoznawania obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl), [rozumienia filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl), [rozumienia dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl) i [rozumienia dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-19 UTC."],[],[]]
