---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl
fetched_at: 2026-07-20T04:41:42.255431+00:00
title: "Wnioskowanie o\u00a0priorytecie \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wnioskowanie o priorytecie

Opis: dowiedz się, jak zoptymalizować czas oczekiwania za pomocą poziomu wnioskowania Priorytet w interfejsie Interactions API

Gemini Priority API to poziom wnioskowania Premium przeznaczony do zbiorów zadań o kluczowym znaczeniu dla firmy, które wymagają mniejszego czasu oczekiwania i najwyższej niezawodności w cenie premium. Ruch na poziomie Priorytet ma wyższy priorytet niż ruch na poziomie Standard i Flex.

Wnioskowanie z priorytetem jest dostępne we wszystkich punktach końcowych interfejsu Interactions API.

## Jak korzystać z priorytetu

Aby korzystać z poziomu Priorytet, ustaw w żądaniu pole `service_tier` na `priority`. Jeśli to pole zostanie pominięte, domyślnym poziomem będzie Standard.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Jak działa wnioskowanie z priorytetem

Wnioskowanie z priorytetem kieruje żądania do kolejek obliczeniowych o wysokim priorytecie, co zapewnia przewidywalną i szybką wydajność w przypadku aplikacji dla użytkowników. Jego głównym mechanizmem jest łagodna degradacja po stronie serwera do standardowego przetwarzania w przypadku ruchu, który przekracza limity dynamiczne. Dzięki temu aplikacja zachowuje stabilność, a żądanie nie jest odrzucane.

| Funkcja | Priorytet | Standardowe | Flex | Wsad |
| --- | --- | --- | --- | --- |
| **Ceny** | 75–100% więcej niż w przypadku poziomu Standard | Pełna cena | 50% zniżki | 50% zniżki |
| **Czas oczekiwania** | Sekundy | Sekundy do minut | Minuty (docelowo 1–15 min) | Do 24 godzin |
| **Niezawodność** | Wysoka (nie można jej obniżyć) | Wysoka / średnio wysoka | Bez gwarancji (można ją obniżyć) | Wysoka (w przypadku przepustowości) |
| **Interfejs** | Synchroniczna | Synchroniczna | Synchroniczna | Asynchroniczna |

### Główne zalety

- **Krótki czas oczekiwania**: zaprojektowany z myślą o czasie odpowiedzi w sekundach w przypadku interaktywnych,
  narzędzi AI dla użytkowników.
- **Wysoka niezawodność**: ruch jest traktowany z najwyższym priorytetem i jest
  ściśle nieobniżalny.
- **Łagodna degradacja**: w przypadku nagłego wzrostu ruchu przekraczającego limity dynamiczne następuje
  automatyczne obniżenie poziomu do Standardowego w celu przetworzenia żądania, co zapobiega przerwom w działaniu usługi.
- **Niewielkie utrudnienia**: używa tej samej synchronicznej `create` metody co poziomy
  Standard i Flex.

### Przypadki użycia

Przetwarzanie z priorytetem jest idealne w przypadku zbiorów zadań o kluczowym znaczeniu dla firmy, w których najważniejsza jest wydajność i niezawodność.

- **Interaktywne aplikacje AI**: chatboty i asystenci obsługi klienta, w przypadku których
  użytkownicy płacą więcej i oczekują szybkich i spójnych odpowiedzi.
- **Silniki podejmowania decyzji w czasie rzeczywistym**: systemy wymagające bardzo niezawodnych wyników z krótkim czasem oczekiwania
  , takie jak triage zgłoszeń na żywo czy wykrywanie oszustw.
- **Funkcje dla klientów premium**: deweloperzy, którzy muszą zagwarantować wyższe cele poziomu usług (SLO) dla płacących klientów.

### Ograniczenia liczby żądań

Zużycie na poziomie Priorytet ma własne ograniczenia liczby żądań, chociaż jest ono wliczane do [ogólnych ograniczeń liczby żądań dotyczących ruchu interaktywnego](https://aistudio.google.com/rate-limit?hl=pl). Domyślne ograniczenia liczby żądań w przypadku wnioskowania z priorytetem to **0,3-krotność standardowego ograniczenia liczby żądań dla modelu / poziomu**.

### Logika łagodnej degradacji

Jeśli limity priorytetu zostaną przekroczone z powodu przeciążenia, żądania przekraczające limit zostaną **automatycznie i łagodnie** obniżone do standardowego przetwarzania zamiast odrzucenia z błędem 503 lub 429. Żądania obniżone do poziomu Standard są rozliczane według stawki standardowej, a nie stawki premium Priorytet.

### Odpowiedzialność klienta

- **Monitorowanie odpowiedzi**: deweloperzy powinni monitorować `x-gemini-service-tier`
  nagłówek w odpowiedzi interfejsu API, aby wykryć, czy żądania są często obniżane do poziomu
  `standard`.
- **Ponawianie prób**: klienci muszą wdrożyć logikę ponawiania prób lub wycofywania się z wykładniczym opóźnieniem w przypadku
  standardowych błędów, takich jak `DEADLINE_EXCEEDED`.

## Ceny

Wnioskowanie z priorytetem jest o 75–100% droższe niż [standardowy interfejs API](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) i rozliczane za token.

## Obsługiwane modele

Wnioskowanie z priorytetem jest obsługiwane przez te modele:

| Model | Wnioskowanie z priorytetem |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ |

## Co dalej?

- [Wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl) w celu zmniejszenia kosztów.
- [Tokeny](https://ai.google.dev/gemini-api/docs/tokens?hl=pl): dowiedz się więcej o tokenach.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-06 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-06 UTC."],[],[]]
