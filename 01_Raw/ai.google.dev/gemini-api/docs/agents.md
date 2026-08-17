---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=it
fetched_at: 2026-08-17T02:24:03.884086+00:00
title: "Panoramica degli agenti \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Panoramica degli agenti

Gli agenti gestiti nell'API Gemini ti offrono un harness dell'agente configurabile. Una singola chiamata API esegue il provisioning di una sandbox Linux in cui l'agente ragiona, esegue il codice, gestisce i file e naviga sul web in modo autonomo.

[rocket\_launch

Guida rapida

Effettua la tua prima chiamata all'agente, trasmetti le risposte in streaming e crea un agente personalizzato.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it)
[smart\_toy

Agente Antigravity

Funzionalità, strumenti, input multimodale e prezzi per l'agente predefinito.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it)
[experiment

Agenti in AI Studio

Playground visivo per la prototipazione di agenti senza scrivere codice.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=it)

## Agenti gestiti disponibili

- **[Agente Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it)**: agente gestito per uso generico basato su Gemini 3.6 Flash. Esegue il codice, gestisce i file e cerca sul web all'interno di una sandbox Linux sicura ospitata da Google. Puoi
  configurare il modello sottostante (ad es. Gemini 3.6 Flash, Gemini 3.5 Flash o Gemini 3.5 Flash-Lite)
  utilizzando `agent_config`, ed estenderlo con le tue istruzioni, skill e dati per
  [creare un agente personalizzato](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it)**: agente di ricerca autonomo
  che pianifica, esegue e sintetizza attività di ricerca in più fasi per casi d'uso
  come analisi di mercato, due diligence e revisioni della letteratura.

## Sicurezza e best practice

Ogni agente viene eseguito in un ambiente sandbox isolato a livello di sistema operativo.
Per impostazione predefinita, la sandbox ha accesso alla rete in uscita senza restrizioni. Puoi limitare o disattivare l'accesso alla rete utilizzando una lista consentita.

### Accesso alla rete

Per impostazione predefinita, gli ambienti hanno accesso alla rete in uscita senza restrizioni. Utilizza una lista consentita `network` per limitare il traffico in uscita a domini specifici o pattern con caratteri jolly. Per i dettagli sulla configurazione, vedi
[Lista consentita di rete](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=it#network_allow_list) (AI
Studio) o [Regole di rete](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it#with_network_rules)
(API).

### Strumenti e API esterni

Puoi collegare strumenti e API esterni per estendere l'agente. Utilizza solo strumenti provenienti da fonti attendibili e limita le autorizzazioni al minimo necessario. Le credenziali possono essere inserite in modo sicuro tramite le trasformazioni delle intestazioni del proxy in uscita e non vengono mai esposte all'interno della sandbox. L'agente può utilizzare qualsiasi credenziale a cui ha accesso, quindi fornisci solo le credenziali di cui sei disposto a concedere l'ambito completo.

- Utilizza service account o chiavi API con privilegi minimi.
- Prediligi i token di breve durata rispetto alle chiavi di lunga durata.
- Fornisci solo le credenziali di cui sei disposto a concedere l'ambito completo.
- Ruota le credenziali a intervalli regolari.

Per i dettagli sulla configurazione delle trasformazioni delle intestazioni, vedi
[Credenziali](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#credentials).

### Supervisione umana

Verifica sempre gli output (codice generato, trasformazioni dei dati, modifiche alla configurazione) prima di eseguirne il deployment, soprattutto per le attività che modificano i dati o interagiscono con sistemi esterni.

## Prezzi

Gli agenti gestiti utilizzano un [modello con pagamento a consumo](https://ai.google.dev/gemini-api/docs/pricing?hl=it#pricing-for-agents)
basato sui token del modello Gemini e sull'utilizzo degli strumenti. Una singola interazione può attivare più loop di ragionamento, in genere consumando da 100.000 a 3 milioni di token. Il calcolo dell'ambiente **non viene fatturato** durante l'anteprima. Consulta i [costi stimati](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it#availability-and-pricing)
per le suddivisioni per attività. Gli agenti gestiti sono disponibili anche nel livello senza costi con un limite di frequenza e una quota di utilizzo senza costi.

## Limiti

| Limite | Descrizione |
| --- | --- |
| **Durata dell'ambiente** | Gli ambienti vengono eliminati definitivamente dopo 7 giorni di inattività. |
| **Arresto delle VM** | Le VM vengono arrestate dopo un breve periodo di inattività per risparmiare risorse. La richiesta successiva ripristina lo stato (con un avvio a freddo). |
| **Software preinstallato** | Ambiente basato su Ubuntu con Python 3.12 e Node.js 22. Per ulteriori informazioni sull'immagine di base dell'ambiente, vedi [Software preinstallato](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#pre-installed-software). |
| **Numero massimo di agenti** | Puoi avere fino a 1000 agenti gestiti. |

## Framework dell'agente

Puoi anche creare agenti con Gemini utilizzando questi framework e SDK:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=it): crea
  flussi di applicazioni stateful e complessi e sistemi multi-agente utilizzando strutture di grafici.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=it): collega gli agenti Gemini ai
  tuoi dati privati per workflow ottimizzati per RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=it)
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=it): crea
  interfacce utente e agenti basati sull'AI in JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): An
  open-source framework for building and orchestrating interoperable AI
  agents.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=it): Crea
  agenti AI autonomi utilizzando gli stessi strumenti, loop dell'agente e gestione del contesto
  che alimentano Google Antigravity, programmabile in Python.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
