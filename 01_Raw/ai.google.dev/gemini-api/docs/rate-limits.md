---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl
fetched_at: 2026-10-19T05:31:22.352849+00:00
title: "Ograniczenia liczby \u017c\u0105da\u0144 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Ograniczenia liczby żądań

Limity liczby żądań określają, ile żądań możesz wysłać do interfejsu Gemini API w danym okresie. Te limity pomagają zapewnić uczciwe korzystanie z usługi, chronić przed nadużyciami i utrzymać wydajność systemu dla wszystkich użytkowników.

[Wyświetlanie aktywnych limitów w AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=pl)

## Jak działają limity szybkości

Limity zwykle mierzy się w 3 wymiarach:

- Żądania na minutę (**RPM**)
- Tokeny na minutę (dane wejściowe) (**TPM**)
- Żądania dziennie (**RPD**)

Wykorzystanie jest oceniane pod kątem każdego limitu, a przekroczenie dowolnego z nich spowoduje błąd limitu liczby żądań. Jeśli na przykład limit zapytań na minutę wynosi 20, wysłanie 21 zapytań w ciągu minuty spowoduje błąd, nawet jeśli nie przekroczysz limitu zapytań na miesiąc ani innych limitów.

Limity liczby żądań są stosowane na poziomie projektu, a nie klucza interfejsu API. Limity liczby żądań dziennie (**RPD**) są resetowane o północy czasu pacyficznego.

Limity różnią się w zależności od używanego modelu, a niektóre limity dotyczą tylko konkretnych modeli. Na przykład liczba obrazów na minutę (IPM) jest obliczana tylko w przypadku modeli, które mogą generować obrazy (Nano Banana), ale jest podobna do liczby tokenów na minutę. Inne modele mogą mieć limit tokenów na dzień (TPD).

W przypadku modeli eksperymentalnych i wersji zapoznawczych limity liczby żądań są bardziej restrykcyjne.

### Limity oparte na wydatkach

Oprócz limitów żądań na minutę (RPM) i tokenów na minutę (TPM) interfejs Gemini API stosuje limity oparte na wydatkach, aby chronić przed nieoczekiwanymi opłatami. To, czy te limity obowiązują na Twoim koncie, zależy od historii płatności i [poziomu wykorzystania](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#usage-tiers).

W tabeli poniżej znajdziesz limity liczby żądań oparte na wydatkach dla poszczególnych [poziomów wykorzystania](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#usage-tiers). Te limity są oceniane w 10-minutowym oknie kroczącym. To, czy te limity dotyczą Twojego konta, zależy od historii płatności i stanu konta.

| Poziom wykorzystania | Limit wydatków (na 10 minut) |
| --- | --- |
| **Free** | Nie dotyczy |
| **Poziom 1** | 10 USD |
| **Poziom 2** | 50 USD |
| **Poziom 3** | 200 HKD |

Jeśli osiągniesz limit oparty na wydatkach, interfejs API zwróci błąd `429 RESOURCE_EXHAUSTED`. Aby rozwiązać ten problem:

- **Poczekaj i spróbuj ponownie** po krótkim czasie.
- **Zmniejsz liczbę kosztownych żądań**, na przykład przez używanie mniejszych okien kontekstu lub krótszych danych wyjściowych.
- Jeśli stale osiągasz ten limit podczas normalnego użytkowania, [poproś o jego zwiększenie](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#request-rate-limit-increase).

## Poziomy wykorzystania

Limity liczby żądań są powiązane z poziomem wykorzystania projektu. W miarę wzrostu wykorzystania interfejsu API i wydatków automatycznie przejdziesz na wyższy poziom z wyższymi limitami liczby żądań.

Kwalifikacje do poziomów 2 i 3 są oparte na łącznych wydatkach na usługi Google Cloud (w tym na interfejs Gemini API) na koncie rozliczeniowym połączonym z Twoim projektem.

| Poziom wykorzystania | Kwalifikacje | [Limit poziomu płatności](https://ai.google.dev/gemini-api/docs/billing?hl=pl#tier-spend-caps) |
| --- | --- | --- |
| **Free** | [Aktywny projekt](https://ai.google.dev/gemini-api/docs/api-key?hl=pl#google-cloud-projects) lub bezpłatny okres próbny | Nie dotyczy |
| **Poziom 1** | [Skonfiguruj i połącz aktywne konto rozliczeniowe](https://ai.google.dev/gemini-api/docs/billing?hl=pl#setup-billing) | 250 USD |
| **Poziom 2** | Wypłata 100 USD + 3 dni od pierwszej udanej płatności | 2000 USD |
| **Poziom 3** | Zapłacono 1000 USD + 30 dni od pierwszej udanej płatności | 20 000–100 000 USD i więcej |

Spełnienie podanych kryteriów kwalifikacji jest zwykle wystarczające do zatwierdzenia, ale w rzadkich przypadkach prośba o przejście na wyższy poziom może zostać odrzucona z powodu innych czynników wykrytych podczas procesu weryfikacji.

Ten system pomaga zachować bezpieczeństwo i integralność platformy Gemini API dla wszystkich użytkowników.

## Limity liczby żądań do interfejsu Gemini API

Limity szybkości zależą od wielu czynników (np. od poziomu wykorzystania) i można je sprawdzić w Google AI Studio. W miarę jak Twój poziom i stan konta będą się zmieniać, limity żądań będą automatycznie aktualizowane.

[Wyświetlanie aktywnych limitów w AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=pl)

Określone limity szybkości nie są gwarantowane, a rzeczywista przepustowość może się różnić.

## Limity szybkości wnioskowania priorytetowego

Wykorzystanie [priorytetowe](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl) ma własne limity, mimo że jest wliczane do ogólnych limitów ruchu interaktywnego. **Domyślne limity to 0,3x [standardowego limitu](https://aistudio.google.com/rate-limit?hl=pl) dla każdego modelu i poziomu**

## Limity Batch API

Żądania do [interfejsu API operacji zbiorczych](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl) podlegają własnym limitom, które są niezależne od wywołań interfejsu API operacji pojedynczych.

- **Równoczesne żądania zbiorcze:** 100
- **Limit rozmiaru pliku wejściowego:** 2 GB
- **Limit miejsca na pliki:** 20 GB
- **Tokeny w kolejce na model:** tabela **Tokeny w kolejce wsadowej** zawiera maksymalną liczbę tokenów, które można umieścić w kolejce do przetwarzania wsadowego we wszystkich aktywnych zadaniach wsadowych dla danego modelu.

### Poziom 1

| Model | Tokeny dodane do kolejki wsadowej |
| --- | --- |
| Modele generujące tekst | | | | |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | 5 000 000 |
| Gemini 3.1 Pro (wersja testowa) | 5 000 000 |
| Gemini 3.5 Flash-Lite | 10 000 000 |
| Gemini 3.8 Flash | 3 000 000 |
| Gemini 3.1 Flash Lite | 10 000 000 |
| Gemini 3.1 Flash Lite (wersja testowa) | 10 000 000 |
| Gemini 3.6 Flash | 3 000 000 |
| Gemini 2.5 Pro | 5 000 000 |
| Gemini 2.5 Pro TTS | 25 000 |
| Gemini 2.5 Flash | 3 000 000 |
| Gemini 2.5 Flash (wersja testowa) | 3 000 000 |
| Gemini 2.5 Flash Image (wersja testowa) | 3 000 000 |
| Gemini 2.5 Flash TTS | 100 000 |
| Gemini 2.5 Flash Lite | 10 000 000 |
| Gemini 2.5 Flash Lite (wersja testowa) | 10 000 000 |
| Gemini 2.0 Flash | 10 000 000 |
| Gemini 2.0 Flash Image | 3 000 000 |
| Gemini 2.0 Flash Lite | 10 000 000 |
| Modele generowania multimodalnego | | | | |
| Gemini 3.1 Flash Image (wersja testowa) 🍌 | 1 000 000 |
| Gemini 3.1 Flash Lite Image 🍌 | 2 000 000 |
| Gemini 3 Pro Image Preview 🍌 | 2 000 000 |
| Modele wektorów dystrybucyjnych | | | | |
| Gemini Embedding | 500 000 |

### Poziom 2

| Model | Tokeny dodane do kolejki wsadowej |
| --- | --- |
| Modele generujące tekst | | | | |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | 500 000 000 |
| Gemini 3.1 Pro (wersja testowa) | 500 000 000 |
| Gemini 3.5 Flash-Lite | 500 000 000 |
| Gemini 3.1 Flash Lite | 500 000 000 |
| Gemini 3.1 Flash Lite (wersja testowa) | 500 000 000 |
| Gemini 3.8 Flash | 400 000 000 |
| Gemini 3.6 Flash | 400 000 000 |
| Gemini 2.5 Pro | 500 000 000 |
| Gemini 2.5 Pro TTS | 100 000 |
| Gemini 2.5 Flash | 400 000 000 |
| Gemini 2.5 Flash (wersja testowa) | 400 000 000 |
| Gemini 2.5 Flash Image (wersja testowa) | 400 000 000 |
| Gemini 2.5 Flash TTS | 100 000 |
| Gemini 2.5 Flash Lite | 500 000 000 |
| Gemini 2.5 Flash Lite (wersja testowa) | 500 000 000 |
| Gemini 2.0 Flash | 1 000 000 000 |
| Gemini 2.0 Flash Image | 400 000 000 |
| Gemini 2.0 Flash Lite | 1 000 000 000 |
| Multimodalne modele generatywne | | | | |
| Gemini 3.1 Flash Image (wersja testowa) 🍌 | 250 000 000 |
| Gemini 3.1 Flash Lite Image 🍌 | 270 000 000 |
| Gemini 3 Pro Image Preview 🍌 | 270 000 000 |
| Modele wektorów dystrybucyjnych | | | | |
| Gemini Embedding | 5 000 000 |

### Poziom 3

| Model | Tokeny dodane do kolejki wsadowej |
| --- | --- |
| Modele generujące tekst | | | | |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | 1 000 000 000 |
| Gemini 3.1 Pro (wersja testowa) | 1 000 000 000 |
| Gemini 3.5 Flash-Lite | 1 000 000 000 |
| Gemini 3.1 Flash Lite | 1 000 000 000 |
| Gemini 3.1 Flash Lite (wersja testowa) | 1 000 000 000 |
| Gemini 3.8 Flash | 1 000 000 000 |
| Gemini 3.6 Flash | 1 000 000 000 |
| Gemini 2.5 Pro | 1 000 000 000 |
| Gemini 2.5 Pro TTS | 1 000 000 |
| Gemini 2.5 Flash | 1 000 000 000 |
| Gemini 2.5 Flash (wersja testowa) | 1 000 000 000 |
| Gemini 2.5 Flash Image (wersja testowa) | 1 000 000 000 |
| Gemini 2.5 Flash TTS | 4 000 000 |
| Gemini 2.5 Flash Lite | 1 000 000 000 |
| Gemini 2.5 Flash Lite (wersja testowa) | 1 000 000 000 |
| Gemini 2.0 Flash | 5 000 000 000 |
| Gemini 2.0 Flash Image | 1 000 000 000 |
| Gemini 2.0 Flash Lite | 5 000 000 000 |
| Multimodalne modele generatywne | | | | |
| Gemini 3.1 Flash Image (wersja testowa) 🍌 | 750 000 000 |
| Gemini 3.1 Flash Lite Image 🍌 | 1 000 000 000 |
| Gemini 3 Pro Image Preview 🍌 | 1 000 000 000 |
| Modele wektorów dystrybucyjnych | | | | |
| Osadzanie Gemini | 10 000 000 |

## Jak przejść na wyższy poziom

Aby przejść z poziomu bezpłatnego na płatny, musisz najpierw [skonfigurować rozliczenia w AI Studio](https://ai.google.dev/gemini-api/docs/billing?hl=pl).

Gdy Twój projekt spełni [określone kryteria](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl#usage-tiers), zostanie automatycznie uaktualniony do następnego poziomu. Przejście z poziomu bezpłatnego na poziom 1 zwykle następuje natychmiast, a kolejne przejścia na wyższe poziomy – w ciągu 10 minut. Aby sprawdzić swoje poziomy, otwórz [stronę Projekty](https://aistudio.google.com/projects?hl=pl) w AI Studio.

## Prośba o zwiększenie limitu częstotliwości

Każda wersja modelu ma powiązane ograniczanie liczby żądań (żądania na minutę, RPM).
Szczegółowe informacje o tych limitach znajdziesz na stronie [Limity AI Studio](https://aistudio.google.com/rate-limit?hl=pl).

[Prośba o zwiększenie limitu częstotliwości w przypadku wersji płatnej](https://forms.gle/ETzX94k8jf7iSotH9)

Nie gwarantujemy, że zwiększymy Twój limit, ale dołożymy wszelkich starań, aby rozpatrzyć Twoją prośbę.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-15 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-15 UTC."],[],[]]
