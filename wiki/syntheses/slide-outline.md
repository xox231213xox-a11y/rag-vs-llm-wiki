---
title: "簡報大綱：AI 怎麼記住知識？RAG 與 LLM Wiki 入門"
type: synthesis
sources: [S1, S2, S3, S4, S5, S6, S7]
updated: 2026-11-23
---

# 簡報大綱：AI 怎麼記住知識？RAG 與 LLM Wiki 入門

對象：沒學過 RAG 的人。目標長度：約 15 分鐘、17 頁。
這頁是 query「要教不熟的人 RAG vs LLM Wiki 需要哪些頁面？」的答案，存回 wiki 供簡報使用。

## 學習目標

- 說得出 LLM 為什麼需要外部知識 [S3]
- 能解釋 RAG 的四個步驟 [S5]
- 說得出 LLM Wiki 和 RAG 差在哪、各自的風險 [S6]

## 全篇比喻：圖書館員 vs 百科全書

- RAG 像圖書館員：你每問一次，他就跑去書庫翻原書，找到相關段落再回答你 [比喻]
- LLM Wiki 像百科全書：編輯平時就把書讀完、整理成互相連結的條目；你來問時直接翻條目 [比喻]
- 書庫裡的原書＝raw；百科條目＝wiki；編輯手冊＝schema [比喻]

## 要定義的名詞（glossary）

簡報上用 `<dfn>` 定義的名詞只能來自這張表；每個名詞都要指到有定義句的 wiki 頁面。

- chunk：長文件切成幾百個 token 的小段 → concepts/chunking.md [S4]
- embedding：把文字轉成一串數字，意思相近的文字數字也相近 → concepts/embedding.md [S5]
- 向量資料庫：存放 embedding、能依意思找最接近內容的資料庫 → concepts/embedding.md [S5]

## 逐頁大綱

1. 封面 — overview.md、index.md
2. 學習目標 — 本頁
3. LLM 的毛病：幻覺、知識過時、難追溯、知識存在參數裡難更新 — concepts/llm-limitations.md
4. 比喻：圖書館員 vs 百科全書 — 本頁
5. RAG 是什麼：定義、2020 年論文、參數記憶＋非參數記憶 — concepts/rag.md、concepts/parametric-memory.md
6. RAG 四步驟：索引 → 檢索 → 增強 → 生成；chunk 與 top-K — concepts/rag.md、concepts/embedding.md
7. RAG 的好處與限制 — concepts/rag.md
8. 盲點：切塊丟失上下文（營收成長 3% 的例子） — concepts/chunking.md
9. 改良：Contextual Retrieval（5.7% → 1.9%）、RAG 三代演進、小知識庫不用 RAG — concepts/contextual-retrieval.md、concepts/rag-paradigms.md
10. LLM Wiki：換個思路，知識會累積 — concepts/llm-wiki.md
11. 三層架構：raw / wiki / schema — concepts/llm-wiki.md
12. 三個操作：Ingest / Query / Lint＋index、log — concepts/wiki-operations.md
13. 對照表：RAG vs LLM Wiki — comparisons/rag-vs-llm-wiki.md
14. LLM Wiki 的風險：過時、知識漂移、ingestion bias — concepts/llm-wiki-risks.md、concepts/ingestion-bias.md
15. 實例：這份簡報本身就是 LLM Wiki 做的 — index.md、log.md
16. 小測驗（3 題） — concepts/rag.md、comparisons/rag-vs-llm-wiki.md、concepts/ingestion-bias.md
17. 重點回顧＋延伸閱讀 — overview.md

## 相關頁面

- [總覽](../overview.md)
- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
