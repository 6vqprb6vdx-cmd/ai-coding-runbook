---
source_url: https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=pl
fetched_at: 2026-09-21T05:49:10.639231+00:00
title: "Orkiestracja zada\u0144 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Orkiestracja zadań

Modele Gemini Robotics ER potrafią planować zadania i rozumować o przestrzeni, wnioskując, jakie działania należy podjąć i jakie obiekty przenieść, aby osiągnąć cel. Ta strona
zawiera przykład sterowania operacją [podnoszenia i przenoszenia](https://ai.google.dev/gemini-api/docs/calling-custom-robot-api?hl=pl)
za pomocą niestandardowego interfejsu API robota, aby skoordynować zadanie umieszczenia przedmiotu
w misce. W tym przykładzie używamy standardowego modelu Gemini ER 2. Przykład przesyłania strumieniowego
znajdziesz w [przewodniku Gemini ER 2 Streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl).

Pełny kod, który można uruchomić, znajdziesz w
[zbiorze przepisów Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Korzystanie z niestandardowego interfejsu API robota

Ten przykład pokazuje koordynację zadań za pomocą niestandardowego interfejsu API robota. Przedstawia on pozorowany interfejs API przeznaczony do operacji podnoszenia i przenoszenia. Zadanie polega na podniesieniu niebieskiego klocka i umieszczeniu go w pomarańczowej misce:

![Obraz przedstawiający blok i miskę](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=pl)

W tym przykładzie używamy tego pozorowanego interfejsu API robota:

### Python

```
def move(x, y, high):
  print(f"Mock Robot: Moving to coordinates: {x}, {y}, {'high above table' if high else 'down at table level'}")

def setGripperState(opened):
  print(f"Mock Robot: {'Opening gripper' if opened else 'Closing gripper'}")

robot_origin_y = 300
robot_origin_x = 500

move_function = {
    "type": "function",
    "name": "move",
    "description": "Moves the arm to the given coordinates.",
    "parameters": {
        "type": "object",
        "properties": {
            "x": {"type": "integer", "description": "X coordinate relative to the origin"},
            "y": {"type": "integer", "description": "Y coordinate relative to the origin"},
            "high": {"type": "boolean", "description": "Set to True to lift the robot arm above the scene for avoiding obstacles. Set to False to place the gripper on the surface."}
        },
        "required": ["x", "y", "high"]
    }
}

set_gripper_state_function = {
    "type": "function",
    "name": "setGripperState",
    "description": "Opens or closes the robot's gripper.",
    "parameters": {
        "type": "object",
        "properties": {
            "opened": {"type": "boolean", "description": "True opens the gripper, False closes the gripper."}
        },
        "required": ["opened"]
    }
}
```

Ten przykład wysyła prompt i obraz do modelu wraz z definicjami narzędzi. Następnie uruchamia pętlę agenta: po każdej odpowiedzi modelu wykonuje wszystkie żądane wywołania funkcji (`move`, `setGripperState`), zwraca wyniki do modelu za pomocą `previous_interaction_id` i powtarza, dopóki model nie przestanie wywoływać funkcji lub nie zostanie osiągnięty limit kroków.

### Python

```
prompt = (
    "You are a robotic arm with six degrees-of-freedom. "
    f"The origin point for calculating the moves is at normalized point y={robot_origin_y}, x={robot_origin_x}. "
    "Use this as the new (0,0) for calculating moves, allowing x and y to be negative.\n\n"
    "Find the blue block and the orange bowl. Calculate their coordinates relative to the origin.\n"
    "Perform a pick and place operation where you pick up the blue block and place it into the orange bowl. "
    "Call the appropriate sequence of functions to complete this operation."
)

# 1. Initial Interaction
interaction = client.interactions.create(
    model=MODEL_ID,
    input=[{"type": "user_input", "content": [
        {"type": "image", "data": img_b64, "mime_type": "image/png"},
        {"type": "text", "text": prompt}
    ]}],
    tools=[move_function, set_gripper_state_function],
    generation_config={"thinking_level": "low"}
)

print("\n--- Executing Orchestrated Plan ---")

max_steps = 15 # Safety limit to prevent infinite loops
step_count = 0

# 2. The Agentic Loop
while step_count < max_steps:
    step_count += 1

    # Check if the model wants to call any functions
    tool_calls = [step for step in interaction.steps if step.type == "function_call"]

    if not tool_calls:
        # If no tools were called, the model is finished with the sequence
        print("Sequence complete.")
        if interaction.output_text:
            print(f"Model Summary: {interaction.output_text}")
        break

    function_results = []

    for step in tool_calls:
        function_name = step.name
        arguments = step.arguments

        # Execute the mock function
        if function_name == "move":
            move(**arguments)
        elif function_name == "setGripperState":
            setGripperState(**arguments)
        else:
            print(f"Unknown function: {function_name}")

        # 3. Create a result object to tell the model the function succeeded
        function_results.append({
            "type": "function_result",
            "name": step.name,
            "call_id": step.id,
            "result": [{"type": "text", "text": '{"status": "success"}'}]
        })

    # 4. Send the results back to the model, passing previous_interaction_id
    # so it remembers the conversation history and generates the NEXT step
    interaction = client.interactions.create(
        model=MODEL_ID,
        previous_interaction_id=interaction.id,
        tools=[move_function, set_gripper_state_function],
        input=function_results
    )
```

Poniżej przedstawiamy możliwe dane wyjściowe modelu na podstawie promptu i pozorowanego interfejsu API robota. Dane wyjściowe obejmują dane wyjściowe wywołań funkcji robota, które model połączył w sekwencję.

```
--- Executing Orchestrated Plan ---
Mock Robot: Opening gripper
Mock Robot: Moving to coordinates: 160, 440, high above table
Mock Robot: Moving to coordinates: 160, 440, down at table level
Mock Robot: Closing gripper
Mock Robot: Moving to coordinates: 160, 440, high above table
Mock Robot: Moving to coordinates: -250, 60, high above table
Mock Robot: Moving to coordinates: -250, 60, down at table level
Mock Robot: Opening gripper
Mock Robot: Moving to coordinates: -250, 60, high above table
Sequence complete.
Model Summary: I have completed the task of picking up the blue block and placing it into the orange bowl.
```

## Co dalej?

- [Robotyka z przesyłaniem strumieniowym](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl) – przesyłanie strumieniowe w czasie rzeczywistym z wywoływaniem funkcji (tylko Gemini Robotics ER 2).
- [Rozumienie obrazu](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=pl) – śledzenie postępu zadania na podstawie filmu (tylko ER 2).
- [Rozumowanie przestrzenne](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=pl) – przykłady wskazywania, śledzenia i ramki ograniczającej.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-08 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-08 UTC."],[],[]]
