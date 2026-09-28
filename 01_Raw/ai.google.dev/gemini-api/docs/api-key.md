---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=pt-BR
fetched_at: 2026-09-28T06:21:52.970074+00:00
title: "Como usar chaves da API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Como usar chaves da API Gemini

Para usar a API Gemini, é necessário autenticar suas solicitações. É possível
autenticar usando uma chave de API padrão ou de autorização.

[Criar ou visualizar uma chave da API Gemini](https://aistudio.google.com/apikey?hl=pt-br)

## Tipos de chaves de API: padrão x autorização

As chaves de API fornecem acesso à API Gemini, mas as características de segurança delas são diferentes. A API Gemini está migrando de chaves de API padrão para chaves de autorização para melhorar a segurança:

- **Chaves de API padrão**: associam solicitações a um projeto do Google Cloud para fins de faturamento e cota. As chaves padrão não identificam um chamador, o que limita a granularidade das permissões e do controle de acesso que elas podem oferecer.
- **Chaves de autorização (auth)**: vinculadas diretamente a uma conta de serviço do Google Cloud. Quando você usa uma chave de autorização, suas solicitações são processadas
  na identidade dessa conta de serviço vinculada, permitindo o controle
  de acesso granular. As chaves de autorização são restritas à API Generative Language (API Gemini) por padrão e oferecem uma aplicação rápida de chaves vazadas que interrompe rapidamente o uso de chaves vazadas detectadas pelos nossos sistemas.

Para garantir o uso seguro, a API Gemini vai migrar de chaves padrão para chaves de autenticação:

- **Chaves de autenticação padrão**: a partir de 28 de maio de 2026, todas as novas chaves de API criadas no Google AI Studio serão criadas automaticamente como chaves de autenticação.
- **Chaves irrestritas rejeitadas**: a API Gemini rejeita solicitações de **chaves padrão irrestritas**. As chaves de API padrão com restrições explícitas aplicadas continuam funcionando. Essa restrição impede o
  uso não autorizado de chaves que podem ser compartilhadas publicamente ou vinculadas a outros
  serviços.

## Como gerenciar chaves de API no Google AI Studio

Você pode gerenciar seus projetos e chaves diretamente no [Google AI Studio](https://aistudio.google.com/apikey?hl=pt-br).

### Projetos do Google Cloud

Cada chave de API do Gemini está associada a um [projeto do Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pt-br).
Os projetos do Google Cloud gerenciam o faturamento, os colaboradores e as permissões. O Google AI Studio oferece uma interface leve para acessar esses projetos.

- **Projeto padrão**: se você for um novo usuário, o Google AI Studio vai criar automaticamente um projeto na nuvem padrão do Google Cloud e uma chave de API depois que você aceitar os Termos de Serviço. Para renomear esse projeto, acesse a visualização **Projetos** no painel.
- **Projetos atuais**: se você já tiver uma conta do Google Cloud, o AI
  Studio não vai criar um projeto padrão. Em vez disso, importe seus projetos atuais.

### Importar projetos

Por padrão, o Google AI Studio não mostra todos os seus projetos do Google Cloud. Importe os projetos que você quer usar:

1. Acesse o [Google AI Studio](https://aistudio.google.com?hl=pt-br).
2. Abra o **Painel** no painel à esquerda e selecione **Projetos**.
3. Clique no botão **Importar projetos**.
4. Pesquise e selecione o projeto na nuvem do Google Cloud que você quer importar e clique em **Importar**.
5. Depois de importar, acesse a página **Chaves de API** no painel para
   criar uma chave nesse projeto.

### Resolver problemas de permissões de criação de chaves

Se o botão **Criar chave de API** estiver indisponível e mostrar a mensagem:
*"Você não tem permissão para criar uma chave neste projeto"*, significa que você não tem as
permissões necessárias do IAM.

Peça ao administrador do projeto ou da organização do Google Cloud para conceder a você um papel
que contenha as seguintes permissões (como Editor de projetos):

- `resourcemanager.projects.get`: permite que o AI Studio verifique o projeto.
- `apikeys.keys.create`: permite a geração de chaves.
- `serviceusage.services.enable`: garante que a API Generative Language esteja ativada.
- `iam.serviceAccounts.create`: obrigatório para criar a conta de serviço vinculada.
- `iam.serviceAccountApiKeyBindings.create`: vincula a conta de serviço à
  chave de API.

Se não for possível conseguir acesso administrativo, crie um projeto do Google Cloud que não esteja associado a uma organização para gerar as chaves.

## Como configurar o ambiente

Depois de ter uma chave, configure seu ambiente para usá-la com segurança nos seus
aplicativos.

### Opção 1: usar variáveis de ambiente (recomendado)

Defina a variável de ambiente `GEMINI_API_KEY` ou `GOOGLE_API_KEY`. As bibliotecas de cliente da API Gemini detectam e usam essas variáveis automaticamente. Se ambos estiverem definidos, `GOOGLE_API_KEY` terá precedência.

Selecione seu sistema operacional para definir a variável:

### Linux/macOS: Bash

Verifique se você tem um arquivo de configuração do bash:

```
~/.bashrc
```

Se não houver, crie e abra um:

```
touch ~/.bashrc && open ~/.bashrc
```

Adicione o comando de exportação ao final do arquivo:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Salve o arquivo e aplique as mudanças:

```
source ~/.bashrc
```

### macOS: Zsh

Verifique se você tem um arquivo de configuração do zsh:

```
~/.zshrc
```

Se não houver, crie e abra um:

```
touch ~/.zshrc && open ~/.zshrc
```

Adicione o comando de exportação:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Salve o arquivo e aplique as mudanças:

```
source ~/.zshrc
```

### Windows

1. Pesquise "Variáveis de ambiente" na barra de pesquisa do Windows.
2. Clique em **Variáveis de ambiente** na caixa de diálogo "Propriedades do sistema".
3. Em **Variáveis de usuário** ou **Variáveis do sistema**, clique em **Nova...**.
4. Defina o nome da variável como `GEMINI_API_KEY` e o valor como sua chave de API.
5. Clique em **OK** para salvar. Abra uma nova sessão de terminal para carregar a variável.

### Opção 2: fornecer a chave de API explicitamente no código

Você pode transmitir a chave de API explicitamente ao inicializar o cliente. Faça isso apenas
se não for possível usar variáveis de ambiente.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = Client.builder().apiKey("YOUR_API_KEY").build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few sentences."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works in a few sentences."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Segurança e gerenciamento de secrets

Trate sua chave da API Gemini como uma senha. Se comprometida, outras pessoas podem consumir
a cota do seu projeto, gerar cobranças inesperadas e acessar recursos
particulares.

### Regras de segurança críticas

- **Mantenha as chaves confidenciais**: nunca verifique as chaves de API em sistemas de controle de origem, como o Git.
- **Nunca exponha chaves do lado do cliente em produção**: não codifique chaves de API
  diretamente em apps da Web ou para dispositivos móveis. As chaves compiladas em código do lado do cliente podem ser
  extraídas pelos usuários. Para proteger apps do lado do cliente, execute um servidor proxy de back-end
  para fazer as chamadas de API reais.

### Práticas recomendadas de gerenciamento de secrets

- **Variáveis de ambiente**: leia chaves de variáveis de ambiente em vez de arquivos de configuração.
- **Secret Manager**: para produção, armazene suas chaves em um armazenamento de secrets seguro, como o [Secret Manager do Google Cloud](https://cloud.google.com/secret-manager?hl=pt-br).
- **Alertas de faturamento**: configure alertas de faturamento no console do Google Cloud para
  receber notificações se houver um aumento no uso ou nos custos.

### Lista de verificação de resposta a vazamentos

Se você suspeitar que sua chave de API foi vazada:

1. **Gere uma nova chave**: crie uma chave substituta no Google AI Studio ou no
   Console do Cloud.
2. **Atualize o aplicativo**: implante o código usando a nova chave.
3. **Desative ou exclua a chave comprometida**: desative a chave vazada no
   Console do Cloud assim que a nova chave for verificada. Não exclua a chave antiga até que a nova esteja totalmente ativa para evitar tempo de inatividade do aplicativo.
4. **Auditoria de uso**: verifique os registros de faturamento e o uso da API no console do Google Cloud para identificar atividades não autorizadas.

## Restringir e proteger suas chaves

Adicionar restrições às chaves de API minimiza o dano potencial se uma chave for comprometida.

### Aplicar restrições de origem da solicitação

As restrições de origem limitam quais endereços IP, sites ou aplicativos podem usar
sua chave.

1. Acesse a [página "Credenciais" do console do Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pt-br).
2. Selecione seu projeto e clique no nome da chave de API que você quer restringir.
3. Em **Restrições de aplicativo**, selecione **Endereços IP** ou o tipo de restrição adequado para seu ambiente.
4. Especifique os endereços ou intervalos de IP permitidos e clique em **Salvar**.

### Como proteger chaves de API padrão sem restrições

Para continuar usando a API Gemini, proteja todas as chaves irrestritas.

#### Método A: restringir a chave apenas à API Gemini (AI Studio)

Se você usar a chave apenas para a API Gemini, proteja-a diretamente no AI Studio:

1. Na página **Chaves de API** do [Google AI Studio](https://aistudio.google.com/api-keys?hl=pt-br), localize as chaves marcadas com o rótulo **Sem restrições**.
2. Passe o cursor sobre o marcador e clique em **Adicionar restrições** na caixa de diálogo.
3. Selecione **Restringir apenas à API Gemini**.
4. Clique em **Restringir chave** para confirmar.

#### Método B: restringir a chave para outros serviços (console do Google Cloud)

Se a chave for compartilhada com outras APIs do Google (não recomendado), restrinja-a no console do Cloud. **Observação: as solicitações da API Gemini que usam essa chave vão falhar depois que essas restrições forem aplicadas.**

1. Acesse a [página "Credenciais" do console do Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pt-br).
2. Selecione o projeto e a chave de API.
3. Em **Restrições da API**, use o menu suspenso **Selecionar restrições da API** para
   escolher as APIs que você quer que essa chave acesse. Não selecione a **API
   Generative Language**.
4. Clique em **Salvar**. Crie uma chave separada e restrita no AI Studio para continuar
   usando a API Gemini.

### Chaves inativas bloqueadas

A partir de 7 de maio de 2026, a API Gemini vai bloquear chaves de API irrestritas que estiverem
inativas por um longo período. Essas chaves mostram uma tag **Bloqueado** no AI Studio. Você precisa gerar uma nova chave ou usar uma chave restrita para continuar.

## Migrar para uma chave de autenticação

Siga estas etapas para criar uma nova chave de API de autenticação e atualizar seus aplicativos:

1. Acesse a página [Chaves de API do AI Studio](https://aistudio.google.com/api-keys?hl=pt-br).
2. Verifique a coluna **Tipo de chave** para identificar as chaves listadas como **Padrão**.
3. Clique em **Criar chave de API** para gerar uma nova chave. Todas as novas chaves criadas no
   AI Studio são criadas automaticamente como chaves de autenticação.
4. Copie a nova chave de API de autenticação.
5. Atualize o código do aplicativo, as variáveis de ambiente e as configurações de implantação
   para usar a nova chave de API de autenticação.
6. Teste o aplicativo para confirmar se ele funciona corretamente com a nova chave.
7. Depois da verificação, exclua ou revogue a chave de tráfego antiga para evitar uso indevido.

## Limitações

O Google AI Studio impõe as seguintes limitações de gerenciamento de projetos e chaves:

- É possível criar no máximo 10 projetos por vez na página **Projetos** do Google AI Studio.
- As páginas **Chaves de API** e **Projetos** mostram um máximo de 100 chaves e 50 projetos.
- Somente as chaves de API irrestritas ou restritas especificamente à
  API Generative Language (API Gemini) são mostradas.

Para gerenciamento avançado de projetos ou para modificar chaves com outras restrições, use
a [página de credenciais do console do Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-25 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-25 UTC."],[],[]]
