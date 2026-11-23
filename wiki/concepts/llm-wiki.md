---
title: "LLM Wiki"
type: concept
sources: [S1, S6]
updated: 2026-11-23
---

# LLM Wiki

## 核心主張

- RAG 每次被問都從原始文件重新找，知識不會累積 [S1]
- LLM Wiki 讓 LLM 持續維護一個互相連結的 markdown wiki，知識「編譯一次、之後持續更新」 [S1]
- 關鍵轉變是把「檢索」和「編譯」分開：讀來源的工作在 ingest 時就做完 [S6]
- 為什麼現在可行：人類放棄維護 wiki 是因為太累，LLM 不怕做整理工作 [S1]

## 三層架構

- Raw：原始資料，LLM 只讀不改 [S1]
- Wiki：LLM 寫的摘要頁、概念頁、比較頁，由 LLM 維護 [S1]
- Schema：CLAUDE.md / AGENTS.md，寫下結構與工作流程，人和 LLM 一起修 [S1]
- 分工：人負責挑來源、問問題；其餘的閱讀、撰寫、整理交給 LLM [S1]

## 現況

- Karpathy 在 2026 年 4 月以 gist 提出，作者強調這是想法而非實作 [S1]
- 截至 2026 年 7 月，多數實作仍是原型 [S6]

## 相關頁面

- [LLM Wiki 的三個操作](wiki-operations.md)
- [LLM Wiki 的風險與限制](llm-wiki-risks.md)
- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
