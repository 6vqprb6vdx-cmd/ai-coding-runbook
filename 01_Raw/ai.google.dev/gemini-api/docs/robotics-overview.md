---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=it
fetched_at: 2026-11-02T07:05:49.867843+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Gemini Robotics ER

I modelli Gemini Robotics ER (embodied reasoning) sono modelli di linguaggio visivo (VLM) che consentono ai robot di percepire e interagire con il mondo fisico. Interpretano i dati visivi, eseguono ragionamenti spaziali e temporali, pianificano attività in più passaggi e orchestrano robot e strumenti.

## Modelli

Il modello Gemini Robotics ER 2 è l'ultimo modello di Gemini Robotics.
È il nostro modello di ragionamento aggiornato che consente ai robot di comprendere con precisione l'ambiente circostante. È specializzato in funzionalità di ragionamento basate sull'interazione con il mondo fisico, come l'orchestrazione agentica dei robot (ad es. utilizzando VLA), la comprensione dei video dei robot, tra cui la comprensione dei progressi e il rilevamento del successo, la lettura degli strumenti, il puntamento e il ragionamento spaziale.

Il modello Gemini Robotics ER 2 introduce due endpoint del modello:

- **`gemini-robotics-er-2-preview`**: il modello ER 2 standard. Si basa su Gemini 3.5 Flash con un ragionamento spaziale migliorato, la ricerca di momenti nei video, la classificazione dell'avanzamento dei video, l'orchestrazione multi-robot e l'utilizzo di strumenti in più passaggi.
- **`gemini-robotics-er-2-streaming-preview`**: ottimizzato per lo streaming in tempo reale utilizzando l'[API Live](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it). Utilizza questo modello per agenti robotici a bassa latenza che elaborano input audio e video continui.

Gemini Robotics ER 1.6 è stato
[ritirato il 31 agosto 2026](https://ai.google.dev/gemini-api/docs/deprecations?hl=it#robotics-models).
Se utilizzi ancora Gemini Robotics ER 1.6, esegui l'upgrade a Gemini Robotics ER 2 sostituendo `model="gemini-robotics-er-1.6-preview"` con `model="gemini-robotics-er-2-preview"` o `model="gemini-robotics-er-2-streaming-preview"` nelle chiamate API.

[Prova Gemini Robotics ER 2 in Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=it)

## Funzionalità di robotica

Gemini Robotics ER supporta una serie di funzionalità di ragionamento basate sull'interazione con il mondo fisico.
Seleziona una funzionalità per saperne di più:

| Capacità | Descrizione | Guida |
| --- | --- | --- |
| Ragionamento spaziale | Indica gli oggetti, monitorali nei video, rilevane la presenza con i riquadri di delimitazione, pianifica le traiettorie. | [Ragionamento spaziale](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=it) |
| Visione agentica | Utilizza l'esecuzione di codice per migliorare altre funzionalità sfruttando gli strumenti di manipolazione delle immagini. | [Visione agentica](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=it) |
| Orchestrazione delle attività | Combina il ragionamento spaziale con API di robot personalizzate per completare attività a lungo termine. | [Orchestrazione delle attività](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=it) |
| Streaming (solo endpoint di streaming Gemini Robotics ER 2) | Streaming bidirezionale per agenti robot in tempo reale con chiamata di funzione a bassa latenza. | [Streaming per la robotica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it) |
| Avanzamento video (solo Gemini Robotics ER 2) | Individuazione di momenti e classificazione dei progressi da feed video continui. | [Comprensione dei video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=it) |

## Prima di iniziare

I modelli Gemini Robotics ER sono disponibili tramite l'**API Gemini Developer**. Per iniziare, crea una [chiave API Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=it) da [Google AI Studio](https://aistudio.google.com/apikey?hl=it) o dalla [console Google Cloud](https://ai.google.dev/gemini-api/docs/api-key?hl=it#cloud-console) e [configura l'ambiente](https://ai.google.dev/gemini-api/docs/api-key?hl=it#setup-environment).

Per informazioni dettagliate sui tipi di chiavi, sulla sicurezza e su come configurare la chiave in Python, JavaScript e altri linguaggi, consulta [Utilizzo delle chiavi API Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=it).

## Per iniziare

L'esempio seguente trova gli oggetti in un'immagine e restituisce le relative etichette e coordinate 2D normalizzate. Puoi passare questo output direttamente a un'API di robotica o a un modello VLA per generare azioni del robot.

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const PROMPT = `
  Point to no more than 10 items in the image. The label returned
  should be an identifying name for the object detected.
  The answer should follow the json format: [{"point": <point>,
  "label": <label1>}, ...]. The points are in [y, x] format
  normalized to 0-1000.
`;
const client = new GoogleGenAI();

const uploadedFile = await client.files.upload({ file: "my-image.png" });

const imageResponse = await client.interactions.create({
  model: "gemini-robotics-er-2-preview",
  input: [
    {
      type: "image",
      uri: uploadedFile.uri,
      mime_type: uploadedFile.mimeType,
    },
    { type: "text", text: PROMPT },
  ],
  generation_config: { thinking_level: "high" },
});

console.log(imageResponse.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.List;

Client client = new Client();

String prompt =
    "Point to no more than 10 items in the image. The label returned "
        + "should be an identifying name for the object detected. "
        + "The answer should follow the json format: [{\"point\": <point>, "
        + "\"label\": <label1>}, ...]. The points are in [y, x] format "
        + "normalized to 0-1000.";

File uploadedFile =
    client.files.upload(
        new java.io.File("my-image.png"),
        UploadFileConfig.builder().mimeType("image/png").build());

Content imageContent =
    ImageContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/png")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-robotics-er-2-preview"))
        .input(InteractionsInput.ofContent(List.of(imageContent, textContent)))
        .generationConfig(
            GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction imageResponse =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(imageResponse.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": <point>,
"label": <label1>}, ...]. The points are in [y, x] format
normalized to 0-1000.`

    uploadedFile, err := client.Files.UploadFromPath(ctx, "my-image.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-robotics-er-2-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: genai.Ptr(interactions.ImageMimeTypeImagePng),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

L'output sarà un array JSON contenente oggetti, ciascuno con un `point` (coordinate `[y, x]` normalizzate) e un `label` che identifica l'oggetto.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

L'immagine seguente è un esempio di come possono essere visualizzati questi punti:

![Un esempio che mostra i punti degli oggetti in un'immagine](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=it)

## Come funziona

Gemini Robotics ER accetta input di immagini, video o audio con prompt in linguaggio naturale. Identifica gli oggetti, ragiona sul contesto della scena e sulle relazioni spaziali e restituisce un output strutturato come coordinate o riquadri di delimitazione.

Gemini Robotics ER è anche agentico: suddivide le attività complesse in sottoattività e le esegue chiamando le funzioni del robot o eseguendo il codice generato. Ad esempio, "metti la mela nella ciotola" diventa una sequenza di passaggi di individuazione, presa e posizionamento.

Per informazioni dettagliate su come Gemini esegue le chiamate degli strumenti, consulta [Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=it#how-it-works).

## Sicurezza

Sebbene Gemini Robotics ER sia stato creato tenendo conto della sicurezza, è tua responsabilità mantenere un ambiente sicuro intorno al robot. I modelli di AI generativa possono commettere errori e i robot fisici possono causare danni. Per saperne di più, visita la [pagina sulla sicurezza di Gemini Robotics](https://deepmind.google/models/gemini-robotics/safety?hl=it).

## Best practice

1. Usa un linguaggio semplice e naturale. Descrivi cosa vuoi che faccia il robot come faresti con una persona. Se un termine non funziona, prova un sinonimo comune.
2. Ottimizza l'input visivo. Ritaglia o aumenta lo zoom su oggetti piccoli o poco chiari prima di inviare l'immagine. L'illuminazione e il basso contrasto cromatico possono influire sul rilevamento.
3. Suddividi le attività complesse in passaggi. Invia ogni passaggio come prompt separato per mantenere il modello concentrato e migliorare l'accuratezza.
4. Esegui query più volte e calcola la media dei risultati per le attività ad alta precisione. Questo approccio basato sul consenso riduce la varianza degli output spaziali.

## Limitazioni

Tieni presenti le seguenti limitazioni durante lo sviluppo con Gemini Robotics ER:

- **Limitazioni delle chiavi API:** l'API Gemini non accetta richieste da chiavi API senza limitazioni e restituisce un errore `403 Forbidden`. Proteggi la tua chiave API aggiungendo limitazioni in [AI Studio](https://aistudio.google.com/api-keys?hl=it).
  Per maggiori dettagli, consulta [Proteggi le chiavi API senza restrizioni](https://ai.google.dev/gemini-api/docs/api-key?hl=it#secure-unrestricted-keys).
- **Latenza e prestazioni:** query complesse, input ad alta risoluzione o livelli di ragionamento elevati possono comportare tempi di elaborazione più lunghi. Per il livello di ragionamento, utilizza Medio per un buon equilibrio tra latenza e prestazioni.
- **Allucinazioni:** come tutti i modelli linguistici di grandi dimensioni, i modelli Gemini Robotics ER
  possono occasionalmente generare "allucinazioni" o fornire informazioni errate,
  soprattutto in caso di prompt ambigui o input fuori distribuzione.
- **Dipendenza dalla qualità del prompt:** la qualità dell'output dipende dalla chiarezza del prompt di input. Utilizza prompt specifici e ben strutturati.
- **Costo di calcolo:** l'esecuzione del modello, in particolare con input video o
  `thinking_budget` elevati, consuma risorse di calcolo e comporta dei costi.
  Per ulteriori dettagli, consulta la pagina [Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it).
- **Tipi di input:** consulta i seguenti argomenti per i dettagli sulle limitazioni di ciascuna modalità.
  - [Input di immagini](https://ai.google.dev/gemini-api/docs/image-understanding?hl=it#technical-details-image)
  - [Input video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it#supported-formats)
  - [Input audio](https://ai.google.dev/gemini-api/docs/audio?hl=it#supported-formats)

## Informativa sulla privacy

Riconosci che i modelli a cui si fa riferimento in questo documento (i "Modelli di robotica") utilizzano dati video e audio per far funzionare e muovere l'hardware in base alle tue istruzioni. Pertanto, puoi utilizzare i Modelli di robotica in modo che i dati di persone identificabili, come dati vocali, immagini e somiglianze ("Dati personali"), vengano raccolti dai Modelli di robotica. Se scegli di utilizzare i Modelli di robotica in modo da raccogliere
Dati personali, accetti di non consentire a nessuna persona identificabile di
interagire con i Modelli di robotica o di essere presente nell'area circostante,
a meno che e fino a quando tali persone identificabili non siano state sufficientemente informate e
non abbiano acconsentito al fatto che i loro Dati personali possano essere forniti a Google e utilizzati
da Google come descritto nei Termini di servizio aggiuntivi delle API Gemini disponibili all'indirizzo
[https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=it)
(i "Termini"), anche in conformità
con la sezione intitolata "In che modo Google utilizza i tuoi dati". L'Utente si assicurerà che tale
avviso consenta la raccolta e l'utilizzo dei Dati personali come descritto nei Termini
e farà ogni sforzo commercialmente ragionevole per ridurre al minimo la raccolta e
la distribuzione dei Dati personali utilizzando tecniche come la sfocatura dei volti e
l'utilizzo dei Modelli di robotica in aree che non contengono persone identificabili,
nella misura possibile.

## Prezzi

Per informazioni dettagliate sui prezzi e sulle regioni disponibili, consulta la pagina dei [prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it).

## Endpoint del modello

### Gemini Robotics ER 2 (anteprima)

| Proprietà | Descrizione |
| --- | --- |
| id\_cardCodice del modello | `gemini-robotics-er-2-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Supportato  **[Uso del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Supportato  **[Ricerca di file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Non supportato  **[Grounding della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Supportato  **[Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto dell'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Supportato |
| speedOpzioni di consumo | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| 123Versioni | Leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models?hl=it#model-versions) per maggiori dettagli.  - Anteprima: `gemini-robotics-er-2-preview` |
| calendar\_monthUltimo aggiornamento | Luglio 2026 |
| id\_cardScheda del modello | [Scheda del modello](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=it) |
| paidPrezzi | [Prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-robotics-er-2) |

### Gemini Robotics ER 2 Streaming Preview

| Proprietà | Descrizione |
| --- | --- |
| id\_cardCodice del modello | `gemini-robotics-er-2-streaming-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Non supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Non supportato  **[Uso del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Non supportato  **[Ricerca di file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Non supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Non supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Supportato  **[Grounding della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Non supportato  **[Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto dell'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Non supportato |
| speedOpzioni di consumo | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Non supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| 123Versioni | Leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models?hl=it#model-versions) per maggiori dettagli.  - Anteprima: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthUltimo aggiornamento | Luglio 2026 |
| id\_cardScheda del modello | [Scheda del modello](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=it) |
| paidPrezzi | [Prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-robotics-er-2-streaming) |

### Gemini Robotics ER 1.6 Preview

| Proprietà | Descrizione |
| --- | --- |
| id\_cardCodice del modello | `gemini-robotics-er-1.6-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Supportato  **[Uso del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Supportato  **[Ricerca di file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Non supportato  **[Grounding della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Supportato  **[Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto dell'URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Supportato |
| speedOpzioni di consumo | **[API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| 123Versioni | Leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models?hl=it#model-versions) per maggiori dettagli.  - Arresta: `gemini-robotics-er-1.6-preview` |
| calendar\_monthUltimo aggiornamento | Dicembre 2025 |
| cognition\_2Knowledge cutoff | Gennaio 2025 |

## Passaggi successivi

- [Ragionamento spaziale](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=it): puntamento, monitoraggio, riquadri di delimitazione, traiettorie.
- [Capacità agentiche](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=it): esecuzione di codice, lettura di strumenti, annotazione di immagini.
- [Orchestrazione delle attività](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=it): attività a lungo termine con API dei robot personalizzate.
- [Robotica con streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it): streaming bidirezionale in tempo reale (solo Gemini Robotics ER 2).
- [Comprensione dei video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=it): individuazione dei momenti e classificazione dei progressi (solo Gemini Robotics ER 2).
- [Sicurezza di Gemini Robotics](https://deepmind.google/models/gemini-robotics/safety?hl=it): ricerca sulla sicurezza alla base della famiglia di modelli.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-29 UTC."],[],[]]
