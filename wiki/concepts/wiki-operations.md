---
title: "LLM Wiki 的三個操作"
type: concept
sources: [S1, S6, S7]
updated: 2026-11-23
---

# LLM Wiki 的三個操作：Ingest、Query、Lint

## Ingest（攝入）

- 放入新來源 → LLM 閱讀 → 先跟人討論重點 → 寫摘要頁 → 更新相關概念頁 → 更新 index → 在 log 追加一筆 [S1]
- 一個來源可能動到 10–15 頁 [S1][S6]
- Karpathy 偏好一次 ingest 一篇並親自參與 [S1]

## Query（查詢）

- LLM 先讀 index，再讀相關頁面，附引用回答 [S1]
- 產出可以是頁面、表格、投影片；好的答案存回 wiki，讓探索也能累積 [S1]

## Lint（健康檢查）

- 定期檢查矛盾、過時說法、孤兒頁、缺少的連結或概念頁 [S1][S6]
- 盲點：lint 只抓得到結構問題，抓不到 ingest 順序造成的框架偏誤 [S7]

## 兩個特殊檔案

- index.md：每頁一行連結＋一句摘要的目錄，查詢時先讀它 [S1]
- log.md：依時間只追加的紀錄，用固定前綴方便 grep [S1]
- 約 100 個來源、數百頁以內，靠 index 就夠，不需要向量資料庫 [S1]

## 相關頁面

- [LLM Wiki](llm-wiki.md)
- [Ingestion bias（攝入順序偏誤）](ingestion-bias.md)
