---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=de
fetched_at: 2026-10-26T05:40:26.086265+00:00
title: "Kontext-Caching \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Kontext-Caching

In einem typischen KI-Workflow werden dieselben Eingabe-Tokens möglicherweise immer wieder an ein Modell übergeben. Die Gemini API bietet implizites Caching, um Leistung und Kosten zu optimieren.

## Implizites Caching

Implizites Caching ist für alle Gemini 2.5- und neueren Modelle standardmäßig aktiviert. Es wird sowohl für [zustandsorientierte](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#multi-turn-conversations) (mit `previous_interaction_id`) als auch für [zustandslose](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#stateless-conversations) Unterhaltungsmodi unterstützt.
Wir geben Kosteneinsparungen automatisch weiter, wenn Ihre Anfrage auf Caches trifft. Sie müssen nichts konfigurieren, um sie zu aktivieren. In der folgenden Tabelle ist die Mindestanzahl von Eingabetokens für jedes Modell aufgeführt:

| Modell | Mindest-Tokenlimit |
| --- | --- |
| Gemini 4 Argon | 4.096 |
| Gemini 3.8 Flash | 4.096 |
| Gemini 3.6 Flash | 4.096 |
| Gemini 3.1 Pro (Vorabversion) | 4.096 |
| Gemini 2.5 Flash | 2.048 |
| Gemini 2.5 Pro | 2.048 |

So erhöhen Sie die Wahrscheinlichkeit eines impliziten Cache-Treffers:

- Versuchen Sie, große und häufige Inhalte am Anfang des Prompts zu platzieren.
- Versuchen Sie, Anfragen mit ähnlichem Präfix innerhalb kurzer Zeit zu senden.

Die Anzahl der Tokens, die Cache-Treffer waren, finden Sie im Feld `usage.total_cached_tokens` (Python und JavaScript) des Antwortobjekts.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-23 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-23 (UTC)."],[],[]]
