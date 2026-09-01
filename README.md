# The Recovery Zone — landing page

Single-page, mobile-first marketing site for The Recovery Zone, a recovery and mobility studio in
Muwaileh, Sharjah. Its only conversion action is sending people to Fresha; everything else is there
to explain the zones and build credibility.

Static HTML/CSS/JS. No build step, no framework. Editorial layout modelled on thehundred.ae:
white space, serif display type (Fraunces), a light sans for body copy (Jost), full-bleed zone
bands, and red as the single accent from the logo palette.

```
index.html      the whole page
styles.css      design system + all sections
main.js         nav drawer, Fresha link wiring, header state, zone image preview
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
| 3 | **Opening hours** | footer | Not published on the Instagram profile. |
| 4 | **Credibility figures** | `.figures` | Sessions delivered, qualified therapists, years operating. Three of four are `X` placeholders. |
| 5 | **Instagram feed** | social strip | Links to the real handle `@therecoveryzone.ae`, but the six tiles are placeholder blocks, not a live feed. |
| 5b | **Client testimonial** | `.quote` | Placeholder wording, flagged on the page. Needs a real client quote. |
| 6 | **Photography** | `assets/placeholders/*.svg` | Every image is a labelled grey block naming the shot it wants ("ice bath, two-person, studio interior"). No stock photos were used — they would misrepresent the studio. Drop real files in and update the `src`/`alt` pairs. |
| 7 | **Treatment copy** | massage menu | Working copy written in the poster's voice. Flagged under the massage list. The seven detailed treatments are rewritten from the poster rather than copied. |
| 7b | **Audience wording** | throughout | The Instagram bio describes a "Men's Wellness and Recovery center". The page copy is written for everyone ("Recovery is for everyone", straight from the same profile) — confirm which framing you want. |
| 8 | **Pricing** | — | Not present anywhere. No prices were invented. |
| 9 | **Contact details** | booking meta + footer | Phone/email to be confirmed. |

Taken from the real Instagram profile `@therecoveryzone.ae`: the studio name, the "Sore today.
Strong tomorrow." headline, "Built for performance. Made for everyone.", "Recovery is for
everyone", "Move better. Feel better.", the service line (Massage · Sauna · Ice Bath · Mobility)
and the Muwaileh Commercial, Sharjah address behind the profile's map link.

Final as delivered: layout and responsive behaviour, the zone structure, the seven-treatment
detail section with working-pressure labels, the how-to-book flow, and all tone/positioning copy.

## Regenerating placeholder images

```bash
python3 tools/make-placeholders.py
```

Edit the `SHOTS` list in that script to change a shot brief or add a new slot.
