---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pl
fetched_at: 2026-06-22T06:28:22.237021+00:00
title: "Przewodnik rozwi\u0105zywania problem\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Przewodnik rozwiązywania problemów

Skorzystaj z tego przewodnika, aby zdiagnozować i rozwiązać typowe problemy, które mogą wystąpić podczas wywoływania Gemini API. Problemy mogą występować zarówno w usłudze backendowej Gemini API, jak i w pakietach SDK klienta. Nasze pakiety SDK klienta są dostępne na licencji open source w tych repozytoriach:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Jeśli masz problemy z kluczem interfejsu API, sprawdź, czy został on prawidłowo skonfigurowany zgodnie z [przewodnikiem konfiguracji klucza interfejsu API](https://ai.google.dev/gemini-api/docs/api-key?hl=pl).

## Kody błędów usługi backendowej Gemini API

W tabeli poniżej znajdziesz listę typowych kodów błędów backendu, które mogą wystąpić, wraz z wyjaśnieniami ich przyczyn i sposobami rozwiązywania problemów:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Kod HTTP** | **Stan** | **Opis** | **Przykład** | **Rozwiązanie** |
| 400 | INVALID\_ARGUMENT | Treść żądania jest nieprawidłowa. | W żądaniu występuje błąd lub brakuje wymaganego pola. | Sprawdź [dokumentację interfejsu API](https://ai.google.dev/api?hl=pl), aby dowiedzieć się więcej o formacie żądania, przykładach i obsługiwanych wersjach. Używanie funkcji z nowszej wersji interfejsu API ze starszym punktem końcowym może powodować błędy. |
| 400 | FAILED\_PRECONDITION | Bezpłatna wersja Gemini API nie jest dostępna w Twoim kraju. Włącz rozliczenia w projekcie w Google AI Studio. | Wysyłasz żądanie w regionie, w którym poziom bezpłatny nie jest obsługiwany, i nie masz włączonych rozliczeń w projekcie w Google AI Studio. | Aby korzystać z Gemini API, musisz skonfigurować płatny plan w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl). |
| 403 | PERMISSION\_DENIED | Twój klucz interfejsu API nie ma wymaganych uprawnień. | Używasz nieprawidłowego klucza interfejsu API; używasz dostrojonego modelu bez [odpowiedniego uwierzytelnienia](https://ai.google.dev/gemini-api/docs/model-tuning?hl=pl). | Sprawdź, czy klucz interfejsu API jest ustawiony i ma odpowiedni dostęp. Upewnij się też, że masz odpowiednie uwierzytelnienie, aby korzystać z dostrojonych modeli. |
| 404 | NOT\_FOUND | Nie znaleziono żądanego zasobu. | Nie znaleziono pliku obrazu, dźwięku ani wideo, do którego odwołujesz się w żądaniu. | Sprawdź, czy wszystkie [parametry w żądaniu są prawidłowe](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pl#check-api) w przypadku Twojej wersji interfejsu API. |
| 429 | RESOURCE\_EXHAUSTED | Przekroczono limit liczby żądań. | Wysyłasz zbyt wiele żądań na minutę w bezpłatnej wersji Gemini API. | Sprawdź, czy nie przekraczasz [limitu liczby żądań modelu](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl). [W razie potrzeby poproś o zwiększenie limitu](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#request-rate-limit-increase). |
| 499 | CANCELLED | Operacja została anulowana, zwykle przez element wywołujący. | Klient zamknął połączenie, zanim interfejs API zdążył odpowiedzieć. | Sprawdź, czy infrastruktura klienta lub sieci nie zamyka przedwcześnie połączenia (np. z powodu przekroczenia limitu czasu po stronie klienta). |
| 500 | INTERNAL | Wystąpił nieoczekiwany błąd po stronie Google. | Kontekst wejściowy jest zbyt długi. | Sprawdź [stronę stanu Gemini API](https://aistudio.google.com/status?hl=pl), aby dowiedzieć się, czy występują jakieś problemy. Skróć kontekst wejściowy lub tymczasowo przejdź na inny model (np. z Gemini 2.5 Pro na Gemini 2.5 Flash) i sprawdź, czy to działa. Możesz też poczekać chwilę i ponowić żądanie. Jeśli problem nadal występuje po ponowieniu próby, zgłoś go za pomocą przycisku **Prześlij opinię** w Google AI Studio. |
| 503 | UNAVAILABLE | Usługa może być tymczasowo przeciążona lub niedostępna. | Usługa tymczasowo wyczerpuje zasoby. | Sprawdź [stronę stanu Gemini API](https://aistudio.google.com/status?hl=pl), aby dowiedzieć się, czy występują jakieś problemy. Tymczasowo przejdź na inny model (np. z Gemini 2.5 Pro na Gemini 2.5 Flash) i sprawdź, czy to działa. Możesz też poczekać chwilę i ponowić żądanie. Jeśli problem nadal występuje po ponowieniu próby, zgłoś go za pomocą przycisku **Prześlij opinię** w Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Usługa nie może zakończyć przetwarzania w wyznaczonym terminie. | Prompt (lub kontekst) jest zbyt duży, aby można go było przetworzyć w odpowiednim czasie. | Aby uniknąć tego błędu, ustaw większy „limit czasu” w żądaniu klienta. |

## Sprawdzanie wywołań interfejsu API pod kątem błędów parametrów modelu

Sprawdź, czy parametry modelu mieszczą się w tych zakresach:

|  |  |
| --- | --- |
| **Parametr modelu** | **Wartości (zakres)** |
| Liczba kandydatów | 1–8 (liczba całkowita) |
| Temperatura | 0,0–1,0 |
| Maksymalna liczba tokenów | Aby określić maksymalną liczbę tokenów dla używanego modelu, otwórz stronę [modeli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl). |
| TopP | 0,0–1,0 |

Oprócz sprawdzania wartości parametrów upewnij się, że używasz prawidłowej
[wersji interfejsu API](https://ai.google.dev/gemini-api/docs/api-versions?hl=pl) (np. `/v1` lub `/v1beta`) i
modelu, który obsługuje potrzebne Ci funkcje. Jeśli na przykład funkcja jest w wersji beta, będzie dostępna tylko w wersji interfejsu API `/v1beta`.

## Sprawdzanie, czy masz odpowiedni model

Sprawdź, czy używasz obsługiwanego modelu wymienionego na naszej [stronie modeli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pl).

## Większe opóźnienie lub wykorzystanie tokenów w przypadku modeli 2.5

Jeśli zauważysz większe opóźnienie lub wykorzystanie tokenów w przypadku modeli 2.5 Flash i Pro, może to być spowodowane tym, że domyślnie mają one **włączone myślenie** , aby poprawić jakość. Jeśli priorytetem jest dla Ciebie szybkość lub chcesz zminimalizować koszty, możesz dostosować lub wyłączyć myślenie.

Wskazówki i przykładowy kod znajdziesz na stronie [myślenia](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#set-budget).

## Problemy z bezpieczeństwem

Jeśli widzisz, że prompt został zablokowany z powodu ustawienia bezpieczeństwa w wywołaniu interfejsu API, sprawdź prompt pod kątem filtrów ustawionych w wywołaniu interfejsu API.

Jeśli widzisz `BlockedReason.OTHER`, zapytanie lub odpowiedź mogą naruszać [warunki
korzystania z usługi](https://ai.google.dev/terms?hl=pl) lub być w inny sposób nieobsługiwane.

## Problem z recytacją

Jeśli widzisz, że model przestaje generować dane wyjściowe z powodu RECITATION, oznacza to, że dane wyjściowe modelu mogą przypominać określone dane. Aby to naprawić, spróbuj, aby prompt lub kontekst były jak najbardziej unikalne, i użyj wyższej temperatury.

## Problem z powtarzającymi się tokenami

Jeśli widzisz powtarzające się tokeny wyjściowe, spróbuj zastosować te sugestie, aby je ograniczyć lub wyeliminować.

| Opis | Przyczyna | Sugerowane obejście |
| --- | --- | --- |
| Powtarzające się łączniki w tabelach Markdown | Może się to zdarzyć, gdy zawartość tabeli jest długa, ponieważ model próbuje utworzyć tabelę Markdown wyrównaną wizualnie. Wyrównanie w Markdown nie jest jednak konieczne do prawidłowego renderowania. | Dodaj do prompta instrukcje, aby podać modelowi konkretne wytyczne dla generowania tabel Markdown. Podaj przykłady zgodne z tymi wytycznymi. Możesz też spróbować dostosować temperaturę. W przypadku generowania kodu lub bardzo ustrukturyzowanych danych wyjściowych, takich jak tabele Markdown, lepiej sprawdzają się wysokie temperatury (>= 0,8).  Oto przykładowy zestaw wytycznych, które możesz dodać do swojego prompta, aby zapobiec temu problemowi:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Powtarzające się tokeny w tabelach Markdown | Podobnie jak w przypadku powtarzających się łączników, dzieje się tak, gdy model próbuje wizualnie wyrównać zawartość tabeli. Wyrównanie w Markdown nie jest nie jest wymagane do prawidłowego renderowania. | - Spróbuj dodać do prompta systemowego instrukcje takie jak te:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Spróbuj dostosować temperaturę. Wyższe temperatury (>= 0,8)   zwykle pomagają wyeliminować powtórzenia lub duplikaty w   danych wyjściowych. |
| Powtarzające się znaki nowego wiersza (`\n`) w ustrukturyzowanych danych wyjściowych | Gdy dane wejściowe modelu zawierają znaki Unicode lub sekwencje ucieczki, takie jak `\u` lub `\t`, może to prowadzić do powtarzających się znaków nowego wiersza. | - Sprawdź, czy w prompcie nie ma zabronionych sekwencji ucieczki, i zastąp je znakami UTF-8. Na przykład sekwencja ucieczki `\u`   w przykładach JSON może spowodować, że model będzie jej używać   w danych wyjściowych. - Poinstruuj model o dozwolonych sekwencjach ucieczki. Dodaj instrukcję systemową, taką jak   ta:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Powtarzający się tekst w ustrukturyzowanych danych wyjściowych | Gdy dane wyjściowe modelu mają inną kolejność pól niż zdefiniowany schemat ustrukturyzowany, może to prowadzić do powtarzania się tekstu. | - Nie określaj kolejności pól w prompcie. - Ustaw wszystkie pola wyjściowe jako wymagane. |
| Powtarzające się wywoływanie narzędzia | Może się to zdarzyć, jeśli model utraci kontekst poprzednich myśli lub wywoła niedostępny punkt końcowy, do którego jest zmuszony. | Poinstruuj model, aby zachowywał stan w procesie myślenia. Dodaj ten tekst na końcu instrukcji systemowych:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Powtarzający się tekst, który nie jest częścią ustrukturyzowanych danych wyjściowych | Może się to zdarzyć, jeśli model utknie na żądaniu, którego nie może rozwiązać. | - Jeśli myślenie jest włączone, unikaj podawania w instrukcjach wyraźnych poleceń dotyczących sposobu   rozwiązywania problemu. Po prostu poproś o ostateczne   dane wyjściowe. - Spróbuj użyć wyższej temperatury >= 0,8. - Dodaj instrukcje takie jak "Bądź zwięzły", "Nie powtarzaj się", lub   "Podaj odpowiedź raz". |

## Zablokowane lub niedziałające klucze interfejsu API

W tej sekcji opisujemy, jak sprawdzić, czy klucz Gemini API jest zablokowany, i co z tym zrobić.

### Przyczyny blokowania kluczy

Zidentyfikowaliśmy lukę w zabezpieczeniach, która mogła spowodować publiczne udostępnienie niektórych kluczy interfejsu API. Aby chronić Twoje dane i zapobiegać nieautoryzowanemu dostępowi, proaktywnie zablokowaliśmy dostęp do Gemini API za pomocą tych znanych, wyciekłych kluczy.

### Sprawdzanie, czy problem dotyczy Twoich kluczy

Jeśli Twój klucz jest znany jako wyciekły, nie możesz go już używać z Gemini API. W [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pl) możesz sprawdzić, czy któryś z
Twoich kluczy interfejsu API jest zablokowany i nie może wywoływać Gemini API, oraz wygenerować nowe
klucze. Podczas próby użycia tych kluczy możesz też zobaczyć ten błąd:

```
Your API key was reported as leaked. Please use another API key.
```

### Działania w przypadku zablokowanych kluczy interfejsu API

W [Google
AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pl) wygeneruj nowe klucze interfejsu API na potrzeby integracji z Gemini API. Zdecydowanie zalecamy sprawdzenie metod zarządzania kluczami interfejsu API, aby upewnić się, że nowe klucze są bezpieczne i nie są publicznie udostępniane.

### Nieoczekiwane opłaty spowodowane luką w zabezpieczeniach

[Prześlij zgłoszenie do zespołu pomocy ds. rozliczeń](https://console.cloud.google.com/support/chat?hl=pl).
Nasz zespół ds. rozliczeń pracuje nad tym problemem i jak najszybciej poinformuje Cię o postępach.

### Środki bezpieczeństwa Google w przypadku wyciekłych kluczy

**Jak Google pomoże mi zabezpieczyć konto przed przekroczeniem kosztów i nadużyciami, jeśli moje klucze interfejsu API wyciekną?**

- Wprowadzamy zmiany, aby klucze interfejsu API były wydawane tylko wtedy, gdy poprosisz o nowy klucz w
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pl). Domyślnie będą one
  ograniczone tylko do Google AI Studio i nie będą akceptować kluczy z innych usług.
  Pomoże to zapobiec niezamierzonemu użyciu kluczy w różnych usługach.
- Domyślnie blokujemy klucze interfejsu API, które wyciekły i są używane z Gemini API, co pomaga zapobiegać nadużyciom związanym z kosztami i danymi aplikacji.
- Stan kluczy interfejsu API możesz sprawdzić w [Google AI
  Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=pl). Będziemy też proaktywnie informować Cię, gdy wykryjemy, że Twoje klucze interfejsu API wyciekły, aby umożliwić Ci podjęcie natychmiastowych działań.

## Poprawianie danych wyjściowych modelu

Aby uzyskać dane wyjściowe modelu o wyższej jakości, spróbuj pisać bardziej ustrukturyzowane prompty. Na stronie
[przewodnika po projektowaniu promptów](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl) znajdziesz podstawowe pojęcia, strategie i sprawdzone metody, które pomogą Ci
zacząć.

## Limity tokenów

Przeczytaj nasz [przewodnik po tokenach](https://ai.google.dev/gemini-api/docs/tokens?hl=pl), aby dowiedzieć się więcej o tym, jak
liczyć tokeny i jakie są ich limity.

## Znane problemy

- Interfejs API obsługuje tylko wybrane języki. Przesyłanie promptów w nieobsługiwanych językach może powodować nieoczekiwane lub nawet zablokowane odpowiedzi. Aktualizacje znajdziesz na liście
  [dostępnych języków](https://ai.google.dev/gemini-api/docs/models?hl=pl#supported-languages) dla
  aktualizacji.

## Zgłaszanie błędu

Jeśli masz pytania, dołącz do dyskusji na
[forum dla deweloperów Google AI](https://discuss.ai.google.dev?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-10 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-10 UTC."],[],[]]
