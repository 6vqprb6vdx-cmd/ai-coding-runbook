---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=pt-BR
fetched_at: 2026-09-14T05:39:10.672827+00:00
title: "Gerar m\u00fasicas com o Lyria 3.5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Gerar músicas com o Lyria 3.5

O Lyria 3.5 é a família de modelos de geração de música do Google, disponível
pela API Gemini. Com o Lyria 3.5, é possível gerar áudio estéreo de alta qualidade em 44, 1 kHz com base em comandos de texto ou imagens. Esses modelos oferecem coerência estrutural, incluindo vocais, letras sincronizadas e arranjos instrumentais completos.

A família Lyria inclui os seguintes modelos:

| Modelo | ID do modelo | Ideal para | Duração | Saída |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Clipes curtos, loops, prévias | 30 segundos | MP3 |
| **Lyria 3.5** | `lyria-3.5` | Músicas completas com versos, refrões e pontes | Alguns minutos (controláveis usando o comando) | MP3 |

Os dois modelos podem ser usados com a nova
[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br), que aceita entradas multimodais (texto e imagens) e produz áudio **estéreo de alta fidelidade de 44,1 kHz**.

## Gerar um videoclipe

O modelo Lyria 3 Clip sempre gera um clipe de **30 segundos**. Para gerar um
clipe, chame o método `interactions.create` com um comando de texto. A resposta sempre inclui a letra e a estrutura da música geradas, além do áudio no esquema `steps`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

É possível recuperar os dados de música gerados usando a propriedade `interaction.output_audio`, que retorna o último bloco de áudio gerado. Também é possível recuperar
a letra e a estrutura da música usando a propriedade `interaction.output_text`. Para detalhes sobre propriedades de conveniência, consulte a
[visão geral das interações](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br#convenience-properties).

## Gerar uma música completa

Use o modelo `lyria-3.5` para gerar músicas completas que duram alguns minutos. O modelo Pro entende a estrutura musical e pode criar
composições com versos, refrões e pontes distintos. É possível influenciar a duração especificando-a no comando (por exemplo, "crie uma música de 2 minutos") ou usando [carimbos de data/hora](#timing) para definir a estrutura.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody."
}'
```

## Selecionar o formato de saída

Por padrão, os modelos do Lyria 3.5 geram áudio no formato **MP3**. Para o Lyria 3.5, também é possível pedir a saída no formato **WAV** definindo o `response_format`.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Analise a resposta

A resposta da Lyria 3.5 contém vários blocos de conteúdo no esquema `steps`.
As interações retornam uma sequência de etapas, em que `model_output` etapas contêm o
conteúdo gerado.
Os blocos de conteúdo de texto contêm a letra gerada ou uma descrição JSON da estrutura da música.
Os blocos de conteúdo do tipo `audio` contêm os dados de áudio codificados em base64.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### Letras e músicas intercaladas

Como a saída do Lyria 3.5 é complexa, contendo etapas e blocos separados para letras geradas (texto) e a música em si (áudio), as propriedades de conveniência oferecem um atalho rápido e recomendado.

No entanto, se você quiser controle programático total sobre a linha do tempo bruta de etapas
retornadas pelo servidor (como registrar blocos de conteúdo individuais à medida que são
recebidos), itere manualmente em `steps`:

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

## Gerar música com base em imagens

O Lyria 3.5 aceita entradas multimodais. Você pode fornecer até **10 imagens** com seu comando de texto na lista `input`, e o modelo vai compor músicas inspiradas no conteúdo visual.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3.5",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3.5",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3.5",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## Fornecer letras personalizadas

Você pode escrever suas próprias letras e incluí-las no comando. Use tags de seção
como `[Verse]`, `[Chorus]` e `[Bridge]` para ajudar o modelo a entender a
estrutura da música:

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## Controlar o tempo e a estrutura

É possível especificar exatamente o que acontece em momentos específicos da música usando
carimbos de data/hora. Isso é útil para controlar quando os instrumentos entram, quando as letras
são entregues e como a música progride:

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Gerar músicas instrumentais

Para música de fundo, trilhas sonoras de jogos ou qualquer caso de uso em que os vocais não sejam necessários, peça ao modelo para produzir músicas apenas instrumentais:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Gerar músicas em diferentes idiomas

O Lyria 3.5 gera letras no idioma do seu comando. Para gerar uma música com letras em francês, escreva o comando nesse idioma. O modelo adapta o estilo vocal e a pronúncia para corresponder ao idioma.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Inteligência do modelo

O Lyria 3.5 analisa seu processo de comando em que o modelo raciocina sobre a estrutura musical (introdução, verso, refrão, ponte etc.) com base no seu comando.
Isso acontece antes da geração do áudio e garante coerência estrutural e musicalidade.

## Guia de comandos

Seu comando pode ser simples, como "uma música folk sobre gatos fofos evitando poças, vocais femininos e o barulho da chuva", ou algo detalhado e estruturado, como:

> Uma música synth-pop no estilo dos anos 80 com uma batida marcante, sintetizadores brilhantes e um refrão cativante e hino. A música precisa ter uma vibe retrofuturista, lembrando os clássicos do pop dos anos 80, com uma produção moderna. O
> tempo precisa ser animado e dançante, em torno de 120 BPM, com uma estrutura
> clara de verso-refrão e um refrão instrumental memorável. A letra fala sobre
> a sensação de se arrumar para uma festa.

Comandos simples e complexos podem gerar boas respostas. Teste estas dicas para descobrir o que funciona melhor para você.

### Gênero

Comece o comando com o gênero musical que você quer, como hip hop, rock e rap. É possível especificar uma mistura de gêneros:

- Uma fusão de metal e rap
- Uma combinação de death metal e ópera
- Uma peça clássica com elementos eletrônicos de drone
- Música eletrônica moderna (EDM) misturada com Europop

Você também pode incorporar uma era:

- Hip-hop do início dos anos 90
- Pop iê-iê francês dos anos 60
- Experimentação eletrônica dos anos 80
- Pop mainstream dos anos 2000

Se você pedir gêneros personalizados ou variantes regionais, como "techno de Berlim" ou "hyphy da área da baía", o modelo vai tentar capturar essa essência, mas nem sempre vai acertar.

### Instrumentos

Por padrão, o Lyria 3.5 cria músicas com os instrumentos e ferramentas que você esperaria para o gênero. Não é necessário ser prescritivo.

No entanto, uma música de dança não vai incluir um saxofone a menos que você peça. Se você quiser um solo de saxofone, use o comando:

> Uma música dançante com uma batida marcante, sintetizadores brilhantes e um refrão cativante e
> empolgante. Um solo de saxofone deve entrar durante a ponte.

Seu comando pode incluir instrumentos específicos, como eles soam e como interagem entre si. Você pode usar essa combinação para criar determinados climas ou texturas:

- Uma linha de baixo suja e distorcida lutando contra hi-hats limpos e nítidos
- Pads de sintetizador analógico quentes aumentando sob um violão acústico seco e intimista
- Uma parede de som criada por várias camadas de guitarras distorcidas, com vocais distantes e enterrados

### Estrutura da música

Você pode descrever a progressão de uma música no comando. Use setas ou uma lista para definir o fluxo:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- Comece com uma introdução de piano suave, crie um verso alto, faça um silêncio e exploda no refrão.

Você também pode especificar como os níveis de energia mudam entre essas seções:

- Crie tensão no pré-refrão e depois faça um silêncio antes de um refrão enorme e
  explosivo.
- Crescendo gradual ao longo da música, adicionando um instrumento de cada vez até uma parede caótica de som
- Parada repentina após a ponte, seguida de um refrão a cappella

Você também pode pedir o horário exato em que quer que algo aconteça:

- Aumente até uma queda em 12 segundos
- Alguém diz "o quê?" a cada dois segundos
- O refrão começa aos 22 segundos

### Letras

Os vocais e a letra são gerados por padrão. Você pode fornecer suas próprias letras, pedir para não incluir letras (ou um instrumental) ou direcionar a geração de letras da maneira que quiser.

A letra vai estar no idioma em que você escrever o comando. Você também pode pedir para as letras serem escritas em outro idioma, como "Escreva a letra em francês".

#### Usar suas próprias letras

Para fornecer suas próprias letras ao modelo, inclua-as no comando com o prefixo "Letra:":

```
Lyrics:

[Intro]
Oooh, oooh

[Verse 1]
Let's go
Let's go
Go with the flow

[Chorus]
...
```

Você pode prefixar partes da música com títulos de seção como `[Intro]`,
`[Verse 1]`, `[Pre-chorus]`, `[Chorus]` e `[Outro]`.

Se você quiser que uma palavra ou linha seja repetida, como um eco ou por cantores de apoio, inclua entre parênteses: "Vamos (vamos)".

#### Pedir ao modelo para escrever letras de músicas

Se você quiser que o Lyria 3.5 crie letras para você, é melhor incluir detalhes sobre o tema no comando. Caso contrário, o modelo precisará inferir um assunto com base no comando de música, e talvez não seja o que você quer.

> A letra fala sobre um amor perdido e a dor de um coração partido. A cantora está relembrando um relacionamento passado e as memórias que voltam à tona.

Se quiser um refrão repetido, peça um no comando:

> A letra fala sobre um amor perdido e a dor de um coração partido. A cantora está relembrando um relacionamento passado e as memórias que voltam à tona. Um refrão forte se concentra em superar a dor e seguir em frente.

O Lyria 3.5 direciona automaticamente a estrutura da letra para o tipo de música que você está pedindo, mas você também pode reforçar isso no comando. Exemplo:

> Uma música eletrônica que repete a mesma frase energética várias vezes.

Também é possível pedir efeitos vocais que não sejam estritamente letras de músicas, por exemplo:

- Uma amostra repetida de um filme diz "Não consigo acreditar!" ao longo da música.
- Uma música techno de alta energia, logo antes da batida, o som para e uma voz diz "Não sei o que estou fazendo aqui", e então a música começa.
- A música começa com uma conversa sobre os filmes dos anos 90 serem melhores do que os de hoje. Em seguida, a faixa passa para uma música pop.

### Vocais

Você pode pedir como quer que a letra seja entregue. Para ter os melhores resultados, especifique um perfil detalhado do cantor, incluindo gênero, timbre e extensão vocal.

- **Soprano feminino**: timbre claro e cristalino com uma qualidade ágil e crescente. Capaz de alcançar notas altas com uma textura arejada e ofegante.
- **Alto feminino**: alcance mais baixo rico, quente e rouco. Timbre esfumaçado com um toque de vocal fry, cheio de alma e ressonante.
- **Tenor masculino**: brilhante, penetrante e energético. Timbre jovem com um leve toque nasal, que se destaca na mixagem com grande potência de canto.
- **Barítono masculino**: grave, aveludado e suave como chocolate. Voz de peito ressonante com uma entrega suave e melodiosa.
- **Rocker experiente (masculino)**: rouca e texturizada com um timbre grave, que lembra o grunge dos anos 90. Intervalo superior tenso para intensidade emocional.

### Outros parâmetros de comando

Você também pode incluir estes parâmetros para refinar ainda mais o comando:

- **BPM**: defina o tempo (por exemplo, "120 BPM", "tempo lento em torno de 70 BPM").
- **Tonalidade/escala**: especifique uma tonalidade musical (por exemplo, "em sol maior", "ré menor").
- **Clima e atmosfera**: use adjetivos descritivos (por exemplo, "nostálgico", "agressivo", "etéreo", "onírico").
- **Duração**: o modelo de clipe sempre produz clipes de 30 segundos. Para o modelo Pro, especifique a duração desejada no comando (por exemplo, "crie uma música de 2 minutos") ou use carimbos de data/hora para controlar a duração.

### Exemplos de comandos

Confira alguns exemplos de comandos eficazes:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Práticas recomendadas

- **Itere primeiro com o Clipe.** Use o modelo `lyria-3-clip-preview` mais rápido para
  testar comandos antes de gerar um texto completo com
  `lyria-3.5`.
- **Faça uma descrição específica**. Comandos vagos geram resultados genéricos. Mencione instrumentos, BPM, tom, humor e estrutura para ter o melhor resultado.
- **Use o mesmo idioma.** Use o comando no idioma em que você quer a letra.
- **Use tags de seção.** As tags `[Verse]`, `[Chorus]` e `[Bridge]` oferecem ao modelo uma estrutura clara para seguir.
- **Separe a letra das instruções.** Ao fornecer letras personalizadas, separe-as claramente das instruções de direção musical.

## Limitações

- **Segurança**: todos os comandos são verificados por filtros de segurança. Os comandos que acionam os filtros são bloqueados. Isso inclui comandos que pedem vozes de artistas específicos ou a geração de letras protegidas por direitos autorais.
- **Marca-d'água**: todo o áudio gerado inclui uma [marca-d'água de áudio do SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=pt-br) para identificação. Essa marca-d'água é imperceptível ao ouvido humano e não afeta a experiência de audição.
- **Edição multiturno**: a geração de música é um processo de turno único.
  A edição iterativa ou o refinamento de um clipe gerado com vários comandos não é compatível com a versão atual do Lyria 3.5.
- **Duração**: o modelo de clipe sempre gera clipes de 30 segundos. O modelo Pro
  gera músicas que duram alguns minutos. A duração exata pode ser
  influenciada pelo comando.
- **Determinismo**: os resultados podem variar entre as chamadas, mesmo com o mesmo comando.

## A seguir

- Confira os [preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) dos modelos do Lyria 3.5.
- Teste a [geração de músicas em streaming e em tempo real](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pt-br) com o Lyria RealTime.
- Gere conversas com vários locutores usando os [modelos de TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br).
- Saiba como gerar [imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) ou [vídeos](https://ai.google.dev/gemini-api/docs/video?hl=pt-br).
- Saiba como o Gemini pode [entender arquivos de áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br).
- Converse em tempo real com o Gemini usando a [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-10 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-10 UTC."],[],[]]
