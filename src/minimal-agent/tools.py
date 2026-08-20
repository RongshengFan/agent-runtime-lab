import subprocess
from pathlib import Path


def read_file(path):
    return Path(path).expanduser().read_text(encoding="utf-8")


def run_shell(command, timeout=30):
    completed = subprocess.run(command, shell=True, text=True, capture_output=True, timeout=timeout)
    return (
        f"command: {command}\n"
        f"exit_code: {completed.returncode}\n"
        f"stdout:\n{completed.stdout}\n"
        f"stderr:\n{completed.stderr}"
    )


TOOLS = {"read_file": read_file, "run_shell": run_shell}


TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "read_file",
        "description": "Read a text file.",
        "parameters": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "type": "function",
        "name": "run_shell",
        "description": "Run a shell command.",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string"},
                "timeout": {"type": "integer", "default": 30},
            },
            "required": ["command"],
        },
    },
]


def execute_tool(name, arguments):
    return TOOLS[name](**arguments)
