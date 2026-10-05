---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=de
fetched_at: 2026-10-05T06:28:48.577420+00:00
title: "\u00dcbersicht \u00fcber die Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Übersicht über die Gemini Live API

Die Live API ermöglicht Sprach- und Bildinteraktionen mit Gemini in Echtzeit und mit geringer Latenz. Die Funktion verarbeitet kontinuierliche Audio-, Bild- und Textstreams und liefert sofortige, menschenähnliche gesprochene Antworten, wodurch eine natürliche Konversation für Ihre Nutzer entsteht.

![Live API – Übersicht](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=de)

[Live API in Google AI Studio ausprobierenmic](https://aistudio.google.com/live?hl=de)
[Beispiel-Apps von GitHub klonencode](https://github.com/google-gemini/gemini-live-api-examples)
[Coding-Agent-Skills verwendenterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=de)

## Anwendungsfälle

Mit der Live API können Sie Echtzeit-Sprach-Agents für verschiedene Branchen erstellen, darunter:

- **E-Commerce und Einzelhandel**:Einkaufsassistenten, die personalisierte Empfehlungen geben, und Support-Agenten, die Kundenprobleme lösen.
- **Gaming**:Interaktive Non-Player Characters (NPCs), In-Game-Hilfeassistenten und Echtzeitübersetzung von In-Game-Inhalten.
- **Schnittstellen der nächsten Generation**:Sprach- und videobasierte Funktionen in Robotern, Smart Glasses und Fahrzeugen.
- **Gesundheitswesen**:Gesundheitsbegleiter zur Unterstützung und Aufklärung von Patienten.
- **Finanzdienstleistungen**:KI-basierte Berater für Vermögensverwaltung und Anlageberatung.
- **Bildung**:KI-Mentoren und Lernbegleiter, die personalisierte Anleitungen und Feedback geben.
- **Übersetzung und Lokalisierung**:Übersetzung gesprochener Unterhaltungen in Echtzeit mit geringer Latenz, um eine nahtlose mehrsprachige Kommunikation zu ermöglichen.
- **Automatische Transkription und Untertitelung**:Echtzeit-Streaming von Sprache zu Text für automatische Untertitel, Besprechungstranskription, Spracheingabe und Protokollierung von Kundenanrufen.

## Wichtige Features

Die Live API bietet eine umfassende Reihe von Funktionen zum Erstellen leistungsstarker Sprach-Agents:

- [**Unterstützung mehrerer Sprachen**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#supported-languages):
  Unterhalten Sie sich in 70 unterstützten Sprachen.
- [**Barge-in**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#interruptions): Nutzer können das Modell jederzeit unterbrechen, um responsive Interaktionen zu ermöglichen.
- [**Tool-Nutzung**](https://ai.google.dev/gemini-api/docs/live-tools?hl=de): Tools wie Funktionsaufrufe und die Google Suche werden für dynamische Interaktionen integriert.
- [**Audio-Transkriptionen**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#audio-transcription): Bietet Texttranskriptionen sowohl der Nutzereingabe als auch der Modellausgabe.
- [**Proaktive Audioausgabe**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#proactive-audio): Damit können Sie steuern, wann und in welchem Kontext das Modell antwortet.
- [**Affektiver Dialog**](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#affective-dialog): Der Antwortstil und der Tonfall werden an die Ausdrucksweise des Nutzers angepasst.
- [**Live-Transkription**](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=de):
  Kontinuierliches Speech-to-Text-Streaming in Echtzeit mit automatischer Spracherkennung und benutzerdefiniertem Vokabular.
- [**Live-Übersetzung**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=de):
  Echtzeit-Sprachübersetzung in über 70 Sprachen.

## Technische Spezifikationen

In der folgenden Tabelle sind die technischen Spezifikationen für die Live API aufgeführt:

| Kategorie | Details |
| --- | --- |
| Eingabemodalitäten | Audio (rohes 16-Bit-PCM-Audio, 16 kHz, Little Endian), Bilder (JPEG <= 1 FPS), Text |
| Ausgabemodalitäten | Audio (rohes 16‑Bit-PCM-Audio, 24 kHz, Little Endian) |
| Protokoll | Statusbehaftete WebSocket-Verbindung (WSS) |

## Implementierungsansatz auswählen

Bei der Integration mit der Live API müssen Sie einen der folgenden Implementierungsansätze auswählen:

- **Server-zu-Server**: Ihr Backend stellt über [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) eine Verbindung zur Live API her. Normalerweise sendet Ihr Client Streamdaten (Audio, Video, Text) an Ihren Server, der sie dann an die Live API weiterleitet.
- **Client-zu-Server**: Ihr Frontend-Code stellt über [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) eine direkte Verbindung zur Live API her, um Daten zu streamen. Ihr Backend wird dabei umgangen.

## Jetzt starten

Wählen Sie die Anleitung aus, die Ihrer Entwicklungsumgebung entspricht:

Server-zu-Server

### [GenAI SDK-Tutorial](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=de)

Verbinden Sie sich mit der Gemini Live API über das GenAI SDK, um eine multimodale Echtzeitanwendung mit einem Python-Backend zu erstellen.

Client-zu-Server

### [WebSocket-Tutorial](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=de)

Stellen Sie über WebSockets eine Verbindung zur Gemini Live API her, um eine multimodale Echtzeitanwendung mit einem JavaScript-Frontend und temporären Tokens zu erstellen.

Agent Development Kit

### [ADK-Tutorial](https://google.github.io/adk-docs/streaming/)

Erstellen Sie einen Agenten und verwenden Sie das ADK-Streaming (Agent Development Kit), um Sprach- und Videokommunikation zu ermöglichen.

## Einbindung in Partnerlösungen

Um die Entwicklung von Audio- und Video-Apps in Echtzeit zu vereinfachen, können Sie eine Drittanbieterintegration verwenden, die die Gemini Live API über WebRTC oder WebSockets unterstützt.

[LiveKit

Gemini Live API mit LiveKit-Agents verwenden](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

Erstellen Sie mit Gemini Live und Pipecat einen KI-Chatbot in Echtzeit.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam von Software Mansion

Mit Fishjam können Sie Anwendungen für Live-Video- und ‑Audiostreams erstellen.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Vision Agents nach Stream

Mit Vision Agents können Sie KI-Anwendungen für Sprach- und Videoinhalte in Echtzeit entwickeln.](https://visionagents.ai/integrations/gemini)
[Voximplant

Eingehende und ausgehende Anrufe mit Voximplant mit der Live API verbinden](https://voximplant.com/products/gemini-client)
[Agora

Mit Agora können Sie konversationelle KI-Anwendungen in Echtzeit entwickeln.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Erste Schritte mit der Gemini Live API und Firebase AI Logic](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-17 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-17 (UTC)."],[],[]]
