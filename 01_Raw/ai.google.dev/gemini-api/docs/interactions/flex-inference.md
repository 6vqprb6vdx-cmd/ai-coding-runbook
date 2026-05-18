---
source_url: https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=pt-BR
fetched_at: 2026-05-18T13:05:16.944967+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Inferência flexível

A API Gemini Flex é um nível de inferência que oferece uma redução de custo de 50% em comparação com as taxas padrão, em troca de latência variável e disponibilidade do melhor esforço. Ele foi projetado para cargas de trabalho tolerantes à latência que exigem processamento síncrono, mas não precisam do desempenho em tempo real da API padrão.

## Como usar o Flex

Para usar o nível Flex, especifique `service_tier` como `flex` na solicitação. Por padrão, as solicitações usam a camada padrão se esse campo for omitido.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.steps[-1].content[0].text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            input: 'Analyze this dataset for trends...',
            service_tier: 'flex'
        });
        console.log(interaction.steps.at(-1).content[0].text);
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}
await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3-flash-preview",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Como a inferência do Flex funciona

A inferência do Gemini Flex faz a ponte entre a API padrão e o tempo de resposta de 24 horas da [API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br). Ele usa capacidade de computação fora do pico e "descartável" para oferecer uma solução econômica para tarefas em segundo plano e fluxos de trabalho sequenciais.

| Recurso | Flex | Prioridade | Padrão | Lote |
| --- | --- | --- | --- | --- |
| **Preços** | 50% de desconto | 75 a 100% mais do que o Standard | Preço total | 50% de desconto |
| **Latência** | Minutos (meta de 1 a 15 minutos) | Baixo (segundos) | Segundos para minutos | Até 24 horas |
| **Confiabilidade** | Melhor esforço (descartável) | Alta (não descartável) | Alta / Média-alta | Alta (para capacidade de processamento) |
| **Interface** | Síncrona | Síncrona | Síncrona | Assíncrono |

### Principais vantagens

- **Eficiência de custos**: economia substancial para avaliações de não produção, agentes em segundo plano e aprimoramento de dados.
- **Baixa fricção**: basta adicionar um único parâmetro às suas solicitações atuais.
- **Fluxos de trabalho síncronos**: ideais para cadeias de API sequenciais em que a próxima solicitação depende da saída da anterior, o que os torna mais flexíveis do que o Batch para fluxos de trabalho com agentes.

### Casos de uso

- **Avaliações off-line**: execução de testes de regressão ou rankings de "LLM como juiz".
- **Agentes em segundo plano**: tarefas sequenciais, como atualizações de CRM, criação de perfis ou moderação de conteúdo, em que minutos de atraso são aceitáveis.
- **Pesquisa limitada pelo orçamento**: experimentos acadêmicos que exigem um alto volume de tokens com um orçamento limitado.

### Limites de taxas

O tráfego de inferência flexível conta para os [limites de taxa](https://aistudio.google.com/rate-limit?hl=pt-br) gerais, mas não oferece limites estendidos como a [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br).

### Capacidade descartável

O tráfego flexível é tratado com prioridade mais baixa. Se houver um pico no tráfego padrão, as solicitações flexíveis poderão ser interrompidas ou removidas para garantir a capacidade dos usuários de alta prioridade. Se você estiver procurando inferência de alta prioridade, confira
[Inferência de prioridade](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=pt-br)

### Códigos de erro

Quando a capacidade flexível não está disponível ou o sistema está congestionado, a API retorna códigos de erro padrão:

- **503 Serviço indisponível**: o sistema está na capacidade máxima.
- **429 Há muitas solicitações**: limites de taxa ou esgotamento de recursos.

### Responsabilidade do cliente

- **Sem substituição do lado do servidor**: para evitar cobranças inesperadas, o sistema não
  fará upgrade automático de uma solicitação flexível para o nível Standard se a capacidade flexível estiver
  cheia.
- **Novas tentativas**: é necessário implementar sua própria lógica de novas tentativas do lado do cliente com
  espera exponencial.
- **Tempos limite**: como as solicitações Flex podem ficar em uma fila, recomendamos aumentar os tempos limite do lado do cliente para 10 minutos ou mais para evitar o fechamento prematuro da conexão.

## Ajustar janelas de tempo limite

É possível configurar tempos limite por solicitação para a API REST e as bibliotecas de cliente.
Sempre verifique se o tempo limite do lado do cliente cobre a janela de espera pretendida do servidor (por exemplo, 600 segundos ou mais para filas de espera flexíveis). Os SDKs esperam valores de tempo limite em milissegundos.

### Tempos limite por solicitação

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="why is the sky blue?",
        service_tier="flex",
    )
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: "gemini-3-flash-preview",
            input: "why is the sky blue?",
            service_tier: "flex",
        }, {timeout: 900000});
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}

await main();
```

## Implementar novas tentativas

Como o Flex pode ser descartado e falha com erros 503, confira um exemplo de
implementação opcional da lógica de repetição para continuar com solicitações com falha:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3-flash-preview",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3-flash-preview",
                    input="Analyze this batch statement."
                )

# Usage
interaction = call_with_retry()
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3-flash-preview",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3-flash-preview",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

## Preços

A inferência flexível custa 50% da [API padrão](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br)
e é cobrada por token.

## Modelos compatíveis

Os seguintes modelos são compatíveis com a inferência flexível:

| Modelo | Inferência flexível |
| --- | --- |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pt-br) | ✔️ |

## A seguir

- [Inferência de prioridade](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=pt-br) para latência ultrabaixa.
- [Tokens](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=pt-br): entenda os tokens.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-12 UTC."],[],[]]
