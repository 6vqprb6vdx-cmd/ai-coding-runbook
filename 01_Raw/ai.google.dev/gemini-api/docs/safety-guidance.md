---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=de
fetched_at: 2026-05-18T13:01:18.500643+00:00
title: "Richtlinien zu Sicherheit und Faktualit\u00e4t \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Richtlinien zu Sicherheit und Faktualität

Modelle für generative künstliche Intelligenz sind leistungsstarke Tools, haben aber auch ihre Grenzen. Ihre Vielseitigkeit und Anwendbarkeit können manchmal zu unerwarteten Ausgaben führen, z. B. zu Ausgaben, die ungenau, voreingenommen oder anstößig sind. Die Nachbearbeitung und eine strenge manuelle Bewertung sind unerlässlich, um das Risiko von Schäden durch solche Ausgaben zu begrenzen.

Die von der Gemini API bereitgestellten Modelle können für eine Vielzahl von Anwendungen für generative KI und Natural Language Processing (NLP) verwendet werden. Die Verwendung dieser
Funktionen ist nur über die Gemini API oder die Webanwendung Google AI Studio
möglich. Ihre Nutzung der Gemini API unterliegt außerdem der [Richtlinie zur unzulässigen Nutzung von generativer KI](https://policies.google.com/terms/generative-ai/use-policy?hl=de) und den
[Nutzungsbedingungen für die Gemini API](https://ai.google.dev/terms?hl=de).

Ein Grund dafür, dass Large Language Models (LLMs) so nützlich sind, ist, dass sie kreative Tools sind, die viele verschiedene Sprachaufgaben bewältigen können. Leider bedeutet das auch, dass Large Language Models unerwartete Ausgaben generieren können, einschließlich Text, der beleidigend, grob oder tatsächlich falsch ist.
Außerdem ist es durch die unglaubliche Vielseitigkeit dieser Modelle schwierig, genau vorherzusagen, welche Art unerwünschter Ausgaben sie erzeugen könnten. Die
Gemini API wurde zwar unter Berücksichtigung der [KI-Prinzipien](https://ai.google/principles/?hl=de) von Google entwickelt, aber es liegt in der Verantwortung der Entwickler, diese Modelle verantwortungsvoll einzusetzen. Um Entwicklern bei der Erstellung sicherer und verantwortungsvoller Anwendungen zu helfen, bietet die Gemini API eine integrierte Inhaltsfilterung sowie anpassbare Sicherheitseinstellungen in vier Dimensionen von Schäden. Weitere Informationen finden Sie im
[Leitfaden zu den Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de). Außerdem wird die Fundierung mit aktivierter Google Suche angeboten, um die Faktengenauigkeit zu verbessern. Diese Funktion kann jedoch für Entwickler deaktiviert werden, deren Anwendungsfälle kreativer sind und nicht auf die Suche nach Informationen ausgerichtet sind.

In diesem Dokument werden einige Sicherheitsrisiken vorgestellt, die bei der Verwendung von LLMs auftreten können. Außerdem werden Empfehlungen für das Sicherheitsdesign und die Entwicklung gegeben. Hinweis: Gesetze und Verordnungen können ebenfalls Einschränkungen auferlegen. Diese Überlegungen gehen jedoch über den Rahmen dieses Leitfadens hinaus.

Beim Erstellen von Anwendungen mit LLMs werden die folgenden Schritte empfohlen:

- Sicherheitsrisiken Ihrer Anwendung verstehen
- Anpassungen zur Minimierung von Sicherheitsrisiken in Betracht ziehen
- Für Ihren Anwendungsfall geeignete Sicherheitstests durchführen
- Nutzerfeedback einholen und Nutzung überwachen

Die Anpassungs- und Testphasen sollten iterativ sein, bis Sie eine für Ihre Anwendung geeignete Leistung erzielen.

![Zyklus der Modellimplementierung](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=de)

## Sicherheitsrisiken Ihrer Anwendung verstehen

In diesem Zusammenhang wird Sicherheit als die Fähigkeit eines LLM definiert, Schäden für seine Nutzer zu vermeiden, z. B. durch die Generierung von toxischen Inhalten oder Inhalten, die Stereotypen fördern. Die über die Gemini API verfügbaren Modelle wurden unter Berücksichtigung der [KI-Grundsätze von Google](https://ai.google/principles/?hl=de) entwickelt und Ihre Nutzung unterliegt der Richtlinie zur [unzulässigen Nutzung von generativer KI](https://policies.google.com/terms/generative-ai/use-policy?hl=de). Die API bietet integrierte Sicherheitsfilter, um einige häufige Probleme mit Language Models zu beheben, z. B. toxische Sprache und Hassreden, und um Inklusivität zu fördern und Stereotypen zu vermeiden. Jede Anwendung kann jedoch unterschiedliche Risiken für ihre Nutzer bergen. Als Inhaber der Anwendung sind Sie dafür verantwortlich, Ihre Nutzer und die potenziellen Schäden zu kennen, die Ihre Anwendung verursachen kann, und dafür zu sorgen, dass Ihre Anwendung LLMs sicher und verantwortungsvoll verwendet.

Im Rahmen dieser Bewertung sollten Sie die Wahrscheinlichkeit des Auftretens von Schäden berücksichtigen und deren Schweregrad und Maßnahmen zur Minimierung ermitteln. Beispielsweise muss bei einer App, die Essays auf der Grundlage von Fakten generiert, mehr darauf geachtet werden, Fehlinformationen zu vermeiden, als bei einer App, die fiktive Geschichten zur Unterhaltung generiert. Eine gute Möglichkeit, potenzielle Sicherheitsrisiken zu untersuchen, besteht darin, Ihre Endnutzer und andere zu recherchieren, die von den Ergebnissen Ihrer Anwendung betroffen sein könnten. Dies kann viele Formen annehmen, z. B. die Recherche von Studien zum aktuellen Stand der Technik in Ihrem Anwendungsbereich, die Beobachtung, wie Nutzer ähnliche Apps verwenden, oder die Durchführung einer Nutzerstudie, einer Umfrage oder informeller Interviews mit potenziellen Nutzern.

#### Weitere Tipps

- Sprechen Sie mit einer vielfältigen Gruppe potenzieller Nutzer in Ihrer Zielgruppe
  über Ihre Anwendung und ihren beabsichtigten Zweck, um eine breitere Perspektive auf potenzielle Risiken zu erhalten und die Diversitätskriterien
  bei Bedarf anzupassen.
- Das vom National Institute of Standards and Technology (NIST) der US-Regierung veröffentlichte [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) bietet detailliertere Anleitungen und zusätzliche Lernressourcen für das KI-Risikomanagement.
- In der Veröffentlichung von DeepMind zu den
  [ethischen und sozialen Risiken von Schäden durch Language Models](https://arxiv.org/abs/2112.04359)
  werden die Möglichkeiten beschrieben, wie Anwendungen mit Language Models
  Schäden verursachen können.

## Anpassungen zur Minimierung von Sicherheits- und Faktengenauigkeitsrisiken in Betracht ziehen

Nachdem Sie sich ein Bild von den Risiken gemacht haben, können Sie entscheiden, wie Sie sie minimieren. Die Entscheidung, welche Risiken priorisiert werden sollen und wie viel Sie tun sollten, um sie zu vermeiden, ist entscheidend, ähnlich wie bei der Priorisierung von Fehlern in einem Softwareprojekt. Sobald Sie die Prioritäten festgelegt haben, können Sie über die Arten von Maßnahmen zur Minimierung nachdenken, die am besten geeignet sind. Oft können einfache Änderungen einen Unterschied machen und Risiken reduzieren.

Beachten Sie beim Entwerfen einer Anwendung beispielsweise Folgendes:

- **Modellausgabe optimieren** , um besser widerzuspiegeln, was im Kontext Ihrer Anwendung akzeptabel ist. Durch die Optimierung kann die Ausgabe des Modells vorhersehbarer und konsistenter werden und so bestimmte Risiken minimieren.
- **Eine Eingabemethode bereitstellen, die sicherere Ausgaben ermöglicht.** Die genaue Eingabe, die Sie einem LLM geben, kann einen Unterschied in der Qualität der Ausgabe machen.
  Es lohnt sich, mit Eingabe-Prompts zu experimentieren, um herauszufinden, was in Ihrem Anwendungsfall am sichersten funktioniert. Dann können Sie eine UX bereitstellen, die dies erleichtert. Sie können beispielsweise festlegen, dass Nutzer nur aus einer Drop-down-Liste mit Eingabe-Prompts auswählen können, oder Pop-up-Vorschläge mit beschreibenden Formulierungen anbieten, die sich im Kontext Ihrer Anwendung als sicher erwiesen haben.
- **Unsichere Eingaben blockieren und Ausgaben filtern, bevor sie dem Nutzer angezeigt werden.** In einfachen Fällen können Sperrlisten eingesetzt werden, um unsichere Wörter oder Formulierungen in Prompts oder Antworten zu ermitteln und zu blockieren oder um manuelle Prüfer zu beauftragen, solche Inhalte manuell zu ändern oder zu blockieren.
- **Trainierte Klassifikatoren verwenden, um jeden Prompt mit Tags für potenzielle Schäden oder bösartige Signale zu versehen.** Dann können verschiedene Strategien zum Umgang mit der Anfrage angewendet werden, je nach der Art des erkannten Schadens. Wenn die Eingabe beispielsweise offensichtlich bösartig oder missbräuchlich ist, kann sie blockiert und stattdessen eine vordefinierte Antwort ausgegeben werden.

  #### Weitere Tipps

  - Wenn Signale darauf hindeuten, dass die Ausgabe schädlich ist,
    kann die Anwendung die folgenden Optionen verwenden:
    - Eine Fehlermeldung oder eine vordefinierte Ausgabe zurückgeben.
    - Den Prompt noch einmal versuchen, falls eine alternative sichere Ausgabe generiert wird
      Manchmal führt derselbe Prompt zu unterschiedlichen Ausgaben
- **Maßnahmen gegen vorsätzlichen Missbrauch ergreifen** , z. B. jedem Nutzer eine eindeutige ID zuweisen und die Anzahl der Nutzerabfragen begrenzen, die in einem bestimmten Zeitraum gesendet werden können. Eine weitere Maßnahme besteht darin, sich vor möglichen Prompt-Injections zu schützen. Prompt-Injection ist ähnlich wie SQL-Injection eine Möglichkeit für böswillige Nutzer, einen Eingabe-Prompt zu erstellen, der die Ausgabe des Modells manipuliert, z. B. indem sie einen Eingabe-Prompt senden, der das Modell anweist, alle vorherigen Beispiele zu ignorieren. Weitere Informationen zu vorsätzlichem Missbrauch finden Sie in der
  [Richtlinie zur unzulässigen Nutzung von generativer KI](https://policies.google.com/terms/generative-ai/use-policy?hl=de).
- **Funktionen anpassen, um das inhärente Risiko zu verringern.**
  Aufgaben mit einem engeren Umfang (z.B. das Extrahieren von Keywords aus Textabschnitten) oder mit einer stärkeren menschlichen Aufsicht (z.B. das Generieren von Kurzformatinhalten, die von einem Menschen überprüft werden) bergen oft ein geringeres Risiko. Anstatt beispielsweise eine Anwendung zu erstellen, die eine E-Mail-Antwort von Grund auf neu verfasst, können Sie sie stattdessen auf das Erweitern einer Gliederung oder das Vorschlagen alternativer Formulierungen beschränken.
- **Sicherheitseinstellungen für schädliche Inhalte anpassen, um die Wahrscheinlichkeit zu verringern, dass potenziell schädliche Antworten angezeigt werden.** Die Gemini API bietet Sicherheitseinstellungen, die Sie während der Prototyping-Phase anpassen können, um zu ermitteln, ob Ihre Anwendung eine mehr oder weniger restriktive Sicherheitskonfiguration erfordert. Sie können diese Einstellungen in fünf Filterkategorien anpassen, um bestimmte Arten von Inhalten zuzulassen oder zu beschränken. Weitere Informationen zu den anpassbaren Sicherheitseinstellungen, die über die Gemini API verfügbar sind, finden Sie im [Leitfaden zu den Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de).
- **Potenzielle sachliche Ungenauigkeiten oder Halluzinationen verringern, indem Sie die Fundierung mit der Google Suche aktivieren.** Viele KI-Modelle sind experimentell und können sachlich falsche Informationen liefern, halluzinieren oder auf andere Weise problematische Ausgaben erzeugen. Die Funktion „Fundierung mit der Google Suche“ verbindet das Gemini-Modell mit Webinhalten in Echtzeit und funktioniert mit allen verfügbaren Sprachen. So kann Gemini genauere Antworten geben und überprüfbare Quellen über den Wissensstand des Modells hinaus zitieren.

## Für Ihren Anwendungsfall geeignete Sicherheitstests durchführen

Tests sind ein wichtiger Bestandteil der Entwicklung robuster und sicherer Anwendungen. Umfang, Umfang und Strategien für Tests variieren jedoch. Ein Haiku-Generator, der nur zum Spaß gedacht ist, birgt wahrscheinlich weniger schwerwiegende Risiken als beispielsweise eine Anwendung, die von Anwaltskanzleien verwendet wird, um juristische Dokumente zusammenzufassen und bei der Erstellung von Verträgen zu helfen. Der Haiku-Generator kann jedoch von einer größeren Anzahl von Nutzern verwendet werden, was bedeutet, dass das Potenzial für bösartige Versuche oder sogar unbeabsichtigte schädliche Eingaben größer sein kann. Auch der Implementierungskontext ist wichtig. Beispielsweise ist es weniger wahrscheinlich, dass eine Anwendung mit Ausgaben, die von menschlichen Experten überprüft werden, bevor Maßnahmen ergriffen werden, schädliche Ausgaben erzeugt als die identische Anwendung ohne diese Aufsicht.

Es ist nicht ungewöhnlich, mehrere Iterationen von Änderungen und Tests durchzuführen, bevor Sie sich sicher sind, dass Sie bereit für die Einführung sind, selbst bei Anwendungen mit relativ geringem Risiko. Zwei Arten von Tests sind besonders nützlich für KI-Anwendungen:

- **Sicherheitsbenchmarking** umfasst das Entwerfen von Sicherheitsmesswerten, die die Möglichkeiten widerspiegeln, wie Ihre Anwendung im Kontext der wahrscheinlichen Verwendung unsicher sein könnte. Anschließend wird getestet, wie gut Ihre Anwendung anhand von Bewertungs-Datasets abschneidet. Es empfiehlt sich, vor dem Testen die minimal akzeptablen Werte für die Sicherheitsmesswerte festzulegen, damit Sie 1) die Testergebnisse mit diesen Erwartungen vergleichen und 2) das Bewertungs-Dataset auf der Grundlage der Tests zusammenstellen können, die die für Sie wichtigsten Messwerte bewerten.

  #### Weitere Tipps

  - Verlassen Sie sich nicht zu sehr auf Standardansätze. Wahrscheinlich müssen Sie Ihre eigenen Test-Datasets mit menschlichen Bewertern erstellen, um den Kontext Ihrer Anwendung vollständig zu berücksichtigen.
  - Wenn Sie mehr als einen Messwert haben, müssen Sie entscheiden, wie Sie
    Kompromisse eingehen, wenn eine Änderung zu Verbesserungen für einen Messwert führt, aber sich negativ auf einen anderen auswirkt. Wie bei anderen Leistungsoptimierungen sollten Sie sich möglicherweise auf die Leistung im Worst-Case-Szenario in Ihrem Bewertungs-Dataset konzentrieren und nicht auf die durchschnittliche Leistung.
- Beim **Adversarial Testing** wird proaktiv versucht, Ihre Anwendung zu beschädigen. Ziel ist es, Schwachstellen zu identifizieren, damit Sie gegebenenfalls Maßnahmen ergreifen können, um sie zu beheben. Adversarial Testing kann viel Zeit und Aufwand von Bewertern mit Fachkenntnissen in Ihrer Anwendung erfordern. Je mehr Sie jedoch tun, desto größer ist die Wahrscheinlichkeit, dass Sie Probleme erkennen, insbesondere solche, die selten oder erst nach wiederholten Ausführungen der Anwendung auftreten.

  - Adversarial Testing ist ein Verfahren zur systematischen Bewertung eines ML-Modells, um zu ermitteln, wie es sich bei beabsichtigten oder unbeabsichtigten schädlichen Eingaben verhält:
    - Eine Eingabe kann bösartig sein, wenn sie eindeutig dazu dient, eine unsichere oder schädliche Ausgabe zu erzeugen, z. B. wenn ein Modell zur Textgenerierung aufgefordert wird, eine Hassrede über eine bestimmte Religion zu generieren.
    - Eine Eingabe ist unbeabsichtigt schädlich, wenn die Eingabe selbst zwar harmlos ist, aber eine schädliche Ausgabe erzeugt, z. B. wenn ein Modell zur Textgenerierung aufgefordert wird, eine Person mit einer bestimmten ethnischen Zugehörigkeit zu beschreiben, und eine rassistische Ausgabe zurückgegeben wird.
  - Ein Adversarial Test unterscheidet sich von einer Standardbewertung durch die Zusammensetzung der für den Test verwendeten Daten. Wählen Sie für Adversarial Tests
    Testdaten aus, die am wahrscheinlichsten problematische Ausgaben von
    dem Modell hervorrufen. Das bedeutet, dass Sie das Verhalten des Modells für alle Arten von Schäden untersuchen müssen, einschließlich seltener oder ungewöhnlicher Beispiele und Grenzfälle, die für Sicherheitsrichtlinien relevant sind. Außerdem sollte die Vielfalt in den verschiedenen Dimensionen eines Satzes berücksichtigt werden, z. B. in Bezug auf Struktur, Bedeutung und Länge. Weitere Informationen dazu, was Sie beim Erstellen eines Test-Datasets beachten sollten, finden Sie in den [Google's Responsible AI
    practices in
    fairness](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=de).

    #### Weitere Tipps

    - Verwenden Sie
      [automatisierte Tests](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=de)
      anstelle der traditionellen Methode, bei der Personen in „Red Teams“ eingesetzt werden,
      um zu versuchen, Ihre Anwendung zu beschädigen. Beim automatisierten Testen ist das
      „Red Team“ ein anderes Language Model, das Eingabetext findet, der
      schädliche Ausgaben des zu testenden Modells hervorruft.

## Auf Probleme überwachen

Egal wie viel Sie testen und minimieren, Sie können nie Perfektion garantieren. Planen Sie daher im Voraus, wie Sie auftretende Probleme erkennen und beheben. Zu den gängigen Ansätzen gehören das Einrichten eines überwachten Kanals, über den Nutzer Feedback geben können (z. B. eine Bewertung mit „Daumen hoch“/„Daumen runter“), und die Durchführung einer Nutzerstudie, um proaktiv Feedback von einer vielfältigen Gruppe von Nutzern einzuholen. Das ist besonders wertvoll, wenn die Nutzungsmuster von den Erwartungen abweichen.

#### Weitere Tipps

- Wenn Nutzer Feedback zu KI-Produkten geben, kann dies die Leistung der KI
  und die Nutzererfahrung im Laufe der Zeit erheblich verbessern, indem Sie beispielsweise
  bessere Beispiele für die Prompt-Optimierung auswählen können. Im
  [Kapitel Feedback und Kontrolle](https://pair.withgoogle.com/chapter/feedback-controls/)
  im [Leitfaden „People + AI Guidebook“ von Google](https://pair.withgoogle.com/guidebook/chapters)
  werden wichtige Überlegungen hervorgehoben, die bei der Entwicklung
  von Feedbackmechanismen berücksichtigt werden sollten.

## Nächste Schritte

- Weitere Informationen zu den
  [Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de), die über die Gemini API verfügbar sind, finden Sie im Leitfaden zu den anpassbaren
  Sicherheitseinstellungen.
- Eine Einführung in Prompts finden Sie unter [Erste Schritte mit Prompts](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=de) zu
  beginnen, Ihre ersten Prompts zu schreiben.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-04-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-04-29 (UTC)."],[],[]]
