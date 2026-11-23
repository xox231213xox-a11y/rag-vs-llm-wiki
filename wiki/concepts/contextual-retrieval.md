---
title: "Contextual Retrieval"
type: concept
sources: [S4]
updated: 2026-11-23
---

# Contextual Retrieval（脈絡化檢索）

- 做法：讓 Claude 讀整份文件，替每個 chunk 寫 50–100 個 token 的脈絡說明，貼在 chunk 前面後再做 embedding 與 BM25 索引 [S4]
- 衡量方式：相關內容沒有出現在前 20 個 chunk 的比例（檢索失敗率） [S4]

## 數據（基準失敗率 5.7%）

- 只加脈絡 embedding：5.7% → 3.7%，降 35% [S4]
- 再加脈絡 BM25：5.7% → 2.9%，降 49% [S4]
- 再加 reranking：5.7% → 1.9%，降 67% [S4]

## 什麼時候乾脆不用 RAG

- 知識庫小於 200,000 個 token（約 500 頁）時，直接整份放進 prompt 即可 [S4]
- 搭配 prompt caching，延遲可降超過 2 倍、成本最多降 90% [S4]

## 相關頁面

- [切塊（Chunking）與上下文遺失](chunking.md)
- [RAG 的三代演進與三個元件](rag-paradigms.md)
