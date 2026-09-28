---
source_url: https://ai.google.dev/gemini-api/docs/voice-design?hl=pt-BR
fetched_at: 2026-09-28T06:10:26.145947+00:00
title: "Design de voz \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Design de voz

Com o design de voz, é possível criar uma persona vocal persistente e inédita com uma descrição em linguagem natural usando o endpoint Voices da API Gemini (`POST /v1beta/voices`). Em vez de ficar limitado a vozes pré-criadas ou gravar áudio de referência, você pode descrever a idade, o timbre, o sotaque e a entonação de um personagem e receber um ID `voice_...` reutilizável salvo no seu projeto.

A maneira mais rápida de criar, testar e iterar vozes personalizadas é com o estúdio interativo **Voice Design** no [Google AI Studio](https://aistudio.google.com/generate-speech?hl=pt-br). Você pode
gerar personas personalizadas com comandos de texto, testá-las com scripts de exemplo e
copiar o ID `voice_...` resultante diretamente no código do aplicativo.

[Testar no Google AI Studio](https://aistudio.google.com/generate-speech?hl=pt-br)

O [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=pt-br) (`gemini-3.8-flash-tts`) e o [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=pt-br) (`gemini-3.8-flash-lite-tts`) são compatíveis com o design de voz.

## Criar uma voz projetada

Use o SDK da GenAI do Google (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) ou a API REST
para criar uma voz personalizada com base em uma descrição de texto. Para vozes `"prompted"`, `voices.create` (`CreateVoice`) e `voices.get` (`GetVoice`) retornam um campo `sample_audio` somente de saída (`mime_type: "audio/wav"`, `data` codificado em base64) para que você possa testar imediatamente a voz gerada:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## Como funciona o design de voz

1. **Criar uma voz com comando**:chame `voices.create` (`POST /v1beta/voices`) com `type="prompted"` e `store=True`.
2. **Receber uma prévia persistente de `voice_id` e `sample_audio`**:a API
   gera a identidade vocal, armazena no seu projeto e retorna um
   ID permanente (por exemplo, `voice_abc123...`) junto com `sample_audio`
   (`mime_type: "audio/wav"`, `data` codificado em base64) contendo o áudio de
   prévia gerado para a voz.
3. **Sintetizar fala**:transmita o `voice_id` em qualquer lugar em que um nome de voz seja aceito
   nas suas solicitações de síntese.

## Sintetizar a fala com a voz criada

Depois de criar uma voz, transmita o `id` (`voice_...`) dela para a API Interactions
para gerar fala:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "annotations": [{
                "type": "speech_metadata",
                "style": "reflective and awe-inspired",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": created_voice.id},
        ]
    },
)

with open("designed_voice.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash-tts",
  input: [{
    type: "user_input",
    content: [{
      type: "text",
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      annotations: [{
        type: "speech_metadata",
        style: "reflective and awe-inspired",
      }],
    }],
  }],
  response_format: { type: "audio" },
  generation_config: {
    speech_config: [
      { voice: createdVoice.id },
    ],
  },
});

fs.writeFileSync("designed_voice.wav", Buffer.from(interaction.output_audio.data, "base64"));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "annotations": [{
          "type": "speech_metadata",
          "style": "reflective and awe-inspired"
        }]
      }]
    }],
    "response_format": {"type": "audio"},
    "generation_config": {
      "speech_config": [
        {"voice": "voice_YOUR_DESIGNED_VOICE_ID"}
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

## Gerenciar suas vozes

É possível listar, filtrar, inspecionar e excluir as vozes armazenadas a qualquer momento usando
a API Voices. Consulte
[Biblioteca de vozes estendida e filtragem](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br#voice-library)
para conferir todos os parâmetros de filtro.

- **Limites de armazenamento e TTL**:as vozes com estado (`store=True`, compartilhadas entre vozes
  solicitadas e replicadas) têm um limite de **200 vozes por projeto**
  e um **TTL de um ano** (tempo de vida).
- **Disponibilidade do `sample_audio`**:`voices.create()` (`CreateVoice`) e `voices.get()` (`GetVoice`) preenchem `sample_audio` (`mime_type:
  "audio/wav"`, `data` codificado em base64) para vozes `"prompted"`. Para manter
  a lista leve, `voices.list()` (`ListVoices`) omite `sample_audio`
  (e `sample_audio` não é definido para vozes `"replicated"` e `"prebuilt"`).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Práticas recomendadas para comandos no design de voz

- **Coloque traços vocais permanentes no design de voz, não em `style`**:defina características imutáveis, como idade, gênero, timbre, textura vocal e sotaque regional, ao criar a voz em `voices.create`.
- **Reserve `speech_metadata.style` para emoções situacionais**:depois de criar sua voz personalizada, use comandos curtos de `style` (por exemplo, `"whispered urgently"` ou `"cheerful and energetic"`) para direcionar a navegação guiada sem alterar a identidade principal do falante.
- **Seja específico e conciso**:uma descrição clara de uma ou duas frases (como *"Uma locutora esportiva enérgica e dinâmica na casa dos 30 anos com um leve sotaque do meio-oeste"*) produz resultados mais limpos e consistentes do que parágrafos contraditórios ou muito longos.

## A seguir

- Saiba como replicar a voz de um falante em
  [Replicação de voz](https://ai.google.dev/gemini-api/docs/voice-replication?hl=pt-br).
- Confira o estilo no nível da vez, tags inline e diálogo com vários locutores no [guia da conversão de texto em voz](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-24 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-24 UTC."],[],[]]
