---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=pt-BR
fetched_at: 2026-08-10T03:11:24.328680+00:00
title: "Resolver problemas do Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Resolver problemas do Google AI Studio

Esta página oferece sugestões para resolver problemas do Google AI Studio.

## Entender erros de acesso restrito 403

Se você receber um erro de acesso restrito 403, significa que está usando o Google AI Studio de uma
maneira que não segue os [Termos de Serviço](https://ai.google.dev/terms?hl=pt-br). Um motivo comum é
que você não está em uma [região aceita](https://ai.google.dev/available_regions?hl=pt-br).

## Resolver respostas sem conteúdo no Google AI Studio

Uma mensagem warning **Sem conteúdo** aparece no
Google AI Studio se o conteúdo for bloqueado por qualquer motivo. Para mais detalhes,
passe o ponteiro sobre **Sem conteúdo** e clique
warning **Segurança**.

Se a resposta foi bloqueada devido às [configurações de segurança](https://ai.google.dev/docs/safety_setting?hl=pt-br) e
você considerou os [riscos de segurança](https://ai.google.dev/docs/safety_guidance?hl=pt-br) para seu caso de uso, você
pode modificar as
[configurações de segurança](https://ai.google.dev/docs/safety_setting?hl=pt-br#safety_settings_in_makersuite)
para influenciar a resposta retornada.

Se a resposta foi bloqueada, mas não devido às configurações de segurança, a consulta ou
resposta pode violar os [Termos de Serviço](https://ai.google.dev/terms?hl=pt-br) ou não ser aceita.

## Verificar o uso e os limites de tokens

Quando você tem um comando aberto, o botão **Visualização de texto** na parte de baixo da tela mostra os tokens usados no momento para o conteúdo do comando e a contagem máxima de tokens para o modelo que está sendo usado.

## Permissões do Cloud IAM do Google Cloud para o AI Studio

Os membros de um projeto na nuvem do Google Cloud precisam de permissões específicas do Identity and Access Management (IAM) para realizar ações no Google AI Studio. Para mais informações sobre essas identidades, consulte a [visão geral dos principais do IAM](https://cloud.google.com/iam/docs/principals?hl=pt-br).

Os usuários com as funções de **Editor** ou **Proprietário** no projeto associado do Google Cloud têm permissões completas para visualizar painéis e gerenciar chaves de API do Gemini. Os usuários com a função de **Leitor** podem visualizar painéis e chaves de API, mas não podem criar, atualizar ou excluir.

Para um controle mais granular, consulte a tabela a seguir para conferir as permissões específicas necessárias para cada recurso do AI Studio. Para instruções sobre como conceder essas permissões, consulte [Conceder, alterar e revogar o acesso a recursos](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=pt-br) na documentação do Google Cloud.

| Recurso do AI Studio | Permissões do IAM obrigatórias | Outros requisitos |
| --- | --- | --- |
| **Pesquisar projeto** (importar projetos) | `resourcemanager.projects.get` |  |
| **Renomear projeto** | `resourcemanager.projects.update` |  |
| **Mostrar nível de cota** | N/A |  |
| **Criar chave de API** | Ter permissões de **Pesquisar projeto** e:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **Listar chaves de API** | Ter permissões de **Pesquisar projeto** e:  `apikeys.keys.list` `serviceusage.services.get` | O projeto na nuvem do Google Cloud precisa ter a [API Generative Language](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=pt-br) ativada. |
| **Renomear chaves de API** | `apikeys.keys.update` |  |
| **Excluir chaves de API** | `apikeys.keys.delete` |  |
| **Painel de uso** | Ter permissões de **Pesquisar projeto** e:  `monitoring.timeSeries.list` |  |
| **Painel de limites de taxa** | Ter permissões do **Painel de uso** e:  `cloudquotas.quotas.get` |  |
| **Gasto (limite de faturamento)** | `billing.resourceCosts.get` (para visualizar o gasto) `billing.resourcebudgets.read` (para visualizar o limite) `billing.resourcebudgets.write` (para definir o limite) |  |
| **Painel de faturamento** | `billing.accounts.get` |  |

### Outras verificações de acesso

Além das permissões do IAM do Google Cloud, o AI Studio também realiza verificações de segurança e compliance. Você pode encontrar um erro `PERMISSION_DENIED` ou de restrição de acesso na interface do AI Studio ou nas respostas da API se não atender aos seguintes requisitos:

- **Verificações de segurança**:sua solicitação precisa passar por verificações de segurança automatizadas.
- **Termos de Serviço**:você precisa aceitar os Termos de Serviço do Google e os Termos de Serviço adicionais da IA generativa.
- **Região aceita:** você precisa estar em uma [região aceita](https://ai.google.dev/gemini-api/docs/available-regions?hl=pt-br).
- **Confiança e segurança**:o projeto na nuvem do Google Cloud não pode ser sinalizado por abuso.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-29 UTC."],[],[]]
