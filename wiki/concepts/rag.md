---
title: "RAG（檢索增強生成）"
type: concept
sources: [S1, S2, S4, S5]
updated: 2026-11-23
---

# RAG（Retrieval-Augmented Generation，檢索增強生成）

## 定義

- RAG 讓 LLM 回答前先從外部資料取回相關資訊，再根據這些資訊回答，因此能用上訓練資料裡沒有的知識 [S5]
- 名稱出自 Lewis 等人 2020 年的論文（NeurIPS 2020） [S2][S5]

## 四步驟流程

- ① 索引（indexing）：事先把資料轉成 embedding，存進可以依意思搜尋的資料庫 [S5]
- ② 檢索（retrieval）：使用者發問時，檢索器找出最相關的文件 [S5]
- ③ 增強（augmentation）：把找到的內容加進問題，給模型當上下文 [S5]
- ④ 生成（generation）：LLM 依問題與找到的內容寫出回答 [S5]
- 實務上文件會先切成幾百個 token 的 chunk，查詢時把最相關的前 K 個 chunk 加進 prompt [S4]

## 好處

- 減少幻覺 [S5]
- 加入新知識不必重新訓練模型 [S5]
- 回答可以附上來源，方便查證 [S5]

## 限制

- RAG 不能防止幻覺 [S5]
- 資訊不足時模型可能還是硬答，而不承認不知道 [S5]
- 可能誤讀被抽離上下文的句子；來源矛盾時可能混出錯誤答案 [S5]
- 每次查詢都重新檢索，問過的東西不會累積（LLM Wiki 提出者的批評） [S1]

## 相關頁面

- [Embedding 與向量資料庫](embedding.md)
- [LLM 的先天限制](llm-limitations.md)
- [參數記憶 vs 非參數記憶](parametric-memory.md)
- [RAG 的三代演進與三個元件](rag-paradigms.md)
- [切塊（Chunking）與上下文遺失](chunking.md)
- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
