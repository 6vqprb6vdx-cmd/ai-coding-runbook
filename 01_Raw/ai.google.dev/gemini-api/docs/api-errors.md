---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=de
fetched_at: 2026-09-21T05:55:54.271701+00:00
title: "API-Fehler \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# API-Fehler

Auf dieser Seite finden Sie eine Referenz für alle Fehlercodes der Interactions API. Außerdem wird das Format der Fehlerantwort beschrieben und es wird erläutert, wie die API Fehler für verschiedene Anfragetypen zurückgibt.

## Standard-API-Fehlercodes

Diese allgemeinen Fehlercodes auf Anfrageebene entsprechen Standard-HTTP-Statuscodes.
Verwenden Sie das Feld `code` in Ihrer Anwendungslogik, um Fehler programmatisch zu beheben.

| Code | HTTP-Status | Beschreibung | Empfohlene Maßnahmen |
| --- | --- | --- | --- |
| `invalid_request` | 400 Fehlerhafte Anfrage | Die Anfrage-Nutzlast ist fehlerhaft oder enthält ungültige Parameter. | Vergleichen Sie die Syntax und die Parameter Ihrer Anfrage mit der [API-Referenz](https://ai.google.dev/api/interactions-api?hl=de). |
| `failed_precondition` | 400 Fehlerhafte Anfrage | Die Anfrage kann nicht verarbeitet werden, da eine Voraussetzung nicht erfüllt ist (z. B. deaktivierte Abrechnung). | Prüfen Sie den Abrechnungsstatus des Projekts oder die Kontovoraussetzungen. |
| `out_of_range` | 416 Requested Range Not Satisfiable (Angefragter Bereich ungültig oder nicht verfügbar) | Der Anfrageparameter liegt außerhalb des gültigen Bereichs. | Prüfen Sie die Parameterwerte und ‑limits. |
| `parameter_unknown` | 400 Fehlerhafte Anfrage | Die Anfrage enthält einen unbekannten Parameter. | Entfernen Sie den nicht erkannten Parameter und versuchen Sie es noch einmal. |
| `authentication` | 401 Nicht autorisiert | Der API-Schlüssel fehlt, ist ungültig oder abgelaufen. | [API-Schlüssel](https://ai.google.dev/gemini-api/docs/api-key?hl=de) prüfen |
| `payment_required` | 402 Payment Required (Zahlung erforderlich) | Ihr Vorauszahlungsguthaben ist aufgebraucht. | [Fügen Sie Ihrem Rechnungskonto Guthaben hinzu](https://ai.google.dev/gemini-api/docs/billing?hl=de#buy-credits) oder aktivieren Sie das [automatische Aufladen](https://ai.google.dev/gemini-api/docs/billing?hl=de#auto-reload). Nicht wiederholen: Die Anfrage kann erst bearbeitet werden, wenn Guthaben hinzugefügt wurde. |
| `permission_denied` | 403 Verboten | Ihr API-Schlüssel ist für diese Ressource nicht autorisiert. | Prüfen Sie die Berechtigungen für Ihren API-Schlüssel und den Projektzugriff. |
| `not_found` | 404 Nicht gefunden | Die angeforderte Ressource wurde nicht gefunden. | Prüfen Sie den Ressourcenpfad und die Parameter. |
| `model_not_found` | 404 Nicht gefunden | Das angegebene Modell wurde nicht gefunden. | Prüfen Sie den Modellnamen oder weichen Sie auf ein anderes Modell aus. |
| `already_exists` | 409-Fehler – Konflikt | Das Entität, die Sie erstellen möchten, existiert bereits. | Prüfen Sie, ob die Ressource bereits vorhanden ist, bevor Sie sie neu erstellen. |
| `aborted` | 409-Fehler – Konflikt | Der Vorgang wurde aufgrund eines Konflikts oder eines Fehlers bei der Parallelitätsprüfung abgebrochen. | Wiederholen Sie die Anfrage auf einer höheren Anwendungsebene. |
| `rate_limit_exceeded` | 429 Zu viele Anfragen | Sie haben das Limit für Anfragen oder Tokens pro Minute oder Sekunde überschritten. | Warten Sie und wiederholen Sie den Vorgang mit exponentiellem Backoff. |
| `quota_exceeded` | 429 Zu viele Anfragen | Sie haben Ihr Tageskontingent überschritten. | Warten Sie, bis das Kontingent zurückgesetzt wird, oder fordern Sie eine Kontingenterhöhung an. |
| `too_many_requests` | 429 Zu viele Anfragen | Sie haben innerhalb kurzer Zeit zu viele Anfragen gestellt. | Warten Sie und wiederholen Sie den Vorgang mit exponentiellem Backoff. |
| `cancelled` | 499 Client Closed Request | Der Client hat die Anfrage abgebrochen, bevor sie abgeschlossen wurde. | Es sind keine Maßnahmen erforderlich. Das bedeutet in der Regel, dass die Verbindung zum Client getrennt wurde. |
| `api_error` | 500 Interner Serverfehler | Auf dem Server ist ein unerwarteter Fehler aufgetreten. | Wiederholen Sie die Anfrage. Sollte das Problem weiterhin auftreten, wenden Sie sich bitte an den Support. |
| `unimplemented` | 501 Not Implemented (Nicht implementiert) | Der Vorgang oder die Funktion ist nicht implementiert oder wird nicht unterstützt. | Prüfen Sie die API-Funktionen oder wechseln Sie zu einem unterstützten Feature. |
| `service_unavailable` | 503 Dienst nicht verfügbar | Der Dienst ist vorübergehend überlastet oder nicht erreichbar. | Warten Sie und wiederholen Sie den Vorgang mit exponentiellem Backoff. |
| `deadline_exceeded` | 504 Gateway-Zeitüberschreitung | Die Anfrage wurde nicht innerhalb der Frist bearbeitet. | Entfernen oder erhöhen Sie die Client-Fristeinstellung, um die Serverstandardeinstellung zu verwenden. |

## Codes für die Generierung blockiert

Diese Fehlercodes weisen darauf hin, dass die Ausgabe des Modells aufgrund von Richtlinien-, Sicherheits- oder Inhaltsbeschränkungen blockiert wurde. Wenn Sie einen dieser Codes erhalten, ändern Sie Ihre Eingabe und versuchen Sie es noch einmal.

| Code | Beschreibung |
| --- | --- |
| `safety` | Die Anfrage wurde aufgrund von Sicherheitsverstößen (schädliche Inhalte) blockiert. |
| `recitation` | Der Antrag wurde aufgrund von Urheberrechts- oder Vortragseinschränkungen blockiert. |
| `language` | Die Anfrage wurde aufgrund einer nicht unterstützten Sprache blockiert. |
| `prohibited_content` | Die Anfrage wurde aufgrund der Richtlinien für unzulässige Inhalte blockiert. |
| `spii` | Die Anfrage wurde aufgrund von Einschränkungen für vertrauliche personenidentifizierbare Informationen blockiert. |
| `blocklist` | Die Anfrage wurde blockiert, weil sie Begriffe enthielt, die auf einer Sperrliste stehen. |
| `image_safety` | Die Bildgenerierung wurde aufgrund von Sicherheitsverstößen blockiert. |
| `image_prohibited_content` | Die Bildgenerierung wurde aufgrund der Richtlinien für unzulässige Inhalte blockiert. |
| `image_recitation` | Die Bildgenerierung wurde aufgrund von Urheberrechts- oder Rezitationsbeschränkungen blockiert. |
| `image_other` | Die Bildgenerierung wurde aus nicht näher genannten Gründen blockiert. |
| `content_blocked` | Die Anfrage wurde aus einem nicht näher angegebenen Richtliniengrund blockiert. |

## Fehlercodes für die Generierung

Diese Fehlercodes weisen auf ein strukturelles Problem mit der generierten Ausgabe des Modells hin, z. B. ein fehlerhafter Funktionsaufruf oder ein nicht deklarierter Tool-Aufruf.

| Code | Beschreibung |
| --- | --- |
| `malformed_function_call` | Das Modell hat einen Funktionsaufruf generiert, der nicht geparst werden konnte. |
| `malformed_tool_call` | Das Modell hat einen Tool-Aufruf generiert, der nicht geparst werden konnte. |
| `unexpected_tool_call` | Das Modell hat ein Tool aufgerufen, das in der Anfrage nicht deklariert wurde. |
| `no_image` | Das Modell konnte kein Bild generieren. |
| `too_many_tool_calls` | Das Modell hat mehr Tool-Aufrufe generiert als zulässig. |
| `missing_thought_signature` | In der Antwort fehlt eine erforderliche Gedanken-Signatur. |

## Format der Fehlerantwort

Alle Fehler der Interactions API geben ein `error`-Objekt mit einem `code` und einem `message` zurück. Wenn Sie beispielsweise einen nicht unterstützten Tooltyp übergeben, wird Folgendes zurückgegeben:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| `code` | String | Ein maschinenlesbarer Fehlercode in `snake_case`. |
| `message` | String | Eine für Menschen lesbare Beschreibung des Problems. |

## So werden Fehler übermittelt

Die API gibt Fehler unterschiedlich zurück, je nachdem, ob Sie eine Standard-HTTP-Anfrage oder eine Streaming-Anfrage (SSE) stellen.

### Standard-HTTP-Anfragen

Bei Standardanfragen (nicht Streaming) legt die API den HTTP-Antwortstatuscode fest (z. B. `400 Bad Request`, `401 Unauthorized` oder `429 Too Many Requests`) und gibt ein `error`-Objekt im JSON-Antworttext zurück:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Streaming-Anfragen (SSE)

Bei Streaminganfragen (`stream: true`) sendet die API Fehlerereignisse über den SSE-Stream (Server-Sent Events), wobei `event_type` auf `"error"` gesetzt ist. Das Feld `error` enthält dieselbe `code`- und `message`-Struktur:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Das vollständige SSE-Ereignisschema finden Sie in der [Interactions API-Referenz](https://ai.google.dev/api/interactions-api?hl=de).

## Nächste Schritte

- [API-Fehlerbehebung](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=de): Häufige Probleme und Fehlerszenarien beheben.
- [Ratenlimits](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de): Informationen zu Anfragelimits und zur Kontingentverwaltung.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-20 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-20 (UTC)."],[],[]]
