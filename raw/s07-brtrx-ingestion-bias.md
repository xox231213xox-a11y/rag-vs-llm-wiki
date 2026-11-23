---
id: S7
title: "LLM Wiki: A Bias-Aware Stateful Lint"
author: brtrx (GitHub gist)
date: 2026（頁面顯示 last active 2026-06-23）
url: https://gist.github.com/brtrx/ba595fd01e344d797cb66d34d982ecad
type: gist / critique & extension
fetched: 2026-11-23
---

# S7 · brtrx (2026)：Bias-Aware Stateful Lint

> raw 層：取得後不再修改。這裡只存來源資訊與擷取重點（改寫），不轉載原文。

## 擷取重點
- 這篇延伸 Karpathy 的 LLM Wiki，指出一次 ingest 一篇會造成「ingestion bias」：最早進來的來源決定了 wiki 頁面的用詞、框架與範圍，後來的來源只是被調和進這個框架，而不是挑戰它；結果 wiki 反映的是「資料到達的順序」，默默偏向早期來源。
- 作者認為這是知識論（epistemic）層面的問題，不是結構問題，所以不會以斷鏈或缺頁的形式出現。
- Lint 的盲點：Karpathy 的 lint 檢查孤兒頁、斷鏈、矛盾、過時說法，只能處理結構層，無法直接偵測框架偏誤。另一個問題是規模：來源超過 50 篇時，一次 lint 可能塞爆 context window，漏檢卻不會回報。
- 提出的解法（三項）：
  1. 分批：每個 session lint 5 個來源。
  2. 隨機順序：LLM 一次性打亂來源順序（seed 42），存在 wiki/lint-status.md，跨 session 固定；匯集多來源的 hub 頁在所有來源 lint 完前標記為 [~]。
  3. 持久 scratchpad：發現記在 wiki/lint-scratch.md，修好的標 FIXED 而不是刪掉，形成可看出重複模式的變更紀錄。
  - 使用者介面仍然只是「lint the wiki」或「continue lint」，流程寫在 CLAUDE.md；當 lint 不再找到矛盾或缺頁，代表結構層已收斂。
- 沒解決的：lint 無法完全修復 ingest 時就嵌入的框架偏誤，收斂訊號也看不出來。建議補救：定期從 raw/ 用不同順序完整重建、明確請 AI 反駁目前的框架、針對疑似過度依賴早期來源的頁面做重寫。
