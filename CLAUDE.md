# CLAUDE.md — RAG vs LLM Wiki 知識庫的 schema

這個 repo 是一個依照 Karpathy「LLM Wiki」模式建立的知識庫，主題是 **RAG 與 LLM Wiki：AI 怎麼記住知識**。
AI（Claude）是 wiki 的維護者；人（Jack）負責挑來源、在 ingest 時討論重點、審核成果。
任何 AI 工具在這個 repo 工作前，先讀完本檔。

## 1. 三層架構

| 層 | 位置 | 誰能改 | 內容 |
|---|---|---|---|
| Raw | `raw/sNN-*.md` | 取得後**不可改** | 來源資訊＋擷取重點（改寫，不轉載全文） |
| Wiki | `wiki/` | AI 維護 | 來源摘要頁、概念頁、比較頁、綜合頁、`index.md`、`log.md` |
| Schema | `CLAUDE.md`（本檔） | 人＋AI 一起改 | 結構、慣例、工作流程（graph） |

## 2. Wiki 頁面慣例

- 每頁開頭要有 frontmatter：`title`、`type`（source / concept / comparison / synthesis / overview）、`sources`（如 `[S1, S6]`）、`updated`。
- **每一條重點（以 `- ` 開頭的列）結尾都要有來源標記**：`[S1]`～`[S7]`，可多個如 `[S1][S6]`。
  - 不是來自來源、而是我們自己為了教學設計的比喻，標 `[比喻]`。
  - 記錄 ingest 討論結果的列，標 `[討論]`。
  - 例外：`## 相關頁面` 底下的連結清單、`index.md`、`log.md` 不需要標記。
- 內含數字（年份、百分比、token 數）的列，該數字必須能在它標記的 raw 來源卡裡找到。
- 連結一律用相對路徑的標準 markdown 連結（GitHub 上可直接點）。
- 每一頁都要列在 `wiki/index.md`；不能有孤兒頁。
- `wiki/log.md` 只能往下追加，格式：`## [YYYY-MM-DD] 操作 | 標題`。
- 用語：繁體中文（台灣），專有名詞第一次出現附英文。

## 3. 工作流程（graph v2，目前版本）

```
N1 取得資料 ─▶ N2 討論（人） ─▶ N3 編譯進 wiki ─▶ N4 Lint ──失敗──▶ 回 N3
   ▲                                              │ 通過
   └──────────────── 下一篇 ◀──────────────────────┘   （每篇來源都跑一次 N1→N4）
                         │ 全部 ingest 完
                         ▼
N5 查詢 wiki ─▶ N6 整理重點（大綱＋名詞表，存回 wiki）─▶ N6c 大綱檢查 ──缺內容──▶ 回 N3（從 raw 補）或 N1（找新來源）
                                                          │ 通過
                                                          ▼
                              N7 產生 HTML 簡報 ─▶ N8 檢查簡報 ──失敗──▶ 回 N7
                                                          │ 通過
                                                          ▼
                                                      N9 發布
```

| 節點 | 做什麼 | 產出 | 檢查方式 |
|---|---|---|---|
| N1 取得資料 | 抓來源、寫 raw 來源卡 | `raw/sNN-*.md` | — |
| N2 討論 | 列出每篇重點，由人勾選要強調什麼 | 討論結果（寫進 log） | 人 |
| N3 編譯 | 寫來源摘要頁、更新概念頁/比較頁、index、log。**每寫一條就對照 raw 來源卡，不准用模型自己的知識補** | `wiki/**` | 自我對照 raw |
| N4 Lint | **每 ingest 一篇就跑**（v1 是全部 ingest 完才跑） | `runs/*-lint.txt` | `scripts/lint_wiki.py`＋語意檢查 |
| N5 查詢 | 讀 `index.md` 找出教學需要的頁面 | 頁面清單 | — |
| N6 整理重點 | 寫成簡報大綱＋「要定義的名詞」表，存回 wiki | `wiki/syntheses/slide-outline.md` | — |
| **N6c 大綱檢查**（v2 新增） | 大綱每頁都指到存在的 wiki 頁；名詞表每個名詞在 wiki 都有定義句 | `runs/*-outline.txt` | `scripts/check_outline.py` |
| N7 產生簡報 | 依大綱產生 HTML，每頁標 `data-wiki` 與來源；**只能用大綱與 wiki 的內容** | `slides/index.html` | — |
| N8 檢查簡報 | C1–C7 來源／數字／名詞對應；逐頁語意對照；截圖看版面 | `runs/*-check.txt`、截圖 | `scripts/check_slides.py`、`scripts/screenshot.py`、人工看截圖 |
| N9 發布 | 推到 GitHub Pages | 網址 | 線上打開確認 |

### 會重複執行的部分
- N1→N4 對每一篇來源各跑一次（7 次）。
- N4 失敗回 N3、N6c 失敗回 N3/N1、N8 失敗回 N7，直到通過。

### 版本歷史
- **v1**：lint 只在全部 ingest 完跑一次；大綱寫完直接產生簡報；簡報做完才檢查。
- **v2**（第一次實際執行後修改，見 `wiki/log.md` 與 `runs/`）：
  1. Lint 從「全部 ingest 後」移到「每篇 ingest 後」：第一次 lint 的 4 個錯誤都是後來的來源改了舊頁面卻沒同步 frontmatter，越晚檢查越難追是哪一篇造成的。
  2. 新增 N6c 大綱檢查，並在大綱加「要定義的名詞」表：v1 的簡報有 3 處內容不在 wiki（embedding、向量資料庫的定義、人與 LLM 的分工），因為大綱沒先確認 wiki 有沒有這些內容，生成時 AI 就自己補。
  3. N3 加上「每條都對照 raw 來源卡」的規則：補 embedding 頁時又寫出一句來源沒有的話（問題也轉成向量），對照 raw 才抓到。
  4. N8 新增 C7 規則（簡報上的名詞必須在名詞表），並修正截圖腳本：v1 的截圖檢查一直量到第 1 頁，給出假的 PASS。

## 4. 指令

- `ingest raw/sNN-*.md`：跑 N2→N3。
- `lint`：`python3 scripts/lint_wiki.py`
- `check outline`：`python3 scripts/check_outline.py`
- `check slides`：`python3 scripts/check_slides.py && python3 scripts/screenshot.py slides/index.html runs/shots`
- `query <問題>`：先讀 `wiki/index.md`，再讀相關頁，附 `[Sx]` 回答；好的答案存到 `wiki/syntheses/`。
