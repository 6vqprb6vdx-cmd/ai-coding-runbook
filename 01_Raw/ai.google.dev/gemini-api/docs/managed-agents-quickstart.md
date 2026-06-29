---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pt-BR
fetched_at: 2026-06-29T05:32:58.185886+00:00
title: "Guia de in\u00edcio r\u00e1pido dos agentes gerenciados \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia de início rápido dos agentes gerenciados

Neste guia, você aprende a criar e usar agentes gerenciados na API Gemini usando o [agente Antigravity](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=pt-br). Você vai fazer sua primeira chamada de agente, continuar uma conversa de várias rodadas, transmitir a resposta, baixar arquivos da sandbox e trabalhar com o agente gerenciado Antigravity.

## Executar sua primeira interação com o agente

Uma única chamada para a [API Interactions](https://ai.google.dev/gemini-api/docs?hl=pt-br) provisiona um sandbox do Linux, executa o loop do agente e retorna o resultado. Você vai definir três parâmetros:

- Transmita o `agent` como `"antigravity-preview-05-2026",`, que é a versão atual do nosso agente gerenciado predefinido e de uso geral.
- Defina `environment="remote"` para provisionar um novo ambiente de sandbox.
- Crie uma entrada, definindo o que você quer que o agente faça.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

A resposta retorna um objeto `Interaction`. Armazene `interaction.id` e `interaction.environment_id` para continuar a conversa na mesma sandbox. Use `interaction.output_text` para acessar a resposta final do agente. `interaction.steps` lista cada etapa realizada pelo agente (raciocínio, chamadas de ferramentas, execução de código).

## Continuar a conversa (vários turnos)

A API rastreia duas dimensões de estado independentes:

- **Contexto da conversa**:histórico de chat, rastreamento de raciocínio, uso de ferramentas, uso de `previous_interaction_id`.
- [**Estado do ambiente**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br):arquivos, pacotes instalados e estado da sandbox, usando `environment`.

Transmita os dois no lugar respectivo para retomar:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

Os arquivos do turno 1 (`fibonacci.txt`) permanecem no turno 2. O agente também retém o contexto da conversa.

É possível misturar e combinar estes itens de forma independente:

- **Limpar conversa, manter arquivos**:omita `previous_interaction_id` e transmita apenas o ID do ambiente usando `environment` para uma nova conversa no mesmo espaço de trabalho.
- **Manter conversa, novo espaço de trabalho**:transmita `previous_interaction_id` e defina `environment="remote"` para um novo sandbox.

### Compactação automática de contexto

Em conversas longas e de várias interações, o histórico bruto de etapas de raciocínio, chamadas de ferramentas e conteúdo de arquivos grandes pode crescer rapidamente e consumir um espaço de contexto significativo. Para evitar erros de limite de token e manter o foco do agente (evitando a "deterioração do contexto"), a API Managed Agents tem uma etapa nativa de compactação de contexto em torno de 135 mil tokens. Isso acontece automaticamente.

## Mostrar composição da resposta

Para tarefas de longa duração, é possível transmitir a resposta para ver o agente trabalhar em tempo real:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

O streaming retorna um iterável de deltas de etapa, que são texto incremental, tokens de raciocínio e atualizações de chamadas de função. Saiba como transmitir respostas no [guia de streaming](https://ai.google.dev/gemini-api/docs/streaming?hl=pt-br).

## Baixar arquivos do ambiente

Quando o agente cria arquivos dentro da sandbox. Faça o download usando a API Files com uma solicitação HTTP direta (ainda não há um método de SDK):

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## Salvar um agente gerenciado

Nas etapas anteriores, usamos o agente Antigravity padrão e o personalizamos inline. Depois de iterar na configuração (instruções, habilidades e ambiente), você pode salvá-la como um agente gerenciado. Isso permite que você o invoque por ID sem repetir a configuração.

Ao salvar um agente, você define um `base_environment` (de fontes ou bifurcando um ambiente existente). O agente vai usar esse ambiente em todas as novas interações.

**De fontes**:defina fontes inline ou de outras fontes, como GitHub ou Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Invocar o agente gerenciado

Depois de salvar um agente gerenciado, você pode invocá-lo por ID. Cada invocação ramifica o ambiente de base, então cada execução começa do zero:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## A seguir

- [Agente antigravidade](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br): recursos, ferramentas compatíveis, entrada multimodal, preços e limitações.
- [Como criar agentes gerenciados](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pt-br): amplie o Antigravity com suas próprias instruções, habilidades e dados.
- [Ambientes](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br): fontes, rede, ciclo de vida, limites de recursos.
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br): a API subjacente para modelos e agentes.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-22 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-22 UTC."],[],[]]
