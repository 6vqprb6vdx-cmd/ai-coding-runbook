---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=pt-BR
fetched_at: 2026-08-24T02:31:46.894855+00:00
title: "Erros da API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Erros da API

Esta página fornece uma referência para todos os códigos de erro da API Interactions, descreve o formato da resposta de erro e explica como a API entrega erros para diferentes tipos de solicitação.

## Códigos de erro padrão da API

Esses códigos de erro gerais no nível da solicitação correspondem a códigos de status HTTP padrão.
Use o campo `code` na lógica do aplicativo para processar erros de maneira programática.

| Código | Status do HTTP | Descrição | Ação recomendada |
| --- | --- | --- | --- |
| `invalid_request` | 400 Solicitação inválida | A solicitação está malformada ou contém parâmetros inválidos. | Verifique as entradas na [referência da API](https://ai.google.dev/api/interactions-api?hl=pt-br). |
| `parameter_unknown` | 400 Solicitação inválida | A solicitação contém um parâmetro desconhecido. | Remova o parâmetro não reconhecido e tente de novo. |
| `authentication` | 401 Não autorizado | A chave de API está ausente ou é inválida. | Verifique sua [chave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br). |
| `permission_denied` | 403 Proibido | Sua chave de API não tem permissão para esse recurso. | Verifique as permissões da chave de API e o acesso ao projeto. |
| `not_found` | 404 Não encontrado | O recurso solicitado não foi encontrado. | Verifique o caminho e os parâmetros do recurso. |
| `model_not_found` | 404 Não encontrado | O modelo especificado não foi encontrado. | Verifique o nome do modelo ou use outro. |
| `rate_limit_exceeded` | 429 número excessivo de solicitações | Você excedeu o limite de solicitações ou de tokens por minuto ou por segundo. | Aguarde e tente de novo com uma espera exponencial. |
| `quota_exceeded` | 429 número excessivo de solicitações | Você excedeu sua cota diária. | Aguarde até que a cota seja redefinida ou peça um aumento. |
| `cancelled` | 499 Solicitação encerrada pelo cliente | O cliente cancelou a solicitação antes que ela fosse concluída. | Nenhuma ação é necessária. Isso geralmente significa que o cliente se desconectou. |
| `api_error` | 500 Internal Server Error | Ocorreu um erro inesperado no servidor. | Tente fazer a solicitação novamente. Se o problema persistir, entre em contato com o suporte. |
| `service_unavailable` | 503 Service Unavailable | O serviço está temporariamente sobrecarregado ou inativo. | Aguarde e tente de novo com uma espera exponencial. |

## Códigos de geração bloqueados

Esses códigos de erro indicam que restrições de política, segurança ou conteúdo bloquearam a saída do modelo. Quando você receber um desses códigos, modifique a entrada e tente de novo.

| Código | Descrição |
| --- | --- |
| `safety` | Violações de segurança (conteúdo nocivo) bloquearam a solicitação. |
| `recitation` | Restrições de direitos autorais ou de recitação bloquearam a solicitação. |
| `language` | Um idioma não compatível bloqueou a solicitação. |
| `prohibited_content` | As diretrizes de conteúdo proibido bloquearam a solicitação. |
| `spii` | Restrições de informações sensíveis de identificação pessoal bloquearam a solicitação. |
| `blocklist` | Termos proibidos em uma lista de bloqueio bloquearam a solicitação. |
| `image_safety` | Violações de segurança bloquearam a geração de imagens. |
| `image_prohibited_content` | As diretrizes de conteúdo proibido bloquearam a geração de imagens. |
| `image_recitation` | Restrições de direitos autorais ou de recitação bloquearam a geração de imagens. |
| `image_other` | Motivos não especificados bloquearam a geração de imagens. |
| `content_blocked` | Um motivo de política não especificado bloqueou a solicitação. |

## Códigos de erro de geração

Esses códigos de erro indicam um problema estrutural com a saída gerada do modelo, como uma chamada de função malformada ou uma chamada de ferramenta não declarada.

| Código | Descrição |
| --- | --- |
| `malformed_function_call` | O modelo produziu uma chamada de função que não pôde ser analisada. |
| `malformed_tool_call` | O modelo produziu uma chamada de ferramenta que não pôde ser analisada. |
| `unexpected_tool_call` | O modelo chamou uma ferramenta que não foi declarada na solicitação. |
| `no_image` | O modelo não conseguiu gerar uma imagem. |
| `too_many_tool_calls` | O modelo gerou mais chamadas de ferramenta do que o permitido. |
| `missing_thought_signature` | A resposta não tem uma assinatura de pensamento obrigatória. |

## Formato da resposta de erro

Todos os erros da API Interactions retornam um `error` que contém um `code` e `message`. Por exemplo, a transmissão de um tipo de ferramenta não compatível retorna:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `code` | string | Um código de erro legível por máquina em `snake_case`. |
| `message` | string | Uma descrição legível por humanos do que deu errado. |

## Como os erros são entregues

A API entrega erros de maneira diferente, dependendo se você faz uma solicitação HTTP padrão ou uma solicitação de streaming (SSE).

### Solicitações HTTP padrão

Para solicitações padrão (não de streaming), a API define o código de status da resposta HTTP (como `400 Bad Request`, `401 Unauthorized`, ou `429 Too Many Requests`) e retorna um objeto `error` no corpo da resposta JSON:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Solicitações de streaming (SSE)

Para solicitações de streaming (`stream: true`), a API envia eventos de erro pelo fluxo de eventos enviados pelo servidor (SSE) com `event_type` definido como `"error"`. O campo `error` contém a mesma estrutura de `code` e `message`:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Para o esquema completo de eventos SSE, consulte a [Referência da API Interactions](https://ai.google.dev/api/interactions-api?hl=pt-br).

## A seguir

- [Solução de problemas da API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=pt-br): resolva problemas comuns e cenários de erro.
- [Limites de taxa](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br): saiba mais sobre limites de solicitação e tratamento de cotas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
