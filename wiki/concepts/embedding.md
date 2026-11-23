---
title: "Embedding 與向量資料庫"
type: concept
sources: [S4, S5]
updated: 2026-11-23
---

# Embedding 與向量資料庫

這頁是簡報檢查後補的（見 log.md）：當初討論決定「不強調 embedding」，但教 RAG 四步驟時初學者一定會碰到這個詞，所以只補最基本的定義。

## 定義

- embedding：把文字轉成一串數字（向量），意思相近的文字，數字也相近 [S5]
- 向量資料庫：存放 embedding 的資料庫，能快速找出與問題「意思最接近」的內容 [S5]

## 在 RAG 裡的位置

- 索引階段：文件切成 chunk → 用 embedding 模型轉成向量 → 存進向量資料庫 [S4]
- 檢索階段：問問題時用語意搜尋，找出最相關的前 K 個 chunk 加進 prompt [S4]

## 相關頁面

- [RAG（檢索增強生成）](rag.md)
- [切塊（Chunking）與上下文遺失](chunking.md)
