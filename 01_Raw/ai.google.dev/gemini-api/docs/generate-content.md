---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-BR
fetched_at: 2026-09-21T05:41:17.644100+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

# Gemini API

A API Gemini é o caminho mais rápido do comando à produção com o Gemini, o Veo, o Nano Banana e muito mais. Ela permite integrar esses modelos generativos aos seus aplicativos para gerar texto e imagens, analisar entradas multimodais e criar agentes conversacionais.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3.8-flash", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[Comece a criar](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)

---

## Conheça os modelos

[Ver tudo](https://ai.google.dev/gemini-api/docs/models?hl=pt-br)

[auto\_awesome
Gemini 3.1 Pro
Novo

Nosso modelo mais inteligente, o melhor do mundo em compreensão multimodal, tudo com base em raciocínio de última geração.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br)
[spark
Gemini 3.6 Flash
Novo

Nosso modelo mais recente, que equilibra velocidade e inteligência para oferecer um desempenho forte em tarefas agênticas e multimodais.](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pt-br)
[spark
Gemini 3.5 Flash

Desempenho de ponta que rivaliza com modelos maiores a uma fração do custo.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pt-br)
[spark
Gemini 3.5 Flash-Lite
Novo

Modelo de alto volume e sensível a custos otimizado para tarefas de subagentes de alta capacidade de processamento e baixa latência.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pt-br)
[spark
Gemini 3.1 Flash-Lite

Modelo de alto volume e sensível a custos com o desempenho e a qualidade da série Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br)
[spark
Gemini 3 Flash

Desempenho de ponta que rivaliza com modelos maiores a uma fração do custo.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br)
[🍌
🍌 Nano Banana 2 e Nano Banana Pro

Modelos de edição e geração de imagens de última geração.](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)
[video\_library
Veo 3.1

Nosso modelo de geração de vídeos de última geração, com áudio nativo.](https://ai.google.dev/gemini-api/docs/video?hl=pt-br)
[spark
Gemini Robotics

Um modelo de visão-linguagem (VLM) que traz os recursos agênticos do Gemini para a robótica e permite raciocínio avançado no mundo físico.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pt-br)

## Conheça os recursos

[imagesmode

Geração de imagens nativa (Nano Banana)

Gere e edite imagens altamente contextuais de forma nativa com o Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)
[article

Contexto longo

Insira milhões de tokens nos modelos do Gemini e extraia compreensão de imagens, vídeos e documentos não estruturados.](https://ai.google.dev/gemini-api/docs/long-context?hl=pt-br)
[code

Respostas estruturadas

Restrinja o Gemini para responder com JSON, um formato de dados estruturado adequado para processamento automatizado.](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br)
[functions

Chamadas de função

Crie fluxos de trabalho agênticos conectando o Gemini a APIs e ferramentas externas.](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)
[videocam

Geração de vídeos com o Veo 3.1

Crie conteúdo de vídeo de alta qualidade com comandos de texto ou imagem usando nosso modelo de última geração.](https://ai.google.dev/gemini-api/docs/video?hl=pt-br)
[android\_recorder

Agentes de voz com a API Live

Crie aplicativos e agentes de voz em tempo real com a API Live.](https://ai.google.dev/gemini-api/docs/live-api?hl=pt-br)
[build

Ferramentas

Conecte o Gemini ao mundo usando ferramentas integradas, como a Pesquisa Google, o contexto de URL, o Google Maps, a execução de código e o uso do computador.](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br)
[stacks

Document Understanding

Processe até 1.000 páginas de arquivos PDF com compreensão multimodal completa ou outros tipos de arquivos baseados em texto.](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br)
[cognition\_2

Pensando

Saiba como os recursos de pensamento melhoram o raciocínio para tarefas e agentes complexos.](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)

[Google AI Studio

Teste comandos, gerencie suas chaves de API, monitore o uso e crie protótipos.](https://aistudio.google.com?hl=pt-br)
[group

Comunidade de desenvolvedores

Faça perguntas e encontre soluções de outros desenvolvedores e engenheiros do Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=pt-br)
[menu\_book

Referência da API

Encontre informações detalhadas sobre a API Gemini na documentação de referência oficial.](https://ai.google.dev/api?hl=pt-br)
[sensors

Status

Confira o status da API Gemini, do Google AI Studio e dos nossos serviços de modelo.](https://aistudio.google.com/status?hl=pt-br)

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-14 UTC.

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-14 UTC."],[],[]]
