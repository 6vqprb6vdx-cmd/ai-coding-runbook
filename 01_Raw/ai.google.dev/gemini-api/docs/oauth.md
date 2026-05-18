---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=pt-BR
fetched_at: 2026-05-18T13:07:23.659999+00:00
title: "Guia de in\u00edcio r\u00e1pido do OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia de início rápido do OAuth

A maneira mais fácil de autenticar a API Gemini é configurar uma chave de API, conforme
descrito no [guia de início rápido da API Gemini](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br). Se você
precisar de controles de acesso mais rigorosos, use o OAuth. Este guia vai ajudar você a configurar a autenticação com OAuth.

Este guia usa uma abordagem de autenticação simplificada adequada para um ambiente de teste. Para um ambiente de produção, saiba mais sobre [autenticação e autorização](https://developers.google.com/workspace/guides/auth-overview?hl=pt-br) antes de [escolher as credenciais de acesso](https://developers.google.com/workspace/guides/create-credentials?hl=pt-br#choose_the_access_credential_that_is_right_for_you) adequadas para seu app.

## Objetivos

- Configurar seu projeto na nuvem para OAuth
- Configurar as credenciais padrão do aplicativo
- Gerenciar credenciais no seu programa em vez de usar `gcloud auth`

## Pré-requisitos

Para executar este guia de início rápido, você precisa de:

- [Um projeto do Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=pt-br).
- [Uma instalação local da CLI gcloud](https://cloud.google.com/sdk/docs/install?hl=pt-br)

## Configurar seu projeto na nuvem

Para concluir este guia de início rápido, primeiro configure seu projeto na nuvem.

### 1. Ativar a API

Antes de usar as APIs do Google, é necessário ativá-las em um projeto na nuvem do Google.

- No console do Google Cloud, ative a API Generative Language do Google.

  [Ativar a API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=pt-br)

### 2. Configurar a tela de permissão OAuth

Em seguida, configure a tela de permissão OAuth do projeto e adicione você mesmo como um usuário de teste. Se você já concluiu esta etapa para seu projeto na nuvem, pule para a próxima seção.

1. No console do Google Cloud, acesse **Menu** >
   **Plataforma de autenticação do Google** > **Visão geral**.

   [Acessar a plataforma Google Auth](https://console.developers.google.com/auth/overview?hl=pt-br)
2. Preencha o formulário de configuração do projeto e defina o tipo de usuário como **Externo** na seção **Público-alvo**.
3. Preencha o restante do formulário, aceite os termos da Política de Dados do Usuário e clique em
   **Criar**.
4. Por enquanto, você pode pular a adição de escopos e clicar em **Salvar e continuar**. No
   futuro, ao criar um app para uso fora da sua organização do Google Workspace, você precisará adicionar e verificar os escopos de autorização que seu
   app exige.
5. Adicione usuários de teste:

   1. Acesse a [página "Público-alvo"](https://console.developers.google.com/auth/audience?hl=pt-br) da plataforma de autenticação do Google.
   2. Em **Usuários de teste**, clique em **Adicionar usuários**.
   3. Insira seu endereço de e-mail e os outros usuários de teste autorizados. Depois, clique em **Salvar**.

### 3. Autorizar credenciais para um aplicativo para computador

Para fazer a autenticação como usuário final e acessar os dados do usuário no app, crie um ou mais IDs do cliente OAuth 2.0. Um ID do cliente é usado para identificar um único app nos servidores OAuth do Google. Se o app for executado em várias plataformas,
crie um ID do cliente separado para cada uma delas.

1. No console do Google Cloud, acesse **Menu** > **Plataforma de autenticação do Google** >
   **Clientes**.

   [Acessar "Credenciais"](https://console.developers.google.com/auth/clients?hl=pt-br)
2. Clique em **Criar cliente**.
3. Clique em **Tipo de aplicativo** > **App para computador**.
4. No campo **Nome**, digite um nome para a credencial. Esse nome é mostrado apenas no console do Google Cloud.
5. Clique em **Criar**. A tela "Cliente OAuth criado" aparece, mostrando seu novo
   ID do cliente e chave secreta do cliente.
6. Clique em **OK**. A credencial recém-criada aparece em **IDs do cliente OAuth 2.0**.
7. Clique no botão de download para salvar o arquivo JSON. Ele será salvo como `client_secret_<identifier>.json`. Renomeie-o como `client_secret.json` e mova para o diretório de trabalho.

## Configurar o Application Default Credentials

Para converter o arquivo `client_secret.json` em credenciais utilizáveis, transmita o local dele ao argumento `--client-id-file` do comando `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

A configuração simplificada do projeto neste tutorial aciona uma caixa de diálogo **"O Google ainda não verificou este app"**. Isso é normal. Escolha **"Continuar"**.

Isso coloca o token resultante em um local conhecido para que ele possa ser acessado
pelo `gcloud` ou pelas bibliotecas de cliente.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

Depois que você define o Application Default Credentials (ADC), as bibliotecas de cliente na maioria das linguagens precisam de pouca ou nenhuma ajuda para encontrá-los.

### Curl

A maneira mais rápida de testar se isso está funcionando é usar o curl para acessar a API REST:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

Em Python, as bibliotecas de cliente encontram as credenciais automaticamente:

```
pip install google-genai
```

Um script mínimo para testar isso pode ser:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## Próximas etapas

Se isso estiver funcionando, você poderá tentar a
[recuperação semântica nos seus dados de texto](https://ai.google.dev/docs/semantic_retriever?hl=pt-br).

## Gerenciar credenciais por conta própria [Python]

Em muitos casos, você não terá o comando `gcloud` disponível para criar o token de acesso do ID do cliente (`client_secret.json`). O Google fornece bibliotecas em várias linguagens para que você gerencie esse processo no seu app. Esta seção demonstra o processo em Python. Existem exemplos equivalentes desse tipo de procedimento para outras linguagens na [documentação da API Drive](https://developers.google.com/drive/api/quickstart/python?hl=pt-br).

### 1. Instalar as bibliotecas necessárias

Instale a biblioteca de cliente do Google para Python e a biblioteca de cliente do Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. Escrever o gerenciador de credenciais

Para minimizar o número de cliques nas telas de autorização,
crie um arquivo chamado `load_creds.py` no diretório de trabalho para
armazenar em cache um arquivo `token.json` que pode ser reutilizado mais tarde ou atualizado se expirar.

Comece com o código a seguir para converter o arquivo `client_secret.json` em um token que pode ser usado com `genai.configure`:

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. Escrever seu programa

Agora crie seu `script.py`:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. Executar o programa

No diretório de trabalho, execute a amostra:

```
python script.py
```

Na primeira vez que você executar o script, ele vai abrir uma janela do navegador e pedir que você autorize o acesso.

1. Se você ainda não estiver conectado à sua Conta do Google, será solicitado a fazer login. Se você tiver feito login em várias contas, **selecione a
   conta que você definiu como "Conta de teste" ao configurar o projeto.**
2. As informações de autorização são armazenadas no sistema de arquivos. Assim, na próxima vez que você executar o exemplo de código, não será necessário fazer a autorização.

Você configurou a autenticação.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
