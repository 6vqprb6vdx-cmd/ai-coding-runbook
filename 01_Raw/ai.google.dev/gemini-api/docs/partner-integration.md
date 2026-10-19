---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=pl
fetched_at: 2026-10-19T05:46:31.743840+00:00
title: "Integracje z\u00a0partnerami i\u00a0bibliotekami \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Integracje z partnerami i bibliotekami

Ten przewodnik zawiera strategie architektoniczne dotyczące tworzenia bibliotek, platform i bram na podstawie interfejsu Gemini API. Opisuje kompromisy techniczne między korzystaniem z oficjalnych pakietów SDK do generatywnej AI, bezpośredniego interfejsu API (REST/gRPC) i warstwy zgodności z OpenAI.

Skorzystaj z tego przewodnika, jeśli tworzysz narzędzia dla innych programistów, takie jak platformy open source, bramy dla przedsiębiorstw lub agregatory SaaS, i musisz zoptymalizować je pod kątem higieny zależności, rozmiaru pakietu lub równoważności funkcji.

## Co to jest integracja z partnerem?

Partner to osoba, która tworzy integrację między interfejsem Gemini API a programistami końcowymi. Dzielimy partnerów na 4 typy. Określenie, który z nich jest najbardziej zbliżony do Twojej sytuacji, pomoże Ci wybrać odpowiednią ścieżkę integracji.

#### Platforma ekosystemu

- **Kim jesteś:** opiekunem platformy open source (np. LangChain, LlamaIndex, Spring AI) lub klientów w określonym języku.
- **Cel:** szeroki zakres zgodności. Chcesz, aby Twoja biblioteka działała w dowolnym środowisku wybranym przez użytkownika bez powodowania konfliktów.

#### Środowisko wykonawcze i platforma brzegowa

- **Kim jesteś:** platformy SaaS, bramy AI lub dostawcy infrastruktury w chmurze (np. Vercel, Cloudflare, Zapier), w przypadku których wykonywanie kodu odbywa się w ograniczonych środowiskach.
- **Twój cel:** skuteczność. Potrzebujesz małego opóźnienia, minimalnego rozmiaru pakietu i szybkiego uruchamiania „na zimno”.

#### Właściciel witryny

- **Kim jesteś:** platformy, serwery proxy lub wewnętrzne „Model Gardens”, które normalizują dostęp do wielu różnych dostawców LLM (np. OpenAI, Anthropic, Google) w jednym interfejsie.
- **Cel:** przenośność i jednolitość.

#### Brama dla firm

- **Kim jesteś:** wewnętrzne zespoły inżynierów platformy w dużych firmach, które tworzą „złote ścieżki” dla setek wewnętrznych programistów.
- **Twój cel:** standaryzacja, zarządzanie i ujednolicone uwierzytelnianie.

## Krótkie porównanie

**Sprawdzona metoda globalna:** wszyscy partnerzy muszą wysyłać [`x-goog-api-client`nagłówek](#client-id) niezależnie od wybranej ścieżki.

| Jeśli jesteś | Zalecana ścieżka | Główna korzyść | Najważniejszy kompromis | Sprawdzona metoda |
| --- | --- | --- | --- | --- |
| **Brama dla przedsiębiorstw, struktura ekosystemu** | **[Pakiet SDK Google GenAI](#genai-sdk)** | **Równoważność i szybkość Gemini Enterprise Agent Platform** Wbudowana obsługa typów, uwierzytelniania i zaawansowanych funkcji (np. przesyłania plików). Bezproblemowa migracja do Google Cloud. | **Waga zależności** Zależności przechodnie mogą być złożone i niezależne od Ciebie. Ograniczone do obsługiwanych języków (Python, Node, Go, Java). | **Blokowanie wersji** Przypinaj wersje pakietu SDK w wewnętrznych obrazach bazowych, aby zapewnić stabilność w różnych zespołach. |
| **Ramy ekosystemu, platformy brzegowe i agregatory** | **[Direct API](#rest)**  *(REST / gRPC)* | **Brak zależności** Masz kontrolę nad klientem HTTP i dokładnym rozmiarem pakietu. Pełny dostęp do wszystkich funkcji interfejsu API i modelu. | **Wysokie koszty po stronie dewelopera.** Struktury JSON mogą być głęboko zagnieżdżone i wymagać ścisłej ręcznej weryfikacji oraz sprawdzania typów. | **Używaj specyfikacji OpenAPI.** Automatyzuj generowanie typów za pomocą naszych oficjalnych specyfikacji zamiast pisać je ręcznie. |
| **Agregator korzystający z pakietów SDK OpenAI, które wymagają tylko przepływów pracy opartych na tekście**  *(Optymalizacja pod kątem starszej przenośności)* | **[Zgodność z OpenAI](#openai)** | **Natychmiastowa przenośność.** Ponownie używaj istniejącego kodu lub bibliotek zgodnych z OpenAI. | **Maksymalna liczba funkcji.** Funkcje specyficzne dla modelu (natywna kreacja wideo, buforowanie) mogą być niedostępne. | **Plan migracji** Używaj tej metody do szybkiego sprawdzania poprawności, ale planuj przejście na interfejs Direct API, aby korzystać z pełnej funkcjonalności interfejsu API. |

## Integracja pakietu Google GenAI SDK

W przypadku platform najprostszym rozwiązaniem jest często wdrożenie [pakietu Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=pl), ponieważ wymaga on najmniejszej liczby wierszy kodu w obsługiwanych językach.

W przypadku wewnętrznych zespołów platformy głównym produktem jest często „złota ścieżka”, która umożliwia inżynierom produktów szybkie działanie przy jednoczesnym zachowaniu zgodności z zasadami bezpieczeństwa.

**Korzyści:**

- **Ujednolicony interfejs do migracji na platformę Gemini Enterprise Agent Platform:** wewnętrzni programiści często tworzą prototypy za pomocą kluczy interfejsu API (Gemini API) i wdrażają je na platformie Gemini Enterprise Agent Platform (IAM) w celu zapewnienia zgodności z wymaganiami produkcyjnymi. Pakiet SDK ukrywa te różnice w uwierzytelnianiu.
  Podobnie w przypadku platform możesz wdrożyć jedną ścieżkę kodu i obsługiwać 2 grupy użytkowników.
- **Narzędzia po stronie klienta:** pakiet SDK zawiera idiomatyczne narzędzia, które ograniczają powtarzalny kod w przypadku złożonych zadań.
  - *Przykłady:* obsługa `PIL` obiektów obrazu bezpośrednio w promptach, automatyczne wywoływanie funkcji i kompleksowe typy.
- **Dostęp do funkcji od pierwszego dnia:** nowe funkcje interfejsu API są dostępne od momentu wprowadzenia na rynek za pomocą pakietów SDK.
- **Ulepszona obsługa generowania kodu:** lokalna instalacja pakietu SDK udostępnia definicje typów i ciągi dokumentacyjne asystentom kodowania (np. Cursor, Copilot).
  Ten kontekst zwiększa dokładność generowania kodu w porównaniu z generowaniem surowych żądań REST.

**Kompromis:**

- **Waga i złożoność zależności:** zestawy SDK mają własne zależności, które mogą zwiększać rozmiar pakietu i potencjalnie ryzyko związane z łańcuchem dostaw.
- **Obsługa wersji:** nowe funkcje interfejsu API są często powiązane z minimalnymi wersjami pakietu SDK.
  Aby uzyskać dostęp do nowych funkcji lub modeli, może być konieczne przesłanie aktualizacji do użytkowników. W niektórych przypadkach może to wymagać zmian w zależnościach przechodnich, które mają wpływ na użytkowników.
- **Limity protokołów:** pakiety SDK obsługują tylko protokół HTTPS w przypadku głównego interfejsu API i protokół WebSocket (WSS) w przypadku interfejsu Live API. gRPC nie jest obsługiwany w przypadku klientów pakietu SDK wysokiego poziomu.
- **Obsługa języków:** pakiety SDK obsługują *aktualne* wersje językowe. Jeśli musisz obsługiwać wersje EOL (np. Python 3.9), musisz utrzymywać fork.

**Sprawdzona metoda:**

- **Blokowanie wersji:** przypinaj wersję pakietu SDK w wewnętrznych obrazach bazowych, aby zapewnić stabilność w różnych zespołach.

## Bezpośrednia integracja interfejsu API

Jeśli rozpowszechniasz bibliotekę wśród tysięcy deweloperów, działasz w ograniczonym środowisku lub tworzysz agregator, który wymaga najnowszych funkcji Gemini, możesz potrzebować bezpośredniej integracji z interfejsem API za pomocą REST lub gRPC.

**Korzyści:**

- **Pełny dostęp do funkcji:** w przeciwieństwie do warstwy zgodności z OpenAI bezpośrednie korzystanie z interfejsu API umożliwia korzystanie z funkcji Gemini, takich jak przesyłanie do interfejsu File API, tworzenie pamięci podręcznej treści i korzystanie z dwukierunkowego interfejsu Live API.
- **Minimalne zależności:** w środowisku, w którym zależności są wrażliwe ze względu na rozmiar lub koszty audytu. Korzystanie z interfejsu API bezpośrednio za pomocą biblioteki standardowej, np. `fetch`, lub za pomocą otoki, np. `httpx`, zapewnia, że biblioteka pozostanie lekka.
- **Niezależne od języka:** to jedyna ścieżka dla języków nieobsługiwanych przez pakiety SDK, takich jak Rust, PHP i Ruby, ponieważ nie ma ograniczeń dotyczących języka.
- **Wydajność:** interfejs Direct API nie ma narzutu na inicjowanie, co minimalizuje zimne starty w funkcjach bezserwerowych.

**Kompromis:**

- **Ręczna implementacja Agent Platform Gemini Enterprise:** w przeciwieństwie do pakietu SDK bezpośrednie używanie interfejsu API nie obsługuje automatycznie różnic w uwierzytelnianiu między AI Studio (klucz interfejsu API) a Agent Platform Gemini Enterprise (IAM). Jeśli chcesz obsługiwać oba środowiska, musisz wdrożyć osobne moduły obsługi autoryzacji.
- **Brak typów natywnych i funkcji pomocniczych:** nie otrzymujesz uzupełnień kodu ani sprawdzania obiektów żądań w czasie kompilacji, chyba że sam je zaimplementujesz. Nie ma „pomocników” klienta (np. konwerterów funkcji na schematy), więc musisz samodzielnie napisać tę logikę.

**Sprawdzona metoda**

Udostępniamy specyfikację w formacie czytelnym dla maszyn, której możesz użyć do wygenerowania definicji typów dla swojej biblioteki, dzięki czemu nie musisz ich pisać ręcznie. Pobierz specyfikację podczas procesu kompilacji, wygeneruj typy i dostarcz skompilowany kod.

- **Punkt końcowy:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Integracja pakietu OpenAI SDK

Jeśli jesteś platformą, która priorytetowo traktuje ujednolicony schemat (OpenAI Chat Completions) zamiast funkcji specyficznych dla modelu, jest to najszybsza droga.

**Korzyści:**

- **Łatwość wdrożenia:** obsługę Gemini możesz często dodać, zmieniając `baseURL`i `apiKey`. To szybki sposób na integrację implementacji „Bring Your Own Key” (BYOK), który umożliwia dodanie obsługi Gemini bez pisania nowego kodu.
- **Ograniczenia:** ta ścieżka jest zalecana tylko wtedy, gdy możesz korzystać tylko z pakietu OpenAI SDK i nie potrzebujesz zaawansowanych funkcji Gemini, takich jak interfejs File API, ani ręcznego dodawania obsługi narzędzi takich jak powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google.

**Kompromis:**

- **Ograniczenia funkcji:** warstwa zgodności ogranicza podstawowe możliwości Gemini. Dostępne narzędzia po stronie serwera różnią się w zależności od platformy i mogą wymagać ręcznej obsługi, aby współpracować z narzędziami interfejsu Gemini API.
- **Dodatkowe koszty tłumaczenia:** ponieważ schemat OpenAI nie jest mapowany 1:1 na architekturę Gemini, korzystanie z warstwy zgodności wprowadza pewne złożoności, które wymagają dodatkowych prac wdrożeniowych, np. mapowania narzędzia „wyszukiwanie” użytkownika na odpowiednie narzędzie platformy.
  Jeśli potrzebujesz znacznej liczby wyjątków, bardziej opłaca się używać osobnego pakietu SDK lub interfejsu API dla każdej platformy.

**Sprawdzona metoda**

W miarę możliwości integruj się bezpośrednio z Gemini API. Aby jednak zapewnić maksymalną zgodność, warto użyć biblioteki, która rozpoznaje różnych dostawców i może obsługiwać mapowanie narzędzi i wiadomości.

## Sprawdzone metody dla wszystkich partnerów: identyfikacja klienta

Podczas wywoływania interfejsu Gemini API jako platforma lub biblioteka musisz identyfikować klienta za pomocą nagłówka `x-goog-api-client`.

Dzięki temu możemy identyfikować konkretne segmenty ruchu, a jeśli Twoja biblioteka generuje określony wzorzec błędów, możemy się z Tobą skontaktować, aby pomóc w jego usunięciu.

Użyj formatu `company-product/version` (np. `acme-framework/1.2.0`).

### Przykłady implementacji

### GenAI SDK

Po udostępnieniu klienta interfejsu API pakiet SDK automatycznie dołącza Twój niestandardowy nagłówek do nagłówków wewnętrznych.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### Bezpośredni interfejs API (REST)

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H 'Content-Type: application/json' \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### OpenAI SDK

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Dalsze kroki

- Aby dowiedzieć się więcej o pakietach SDK GenAI, zapoznaj się z [przeglądem bibliotek](https://ai.google.dev/gemini-api/docs/libraries?hl=pl).
- Przejrzyj [dokumentację API](https://ai.google.dev/api?hl=pl)
- Przeczytaj [przewodnik po zgodności z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-30 UTC."],[],[]]
