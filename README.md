# Recovery Zone UAE — landing page

Single-page, mobile-first marketing site for Recovery Zone UAE, a clinician-led recovery and
mobility studio. Its only conversion action is sending people to Fresha; everything else is there
to explain the three zones and build credibility.

Static HTML/CSS/JS. No build step, no framework, no web fonts, no third-party requests.

```
index.html      the whole page
styles.css      design system + all sections
main.js         nav drawer, Fresha link wiring, treatment expand-on-jump
assets/         favicon + placeholder image blocks
tools/          regenerates the placeholder blocks
```

## Run it

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

Deploy by uploading the repo root to any static host (Netlify, Vercel, Cloudflare Pages, S3).

## Placeholder vs. final

Everything below is deliberately unfinished and marked in the markup with `data-placeholder`
(search the repo for `PLACEHOLDER` to find each one).

| # | Placeholder | Where | What's needed |
|---|---|---|---|
| 1 | **Fresha booking URL** | `main.js` → `FRESHA_URL` | The studio's real Fresha page. Set that one constant and every CTA (header, drawer, booking section, footer, sticky mobile bar) points at it. Until it is set the CTAs scroll to the booking section rather than to a dead link. |
| 2 | **Fresha embedded widget** | `index.html` → `.fresha-embed` | Fresha issues a per-venue website widget from the partner dashboard (Marketplace → Online booking). Paste the supplied iframe/script over that panel; the button underneath stays as the fallback. Not embedded yet because the widget snippet is venue-specific and we don't have the venue. |
| 3 | **Studio address** | booking section + footer | Exact area/mall. **Note:** the brief says Sharjah, the stat bar wording and the attached poster say Dubai (Cityland Mall). The page currently reads "Sharjah, UAE" — confirm which is right. |
| 4 | **Credibility stats** | `.stats` | Sessions delivered, number of qualified therapists, years operating. Three of four are `X` placeholders; the "Assessment-first, always" one is real copy. |
| 5 | **Instagram handle** | social strip, booking meta, footer | Currently links to the Birmingham sister page `@the_recovery_room_birmingham` and says so. Swap when the UAE handle is live. The grid is placeholder tiles, not a live feed. |
| 6 | **Photography** | `assets/placeholders/*.svg` | Every image is a labelled grey block naming the shot it wants ("ice bath, two-person, studio interior"). No stock photos were used — they would misrepresent the studio. Drop real files in and update the `src`/`alt` pairs. |
| 7 | **Treatment copy** | massage menu | Working copy written in the poster's voice. Flagged under the massage list. The seven detailed treatments are rewritten from the poster rather than copied. |
| 8 | **Pricing** | — | Not present anywhere. No prices were invented. |
| 9 | **Contact details** | booking meta + footer | Phone/email to be confirmed. |

Final as delivered: layout and responsive behaviour, the three-zone structure, the seven-treatment
detail section with working-pressure badges, the how-to-book flow, and all tone/positioning copy.

## Regenerating placeholder images

```bash
python3 tools/make-placeholders.py
```

Edit the `SHOTS` list in that script to change a shot brief or add a new slot.
