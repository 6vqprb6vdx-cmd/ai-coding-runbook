---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=pt-BR
fetched_at: 2026-09-07T05:33:41.916057+00:00
title: "Configurar seu assistente de programa\u00e7\u00e3o com o Gemini MCP e Skills \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Configurar seu assistente de programação com o Gemini MCP e Skills

Os assistentes de programação de IA são poderosos, mas têm limitações: os dados de treinamento são interrompidos em uma data específica, sem novos recursos e mudanças na API. Sem acesso à documentação específica do Gemini, os agentes podem sugerir padrões genéricos em vez de abordagens otimizadas.

Para manter o assistente de programação atualizado com a API Gemini em evolução e o uso recomendado dela, recomendamos configurar o **MCP do Gemini Docs** e melhorar seu ambiente com as **habilidades da API Gemini**. Embora essas ferramentas possam ser usadas de forma independente, elas foram projetadas para funcionar juntas e oferecer cobertura completa.

## Conectar o MCP do Gemini Docs

O Gemini hospeda um servidor público do Protocolo de Contexto de Modelo (MCP) em `https://gemini-api-docs-mcp.dev`. Conectar seu agente de programação a esse servidor garante que todas as consultas tenham acesso às APIs mais recentes, atualizações de código e exemplos de configuração ideais.

Execute o comando a seguir no terminal ou na raiz do projeto do agente para instalar o servidor:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Esse servidor adiciona uma função `search_documentation` que o agente pode usar para recuperar definições de API em tempo real e padrões de integração dos arquivos de documentação oficiais do Gemini.

## Adicionar habilidades de desenvolvimento de API

As habilidades fornecem **regras e práticas recomendadas integradas** (como a aplicação do SDK correto e das versões atuais do modelo) diretamente no contexto do assistente. A habilidade funciona com o serviço MCP do Gemini Docs: se você tiver os dois instalados, a habilidade vai usar o serviço MCP para documentação, mas, mesmo sem o MCP instalado, ela vai buscar `llms.txt` em `ai.google.dev` como um substituto.

Para instalar essas habilidades, use uma das seguintes ferramentas compatíveis. As instruções de instalação para as duas são fornecidas abaixo de cada módulo de habilidade:

- **[skills.sh](https://skills.sh)**: recomendado. O padrão aberto para comportamentos de agentes portáteis.
- **[Context7](https://context7.com)**: com suporte para usuários que já utilizam o ecossistema Context7.

### gemini-api-dev

A habilidade fundamental para o desenvolvimento do Gemini de uso geral. Essa habilidade fornece documentação e práticas recomendadas para:

- Rotear comandos para modelos atuais (por exemplo, Gemini 3.1 Pro/Flash) e evitar modelos obsoletos
- Comandos multimodais, chamada de função, saídas estruturadas e padrões de integração comuns

#### Instalar com skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Instalar com Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Habilidade para criar aplicativos de IA conversacional em tempo real com a API Gemini Live. Essa habilidade fornece documentação e práticas recomendadas para:

- Conexões WebSocket para streaming de baixa latência
- Streaming de áudio, vídeo e texto
- Detecção de atividade de voz e suporte de interrupção

#### Instalar com skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Instalar com Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

Habilidade para criar apps com a
[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br). A API Interactions é a maneira mais simples e melhor de criar com modelos e agentes do Gemini. Essa habilidade abrange:

- Geração de texto, chat multiturno e streaming
- Chamada de função, saída estruturada e geração de imagens
- Execução em segundo plano e agentes Deep Research
- Gerenciamento do estado de conversação do lado do servidor
- Padrões de SDK do Python e TypeScript

#### Instalar com skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Instalar com Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## Confirme a instalação

Após a instalação, confirme se o assistente de programação pode se conectar ao servidor MCP do Gemini Docs e usar as habilidades instaladas.

### 1. Verificar o comportamento do agente

A maneira mais confiável de verificar é fazer uma pergunta técnica ao agente sobre a API Gemini.

**Comando** : "Como faço para usar o armazenamento em cache de contexto com a API Gemini?"

Uma configuração bem-sucedida vai:

- **Fornecer código preciso**: referenciar métodos específicos do Gemini, como `cacheContent` ou `cachedContents.create`, dos endpoints mais recentes.
- **Usar a ferramenta MCP**: mostrar que ela está conectada ao **servidor MCP do Gemini Docs** ou usando a ferramenta `search_documentation` para buscar dados.
- **Invocar habilidades carregadas**: mostrar um indicador de que está "Usando a habilidade: gemini-api-dev" (se estiver usando um wrapper secundário).

### 2. Verificar manifestações e ferramentas

Se o agente der uma resposta geral ou genérica, use os comandos Discovery ou Status específicos do seu ambiente para verificar se o MCP ou a habilidade do Docs está carregada na memória.

| Ambiente | Verificação do MCP | Verificação de habilidades |
| --- | --- | --- |
| **Claude Code** | Digite `/mcp` no terminal para conferir os servidores ativos e as ferramentas `search_documentation`. | Digite `/skills` no terminal para listar todos os manifestos ativos. |
| **Cursor** | Acesse **Configurações > Recursos > MCP**. Verifique se o servidor está "Conectado". | Abra **Configurações > Regras**. Verifique se a habilidade aparece em "O agente decide". |
| **Antigravity** | Confira o status do MCP na barra lateral **Personalizações > Conexões**. | Digite `/skills list` ou confira a barra lateral **Personalizações > Regras**. |
| **CLI do Gemini** | Execute `gemini mcp list` ou use `/mcp list`. | Execute `gemini skills list` ou use o comando de barra `/skills` na sessão. |
| **Copilot** | Digite `@gemini /mcp` para listar os conectores de dados ativos. | Digite `@gemini /skills` (ou `/skills`) para conferir as extensões ativas. |

## Solução de problemas

Se o agente fornecer apenas informações gerais ou não reconhecer métodos específicos do Gemini, verifique o seguinte:

### O agente não descobriu a habilidade

A maioria dos agentes indexa habilidades apenas na inicialização.

**Correção**:reinicie completamente o ambiente de desenvolvimento integrado (Cursor/VS Code) ou saia e reabra o agente baseado em terminal (Claude Code).

### Conflito global x local

Se você instalou com a flag `--global`, o agente poderá ignorá-la em favor de regras específicas do projeto.

**Correção**:tente instalar a habilidade diretamente na raiz do projeto sem a flag global:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Recursos

- [Habilidades da API Gemini no GitHub (em inglês)](https://github.com/google-gemini/gemini-skills)
- [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br)
- [Primeiros passos](https://ai.google.dev/gemini-api/docs/get-started?hl=pt-br)
- [Bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-08 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-08 UTC."],[],[]]
