---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=pl
fetched_at: 2026-09-07T05:40:58.486728+00:00
title: "B\u0142\u0119dy interfejsu API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Błędy interfejsu API

Na tej stronie znajdziesz informacje o kodach błędów backendu zwracanych przez interfejs `GenerateContent` API, opis formatu odpowiedzi na błąd gRPC oraz instrukcje rozwiązywania problemów.

## Kody błędów HTTP

W tabeli poniżej znajdziesz listę typowych kodów błędów backendu, wyjaśnienia ich przyczyn oraz zalecane rozwiązania:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kod HTTP** | **Stan** | **Opis** | **Przykład** | **Rozwiązanie** |
| 400 | INVALID\_ARGUMENT | Treść żądania jest błędnie sformatowana. | W żądaniu występuje literówka lub brakuje wymaganego pola. | Sprawdź [dokumentację interfejsu API](https://ai.google.dev/api?hl=pl), aby dowiedzieć się więcej o formacie żądania, przykładach i obsługiwanych wersjach. Używanie funkcji z nowszej wersji interfejsu API ze starszym punktem końcowym może powodować błędy. |
| 400 | FAILED\_PRECONDITION | Bezpłatna wersja Gemini API nie jest dostępna w Twoim kraju. Włącz rozliczenia w projekcie w Google AI Studio. | Wysyłasz żądanie w regionie, w którym poziom bezpłatny nie jest obsługiwany, i nie masz włączonych rozliczeń w projekcie w Google AI Studio. | Aby korzystać z Gemini API, musisz skonfigurować płatny plan w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl). |
| 403 | PERMISSION\_DENIED | Twój klucz interfejsu API nie ma wymaganych uprawnień. | Używasz nieprawidłowego klucza interfejsu API; próbujesz użyć dostrojonego modelu bez [odpowiedniego uwierzytelnienia](https://ai.google.dev/gemini-api/docs/model-tuning?hl=pl). | Sprawdź, czy klucz interfejsu API jest ustawiony i ma odpowiedni dostęp. Upewnij się też, że masz odpowiednie uwierzytelnienie, aby korzystać z dostrojonych modeli. |
| 404 | NOT\_FOUND | Nie znaleziono żądanego zasobu. | Nie znaleziono pliku obrazu, dźwięku ani wideo, do którego odwołujesz się w żądaniu. | Sprawdź, czy wszystkie parametry w żądaniu są prawidłowe w przypadku używanej wersji interfejsu API. |
| 429 | RESOURCE\_EXHAUSTED | Przekroczono jeden z limitów częstotliwości żądań interfejsu API (RPM, TPM, RPD, wydatki itp.). | Wysyłasz zbyt wiele żądań, używasz zbyt wielu tokenów lub przekraczasz limity oparte na wydatkach w historii płatności i poziomie konta. | Sprawdź, czy nie przekraczasz [limitów częstotliwości żądań modelu](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl). Odczekaj chwilę i spróbuj ponownie. Zmniejsz częstotliwość lub rozmiar żądań. [W razie potrzeby poproś o zwiększenie limitu częstotliwości żądań](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#request-rate-limit-increase). |
| 499 | CANCELLED | Operacja została anulowana, zwykle przez element wywołujący. | Klient zamknął połączenie, zanim interfejs API zdążył odpowiedzieć. | Sprawdź, czy infrastruktura klienta lub sieci nie zamyka przedwcześnie połączenia (np. z powodu przekroczenia limitu czasu po stronie klienta). |
| 500 | WEWNĘTRZNY | Wystąpił nieoczekiwany błąd po stronie Google. | Kontekst wejściowy jest zbyt długi. | Sprawdź [stronę stanu Gemini API](https://aistudio.google.com/status?hl=pl), aby dowiedzieć się, czy występują jakieś problemy. Zmniejsz kontekst wejściowy lub tymczasowo przełącz się na inny model (np. z Gemini 2.5 Pro na Gemini 2.5 Flash) i sprawdź, czy to działa. Możesz też poczekać chwilę i ponowić żądanie. Jeśli problem będzie się powtarzać po ponowieniu próby, zgłoś go za pomocą przycisku **Prześlij opinię** w Google AI Studio. |
| 503 | PRODUKT NIEDOSTĘPNY | Usługa może być tymczasowo przeciążona lub niedostępna. | Usługa tymczasowo wyczerpuje zasoby. | Sprawdź [stronę stanu Gemini API](https://aistudio.google.com/status?hl=pl), aby dowiedzieć się, czy występują jakieś problemy. Tymczasowo przełącz się na inny model (np. z Gemini 2.5 Pro na Gemini 2.5 Flash) i sprawdź, czy to działa. Możesz też poczekać chwilę i ponowić żądanie. Jeśli problem będzie się powtarzać po ponowieniu próby, zgłoś go za pomocą przycisku **Prześlij opinię** w Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Usługa nie może zakończyć przetwarzania w wyznaczonym terminie. | Prompt (lub kontekst) jest zbyt duży, aby można go było przetworzyć na czas. | Aby uniknąć tego błędu, ustaw większy „limit czasu” w żądaniu klienta. |

## Format odpowiedzi na błąd

Gdy żądanie `GenerateContent` nie powiedzie się, interfejs API ustawia kod stanu HTTP (np. `400 Bad Request`, `403 Forbidden` lub `429 Too Many Requests`) i zwraca treść odpowiedzi JSON zawierającą szczegóły stanu gRPC:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| Pole | Typ | Opis |
| --- | --- | --- |
| `code` | liczba całkowita | Kod stanu HTTP. |
| `message` | tekst | Opis błędu w języku naturalnym. |
| `status` | tekst | Kod stanu gRPC w formacie `SCREAMING_CASE`. |
| `details` | tablica | Dodatkowy kontekst błędu, np. `ErrorInfo` lub `LocalizedMessage`. |

## Co dalej?

- [Rozwiązywanie problemów z interfejsem API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pl): rozwiązywanie typowych problemów i scenariuszy błędów.
- [Limity częstotliwości żądań](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl): informacje o limitach żądań i obsłudze limitów.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
