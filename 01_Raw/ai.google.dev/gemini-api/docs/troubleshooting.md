---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=de
fetched_at: 2026-08-10T03:19:31.542652+00:00
title: "Tipps zur Fehlerbehebung \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Tipps zur Fehlerbehebung

In dieser Anleitung erfahren Sie, wie Sie häufige Probleme diagnostizieren und beheben, die beim Aufrufen der Gemini API auftreten. Probleme können entweder im Backend-Dienst der Gemini API oder in den Client-SDKs auftreten. Unsere Client-SDKs sind Open Source und in den folgenden Repositorys verfügbar:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Wenn Probleme mit dem API-Schlüssel auftreten, prüfen Sie, ob Sie
Ihren API-Schlüssel gemäß der [Anleitung zur Einrichtung des API-Schlüssels](https://ai.google.dev/gemini-api/docs/api-key?hl=de) korrekt eingerichtet haben.

## Fehlercodes des Backend-Dienstes der Gemini API

In der folgenden Tabelle sind häufige Backend-Fehlercodes aufgeführt, die auftreten können, sowie Erklärungen zu ihren Ursachen und Schritten zur Fehlerbehebung:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP-Code** | **Status** | **Beschreibung** | **Beispiel** | **Lösung** |
| 400 | INVALID\_ARGUMENT | Der Anfragetext ist fehlerhaft. | Ihre Anfrage enthält einen Tippfehler oder ein fehlendes Pflichtfeld. | In der [API-Referenz](https://ai.google.dev/api?hl=de) finden Sie Informationen zum Anfrageformat, Beispiele und unterstützte Versionen. Die Verwendung von Funktionen einer neueren API-Version mit einem älteren Endpunkt kann zu Fehlern führen. |
| 400 | FAILED\_PRECONDITION | Die kostenlose Stufe der Gemini API ist in Ihrem Land nicht verfügbar. Aktivieren Sie die Abrechnung für Ihr Projekt in Google AI Studio. | Sie senden eine Anfrage in einer Region, in der die kostenlose Stufe nicht unterstützt wird, und Sie haben die Abrechnung für Ihr Projekt in Google AI Studio nicht aktiviert. | Wenn Sie die Gemini API verwenden möchten, müssen Sie in [Google AI Studio](https://aistudio.google.com/apikey?hl=de) einen kostenpflichtigen Plan einrichten. |
| 403 | PERMISSION\_DENIED | Ihr API-Schlüssel hat nicht die erforderlichen Berechtigungen. | [Sie verwenden den falschen API-Schlüssel oder versuchen, ein optimiertes Modell zu verwenden, ohne sich ordnungsgemäß zu authentifizieren.](https://ai.google.dev/gemini-api/docs/model-tuning?hl=de) | Prüfen Sie, ob Ihr API-Schlüssel festgelegt ist und die richtigen Zugriffsberechtigungen hat. Außerdem müssen Sie sich ordnungsgemäß authentifizieren, um optimierte Modelle zu verwenden. |
| 404 | NOT\_FOUND | Die angeforderte Ressource wurde nicht gefunden. | Eine in Ihrer Anfrage referenzierte Bild-, Audio- oder Videodatei wurde nicht gefunden. | Prüfen Sie, ob alle [Parameter in Ihrer Anfrage gültig sind](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=de#check-api) für Ihre API-Version. |
| 429 | RESOURCE\_EXHAUSTED | Sie haben eines der Ratenlimits der API überschritten (Anfragen pro Minute, Tokens pro Minute, Anfragen pro Tag, Ausgaben usw.). | Sie senden zu viele Anfragen, verwenden zu viele Tokens oder überschreiten ausgabenbasierte Limits für den Abrechnungsverlauf und die Stufe Ihres Kontos. | Prüfen Sie, ob Sie die [Ratenlimits](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de) des Modells einhalten. Warten Sie kurz und versuchen Sie es dann noch einmal. Reduzieren Sie die Rate oder Größe Ihrer Anfragen. [Fordern Sie bei Bedarf eine Erhöhung des Ratenlimits an](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de#request-rate-limit-increase). |
| 499 | CANCELLED | Der Vorgang wurde abgebrochen, üblicherweise vom Aufrufer. | Der Client hat die Verbindung geschlossen, bevor die API die Antwort senden konnte. | Prüfen Sie, ob Ihre Client- oder Netzwerkinfrastruktur die Verbindung vorzeitig schließt (z.B. aufgrund eines clientseitigen Timeouts). |
| 500 | INTERN | Bei Google ist ein unerwarteter Fehler aufgetreten. | Ihr Eingabekontext ist zu lang. | Prüfen Sie auf der [Statusseite der Gemini API](https://aistudio.google.com/status?hl=de), ob es aktuelle Vorfälle gibt. Reduzieren Sie den Eingabekontext oder wechseln Sie vorübergehend zu einem anderen Modell (z.B. von Gemini 2.5 Pro zu Gemini 2.5 Flash) und prüfen Sie, ob das Problem dadurch behoben wird. Alternativ können Sie auch etwas warten und die Anfrage dann noch einmal senden. Wenn das Problem nach dem Wiederholen weiterhin besteht, melden Sie es bitte über die Schaltfläche **Feedback senden** in Google AI Studio. |
| 503 | UNAVAILABLE | Der Dienst ist möglicherweise vorübergehend überlastet oder nicht verfügbar. | Die Kapazität des Dienstes ist vorübergehend erschöpft. | Prüfen Sie auf der [Statusseite der Gemini API](https://aistudio.google.com/status?hl=de), ob es aktuelle Vorfälle gibt. Wechseln Sie vorübergehend zu einem anderen Modell (z.B. von Gemini 2.5 Pro zu Gemini 2.5 Flash) und prüfen Sie, ob das Problem dadurch behoben wird. Alternativ können Sie auch etwas warten und die Anfrage dann noch einmal senden. Wenn das Problem nach dem Wiederholen weiterhin besteht, melden Sie es bitte über die Schaltfläche **Feedback senden** in Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Der Dienst kann die Verarbeitung nicht innerhalb des Zeitlimits abschließen. | Ihr Prompt (oder Kontext) ist zu groß, um rechtzeitig verarbeitet zu werden. | Legen Sie in Ihrer Clientanfrage ein höheres Zeitlimit fest, um diesen Fehler zu vermeiden. |

## Wiederholungsstrategie

Wenn Sie eine Fehlermeldung erhalten, die darauf hinweist, dass Sie die Anfrage wiederholen sollten (z. B. `429 RESOURCE_EXHAUSTED` oder `503 UNAVAILABLE`), empfehlen wir, eine Strategie für exponentiellen Backoff zu implementieren. Das bedeutet, dass Sie vor dem ersten Wiederholungsversuch eine kurze Zeit warten und dann die Wartezeit zwischen den nachfolgenden Wiederholungsversuchen schrittweise erhöhen.

Die offiziellen Client-SDKs für die Gemini API, z. B. das [Python SDK](https://github.com/googleapis/python-genai), enthalten standardmäßig eine automatische Wiederholungslogik mit exponentiellem Backoff für die Behandlung vorübergehender Fehler wie Timeouts, Netzwerkprobleme und Ratenlimits (`429` und `5xx` Statuscodes). Das Python SDK wiederholt vorübergehende Fehler beispielsweise automatisch bis zu viermal mit einer anfänglichen Verzögerung von etwa 1 Sekunde und einer maximalen Verzögerung von 60 Sekunden.

Wenn Sie direkte REST API-Anfragen senden oder Ihre Wiederholungslogik anpassen, sollten Sie die folgenden Best Practices beachten, um die Wahrscheinlichkeit einer erfolgreichen Anfrage zu erhöhen und den Dienst nicht zu überlasten:

- **Exponentiellen Backoff verwenden**:Warten Sie vor dem ersten Wiederholungsversuch eine kurze Zeit (z. B. 1 Sekunde) und erhöhen Sie dann die Verzögerung exponentiell (z. B. 2 Sekunden, 4 Sekunden, 8 Sekunden).
- **Jitter hinzufügen**:Fügen Sie der Verzögerung zufälligen „Jitter“ hinzu, um zu verhindern, dass alle Clients gleichzeitig Wiederholungsversuche durchführen.
- **Wiederholungsversuche bei bestimmten Fehlern**:Wiederholen Sie nur vorübergehende Fehler (z. B. `429`, `408` oder `5xx`). Wiederholen Sie keine Clientfehler (z. B. `400` oder `403`), da diese auf Probleme wie ungültige API-Schlüssel oder eine fehlerhafte Syntax hinweisen.
- **Maximale Anzahl von Wiederholungsversuchen festlegen**:Definieren Sie eine maximale Anzahl von Wiederholungsversuchen, um Endlosschleifen zu vermeiden.

## API-Aufrufe auf Fehler bei Modellparametern prüfen

Prüfen Sie, ob Ihre Modellparameter innerhalb der folgenden Werte liegen:

|  |  |
| --- | --- |
| **Modellparameter** | **Werte (Bereich)** |
| Anzahl der Kandidaten | 1–8 (Ganzzahl) |
| Temperatur | 0,0–1,0 |
| Maximale Ausgabetokens | Verwenden Sie die Seite „[Modelle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de)“, um die maximale Anzahl von Tokens für das verwendete Modell zu ermitteln. |
| TopP | 0,0–1,0 |

Prüfen Sie nicht nur die Parameterwerte, sondern auch, ob Sie die richtige
[API-Version](https://ai.google.dev/gemini-api/docs/api-versions?hl=de) (z.B. `/v1` oder `/v1beta`) und
das richtige Modell verwenden, das die benötigten Funktionen unterstützt. Wenn sich eine Funktion beispielsweise in der Betaphase befindet, ist sie nur in der API-Version `/v1beta` verfügbar.

## Prüfen, ob Sie das richtige Modell verwenden

Prüfen Sie, ob Sie ein unterstütztes Modell verwenden, das auf unserer [Seite „Modelle“
aufgeführt ist](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de).

## Höhere Latenz oder Tokennutzung bei 2.5-Modellen

Wenn Sie bei den Modellen 2.5 Flash und Pro eine höhere Latenz oder Tokennutzung feststellen, liegt das daran, dass **Thinking standardmäßig aktiviert** ist, um die Qualität zu verbessern. Wenn Sie Geschwindigkeit priorisieren oder Kosten minimieren müssen, können Sie Thinking anpassen oder deaktivieren.

Auf der Seite [„Thinking“](https://ai.google.dev/gemini-api/docs/thinking?hl=de#set-budget) finden Sie eine
Anleitung und Beispielcode.

## Sicherheitsprobleme

Wenn ein Prompt aufgrund einer Sicherheitseinstellung in Ihrem API-Aufruf blockiert wurde, prüfen Sie den Prompt im Hinblick auf die Filter, die Sie im API-Aufruf festgelegt haben.

Wenn `BlockedReason.OTHER` angezeigt wird, verstößt die Anfrage oder Antwort möglicherweise gegen die [Nutzungsbedingungen](https://ai.google.dev/terms?hl=de) oder wird anderweitig nicht unterstützt.

## Problem mit der Rezitation

Wenn das Modell die Ausgabe aufgrund des Grunds „RECITATION“ beendet, ähnelt die Modellausgabe bestimmten Daten. Um dieses Problem zu beheben, versuchen Sie, den Prompt / Kontext so eindeutig wie möglich zu gestalten und eine höhere Temperatur zu verwenden.

## Problem mit sich wiederholenden Tokens

Wenn wiederholte Ausgabetokens angezeigt werden, versuchen Sie es mit den folgenden Vorschlägen, um sie zu reduzieren oder zu entfernen.

| Beschreibung | Ursache | Vorgeschlagene Problemumgehung |
| --- | --- | --- |
| Wiederholte Bindestriche in Markdown-Tabellen | Dies kann auftreten, wenn der Inhalt der Tabelle lang ist, da das Modell versucht, eine visuell ausgerichtete Markdown-Tabelle zu erstellen. Die Ausrichtung in Markdown ist jedoch für das korrekte Rendering nicht erforderlich. | Fügen Sie Ihrem Prompt Anweisungen hinzu, um dem Modell spezifische Richtlinien für die Generierung von Markdown-Tabellen zu geben. Geben Sie Beispiele an, die diesen Richtlinien entsprechen. Sie können auch versuchen, die Temperatur anzupassen. Für die Generierung Code oder sehr strukturierter Ausgabe wie Markdown-Tabellen, haben sich hohe Temperaturen (>= 0,8) als besser erwiesen.  Im Folgenden finden Sie ein Beispiel für Richtlinien, die Sie Ihrem Prompt hinzufügen können, um dieses Problem zu vermeiden:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Wiederholte Tokens in Markdown-Tabellen | Ähnlich wie bei den wiederholten Bindestrichen tritt dieses Problem auf, wenn das Modell versucht, den Inhalt der Tabelle visuell auszurichten. Die Ausrichtung in Markdown ist für das korrekte Rendering nicht erforderlich. | - Fügen Sie Ihrem Systemprompt Anweisungen wie die folgenden hinzu:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Versuchen Sie, die Temperatur anzupassen. Höhere Temperaturen (>= 0,8)   tragen in der Regel dazu bei, Wiederholungen oder Duplikate in   der Ausgabe zu vermeiden. |
| Wiederholte Zeilenumbrüche (`\n`) in strukturierter Ausgabe | Wenn die Modelleingabe Unicode- oder Escapesequenzen wie `\u` oder `\t` enthält, kann das zu wiederholten Zeilenumbrüchen führen. | - Suchen Sie in Ihrem Prompt nach verbotenen Escapesequenzen und ersetzen Sie sie durch UTF-8-Zeichen. Die Escapesequenz `\u`   in Ihren JSON-Beispielen kann beispielsweise dazu führen, dass das Modell sie   auch in der Ausgabe verwendet. - Weisen Sie das Modell auf zulässige Escapesequenzen hin. Fügen Sie eine Systemanweisung wie   diese hinzu:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Wiederholter Text bei Verwendung strukturierter Ausgabe | Wenn die Modellausgabe eine andere Reihenfolge für die Felder hat als das definierte strukturierte Schema, kann das zu wiederholtem Text führen. | - Geben Sie die Reihenfolge der Felder nicht in Ihrem Prompt an. - Machen Sie alle Ausgabefelder zu Pflichtfeldern. |
| Wiederholte Toolaufrufe | Dies kann auftreten, wenn das Modell den Kontext früherer Gedanken verliert und/oder einen nicht verfügbaren Endpunkt aufruft, zu dem es gezwungen ist. | Weisen Sie das Modell an, den Status im Denkprozess beizubehalten. Fügen Sie dies am Ende Ihrer Systemanweisungen hinzu:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Wiederholter Text, der nicht Teil der strukturierten Ausgabe ist | Dies kann auftreten, wenn das Modell bei einer Anfrage hängen bleibt, die es nicht lösen kann. | - Wenn Thinking aktiviert ist, geben Sie in den Anweisungen keine expliziten Anweisungen dazu, wie ein Problem durchdacht werden soll. Fordern Sie nur die endgültige   Ausgabe an. - Versuchen Sie es mit einer höheren Temperatur >= 0,8. - Fügen Sie Anweisungen wie „Sei prägnant“, „Wiederhole dich nicht“ oder   „Gib die Antwort einmal“ hinzu. |

## Blockierte oder nicht funktionierende API-Schlüssel

In diesem Abschnitt wird beschrieben, wie Sie prüfen können, ob Ihr Gemini API-Schlüssel blockiert ist, und was Sie dagegen tun können.

### Gründe für die Blockierung von Schlüsseln

Wir haben eine Sicherheitslücke festgestellt, durch die einige API-Schlüssel öffentlich zugänglich gemacht wurden. Um Ihre Daten zu schützen und unbefugten Zugriff zu verhindern, haben wir diese bekannten, offengelegten Schlüssel proaktiv blockiert, damit sie nicht auf die Gemini API zugreifen können.

### Prüfen, ob Ihre Schlüssel betroffen sind

Wenn Ihr Schlüssel offengelegt wurde, können Sie ihn nicht mehr mit der Gemini API verwenden. In [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=de) können Sie prüfen, ob einer Ihrer
API-Schlüssel blockiert ist und keine Aufrufe an die Gemini API senden kann, und neue
Schlüssel generieren. Wenn Sie versuchen, diese Schlüssel zu verwenden, wird möglicherweise auch der folgende Fehler zurückgegeben:

```
Your API key was reported as leaked. Please use another API key.
```

### Maßnahmen für blockierte API-Schlüssel

Sie sollten in [Google
AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=de) neue API-Schlüssel für Ihre Gemini API-Integrationen generieren. Wir empfehlen dringend, Ihre API-Schlüsselverwaltungspraktiken zu überprüfen, um sicherzustellen, dass Ihre neuen Schlüssel sicher aufbewahrt und nicht öffentlich zugänglich gemacht werden.

### Unerwartete Kosten aufgrund einer Sicherheitslücke

[Reichen Sie eine Supportanfrage zur Abrechnung ein](https://console.cloud.google.com/support/chat?hl=de).
Unser Abrechnungsteam arbeitet an diesem Problem und wir werden Sie so schnell wie möglich über Neuigkeiten informieren.

### Sicherheitsmaßnahmen von Google für offengelegte Schlüssel

**Wie hilft Google, mein Konto vor Kostenüberschreitungen und Missbrauch zu schützen, wenn meine API-Schlüssel offengelegt werden?**

- Wir werden API-Schlüssel ausgeben, wenn Sie in
  [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=de) einen neuen Schlüssel anfordern. Diese Schlüssel sind standardmäßig auf
  Google AI Studio beschränkt und akzeptieren keine Schlüssel von anderen Diensten.
  Dadurch wird eine unbeabsichtigte Verwendung von Schlüsseln verhindert.
- Wir blockieren standardmäßig API-Schlüssel, die offengelegt und mit der Gemini API verwendet werden, um Missbrauch von Kosten und Ihren Anwendungsdaten zu verhindern.
- Sie können den Status Ihrer API-Schlüssel in [Google AI
  Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=de) einsehen. Wir werden Sie proaktiv informieren, wenn wir feststellen, dass Ihre API-Schlüssel offengelegt wurden, damit Sie sofort Maßnahmen ergreifen können.

## Modellausgabe verbessern

Wenn Sie qualitativ hochwertigere Modellausgaben wünschen, sollten Sie strukturiertere Prompts schreiben. Auf der
[Prompt Engineering Guide](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de)-Seite
werden einige grundlegende Konzepte, Strategien und Best Practices vorgestellt, die Ihnen den
Einstieg erleichtern.

## Informationen zu Tokenlimits

In unserem [Leitfaden zu Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de) erfahren Sie mehr darüber, wie
Sie Tokens zählen und welche Limits gelten.

## Bekannte Probleme

- Die API unterstützt nur eine begrenzte Anzahl von Sprachen. Wenn Sie Prompts in nicht unterstützten Sprachen senden, können unerwartete oder sogar blockierte Antworten zurückgegeben werden. [Auf der Seite „Verfügbare Sprachen“ finden Sie aktuelle Informationen.](https://ai.google.dev/gemini-api/docs/models?hl=de#supported-languages)

## Fehler melden

Wenn Sie Fragen haben, können Sie sich im
[Google AI-Entwicklerforum](https://discuss.ai.google.dev?hl=de)
an der Diskussion beteiligen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-08 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-08 (UTC)."],[],[]]
