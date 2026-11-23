---
title: "參數記憶 vs 非參數記憶"
type: concept
sources: [S2, S5]
updated: 2026-11-23
---

# 參數記憶 vs 非參數記憶

- 參數記憶（parametric memory）：知識在訓練時被「壓」進模型的參數裡，例如預訓練的 seq2seq 模型 [S2]
- 非參數記憶（non-parametric memory）：知識放在模型外面，例如 Wikipedia 的稠密向量索引，用檢索器去查 [S2]
- RAG 的原始論文就是把這兩種記憶接在一起 [S2]
- 非參數記憶的好處是可以直接改資料來更新知識，也能指出答案來自哪段文字 [S2][S5]

## 相關頁面

- [RAG（檢索增強生成）](rag.md)
- [LLM 的先天限制](llm-limitations.md)
