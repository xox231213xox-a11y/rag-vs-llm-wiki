---
title: "Ingestion bias（攝入順序偏誤）"
type: concept
sources: [S7]
updated: 2026-11-23
---

# Ingestion bias（攝入順序偏誤）

- 定義：一次 ingest 一篇時，最早的來源決定了 wiki 的用詞、框架與範圍，後來的來源只被調和進去，而不是挑戰它 [S7]
- 結果：wiki 反映的是資料到達的順序，默默偏向早期來源 [S7]
- 這是知識層面的問題，不會以斷鏈或缺頁的形式出現，所以一般 lint 抓不到 [S7]

## 解法與補救

- 分批 lint（每次 5 個來源）、固定的隨機順序、用 scratchpad 記錄發現 [S7]
- 換順序從 raw 完整重建、請 AI 反駁目前的框架、重寫疑似偏向早期來源的頁面 [S7]

## 本 wiki 的對應做法

- 本 wiki 的 ingest 順序是：S5 → S2 → S3 → S4 → S1 → S6 → S7（先 RAG 基礎、再 LLM Wiki、最後批評） [討論]

## 相關頁面

- [LLM Wiki 的風險與限制](llm-wiki-risks.md)
- [LLM Wiki 的三個操作](wiki-operations.md)
