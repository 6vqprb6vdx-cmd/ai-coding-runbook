---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=de
fetched_at: 2026-09-21T05:52:42.713643+00:00
title: "Kundensupportanalyse mit Gemini und CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Kundensupportanalyse mit Gemini und CrewAI

[CrewAI](https://docs.crewai.com/introduction) ist ein Framework zur Orchestrierung
autonomer KI-Agenten, die zusammenarbeiten, um komplexe Ziele zu erreichen. Sie können Agenten definieren, indem Sie Rollen, Ziele und Hintergrundinformationen angeben und dann Aufgaben
für sie definieren.

In diesem Beispiel wird gezeigt, wie Sie ein System mit mehreren Agenten erstellen, um Kundensupportdaten zu analysieren, Probleme zu identifizieren und Prozessverbesserungen mit Gemini 3 Flash vorzuschlagen. Dabei wird ein Bericht erstellt, der für einen Chief Operating Officer (COO) bestimmt ist.

In dieser Anleitung erfahren Sie, wie Sie eine „Crew“ von KI-Agenten erstellen, die folgende Aufgaben ausführen können:

1. Kundensupportdaten abrufen und analysieren (in diesem Beispiel simuliert).
2. Wiederkehrende Probleme und Engpässe im Prozess identifizieren.
3. Umsetzbare Verbesserungen vorschlagen.
4. Die Ergebnisse in einem prägnanten Bericht zusammenfassen, der für einen COO geeignet ist.

Sie benötigen einen Gemini API-Schlüssel. Wenn Sie noch keinen haben, können Sie [einen in
Google AI Studio](https://aistudio.google.com/apikey?hl=de) erstellen.

```
pip install "crewai[tools]"
```

Legen Sie Ihren Gemini API-Schlüssel als Umgebungsvariable mit dem Namen `GEMINI_API_KEY` fest und konfigurieren Sie CrewAI so, dass das Gemini-Modell verwendet wird.

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

## Komponenten definieren

Erstellen Sie CrewAI-Anwendungen mit **Tools**, **Agents**, **Tasks** und der
**Crew** selbst. In den folgenden Abschnitten werden die einzelnen Komponenten erläutert.

### Tools

Tools sind Funktionen, mit denen Agenten mit der Außenwelt interagieren oder bestimmte Aktionen ausführen können. Hier definieren Sie ein Platzhalter-Tool, um das Abrufen von Kundensupportdaten zu simulieren. In einer echten Anwendung würden Sie eine Verbindung zu einer Datenbank, API oder einem Dateisystem herstellen. Weitere Informationen zu Tools finden Sie in der Anleitung zu [CrewAI
Tools](https://docs.crewai.com/concepts/tools).

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

### Agents

Agents sind die einzelnen KI-Mitarbeiter in Ihrer Crew. Jeder Agent hat eine bestimmte `role`, ein `goal`, eine `backstory`, ein zugewiesenes `llm` und optionale `tools`. Weitere Informationen zu Agents finden Sie in der Anleitung zu [CrewAI-Agents
guide](https://docs.crewai.com/concepts/agents).

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

Tasks definieren die spezifischen Aufgaben für die Agenten. Jede Aufgabe hat eine `description` und eine `expected_output` und ist einem `agent` zugewiesen. Aufgaben werden standardmäßig sequenziell ausgeführt und enthalten den Kontext der vorherigen Aufgabe. Weitere Informationen zu Aufgaben finden Sie in der Anleitung zu [CrewAI-Aufgaben
guide](https://docs.crewai.com/concepts/tasks).

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

### Crew

Die `Crew` führt die Agenten und Aufgaben zusammen und definiert den Workflowprozess (z. B. „sequenziell“).

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## Crew ausführen

Starten Sie schließlich die Ausführung der Crew mit allen erforderlichen Eingaben.

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

Das Skript wird jetzt ausgeführt. Der `Data Analyst` verwendet das Tool, der `Process
Optimizer` analysiert die Ergebnisse und der `Report Writer` erstellt den
Abschlussbericht, der dann in der Console ausgegeben wird. Mit der Einstellung `verbose=True` werden der detaillierte Denkprozess und die Aktionen jedes Agenten angezeigt.

Weitere Informationen zu CrewAI finden Sie in der [CrewAI
Einführung](https://docs.crewai.com/introduction).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
