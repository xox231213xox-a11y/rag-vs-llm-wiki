---
title: "S7 · brtrx (2026)：Bias-Aware Stateful Lint"
type: source
sources: [S7]
updated: 2026-11-23
---

# S7 · brtrx (2026)：Bias-Aware Stateful Lint

原始來源卡：[raw/s07-brtrx-ingestion-bias.md](../../raw/s07-brtrx-ingestion-bias.md) · 原文：<https://gist.github.com/brtrx/ba595fd01e344d797cb66d34d982ecad>

## 討論結果（N2）

- 強調：Ingestion bias、Lint 的盲點、解法、補救（四項全選） [討論]

## 重點摘要

- Ingestion bias：一次 ingest 一篇時，最早進來的來源會決定用詞與框架，後來的來源只是被塞進這個框架 [S7]
- Lint 的盲點：lint 抓得到斷鏈、孤兒頁這類結構問題，抓不到框架偏誤；來源超過 50 篇時一次 lint 還可能塞爆 context [S7]
- 解法：每次只 lint 5 個來源、用固定的隨機順序、把發現記在 scratchpad（修好標 FIXED 不刪除） [S7]
- 補救：換順序從 raw 重建、請 AI 反駁目前的框架、重寫疑似偏向早期來源的頁面 [S7]

## 相關頁面

- [Ingestion bias（攝入順序偏誤）](../concepts/ingestion-bias.md)
- [LLM Wiki 的風險與限制](../concepts/llm-wiki-risks.md)
- [LLM Wiki 的三個操作](../concepts/wiki-operations.md)
