---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=sq
fetched_at: 2026-10-19T05:34:49.812195+00:00
title: "Heqjet nga funksionimi t\u00eb Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Heqjet nga funksionimi të Gemini

Kjo faqe liston programet e njohura të zhvlerësimit për modelet [të qëndrueshme (GA)](https://ai.google.dev/gemini-api/docs/models?hl=sq#stable) dhe [versionet paraprake](https://ai.google.dev/gemini-api/docs/models?hl=sq#preview), si dhe për agjentët e menaxhuar në Gemini API. "**Heqja nga funksionimi**" është njoftimi që ne nuk ofrojmë më mbështetje për një model dhe që ai do të "**mbyllet**" në të ardhmen e afërt. Pasi një model "**mbyllet**", ai është
çaktivizuar plotësisht dhe pika fundore nuk ofrohet më.

Njoftimet për vjetrimin bëhen në faqen e
[Shënimeve të publikimit](https://ai.google.dev/gemini-api/docs/changelog?hl=sq) dhe datat më të hershme të njoftuara
për mbylljen monitorohen në këtë faqe.
Modelet që janë mbyllur tashmë tregohen me sfonde gri.

## Modelet e Gemini 3

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-3.8-flash-tts` | 22 shtator 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3.8-flash-lite-tts` | 22 shtator 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| `gemini-3.8-live` | 15 shtator 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3.8-live-extended-thinking` | 15 shtator 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3.8-flash` | 2 shtator 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3.7-flash` | 13 gusht 2026 | Nuk ka | `gemini-3.8-flash` (nuk ofrohet për t'u zgjedhur në Google AI Studio; pika fundore nuk po mbyllet dhe i ridrejton automatikisht kërkesat e API-së te `gemini-3.8-flash`) |
| `gemini-3.6-flash` | 21 korrik 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| `gemini-3.5-flash-lite` | 21 korrik 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| `gemini-3.5-flash` | 19 maj 2026 | Nuk ka | `gemini-3.6-flash` (nuk ofrohet për t'u zgjedhur në Google AI Studio; pika fundore nuk po mbyllet dhe i ridrejton automatikisht kërkesat e API-së te `gemini-3.6-flash`) |
| `gemini-3.1-flash-lite` | 7 maj 2026 | 7 maj 2027 | `gemini-3.5-flash-lite` |
| Shiko paraprakisht modelet | | | |
| `gemini-3.1-flash-tts-preview` | 26 shkurt 2026 | 17 nëntor 2026 | `gemini-3.8-flash-tts` ose `gemini-3.8-flash-lite-tts` |
| `gemini-3.1-pro-preview` | 19 shkurt 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3-flash-preview` | 17 dhjetor 2025 | Nuk është njoftuar asnjë datë mbylljeje | `gemini-3.6-flash` |
| `gemini-3-pro-preview` | 18 nëntor 2025 | 9 mars 2026 | `gemini-3.1-pro-preview` |
| `gemini-3.1-flash-lite-preview` | 3 mars 2026 | 25 maj 2026 | `gemini-3.1-flash-lite` |

## Modelet e Gemini 2.5 Pro

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | 17 qershor 2025 | Nuk është njoftuar asnjë datë mbylljeje |  |
| Shiko paraprakisht modelet | | | |
| `gemini-2.5-computer-use-preview-10-2025` | 7 tetor 2025 | 28 korrik 2026 | `gemini-3.8-flash` |
| `gemini-2.5-pro-preview-03-25` | 3 mars 2025 | 2 dhjetor 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | 6 maj 2025 | 2 dhjetor 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | 5 qershor 2025 | 2 dhjetor 2025 | `gemini-3.1-pro-preview` |

## Modelet e Gemini 2.5 Flash

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | 17 qershor 2025 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-2.5-flash-lite` | 22 korrik 2025 | Nuk është njoftuar asnjë datë mbylljeje |  |
| Shiko paraprakisht modelet | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | 25 shtator 2025 | 31 mars 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | 20 maj 2025 | 18 nëntor 2025 | `gemini-3.6-flash` |
| `gemini-2.5-flash-preview-09-25` | 25 shtator 2025 | 17 shkurt 2026 | `gemini-3.6-flash` |

## Modelet e Gemini 2.0

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | 5 shkurt 2025 | 1 qershor 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-001` | 5 shkurt 2025 | 1 qershor 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` | 25 shkurt 2025 | 1 qershor 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-001` | 25 shkurt 2025 | 1 qershor 2026 | `gemini-3.1-flash-lite` |
| Shiko paraprakisht modelet | | | |
| `gemini-2.0-flash-lite-preview` | 5 shkurt 2025 | 9 dhjetor 2025 | `gemini-2.5-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | 5 shkurt 2025 | 9 dhjetor 2025 | `gemini-2.5-flash-lite` |

## Modelet e API-së së transmetimit të drejtpërdrejtë

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-3.8-live` | 15 shtator 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3.8-live-extended-thinking` | 15 shtator 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| `gemini-3.5-transcribe-live` | Gusht 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| `gemini-2.0-flash-live-001` | 9 prill 2025 | 9 dhjetor 2025 | `gemini-3.8-live` |
| Shiko paraprakisht modelet | | | |
| `gemini-3.5-live-translate-preview` | Qershor 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3.1-flash-live-preview` | 11 mars 2026 | 17 nëntor 2026 | `gemini-3.8-live` |
| `gemini-2.5-flash-native-audio-preview-12-2025` | 12 dhjetor 2025 | 17 nëntor 2026 | `gemini-3.8-live` |
| `gemini-live-2.5-flash-preview` | 17 qershor 2025 | 9 dhjetor 2025 | `gemini-3.8-live` |

## Modelet e audios

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-3.5-transcribe` | Gusht 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| Shiko paraprakisht modelet | | | |
| `gemini-2.5-flash-preview-tts` | 20 maj 2025 | 17 nëntor 2026 | `gemini-3.8-flash-tts` ose `gemini-3.8-flash-lite-tts` |
| `gemini-2.5-pro-preview-tts` | 20 maj 2025 | 17 nëntor 2026 | `gemini-3.8-flash-tts` ose `gemini-3.8-flash-lite-tts` |

## Modelet e integrimit

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-embedding-2` | 22 prill 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| `gemini-embedding-001` | 14 korrik 2025 | 14 maj 2028 | `gemini-embedding-2` |
| `text-embedding-004` | 9 prill 2024 | 14 janar 2026 | `gemini-embedding-2` |
| Shiko paraprakisht modelet | | | |
| `embedding-2-preview` | 10 mars 2026 | 10 gusht 2026 | `gemini-embedding-2` |
| `embedding-001` | 9 prill 2024 | 30 tetor 2025 | `gemini-embedding-2` |
| `embedding-gecko-001` |  | 30 tetor 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp` |  | 30 tetor 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp-03-07` |  | 30 tetor 2025 | `gemini-embedding-2` |

## Modelet e Nano Banana

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-nano-banana-2.1` | 6 tetor 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3.1-flash-lite-image` | 30 qershor 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-3.1-flash-image` | 28 maj 2026 | Nuk është njoftuar asnjë datë për çaktivizimin | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image` | 28 maj 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `gemini-2.5-flash-image` | 2 tetor 2025 | 15 mars 2027 | `gemini-3.1-flash-lite-image` |
| Shiko paraprakisht modelet | | | |
| `gemini-3.1-flash-image-preview` | 26 shkurt 2026 | 25 qershor 2026 | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image-preview` | 20 nëntor 2025 | 25 qershor 2026 | `gemini-3-pro-image` |
| `gemini-2.5-flash-image-preview` | 7 maj 2025 | 15 janar 2026 | `gemini-nano-banana-2.1` |
| `gemini-2.0-flash-preview-image-generation` | 7 maj 2025 | 14 nëntor 2025 | `gemini-nano-banana-2.1` |

## Modelet e Imagen

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | 24 qershor 2025 | 17 gusht 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-001` | 24 qershor 2025 | 17 gusht 2026 | `gemini-nano-banana-2.1` |
| `imagen-4.0-fast-generate-001` | 24 qershor 2025 | 17 gusht 2026 | `gemini-nano-banana-2.1` |
| `imagen-3.0-generate-002` | 6 shkurt 2025 | 10 nëntor 2025 | `imagen-4.0-generate-001` |
| Shiko paraprakisht modelet | | | |
| `imagen-4.0-generate-preview-06-06` | 24 qershor 2025 | 17 shkurt 2026 | `imagen-4.0-generate-001` |
| `imagen-4.0-ultra-generate-preview-06-06` | 24 qershor 2025 | 17 shkurt 2026 | `imagen-4.0-ultra-generate-001` |

## Modelet e Veo

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | 9 shtator 2025 | 30 qershor 2026 | `veo-3.1-generate-preview` ose modelet GA në [Platformën e agjentit të Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=sq) |
| `veo-3.0-fast-generate-001` | 9 shtator 2025 | 30 qershor 2026 | `veo-3.1-fast-generate-preview` ose modelet GA në [Platformën e agjentit të Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=sq) |
| `veo-2.0-generate-001` | 9 prill 2025 | 30 qershor 2026 | `veo-3.1-generate-preview` ose modelet GA në [Platformën e agjentit të Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=sq) |
| Shiko paraprakisht modelet | | | |
| `veo-3.1-lite-generate-preview` | 31 mars 2026 | 22 tetor 2026 | `gemini-omni-1.1-flash` |
| `veo-3.1-generate-preview` | 15 tetor 2025 | 22 tetor 2026 | `gemini-omni-1.1-flash` |
| `veo-3.1-fast-generate-preview` | 15 tetor 2025 | 22 tetor 2026 | `gemini-omni-1.1-flash` |
| `veo-3.0-generate-preview` | 31 korrik 2025 | 12 nëntor 2025 | `veo-3.1-generate-preview` |
| `veo-3.0-fast-generate-preview` | 31 korrik 2025 | 12 nëntor 2025 | `veo-3.1-fast-generate-preview` |

## Modelet e Gemini Omni Flash

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `gemini-omni-1.1-flash` | 27 gusht 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| Shiko paraprakisht modelet | | | |
| `gemini-omni-flash-preview` | 30 qershor 2026 | 22 tetor 2026 | `gemini-omni-1.1-flash` |

## Modelet e Lyria

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| `lyria-3.5` | 3 shtator 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| Shiko paraprakisht modelet | | | |
| `lyria-3-clip-preview` | 25 mars 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| `lyria-3-pro-preview` | 25 mars 2026 | Nuk është njoftuar asnjë datë mbylljeje | `lyria-3.5` |
| `lyria-realtime-exp` | 20 maj 2025 | Nuk është njoftuar asnjë datë mbylljeje |  |

## Modele robotike

| **Modeli** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| Shiko paraprakisht modelet | | | |
| `gemini-robotics-er-1.6-preview` | 14 prill 2026 | 31 gusht 2026 | gemini-robotics-er-2-preview |
| `gemini-robotics-er-1.5-preview` | 25 shtator 2025 | 30 prill 2026 | `gemini-robotics-er-1.6-preview` |

## Agjentët e menaxhuar

| **Agent** | **Data e publikimit** | **Data e heqjes nga funksionimi** | **Zëvendësimi i rekomanduar** |
| --- | --- | --- | --- |
| Shiko paraprakisht agjentët | | | |
| `antigravity-preview-09-2026` | 17 shtator 2026 | Nuk është njoftuar asnjë datë për çaktivizimin |  |
| `antigravity-preview-05-2026` | 19 maj 2026 | 5 tetor 2026 | `antigravity-preview-09-2026` |
| `deep-research-preview-04-2026` | 21 prill 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `deep-research-max-preview-04-2026` | 21 prill 2026 | Nuk është njoftuar asnjë datë mbylljeje |  |
| `deep-research-pro-preview-12-2025` | 11 dhjetor 2025 | 23 tetor 2026 | `deep-research-preview-04-2026` |

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-12 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-12 UTC."],[],[]]
