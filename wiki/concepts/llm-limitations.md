---
title: "LLM 的先天限制"
type: concept
sources: [S1, S2, S3, S5]
updated: 2026-11-23
---

# LLM 的先天限制（為什麼需要外部知識）

- 幻覺（hallucination）：模型會自信地說出錯誤的內容 [S3][S5]
- 知識過時：模型只知道訓練時看過的資料 [S3]
- 推理不透明：很難追溯答案是怎麼來的 [S3]
- 知識存在參數裡，難以精確存取、難以更新，也說不出答案的出處 [S2]
- RAG 與 LLM Wiki 都是「把知識放在模型外面」來處理這些問題的方法 [S3][S1]

## 相關頁面

- [RAG（檢索增強生成）](rag.md)
- [參數記憶 vs 非參數記憶](parametric-memory.md)
- [LLM Wiki](llm-wiki.md)
