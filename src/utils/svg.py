"""Tiny SVG chart writer, no dependencies. Light and dark colors switch with
prefers-color-scheme, so the charts follow the GitHub theme."""
from html import escape

STYLE = """<style>
svg{--bg:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--grid:#e4e3df;--base:#a3a29c;
--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--cell:#e9e8e4;font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
@media (prefers-color-scheme:dark){svg{--bg:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--grid:#383835;
--base:#77766f;--s1:#3987e5;--s2:#d95926;--s3:#199e70;--cell:#3a3a37}}
.bg{fill:var(--bg)}.t{fill:var(--ink)}.t2{fill:var(--ink2)}.g{stroke:var(--grid)}
.base{fill:var(--base)}.s1{fill:var(--s1)}.s2{fill:var(--s2)}.s3{fill:var(--s3)}.cell{fill:var(--cell)}
.l1{stroke:var(--s1)}.l2{stroke:var(--s2)}.l3{stroke:var(--s3)}.lb{stroke:var(--base)}
</style>"""


class Svg:
    def __init__(self, w, h, title):
        self.w, self.h, self.parts = w, h, []
        self.parts.append(f'<rect class="bg" width="{w}" height="{h}" rx="8"/>')
        self.text(20, 30, title, size=16, weight=600)

    def text(self, x, y, s, cls="t", size=12, anchor="start", weight=400):
        self.parts.append(f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" font-size="{size}" '
                          f'font-weight="{weight}" text-anchor="{anchor}">{escape(str(s))}</text>')

    def rect(self, x, y, w, h, cls, rx=2, tip=None):
        t = f"<title>{escape(tip)}</title>" if tip else ""
        self.parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(0, w):.1f}" height="{h:.1f}" '
                          f'rx="{rx}" class="{cls}">{t}</rect>')

    def line(self, x1, y1, x2, y2, cls="g", width=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                          f'class="{cls}" stroke-width="{width}"{d}/>')

    def path(self, pts, cls, width=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        p = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f},{y:.1f}" for i, (x, y) in enumerate(pts))
        self.parts.append(f'<path d="{p}" class="{cls}" fill="none" stroke-width="{width}"{d}/>')

    def dot(self, x, y, cls, tip=None):
        t = f"<title>{escape(tip)}</title>" if tip else ""
        self.parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" class="{cls}" '
                          f'stroke="var(--bg)" stroke-width="2">{t}</circle>')

    def legend(self, x, y, items):
        for cls, label in items:
            self.rect(x, y - 9, 10, 10, cls)
            self.text(x + 15, y, label, "t2", 12)
            x += 22 + 7 * len(label)

    def save(self, path):
        body = "\n".join(self.parts)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                    f'viewBox="0 0 {self.w} {self.h}">\n{STYLE}\n{body}\n</svg>\n')


def hbars(path, title, rows, unit="", width=860, label_w=230, note=None, max_v=None):
    """rows: (label, value, cls, value_text). One series, grouped by row."""
    row_h = 22
    top = 56 if note else 46
    h = top + row_h * len(rows) + 30
    s = Svg(width, h, title)
    if note:
        s.text(20, 48, note, "t2", 12)
    x0, x1 = label_w, width - 80
    vmax = max_v or nice(max(v for _, v, _, _ in rows))
    for k in range(5):
        gx = x0 + (x1 - x0) * k / 4
        s.line(gx, top - 4, gx, top + row_h * len(rows), "g")
        s.text(gx, top + row_h * len(rows) + 16, f"{vmax * k / 4:.0f}{unit}", "t2", 11, "middle")
    for i, (label, v, cls, vt) in enumerate(rows):
        y = top + i * row_h
        s.text(x0 - 8, y + 15, label, "t", 12, "end")
        s.rect(x0, y + 4, (x1 - x0) * v / vmax, row_h - 8, cls, tip=f"{label}: {vt}")
        s.text(x0 + (x1 - x0) * v / vmax + 6, y + 15, vt, "t2", 11)
    s.save(path)


def panels(path, title, labels, cols, label_w=250, width=900, legend=None):
    """Small multiples: one bar panel per metric, rows share labels.
    cols: (name, values, fmt, classes)."""
    row_h = 21
    top = 90
    h = top + row_h * len(labels) + 20
    s = Svg(width, h, title)
    if legend:
        s.legend(20, 52, legend)
    pw = (width - label_w - 20) / len(cols)
    for i, lb in enumerate(labels):
        s.text(label_w - 8, top + i * row_h + 14, lb, "t", 12, "end")
    for c, (name, vals, fmt, classes) in enumerate(cols):
        x0 = label_w + c * pw + 6
        bw = pw - 60
        vmax = max(vals) * 1.05
        s.text(x0, top - 8, name, "t", 12, weight=600)
        s.line(x0, top - 2, x0, top + row_h * len(labels), "g")
        for i, v in enumerate(vals):
            y = top + i * row_h
            s.rect(x0, y + 4, bw * v / vmax, row_h - 8, classes[i], tip=f"{labels[i]}: {fmt(v)}")
            s.text(x0 + bw * v / vmax + 5, y + 14, fmt(v), "t2", 11)
    s.save(path)


def nice(v):
    """Smallest round axis end at or above v, with 4 grid steps."""
    for mag in (0.1, 1, 10, 100, 1000):
        for st in (1, 2, 2.5, 3, 5):
            if st * mag * 4 >= v * 1.05:
                return st * mag * 4
    return v


def lines(path, title, xs, series, ylabel, width=430, height=280, x_fmt=str, hi=None):
    """series: (label, values, line_cls, dot_cls, dash)."""
    s = Svg(width, height, title)
    s.legend(20, 52, [(d or l.replace("l", "s") if l != "lb" else "base", n) for n, _, l, d, _ in series])
    x0, x1, y0, y1 = 50, width - 20, height - 40, 90
    allv = [v for _, vals, *_ in series for v in vals]
    lo, hi = 0, hi or nice(max(allv))
    for k in range(5):
        gy = y0 - (y0 - y1) * k / 4
        s.line(x0, gy, x1, gy, "g")
        s.text(x0 - 6, gy + 4, f"{lo + (hi - lo) * k / 4:.0f}", "t2", 11, "end")
    s.text(x0, y1 - 10, ylabel, "t2", 11)

    def px(i):
        return x0 + (x1 - x0) * i / (len(xs) - 1)

    for i, x in enumerate(xs):
        s.text(px(i), y0 + 16, x_fmt(x), "t2", 11, "middle")
    for label, vals, lcls, dcls, dash in series:
        pts = [(px(i), y0 - (y0 - y1) * (v - lo) / (hi - lo)) for i, v in enumerate(vals)]
        s.path(pts, lcls, 2, dash)
        if dcls:
            for (x, y), v, xv in zip(pts, vals, xs):
                s.dot(x, y, dcls, f"{label}, {x_fmt(xv)}: {v:.1f}")
    s.save(path)


def strips(path, title, rows, abbrev, cls_of, legend, width=900):
    """rows: (label, maps). One cell per round."""
    cell, gap, label_w = 21, 2, 190
    top = 70
    h = top + len(rows) * (cell + 10) + 10
    s = Svg(width, h, title)
    s.legend(20, 52, legend)
    for r, (label, maps) in enumerate(rows):
        y = top + r * (cell + 10)
        s.text(label_w - 8, y + 15, label, "t", 12, "end")
        for i, m in enumerate(maps):
            x = label_w + i * (cell + gap)
            if x + cell > width - 10:
                break
            cls = cls_of(m)
            s.rect(x, y, cell, cell, cls, 3, f"Round {i + 1}: {m}")
            s.text(x + cell / 2, y + 14.5, abbrev(m), "t" if cls == "cell" else "t", 9, "middle", 600)
    s.save(path)
