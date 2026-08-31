---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=pl
fetched_at: 2026-08-31T06:44:00.614459+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Hooks

Haczyki umożliwiają uruchamianie niestandardowych skryptów lub zewnętrznych żądań HTTP bezpośrednio przed lub po wykonaniu kodu przez agenta albo po zmodyfikowaniu przez niego plików w zdalnej piaskownicy. Używaj haczyków, aby rozszerzyć pętlę agenta o automatyczne zabezpieczenia i przepływy pracy w tle, takie jak:

- **egzekwowanie zabezpieczeń i ograniczeń dostępu** przed wykonaniem poleceń powłoki wysokiego ryzyka lub odczytaniem plików z ograniczeniami;
- **automatyzowanie przekształceń w potoku danych** bezpośrednio po utworzeniu lub zmodyfikowaniu plików przez agenta;
- **przesyłanie strumieniowe danych telemetrycznych kontroli przedsiębiorstwa** do zewnętrznych systemów monitorowania po wykonaniu narzędzia.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
            },
        ],
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
    },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## Obsługiwane zdarzenia cyklu życia

Haczyki obsługują 2 zdarzenia w piaskownicy:

| Zdarzenie | Kiedy jest wywoływane | Działanie |
| --- | --- | --- |
| `pre_tool_execution` | Bezpośrednio przed uruchomieniem narzędzia | Może zatwierdzić (`allow`) lub zablokować (`deny`) narzędzie przed jego wykonaniem. Gdy narzędzie jest zablokowane, model widzi powód odrzucenia i dostosowuje się. |
| `post_tool_execution` | Bezpośrednio po zakończeniu działania narzędzia | Uruchamia zadania uzupełniające, takie jak formatowanie kodu, uruchamianie testów jednostkowych lub rejestrowanie danych telemetrycznych. Nie można zablokować ani cofnąć wykonanych działań. |

### `pre_tool_execution`

Jest wywoływane bezpośrednio przed wykonaniem narzędzia. Twój skrypt odczytuje szczegóły wywołania narzędzia z `stdin` i wysyła decyzję w formacie JSON (`allow` lub `deny`) do `stdout`.

**Ładunek wejściowy (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**Odpowiedź wyjściowa (`stdout`):**

Aby zatwierdzić wywołanie narzędzia:

```
{
  "decision": "allow"
}
```

Aby zablokować wywołanie narzędzia i przekazać modelowi opinię:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

Gdy haczyk odrzuci polecenie, wywołanie narzędzia zostanie natychmiast pominięte. Agent zobaczy w bieżącej turze wynik błędu zawierający powód odrzucenia. Model może wtedy samodzielnie poprawić błąd, wybierając alternatywne polecenie lub wyjaśniając użytkownikowi blokadę.

Jeśli skrypt wyśle nierozpoznany format JSON, zwykły tekst lub cokolwiek innego niż `{"decision": "deny"}`, środowisko wykonawcze potraktuje odpowiedź jako zatwierdzenie (`allow`).

### `post_tool_execution`

Jest wywoływane bezpośrednio po zakończeniu działania narzędzia. Twój skrypt odczytuje szczegóły wykonania i stan błędu z `stdin`.

**Ładunek wejściowy (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

Jeśli polecenie powłoki wyświetli błędy w standardowym strumieniu błędów (`stderr`) lub operacja systemu plików się nie powiedzie, do ładunku zostanie dodane pole `"error"` zawierające tekst błędu. Gdy polecenie zakończy się bez błędów, pole `"error"` zostanie całkowicie pominięte.

**Odpowiedź wyjściowa (`stdout`):**

```
{}
```

Ponieważ haczyki po wykonaniu narzędzia działają wyłącznie w przypadku zadań w tle, takich jak formatowanie kodu lub rejestrowanie, środowisko wykonawcze ignoruje wszystkie wartości decyzji zwracane w `stdout`.

## Wykrywanie konfiguracji

Środowisko wykonawcze automatycznie wykrywa definicje haczyków w pliku `.agents/hooks.json` lub `/.agents/hooks.json` w środowisku piaskownicy. Możesz podać `hooks.json` wraz ze skryptami niestandardowymi, korzystając z dowolnego obsługiwanego [źródła środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#mount_from_a_source):

- **Montowanie repozytorium**: repozytorium Git zawierające `.agents/hooks.json` oraz `AGENTS.md`.
- **Cloud Storage (`gcs`):** zasobnik GCS zawierający plik `hooks.json` skopiowany do środowiska.
- **Źródła wbudowane**: surowy ciąg JSON i zawartość skryptu przekazywane w `environment.sources` podczas wywoływania `client.interactions.create`.

### Schemat pliku `hooks.json`

Plik `hooks.json` grupuje definicje zdarzeń (`pre_tool_execution` lub `post_tool_execution`) pod nazwami niestandardowymi. Każdą grupę możesz włączać i wyłączać niezależnie:

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### Składnia i reguły dopasowywania

Każda grupa reguł w `hooks.json` określa, kiedy i jak mają być wywoływane procedury obsługi, za pomocą właściwości `matcher` i `hooks`:

| Pole | Typ | Opis |
| --- | --- | --- |
| `enabled` | `boolean` | Opcjonalnie. Ustaw wartość `false`, aby wyłączyć grupę (domyślnie `true`). |
| `matcher` | `string` | Wzorzec wyrażenia regularnego pasujący do nazw narzędzi docelowych w kontenerze. |
| `hooks` | `array` | Uporządkowana lista definicji procedur obsługi (`command` lub `http`). Procedury obsługi są uruchamiane sekwencyjnie w kolejności deklaracji. |

#### Jak działa ocena wyrażeń regularnych

Gdy agent wywoła narzędzie w piaskownicy, środowisko wykonawcze oceni nazwę kontenera narzędzia na podstawie wzorca `matcher` za pomocą standardowych wyrażeń regularnych RE2. Jeśli wyrażenie regularne pasuje do nazwy narzędzia, wszystkie procedury obsługi w tablicy `hooks` zostaną wykonane w kolejności. Jeśli do tego samego narzędzia pasuje kilka grup reguł, zostaną uruchomione wszystkie odpowiednie tablice procedur obsługi.

Możesz kierować reklamy na dowolną wbudowaną nazwę narzędzia kontenera: wykonywanie kodu (`code_execution`) lub operacje systemu plików (`read_file`, `write_file`, `list_files` i `delete_file`).

#### Typowe wyrażenia dopasowywania

- `"code_execution"`: dokładne dopasowanie ciągu znaków do poleceń powłoki i wykonywania skryptów.
- `"write_file"`: dokładne dopasowanie do tworzenia plików w systemie plików i zapisywania na dysku.
- `"read_file|write_file"`: rozdzielenie pionową kreską umożliwia dopasowanie kilku konkretnych nazw narzędzi w jednej regule.
- `".*_file"`: symbol wieloznaczny wyrażenia regularnego pasujący do dowolnego narzędzia kończącego się na `_file` (np. `read_file`, `write_file` lub `delete_file`). Standardowe wyrażenia regularne RE2 wymagają użycia `.*`; proste symbole powłoki, takie jak `*_file`, są nieprawidłową składnią wyrażenia regularnego i nie będą pasować.
- `".*"` lub `"*"` lub `""`: wzorzec obejmujący wszystkie przypadki, który przechwytuje każde wywołanie narzędzia w kontenerze.

## Typy procedur obsługi

### Haczyki poleceń

Haczyki poleceń wykonują polecenie powłoki lub skrypt w piaskownicy. Skrypt otrzymuje zdarzenie w formacie JSON w `stdin` i wysyła decyzję w formacie JSON w `stdout`.

| Pole | Typ | Opis |
| --- | --- | --- |
| `type` | `string` | Musi mieć wartość `"command"`. |
| `command` | `string` | Wiersz poleceń do uruchomienia w piaskownicy (np. `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | Czas oczekiwania w sekundach. Domyślnie: `30`. |

### Haczyki HTTP

Haczyki HTTP wysyłają zdarzenie w formacie JSON jako żądanie POST do zewnętrznego adresu URL HTTPS bezpośrednio z sieci piaskownicy. Serwer docelowy zwraca decyzję w treści odpowiedzi HTTP w dokładnie tym samym formacie JSON (`{"decision": "allow"}` lub `{"decision": "deny", "reason": "..."}`).

| Pole | Typ | Opis |
| --- | --- | --- |
| `type` | `string` | Musi mieć wartość `"http"`. |
| `url` | `string` | Zewnętrzny punkt końcowy HTTPS, do którego należy wysłać ładunek zdarzenia. |
| `headers` | `object` | Opcjonalne pary klucz-wartość dla niestandardowych nagłówków nie zawierających informacji poufnych (np. `{"X-Event-Source": "agent-sandbox"}`). W przypadku danych uwierzytelniających użyj serwera proxy sieci. |
| `timeout` | `integer` | Czas oczekiwania w sekundach. Domyślnie: `30`. |

#### Serwer proxy ruchu wychodzącego i przekształcanie tokenów

Ponieważ haczyki HTTP są wykonywane bezpośrednio z przestrzeni nazw sieci piaskownicy, żądania wychodzące przechodzą przez przezroczysty serwer proxy ruchu wychodzącego. Ta architektura zapewnia 2 kluczowe zalety związane z bezpieczeństwem:

- **Lista dozwolonych adresów w sieci:** punkty końcowe docelowe muszą być wyraźnie dozwolone w `network.allowlist` środowiska. Serwer proxy blokuje ruch w pętli zwrotnej (`127.0.0.1` lub `localhost`); zawsze kieruj reklamy na zewnętrzne punkty końcowe znajdujące się na liście dozwolonych.
- **Przekształcanie tokenów:** nie musisz przechowywać kluczy interfejsu API ani tajnych tokenów okaziciela w pliku `.agents/hooks.json` ani montować ich w kontenerze. Zamiast tego skonfiguruj reguły przekształcania tokenów w [konfiguracji sieci](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#network-configuration) (`network.allowlist.transform`). Serwer proxy ruchu wychodzącego automatycznie przechwytuje wychodzący ruch haczyków HTTP i wstawia rzeczywiste nagłówki uwierzytelniania przed opuszczeniem piaskownicy.

## Jak środowisko wykonawcze obsługuje decyzje i błędy

- **Synchroniczne oczekiwanie:** agent wstrzymuje działanie i czeka na zakończenie działania haczyków przed kontynuowaniem.
- **Blokowanie wykonywania narzędzia:** jeśli haczyk przed wykonaniem narzędzia zwróci `{"decision": "deny", "reason": "<your reason>"}`, środowisko wykonawcze natychmiast anuluje wywołanie narzędzia. Model zobaczy powód odrzucenia w historii rozmowy i dostosuje się, wybierając bezpieczną alternatywę lub wyjaśniając użytkownikowi blokadę.
- **Obsługa awarii skryptów, błędów HTTP i przekroczeń limitu czasu:** jeśli skrypt polecenia ulegnie awarii (niezerowy kod zakończenia), haczyk HTTP zwróci kod stanu inny niż 2xx (np. błąd serwera 4xx lub 5xx) albo operacja przekroczy limit czasu lub zwróci nierozpoznany format JSON, środowisko wykonawcze potraktuje to jako zatwierdzenie (`allow`). Wykonywanie narzędzia będzie kontynuowane normalnie, więc uszkodzony skrypt lub niedostępny serwer telemetryczny nigdy nie spowoduje zakleszczenia aplikacji.

## Częste zastosowania

### Odzyskiwanie danych w wielu turach w celu zapewnienia prywatności danych i zgodności z przepisami

Gdy haczyk zablokuje dostęp do zasobów z ograniczeniami, takich jak katalogi zawierające informacje umożliwiające identyfikację osoby lub poufne dane finansowe, możesz przekazać `previous_interaction_id` w następnym wywołaniu, aby kontynuować turę w tym samym środowisku. Agent odczyta wyjaśnienie odmowy i automatycznie odzyska dane, wysyłając zapytanie do zatwierdzonych tabel publicznych.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "read_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "read_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"read_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-05-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### Zewnętrzne rejestrowanie kontrolne i dane telemetryczne

Wysyłaj zdarzenia kontrolne w czasie rzeczywistym z piaskownicy do zewnętrznego serwera monitorowania za każdym razem, gdy pliki są odczytywane lub modyfikowane.

- **Dopasowywanie wielu narzędzi:** ponieważ dopasowywanie używa standardowych wyrażeń regularnych, możesz łączyć kilka narzędzi w jednej regule za pomocą pionowych kresek (`read_file|write_file`) lub symboli wieloznacznych (`.*_file`).
- **Ukrywanie informacji poufnych w konfiguracji:** zdefiniuj tokeny uwierzytelniania w [konfiguracji sieci](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#network-configuration) środowiska (`network.allowlist.transform`). Serwer proxy ruchu wychodzącego automatycznie wstawia rzeczywiste tokeny okaziciela w żądaniach wychodzących.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "read_file|write_file",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
                {"domain": "*"},
            ]
        },
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "read_file|write_file",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
    },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"read_file|write_file\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## Ograniczenia

- **Zakres narzędzi piaskownicy:** haczyki przechwytują wbudowane narzędzia w piaskownicy: wykonywanie kodu (`code_execution`) i operacje systemu plików (`read_file`, `write_file`, `list_files` i `delete_file`). Nie są wywoływane w przypadku niestandardowych wywołań funkcji (`function`) ani zewnętrznych narzędzi Model Context Protocol (`mcp_server`) obsługiwanych poza kontenerem.
- **Listy dozwolonych adresów w sieci:** haczyki HTTP działają w sieci kontenera. Musisz wyraźnie zezwolić na adresy URL docelowe w `network.allowlist` środowiska. Serwer proxy blokuje adresy pętli zwrotnej (`localhost`, `127.0.0.1`).
- **Automatyczne zatwierdzanie w przypadku błędów:** jeśli skrypt haczyka ulegnie awarii (niezerowy kod zakończenia), przekroczy limit czasu lub się nie powiedzie, środowisko wykonawcze zarejestruje błąd i zezwoli na kontynuowanie wywołania narzędzia. Dzięki temu uszkodzone skrypty linterów lub zawieszające się procesy nigdy nie spowodują zakleszczenia aplikacji.
- **Ochrona konfiguracji piaskownicy:** ponieważ haczyki są wykonywane w piaskownicy kontenera, agenci z uprawnieniami do zapisywania w systemie plików lub wykonywania kodu powłoki mogą modyfikować lokalny plik `.agents/hooks.json` lub skrypty w obszarach roboczych z możliwością zapisu. Używaj haczyków kontenera jako automatycznych wskazówek dotyczących zasad i zabezpieczeń operacyjnych. Jeśli wymagana jest ścisła ochrona przed manipulacjami w przypadku wykonywania przez niezaufany model, zamontuj źródła konfiguracji z repozytoriów tylko do odczytu.

## Co dalej?

- Dowiedz się, jak skonfigurować trwałe [zdalne piaskownice i środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl).
- Poznaj możliwości i wbudowane narzędzia agenta [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl).
- Zapoznaj się z [omówieniem interfejsu API interakcji](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) w przypadku sesji wieloetapowych i przesyłania strumieniowego.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
