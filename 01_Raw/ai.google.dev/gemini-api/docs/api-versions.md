---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=pl
fetched_at: 2026-06-15T06:27:07.996282+00:00
title: "Om\u00f3wienie wersji interfejsu API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumentacja API](https://ai.google.dev/api?hl=pl)

Prześlij opinię

# Omówienie wersji interfejsu API

Ten dokument zawiera ogólne omówienie różnic między wersjami `v1`
i `v1beta` interfejsu Gemini API.

- **v1**: stabilna wersja interfejsu API. Funkcje w stabilnej wersji są w pełni obsługiwane przez cały okres istnienia głównej wersji. Jeśli wystąpią niezgodne zmiany, zostanie utworzona następna główna wersja interfejsu API, a dotychczasowa wersja zostanie wycofana po rozsądnym czasie.
  W interfejsie API mogą zostać wprowadzone zmiany, które nie powodują niezgodności, bez zmiany głównej wersji.
- **v1beta**: ta wersja zawiera wczesne funkcje, które mogą być w trakcie opracowywania i mogą ulec niezgodnym zmianom. Nie ma też gwarancji, że funkcje w wersji beta zostaną przeniesione do wersji stabilnej. **Jeśli w środowisku produkcyjnym wymagana jest stabilność i nie możesz sobie pozwolić na niezgodne zmiany, nie używaj tej wersji w środowisku produkcyjnym.**

| Funkcja | v1 | v1beta |
| --- | --- | --- |
| Generowanie treści – dane wejściowe zawierające tylko tekst |  |  |
| Generowanie treści – dane wejściowe zawierające tekst i obraz |  |  |
| Generowanie treści – dane wyjściowe zawierające tekst |  |  |
| Generowanie treści – rozmowy wieloetapowe (czat) |  |  |
| Generowanie treści – wywołania funkcji |  |  |
| Generowanie treści – przesyłanie strumieniowe |  |  |
| Osadzanie treści – dane wejściowe zawierające tylko tekst |  |  |
| Generowanie odpowiedzi |  |  |
| Wyszukiwarka semantyczna |  |  |
| Interfejs Interactions API |  |  |

- – Obsługiwane
- \– Nigdy nie będzie obsługiwane

## Konfigurowanie wersji interfejsu API w pakiecie SDK

Pakiety SDK interfejsu Gemini API domyślnie używają wersji `v1beta`, ale możesz wyraźnie określić wersje, ustawiając wersję interfejsu API, jak pokazano w tym przykładowym kodzie:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents="Explain how AI works",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'
```

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-28 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-28 UTC."],[],[]]
