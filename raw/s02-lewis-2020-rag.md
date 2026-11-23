---
id: S2
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
author: Patrick Lewis, Ethan Perez, Aleksandra Piktus, et al. (Facebook AI Research / UCL / NYU)
date: 2020-05-22 (arXiv v1)；NeurIPS 2020
url: https://arxiv.org/abs/2005.11401
type: paper
fetched: 2026-11-23
---

# S2 · Lewis et al. (2020)：RAG 原始論文

> raw 層：取得後不再修改。這裡只存來源資訊與擷取重點（改寫），不轉載原文。

## 擷取重點
- 問題：大型預訓練語言模型把事實知識存在參數裡，但很難精確地存取與操作這些知識，所以在知識密集型任務上輸給專門設計的架構。摘要點名兩個尚未解決的問題：為決策提供出處（provenance），以及更新模型的世界知識。
- 方法：RAG 模型結合兩種記憶——
  - 參數記憶（parametric memory）：一個預訓練的 seq2seq 模型。
  - 非參數記憶（non-parametric memory）：Wikipedia 的稠密向量索引（dense vector index），透過預訓練的神經檢索器存取。
- 比較兩種做法：整段輸出都用同一組檢索到的段落，或每個 token 可以用不同段落。
- 結果：在三個開放領域問答（open-domain QA）任務達到當時最佳（state-of-the-art），勝過只用參數的 seq2seq 模型與 retrieve-and-extract 架構；在語言生成任務上，產出的文字比純參數模型「更具體、更多樣、更符合事實」。
- 名稱：RAG（Retrieval-Augmented Generation）這個詞由這篇論文提出（見 S5 的歷史段落）。
