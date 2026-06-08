---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pl
fetched_at: 2026-06-08T15:00:43.154315+00:00
title: "Tworzenie aplikacji w\u00a0Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Tworzenie aplikacji w Google AI Studio

Na tej stronie opisujemy, jak używać Google AI Studio do szybkiego tworzenia (czyli "vibe
coding”) i wdrażania aplikacji, które testują najnowsze możliwości Gemini, takie jak
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) i [Live
API](https://ai.google.dev/gemini-api/docs/live?hl=pl). Google AI Studio obsługuje tworzenie **aplikacji internetowych** z pełnym stosem środowisk wykonawczych oraz **natywnych aplikacji na Androida** za pomocą Kotlina i Jetpack Compose – wszystko to za pomocą promptów w języku naturalnym.

## Rozpocznij

Zacznij stosować vibe coding w trybie [tworzenia](https://aistudio.google.com/apps?hl=pl) w Google AI Studio. Możesz zacząć tworzyć na kilka sposobów:

- **Zacznij od prompta**: w trybie tworzenia użyj okna do wprowadzania danych, aby opisać, co chcesz utworzyć. Wybierz AI Chips, aby dodać do prompta określone funkcje, takie jak generowanie obrazów lub dane Map Google. Możesz też powiedzieć, co chcesz zrobić, za pomocą przycisku zamiany mowy na tekst.
- **Przycisk „Szczęśliwy traf”**: jeśli potrzebujesz inspiracji, użyj przycisku „Szczęśliwy traf”, a Gemini wygeneruje prompta z pomysłem na projekt
  który pomoże Ci zacząć.
- **Remiksowanie projektu z galerii**: otwórz projekt z [Galerii
  aplikacji](https://aistudio.google.com/apps?source=showcase&hl=pl) i kliknij **Kopiuj aplikację**.

Po uruchomieniu prompta zobaczysz wygenerowany kod i pliki, a po prawej stronie pojawi się podgląd aplikacji na żywo.

## Co jest tworzone?

Gdy uruchomisz prompta, AI Studio utworzy kompletną aplikację. Za pomocą selektora platformy możesz utworzyć **aplikację internetową** lub **natywną aplikację na Androida**.

W przypadku **aplikacji internetowych** (domyślnie) AI Studio tworzy środowisko full stack, które obejmuje:

- **Po stronie klienta**: frontend internetowy (domyślnie React).
- **Po stronie serwera**: środowisko wykonawcze Node.js, które umożliwia bezpieczne wywołania interfejsu API, połączenia z bazą danych i korzystanie z pakietów npm.

W przypadku **aplikacji na Androida** AI Studio generuje projekt w Kotlinie i Jetpack Compose
który możesz wyświetlić w emulatorze w przeglądarce, zainstalować na urządzeniu fizycznym
i opublikować w Sklepie Play na potrzeby testowania. [Dowiedz się więcej o tworzeniu aplikacji na Androida](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pl).

Kod wygenerowany przez AI Studio możesz wyświetlić, klikając kartę **Kod** w panelu podglądu po prawej stronie. **Agent Antigravity** inteligentnie zarządza wieloma plikami w całym stosie, zapewniając prawidłowe propagowanie zmian.

### Agent Antigravity

**Agent Antigravity** to główna funkcja AI w [Google
Antigravity](https://antigravity.google?hl=pl), a teraz podstawowe komponenty
agenta obsługują tryb tworzenia w Google AI Studio. Wykracza on poza proste generowanie kodu, ponieważ utrzymuje kontekst całego projektu, zarządza wieloma plikami i rozumie złożone instrukcje, aby tworzyć niezawodne aplikacje full stack.

Najważniejsze funkcje:

- **Świadomość kontekstu**: utrzymuje kontekst poprzednich promptów i stanów plików.
- **Zarządzanie wieloma plikami**: obsługuje zależności w wielu plikach.
- **Zweryfikowane wykonanie**: weryfikuje aktualizacje kodu, aby ograniczyć halucynacje.

## Możliwości full stack

Google AI Studio odblokowuje możliwości nowoczesnego ekosystemu internetowego, umożliwiając tworzenie nie tylko prototypów po stronie klienta.

- **Środowisko wykonawcze po stronie serwera i npm:** korzystaj z obszernej biblioteki pakietów npm. Agent automatycznie identyfikuje i instaluje pakiety potrzebne do działania aplikacji (np. określone biblioteki do wizualizacji danych lub klientów interfejsu API). W razie potrzeby możesz też poprosić o konkretne pakiety.
- **Zarządzanie obiektami tajnymi**: bezpiecznie przechowuj klucze interfejsu API i obiekty tajne w menu
  **Ustawienia**. Są one dostępne w kodzie po stronie serwera, dzięki czemu są chronione przed ujawnieniem po stronie klienta.
- **Wieloosobowa rozgrywka**: twórz interaktywne aplikacje w czasie rzeczywistym bezpośrednio w
  AI Studio. Środowisko wykonawcze po stronie serwera zarządza stanem i połączeniami wymaganymi do interakcji użytkowników.
- **Firebase Firestore i uwierzytelnianie**: automatycznie udostępniaj i konfiguruj Firebase,
  w tym bazę danych Firestore (trwałe przechowywanie danych) i
  uwierzytelnianie Firebase (procesy logowania, w szczególności „Zaloguj się przez Google”).
  Agent obsługuje cały proces konfiguracji, a nawet pisze kod w aplikacji dla tych usług.
- **Integracje z Google Workspace**: połącz aplikację z interfejsami API Google Workspace, takimi jak Gmail, Arkusze, Dokumenty, Dysk, Kalendarz i inne. AI Studio automatycznie obsługuje całą konfigurację OAuth.

[Dowiedz się więcej o tworzeniu aplikacji full stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pl)

### Aplikacje na Androida

Możesz też tworzyć natywne aplikacje na Androida za pomocą Kotlina i Jetpack Compose.
Wyświetl podgląd aplikacji w emulatorze Androida w przeglądarce, zainstaluj ją na urządzeniu fizycznym za pomocą ADB w przeglądarce i opublikuj w Sklepie Play na potrzeby testów wewnętrznych.

[Dowiedz się więcej o tworzeniu aplikacji na Androida](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pl)

## Kontynuuj tworzenie

Gdy Google AI Studio wygeneruje początkowy kod aplikacji, możesz go dalej ulepszać:

### Tworzenie w Google AI Studio

- **Iteracja z Gemini**: użyj panelu czatu w **trybie tworzenia**, aby zapytaj Gemini
  o wprowadzenie zmian, dodanie nowych funkcji lub zmianę stylu.
- **Bezpośrednia edycja kodu**: otwórz **kartę Kod** w panelu podglądu, aby
  wprowadzać zmiany na żywo.

### Tworzenie poza AI Studio

W przypadku bardziej zaawansowanych procesów możesz wyeksportować kod i pracować w preferowanym środowisku:

- **Pobieranie i tworzenie lokalne**: wyeksportuj wygenerowany kod jako **plik
  ZIP** i zaimportuj go do edytora kodu.
- **Przesyłanie do GitHuba**: zintegruj kod z dotychczasowymi procesami tworzenia i
  wdrażania, przesyłając go do **repozytorium GitHub**.

## Najważniejsze funkcje

Google AI Studio zawiera kilka funkcji, które sprawiają, że proces tworzenia jest intuicyjny i wizualny:

- **Tworzenie aplikacji full stack i ich iteracyjne ulepszanie**: twórz aplikacje full stack za pomocą
  prompta i iteruj je w trybie czatu lub **trybie adnotacji**. Tryb adnotacji umożliwia wyróżnienie dowolnej części interfejsu aplikacji i opisanie żądanej zmiany.
- **Udostępnianie i wdrażanie aplikacji**: możesz udostępniać swoje projekty innym osobom, aby
  współpracować lub prezentować swoją pracę. Podczas udostępniania wywołania interfejsu API są wliczane do limitów użycia. Jeśli używasz płatnych modeli, mogą zostać naliczone opłaty. Gdy aplikacja będzie gotowa, wdróż ją w Cloud Run.
- **Galeria aplikacji**: Galeria aplikacji to wizualna biblioteka pomysłów na projekty.
  Możesz przeglądać możliwości Gemini, wyświetlać podgląd aplikacji i remiksować je, aby dostosować je do swoich potrzeb.

## Wdrażanie lub archiwizowanie aplikacji

Gdy aplikacja będzie gotowa, możesz ją wdrożyć:

- **Cloud Run**: wdróż aplikację jako skalowalną usługę.
  W zależności od użycia mogą obowiązywać opłaty za [Google Cloud Run](https://cloud.google.com/run?hl=pl). Więcej informacji o wdrażaniu znajdziesz w artykule
  [Wdrażanie z Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pl).
- **GitHub**: wyeksportuj projekt do repozytorium GitHub.

## Ograniczenia

Ta sekcja zawiera listę aktualnych ograniczeń trybu tworzenia w Google AI Studio.

### Zarządzanie kluczami interfejsu API

Gdy utworzysz nową aplikację, która korzysta z Gemini API, AI Studio automatycznie skonfiguruje klucz Gemini API jako obiekt tajny w środowisku po stronie serwera aplikacji.
Ten klucz możesz wyświetlić i nim zarządzać w panelu **Obiekty tajne**.

- **Automatyczna konfiguracja**: klucz `GEMINI_API_KEY` jest konfigurowany automatycznie – aby rozpocząć tworzenie, nie musisz niczego konfigurować ręcznie.
- **Tylko po stronie serwera**: klucze interfejsu API są wstrzykiwane do środowiska wykonawczego po stronie serwera i
  nigdy nie są uwzględniane w kodzie po stronie klienta.
- **Istniejące aplikacje**: w przypadku aplikacji utworzonych przed 14 maja 2026 r. agent automatycznie zaktualizuje integrację Gemini API do zalecanego podejścia po stronie serwera przy następnej modyfikacji funkcji Gemini w aplikacji.

### Wdrażanie poza Google AI Studio

- **Cloud Run**: gdy wdrożysz aplikację w Cloud Run z AI Studio, klucz interfejsu API zostanie
  bezpiecznie uwzględniony w środowisku po stronie serwera. Wdrożona aplikacja będzie używać Twojego klucza interfejsu API do wszystkich wywołań Gemini API przez użytkowników.
- **Pobieranie pliku ZIP**: jeśli pobierzesz aplikację jako plik ZIP, aby uruchomić ją w innym miejscu, musisz ustawić zmienną środowiskową `GEMINI_API_KEY` w środowisku hostingu. Ponieważ wywołania Gemini API w aplikacji są wykonywane z kodu po stronie serwera, klucz nie jest udostępniany użytkownikom.

### Błąd podczas udostępniania aplikacji

Jeśli udostępnisz aplikację, a użytkownik napotka błąd **403 Access Restricted** (Odmowa dostępu) podczas korzystania z udostępnionego adresu URL, może to być spowodowane jednym z tych powodów:

- **Rozszerzenia przeglądarki**: rozszerzenia prywatności, takie jak Privacy Badger, mogą blokować aplikację. Aby uniknąć błędu, wyłącz rozszerzenie.
- **Problemy z kompilacją**: mogą występować problemy z bieżącym kodem. Poproś agenta o „naprawienie problemów z kompilacją w bieżącym kodzie”, a następnie ponownie udostępnij adres URL.

## Najczęstsze pytania

### Co to jest tworzenie w AI Studio?

Tworzenie w AI Studio to platforma, która umożliwia przejście od prostego prompta do gotowej do wdrożenia aplikacji opartej na AI i korzystającej z Gemini. Opisz, co chcesz utworzyć, za pomocą prompta, a Gemini wygeneruje dla Ciebie aplikację. Możesz też przejrzeć naszą galerię, aby zobaczyć, co można zrobić za pomocą Gemini API, i remiksować aplikacje, aby dostosować je do swoich potrzeb.

### Jak tworzenie obsługuje mój klucz Gemini API?

Gdy utworzysz aplikację, która korzysta z Gemini API, AI Studio automatycznie skonfiguruje klucz Gemini API jako obiekt tajny po stronie serwera. Wywołania Gemini API w aplikacji są wykonywane z kodu po stronie serwera za pomocą tego klucza, więc nigdy nie są ujawniane w przeglądarce. Klucz interfejsu API możesz wyświetlić w panelu **Obiekty tajne** w Ustawieniach.

### Czy mój klucz interfejsu API jest ujawniany podczas udostępniania aplikacji?

Nie. Twój klucz interfejsu API jest przechowywany jako obiekt tajny po stronie serwera i nigdy nie jest uwzględniany w kodzie po stronie klienta. Gdy udostępnisz aplikację, inni użytkownicy będą mogli z niej korzystać, ale nie będą mogli zobaczyć Twojego klucza interfejsu API.

Podczas udostępniania aplikacji innym osobom wywołania interfejsu API są wliczane do limitów użycia.
Jeśli używasz płatnych modeli, mogą zostać naliczone opłaty. AI Studio wyświetli ostrzeżenie podczas konfiguracji i przed udostępnieniem, jeśli korzystanie z aplikacji może wiązać się z kosztami.

### Kto może zobaczyć moje aplikacje?

Domyślnie Twoja aplikacja jest prywatna. Możesz udostępnić aplikację innym użytkownikom, aby mogli z niej korzystać. Użytkownicy, którym udostępnisz aplikację, mogą zobaczyć jej kod i utworzyć jego kopię na własny użytek. Jeśli udostępnisz aplikację z uprawnieniami do edycji, inni użytkownicy będą mogli edytować jej kod.

### Czy mogę uruchamiać aplikacje poza AI Studio?

Tak. Możesz wdrożyć aplikację w
[Cloud Run](https://cloud.google.com/run?hl=pl) z AI Studio, co
zapewni jej publiczny adres URL z bezpiecznie skonfigurowanym kluczem interfejsu API w
środowisku po stronie serwera. Możesz też pobrać aplikację jako plik ZIP i hostować ją w innym miejscu – w tym celu musisz ustawić zmienną środowiskową `GEMINI_API_KEY` w środowisku hostingu. Ponieważ wywołania Gemini API są wykonywane z kodu po stronie serwera, Twój klucz pozostaje bezpieczny.

Więcej informacji o opcjach wdrażania znajdziesz w artykule [Wdrażanie z Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pl).

### Czy mogę tworzyć aplikacje lokalnie za pomocą własnych narzędzi, a następnie udostępniać je tutaj?

Ta funkcja nie jest jeszcze dostępna. Cieszymy się, że w przyszłości będziemy mogli obsługiwać więcej przypadków użycia aplikacji. Jeśli masz jakieś konkretne pomysły, przekaż nam swoją opinię.

### Jak mogę używać bazy danych lub innego miejsca na dane w swoich aplikacjach?

Aplikacje AI Studio to standardowe aplikacje działające w kontenerze Cloud Run. Możesz używać dowolnego rozwiązania do przechowywania danych, z którym możesz się połączyć przez sieć, o ile nie ma zapory sieciowej uniemożliwiającej dostęp z dynamicznego zakresu adresów IP.

Pracujemy nad dodaniem w przyszłości bezpośredniej obsługi przechowywania danych, którą będzie można skonfigurować bezpośrednio w AI Studio.

### Jak mogę uzyskać dostęp do mikrofonu, kamery internetowej i innych interfejsów Navigator API?

Aby widzowie wiedzieli, że aplikacja korzysta z ich kamery internetowej lub innych
urządzeń, wymagamy dodatkowego potwierdzenia, zanim aplikacja będzie mogła uzyskać dostęp
do tych [interfejsów Navigator API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator).
Twórcy aplikacji mogą dodać te prośby o uprawnienia do pliku `metadata.json` aplikacji. Na przykład:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Obsługiwane wartości dla `requestFramePermissions` to podzbiór
standardowych [funkcji kontrolowanych przez zasady](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### Jak mogę używać GitHuba w swoich aplikacjach?

Integracja AI Studio z GitHubem umożliwia utworzenie repozytorium na potrzeby pracy i zatwierdzenie najnowszych zmian. Obecnie nie obsługujemy pobierania zmian zdalnych.

### Czy mogę przyznać innym użytkownikom dostęp do edycji mojej aplikacji?

Ta funkcja nie jest jeszcze obsługiwana, ale wkrótce będzie dostępna.

### Dlaczego moja aplikacja została oznaczona jako naruszająca zasady?

Mamy systemy, które automatycznie sprawdzają aplikacje pod kątem zgodności z naszymi zasadami. Jeśli stwierdzimy, że aplikacja narusza nasze zasady, zostanie usunięta z AI Studio. Naruszenia zasad mogą obejmować m.in.:

- aplikacje zawierające złośliwe oprogramowanie, wyłudzanie informacji lub podszywanie się pod inne osoby;
- aplikacje, które wyświetlają lub rozpowszechniają treści naruszające zasady dotyczące materiałów wizualnych przedstawiających wykorzystywanie seksualne dzieci;
- aplikacje, które wyświetlają lub rozpowszechniają treści naruszające zasady dotyczące nękania;
- aplikacje, które wyświetlają lub rozpowszechniają treści naruszające zasady dotyczące szerzenia nienawiści;
- aplikacje, które wyświetlają lub rozpowszechniają treści naruszające zasady dotyczące handlu ludźmi;
- aplikacje, które wyświetlają lub rozpowszechniają treści naruszające zasady dotyczące treści o charakterze jednoznacznie seksualnym;
- aplikacje, które wyświetlają lub rozpowszechniają treści naruszające zasady dotyczące przemocy i okrucieństwa;
- aplikacje, które wyświetlają lub rozpowszechniają treści naruszające zasady dotyczące szkodliwych lub niebezpiecznych treści.

Jeśli Twoja aplikacja została oznaczona jako naruszająca zasady i uważasz, że doszło do pomyłki, możesz przesłać odwołanie. Powtarzające się naruszenia naszych zasad mogą spowodować utratę dostępu do AI Studio.

### Jakie są moje obowiązki jako dewelopera aplikacji?

Przypominamy, że jako właściciel aplikacji odpowiadasz za jej działanie i wszystkie dane, które przetwarza. Obejmuje to m.in.:

- **Zgodność z przepisami i prawa osób trzecich:** musisz dopilnować, aby Twoja aplikacja była zgodna z obowiązującymi przepisami i nie naruszała praw innych osób, w tym praw własności intelektualnej i praw do prywatności.
- **Monitorowanie treści:** w przypadku innych usług używanych przez aplikację mogą obowiązywać dodatkowe warunki. Na przykład [Warunki korzystania z Google Cloud](https://cloud.google.com/terms?hl=pl), które obowiązują w przypadku Firestore, wymagają od klientów hostujących treści osób trzecich publikowania zasad określających, jakie treści są zabronione (np. treści niezgodne z prawem), oraz monitorowania obecności takich treści.
- **Bezpieczne wdrożenie:** musisz wdrożyć niezbędne zabezpieczenia i narzędzia do moderowania, aby zapobiec niewłaściwemu użyciu aplikacji.

Zapoznaj się z [ograniczeniami dotyczącymi użytkowania](https://ai.google.dev/gemini-api/terms?hl=pl#use-restrictions)
w Warunkach korzystania z usługi.

### Jakie warunki obowiązują w przypadku aplikacji w galerii aplikacji w AI Studio?

O ile nie zaznaczono inaczej, w przypadku korzystania z aplikacji prezentowanych w galerii aplikacji w AI Studio obowiązują [dodatkowe warunki korzystania z usługi Gemini API](https://ai.google.dev/gemini-api/terms?hl=pl).

## Co dalej?

- [Tworzenie aplikacji full stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pl) (internetowych)
- [Tworzenie aplikacji na Androida](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pl)
- Przykłady znajdziesz w [Galerii aplikacji](https://aistudio.google.com/apps?source=showcase&hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-19 UTC."],[],[]]
