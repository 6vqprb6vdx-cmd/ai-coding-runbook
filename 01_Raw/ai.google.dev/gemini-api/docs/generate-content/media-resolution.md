---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=pl
fetched_at: 2026-07-20T04:44:03.481569+00:00
title: "Rozdzielczo\u015b\u0107 multimedi\u00f3w \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozdzielczość multimediów

Parametr `media_resolution` określa, jak interfejs Gemini API przetwarza dane wejściowe multimediów, takie jak obrazy, filmy i dokumenty PDF, poprzez określenie **maksymalnej liczby tokenów** przydzielonych na dane wejściowe multimediów. Dzięki temu możesz zrównoważyć jakość odpowiedzi z opóźnieniem i kosztem. Więcej informacji o różnych ustawieniach, wartościach domyślnych i ich odpowiednikach w tokenach znajdziesz w sekcji [Liczba tokenów](#token-counts).

Rozdzielczość multimediów możesz skonfigurować na 2 sposoby:

- [Dla każdej części](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl#per-part-media-resolution) (tylko Gemini 3)
- [Globalnie](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl#global-media-resolution) dla całego żądania `generateContent` (wszystkie modele multimodalne)

## Rozdzielczość multimediów dla każdej części (tylko Gemini 3)

Gemini 3 umożliwia ustawienie rozdzielczości multimediów dla poszczególnych obiektów multimedialnych w żądaniu, co pozwala na precyzyjną optymalizację wykorzystania tokenów. W jednym żądaniu możesz mieszać poziomy rozdzielczości. Na przykład możesz użyć wysokiej rozdzielczości w przypadku złożonego diagramu i niskiej rozdzielczości w przypadku prostego obrazu kontekstowego. To ustawienie zastępuje dowolną konfigurację globalną dla określonej części. Ustawienia domyślne znajdziesz w sekcji [Liczba tokenów](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is currently only available in the v1alpha API version. (experimental)
client = genai.Client(
  http_options={
      'api_version': 'v1alpha',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1alpha' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1alpha/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Globalna rozdzielczość multimediów

Możesz ustawić domyślną rozdzielczość dla wszystkich części multimediów w żądaniu za pomocą `GenerationConfig`. Jest to obsługiwane przez wszystkie modele multimodalne. Jeśli żądanie
zawiera zarówno ustawienia globalne, jak i [ustawienia dla każdej części](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl#per-part-media-resolution), ustawienie dla każdej części ma pierwszeństwo w przypadku tego konkretnego elementu.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Dostępne wartości rozdzielczości

Interfejs Gemini API definiuje te poziomy rozdzielczości multimediów:

- `MEDIA_RESOLUTION_UNSPECIFIED`: ustawienie domyślne. Liczba tokenów na tym poziomie znacznie różni się w zależności od tego, czy używasz Gemini 3, czy wcześniejszych modeli Gemini.
- `MEDIA_RESOLUTION_LOW`: mniejsza liczba tokenów, co skutkuje szybszym przetwarzaniem i niższym kosztem, ale mniejszą ilością szczegółów.
- `MEDIA_RESOLUTION_MEDIUM`: równowaga między szczegółowością, kosztem i opóźnieniem.
- `MEDIA_RESOLUTION_HIGH`: większa liczba tokenów, co zapewnia modelowi więcej szczegółów, ale kosztem większego opóźnienia i kosztów.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (tylko dla każdej części): największa liczba tokenów, wymagana w określonych
  przypadkach użycia, np. w przypadku korzystania z [komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl).

Pamiętaj, że `MEDIA_RESOLUTION_HIGH` zapewnia optymalną wydajność w większości przypadków użycia.

Dokładna liczba tokenów wygenerowanych na każdym z tych poziomów zależy zarówno od **typu multimediów** (obraz, film, PDF), jak i **wersji modelu**.

## Liczba tokenów

Tabele poniżej zawierają podsumowanie przybliżonej liczby tokenów dla każdej wartości `media_resolution` i typu multimediów w przypadku każdej rodziny modeli.

**Modele Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **Obraz** | **Film** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (domyślna) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + tekst natywny |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + tekst natywny |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + tekst natywny |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | Nie dotyczy | Nie dotyczy |

**Modele Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Obraz** | **Film** | **PDF (zeskanowany)** | **PDF (natywny)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (domyślna) | 256 + przesuwanie i skanowanie (~2048) | 256 | 256 + OCR | 256 + tekst natywny |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + tekst natywny |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + tekst natywny |
| `MEDIA_RESOLUTION_HIGH` | 256 + przesuwanie i skanowanie | 256 | 256 + OCR | 256 + tekst natywny |

## Wybór odpowiedniej rozdzielczości

- **Domyślna (`UNSPECIFIED`):** zacznij od ustawienia domyślnego. Jest ono dostosowane do zapewnienia równowagi między jakością, opóźnieniem i kosztem w większości typowych przypadków użycia.
- **`LOW`:** używaj w sytuacjach, w których najważniejsze są koszt i opóźnienie, a szczegółowość jest mniej istotna.
- **`MEDIUM` / `HIGH`:** zwiększ rozdzielczość, gdy zadanie wymaga zrozumienia złożonych szczegółów w multimediach. Jest to często potrzebne w przypadku złożonej analizy wizualnej, odczytywania wykresów lub zrozumienia dokumentów zawierających dużo tekstu.
- **`ULTRA HIGH`** – dostępne tylko w przypadku ustawienia dla każdej części. Zalecane w określonych przypadkach użycia, np. w przypadku korzystania z komputera, lub gdy testy wykazują wyraźną poprawę w porównaniu z ustawieniem `HIGH`.
- **Sterowanie dla każdej części (Gemini 3):** optymalizuje wykorzystanie tokenów. Na przykład w przypadku prompta z kilkoma obrazami użyj ustawienia `HIGH` w przypadku złożonego diagramu oraz ustawienia `LOW` lub `MEDIUM` w przypadku prostszych obrazów kontekstowych.

**Zalecane ustawienia**

Poniżej znajdziesz zalecane ustawienia rozdzielczości multimediów dla każdego obsługiwanego typu multimediów.

|  |  |  |  |
| --- | --- | --- | --- |
| **Typ multimediów** | **Zalecane ustawienie** | **Maks. liczba tokenów** | **Wytyczne dotyczące użytkowania** |
| **Grafika** | `MEDIA_RESOLUTION_HIGH` | 1120 | Zalecane w przypadku większości zadań analizy obrazów, aby zapewnić maksymalną jakość. |
| **Pliki PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Optymalne do zrozumienia dokumentu; jakość zwykle osiąga poziom nasycenia przy ustawieniu `medium`. Zwiększenie do `high` rzadko poprawia wyniki OCR w przypadku standardowych dokumentów. |
| **Film** (ogólnie) | `MEDIA_RESOLUTION_LOW` (lub `MEDIA_RESOLUTION_MEDIUM`) | 70 (na klatkę) | **Uwaga:** w przypadku filmów ustawienia `low` i `medium` są traktowane identycznie (70 tokenów), aby zoptymalizować wykorzystanie kontekstu. Jest to wystarczające w przypadku większości zadań rozpoznawania i opisywania działań. |
| **Film** (zawierający dużo tekstu) | `MEDIA_RESOLUTION_HIGH` | 280 (na klatkę) | Wymagane tylko wtedy, gdy przypadek użycia obejmuje odczytywanie tekstu (OCR) lub małych szczegółów w klatkach filmu. |

Zawsze testuj i oceniaj wpływ różnych ustawień rozdzielczości na konkretną aplikację, aby znaleźć najlepszy kompromis między jakością, opóźnieniem i kosztem.

## Podsumowanie zgodności wersji

- Wyliczenie `MediaResolution` jest dostępne w przypadku wszystkich modeli obsługujących dane wejściowe multimediów.
- Liczba tokenów powiązana z każdym poziomem wyliczenia **różni się** w zależności od tego, czy używasz modeli Gemini 3, czy wcześniejszych wersji Gemini.
- Ustawienie `media_resolution` w poszczególnych obiektach `Part` jest **dostępne tylko w przypadku modeli Gemini 3**.

## Dalsze kroki

- Więcej informacji o możliwościach multimodalnych interfejsu Gemini API znajdziesz w
  [przewodnikach dotyczących rozpoznawania obrazów](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=pl), [rozpoznawania filmów](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pl) i
  [rozpoznawania dokumentów](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-24 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-24 UTC."],[],[]]
