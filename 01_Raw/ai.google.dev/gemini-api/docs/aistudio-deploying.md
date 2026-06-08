---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=de
fetched_at: 2026-06-08T15:07:28.649335+00:00
title: "\u00dcber Google\u00a0AI Studio bereitstellen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Über Google AI Studio bereitstellen

Mit Google AI Studio können Sie Ihre Full-Stack-Anwendungen direkt im Build-Modus bereitstellen. So gelangen Sie schnell vom Prototyp zu einer verwalteten, skalierbaren Produktionsumgebung.

## Bereitstellungsoptionen

Die Anforderungen für die Bereitstellung Ihrer Anwendung im Build-Modus von AI Studio hängen von der verwendeten Stufe ab:

- [**Google Cloud Starter-Stufe**](https://docs.cloud.google.com/docs/starter-tier?hl=de):
  Sie können bis zu zwei Full-Stack-Anwendungen veröffentlichen, ohne ein
  Google Cloud-Projekt oder ein Rechnungskonto einzurichten.
- **Standardbereitstellung**: Erfordert ein Google Cloud-Projekt, das mit Ihrem
  AI Studio-Konto verknüpft ist, und die aktivierte Abrechnung für dieses Projekt.

## Informationen zur Starter-Stufe

Die Google Cloud Starter-Stufe bietet einen optimierten Weg, um Anwendungen direkt aus Google AI Studio in Google Cloud bereitzustellen, ohne eine vollständige Google Cloud-Umgebung oder ein Rechnungskonto einzurichten.

Bei jeder Bereitstellung in Google AI Studio wird ein entsprechender Dienst in Cloud Run erstellt. Für Dienste, die in Google AI Studio mit der Starter-Stufe bereitgestellt werden, gelten die folgenden Einschränkungen:

- Sie können bis zu zwei Dienste bereitstellen.
- Ihre Dienste werden in einer
  [einzigen Cloud Run-Region bereitgestellt](https://docs.cloud.google.com/run/docs/locations?hl=de).

## Bereitstellungsschritte für die Starter-Stufe

Nachdem Sie Ihre App im Build-Modus entworfen haben, stellen Sie sie mit der Starter-Stufe bereit:

1. Klicken Sie rechts oben auf die Schaltfläche **Veröffentlichen**.
2. Klicken Sie auf **Jetzt starten**.
3. Klicken Sie auf **App veröffentlichen**.

Nach Abschluss der Bereitstellung stellt AI Studio eine Cloud Run-URL bereit, über die Sie auf Ihre Live-Anwendung zugreifen können.

## Standardmäßige Bereitstellung

Wenn sich Ihre Anwendungen weiterentwickeln, benötigen Sie möglicherweise Funktionen, die über die Starter-Stufe hinausgehen, z. B. höhere Kontingente, mehr Rechenressourcen oder andere Google Cloud-Produkte, die in der Starter-Stufe nicht verfügbar sind. Um diese Funktionen freizuschalten, können Sie Ihr vollständig verwaltetes Starter-Stufen-Projekt in ein Standard-Google Cloud-Projekt umwandeln.

So können Sie nahtlos skalieren, ohne Ihre Fortschritte zu verlieren. Folgen Sie der Anleitung, um
[ein Cloud-Rechnungskonto zu erstellen](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=de#create-new-billing-account), die Standard-Nutzungsbedingungen von Google Cloud formell zu akzeptieren und
[ein Upgrade auf ein Standard-Google Cloud-Projekt durchzuführen](https://docs.cloud.google.com/docs/starter-tier?hl=de#upgradee).
Weitere Informationen finden Sie unter
[Einrichtung für kostenpflichtige Konten](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=de#paid-setup).

Weitere Informationen zu Abrechnungsstufen finden Sie unter [Abrechnung](https://ai.google.dev/gemini-api/docs/billing?hl=de).

## Anwendung löschen

Wenn Sie Ihre App nicht mehr benötigen, können Sie sie in Google AI Studio löschen. Folgen Sie dazu dieser Anleitung:

1. Rufen Sie in Google AI Studio die
   [Seite „Apps“](https://aistudio.google.com/app/apps?hl=de) auf.
2. Wählen Sie im Menü auf der linken Seite **Apps** aus.
3. Bewegen Sie den Mauszeiger auf die App, die Sie löschen möchten.
4. Klicken Sie rechts neben der Zeile auf das Papierkorbsymbol, um die App zu löschen.

## Nächste Schritte

- Weitere Informationen zur
  [Google Cloud Starter-Stufe](https://docs.cloud.google.com/docs/starter-tier?hl=de).
- Informationen zur [Abrechnung](https://ai.google.dev/gemini-api/docs/billing?hl=de) in der Gemini API

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-16 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-16 (UTC)."],[],[]]
