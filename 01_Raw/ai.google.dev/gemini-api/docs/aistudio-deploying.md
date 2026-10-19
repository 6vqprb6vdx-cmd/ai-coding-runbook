---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pl
fetched_at: 2026-10-19T05:32:34.349624+00:00
title: "Wdra\u017canie z Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wdrażanie z Google AI Studio

Google AI Studio umożliwia wdrażanie aplikacji pełnostosowych bezpośrednio z trybu tworzenia. Umożliwia to szybkie przejście od prototypu do zarządzanego, skalowalnego środowiska produkcyjnego.

## Opcje wdrażania

Wymagania dotyczące wdrażania aplikacji w trybie tworzenia AI Studio zależą od używanego pakietu:

- [**Poziom startowy Google Cloud:**](https://docs.cloud.google.com/docs/starter-tier?hl=pl) umożliwia kwalifikującym się kontom publikowanie maksymalnie 2 aplikacji pełnostosowych bez konfigurowania projektu w chmurze Google Cloud ani konta rozliczeniowego.
- **Wdrożenie standardowe:** wymaga projektu Google Cloud połączonego z kontem AI Studio i włączonych płatności w tym projekcie.

## Informacje o poziomie Starter

Poziom startowy Google Cloud zapewnia uproszczoną ścieżkę wdrażania aplikacji w Google Cloud bezpośrednio z Google AI Studio w przypadku kwalifikujących się kont. Nie musisz konfigurować pełnego środowiska Google Cloud ani konta rozliczeniowego.

Każde wdrożenie w Google AI Studio tworzy odpowiednią usługę w Cloud Run. W przypadku usług wdrożonych w Google AI Studio w ramach pakietu Starter obowiązują te ograniczenia:

- Możesz wdrożyć maksymalnie 2 usługi.
- Usługi są wdrażane w [jednym regionie Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=pl).

### Kto może korzystać z poziomu startowego

Nie wszystkie konta kwalifikują się do korzystania z poziomu Starter Google Cloud. Twoje konto może nie kwalifikować się do programu, jeśli spełnia którykolwiek z tych warunków:

- Korzystasz z konta Google Workspace (w tym płatnych lub bezpłatnych subskrypcji Google Workspace, Google Workspace for Education lub Google for Nonprofits).
- Masz aktywne lub poprzednie płatne konto rozliczeniowe Google Cloud.
- Nie mamy wystarczających dowodów na podstawie aktywności na Twoim koncie, aby przyznać Ci obecnie dostęp do poziomu startowego.

Zespół pomocy Google AI Studio nie może zmienić kwalifikacji do poziomu Starter. Jeśli Twoje konto nie spełnia wymagań, dołącz konto rozliczeniowe i użyj [standardowego wdrażania](#standard-deployment), aby opublikować aplikacje.

## Wdrażanie na poziomie Starter

Po zaprojektowaniu aplikacji w trybie tworzenia wdróż ją na poziomie Starter:

1. W prawym górnym rogu kliknij przycisk **Opublikuj**.
2. Kliknij **Rozpocznij**.
3. Kliknij **Opublikuj aplikację**.

Po zakończeniu wdrażania AI Studio udostępnia adres URL Cloud Run, pod którym możesz uzyskać dostęp do aktywnej aplikacji.

## Niestandardowe adresy URL w AI Studio

Podczas publikowania aplikacji z Google AI Studio możesz ustawić niestandardową, łatwą do zapamiętania subdomenę w sekcji `ai.studio` (np. `https://your-app-name.ai.studio`).

Google AI Studio wymaga, aby subdomeny były globalnie unikalne we wszystkich projektach i przydziela je według kolejności zgłoszeń. Jeśli inna nazwa projektu jest już używana, AI Studio poprosi Cię o wybranie innej. Jeśli wycofasz publikację aplikacji lub ją usuniesz, jej niestandardowy adres URL zostanie zwolniony i będzie dostępny dla innych użytkowników.

### Ustawianie niestandardowego adresu URL

Aby ustawić lub zaktualizować niestandardowy adres URL aplikacji:

1. Otwórz aplikację w Google AI Studio w trybie **Tworzenie**.
2. W prawym górnym rogu kliknij **Opublikuj**.
3. W konfiguracji wdrożenia wpisz preferowaną subdomenę w polu **Niestandardowy URL** lub zaakceptuj sugerowany adres URL.
4. Kliknij **Opublikuj aplikację**.

Aby przenieść istniejący niestandardowy adres URL do innej aplikacji, musisz najpierw wycofać z publikacji lub usunąć aplikację, do której jest przypisany ten niestandardowy adres URL, a następnie opublikować nową aplikację, używając wybranej subdomeny.

### Zgłaszanie problemów dotyczących znaków towarowych lub praw autorskich

Niestandardowe subdomeny muszą być zgodne z [Warunkami korzystania z usług Google](https://policies.google.com/terms?hl=pl). Jeśli zauważysz niestandardowy adres URL, który narusza znak towarowy lub wykorzystuje nazwę chronioną prawem autorskim bez pozwolenia, możesz to zgłosić za pomocą [narzędzia Google do rozwiązywania problemów prawnych](https://support.google.com/legal/troubleshooter/1114905?hl=pl).

## Wdrożenie standardowe

W miarę rozwoju aplikacji możesz potrzebować funkcji wykraczających poza poziom Starter, takich jak wyższe limity, większe zasoby obliczeniowe lub inne usługi Google Cloud niedostępne na poziomie Starter. Aby odblokować te funkcje, możesz przekształcić w pełni zarządzany projekt w ramach pakietu Starter w standardowy projekt Google Cloud.

Dzięki temu możesz bezproblemowo skalować kampanie bez utraty postępów. Wykonaj czynności, aby [utworzyć konto rozliczeniowe Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=pl#create-new-billing-account), formalnie zaakceptować standardowe Warunki korzystania z usługi Google Cloud i [przejść na standardowy projekt Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pl#upgradee).
Więcej informacji znajdziesz w artykule [Konfiguracja kont płatnych](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pl#paid-setup).

Więcej informacji o poziomach płatności znajdziesz w sekcji [Płatności](https://ai.google.dev/gemini-api/docs/billing?hl=pl).

## Usuwanie aplikacji

Jeśli nie potrzebujesz już aplikacji, możesz ją usunąć w Google AI Studio, wykonując te czynności:

1. W Google AI Studio otwórz [stronę Aplikacje](https://aistudio.google.com/app/apps?hl=pl).
2. W menu po lewej stronie kliknij **Aplikacje**.
3. Umieść wskaźnik nad aplikacją, którą chcesz usunąć.
4. Aby usunąć aplikację, kliknij ikonę kosza po prawej stronie wiersza.

## Co dalej?

- Dowiedz się więcej o [poziomie startowym Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pl).
- Dowiedz się więcej o [płatnościach](https://ai.google.dev/gemini-api/docs/billing?hl=pl) za Gemini API.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-28 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-28 UTC."],[],[]]
