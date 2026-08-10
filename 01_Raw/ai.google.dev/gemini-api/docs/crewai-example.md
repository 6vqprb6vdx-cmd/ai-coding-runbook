---
source_url: https://ai.google.dev/gemini-api/docs/crewai-example?hl=es-419
fetched_at: 2026-08-10T03:15:59.027036+00:00
title: "An\u00e1lisis de la asistencia al cliente con Gemini y CrewAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Análisis de la asistencia al cliente con Gemini y CrewAI

[CrewAI](https://docs.crewai.com/introduction) es un framework para organizar agentes de IA autónomos que colaboran para lograr objetivos complejos. Te permite definir agentes especificando roles, objetivos y antecedentes, y, luego, definir tareas para ellos.

En este ejemplo, se muestra cómo compilar un sistema multiagente para analizar los datos de asistencia al cliente, identificar problemas y proponer mejoras en los procesos con Gemini 3 Flash, y generar un informe que leerá el director de operaciones (COO).

En la guía, se muestra cómo crear un "equipo" de agentes de IA que pueden realizar las siguientes tareas:

1. Recupera y analiza los datos de asistencia al cliente (simulados en este ejemplo).
2. Identificar problemas recurrentes y cuellos de botella en los procesos
3. Sugerir mejoras prácticas
4. Compila los hallazgos en un informe conciso adecuado para un COO.

Necesitas una clave de la API de Gemini. Si aún no tienes una, puedes [obtener una en Google AI Studio](https://aistudio.google.com/apikey?hl=es-419).

```
pip install "crewai[tools]"
```

Establece tu clave de API de Gemini como una variable de entorno llamada `GEMINI_API_KEY` y, luego, configura CrewAI para que use el modelo de Gemini.

```
import os
from crewai import LLM

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model='gemini/gemini-3.5-flash',
    api_key=gemini_api_key,
    temperature=1.0  # Use the Gemini 3 recommended temperature
)
```

## Define componentes

Crea aplicaciones de CrewAI con **Herramientas**, **Agentes**, **Tareas** y el **Equipo** en sí. En las siguientes secciones, se explica cada uno de estos componentes.

### Herramientas

Las herramientas son capacidades que los agentes pueden usar para interactuar con el mundo exterior o realizar acciones específicas. Aquí, definirás una herramienta de marcador de posición para simular la recuperación de datos de asistencia al cliente. En una aplicación real, te conectarías a una base de datos, una API o un sistema de archivos. Para obtener más información sobre las herramientas, consulta la [guía de herramientas de CrewAI](https://docs.crewai.com/concepts/tools).

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

### Agentes

Los agentes son los trabajadores individuales de IA de tu equipo. Cada agente tiene un `role`, `goal`, `backstory`, un `llm` asignado y un `tools` opcional específicos. Para obtener más información sobre los agentes, consulta la [guía de agentes de CrewAI](https://docs.crewai.com/concepts/agents).

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

Las tareas definen las asignaciones específicas para los agentes. Cada tarea tiene un `description`, un `expected_output` y se asigna a un `agent`. De forma predeterminada, las tareas se ejecutan de forma secuencial y se incluye el contexto de la tarea anterior. Para obtener más información sobre las tareas, consulta la [guía de tareas de CrewAI](https://docs.crewai.com/concepts/tasks).

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

### Equipo de rodaje

El `Crew` reúne a los agentes y las tareas, y define el proceso del flujo de trabajo (por ejemplo, "secuencial").

```
from crewai import Crew, Process

support_analysis_crew = Crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task],
    process=Process.sequential,  # Tasks will run sequentially in the order defined
    verbose=True
)
```

## Ejecuta el equipo

Por último, inicia la ejecución del equipo con las entradas necesarias.

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

Ahora se ejecutará la secuencia de comandos. El `Data Analyst` usará la herramienta, el `Process
Optimizer` analizará los resultados y el `Report Writer` compilará el informe final, que luego se imprimirá en la consola. El parámetro de configuración `verbose=True` mostrará el proceso de pensamiento y las acciones detallados de cada agente.

Para obtener más información sobre CrewAI, consulta la [introducción a CrewAI](https://docs.crewai.com/introduction).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-10 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-10 (UTC)"],[],[]]
