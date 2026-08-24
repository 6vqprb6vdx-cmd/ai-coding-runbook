---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=pl
fetched_at: 2026-08-24T02:24:00.468656+00:00
title: "Generowanie obraz\u00f3w za pomoc\u0105 Imagen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie obrazów za pomocą Imagen

Imagen to model Google do generowania obrazów wysokiej jakości, który potrafi tworzyć realistyczne obrazy wysokiej jakości na podstawie promptów tekstowych. Wszystkie wygenerowane obrazy zawierają znak wodny SynthID. Więcej informacji o dostępnych wariantach modelu Imagen znajdziesz w sekcji [Wersje modelu](#model-versions).

## Migracja do Nano Banana

Modele Imagen są wycofywane i zostaną wyłączone 17 sierpnia 2026 r. Zalecamy przejście na Nano Banana, jeśli potrzebujesz generować obrazy.

Migracja obejmuje następujące zmiany:

- **Nazwa modelu:** używaj symbolu `gemini-2.5-flash-image` zamiast nazw modeli Imagen.
- **Metoda:** używaj `client.models.generate_content` zamiast `client.models.generate_images`.
- **Obsługa odpowiedzi:** Nano Banana zwraca części treści, które mogą zawierać dane obrazu, zamiast konkretnego obiektu odpowiedzi obrazu.

Więcej informacji i przykładów znajdziesz w [przewodniku po generowaniu obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl).

## Generowanie obrazów za pomocą modeli Imagen

Ten przykład pokazuje generowanie obrazów za pomocą [modelu Imagen](https://deepmind.google/technologies/imagen/?hl=pl):

### Python

```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 4,
    )
)
for generated_image in response.generated_images:
  generated_image.image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const response = await ai.models.generateImages({
    model: 'imagen-4.0-generate-001',
    prompt: 'Robot holding a red skateboard',
    config: {
      numberOfImages: 4,
    },
  });

  let idx = 1;
  for (const generatedImage of response.generatedImages) {
    let imgBytes = generatedImage.image.imageBytes;
    const buffer = Buffer.from(imgBytes, "base64");
    fs.writeFileSync(`imagen-${idx}.png`, buffer);
    idx++;
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  config := &genai.GenerateImagesConfig{
      NumberOfImages: 4,
  }

  response, _ := client.Models.GenerateImages(
      ctx,
      "imagen-4.0-generate-001",
      "Robot holding a red skateboard",
      config,
  )

  for n, image := range response.GeneratedImages {
      fname := fmt.Sprintf("imagen-%d.png", n)
          _ = os.WriteFile(fname, image.Image.ImageBytes, 0644)
  }
}
```

### REST

```
curl -X POST \
    "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "instances": [
          {
            "prompt": "Robot holding a red skateboard"
          }
        ],
        "parameters": {
          "sampleCount": 4
        }
      }'
```

![Obraz wygenerowany przez AI przedstawiający robota trzymającego czerwoną deskorolkę](https://ai.google.dev/static/gemini-api/docs/images/robot-skateboard.png?hl=pl)

Obraz wygenerowany przez AI przedstawiający robota trzymającego czerwoną deskorolkę

### Konfiguracja Imagen

Obecnie Imagen obsługuje tylko prompty w języku angielskim i te parametry:

- `numberOfImages`: liczba obrazów do wygenerowania, od 1 do 4 (włącznie).
  Wartość domyślna to 4.
- `imageSize`: rozmiar wygenerowanego obrazu. Ta funkcja jest obsługiwana tylko w przypadku modeli Standard i Ultra. Obsługiwane wartości to `1K` i `2K`.
  Wartość domyślna to `1K`.
- `aspectRatio`: zmienia format wygenerowanego obrazu. Obsługiwane wartości to `"1:1"`, `"3:4"`, `"4:3"`, `"9:16"` i `"16:9"`. Wartość domyślna to `"1:1"`.
- `personGeneration`: zezwolenie modelowi na generowanie obrazów osób; Obsługiwane są te wartości:

  - `"dont_allow"`: blokowanie generowania obrazów przedstawiających ludzi.
  - `"allow_adult"`: generować obrazy przedstawiające osoby dorosłe, ale nie dzieci. Jest to ustawienie domyślne.
  - `"allow_all"`: generować obrazy przedstawiające dorosłych i dzieci;

## Przewodnik po tworzeniu promptów Imagen

W tej sekcji przewodnika po Imagen znajdziesz informacje o tym, jak modyfikowanie promptu do zamiany tekstu na obraz może dać różne wyniki, a także przykłady obrazów, które możesz utworzyć.

### Podstawowe informacje o pisaniu promptów

Dobry prompt jest opisowy i jasny, a także zawiera odpowiednie słowa kluczowe i modyfikatory. Zacznij od określenia **tematu**, **kontekstu** i **stylu**.

![Prompt z podkreślonym tematem, kontekstem i stylem](https://ai.google.dev/static/gemini-api/docs/images/imagen/style-subject-context.png?hl=pl)

Tekst obrazu: *Szkic* (**styl**) *nowoczesnego budynku mieszkalnego* (**obiekt**) otoczonego *wieżowcami* (**kontekst i tło**).

1. **Temat:** pierwszą rzeczą, o której należy pomyśleć w przypadku każdego prompta, jest *temat*, czyli obiekt, osoba, zwierzę lub sceneria, które mają się znaleźć na obrazie.
2. **Kontekst i tło:** równie ważne jest *tło lub kontekst*, w którym umieścisz obiekt. Spróbuj umieścić fotografowany obiekt na różnych tłach. Na przykład studio z białym tłem, plener lub wnętrze.
3. **Styl:** na koniec dodaj styl obrazu, który chcesz uzyskać. *Style* może być ogólny (obraz, zdjęcie, szkic) lub bardzo szczegółowy (pastel, rysunek węglem, izometryczny obraz 3D). Możesz też łączyć style.

Po napisaniu pierwszej wersji prompta dopracuj go, dodając więcej szczegółów, aż uzyskasz obraz, który Cię zadowoli. Iteracja jest ważna.
Zacznij od ustalenia głównego pomysłu, a następnie dopracowuj go i rozwijaj, aż wygenerowany obraz będzie zbliżony do Twojej wizji.

|  |  |  |
| --- | --- | --- |
| Przykładowy obraz fotorealistyczny 1   Prompt: A park in the spring next to a lake | przykładowy fotorealistyczny obraz 2   Prompt: Park wiosną nad jeziorem, **słońce zachodzi nad jeziorem, złota godzina** | przykładowy fotorealistyczny obraz 3   Prompt: Park wiosną nad jeziorem, ***zachód słońca nad jeziorem, złota godzina, czerwone dzikie kwiaty*** |

Modele Imagen mogą przekształcać Twoje pomysły w szczegółowe obrazy, niezależnie od tego, czy prompty są krótkie, czy długie i szczegółowe. Dopracuj swoją wizję,
iteracyjnie dodając szczegóły, aż uzyskasz idealny
rezultat.

|  |  |
| --- | --- |
| Krótkie prompty umożliwiają szybkie wygenerowanie obrazu.  Przykład krótkiego prompta w Imagen 4   Prompt: zdjęcie z bliska kobiety w wieku 20 lat, fotografia uliczna, kadr z filmu, stonowane ciepłe odcienie pomarańczowego | Dłuższe prompty pozwalają dodawać szczegółowe informacje i budować obraz.  Przykład długiego prompta w Imagen 4   Prompt: captivating photo of a woman in her 20s utilizing a street photography style. Obraz powinien wyglądać jak kadr z filmu z przytłumionymi pomarańczowymi i ciepłymi odcieniami. |

Dodatkowe wskazówki dotyczące pisania promptów w usłudze Imagen:

- **Używaj opisowego języka:** używaj szczegółowych przymiotników i przysłówków, aby stworzyć dla Imagen jasny obraz.
- **Podaj kontekst:** w razie potrzeby podaj dodatkowe informacje, które pomogą AI zrozumieć Twoje potrzeby.
- **Odwołuj się do konkretnych artystów lub stylów:** jeśli masz na myśli konkretną estetykę, pomocne może być odwołanie się do konkretnych artystów lub ruchów artystycznych.
- **Korzystaj z narzędzi do tworzenia promptów:** rozważ użycie narzędzi lub materiałów do tworzenia promptów, które pomogą Ci je ulepszać i uzyskiwać optymalne wyniki.
- **Poprawianie szczegółów twarzy na zdjęciach osobistych i grupowych:** określ szczegóły twarzy jako główny element zdjęcia (np. użyj słowa „portret” w prompcie).

### Generowanie tekstu na obrazach

Modele Imagen mogą dodawać tekst do obrazów, co otwiera nowe możliwości kreatywnego generowania obrazów. Aby w pełni korzystać z tej funkcji, postępuj zgodnie z tymi wskazówkami:

- **Iteruj z pewnością**: może być konieczne wielokrotne generowanie obrazów, aż uzyskasz pożądany efekt. Integracja tekstu w Imagen wciąż się rozwija, a czasami najlepsze wyniki uzyskuje się po kilku próbach.
- **Krótko:** aby uzyskać optymalne wyniki, ogranicz tekst do maksymalnie 25 znaków.
- **Kilka wyrażeń:** eksperymentuj z 2–3 różnymi wyrażeniami, aby podać dodatkowe informacje. Aby uzyskać bardziej przejrzyste kompozycje, unikaj przekraczania 3 wyrażeń.

  ![Przykład generowania tekstu przez Imagen 4](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_generate-text.png?hl=pl)

  Prompt: Plakat z pogrubioną czcionką tekstu „Summerland” jako tytułem, pod którym znajduje się slogan „Summer never felt so good”.
- **Umieszczanie tekstu:** Imagen może próbować umieścić tekst zgodnie z instrukcjami, ale mogą wystąpić pewne odchylenia. Ta funkcja jest stale ulepszana.
- **Styl czcionki Inspire:** określ ogólny styl czcionki, aby subtelnie wpłynąć na wybory Imagen. Nie polegaj na dokładnym odwzorowaniu czcionki, ale spodziewaj się kreatywnych interpretacji.
- **Rozmiar czcionki:** określ rozmiar czcionki lub ogólny wskaźnik rozmiaru (np. *mały*, *średni*, *duży*), aby wpłynąć na generowanie rozmiaru czcionki.

### Parametryzacja promptów

Aby lepiej kontrolować wyniki, możesz sparametryzować dane wejściowe Imagen. Załóżmy na przykład, że chcesz, aby klienci mogli generować logo dla swojej firmy, i chcesz mieć pewność, że logo są zawsze generowane na jednolitym tle. Chcesz też ograniczyć opcje, które klient może wybrać z menu.

W tym przykładzie możesz utworzyć prompt z parametrami podobny do tego:

```
A {logo_style} logo for a {company_area} company on a solid color background. Include the text {company_name}.
```

W niestandardowym interfejsie użytkownika klient może wprowadzać parametry za pomocą menu, a wybrana wartość jest wypełniana w prompcie otrzymywanym przez Imagen.

Na przykład:

1. Prompt: `A minimalist logo for a health care company on a solid color background. Include the text Journey.`

   ![Przykład parametryzacji prompta w Imagen 4 – 1](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_healthcare.png?hl=pl)
2. Prompt: `A modern logo for a software company on a solid color background. Include the text Silo.`

   ![Przykład parametryzacji prompta w Imagen 4 – 2](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_software.png?hl=pl)
3. Prompt: `A traditional logo for a baking company on a solid color background. Include the text Seed.`

   ![Przykład parametryzacji prompta w Imagen 4 – 3](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_baking.png?hl=pl)

### Zaawansowane techniki pisania promptów

Skorzystaj z tych przykładów, aby tworzyć bardziej szczegółowe prompty na podstawie atrybutów, takich jak deskryptory fotografii, kształty i materiały, historyczne kierunki w sztuce i modyfikatory jakości obrazu.

#### Fotografia

- Prompt zawiera: *„Zdjęcie…”*

Aby użyć tego stylu, zacznij od słów kluczowych, które wyraźnie informują Imagen, że szukasz zdjęcia. Rozpocznij prompta od słów *„Zdjęcie”. . ."*. Na przykład:

|  |  |  |
| --- | --- | --- |
| Przykładowy obraz fotorealistyczny 1   Prompt: **Zdjęcie** ziaren kawy w kuchni na drewnianej powierzchni | przykładowy fotorealistyczny obraz 2   Prompt: **Zdjęcie** batona czekoladowego na blacie kuchennym | przykładowy fotorealistyczny obraz 3   Prompt: **Zdjęcie** nowoczesnego budynku z wodą w tle |

Źródło obrazu: każdy obraz został wygenerowany przy użyciu odpowiedniego promptu tekstowego i modelu Imagen 4.

##### Modyfikatory fotograficzne

W przykładach poniżej znajdziesz kilka modyfikatorów i parametrów związanych z fotografią. Możesz połączyć kilka modyfikatorów, aby uzyskać większą kontrolę.

1. **Bliskość aparatu** – *zbliżenie, zdjęcie z daleka*

   |  |  |
   | --- | --- |
   | zdjęcie zrobione z bliska   Prompt: **Zdjęcie z bliska** ziaren kawy | pomniejszone zdjęcie z kamery   Prompt: **Oddalone** zdjęcie małej torebki z  ziarnami kawy w nieuporządkowanej kuchni |
2. **Pozycja kamery** – *z góry, z dołu*

   |  |  |
   | --- | --- |
   | Przykładowe zdjęcie lotnicze   Prompt: **zdjęcie lotnicze** miasta z wieżowcami | przykładowe zdjęcie z widokiem od dołu,   Prompt: Zdjęcie korony drzew w lesie z błękitnym niebem **z perspektywy od dołu** |
3. **Oświetlenie** – *naturalne, efektowne, ciepłe, zimne*

   |  |  |
   | --- | --- |
   | Przykładowe zdjęcie z naturalnym oświetleniem   Prompt: studio photo of a modern arm chair, **natural lighting** | Przykładowy obraz z dramatycznym oświetleniem   Prompt: studio photo of a modern arm chair, **dramatic lighting** |
4. **Ustawienia aparatu** *– rozmycie ruchu, miękka ostrość, bokeh, portret*

   |  |  |
   | --- | --- |
   | przykładowy obraz z rozmyciem ruchu   Prompt: zdjęcie miasta z wieżowcami zrobione z wnętrza samochodu z **rozmyciem w ruchu** | Przykładowy obraz z efektem nieostrości   Prompt: **soft focus** photograph of a bridge in an urban city at night |
5. **Rodzaje obiektywów** – *35 mm, 50 mm, typu rybie oko, szerokokątny, makro*

   |  |  |
   | --- | --- |
   | Przykładowe zdjęcie zrobione obiektywem makro   Prompt: zdjęcie liścia, **obiektyw makro** | przykładowe zdjęcie zrobione obiektywem typu rybie oko   Prompt: street photography, new york city, **fisheye lens** |
6. **Rodzaje filmów** – *czarno-białe, polaroid*

   |  |  |
   | --- | --- |
   | Przykładowe zdjęcie z Polaroida   Prompt: **zdjęcie polaroidowe** przedstawiające psa w okularach przeciwsłonecznych | przykładowe zdjęcie czarno-białe   Prompt: **czarno-białe zdjęcie** psa w okularach przeciwsłonecznych |

Źródło obrazu: każdy obraz został wygenerowany przy użyciu odpowiedniego promptu tekstowego i modelu Imagen 4.

### Ilustracje i dzieła sztuki

- Prompt zawiera: *„A painting of...”*, *„sketch z …”*

Style artystyczne są różne – od monochromatycznych, takich jak szkice ołówkiem, po hiperrealistyczne cyfrowe dzieła sztuki. Na przykład te obrazy zostały wygenerowane na podstawie tego samego prompta, ale w różnych stylach:

*„Zdjęcie [art style or creation technique] kanciastego, sportowego sedana elektrycznego z wieżowcami w tle”*

|  |  |  |
| --- | --- | --- |
| przykładowe obrazy   Prompt: **Rysunek techniczny ołówkiem** przedstawiający kanciasty... | przykładowe obrazy   Prompt: **Rysunek węglem** przedstawiający kanciasty... | przykładowe obrazy   Prompt: **Rysunek kredkami** przedstawiający kanciasty... |

|  |  |  |
| --- | --- | --- |
| przykładowe obrazy   Prompt: **Pastelowy obraz** przedstawiający kanciasty... | przykładowe obrazy   Prompt: **Cyfrowa grafika** przedstawiająca kanciasty... | przykładowe obrazy   Prompt: An **art deco (poster)** of an angular... |

Źródło obrazu: każdy obraz został wygenerowany przy użyciu odpowiedniego promptu tekstowego w modelu Imagen 2.

##### Kształty i materiały

- Prompt zawiera: *„...wykonane z...”*, *„…w kształcie…”*

Jedną z zalet tej technologii jest możliwość tworzenia obrazów, które w inny sposób byłyby trudne lub niemożliwe do uzyskania. Możesz na przykład odtworzyć logo firmy w różnych materiałach i teksturach.

|  |  |  |
| --- | --- | --- |
| Przykład kształtów i materiałów 1   Prompt: torba płócienna **zrobiona** z sera | Przykład kształtów i materiałów 2   Prompt: neon tubes **in the shape** of a bird | kształty i materiały – przykład 3   Prompt: fotel **z papieru**, zdjęcie studyjne, styl origami |

Źródło obrazu: każdy obraz został wygenerowany przy użyciu odpowiedniego promptu tekstowego i modelu Imagen 4.

#### Odwołania do historycznych dzieł sztuki

- Prompt zawiera: *„...w stylu...”*

Niektóre style stały się kultowe na przestrzeni lat. Oto kilka pomysłów na style malarstwa historycznego lub style artystyczne, które możesz wypróbować.

*„wygeneruj obraz w stylu [art period or movement]
: farma wiatrowa”*

|  |  |  |
| --- | --- | --- |
| Przykładowy obraz impresjonizmu   Prompt: wygeneruj obraz **w stylu *impresjonistycznego obrazu***: farma wiatrowa | renesansowy przykład obrazu   Prompt: wygeneruj obraz **w stylu *renesansowego obrazu***: farma wiatrowa | Przykładowy obraz w stylu pop-artu   Prompt: wygeneruj obraz **w stylu *pop-artu***: farma wiatrowa |

Źródło obrazu: każdy obraz został wygenerowany przy użyciu odpowiedniego promptu tekstowego i modelu Imagen 4.

#### Modyfikatory jakości obrazu

Niektóre słowa kluczowe mogą informować model, że szukasz zasobu wysokiej jakości. Przykłady modyfikatorów jakości:

- **Modyfikatory ogólne** – *wysoka jakość, piękny, stylizowany*
- **Zdjęcia** – *4K, HDR, zdjęcie studyjne*
- **Sztuka, ilustracja** – *profesjonalna, szczegółowa*

Poniżej znajdziesz kilka przykładów promptów bez modyfikatorów jakości i tych samych promptów z modyfikatorami jakości.

|  |  |
| --- | --- |
| Przykładowy obraz kukurydzy bez modyfikatorów   Prompt (bez modyfikatorów jakości): zdjęcie łodygi kukurydzy | Przykładowy obraz kukurydzy z modyfikatorami   Prompt (z modyfikatorami jakości): **4k HDR beautiful**   photo of a corn stalk **taken by a   professional photographer** |

Źródło obrazu: każdy obraz został wygenerowany przy użyciu odpowiedniego promptu tekstowego i modelu Imagen 4.

#### Formaty obrazu

Generowanie obrazów w Imagen umożliwia ustawienie 5 różnych formatów obrazu.

1. **Kwadrat** (1:1, domyślny) – standardowe zdjęcie kwadratowe. Ten format jest często używany w postach w mediach społecznościowych.
2. **Pełny ekran** (4:3) – ten format jest często używany w mediach i filmach.
   Jest to też format większości starszych telewizorów (nie panoramicznych) i aparatów średnioformatowych. Obejmuje on większą część sceny w poziomie (w porównaniu z formatem 1:1),
   dlatego jest preferowanym formatem w fotografii.

   |  |  |
   | --- | --- |
   | przykład formatu obrazu   Prompt: zbliżenie na palce muzyka grającego na pianinie, czarno-biały film, vintage (format obrazu 4:3) | przykład formatu obrazu   Prompt: Profesjonalne zdjęcie studyjne frytek dla ekskluzywnej restauracji w stylu magazynu kulinarnego (format obrazu 4:3) |
3. **Pełny ekran w orientacji pionowej** (3:4) – to pełnoekranowy format obrazu obrócony o 90 stopni. Dzięki temu możesz uchwycić więcej sceny w pionie niż w przypadku formatu 1:1.

   |  |  |
   | --- | --- |
   | przykład formatu obrazu   Prompt: kobieta wędrująca po górach, zbliżenie na jej buty odbijające się w kałuży, w tle duże góry, w stylu reklamy, dramatyczne ujęcia (format obrazu 3:4) | przykład formatu obrazu   Prompt: ujęcie z lotu ptaka przedstawiające rzekę płynącą w górę mistycznej doliny (format obrazu 3:4) |
4. **Panoramiczny** (16:9) – ten format zastąpił format 4:3 i jest obecnie najpopularniejszym formatem obrazu w telewizorach, monitorach i ekranach telefonów komórkowych (w orientacji poziomej).
   Użyj tego formatu, jeśli chcesz uchwycić większą część tła (np. malownicze krajobrazy).

   ![przykład formatu obrazu](https://ai.google.dev/static/gemini-api/docs/images/imagen/aspect-ratios_16-9_man.png?hl=pl)

   Prompt: a man wearing all white
   clothing sitting on the beach, close up, golden hour lighting (16:9
   aspect ratio)
5. **Pionowa** (9:16) – ten format jest panoramiczny, ale obrócony. Jest to stosunkowo nowy format obrazu, który zyskał popularność dzięki aplikacjom z krótkimi filmami (np. YouTube Shorts). Używaj tego trybu w przypadku wysokich obiektów o wyraźnej orientacji pionowej, takich jak budynki, drzewa, wodospady lub inne podobne obiekty.

   ![przykład formatu obrazu](https://ai.google.dev/static/gemini-api/docs/images/imagen/aspect-ratios_9-16_skyscraper.png?hl=pl)

   Prompt: cyfrowa wizualizacja ogromnego, nowoczesnego drapacza chmur, który wygląda imponująco i epicko, z pięknym zachodem słońca w tle (format obrazu 9:16)

#### Fotorealistyczne obrazy

Różne wersje modelu generowania obrazów mogą oferować połączenie wyjść artystycznych i fotorealistycznych. W promptach używaj poniższych sformułowań, aby generować bardziej fotorealistyczne wyniki na podstawie tematu, który chcesz wygenerować.

| Przypadek użycia | Rodzaj obiektywu | Ogniskowe | Informacje dodatkowe |
| --- | --- | --- | --- |
| Osoby (portrety) | Powiększenie główne | 24-35mm | film czarno-biały, film noir, głębia ostrości, duotone (wymień 2 kolory) |
| Jedzenie, owady, rośliny (obiekty, martwa natura) | Makro | 60-105mm | Wysoka szczegółowość, precyzyjne ustawianie ostrości, kontrolowane oświetlenie |
| Sport, dzika przyroda (ruch) | Powiększenie teleobiektywu | 100-400mm | Szybka szybkość migawki, śledzenie akcji lub ruchu |
| Astronomiczne, krajobrazowe (szerokokątne) | Szerokokątny | 10-24mm | Długi czas naświetlania, ostra ostrość, długi czas naświetlania, gładka woda lub chmury |

##### Portrety

| Przypadek użycia | Rodzaj obiektywu | Ogniskowe | Informacje dodatkowe |
| --- | --- | --- | --- |
| Osoby (portrety) | Powiększenie główne | 24-35mm | film czarno-biały, film noir, głębia ostrości, duotone (wymień 2 kolory) |

Korzystając z kilku słów kluczowych z tabeli, Imagen może wygenerować te portrety:

|  |  |  |  |
| --- | --- | --- | --- |
| Przykład fotografii portretowej | Przykład fotografii portretowej | Przykład fotografii portretowej | Przykład fotografii portretowej |

Prompt: *Kobieta, portret 35 mm, duotony w odcieniach niebieskiego i szarego*  
Model: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| Przykład fotografii portretowej | Przykład fotografii portretowej | Przykład fotografii portretowej | Przykład fotografii portretowej |

Prompt: *Kobieta, portret 35 mm, film noir*  
Model: `imagen-4.0-generate-001`

##### Obiekty

| Przypadek użycia | Rodzaj obiektywu | Ogniskowe | Informacje dodatkowe |
| --- | --- | --- | --- |
| Jedzenie, owady, rośliny (obiekty, martwa natura) | Makro | 60-105mm | Wysoka szczegółowość, precyzyjne ustawianie ostrości, kontrolowane oświetlenie |

Korzystając z kilku słów kluczowych z tabeli, Imagen może wygenerować te obrazy obiektów:

|  |  |  |  |
| --- | --- | --- | --- |
| przykład fotografii obiektu | przykład fotografii obiektu | przykład fotografii obiektu | przykład fotografii obiektu |

Prompt: *liść maranty, obiektyw makro, 60 mm*  
Model: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| przykład fotografii obiektu | przykład fotografii obiektu | przykład fotografii obiektu | przykład fotografii obiektu |

Prompt: *a plate of pasta, 100mm Macro lens*  
Model: `imagen-4.0-generate-001`

##### Ruch

| Przypadek użycia | Rodzaj obiektywu | Ogniskowe | Informacje dodatkowe |
| --- | --- | --- | --- |
| Sport, dzika przyroda (ruch) | Powiększenie teleobiektywu | 100-400mm | Szybka szybkość migawki, śledzenie akcji lub ruchu |

Korzystając z kilku słów kluczowych z tabeli, Imagen może wygenerować te obrazy w ruchu:

|  |  |  |  |
| --- | --- | --- | --- |
| przykład fotografii ruchu, | przykład fotografii ruchu, | przykład fotografii ruchu, | przykład fotografii ruchu, |

Prompt: *zwycięskie przyłożenie, krótki czas otwarcia migawki, śledzenie ruchu*  
Model: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| przykład fotografii ruchu, | przykład fotografii ruchu, | przykład fotografii ruchu, | przykład fotografii ruchu, |

Prompt: *Jeleń biegnący po lesie, szybka migawka, śledzenie ruchu*  
Model: `imagen-4.0-generate-001`

##### Szerokokątny

| Przypadek użycia | Rodzaj obiektywu | Ogniskowe | Informacje dodatkowe |
| --- | --- | --- | --- |
| Astronomiczne, krajobrazowe (szerokokątne) | Szerokokątny | 10-24mm | Długi czas naświetlania, ostra ostrość, długi czas naświetlania, gładka woda lub chmury |

Korzystając z kilku słów kluczowych z tabeli, Imagen może wygenerować te zdjęcia szerokokątne:

|  |  |  |  |
| --- | --- | --- | --- |
| Przykład fotografii szerokokątnej | Przykład fotografii szerokokątnej | Przykład fotografii szerokokątnej | Przykład fotografii szerokokątnej |

Prompt: *an expansive mountain range, landscape wide angle 10mm*  
Model: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| Przykład fotografii szerokokątnej | Przykład fotografii szerokokątnej | Przykład fotografii szerokokątnej | Przykład fotografii szerokokątnej |

Prompt: *zdjęcie księżyca, astrofotografia, obiektyw szerokokątny 10 mm*  
Model: `imagen-4.0-generate-001`

## Wersje modelu

### Imagen 4 (wycofany)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `imagen-4.0-generate-001`  `imagen-4.0-ultra-generate-001`  `imagen-4.0-fast-generate-001` |
| saveObsługiwane typy danych | **Wejście**  Tekst  **Dane wyjściowe**  Obrazy |
| token\_autoLimity tokenów[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | **Limit tokenów wejściowych**  480 tokenów (tekst)  **Obrazy wyjściowe**  1–4 (Ultra/Standard/Fast) |
| calendar\_monthOstatnia aktualizacja | Czerwiec 2025 r. |

### Imagen 3

Model Imagen 3 został [wyłączony](https://ai.google.dev/gemini-api/docs/deprecations?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-16 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-16 UTC."],[],[]]
