#!/usr/bin/env python3
"""Generate the neutral placeholder image blocks used until real studio photography lands.

Each block is a lightweight SVG: a muted duotone field, a frame, and the shot brief
so anyone reviewing the page can see exactly which photograph belongs there.
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "placeholders"

# name, width, height, label, shot brief, quiet
# quiet blocks sit under a text overlay on the page, so they stay unlabelled —
# the shot brief lives in the alt text instead of on top of the artwork.
SHOTS = [
    ("massage-zone", 1600, 1000, "Massage Zone", "Treatment room, therapist working, low warm light", True),
    ("contrast-zone", 1600, 1000, "Contrast Zone", "Sauna and ice bath, studio interior, wide", True),
    ("sports-massage", 900, 700, "Sports Massage", "Hamstring work, athlete on table", True),
    ("deep-tissue", 900, 700, "Deep Tissue", "Forearm pressure into upper back", True),
    ("ice-bath", 900, 700, "Ice Bath", "Two-person ice bath, water surface detail", True),
    ("stretch-zone", 900, 700, "Stretch Zone", "Assisted hip stretch on the mat", True),
    ("ice-bath-card", 1200, 900, "Ice Bath", "Two-person ice bath, water surface detail"),
    ("sauna", 1200, 900, "Sauna", "Five-person sauna, timber interior"),
    ("contrast-bath", 1200, 900, "Contrast Bath", "Client moving sauna to ice bath"),
    ("massage-chair", 1200, 900, "Massage Chair", "Massage chair in the recovery lounge"),
    ("consultation", 1200, 900, "Consultation", "Therapist and client at the assessment desk"),
    ("mobility", 1200, 900, "Mobility Work", "Loaded shoulder mobility drill"),
    ("ig-1", 800, 800, "Instagram", "Ice bath entry, shot from above"),
    ("ig-2", 800, 800, "Instagram", "Therapist hands, deep tissue detail"),
    ("ig-3", 800, 800, "Instagram", "Sauna door, steam, low light"),
    ("ig-4", 800, 800, "Instagram", "Assisted stretch, side profile"),
    ("ig-5", 800, 800, "Instagram", "Studio signage detail"),
    ("ig-6", 800, 800, "Instagram", "Client post-session, towel, cold plunge"),
]

QUIET_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label} placeholder">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e2e6ec"/>
      <stop offset="1" stop-color="#bcc4cf"/>
    </linearGradient>
    <pattern id="p" width="18" height="18" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
      <line x1="0" y1="0" x2="0" y2="18" stroke="#0e1114" stroke-opacity=".045" stroke-width="8"/>
    </pattern>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <rect width="{w}" height="{h}" fill="url(#p)"/>
</svg>
"""

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label} placeholder">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e9ebef"/>
      <stop offset="1" stop-color="#cfd4dc"/>
    </linearGradient>
    <pattern id="p" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
      <rect width="14" height="14" fill="none"/>
      <line x1="0" y1="0" x2="0" y2="14" stroke="#0e1114" stroke-opacity=".05" stroke-width="6"/>
    </pattern>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <rect width="{w}" height="{h}" fill="url(#p)"/>
  <rect x="{m}" y="{m}" width="{iw}" height="{ih}" fill="none" stroke="#0e1114" stroke-opacity=".22" stroke-width="2" stroke-dasharray="10 8"/>
  <text x="50%" y="{ty}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="{fs}" font-weight="700" letter-spacing="{ls}" fill="#0e1114" fill-opacity=".62">{label_uc}</text>
  <text x="50%" y="{sy}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="{sfs}" font-weight="500" fill="#0e1114" fill-opacity=".45">{brief}</text>
  <text x="50%" y="{ny}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="{sfs}" font-weight="600" letter-spacing="3" fill="#0e1114" fill-opacity=".3">PHOTOGRAPHY PENDING</text>
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, w, h, label, brief, *rest in SHOTS:
        m = round(min(w, h) * 0.045)
        fs = round(min(w, h) * 0.072)
        if rest and rest[0]:
            (OUT / f"{name}.svg").write_text(QUIET_TEMPLATE.format(w=w, h=h, label=label))
            continue
        svg = TEMPLATE.format(
            w=w, h=h, m=m, iw=w - 2 * m, ih=h - 2 * m,
            label=label, label_uc=label.upper(), brief=brief,
            fs=fs, sfs=round(fs * 0.42), ls=round(fs * 0.06, 1),
            ty=round(h / 2 - fs * 0.15), sy=round(h / 2 + fs * 0.62),
            ny=round(h / 2 + fs * 1.4),
        )
        (OUT / f"{name}.svg").write_text(svg)
    print(f"wrote {len(SHOTS)} placeholders to {OUT}")


if __name__ == "__main__":
    main()
