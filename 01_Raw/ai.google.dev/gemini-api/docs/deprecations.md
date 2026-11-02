---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=de
fetched_at: 2026-11-02T07:03:56.447952+00:00
title: "Einstellung von Gemini-Produkten \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Einstellung von Gemini-Produkten

Auf dieser Seite sind die bekannten Einstellungszeitpläne für [stabile (GA-)](https://ai.google.dev/gemini-api/docs/models?hl=de#stable) und [Vorschau](https://ai.google.dev/gemini-api/docs/models?hl=de#preview)-Modelle sowie für verwaltete KI-Agenten in der Gemini API aufgeführt. Eine **Einstellung** ist die Ankündigung, dass wir ein Modell nicht mehr unterstützen und es in naher Zukunft **deaktiviert** wird. Wenn ein Modell **deaktiviert** wurde, ist es vollständig abgeschaltet und der Endpunkt ist nicht mehr verfügbar.

Ankündigungen zur Einstellung werden auf der Seite [Versionshinweise](https://ai.google.dev/gemini-api/docs/changelog?hl=de) veröffentlicht. Die angekündigten frühesten Termine für die Einstellung werden auf dieser Seite aufgeführt.
Bereits heruntergefahrene Modelle werden mit grauem Hintergrund angezeigt.

## Gemini 3-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-3.8-flash-tts` | 22. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.8-flash-lite-tts` | 22. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.8-live` | 15. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.8-live-extended-thinking` | 15. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.8-flash` | 2. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.7-flash` | 13. August 2026 | – | `gemini-3.8-flash` (kann in Google AI Studio nicht ausgewählt werden; der Endpunkt wird nicht eingestellt und leitet API-Anfragen automatisch an `gemini-3.8-flash` weiter) |
| `gemini-3.6-flash` | 21. Juli 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.5-flash-lite` | 21. Juli 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.5-flash` | 19. Mai 2026 | – | `gemini-3.6-flash` (kann in Google AI Studio nicht ausgewählt werden; der Endpunkt wird nicht eingestellt und leitet API-Anfragen automatisch an `gemini-3.6-flash` weiter) |
| `gemini-3.1-flash-lite` | 7. Mai 2026 | 7. Mai 2027 | `gemini-3.5-flash-lite` |
| Modelle in Vorabversion | | | |
| `gemini-3.1-flash-tts-preview` | 26. Februar 2026 | 17. November 2026 | `gemini-3.8-flash-tts` oder `gemini-3.8-flash-lite-tts` |
| `gemini-3.1-pro-preview` | 19. Februar 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3-flash-preview` | 17. Dezember 2025 | Kein Datum für die Einstellung angekündigt | `gemini-3.6-flash` |
| `gemini-3-pro-preview` | 18. November 2025 | 9. März 2026 | `gemini-3.1-pro-preview` |
| `gemini-3.1-flash-lite-preview` | 3. März 2026 | 25. Mai 2026 | `gemini-3.1-flash-lite` |

## Gemini 2.5 Pro-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | 17. Juni 2025 | Kein Datum für die Einstellung angekündigt |  |
| Modelle in Vorabversion | | | |
| `gemini-2.5-computer-use-preview-10-2025` | 7. Oktober 2025 | 28. Juli 2026 | `gemini-3.8-flash` |
| `gemini-2.5-pro-preview-03-25` | 3. März 2025 | 2. Dezember 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | 6. Mai 2025 | 2. Dezember 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | 5. Juni 2025 | 2. Dezember 2025 | `gemini-3.1-pro-preview` |

## Gemini 2.5 Flash-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | 17. Juni 2025 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-2.5-flash-lite` | 22. Juli 2025 | Kein Datum für die Einstellung angekündigt |  |
| Modelle in Vorabversion | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | 25. September 2025 | 31. März 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | 20. Mai 2025 | 18. November 2025 | `gemini-3.6-flash` |
| `gemini-2.5-flash-preview-09-25` | 25. September 2025 | 17. Februar 2026 | `gemini-3.6-flash` |

## Gemini 2.0-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | 5. Februar 2025 | 1. Juni 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-001` | 5. Februar 2025 | 1. Juni 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` | 25. Februar 2025 | 1. Juni 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-001` | 25. Februar 2025 | 1. Juni 2026 | `gemini-3.1-flash-lite` |
| Modelle in Vorabversion | | | |
| `gemini-2.0-flash-lite-preview` | 5. Februar 2025 | 9. Dezember 2025 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | 5. Februar 2025 | 9. Dezember 2025 | `gemini-3.1-flash-lite` |

## Live API-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-3.8-live` | 15. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.8-live-extended-thinking` | 15. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.5-transcribe-live` | August 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-2.0-flash-live-001` | 9. April 2025 | 9. Dezember 2025 | `gemini-3.8-live` |
| Modelle in Vorabversion | | | |
| `gemini-3.5-live-translate-preview` | Juni 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.1-flash-live-preview` | 11. März 2026 | 17. November 2026 | `gemini-3.8-live` |
| `gemini-2.5-flash-native-audio-preview-12-2025` | 12. Dezember 2025 | 17. November 2026 | `gemini-3.8-live` |
| `gemini-live-2.5-flash-preview` | 17. Juni 2025 | 9. Dezember 2025 | `gemini-3.8-live` |

## Audiomodelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-3.5-transcribe` | August 2026 | Kein Datum für die Einstellung angekündigt |  |
| Modelle in Vorabversion | | | |
| `gemini-2.5-flash-preview-tts` | 20. Mai 2025 | 17. November 2026 | `gemini-3.8-flash-tts` oder `gemini-3.8-flash-lite-tts` |
| `gemini-2.5-pro-preview-tts` | 20. Mai 2025 | 17. November 2026 | `gemini-3.8-flash-tts` oder `gemini-3.8-flash-lite-tts` |

## Einbettungsmodelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-embedding-2` | 22. April 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-embedding-001` | 14. Juli 2025 | 14. Mai 2028 | `gemini-embedding-2` |
| `text-embedding-004` | 9. April 2024 | 14. Januar 2026 | `gemini-embedding-2` |
| Modelle in Vorabversion | | | |
| `embedding-2-preview` | 10. März 2026 | 10. August 2026 | `gemini-embedding-2` |
| `embedding-001` | 9. April 2024 | 30. Oktober 2025 | `gemini-embedding-2` |
| `embedding-gecko-001` |  | 30. Oktober 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp` |  | 30. Oktober 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp-03-07` |  | 30. Oktober 2025 | `gemini-embedding-2` |

## Nano Banana-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-nano-banana-2.1` | 6. Oktober 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.1-flash-lite-image` | 30. Juni 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-3.1-flash-image` | 28. Mai 2026 | Kein Datum für die Einstellung angekündigt | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image` | 28. Mai 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-2.5-flash-image` | 2. Oktober 2025 | 15. März 2027 | `gemini-3.1-flash-lite-image` |
| Modelle in Vorabversion | | | |
| `gemini-3.1-flash-image-preview` | 26. Februar 2026 | 25. Juni 2026 | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image-preview` | 20. November 2025 | 25. Juni 2026 | `gemini-3-pro-image` |
| `gemini-2.5-flash-image-preview` | 7. Mai 2025 | 15. Januar 2026 | `gemini-nano-banana-2.1` |
| `gemini-2.0-flash-preview-image-generation` | 7. Mai 2025 | 14. November 2025 | `gemini-nano-banana-2.1` |

## Imagen-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | 24. Juni 2025 | 17. August 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-001` | 24. Juni 2025 | 17. August 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-fast-generate-001` | 24. Juni 2025 | 17. August 2026 | `gemini-nano-banana-2.1` |
| `imagen-3.0-generate-002` | 6. Februar 2025 | 10. November 2025 | `gemini-nano-banana-2.1` |
| Vorschaumodelle | | | |
| `imagen-4.0-generate-preview-06-06` | 24. Juni 2025 | 17. Februar 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-preview-06-06` | 24. Juni 2025 | 17. Februar 2026 | `gemini-nano-banana-2.1` |

## Veo-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | 9. September 2025 | 30. Juni 2026 | `gemini-omni-1.1-flash` oder die GA-Modelle auf der [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=de) |
| `veo-3.0-fast-generate-001` | 9. September 2025 | 30. Juni 2026 | `gemini-omni-1.1-flash` oder die GA-Modelle auf der [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=de) |
| `veo-2.0-generate-001` | 9. April 2025 | 30. Juni 2026 | `gemini-omni-1.1-flash` oder die GA-Modelle auf der [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=de) |
| Modelle in Vorabversion | | | |
| `veo-3.1-lite-generate-preview` | 31. März 2026 | 22. Oktober 2026 | `gemini-omni-1.1-flash` |
| `veo-3.1-generate-preview` | 15. Oktober 2025 | 22. Oktober 2026 | `gemini-omni-1.1-flash` |
| `veo-3.1-fast-generate-preview` | 15. Oktober 2025 | 22. Oktober 2026 | `gemini-omni-1.1-flash` |
| `veo-3.0-generate-preview` | 31. Juli 2025 | 12. November 2025 | `gemini-omni-1.1-flash` |
| `veo-3.0-fast-generate-preview` | 31. Juli 2025 | 12. November 2025 | `gemini-omni-1.1-flash` |

## Gemini Omni Flash-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `gemini-omni-1.1-flash` | 27. August 2026 | Kein Datum für die Einstellung angekündigt |  |
| Modelle in Vorabversion | | | |
| `gemini-omni-flash-preview` | 30. Juni 2026 | 22. Oktober 2026 | `gemini-omni-1.1-flash` |

## Lyria-Modelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| `lyria-3.5` | 3. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| Modelle in Vorabversion | | | |
| `lyria-3-clip-preview` | 25. März 2026 | Kein Datum für die Einstellung angekündigt |  |
| `lyria-3-pro-preview` | 25. März 2026 | Kein Datum für die Einstellung angekündigt | `lyria-3.5` |
| `lyria-realtime-exp` | 20. Mai 2025 | Kein Datum für die Einstellung angekündigt |  |

## Robotikmodelle

| **Modell** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| Modelle in Vorabversion | | | |
| `gemini-robotics-er-2-preview` | 30. Juli 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-robotics-er-2-streaming-preview` | 30. Juli 2026 | Kein Datum für die Einstellung angekündigt |  |
| `gemini-robotics-er-1.6-preview` | 14. April 2026 | 31. August 2026 | `gemini-robotics-er-2-preview` |
| `gemini-robotics-er-1.5-preview` | 25. September 2025 | 30. April 2026 | `gemini-robotics-er-2-preview` |

## Verwaltete KI-Agenten

| **Agentenmodus** | **Veröffentlicht** | **Einstellungsdatum** | **Empfohlener Ersatz** |
| --- | --- | --- | --- |
| Vorschau auf KI-Agenten | | | |
| `antigravity-preview-09-2026` | 17. September 2026 | Kein Datum für die Einstellung angekündigt |  |
| `deep-research-preview-04-2026` | 21. April 2026 | Kein Datum für die Einstellung angekündigt |  |
| `deep-research-max-preview-04-2026` | 21. April 2026 | Kein Datum für die Einstellung angekündigt |  |
| `deep-research-pro-preview-12-2025` | 11. Dezember 2025 | 23. Oktober 2026 | `deep-research-preview-04-2026` |
| `antigravity-preview-05-2026` | 19. Mai 2026 | 5. Oktober 2026 | `antigravity-preview-09-2026` |

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-22 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-22 (UTC)."],[],[]]
