---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=pl
fetched_at: 2026-05-05T13:15:22.123938+00:00
title: "Ephemeral tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Ephemeral tokens

Tokeny tymczasowe to krótkotrwałe tokeny uwierzytelniające, które umożliwiają dostęp do interfejsu Gemini API za pomocą [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Zostały one zaprojektowane w celu zwiększenia bezpieczeństwa podczas łączenia się bezpośrednio z interfejsem API z urządzenia użytkownika (implementacja [klient-serwer](https://ai.google.dev/gemini-api/docs/live?hl=pl#implementation-approach)). Podobnie jak standardowe klucze interfejsu API, tymczasowe tokeny można wyodrębnić z aplikacji po stronie klienta, takich jak przeglądarki internetowe lub aplikacje mobilne. Jednak tymczasowe tokeny szybko wygasają i można je ograniczać, co znacznie zmniejsza ryzyko związane z bezpieczeństwem w środowisku produkcyjnym. Używaj ich, gdy uzyskujesz dostęp do interfejsu Live API bezpośrednio z aplikacji po stronie klienta, aby zwiększyć bezpieczeństwo klucza interfejsu API.

## Jak działają tymczasowe tokeny

Ogólnie tokeny przejściowe działają w ten sposób:

1. Klient (np. aplikacja internetowa) uwierzytelnia się w backendzie.
2. Backend wysyła żądanie tokena tymczasowego do usługi udostępniania interfejsu Gemini API.
3. Interfejs Gemini API wydaje krótkotrwały token.
4. Backend wysyła token do klienta w przypadku połączeń WebSocket z Live API. Możesz to zrobić, zastępując klucz interfejsu API tokenem tymczasowym.
5. Klient używa tokena tak, jakby był kluczem interfejsu API.

![Omówienie tokenów efemerycznych](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=pl)

Zwiększa to bezpieczeństwo, ponieważ nawet jeśli token zostanie wyodrębniony, będzie miał krótki okres ważności, w przeciwieństwie do klucza interfejsu API o długim okresie ważności wdrożonego po stronie klienta. Ponieważ klient wysyła dane bezpośrednio do Gemini, poprawia to też opóźnienia i eliminuje konieczność przekazywania danych w czasie rzeczywistym przez backendy.

## Tworzenie tokena efemerycznego

Oto uproszczony przykład uzyskiwania tymczasowego tokena z Gemini.
Domyślnie masz 1 minutę na rozpoczęcie nowych sesji interfejsu Live API przy użyciu tokena z tego żądania (`newSessionExpireTime`) i 30 minut na wysyłanie wiadomości przez to połączenie (`expireTime`).

### Python

```
import datetime

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

  const token: AuthToken = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

Ograniczenia wartości, wartości domyślne i inne specyfikacje pól `expireTime` znajdziesz w [dokumentacji API](https://ai.google.dev/api/live?hl=pl#ephemeral-auth-tokens).
W `expireTime` tym czasie musisz [`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=pl#session-resumption) ponownie połączyć się z połączeniem co 10 minut (możesz to zrobić za pomocą tego samego tokena, nawet jeśli `uses: 1`).

Możesz też powiązać token efemeryczny z zestawem konfiguracji. Może to być przydatne do dalszego zwiększania bezpieczeństwa aplikacji i przechowywania instrukcji systemowych po stronie serwera.

### Python

```
client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

Możesz też zablokować podzbiór pól. Więcej informacji znajdziesz w [dokumentacji pakietu SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields).

## Łączenie się z Live API za pomocą tokena tymczasowego

Gdy uzyskasz token tymczasowy, używaj go tak, jakby był kluczem interfejsu API (pamiętaj jednak, że działa on tylko w przypadku interfejsu API w wersji produkcyjnej i tylko z wersją `v1alpha` interfejsu API).

Używanie tymczasowych tokenów ma sens tylko w przypadku wdrażania aplikacji, które korzystają z [implementacji po stronie klienta i serwera](https://ai.google.dev/gemini-api/docs/live?hl=pl#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Więcej przykładów znajdziesz w artykule [Pierwsze kroki z interfejsem Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).

## Sprawdzone metody

- Ustaw krótki czas wygaśnięcia za pomocą parametru `expire_time`.
- Tokeny wygasają, co wymaga ponownego rozpoczęcia procesu udostępniania.
- Sprawdź bezpieczne uwierzytelnianie na własnym backendzie. Tokeny tymczasowe będą tak bezpieczne, jak metoda uwierzytelniania backendu.
- Zwykle unikaj używania tymczasowych tokenów w przypadku połączeń między backendem a Gemini, ponieważ ta ścieżka jest zwykle uważana za bezpieczną.

## Ograniczenia

Obecnie tokeny tymczasowe są zgodne tylko z [interfejsem Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).

## Co dalej?

- Więcej informacji znajdziesz w [dokumentacji API](https://ai.google.dev/api/live?hl=pl#ephemeral-auth-tokens) interfejsu Live API na temat tokenów tymczasowych.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
