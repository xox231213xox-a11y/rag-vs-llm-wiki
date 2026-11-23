---
title: "S5 · Wikipedia：Retrieval-augmented generation"
type: source
sources: [S5]
updated: 2026-11-23
---

# S5 · Wikipedia：RAG 條目

原始來源卡：[raw/s05-wikipedia-rag.md](../../raw/s05-wikipedia-rag.md) · 原文：<https://en.wikipedia.org/wiki/Retrieval-augmented_generation>

## 討論結果（N2）

- 強調：四步驟流程、好處、限制 [討論]
- 不強調：Embedding 的細部定義，只在流程第一步帶過 [討論]

## 重點摘要

- RAG 讓 LLM 在回答前先從外部資料取回資訊，用上訓練資料裡沒有的、較新或特定領域的知識 [S5]
- 流程分四步：索引（indexing）→ 檢索（retrieval）→ 增強（augmentation）→ 生成（generation） [S5]
- 好處：減少幻覺、不必重新訓練模型就能加入新知識、回答可以附來源讓人查證 [S5]
- 限制：RAG 不能防止幻覺；資訊不夠時模型仍可能硬答；可能誤讀被抽離上下文的句子；來源矛盾時可能混出誤導的答案 [S5]
- RAG 這個名詞出自 2020 年第一作者為 Patrick Lewis 的論文 [S5]

## 相關頁面

- [RAG（檢索增強生成）](../concepts/rag.md)
- [LLM 的先天限制](../concepts/llm-limitations.md)
