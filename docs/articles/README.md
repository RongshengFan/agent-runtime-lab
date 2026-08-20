# Articles

这里用于沉淀已经形成完整论证链的技术输出。文章不是学习笔记的简单润色，而应尽量包含：问题、实现/源码证据、推导过程、自己的判断与 trade-off。

## Planned

### 01. Agent 到底是什么？从一个最小 Agent Loop 开始

核心问题：

- 普通 LLM Chat 与 Agent 的最小差异是什么？
- Tool Calling 如何形成闭环？
- 为什么一个几十/几百行 Agent 很快会长出 Session、Context、Persistence、Sandbox 等 Runtime 能力？

### 02. 从一次真实 Session 反推 DeepSeek Harness

核心问题：

- human turn、model step、inbox 与 runtime context 如何协作？
- DSH 为什么把 Session Event Log 作为状态事实源？
- Everything is a Plugin 背后真正稳定的 core 是什么？

### 03. 从 Demo Agent 到 Production Harness

核心问题：

- Context、tool execution、recovery、concurrency、permission、sandbox 分别解决了什么工程问题？

### 04. 主流 Agent Runtime 设计比较

计划比较 DeepSeek Harness、Claude Agent SDK、OpenAI Agents SDK、LangGraph、OpenHands / SWE-agent。
