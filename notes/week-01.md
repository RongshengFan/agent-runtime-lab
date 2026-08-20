# Week 01 — Minimal Agent Runtime

时间窗口：2026-08-20 ～ 2026-08-23

本周目标不是学完 Agent，而是完成第一个闭环：**亲手实现一个最小 tool-use Agent，并理解它为什么会逐步演化成 Runtime / Harness。**

## Day 0 — Bootstrap

- [x] 创建 `agent-runtime-lab`
- [x] 建立学习目标与仓库结构
- [ ] 选定模型 API 与开发语言
- [ ] 跑通普通 chat request

## Day 1 — Minimal Tool-use Agent

- [ ] 定义 2 个简单工具
- [ ] 定义 tool schema
- [ ] 实现 Tool Registry
- [ ] 实现 `LLM → tool_call → execute → tool_result → LLM` 循环
- [ ] 记录：普通 Chat 与 Agent 的最小差异是什么？

## Day 2 — From Agent to Runtime

- [ ] 定义 Turn
- [ ] 定义 Step
- [ ] 定义最小 Session Event
- [ ] 记录 `turn/start`、`step/start`、`user/message`、`assistant/message`、`tool/call`、`tool/result` 等事件
- [ ] 思考：为什么不直接维护一个 `messages[]` 就结束？

## Day 3 — Compare with DSH

- [ ] 阅读 DSH `core/agent`
- [ ] 阅读 DSH `core/agent-loop`
- [ ] 阅读 DSH `core/session`
- [ ] 将自己的实现映射到 DSH runtime spine
- [ ] 至少记录 5 个“为什么 DSH 要多做这一层？”的问题

## Output

- [ ] `src/minimal-agent` 可运行
- [ ] 一篇 `Agent Loop` 概念笔记
- [ ] 一份 DSH 对照笔记
- [ ] 第一篇文章草稿

## Questions Log

学习过程中把问题先记下来，不要求立即回答：

1. Agent 的最小定义到底是什么？
2. Tool Calling 本身为什么还不能等价于 Agent？
3. Turn 与 Step 的边界由谁决定？
4. Runtime state 与 model context 为什么不能混为一谈？
5. 一个最小 `messages[]` 实现在哪些需求出现后会开始失效？
