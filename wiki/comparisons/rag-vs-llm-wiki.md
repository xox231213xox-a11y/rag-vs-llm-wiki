---
title: "RAG vs LLM Wiki"
type: comparison
sources: [S1, S4, S6]
updated: 2026-11-23
---

# RAG vs LLM Wiki

## 一句話差別

- RAG 在「被問的時候」才去原始資料找；LLM Wiki 在「資料進來的時候」就先整理好 [S6][S1]

## 對照表

| 面向 | RAG | LLM Wiki | 來源 |
|---|---|---|---|
| 工作發生時間 | 查詢時 | ingest 時 | S6 |
| 留下什麼 | 查詢之間什麼都不留 | 編譯好的 markdown 頁面 | S6 |
| 新鮮度 | 直接讀即時來源 | 要重新 ingest，會落後 | S6 |
| 跨來源綜合 | 可能漏掉跨 chunk 的關聯 | 綜合做一次並經過審視 | S6 |
| 維護 | 建好索引後幾乎不用 | 需要 lint、矛盾檢查 | S6 |
| 擴展性 | 可預期的搜尋問題 | 要保持一致，變大後需要索引或搜尋 | S6 |

- 上表六個面向整理自 DataCamp 的對照 [S6]

## 兩者的關係

- 兩者互補而不是取代；wiki 變大後也可以對 wiki 跑 RAG [S6]
- 知識庫很小（低於 200,000 token）時，Anthropic 建議連 RAG 都不必做，直接整份放進 prompt [S4]

## 相關頁面

- [RAG（檢索增強生成）](../concepts/rag.md)
- [LLM Wiki](../concepts/llm-wiki.md)
- [LLM Wiki 的風險與限制](../concepts/llm-wiki-risks.md)
