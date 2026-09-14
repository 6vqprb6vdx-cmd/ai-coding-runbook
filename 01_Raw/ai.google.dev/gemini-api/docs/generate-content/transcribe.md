---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=pt-BR
fetched_at: 2026-09-14T05:41:38.225503+00:00
title: "Transcri\u00e7\u00e3o de \u00e1udio \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

Envie comentários

# Transcrição de áudio

A API Gemini converte a fala em arquivos de áudio em texto usando o modelo Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). Com base nos recursos de compreensão de áudio do Gemini, ela oferece transcrição precisa com identificação automática de idioma, diarização de falantes, carimbos de data/hora no nível da palavra e dicas de vocabulário personalizadas. Ele também oferece um modo de [transcrição inteligente](#transcription-modes) com remoção de disfluências e formatação inteligente.

Para transcrever um arquivo de áudio, faça upload dele e transmita para `gemini-3.5-transcribe`:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const audioFile = await ai.files.upload({
  file: "path/to/sample.mp3",
  mimeType: "audio/mp3",
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
});

console.log(response.text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ]
  }'
```

## Visão geral

O Gemini 3.5 Transcribe é otimizado para tarefas de conversão de voz em texto. Ele lida com diversos sotaques, ruídos de fundo e conversas em vários idiomas.

As principais capacidades incluem:

- **Reconhecimento automático de fala (ASR)**: detecta automaticamente idiomas em mais de [85 localidades](#supported-languages). Lida com a troca de código intrafrasal e interfrasal sem configuração manual.
- **Vocabulário personalizado**:favorece o reconhecimento de termos específicos do domínio, acrônimos e nomes próprios ao transmitir até 1.000 frases.
- **Diarização de locutor**:distingue entre vários locutores e atribui segmentos falados a identificadores distintos.
- **Carimbos de data/hora no nível da palavra**:geram ajustes de horário de início e término precisos para cada palavra reconhecida.
- **Transcrição inteligente**:limpa disfluências, palavras desnecessárias, repetições e aplica formatação estruturada.
- **Formatação e normalização**:aplica o uso de maiúsculas e minúsculas, pontuação e normalização de texto inversa, como converter "vinte e seis milhões de dólares" em "US$ 26 milhões".

Para raciocínio geral sobre áudio ou respostas a perguntas sobre conteúdo de áudio, use o [Entendimento de áudio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=pt-br). Para síntese de áudio de conversão de texto em voz, use a [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-br).

## Detecção e dicas de idioma

Por padrão, o modelo detecta o idioma falado automaticamente. Ele alterna entre idiomas dinamicamente quando os falantes mudam de código.

Para usar a detecção automática, omita `language_codes` ou forneça uma lista vazia:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            language_codes=[],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      languageCodes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "languageCodes": []
      }
    }
  }'
```

Se você souber o idioma com antecedência, especifique os códigos de idioma BCP-47 em `language_codes` para melhorar a precisão da transcrição. Consulte [Idiomas aceitos](#supported-languages):

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    languageCodes: ["es-ES"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "languageCodes": ["es-ES"]
    }
  }
}
```

## Vocabulário personalizado

Você pode orientar o modelo de fala para palavras incomuns, jargão técnico, nomes de marcas ou substantivos próprios. Forneça até 1.000 termos na matriz `custom_vocabulary`. Os melhores resultados geralmente são alcançados com até 100 termos:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      customVocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "customVocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## Diarização de locutor

A diarização de locutor identifica vozes diferentes na gravação e marca cada segmento com um identificador de locutor, como `spk_1` ou `spk_2`. É possível usar até oito alto-falantes. A atribuição para três ou mais alto-falantes é experimental.

Para ativar a diarização, defina `diarization` como `True`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            diarization=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      diarization: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "diarization": true
      }
    }
  }'
```

## Carimbos de data/hora no nível da palavra

Os carimbos de data/hora no nível da palavra fornecem ajustes de início e término exatos para cada palavra reconhecida no fluxo de áudio.

Para ativar os carimbos de data/hora, defina `word_timestamp` como `True`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            word_timestamp=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      wordTimestamp: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "wordTimestamp": true
      }
    }
  }'
```

É possível combinar `diarization` e `word_timestamp` em uma única solicitação para receber identificadores de locutor e marcações de tempo de palavras:

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        diarization=True,
        word_timestamp=True,
        custom_vocabulary=["Gemini"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    diarization: true,
    wordTimestamp: true,
    customVocabulary: ["Gemini"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "diarization": true,
      "wordTimestamp": true,
      "customVocabulary": ["Gemini"]
    }
  }
}
```

## Modos de transcrição

O Gemini 3.5 Transcribe é compatível com dois modos de transcrição usando o parâmetro `mode`:

- **`VERBATIM` (padrão)**: retorna uma transcrição exata de tudo o que foi dito, preservando palavras de preenchimento ("hum", "ã", "tipo", "sabe"), repetições, pausas e falsos começos. Obrigatório ao usar carimbos de data/hora ou diarização de falantes.
- **`SMART` (Transcrição inteligente)**: otimiza a transcrição para leitura aplicando pós-processamento inteligente:
  - **Remoção de disfluências**: remove palavras de preenchimento, gaguejos e falsos inícios de conversa.
  - **Autocorreções inline**: resolvem correções faladas diretamente. Por exemplo, *"Vamos nos encontrar na terça-feira, na verdade não, na quarta-feira às duas"* se torna *"Vamos nos encontrar na quarta-feira às 14h"*.
  - **Formatação estruturada automática**: organiza automaticamente os pensamentos falados em parágrafos, listas numeradas, marcadores, datas, moedas e números formatados.
  - **Limpeza gramatical**: aplica pontuação natural, capitalização de frases e fluxo.

| Áudio falado | Saída `VERBATIM` | Saída `SMART` (transcrição inteligente) |
| --- | --- | --- |
| "Hum, então, para a reunião, acho que devemos convidar Alice e, não, Bob e Carol." | "Um so for the meeting I think we should uh invite Alice and wait no Bob and Carol." | "Para a reunião, acho que devemos convidar o Bob e a Carol." |
| "Primeiro item revisar orçamento segundo item finalizar cronograma terceiro item enviar resumo" | "primeiro item revisar orçamento segundo item finalizar linha do tempo terceiro item enviar resumo" | "1. Revisar o orçamento 2. Finalizar linha do tempo 3. Enviar resumo" |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            mode="SMART",
        )
    ),
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      mode: "SMART",
    },
  },
});
console.log(response.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "mode": "SMART"
      }
    }
  }'
```

## Analisando a saída da transcrição

O texto completo da transcrição é retornado em `response.text`.

Quando `word_timestamp` ou `diarization` está ativado, a API também retorna anotações detalhadas no nível da palavra e identificadores de locutor anexados às partes candidatas.

Veja como extrair e iterar carimbos de data/hora de palavras e turnos de falas:

### Python

```
def extract_word_transcriptions(response):
    words = []
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", []) or []:
            transcription = getattr(part, "audio_transcription", None)
            if transcription:
                speaker = getattr(transcription, "speaker_label", "")
                for word_info in getattr(transcription, "words", []) or []:
                    word = getattr(word_info, "word", "")
                    start = getattr(word_info, "start_offset", "")
                    end = getattr(word_info, "end_offset", "")
                    words.append({
                        "word": word,
                        "speaker": speaker,
                        "start_offset": start,
                        "end_offset": end,
                    })
    return words

words = extract_word_transcriptions(response)

for w in words:
    speaker = f"[{w['speaker']}] " if w["speaker"] else ""
    timing = f"({w['start_offset']} -> {w['end_offset']}) " if w["start_offset"] and w["end_offset"] else ""
    print(f"{speaker}{timing}{w['word']}")
```

### JavaScript

```
function extractWordTranscriptions(response) {
  const words = [];
  for (const candidate of response.candidates ?? []) {
    for (const part of candidate.content?.parts ?? []) {
      const transcription = part.audioTranscription;
      if (transcription) {
        const speaker = transcription.speakerLabel ?? "";
        for (const wordInfo of transcription.words ?? []) {
          words.push({
            word: wordInfo.word ?? "",
            speaker: speaker,
            startOffset: wordInfo.startOffset ?? "",
            endOffset: wordInfo.endOffset ?? "",
          });
        }
      }
    }
  }
  return words;
}

const words = extractWordTranscriptions(response);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.startOffset && w.endOffset) ? `(${w.startOffset} -> ${w.endOffset}) ` : "";
  console.log(`${speaker}${timing}${w.word}`);
}
```

### REST

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "audioTranscription": {
              "speakerLabel": "spk_1",
              "words": [
                {
                  "word": "Hello",
                  "startOffset": "0.100s",
                  "endOffset": "0.450s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.850s"
                }
              ]
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ]
}
```

## Idiomas compatíveis

Os seguintes idiomas e códigos de idioma BCP-47 são compatíveis com o Gemini 3.5 Transcribe:

| Idioma | Código BCP-47 | Idioma | Código BCP-47 |
| --- | --- | --- | --- |
| Africâner | `af-ZA` | Japonês | `ja-JP` |
| Amárico | `am-ET` | Javanês | `jv-ID` |
| Árabe (Egito) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armênio | `hy-AM` | Canarês | `kn-IN` |
| Assamês | `as-IN` | Cazaque | `kk-KZ` |
| Azerbaijano | `az-AZ` | Coreano | `ko-KR` |
| Bielorrusso | `be-BY` | Quirguiz | `ky-KG` |
| Bengali (Bangladesh) | `bn-BD` | Letão | `lv-LV` |
| Bengali (Índia) | `bn-IN` | Lingala | `ln-CD` |
| Bósnio | `bs-BA` | Lituano | `lt-LT` |
| Búlgaro | `bg-BG` | Macedônio | `mk-MK` |
| Búlgaro (aromaniano) | `rup-BG` | Malaio | `ms-MY` |
| Birmanês | `my-MM` | Malaiala | `ml-IN` |
| Cantonês (tradicional) | `yue-Hant-HK` | Maltês | `mt-MT` |
| Catalão | `ca-ES` | Chinês mandarim (simplificado) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marati | `mr-IN` |
| Khmer central | `km-KH` | Mongol | `mn-MN` |
| Croata | `hr-HR` | Nepalês | `ne-NP` |
| Tcheco | `cs-CZ` | Norueguês | `nb-NO` |
| Dinamarquês | `da-DK` | Oriá | `or-IN` |
| Holandês | `nl-NL` | Polonês | `pl-PL` |
| Inglês (Grã-Bretanha) | `en-GB` | Português (Brasil) | `pt-BR` |
| Inglês (Índia) | `en-IN` | Português (Portugal) | `pt-PT` |
| Inglês (EUA) | `en-US` | Punjabi | `pa-IN` |
| Estoniano | `et-EE` | Punjabi (script gurmukhi) | `pa-Guru-IN` |
| Farsi | `fa-IR` | Romeno | `ro-RO` |
| Filipino | `fil-PH` | Russo | `ru-RU` |
| Finlandês | `fi-FI` | Sérvio | `sr-RS` |
| Francês | `fr-FR` | Sindi (escrita árabe) | `sd-Arab-IN` |
| Galego | `gl-ES` | Eslovaco | `sk-SK` |
| Georgiano | `ka-GE` | Esloveno | `sl-SI` |
| Alemão | `de-DE` | Espanhol (América Latina) | `es-419` |
| Grego | `el-GR` | Espanhol (Estados Unidos) | `es-US` |
| Gujarati | `gu-IN` | Suaíli (Quênia) | `sw-KE` |
| Hauçá | `ha-NG` | Sueco | `sv-SE` |
| Hebraico | `he-IL` | Tadjique | `tg-TJ` |
| Hindi | `hi-IN` | Télugo | `te-IN` |
| Húngaro | `hu-HU` | Tailandês | `th-TH` |
| Islandês | `is-IS` | Turco | `tr-TR` |
| Inglês indiano | `en-IN` | Ucraniano | `uk-UA` |
| Indonésio | `id-ID` | Usbeque | `uz-UZ` |
| Italiano | `it-IT` | Vietnamita | `vi-VN` |

## Referência de parâmetros

Configure a transcrição definindo campos no objeto `audio_transcription_config` em `GenerateContentConfig`:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `language_codes` | Matriz de strings | Códigos de idioma BCP-47 (por exemplo, `["en-US"]`). Se omitido ou vazio (`[]`), o modelo detecta automaticamente o idioma e processa a troca de código. |
| `custom_vocabulary` | Matriz de strings | Até 1.000 termos personalizados, acrônimos ou nomes próprios para polarizar o reconhecimento de fala. |
| `word_timestamp` | Booleano | Defina como `True` para incluir ajustes de início e fim de palavras. Se for omitido ou `False`, nenhuma marcação de tempo de palavra será retornada. |
| `diarization` | Booleano | Defina como `True` para identificar e rotular locutores diferentes. |
| `mode` | String | Modo de transcrição. Valores aceitos: `"VERBATIM"` (padrão) e `"SMART"`. Incompatível com carimbos de data/hora e diarização. |

## Práticas recomendadas

- **Forneça áudio limpo**:garanta que as gravações de áudio tenham separação de voz clara e evite cortes graves.
- **Forneça dicas de idioma quando souber:** se você souber o idioma do áudio com antecedência, especifique `language_codes` para maximizar a precisão.
- **Segmentar vocabulário personalizado**:inclua apenas termos de domínio, nomes de marcas ou substantivos próprios distintos em `custom_vocabulary`, em vez de palavras comuns do dia a dia.
- **Use a API Files para gravações longas**:para arquivos com mais de alguns segundos, faça upload usando `client.files.upload` e transmita o arquivo retornado para o conteúdo do modelo.

## Limitações

- **Duração do áudio**:as solicitações unárias padrão são compatíveis com arquivos de áudio de até 1 hora. O processamento de áudio é limitado a 30 minutos quando recursos como diarização de locutor ou carimbos de data/hora no nível da palavra estão ativados.
- **Carimbos de data/hora no nível da palavra**:ativar esse recurso pode reduzir a acurácia geral da transcrição.
- **Diarização de locutor**:a diarização de locutor é compatível com até oito locutores. A atribuição de falante para três ou mais pessoas está em fase experimental.
- **Vocabulário personalizado**:é possível fornecer até 1.000 termos em `custom_vocabulary`, mas os melhores resultados geralmente são alcançados com até 100 termos.
- **Compatibilidade de modo**:a transcrição inteligente (`mode: "SMART"`) não pode ser combinada com `word_timestamp` ou `diarization`.

## A seguir

- Transmita áudio em tempo real com o [guia de transcrição em tempo real](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=pt-br) usando a API Live.
- Acesse [Entendimento de áudio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=pt-br) para analisar, resumir ou consultar conteúdo de áudio.
- Saiba como sintetizar áudio a partir de texto usando a [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pt-br).
- Confira a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-3.5-transcribe) para saber os preços dos modelos e os limites de tokens.
- Consulte o guia da [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br) para saber como fazer upload e gerenciar arquivos de mídia.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-10 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-10 UTC."],[],[]]
