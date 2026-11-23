---
title: "S4 · Anthropic (2024)：Contextual Retrieval"
type: source
sources: [S4]
updated: 2026-11-23
---

# S4 · Anthropic (2024)：Contextual Retrieval

原始來源卡：[raw/s04-anthropic-contextual-retrieval.md](../../raw/s04-anthropic-contextual-retrieval.md) · 原文：<https://www.anthropic.com/news/contextual-retrieval>

## 討論結果（N2）

- 強調：切塊會丟上下文、解法、數據、小知識庫不用 RAG（四項全選） [討論]

## 重點摘要

- 傳統 RAG 會把文件切成幾百個 token 的 chunk，切開後一個 chunk 可能失去上下文 [S4]
- 例子：「公司營收比上一季成長 3%」這個 chunk 看不出是哪家公司、哪一季 [S4]
- 解法：先讓 Claude 讀整份文件，替每個 chunk 補上 50–100 個 token 的脈絡說明，再做 embedding 和 BM25 索引 [S4]
- 效果：前 20 個 chunk 的檢索失敗率從 5.7% 降到 1.9%（加上 reranking，降 67%） [S4]
- 知識庫小於 200,000 個 token（約 500 頁）時，可以直接整份放進 prompt，不必做 RAG [S4]

## 相關頁面

- [切塊（Chunking）與上下文遺失](../concepts/chunking.md)
- [Contextual Retrieval](../concepts/contextual-retrieval.md)
