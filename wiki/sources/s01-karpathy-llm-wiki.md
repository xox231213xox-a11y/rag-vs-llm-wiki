---
title: "S1 · Karpathy (2026)：LLM Wiki"
type: source
sources: [S1]
updated: 2026-11-23
---

# S1 · Karpathy (2026)：LLM Wiki

原始來源卡：[raw/s01-karpathy-llm-wiki.md](../../raw/s01-karpathy-llm-wiki.md) · 原文：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## 討論結果（N2）

- 強調：核心主張、三層架構、三個操作、index.md 與 log.md（四項全選） [討論]

## 重點摘要

- 核心主張：RAG 每次被問都要從原始文件重新找知識，問過的東西不會累積；LLM Wiki 則把知識編譯一次、之後持續更新 [S1]
- 三層架構：raw（不可改的原始資料）、wiki（LLM 維護的 markdown）、schema（CLAUDE.md / AGENTS.md 定義的規則） [S1]
- 三個操作：Ingest（讀來源、先討論重點、再寫頁面）、Query（查 wiki 回答，好答案存回 wiki）、Lint（定期健康檢查） [S1]
- index.md 是目錄、log.md 是只追加的時間紀錄；約 100 個來源以內，不需要向量資料庫 [S1]
- 這份 gist 發表於 2026 年 4 月，作者強調它是「想法」而不是實作 [S1]

## 相關頁面

- [LLM Wiki](../concepts/llm-wiki.md)
- [LLM Wiki 的三個操作](../concepts/wiki-operations.md)
- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
