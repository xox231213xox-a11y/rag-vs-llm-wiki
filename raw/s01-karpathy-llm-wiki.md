---
id: S1
title: "LLM Wiki (idea file)"
author: Andrej Karpathy
date: 2026-04-04
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
type: gist / idea file
fetched: 2026-11-23
---

# S1 · Karpathy：LLM Wiki（idea file）

> raw 層：取得後不再修改。這裡只存來源資訊與擷取重點（改寫），不轉載原文。

## 擷取重點
- 多數 LLM 文件工具在「問問題當下」才去檢索相關片段再生成答案；作者認為這樣 LLM 每次都在「從零重新發現知識」，問過的東西不會累積。
- 提出的做法：LLM 逐步建立並維護一個持久的、互相連結的 markdown wiki；知識「編譯一次、之後持續更新」，而不是每次問都重新推導。原文稱 wiki 是 "a persistent, compounding artifact"。
- 三層架構：
  - Raw sources：不可變的原始資料（文章、論文、圖片、資料），LLM 只讀不改。
  - The wiki：LLM 產生的 markdown（摘要頁、實體頁、概念頁、比較頁、總覽），由 LLM 擁有並維護，人負責閱讀。
  - The schema：設定文件（如 CLAUDE.md 或 AGENTS.md），定義 wiki 結構、慣例與工作流程，人與 LLM 一起逐步修訂。
- 三個操作：
  - Ingest：放入新來源 → LLM 閱讀 → 與使用者討論重點 → 寫摘要頁 → 更新 index → 更新相關概念/實體頁 → 在 log 追加一筆。一個來源可能動到 10–15 頁。作者偏好一次 ingest 一篇並親自參與，但也可以批次。
  - Query：LLM 搜尋 wiki、讀相關頁面、附引用回答；產出可以是頁面、表格、投影片或圖表；好的答案可以存回 wiki，讓探索也能累積。
  - Lint：定期健康檢查：矛盾、過時說法、孤兒頁、缺少的交叉連結或概念頁、可用網路搜尋補的資料缺口。
- 兩個特殊檔案：
  - index.md：內容導向的目錄，每頁一行連結＋一句摘要，依類別分；回答問題時 LLM 先讀它。作者說在中等規模（約 100 個來源、數百頁）下，不需要 embedding 基礎設施也能運作。
  - log.md：依時間、只追加的紀錄（ingest、query、lint），用一致前綴如 `## [2026-04-02] ingest | Article Title`，方便用 grep 查。
- 工具：Obsidian（瀏覽與 graph view、Web Clipper、Marp 投影片、Dataview）、qmd（本地 markdown 搜尋，BM25＋向量混合）、Git（wiki 就是一個 markdown 的 git repo）、各種 coding agent（Claude Code、Codex 等）。
- 比喻：Obsidian 是 IDE、LLM 是工程師、wiki 是程式碼庫；也提到 Vannevar Bush 1945 年的 Memex——當年缺的是「誰來維護」，現在由 LLM 負責。
- 核心理由：人類放棄 wiki 是因為維護成本比價值長得快；LLM 不會厭倦記帳式工作，維護成本接近零。人負責挑來源、問問題，其餘交給 LLM。
- 作者自己的但書：文件刻意寫得抽象，是一個想法而非實作；index 做法適用中等規模；所有元件都是可選、模組化的。
