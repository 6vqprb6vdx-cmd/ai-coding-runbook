---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=de
fetched_at: 2026-08-10T03:17:18.394387+00:00
title: "Musik in Echtzeit mit Lyria RealTime generieren \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Musik in Echtzeit mit Lyria RealTime generieren

Die Gemini API bietet mit
[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=de),
Zugriff auf ein hochmodernes Modell zur Musik
generierung in Echtzeit. Damit können Entwickler Anwendungen erstellen, mit denen Nutzer interaktiv Instrumentalmusik erstellen, kontinuierlich steuern und ausführen können.

Bei der Musikgenerierung mit Lyria RealTime wird eine persistente, bidirektionale,
Streamingverbindung mit niedriger Latenz über
[WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) verwendet.

Wenn Sie sehen möchten, was mit Lyria RealTime möglich ist, probieren Sie es in AI Studio
mit den [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=de) oder den
[MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=de) Apps aus.

## Musik generieren und steuern

Lyria RealTime funktioniert ähnlich wie die [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=de)
da es Websockets verwendet, um die Echtzeitkommunikation mit dem Modell aufrechtzuerhalten.

Der folgende Code zeigt, wie Sie Musik generieren:

### Python

In diesem Beispiel wird die Lyria RealTime-Sitzung mit `client.aio.live.music.connect()` initialisiert. Anschließend wird mit `session.set_weighted_prompts()` ein erster Prompt zusammen mit einer ersten Konfiguration mit `session.set_music_generation_config` gesendet. Die Musikgenerierung wird mit `session.play()` gestartet und `receive_audio()` wird eingerichtet, um die empfangenen Audio-Chunks zu verarbeiten.

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

In diesem Beispiel wird die Lyria RealTime-Sitzung mit `client.live.music.connect()` initialisiert. Anschließend wird mit `session.setWeightedPrompts()` ein erster Prompt zusammen mit einer ersten Konfiguration mit `session.setMusicGenerationConfig` gesendet. Die Musikgenerierung wird mit `session.play()` gestartet und ein `onMessage`-Callback wird eingerichtet, um die empfangenen Audio-Chunks zu verarbeiten.

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

Mit `session.play()`, `session.pause()`, `session.stop()` und `session.reset_context()` können Sie die Sitzung starten, pausieren, beenden oder zurücksetzen.

## Musik in Echtzeit steuern

Sie können die Musikgenerierung in Echtzeit steuern, indem Sie Prompts senden und die Generierungsparameter in Echtzeit aktualisieren.

### Prompt für Lyria RealTime

Während der Stream aktiv ist, können Sie jederzeit neue `WeightedPrompt`-Nachrichten senden, um die generierte Musik zu ändern. Das Modell führt basierend auf der neuen Eingabe einen reibungslosen Übergang durch.

Die Prompts müssen das richtige Format mit einem `text` (dem eigentlichen Prompt) und einem `weight` haben. Für `weight` kann ein beliebiger Wert außer `0` verwendet werden. `1.0`
ist normalerweise ein guter Ausgangspunkt.

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

Beachten Sie, dass die Übergänge des Modells etwas abrupt sein können, wenn Sie die Prompts drastisch ändern. Daher wird empfohlen, eine Art Überblendung zu implementieren, indem Sie dem Modell Zwischenwerte für das Gewicht senden.

### Konfiguration aktualisieren

Sie können die Musikgenerierung steuern, indem Sie die Parameter für die Musikgenerierung in Echtzeit aktualisieren. Sie können nicht nur einen Parameter aktualisieren, sondern müssen die gesamte Konfiguration festlegen. Andernfalls werden die anderen Felder auf ihre Standardwerte zurückgesetzt.

Da die Aktualisierung von BPM oder Tonart eine drastische Änderung für das Modell darstellt, müssen Sie es auch anweisen, den Kontext mit `reset_context()` zurückzusetzen, damit die neue Konfiguration berücksichtigt wird. Dadurch wird der Stream nicht beendet, aber es kommt zu einem harten Übergang. Für die anderen Parameter ist das nicht erforderlich.

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

## Leitfaden für Prompts für Lyria RealTime

Hier ist eine unvollständige Liste von Prompts, die Sie für Lyria RealTime verwenden können:

- Instrumente: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
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
- Musikgenre: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
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
- Stimmung/Beschreibung: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

Das sind nur einige Beispiele. Lyria RealTime kann noch viel mehr. Probieren Sie es mit eigenen Prompts aus.

## Best Practices

- Clientanwendungen müssen eine robuste Audio-Pufferung implementieren, um eine reibungslose Wiedergabe zu gewährleisten. So können Netzwerklatenz und geringfügige Abweichungen bei der Generierungslatenz berücksichtigt werden.
- Effektive Prompts:
  - Verwenden Sie anschauliche Begriffe. Verwenden Sie Adjektive, um Stimmung, Genre und Instrumentierung zu beschreiben.
  - Iterieren und steuern Sie schrittweise. Anstatt den Prompt komplett zu ändern, versuchen Sie, Elemente hinzuzufügen oder zu ändern, um die Musik reibungsloser zu verändern.
  - Experimentieren Sie mit dem Gewicht von `WeightedPrompt`, um zu beeinflussen, wie stark sich ein neuer Prompt auf die laufende Generierung auswirkt.

## Technische Details

In diesem Abschnitt werden die Besonderheiten der Verwendung der Musikgenerierung mit Lyria RealTime beschrieben.

### Spezifikationen

- Ausgabeformat: Raw 16-Bit-PCM-Audio
- Abtastrate: 48 kHz
- Kanäle: 2 (Stereo)

### Steuerelemente

Die Musikgenerierung kann in Echtzeit beeinflusst werden, indem Nachrichten mit Folgendem gesendet werden:

- `WeightedPrompt`: Ein Textstring, der eine musikalische Idee, ein Genre, ein Instrument, eine Stimmung oder eine Eigenschaft beschreibt. Es können mehrere Prompts angegeben werden, um Einflüsse zu mischen. Weitere Informationen zum Erstellen von Prompts für
  Lyria RealTime finden Sie [oben](#steer-music).
- `MusicGenerationConfig`: Konfiguration für den Musikgenerierungsprozess, die die Eigenschaften des Ausgabes beeinflusst. Parameter:
  - `guidance`: (float) Bereich: `[0.0, 6.0]`. Standard: `4.0`.
    Steuert, wie genau das Modell den Prompts folgt. Eine höhere Anleitung verbessert die Einhaltung des Prompts, macht Übergänge aber abrupter.
  - `bpm`: (int) Bereich: `[60, 200]`.
    Legt die Beats pro Minute für die generierte Musik fest. Sie müssen den Kontext für das Modell beenden/wiedergeben oder zurücksetzen, damit die neuen BPM berücksichtigt werden.
  - `density`: (float) Bereich: `[0.0, 1.0]`.
    Steuert die Dichte der Musiknoten/Sounds. Niedrigere Werte erzeugen spärlichere Musik, höhere Werte erzeugen „geschäftigere“ Musik.
  - `brightness`: (float) Bereich: `[0.0, 1.0]`.
    Passt die Klangqualität an. Höhere Werte erzeugen einen „helleren“ Klang und betonen im Allgemeinen höhere Frequenzen.
  - `scale`: (Enum) Legt die Tonart (Tonart und Modus) für die Generierung fest. Verwenden Sie die
    [`Scale` Enum-Werte](#scale-enum), die vom SDK bereitgestellt werden. Sie müssen den Kontext für das Modell beenden/wiedergeben oder zurücksetzen, damit die neue Tonart berücksichtigt wird.
  - `mute_bass`: (bool) Standard: `False`.
    Steuert, ob das Modell den Bass der Ausgaben reduziert.
  - `mute_drums`: (bool) Standard: `False`.
    Steuert, ob das Modell die Drums der Ausgaben reduziert.
  - `only_bass_and_drums`: (bool) Standard: `False`.
    Weisen Sie das Modell an, nur Bass und Drums auszugeben.
  - `music_generation_mode`: (Enum) Gibt dem Modell an, ob es sich auf `QUALITY` (Standardwert) oder `DIVERSITY` der Musik konzentrieren soll. Es kann auch auf `VOCALIZATION` gesetzt werden, damit das Modell Gesang als weiteres Instrument generiert (fügen Sie sie als neue Prompts hinzu).
- `PlaybackControl`: Befehle zum Steuern von Wiedergabeaspekten wie Wiedergabe, Pause, Beenden oder Zurücksetzen des Kontexts.

Wenn für `bpm`, `density`, `brightness` und `scale` kein Wert angegeben wird, entscheidet das Modell anhand Ihrer ersten Prompts, was am besten ist.

Weitere klassische Parameter wie `temperature` (0,0 bis 3,0, Standard 1,1), `top_k` (1 bis 1000, Standard 40) und `seed` (0 bis 2.147.483.647, standardmäßig zufällig ausgewählt) können auch in `MusicGenerationConfig` angepasst werden.

#### Enum-Werte für Tonart

Hier sind alle Tonartwerte, die das Modell akzeptieren kann:

| Enum-Wert | Tonart |
| --- | --- |
| `C_MAJOR_A_MINOR` | C-Dur / A-Moll |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Des-Dur / B-Moll |
| `D_MAJOR_B_MINOR` | D-Dur / H-Moll |
| `E_FLAT_MAJOR_C_MINOR` | Es-Dur / C-Moll |
| `E_MAJOR_D_FLAT_MINOR` | E-Dur / Cis-Moll/Des-Moll |
| `F_MAJOR_D_MINOR` | F-Dur / D-Moll |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | Ges-Dur / Es-Moll |
| `G_MAJOR_E_MINOR` | G-Dur / E-Moll |
| `A_FLAT_MAJOR_F_MINOR` | As-Dur / F-Moll |
| `A_MAJOR_G_FLAT_MINOR` | A-Dur / Fis-Moll/Ges-Moll |
| `B_FLAT_MAJOR_G_MINOR` | B-Dur / G-Moll |
| `B_MAJOR_A_FLAT_MINOR` | H-Dur / Gis-Moll/As-Moll |
| `SCALE_UNSPECIFIED` | Standard / Das Modell entscheidet |

Das Modell kann die gespielten Noten steuern, unterscheidet aber nicht zwischen relativen Tonarten. Daher entspricht jede Enum sowohl der relativen Dur- als auch der relativen Moll-Tonart. `C_MAJOR_A_MINOR` würde beispielsweise allen weißen Tasten eines Klaviers entsprechen und `F_MAJOR_D_MINOR` allen weißen Tasten außer B.

### Beschränkungen

- Nur Instrumentalmusik: Das Modell generiert nur Instrumentalmusik.
- Sicherheit: Prompts werden von Sicherheitsfiltern überprüft. Prompts, die die Filter auslösen, werden ignoriert. In diesem Fall wird im Feld `filtered_prompt` der Ausgabe eine Erklärung angezeigt.
- Wasserzeichen: Die Audioausgabe wird immer mit einem Wasserzeichen versehen, um sie gemäß unseren [Prinzipien für verantwortungsbewusste Anwendung von KI](https://ai.google/responsibility/principles/?hl=de) zu identifizieren.

## Nächste Schritte

- Mit [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=de) vollständige Songs und Gesangsstücke generieren
- Anstatt Musik zu generieren, können Sie mit den
  den [TTS-Modellen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de) Unterhaltungen mit mehreren Sprechern generieren.
- Bilder[oder](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) Videos[generieren](https://ai.google.dev/gemini-api/docs/video?hl=de)
- Anstatt Musik oder Audio zu generieren, können Sie herausfinden, wie Gemini
  [Audiodateien verstehen kann](https://ai.google.dev/gemini-api/docs/audio?hl=de).
- Mit der
  [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=de) in Echtzeit mit Gemini sprechen.

Weitere
Codebeispiele und Anleitungen finden Sie im [Cookbook](https://github.com/google-gemini/cookbook).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-28 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-28 (UTC)."],[],[]]
