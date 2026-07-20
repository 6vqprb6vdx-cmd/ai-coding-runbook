---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=pt-BR
fetched_at: 2026-07-20T04:34:14.854390+00:00
title: "Acelere a descoberta com o Gemini for Research \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)

# Acelere a descoberta com o Gemini for Research

[Gerar uma chave da API Gemini](https://aistudio.google.com/apikey?hl=pt-br)

Os modelos Gemini podem ser usados para avançar a pesquisa fundamental em várias disciplinas.
Confira algumas maneiras de usar o Gemini na sua pesquisa:

- **Analisar e controlar as saídas do modelo**: para uma análise mais detalhada, examine um
  candidato de resposta gerado pelo modelo usando ferramentas como
  `CitationMetadata`. Também é possível configurar opções para a geração e as saídas do modelo, como `responseSchema`, `topP` e `topK`. [Saiba mais](https://ai.google.dev/api/generate-content?hl=pt-br).
- **Entradas multimodais**: o Gemini pode processar imagens, áudio e vídeos, permitindo uma
  infinidade de direções de pesquisa interessantes. [Saiba mais](https://ai.google.dev/gemini-api/docs/vision?hl=pt-br).
- **Recursos de contexto longo**: o Gemini 3.0 Flash e Pro vêm com uma janela de contexto de 1 milhão de tokens. [Saiba mais](https://ai.google.dev/gemini-api/docs/long-context?hl=pt-br).
- **Cresça com o Google**: acesse rapidamente os modelos do Gemini pela API e pelo Google AI
  Studio para casos de uso de produção. Se você estiver procurando uma plataforma baseada no Google Cloud, a Gemini Enterprise Agent Platform poderá fornecer infraestrutura de suporte adicional.

Para apoiar a pesquisa acadêmica e impulsionar a pesquisa de ponta, o Google oferece
acesso a créditos da API Gemini para cientistas e pesquisadores acadêmicos pelo
[Programa Acadêmico Gemini](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=pt-br#gemini-academic-program).

## Comece a usar o Gemini

A API Gemini e o Google AI Studio ajudam você a começar a trabalhar com os modelos mais recentes do Google e a transformar suas ideias em aplicativos escalonáveis.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## Acadêmicos em destaque

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=pt-br)

"Nossa pesquisa investiga o Gemini como um modelo de linguagem visual (VLM, na sigla em inglês) e seus comportamentos agênticos em diversos ambientes, do ponto de vista da robustez e da segurança. Até agora, avaliamos a robustez do Gemini contra distrações, como janelas pop-up, quando os agentes VLM realizam tarefas de computador, e usamos o Gemini para analisar a interação social, eventos temporais e fatores de risco com base na entrada de vídeo."

[Site de Diyi Yang (em inglês)](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=pt-br)

"O Gemini Pro e o Flash, com a janela de contexto longa, têm nos ajudado no OK-Robot, nosso projeto de manipulação móvel de vocabulário aberto. O Gemini permite consultas e comandos complexos de linguagem natural na "memória" do robô: nesse caso, observações anteriores feitas pelo robô durante uma longa duração de operação. Mahi Shafiullah e eu também estamos usando o Gemini para decompor tarefas em código que o robô pode executar no mundo real."

[Site de Lerrel Pinto (em inglês)](https://www.lerrelpinto.com/)

## Programa Acadêmico Gemini

Pesquisadores acadêmicos qualificados (como professores, funcionários e estudantes de doutorado) em [países
aceitos](https://ai.google.dev/gemini-api/docs/available-regions?hl=pt-br) podem se inscrever para receber créditos da API Gemini
e limites de taxa mais altos para projetos de pesquisa. Esse suporte permite maior capacidade de processamento para experimentos científicos e avanços na pesquisa.

Estamos particularmente interessados nas áreas de pesquisa na seção a seguir, mas aceitamos inscrições de diversas disciplinas científicas:

- **Avaliações e comparativos**: métodos de avaliação aprovados pela comunidade que podem fornecer um indicador de desempenho forte em áreas como veracidade, segurança, instruções, raciocínio e planejamento.
- **Acelerar a descoberta científica para beneficiar a humanidade**: possíveis
  aplicações de IA em pesquisas científicas interdisciplinares, incluindo áreas
  como doenças raras e negligenciadas, biologia experimental, ciência dos materiais
  e sustentabilidade.
- **Incorporação e interações**: uso de modelos de linguagem grandes para
  investigar novas interações nos campos de IA incorporada, interações ambientais,
  robótica e interação humano-computador.
- **Recursos emergentes**: explorar novos recursos agênticos necessários para
  melhorar o raciocínio e o planejamento, e como os recursos podem ser expandidos durante a
  inferência (por exemplo, usando o Gemini Flash).
- **Interação e compreensão multimodal**: identificar lacunas e
  oportunidades para modelos fundamentais multimodais para análise, raciocínio,
  e planejamento em várias tarefas.

Qualificação: somente pessoas (professores, pesquisadores ou equivalentes) afiliadas a uma instituição acadêmica válida ou organização de pesquisa acadêmica podem se inscrever. O acesso e os créditos da API serão concedidos e removidos a critério do Google. Analisamos as inscrições mensalmente.

### Comece a pesquisar com a API Gemini

[Faça sua inscrição agora](https://forms.gle/HMviQstU8PxC5iCt5)

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-01 UTC.

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-01 UTC."],[],[]]
