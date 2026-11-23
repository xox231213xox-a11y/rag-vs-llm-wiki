---
title: "S2 · Lewis et al. (2020)：RAG 原始論文"
type: source
sources: [S2]
updated: 2026-11-23
---

# S2 · Lewis et al. (2020)：RAG 原始論文

原始來源卡：[raw/s02-lewis-2020-rag.md](../../raw/s02-lewis-2020-rag.md) · 原文：<https://arxiv.org/abs/2005.11401>

## 討論結果（N2）

- 強調：名稱由來、兩種記憶、想解決的問題、實驗結果（四項全選） [討論]

## 重點摘要

- RAG 這個名稱由這篇 2020 年的論文提出，發表於 NeurIPS 2020 [S2]
- 想解決的問題：模型把知識存在參數裡，難以精確存取、難以更新，也無法說明答案的出處 [S2]
- 做法：把「參數記憶」（預訓練 seq2seq 模型）和「非參數記憶」（Wikipedia 的稠密向量索引＋神經檢索器）接在一起 [S2]
- 結果：在三個開放領域問答任務達到當時最佳，生成的文字比純參數模型更具體、更多樣、更符合事實 [S2]

## 相關頁面

- [RAG（檢索增強生成）](../concepts/rag.md)
- [參數記憶 vs 非參數記憶](../concepts/parametric-memory.md)
- [LLM 的先天限制](../concepts/llm-limitations.md)
