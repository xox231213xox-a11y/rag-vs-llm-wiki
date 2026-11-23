#!/usr/bin/env python3
"""N4 Lint：檢查 wiki 的結構與來源對應。

檢查項目
  L1 frontmatter 齊全（title / type / sources / updated）
  L2 每條重點（- 開頭的列）都有來源標記 [Sx] / [比喻] / [討論]（「相關頁面」段落除外）
  L3 標記的來源存在於 raw/
  L4 頁內用到的 [Sx] 都列在 frontmatter 的 sources 裡
  L5 數字檢查：列中的數字必須出現在它標記的 raw 來源卡裡
  L6 相對連結都指得到檔案
  L7 沒有孤兒頁：每頁都列在 index.md
  L8 log.md 標題格式 ## [YYYY-MM-DD] 操作 | 標題

用法：python3 scripts/lint_wiki.py [--out runs/xxx-lint.txt]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"

TAG_RE = re.compile(r"\[(S\d+|比喻|討論)\]")
SRC_TAG_RE = re.compile(r"\[(S\d+)\]")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?%?")
LOG_HEAD_RE = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] [a-z]+ \| .+")


def raw_cards():
    cards = {}
    for p in sorted(RAW.glob("s*.md")):
        m = re.search(r"^id:\s*(S\d+)", p.read_text(encoding="utf-8"), re.M)
        if m:
            cards[m.group(1)] = p.read_text(encoding="utf-8")
    return cards


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text[end + 4:]


def numbers_in(line):
    clean = SRC_TAG_RE.sub("", line)
    clean = LINK_RE.sub(lambda m: m.group(1), clean)
    clean = re.sub(r"<https?://[^>]+>", "", clean)
    nums = []
    for n in NUM_RE.findall(clean):
        n = n.rstrip(",")
        if n:
            nums.append(n)
    return nums


def main():
    out_path = None
    if "--out" in sys.argv:
        out_path = ROOT / sys.argv[sys.argv.index("--out") + 1]

    cards = raw_cards()
    errors, warns = [], []
    pages = sorted(p for p in WIKI.rglob("*.md"))
    content_pages = [p for p in pages if p.name not in ("index.md", "log.md")]
    stats = {"pages": len(pages), "bullets": 0, "tagged": 0, "numbers_checked": 0, "links": 0}

    for p in pages:
        rel = p.relative_to(ROOT)
        text = p.read_text(encoding="utf-8")

        # L6 links (all pages)
        for _, target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            stats["links"] += 1
            t = (p.parent / target.split("#")[0]).resolve()
            if not t.exists():
                errors.append(f"L6 斷鏈 {rel}: ({target})")

        if p.name == "log.md":
            for line in text.splitlines():
                if line.startswith("## ") and not LOG_HEAD_RE.match(line):
                    errors.append(f"L8 log 標題格式錯 {rel}: {line}")
            continue
        if p.name == "index.md":
            continue

        fm, body = parse_frontmatter(text)
        if fm is None:
            errors.append(f"L1 缺 frontmatter {rel}")
            fm = {}
        for k in ("title", "type", "sources", "updated"):
            if k not in fm:
                errors.append(f"L1 frontmatter 缺 {k}: {rel}")
        fm_sources = set(re.findall(r"S\d+", fm.get("sources", "")))

        section = ""
        used = set()
        for i, line in enumerate(body.splitlines(), 1):
            if line.startswith("## "):
                section = line[3:].strip()
                continue
            if not line.startswith("- "):
                continue
            if section == "相關頁面":
                continue
            stats["bullets"] += 1
            tags = TAG_RE.findall(line)
            if not tags:
                errors.append(f"L2 沒有來源標記 {rel}: {line[:60]}")
                continue
            stats["tagged"] += 1
            srcs = [t for t in tags if t.startswith("S")]
            for s in srcs:
                used.add(s)
                if s not in cards:
                    errors.append(f"L3 來源不存在 {rel}: [{s}]")
            # L5 numbers
            if srcs:
                for n in numbers_in(line):
                    stats["numbers_checked"] += 1
                    if not any(n in cards.get(s, "") for s in srcs):
                        errors.append(f"L5 數字 {n} 不在標記的來源 {srcs} 裡 {rel}: {line[:60]}")
        missing = used - fm_sources
        if missing:
            errors.append(f"L4 frontmatter sources 少了 {sorted(missing)}: {rel}")

    # L7 orphans
    index_text = (WIKI / "index.md").read_text(encoding="utf-8")
    linked = {(WIKI / t.split("#")[0]).resolve() for _, t in LINK_RE.findall(index_text)}
    for p in content_pages:
        if p.resolve() not in linked:
            errors.append(f"L7 孤兒頁（index 沒列）: {p.relative_to(ROOT)}")

    lines = ["# lint_wiki 報告",
             f"頁數 {stats['pages']}｜重點列 {stats['bullets']}（有標記 {stats['tagged']}）｜"
             f"檢查數字 {stats['numbers_checked']}｜相對連結 {stats['links']}｜來源卡 {len(cards)}",
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
