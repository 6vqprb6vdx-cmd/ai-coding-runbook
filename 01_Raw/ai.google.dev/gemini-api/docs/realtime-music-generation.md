---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pt-BR
fetched_at: 2026-11-02T07:14:55.272307+00:00
title: "Gera\u00e7\u00e3o de m\u00fasica em tempo real com o Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Geração de música em tempo real com o Lyria RealTime

A API Gemini, usando o [Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=pt-br), oferece acesso a um modelo de geração de música por streaming em tempo real e de última geração. Ele permite que os desenvolvedores criem aplicativos em que os usuários
podem criar, conduzir e tocar músicas instrumentais
de forma interativa.

A geração de música do Lyria RealTime usa uma conexão de streaming persistente, bidirecional e de baixa latência usando [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Para saber o que pode ser criado com o Lyria RealTime, teste no AI Studio
usando os apps [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=pt-br) ou
[MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=pt-br).

## Gerar e controlar músicas

O Lyria RealTime funciona de maneira semelhante à [API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br), usando WebSockets para manter a comunicação em tempo real com o modelo.

O código a seguir demonstra como gerar música:

### Python

Este exemplo inicializa a sessão do Lyria RealTime usando
`client.aio.live.music.connect()`, envia um
comando inicial com `session.set_weighted_prompts()` e uma
configuração inicial usando `session.set_music_generation_config`, inicia a geração de
música usando `session.play()` e configura
`receive_audio()` para processar os trechos de áudio recebidos.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1beta'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

Este exemplo inicializa a sessão do Lyria RealTime usando
`client.live.music.connect()`, envia um
comando inicial com `session.setWeightedPrompts()` e uma
configuração inicial usando `session.setMusicGenerationConfig`, inicia a geração de
música usando `session.play()` e configura um
callback `onMessage` para processar os trechos de áudio recebidos.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1beta" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

Em seguida, use `session.play()`, `session.pause()`, `session.stop()` e `session.reset_context()` para iniciar, pausar, interromper ou redefinir a sessão.

## Conduzir a música em tempo real

Você pode direcionar a geração de músicas em tempo real enviando comandos e atualizando os parâmetros de geração.

### Comandar o Lyria RealTime

Enquanto a transmissão estiver ativa, você pode enviar novas mensagens de `WeightedPrompt` a qualquer momento para alterar a música gerada. O modelo fará uma transição suave com base na nova entrada.

Os comandos precisam seguir o formato correto com um `text` (o comando real) e um `weight`. O `weight` pode assumir qualquer valor, exceto `0`. `1.0` costuma ser um bom ponto de partida.

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

As transições de modelo podem ser um pouco abruptas ao mudar drasticamente os comandos. Por isso, é recomendável implementar algum tipo de fade-out cruzado enviando valores de ponderação intermediários ao modelo.

### Atualizar a configuração

É possível direcionar a geração de músicas atualizando os parâmetros em tempo real. Não é possível apenas atualizar um parâmetro. É necessário definir toda a configuração. Caso contrário, os outros campos serão redefinidos para os valores padrão.

Como atualizar o bpm ou a escala é uma mudança drástica para o modelo, você também precisa pedir que ele redefina o contexto usando `reset_context()` para considerar a nova configuração. Ela não vai interromper a transmissão, mas será uma transição difícil. Não é necessário fazer isso para os outros parâmetros.

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## Comandos do Lyria RealTime

O Lyria RealTime usa comandos ponderados para combinar gêneros musicais, instrumentos e estilos de forma dinâmica. Para conhecer estratégias de direcionamento de comandos, vocabulários de tags de palavras-chave e exemplos de comandos completos, consulte o [guia de comandos do Lyria](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=pt-br#realtime-prompting).

## Práticas recomendadas

- Os aplicativos cliente precisam implementar um buffer de áudio robusto para garantir uma
  reprodução sem problemas. Isso ajuda a considerar o jitter da rede e pequenas variações na latência de geração.
- Comandos eficazes:
  - Utilize descrições. Use adjetivos que descrevam o clima, o gênero e a instrumentação.
  - Faça iterações e direcione gradualmente. Em vez de mudar completamente o comando, adicione ou modifique elementos para transformar a música de maneira mais suave.
  - Teste o peso em `WeightedPrompt` para influenciar a intensidade com que um novo
    comando afeta a geração em andamento.

## Detalhes técnicos

Esta seção descreve os detalhes de como usar a geração de música em tempo real do Lyria.

### Especificações

- Formato de saída: áudio PCM bruto de 16 bits
- Taxa de amostragem: 48 kHz
- Canais: 2 (estéreo)

### Controles

A geração de música pode ser influenciada em tempo real enviando mensagens que contenham:

- `WeightedPrompt`: uma string de texto que descreve uma ideia musical, um gênero, um instrumento, um clima ou uma característica. Vários comandos podem ser fornecidos para combinar influências. Consulte [acima](#steer-music) para mais detalhes sobre como dar comandos à Lyria RealTime.
- `MusicGenerationConfig`: configuração do processo de geração de música, que influencia as características do áudio de saída. Os parâmetros incluem:
  - `guidance`: (ponto flutuante) Intervalo: `[0.0, 6.0]`. Padrão: `4.0`.
    Controla o nível de rigor com que o modelo segue os comandos. Uma orientação mais alta melhora a aderência ao comando, mas torna as transições mais abruptas.
  - `bpm`: (int) Intervalo: `[60, 200]`.
    Define os batimentos por minuto que você quer para a música gerada. Você precisa
    parar/tocar ou redefinir o contexto para que o modelo considere o novo
    bpm.
  - `density`: (ponto flutuante) Intervalo: `[0.0, 1.0]`.
    Controla a densidade das notas/sons musicais. Valores mais baixos produzem músicas mais esparsas, e valores mais altos produzem músicas mais "agitadas".
  - `brightness`: (ponto flutuante) Intervalo: `[0.0, 1.0]`.
    Ajusta a qualidade tonal. Valores mais altos produzem um áudio mais "brilhante", geralmente enfatizando frequências mais altas.
  - `scale`: (enum)
    Define a escala musical (chave e modo) para a geração. Use os
    [valores de enumeração `Scale`](#scale-enum) fornecidos pelo SDK. Você precisa
    parar/tocar ou redefinir o contexto para que o modelo considere a nova
    escala.
  - `mute_bass`: (bool) Padrão: `False`.
    Controla se o modelo reduz o baixo das saídas.
  - `mute_drums`: (bool) Padrão: `False`.
    Controla se a saída do modelo reduz a bateria.
  - `only_bass_and_drums`: (bool) Padrão: `False`.
    Direcione o modelo para tentar gerar apenas baixo e bateria.
  - `music_generation_mode`: (enum)
    Indica ao modelo se ele deve se concentrar em `QUALITY` (valor padrão) ou
    `DIVERSITY` da música. Também é possível definir como `VOCALIZATION` para que o modelo gere vocalizações como outro instrumento (adicione-as como novos comandos).
- `PlaybackControl`: comandos para controlar aspectos da reprodução, como tocar, pausar, parar ou redefinir o contexto.

Para `bpm`, `density`, `brightness` e `scale`, se nenhum valor for fornecido, o modelo vai decidir o que é melhor de acordo com seus comandos iniciais.

Outros parâmetros mais clássicos, como `temperature` (0,0 a 3,0, padrão 1,1), `top_k` (1 a 1.000, padrão 40) e `seed` (0 a 2.147.483.647, selecionado aleatoriamente por padrão), também podem ser personalizados no `MusicGenerationConfig`.

#### Dimensionar valores de tipo enumerado

Estes são todos os valores de escala que o modelo pode aceitar:

| Valor de tipo enumerado | Escala / Chave |
| --- | --- |
| `C_MAJOR_A_MINOR` | C maior / A menor |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Dó bemol maior / Si bemol menor |
| `D_MAJOR_B_MINOR` | Ré maior / Si menor |
| `E_FLAT_MAJOR_C_MINOR` | Mi bemol maior / dó menor |
| `E_MAJOR_D_FLAT_MINOR` | Mi maior / dó sustenido/ré bemol menor |
| `F_MAJOR_D_MINOR` | Fá maior / Ré menor |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | G♭ maior / E♭ menor |
| `G_MAJOR_E_MINOR` | Sol maior / Mi menor |
| `A_FLAT_MAJOR_F_MINOR` | A♭ maior / F menor |
| `A_MAJOR_G_FLAT_MINOR` | A maior / F♯/G♭ menor |
| `B_FLAT_MAJOR_G_MINOR` | B♭ maior / G menor |
| `B_MAJOR_A_FLAT_MINOR` | B maior / G♯/A♭ menor |
| `SCALE_UNSPECIFIED` | Padrão / O modelo decide |

O modelo consegue orientar as notas tocadas, mas não distingue entre teclas relativas. Assim, cada enumeração corresponde tanto à versão principal quanto à secundária relativa. Por exemplo, `C_MAJOR_A_MINOR` corresponderia a todas as teclas brancas de um piano, e `F_MAJOR_D_MINOR` seria todas as teclas brancas, exceto si bemol.

### Limitações

- Somente instrumental: o modelo gera apenas músicas instrumentais.
- Segurança: os comandos são verificados por filtros de segurança. Os comandos que acionam os filtros serão ignorados. Nesse caso, uma explicação será escrita no campo `filtered_prompt` da saída.
- Marca d'água: o áudio de saída sempre recebe uma marca d'água para identificação, seguindo nossos princípios de [IA responsável](https://ai.google/responsibility/principles/?hl=pt-br).

## A seguir

- Gere músicas completas e faixas vocais com o [Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=pt-br).
- Em vez de música, aprenda a gerar conversas com vários locutores usando os [modelos de TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pt-br).
- Descubra como gerar [imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) ou [vídeos](https://ai.google.dev/gemini-api/docs/video?hl=pt-br),
- Em vez de gerar música ou áudio, saiba como o Gemini pode
  [entender arquivos de áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br),
- Converse em tempo real com o Gemini usando a [API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br).

Confira o [Cookbook](https://github.com/google-gemini/cookbook) para mais exemplos de código e tutoriais.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-18 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-18 UTC."],[],[]]
