#!/usr/bin/env python3
"""N8 檢查簡報：簡報內容是否都能對應回 wiki。

檢查項目
  C1 每頁都有 data-wiki，且指到的 wiki 頁面存在
  C2 每頁的來源標記（data-src）都能在它引用的 wiki 頁面裡找到
  C3 數字：頁面上的每個數字，都要出現在它引用的 wiki 頁面裡
  C4 名詞：用 <dfn> 標記、在簡報上定義的名詞，要在引用的 wiki 頁面裡出現
  C5 頁數與 wiki/syntheses/slide-outline.md 的逐頁大綱一致
  C6 大綱引用的 wiki 頁面，簡報都有用到
  C7 簡報上 <dfn> 定義的名詞必須列在大綱的「要定義的名詞」，且該頁引用了名詞表指定的 wiki 頁（graph v2 新增）

用法：python3 scripts/check_slides.py [--out runs/xxx-check.txt]
"""
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SLIDES = ROOT / "slides" / "index.html"
OUTLINE = WIKI / "syntheses" / "slide-outline.md"
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?%?")


def main():
    out_path = None
    if "--out" in sys.argv:
        out_path = ROOT / sys.argv[sys.argv.index("--out") + 1]

    soup = BeautifulSoup(SLIDES.read_text(encoding="utf-8"), "html.parser")
    slides = soup.select("section.slide")
    errors = []
    used_pages = set()
    outline_text = OUTLINE.read_text(encoding="utf-8")
    gloss = dict(re.findall(r"^- (.+?)：.*?→ (\S+\.md)", outline_text, re.M))
    n_numbers = n_terms = 0

    for i, s in enumerate(slides, 1):
        title_el = s.find(["h1", "h2"])
        title = title_el.get_text(strip=True) if title_el else "(無標題)"
        label = f"第 {i} 頁「{title[:18]}」"
        pages = (s.get("data-wiki") or "").split()
        if not pages:
            errors.append(f"C1 {label}: 沒有 data-wiki")
            continue
        texts = []
        for p in pages:
            f = WIKI / p
            if not f.exists():
                errors.append(f"C1 {label}: wiki 頁面不存在 {p}")
            else:
                used_pages.add(p)
                texts.append(f.read_text(encoding="utf-8"))
        wiki_text = "\n".join(texts)

        for t in (s.get("data-src") or "").split():
            if f"[{t}]" not in wiki_text:
                errors.append(f"C2 {label}: 來源 [{t}] 不在引用的 wiki 頁面 {pages}")

        # 去掉不檢查的區塊再取文字
        body = BeautifulSoup(str(s), "html.parser")
        for el in body.select("[data-nocheck], style, script"):
            el.decompose()
        text = body.get_text(" ", strip=True)
        for n in NUM_RE.findall(text):
            n = n.rstrip(",")
            n_numbers += 1
            if n not in wiki_text:
                errors.append(f"C3 {label}: 數字 {n} 在引用的 wiki 頁面裡找不到")

        for d in s.find_all("dfn"):
            term = d.get_text(strip=True)
            n_terms += 1
            if term.lower() not in wiki_text.lower():
                errors.append(f"C4 {label}: 名詞「{term}」在引用的 wiki 頁面裡找不到")
            if term not in gloss:
                errors.append(f"C7 {label}: 名詞「{term}」沒有列在大綱的名詞表")
            elif gloss[term] not in pages:
                errors.append(f"C7 {label}: 名詞「{term}」應引用 {gloss[term]}")

    outline = OUTLINE.read_text(encoding="utf-8")
    planned = re.findall(r"^\d+\. ", outline, re.M)
    if len(planned) != len(slides):
        errors.append(f"C5 大綱有 {len(planned)} 頁，簡報有 {len(slides)} 頁")
    outline_pages = set(re.findall(r"(?:concepts|comparisons|syntheses)/[\w-]+\.md", outline))
    for p in sorted(outline_pages - used_pages):
        errors.append(f"C6 大綱用到 {p}，但簡報沒有任何一頁引用它")

    lines = ["# check_slides 報告",
             f"頁數 {len(slides)}｜引用 wiki 頁 {len(used_pages)}｜檢查數字 {n_numbers}｜檢查名詞 {n_terms}",
             f"錯誤 {len(errors)}"]
    lines += [f"  ✗ {e}" for e in errors]
    lines.append("結果：" + ("PASS ✅" if not errors else "FAIL ❌"))
    report = "\n".join(lines)
    print(report)
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report + "\n", encoding="utf-8")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
