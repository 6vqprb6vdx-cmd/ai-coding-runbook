---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=pl
fetched_at: 2026-06-15T06:20:25.530806+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# Przewodnik dla deweloperów Gemini 3

Gemini 3 to nasza najinteligentniejsza rodzina modeli, która została zbudowana na bazie najnowocześniejszego rozumowania. Została zaprojektowana tak, aby realizować każdy pomysł dzięki opanowaniu przepływów pracy agentów, autonomicznego kodowania i złożonych zadań multimodalnych. Ten przewodnik zawiera najważniejsze funkcje rodziny modeli Gemini 3 i informacje o tym, jak w pełni wykorzystać jej możliwości.

[Wypróbuj wersję podglądową Gemini 3.1 Pro](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=pl)
[Wypróbuj wersję podglądową Gemini 3 Flash](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=pl)
[Wypróbuj Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=pl)
[Wypróbuj Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=pl)

Zapoznaj się z naszą [kolekcją aplikacji Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=pl), aby zobaczyć, jak model radzi sobie z zaawansowanym wnioskowaniem, autonomicznym kodowaniem i złożonymi zadaniami multimodalnymi.

Aby rozpocząć, wystarczy kilka wierszy kodu:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Poznaj serię Gemini 3

Gemini 3.1 Pro najlepiej sprawdza się w przypadku złożonych zadań, które wymagają szerokiej wiedzy o świecie i zaawansowanego wnioskowania w różnych trybach.

Gemini 3 Flash to nasz najnowszy model z serii 3, który zapewnia inteligencję na poziomie Pro przy szybkości i cenie Flash.

Nano Banana Pro (znany też jako Gemini 3 Pro Image) to nasz model do generowania obrazów o najwyższej jakości, a Nano Banana 2 (znany też jako Gemini 3.1 Flash Image) to odpowiednik o dużej wydajności i niższej cenie.

Gemini 3.1 Flash-Lite to nasz model do pracy, stworzony z myślą o niskich kosztach i dużej liczbie zadań.

| Identyfikator modelu | Okno kontekstu (wejście / wyjście) | Granica wiedzy | Ceny (dane wejściowe / wyjściowe)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 M / 64 k | Styczeń 2025 r. | 0,25 USD (tekst, obraz, film), 0,50 USD (dźwięk) / 1,50 USD |
| **gemini-3.1-flash-image-preview** | 128 tys. / 32 tys. | Styczeń 2025 r. | 0,25 USD (wpisywanie tekstu) / 0,067 USD (generowanie obrazów)\*\* |
| **gemini-3.1-pro-preview** | 1 M / 64 k | Styczeń 2025 r. | 2 USD / 12 USD (<200 tys. tokenów)   4 USD / 18 USD (>200 tys. tokenów) |
| **gemini-3-flash-preview** | 1 M / 64 k | Styczeń 2025 r. | 0,50 USD / 3 USD |
| **gemini-3-pro-image-preview** | 65 tys. / 32 tys. | Styczeń 2025 r. | 2 USD (wpisywanie tekstu) / 0,134 USD (generowanie obrazu)\*\* |

*\* Ceny dotyczą 1 miliona tokenów, chyba że zaznaczono inaczej.*
*\*\* Ceny obrazów różnią się w zależności od rozdzielczości. Szczegółowe informacje znajdziesz na [stronie z cennikiem](https://ai.google.dev/gemini-api/docs/pricing?hl=pl).*

Szczegółowe limity, cennik i dodatkowe informacje znajdziesz na [stronie modeli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl).

## Nowe funkcje interfejsu API w Gemini 3

Gemini 3 wprowadza nowe parametry, które zapewniają deweloperom większą kontrolę nad latencją, kosztami i wiernością multimodalną.

### Poziom myślenia

Modele z serii Gemini 3 domyślnie korzystają z myślenia dynamicznego, aby analizować prompty. Możesz użyć parametru `thinking_level`, który kontroluje **maksymalną** głębokość wewnętrznego procesu rozumowania modelu przed wygenerowaniem odpowiedzi. Gemini 3 traktuje te poziomy jako względne limity myślenia, a nie ścisłe gwarancje tokenów.

Jeśli nie podasz wartości `thinking_level`, Gemini 3 domyślnie przyjmie wartość `high`. Aby uzyskać szybsze odpowiedzi o mniejszych opóźnieniach, gdy nie jest wymagane złożone rozumowanie, możesz ograniczyć poziom myślenia modelu do `low`.

| Poziom myślenia | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Opis |
| --- | --- | --- | --- | --- |
| **`minimal`** | Nieobsługiwane | Obsługiwane (domyślnie) | Obsługiwane | W przypadku większości zapytań odpowiada ustawieniu „bez myślenia”. W przypadku złożonych zadań związanych z kodowaniem model może myśleć w bardzo ograniczonym zakresie. Minimalizuje opóźnienia w przypadku aplikacji do czatu lub aplikacji o wysokiej przepustowości. Pamiętaj, że `minimal` nie gwarantuje, że myślenie jest wyłączone. |
| **`low`** | Obsługiwane | Obsługiwane | Obsługiwane | Minimalizuje opóźnienie i koszty. Najlepiej sprawdza się w przypadku prostych instrukcji, czatów i aplikacji o wysokiej przepustowości. |
| **`medium`** | Obsługiwane | Obsługiwane | Obsługiwane | Zrównoważone myślenie w przypadku większości zadań. |
| **`high`** | Obsługiwane (domyślne, dynamiczne) | Obsługiwane (dynamiczne) | Obsługiwane (domyślne, dynamiczne) | Zwiększa głębokość rozumowania. Model może potrzebować znacznie więcej czasu, aby wygenerować pierwszy token wyjściowy (niebędący tokenem myślenia), ale wynik będzie bardziej przemyślany. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Rozdzielczość multimediów

Gemini 3 wprowadza szczegółową kontrolę nad przetwarzaniem obrazu multimodalnego za pomocą parametru `media_resolution`. Wyższe rozdzielczości zwiększają zdolność modelu do odczytywania drobnego tekstu lub rozpoznawania małych szczegółów, ale zwiększają wykorzystanie tokenów i opóźnienia.
Parametr `media_resolution` określa **maksymalną liczbę tokenów
przydzielonych do każdego obrazu wejściowego lub klatki filmu**.

Możesz teraz ustawić rozdzielczość na `media_resolution_low`, `media_resolution_medium`, `media_resolution_high` lub `media_resolution_ultra_high` dla poszczególnych treści nagranych lub globalnie (za pomocą parametru `generation_config`, który nie jest dostępny w przypadku rozdzielczości ultra high). Jeśli nie określisz rozdzielczości, model użyje optymalnych ustawień domyślnych na podstawie typu zawartości.

**Zalecane ustawienia**

| Typ mediów | Zalecane ustawienie | Maksymalna liczba tokenów | Wytyczne dotyczące użytkowania |
| --- | --- | --- | --- |
| **Obrazy** | `media_resolution_high` | 1120 | Zalecane w przypadku większości zadań związanych z analizą obrazów, aby zapewnić maksymalną jakość. |
| **Pliki PDF** | `media_resolution_medium` | 560 | Optymalny do analizy dokumentów; jakość zwykle osiąga maksymalny poziom przy wartości `medium`. Zwiększenie do `high` rzadko poprawia wyniki OCR w przypadku standardowych dokumentów. |
| **Wideo** (ogólne) | `media_resolution_low` (lub `media_resolution_medium`) | 70 (na klatkę) | **Uwaga:** w przypadku filmów ustawienia `low` i `medium` są traktowane identycznie (70 tokenów), aby zoptymalizować wykorzystanie kontekstu. Jest to wystarczające w przypadku większości zadań związanych z rozpoznawaniem i opisywaniem działań. |
| **Film** (z dużą ilością tekstu) | `media_resolution_high` | 280 (na klatkę) | Wymagane tylko wtedy, gdy przypadek użycia obejmuje odczytywanie gęstego tekstu (OCR) lub drobnych szczegółów w klatkach wideo. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Temperatura

W przypadku wszystkich modeli Gemini 3 zdecydowanie zalecamy pozostawienie parametru temperatury na domyślnej wartości `1.0`.

W przypadku poprzednich modeli dostosowywanie temperatury często pomagało kontrolować kreatywność i determinizm, ale w przypadku Gemini 3 funkcje rozumowania są zoptymalizowane pod kątem ustawienia domyślnego. Zmiana temperatury (ustawienie poniżej 1,0) może prowadzić do nieoczekiwanych zachowań, takich jak zapętlanie lub pogorszenie wydajności, szczególnie w przypadku złożonych zadań matematycznych lub wymagających rozumowania.

### Podpisy myśli

Gemini 3 używa [sygnatur myśli](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pl), aby zachować kontekst rozumowania w wywołaniach interfejsu API. Są to zaszyfrowane reprezentacje wewnętrznego procesu myślowego modelu. Aby model zachował swoje możliwości rozumowania, musisz zwrócić te sygnatury do modelu w żądaniu dokładnie w takiej postaci, w jakiej zostały otrzymane:

- **Wywoływanie funkcji (ścisłe):** interfejs API wymusza ścisłą weryfikację w przypadku „bieżącej tury”. Brakujące podpisy spowodują błąd 400.
- **Tekst/czat:** weryfikacja nie jest ściśle egzekwowana, ale pominięcie sygnatur obniży jakość rozumowania i odpowiedzi modelu.
- **Generowanie/edytowanie obrazów (ścisłe):** interfejs API wymusza ścisłą weryfikację wszystkich części modelu, w tym `thoughtSignature`. Brakujące podpisy spowodują błąd 400.

#### Wywoływanie funkcji (ścisła weryfikacja)

Gdy Gemini generuje `functionCall`, korzysta z `thoughtSignature`, aby prawidłowo przetworzyć dane wyjściowe narzędzia w następnej turze. „Obecna tura” obejmuje wszystkie kroki wykonane przez model (`functionCall`) i użytkownika (`functionResponse`) od ostatniej standardowej wiadomości **użytkownika** `text`.

- **Pojedyncze wywołanie funkcji:** część `functionCall` zawiera sygnaturę. Musisz go zwrócić.
- **Równoległe wywołania funkcji:** tylko pierwsza część `functionCall` na liście będzie zawierać sygnaturę. Musisz zwrócić części w dokładnie takiej samej kolejności, w jakiej zostały otrzymane.
- **Wielokrokowe (sekwencyjne):** jeśli model wywołuje narzędzie, otrzymuje wynik i wywołuje *inne* narzędzie (w ramach tej samej tury), **oba** wywołania funkcji mają sygnatury. Musisz zwrócić **wszystkie** zgromadzone sygnatury w historii.

#### Tekst i streaming

W przypadku standardowego czatu lub generowania tekstu obecność podpisu nie jest gwarantowana.

- **Non-Streaming**: ostatnia część treści odpowiedzi może zawierać znak `thoughtSignature`, ale nie zawsze jest on obecny. Jeśli zostanie zwrócony, należy go odesłać, aby zachować najwyższą skuteczność.
- **Streaming:** jeśli sygnatura zostanie wygenerowana, może pojawić się w ostatnim bloku, który zawiera pustą część tekstową. Upewnij się, że parser strumienia sprawdza sygnatury nawet wtedy, gdy pole tekstowe jest puste.

#### Generowanie i edytowanie obrazów

W przypadku `gemini-3-pro-image-preview` i `gemini-3.1-flash-image-preview` podpisy myślowe mają kluczowe znaczenie w edytowaniu w trybie konwersacyjnym. Gdy poprosisz model o zmodyfikowanie obrazu, będzie on korzystać z `thoughtSignature` z poprzedniej tury, aby zrozumieć kompozycję i logikę oryginalnego obrazu.

- **Edytowanie:** podpisy są gwarantowane w pierwszej części po przemyśleniach w odpowiedzi (`text` lub `inlineData`) i w każdej kolejnej części `inlineData`. Aby uniknąć błędów, musisz zwrócić wszystkie te podpisy.

#### Przykłady kodu

#### Wieloetapowe wywoływanie funkcji (sekwencyjne)

Użytkownik zadaje pytanie wymagające wykonania 2 osobnych czynności (sprawdzenie lotu –> rezerwacja taksówki) w jednym kroku.   
  
**Krok 1. Model wywołuje narzędzie do wyszukiwania lotów.**  
Model zwraca sygnaturę `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Krok 2. Użytkownik wysyła wynik wyszukiwania lotu**  
Aby zachować tok myślenia modelu, musimy odesłać `<Sig_A>`.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Krok 3. Model wywołuje narzędzie do zamawiania taksówek**  
Model zapamiętuje opóźnienie lotu za pomocą `<Sig_A>` i decyduje się zamówić taksówkę. Wygeneruje to *nowy* podpis `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Krok 4. Użytkownik wysyła wynik taksówki**  
Aby zakończyć turę, musisz odesłać cały łańcuch: `<Sig_A>` I `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Równoległe wywoływanie funkcji

Użytkownik pyta: „Sprawdź pogodę w Paryżu i Londynie”. Model zwraca 2 wywołania funkcji w jednej odpowiedzi.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Tekst/uzasadnienie w kontekście (bez weryfikacji)

Użytkownik zadaje pytanie, które wymaga wnioskowania w kontekście bez użycia narzędzi zewnętrznych. Chociaż nie jest to ściśle weryfikowane, dołączenie podpisu pomaga modelowi utrzymać ciąg rozumowania w przypadku pytań uzupełniających.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Generowanie i edytowanie obrazów

W przypadku generowania obrazów podpisy są ściśle weryfikowane. Wyświetlają się w **pierwszej części** (tekst lub obraz) i **wszystkich kolejnych częściach obrazu**. Wszystkie muszą zostać zwrócone w następnej turze.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Migracja z innych modeli

Jeśli przenosisz ślad rozmowy z innego modelu (np. Gemini 2.5) lub wstawiasz niestandardowe wywołanie funkcji, które nie zostało wygenerowane przez Gemini 3, nie będziesz mieć prawidłowego podpisu.

Aby pominąć ścisłą weryfikację w tych konkretnych scenariuszach, wypełnij pole tym konkretnym ciągiem znaków: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Uporządkowane dane wyjściowe z narzędziami

Modele Gemini 3 umożliwiają łączenie [danych wyjściowych o ustrukturyzowanej formie](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl) z wbudowanymi narzędziami, takimi jak [powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl), [kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl), [wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) i [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Generowanie obrazów

Gemini 3.1 Flash Image i Gemini 3 Pro Image umożliwiają generowanie i edytowanie obrazów na podstawie promptów tekstowych. Wykorzystuje rozumowanie, aby „przemyśleć” prompt, i może pobierać dane w czasie rzeczywistym, takie jak prognozy pogody czy wykresy giełdowe, a następnie korzystać z [wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl), aby generować obrazy o wysokiej jakości.

**Nowe i ulepszone funkcje:**

- **Renderowanie tekstu i rozdzielczość 4K:** generuj wyraźny i czytelny tekst oraz diagramy w rozdzielczości do 2K i 4K.
- **Generowanie na podstawie źródeł:** użyj `google_search` narzędzia, aby weryfikować fakty i generować obrazy na podstawie informacji ze świata rzeczywistego. Powiązanie ze źródłem informacji przy użyciu wyszukiwarki *grafiki* Google jest dostępne w przypadku Gemini 3.1 Flash Image.
- **Edytowanie w trybie konwersacyjnym:** wieloetapowa edycja obrazów za pomocą prostych poleceń (np. „Zmień tło na zachód słońca”). Ten przepływ pracy wykorzystuje **sygnatury myśli**, aby zachować kontekst wizualny między turami.

Szczegółowe informacje o proporcjach obrazu, przepływach pracy związanych z edycją i opcjach konfiguracji znajdziesz w [przewodniku po generowaniu obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**Przykładowa odpowiedź**

![Pogoda w Tokio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=pl)

### Wykonywanie kodu z obrazami

Gemini 3 Flash może traktować wizję jako aktywne badanie, a nie tylko statyczne spojrzenie. Łącząc rozumowanie z [wykonywaniem kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl), model formułuje plan, a następnie pisze i wykonuje kod w Pythonie, aby krok po kroku powiększać, przycinać, dodawać adnotacje lub w inny sposób manipulować obrazami, aby wizualnie uzasadnić swoje odpowiedzi.

**Możesz na przykład:**

- **Powiększanie i sprawdzanie:** model automatycznie wykrywa, kiedy szczegóły są zbyt małe (np. odczytywanie odległego wskaźnika lub numeru seryjnego) i generuje kod, aby przyciąć i ponownie zbadać obszar w wyższej rozdzielczości.
- **Wizualne obliczenia matematyczne i wykresy:** model może wykonywać wieloetapowe obliczenia za pomocą kodu (np. sumować pozycje na paragonie lub generować wykres Matplotlib na podstawie wyodrębnionych danych).
- **Adnotacje do obrazów:** model może rysować strzałki, ramki ograniczające lub inne adnotacje bezpośrednio na obrazach, aby odpowiadać na pytania dotyczące przestrzeni, np. „Gdzie powinien znajdować się ten produkt?”.

Aby włączyć myślenie wizualne, skonfiguruj [wywoływanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) jako narzędzie. W razie potrzeby model automatycznie użyje kodu do manipulowania obrazami.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Więcej informacji o wykonywaniu kodu z obrazami znajdziesz w sekcji [Wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl#images).

### Odpowiedzi funkcji multimodalnych

[Wywoływanie funkcji multimodalnych](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#multimodal)
umożliwia użytkownikom uzyskiwanie odpowiedzi funkcji zawierających
obiekty multimodalne, co pozwala na lepsze wykorzystanie możliwości wywoływania funkcji
modelu. Standardowe wywołanie funkcji obsługuje tylko odpowiedzi funkcji oparte na tekście:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Łączenie wbudowanych narzędzi i wywoływania funkcji

Gemini 3 umożliwia korzystanie z wbudowanych narzędzi (takich jak wyszukiwarka Google, kontekst adresu URL i [inne](https://ai.google.dev/gemini-api/docs/tools?hl=pl)) oraz niestandardowych narzędzi do [wywoływania funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) w ramach tego samego wywołania interfejsu API, co pozwala na bardziej złożone przepływy pracy. Więcej informacji znajdziesz na stronie [kombinacje narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## Przenoszenie danych z Gemini 2.5

Gemini 3 to nasza najbardziej zaawansowana rodzina modeli, która zapewnia stopniową poprawę w porównaniu z Gemini 2.5. Podczas migracji weź pod uwagę te kwestie:

- **Model myślący:** jeśli wcześniej używasz złożonych promptów (np. łańcucha myśli), aby zmusić Gemini 2.5 do wyciągania wniosków, wypróbuj Gemini 3 z `thinking_level: "high"` i uproszczonymi promptami.
- **Ustawienia temperatury:** jeśli Twój dotychczasowy kod wyraźnie ustawia temperaturę (zwłaszcza na niskie wartości w przypadku deterministycznych wyników), zalecamy usunięcie tego parametru i użycie domyślnej wartości 1,0 w przypadku Gemini 3, aby uniknąć potencjalnych problemów z zapętlaniem lub pogorszenia wydajności w przypadku złożonych zadań.
- **Rozumienie plików PDF i dokumentów:** jeśli w przypadku analizowania dokumentów o dużej gęstości informacji korzystasz z określonego działania, przetestuj nowe ustawienie `media_resolution_high`, aby zapewnić dalszą dokładność.
- **Zużycie tokenów:** przejście na domyślne ustawienia Gemini 3 może **zwiększyć** zużycie tokenów w przypadku plików PDF, ale **zmniejszyć** zużycie tokenów w przypadku filmów. Jeśli żądania przekraczają teraz okno kontekstu z powodu wyższych domyślnych rozdzielczości, zalecamy wyraźne zmniejszenie rozdzielczości multimediów.
- **Segmentacja obrazu:** funkcje segmentacji obrazu (zwracanie masek obiektów na poziomie pikseli) nie są obsługiwane w modelach Gemini 3 Pro ani Gemini 3 Flash. W przypadku zadań wymagających natywnej segmentacji obrazu zalecamy dalsze korzystanie z modelu Gemini 2.5 Flash z wyłączoną funkcją modelu myślącego lub z modelu [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pl).
- **Korzystanie z komputera:** Gemini 3 Pro i Gemini 3 Flash obsługują [korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl). W przeciwieństwie do serii 2.5 nie musisz używać osobnego modelu, aby uzyskać dostęp do narzędzia Computer Use.
- **Obsługa narzędzi:** [łączenie wbudowanych narzędzi z wywoływaniem funkcji](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl) jest teraz obsługiwane w przypadku modeli Gemini 3. [Uziemienie w Mapach](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl) jest teraz obsługiwane również w przypadku modeli Gemini 3.
- **Liczba kandydatów:** modele Gemini 3 nie obsługują `candidateCount > 1`.
  Ustawienie tego parametru na wartość większą niż `1` spowoduje zwrócenie błędu 400.

## Zgodność z OpenAI

W przypadku użytkowników korzystających z [warstwy zgodności OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl) standardowe parametry (`reasoning_effort` OpenAI) są automatycznie mapowane na odpowiedniki w Gemini (`thinking_level`).

## Sprawdzone metody dotyczące promptów

Gemini 3 to model rozumowania, który zmienia sposób, w jaki należy formułować prompty.

- **Precyzyjne instrukcje:** używaj zwięzłych promptów. Gemini 3 najlepiej reaguje na bezpośrednie i jasne instrukcje. Może nadmiernie analizować rozbudowane lub zbyt złożone techniki tworzenia promptów, które były używane w przypadku starszych modeli.
- **Poziom szczegółowości odpowiedzi:** domyślnie Gemini 3 jest mniej rozbudowany i woli udzielać bezpośrednich, zwięzłych odpowiedzi. Jeśli Twój przypadek użycia wymaga bardziej konwersacyjnej lub „gadatliwej” osobowości, musisz wyraźnie nakierować model w prompcie (np. „Wyjaśnij to jako przyjazny, rozmowny asystent”).
- **Zarządzanie kontekstem:** podczas pracy z dużymi zbiorami danych (np. całymi książkami, bazami kodu lub długimi filmami) umieszczaj konkretne instrukcje lub pytania na końcu promptu, po kontekście danych. Zakotwicz rozumowanie modelu w dostarczonych danych, zaczynając pytanie od frazy takiej jak „Na podstawie powyższych informacji…”.

Więcej informacji o strategiach projektowania promptów znajdziesz w [przewodniku po inżynierii promptów](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl).

## Najczęstsze pytania

1. **Jaka jest granica wiedzy w przypadku Gemini 3?** Modele Gemini 3 mają granicę wiedzy w styczniu 2025 r. Aby uzyskać najnowsze informacje, skorzystaj z narzędzia [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=pl).
2. **Jakie są limity okna kontekstu?** Modele Gemini 3 obsługują okno kontekstu o pojemności 1 miliona tokenów i do 64 tys. tokenów wyjściowych.
3. **Czy jest dostępny bezpłatny poziom Gemini 3?** Gemini 3 Flash`gemini-3-flash-preview` i 3.1 Flash-Lite`gemini-3.1-flash-lite` mają bezpłatne poziomy w Gemini API. Możesz bezpłatnie wypróbować Gemini 3.1 Pro i 3 Flash w Google AI Studio, ale w Gemini API nie ma bezpłatnego poziomu dla`gemini-3.1-pro-preview`.
4. **Czy mój stary kod `thinking_budget` będzie nadal działać?** Tak, `thinking_budget` jest nadal obsługiwane ze względu na zgodność z wcześniejszymi rozwiązaniami, ale zalecamy przejście na `thinking_level`, aby uzyskać bardziej przewidywalną skuteczność. Nie używaj obu tych parametrów w tym samym żądaniu.
5. **Czy Gemini 3 obsługuje interfejs Batch API?** Tak, Gemini 3 obsługuje [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl).
6. **Czy buforowanie kontekstu jest obsługiwane?** Tak, [pamięć podręczna kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl) jest obsługiwana w przypadku Gemini 3.
7. **Które narzędzia są obsługiwane w Gemini 3?** Gemini 3 obsługuje [wyszukiwarkę Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl), [powiązanie ze źródłem informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl), [wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl), [wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) i [kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl). Obsługuje też standardowe [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) w przypadku własnych narzędzi niestandardowych i [w połączeniu z narzędziami wbudowanymi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).
8. **Czym jest `gemini-3.1-pro-preview-customtools`?** Jeśli używasz modelu `gemini-3.1-pro-preview`, a on ignoruje Twoje niestandardowe narzędzia na rzecz poleceń bash, spróbuj użyć modelu `gemini-3.1-pro-preview-customtools`. Więcej informacji znajdziesz [tutaj](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl#gemini-31-pro-preview-customtools).

## Dalsze kroki

- Pierwsze kroki z [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=pl#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- Zapoznaj się z przewodnikiem Cookbook dotyczącym [poziomów myślenia](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=pl#gemini3) i przejścia z budżetu na myślenie na poziomy myślenia.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-04 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-04 UTC."],[],[]]
