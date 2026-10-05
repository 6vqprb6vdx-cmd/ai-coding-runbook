---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=de
fetched_at: 2026-10-05T06:39:01.858584+00:00
title: "Android-Apps in Google\u00a0AI Studio entwickeln \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Android-Apps in Google AI Studio entwickeln

Mit Google AI Studio können Sie native Android-Apps aus einem Prompt in natürlicher Sprache erstellen. Beschreiben Sie die gewünschte App und der [Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=de#antigravity-agent) generiert ein vollständiges Kotlin- und [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=de)-Projekt. Im Browser können Sie sich eine Vorschau Ihrer App in einem browserbasierten Android-Emulator ansehen, sie auf einem physischen Gerät installieren und sie zum Testen veröffentlichen.

## Jetzt starten

So erstellen Sie eine Android-App:

1. Rufen Sie über den linken Navigationsbereich den [Build-Modus](https://aistudio.google.com/apps?hl=de) in Google AI Studio auf.
2. Wählen Sie in der Plattformauswahl **Android** aus.
3. Geben Sie einen Prompt ein, der die App beschreibt, die Sie erstellen möchten, z. B. *„Erstelle einen Aufgaben-Tracker für tägliche Aufgaben mit lokaler Speicherung“* oder *„Erstelle einen einfachen Taschenrechner“*.
4. Der Agent generiert das Projekt und startet es im browserbasierten Android-Emulator.

Anschließend können Sie Ihre App über den Chatbereich iterieren, genau wie in der Webversion. Der Agent verwaltet alle Dateien in Ihrem Android-Projekt und überträgt Änderungen in der gesamten Codebasis.

## Browserbasierter Android-Emulator

Der Android-Emulator wird vollständig in der Cloud ausgeführt und in Ihren Browser gestreamt.
Sie müssen das Android SDK, Android Studio oder einen lokalen Emulator nicht installieren.

Der Emulator bietet:

- **Pixel-ähnliche Gerätesimulation**: Tippen, scrollen und interagieren Sie mit Ihrer App wie auf einem echten Gerät.
- **Unterstützung für Drehung**: Sie können zwischen Hoch- und Querformat wechseln.
- **Live-Vorschau**: Wenn der Agent Codeänderungen vornimmt, wird die App neu erstellt und der Emulator automatisch aktualisiert.

### Einschränkungen bei Emulatoren

Der browserbasierte Emulator unterstützt nicht alle Hardwarefunktionen. Folgendes ist im Emulator nicht verfügbar:

- Kamera- und Fotoaufnahmen
- NFC und Bluetooth
- GPS (Standort wird simuliert)
- Google Play-Dienste (Google Log‑in, Maps und andere Play-Dienste-Funktionen funktionieren auf einem echten Gerät, aber nicht im Emulator)

## Installation auf einem Gerät mit ADB

Sie können die erstellte APK direkt auf einem physischen Android-Gerät installieren, das über USB mit Ihrem Computer verbunden ist. Dabei wird [WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=de) verwendet, um über den Browser mit Ihrem Gerät zu kommunizieren. Es ist keine lokale ADB-Installation erforderlich.

### Vorbereitung

- Einen Chrome- oder Edge-Browser, der WebUSB unterstützt.
- Ein Android-Gerät, auf dem [Entwickleroptionen und USB-Debugging](https://developer.android.com/studio/debug/dev-options?hl=de) aktiviert sind.
- Ein USB-Kabel, mit dem Sie Ihr Gerät mit Ihrem Computer verbinden.

### App auf dem Gerät installieren

1. Klicken Sie im Vorschaufenster auf **Auf Gerät installieren**.
2. Wählen Sie Ihr Android-Gerät in der USB-Geräteauswahl des Browsers aus.
3. Die APK wird übertragen und auf Ihrem Gerät installiert.
4. Die App wird automatisch gestartet.

## Im Google Play Store veröffentlichen

Sie können Ihre Android-App im [Google Play Console](https://play.google.com/console?hl=de)-Track für interne Tests veröffentlichen und so an bis zu 100 Tester verteilen.

### Vorbereitung

- Ein [Google Play-Entwicklerkonto](https://play.google.com/console/signup?hl=de) (dafür ist eine einmalige Registrierungsgebühr von 25 $ erforderlich).
- Ein vollständiges Entwicklerprofil in der Play Console.

### App veröffentlichen

1. Öffnen Sie in Google AI Studio **Einstellungen > Veröffentlichen**.
2. Klicken Sie auf **Im Google Play Store veröffentlichen**.
3. Authentifizieren Sie sich mit Ihrem Google Play-Entwicklerkonto.
4. AI Studio signiert das APK, erstellt den App-Eintrag (oder lädt eine neue Version hoch) und veröffentlicht die App im internen Test-Track.
5. Sie erhalten einen Link, den Sie mit Ihren Testern teilen können.

In AI Studio wird die APK-Signierung automatisch über einen verwalteten Keystore verwaltet. Sie können den App-Eintrag (Symbol, Screenshots, Beschreibung) später in der Play Console anpassen.

## Was wird generiert?

Wenn Sie eine Android-App erstellen, generiert der Agent ein standardmäßiges Gradle-basiertes Projekt mit der folgenden Struktur:

- **Build-Konfiguration**: `build.gradle.kts`-Dateien (Projekt- und App-Ebene) mit Kotlin DSL.
- **UI-Ebene**: [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=de)-Komponenten mit [Material 3](https://m3.material.io/)-Theming.
- **Architektur**: Architektur mit einer einzelnen Aktivität mit ViewModels und Datenklassen.
- **Ressourcen**: `AndroidManifest.xml`, Drawables, Strings und andere Android-Ressourcen.

Der Agent verwaltet Gradle-Abhängigkeiten automatisch und fügt bei Bedarf Pakete aus Maven- und Google-Repositories hinzu.

Sie können den generierten Code auf dem Tab **Code** im Vorschaufenster ansehen und bearbeiten. Wenn Sie die Entwicklung in Android Studio fortsetzen möchten, laden Sie das Projekt als **ZIP-Datei** herunter.

## Beschränkungen

Für das Erstellen von Android-Apps in AI Studio gelten die folgenden Einschränkungen:

### Plattformeinschränkungen

- **Nur clientseitig**: Android-Apps enthalten keine serverseitige Komponente.
  Funktionen, für die eine Serverlaufzeit erforderlich ist (Secrets-Verwaltung, Multiplayer, Firebase, Google Workspace APIs), sind nicht verfügbar.
- **Architektur mit nur einer Aktivität**: Es werden nur Projekte mit einer Aktivität und einem Modul unterstützt.
- **Nur Jetpack Compose**: Apps verwenden Kotlin und Jetpack Compose. Java- und XML-Layouts werden nicht unterstützt.
- **Kein NDK oder nativer Code**: C- und C++-Code wird nicht unterstützt.
- **Kein Wear OS oder Android TV**: Es werden nur Smartphone- und Tablet-Formfaktoren unterstützt.

### Exportbeschränkungen

- **Nur ZIP-Download**: Sie können das Projekt als ZIP-Datei herunterladen. Der GitHub-Export ist für Android-Projekte noch nicht verfügbar.

## Nächste Schritte

- [Apps in Google AI Studio entwickeln](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=de)
- [Full-Stack-Apps entwickeln](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=de) (Web)
- Beispiele finden Sie in der [App-Galerie](https://aistudio.google.com/apps?source=showcase&hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-08-19 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-08-19 (UTC)."],[],[]]
