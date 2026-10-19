---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=pt-BR
fetched_at: 2026-10-19T05:48:04.365837+00:00
title: "Novidades do Gemini 4 Argon \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

Envie comentários

# Novidades do Gemini 4 Argon

O Gemini 4 Argon (`gemini-4-argon`) é nosso modelo mais recente e avançado. Ele pode raciocinar por mais tempo sobre problemas difíceis para gerar resultados melhores em tarefas complexas de programação, agentes, matemática e ciências. O Gemini 4 Argon está disponível pela API Gemini e no Google AI Studio.

O Gemini 4 Argon é compatível com um limite unificado de 1 milhão de tokens de entrada e saída, decodificação longa de até 1 milhão de tokens e níveis de raciocínio ajustáveis (`low`, `medium`, `high`).

[experiment

Teste no AI Studio

Crie apps do zero com o Gemini 4 Argon e o AI Studio.](https://aistudio.google.com/apps?model=gemini-4-argon&hl=pt-br)
[smart\_toy

Galeria de aplicativos

Brinque e remix apps criados com o Gemini 4 Argon.](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=pt-br)
[rocket\_launch

Primeiros passos

Comece a usar o Gemini 4 Argon com comandos iniciais.](https://aistudio.google.com/learn/gemini-4-argon?hl=pt-br)

Este guia explica as novidades do Gemini 4 Argon, as mudanças na API, exemplos de código e orientações de migração.

## Novo modelo

| Modelo | ID do modelo | Nível de raciocínio padrão | Preços | Descrição |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | Disponível até 30 de novembro de 2026 pelo preço inicial de US $2/1 milhão de tokens de entrada e US $10/1 milhão de tokens de saída (US$ 4/1 milhão de entrada e US $20/1 milhão de saída depois disso). Consulte os [preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) para mais detalhes. | Nosso modelo mais avançado, criado para resolver os problemas mais difíceis com profundidade e precisão em tarefas de engenharia de software e trabalho intelectual do mundo real. |

## Guia de início rápido

Use o exemplo a seguir para enviar uma solicitação para `gemini-4-argon` com o `thinking_level` padrão recomendado (`medium`) e um limite de token de saída de 64K:

### Python

```
pip install -U "google-genai>=2.30.1"
```

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
    config=types.GenerateContentConfig(
        max_output_tokens=65536,
        thinking_config=types.ThinkingConfig(thinking_level="medium"),
    ),
)

print(response.text)
```

### JavaScript

```
npm install "@google/genai@>=2.29.1"
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-4-argon",
  contents: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
  config: {
    maxOutputTokens: 65536,
    thinkingConfig: {
      thinkingLevel: "medium",
    },
  },
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."}]
    }],
    "generationConfig": {
      "maxOutputTokens": 65536,
      "thinkingConfig": {
        "thinkingLevel": "medium"
      }
    }
  }'
```

## Novidades do Gemini 4 Argon

- **Limite unificado de 1 milhão de tokens de entrada e saída**:os tokens de entrada, pensamento e saída compartilham uma única janela de 1 milhão de tokens, com um limite de 32 mil por solicitação para chamadas sem streaming e de 64 mil por stream para chamadas com streaming.
- **Decodificação longa de até 1 milhão de tokens**:o modelo pode gerar além do limite por solicitação, até 1 milhão de tokens menos sua entrada. Os SDKs mais recentes da IA generativa do Google continuam disponíveis para você por padrão.
- **Compreensão agêntica de vídeos (GA)**: a [compreensão agêntica de vídeos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pt-br#agentic-video-understanding) agora está em disponibilidade geral.
- **Disponível nos Agentes Gerenciados**:o [agente do Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pt-br) nos Agentes Gerenciados do Gemini agora é compatível com o Gemini 4 Argon.

Para mais detalhes, consulte a [página do modelo Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pt-br). Para mais detalhes, consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-4-argon).

## Saída maior e decodificação longa

Quando uma tarefa exige raciocínio profundo, o Gemini 4 Argon pode pensar por mais tempo e se esforçar mais para resolver problemas complexos de matemática, ciências e programação em uma única geração.

- **Limite unificado de 1 milhão de tokens de entrada e saída**:o Argon pode usar até 1 milhão de tokens, menos os tokens de entrada, para o raciocínio e a saída combinados.
- **Os tokens de raciocínio são contabilizados no `max_output_tokens`**:em tarefas difíceis, o modelo usa mais do seu orçamento de `max_output_tokens` para chegar a uma resposta melhor. Use `thinking_level` para controlar o uso de tokens.
- **Limites por solicitação (64 mil para streaming / 32 mil para não streaming)**: uma solicitação de streaming retorna até 65.536 tokens. Uma solicitação sem streaming retorna até 32.768 tokens, em comparação com 65.536 no Gemini 3.x. Para chamadas REST, esses limites também são os padrões.

Os SDKs mais recentes da IA generativa do Google executam a decodificação longa por padrão. Use o Python `google-genai` 2.30.1 ou mais recente ou o JavaScript `@google/genai` 2.29.1 ou mais recente.

Nessas versões, `automatic_continuation` é `True` por padrão, então não é necessário defini-lo. Quando você define `max_output_tokens` acima do limite por solicitação, `generate_content` e `generate_content_stream` continuam automaticamente entre as solicitações até que o modelo termine ou alcance `max_output_tokens`, retornando uma resposta combinada.

```
response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Write a complete, rigorous proof of the prime number theorem.",
    config=types.GenerateContentConfig(
        max_output_tokens=262144,
        thinking_config=types.ThinkingConfig(thinking_level="high"),
        automatic_continuation=True,  # Default.
    ),
)
```

Para executar o loop por conta própria, defina `automatic_continuation=False`. Se você chamar a REST ou usar um SDK mais antigo, as solicitações vão parar no limite por solicitação. Para loops REST, frameworks de terceiros, contagem de tokens e quando usar a decodificação longa, consulte o [guia de decodificação longa](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=pt-br).

### Como definir limites de tokens de saída

`max_output_tokens` define o total de tokens de processamento e saída para uma geração, incluindo todas as solicitações de continuação. Defina um valor alto o suficiente para que o pensamento não interrompa a resposta. Defina um valor baixo o suficiente para limitar os gastos quando um comando fixo usar todo o orçamento.

Use as orientações a seguir como ponto de partida:

- **Tarefas padrão**:mantenha o padrão.
- **Apps com um limite inferior a 32 mil**:aumente `max_output_tokens` para 32.768. Para usar menos tokens, diminua `thinking_level`.
- **Tarefas que usavam mais de 32 mil tokens antes**:defina `max_output_tokens` como 65.536.
- **Raciocínio e programação complexos**:defina `max_output_tokens` como 131.072 ou 262.144, até 1.048.576 menos os tokens de entrada.

Se uma solicitação usar todo o `max_output_tokens`, ela vai retornar `finish_reason: "MAX_TOKENS"` e incluir um `continuation_token`. Você pode retomar ou começar de novo.

- **Retomar do checkpoint**:envie a solicitação original com o `continuation_token` mais recente e um `max_output_tokens` maior. Se você não gerar `max_output_tokens`, a solicitação vai retornar `400 INVALID_ARGUMENT`.
- **Comece de novo**:envie a solicitação original com um `max_output_tokens` maior e sem `continuation_token`.

### Entender os níveis de raciocínio

O [nível de raciocínio](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=pt-br) é o principal controle sobre qualidade, latência e uso de tokens no Gemini 4 Argon:

| Nível de raciocínio | Uso de tokens | Quando usar |
| --- | --- | --- |
| `low` | Menos tokens, menor latência | Tarefas mais simples e trabalho sensível a custos. Também funciona para tarefas de análise e escrita que exigem um raciocínio simples. A qualidade pode cair em tarefas difíceis. |
| `medium` (padrão) | Equilibrada | Recomendado para a maioria das tarefas, incluindo código complexo e casos de uso agênticos. |
| `high` | Mais tokens, primeiro token mais lento | Raciocínio complexo, matemática e ciências avançadas e as tarefas mais difíceis de código ou agente. Combina bem com a decodificação longa para saídas longas. |

Execute as avaliações nos três níveis com um `max_output_tokens` alto para que o limite não corte as respostas. Em seguida, escolha o menor `thinking_level` que atenda ao seu padrão de qualidade.

## Checklist de migração

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### Migrar para o gemini-4-argon

- **Atualize o ID do modelo**:mude a string do modelo para `gemini-4-argon`.
- **Defina `max_output_tokens` explicitamente**:o padrão é 64 mil para chamadas de streaming e do SDK e 32 mil para chamadas REST que não são de streaming.
- **Aumentar limites inferiores a 32 mil**:aumente qualquer limite inferior a 32 mil para pelo menos 32.768. Use `thinking_level` para reduzir o gasto de tokens.
- **Planeje decodificações longas**:para tarefas acima do limite por solicitação, use o SDK mais recente ou adicione um loop `continuation_token`.
- **Substitua `thinking_budget` por `thinking_level`**:`thinking_budget` ainda funciona e é mapeado para o `thinking_level` mais próximo, mas retorna um aviso. Teste sua carga de trabalho em `low`, `medium` e `high`.
- **Remova o armazenamento em cache de contexto explícito**:o armazenamento em cache explícito (`cachedContents` /
  `caches.create`) não é compatível com o Gemini 4 Argon e retorna um erro.
  Remova as chamadas que criam ou transmitem `cached_content` em `GenerateContentConfig`.
  O [armazenamento em cache implícito](https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=pt-br) é ativado por
  padrão para comandos de pelo menos 4.096 tokens e desconta os tokens de entrada armazenados em cache
  em 95% nas ocorrências em cache.
- **Remover parâmetros descontinuados**:remova `temperature`, `top_p`, `top_k` e `candidate_count` das solicitações. Se fornecidos, os parâmetros de amostragem serão ignorados.
- **Aumente os tempos limite do cliente**:defina os tempos limite do cliente HTTP para pelo menos 20 minutos por chamada.
- **Preserve as assinaturas de pensamento**:transmita o histórico completo da conversa, incluindo as [assinaturas de pensamento](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=pt-br#signatures), em solicitações de vários turnos e de chamada de função.

## Preços

O Gemini 4 Argon está disponível com preço inicial até 30 de novembro de 2026:

- **Tokens de entrada**:US $2,00 por 1 milhão de tokens (US$ 4,00 a partir de 1º de dezembro de 2026)
  - **Tokens de entrada em cache**:o armazenamento em cache implícito reduz o custo da entrada em cache em 95%, para US $0,10 por 1 milhão de tokens (US$ 0,20 a partir de 1º de dezembro de 2026).
- **Tokens de saída, incluindo tokens de raciocínio**:US $10,00 por 1 milhão de tokens (US$ 20,00 a partir de 1º de dezembro de 2026)

O Gemini 4 Argon não está disponível no nível sem custo financeiro. Para ver os níveis de preços completos, consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-4-argon).

## Outros modelos

- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8?hl=pt-br)
- [Gemini 3.6 Flash e 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6?hl=pt-br)
- [Ver todos os modelos](https://ai.google.dev/gemini-api/docs/models?hl=pt-br)

## A seguir

- Leia o [guia para desenvolvedores sobre decodificação longa](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=pt-br) para conferir os padrões completos de streaming, reconexão e contagem de tokens.
- Saiba como os níveis de raciocínio e os resumos de pensamento funcionam no [guia de raciocínio](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=pt-br).
- Teste o Gemini 4 Argon no [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-16 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-16 UTC."],[],[]]
