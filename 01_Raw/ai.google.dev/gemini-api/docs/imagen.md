---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=pl
fetched_at: 2026-09-28T06:09:05.887019+00:00
title: "Generowanie obraz\u00f3w za pomoc\u0105 Imagen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)

Prześlij opinię

# Generowanie obrazów za pomocą Imagen

Imagen to starszy model Google do generowania obrazów. Został on wyłączony i nie jest już dostępny w interfejsie Gemini API.

## Przejdź na Nano Banana

Przejdź na Nano Banana, aby generować obrazy:

- **Nazwa modelu:** zamiast nazw modeli Imagen używaj `gemini-2.5-flash-image` (lub modeli Nano Banana 2, np. `gemini-3.1-flash-image`).
- **Metoda:** używaj `client.models.generate_content` zamiast `client.models.generate_images`.
- **Obsługa odpowiedzi:** Nano Banana zwraca części treści zawierające dane obrazu zamiast konkretnego obiektu odpowiedzi obrazu.

Szczegółowe informacje i przykłady znajdziesz w [przewodniku po generowaniu obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-18 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-18 UTC."],[],[]]
