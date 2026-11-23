# Wiki 目錄（index）

主題：**RAG 與 LLM Wiki — AI 怎麼記住知識？** ｜ 7 個來源 ｜ 維護規則見 [CLAUDE.md](../CLAUDE.md) ｜ 操作紀錄見 [log.md](log.md)

## 總覽

- [總覽：AI 怎麼記住知識？](overview.md) — 整個主題的一頁摘要，從這裡開始讀

## 概念（concepts）

- [LLM 的先天限制](concepts/llm-limitations.md) — 幻覺、知識過時、難以追溯：為什麼需要外部知識
- [RAG（檢索增強生成）](concepts/rag.md) — 定義、四步驟流程、好處與限制
- [Embedding 與向量資料庫](concepts/embedding.md) — 簡報檢查後補的最基本定義（S5、S4）
- [參數記憶 vs 非參數記憶](concepts/parametric-memory.md) — RAG 原始論文的核心想法
- [RAG 的三代演進與三個元件](concepts/rag-paradigms.md) — Naive / Advanced / Modular；檢索、增強、生成
- [切塊（Chunking）與上下文遺失](concepts/chunking.md) — 「營收成長 3%」的例子
- [Contextual Retrieval](concepts/contextual-retrieval.md) — 替 chunk 補脈絡，失敗率 5.7% → 1.9%
- [LLM Wiki](concepts/llm-wiki.md) — 核心主張、三層架構、現況
- [LLM Wiki 的三個操作](concepts/wiki-operations.md) — Ingest、Query、Lint；index.md 與 log.md
- [LLM Wiki 的風險與限制](concepts/llm-wiki-risks.md) — 過時、知識漂移、查證、規模
- [Ingestion bias（攝入順序偏誤）](concepts/ingestion-bias.md) — 先進來的來源決定框架

## 比較（comparisons）

- [RAG vs LLM Wiki](comparisons/rag-vs-llm-wiki.md) — 六個面向的對照表與兩者關係

## 來源摘要（sources）— 依 ingest 順序

- [S5 · Wikipedia：RAG 條目](sources/s05-wikipedia-rag.md) — RAG 定義、四步驟、好處與限制
- [S2 · Lewis et al. (2020)](sources/s02-lewis-2020-rag.md) — RAG 原始論文：兩種記憶
- [S3 · Gao et al. (2023)](sources/s03-gao-2023-rag-survey.md) — RAG 綜述：三個問題、三代、三元件
- [S4 · Anthropic (2024)](sources/s04-anthropic-contextual-retrieval.md) — Contextual Retrieval 與數據
- [S1 · Karpathy (2026)](sources/s01-karpathy-llm-wiki.md) — LLM Wiki 原始 idea file
- [S6 · DataCamp (2026)](sources/s06-datacamp-llm-wiki.md) — RAG vs LLM Wiki 對照、風險、現況
- [S7 · brtrx (2026)](sources/s07-brtrx-ingestion-bias.md) — 對 LLM Wiki 的批評：ingestion bias

## 綜合（syntheses）

- [簡報大綱：RAG 與 LLM Wiki 入門](syntheses/slide-outline.md) — 查詢結果：教學目標、全篇比喻、17 頁逐頁大綱
