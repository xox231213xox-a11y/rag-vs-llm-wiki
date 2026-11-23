---
id: S3
title: "Retrieval-Augmented Generation for Large Language Models: A Survey"
author: Yunfan Gao, Yun Xiong, Xinyu Gao, et al. (Tongji University / Fudan University)
date: 2023-12-18 (arXiv v1)；v5 2024-03-27
url: https://arxiv.org/abs/2312.10997
type: survey paper
fetched: 2026-11-23
---

# S3 · Gao et al. (2023)：RAG 綜述論文

> raw 層：取得後不再修改。這裡只存來源資訊與擷取重點（改寫），不轉載原文。

## 擷取重點
- LLM 面臨的問題：幻覺（hallucination）、知識過時（outdated knowledge）、推理過程不透明且難以追溯。
- RAG 的定位：從外部資料庫引入知識，提升生成的準確度與可信度，特別是知識密集型任務；也讓知識可以持續更新、加入特定領域資訊。原文說 RAG 是 "a promising solution"。
- 三代演進（paradigms）：Naive RAG → Advanced RAG → Modular RAG。
- 三個核心元件：檢索（retrieval）、生成（generation）、增強（augmentation），論文逐一回顧各元件的技術。
- 另外提出評估框架與 benchmark，並整理目前的挑戰與未來方向。
