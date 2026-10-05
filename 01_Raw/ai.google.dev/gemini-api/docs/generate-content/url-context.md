---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/url-context?hl=de
fetched_at: 2026-10-05T06:28:31.215535+00:00
title: "URL-Kontext \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# URL-Kontext

Mit dem Tool „URL-Kontext“ können Sie den Modellen zusätzlichen Kontext in Form von URLs zur Verfügung stellen. Wenn Sie URLs in Ihre Anfrage einfügen, greift das Modell auf die Inhalte dieser Seiten zu (sofern es sich nicht um einen URL-Typ handelt, der im Abschnitt zu den[Beschränkungen](#limitations)aufgeführt ist), um seine Antwort zu informieren und zu verbessern.

Das Tool „URL-Kontext“ ist für Aufgaben wie die folgenden nützlich:

- **Daten extrahieren**: Bestimmte Informationen wie Preise, Namen oder wichtige
  Ergebnisse aus mehreren URLs abrufen.
- **Dokumente vergleichen**: Mehrere Berichte, Artikel oder PDFs analysieren, um
  Unterschiede zu ermitteln und Trends zu verfolgen.
- **Inhalte zusammenführen und erstellen**: Informationen aus mehreren Quell-URLs kombinieren, um genaue Zusammenfassungen, Blogposts oder Berichte zu erstellen.
- **Code und Dokumente analysieren**: Auf ein GitHub-Repository oder eine technische Dokumentation verweisen, um Code zu erklären, Einrichtungsanleitungen zu erstellen oder Fragen zu beantworten.

Im folgenden Beispiel wird gezeigt, wie Sie zwei Rezepte von verschiedenen Websites vergleichen.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.6-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## Funktionsweise

Das Tool „URL-Kontext“ verwendet einen zweistufigen Abrufprozess, um Geschwindigkeit, Kosten und Zugriff auf aktuelle Daten auszubalancieren. Wenn Sie eine URL angeben, versucht das Tool zuerst, die Inhalte aus einem internen Index-Cache abzurufen. Dieser dient als hochoptimierter Cache. Wenn eine URL nicht im Index verfügbar ist (z. B. wenn es sich um eine sehr neue Seite handelt), führt das Tool automatisch einen Live-Abruf durch.
Dabei wird direkt auf die URL zugegriffen, um die Inhalte in Echtzeit abzurufen.

## Kombination mit anderen Tools

Sie können das Tool „URL-Kontext“ mit anderen Tools kombinieren, um leistungsstärkere Workflows zu erstellen.

[Gemini 3-Modelle](#supported-models) unterstützen die Kombination von integrierten Tools
(z. B. „URL-Kontext“) mit benutzerdefinierten Tools (Funktionsaufrufe). Weitere Informationen finden Sie auf der
[Seite zu Tool-Kombinationen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de).

### Fundierung mit der Suche

Wenn sowohl „URL-Kontext“ als auch
[„Fundierung mit der Google Suche“](https://ai.google.dev/gemini-api/docs/grounding?hl=de) aktiviert sind,
kann das Modell seine Suchfunktionen verwenden, um
relevante Informationen online zu finden. Anschließend kann es mit dem Tool „URL-Kontext“ ein besseres
Verständnis der gefundenen Seiten erhalten. Dieser Ansatz ist nützlich für Prompts, die sowohl eine umfassende Suche als auch eine detaillierte Analyse bestimmter Seiten erfordern.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.6-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Antwort verstehen

Wenn das Modell das Tool „URL-Kontext“ verwendet, enthält die Antwort ein `url_context_metadata`-Objekt. In diesem Objekt sind die URLs aufgeführt, von denen das Modell Inhalte abgerufen hat, sowie der Status der einzelnen Abrufversuche. Das ist nützlich für die Überprüfung und Fehlerbehebung.

Im Folgenden sehen Sie ein Beispiel für diesen Teil der Antwort (Teile der Antwort wurden aus Gründen der Übersichtlichkeit weggelassen):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Vollständige Informationen zu diesem Objekt finden Sie in der
[`UrlContextMetadata` API-Referenz](https://ai.google.dev/api/generate-content?hl=de#UrlContextMetadata).

### Sicherheitschecks

Das System führt eine Inhaltsmoderationsprüfung für die URL durch, um zu bestätigen, dass sie den Sicherheitsstandards entspricht. Wenn die von Ihnen angegebene URL diese Prüfung nicht besteht, erhalten Sie für `url_retrieval_status` den Wert `URL_RETRIEVAL_STATUS_UNSAFE`.

### Tokenanzahl

Die Inhalte, die von den in Ihrem Prompt angegebenen URLs abgerufen werden, werden als Teil der Eingabetokens gezählt. Die Tokenanzahl für Ihren Prompt und
die Tool-Nutzung finden Sie im [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=de#UsageMetadata)
Objekt der Modellausgabe. Hier ist ein Beispiel für die Ausgabe:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

Der Preis pro Token hängt vom verwendeten Modell ab. Weitere Informationen finden Sie auf der
[Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

## Unterstützte Modelle

| Modell | URL-Kontext |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=de) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=de) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/generate-content/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Best Practices

- **Bestimmte URLs angeben**: Die besten Ergebnisse erzielen Sie, wenn Sie direkte URLs zu den
  Inhalten angeben, die das Modell analysieren soll. Das Modell ruft nur Inhalte von den von Ihnen angegebenen URLs ab, nicht von verschachtelten Links.
- **Zugänglichkeit prüfen**: Prüfen Sie, ob die von Ihnen angegebenen URLs nicht zu
  Seiten führen, für die eine Anmeldung erforderlich ist oder die sich hinter einer Paywall befinden.
- **Vollständige URL verwenden**: Geben Sie die vollständige URL einschließlich des Protokolls an
  (z.B. https://www.google.com anstelle von google.com).

## Beschränkungen

- Funktionsaufrufe: Die Tool-Nutzung (URL-Kontext, Fundierung mit der Google Suche usw.) mit Funktionsaufrufen wird derzeit nicht unterstützt.
- Anfragelimit: Das Tool kann bis zu 20 URLs pro Anfrage verarbeiten.
- Größe der URL-Inhalte: Die maximale Größe für Inhalte, die von einer einzelnen URL abgerufen werden, beträgt 34 MB.
- Öffentliche Zugänglichkeit: Die URLs müssen öffentlich im Web zugänglich sein.
  Localhost-Adressen (z.B. localhost, 127.0.0.1), private Netzwerke und Tunneling-Dienste (z.B. ngrok, pinggy) werden nicht unterstützt.
- Nur Gemini API: „URL-Kontext“ ist nur in der Gemini API verfügbar, nicht über die Gemini Enterprise Agent Platform.

### Unterstützte und nicht unterstützte Inhaltstypen

Das Tool kann Inhalte aus URLs mit den folgenden Inhaltstypen extrahieren:

- Text (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- Bild (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Die folgenden Inhaltstypen werden **nicht** unterstützt:

- Paywall-Inhalte
- YouTube-Videos (Informationen zum Verarbeiten von YouTube-URLs finden Sie unter
  [Video-Understanding](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#youtube))
- Google Workspace-Dateien wie Google Docs-Dokumente oder Google-Tabellen
- Video- und Audiodateien

## Nächste Schritte

- Weitere Beispiele finden Sie im [Cookbook zum Tool „URL-Kontext“](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=de#url-context).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
