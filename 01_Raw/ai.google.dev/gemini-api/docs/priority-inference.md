---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl
fetched_at: 2026-10-26T06:02:17.903633+00:00
title: "Wnioskowanie o\u00a0priorytecie \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wnioskowanie o priorytecie

Opis: jak zoptymalizować czas oczekiwania za pomocą poziomu wnioskowania Priority w interfejsie Interactions API

Gemini Priority API to poziom wnioskowania Premium przeznaczony do zbiorów zadań o kluczowym znaczeniu dla firmy, które wymagają mniejszego czasu oczekiwania i najwyższej niezawodności w cenie premium. Ruch na poziomie Priority ma wyższy priorytet niż ruch na poziomie standardowym interfejsu API i na poziomie Flex.

Wnioskowanie Priority jest dostępne we wszystkich punktach końcowych interfejsu Interactions API.

## Jak korzystać z poziomu Priority

Aby korzystać z poziomu Priority, ustaw w żądaniu pole `service_tier` na `priority`. Jeśli to pole zostanie pominięte, domyślnym poziomem będzie standardowy.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Perform a priority inference task."))
        .serviceTier(ServiceTier.PRIORITY)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Perform a priority inference task."),
            ServiceTier: interactions.ServiceTierPriority.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Jak działa wnioskowanie Priority

Wnioskowanie Priority kieruje żądania do kolejek obliczeniowych o wysokim znaczeniu, co zapewnia przewidywalną i szybką wydajność w przypadku aplikacji przeznaczonych dla użytkowników. Jego głównym mechanizmem jest płynne przejście po stronie serwera do standardowego przetwarzania ruchu, który przekracza limity dynamiczne. Dzięki temu zamiast odrzucać żądanie, zapewnia stabilność aplikacji.

| Funkcja | Priorytet | Standardowy | Flex | Wsad |
| --- | --- | --- | --- | --- |
| **Ceny** | O 75–100% wyższe niż w przypadku poziomu standardowego | Bilet normalny | 50% rabatu | 50% rabatu |
| **Czas oczekiwania** | Sekundy | Sekundy do minut | Minuty (docelowo 1–15 min) | Do 24 godzin |
| **Niezawodność** | Wysoka (nie można jej obniżyć) | Wysoka / średnio wysoka | Najlepsze możliwości (można ją obniżyć) | Wysoka (w przypadku przepustowości) |
| **Interfejs** | Synchroniczna | Synchroniczna | Synchroniczna | Asynchroniczny |

### Główne zalety

- **Krótki czas oczekiwania**: zaprojektowany z myślą o czasie odpowiedzi w sekundach w przypadku interaktywnych,
  narzędzi AI przeznaczonych dla użytkowników.
- **Wysoka niezawodność**: ruch jest traktowany z najwyższym priorytetem i jest
  ściśle nieobniżalny.
- **Łagodna degradacja**: w przypadku nagłego wzrostu ruchu przekraczającego limity dynamiczne następuje automatyczne przejście do przetwarzania na poziomie standardowym zamiast odrzucania żądania, co zapobiega przerwom w działaniu usługi.
- **Niewielkie utrudnienia**: używa tej samej synchronicznej `create` metody co poziomy
  standardowy i Flex.

### Przypadki użycia

Przetwarzanie Priority jest idealne w przypadku zbiorów zadań o kluczowym znaczeniu dla firmy, w których najważniejsza jest wydajność i niezawodność.

- **Interaktywne aplikacje AI**: czatboty i asystenci obsługi klienta, w przypadku których
  użytkownicy płacą więcej i oczekują szybkich, spójnych odpowiedzi.
- **Silniki decyzyjne w czasie rzeczywistym**: systemy wymagające bardzo niezawodnych wyników o niskim czasie oczekiwania
  , takich jak triage zgłoszeń na żywo czy wykrywanie oszustw.
- **Funkcje premium dla klientów**: deweloperzy, którzy muszą zagwarantować wyższe cele poziomu usług (SLO) dla płacących klientów.

### Ograniczenia liczby żądań

Wykorzystanie poziomu Priority ma własne ograniczenia liczby żądań, mimo że jest ono wliczane do [ogólnych ograniczeń liczby żądań dotyczących ruchu interaktywnego](https://aistudio.google.com/rate-limit?hl=pl). Domyślne ograniczenia liczby żądań w przypadku wnioskowania Priority to **0,3-krotność standardowego ograniczenia liczby żądań dla modelu / poziomu**.

### Logika płynnego przejścia

Jeśli limity Priority zostaną przekroczone z powodu dużego natężenia ruchu, żądania przekraczające limit zostaną **automatycznie i płynnie** przeniesione do przetwarzania standardowego zamiast odrzucenia z błędem 503 lub 429. Żądania przeniesione na niższy poziom są rozliczane według stawki standardowej, a nie stawki premium Priority.

### Odpowiedzialność klienta

- **Monitorowanie odpowiedzi**: deweloperzy powinni monitorować `x-gemini-service-tier`
  nagłówek w odpowiedzi interfejsu API, aby wykryć, czy żądania są często przenoszone na poziom
  `standard`.
- **Ponawianie prób**: klienci muszą wdrożyć logikę ponawiania prób/wykładniczego wycofywania w przypadku
  standardowych błędów, takich jak `DEADLINE_EXCEEDED`.

## Ceny

Wnioskowanie Priority jest o 75–100% droższe niż [standardowy interfejs API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) i rozliczane za token.

## Obsługiwane modele

Wnioskowanie Priority jest obsługiwane przez te modele:

| Model | Wnioskowanie Priority |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pl) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=pl) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pl) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja zapoznawcza)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja zapoznawcza)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Co dalej?

- [Wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl) w celu zmniejszenia kosztów.
- [Tokeny](https://ai.google.dev/gemini-api/docs/tokens?hl=pl): informacje o tokenach.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-13 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-13 UTC."],[],[]]
