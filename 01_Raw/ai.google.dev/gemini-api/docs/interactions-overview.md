---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de
fetched_at: 2026-08-10T03:10:05.708946+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Interactions API

Die Interactions API ist die beste Möglichkeit, Anwendungen mit Gemini-Modellen und ‑Agents zu entwickeln. Seit Juni 2026 ist sie allgemein verfügbar und wird für alle neuen Projekte empfohlen. Die ursprüngliche [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=de) API wird weiterhin vollständig unterstützt.

## Vorteile der Interactions API

- **Universelle Schnittstelle für alle Anwendungen**: Diese Schnittstelle ist als Standardschnittstelle für alle Anwendungsfälle konzipiert, einschließlich der Textgenerierung in einem Durchgang, des multimodalen Verständnisses, strukturierter Ausgaben, der Tool-Orchestrierung und von Agent-Workflows.
- **Eine API für Modelle und Agents**: Ein einheitlicher Endpunkt und einheitliches Muster zum direkten Aufrufen von Standard-Gemini-Modellen sowie spezialisierten Agents wie Deep Research und benutzerdefinierten verwalteten Agents.
- **Neue Funktionen**: Funktionen wie der optionale serverseitige Unterhaltungsstatus mit `previous_interaction_id`, beobachtbare Ausführungsschritte für das Debugging und das Rendern der Benutzeroberfläche sowie die [Hintergrundausführung](https://ai.google.dev/gemini-api/docs/background-execution?hl=de) für lang andauernde Aufgaben mit `background=true`.
- **Geringere Kosten durch höhere Cache-Trefferraten**: Bei Verwendung von Unterhaltungen mit mehreren Durchgängen ermöglicht die optionale serverseitige Statusverwaltung ein effizienteres Kontext-Caching über mehrere Durchgänge hinweg, wodurch die Tokenkosten gesenkt werden.
- **Einführung neuer Funktionen**: Künftig werden alle neuen Modelle, multimodalen Funktionen, Tools und Agent-Funktionen über die Interactions API eingeführt.

Standardmäßig werden Anfragen in der Interactions API gespeichert, damit Sie die serverseitigen Funktionen zur Statusverwaltung mit `previous_interaction_id` nutzen können. Sie können das statuslose Verhalten aktivieren, indem Sie `store=false` festlegen. Weitere Informationen finden Sie im Abschnitt [Datenaufbewahrung](#data-storage-retention).

## Jetzt starten

- **KI-Programmieragenten einrichten**: Verbinden Sie sich mit dem **Gemini Docs MCP** und installieren Sie den `gemini-interactions-api`-Skill, um Ihrem Assistenten direkten Zugriff auf die neuesten Entwicklerdokumente und Best Practices zu ermöglichen. Eine ausführliche Anleitung finden Sie im [Leitfaden zum Einrichten Ihres Coding-Agents](https://ai.google.dev/gemini-api/docs/coding-agents?hl=de).
- **Von `generateContent` migrieren**: Wenn Sie eine bestehende Integration haben, folgen Sie der [Migrationsanleitung](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=de), um zur Interactions API zu wechseln.
- **Erste Schritte**: Folgen Sie der Anleitung unter [Erste Schritte mit der Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=de).

### Leitfäden für Funktionen

In diesen Leitfäden erfahren Sie mehr über die spezifischen Funktionen der Interactions API. Mit dem Ein/Aus-Schalter auf diesen Seiten können Sie zwischen der generateContent API und der Interactions API wechseln:

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de)
- [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de)
- [Bildverständnis](https://ai.google.dev/gemini-api/docs/image-understanding?hl=de)
- [Audioverständnis](https://ai.google.dev/gemini-api/docs/audio?hl=de)
- [Video-Understanding](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de)
- [Dokumentverarbeitung](https://ai.google.dev/gemini-api/docs/document-processing?hl=de)
- [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)
- [Strukturierte Ausgabe](https://ai.google.dev/gemini-api/docs/structured-output?hl=de)
- [Deep Research-Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=de)
- [Flex-Inferenz](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de)
- [Prioritätsinferenz](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de)

## Funktionsweise der Interactions API

Die Interactions API dreht sich um eine zentrale Ressource: die [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=de#Resource:Interaction). Ein `Interaction` steht für einen vollständigen Zug in einer Unterhaltung oder Aufgabe. Es dient als Sitzungsaufzeichnung und enthält den gesamten Verlauf einer Interaktion als chronologische Abfolge von **Ausführungsschritten**. Diese Schritte umfassen Modellüberlegungen, serverseitige oder clientseitige Tool-Aufrufe und Ergebnisse (z. B. `function_call` und `function_result`) sowie die endgültige `model_output`. Die gespeicherte Ressource (abgerufen über `interactions.get`) enthält auch `user_input`-Schritte für den vollständigen Kontext. Die `interactions.create`-Antwort gibt jedoch nur vom Modell generierte Schritte zurück.

Wenn Sie einen Aufruf an [`interactions.create`](https://ai.google.dev/api/interactions-api?hl=de#CreateInteraction) senden, erstellen Sie eine neue `Interaction`-Ressource.

### Serverseitige Statusverwaltung

Sie können die `id` einer abgeschlossenen Interaktion in einem nachfolgenden Aufruf mit dem Parameter `previous_interaction_id` verwenden, um die Unterhaltung fortzusetzen. Der Server verwendet diese ID, um den Unterhaltungsverlauf abzurufen. So müssen Sie nicht den gesamten Chatverlauf noch einmal senden.

Mit dem Parameter `previous_interaction_id` wird nur der Unterhaltungsverlauf (Ein- und Ausgaben) mit `previous_interaction_id` beibehalten. Die anderen Parameter sind **interaktionsbezogen** und gelten nur für die jeweilige Interaktion, die Sie gerade generieren:

- `tools`
- `system_instruction`
- `generation_config` (einschließlich `thinking_level`, `temperature` usw.)

Das bedeutet, dass Sie diese Parameter bei jeder neuen Interaktion neu angeben müssen, wenn sie angewendet werden sollen. Diese serverseitige Statusverwaltung ist optional. Sie können auch im zustandslosen Modus arbeiten, indem Sie den vollständigen Unterhaltungsverlauf in jeder Anfrage senden.

### Datenspeicherung und ‑aufbewahrung

Standardmäßig speichert die API alle Interaktionsobjekte (`store=true`), um die Verwendung von serverseitigen Funktionen zur Statusverwaltung (mit `previous_interaction_id`), [Hintergrundausführung](https://ai.google.dev/gemini-api/docs/background-execution?hl=de) (mit `background=true`) und Observability zu vereinfachen.

- **Aboversion**: Das System behält Interaktionen **55 Tage** lang bei.
- **Kostenloses Kontingent**: Interaktionen werden **einen Tag** lang gespeichert.

Wenn Sie das nicht möchten, können Sie in Ihrer Anfrage `store=false` festlegen. Diese Einstellung ist unabhängig von der Statusverwaltung. Sie können die Speicherung für jede Interaktion deaktivieren. `store=false` ist jedoch nicht mit der [Hintergrundausführung](https://ai.google.dev/gemini-api/docs/background-execution?hl=de) kompatibel und verhindert die Verwendung von `previous_interaction_id` für nachfolgende Züge.

Bei Projekten im kostenpflichtigen Tarif können Sie das Aufbewahrungszeitfenster in [AI Studio](https://aistudio.google.com/logs?hl=de) konfigurieren, um Protokolle nach 7, 14, 28 oder 55 Tagen automatisch zum Löschen aus dem Projektspeicher zu markieren. Eine kürzere Aufbewahrungsdauer kann sich auf das Abrufen vergangener Unterhaltungen auswirken.

Sie können gespeicherte Interaktionen jederzeit programmatisch mit der Methode [`delete`](https://ai.google.dev/api/interactions-api?hl=de#deleteInteraction) löschen. Dazu ist die Interaktions-ID erforderlich. Sie können auch gespeicherte Interaktionslogs in [AI Studio](https://aistudio.google.com/logs?hl=de) ansehen und verwalten, einschließlich des Löschens aus dem Projektspeicher.

Nach Ablauf der Aufbewahrungsdauer werden Ihre Daten automatisch gelöscht.

Interaktionsobjekte werden gemäß den [Nutzungsbedingungen](https://ai.google.dev/gemini-api/terms?hl=de) verarbeitet.

### Interaktionen in AI Studio ansehen

Die API speichert Interactions API-Anfragen, die mit `store=true` für Projekte in der kostenpflichtigen Stufe ausgeführt werden. Sie können sie direkt auf der [Seite „Logs“ in Google AI Studio](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=de) aufrufen. Weitere Informationen finden Sie im [Leitfaden zu Logs](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de).

## Best Practices

- **Cache-Trefferrate**: Implizites Caching wird sowohl im zustandsbehafteten als auch im zustandslosen Modus unterstützt (siehe [Kurzanleitung](https://ai.google.dev/gemini-api/docs/get-started?hl=de#4_multi-turn_conversations)). Wenn Sie `previous_interaction_id` (zustandsbehaftet) verwenden, um Unterhaltungen fortzusetzen, kann das System den Unterhaltungsverlauf einfacher implizit zwischenspeichern. Das verbessert die Leistung und senkt die Kosten.
- **Interaktionen mischen**: Sie können Agent- und Modellinteraktionen in einem Gespräch mischen. Sie können beispielsweise einen spezialisierten Agenten wie den Deep Research Agent für die erste Datenerhebung verwenden und dann ein Standard-Gemini-Modell für Folgeaufgaben wie das Zusammenfassen oder Umformatieren nutzen. Diese Schritte lassen sich mit dem `previous_interaction_id` verknüpfen.

## Unterstützte Modelle und KI-Agenten

| Modellname | Typ | Modell-ID |
| --- | --- | --- |
| Gemini 3.5 Flash | Modell | `gemini-3.5-flash` |
| Gemini 3.1 Pro (Vorabversion) | Modell | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash Lite | Modell | `gemini-3.1-flash-lite` |
| Gemini 3 Flash (Vorabversion) | Modell | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Modell | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Modell | `gemini-2.5-flash` |
| Gemini 2.5 Flash-Lite | Modell | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Modell | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | Modell | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS (Vorabversion) | Modell | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Modell | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Modell | `gemma-4-26b-a4b-it` |
| Lyria 3-Clip-Vorschau | Modell | `lyria-3-clip-preview` |
| Lyria 3 Pro (Vorabversion) | Modell | `lyria-3-pro-preview` |
| Deep Research-Vorabversion | Agent | `deep-research-preview-04-2026` |
| Deep Research-Vorabversion | Agent | `deep-research-max-preview-04-2026` |
| Antigravity-Vorschau | Agent | `antigravity-preview-05-2026` |

## SDKs

Sie können die aktuelle Version der Google GenAI SDKs verwenden, um auf die Interactions API zuzugreifen.

- In Python ist dies das Paket `google-genai` ab Version `2.3.0`.
- In JavaScript ist das das `@google/genai`-Paket ab Version `2.3.0`.

Weitere Informationen zum Installieren der SDKs finden Sie auf der Seite [Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de).

## Beschränkungen

- **Remote-MCP**: Gemini 3 unterstützt kein Remote-MCP. Diese Funktion wird bald eingeführt.
- **Kompatibilität von Modellen mit mehreren Durchgängen**: Wenn Sie verschiedene Modelle in einer Unterhaltung (mit oder ohne Status) kombinieren, müssen nachfolgende Modelle die Ausgabemodalitäten der vorherigen Modelle als Eingabe unterstützen. Wenn Sie beispielsweise ein Bild mit `gemini-3.1-flash-image` generieren, können Sie die Unterhaltung nicht mit einem Modell fortsetzen, das keine Bildeingaben akzeptiert, z. B. ein reines Textmodell oder ein Musikgenerierungsmodell wie Lyria.

Die folgenden Funktionen werden von der [`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=de) API unterstützt, sind aber **noch nicht** in der Interactions API verfügbar:

- **[Videometadaten](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de)**: Das Feld `video_metadata` wird verwendet, um Clipping-Intervalle und benutzerdefinierte Frameraten für die Videoanalyse festzulegen.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de)**
- **[Automatische Funktionsaufrufe (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=de#automatic_function_calling_python_only)**
- **[Explizites Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de)**: Das serverseitige implizite Caching ist in der Interactions API über `previous_interaction_id` verfügbar.
- **[Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de)**: Benutzerdefinierte Sicherheitseinstellungen werden in der Interactions API nicht unterstützt.

## Feedback

Ihr Feedback ist für die Entwicklung der Interactions API von entscheidender Bedeutung.
Im [Google AI Developer Community-Forum](https://discuss.ai.google.dev/c/gemini-api/4?hl=de) können Sie Ihre Meinung äußern, Fehler melden oder Funktionen anfragen.

## Nächste Schritte

- [Kurzanleitung für die Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=de)
- [Weitere Informationen zum Gemini Deep Research-Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-16 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-16 (UTC)."],[],[]]
