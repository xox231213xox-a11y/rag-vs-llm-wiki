---
id: S6
title: "LLM Wiki: Understanding the New AI Knowledge Architecture"
author: Dario Radečić (DataCamp)
date: 2026-07-17
url: https://www.datacamp.com/blog/llm-wiki
type: blog / explainer
fetched: 2026-11-23
---

# S6 · DataCamp (2026)：LLM Wiki 架構解析

> raw 層：取得後不再修改。這裡只存來源資訊與擷取重點（改寫），不轉載原文。

## 擷取重點
- 核心：LLM Wiki 在 ingest 時就把來源「編譯」成持久、互相連結的知識庫；之後查詢時讀這個編譯好的知識庫，而不是每次重新檢索原始 chunk。知識隨著加入來源而累積。
- 起源：2026 年由 Karpathy 以 GitHub gist 提出，之後有開源專案把它做成可執行的版本。關鍵轉變是把「檢索（retrieval）」和「編譯（compilation）」分開。
- 與 RAG 的對照（文章表格，改寫）：
  - 工作發生時間：RAG 在查詢時；LLM Wiki 在 ingest 時。
  - 留下什麼：RAG 查詢之間什麼都不留（上下文用完即丟）；LLM Wiki 留下編譯好的 markdown 頁面。
  - 新鮮度：RAG 直接讀即時來源，變更立刻生效；LLM Wiki 要重新 ingest，會落後原始來源。
  - 跨來源綜合：RAG 可能漏掉超出 context 的跨 chunk 關聯；LLM Wiki 的綜合做一次並經過審視。
  - 維護：RAG 建好索引後幾乎不用維護；LLM Wiki 需要 lint、矛盾檢查、刪減頁面。
  - 擴展性：RAG 是可預期的搜尋問題；LLM Wiki 取決於能否保持知識一致，大型 wiki 需要索引檔、搜尋或 embedding。
  - 兩者互補：有些實作在 wiki 長大後，再對 wiki 跑 RAG。
- 架構三段：來源文件（不可變儲存，留稽核軌跡）→ 知識編譯（萃取概念、更新/新增頁面、加交叉連結；一個來源可能更新 10–15 頁）→ AI 應用（聊天、研究助理、agent，可透過 MCP 串接）。
- 建置迴圈五步：ingest 進 raw → 辨識實體與概念並檢查 wiki 已有什麼 → 產生或更新頁面（矛盾標記在頁面上而非直接覆寫）→ 維護雙向連結 → 定期 lint（矛盾、過時、孤兒頁、缺概念頁）。
- 現況：截至 2026 年 7 月，這些實作都還沒完成，多數是原型。
- 何時用哪個（文章隱含）：長期研究、跨 session 的 agent 記憶、需要跨多來源綜合 → LLM Wiki；來源變動快、需要即時新鮮度、不需綜合 → RAG；很多系統兩者並用。
- 限制與風險：
  - 過時：來源改了就要重新 ingest，否則一直引用舊版本。
  - 錯誤傳播與知識漂移（knowledge drift）：每次 ingest 都可能帶進小錯，經過數百次 ingest 會累積，原本正確的頁面可能慢慢變得有點錯。
  - 查證：每個說法都是模型寫的，附來源有幫助，但讀者還是得信任摘要。
  - 維護與成本：矛盾檢查與重新 ingest 需要時間和運算（文章未量化）。
  - 規模：超過一定大小需要索引、搜尋或 embedding 層；10,000 頁的 wiki 尚未被驗證過。
  - 驗證：在大規模下抓出模型錯誤是未解問題，人工審查難以擴展。
- 常見誤解：它不會取代 RAG；它不只是向量資料庫（它產生新的綜合頁面）；它仍然需要維護。
