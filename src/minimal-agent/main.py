import json

from llm import llm
from tools import TOOL_SCHEMAS, execute_tool


while True:
    prompt = input("user> ").strip()
    if prompt in ("exit", "quit"):
        break

    messages = [
        {
            "role": "user",
            "content": "Only use tools when the user explicitly asks to read files or run shell commands. "
            f"If the request is unclear, ask a short clarification.\n\nUser request: {prompt}",
        }
    ]

    while True:
        response = llm(messages, tools=TOOL_SCHEMAS)
        messages.append(response)

        if response.get("content"):
            print("\nagent:")
            print(response["content"])

        if not response.get("tool_calls"):
            break

        for call in response["tool_calls"]:
            name = call["function"]["name"]
            args = json.loads(call["function"].get("arguments") or "{}")
            result = execute_tool(name, args)

            print(f"\ntool call: {name}({json.dumps(args, ensure_ascii=False)})")
            print(f"tool result:\n{result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call["id"],
                    "content": result,
                }
            )
