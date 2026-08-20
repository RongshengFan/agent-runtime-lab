# DeepSeek Harness Study

DSH 是当前 Agent Runtime / Harness 学习的主要源码样本，但不是这个仓库的最终边界。

## Runtime Spine

优先沿下面这条纵向执行链阅读，而不是遍历全部 package：

```text
core/agent
    ↓
core/agent-loop
    ↓
core/session
    ↓
core/system-prompt
    ↓
core/tools
    ↓
llm/llm
```

## Questions to Answer

- Agent、Harness、Platform 的边界在哪里？
- 一个 human turn 为什么可能包含多个 model step？
- Session 为什么采用 append-only event log？
- 模型可见上下文如何从 durable state 重建？
- Tool execution 为什么需要 policy、approval、sandbox 与 ordered result semantics？
- Everything is a Plugin 是否真的意味着“没有 core”？
- DSH 为 composability、recoverability 与 governability 分别付出了什么复杂度？

## Method

每个结论尽量同时找到三类证据：

1. 官方架构文档；
2. 核心源码；
3. 真实 session / runtime trace。

目标不是复述 DSH 文档，而是借 DSH 建立可迁移的 Agent Runtime 认知。
