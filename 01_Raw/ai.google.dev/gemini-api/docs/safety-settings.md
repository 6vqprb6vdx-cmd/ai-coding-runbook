---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=pl
fetched_at: 2026-10-05T06:30:16.616273+00:00
title: "Ustawienia bezpiecze\u0144stwa \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Ustawienia bezpieczeństwa

Interfejs Gemini API udostępnia ustawienia bezpieczeństwa, które możesz dostosować na etapie prototypowania, aby określić, czy aplikacja wymaga bardziej czy mniej restrykcyjnej konfiguracji bezpieczeństwa. Możesz dostosować te ustawienia w 4 kategoriach filtrów, aby ograniczyć lub zezwolić na określone typy treści.

Z tego przewodnika dowiesz się, jak interfejs Gemini API obsługuje ustawienia bezpieczeństwa i filtrowanie oraz jak możesz zmienić ustawienia bezpieczeństwa w swojej aplikacji.

## Filtry bezpieczeństwa

Dostosowywane filtry bezpieczeństwa Gemini API obejmują te kategorie:

| Kategoria | Opis |
| --- | --- |
| Nękanie | Negatywne lub szkodliwe komentarze dotyczące tożsamości innej osoby lub cech chronionych atrybutów. |
| Szerzenie nienawiści | Treści, które są niegrzeczne, lekceważące lub wulgarne. |
| Treści o charakterze jednoznacznie seksualnym | Zawierają odniesienia do aktów seksualnych lub inne treści obsceniczne. |
| Treści niebezpieczne | Promują, ułatwiają lub zachęcają do szkodliwych działań. |

Te kategorie są zdefiniowane w [`HarmCategory`](https://ai.google.dev/api/rest/v1/HarmCategory?hl=pl). Za pomocą tych filtrów możesz dostosować treści do swojego przypadku użycia. Jeśli na przykład tworzysz dialogi w grze wideo, możesz zezwolić na więcej treści ocenionych jako *niebezpieczne* ze względu na charakter gry.

Oprócz dostosowywanych filtrów bezpieczeństwa interfejs Gemini API ma wbudowane zabezpieczenia przed podstawowymi szkodami, takimi jak treści zagrażające bezpieczeństwu dzieci.
Te rodzaje szkód są zawsze blokowane i nie można ich dostosować.

### Poziom filtrowania treści pod kątem bezpieczeństwa

Interfejs Gemini API klasyfikuje poziom prawdopodobieństwa, że treści są niebezpieczne, jako `HIGH`, `MEDIUM`, `LOW` lub `NEGLIGIBLE`.

Interfejs Gemini API blokuje treści na podstawie prawdopodobieństwa, że są one niebezpieczne, a nie na podstawie ich szkodliwości. Warto o tym pamiętać, ponieważ niektóre treści mogą mieć niskie prawdopodobieństwo, że są niebezpieczne, ale ich szkodliwość może być wysoka. Porównaj na przykład te zdania:

1. Robot mnie uderzył.
2. Robot mnie pociął.

Pierwsze zdanie może skutkować wyższym prawdopodobieństwem, że jest niebezpieczne, ale drugie zdanie może być bardziej szkodliwe pod względem przemocy.
Dlatego ważne jest, aby dokładnie przetestować i rozważyć, jaki poziom blokowania jest odpowiedni do obsługi kluczowych przypadków użycia, przy jednoczesnym zminimalizowaniu szkód dla użytkowników.

### Filtrowanie pod kątem bezpieczeństwa na podstawie żądania

Ustawienia bezpieczeństwa możesz dostosować w każdym żądaniu wysyłanym do interfejsu API. Gdy wysyłasz żądanie, treści są analizowane i otrzymują ocenę bezpieczeństwa. Ocena bezpieczeństwa obejmuje kategorię i prawdopodobieństwo klasyfikacji szkody. Jeśli na przykład treści zostały zablokowane, ponieważ system stwierdził wysokie prawdopodobieństwo wystąpienia treści nękających, ocena bezpieczeństwa będzie zawierać kategorię `HARASSMENT` i prawdopodobieństwo szkody ustawione na `HIGH`.

Ze względu na wbudowane zabezpieczenia modelu dodatkowe filtry są domyślnie **wyłączone**.
Jeśli zdecydujesz się je włączyć, możesz skonfigurować system tak, aby blokował treści na podstawie prawdopodobieństwa, że są one niebezpieczne. Domyślne działanie modelu obejmuje większość przypadków użycia, dlatego te ustawienia należy dostosowywać tylko wtedy, gdy jest to na dłuższą metę niezbędne w danej aplikacji.

W tabeli poniżej opisujemy ustawienia blokowania, które możesz dostosować w każdej kategorii. Jeśli na przykład ustawisz w kategorii **Szerzenie nienawiści** ustawienie blokowania na **Blokuj niektóre** , wszystko, co ma wysokie prawdopodobieństwo, że jest treścią szerzącą nienawiść, zostanie zablokowane. Wszystko, co ma niższe prawdopodobieństwo, zostanie dopuszczone.

| Próg (Google AI Studio) | Próg (interfejs API) | Opis |
| --- | --- | --- |
| Wył. | `OFF` | Wyłącz filtr bezpieczeństwa |
| Blokowane: brak | `BLOCK_NONE` | Zawsze wyświetlaj treści niezależnie od prawdopodobieństwa wystąpienia treści niebezpiecznych |
| Blokuj niektóre | `BLOCK_ONLY_HIGH` | Blokuj, gdy prawdopodobieństwo wystąpienia treści niebezpiecznych jest wysokie |
| Blokuj część | `BLOCK_MEDIUM_AND_ABOVE` | Blokuj, gdy prawdopodobieństwo wystąpienia treści niebezpiecznych jest średnie lub wysokie |
| Blokuj większość | `BLOCK_LOW_AND_ABOVE` | Blokuj, gdy prawdopodobieństwo wystąpienia treści niebezpiecznych jest niskie, średnie lub wysokie |
| Nie dotyczy | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Próg nie jest określony, blokuj przy użyciu progu domyślnego |

Jeśli próg nie jest ustawiony, domyślny próg blokowania jest **wyłączony** w przypadku modeli Gemini 2.5 i 3.

Te ustawienia możesz skonfigurować w każdym żądaniu wysyłanym do usługi generatywnej.
Więcej informacji znajdziesz w dokumentacji interfejsu API [`HarmBlockThreshold`](https://ai.google.dev/api/generate-content?hl=pl#harmblockthreshold).

### Opinie dotyczące bezpieczeństwa

[`generateContent`](https://ai.google.dev/api/generate-content?hl=pl#method:-models.generatecontent)
zwraca
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=pl#generatecontentresponse), który
zawiera opinie dotyczące bezpieczeństwa.

Opinie dotyczące promptów są zawarte w
[`promptFeedback`](https://ai.google.dev/api/generate-content?hl=pl#promptfeedback). Jeśli ustawiony jest parametr `promptFeedback.blockReason`, oznacza to, że treść promptu została zablokowana.

Opinie dotyczące kandydata na odpowiedź są zawarte w
[`Candidate.finishReason`](https://ai.google.dev/api/generate-content?hl=pl#candidate) i
[`Candidate.safetyRatings`](https://ai.google.dev/api/generate-content?hl=pl#candidate). Jeśli treść odpowiedzi została zablokowana, a `finishReason` to `SAFETY`, możesz sprawdzić `safetyRatings`, aby uzyskać więcej informacji. Zablokowane treści nie są zwracane.

## Dostosowywanie ustawień bezpieczeństwa

Z tej sekcji dowiesz się, jak dostosować ustawienia bezpieczeństwa w Google AI Studio i w kodzie.

### Google AI Studio

Ustawienia bezpieczeństwa możesz dostosować w Google AI Studio.

W panelu **Ustawienia uruchamiania** kliknij **Ustawienia bezpieczeństwa** w sekcji **Ustawienia zaawansowane** , aby otworzyć okno **Ustawienia bezpieczeństwa uruchamiania**. W tym oknie możesz użyć suwaków, aby dostosować poziom filtrowania treści w każdej kategorii bezpieczeństwa:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=pl)

Gdy wyślesz żądanie (np. zadając modelowi pytanie), a jego treść zostanie zablokowana, pojawi się komunikat warning
**Treść zablokowana**. Aby zobaczyć więcej szczegółów, najedź wskaźnikiem na tekst **Treść zablokowana** , aby zobaczyć kategorię i prawdopodobieństwo klasyfikacji szkody.

### Przykłady kodu

Ten fragment kodu pokazuje, jak ustawić ustawienia bezpieczeństwa w wywołaniu `GenerateContent`. Ustawia on próg dla kategorii szerzenia nienawiści (`HARM_CATEGORY_HATE_SPEECH`). Ustawienie tej kategorii na `BLOCK_LOW_AND_ABOVE` blokuje wszystkie treści, które mają niskie lub wyższe prawdopodobieństwo, że są treściami szerzącymi nienawiść. Aby zrozumieć ustawienia progów, przeczytaj sekcję [Filtrowanie pod kątem bezpieczeństwa
na podstawie żądania](#safety-filtering-per-request).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Some potentially unsafe prompt",
    config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
      ]
    )
)

print(response.text)
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        SafetySettings: []*genai.SafetySetting{
            {
                Category:  "HARM_CATEGORY_HATE_SPEECH",
                Threshold: "BLOCK_LOW_AND_ABOVE",
            },
        },
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Some potentially unsafe prompt."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const safetySettings = [
  {
    category: "HARM_CATEGORY_HATE_SPEECH",
    threshold: "BLOCK_LOW_AND_ABOVE",
  },
];

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Some potentially unsafe prompt.",
    config: {
      safetySettings: safetySettings,
    },
  });
  console.log(response.text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HarmBlockThreshold;
import com.google.genai.types.HarmCategory;
import com.google.genai.types.SafetySetting;
import java.util.Arrays;

Client client = new Client();

SafetySetting hateSpeechSafety =
    SafetySetting.builder()
        .category(HarmCategory.Known.HARM_CATEGORY_HATE_SPEECH)
        .threshold(HarmBlockThreshold.Known.BLOCK_LOW_AND_ABOVE)
        .build();

GenerateContentConfig config =
    GenerateContentConfig.builder()
        .safetySettings(Arrays.asList(hateSpeechSafety))
        .build();

GenerateContentResponse response =
    client.models.generateContent(
        "gemini-3.8-flash", "Some potentially unsafe prompt.", config);

System.out.println(response.text());
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "safetySettings": [
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"}
    ],
    "contents": [{
        "parts":[{
            "text": "'\''Some potentially unsafe prompt.'\''"
        }]
    }]
}'
```

## Dalsze kroki

- Więcej informacji o pełnym interfejsie API znajdziesz w [dokumentacji API](https://ai.google.dev/api?hl=pl).
- Zapoznaj się z [wytycznymi dotyczącymi bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pl), aby uzyskać ogólne informacje o kwestiach bezpieczeństwa
  podczas tworzenia aplikacji z użyciem dużych modeli językowych.
- Dowiedz się więcej o ocenie prawdopodobieństwa w porównaniu z szkodliwością od zespołu [Jigsaw
  team](https://developers.perspectiveapi.com/s/about-the-api-score).
- Dowiedz się więcej o produktach, które przyczyniają się do tworzenia rozwiązań w zakresie bezpieczeństwa, takich jak
  [Perspective
  API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7).
  \* Za pomocą tych ustawień bezpieczeństwa możesz utworzyć klasyfikator toksyczności. Na początek zapoznaj się z przykładem [klasyfikacji](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-18 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-18 UTC."],[],[]]
