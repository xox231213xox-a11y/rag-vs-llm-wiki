#!/usr/bin/env python3
"""N6c 大綱檢查（graph v2 新增）：產生簡報之前，先確認大綱要教的東西 wiki 裡都有。

  O1 大綱每一頁都指到至少一個存在的 wiki 頁面
  O2 「要定義的名詞」裡的每個名詞，在它指到的 wiki 頁面裡有定義句（名詞＋全形冒號）
  O3 大綱本身也是 wiki 頁：它的重點列要通過 lint（由 lint_wiki.py 負責，這裡只提醒）
有任何 O1/O2 錯誤 → 不准進 N7，回 N3（從 raw 補）或 N1（找新來源）。

用法：python3 scripts/check_outline.py [--out runs/xxx.txt]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
OUTLINE = WIKI / "syntheses" / "slide-outline.md"
PAGE_RE = re.compile(r"(?:concepts|comparisons|syntheses|sources)/[\w-]+\.md|overview\.md|index\.md|log\.md")

out = ROOT / sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
text = OUTLINE.read_text(encoding="utf-8")
errors, n_slides, n_terms = [], 0, 0

for line in text.splitlines():
    m = re.match(r"^(\d+)\. (.+)", line)
    if m:
        n_slides += 1
        pages = PAGE_RE.findall(line)
        if not pages and "本頁" not in line:
            errors.append(f"O1 第 {m.group(1)} 頁沒有指到任何 wiki 頁面：{line[:30]}")
        for p in pages:
            if not (WIKI / p).exists():
                errors.append(f"O1 第 {m.group(1)} 頁指到不存在的頁面 {p}")

sec = re.search(r"## 要定義的名詞.*?\n(.*?)(?=\n## )", text, re.S)
if not sec:
    errors.append("O2 大綱缺少「要定義的名詞」段落")
else:
    for line in sec.group(1).splitlines():
        m = re.match(r"^- (.+?)：.*?→ (\S+\.md)", line)
        if not m:
            continue
        term, page = m.group(1).strip(), m.group(2)
        n_terms += 1
        f = WIKI / page
        if not f.exists():
            errors.append(f"O2 名詞「{term}」指到不存在的頁面 {page}"); continue
        body = f.read_text(encoding="utf-8")
        if not re.search(rf"^- {re.escape(term)}：", body, re.M | re.I):
            errors.append(f"O2 名詞「{term}」在 {page} 裡沒有定義句（需要「- {term}：…」）")

report = "\n".join(["# check_outline 報告", f"大綱頁數 {n_slides}｜要定義的名詞 {n_terms}", f"錯誤 {len(errors)}"]
                   + [f"  ✗ {e}" for e in errors] + ["結果：" + ("PASS ✅ 可以進 N7" if not errors else "FAIL ❌ 回 N3/N1 補 wiki")])
print(report)
if out:
    out.write_text(report + "\n", encoding="utf-8")
sys.exit(1 if errors else 0)
