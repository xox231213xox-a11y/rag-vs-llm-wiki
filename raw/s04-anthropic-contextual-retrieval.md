---
id: S4
title: "Introducing Contextual Retrieval"
author: Anthropic
date: 2024-09-19
url: https://www.anthropic.com/news/contextual-retrieval
type: engineering blog
fetched: 2026-11-23
---

# S4 · Anthropic (2024)：Contextual Retrieval

> raw 層：取得後不再修改。這裡只存來源資訊與擷取重點（改寫），不轉載原文。

## 擷取重點
- 基本 RAG 流程：把文件切成 chunk（通常幾百個 token）→ 用 embedding 模型轉成向量 → 存進向量資料庫做語意搜尋 → 問問題時把最相關的 chunk 加進 prompt。也可以加上 BM25（字詞比對，適合錯誤代碼這類精確詞），用 rank fusion 合併兩種結果，取前 K 個 chunk。
- 傳統 RAG 的問題：切塊會把上下文切掉，單獨一個 chunk 可能檢索不到或看不懂。文章的例子：問「ACME 公司 2023 Q2 營收成長多少」，相關 chunk 只寫「公司營收比上一季成長 3%」，沒寫是哪家公司、哪一季。
- 方法：Contextual Retrieval——在做 embedding（Contextual Embeddings）與建立 BM25 索引（Contextual BM25）之前，先在每個 chunk 前面加上一段說明它在整份文件中脈絡的文字；這段說明由 Claude 讀整份文件後產生，通常每個 chunk 50–100 個 token，用 prompt caching 避免每個 chunk 都重送整份文件。
- 效果（以 top-20 chunk 檢索失敗率衡量，基準 5.7%）：
  - 只用 Contextual Embeddings：失敗率降 35%（5.7% → 3.7%）
  - Contextual Embeddings + Contextual BM25：降 49%（5.7% → 2.9%）
  - 再加上 reranking：降 67%（5.7% → 1.9%）
- 評估指標：1 − recall@20，也就是相關文件沒有出現在前 20 個 chunk 裡的比例。
- 什麼時候不需要 RAG：知識庫小於 200,000 個 token（約 500 頁）時，可以直接把整個知識庫放進 prompt；搭配 prompt caching，延遲可降低超過 2 倍、成本最多降 90%。
