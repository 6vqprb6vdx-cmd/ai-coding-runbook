---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=de
fetched_at: 2026-08-03T04:25:50.309751+00:00
title: "Datenerfassung und \u2011freigabe \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Datenerfassung und ‑freigabe

Auf dieser Seite werden die Speicherung und Verwaltung von
[Gemini API-Logs](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de) beschrieben. Dabei handelt es sich um API-Daten von Entwicklern aus unterstützten Gemini API-Aufrufen für Projekte mit aktivierter Abrechnung. Logs umfassen den gesamten Prozess von der Anfrage eines Nutzers bis zur Antwort des Modells.
Diese Logs sind privat für Ihr Google Cloud-Projekt und getrennt von allen
Logs, die ausschließlich zur [Missbrauchsüberwachung](https://ai.google.dev/gemini-api/docs/usage-policies?hl=de)
verwendet werden.

## Daten, die freigegeben werden können

Als Projektinhaber haben Sie die Möglichkeit, die Protokollierung von Gemini API-Aufrufen zu aktivieren. Sie können die Logs für eigene Zwecke verwenden oder Google Feedback geben und die Logs mit Google teilen, damit wir unsere Modelle kontinuierlich verbessern können.

Wenn die Protokollierung aktiviert ist, können Sie uns helfen, KI-Systeme zu entwickeln, die für Entwickler in verschiedenen Bereichen und Anwendungsfällen weiterhin wertvoll sind. Dazu können Sie die folgenden Daten zur Produktverbesserung und zum Modelltraining beitragen:

- **Datasets**:Über die Benutzeroberfläche „Logs und Datasets“ von Google AI Studio können Sie Logs (Anfragen, Antworten, Metadaten usw.) aus unterstützten Gemini API-Aufrufen auswählen. Diese werden durch Aufnahme in Datasets beigetragen. Sie haben die Möglichkeit, die Aufnahme während der Dataset-Erstellung zu deaktivieren.
- **Feedback**:Wenn Sie Logs überprüfen, können Sie Feedback geben, z. B. mit „Mag ich“ und „Mag ich nicht“ bewerten und Kommentare schreiben.

Wenn Sie ein Dataset mit Google teilen, werden Ihre Logs in diesem Dataset, einschließlich
Anfragen und Antworten, gemäß unseren
[Bedingungen](https://developers.google.com/terms?hl=de) für
"[Kostenlose Dienste](https://ai.google.dev/gemini-api/terms?hl=de#data-use-unpaid)"
verarbeitet. Das Dataset kann also verwendet werden, um Google
Produkte, ‑Dienste und Technologien für maschinelles Lernen zu entwickeln und zu verbessern, einschließlich der Verbesserung und des
Trainings unserer Modelle. **Geben Sie keine personenbezogenen, sensiblen oder vertraulichen Informationen an.**

## Wie wir Ihre Daten verwenden

Logs werden standardmäßig maximal 55 Tage lang aufbewahrt. Danach werden sie automatisch zur Löschung markiert. Der Aufbewahrungszeitraum für ein Projekt kann in AI Studio aktualisiert werden, sodass Logs nach 7, 14, 28 oder 55 Tagen automatisch zur Löschung markiert werden.

[Datasets](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de) können erstellt werden, um Logs von
Interesse über den festgelegten Aufbewahrungszeitraum hinaus für nachgelagerte Anwendungsfälle aufzubewahren und
optional zur Verbesserung von Modellen beizutragen. Für Logs, die in Datasets gespeichert sind, gibt es keine festgelegten Aufbewahrungszeiträume.

Da die Protokollierung standardmäßig nur für Projekte mit aktivierter Abrechnung verfügbar ist,
werden Prompts und Antworten in Logs gemäß unseren [Bedingungen](https://developers.google.com/terms?hl=de)
zur Datennutzung nicht zur Produktverbesserung oder
‑entwicklung verwendet.

Wenn Sie Datasets Ihrer Logs mit Google teilen, werden diese Datasets als Daten aus der Praxis verwendet, um die Vielfalt der Bereiche und Kontexte besser zu verstehen, in denen KI-Systeme und ‑Anwendungen eingesetzt werden. Diese Daten können verwendet werden, um die Modellqualität zu verbessern und das Training und die Bewertung zukünftiger Modelle und Dienste zu unterstützen. Diese Daten werden gemäß unseren Bedingungen zur Datennutzung für [kostenlose Dienste](https://ai.google.dev/gemini-api/terms?hl=de#data-use-unpaid) verarbeitet.

Prüfer können die von Ihnen freigegebenen API-Eingaben und ‑Ausgaben lesen, mit Anmerkungen versehen und verarbeiten. Bevor Daten zur Modellverbesserung verwendet werden, ergreift Google im Rahmen dieses Prozesses Maßnahmen, um die Privatsphäre der Nutzer zu schützen. Dazu wird unter anderem dafür gesorgt, dass entsprechende Daten nicht mit Ihrem Google-Konto, API-Schlüssel und Cloud-Projekt in Verbindung gebracht werden können, bevor sie von Prüfern eingesehen oder mit Vermerken versehen werden.

## Datenberechtigungen

Wenn Sie API-Daten beitragen, bestätigen Sie, dass Sie die erforderlichen Berechtigungen haben, damit Google die Daten wie in dieser Dokumentation beschrieben verarbeiten und verwenden kann. **Bitte tragen Sie keine Logs bei, die sensible, vertrauliche oder geschützte Informationen enthalten, die über den kostenpflichtigen Dienst erhalten wurden.**
Die Befugnis, die Sie Google unter dem Abschnitt „[Einreichung von Inhalten](https://developers.google.com/terms?hl=de#b_submission_of_content)“ der API-Bedingungen erteilen, erstreckt sich auch auf alle Inhalte (z.B. Prompts, einschließlich zugehöriger Systemanweisungen, im Cache gespeicherter Inhalte und Dateien wie Bilder, Videos oder Dokumente), die Sie an die Dienste senden, und auf alle generierten Antworten, soweit dies nach geltendem Recht für deren Nutzung durch uns erforderlich ist.

## Datenfreigabe und Feedback

Sie können uns helfen, die KI-Forschung, die Gemini API und Google AI Studio weiterzuentwickeln, indem Sie Ihre Daten als Beispiele freigeben. So können wir unsere Modelle in verschiedenen Kontexten kontinuierlich verbessern und KI-Systeme entwickeln, die für Entwickler in verschiedenen Bereichen und Anwendungsfällen weiterhin wertvoll sind.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-09 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-09 (UTC)."],[],[]]
