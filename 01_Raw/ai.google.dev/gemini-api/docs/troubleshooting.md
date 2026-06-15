---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=de
fetched_at: 2026-06-15T06:29:32.402743+00:00
title: "Tipps zur Fehlerbehebung \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Tipps zur Fehlerbehebung

In dieser Anleitung erfahren Sie, wie Sie häufige Probleme diagnostizieren und beheben, die beim Aufrufen der Gemini API auftreten können. Probleme können entweder im Backend-Dienst der Gemini API oder in den Client-SDKs auftreten. Unsere Client-SDKs sind Open Source und in den folgenden Repositorys verfügbar:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Wenn Sie Probleme mit dem API-Schlüssel haben, prüfen Sie, ob Sie ihn gemäß der [Anleitung zum Einrichten von API-Schlüsseln](https://ai.google.dev/gemini-api/docs/api-key?hl=de) richtig eingerichtet haben.

## Gemini API – Backend-Dienstfehlercodes

In der folgenden Tabelle sind häufige Backend-Fehlercodes aufgeführt, die auftreten können, zusammen mit Erklärungen zu ihren Ursachen und Schritten zur Fehlerbehebung:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP-Code** | **Status** | **Beschreibung** | **Beispiel** | **Lösung** |
| 400 | INVALID\_ARGUMENT | Der Anfragetext ist fehlerhaft. | Ihre Anfrage enthält einen Tippfehler oder ein Pflichtfeld fehlt. | Informationen zum Anfrageformat, zu Beispielen und zu unterstützten Versionen finden Sie in der [API-Referenz](https://ai.google.dev/api?hl=de). Wenn Sie Funktionen einer neueren API-Version mit einem älteren Endpunkt verwenden, kann dies zu Fehlern führen. |
| 400 | FAILED\_PRECONDITION | Die kostenlose Stufe der Gemini API ist in Ihrem Land nicht verfügbar. Aktivieren Sie die Abrechnung für Ihr Projekt in Google AI Studio. | Sie stellen eine Anfrage in einer Region, in der das kostenlose Kontingent nicht unterstützt wird, und haben die Abrechnung für Ihr Projekt in Google AI Studio nicht aktiviert. | Wenn Sie die Gemini API verwenden möchten, müssen Sie ein kostenpflichtiges Abo über [Google AI Studio](https://aistudio.google.com/apikey?hl=de) einrichten. |
| 403 | PERMISSION\_DENIED | Ihr API-Schlüssel hat nicht die erforderlichen Berechtigungen. | Sie verwenden den falschen API-Schlüssel oder versuchen, ein abgestimmtes Modell zu verwenden, ohne die [richtige Authentifizierung](https://ai.google.dev/gemini-api/docs/model-tuning?hl=de) durchzuführen. | Prüfen Sie, ob Ihr API-Schlüssel festgelegt ist und die richtigen Zugriffsrechte hat. Außerdem müssen Sie sich richtig authentifizieren, um abgestimmte Modelle verwenden zu können. |
| 404 | NOT\_FOUND | Die angeforderte Ressource wurde nicht gefunden. | Eine in Ihrer Anfrage referenzierte Bild-, Audio- oder Videodatei wurde nicht gefunden. | Prüfen Sie, ob alle [Parameter in Ihrer Anfrage für Ihre API-Version gültig sind](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=de#check-api). |
| 429 | RESOURCE\_EXHAUSTED | Sie haben das Ratenlimit überschritten. | Sie senden mit der kostenlosen Gemini API zu viele Anfragen pro Minute. | Prüfen Sie, ob Sie das [Ratenlimit](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de) des Modells einhalten. [Fordern Sie bei Bedarf eine Kontingenterhöhung an](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de#request-rate-limit-increase). |
| 499 | ABGEBROCHEN | Der Vorgang wurde abgebrochen, üblicherweise vom Aufrufer. | Der Client hat die Verbindung geschlossen, bevor die API die Antwort fertigstellen konnte. | Prüfen Sie, ob Ihre Client- oder Netzwerkinfrastruktur die Verbindung vorzeitig schließt, z.B. aufgrund eines clientseitigen Timeouts. |
| 500 | INTERN | Bei Google ist ein unerwarteter Fehler aufgetreten. | Der Kontext Ihrer Eingabe ist zu lang. | Sehen Sie auf der [Statusseite der Gemini API](https://aistudio.google.com/status?hl=de) nach, ob es aktuelle Vorfälle gibt. Reduzieren Sie den Eingabekontext oder wechseln Sie vorübergehend zu einem anderen Modell (z.B. von Gemini 2.5 Pro zu Gemini 2.5 Flash) und prüfen Sie, ob es funktioniert. Alternativ können Sie auch etwas warten und die Anfrage noch einmal senden. Wenn das Problem weiterhin besteht, melden Sie es bitte über die Schaltfläche **Feedback geben** in Google AI Studio. |
| 503 | UNAVAILABLE | Möglicherweise ist der Dienst vorübergehend überlastet oder nicht erreichbar. | Der Dienst hat vorübergehend keine Kapazitäten mehr. | Sehen Sie auf der [Statusseite der Gemini API](https://aistudio.google.com/status?hl=de) nach, ob es aktuelle Vorfälle gibt. Wechseln Sie vorübergehend zu einem anderen Modell (z.B. von Gemini 2.5 Pro zu Gemini 2.5 Flash) und prüfen Sie, ob es funktioniert. Oder warten Sie etwas und wiederholen Sie Ihre Anfrage. Wenn das Problem nach dem Wiederholen weiterhin besteht, melden Sie es bitte über die Schaltfläche **Feedback geben** in Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Der Dienst kann die Verarbeitung nicht innerhalb der Frist abschließen. | Ihr Prompt (oder Kontext) ist zu groß, um rechtzeitig verarbeitet zu werden. | Legen Sie in Ihrer Clientanfrage ein längeres Zeitlimit fest, um diesen Fehler zu vermeiden. |

## API-Aufrufe auf Fehler bei Modellparametern prüfen

Prüfen Sie, ob die Parameter Ihres Modells die folgenden Werte einhalten:

|  |  |
| --- | --- |
| **Modellparameter** | **Werte (Bereich)** |
| Anzahl der Kandidaten | 1–8 (Ganzzahl) |
| Temperatur | 0,0–1,0 |
| Maximale Ausgabetokens | Auf der [Seite „Modelle“](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de) können Sie die maximale Anzahl von Tokens für das von Ihnen verwendete Modell ermitteln. |
| TopP | 0,0–1,0 |

Achten Sie nicht nur darauf, dass Sie die richtigen Parameterwerte verwenden, sondern auch die richtige [API-Version](https://ai.google.dev/gemini-api/docs/api-versions?hl=de) (z.B. `/v1` oder `/v1beta`) und das richtige Modell, das die benötigten Funktionen unterstützt. Wenn eine Funktion beispielsweise in der Betaphase ist, ist sie nur in der API-Version `/v1beta` verfügbar.

## Prüfen, ob Sie das richtige Modell haben

Prüfen Sie, ob Sie ein unterstütztes Modell verwenden, das auf unserer [Seite „Modelle“](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de) aufgeführt ist.

## Höhere Latenz oder Tokennutzung bei 2.5-Modellen

Wenn Sie bei den Modellen 2.5 Flash und Pro eine höhere Latenz oder Tokennutzung feststellen, kann das daran liegen, dass **Thinking standardmäßig aktiviert** ist, um die Qualität zu verbessern. Wenn Sie Geschwindigkeit priorisieren oder Kosten minimieren müssen, können Sie die Denkphase anpassen oder deaktivieren.

[Hier finden Sie](https://ai.google.dev/gemini-api/docs/thinking?hl=de#set-budget) Anleitungen und Beispielcode.

## Sicherheitsprobleme

Wenn ein Prompt aufgrund einer Sicherheitseinstellung in Ihrem API-Aufruf blockiert wurde, überprüfen Sie den Prompt im Hinblick auf die Filter, die Sie im API-Aufruf festgelegt haben.

Wenn Sie `BlockedReason.OTHER` sehen, verstößt die Anfrage oder Antwort möglicherweise gegen die [Nutzungsbedingungen](https://ai.google.dev/terms?hl=de) oder wird anderweitig nicht unterstützt.

## Problem mit der Rezitation

Wenn das Modell die Ausgabe aufgrund des RECITATION-Grundes beendet, kann es sein, dass die Modellausgabe bestimmten Daten ähnelt. Um dieses Problem zu beheben, sollten Sie den Prompt bzw. Kontext so einzigartig wie möglich gestalten und eine höhere Temperatur verwenden.

## Problem mit sich wiederholenden Tokens

Wenn Sie wiederholte Ausgabetokens sehen, können Sie versuchen, sie mit den folgenden Vorschlägen zu reduzieren oder zu eliminieren.

| Beschreibung | Ursache | Vorgeschlagene Problemumgehung |
| --- | --- | --- |
| Wiederholte Bindestriche in Markdown-Tabellen | Dies kann passieren, wenn der Inhalt der Tabelle lang ist, da das Modell versucht, eine visuell ausgerichtete Markdown-Tabelle zu erstellen. Die Ausrichtung in Markdown ist jedoch für das korrekte Rendern nicht erforderlich. | Fügen Sie Ihrem Prompt Anweisungen hinzu, um dem Modell spezifische Richtlinien für die Generierung von Markdown-Tabellen zu geben. Geben Sie Beispiele an, die diesen Richtlinien entsprechen. Sie können auch versuchen, die Temperatur anzupassen. Für das Generieren von Code oder sehr strukturierten Ausgaben wie Markdown-Tabellen hat sich eine hohe Temperatur (>= 0,8) als besser erwiesen.  Im Folgenden finden Sie ein Beispiel für Richtlinien, die Sie Ihrem Prompt hinzufügen können, um dieses Problem zu vermeiden:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Wiederholte Tokens in Markdown-Tabellen | Ähnlich wie bei den wiederholten Bindestrichen tritt dies auf, wenn das Modell versucht, den Inhalt der Tabelle visuell auszurichten. Die Ausrichtung in Markdown ist für das korrekte Rendern nicht erforderlich. | - Fügen Sie Ihrem System-Prompt Anweisungen wie die folgenden hinzu:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Versuche, die Temperatur anzupassen. Höhere Temperaturen (>= 0,8) tragen in der Regel dazu bei, Wiederholungen oder Duplikate in der Ausgabe zu vermeiden. |
| Wiederholte Zeilenumbrüche (`\n`) in der strukturierten Ausgabe | Wenn die Modelleingabe Unicode- oder Escape-Sequenzen wie `\u` oder `\t` enthält, kann dies zu wiederholten Zeilenumbrüchen führen. | - Suchen Sie in Ihrem Prompt nach verbotenen Escape-Sequenzen und ersetzen Sie sie durch UTF-8-Zeichen. Wenn Sie beispielsweise die Escape-Sequenz `\u` in Ihren JSON-Beispielen verwenden, kann es sein, dass das Modell sie auch in seiner Ausgabe verwendet. - Weisen Sie das Modell auf zulässige Escapes hin. Fügen Sie eine Systemanweisung wie diese hinzu:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Wiederholter Text bei Verwendung strukturierter Ausgabe | Wenn die Felder in der Modellausgabe in einer anderen Reihenfolge als im definierten strukturierten Schema stehen, kann dies zu sich wiederholendem Text führen. | - Geben Sie die Reihenfolge der Felder nicht in Ihrem Prompt an. - Machen Sie alle Ausgabefelder zu Pflichtfeldern. |
| Wiederholte Toolaufrufe | Das kann passieren, wenn das Modell den Kontext früherer Überlegungen verliert und/oder einen nicht verfügbaren Endpunkt aufruft, zu dem es gezwungen wird. | Weisen Sie das Modell an, den Status in seinem Denkprozess beizubehalten. Fügen Sie Folgendes am Ende Ihrer Systemanweisungen hinzu:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Wiederholter Text, der nicht Teil der strukturierten Ausgabe ist | Das kann passieren, wenn das Modell bei einer Anfrage hängen bleibt, die es nicht beantworten kann. | - Wenn die Funktion „Denken“ aktiviert ist, sollten Sie in den Anweisungen keine expliziten Anweisungen dazu geben, wie ein Problem durchdacht werden soll. Fragen Sie einfach nach der endgültigen Ausgabe. - Versuchen Sie es mit einer höheren Temperatur ≥ 0,8. - Fügen Sie Anweisungen wie „Fasse dich kurz“, „Wiederhole dich nicht“ oder „Gib die Antwort nur einmal“ hinzu. |

## Blockierte oder nicht funktionierende API-Schlüssel

In diesem Abschnitt wird beschrieben, wie Sie prüfen, ob Ihr Gemini API-Schlüssel gesperrt ist, und was Sie in diesem Fall tun können.

### Gründe für die Sperrung von Schlüsseln

Wir haben eine Sicherheitslücke entdeckt, durch die einige API-Schlüssel öffentlich zugänglich gewesen sein könnten. Zum Schutz Ihrer Daten und zur Verhinderung unbefugten Zugriffs haben wir diese bekannten, offengelegten Schlüssel proaktiv für den Zugriff auf die Gemini API gesperrt.

### Prüfen, ob Ihre Schlüssel betroffen sind

Wenn Ihr Schlüssel bekannt ist, können Sie ihn nicht mehr mit der Gemini API verwenden. In [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=de) können Sie nachsehen, ob Ihre API-Schlüssel für Aufrufe der Gemini API gesperrt sind, und neue Schlüssel generieren. Möglicherweise wird auch der folgende Fehler zurückgegeben, wenn Sie versuchen, diese Schlüssel zu verwenden:

```
Your API key was reported as leaked. Please use another API key.
```

### Maßnahmen bei blockierten API-Schlüsseln

Sie sollten neue API-Schlüssel für Ihre Gemini API-Integrationen mit [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=de) generieren. Wir empfehlen dringend, Ihre API-Schlüsselverwaltung zu überprüfen, um sicherzustellen, dass Ihre neuen Schlüssel sicher aufbewahrt und nicht öffentlich zugänglich sind.

### Unerwartete Kosten aufgrund von Sicherheitslücken

[Supportanfrage zur Abrechnung einreichen](https://console.cloud.google.com/support/chat?hl=de)
Unser Abrechnungsteam arbeitet daran und wir werden Sie so bald wie möglich über Neuigkeiten informieren.

### Sicherheitsmaßnahmen von Google bei offengelegten Schlüsseln

**Wie kann Google mein Konto vor Kostenüberschreitungen und Missbrauch schützen, wenn meine API-Schlüssel offengelegt werden?**

- Wir stellen API-Schlüssel künftig nur noch aus, wenn Sie einen neuen Schlüssel über [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=de) anfordern. Diese Schlüssel sind standardmäßig auf Google AI Studio beschränkt und akzeptieren keine Schlüssel von anderen Diensten.
  So wird eine unbeabsichtigte Verwendung von Schlüsseln verhindert.
- Wir blockieren standardmäßig API-Schlüssel, die offengelegt und mit der Gemini API verwendet werden. So können wir Missbrauch von Kosten und Ihren Anwendungsdaten verhindern.
- Den Status Ihrer API-Schlüssel finden Sie in [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=de). Wir werden Sie proaktiv informieren, wenn wir feststellen, dass Ihre API-Schlüssel offengelegt wurden, damit Sie sofort Maßnahmen ergreifen können.

## Modellausgabe verbessern

Wenn Sie eine höhere Qualität der Modellausgaben wünschen, sollten Sie strukturiertere Prompts schreiben. Auf der Seite [Leitfaden zum Prompt Engineering](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=de) werden einige grundlegende Konzepte, Strategien und Best Practices vorgestellt, die Ihnen den Einstieg erleichtern.

## Informationen zu Tokenlimits

In unserem [Leitfaden zu Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de) erfahren Sie mehr darüber, wie Tokens gezählt werden und welche Limits gelten.

## Bekannte Probleme

- Die API unterstützt nur eine begrenzte Anzahl von Sprachen. Wenn Sie Prompts in nicht unterstützten Sprachen einreichen, kann das zu unerwarteten oder sogar blockierten Antworten führen. [Verfügbare Sprachen](https://ai.google.dev/gemini-api/docs/models?hl=de#supported-languages)

## Fehler melden

Wenn Sie Fragen haben, können Sie sich im [Google AI-Entwicklerforum](https://discuss.ai.google.dev?hl=de) an der Diskussion beteiligen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-10 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-10 (UTC)."],[],[]]
