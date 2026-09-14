---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=fr
fetched_at: 2026-09-14T05:37:08.424760+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)

Envoyer des commentaires

# Hooks

Les hooks vous permettent d'exécuter des scripts personnalisés ou des requêtes HTTP externes juste avant ou après que l'agent exécute du code ou modifie des fichiers dans son bac à sable distant. Utilisez des hooks pour étendre la boucle de l'agent avec des garde-fous automatisés et des workflows en arrière-plan, par exemple :

- **Appliquer des garde-fous de sécurité et d'accès** avant l'exécution de commandes shell à haut risque ou de lectures de fichiers restreintes.
- **Automatiser les transformations de pipeline de données** juste après qu'un agent crée ou modifie des fichiers.
- **Diffuser la télémétrie d'audit d'entreprise** vers des systèmes de surveillance externes après l'exécution de l'outil.

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

## Événements de cycle de vie compatibles

Les hooks sont compatibles avec deux événements dans le bac à sable :

| Événement | Quand il se déclenche | Description |
| --- | --- | --- |
| `pre_tool_execution` | Juste avant l'exécution d'un outil | Peut approuver (`allow`) ou bloquer (`deny`) l'outil avant son exécution. En cas de blocage, le modèle voit le motif de votre refus et s'adapte. |
| `post_tool_execution` | Juste après la fin d'un outil | Exécute des tâches de suivi telles que le formatage du code, l'exécution de tests unitaires ou la journalisation de la télémétrie. Impossible de bloquer ou d'annuler les actions terminées. |

### `pre_tool_execution`

Se déclenche juste avant l'exécution d'un outil. Votre script lit les détails de l'appel de l'outil à partir de `stdin` et génère sa décision JSON (`allow` ou `deny`) dans `stdout`.

**Charge utile d'entrée (`stdin`) :**

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

**Réponse de sortie (`stdout`) :**

Pour approuver l'appel de l'outil :

```
{
  "decision": "allow"
}
```

Pour bloquer l'appel de l'outil et renvoyer des commentaires au modèle :

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

Lorsqu'un hook refuse une commande, l'appel de l'outil est immédiatement ignoré. L'agent voit un résultat d'erreur contenant le motif de votre refus directement dans son tour actuel. Le modèle peut ensuite s'auto-corriger en choisissant une autre commande ou en expliquant le blocage à l'utilisateur.

Si votre script génère un JSON non reconnu, du texte brut ou tout autre élément que `{"decision": "deny"}`, l'environnement d'exécution traite la réponse comme une approbation (`allow`).

### `post_tool_execution`

Se déclenche juste après la fin d'un outil. Votre script lit les détails de l'exécution et tout état d'erreur à partir de `stdin`.

**Charge utile d'entrée (`stdin`) :**

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

Si une commande shell affiche des erreurs dans l'erreur standard (`stderr`) ou si une opération de système de fichiers échoue, un `"error"` champ contenant le texte de l'erreur est inclus dans la charge utile. Lorsque la commande réussit sans erreur, le `"error"` champ est entièrement omis.

**Réponse de sortie (`stdout`) :**

```
{}
```

Étant donné que les hooks post-outil s'exécutent strictement pour les tâches en arrière-plan telles que le formatage ou la journalisation du code, l'environnement d'exécution ignore toutes les valeurs de décision renvoyées sur `stdout`.

## Découverte de la configuration

L'environnement d'exécution détecte automatiquement les définitions de hook à partir de `.agents/hooks.json` ou `/.agents/hooks.json` dans l'environnement bac à sable. Vous pouvez fournir `hooks.json` avec vos scripts personnalisés à l'aide de n'importe quelle [source d'environnement](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#mount_from_a_source) compatible :

- **Montage de dépôt** : dépôt Git contenant `.agents/hooks.json` avec `AGENTS.md`.
- **Cloud Storage (`gcs`)** : bucket GCS contenant `hooks.json` copié dans l'environnement.
- **Sources intégrées** : chaîne JSON brute et contenu du script transmis dans `environment.sources` lors de l'appel de `client.interactions.create`.

### Schéma `hooks.json`

Un fichier `hooks.json` regroupe les définitions d'événements (`pre_tool_execution` ou `post_tool_execution`) sous des noms personnalisés. Vous pouvez activer ou désactiver chaque groupe indépendamment :

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

### Syntaxe et règles du matcher

Chaque groupe de règles dans `hooks.json` définit quand et comment les gestionnaires se déclenchent à l'aide des propriétés `matcher` et `hooks` :

| Champ | Type | Description |
| --- | --- | --- |
| `enabled` | `boolean` | Facultatif. Définissez la valeur sur `false` pour désactiver le groupe (`true` par défaut). |
| `matcher` | `string` | Modèle d'expression régulière correspondant aux noms d'outils cibles dans le conteneur. |
| `hooks` | `array` | Liste ordonnée des définitions de gestionnaires (`command` ou `http`). Les gestionnaires s'exécutent de manière séquentielle dans l'ordre de déclaration. |

#### Fonctionnement de l'évaluation des expressions régulières

Lorsque l'agent appelle un outil dans le bac à sable, l'environnement d'exécution évalue le nom du conteneur de l'outil par rapport à votre modèle `matcher` à l'aide d'expressions régulières RE2 standards. Si l'expression régulière correspond au nom de l'outil, tous les gestionnaires du tableau `hooks` s'exécutent dans l'ordre. Si plusieurs groupes de règles correspondent au même outil, tous les tableaux de gestionnaires correspondants s'exécutent.

Vous pouvez cibler n'importe quel nom d'outil de conteneur intégré : exécution de code (`code_execution`) ou opérations de système de fichiers (`read_file`, `write_file`, `list_files` et `delete_file`).

#### Expressions de matcher courantes

- `"code_execution"`: correspondance exacte de chaîne pour les commandes shell et les exécutions de scripts.
- `"write_file"`: correspondance exacte pour la création de fichiers de système de fichiers et les écritures sur disque.
- `"read_file|write_file"`: la séparation par un canal correspond à plusieurs noms d'outils spécifiques dans une seule règle.
- `".*_file"` : caractère générique d'expression régulière correspondant à n'importe quel outil se terminant par `_file` (tel que `read_file`, `write_file` ou `delete_file`). Les expressions régulières RE2 standards nécessitent `.*` ; les globs shell simples tels que `*_file` ne sont pas une syntaxe d'expression régulière valide et ne correspondront pas.
- `".*"` ou `"*"` ou `""` : modèle générique qui intercepte chaque appel d'outil dans le conteneur.

## Types de gestionnaires

### Hooks de commande

Les hooks de commande exécutent une commande ou un script shell dans le bac à sable. Le script reçoit le JSON de l'événement sur `stdin` et génère son JSON de décision sur `stdout`.

| Champ | Type | Description |
| --- | --- | --- |
| `type` | `string` | Doit être `"command"`. |
| `command` | `string` | Ligne de commande à exécuter dans le bac à sable (par exemple, `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | Délai avant expiration exprimé en secondes. Valeur par défaut : `30`. |

### Hooks HTTP

Les hooks HTTP envoient le JSON de l'événement en tant que requête POST à une URL HTTPS externe directement depuis le réseau bac à sable. Le serveur cible renvoie sa décision dans le corps de la réponse HTTP au format JSON exact (`{"decision": "allow"}` ou `{"decision": "deny", "reason": "..."}`).

| Champ | Type | Description |
| --- | --- | --- |
| `type` | `string` | Doit être `"http"`. |
| `url` | `string` | Point de terminaison HTTPS externe vers lequel envoyer la charge utile de l'événement. |
| `headers` | `object` | Paires clé-valeur facultatives pour les en-têtes personnalisés non sensibles (tels que `{"X-Event-Source": "agent-sandbox"}`). Pour les identifiants d'authentification, utilisez plutôt le proxy réseau. |
| `timeout` | `integer` | Délai avant expiration exprimé en secondes. Valeur par défaut : `30`. |

#### Proxy de sortie et transformation de jetons

Étant donné que les hooks HTTP s'exécutent directement à partir de l'espace de noms du réseau bac à sable, les requêtes sortantes passent par le proxy de sortie transparent. Cette architecture vous offre deux avantages essentiels en termes de sécurité :

- **Liste d'autorisation réseau** : les points de terminaison cibles doivent être explicitement autorisés dans le `network.allowlist` de votre environnement. Le trafic de rebouclage (`127.0.0.1` ou `localhost`) est bloqué par le proxy. Ciblez toujours les points de terminaison externes autorisés.
- **Transformation de jetons** : vous n'avez pas besoin de stocker les clés API ni les jetons porteurs secrets dans `.agents/hooks.json` ni de les monter dans le conteneur. Configurez plutôt des règles de transformation de jetons dans votre [configuration réseau](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#network-configuration) (`network.allowlist.transform`). Le proxy de sortie intercepte automatiquement le trafic de hook HTTP sortant et injecte vos en-têtes d'authentification réels sur le réseau avant de quitter le bac à sable.

## Gestion des décisions et des échecs par l'environnement d'exécution

- **Attente synchrone** : l'agent s'interrompt et attend la fin de vos hooks avant de continuer.
- **Blocage de l'exécution de l'outil** : si votre hook pré-outil renvoie `{"decision": "deny", "reason": "<your reason>"}`, l'environnement d'exécution annule immédiatement l'appel de l'outil. Le modèle voit le motif de votre refus dans son historique de conversation et s'adapte en choisissant une alternative sûre ou en expliquant le blocage à l'utilisateur.
- **Gestion des plantages de scripts, des erreurs HTTP et des délais avant expiration** : si un script de commande plante (état de sortie non nul), qu'un hook HTTP renvoie un code d'état non 2xx (tel qu'une erreur de serveur 4xx ou 5xx), qu'une opération expire ou qu'elle renvoie un JSON non reconnu, l'environnement d'exécution le traite comme une approbation (`allow`). L'exécution de l'outil se poursuit normalement, de sorte qu'un script défectueux ou un serveur de télémétrie inaccessible ne bloque jamais votre application.

## Cas d'utilisation courants

### Récupération multi-tour pour la confidentialité et la conformité des données

Lorsqu'un hook bloque l'accès à des ressources restreintes, telles que des répertoires contenant des informations permettant d'identifier personnellement l'utilisateur (PII) ou des enregistrements financiers confidentiels, vous pouvez transmettre `previous_interaction_id` lors de l'appel suivant pour continuer le tour dans le même environnement. L'agent lit l'explication du refus et récupère automatiquement les données en interrogeant des tables publiques approuvées.

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

### Journalisation et télémétrie d'audit externes

Envoyez des événements d'audit en temps réel depuis le bac à sable vers un serveur de surveillance externe chaque fois que des fichiers sont lus ou modifiés.

- **Faire correspondre plusieurs outils** : étant donné que les matchers utilisent des expressions régulières standards, vous pouvez combiner plusieurs outils dans une seule règle à l'aide de canaux (`read_file|write_file`) ou de caractères génériques (`.*_file`).
- **Ne pas inclure de secrets dans votre configuration** : définissez des jetons d’authentification dans la [configuration réseau](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr#network-configuration) de votre environnement (`network.allowlist.transform`). Le proxy de sortie injecte automatiquement vos jetons porteurs réels dans les requêtes sortantes.

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

## Limites

- **Champ d'application de l'outil bac à sable** : les hooks interceptent les outils intégrés dans le bac à sable : exécution de code (`code_execution`) et opérations de système de fichiers (`read_file`, `write_file`, `list_files` et `delete_file`). Ils ne se déclenchent pas pour les appels de fonction personnalisés (`function`) ni pour les outils externes Model Context Protocol (`mcp_server`) gérés en dehors du conteneur.
- **Listes d'autorisation réseau** : les hooks HTTP s'exécutent dans le réseau de conteneurs. Vous devez autoriser explicitement les URL cibles dans le `network.allowlist` de votre environnement. Les adresses de rebouclage (`localhost`, `127.0.0.1`) sont bloquées par le proxy.
- **Approbation automatique en cas d'erreur** : si un script de hook plante (état de sortie non nul), expire ou échoue, l'environnement d'exécution enregistre l'échec et autorise la poursuite de l'appel de l'outil. Cela garantit que les scripts de lint défectueux ou les processus bloqués ne provoquent jamais d'interblocage dans vos applications.
- **Protection de la configuration du bac à sable** : étant donné que les hooks s'exécutent dans le bac à sable du conteneur, les agents disposant d'outils d'écriture de système de fichiers ou d'autorisations d'exécution de code shell peuvent modifier les fichiers `.agents/hooks.json` ou les scripts locaux dans des espaces de travail accessibles en écriture. Utilisez les hooks de conteneur comme conseils de règles automatisés et garde-fous opérationnels. Si une résistance stricte à la falsification est requise contre les exécutions de modèles non fiables, montez les sources de configuration à partir de dépôts en lecture seule.

## Étape suivante

- [Découvrez comment configurer des bacs à sable et des environnements distants persistants.](https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr)
- Découvrez les fonctionnalités et les outils intégrés de l'[agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr).
- Consultez la [présentation de l'API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) pour les sessions multi-tours et la diffusion en streaming.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/11 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/11 (UTC)."],[],[]]
