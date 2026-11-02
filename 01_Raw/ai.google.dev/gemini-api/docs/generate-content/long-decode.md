---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=pl
fetched_at: 2026-11-02T07:11:46.041495+00:00
title: "D\u0142ugie dekodowanie \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# Długie dekodowanie

Długie dekodowanie pozwala Gemini 4 Argon generować odpowiedzi przekraczające limit danych wyjściowych dla pojedynczego żądania w przypadku zadań wymagających głębokiego rozumowania, aż do osiągnięcia limitu ujednoliconego okna kontekstowego o rozmiarze 1 mln tokenów (1 048 576 tokenów współdzielonych między dane wejściowe, rozumowanie i dane wyjściowe).

Sama zmiana identyfikatora modelu nie umożliwia długiego dekodowania. Bez dodatkowej konfiguracji dane wyjściowe zatrzymują się na 64 tys. tokenów w przypadku wywołań strumieniowych i 32 tys. tokenów w przypadku wywołań niestreamingowych. Najszybszym sposobem na włączenie długiego dekodowania jest uaktualnienie pakietu Google GenAI SDK i ustawienie wartości `max_output_tokens` większej niż 65 536. Z tego przewodnika dowiesz się, jak działa długie dekodowanie, kiedy go używać i jak włączyć tę funkcję za pomocą `generateContent`.

## Jak długo działa dekodowanie

Pojedyncze żądanie przesyłania strumieniowego lub żądanie pakietu SDK generuje do 64 tys. tokenów, a żądanie REST bez przesyłania strumieniowego generuje do 32 tys. tokenów. Gdy odpowiedź wymaga większej liczby tokenów, model generuje ją w ramach wielu etapów żądania i odpowiedzi, z których każdy jest kontynuacją poprzedniego.

- **Ujednolicony limit tokenów wejściowych i wyjściowych:** tokeny wejściowe, tokeny związane z myśleniem, wywołania funkcji i ostateczna odpowiedź mieszczą się w jednym oknie o wielkości 1 mln tokenów. Dane wyjściowe mogą wykorzystywać do 1 048 576 tokenów pomniejszonych o liczbę tokenów wejściowych.
- **Limit dla każdego przeskoku:** jeden przeskok zwraca maksymalnie 65 536 tokenów wyjściowych. Żądania REST bez strumieniowania zwracają do 32 768 tokenów.
- **Sygnał kontynuacji:** jeśli model osiągnie limit i pozostaną mu tokeny, odpowiedź kończy się symbolem `finish_reason: CONTINUATION` i `continuation_token`.
- **Następna brama:** klient ponownie wysyła to samo żądanie z tokenem. Model będzie kontynuował od miejsca, w którym się zatrzymał.
- **Łączna liczba tokenów dla wszystkich przeskoków:** `max_output_tokens` ustawia łączną liczbę tokenów wymagających myślenia i tokenów wyjściowych dla wszystkich przeskoków.
- **Sygnał zatrzymania:** gdy model wykorzysta wszystkie `max_output_tokens`, odpowiedź kończy się znakiem `finish_reason: MAX_TOKENS`.

W przypadku trudnych problemów krok może wykorzystać wszystkie tokeny na wewnętrzne rozważania i zwrócić pusty tekst z symbolem `continuation_token`. Jest to normalne, a ostateczna odpowiedź pojawia się w późniejszych przeskokach.

## Domyślne limity danych wyjściowych

Bez długiego dekodowania pojedyncze żądanie zatrzymuje się na tych limitach na żądanie:

- **Żądania strumieniowe i niestrumieniowe wysyłane za pomocą pakietu Google GenAI SDK (`generate_content`):** domyślnie 64 tys. tokenów wyjściowych.
- **Bezpośrednie wywołania REST bez strumieniowania (`generateContent`):** domyślnie 32 tys. tokenów wyjściowych. Ustawienie `max_output_tokens` na wartość większą niż 32 768 w przypadku wywołania REST bez strumieniowania i bez `continuation_token` zwraca błąd `400`.

| Sposób wywoływania modelu | Limit danych wyjściowych bez długiego dekodowania | Długie dekodowanie przy uruchamianiu | Co zrobić |
| --- | --- | --- | --- |
| Google GenAI SDK, najnowsza wersja | 64 KB | Tak, pakiet SDK będzie nadal działać. | Ustaw `max_output_tokens`. |
| Pakiet SDK Google GenAI, starsza wersja, bez strumieniowania | 64 KB | Nie | Uaktualnij pakiet SDK. |
| REST `streamGenerateContent` | 64 KB | Tak, z własną pętlą | Napisz pętlę. Zobacz [Opcję 2](#option-2-loop). |
| REST `generateContent` | 32 tys. | Tak, z własną pętlą | Napisz pętlę. Zobacz [opcję 2](#option-2-loop). |

## Kiedy używać długiego dekodowania

Większość żądań mieści się w limicie pojedynczego żądania (64 tys. tokenów w przypadku wywołań przesyłania strumieniowego i pakietu SDK lub 32 tys. tokenów w przypadku wywołań REST bez przesyłania strumieniowego). Używaj długiego dekodowania, gdy odpowiedź wymaga więcej połączonych tokenów myślenia i wyjściowych, niż pozwala na to pojedyncze żądanie. Zwiększenie wartości `max_output_tokens` daje modelowi większe możliwości rozumowania w przypadku trudnych problemów, zamiast wydłużać standardowe odpowiedzi.

| Zbiór zadań | Użyć długiego dekodowania? | Dlaczego |
| --- | --- | --- |
| Trudne zadania matematyczne, naukowe, badawcze i formalne dowody | Tak | Model może wykorzystać ponad 64 tys. tokenów, aby przeanalizować i sprawdzić swoje rozumowanie. |
| Najtrudniejsze zadania związane z kodowaniem i agentami | Tak | Niektóre zadania wymagają więcej niż 64 tys. tokenów myślenia i kodu w jednej odpowiedzi. Większość zadań związanych z kodowaniem i agentowych kończy się poniżej 64 tys. tokenów. |
| Zestawy do oceny, które zatrzymują się po osiągnięciu limitu danych wyjściowych | Tak | Długie dekodowanie zapobiega ucinaniu odpowiedzi, gdy model poświęca całe żądanie o wielkości 64 tys. lub 32 tys. tokenów na myślenie. |
| Czat, pytania i odpowiedzi, podsumowywanie, klasyfikacja i wyodrębnianie | Nie | Te zadania są wykonywane przy użyciu znacznie mniejszej liczby tokenów niż 32 tys. |
| prośby o określoną długość, np. „napisz książkę o objętości 700 tys. słów”; | Nie | Model nie przestrzega docelowej długości. |
| Agenty, które wywołują narzędzia w wielu krótkich turach | Nie | Każda tura jest krótka. Duże dane wyjściowe w każdej turze szybko wypełniają ujednolicone okno danych wejściowych i wyjściowych o wielkości 1 mln. |
| Prompty zbliżające się do limitu 1 mln tokenów wejściowych | Nie | Dane wyjściowe mogą wykorzystywać tylko 1 mln minus dane wejściowe. |
| Żądania wrażliwe na opóźnienia | Nie | Długie dekodowanie może potrwać kilka minut. |

Ustawienie wysokiej wartości `max_output_tokens` daje modelowi możliwość dłuższego zastanawiania się nad trudnymi problemami, ale model nadal decyduje, ile napisać. Aby kontrolować, ile wysiłku model wkłada w rozumowanie, ustaw parametr [`thinking_level`](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=pl).

## Włączanie długiego dekodowania

Możesz uruchomić długie dekodowanie automatycznie za pomocą pakietu Google GenAI SDK (opcja 1, zalecana w przypadku większości aplikacji) lub napisać własną pętlę kontynuacji (opcja 2). Obie opcje obsługują pełne okno kontekstu o wielkości 1 mln tokenów.

|  | Opcja 1. Pakiet SDK Google GenAI (zalecana) | Opcja 2. Własna pętla strumieniowa | Opcja 2. Własna pętla bez strumieniowania |
| --- | --- | --- | --- |
| **Kto rozpoczyna każdy skok** | pakiet SDK, Ustawiono: `max_output_tokens`. | kod w każdym punkcie kontrolnym lub po przerwaniu strumienia; | Twój kod, co 32 tys. tokenów |
| **Tokeny na żądanie** | 64 KB na przeskok | 64 tys. tokenów na strumień, z punktem kontrolnym co 5 tys. tokenów po przekroczeniu 32 tys. | 32 tys. na żądanie |
| **Limit czasu na żądanie** | 20 minut | 20 minut | 20 minut |
| **Miejsce na dane** | Brak miejsca na dane na serwerze | Brak miejsca na dane na serwerze | Brak miejsca na dane na serwerze |
| **Najlepsze zastosowania** | Większość aplikacji | wywołania REST i niestandardowe zestawy testowe, które przesyłają strumieniowo; | Proste platformy do oceny |

Zaszyfrowany `continuation_token` przenosi stan modelu między żądaniami, więc na serwerze nic nie jest przechowywane.

### Opcja 1. Użyj pakietu Google GenAI SDK (zalecane)

W najnowszym pakiecie Google GenAI SDK funkcja `automatic_continuation` jest domyślnie włączona zarówno w przypadku wywołań strumieniowych, jak i niestrumieniowych, więc nie musisz jej ustawiać. Jeśli ustawisz parametr `max_output_tokens` powyżej limitu na żądanie, pakiet SDK automatycznie wykona skoki kontynuacji i zwróci jedną połączoną odpowiedź.

1. Uaktualnij pakiet SDK.

   ### Python

   ```
   pip install -U "google-genai>=2.30.1"
   ```

   ### JavaScript

   ```
   npm install "@google/genai@>=2.29.1"
   ```
2. Ustaw `max_output_tokens` na wartość większą niż 65 536.

   ### Python

   ```
   from google import genai
   from google.genai import types

   client = genai.Client()  # Reads GEMINI_API_KEY

   response = client.models.generate_content(
       model="gemini-4-argon",
       contents="Write a complete, rigorous proof of the prime number theorem.",
       config=types.GenerateContentConfig(
           max_output_tokens=262_144,  # Total thinking and output for all hops
           thinking_config=types.ThinkingConfig(thinking_level="high"),
           automatic_continuation=True,  # Default. Shown for clarity.
       ),
   )

   print(response.text)
   print("Finish reason:", response.candidates[0].finish_reason)
   print("Prompt size:", response.usage_metadata.initial_prompt_token_count)
   print("Billed tokens:", response.usage_metadata.total_token_count)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI, ThinkingLevel } from "@google/genai";

   const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY

   const response = await ai.models.generateContent({
     model: "gemini-4-argon",
     contents: "Write a complete, rigorous proof of the prime number theorem.",
     config: {
       maxOutputTokens: 262144, // Total thinking and output for all hops
       thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
       automaticContinuation: true, // Default. Shown for clarity.
     },
   });

   console.log(response.text);
   console.log("Finish reason:", response.candidates?.[0]?.finishReason);
   console.log("Prompt size:", response.usageMetadata?.initialPromptTokenCount);
   console.log("Billed tokens:", response.usageMetadata?.totalTokenCount);
   ```

Pamiętaj, że:

- **Strumieniowanie:** `generate_content_stream` (Python) i `generateContentStream` (JavaScript) również będą kontynuowane. Jeśli strumień zostanie przerwany po punkcie kontrolnym, pakiet SDK wznowi działanie od tego punktu.
- **Limity czasu:** limity czasu i ponowne próby dotyczą każdego przeskoku, a nie całego uruchomienia.
- **Sterowanie ręczne:** aby samodzielnie uruchomić pętlę, ustaw `automatic_continuation=False` (Python) lub `automaticContinuation: false` (JavaScript). Następnie wykonaj czynności opisane w sekcji Opcja 2.
- **Wykorzystanie:** pola wykorzystania pokazują sumę wszystkich przeskoków. Aby sprawdzić rozmiar prompta, przeczytaj `initial_prompt_token_count`. Zobacz [Zliczanie tokenów](#count-tokens).

### Opcja 2. Napisz własną pętlę

Jeśli wywołujesz REST bezpośrednio, używasz języka bez najnowszego pakietu SDK lub potrzebujesz pełnej kontroli, napisz własną pętlę. Możesz też zapoznać się z implementacjami pakietu Google GenAI SDK w [Pythonie](https://github.com/googleapis/python-genai/blob/v2.30.1/google/genai/models.py#L6111) i [JavaScript/TypeScript](https://github.com/googleapis/js-genai/blob/v2.29.1/src/models.ts#L88).

Przestrzegaj tych zasad:

1. **Wysyłaj to samo żądanie przy każdym przeskoku.** Prześlij oryginalne wartości `contents`, `system_instruction`, `tools` i `generation_config`. Zachowaj wartość `max_output_tokens`.
2. **Nie dodawaj częściowych danych wyjściowych do `contents`.** `continuation_token` zawiera stan modelu, w tym jego proces myślowy.
3. **Wysyłaj tylko najnowszy token.** Każdy token zawiera wszystkie wcześniejsze postępy.
4. **Kontynuuj, gdy `finish_reason` jest `CONTINUATION`.** Zatrzymaj w przypadku innego powodu zakończenia.
5. **Połącz części po ostatnim przeskoku.** Połącz części ze wszystkich przeskoków w jedną turę modelu w historii rozmów.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()  # Reads GEMINI_API_KEY
PROMPT = "Write a complete, rigorous proof of the prime number theorem."
parts = []
token = None

while True:
    response = client.models.generate_content(
        model="gemini-4-argon",
        contents=PROMPT,  # The original contents on every request
        config=types.GenerateContentConfig(
            max_output_tokens=262_144,  # The same total on every request
            thinking_config=types.ThinkingConfig(thinking_level="high"),
            automatic_continuation=False,  # You run the loop
            continuation_token=token,
        ),
    )
    candidate = response.candidates[0]
    if candidate.content and candidate.content.parts:
        parts.extend(candidate.content.parts)
    token = candidate.continuation_token
    if candidate.finish_reason != types.FinishReason.CONTINUATION or not token:
        break

print("".join(p.text for p in parts if p.text and not p.thought))
print("Finish reason:", candidate.finish_reason)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY
const PROMPT = "Write a complete, rigorous proof of the prime number theorem.";
const parts = [];
let token = undefined;
let candidate = undefined;

while (true) {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: PROMPT, // The original contents on every request
    config: {
      maxOutputTokens: 262144, // The same total on every request
      thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
      automaticContinuation: false, // You run the loop
      continuationToken: token,
    },
  });
  candidate = response.candidates?.[0];
  if (candidate?.content?.parts) {
    parts.push(...candidate.content.parts);
  }
  token = candidate?.continuationToken;
  if (candidate?.finishReason !== "CONTINUATION" || !token) {
    break;
  }
}

console.log(parts.filter((p) => p.text && !p.thought).map((p) => p.text).join(""));
console.log("Finish reason:", candidate?.finishReason);
```

### REST

```
# Hop 1: send the request with max_output_tokens.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    }
  }'

# Hop 2: if finishReason is CONTINUATION, send the same request plus the token.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    },
    "continuationToken": "TOKEN_FROM_HOP_1"
  }'
```

Przeskok poświęcony wyłącznie na myślenie zwraca pusty obiekt `text` z `finishReason: "CONTINUATION"`. Potraktuj to jako normalny postęp i poproś o następny przeskok:

```
{
  "candidates": [{
    "content": {"role": "model", "parts": [{"text": ""}]},
    "finishReason": "CONTINUATION",
    "continuationToken": "CiQ4ZmQ3..."
  }],
  "usageMetadata": {
    "promptTokenCount": 142,
    "candidatesTokenCount": 0,
    "thoughtsTokenCount": 32768,
    "totalTokenCount": 32910
  }
}
```

**Pętle strumieniowania** wymagają jeszcze 1 reguły. Po pierwszych 32 768 tokenach strumień wysyła token punktu kontrolnego co 5000 tokenów. Zachowaj nowe fragmenty na liście oczekujących. Gdy fragment ma wartość `continuation_token`, przenieś oczekujące fragmenty do zatwierdzonych danych wyjściowych i zapisz token. Jeśli strumień zostanie przerwany, odrzuć oczekujące fragmenty i wznów od ostatniego tokena. Jeśli strumień zostanie przerwany przed pierwszym punktem kontrolnym, ponownie wyślij pierwotne żądanie.

## Zestaw `max_output_tokens`

`max_output_tokens` określa łączny limit myślenia i danych wyjściowych we wszystkich etapach. Zmniejszenie tej wartości nie sprawi, że model będzie myślał bardziej zwięźle, ale spowoduje, że odpowiedź zostanie szybciej przerwana.

| Twoje zadanie | Zalecane okno konwersji: `max_output_tokens` |
| --- | --- |
| aplikacji, które są już dostępne i mają limit niższy niż 32 tys. znaków; | Zwiększ ją do 32 768. |
| Długie zadania związane z kodowaniem i zadania agentowe | Zacznij od 65 536. |
| Trudne zadania z matematyki i nauk ścisłych, badania i dowody | Przetestuj wartości od 262 144 do 1 048 576 minus tokeny wejściowe. |

Aby użyć mniejszej liczby tokenów, zmniejsz wartość `thinking_level`. W przypadku najtrudniejszych zadań wymagających rozumowania używaj modelu `high`. W przypadku większości zadań związanych z kodowaniem i agentami używaj ustawienia `medium` (domyślnego). W przypadku mniej złożonych zadań używaj elementu `low`.

## Obsługa długotrwałych żądań

Ponieważ Gemini 4 Argon dłużej analizuje trudne problemy niż modele Gemini 3.x, należy zwiększyć limity czasu klienta, aby długie żądania nie były przedwcześnie rozłączane.

- **Połączenia bez strumieniowania:** serwer zamyka połączenie po 10 minutach.
- **Połączenia strumieniowe:** serwer zamyka strumień po 20 minutach.
- **Limity czasu klienta:** ustaw limit czasu odczytu HTTP na 20 minut. 3- lub 5-minutowy limit czasu powoduje wcześniejsze zatrzymanie żądania.

W Pythonie ustaw limit czasu klienta w milisekundach:

```
client = genai.Client(http_options=types.HttpOptions(timeout=1_200_000))  # 20 minutes
```

W przypadku zadań, które klient odpytuje, interfejs Interactions API wykonuje długie dekodowanie na serwerze. Zobacz [wykonywanie w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl).

## Wznów, gdy model użyje wszystkich tokenów wyjściowych

Gdy odpowiedź kończy się znakiem `MAX_TOKENS`, nadal zawiera znak `continuation_token`. Masz 2 możliwości:

- **Kontynuuj:** wyślij to samo żądanie z tokenem i wyższą wartością `max_output_tokens`. Wartość musi być większa niż liczba tokenów użytych do tej pory. W przeciwnym razie interfejs API zwraca błąd 400.
- **Zacznij od nowa:** wyślij pierwotne żądanie z wyższą wartością parametru `max_output_tokens` i bez tokena. Płacisz za oba przebiegi.

## Zliczanie tokenów

W przypadku automatycznego kontynuowania funkcja `usage_metadata` raportuje sumy ze wszystkich przeskoków. Pakiet SDK sumuje wszystkie pola liczby: `prompt_token_count`, `cached_content_token_count`, `candidates_token_count`, `thoughts_token_count` i `total_token_count`.

`prompt_token_count` sumuje tokeny wejściowe każdego przeskoku. Każdy przeskok wysyła prompta i wszystko, co zostało wygenerowane do tej pory, z powrotem do modelu jako dane wejściowe, więc te same tokeny są ponownie zliczane w każdym kolejnym przeskoku. Na przykład w przypadku pakietu SDK Google GenAI prompt o długości 1000 tokenów, który generuje 200 tys. tokenów myślenia i wyniku, wymaga 4 kroków:

| Hop | Dane wejściowe wysłane do modelu | Tokeny wejściowe |
| --- | --- | --- |
| 1 | Prompt | 1000 |
| 2 | Prompt + hop 1 | 66 536 |
| 3 | Prompt + hops 1 and 2 | 132 072 |
| 4 | Prompt + przeskoki 1–3 | 197 608 |
| **Łącznie** |  | **397 216** |

`prompt_token_count` podaje około 397 000 tokenów (przy czym powtarzające się dane wejściowe są automatycznie pomniejszane o 95% dzięki ukrytemu buforowaniu), a `total_token_count` – około 597 000 tokenów, mimo że rzeczywisty rozmiar kontekstu to tylko około 201 000 tokenów: prompt o rozmiarze 1000 tokenów plus 200 000 tokenów na proces rozumowania i dane wyjściowe. Pętla REST bez przesyłania strumieniowego używa 32 tys. przeskoków, więc w przypadku tego samego wyniku potrzebuje 7 przeskoków i raportuje 695 128 tokenów wejściowych.

| Sposób wywoływania modelu | Co pokazuje `usage_metadata` | Za koszt | W przypadku rozmiaru promptu |
| --- | --- | --- | --- |
| Pakiet SDK Google GenAI, automatyczna kontynuacja (domyślnie) | Łącznie dla wszystkich przeskoków | Odczytuj pola wykorzystania w takiej postaci, w jakiej są. | Przeczytaj `usage_metadata.initial_prompt_token_count` (Python) lub `usageMetadata.initialPromptTokenCount` (JavaScript). |
| Pakiet SDK z `automatic_continuation=False` lub REST | Jeden przeskok na odpowiedź | Dodaj każde pole w ramach kolejnych przeskoków. | Odczytaj `prompt_token_count` z pierwszego przeskoku. |

`prompt_token_count` i `total_token_count` to suma wszystkich przeskoków, a nie rozmiar kontekstu. Nie używaj ich do decydowania, kiedy podsumować lub skrócić historię rozmów (kompresja kontekstu) ani do egzekwowania limitu kontekstu. Aby oszacować rozmiar kontekstu, dodaj rozmiar prompta z tabeli do `candidates_token_count` i `thoughts_token_count`.

Zanim uruchomisz długie dekodowanie, zaktualizuj platformę agenta, narzędzie do oceny lub serwer proxy:

- **Agenty i narzędzia do oceny:** jeśli kod kompresuje kontekst lub zatrzymuje działanie po osiągnięciu limitu tokenów, użyj `initial_prompt_token_count` (lub `prompt_token_count` pierwszego przeskoku w REST) zamiast sumy `prompt_token_count`. Odpowiedzi, które kończą się w jednym przeskoku, zgłaszają tę samą wartość w obu polach, więc krótkie testy nie pokazują problemu.
- **Serwery proxy i bramy wywołujące REST:** każda odpowiedź REST raportuje tylko swój własny przeskok. Dodaj każde pole we wszystkich przeskokach, aby obliczyć koszt, i zachowaj wartość `promptTokenCount` pierwszego przeskoku jako rozmiar promptu. W przeciwnym razie użytkownicy będą widzieć inne numery niż użytkownicy pakietu SDK w przypadku tego samego żądania.
- **Logi i odpowiedzi zserializowane:** pakiet SDK oblicza wartość `initial_prompt_token_count` po stronie klienta. Nie ma go w odpowiedzi REST ani w danych wyjściowych JSON pakietu SDK, takich jak `model_dump()`. Jeśli będzie Ci potrzebny później, zapisz go jako osobną wartość.

Jeśli przesyłasz strumieniowo we własnej pętli, wartość `usage_metadata` jest sumowana w ramach każdej transmisji. Zachowaj tylko ostatnią wartość każdego strumienia, a następnie dodaj wartości ze wszystkich przeskoków.

## Informacje o płatnościach

Płacisz za każdy token w każdym przeskoku, w tym za przeskoki, które zawierają tylko proces myślowy.

- **Zniżka za dane z pamięci podręcznej:** niejawne zapisywanie w pamięci podręcznej obniża koszt powtarzających się danych wejściowych w każdym przeskoku o 95%. W okresie wprowadzającym koszt danych wejściowych z pamięci podręcznej wynosi 0,10 USD za 1 mln tokenów zamiast 2,00 USD.
- **Wygasanie pamięci podręcznej:** pamięć podręczna wygasa po 15–20 minutach bez użycia. Długa przerwa między skokami powoduje ponowne naliczenie pełnej stawki za dane wejściowe.
- **Nieudane przeskoki bez przesyłania strumieniowego:** płacisz tylko wtedy, gdy odpowiedź zostanie wygenerowana w całości. Nieudane lub odrzucone żądanie kosztuje 0 USD.
- **Przerwane strumienie:** strumień, który zostanie przerwany przed wygenerowaniem 32 tys. tokenów, kosztuje 0 USD. Następnie płacisz do ostatniego tokena punktu kontrolnego, ponieważ możesz wznowić od niego.

## Rozwiązywanie problemów

| Krótki opis problemu | Przyczyna i rozwiązanie |
| --- | --- |
| Dane wyjściowe zatrzymują się na 64 tys. lub 32 tys. znaków z `CONTINUATION` | Model ma jeszcze tokeny, ale nic nie kontynuowało żądania. Uaktualnij pakiet SDK lub dodaj pętlę. |
| Dane wyjściowe zatrzymują się na 64 tys. lub 32 tys. w przypadku `MAX_TOKENS` | Wartość `max_output_tokens` nie jest ustawiona lub jest za niska. Ustaw wartość większą niż 65 536. |
| Pusty tekst z symbolem `MAX_TOKENS` | Model wykorzystał wszystkie tokeny na myślenie. Podnieś `max_output_tokens` lub opuść `thinking_level`. |
| 400. „Token kontynuacji wykorzystał już tokeny wyjściowe…” | Wartość `max_output_tokens` nie jest wyższa niż liczba tokenów użytych do tej pory. Podnieś ją. |
| Błąd dotyczący `thinking_level: "minimal"` lub `thinking_budget` z `thinking_level` | Gemini 4 Argon nie obsługuje tego typu pliku: `minimal`. Użyj `low`, `medium` lub `high`. Ustaw `thinking_level` lub `thinking_budget`, ale nie oba te parametry. |
| Ostrzeżenie dotyczące `thinking_budget`, `temperature`, `top_p` lub `top_k` | Gemini 4 Argon ignoruje te pola lub mapuje je. Użyj `thinking_level` i usuń parametry próbkowania. |
| Prośba kończy się po 3 lub 5 minutach. | Limit czasu klienta jest za krótki. Ustaw na 20 minut. |
| Kompaktowanie kontekstu rozpoczyna się za wcześnie | Wiązka odczytuje zsumowane dane wejściowe. Zamiast tego przeczytaj `initial_prompt_token_count`. |

## Ograniczenia

- **Punkt końcowy zgodności z OpenAI:** długie dekodowanie jest niedostępne. Dane wyjściowe zatrzymują się na limicie na żądanie.
- **Starsze pakiety SDK:** wersje poniżej minimalnych wartości podanych w uwadze nie będą aktualizowane automatycznie.
- **Długość:** model nie przestrzega docelowej długości tokenów ani liczby słów.

## Lista kontrolna

- Uaktualnij pakiet SDK Google GenAI do minimalnej wersji.
- Ustaw `max_output_tokens` na wartość większą niż 65 536.
- Używaj `thinking_level` (`low`, `medium` lub `high`), a nie `thinking_budget`.
- Ustaw limity czasu odczytu HTTP na 20 minut.
- Użyj `initial_prompt_token_count` w przypadku rozmiaru kontekstu i kompresji.
- Przed przeprowadzeniem dużej oceny uruchom jeden prompt jako test.

## Dalsze kroki

- [Nowości w Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=pl)
- [Myślę](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=pl)
- [Zliczanie tokenów](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-13 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-13 UTC."],[],[]]
