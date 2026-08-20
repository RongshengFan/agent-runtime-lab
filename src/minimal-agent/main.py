import json

from llm import llm
from tools import TOOL_SCHEMAS, execute_tool


SYSTEM_PROMPT = (
    "你是一个Mini Agent。默认使用中文回答。"
    "只有当用户明确要求读取文件或执行 shell 命令时才使用工具；"
    "如果用户请求不清楚，请用中文追问。"
    "如果用户只是在简单询问问题或者和你聊天，请用中文回复即可。"
)

while True:
    prompt = input("user> ").strip()
    if prompt in ("exit", "quit"):
        break
    if not prompt:
        continue

    messages = [{"role": "user", "content": f"{SYSTEM_PROMPT}\n\n用户请求：{prompt}"}]

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
