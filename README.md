# Solar transparency website (solar.org)

- **solar-site/** — the built static site (HTML/CSS + app.js, live chain data from api.solar.org). Deployed at https://solar.org.
- **solar-build/** — Python build pipeline that generates `solar-site/` (`rebuild.sh`, build_*.py, evidence/posts data).
- **solar-transparency/** — research & design docs (history research, design brief, roadmap).
- **solar-site-server.js** — dependency-free Node clean-URL static server (runs under pm2 on the node; `/history` → history.html, `.html` → 301, unknown → 404).

Static, no backend. Clean URLs required (root-absolute extensionless links); see solar-site/DEPLOY.md.
