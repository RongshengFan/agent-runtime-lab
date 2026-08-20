# Minimal Agent

这里是一版不依赖 Agent SDK 的最小 Agent loop，只保留核心闭环。

闭环只有这几步：

```text
User
  ↓
messages
  ↓
LLM
  ↓
tool_call ?
  ├─ no  → final answer
  └─ yes → execute tool → tool_result → messages → LLM
```

## Files

- `main.py`: 终端入口、agent loop、工具调度和终端打印
- `llm.py`: LLM API 请求
- `tools.py`: 工具 schema 和执行

## Run

使用 OpenAI-compatible Chat Completions API：

```bash
cd /Users/bytedance/Desktop/agent-runtime-lab
export OPENAI_API_KEY="your-api-key"

python src/minimal-agent/main.py "读取 src/minimal-agent/README.md，然后用一句话总结"
```

模型和 API URL 直接改 `llm.py` 顶部的 `MODEL` / `URL`。

## Tools

- `read_file(path)`: 读取 UTF-8 文本文件
- `run_shell(command, timeout=30)`: 执行 shell 命令，返回 exit code、stdout、stderr

运行时会把 LLM 输出、tool call 和 tool result 打印到终端。
