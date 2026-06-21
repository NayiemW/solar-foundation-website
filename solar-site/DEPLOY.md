# Deploy instructions — solar.org (Solar Foundation transparency site)

## What this is
A **static website** — plain HTML/CSS + one `app.js`, no build step, no backend, no database.
It fetches live chain data **client-side** from `https://api.solar.org` (CORS is open/reflective, so it works from any domain). Nothing server-side is required.

- **Source directory to deploy:** `/home/blackwell/workspace/monolythium-ecosystem/solar-site/`
- **Target domain:** `https://solar.org` (deploy at the **root** of the domain)
- **Size:** ~21 MB (mostly the 82 exhibit screenshots under `report-assets/`)

## ⚠️ The one hard requirement: CLEAN URLs (extensionless)
All internal navigation uses root-absolute, extensionless paths (`/history`, `/core5`, `/agreement`, `/report`, `/evidence`, `/faq`, `/governance`, `/status`, `/exchanges`, `/archive`, `/archive/<slug>`).
The host **must** serve `history.html` at `/history` (and ideally 301-redirect `/history.html` → `/history`).
**Do NOT** deploy as a single-page app / catch-all to `index.html` — unknown paths should 404, known `.html` files must resolve at their extensionless path.

## Files already included (don't add/remove)
`index.html` + 10 pages, `archive/` (5 snapshots), `report-assets/` (82 `.jpg` + nothing else), `solar-community-report.docx`, `app.js`, `og.png`, `sitemap.xml`, `robots.txt`, `llms.txt`, `favicon` is referenced via external URL.

---

## Pick ONE host

### Option 1 — Cloudflare Pages (recommended: free, fast, clean URLs automatic)
1. Create a Pages project, **Direct Upload** (no build command, output dir = the folder).
   - CLI: `npx wrangler pages deploy /home/blackwell/workspace/monolythium-ecosystem/solar-site --project-name solar-org`
2. Clean URLs work by default (serves `/history` from `history.html`, redirects `.html`).
3. Add custom domain `solar.org` in the Pages project → set DNS (Cloudflare will guide; CNAME/`A` to Pages).

### Option 2 — Netlify (drag-and-drop or CLI)
1. `npx netlify deploy --dir=/home/blackwell/workspace/monolythium-ecosystem/solar-site --prod`
2. Netlify "Pretty URLs" is on by default → clean URLs + `.html` redirects handled.
3. Add domain `solar.org` in Site settings → DNS.

### Option 3 — Vercel
1. Add a `vercel.json` in the folder with:
   ```json
   { "cleanUrls": true, "trailingSlash": false }
   ```
2. `npx vercel deploy --prod /home/blackwell/workspace/monolythium-ecosystem/solar-site`
3. Assign domain `solar.org`.

### Option 4 — Railway / any VPS via Caddy (clean URLs built in)
Put this `Caddyfile` next to the site and run Caddy with the folder as web root:
```
solar.org {
    root * /srv
    encode gzip zstd
    try_files {path} {path}.html {path}/index.html
    file_server
    header /og.png Cache-Control "public, max-age=86400"
}
```
- Copy `solar-site/*` into `/srv`. `try_files {path} {path}.html` is what gives clean URLs.
- On Railway: deploy a Caddy service, mount/copy the `solar-site` contents as the web root, point the `solar.org` domain at the service.

### Option 5 — nginx
```
server {
    listen 443 ssl;
    server_name solar.org;
    root /var/www/solar-site;
    index index.html;
    location / { try_files $uri $uri.html $uri/ =404; }
}
```

---

## DNS
Point `solar.org` (apex) to the chosen host per its instructions. Keep `blog.solar.org` and `explorer/solarscan` untouched — this deploy is **only** the apex `solar.org`.

## Post-deploy verification (must all pass)
```
https://solar.org/                → 200 (homepage, live block height renders)
https://solar.org/history         → 200 (NOT a 404, NOT index.html)
https://solar.org/agreement       → 200
https://solar.org/report          → 200 (82 exhibits load)
https://solar.org/evidence        → 200 (tally + rows; "View screenshot" expands)
https://solar.org/archive/resignation-statement-nayiem-w → 200
https://solar.org/history.html    → 301 → /history   (clean-URL redirect)
https://solar.org/og.png          → 200 image/png
https://solar.org/sitemap.xml     → 200
https://solar.org/robots.txt      → 200
https://solar.org/llms.txt        → 200
```
Also confirm: the hero "last block height" updates (client fetch to api.solar.org), nav dropdowns open, FAQ accordion works, social preview shows the og.png card (test with an X/Discord/Slack paste or opengraph.xyz).

## After it's live
- Submit `https://solar.org/sitemap.xml` in Google Search Console.
- Do **not** change the canonical domain (all `<link rel=canonical>` + sitemap + OG point to `https://solar.org`).

## Notes / TODO from the build session
- Discord / X URLs were not available, so those nav/community links were omitted (Contact → hello@solar.org is wired). Add them later if desired.
- To regenerate the site after content edits: run `../solar-build/rebuild.sh` (order: pages → report → evidence → SEO → unified-nav).
