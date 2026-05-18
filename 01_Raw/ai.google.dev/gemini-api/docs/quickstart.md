---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-BR
fetched_at: 2026-05-18T13:06:07.332455+00:00
title: "Guia de in\u00edcio r\u00e1pido da API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia de início rápido da API Gemini

Este guia de início rápido mostra como instalar nossas [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br)
e fazer sua primeira solicitação de API Gemini.

## Antes de começar

Para usar a API Gemini, você precisa de uma chave de API para autenticar suas solicitações, aplicar limites de segurança e acompanhar o uso da sua conta.

Crie uma no AI Studio sem custo financeiro para começar:

[Crie uma chave da API Gemini](https://aistudio.google.com/app/apikey?hl=pt-br)

## Instalar o SDK da IA generativa do Google

### Python

Usando [Python 3.9 ou mais recente](https://www.python.org/downloads/), instale o
[`google-genai` pacote](https://pypi.org/project/google-genai/)
usando o seguinte
[comando pip](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai
```

### JavaScript

Usando [Node.js v18+](https://nodejs.org/en/download/package-manager),
instale o
[SDK de IA Generativa do Google para TypeScript e JavaScript](https://www.npmjs.com/package/@google/genai)
usando o seguinte
[comando npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```
npm install @google/genai
```

### Go

Instale
[google.golang.org/genai](https://pkg.go.dev/google.golang.org/genai) no
diretório do módulo usando o [comando go get](https://go.dev/doc/code):

```
go get google.golang.org/genai
```

### Java

Se você estiver usando o Maven, instale
[google-genai](https://github.com/googleapis/java-genai) adicionando o
seguinte às dependências:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

Instale
[googleapis/go-genai](https://googleapis.github.io/dotnet-genai/) no
diretório do módulo usando o [comando dotnet add](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add)

```
dotnet add package Google.GenAI
```

### Apps Script

1. Para criar um novo projeto do Apps Script, acesse
   [script.new](https://script.google.com/u/0/home/projects/create?hl=pt-br).
2. Clique em **Projeto sem título**.
3. Renomeie o projeto do Apps Script como **AI Studio** e clique em **Renomear**.
4. Defina sua [chave de API](https://developers.google.com/apps-script/guides/properties?hl=pt-br#manage_script_properties_manually)
   1. À esquerda, clique em **Configurações do projeto** ![O ícone das configurações do projeto](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg).
   2. Em **Propriedades do script** , clique em **Adicionar propriedade do script**.
   3. Em **Propriedade**, insira o nome da chave: `GEMINI_API_KEY`.
   4. Em **Valor**, insira o valor da chave de API.
   5. Clique em **Salvar propriedades do script**.
5. Substitua o conteúdo do arquivo `Code.gs` pelo código a seguir:

## Faça sua primeira solicitação

Há duas maneiras de enviar uma solicitação à API Gemini:

- ***(Recomendado)*** [A API Interactions](https://ai.google.dev/api/interactions-api?hl=pt-br) é uma nova primitiva com suporte nativo para uso de ferramentas de várias etapas, orquestração e fluxos de raciocínio complexos por etapas de execução digitadas. No futuro, novos modelos além da família principal, além de novos recursos e ferramentas de agentes, serão lançados exclusivamente na API Interactions.
- [`generateContent`](https://ai.google.dev/api/generate-content?hl=pt-br#method:-models.generatecontent) oferece uma maneira de gerar uma resposta simples e sem estado de um modelo. Embora recomendemos o uso da API Interactions, `generateContent` tem suporte total.

Este exemplo usa o
[`generateContent`](https://ai.google.dev/api/generate-content?hl=pt-br#method:-models.generatecontent) método
para enviar uma solicitação à API Gemini usando o modelo Gemini 2.5 Flash.

Se você [definir sua chave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#set-api-env-var) como a
variável de ambiente `GEMINI_API_KEY`, ela será selecionada automaticamente pelo
cliente ao usar as [bibliotecas da API Gemini](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br).
Caso contrário, será necessário [transmitir a chave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#provide-api-key-explicitly) como
um argumento ao inicializar o cliente.

Observe que todos os exemplos de código na documentação da API Gemini pressupõem que você definiu a variável de ambiente `GEMINI_API_KEY`.

### Python

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
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
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
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
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
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
    // The client gets the API key from the environment variable `GOOGLE_API_KEY`.
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## A seguir

Agora que você fez sua primeira solicitação de API, talvez queira conferir os seguintes guias que mostram o Gemini em ação:

- [Geração de texto](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br)
- [Geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br)
- [Compreensão de imagens](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pt-br)
- [Raciocínio](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br)
- [Chamadas de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br)
- [Contexto longo](https://ai.google.dev/gemini-api/docs/long-context?hl=pt-br)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-11 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-11 UTC."],[],[]]
