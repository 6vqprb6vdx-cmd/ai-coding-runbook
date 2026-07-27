---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-BR
fetched_at: 2026-07-27T04:36:52.227413+00:00
title: "Limites de taxas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Limites de taxas

Os limites de taxa regulam o número de solicitações que você pode fazer para a API Gemini
em um determinado período. Esses limites ajudam a manter o uso justo, proteger contra
abusos e manter o desempenho do sistema para todos os usuários.

[Conferir seus limites de taxa ativos no AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=pt-br)

## Como funcionam os limites de taxa

Os limites de taxa geralmente são medidos em três dimensões:

- Solicitações por minuto (**RPM**)
- Tokens por minuto (entrada) (**TPM**)
- Solicitações por dia (**RPD**)

Seu uso é avaliado em relação a cada limite, e exceder qualquer um deles vai
acionar um erro de limitação de taxa. Por exemplo, se o limite de RPM for 20, fazer 21 solicitações em um minuto vai resultar em um erro, mesmo que você não tenha excedido o TPM ou outros limites.

Os limites de taxa são aplicados por projeto, não por chave de API. As cotas de solicitações por dia (**RPD**) são redefinidas à meia-noite do horário do Pacífico.

Os limites variam de acordo com o modelo específico usado, e alguns limites só se aplicam a modelos específicos. Por exemplo, as imagens por minuto (IPM) só são calculadas para modelos capazes de gerar imagens (Nano Banana), mas são conceitualmente semelhantes às TPM. Outros modelos podem ter um limite de token por dia (TPD).

Os limites de taxa são mais restritos para modelos experimentais e de prévia.

### Limites de taxa com base em gastos

Além dos limites de solicitações por minuto (RPM) e tokens por minuto (TPM), a API Gemini aplica limites de taxa com base em gastos para proteger contra cobranças inesperadas. Se esses limites se aplicam à sua conta, isso depende do seu histórico de faturamento e do [nível de uso](#usage-tiers).

A tabela a seguir mostra os limites de taxa com base no gasto para cada [nível de uso](#usage-tiers). Esses limites são avaliados em uma janela de 10 minutos. A aplicação desses limites à sua conta depende do histórico de faturamento e da situação da conta.

| Nível de uso | Limite de taxa de gasto (a cada 10 minutos) |
| --- | --- |
| **Free** (link em francês) | N/A |
| **Nível 1** | US$ 10 |
| **Nível 2** | US$ 200 |
| **Nível 3** | US$ 200 |

Se você atingir um limite de taxa com base em gastos, a API vai retornar um erro `429 RESOURCE_EXHAUSTED`. Para solucioná-lo:

- **Aguarde e tente de novo** após um curto período.
- **Reduza a taxa de solicitações caras**, por exemplo, usando janelas de contexto menores ou saídas mais curtas.
- Se você atingir esse limite com frequência durante o uso normal, [solicite um aumento do limite de taxa](#request-rate-limit-increase).

## Níveis de uso

Os limites de taxa estão vinculados ao nível de uso do projeto. À medida que seu uso e gastos com a API aumentam, você recebe um upgrade automático para um nível mais alto com limites de taxa maiores.

As qualificações para os níveis 2 e 3 são baseadas no gasto total acumulado em serviços do Google Cloud (incluindo, entre outros, a API Gemini) para a conta de faturamento vinculada ao seu projeto.

| Nível de uso | Qualificação | [Limite do nível de faturamento](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br#tier-spend-caps) |
| --- | --- | --- |
| **Free** (link em francês) | [Projeto ativo](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#google-cloud-projects) ou teste sem custo financeiro | N/A |
| **Nível 1** | [Configurar e vincular uma conta de faturamento ativa](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br#setup-billing) | US$ 250,00 |
| **Nível 2** | Pagamento de US $100 + 3 dias desde o primeiro pagamento bem-sucedido | US$ 2.000 |
| **Nível 3** | Pago US $1.000 + 30 dias desde o primeiro pagamento bem-sucedido | US$ 20.000 a US$ 100.000 ou mais |

Embora atender aos critérios de qualificação declarados seja geralmente suficiente para aprovação, em casos raros, uma solicitação de upgrade pode ser negada com base em outros fatores identificados durante o processo de revisão.

Esse sistema ajuda a manter a segurança e a integridade da plataforma da API Gemini para todos os usuários.

## Limites de taxa da API Gemini

Os limites de taxa dependem de vários fatores, como seu nível de uso, e podem ser consultados no Google AI Studio. À medida que seu nível e o status da conta mudam com o tempo, os limites de taxa são atualizados automaticamente.

[Conferir seus limites de taxa ativos no AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=pt-br)

Os limites de taxa especificados não são garantidos, e a capacidade real pode variar.

## Limites de taxa de inferência de prioridade

O consumo de [prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br) tem limites de taxa próprios, mesmo que o consumo seja contado para os limites de taxa gerais de tráfego interativo. **Os limites de taxa padrão são: 0,3 vezes o [limite de taxa padrão](https://aistudio.google.com/rate-limit?hl=pt-br) para cada modelo e nível**

## Limites de taxa da API Batch

As solicitações da [API em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br) estão sujeitas a limites de taxa próprios, separados das chamadas de API que não são em lote.

- **Solicitações em lote simultâneas**:100
- **Limite de tamanho do arquivo de entrada**:2 GB
- **Limite de armazenamento de arquivos**:20 GB
- **Tokens enfileirados por modelo**:a tabela **Tokens enfileirados em lote** lista o número máximo de tokens que podem ser enfileirados para processamento em lote em todos os seus jobs em lote ativos para um determinado modelo.

### Nível 1

| Modelo | Tokens em lote na fila |
| --- | --- |
| Modelos de saída de texto | | | | |
| --- | --- | --- | --- | --- |
| Pré-lançamento do Gemini 3.1 Pro | 5.000.000 |
| Gemini 3.1 Flash Lite | 10.000.000 |
| Pré-lançamento do Gemini 3.1 Flash Lite | 10.000.000 |
| Gemini 3.5 Flash | 3.000.000 |
| Gemini 2.5 Pro | 5.000.000 |
| Gemini 2.5 Pro TTS | 25.000 |
| Gemini 2.5 Flash | 3.000.000 |
| Pré-lançamento do Gemini 2.5 Flash | 3.000.000 |
| Pré-lançamento do Gemini 2.5 Flash Image | 3.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 10.000.000 |
| Pré-lançamento do Gemini 2.5 Flash Lite | 10.000.000 |
| Gemini 2.0 Flash | 10.000.000 |
| Imagem do Gemini 2.0 Flash | 3.000.000 |
| Gemini 2.0 Flash Lite | 10.000.000 |
| Modelos de geração multimodal | | | | |
| Pré-lançamento do Gemini 3.1 Flash Image 🍌 | 1.000.000 |
| Imagem do Gemini 3.1 Flash Lite 🍌 | 2.000.000 |
| Pré-lançamento do Gemini 3 Pro Image 🍌 | 2.000.000 |
| Modelos de embeddings | | | | |
| Embedding do Gemini | 500.000 |

### Nível 2

| Modelo | Tokens em lote na fila |
| --- | --- |
| Modelos de saída de texto | | | | |
| --- | --- | --- | --- | --- |
| Pré-lançamento do Gemini 3.1 Pro | 500.000.000 |
| Gemini 3.1 Flash Lite | 500.000.000 |
| Pré-lançamento do Gemini 3.1 Flash Lite | 500.000.000 |
| Gemini 3.5 Flash | 400.000.000 |
| Gemini 2.5 Pro | 500.000.000 |
| Gemini 2.5 Pro TTS | 100.000 |
| Gemini 2.5 Flash | 400.000.000 |
| Pré-lançamento do Gemini 2.5 Flash | 400.000.000 |
| Pré-lançamento do Gemini 2.5 Flash Image | 400.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 500.000.000 |
| Pré-lançamento do Gemini 2.5 Flash Lite | 500.000.000 |
| Gemini 2.0 Flash | 1.000.000.000 |
| Imagem do Gemini 2.0 Flash | 400.000.000 |
| Gemini 2.0 Flash Lite | 1.000.000.000 |
| Modelos de geração multimodal | | | | |
| Pré-lançamento do Gemini 3.1 Flash Image 🍌 | 250.000.000 |
| Imagem do Gemini 3.1 Flash Lite 🍌 | 270.000.000 |
| Pré-lançamento do Gemini 3 Pro Image 🍌 | 270.000.000 |
| Modelos de embeddings | | | | |
| Embedding do Gemini | 5.000.000 |

### Nível 3

| Modelo | Tokens em lote na fila |
| --- | --- |
| Modelos de saída de texto | | | | |
| --- | --- | --- | --- | --- |
| Pré-lançamento do Gemini 3.1 Pro | 1.000.000.000 |
| Gemini 3.1 Flash Lite | 1.000.000.000 |
| Pré-lançamento do Gemini 3.1 Flash Lite | 1.000.000.000 |
| Gemini 3.5 Flash | 1.000.000.000 |
| Gemini 2.5 Pro | 1.000.000.000 |
| Gemini 2.5 Pro TTS | 1.000.000 |
| Gemini 2.5 Flash | 1.000.000.000 |
| Pré-lançamento do Gemini 2.5 Flash | 1.000.000.000 |
| Pré-lançamento do Gemini 2.5 Flash Image | 1.000.000.000 |
| Gemini 2.5 Flash TTS | 4.000.000 |
| Gemini 2.5 Flash Lite | 1.000.000.000 |
| Pré-lançamento do Gemini 2.5 Flash Lite | 1.000.000.000 |
| Gemini 2.0 Flash | 5.000.000.000 |
| Imagem do Gemini 2.0 Flash | 1.000.000.000 |
| Gemini 2.0 Flash Lite | 5.000.000.000 |
| Modelos de geração multimodal | | | | |
| Pré-lançamento do Gemini 3.1 Flash Image 🍌 | 750.000.000 |
| Imagem do Gemini 3.1 Flash Lite 🍌 | 1.000.000.000 |
| Pré-lançamento do Gemini 3 Pro Image 🍌 | 1.000.000.000 |
| Modelos de embeddings | | | | |
| Embedding do Gemini | 10.000.000 |

## Como fazer upgrade para o próximo nível

Para fazer a transição do nível sem custo financeiro para um nível pago, primeiro [configure o faturamento no AI Studio](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br).

Quando seu projeto atender aos [critérios especificados](#usage-tiers), ele será atualizado automaticamente para o próximo nível. Os upgrades do Nível sem custo financeiro para o Nível 1
geralmente entram em vigor instantaneamente, e os upgrades de nível subsequentes levam
até 10 minutos. Acesse a [página "Projetos"](https://aistudio.google.com/projects?hl=pt-br) no AI Studio para verificar seus níveis.

## Solicitar um aumento no limite de taxa

Cada variação de modelo tem um limite de taxa associado (solicitações por minuto, RPM).
Para mais detalhes sobre esses limites de taxa, consulte a página
[Limite de taxa do AI Studio](https://aistudio.google.com/rate-limit?hl=pt-br).

[Solicitar um aumento no limite de taxa do nível pago](https://forms.gle/ETzX94k8jf7iSotH9)

Não podemos garantir que vamos aumentar seu limite de taxa, mas faremos o possível para analisar seu pedido.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-03 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-03 UTC."],[],[]]
