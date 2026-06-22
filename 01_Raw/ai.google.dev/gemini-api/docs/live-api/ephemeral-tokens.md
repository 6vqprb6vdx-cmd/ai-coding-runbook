---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=de
fetched_at: 2026-06-22T06:24:12.813580+00:00
title: "Ephemerische Tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Ephemerische Tokens

Temporäre Tokens sind kurzlebige Authentifizierungstokens für den Zugriff auf die Gemini API über [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Sie sollen die Sicherheit verbessern, wenn Sie direkt vom Gerät eines Nutzers aus eine Verbindung zur API herstellen (eine [Client-zu-Server](https://ai.google.dev/gemini-api/docs/live?hl=de#implementation-approach)-Implementierung). Wie Standard-API-Schlüssel können auch temporäre Tokens aus clientseitigen Anwendungen wie Webbrowsern oder mobilen Apps extrahiert werden. Da temporäre Tokens jedoch schnell ablaufen und eingeschränkt werden können, verringern sie die Sicherheitsrisiken in einer Produktionsumgebung erheblich. Sie sollten sie verwenden, wenn Sie direkt von clientseitigen Anwendungen auf die Live API zugreifen, um die Sicherheit von API-Schlüsseln zu erhöhen.

## Funktionsweise von temporären Tokens

So funktionieren temporäre Tokens:

1. Ihr Client (z.B. eine Web-App) wird bei Ihrem Backend authentifiziert.
2. Ihr Backend fordert ein temporäres Token vom Bereitstellungsdienst der Gemini API an.
3. Die Gemini API gibt ein kurzlebiges Token aus.
4. Ihr Backend sendet das Token an den Client für WebSocket-Verbindungen zur Live API. Dazu können Sie Ihren API-Schlüssel durch ein temporäres Token ersetzen.
5. Der Client verwendet das Token dann so, als wäre es ein API-Schlüssel.

![Sitzungsspezifische Tokens – Übersicht](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=de)

Das erhöht die Sicherheit, da das Token auch im Falle eines Diebstahls nur kurzlebig ist. Im Gegensatz dazu ist ein clientseitig bereitgestellter API-Schlüssel langlebig. Da der Client Daten direkt an Gemini sendet, wird auch die Latenz verbessert und Ihre Back-Ends müssen die Echtzeitdaten nicht weiterleiten.

## Sitzungsspezifisches Token erstellen

Hier ist ein vereinfachtes Beispiel dafür, wie Sie ein temporäres Token von Gemini erhalten.
Standardmäßig haben Sie eine Minute Zeit, um neue Live API-Sitzungen mit dem Token aus dieser Anfrage (`newSessionExpireTime`) zu starten, und 30 Minuten Zeit, um Nachrichten über diese Verbindung (`expireTime`) zu senden.

### Python

```
import datetime
from google import genai

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

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

Informationen zu `expireTime`-Wertbeschränkungen, Standardwerten und anderen Feldspezifikationen finden Sie in der [API-Referenz](https://ai.google.dev/api/live?hl=de#ephemeral-auth-tokens). Innerhalb des `expireTime`-Zeitraums müssen Sie [`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=de#session-resumption), um die Verbindung alle 10 Minuten wiederherzustellen. Das kann mit demselben Token erfolgen, auch wenn `uses: 1`.

Es ist auch möglich, ein temporäres Token für eine Reihe von Konfigurationen zu sperren. Das kann nützlich sein, um die Sicherheit Ihrer Anwendung weiter zu verbessern und Ihre Systemanweisungen auf der Serverseite zu behalten.

### Python

```
from google import genai

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

Sie können auch eine Teilmenge von Feldern sperren. Weitere Informationen finden Sie in der [SDK-Dokumentation](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields).

## Mit einem temporären Token eine Verbindung zur Live API herstellen

Sobald Sie ein temporäres Token haben, verwenden Sie es wie einen API-Schlüssel. Es funktioniert jedoch nur für die Live-API und nur mit der `v1alpha`-Version der API.

Die Verwendung von temporären Tokens ist nur dann sinnvoll, wenn Anwendungen bereitgestellt werden, die dem [Client-zu-Server-Implementierungsansatz](https://ai.google.dev/gemini-api/docs/live?hl=de#implementation-approach) folgen.

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

Weitere Beispiele finden Sie unter [Erste Schritte mit der Live API](https://ai.google.dev/gemini-api/docs/live?hl=de).

## Best Practices

- Legen Sie mit dem Parameter `expire_time` eine kurze Ablaufdauer fest.
- Tokens laufen ab und der Bereitstellungsprozess muss neu gestartet werden.
- Sorgen Sie für eine sichere Authentifizierung für Ihr eigenes Backend. Die Sicherheit von temporären Tokens hängt von der Authentifizierungsmethode Ihres Backends ab.
- Im Allgemeinen sollten Sie keine temporären Tokens für Backend-zu-Gemini-Verbindungen verwenden, da dieser Pfad in der Regel als sicher gilt.

## Beschränkungen

Kurzlebige Tokens sind derzeit nur mit der [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de) kompatibel.

## Nächste Schritte

- Weitere Informationen finden Sie in der [Referenz zur Live API](https://ai.google.dev/api/live?hl=de#ephemeral-auth-tokens) zu temporären Tokens.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-12 (UTC)."],[],[]]
