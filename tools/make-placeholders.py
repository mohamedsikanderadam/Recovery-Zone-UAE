#!/usr/bin/env python3
"""Generate the neutral placeholder image blocks used until real studio photography lands.

Each block is a lightweight SVG: a muted tonal field and, where the artwork is not
sitting under page text, the shot brief so anyone reviewing can see which photograph
belongs there.

style:
  "quiet" — light tonal field, no text (sits behind or beside copy)
  "dark"  — charcoal tonal field, no text (full-bleed bands with white text over them)
  "brief" — light field with the shot brief printed on it
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "placeholders"

# name, width, height, label, shot brief, style
SHOTS = [
    ("hero", 2400, 1350, "Studio", "Studio interior, wide, low light", "dark"),
    ("massage-zone", 1600, 1200, "Massage", "Treatment suite, therapist working, low warm light", "quiet"),
    ("contrast-zone", 1600, 1200, "Contrast Zone", "Sauna and ice bath side by side, wide", "quiet"),
    ("stretch-zone", 1600, 1200, "Stretch Zone", "Assisted hip stretch on the mat", "quiet"),
    ("suites", 1600, 1200, "Recovery Suites", "Private recovery suite, chair and plants", "quiet"),
    ("sports-massage", 900, 700, "Sports Massage", "Hamstring work, athlete on table", "quiet"),
    ("deep-tissue", 900, 700, "Deep Tissue", "Forearm pressure into upper back", "quiet"),
    ("ice-bath", 900, 700, "Ice Bath", "Two-person ice bath, water surface detail", "quiet"),
    ("ice-bath-card", 1200, 900, "Ice Bath", "Two-person ice bath, water surface detail", "brief"),
    ("sauna", 1200, 900, "Sauna", "Five-person sauna, timber interior", "brief"),
    ("contrast-bath", 1200, 900, "Contrast Bath", "Client moving sauna to ice bath", "brief"),
    ("massage-chair", 1200, 900, "Massage Chair", "Massage chair in the recovery lounge", "brief"),
    ("consultation", 1200, 900, "Consultation", "Therapist and client at the assessment desk", "brief"),
    ("mobility", 1200, 900, "Mobility Work", "Loaded shoulder mobility drill", "brief"),
    ("ig-1", 800, 800, "Instagram", "Ice bath entry, shot from above", "quiet"),
    ("ig-2", 800, 800, "Instagram", "Therapist hands, deep tissue detail", "quiet"),
    ("ig-3", 800, 800, "Instagram", "Sauna door, steam, low light", "quiet"),
    ("ig-4", 800, 800, "Instagram", "Assisted stretch, side profile", "quiet"),
    ("ig-5", 800, 800, "Instagram", "Studio signage detail", "quiet"),
    ("ig-6", 800, 800, "Instagram", "Client post-session, towel, cold plunge", "quiet"),
]

FIELD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label} placeholder">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c1}"/>
      <stop offset="1" stop-color="{c2}"/>
    </linearGradient>
    <pattern id="p" width="18" height="18" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
      <line x1="0" y1="0" x2="0" y2="18" stroke="{ink}" stroke-opacity="{op}" stroke-width="8"/>
    </pattern>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <rect width="{w}" height="{h}" fill="url(#p)"/>
{extra}</svg>
"""

BRIEF_EXTRA = """  <text x="50%" y="{ty}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="{fs}" font-weight="600" letter-spacing="{ls}" fill="#0e1114" fill-opacity=".55">{label_uc}</text>
  <text x="50%" y="{sy}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="{sfs}" font-weight="400" fill="#0e1114" fill-opacity=".42">{brief}</text>
  <text x="50%" y="{ny}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="{sfs}" font-weight="500" letter-spacing="3" fill="#0e1114" fill-opacity=".28">PHOTOGRAPHY PENDING</text>
"""

TONES = {
    "quiet": ("#e9ebee", "#c8ccd2", "#0e1114", ".05"),
    "brief": ("#eceef1", "#d2d6dc", "#0e1114", ".05"),
    "dark": ("#2b2f34", "#101316", "#ffffff", ".035"),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, w, h, label, brief, style in SHOTS:
        c1, c2, ink, op = TONES[style]
        extra = ""
        if style == "brief":
            fs = round(min(w, h) * 0.062)
            extra = BRIEF_EXTRA.format(
                label_uc=label.upper(), brief=brief,
                fs=fs, sfs=round(fs * 0.46), ls=round(fs * 0.08, 1),
                ty=round(h / 2 - fs * 0.15), sy=round(h / 2 + fs * 0.7),
                ny=round(h / 2 + fs * 1.55),
            )
        (OUT / f"{name}.svg").write_text(
            FIELD.format(w=w, h=h, label=label, c1=c1, c2=c2, ink=ink, op=op, extra=extra)
        )
    print(f"wrote {len(SHOTS)} placeholders to {OUT}")


if __name__ == "__main__":
    main()
