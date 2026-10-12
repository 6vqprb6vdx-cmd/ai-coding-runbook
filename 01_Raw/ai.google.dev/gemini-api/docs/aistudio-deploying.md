---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pt-BR
fetched_at: 2026-10-12T07:04:21.483735+00:00
title: "Implanta\u00e7\u00e3o do Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Implantação do Google AI Studio

Com o Google AI Studio, você pode implantar seus aplicativos de pilha completa diretamente
no modo de criação. Isso oferece um caminho rápido do protótipo para um ambiente de produção gerenciado e escalonável.

## Opções de implantação

Para implantar seu aplicativo no modo Build do AI Studio, os requisitos dependem
do nível que você usa:

- [**Nível Starter do Google Cloud**](https://docs.cloud.google.com/docs/starter-tier?hl=pt-br):
  permite que contas qualificadas publiquem até dois aplicativos full-stack sem
  configurar um projeto na nuvem ou uma conta de faturamento do Google Cloud.
- **Implantação padrão**: exige um projeto na nuvem do Google Cloud vinculado à sua conta do AI Studio e o faturamento ativado nesse projeto.

## Sobre o nível Starter

O nível Starter do Google Cloud oferece um caminho simplificado para que contas qualificadas
implantem aplicativos no Google Cloud diretamente do Google AI Studio. Não é necessário configurar um ambiente completo do Google Cloud ou uma conta de faturamento.

Cada implantação do Google AI Studio cria um serviço correspondente no
Cloud Run. Para serviços implantados no Google AI Studio com o nível
Starter, as seguintes limitações se aplicam:

- É possível implantar até dois serviços.
- Seus serviços são implantados em uma [única região do Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=pt-br).

### Qualificação para o nível Starter

Nem todas as contas estão qualificadas para o nível Starter do Google Cloud. Sua conta poderá não estar qualificada se alguma das seguintes situações se aplicar:

- Você fez login com uma conta do Google Workspace (incluindo assinaturas pagas ou sem custo financeiro do Google Workspace, Google Workspace for Education ou Google para organizações sem fins lucrativos).
- Você tem uma conta de faturamento do Google Cloud ativa ou paga anteriormente.
- No momento, não temos evidências suficientes da atividade da sua conta para conceder acesso ao nível inicial.

A equipe de suporte do Google AI Studio não pode substituir a qualificação para o nível Starter. Se a sua conta não estiver qualificada, anexe uma conta de faturamento e use a [implantação padrão](#standard-deployment) para publicar apps.

## Implantar com o nível Starter

Depois de criar o app no modo de criação, implante-o com o nível Starter:

1. Clique no botão **Publicar** no canto superior direito.
2. Clique em **Primeiros passos**.
3. Clique em **Publicar app**.

Quando a implantação for concluída, o AI Studio vai fornecer um URL do Cloud Run em que você pode
acessar seu aplicativo ativo.

## URLs personalizados para o AI Studio

Ao publicar um aplicativo no Google AI Studio, você pode definir um subdomínio personalizado e
fácil de lembrar em `ai.studio` (por exemplo,
`https://your-app-name.ai.studio`).

O Google AI Studio exige que os subdomínios sejam globalmente exclusivos em todos os projetos
e os atribui por ordem de chegada. Se outro projeto já usar um nome, o AI Studio vai pedir para você escolher outro. Se você
cancelar a publicação ou excluir um aplicativo, o URL personalizado dele será liberado e ficará
disponível para outros usuários reivindicarem.

### Definir um URL personalizado

Para definir ou atualizar um URL personalizado para seu aplicativo:

1. Abra seu aplicativo no Google AI Studio no modo **Criar**.
2. Clique em **Publicar** no canto superior direito.
3. Na configuração de implantação, insira seu subdomínio preferido no campo **URL personalizado** ou aceite o URL sugerido.
4. Clique em **Publicar app**.

Para transferir um URL personalizado para outro aplicativo, primeiro
cancele a publicação ou exclua o aplicativo que está atribuído a esse URL personalizado e depois
publique o novo aplicativo usando o subdomínio escolhido.

### Denunciar problemas de direitos autorais ou marca registrada

Os subdomínios personalizados precisam obedecer aos [Termos de Serviço do Google](https://policies.google.com/terms?hl=pt-br). Se você notar um URL personalizado que viola uma marca registrada ou usa um nome protegido por direitos autorais sem permissão, denuncie usando o [solucionador de problemas legais do Google](https://support.google.com/legal/troubleshooter/1114905?hl=pt-br).

## Implantação padrão

À medida que seus aplicativos evoluem, você pode precisar de recursos além do nível Starter, como cotas mais altas, mais recursos de computação ou outros produtos do Google Cloud não disponíveis nesse nível. Para desbloquear
essas funcionalidades, você pode converter seu projeto totalmente gerenciado do nível Starter em
um projeto padrão do Google Cloud.

Isso garante que você possa dimensionar sem perder o progresso. Siga as etapas para
[criar uma conta do Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=pt-br#create-new-billing-account),
aceitar formalmente os Termos de Serviço padrão do Google Cloud e
[fazer upgrade para um projeto padrão do Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pt-br#upgradee).
Para mais informações, consulte
[Configuração para contas pagas](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pt-br#paid-setup).

Para saber mais sobre os níveis de faturamento, consulte [Faturamento](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br).

## Excluir sua inscrição

Se você não precisar mais do app, siga estas instruções para excluí-lo no Google AI Studio:

1. No Google AI Studio, acesse a
   [página de apps](https://aistudio.google.com/app/apps?hl=pt-br).
2. No menu à esquerda, selecione **Apps**.
3. Passe o cursor sobre o app que você quer excluir.
4. Clique no ícone de lixeira no lado direito da linha para excluir o app.

## A seguir

- Saiba mais sobre o
  [nível Starter do Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pt-br).
- Leia sobre o [faturamento](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br) na API Gemini.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-28 UTC."],[],[]]
