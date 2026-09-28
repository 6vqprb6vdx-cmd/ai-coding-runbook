---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=pl
fetched_at: 2026-09-28T06:09:39.120350+00:00
title: "B\u0142\u0119dy interfejsu API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# Błędy interfejsu API

Ta strona zawiera informacje o kodach błędów backendu zwracanych przez interfejs `GenerateContent` API, opisuje format odpowiedzi na błąd gRPC i zawiera kroki rozwiązywania problemów.

## Kody błędów HTTP

W tabeli poniżej znajdziesz typowe kody błędów backendu, wyjaśnienia ich przyczyn i zalecane rozwiązania:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kod HTTP** | **Stan** | **Opis** | **Przykład** | **Rozwiązanie** |
| 400 | INVALID\_ARGUMENT | Treść żądania jest błędnie sformatowana. | W żądaniu jest błąd w pisowni lub brakuje wymaganego pola. | Format żądania, przykłady i obsługiwane wersje znajdziesz w [dokumentacji API](https://ai.google.dev/api?hl=pl). Używanie funkcji z nowszej wersji interfejsu API ze starszym punktem końcowym może powodować błędy. |
| 400 | FAILED\_PRECONDITION | Bezpłatny poziom Gemini API nie jest dostępny w Twoim kraju. Włącz płatności w projekcie w Google AI Studio. | Wysyłasz żądanie w regionie, w którym poziom bezpłatny nie jest obsługiwany, a w projekcie w Google AI Studio nie masz włączonych rozliczeń. | Aby korzystać z Gemini API, musisz skonfigurować abonament w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl). |
| 402 | RESOURCE\_EXHAUSTED | Saldo środków z przedpłaty zostało wyczerpane. | Na Twoim koncie rozliczeniowym wyczerpały się środki przedpłaty, więc wszystkie klucze API powiązane z tym kontem rozliczeniowym przestają działać. | [Dodaj środki](https://ai.google.dev/gemini-api/docs/billing?hl=pl#buy-credits) na konto rozliczeniowe lub włącz [automatyczne doładowanie](https://ai.google.dev/gemini-api/docs/billing?hl=pl#auto-reload). Nie próbuj ponownie wysłać tego żądania: nie powiedzie się, dopóki nie dodasz środków. |
| 403 | PERMISSION\_DENIED | Twój klucz API nie ma wymaganych uprawnień. | Używasz nieprawidłowego klucza interfejsu API. Próbujesz użyć dostosowanego modelu bez [prawidłowego uwierzytelniania](https://ai.google.dev/gemini-api/docs/model-tuning?hl=pl). | Sprawdź, czy klucz interfejsu API jest ustawiony i ma odpowiedni dostęp. Aby korzystać z dostosowanych modeli, musisz przejść odpowiednią weryfikację. |
| 404 | NOT\_FOUND | Nie znaleziono żądanego zasobu. | Nie znaleziono pliku obrazu, audio ani wideo, do którego odwołuje się Twoja prośba. | Sprawdź, czy wszystkie parametry w żądaniu są prawidłowe w przypadku używanej wersji interfejsu API. |
| 429 | RESOURCE\_EXHAUSTED | Przekroczono jeden z limitów częstotliwości interfejsu API (RPM, TPM, RPD, wydatki itp.). | Wysyłasz zbyt wiele żądań, używasz zbyt wielu tokenów lub przekraczasz limity oparte na wydatkach w przypadku historii płatności i poziomu konta. | Sprawdź, czy nie przekraczasz [limitów szybkości](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl) modelu. Poczekaj chwilę i spróbuj ponownie. Zmniejsz częstotliwość lub rozmiar żądań. W razie potrzeby [poproś o zwiększenie limitu częstotliwości](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#request-rate-limit-increase). |
| 499 | ANULOWANO | Operacja została anulowana, zwykle przez element wywołujący. | Klient zamknął połączenie, zanim interfejs API zdążył odpowiedzieć. | Sprawdź, czy klient lub infrastruktura sieciowa przedwcześnie zamyka połączenie (np. z powodu limitu czasu po stronie klienta). |
| 500 | WEWNĘTRZNY | Po stronie Google wystąpił nieoczekiwany błąd. | Kontekst wejściowy jest za długi. | Sprawdź [stronę stanu Gemini API](https://aistudio.google.com/status?hl=pl), aby dowiedzieć się o bieżących incydentach. Zmniejsz kontekst wejściowy lub tymczasowo przełącz się na inny model (np. z Gemini 2.5 Pro na Gemini 2.5 Flash) i sprawdź, czy to pomoże. Możesz też poczekać chwilę i ponowić prośbę. Jeśli problem będzie się powtarzać, zgłoś go, klikając przycisk **Prześlij opinię** w Google AI Studio. |
| 503 | PRODUKT NIEDOSTĘPNY | Usługa może być tymczasowo przeciążona lub niedostępna. | Usługa tymczasowo wyczerpuje swoje możliwości. | Sprawdź [stronę stanu Gemini API](https://aistudio.google.com/status?hl=pl), aby dowiedzieć się o bieżących incydentach. Tymczasowo przełącz się na inny model (np. z Gemini 2.5 Pro na Gemini 2.5 Flash) i sprawdź, czy to działa. Możesz też poczekać chwilę i ponowić prośbę. Jeśli problem będzie się powtarzać, zgłoś go, klikając przycisk **Prześlij opinię** w Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Usługa nie może zakończyć przetwarzania w terminie. | Prompt (lub kontekst) jest zbyt duży, aby można go było przetworzyć na czas. | Aby uniknąć tego błędu, ustaw w żądaniu klienta dłuższy „limit czasu”. |

## Format odpowiedzi na błąd

Gdy żądanie `GenerateContent` zakończy się niepowodzeniem, interfejs API ustawia kod stanu HTTP (np. `400 Bad Request`, `403 Forbidden` lub `429 Too Many Requests`) i zwraca treść odpowiedzi JSON zawierającą szczegóły stanu gRPC:

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
| `message` | tekst | Zrozumiały dla człowieka opis błędu. |
| `status` | tekst | Kod stanu gRPC w `SCREAMING_CASE`. |
| `details` | tablica | Dodatkowy kontekst błędu, np. `ErrorInfo` lub `LocalizedMessage`. |

## Co dalej?

- [Rozwiązywanie problemów z interfejsem API:](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pl) rozwiązywanie typowych problemów i scenariuszy błędów.
- [Limity](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl): dowiedz się więcej o limitach żądań i obsłudze limitów.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-20 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-20 UTC."],[],[]]
