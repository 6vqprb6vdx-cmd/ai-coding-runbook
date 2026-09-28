---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-key?hl=pl
fetched_at: 2026-09-28T06:17:11.668181+00:00
title: "Korzystanie z kluczy interfejsu Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# Korzystanie z kluczy interfejsu Gemini API

Aby korzystać z interfejsu Gemini API, musisz uwierzytelniać swoje żądania. Możesz uwierzytelnić się za pomocą standardowego klucza interfejsu API lub klucza autoryzacji.

[Tworzenie lub wyświetlanie klucza interfejsu Gemini API](https://aistudio.google.com/apikey?hl=pl)

## Typy kluczy interfejsu API: standardowy i autoryzacyjny

Klucze interfejsu API zapewniają dostęp do Gemini API, ale różnią się pod względem bezpieczeństwa. Aby zwiększyć bezpieczeństwo, interfejs Gemini API przechodzi z standardowych kluczy API na klucze autoryzacji:

- **Standardowe klucze interfejsu API:** powiązują żądania z projektem Google Cloud na potrzeby rozliczeń i limitów. Klucze standardowe nie identyfikują dzwoniącego, co ogranicza szczegółowość uprawnień i kontroli dostępu, które mogą obsługiwać.
- **Klucze autoryzacji**: powiązane bezpośrednio z kontem usługi Google Cloud. Gdy używasz klucza autoryzacji, Twoje żądania są przetwarzane w ramach tożsamości powiązanego konta usługi, co umożliwia szczegółową kontrolę dostępu. Klucze autoryzacji są domyślnie ograniczone do interfejsu Generative Language API (Gemini API) i zapewniają szybkie egzekwowanie zasad dotyczących wycieku kluczy, które szybko zatrzymuje używanie wyciekłych kluczy wykrytych przez nasze systemy.

Aby zapewnić bezpieczne korzystanie z interfejsu Gemini API, przejdziemy z kluczy standardowych na klucze autoryzacji:

- **Domyślne klucze autoryzacji:** od 28 maja 2026 r. wszystkie nowe klucze interfejsu API utworzone w Google AI Studio będą automatycznie tworzone jako klucze autoryzacji.
- **Odrzucanie kluczy bez ograniczeń:**  interfejs Gemini API odrzuca żądania pochodzące z **kluczy standardowych bez ograniczeń**. Standardowe klucze interfejsu API, do których zastosowano wyraźne ograniczenia, nadal działają. To ograniczenie uniemożliwia nieautoryzowane użycie kluczy, które mogą być udostępniane publicznie lub powiązane z innymi usługami.

## Zarządzanie kluczami interfejsu API w Google AI Studio

Projektami i kluczami możesz zarządzać bezpośrednio w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl).

### Projekty Google Cloud

Każdy klucz interfejsu Gemini API jest powiązany z [projektem w chmurze Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pl).
Projekty Google Cloud służą do zarządzania płatnościami, współpracownikami i uprawnieniami. Google AI Studio udostępnia prosty interfejs umożliwiający dostęp do tych projektów.

- **Domyślny projekt:** jeśli jesteś nowym użytkownikiem, po zaakceptowaniu Warunków korzystania z usługi Google AI Studio automatycznie utworzy domyślny projekt w chmurze Google Cloud i klucz interfejsu API. Aby zmienić nazwę tego projektu, otwórz widok **Projekty** w panelu.
- **Istniejące projekty:** jeśli masz już konto Google Cloud, AI Studio nie tworzy projektu domyślnego. Zamiast tego musisz zaimportować dotychczasowe projekty.

### Importowanie projektów

Domyślnie Google AI Studio nie wyświetla wszystkich projektów Google Cloud. Musisz zaimportować projekty, których chcesz używać:

1. Otwórz [Google AI Studio](https://aistudio.google.com?hl=pl).
2. W panelu po lewej stronie otwórz **Panel** i wybierz **Projekty**.
3. Kliknij przycisk **Importuj projekty**.
4. Wyszukaj i wybierz projekt w chmurze Google, który chcesz zaimportować, a potem kliknij **Importuj**.
5. Po zaimportowaniu otwórz stronę **Klucze interfejsów API** w panelu, aby utworzyć klucz w tym projekcie.

### Rozwiązywanie problemów z uprawnieniami do tworzenia kluczy

Jeśli przycisk **Utwórz klucz interfejsu API** jest niedostępny i wyświetla się komunikat *„Nie masz uprawnień do tworzenia klucza w tym projekcie”*, oznacza to, że nie masz wymaganych uprawnień IAM.

Poproś administratora projektu w chmurze lub administratora organizacji Google Cloud o przypisanie Ci roli zawierającej te uprawnienia (np. edytującego projektu):

- `resourcemanager.projects.get`: umożliwia AI Studio weryfikację projektu.
- `apikeys.keys.create`: umożliwia generowanie kluczy.
- `serviceusage.services.enable`: sprawdza, czy interfejs Generative Language API jest włączony.
- `iam.serviceAccounts.create`: wymagane do utworzenia połączonego konta usługi.
- `iam.serviceAccountApiKeyBindings.create`: wiąże konto usługi z kluczem interfejsu API.

Jeśli nie możesz uzyskać dostępu administracyjnego, możesz utworzyć nowy projekt Google Cloud, który nie jest powiązany z organizacją, aby wygenerować klucze.

## Konfiguruję środowisko

Gdy uzyskasz klucz, skonfiguruj środowisko, aby bezpiecznie używać go w aplikacjach.

### Używaj zmiennych środowiskowych (zalecane)

Ustaw zmienną środowiskową `GEMINI_API_KEY` lub `GOOGLE_API_KEY`. Biblioteki klienta interfejsu Gemini API automatycznie wykrywają i używają tych zmiennych. Jeśli oba parametry są skonfigurowane, pierwszeństwo ma parametr `GOOGLE_API_KEY`.

Aby ustawić zmienną, wybierz system operacyjny:

### Linux/macOS – Bash

Sprawdź, czy masz plik konfiguracyjny bash:

```
~/.bashrc
```

Jeśli nie, utwórz go i otwórz:

```
touch ~/.bashrc && open ~/.bashrc
```

Na końcu pliku dodaj polecenie eksportu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Zapisz plik, a następnie zastosuj zmiany:

```
source ~/.bashrc
```

### macOS – Zsh

Sprawdź, czy masz plik konfiguracji zsh:

```
~/.zshrc
```

Jeśli nie, utwórz go i otwórz:

```
touch ~/.zshrc && open ~/.zshrc
```

Dodaj polecenie eksportu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Zapisz plik, a następnie zastosuj zmiany:

```
source ~/.zshrc
```

### Windows

1. Na pasku wyszukiwania systemu Windows wyszukaj „Zmienne środowiskowe”.
2. W oknie Właściwości systemu kliknij **Zmienne środowiskowe**.
3. W sekcji **Zmienne użytkownika** lub **Zmienne systemowe** kliknij **Nowa...**.
4. Jako nazwę zmiennej wpisz `GEMINI_API_KEY`, a jako wartość podaj klucz interfejsu API.
5. Kliknij **OK**, aby zapisać zmiany. Otwórz nową sesję terminala, aby wczytać zmienną.

### Jawne podanie klucza interfejsu API w kodzie

Klucz interfejsu API możesz przekazać bezpośrednio podczas inicjowania klienta. Zrób to tylko wtedy, gdy nie możesz używać zmiennych środowiskowych.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"       -H 'Content-Type: application/json'       -H "x-goog-api-key: YOUR_API_KEY"       -X POST       -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Bezpieczeństwo i zarządzanie obiektami tajnymi

Traktuj klucz interfejsu Gemini API jak hasło. Jeśli zostanie przejęty, inne osoby mogą wykorzystać limit projektu, ponieść nieoczekiwane opłaty za usługi i uzyskać dostęp do prywatnych zasobów.

### Krytyczne reguły zabezpieczeń

- **Zachowaj klucze w poufności:** nigdy nie sprawdzaj kluczy interfejsu API w systemach kontroli źródła, takich jak Git.
- **Nigdy nie udostępniaj kluczy po stronie klienta w środowisku produkcyjnym:** nie koduj na stałe kluczy interfejsu API bezpośrednio w aplikacjach internetowych ani mobilnych. Klucze skompilowane w kodzie po stronie klienta mogą być wyodrębniane przez użytkowników. Aby zabezpieczyć aplikacje po stronie klienta, uruchom serwer proxy backendu, który będzie wykonywać rzeczywiste wywołania interfejsu API.

### Sprawdzone metody zarządzania danymi tajnymi

- **Zmienne środowiskowe:** odczytuj klucze ze zmiennych środowiskowych zamiast z plików konfiguracyjnych.
- **Secret Manager:** w środowisku produkcyjnym przechowuj klucze w bezpiecznym magazynie obiektów tajnych, takim jak [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=pl).
- **Alerty dotyczące rozliczeń:** skonfiguruj w konsoli Google Cloud alerty dotyczące rozliczeń, które będą Cię informować o nagłym wzroście wykorzystania lub kosztów.

### Lista kontrolna reagowania na wyciek

Jeśli podejrzewasz, że Twój klucz interfejsu API wyciekł:

1. **Wygeneruj nowy klucz:** utwórz klucz zastępczy w Google AI Studio lub w konsoli Cloud Console.
2. **Zaktualizuj aplikację:** wdróż kod za pomocą nowego klucza.
3. **Wyłącz lub usuń naruszony klucz:** po zweryfikowaniu nowego klucza wyłącz wyciekły klucz w konsoli Cloud. Nie usuwaj starego klucza, dopóki nowy klucz nie zostanie w pełni aktywowany, aby uniknąć przestoju aplikacji.
4. **Sprawdzanie wykorzystania:** sprawdzaj logi płatności i wykorzystanie interfejsu API w konsoli Google Cloud, aby wykrywać nieautoryzowaną aktywność.

## Ograniczanie i zabezpieczanie kluczy

Dodanie ograniczeń do kluczy interfejsu API minimalizuje potencjalne szkody w przypadku naruszenia bezpieczeństwa klucza.

### Stosowanie ograniczeń dotyczących pochodzenia żądań

Ograniczenia dotyczące pochodzenia ograniczają adresy IP, witryny lub aplikacje, które mogą używać Twojego klucza.

1. Otwórz [stronę Dane logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).
2. Wybierz projekt i kliknij nazwę klucza API, który chcesz ograniczyć.
3. W sekcji **Ograniczenia aplikacji** wybierz **Adresy IP** (lub odpowiedni typ ograniczenia dla Twojego środowiska).
4. Określ dozwolone adresy lub zakresy adresów IP, a następnie kliknij **Zapisz**.

### Zabezpieczanie standardowych kluczy interfejsu API bez ograniczeń

Aby nadal korzystać z interfejsu Gemini API, musisz zabezpieczyć wszystkie klucze bez ograniczeń.

#### Ogranicz klucz tylko do Gemini API za pomocą AI Studio

Jeśli używasz klucza tylko w przypadku Gemini API, zabezpiecz go bezpośrednio w AI Studio:

1. Na stronie **Klucze interfejsu API** w [Google AI Studio](https://aistudio.google.com/api-keys?hl=pl) znajdź klucze oznaczone etykietą **Bez ograniczeń**.
2. Najedź kursorem na etykietę i w oknie kliknij **Dodaj ograniczenia**.
3. Wybierz **Ogranicz do Gemini API**.
4. Aby potwierdzić, kliknij **Ogranicz klucz**.

#### Ograniczanie klucza dla innych usług za pomocą konsoli Google Cloud

Jeśli klucz jest udostępniany innym interfejsom API Google (nie jest to zalecane), ogranicz go w konsoli Cloud. **Uwaga: po zastosowaniu tych ograniczeń żądania do interfejsu Gemini API korzystające z tego klucza będą kończyć się niepowodzeniem.**

1. Otwórz [stronę Dane logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).
2. Wybierz projekt i klucz interfejsu API.
3. W sekcji **Ograniczenia interfejsów API** wybierz **Ogranicz klucz**.
4. Z menu wybierz interfejsy API, do których ten klucz ma mieć dostęp. Nie wybieraj **Generative Language API**.
5. Kliknij **Zapisz**. Aby nadal korzystać z Gemini API, utwórz w AI Studio osobny klucz z ograniczeniami.

### Blokowanie nieaktywnych kluczy

Od 7 maja 2026 r. interfejs Gemini API będzie blokować klucze interfejsu API bez ograniczeń, które przez dłuższy czas były nieaktywne. Te klucze będą miały w AI Studio tag **Zablokowany**. Aby kontynuować, musisz wygenerować nowy klucz lub użyć istniejącego klucza z ograniczeniami.

## Migracja do klucza uwierzytelniającego

Aby utworzyć nowy klucz interfejsu API do autoryzacji i zaktualizować aplikacje:

1. Otwórz [stronę kluczy interfejsów API AI Studio](https://aistudio.google.com/api-keys?hl=pl).
2. Sprawdź kolumnę **Typ klucza**, aby znaleźć klucze oznaczone jako **Standardowy**.
3. Aby wygenerować nowy klucz, kliknij **Utwórz klucz interfejsu API**. Wszystkie nowe klucze utworzone w AI Studio są automatycznie tworzone jako klucze uwierzytelniania.
4. Skopiuj nowy klucz interfejsu API do autoryzacji.
5. Zaktualizuj kod aplikacji, zmienne środowiskowe i wszystkie konfiguracje wdrożenia, aby używać nowego klucza interfejsu API autoryzacji.
6. Przetestuj aplikację, aby sprawdzić, czy działa prawidłowo z nowym kluczem.
7. Po weryfikacji usuń lub unieważnij stary klucz ruchu, aby zapobiec jego niewłaściwemu użyciu.

## Ograniczenia

Google AI Studio ma te ograniczenia dotyczące zarządzania projektami i kluczami:

- Możesz utworzyć maksymalnie 10 projektów naraz na stronie **Projekty** w Google AI Studio.
- Na stronach **Klucze interfejsu API** i **Projekty** wyświetla się maksymalnie 100 kluczy i 50 projektów.
- Wyświetlane są tylko klucze interfejsu API, które nie mają ograniczeń lub są ograniczone do interfejsu Generative Language API (Gemini API).

Aby uzyskać dostęp do zaawansowanych funkcji zarządzania projektami lub zmodyfikować klucze z innymi ograniczeniami, otwórz [stronę danych logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-25 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-25 UTC."],[],[]]
