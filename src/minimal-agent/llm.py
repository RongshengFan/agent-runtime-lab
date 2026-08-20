import json
import os
import urllib.request


BASE_URL = "https://ark.cn-beijing.volces.com/api/v3/responses"
MODEL = "deepseek-v4-flash-ga-260731"
PREVIOUS_RESPONSE_ID = None


def llm(messages, tools=None):
    global PREVIOUS_RESPONSE_ID

    input_items = to_input(messages)
    payload = {"model": MODEL, "input": input_items, "store": True}
    if PREVIOUS_RESPONSE_ID:
        payload["previous_response_id"] = PREVIOUS_RESPONSE_ID
    if tools and not is_tool_output(input_items):
        payload["tools"] = tools

    api_key = os.getenv("ARK_API_KEY")
    if not api_key:
        raise RuntimeError("set ARK_API_KEY first")
    headers = {"Content-Type": "application/json"}
    headers["Authorization"] = f"Bearer {api_key}"

    request = urllib.request.Request(BASE_URL, json.dumps(payload).encode("utf-8"), headers, method="POST")
    data = json.loads(urllib.request.urlopen(request, timeout=120).read().decode("utf-8"))
    PREVIOUS_RESPONSE_ID = data["id"]
    return to_message(data)


def is_tool_output(input_items):
    return input_items and input_items[0].get("type") == "function_call_output"


def to_input(messages):
    tool_outputs = []
    for message in reversed(messages):
        if message.get("role") != "tool":
            break
        tool_outputs.append(message)

    if tool_outputs:
        return [
            {"type": "function_call_output", "call_id": m["tool_call_id"], "output": m["content"]}
            for m in reversed(tool_outputs)
        ]

    return [
        {"type": "message", "role": m["role"], "content": m["content"]}
        for m in messages
        if m.get("role") in ("user", "assistant") and m.get("content")
    ]


def to_message(data):
    text = []
    tool_calls = []

    for item in data.get("output", []):
        if item.get("type") == "function_call":
            tool_calls.append(
                {
                    "id": item["call_id"],
                    "type": "function",
                    "function": {"name": item["name"], "arguments": item.get("arguments") or "{}"},
                }
            )
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    text.append(content.get("text") or "")

    message = {"role": "assistant", "content": "".join(text) or data.get("output_text", "")}
    if tool_calls:
        message["tool_calls"] = tool_calls
    return message
