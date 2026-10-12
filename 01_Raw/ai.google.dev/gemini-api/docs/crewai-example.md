---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=it
fetched_at: 2026-10-12T07:15:40.071139+00:00
title: "Analisi dell'assistenza clienti con Gemini e CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Analisi dell'assistenza clienti con Gemini e CrewAI

[CrewAI](https://docs.crewai.com/introduction) è un framework per orchestrare
agenti AI autonomi che collaborano per raggiungere obiettivi complessi. Ti consente di
definire gli agenti specificando ruoli, obiettivi e retroscena, quindi di definire le attività
per loro.

Questo esempio mostra come creare un sistema multi-agente per analizzare i dati dell'assistenza clienti per identificare i problemi e proporre miglioramenti dei processi utilizzando Gemini 3 Flash, generando un report destinato a essere letto da un Chief Operating Officer (COO).

La guida ti mostrerà come creare una "troupe" di agenti AI in grado di svolgere le seguenti attività:

1. Recuperare e analizzare i dati dell'assistenza clienti (simulati in questo esempio).
2. Identificare problemi ricorrenti e colli di bottiglia dei processi.
3. Suggerire miglioramenti pratici.
4. Compilare i risultati in un report conciso adatto a un COO.

Devi avere una chiave API Gemini. Se non ne hai già una, puoi [ottenerla in
Google AI Studio](https://aistudio.google.com/apikey?hl=it).

```
pip install "crewai[tools]"
```

Imposta la chiave API Gemini come variabile di ambiente denominata `GEMINI_API_KEY`, quindi configura CrewAI per utilizzare il modello Gemini.

```
import os
from crewai import LLM

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model='gemini/gemini-3.6-flash',
    api_key=gemini_api_key,
    temperature=1.0  # Use the Gemini 3 recommended temperature
)
```

## Definisci i componenti

Crea applicazioni CrewAI utilizzando **Strumenti**, **Agenti**, **Attività** e la
**Troupe** stessa. Le sezioni seguenti spiegano ciascuno di questi componenti.

### Strumenti

Gli strumenti sono funzionalità che gli agenti possono utilizzare per interagire con il mondo esterno o eseguire azioni specifiche. Qui definisci uno strumento segnaposto per simulare il recupero dei dati dell'assistenza clienti. In un'applicazione reale, ti connetteresti a un database, un'API o un file system. Per saperne di più sugli strumenti, consulta la [guida agli strumenti
di CrewAI](https://docs.crewai.com/concepts/tools).

```
from crewai.tools import BaseTool

# Placeholder tool for fetching customer support data
class CustomerSupportDataTool(BaseTool):
    name: str = "Customer Support Data Fetcher"
    description: str = (
      "Fetches recent customer support interactions, tickets, and feedback. "
      "Returns a summary string.")

    def _run(self, argument: str) -> str:
        # In a real scenario, this would query a database or API.
        # For this example, return simulated data.
        print(f"--- Fetching data for query: {argument} ---")
        return (
            """Recent Support Data Summary:
- 50 tickets related to 'login issues'. High resolution time (avg 48h).
- 30 tickets about 'billing discrepancies'. Mostly resolved within 12h.
- 20 tickets on 'feature requests'. Often closed without resolution.
- Frequent feedback mentions 'confusing user interface' for password reset.
- High volume of calls related to 'account verification process'.
- Sentiment analysis shows growing frustration with 'login issues' resolution time.
- Support agent notes indicate difficulty reproducing 'login issues'."""
        )

support_data_tool = CustomerSupportDataTool()
```

### Agenti

Gli agenti sono i singoli operatori AI della tua troupe. Ogni agente ha un
`role`, `goal`, `backstory`, un `llm` assegnato e `tools` facoltativi specifici. Per saperne di più sugli agenti, consulta la [guida agli agenti di CrewAI](https://docs.crewai.com/concepts/agents).

```
from crewai import Agent

# Agent 1: Data analyst
data_analyst = Agent(
    role='Customer Support Data Analyst',
    goal='Analyze customer support data to identify trends, recurring issues, and key pain points.',
    backstory=(
        """You are an expert data analyst specializing in customer support operations.
        Your strength lies in identifying patterns and quantifying problems from raw support data."""
    ),
    verbose=True,
    allow_delegation=False,  # This agent focuses on its specific task
    tools=[support_data_tool],  # Assign the data fetching tool
    llm=gemini_llm  # Use the configured Gemini LLM
)

# Agent 2: Process optimizer
process_optimizer = Agent(
    role='Process Optimization Specialist',
    goal='Identify bottlenecks and inefficiencies in current support processes based on the data analysis. Propose actionable improvements.',
    backstory=(
        """You are a specialist in optimizing business processes, particularly in customer support.
        You excel at pinpointing root causes of delays and inefficiencies and suggesting concrete solutions."""
    ),
    verbose=True,
    allow_delegation=False,
    # No tools needed, this agent relies on the context provided by data_analyst.
    llm=gemini_llm
)

# Agent 3: Report writer
report_writer = Agent(
    role='Executive Report Writer',
    goal='Compile the analysis and improvement suggestions into a concise, clear, and actionable report for the COO.',
    backstory=(
        """You are a skilled writer adept at creating executive summaries and reports.
        You focus on clarity, conciseness, and highlighting the most critical information and recommendations for senior leadership."""
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)
```

### Tasks

Le attività definiscono le assegnazioni specifiche per gli agenti. Ogni attività ha un
`description`, `expected_output` e viene assegnata a un `agent`. Per impostazione predefinita, le attività vengono eseguite in sequenza e includono il contesto dell'attività precedente. Per saperne di più sulle attività, consulta la [guida alle attività di CrewAI](https://docs.crewai.com/concepts/tasks).

```
from crewai import Task

# Task 1: Analyze data
analysis_task = Task(
    description=(
        """Fetch and analyze the latest customer support interaction data (tickets, feedback, call logs)
        focusing on the last quarter. Identify the top 3-5 recurring issues, quantify their frequency
        and impact (e.g., resolution time, customer sentiment). Use the Customer Support Data Fetcher tool."""
    ),
    expected_output=(
        """A summary report detailing the key findings from the customer support data analysis, including:
- Top 3-5 recurring issues with frequency.
- Average resolution times for these issues.
- Key customer pain points mentioned in feedback.
- Any notable trends in sentiment or support agent observations."""
    ),
    agent=data_analyst  # Assign task to the data_analyst agent
)

# Task 2: Identify bottlenecks and suggest improvements
optimization_task = Task(
    description=(
        """Based on the data analysis report provided by the Data Analyst, identify the primary bottlenecks
        in the support processes contributing to the identified issues (especially the top recurring ones).
        Propose 2-3 concrete, actionable process improvements to address these bottlenecks.
        Consider potential impact and ease of implementation."""
    ),
    expected_output=(
        """A concise list identifying the main process bottlenecks (e.g., lack of documentation for agents,
        complex escalation path, UI issues) linked to the key problems.
A list of 2-3 specific, actionable recommendations for process improvement
(e.g., update agent knowledge base, simplify password reset UI, implement proactive monitoring)."""
    ),
    agent=process_optimizer  # Assign task to the process_optimizer agent
    # This task implicitly uses the output of analysis_task as context
)

# Task 3: Compile COO report
report_task = Task(
    description=(
        """Compile the findings from the Data Analyst and the recommendations from the Process Optimization Specialist
        into a single, concise executive report for the COO. The report should clearly state:
1. The most critical customer support issues identified (with brief data points).
2. The key process bottlenecks causing these issues.
3. The recommended process improvements.
Ensure the report is easy to understand, focuses on actionable insights, and is formatted professionally."""
    ),
    expected_output=(
        """A well-structured executive report (max 1 page) summarizing the critical support issues,
        underlying process bottlenecks, and clear, actionable recommendations for the COO.
        Use clear headings and bullet points."""
    ),
    agent=report_writer  # Assign task to the report_writer agent
)
```

### Banda

Il `Crew` riunisce gli agenti e le attività, definendo il processo del flusso di lavoro
(ad esempio "sequenziale").

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## Esegui la troupe

Infine, avvia l'esecuzione della troupe con gli input necessari.

```
# Start the crew's work
print("--- Starting Customer Support Analysis Crew ---")
# The 'inputs' dictionary provides initial context if needed by the first task.
# In this case, the tool simulates data fetching regardless of the input.
result = support_analysis_crew.kickoff(inputs={'data_query': 'last quarter support data'})

print("--- Crew Execution Finished ---")
print("--- Final Report for COO ---")
print(result)
```

Lo script verrà ora eseguito. Il `Data Analyst` utilizzerà lo strumento, il `Process
Optimizer` analizzerà i risultati e il `Report Writer` compilerà il
report finale, che verrà poi stampato nella console. L'impostazione `verbose=True` mostrerà il processo di pensiero e le azioni dettagliate di ogni agente.

Per saperne di più su CrewAI, consulta la guida introduttiva a [CrewAI
.](https://docs.crewai.com/introduction)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-12 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-12 UTC."],[],[]]
