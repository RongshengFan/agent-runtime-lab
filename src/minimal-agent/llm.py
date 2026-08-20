import json
import os
import urllib.request


BASE_URL = ""
MODEL = ""


def llm(messages, tools=None):
    payload = {"model": MODEL, "messages": messages, "temperature": 0}
    if tools:
        payload["tools"] = tools
        payload["tool_choice"] = "auto"

    headers = {"Content-Type": "application/json"}
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    request = urllib.request.Request(BASE_URL, json.dumps(payload).encode("utf-8"), headers, method="POST")
    data = json.loads(urllib.request.urlopen(request, timeout=120).read().decode("utf-8"))
    return data["choices"][0]["message"]
