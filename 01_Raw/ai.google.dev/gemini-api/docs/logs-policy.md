---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=pl
fetched_at: 2026-09-07T05:31:53.069167+00:00
title: "Logowanie i\u00a0udost\u0119pnianie danych \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Logowanie i udostępnianie danych

Na tej stronie opisujemy przechowywanie logów
[Gemini API](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pl)i zarządzanie nimi. Są to dane interfejsu
API należące do dewelopera, pochodzące z obsługiwanych wywołań Gemini API w projektach z włączonymi płatnościami. Logi obejmują cały proces od żądania użytkownika do odpowiedzi modelu.
Te logi, które są prywatne dla Twojego projektu w chmurze Google Cloud, są oddzielone od wszelkich
logów przechowywanych wyłącznie na potrzeby [monitorowania nadużyć](https://ai.google.dev/gemini-api/docs/usage-policies?hl=pl).

## Dane, które można udostępniać

Jako właściciel projektu możesz włączyć logowanie wywołań Gemini API na własny użytek lub w celu przekazywania opinii i udostępniania ich Google, aby pomóc nam w ciągłym ulepszaniu naszych modeli.

Jeśli włączysz logowanie, możesz pomóc nam w tworzeniu systemów AI, które będą nadal przydatne dla deweloperów w różnych dziedzinach i przypadkach użycia. W tym celu możesz udostępniać te dane na potrzeby ulepszania usług i trenowania modeli:

- **Zbiory danych:** użyj interfejsu Logi i zbiory danych w Google AI Studio, aby wybrać logi (żądania, odpowiedzi, metadane itp.) z obsługiwanych wywołań Gemini API. Możesz je udostępnić, dodając je do zbiorów danych. Podczas tworzenia zbioru danych możesz zrezygnować z udostępniania.
- **Opinie:** podczas przeglądania logów możesz przekazywać opinie, w tym oceny (kciuk w górę lub w dół) oraz wszelkie pisemne komentarze.

Gdy udostępniasz Google zbiór danych, Twoje logi w tym zbiorze, w tym
żądania i odpowiedzi, będą przetwarzane zgodnie z naszymi
[Warunkami korzystania](https://developers.google.com/terms?hl=pl) z
"[Usług bezpłatnych](https://ai.google.dev/gemini-api/terms?hl=pl#data-use-unpaid),"
Oznacza to, że zbiór danych może być używany do rozwijania i ulepszania usług Google
produktów, usług i technologii uczenia maszynowego, w tym do ulepszania i
szkolenia naszych modeli. **Nie podawaj danych osobowych, poufnych ani wrażliwych.**

## Jak wykorzystujemy Twoje dane

Logi są przechowywane przez domyślny maksymalny okres 55 dni. Po tym okresie logi są automatycznie oznaczane do usunięcia. Okres przechowywania projektu można zaktualizować w AI Studio, aby automatycznie oznaczać logi do usunięcia po 7, 14, 28 lub 55 dniach.

[Zbiory danych](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pl) można tworzyć w celu przechowywania logów, które Cię interesują, przez okres dłuższy niż ustawiony okres przechowywania. Można je wykorzystywać w dalszych przypadkach użycia i
opcjonalnie udostępniać na potrzeby ulepszania modeli. Logi przechowywane w zbiorach danych nie mają ustawionych okresów przechowywania.

Domyślnie logowanie jest dostępne tylko w projektach z włączonymi płatnościami,
dlatego prompty i odpowiedzi w logach nie są używane do ulepszania ani
rozwijania usług zgodnie z naszymi [Warunkami](https://developers.google.com/terms?hl=pl)
korzystania z danych.

Jeśli zdecydujesz się udostępniać Google zbiory danych z logami, będą one używane jako dane demonstracyjne z rzeczywistych przypadków użycia, aby lepiej zrozumieć różnorodność domen i kontekstów, w których używane są systemy i aplikacje AI. Te dane mogą być używane do poprawy jakości modelu oraz do trenowania i oceniania przyszłych modeli i usług. Dane te są przetwarzane zgodnie z naszymi warunkami korzystania z danych
w przypadku [usług bezpłatnych](https://ai.google.dev/gemini-api/terms?hl=pl#data-use-unpaid).

W związku z tym osoby weryfikujące treści mogą odczytywać i przetwarzać udostępniane przez Ciebie dane wejściowe i wyjściowe interfejsu API oraz dodawać do nich adnotacje. Zanim dane zostaną użyte do ulepszania modelu, Google podejmuje działania mające na celu ochronę prywatności użytkowników. Obejmuje to odłączenie tych danych od Twojego konta Google, klucza API i projektu w chmurze, zanim weryfikatorzy je zobaczą lub opatrzą adnotacjami.

## Uprawnienia do danych

Jeśli zdecydujesz się udostępniać dane interfejsu API, potwierdzasz, że masz niezbędne uprawnienia, aby Google mogło przetwarzać i wykorzystywać te dane zgodnie z opisem w tej dokumentacji. **Nie udostępniaj logów zawierających informacje poufne, wrażliwe ani zastrzeżone, które zostały uzyskane w ramach płatnej usługi.**
Licencja, której udzielasz Google w sekcji „[Przesyłanie treści](https://developers.google.com/terms?hl=pl#b_submission_of_content)” w Warunkach korzystania z interfejsu API, obejmuje również, w zakresie wymaganym przez obowiązujące prawo, wszelkie treści (np. prompty, w tym powiązane instrukcje systemowe, treści zapisane w pamięci podręcznej i pliki takie jak obrazy, filmy czy dokumenty) przesyłane do usług oraz wszelkie wygenerowane odpowiedzi.

## Udostępnianie danych i opinie

Możesz pomóc nam w rozwoju badań nad AI, Gemini API i Google AI Studio, udostępniając swoje dane jako przykłady. Dzięki temu będziemy mogli stale ulepszać nasze modele w różnych kontekstach i tworzyć systemy AI, które będą nadal przydatne dla deweloperów w różnych dziedzinach i przypadkach użycia.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-04 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-04 UTC."],[],[]]
