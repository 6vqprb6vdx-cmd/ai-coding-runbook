---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pl
fetched_at: 2026-10-12T06:58:38.227808+00:00
title: "Tworzenie aplikacji na Androida w\u00a0Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Tworzenie aplikacji na Androida w Google AI Studio

Google AI Studio umożliwia tworzenie natywnych aplikacji na Androida na podstawie prompta w języku naturalnym. Opisz aplikację, którą chcesz utworzyć, a
[Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pl#antigravity-agent)
wygeneruje kompletny projekt w Kotlinie i [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=pl). W przeglądarce możesz wyświetlić podgląd aplikacji w emulatorze Androida, zainstalować ją na urządzeniu fizycznym i opublikować na potrzeby testowania.

## Rozpocznij

Aby zacząć tworzyć aplikację na Androida:

1. W panelu użytkownika po lewej stronie otwórz tryb [tworzenia](https://aistudio.google.com/apps?hl=pl) w Google AI Studio.
2. W selektorze platform wybierz **Android**.
3. Wpisz prompta opisującego aplikację, którą chcesz utworzyć (np. *„Utwórz element śledzenia codziennych zadań z pamięcią lokalną”* lub *„Utwórz prosty Kalkulator”*).
4. Agent wygeneruje projekt i uruchomi go w emulatorze Androida w przeglądarce.

Następnie możesz iterować aplikację za pomocą panelu czatu, tak jak w przypadku aplikacji internetowych. Agent zarządza wszystkimi plikami w projekcie aplikacji na Androida i propaguje zmiany w bazie kodu.

## Emulator Androida w przeglądarce

Emulator Androida działa w całości w chmurze i przesyła strumieniowo dane do przeglądarki.
Nie musisz instalować pakietu Android SDK, Android Studio ani emulatora lokalnego.

Emulator zapewnia:

- **Symulację urządzenia podobnego do Pixela**: możesz dotykać, przewijać i wchodzić w interakcję z aplikacją
  tak jak na prawdziwym urządzeniu.
- **Obsługę obracania**: możesz przełączać się między orientacją pionową a poziomą.
- **Podgląd na żywo**: gdy agent wprowadzi zmiany w kodzie, aplikacja zostanie ponownie skompilowana, a
  emulator automatycznie się odświeży.

### Ograniczenia emulatora

Emulator w przeglądarce nie obsługuje wszystkich funkcji sprzętowych. W emulatorze nie są dostępne te funkcje:

- Aparat i robienie zdjęć
- NFC i Bluetooth
- GPS (lokalizacja jest symulowana)
- Usługi Google Play (Logowanie przez Google, Mapy i inne funkcje usług Play działają na prawdziwym urządzeniu, ale nie w emulatorze)

## Instalacja na urządzeniu za pomocą ADB

Skompilowany plik APK możesz zainstalować bezpośrednio na fizycznym urządzeniu z Androidem podłączonym do komputera przez USB. Do komunikacji z urządzeniem przez przeglądarkę używana jest funkcja
[WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=pl). Nie musisz instalować lokalnie narzędzia ADB.

### Wymagania wstępne

- Przeglądarka Chrome lub Edge obsługująca WebUSB.
- Urządzenie z Androidem, na którym włączono
  [opcje programisty i debugowanie USB](https://developer.android.com/studio/debug/dev-options?hl=pl).
- Kabel USB łączący urządzenie z komputerem.

### Instalowanie aplikacji na urządzeniu

1. W panelu podglądu kliknij **Zainstaluj na urządzeniu**.
2. W selektorze urządzeń USB w przeglądarce wybierz urządzenie z Androidem.
3. Plik APK zostanie przesłany i zainstalowany na urządzeniu.
4. Aplikacja uruchomi się automatycznie.

## Publikowanie w Sklepie Play

Aplikację na Androida możesz opublikować na
[ścieżce testów wewnętrznych w Konsoli Google Play](https://play.google.com/console?hl=pl), co pozwoli Ci udostępnić ją maksymalnie 100 testerom.

### Wymagania wstępne

- Konto dewelopera w [Google Play](https://play.google.com/console/signup?hl=pl) (wymaga jednorazowej opłaty rejestracyjnej w wysokości 25 USD).
- Uzupełniony profil dewelopera w Konsoli Play.

### Publikowanie aplikacji

1. W Google AI Studio otwórz **Ustawienia > Opublikuj**.
2. Kliknij **Opublikuj w Sklepie Play**.
3. Zaloguj się na konto dewelopera w Google Play.
4. AI Studio podpisze plik APK, utworzy stronę aplikacji (lub prześle nową wersję) i opublikuje ją na ścieżce testów wewnętrznych.
5. Otrzymasz link, który możesz udostępnić testerom.

AI Studio automatycznie zarządza podpisywaniem plików APK za pomocą zarządzanego magazynu kluczy. Stronę aplikacji (ikonę, zrzuty ekranu, opis) możesz dostosować później w Konsoli Play.

## Co jest generowane

Gdy tworzysz aplikację na Androida, agent generuje standardowy projekt oparty na Gradle o tej strukturze:

- **Konfiguracja kompilacji**: `build.gradle.kts` pliki (na poziomie projektu i aplikacji)
  z użyciem Kotlin DSL.
- **Warstwa interfejsu**: [komponenty](https://developer.android.com/develop/ui/compose?hl=pl)
  Jetpack Compose z [motywem Material 3](https://m3.material.io/).
- **Architektura**: architektura z jednym działaniem z klasami ViewModel i klasami danych.
- **Zasoby**: `AndroidManifest.xml`, grafiki, ciągi znaków i inne zasoby Androida.

Agent automatycznie zarządza zależnościami Gradle, dodając w razie potrzeby pakiety z repozytoriów Maven i Google.

Wygenerowany kod możesz wyświetlić i edytować na karcie **Kod** w panelu podglądu. Aby kontynuować tworzenie w Android Studio, pobierz projekt jako **plik ZIP**.

## Ograniczenia

Tworzenie aplikacji na Androida w AI Studio ma te ograniczenia:

### Ograniczenia platform

- **Tylko po stronie klienta**: aplikacje na Androida nie zawierają komponentu po stronie serwera.
  Funkcje wymagające środowiska wykonawczego po stronie serwera (zarządzanie tajnymi danymi, tryb wieloosobowy, Firebase, interfejsy Google Workspace API) są niedostępne.
- **Architektura z jednym działaniem**: obsługiwane są tylko projekty z jednym działaniem i jednym modułem.
- **Tylko Jetpack Compose**: aplikacje używają Kotlina i Jetpack Compose. Układy Java i XML nie są obsługiwane.
- **Brak NDK i kodu natywnego**: kod C i C++ nie jest obsługiwany.
- **Brak Wear OS i Androida TV**: obsługiwane są tylko telefony i tablety.

### Ograniczenia eksportu

- **Tylko pobieranie ZIP**: projekt możesz pobrać jako plik ZIP. Eksport do GitHub nie jest jeszcze dostępny w przypadku projektów na Androida.

## Co dalej?

- [Tworzenie aplikacji w Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pl)
- [Tworzenie aplikacji pełnostosowych](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pl) (internetowych)
- Przykłady znajdziesz w [Galerii aplikacji](https://aistudio.google.com/apps?source=showcase&hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-08-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-08-19 UTC."],[],[]]
