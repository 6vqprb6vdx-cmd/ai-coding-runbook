---
source_url: https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ja
fetched_at: 2026-11-02T07:09:40.385686+00:00
title: "\u30bf\u30b9\u30af \u30aa\u30fc\u30b1\u30b9\u30c8\u30ec\u30fc\u30b7\u30e7\u30f3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# タスク オーケストレーション

Gemini Robotics ER モデルは、タスクを計画し、空間について推論して、目標を達成するためにどのようなアクションを実行し、どのオブジェクトを移動するかを推測できます。このページでは、カスタム ロボット API を介して[ピック アンド プレースを駆動](#calling-custom-robot-api)し、アイテムをボウルに入れるタスクをオーケストレートする例を示します。この例では標準の Gemini ER 2 モデルを使用します。ストリーミングの例については、[Gemini ER 2 ストリーミング ガイド](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja)をご覧ください。

実行可能な完全なコードについては、[ロボティクス クックブック](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)をご覧ください。

## カスタム ロボット API を使用する

この例では、カスタム ロボット API を使用したタスク オーケストレーションを示します。このサンプルでは、ピッキングと配置のオペレーション用に設計されたモック API を紹介します。青いブロックを拾ってオレンジ色のボウルに入れるタスクです。

![ブロックとボウルの画像](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=ja)

この例では、次のモックロボット API を使用します。

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

次の例では、プロンプトと画像をツール定義とともにモデルに送信します。次に、エージェント ループを実行します。各モデル レスポンスの後、リクエストされた関数呼び出し（`move`、`setGripperState`）を実行し、`previous_interaction_id` を使用して結果をモデルに返し、モデルが関数の呼び出しを停止するか、ステップの上限に達するまで繰り返します。

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

プロンプトとモックロボット API に基づくモデルの出力例を次に示します。出力には、モデルが順序付けたロボット関数呼び出しの出力が含まれます。

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

## 次のステップ

- [ストリーミングを使用したロボット工学](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) - 関数呼び出しを使用したリアルタイム ストリーミング（Gemini Robotics ER 2 のみ）。
- [動画の理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ja) - 動画からタスクの進捗状況を追跡します（ER 2 のみ）。
- [空間推論](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=ja) - ポインティング、トラッキング、境界ボックスの例。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-01 UTC。"],[],[]]
