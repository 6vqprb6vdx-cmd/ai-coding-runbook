---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=es-419
fetched_at: 2026-07-20T04:35:04.449641+00:00
title: "Generaci\u00f3n de m\u00fasica en tiempo real con Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Generación de música en tiempo real con Lyria RealTime

La API de Gemini, que usa [Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=es-419), proporciona acceso a un modelo de generación de música en tiempo real y de transmisión de vanguardia. Permite a los desarrolladores crear aplicaciones en las que los usuarios pueden crear, dirigir y ejecutar música instrumental de forma interactiva.

La generación de música de Lyria RealTime usa una conexión de transmisión persistente, bidireccional y de baja latencia con [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Para experimentar lo que se puede crear con Lyria RealTime, pruébalo en AI Studio con las apps [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=es-419) o [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=es-419).

## Genera y controla música

Lyria RealTime funciona de manera similar a la [API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419), ya que usa WebSockets para mantener la comunicación en tiempo real con el modelo.

En el siguiente código, se muestra cómo generar música:

### Python

En este ejemplo, se inicializa la sesión de Lyria RealTime con `client.aio.live.music.connect()`, luego se envía una instrucción inicial con `session.set_weighted_prompts()` junto con una configuración inicial con `session.set_music_generation_config`, se inicia la generación de música con `session.play()` y se configura `receive_audio()` para procesar los fragmentos de audio que recibe.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1alpha'})

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

En este ejemplo, se inicializa la sesión de Lyria RealTime con `client.live.music.connect()`, luego se envía una instrucción inicial con `session.setWeightedPrompts()` junto con una configuración inicial con `session.setMusicGenerationConfig`, se inicia la generación de música con `session.play()` y se configura una devolución de llamada `onMessage` para procesar los fragmentos de audio que recibe.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1alpha" ,
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

Luego, puedes usar `session.play()`, `session.pause()`, `session.stop()` y `session.reset_context()` para iniciar, pausar, detener o restablecer la sesión.

## Dirige la música en tiempo real

Puedes dirigir la generación de música en tiempo real enviando instrucciones y actualizando los parámetros de generación en tiempo real.

### Cómo solicitarle a Lyria RealTime

Mientras la transmisión esté activa, puedes enviar mensajes `WeightedPrompt` nuevos en cualquier momento para alterar la música generada. El modelo realizará una transición fluida en función de la nueva entrada.

Las instrucciones deben seguir el formato correcto con un `text` (la instrucción real) y un `weight`. El `weight` puede tomar cualquier valor, excepto `0`. `1.0`
suele ser un buen punto de partida.

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
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

Ten en cuenta que las transiciones del modelo pueden ser un poco abruptas cuando se cambian drásticamente las instrucciones, por lo que se recomienda implementar algún tipo de fundido cruzado enviando valores de peso intermedios al modelo.

### Actualiza la configuración

Puedes dirigir la generación de música actualizando los parámetros de generación de música en tiempo real. No puedes solo actualizar un parámetro, sino que debes establecer toda la configuración. De lo contrario, los otros campos se restablecerán a sus valores predeterminados.

Como actualizar el BPM o la escala es un cambio drástico para el modelo, también deberás indicarle que restablezca su contexto con `reset_context()` para tener en cuenta la nueva configuración. No detendrá la transmisión, pero será una transición abrupta. No es necesario que lo hagas para los demás parámetros.

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

## Guía de instrucciones para Lyria RealTime

Esta es una lista no exhaustiva de instrucciones que puedes usar para indicarle a Lyria RealTime:

- Instrumentos: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- Género musical: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- Estado de ánimo o descripción: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

Estos son solo algunos ejemplos, ya que Lyria RealTime puede hacer mucho más. Experimenta con tus propias instrucciones.

## Prácticas recomendadas

- Las aplicaciones cliente deben implementar un almacenamiento en búfer de audio sólido para garantizar una reproducción fluida. Esto ayuda a tener en cuenta la fluctuación de la red y las pequeñas variaciones en la latencia de generación.
- Instrucciones eficaces:
  - Sea descriptivo. Usa adjetivos que describan el estado de ánimo, el género y la instrumentación.
  - Itera y dirige el proyecto de forma gradual. En lugar de cambiar por completo la instrucción, intenta agregar o modificar elementos para transformar la música de forma más fluida.
  - Experimenta con el peso en `WeightedPrompt` para influir en la intensidad con la que una nueva instrucción afecta la generación en curso.

## Detalles técnicos

En esta sección, se describen los detalles específicos para usar la generación de música en tiempo real de Lyria.

### Especificaciones

- Formato de salida: Audio PCM sin procesar de 16 bits
- Tasa de muestreo: 48 kHz
- Canales: 2 (estéreo)

### Controles

La generación de música se puede influenciar en tiempo real enviando mensajes que contengan lo siguiente:

- `WeightedPrompt`: Es una cadena de texto que describe una idea musical, un género, un instrumento, un estado de ánimo o una característica. Se pueden proporcionar varias instrucciones para combinar influencias. Consulta [arriba](#steer-music) para obtener más detalles sobre cómo solicitarle información a Lyria RealTime de la mejor manera.
- `MusicGenerationConfig`: Es la configuración del proceso de generación de música, que influye en las características del audio de salida. Los parámetros incluyen lo siguiente:
  - `guidance`: (float) Rango: `[0.0, 6.0]`. Valor predeterminado: `4.0`.
    Controla qué tan estrictamente el modelo sigue las instrucciones. Una mayor orientación mejora el cumplimiento de la instrucción, pero hace que las transiciones sean más abruptas.
  - `bpm`: (int) Rango: `[60, 200]`.
    Establece las pulsaciones por minuto que deseas para la música generada. Debes detener, reproducir o restablecer el contexto del modelo para que tenga en cuenta el nuevo BPM.
  - `density`: (float) Rango: `[0.0, 1.0]`.
    Controla la densidad de las notas o los sonidos musicales. Los valores más bajos producen música más dispersa, mientras que los valores más altos producen música más "ocupada".
  - `brightness`: (float) Rango: `[0.0, 1.0]`.
    Ajusta la calidad tonal. Los valores más altos producen un audio con un sonido más "brillante", que generalmente enfatiza las frecuencias más altas.
  - `scale`: (Enum)
    Establece la escala musical (clave y modo) para la generación. Usa los [valores de enumeración `Scale`](#scale-enum) que proporciona el SDK. Debes detener, reproducir o restablecer el contexto para que el modelo tenga en cuenta la nueva escala.
  - `mute_bass`: (bool) Valor predeterminado: `False`.
    Controla si el modelo reduce los graves de los resultados.
  - `mute_drums`: (bool) Valor predeterminado: `False`.
    Controla si el modelo reduce los tambores de los resultados.
  - `only_bass_and_drums`: (bool) Valor predeterminado: `False`.
    Dirige el modelo para que intente generar solo el bajo y la batería.
  - `music_generation_mode`: (Enum)
    Indica al modelo si debe enfocarse en el `QUALITY` (valor predeterminado) o el `DIVERSITY` de la música. También se puede establecer en `VOCALIZATION` para permitir que el modelo genere vocalizaciones como otro instrumento (agrégalas como nuevas instrucciones).
- `PlaybackControl`: Comandos para controlar aspectos de la reproducción, como reproducir, pausar, detener o restablecer el contexto.

En el caso de `bpm`, `density`, `brightness` y `scale`, si no se proporciona ningún valor, el modelo decidirá qué es mejor según tus instrucciones iniciales.

En `MusicGenerationConfig`, también se pueden personalizar parámetros más clásicos, como `temperature` (de 0.0 a 3.0, 1.1 de forma predeterminada), `top_k` (de 1 a 1,000, 40 de forma predeterminada) y `seed` (de 0 a 2,147,483,647, seleccionado de forma aleatoria de forma predeterminada).

#### Valores de enumeración de la escala

Estos son todos los valores de escala que puede aceptar el modelo:

| Valor de enum | Escala o clave |
| --- | --- |
| `C_MAJOR_A_MINOR` | Do mayor / La menor |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Re♭ mayor / si♭ menor |
| `D_MAJOR_B_MINOR` | Re mayor / Si menor |
| `E_FLAT_MAJOR_C_MINOR` | Mi♭ mayor / Do menor |
| `E_MAJOR_D_FLAT_MINOR` | Mi mayor / Do sostenido menor/Re bemol menor |
| `F_MAJOR_D_MINOR` | Fa mayor / Re menor |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | Sol♭ mayor / mi♭ menor |
| `G_MAJOR_E_MINOR` | Sol mayor / Mi menor |
| `A_FLAT_MAJOR_F_MINOR` | La bemol mayor / fa menor |
| `A_MAJOR_G_FLAT_MINOR` | La mayor / la menor de F♯/G♭ |
| `B_FLAT_MAJOR_G_MINOR` | Si bemol mayor / sol menor |
| `B_MAJOR_A_FLAT_MINOR` | Si mayor / La♯/Si♭ menor |
| `SCALE_UNSPECIFIED` | Predeterminado: El modelo decide |

El modelo puede guiar las notas que se reproducen, pero no distingue entre las claves relativas. Por lo tanto, cada enumeración corresponde tanto a la versión principal como a la secundaria relativas. Por ejemplo, `C_MAJOR_A_MINOR` correspondería a todas las teclas blancas de un piano, y `F_MAJOR_D_MINOR` serían todas las teclas blancas, excepto la B bemol.

### Limitaciones

- Solo instrumental: El modelo solo genera música instrumental.
- Seguridad: Los filtros de seguridad verifican las instrucciones. Se ignorarán las instrucciones que activen los filtros, en cuyo caso se escribirá una explicación en el campo `filtered_prompt` del resultado.
- Marcas de agua: El audio de salida siempre tiene una marca de agua para su identificación, de acuerdo con nuestros principios de [IA responsable](https://ai.google/responsibility/principles/?hl=es-419).

## ¿Qué sigue?

- Genera canciones completas y pistas vocales con [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=es-419).
- En lugar de música, aprende a generar conversaciones con varios oradores usando los [modelos de TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419).
- Descubre cómo generar [imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419) o [videos](https://ai.google.dev/gemini-api/docs/video?hl=es-419).
- En lugar de generar música o audio, descubre cómo Gemini puede [comprender archivos de audio](https://ai.google.dev/gemini-api/docs/audio?hl=es-419).
- Mantén una conversación en tiempo real con Gemini usando la [API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419).

Explora el [Cookbook](https://github.com/google-gemini/cookbook) para obtener más ejemplos de código y tutoriales.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-16 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-16 (UTC)"],[],[]]
