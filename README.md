# Agent Runtime Lab

> 从 Agent SDK / 平台集成出发，系统理解、实现并分析现代 AI Agent Runtime / Harness。

这个仓库不是框架教程合集，而是一个持续迭代的 **Agent Engineering 学习与实验项目**。目标是通过「自己实现 → 阅读源码 → 做实验 → 写出判断」的方式，把零散概念沉淀成可运行代码、技术笔记和公开文章。

## Current Goal

用 1 个月建立 Agent Runtime 的系统认知，并形成一组可持续积累的工程作品与技术输出。

当前阶段重点：

- 从零实现一个不依赖 Agent SDK 的 minimal tool-use agent
- 理解 Agent Loop、Turn、Step、Session、Context 与 Tool Runtime
- 以 DeepSeek Harness（DSH）为主要源码研究对象
- 后续横向比较 Claude Agent SDK、OpenAI Agents SDK、LangGraph、OpenHands 等体系

## Learning Loop

```text
问题 / 概念
    ↓
最小实现或实验
    ↓
源码验证
    ↓
形成自己的判断
    ↓
笔记 / 文章 / 代码
```

## Repository Structure

```text
agent-runtime-lab/
├── src/
│   └── minimal-agent/      # 从零实现 Agent Runtime
├── docs/
│   ├── concepts/           # 已经能够独立解释的核心概念
│   ├── dsh/                # DeepSeek Harness 源码研究
│   └── articles/           # 长文草稿与文章索引
├── experiments/            # Runtime 机制实验
└── notes/                  # 阶段性学习记录与问题
```

## Roadmap

### Phase 1 — Minimal Agent

- [ ] 完成一次普通 LLM chat request
- [ ] 定义 Tool schema 与 Tool Registry
- [ ] 实现 tool-use Agent Loop
- [ ] 引入 Turn / Step 模型
- [ ] 引入最小 Session Event Log
- [ ] 写出第一篇阶段文章

### Phase 2 — Agent Runtime Spine

- [ ] Agent / Agent Loop
- [ ] Session / Context
- [ ] System Prompt
- [ ] Tool execution pipeline
- [ ] LLM adapter
- [ ] Streaming / cancellation / error handling

### Phase 3 — Production Runtime

- [ ] Persistence / resume / replay
- [ ] Context compaction
- [ ] Tool concurrency
- [ ] Permission / approval / sandbox
- [ ] Subagent
- [ ] Observability / tracing

### Phase 4 — Comparative Study

- [ ] DeepSeek Harness
- [ ] Claude Agent SDK
- [ ] OpenAI Agents SDK
- [ ] LangGraph
- [ ] OpenHands / SWE-agent

## Week 1 Deliverable

当前第一阶段只追求一个最小闭环：

1. 自己写出一个可运行的 tool-use Agent Loop。
2. 能解释普通 Chat 与 Agent 的差异。
3. 给执行过程加入最小 Turn / Step / Session 表达。
4. 用自己的实现去映射 DSH 的 Agent Runtime 设计。
5. 形成第一篇公开技术文章。

## Working Principle

- 不追求先把所有 Agent 概念学完再开始。
- 不复制框架文档；所有结论尽量经过代码、实验或源码验证。
- 笔记只记录自己已经能解释清楚的内容，以及尚未解决的问题。
- 代码优先保持小而可读，复杂能力按真实问题逐步加入。

---

This repository is intentionally iterative. The implementation and notes will evolve as the understanding of Agent Runtime deepens.
