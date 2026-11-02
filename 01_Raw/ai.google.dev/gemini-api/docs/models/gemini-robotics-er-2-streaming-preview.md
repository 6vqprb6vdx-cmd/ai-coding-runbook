---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=pl
fetched_at: 2026-11-02T07:20:51.789749+00:00
title: "Przesy\u0142anie strumieniowe Gemini Robotics ER\u00a02 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Przesyłanie strumieniowe Gemini Robotics ER 2

Gemini Robotics ER 2 Streaming to model wizyjno-językowy (VLM) do robotyki zoptymalizowany pod kątem strumieniowego przesyłania tekstu w czasie rzeczywistym za pomocą interfejsu Live API. Akceptuje dane wejściowe w formie tekstu, obrazu, filmu i dźwięku oraz obsługuje dwukierunkowe strumieniowanie z wywoływaniem funkcji.

[Wypróbuj w Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=pl)

## Dokumentacja

Aby dowiedzieć się więcej o funkcjach i możliwościach, odwiedź stronę [Live API for robotics](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl).

## gemini-robotics-er-2-streaming-preview

### Gemini Robotics ER 2 (wersja testowa)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | `gemini-robotics-er-2-preview` |
| saveObsługiwane typy danych | **Dane wejściowe**  Tekst, obrazy, filmy, dźwięk  **Dane wyjściowe**  Tekst |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  131 072  **Limit tokenów wyjściowych**  65 536 |
| handymanMożliwości | **[Generowanie dźwięku](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl)**  Nieobsługiwane  **[Zapisywanie w pamięci podręcznej](https://ai.google.dev/gemini-api/docs/caching?hl=pl)**  Obsługiwane  **[Wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl)**  Obsługiwane  **[Korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl)**  Obsługiwane  **[Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)**  Obsługiwane  **[Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)**  Obsługiwane  **[Powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)**  Obsługiwane  **[Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)**  Nieobsługiwane  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl)**  Nieobsługiwane  **[Szukaj groundingu](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)**  Obsługiwane  **[Uporządkowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl)**  Obsługiwane  **[Myślę](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)**  Obsługiwane  **[Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)**  Obsługiwane |
| speedOpcje wykorzystania | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl)**  Obsługiwane  **[wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl)**  Nieobsługiwane  **[Wnioskowanie o priorytecie](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl)**  Nieobsługiwane |
| 123Wersje | Więcej informacji znajdziesz we wzorcach wersji modelu .  - Podgląd: `gemini-robotics-er-2-preview` |
| calendar\_monthOstatnia aktualizacja | Lipiec 2026 r. |
| id\_cardKarta modelu | [Karta modelu](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=pl) |
| paidCeny | [Ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#gemini-robotics-er-2) |

### Gemini Robotics ER 2 Streaming Preview

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | `gemini-robotics-er-2-streaming-preview` |
| saveObsługiwane typy danych | **Dane wejściowe**  Tekst, obrazy, filmy, dźwięk  **Dane wyjściowe**  Tekst |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  131 072  **Limit tokenów wyjściowych**  65 536 |
| handymanMożliwości | **[Generowanie dźwięku](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl)**  Nieobsługiwane  **[Zapisywanie w pamięci podręcznej](https://ai.google.dev/gemini-api/docs/caching?hl=pl)**  Nieobsługiwane  **[Wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl)**  Nieobsługiwane  **[Korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl)**  Nieobsługiwane  **[Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)**  Nieobsługiwane  **[Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)**  Obsługiwane  **[Powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)**  Nieobsługiwane  **[Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)**  Nieobsługiwane  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl)**  Obsługiwane  **[Szukaj groundingu](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)**  Obsługiwane  **[Uporządkowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl)**  Nieobsługiwane  **[Myślę](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)**  Obsługiwane  **[Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)**  Nieobsługiwane |
| speedOpcje wykorzystania | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl)**  Nieobsługiwane  **[wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl)**  Nieobsługiwane  **[Wnioskowanie o priorytecie](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl)**  Nieobsługiwane |
| 123Wersje | Więcej informacji znajdziesz we wzorcach wersji modelu .  - Podgląd: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthOstatnia aktualizacja | Lipiec 2026 r. |
| id\_cardKarta modelu | [Karta modelu](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=pl) |
| paidCeny | [Ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#gemini-robotics-er-2-streaming) |

### Gemini Robotics ER 1.6 (wersja testowa)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | `gemini-robotics-er-1.6-preview` |
| saveObsługiwane typy danych | **Dane wejściowe**  Tekst, obrazy, filmy, dźwięk  **Dane wyjściowe**  Tekst |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  131 072  **Limit tokenów wyjściowych**  65 536 |
| handymanMożliwości | **[Generowanie dźwięku](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl)**  Nieobsługiwane  **[Zapisywanie w pamięci podręcznej](https://ai.google.dev/gemini-api/docs/caching?hl=pl)**  Obsługiwane  **[Wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl)**  Obsługiwane  **[Korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl)**  Obsługiwane  **[Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl)**  Obsługiwane  **[Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)**  Obsługiwane  **[Powiązanie ze źródłami informacji przy użyciu Map Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl)**  Obsługiwane  **[Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)**  Nieobsługiwane  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=pl)**  Nieobsługiwane  **[Szukaj groundingu](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)**  Obsługiwane  **[Uporządkowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl)**  Obsługiwane  **[Myślę](https://ai.google.dev/gemini-api/docs/thinking?hl=pl)**  Obsługiwane  **[Kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl)**  Obsługiwane |
| speedOpcje wykorzystania | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl)**  Obsługiwane  **[wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl)**  Nieobsługiwane  **[Wnioskowanie o priorytecie](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl)**  Nieobsługiwane |
| 123Wersje | Więcej informacji znajdziesz we wzorcach wersji modelu .  - Wyłącz: `gemini-robotics-er-1.6-preview` |
| calendar\_monthOstatnia aktualizacja | Grudzień 2025 r. |
| cognition\_2Granica wiedzy | Styczeń 2025 r. |

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-29 UTC."],[],[]]
