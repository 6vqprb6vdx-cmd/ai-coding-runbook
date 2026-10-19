---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-BR
fetched_at: 2026-10-19T05:40:09.705957+00:00
title: "Gera\u00e7\u00e3o de convers\u00e3o de texto em voz (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

Envie comentários

# Geração de conversão de texto em voz (TTS)

A API Gemini pode transformar entradas de texto em áudio de um ou vários locutores usando os recursos de geração de conversão de texto em voz (TTS) do Gemini.
A geração de conversão de texto em voz é
*[controlável](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-br#controllable)*,
ou seja, é possível combinar metadados estruturados de turno (`speech_metadata`) e tags vocais
inline para orientar o *estilo*, o *sotaque*, o *ritmo* e o *tom* do áudio.

[Testar no Google AI Studio](https://aistudio.google.com/generate-speech?hl=pt-br)

A capacidade de TTS é diferente da geração de fala fornecida pela [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br), que foi projetada para áudio interativo e não estruturado, além de entradas e saídas multimodais. Enquanto a API Live se destaca
em contextos de conversação dinâmicos, a TTS pela API Gemini
é adaptada para cenários que exigem a leitura exata de textos com controle
detalhado sobre o estilo e o som, como a geração de podcasts ou audiolivros.

Este guia mostra como gerar áudio de uma ou várias pessoas com base em texto usando o [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=pt-br) (`gemini-3.8-flash-tts`) e o [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=pt-br) (`gemini-3.8-flash-lite-tts`).

## Antes de começar

Use um modelo do Gemini TTS listado na seção
[Modelos compatíveis](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-br#supported-models). Para ter os melhores resultados, consulte [Quando usar qual modelo](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-br#when-to-use-which-model) para selecionar o melhor modelo para sua carga de trabalho.

Talvez seja útil [testar os modelos de TTS do Gemini no AI Studio](https://aistudio.google.com/generate-speech?hl=pt-br) antes de começar a criar.

## TTS de um único locutor

Para converter texto em áudio de um único locutor com os modelos de TTS do Gemini 3.8, transmita a
transcrição literal em `parts[].text`, anexe o estilo de turno em
`parts[].speech_metadata` e configure sua voz em
`speechConfig.voiceConfig`. É possível transmitir um nome de voz predefinido, um ID da biblioteca de voz estendida, um ID de [design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br) personalizado (`voice_...`) ou um ID de [replicação de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=pt-br) (`voice_...` ou `voicekey_...` sem estado opcional).

Este exemplo salva o áudio de saída do modelo em um arquivo WAV:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.wav
```

## TTS com vários locutores

Para diálogos com vários locutores, configure dois locutores em
`multiSpeakerVoiceConfig.speakerVoiceConfigs` usando `prebuiltVoiceConfig` e
transmita cada turno de diálogo como um `part` separado com `speech_metadata` especificando
`speaker` e `style` opcional no nível do turno:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [
            {
                "text": "How's it going today Jane?",
                "speech_metadata": {
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                },
            },
            {
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "speech_metadata": {
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                },
            },
        ],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "multi_speaker_voice_config": {
                "speaker_voice_configs": [
                    {
                        "speaker": "Joe",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Puck"}
                        },
                    },
                    {
                        "speaker": "Jane",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Kore"}
                        },
                    },
                ]
            }
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [
            {
               text: "How's it going today Jane?",
               speechMetadata: {
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               },
            },
            {
               text: 'Not too bad, how about you? Ready to test these new voices?',
               speechMetadata: {
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               },
            },
         ],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            multiSpeakerVoiceConfig: {
               speakerVoiceConfigs: [
                  {
                     speaker: 'Joe',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Puck' },
                     },
                  },
                  {
                     speaker: 'Jane',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Kore' },
                     },
                  },
               ],
            },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {
          "text": "How'\''s it going today Jane?",
          "speech_metadata": {
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }
        },
        {
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "speech_metadata": {
            "speaker": "Jane",
            "style": "calm and relaxed"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {
              "speaker": "Joe",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Puck" }
              }
            },
            {
              "speaker": "Jane",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Kore" }
              }
            }
          ]
        }
      }
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
      base64 --decode > out.wav
```

## Controlar o estilo de fala com metadados e tags

O Gemini 3.8 TTS trata o campo `text` estritamente como uma transcrição literal. Para
controlar a entrega sem que as instruções de palco sejam lidas em voz alta, divida as
instruções por escopo:

- **Entrega sustentada no nível da fala (`speech_metadata.style`)**: coloque emoções,
  estilo de entrega, prosódia, ritmo e volume que se aplicam a uma fala inteira
  em `speech_metadata.style` (por exemplo, `"style": "whispered urgently"`,
  `"style": "out of breath"` ou `"style": "warm and enthusiastic"`).
- **Eventos pontuais (tags inline)**: coloque pausas ou explosões vocais momentâneas que não sejam de fala diretamente na transcrição usando colchetes angulares (por exemplo, `"Wait... <short pause> did you hear that? <sigh>"` ou `"Excuse me <cough> as I was saying..."`).

Consulte o
[Guia de comandos](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-br#prompting-guide)
para conferir as práticas recomendadas abrangentes.

## Opções de voz

O Gemini 3.8 TTS oferece quatro maneiras de selecionar ou criar vozes:

1. **Vozes de estúdio predefinidas**:30 vozes selecionadas listadas na tabela a seguir.
2. **Biblioteca de voz estendida**:centenas de vozes adicionais em vários idiomas,
   sotaques e arquétipos de personagens acessíveis usando `client.voices.list()`
   (`GET /v1beta/voices`).
3. **[Design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br)**:gere
   uma persona vocal personalizada com base em uma descrição em linguagem natural no
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=pt-br) ou usando
   `POST /v1beta/voices` (`type="prompted"`, que retorna um ID
   `voice_...` persistente e uma prévia em WAV `sample_audio` em `CreateVoice` e
   `GetVoice`).
4. **[Replicação de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=pt-br)**:replique a voz de um falante usando áudio de referência e consentimento no
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=pt-br) ou usando
   `POST /v1beta/voices` (`type="replicated"`, `store=True` persistente por
   padrão ou `store=False` sem estado opcional).

### Limites e TTL de voz personalizada

| Tipo de voz | Modo de armazenamento | Cota / limite | Retenção (TTL) |
| --- | --- | --- | --- |
| **Vozes com estado** (`voice_...`, com comando ou replicadas) | `store=True` | **200 vozes por projeto** (compartilhadas entre vozes replicadas e com comandos) | **1 ano desde o último uso\*** |
| **Chaves de voz sem estado** (`voicekey_...`, replicadas) | `store=False` | Gerenciada pelo cliente | **7 dias** |

\* **Extensão do TTL**:a janela de retenção de um ano é redefinida sempre que a voz é usada ativamente (seja para sintetizar a fala ou como base para remixagem). As vozes sem atividade por 1 ano são excluídas automaticamente.

### Vozes predefinidas

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Brilhante* | **Puck** -- *Upbeat* | **Charon**: *informativa* |
| **Kore**: *firme* | **Fenrir**: *Excitável* | **Leda** -- *Jovem* |
| **Orus** -- *Firm* | **Aoede**: *Breezy* | **Callirrhoe** -- *Tranquila* |
| **Autonoe** -- *Brilhante* | **Enceladus**: *Breathy* | **Iapetus**: *Limpar* |
| **Umbriel**: *tranquilo* | **Algieba**: *Suave* | **Despina** -- *Suave* |
| **Erinome**: *Limpar* | **Algenib** -- *Gravelly* | **Rasalgethi** — *Informativa* |
| **Laomedeia** — *Upbeat* | **Achernar**: *Soft* | **Alnilam** -- *Firme* |
| **Schedar** -- *Even* | **Gacrux**: *Adulto* | **Pulcherrima** -- *Avançar* |
| **Achird**: *Friendly* | **Zubenelgenubi** -- *Casual* | **Vindemiatrix** -- *Gentle* |
| **Sadachbia** -- *Lively* | **Sadaltager** — *Conhecimento* | **Sulafat**: *quente* |

### Biblioteca de vozes estendida e filtragem

Além das 30 vozes de estúdio em destaque na tabela anterior, a **Biblioteca de Vozes Estendida** oferece centenas de outras vozes em vários idiomas, sotaques regionais, personas de personagens e domínios. Você pode navegar, filtrar e testar a Biblioteca de vozes completa de forma interativa no [Google AI Studio](https://aistudio.google.com/generate-speech?hl=pt-br) ou consultar programaticamente usando `client.voices.list()` (`GET /v1beta/voices`, usando `google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

O `ListVoices` retorna suas vozes personalizadas armazenadas (ordenadas da mais recente para a mais antiga), seguidas
pelas vozes do catálogo pré-criado que correspondem aos seus critérios de filtro. Quando vários valores são transmitidos para um filtro de lista, as vozes que correspondem a **qualquer** valor nesse filtro são retornadas (`OR`), enquanto parâmetros de filtro distintos se combinam com `AND`:

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| `language_code` | `list[str]` | Tags de idioma BCP-47 (por exemplo, `["en-US", "en-GB"]`). Correspondência exata que não diferencia maiúsculas de minúsculas. |
| `region_code` | `list[str]` | Códigos de região ISO 3166-1 alfa-2 ou UN M.49 (por exemplo, `["US", "GB"]`). |
| `accent` | `list[str]` | Descritores de sotaque regional (por exemplo, `["American", "British"]`). |
| `gender` | `list[str]` | Apresentação de gênero percebida (`"female"`, `"male"` ou `"neutral"`). |
| `pitch` | `list[str]` | Classificação de tom vocal (`"low"`, `"medium"` ou `"high"`). |
| `persona` | `list[str]` | Persona vocal ou arquétipo de personagem (por exemplo, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` em REST) | `list[str]` | Domínio de uso ideal (por exemplo, `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` em Python) | `list[str]` | Filtre por fonte de voz: `"prebuilt"`, `"prompted"` ([Design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br)) ou `"replicated"` ([Replicação de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=pt-br)). |
| `search` | `str` | A pesquisa de substring de texto livre fez uma correspondência não diferencia maiúsculas de minúsculas com `display_name` e `description`. |
| `page_size` | `int` | Número máximo de vozes retornadas por página (padrão `50`, máximo `1000`). |
| `page_token` | `str` | Token de `response.next_page_token` para buscar a próxima página de resultados. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## Idiomas compatíveis

Os modelos de TTS detectam o idioma de entrada automaticamente.
O [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=pt-br)
(`gemini-3.8-flash-tts`) oferece suporte a **mais de 130 idiomas**, e o
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=pt-br)
(`gemini-3.8-flash-lite-tts`) oferece suporte a **mais de 100 idiomas**:

| Idioma | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Achinês (alfabeto árabe) | ✔️ | ✔️ |
| Africâner | ✔️ | ✔️ |
| Akan | ✔️ | ✔️ |
| Amárico | ✔️ | ✔️ |
| Armênio | ✔️ | ✔️ |
| Assamês | ✔️ | ✔️ |
| Awadhi | ✔️ | ✔️ |
| Balinês | ✔️ | ✔️ |
| Bengali | ✔️ | ✔️ |
| Banjarês (alfabeto árabe) | ✔️ | — |
| Banjar (alfabeto latino) | ✔️ | ✔️ |
| Bashkir | ✔️ | — |
| Basco | ✔️ | ✔️ |
| Bielorrusso | ✔️ | ✔️ |
| Bemba | ✔️ | — |
| Boiapuri | ✔️ | ✔️ |
| Bósnio | ✔️ | ✔️ |
| Buguinês | ✔️ | ✔️ |
| Búlgaro | ✔️ | ✔️ |
| Birmanês | ✔️ | — |
| Cantonês | ✔️ | ✔️ |
| Catalão | ✔️ | ✔️ |
| Cebuano | ✔️ | ✔️ |
| Sorâni | ✔️ | ✔️ |
| Chhattisgarhi | ✔️ | ✔️ |
| Chinês (script Hans) | ✔️ | ✔️ |
| Chinês (script Hant) | ✔️ | ✔️ |
| Tártaro da Crimeia | ✔️ | — |
| Croata | ✔️ | ✔️ |
| Tcheco | ✔️ | ✔️ |
| Dinamarquês | ✔️ | ✔️ |
| Holandês | ✔️ | ✔️ |
| Diúla | ✔️ | — |
| Dzonga | ✔️ | — |
| Árabe egípcio | ✔️ | ✔️ |
| Inglês | ✔️ | ✔️ |
| Estoniano | ✔️ | ✔️ |
| Filipino | ✔️ | ✔️ |
| Finlandês | ✔️ | — |
| Francês | ✔️ | ✔️ |
| Galego | ✔️ | ✔️ |
| Ganda | ✔️ | ✔️ |
| Georgiano | ✔️ | ✔️ |
| Alemão | ✔️ | ✔️ |
| Grego | ✔️ | ✔️ |
| Guarani | ✔️ | — |
| Gujarati | ✔️ | ✔️ |
| Crioulo haitiano | ✔️ | ✔️ |
| Mongol de Halh | ✔️ | ✔️ |
| Hauçá | ✔️ | ✔️ |
| Hebraico | ✔️ | ✔️ |
| Hindi | ✔️ | ✔️ |
| Húngaro | ✔️ | ✔️ |
| Islandês | ✔️ | ✔️ |
| Igbo | ✔️ | — |
| Iloko | ✔️ | ✔️ |
| Indonésio | ✔️ | ✔️ |
| Persa iraniano | ✔️ | ✔️ |
| Italiano | ✔️ | ✔️ |
| Japonês | ✔️ | ✔️ |
| Javanês | ✔️ | ✔️ |
| Kabyle | ✔️ | — |
| Kamba | ✔️ | ✔️ |
| Canarês | ✔️ | ✔️ |
| Caxemira (alfabeto árabe) | ✔️ | ✔️ |
| Caxemira (escrita devanágari) | ✔️ | ✔️ |
| Cazaque | ✔️ | ✔️ |
| Khmer | ✔️ | ✔️ |
| Kikuyu | ✔️ | ✔️ |
| Quiniaruanda | ✔️ | ✔️ |
| Quicongo | ✔️ | ✔️ |
| Coreano | ✔️ | ✔️ |
| Quirguiz | ✔️ | ✔️ |
| Laosiano | ✔️ | ✔️ |
| Latgaliano | ✔️ | — |
| Lingala | ✔️ | ✔️ |
| Lituano | ✔️ | — |
| Luxemburguês | ✔️ | — |
| Macedônio | ✔️ | ✔️ |
| Magahi | ✔️ | ✔️ |
| Maithili | ✔️ | ✔️ |
| Malaiala | ✔️ | ✔️ |
| Maltês | ✔️ | ✔️ |
| Manipuri | ✔️ | ✔️ |
| Marati | ✔️ | ✔️ |
| Minangkabau (alfabeto árabe) | ✔️ | ✔️ |
| Minangkabau (alfabeto latino) | ✔️ | — |
| Mizo | ✔️ | ✔️ |
| Nepalês (idioma individual) | ✔️ | ✔️ |
| Fulfulde nigeriano | ✔️ | ✔️ |
| Azerbaijano do norte | ✔️ | ✔️ |
| Soto do norte | ✔️ | ✔️ |
| Uzbeque do norte | ✔️ | ✔️ |
| Bokmål norueguês | ✔️ | ✔️ |
| Norueguês (Nynorsk) | ✔️ | ✔️ |
| Nianja | ✔️ | ✔️ |
| Occitânico | ✔️ | — |
| Oriá (idioma individual) | ✔️ | ✔️ |
| Língua pangasiana | ✔️ | — |
| Persa (Afeganistão) | ✔️ | ✔️ |
| Polonês | ✔️ | ✔️ |
| Português | ✔️ | ✔️ |
| Punjabi | ✔️ | ✔️ |
| Romeno | ✔️ | ✔️ |
| Russo | ✔️ | ✔️ |
| Santali | ✔️ | ✔️ |
| Sérvio | ✔️ | ✔️ |
| Sindi | ✔️ | — |
| Cingalês | ✔️ | ✔️ |
| Eslovaco | ✔️ | ✔️ |
| Esloveno | ✔️ | — |
| Somali | ✔️ | — |
| Azerbaijão do Sul | ✔️ | ✔️ |
| Pashto do sul | ✔️ | ✔️ |
| Soto do sul | ✔️ | — |
| Espanhol | ✔️ | ✔️ |
| Árabe padrão (alfabeto árabe) | ✔️ | ✔️ |
| Árabe padrão (alfabeto latino) | ✔️ | ✔️ |
| Letão padrão | ✔️ | ✔️ |
| Malaio padrão | ✔️ | ✔️ |
| Suaíli (idioma individual) | ✔️ | — |
| Swati | ✔️ | — |
| Sueco | ✔️ | — |
| Tadjique | ✔️ | — |
| Tâmil | ✔️ | ✔️ |
| Télugo | ✔️ | ✔️ |
| Tailandês | ✔️ | — |
| Tigrínia | ✔️ | — |
| Albanês Tosk | ✔️ | — |
| Turco | ✔️ | ✔️ |
| Uigur | ✔️ | — |
| Vietnamita | ✔️ | ✔️ |

## Modelos compatíveis

| Modelo | Falante único | Vários falantes | Design de voz | Replicação de voz |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=pt-br) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=pt-br) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Pré-lançamento do Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=pt-br) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=pt-br) | ✔️ | ✔️ | — | — |

### Quando usar cada modelo

Os dois modelos de TTS do Gemini 3.8 compartilham o mesmo esquema de API e formato de comando,
permitindo que você alterne entre eles com uma única mudança de parâmetro:

- **Use o [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=pt-br)
  (`gemini-3.8-flash-tts`)** quando a fidelidade acústica máxima, a atuação com nuances
  e o controle expressivo forem prioridades. Ele é ideal para trabalhos criativos de nível de estúdio, diálogos complexos com vários falantes, tags de explosão vocal pesadas, pronúncias difíceis, dialetos regionais ou minoritários e narrações longas que exigem uma voz sólida e estabilidade de tom de ambiente.
- **Use o [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=pt-br)
  (`gemini-3.8-flash-lite-tts`)** como uma substituição rápida e econômica
  para o `gemini-3.1-flash-tts-preview`. Ele é otimizado para produção em massa de alto volume, cascatas de agentes de voz conversacionais, recursos de leitura em voz alta, replicação de voz confiável e fala cotidiana de um único falante nos principais idiomas.

### Guia de migração

Ao fazer upgrade de modelos de pré-lançamento anteriores (`gemini-3.1-flash-tts-preview` ou
`gemini-2.5-pro-preview-tts`) para o Gemini 3.8 TTS (`gemini-3.8-flash-tts` ou
`gemini-3.8-flash-lite-tts`), confira estas cinco mudanças principais:

1. **Separe o estilo da transcrição**:mova instruções de atuação, tom, prosódia e ritmo (como `"whispering"`, `"out of breath"` ou `"speaking slowly"`) do texto simples para `speech_metadata.style`.
   Mantenha `text` estritamente como a transcrição literal mais as tags vocais inline.
2. **Crie personas com antecedência usando o design de voz**:substitua blocos `"Audio Profile"` ou `"Director's Notes"` de vários parágrafos por uma voz personalizada criada no [design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br) e, em seguida, use esse ID `voice_...` nas solicitações de TTS com strings `style` mínimas ou vazias.
3. **Use turnos de diálogo estruturados**:para diálogos com vários participantes, transmita um
   `part` por turno de fala com `speech_metadata.speaker` em vez de incorporar
   prefixos `Speaker: ...` em um único bloco de texto.
4. **Use colchetes angulares para tags vocais inline**:use colchetes angulares (`<laugh>`, `<sigh>`, `<cough>`, `<breath>`, `<short pause>`) para vocalizações e pausas humanas em um momento específico. Evite tags de efeitos sonoros não vocais (como
   aplausos ou batidas).
5. **Considere a saída WAV (`AUDIO_WAV`) padrão em solicitações unárias**:ao contrário de
   `gemini-3.1-flash-tts-preview` (que retornava PCM bruto sem cabeçalho
   `AUDIO_L16` por padrão), os modelos de TTS do Gemini 3.8 retornam áudio **WAV
   (`AUDIO_WAV`)** completo com um cabeçalho RIFF (24 kHz, mono, PCM de 16 bits) em
   solicitações unárias:
   - Se o código anteriormente encapsulava bytes PCM brutos em um cabeçalho WAV (por exemplo, usando o módulo `wave` do Python ou o pacote `wav` do Node), remova o wrapper de cabeçalho manual e grave os bytes de áudio decodificados diretamente em um arquivo `.wav`.
   - Se o pipeline atual exigir áudio PCM bruto sem cabeçalho, mu-law ou A-law, defina explicitamente `generationConfig.responseFormat.audio.mimeType` como `"AUDIO_L16"`, `"AUDIO_MULAW"` ou `"AUDIO_ALAW"` usando a API REST (por exemplo, `{"responseFormat": {"audio": {"mimeType": "AUDIO_L16"}}}` em `generateContent`; substituições personalizadas de `responseFormat` em `generateContent` são compatíveis com a API REST, enquanto o suporte do SDK Python e SDK para JavaScript para `response_format` em `GenerateContentConfig` está pendente ou use `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` na API Interactions). Consulte
     [Formatos de saída de áudio](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-br#audio-output-formats).

## Guia para a criação de comandos

Os modelos de TTS do Gemini 3.8 tratam o texto de entrada estritamente como uma **transcrição literal**.
Ao contrário dos modelos de prévia anteriores, em que as instruções de palco eram incorporadas em texto simples,
o Gemini 3.8 TTS separa as instruções de turno sustentado (`speech_metadata`)
das tags vocais inline pontuais.

### Campo de estilo x tags inline

Divida as instruções de performance por escopo:

- **Entrega no nível da fala (`speech_metadata.style`)**: coloque atributos de entrega
  sustentados, como emoção, prosódia, ritmo geral ou estilo de entrega (como
  `"whispering"`, `"out of breath"`, `"muttering"` ou `"sarcastic"`), no campo
  `style` de `speech_metadata`. Para criar um personagem e uma performance estáveis em todas as interações, crie a persona antecipadamente em [Design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br) e use `style` apenas para ajustes opcionais no nível da interação.
- **Eventos pontuais (tags inline)**: coloque pausas, respirações ou explosões vocais momentâneas não relacionadas à fala inline na transcrição usando colchetes angulares (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`). Use colchetes angulares (`<...>`) para ter a melhor qualidade do áudio e use vocalizações humanas em vez de efeitos sonoros não vocais.

| Escopo | Onde colocar | Exemplos |
| --- | --- | --- |
| **Nível de turno** (sustentado durante o turno) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **Pontual** (ocorre em uma palavra específica) | Inline em `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Ritmo e pausas

É possível controlar o ritmo e o silêncio em três níveis de granularidade:

- **Pontuação e reticências**:use vírgulas, travessões (`--`) e reticências (`...`)
  para hesitações naturais na conversa.
- **Tags de pausa inline**:insira `<short pause>` ou `<long pause>` nos pontos exatos
  do script em que o locutor deve fazer uma pausa:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Ritmo no nível da fala**:defina `"style": "speaking rapidly"` ou
  `"style": "speaking slowly"` em `speech_metadata` para controlar a taxa de fala
  em toda a fala.

### Prosódia e tom

Use **`speech_metadata.style`** para controlar a prosódia, o tom e a inflexão em
uma fala (por exemplo, `"style": "high pitch, cheerful and excited inflection"` ou
`"style": "monotone and flat"`). Se a emoção ou a prosódia mudar no meio do diálogo,
divida o script em falas separadas com valores `style` distintos para cada uma.

### Ênfase

Use letras maiúsculas em palavras específicas na transcrição, combinadas com pontuação e tags vocais inline, para colocar ênfase vocal natural em palavras-chave:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Sons não verbais e explosões vocais

Coloque vocalizações humanas não verbais inline usando colchetes angulares (`<...>`) no
ponto exato em que o som deve ocorrer. As tags vocais recomendadas incluem:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>` / `<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>` / `<laughter>` | `<moan>` | `<pant>` | `<pff>` / `<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>` / `<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>` / `<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### Backchannels e fala sobreposta

Em diálogos com vários falantes, envolva as reações do listener com caracteres de barra vertical
(`|reaction|`) dentro da vez de um falante para criar backchannels naturais ou
fala sobreposta sem interromper uma vez separada por reação.

- **Trocas curtas de canal de retorno**:reações breves do ouvinte (`|oh hmm|`,
  `|oh really?|`, `|absolutely|`) durante a fala do apresentador ativo:
  - **Turno 1 (falante A)**: `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Turno 2 (Speaker B):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Turno 3 (Locutor A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Fala sobreposta e intercalada**:use vários segmentos de barra vertical para
  simular fala simultânea ou intercalada entre dois falantes (funciona melhor
  com `gemini-3.8-flash-tts`):
  - **Contagem regressiva/refrão simultâneo**:`"Let's surprise him on three |ok| ready?"` seguido de `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Sobreposição total de locutores**:`"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Consistência entre gerações e o que evitar

Siga estas diretrizes para manter a identidade vocal estável em todas as interações:

- **Crie personas com antecedência no design de voz em vez de usar blocos de estilo longos**:parágrafos longos de `"Audio Profile"` e listas com vários marcadores de `"Director's Notes"`
  transferidos de modelos anteriores são a causa mais comum de desvio de voz.
  Use essa mesma intuição criativa no
  [design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br) para gerar uma
  persona personalizada persistente do `voice_...` e, em seguida, use esse ID de voz nas
  chamadas de TTS.
- **Confie na referência de voz para estabilidade (omita as metainstruções)**:
  os modelos TTS do Gemini 3.8 são treinados para se ancorar primeiro na referência de áudio.
  Não inclua instruções que digam ao modelo para manter a voz estável (como
  `"do not switch speaker identity"` ou `"maintain identical timbre"`). O texto extra
  do comando aumenta o desvio. Remova instruções de estilo desnecessárias e deixe o
  modelo variar naturalmente em torno do ponto estável fornecido pela referência de voz.
- **Não tente mudar características imutáveis do locutor em `style`**:evite colocar
  idade, gênero, nomes ou mudanças permanentes de sotaque em `speech_metadata.style`.
  Em vez disso, escolha uma voz regional na Biblioteca de vozes avançada ou crie uma com [Design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br).

### Fluxo de trabalho recomendado

1. **Crie o personagem uma vez**:crie seu personagem no
   [Design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br) ou selecione uma
   voz regional da biblioteca de vozes estendida que corresponda ao idioma-alvo
   e à persona.
2. **Escreva transcrições faladas naturais com disfluências**:para máxima
   naturalidade, escreva o `text` como uma transcrição falada real, incluindo disfluências
   e hesitações naturais da conversa (por exemplo,
   `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Teste primeiro a TTS simples**:sintetize sua transcrição com um campo `style`
   vazio primeiro. A maioria das solicitações não precisa de nenhuma instrução `style`.
4. **Adicione comandos curtos de `style` apenas para ajustes**:adicione uma string de `style` concisa
   (como `"casual, friendly"` ou `"muttering, then reassuring"`) apenas para
   as falas que precisam de um ajuste de entrega específico e reutilize essa string curta
   exata em todas as falas quando quiser uma linha de base consistente.

### Diálogo em várias etapas e agentes de voz

Ao criar agentes de voz de conversação em tempo real ou aplicativos de várias rodadas:

- Faça **uma chamada de TTS por vez** à medida que os blocos de texto do LLM chegam.
- Permita que o `voice` configurado (`voice_...` pré-criado, projetado ou `voice_...` / `voicekey_...` replicado) carregue a identidade do falante em todas as interações. Nunca reenvie uma persona de personagem longa em cada interação.
- Deixe o campo `style` por turno vazio ou envie uma string constante curta
  (como `"casual, friendly"`) para toda a conversa.
- Divida respostas longas do agente em turnos mais curtos em vez de usar comandos de estilo mais fortes.

## Geração de fala em streaming

É possível transmitir o áudio gerado enquanto ele é sintetizado pelo modelo. Ao contrário
das solicitações unárias (que retornam um arquivo WAV completo com um cabeçalho RIFF),
**as solicitações de streaming retornam blocos PCM lineares de 16 bits assinados sem cabeçalho (`AUDIO_L16` / `audio/L16;codec=pcm;rate=24000`, 24 kHz, mono) por
padrão** para que os blocos de áudio possam ser reproduzidos ou concatenados continuamente sem
cabeçalhos de contêiner:

### Python

```
from google import genai

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

for chunk in response_stream:
    try:
        data = chunk.candidates[0].content.parts[0].inline_data.data
        # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
    except (IndexError, AttributeError):
        pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }'
```

## Formatos de saída de áudio

Os modelos de TTS do Gemini 3.8 usam formatos de áudio padrão diferentes, dependendo se a solicitação é unária ou de streaming:

- **Solicitações unárias (`models.generate_content`)**: retornam áudio **WAV
  (`AUDIO_WAV`)** completo com um cabeçalho RIFF (24 kHz, mono, PCM little-endian de 16 bits com sinal). É possível gravar os bytes de áudio decodificados diretamente em um arquivo `.wav` sem adicionar manualmente um contêiner WAV.
- **Solicitações de streaming (`models.generate_content_stream` / `streamGenerateContent`)**:
  retornam blocos **PCM linear bruto sem cabeçalho (`AUDIO_L16`)** (24 kHz, mono,
  PCM little-endian assinado de 16 bits) por padrão para que os blocos possam ser transmitidos ou
  concatenados continuamente sem cabeçalhos de contêiner em cada bloco.

É possível substituir a codificação e a taxa de amostragem do áudio de saída usando
`generationConfig.responseFormat.audio`:

| Valor de `mimeType` | Formato | Descrição |
| --- | --- | --- |
| `"AUDIO_WAV"` *(padrão unário)* | WAV (`audio/wav`) | Arquivo WAV completo com um cabeçalho RIFF (24 kHz, mono, PCM de 16 bits). |
| `"AUDIO_L16"` *(padrão de streaming)* | PCM linear (`audio/l16`) | PCM linear de 16 bits sem cabeçalho, bruto, assinado e little-endian. Ideal para streaming, pipelines de áudio personalizados ou concatenação de clipes multiturno. |
| `"AUDIO_MULAW"` | μ-law (`audio/basic` / `audio/mulaw`) | Áudio compactado com a lei μ do G.711. Comumente usado na telefonia norte-americana e japonesa (8 kHz). |
| `"AUDIO_ALAW"` | Lei A (`audio/alaw`) | Áudio compactado G.711 A-law. Comumente usado em telefonia europeia e internacional (8 kHz). |

Também é possível especificar `sampleRate` (por exemplo, `24000`, `16000` ou
`8000` Hz; o padrão é `24000` Hz).

O exemplo de REST a seguir solicita PCM bruto de 16 bits sem cabeçalho (`AUDIO_L16`) a
24 kHz:

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "responseFormat": {
            "audio": {
              "mimeType": "AUDIO_L16",
              "sampleRate": 24000
            }
          },
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.pcm
```

## Limitações

- Os modelos de TTS aceitam entradas somente de texto e geram saídas somente de áudio.
- A geração com vários locutores em uma única solicitação (`multiSpeakerVoiceConfig`) aceita até dois locutores usando vozes pré-criadas. Para combinar vozes personalizadas
  (`voice_...`) ou replicadas (`voice_...` / `voicekey_...`) em
  diálogos com vários personagens, sintetize a fala de cada falante individualmente.
  Como as solicitações unárias retornam `audio/wav` com um cabeçalho RIFF de 44 bytes por
  padrão, solicite PCM bruto (`AUDIO_L16`) ou remova o cabeçalho WAV de cada
  turno antes de concatenar os frames de áudio PCM de 24 kHz.
- **Limites de armazenamento de voz personalizada e TTL:**
  - **Vozes com estado (`store=True`, solicitadas ou replicadas)**: máximo de **200 vozes por projeto** com um **TTL de um ano** (time-to-live).
  - **Chaves de voz sem estado (`store=False`, `voicekey_...`)**: **TTL de sete dias**
    (time to live).
- Consulte a seção
  [Idiomas disponíveis](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-br#languages)
  para saber mais sobre a cobertura de idiomas.

## A seguir

- Crie personas vocais personalizadas usando linguagem natural com o
  [Design de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=pt-br).
- Replique a voz de um locutor na
  [Replicação de voz](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=pt-br).
- Compare as especificações dos modelos nas páginas [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=pt-br) e [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=pt-br).
- Conheça o áudio bidirecional interativo com a
  [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-12 UTC."],[],[]]
