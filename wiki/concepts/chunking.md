---
title: "切塊（Chunking）與上下文遺失"
type: concept
sources: [S4, S5]
updated: 2026-11-23
---

# 切塊（Chunking）與上下文遺失

- chunk：長文件切成的小段，通常幾百個 token；RAG 以 chunk 為單位建立索引與檢索 [S4]
- 問題：切開後，一個 chunk 可能缺少關鍵脈絡，導致檢索不到或看不懂 [S4]
- 例子：問「ACME 公司 2023 Q2 營收成長多少」，相關 chunk 只寫「公司營收比上一季成長 3%」，看不出公司與時間 [S4]
- 這也呼應 RAG 的一般限制：句子被抽離上下文時容易被誤讀 [S5]

## 相關頁面

- [Contextual Retrieval](contextual-retrieval.md)
- [RAG（檢索增強生成）](rag.md)
