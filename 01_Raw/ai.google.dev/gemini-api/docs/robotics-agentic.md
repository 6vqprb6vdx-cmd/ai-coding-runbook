---
source_url: https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=pl
fetched_at: 2026-09-28T06:19:06.362426+00:00
title: "Agentic Vision \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Agentic Vision

Modele Gemini Robotics ER mogą pisać i wykonywać kod w języku Python, aby manipulować obrazami i stosować logikę przed udzieleniem odpowiedzi. Na tej stronie znajdziesz przykłady wykonywania kodu: wykrywanie obiektów z powiększeniem i przycinaniem, odczytywanie wskazań przyrządów, pomiar płynów, odczytywanie informacji z płytek drukowanych i dodawanie adnotacji do obrazów.

Aby dostosować te przykłady do swojego przypadku użycia, zastąp tekst prompta i przesłany plik obrazu własnymi. Możesz też dostosować żądany schemat JSON w prompcie, aby pasował do struktury danych wyjściowych wymaganej przez Twoją aplikację, lub dodać `system_instruction`, aby wymusić format i precyzję danych wyjściowych.

Pełny kod, który można uruchomić, znajdziesz w
[przewodniku Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Poziom myślenia

Możesz kontrolować poziom myślenia modelu, aby zwiększyć dokładność kosztem opóźnienia. Zadania przestrzenne, takie jak wykrywanie obiektów, działają dobrze przy niskim poziomie myślenia. Złożone zadania, takie jak liczenie lub szacowanie wagi, wymagają wyższego poziomu myślenia.

Poniższy przykład ustawia poziom myślenia na `high` w przypadku złożonego zadania liczenia:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="scene.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": "Identify and count all objects on the table."}
    ],
    generation_config={
        "thinking_level": "high"  # Use "minimal" or "low" for faster spatial tasks
    }
)

print(interaction.output_text)
```

Więcej informacji znajdziesz w sekcji [Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl).

## Wykrywanie obiektów (powiększenie i przycinanie)

Poniższy przykład wykorzystuje wykonywanie kodu do powiększania i przycinania obrazu, aby uzyskać wyraźniejszy widok podczas wykrywania obiektów i zwracania obwiedni.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="sorting.jpeg")

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

Dane wyjściowe modelu będą podobne do tej odpowiedzi JSON:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

Na tym obrazie widać pola zwrócone przez model.

![Przykład pokazujący pola ograniczenia znalezionych obiektów](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=pl)

## Odczytywanie wskazań przyrządu analogowego i stosowanie logiki

Poniższy przykład pokazuje, jak używać modelu do odczytywania wskazań przyrządu analogowego i wykonywania obliczeń czasu. Używa instrukcji systemowej, aby wymusić dane wyjściowe w formacie JSON.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="gauge.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

## Pomiar płynu w pojemniku

Poniższy przykład pokazuje, jak używać wykonywania kodu do pomiaru poziomu płynu w pojemniku.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="fluid.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

## Odczytywanie oznaczeń na płytce drukowanej

Poniższy przykład pokazuje, jak używać wykonywania kodu do odczytywania oznaczeń na płytce drukowanej.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="circuit_board.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

![Przykład pokazujący oznaczenia na płytce drukowanej](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=pl)

## Adnotacja do obrazu

Poniższy przykład pokazuje, jak używać wykonywania kodu do dodawania adnotacji do obrazu (np. rysowania strzałek z instrukcjami utylizacji) i zwracania zmodyfikowanego obrazu.

### Python

```
from google import genai

client = genai.Client()

# Load your image
uploaded_file = client.files.upload(file="sorting.jpeg")

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

Poniżej znajdziesz przykładowy obraz wejściowy.

![Przykład pokazujący zegar do odczytania](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=pl)

Dane wyjściowe modelu będą podobne do tych:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## Co dalej?

- [Orkiestracja zadań](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=pl) – zadania długoterminowe z niestandardowymi interfejsami API robotów.
- [Robotyka ze strumieniowaniem](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl) – dwukierunkowe strumieniowanie w czasie rzeczywistym (tylko Gemini Robotics ER 2).
- [Rozumienie treści wideo](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=pl) – wyszukiwanie momentów i klasyfikacja postępów (tylko Gemini Robotics ER 2).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-08 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-08 UTC."],[],[]]
