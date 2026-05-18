---
source_url: https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=pt-BR
fetched_at: 2026-05-18T13:04:28.854893+00:00
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

# Inferência prioritária

A API Gemini Priority é um nível de inferência premium projetado para cargas de trabalho essenciais aos negócios que exigem menor latência e maior confiabilidade a um preço premium. O tráfego de nível prioritário tem prioridade sobre o tráfego da API padrão e do nível Flex.

A inferência prioritária está disponível em todos os endpoints da API Interactions.

## Como usar a prioridade

Para usar o nível de prioridade, defina o campo `service_tier` na solicitação como `priority`. O nível padrão será usado se o campo for omitido.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="Triage this critical customer support ticket immediately.",
        service_tier='priority'
    )

    # Validate for graceful downgrade
    # Note: Checking headers might vary by SDK implementation, this is illustrative
    # if interaction.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
    #     print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(interaction.steps[-1].content[0].text)

except Exception as e:
    print(f"Error during API call: {e}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const interaction = await ai.interactions.create({
          model: "gemini-3-flash-preview",
          input: "Triage this critical customer support ticket immediately.",
          service_tier: "priority"
      });

      // Validate for graceful downgrade
      // if (interaction.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
      //     console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      // }

      console.log(interaction.steps.at(-1).content[0].text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
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
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Como funciona a inferência prioritária

A inferência prioritária encaminha solicitações para filas de computação de alta criticidade, oferecendo desempenho rápido e previsível para aplicativos voltados ao usuário. O mecanismo principal é um downgrade suave do lado do servidor para o processamento padrão de tráfego que excede os limites dinâmicos, garantindo a estabilidade do aplicativo em vez de falhar na solicitação.

| Recurso | Prioridade | Padrão | Flex | Lote |
| --- | --- | --- | --- | --- |
| **Preços** | 75 a 100% mais caro que o padrão | Preço total | 50% de desconto | 50% de desconto |
| **Latência** | Segundos | Segundos a minutos | Minutos (meta de 1 a 15 min) | Até 24 horas |
| **Confiabilidade** | Alta (não descartável) | Alta / média-alta | Melhor esforço (descartável) | Alta (para capacidade de processamento) |
| **Interface** | Síncrona | Síncrona | Síncrona | Assíncrona |

### Principais benefícios

- **Baixa latência**: projetado para tempos de resposta de segundos para ferramentas de IA interativas,
  voltadas ao usuário.
- **Alta confiabilidade**: o tráfego é tratado com a maior criticidade e é
  estritamente não descartável.
- **Degradação suave**: picos de tráfego que excedem os limites dinâmicos são
  automaticamente rebaixados para o nível padrão para processamento em vez de falhar,
  evitando interrupções de serviço.
- **Baixa fricção**: usa o mesmo método `create` síncrono que os
  níveis padrão e Flex.

### Casos de uso

O processamento prioritário é ideal para fluxos de trabalho essenciais aos negócios em que o desempenho e a confiabilidade são fundamentais.

- **Aplicativos de IA interativos**: chatbots e copilotos de atendimento ao cliente em que
  os usuários pagam um valor premium e esperam respostas rápidas e consistentes.
- **Mecanismos de decisão em tempo real**: sistemas que exigem resultados altamente confiáveis e de baixa latência
  como triagem de tickets ao vivo ou detecção de fraudes.
- **Recursos premium para clientes**: desenvolvedores que precisam garantir objetivos de nível de serviço (SLOs) mais altos para clientes pagantes.

### Limites de taxas

O consumo prioritário tem limites de taxa próprios, mesmo que o consumo seja contabilizado nos [limites gerais de taxa de tráfego interativo](https://aistudio.google.com/rate-limit?hl=pt-br). Os limites de taxa padrão para inferência prioritária são **0,3 vezes o limite de taxa padrão para modelo / nível**

### Lógica de downgrade suave

Se os limites de prioridade forem excedidos devido ao congestionamento, as solicitações de estouro serão **rebaixadas automaticamente e de maneira suave** para o processamento padrão em vez de falhar com um erro 503 ou 429. As solicitações rebaixadas são cobradas na taxa padrão, não na taxa premium de prioridade.

### Responsabilidade do cliente

- **Monitoramento de respostas**: os desenvolvedores precisam monitorar o `x-gemini-service-tier`
  cabeçalho na resposta da API para detectar se as solicitações estão sendo rebaixadas com frequência para
  `standard`.
- **Repetições**: os clientes precisam implementar a lógica de repetição/espera exponencial para
  erros padrão, como `DEADLINE_EXCEEDED`.

## Preços

A inferência prioritária custa de 75 a 100% mais do que a [API padrão](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) e é cobrada por token.

## Modelos compatíveis

Os seguintes modelos oferecem suporte à inferência prioritária:

| Modelo | Inferência prioritária |
| --- | --- |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pt-br) | ✔️ |

## A seguir

- [Inferência flexível](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=pt-br) para redução de custos.
- [Tokens](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=pt-br): entenda os tokens.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-12 UTC."],[],[]]
