# Wiki 操作紀錄（log，只追加）

## [2026-11-23] init | 建立 wiki 與 schema
- 主題：RAG vs LLM Wiki。建立 raw/、wiki/、CLAUDE.md（graph v1）。
- ingest 順序刻意安排：先 RAG 基礎（S5→S2→S3→S4），再 LLM Wiki（S1→S6），最後放批評（S7）。

## [2026-11-23] fetch | S1–S7 來源卡
- N1 取得資料：7 篇來源寫成 raw/s01～s07 來源卡（只存擷取重點，不轉載全文）。

## [2026-11-23] discuss | 第一輪討論（RAG 側：S5、S2、S3、S4）
- S5：Jack 選「四步驟流程、好處、限制」；沒選「Embedding 是什麼」→ embedding 只在流程中帶過，不另開頁。
- S2：四項全選（名稱由來、兩種記憶、想解決的問題、實驗結果）。
- S3：三項全選（LLM 三個問題、三代演進、三個元件）。
- S4：四項全選（切塊丟上下文、解法、數據、小知識庫不用 RAG）。

## [2026-11-23] discuss | 第二輪討論（LLM Wiki 側：S1、S6、S7＋簡報比喻）
- S1：四項全選（核心主張、三層架構、三個操作、index/log）。
- S6：選「對照表、風險、現況」；沒選「何時用哪個」。
- S7：四項全選（ingestion bias、lint 盲點、解法、補救）。
- 簡報比喻：選「圖書館員 vs 百科全書」。

## [2026-11-23] ingest | S5 Wikipedia：Retrieval-augmented generation
- 新增 sources/s05、concepts/rag.md、concepts/llm-limitations.md。

## [2026-11-23] ingest | S2 Lewis et al. 2020
- 新增 sources/s02、concepts/parametric-memory.md；更新 rag.md（名稱由來）、llm-limitations.md。

## [2026-11-23] ingest | S3 Gao et al. 2023
- 新增 sources/s03、concepts/rag-paradigms.md；更新 llm-limitations.md（三個問題）。

## [2026-11-23] ingest | S4 Anthropic Contextual Retrieval
- 新增 sources/s04、concepts/chunking.md、concepts/contextual-retrieval.md；更新 rag.md（chunk、top-K）、rag-paradigms.md。

## [2026-11-23] ingest | S1 Karpathy LLM Wiki
- 新增 sources/s01、concepts/llm-wiki.md、concepts/wiki-operations.md、comparisons/rag-vs-llm-wiki.md；更新 rag.md（限制：知識不累積）。

## [2026-11-23] ingest | S6 DataCamp LLM Wiki
- 新增 sources/s06、concepts/llm-wiki-risks.md；更新 llm-wiki.md（現況）、wiki-operations.md、comparisons/rag-vs-llm-wiki.md（對照表）。

## [2026-11-23] ingest | S7 brtrx Bias-Aware Lint
- 新增 sources/s07、concepts/ingestion-bias.md；更新 wiki-operations.md（lint 盲點）、llm-wiki-risks.md。
- 新增 overview.md 總覽頁、index.md 目錄。

## [2026-11-23] lint | 第一次 lint（N4）
- lint_wiki.py 抓到 4 個錯：都是 L4（後來的來源更新了舊頁面，frontmatter 的 sources 沒同步）。
- 人工語意檢查抓到 2 個：M1 比較頁說得比 S4 多；M2 S5 摘要頁引用了還沒 ingest 的 S2。
- 回 N3 修正後重跑：PASS。紀錄見 runs/01-wiki-lint-v1.txt、runs/02-wiki-lint-v1-rerun.txt。

## [2026-11-23] query | 要教不熟的人「RAG vs LLM Wiki」，需要哪些頁面？
- 讀 index.md → 選 overview、llm-limitations、rag、parametric-memory、chunking、contextual-retrieval、rag-paradigms、llm-wiki、wiki-operations、comparisons/rag-vs-llm-wiki、llm-wiki-risks、ingestion-bias。
- 答案存成 syntheses/slide-outline.md（簡報大綱）。

## [2026-11-23] build | 產生簡報 v1（N6 大綱 → N7 簡報）
- 依 syntheses/slide-outline.md 產生 slides/index.html（17 頁），每頁標 data-wiki 與來源。

## [2026-11-23] check | 檢查簡報 v1（N8）
- check_slides.py：C4 第 6 頁「向量資料庫」在 wiki 找不到。
- 語意檢查：第 6 頁 embedding、向量資料庫的定義與第 11 頁「人與 LLM 分工」不在 wiki → N7 生成時用模型自己的知識補了內容。
- 截圖檢查：腳本第一次給出假 PASS（一直量第 1 頁），修正後重跑；人工看截圖另抓到 3 個版面問題。
- 紀錄：runs/03～06。

## [2026-11-23] discuss | Embedding 要不要補進 wiki？
- Jack 決定：回 wiki 補一句定義（推翻第一輪「不強調 embedding」，只補最基本定義）。

## [2026-11-23] ingest | 從 S5、S4 來源卡補 concepts/embedding.md
- 新增 embedding.md；llm-wiki.md 補「人與 LLM 分工」（S1）。
- 自我對照 raw 時發現多寫了「問題也轉成向量」（S4 卡沒有這句），改成來源原本的說法。
- 立刻跑 lint（v2 規則：每次 ingest 後就 lint）：PASS。

## [2026-11-23] schema | graph v1 → v2
- lint 移到每篇 ingest 後；新增 N6c 大綱檢查與名詞表；N3 對照 raw；N8 新增 C7。詳見 CLAUDE.md 版本歷史。

## [2026-11-23] check | 大綱檢查（N6c，第一次跑）
- 抓到 3 個錯：大綱兩頁的 wiki 路徑寫不完整；chunking.md 沒有「chunk：」定義句。修正後 PASS，才進 N7。

## [2026-11-23] build | 產生簡報 v2＋檢查
- 第 6 頁改引用 embedding.md、chunking.md；第 11 頁對齊 wiki 用字；修 3 個版面問題。
- check_slides.py（C1–C7）PASS、截圖版面 PASS、人工看截圖 OK。紀錄：runs/08～12。

## [2026-11-23] publish | 發布到 GitHub Pages（N9）
- 總覽頁：https://xox231213xox-a11y.github.io/rag-vs-llm-wiki/ ；簡報：/slides/
- 線上確認：鍵盤／按鈕翻頁、#頁碼連結、小測驗、頁尾 Wiki 連結（GitHub 上都存在）、Google 字型、修正前後截圖都正常。
