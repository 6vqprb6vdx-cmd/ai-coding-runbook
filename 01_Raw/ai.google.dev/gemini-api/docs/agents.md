---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=pl
fetched_at: 2026-06-29T05:32:54.988272+00:00
title: "Przegl\u0105d agent\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Przegląd agentów

Zarządzane agenty w interfejsie Gemini API zapewniają konfigurowalny
szablon agenta. Pojedyncze wywołanie interfejsu API udostępnia piaskownicę Linuksa, w której agent samodzielnie analizuje, wykonuje kod, zarządza plikami i przegląda internet.

[rocket\_launch

Krótkie wprowadzenie

Wykonaj pierwsze połączenie z agentem, przesyłaj strumieniowo odpowiedzi i utwórz własnego agenta.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl)
[smart\_toy

Agent Antigravity

Możliwości, narzędzia, multimodalne wprowadzanie danych i ceny domyślnego agenta.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl)
[experiment

Agenty w AI Studio

Wizualne środowisko do tworzenia prototypów agentów bez pisania kodu.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pl)

## Dostępne agenty zarządzane

- **[Agent Antigravity:](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl)** agent do zwykłych obciążeń, zarządzany, oparty na Gemini 3.5 Flash. Uruchamia kod, zarządza plikami i przeszukuje internet w bezpiecznej piaskownicy Linuksa hostowanej przez Google. Możesz rozszerzyć go o własne instrukcje, umiejętności i dane, aby [utworzyć agenta niestandardowego](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl)**: autonomiczny agent badawczy, który planuje, wykonuje i syntetyzuje wieloetapowe zadania badawcze w przypadkach użycia takich jak analiza rynku, należyta staranność i przeglądy literatury.

## Bezpieczeństwo i sprawdzone metody

Każdy agent działa w środowisku piaskownicy, które jest izolowane na poziomie systemu operacyjnego.
Piaskownica ma domyślnie nieograniczony dostęp wychodzący do sieci. Możesz ograniczyć lub wyłączyć dostęp do sieci za pomocą listy dozwolonych.

### Dostęp do sieci

Domyślnie środowiska mają nieograniczony dostęp do sieci wychodzącej. Użyj `network`listy dozwolonych, aby ograniczyć ruch wychodzący do określonych domen lub wzorców z wieloznacznymi symbolami. Szczegółowe informacje o konfiguracji znajdziesz w artykule [Lista dozwolonych sieci](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pl#network_allow_list) (AI Studio) lub [Reguły sieciowe](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl#with_network_rules) (API).

### Narzędzia i interfejsy API zewnętrzne

Możesz połączyć narzędzia zewnętrzne i interfejsy API, aby rozszerzyć możliwości agenta. Używaj tylko narzędzi z zaufanych źródeł i ograniczaj uprawnienia do niezbędnego minimum. Dane logowania można bezpiecznie wstrzykiwać za pomocą transformacji nagłówków wychodzącego serwera proxy. Nigdy nie są one ujawniane w piaskownicy. Agent może używać dowolnych danych logowania, do których ma dostęp, dlatego podawaj tylko te dane, których pełny zakres chcesz przyznać.

- Używaj kont usługi lub kluczy API o jak najmniejszych uprawnieniach.
- Preferuj krótkoterminowe tokeny zamiast długoterminowych kluczy.
- Podawaj tylko te dane logowania, których pełny zakres chcesz przyznać.
- Regularnie zmieniaj dane logowania.

Szczegółowe informacje o konfigurowaniu przekształceń nagłówków znajdziesz w sekcji [Dane logowania](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#credentials).

### Nadzór ze strony człowieka

Zawsze sprawdzaj wyniki (wygenerowany kod, przekształcenia danych, zmiany konfiguracji) przed ich wdrożeniem, zwłaszcza w przypadku zadań, które modyfikują dane lub wchodzą w interakcje z systemami zewnętrznymi.

## Ceny

Agenci zarządzani korzystają z [modelu płatności według wykorzystania](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#pricing-for-agents) opartego na tokenach modelu Gemini i użyciu narzędzi. Pojedyncza interakcja może wywołać wiele pętli wnioskowania, które zwykle zużywają od 100 tys. do 3 mln tokenów. W okresie korzystania z wersji przedpremierowej za moc obliczeniową środowiska **nie są pobierane opłaty**. Szczegółowe informacje o kosztach poszczególnych zadań znajdziesz w sekcji [Szacowane koszty](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl#availability-and-pricing).

## Limity

| Limit | Opis |
| --- | --- |
| **Okres istnienia środowiska** | Środowiska są trwale usuwane po 7 dniach braku aktywności. |
| **Wyłączanie maszyn wirtualnych** | Maszyny wirtualne wyłączają się po krótkim okresie bezczynności, aby oszczędzać zasoby. Kolejne żądanie przywraca stan (z uruchomieniem „na zimno”). |
| **Fabrycznie zainstalowane oprogramowanie** | Środowisko oparte na Ubuntu z Pythonem 3.12 i Node.js 22. Więcej informacji o obrazie bazowym środowiska znajdziesz w sekcji [Preinstalowane oprogramowanie](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#pre-installed-software). |
| **Maksymalna liczba agentów** | Możesz mieć maksymalnie 1000 zarządzanych agentów. |

## Platformy agentów

Możesz też tworzyć agentów z Gemini za pomocą tych platform i pakietów SDK:

- [**LangChain / LangGraph:**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=pl) twórz złożone przepływy aplikacji z zachowywaniem stanu i systemy wieloagentowe przy użyciu struktur grafów.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=pl) połącz agenty Gemini z danymi prywatnymi, aby korzystać z przepływów pracy opartych na RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=pl) koordynuj współpracę autonomicznych agentów AI odgrywających różne role.
- [**Vercel AI SDK:**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=pl) tworzenie interfejsów użytkownika i agentów opartych na AI w JavaScript/TypeScript.
- [**Google ADK:**](https://google.github.io/adk-docs/get-started/python/) platforma open source do tworzenia i koordynowania interoperacyjnych agentów AI.
- [**Antigravity SDK:**](https://antigravity.google/product/antigravity-sdk?hl=pl) twórz autonomiczne agenty AI za pomocą tych samych narzędzi, pętli agenta i zarządzania kontekstem, które są używane w Google Antigravity. Możesz programować w Pythonie.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-20 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-20 UTC."],[],[]]
