# Minimal Agent

这里用于从零实现一个不依赖 Agent SDK 的最小 Agent Runtime。

第一阶段只实现最小闭环：

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

## Implementation Order

1. 普通 LLM chat request
2. Tool schema
3. Tool Registry
4. Tool-use loop
5. Turn / Step
6. Session Event Log
7. Streaming / cancellation / error handling

原则：先保持实现小而清楚，再通过真实问题逐步增加 Runtime 能力。
