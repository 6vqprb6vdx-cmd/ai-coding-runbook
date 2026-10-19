---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=sq
fetched_at: 2026-10-19T05:30:32.974250+00:00
title: "P\u00ebrmbledhja e Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Përmbledhja e Gemini Live API

API-ja e transmetimit të drejtpërdrejtë mundëson ndërveprime me zë dhe pamje në kohë reale me vonesë të ulët me Gemini. Ai përpunon transmetime të vazhdueshme të audios, imazheve dhe tekstit për të ofruar përgjigje të menjëhershme të ligjëruara si nga një njeri, duke krijuar një përvojë natyrale bisedore për përdoruesit e tu.

![Përmbledhja e API-së së transmetimit të drejtpërdrejtë](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=sq)

[Provo API-n e transmetimit të drejtpërdrejtë në Google AI Studiomic](https://aistudio.google.com/live?hl=sq)
[Klonizo shembuj të aplikacioneve nga GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Përdor aftësitë e agjentit të kodimitterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=sq)

## Rastet e përdorimit

API-ja e Live mund të përdoret për të ndërtuar agjentë zanorë në kohë reale për një
larmi industrish, duke përfshirë:

- **Tregtia online dhe shitësit me pakicë:** Asistentë për blerjet që ofrojnë rekomandime të personalizuara dhe agjentë të mbështetjes që zgjidhin problemet e klientëve.
- **Lojëra:** Personazhe ndërveprues që nuk mund të luhen (NPC), ndihmës brenda lojës dhe përkthim në kohë reale të përmbajtjeve brenda lojës.
- **Ndërfaqet e gjeneratës së ardhshme:** Përvojat e aktivizuara me zë dhe video në robotikë, syze inteligjente dhe automjete.
- **Kujdesi shëndetësor:** Shoqëruesit shëndetësorë për mbështetjen dhe edukimin e pacientëve.
- **Shërbimet financiare:** Këshilltarë të IA-së për menaxhimin e pasurisë dhe udhëzime për investimet.
- **Edukimi:** Mentorë me IA dhe shoqërues të nxënësve që ofrojnë udhëzime dhe komente të personalizuara.
- **Përkthimi dhe lokalizimi:** Përkthimi në kohë reale me vonesë të ulët i bisedave të folura, duke mundësuar komunikimin e pandërprerë në shumë gjuhë.
- **Transkriptimi dhe titrat e drejtpërdrejta:** Transmetimi i ligjërimit në tekst në kohë reale për titrat e drejtpërdrejta, transkriptimin e takimeve, diktimin me zë dhe regjistrimin e telefonatave me klientët.

## Veçoritë kryesore

API-ja e drejtpërdrejtë ofron një grup gjithëpërfshirës veçorish për ndërtimin e
agjentëve të fuqishëm zanorë:

- [**Mbështetja shumëgjuhëshe**](https://ai.google.dev/gemini-api/docs/live-guide?hl=sq#supported-languages):
  Bisedo në 70 gjuhë të mbështetura.
- [**Ndërhyrja**](https://ai.google.dev/gemini-api/docs/live-guide?hl=sq#interruptions):
  Përdoruesit mund ta ndërpresin modelin në çdo kohë për ndërveprime të përgjegjshme.
- [**Përdorimi i veglës**](https://ai.google.dev/gemini-api/docs/live-tools?hl=sq):
  Integron veglat si telefonatat e funksioneve dhe "Kërko në Google" për ndërveprime dinamike.
- [**Transkriptimet e audios**](https://ai.google.dev/gemini-api/docs/live-guide?hl=sq#audio-transcription):
  Ofron transkriptet me tekst të hyrjes së përdoruesit dhe daljes së modelit.
- [**Audio proaktiv**](https://ai.google.dev/gemini-api/docs/live-guide?hl=sq#proactive-audio):
  Të lejon të kontrollosh se kur përgjigjet modeli dhe në çfarë kontekstesh.
- [**Dialogu afektiv**](https://ai.google.dev/gemini-api/docs/live-guide?hl=sq#affective-dialog):
  Përshtat stilin dhe tonin e përgjigjes për t'iu përshtatur shprehjes së hyrjes së përdoruesit.
- [**Transkriptimi në çast**](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=sq):
  Transmetimi i vazhdueshëm i ligjërimit në tekst në kohë reale me zbulimin automatik të gjuhës dhe fjalorin e personalizuar.
- [**Përkthimi në çast**](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=sq):
  Përkthimi zë-zë në kohë reale në mbi 70 gjuhë.

## Specifikimet teknike

Tabela e mëposhtme përcakton specifikimet teknike për
API-në e transmetimit të drejtpërdrejtë:

| Kategoria | Detajet |
| --- | --- |
| Modalitetet e hyrjes | Audio (audio PCM 16-bitëshe e papërpunuar, 16 kHz, little-endian), imazhe (JPEG <= 1 FPS), tekst |
| Modalitetet e daljes | Audio (audio PCM 16-bit i papërpunuar, 24 kHz, little-endian) |
| Protokolli | Lidhje me gjendje të WebSocket (WSS) |

## Zgjidh një qasje zbatimi

Kur integrohesh me API-në e transmetimit të drejtpërdrejtë, do të duhet të zgjedhësh një nga qasjet e mëposhtme të
zbatimit:

- **Server-to-server**: Backend-i yt lidhet me Live API duke përdorur
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Zakonisht, klienti yt dërgon të dhëna transmetimi (audio, video, tekst) në serverin tënd, i cili më pas i transferon ato te Live API.
- **Klient-te-server**: Kodi yt i frontend-it lidhet drejtpërdrejt me Live API
  duke përdorur [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) për të transmetuar të dhëna, duke anashkaluar backend-in tënd.

## Fillo

Zgjidh udhëzuesin që përputhet me mjedisin tënd të zhvillimit:

Nga serveri te serveri

### [Udhëzuesi i GenAI SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=sq)

Lidhu me Gemini Live API duke përdorur GenAI SDK për të ndërtuar një aplikacion multimodal në kohë reale me një sistem fundor në Python.

Klient-te-server

### [Udhëzuesi i WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=sq)

Lidhu me API-në e Gemini Live duke përdorur WebSockets për të ndërtuar një aplikacion multimodal në kohë reale me një frontend në JavaScript dhe kode qasjeje të përkohshme.

Paketa e zhvillimit të agjentit

### [Udhëzuesi i ADK-së](https://google.github.io/adk-docs/streaming/)

Krijo një agjent dhe përdor transmetimin e Agent Development Kit (ADK) për të aktivizuar komunikimin zanor dhe me video.

## Integrimet e partnerëve

Për të thjeshtuar zhvillimin e aplikacioneve të audios dhe videos në kohë reale, mund të përdorësh një integrim të një pale të tretë që mbështet API-n e Gemini Live nëpërmjet WebRTC ose WebSockets.

[LiveKit

Përdor Gemini Live API me LiveKit Agents.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat nga Daily

Krijo një robot bisede me IA në kohë reale duke përdorur Gemini Live dhe Pipecat.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam nga Software Mansion

Krijoni aplikacione të transmetimit të drejtpërdrejtë të videos dhe audios me Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Agjentët e vizionit sipas transmetimit

Krijo aplikacione të IA-së për zërin dhe videon në kohë reale me Vision Agents.](https://visionagents.ai/integrations/gemini)
[Voximplant

Lidh telefonatat hyrëse dhe dalëse me Live API me Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

Krijo aplikacione bisedare në kohë reale me IA-në me Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Fillo me Gemini Live API duke përdorur Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=sq)

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-07 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-07 UTC."],[],[]]
