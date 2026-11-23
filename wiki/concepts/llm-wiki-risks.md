---
title: "LLM Wiki 的風險與限制"
type: concept
sources: [S1, S6, S7]
updated: 2026-11-23
---

# LLM Wiki 的風險與限制

- 過時：來源更新後要重新 ingest，否則 wiki 一直引用舊版本 [S6]
- 知識漂移（knowledge drift）：每次 ingest 可能帶進小錯，數百次後原本正確的頁面會慢慢變得有點錯 [S6]
- 查證困難：所有說法都是模型寫的，附來源有幫助，但讀者仍得信任摘要 [S6]
- 規模：index 做法適合中等規模；10,000 頁等級的 wiki 還沒被驗證過 [S1][S6]
- Ingestion bias：先進來的來源決定框架，lint 抓不到 [S7]
- 維護成本：lint、矛盾檢查與重新 ingest 都要花時間與運算 [S6]

## 相關頁面

- [Ingestion bias（攝入順序偏誤）](ingestion-bias.md)
- [LLM Wiki](llm-wiki.md)
- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
