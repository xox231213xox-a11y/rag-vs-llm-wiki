---
title: "總覽：AI 怎麼記住知識？"
type: overview
sources: [S1, S2, S3, S4, S5, S6, S7]
updated: 2026-11-23
---

# 總覽：AI 怎麼記住知識？

- LLM 只會訓練時學到的東西，且會幻覺、知識過時、難以追溯 [S3]
- 解法一 RAG（2020）：回答前先去外部資料找相關段落，再根據段落回答 [S2][S5]
- RAG 的弱點之一是切塊會丟失上下文；Contextual Retrieval 可把檢索失敗率從 5.7% 降到 1.9% [S4]
- 解法二 LLM Wiki（2026）：資料進來時就讓 LLM 整理成互相連結的 wiki，知識會累積 [S1][S6]
- LLM Wiki 的代價：要維護、會過時、錯誤可能累積、ingest 順序會造成偏誤 [S6][S7]
- 兩者互補，不是誰取代誰 [S6]
- 教學比喻：RAG 像每次都請圖書館員去書庫找書；LLM Wiki 像平時就編好一套百科全書 [比喻]

## 相關頁面

- [RAG（檢索增強生成）](concepts/rag.md)
- [LLM Wiki](concepts/llm-wiki.md)
- [RAG vs LLM Wiki](comparisons/rag-vs-llm-wiki.md)
