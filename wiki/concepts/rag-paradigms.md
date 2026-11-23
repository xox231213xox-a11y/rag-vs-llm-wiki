---
title: "RAG 的三代演進與三個元件"
type: concept
sources: [S3, S4]
updated: 2026-11-23
---

# RAG 的三代演進與三個元件

## 三代演進

- Naive RAG → Advanced RAG → Modular RAG [S3]
- 改良的方向之一是讓「檢索」更準，例如替 chunk 補脈絡、混合 BM25、加 reranking [S4]

## 三個元件

- 檢索（retrieval）：從外部知識找出相關內容 [S3]
- 增強（augmentation）：把找到的內容組進給模型的輸入 [S3]
- 生成（generation）：模型根據增強後的輸入產生回答 [S3]

## 相關頁面

- [RAG（檢索增強生成）](rag.md)
- [Contextual Retrieval](contextual-retrieval.md)
