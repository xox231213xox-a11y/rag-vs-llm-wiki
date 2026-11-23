#!/usr/bin/env python3
"""N8 版面檢查：用無頭瀏覽器逐頁截圖，並檢查內容有沒有壓到頁尾或超出畫面。

  V1 內容最下緣不能壓到頁尾的來源列
  V2 任何元素不能超出 1280×720 畫面右側或下緣
用法：python3 scripts/screenshot.py <html 路徑> <截圖資料夾> [--out runs/xxx.txt]
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

html = Path(sys.argv[1]).resolve()
shots = Path(sys.argv[2]); shots.mkdir(parents=True, exist_ok=True)
out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else None

JS = """() => {
  const s = document.querySelector('.slide.active');
  const sr = s.getBoundingClientRect();
  const foot = s.querySelector('footer.src').getBoundingClientRect();
  let maxBottom = 0, maxRight = 0, worst = '';
  s.querySelectorAll('*').forEach(el => {
    if (el.closest('footer.src') || el.classList.contains('content')) return;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    if (r.bottom - sr.top > maxBottom) { maxBottom = r.bottom - sr.top; worst = el.tagName + '.' + el.className + ' 「' + (el.textContent || '').trim().slice(0, 16) + '」'; }
    maxRight = Math.max(maxRight, r.right - sr.left);
  });
  return {title: (s.querySelector('h1,h2') || {}).textContent, maxBottom, footTop: foot.top - sr.top, maxRight, worst};
}"""

errors, lines = [], []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.goto(html.as_uri() + "#1")
    pg.wait_for_timeout(600)
    n = pg.evaluate("document.querySelectorAll('.slide').length")
    for i in range(1, n + 1):
        pg.evaluate(f"location.hash = '#{i}'"); pg.wait_for_timeout(250)
        idx = pg.evaluate("Array.from(document.querySelectorAll('.slide')).findIndex(s => s.classList.contains('active')) + 1")
        if idx != i:
            errors.append(f"V0 切換到第 {i} 頁失敗（目前在第 {idx} 頁），量測無效"); continue
        r = pg.evaluate(JS)
        pg.screenshot(path=str(shots / f"slide-{i:02d}.png"))
        t = (r["title"] or "").strip()[:18]
        lines.append(f"第 {i:2d} 頁 {t}: 內容下緣 {r['maxBottom']:.0f}px／頁尾 {r['footTop']:.0f}px，最右 {r['maxRight']:.0f}px")
        if r["maxBottom"] > r["footTop"] - 2:
            errors.append(f"V1 第 {i} 頁「{t}」內容壓到頁尾（下緣 {r['maxBottom']:.0f} > 頁尾 {r['footTop']:.0f}），最低的元素：{r['worst']}")
        if r["maxRight"] > 1280 or r["maxBottom"] > 720:
            errors.append(f"V2 第 {i} 頁「{t}」超出畫面")
    b.close()

report = "\n".join(["# 版面檢查報告（1280×720）"] + lines + [f"錯誤 {len(errors)}"] + [f"  ✗ {e}" for e in errors] + ["結果：" + ("PASS ✅" if not errors else "FAIL ❌")])
print(report)
if out:
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(report + "\n", encoding="utf-8")
sys.exit(1 if errors else 0)
