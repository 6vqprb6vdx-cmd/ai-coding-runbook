---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=pl
fetched_at: 2026-07-06T05:12:33.353579+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Gemini

[Modele z serii Gemini 3 i 2.5](https://ai.google.dev/gemini-api/docs/models?hl=pl) wykorzystują „proces myślowy”, który znacznie poprawia ich zdolność do rozumowania i planowania wieloetapowego, dzięki czemu są bardzo skuteczne w przypadku złożonych zadań, takich jak kodowanie, zaawansowana matematyka i analiza danych.

Gdy używasz modelu myślenia, Gemini analizuje prompta wewnętrznie przed udzieleniem odpowiedzi. Interfejs API interakcji udostępnia to rozumowanie za pomocą `thought`kroków, czyli specjalnych kroków, które pojawiają się chronologicznie obok wywołań funkcji, danych wejściowych użytkownika lub danych wyjściowych modelu w `steps`tablicy.

Każdy krok myślowy zawiera 2 pola:

| Pole | Wymagane | Opis |
| --- | --- | --- |
| `signature` | ✅ Tak | zaszyfrowana reprezentacja wewnętrznego stanu rozumowania modelu; Zawsze obecne, nawet gdy model wykonuje minimalne rozumowanie. |
| `summary` | ❌ Nie | Tablica treści (tekst lub obrazy) podsumowująca uzasadnienie. Może być pusta w zależności od konfiguracji [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=pl), tego, czy model przeprowadził wystarczające rozumowanie, lub typu treści (np. latentne obrazy mogą nie mieć podsumowań tekstowych). |

## Interakcje z myśleniem

Rozpoczęcie interakcji z modelem myślowym jest podobne do każdego innego żądania interakcji. W polu `model` określ jeden z [modeli z obsługą myślenia](#thinking-levels):

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Podsumowania myśli

Podsumowania myśli zawierają informacje o wewnętrznym procesie rozumowania modelu.
Domyślnie zwracane są tylko dane wyjściowe. Podsumowania myśli możesz włączyć, klikając `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

W tych przypadkach blok myśli może zawierać **tylko podpis bez podsumowania**:

- Proste żądania, w przypadku których model nie przeprowadził wystarczającego rozumowania, aby wygenerować podsumowanie.
- `thinking_summaries: "none"`, w przypadku których podsumowania są wyraźnie wyłączone.
- Niektóre typy treści, np. obrazy, mogą nie mieć podsumowań tekstowych.

Kod powinien zawsze obsługiwać bloki myśli, w których pole `summary` jest puste lub nie występuje.

## Streaming z myśleniem

Użyj przesyłania strumieniowego, aby otrzymywać przyrostowe podsumowania myśli podczas generowania.
Bloki myśli są dostarczane za pomocą zdarzeń wysyłanych przez serwer (SSE) z 2 różnymi typami zmian:

| Typ delty | Zawiera | Czas wysłania |
| --- | --- | --- |
| `thought_summary` | treści podsumowujące w formie tekstu lub obrazu; | Co najmniej 1 zmiana z przyrostowym podsumowaniem |
| `thought_signature` | Podpis kryptograficzny | ostatnia zmiana przed `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

Odpowiedź strumieniowa korzysta ze zdarzeń wysyłanych przez serwer (SSE) i składa się z kroków i zdarzeń, np.:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Kontrolowanie myślenia

Modele Gemini domyślnie stosują dynamiczne myślenie, automatycznie dostosowując poziom rozumowania do złożoności żądania. Możesz kontrolować to zachowanie za pomocą parametru `thinking_level`.

| Model | Domyślne myślenie | Obsługiwane poziomy |
| --- | --- | --- |
| gemini-3.1-pro-preview | Włączone (wysokie) | niski, średni, wysoki |
| gemini-3.1-flash-lite-image | Włączono (minimalne) | minimalna, wysoka |
| gemini-3-flash-preview | Włączone (wysokie) | minimalny, niski, średni, wysoki |
| gemini-3-pro-preview | Włączone (wysokie) | niski, wysoki |
| gemini-3.5-flash | Włączono (średni) | minimalny, niski, średni, wysoki |
| gemini-2.5-pro | Wł. | niski, średni, wysoki |
| gemini-2.5-flash | Wł. | niski, średni, wysoki |
| gemini-2.5-flash-lite | Wył. | niski, średni, wysoki |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Podpisy myśli

Sygnatury myśli to zaszyfrowane reprezentacje wewnętrznego rozumowania modelu. Muszą one zachowywać ciągłość rozumowania w interakcjach wieloetapowych.

Interfejs Interactions API znacznie upraszcza obsługę sygnatur myśli w porównaniu z interfejsem `generateContent` API.

### Tryb stanowy (zalecany)

Domyślnie, gdy używasz interfejsu API interakcji w trybie stanowym (ustawiając `store: true` i przekazując `previous_interaction_id` w kolejnych turach), serwer automatycznie zarządza stanem rozmowy, w tym wszystkimi blokami myśli i sygnaturami. W tym trybie nie musisz nic robić w związku z podpisami. Są one obsługiwane w całości po stronie serwera.

### Tryb bezstanowy

Jeśli samodzielnie zarządzasz stanem rozmowy (tryb bezstanowy) i w każdym żądaniu przekazujesz pełną historię danych wejściowych i wyjściowych:

- **MUSISZ** zawsze ponownie wysyłać wszystkie bloki `thought` dokładnie w takiej postaci, w jakiej zostały otrzymane z modelu.
- **NIE** usuwaj ani nie modyfikuj bloków myślowych z historii, ponieważ zawierają one sygnatury wymagane do dalszego wnioskowania przez model.
- Podczas przełączania modeli w ramach sesji nadal musisz ponownie wysyłać bloki myślowe poprzedniego modelu. Zgodnością zarządza backend.

## Ceny

Gdy myślenie jest włączone, cena odpowiedzi to suma tokenów wyjściowych i tokenów myślenia. Łączną liczbę wygenerowanych tokenów myślenia możesz uzyskać z pola `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

Modele myślowe generują pełne myśli, aby poprawić jakość ostatecznej odpowiedzi, a następnie wyświetlają [podsumowania](#summaries), które pozwalają zrozumieć proces myślowy. Ceny są oparte na pełnych tokenach myśli, które model musi wygenerować, mimo że interfejs API zwraca tylko podsumowanie.

Więcej informacji o tokenach znajdziesz w przewodniku [Liczba tokenów](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

## Sprawdzone metody

Skutecznie korzystaj z modeli myślowych, postępując zgodnie z tymi wskazówkami.

- **Sprawdzanie uzasadnienia:** analizuj podsumowania myśli, aby zrozumieć przyczyny niepowodzeń i ulepszać prompty.
- **Kontrolowanie budżetu na myślenie:** poproś model, aby mniej myślał w przypadku długich danych wyjściowych, aby zaoszczędzić tokeny.
- **Proste zadania:** wymagają minimalnego lub niewielkiego wysiłku umysłowego w zakresie wyszukiwania faktów lub klasyfikacji (np. „Gdzie powstała firma DeepMind?”).
- **Moderowanie zadań:** używaj domyślnego sposobu myślenia do porównywania koncepcji lub kreatywnego rozumowania (np. porównaj samochody elektryczne i hybrydowe).
- **Złożone zadania:** używaj maksymalnego poziomu myślenia w przypadku zaawansowanego kodowania, matematyki lub planowania wieloetapowego (np. rozwiązywania problemów matematycznych z AIME).

## Co dalej?

- [Generowanie tekstu:](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl) podstawowe odpowiedzi tekstowe
- [Wywoływanie funkcji:](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) łączenie z narzędziami
- [Przewodnik po Gemini 3:](https://ai.google.dev/gemini-api/docs/gemini-3?hl=pl) funkcje poszczególnych modeli

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-01 UTC."],[],[]]
