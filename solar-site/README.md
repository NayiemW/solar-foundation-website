# solar.org — Solar Foundation static site

A self-contained, dependency-free static site (no build step, no React/Babel runtime).
Plain HTML + one small `app.js`. Deploy anywhere that serves static files.

## View it

**Option A — open directly (zero setup):**
Open `index.html` in a browser. Internal links, the accordion, the archive filter,
and the **live chain data** (fetched from `https://api.solar.org`) all work from `file://`.

**Option B — local server (production-like):**
```bash
cd solar-site
python3 -m http.server 8099
# open http://localhost:8099
```
Any static server works equally (nginx, Caddy, `npx serve`, Netlify, Cloudflare Pages, GitHub Pages).

## Pages
- `index.html` — homepage (hero + live console, stats, status, history accordion, exchanges, get-involved)
- `history.html` — full sourced timeline (Verified / Reported / Foundation-account tags)
- `governance.html` — SXP-GOV-2026-01 vote record + full proposal text
- `status.html` — current status + live chain metrics
- `exchanges.html` — where SXP trades + holder/exchange guidance + network parameters
- `archive.html` — blog archive (search + tag filter); 5 critical posts are durable local snapshots
- `archive/*.html` — local snapshots of the resignation, status update, governance posts, etc.

## Live data
`app.js` fetches the latest block + supply from `https://api.solar.org` every 30s and updates
the height, "last block Xs ago", supply, and the **advancing / delayed / stalled** indicator
based on the *real* last-block age. If the API is unreachable it shows "status unknown"
(it never fabricates liveness).

## ⚠ Before going live — fill these in
1. **Discord & Community/X URLs** — `index.html` has two `href="#"` placeholders in the
   "Get involved" grid (cards labelled *Discord* and *Community / X*). Replace `#` with real URLs.
2. **Confirm exchange links** still resolve and that each deposit network is **Solar mainnet**
   (the page already warns users to verify). `exchanges.html`, "Last reviewed" date.
3. Optionally point the homepage "community transparency report" button at a hosted copy of the report.

## Notes on accuracy
All facts were cross-checked against the research dossier (`../solar-transparency/SOLAR_HISTORY_RESEARCH.md`).
Archive dates/slugs were corrected (e.g. Core 3.3.0 → 2022-05-30, Solar Card → 2023-02-12,
BrighterVPN → 2024-10-18). The dead `github.com/NayiemW/solar-proposal` link was repointed to
`proposals.solar.org`. Voice is institutional (Foundation), third-person; Binance-related grievances
are labelled as the Foundation's account, not adjudicated fact.

Source design (Claude design-canvas export) is preserved in `../solar-foundation-site/`.
