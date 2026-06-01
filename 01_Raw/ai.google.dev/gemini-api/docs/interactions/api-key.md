---
source_url: https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=de
fetched_at: 2026-06-01T19:48:36.779003+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini API-Schlüssel verwenden

Für die Verwendung der Gemini API benötigen Sie einen API-Schlüssel. Auf dieser Seite wird beschrieben, wie Sie Ihre Schlüssel in Google AI Studio erstellen und verwalten und wie Sie Ihre Umgebung einrichten, um sie in Ihrem Code zu verwenden.

[Gemini API-Schlüssel erstellen oder ansehen](https://aistudio.google.com/app/apikey?hl=de)

## API-Schlüssel

Sie können alle Ihre Gemini API-Schlüssel auf der
[Google AI Studio](https://aistudio.google.com/app/apikey?hl=de) **API-Schlüssel**-Seite erstellen und verwalten.

Sobald Sie einen API-Schlüssel haben, haben Sie die folgenden Möglichkeiten, eine Verbindung zur Gemini API herzustellen:

- [API-Schlüssel als Umgebungsvariable festlegen](#set-api-env-var)
- [API-Schlüssel explizit angeben](#provide-api-key-explicitly)

Für erste Tests können Sie einen API-Schlüssel fest codieren. Dies sollte jedoch nur vorübergehend erfolgen, da es nicht sicher ist. Beispiele für die Festcodierung des API
Schlüssels finden Sie im Abschnitt [API-Schlüssel explizit angeben](#provide-api-key-explicitly).

## Google Cloud-Projekte

[Google Cloud-Projekte](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=de)
sind unerlässlich für die Verwendung von Google Cloud-Diensten (z. B. der Gemini API),
die Verwaltung der Abrechnung und die Steuerung von Mitbearbeitern und Berechtigungen. Google AI Studio bietet eine einfache Benutzeroberfläche für Ihre Google Cloud-Projekte.

Wenn Sie noch keine Projekte erstellt haben, müssen Sie entweder ein neues Projekt erstellen oder eines aus Google Cloud in Google AI Studio importieren. Auf der Seite **Projekte** in Google AI Studio werden alle Schlüssel angezeigt, die über die erforderliche Berechtigung zur Verwendung der Gemini API verfügen. Eine Anleitung finden Sie im Abschnitt [Projekte importieren](#import-projects).

### Standardprojekt

Für neue Nutzer erstellt Google AI Studio nach dem Akzeptieren der Nutzungsbedingungen ein Standard-Google Cloud-Projekt und einen API-Schlüssel, um die Verwendung zu erleichtern. Sie können dieses
Projekt in Google AI Studio umbenennen. Rufen Sie dazu im
**Dashboard** die Ansicht **Projekte** auf, klicken Sie neben einem Projekt auf die Schaltfläche mit den drei Punkten und
wählen Sie **Projekt umbenennen** aus. Für bestehende Nutzer oder Nutzer, die bereits Google Cloud-Konten haben, wird kein Standardprojekt erstellt.

## Projekte importieren

Jeder Gemini API-Schlüssel ist mit einem Google Cloud-Projekt verknüpft. Standardmäßig werden in Google AI Studio nicht alle Ihre Cloud-Projekte angezeigt. Sie müssen die gewünschten Projekte importieren, indem Sie im Dialogfeld **Projekte importieren** nach dem Namen oder der Projekt-ID suchen. Eine vollständige Liste der Projekte, auf die Sie Zugriff haben, finden Sie in der Cloud Console.

Wenn Sie noch keine Projekte importiert haben, führen Sie die folgenden Schritte aus, um ein Google Cloud-Projekt zu importieren und einen Schlüssel zu erstellen:

1. Rufen Sie [Google AI Studio](https://aistudio.google.com?hl=de) auf.
2. Öffnen Sie das **Dashboard** über die linke Seitenleiste.
3. Wählen Sie **Projekte** aus.
4. Wählen Sie auf der Seite **Projekte** die Schaltfläche **Projekte importieren** aus.
5. Suchen Sie nach dem Google Cloud-Projekt, das Sie importieren möchten, wählen Sie es aus und klicken Sie auf die Schaltfläche **Importieren**.

Nachdem ein Projekt importiert wurde, rufen Sie im Menü **Dashboard** die Seite **API-Schlüssel** auf und erstellen Sie einen API-Schlüssel in dem gerade importierten Projekt.

## Beschränkungen

Die folgenden Beschränkungen gelten für die Verwaltung von API-Schlüsseln und Google Cloud-Projekten in Google AI Studio.

- Sie können maximal 10 Projekte gleichzeitig auf der Google AI Studio-Seite **Projekte** erstellen.
- Sie können Projekte und Schlüssel benennen und umbenennen.
- Auf den Seiten **API-Schlüssel** und **Projekte** werden maximal 100 Schlüssel und 50 Projekte angezeigt.
- Es werden nur API-Schlüssel angezeigt, die keine Einschränkungen haben oder auf die Generative Language API beschränkt sind.

Für zusätzlichen Verwaltungszugriff auf Ihre Projekte, einschließlich des Änderns und
Einschränkens von API-Schlüsseln, rufen Sie die
[Seite Anmeldedaten in der Google Cloud Console auf](https://console.cloud.google.com/apis/credentials?hl=de).
In der Cloud Console können Sie Ihr Projekt auswählen, auf einen vorhandenen API-Schlüssel klicken und ihn dann auf die **Generative Language API** beschränken.

## API-Schlüssel als Umgebungsvariable festlegen

Wenn Sie die Umgebungsvariable `GEMINI_API_KEY` oder `GOOGLE_API_KEY` festlegen, wird der
API-Schlüssel automatisch vom Client übernommen, wenn Sie eine der
[Gemini API-Bibliotheken](https://ai.google.dev/gemini-api/docs/libraries?hl=de) verwenden. Es wird empfohlen, nur eine dieser Variablen festzulegen. Wenn beide festgelegt sind, hat `GOOGLE_API_KEY` Vorrang.

Wenn Sie die REST API oder JavaScript im Browser verwenden, müssen Sie den API-Schlüssel explizit angeben.

So legen Sie Ihren API-Schlüssel lokal als Umgebungsvariable `GEMINI_API_KEY` mit verschiedenen Betriebssystemen fest:

### Linux/macOS – Bash

Bash ist eine gängige Terminalkonfiguration für Linux und macOS. Sie können prüfen, ob Sie eine Konfigurationsdatei dafür haben, indem Sie den folgenden Befehl ausführen:

```
~/.bashrc
```

Wenn die Antwort „No such file or directory“ lautet, müssen Sie diese Datei erstellen und öffnen, indem Sie die folgenden Befehle ausführen oder `zsh` verwenden:

```
touch ~/.bashrc
open ~/.bashrc
```

Als Nächstes müssen Sie Ihren API-Schlüssel festlegen, indem Sie den folgenden Exportbefehl hinzufügen:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Nachdem Sie die Datei gespeichert haben, übernehmen Sie die Änderungen mit folgendem Befehl:

```
source ~/.bashrc
```

### macOS – Zsh

Zsh ist eine gängige Terminalkonfiguration für Linux und macOS. Sie können prüfen, ob Sie eine Konfigurationsdatei dafür haben, indem Sie den folgenden Befehl ausführen:

```
~/.zshrc
```

Wenn die Antwort „No such file or directory“ lautet, müssen Sie diese Datei erstellen und öffnen, indem Sie die folgenden Befehle ausführen oder `bash` verwenden:

```
touch ~/.zshrc
open ~/.zshrc
```

Als Nächstes müssen Sie Ihren API-Schlüssel festlegen, indem Sie den folgenden Exportbefehl hinzufügen:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Nachdem Sie die Datei gespeichert haben, übernehmen Sie die Änderungen mit folgendem Befehl:

```
source ~/.zshrc
```

### Windows

1. Suchen Sie in der Suchleiste nach „Umgebungsvariablen“.
2. Wählen Sie aus, die **Systemeinstellungen** zu ändern. Möglicherweise müssen Sie bestätigen, dass Sie dies tun möchten.
3. Klicken Sie im Dialogfeld „Systemeinstellungen“ auf die Schaltfläche **Umgebungsvariablen**.
4. Klicken Sie entweder unter **Benutzervariablen** (für den aktuellen Nutzer) oder **Systemvariablen** (gilt für alle Nutzer des Computers) auf **Neu...**.
5. Geben Sie `GEMINI_API_KEY` als Variablennamen an. Geben Sie Ihren Gemini API-Schlüssel als Variablenwert an.
6. Klicken Sie auf **OK** , um die Änderungen zu übernehmen.
7. Öffnen Sie eine neue Terminalsitzung (cmd oder PowerShell), um die neue Variable zu erhalten.

## API-Schlüssel explizit angeben

In einigen Fällen möchten Sie möglicherweise explizit einen API-Schlüssel angeben. Beispiel:

- Sie führen einen einfachen API-Aufruf aus und bevorzugen es, den API-Schlüssel fest zu codieren.
- Sie möchten explizite Kontrolle, ohne auf die automatische Erkennung von Umgebungsvariablen durch die Gemini API-Bibliotheken angewiesen zu sein.
- Sie verwenden eine Umgebung, in der Umgebungsvariablen nicht unterstützt werden (z. B. Web), oder Sie führen REST-Aufrufe aus.

Im Folgenden finden Sie Beispiele dafür, wie Sie einen API-Schlüssel explizit mit der Interactions API angeben können:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## API-Schlüssel schützen

Behandeln Sie Ihren Gemini API-Schlüssel wie ein Passwort. Wenn er kompromittiert wird, können andere das Kontingent Ihres Projekts verwenden, Gebühren verursachen (wenn die Abrechnung aktiviert ist) und auf Ihre privaten Daten wie Dateien zugreifen.

### Wichtige Sicherheitsregeln

- **Schlüssel vertraulich behandeln**: API-Schlüssel für Gemini können auf vertrauliche Daten zugreifen, von denen Ihre
  Anwendung abhängt.

  - **API-Schlüssel niemals in die Quellcodeverwaltung einchecken.** Checken Sie Ihren API-Schlüssel nicht in Versionsverwaltungssysteme wie Git ein.
  - **API-Schlüssel niemals clientseitig preisgeben.** Verwenden Sie Ihren API-Schlüssel nicht direkt in Web- oder mobilen Apps in der Produktion. Schlüssel in clientseitigem Code (einschließlich unserer JavaScript-/TypeScript-Bibliotheken und REST-Aufrufe) können extrahiert werden.
- **Zugriff einschränken**: Beschränken Sie die Verwendung von API-Schlüsseln nach Möglichkeit auf bestimmte IP-Adressen, HTTP
  Verweis-URLs oder Android-/iOS-Apps.
- **Verwendung einschränken**: Aktivieren Sie für jeden Schlüssel nur die erforderlichen APIs.
- **Regelmäßige Audits durchführen**: Prüfen Sie Ihre API-Schlüssel regelmäßig und rotieren Sie sie
  in regelmäßigen Abständen.

### Best Practices

- **Serverseitige Aufrufe mit API-Schlüsseln verwenden** : Die sicherste Möglichkeit, Ihren API-Schlüssel zu verwenden, besteht darin, die Gemini API von einer serverseitigen Anwendung aufzurufen, in der der Schlüssel vertraulich behandelt werden kann.
- **Kurzlebige Tokens für den clientseitigen Zugriff verwenden (nur Live API)** : Für den direkten clientseitigen Zugriff auf die Live API können Sie kurzlebige Tokens verwenden. Sie bergen geringere Sicherheitsrisiken und können für die Produktion geeignet sein. Weitere Informationen finden Sie im Leitfaden zu
  [kurzlebigen Tokens](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=de).
- **Einschränkungen für den Schlüssel hinzufügen**:Sie können die Berechtigungen eines Schlüssels einschränken
  indem Sie [API-Schlüsseleinschränkungen](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=de#add-api-restrictions) hinzufügen.
  So werden potenzielle Schäden minimiert, wenn der Schlüssel jemals offengelegt wird.

Einige allgemeine Best Practices finden Sie auch in diesem
[Hilfeartikel](https://support.google.com/googleapi/answer/6310037?hl=de).

## Fehlerbehebung bei der Erstellung von API-Schlüsseln

In Google AI Studio ist die Schaltfläche **API-Schlüssel erstellen** möglicherweise nicht verfügbar und es wird
die folgende Meldung angezeigt: "*Sie sind nicht berechtigt, in diesem Projekt einen Schlüssel zu erstellen*".

Dies tritt auf, wenn Sie nicht die erforderlichen Berechtigungen im Projekt haben, um einen neuen Schlüssel zu generieren:

- **`resourcemanager.projects.get`**: Ermöglicht AI Studio, die Existenz des Projekts zu überprüfen.
- **`apikeys.keys.create`**: Ermöglicht die Generierung des API-Schlüssels selbst.
- **`serviceusage.services.enable`**: Erforderlich, um sicherzustellen, dass die Gemini API im Projekt aktiv ist.
- **`iam.serviceAccounts.create`**: Für jeden neuen API-Schlüssel ist jetzt ein verknüpftes
  [Dienstkonto](https://docs.cloud.google.com/docs/authentication/api-keys?hl=de#api-keys-bound-sa)erforderlich,
  das bei der Erstellung des API-Schlüssels generiert wird.
- **`iam.serviceAccountApiKeyBindings.create`**: Erforderlich, um das neu erstellte Dienstkonto an den API-Schlüssel zu binden.

Um Ihre Berechtigungen zu korrigieren, bitten Sie Ihren Projektadministrator oder den Administrator Ihrer Organisation (wenn das Projekt zu einer [Organisation](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=de) gehört), Ihnen eine Rolle mit den oben aufgeführten Berechtigungen zu gewähren (z. B. Projektbearbeiter oder eine benutzerdefinierte Rolle).

Wenn Sie keinen Administratorzugriff auf ein Projekt haben, können Sie ein neues Projekt erstellen, das nicht mit einer Organisation verknüpft ist, um Ihre Schlüssel zu generieren.

Eine vollständige Liste der IAM-Berechtigungen, die für alle Google AI Studio-Funktionen erforderlich sind (z. B. Nutzung, Ratenbegrenzungen oder Abrechnung), finden Sie im [Leitfaden zur Fehlerbehebung in AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=de#iam-permissions).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-29 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-29 (UTC)."],[],[]]
