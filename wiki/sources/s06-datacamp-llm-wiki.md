---
title: "S6 · DataCamp (2026)：LLM Wiki 架構解析"
type: source
sources: [S6]
updated: 2026-11-23
---

# S6 · DataCamp (2026)：LLM Wiki 架構解析

原始來源卡：[raw/s06-datacamp-llm-wiki.md](../../raw/s06-datacamp-llm-wiki.md) · 原文：<https://www.datacamp.com/blog/llm-wiki>

## 討論結果（N2）

- 強調：對照表、風險、現況 [討論]
- 不強調：「何時用哪個」的建議（文章本身也沒有給正式的判斷規則） [討論]

## 重點摘要

- 關鍵轉變是把「檢索」和「編譯」分開：RAG 在查詢時做事，LLM Wiki 在 ingest 時做事 [S6]
- 對照表六個面向：工作發生時間、留下什麼、新鮮度、跨來源綜合、維護、擴展性 [S6]
- 風險：來源改了要重新 ingest；每次 ingest 的小錯會累積成知識漂移（knowledge drift）；所有說法都是模型寫的，需要查證 [S6]
- 現況：截至 2026 年 7 月，多數實作仍是原型 [S6]
- 兩者互補，不是取代關係；有些系統在 wiki 長大後再對 wiki 跑 RAG [S6]

## 相關頁面

- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
- [LLM Wiki 的風險與限制](../concepts/llm-wiki-risks.md)
- [LLM Wiki](../concepts/llm-wiki.md)
