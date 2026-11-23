# RAG vs LLM Wiki — 用 LLM Wiki 做教學 HTML 簡報

北科 115378024 工管碩一 連顥哲｜生成式 AI 課程作業（2026/11/23）

- 🌐 作業總覽（含 graph、執行紀錄）：https://xox231213xox-a11y.github.io/rag-vs-llm-wiki/
- ▶ 教學 HTML 簡報：https://xox231213xox-a11y.github.io/rag-vs-llm-wiki/slides/
- 📚 LLM Wiki 目錄：[wiki/index.md](wiki/index.md)　｜　操作紀錄：[wiki/log.md](wiki/log.md)

## 結構（Karpathy LLM Wiki 三層）

| 資料夾／檔案 | 用途 |
|---|---|
| `raw/` | 7 篇來源的來源卡（出處＋擷取重點，不轉載原文），取得後不改 |
| `wiki/` | LLM 維護的知識：`sources/` 來源摘要、`concepts/` 概念、`comparisons/` 比較、`syntheses/` 查詢結果（簡報大綱）、`index.md`、`log.md` |
| `CLAUDE.md` / `AGENTS.md` | Schema：Wiki 規則與工作流程（graph v2）、版本歷史 |
| `slides/index.html` | 教學 HTML 簡報（17 頁），每頁標出對應的 Wiki 頁 |
| `scripts/` | 檢查節點：`lint_wiki.py`（N4）、`check_outline.py`（N6c）、`check_slides.py`、`screenshot.py`（N8） |
| `runs/` | 這次實際執行的 12 份檢查報告與兩版截圖 |

## 重跑檢查

```bash
python3 scripts/lint_wiki.py
python3 scripts/check_outline.py
python3 scripts/check_slides.py
python3 scripts/screenshot.py slides/index.html runs/shots   # 需要 playwright
```
