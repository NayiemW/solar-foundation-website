#!/usr/bin/env python3
import os, re, html, json
SITE = "/home/blackwell/workspace/monolythium-ecosystem/solar-site"
BASE = "https://solar.org"
OGIMG = "https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png"
OG = BASE + "/og.png"   # 1200x630 social card
LASTMOD = "2026-06-20"

def clean_path(relpath):
    # relpath like 'index.html', 'history.html', 'archive/slug.html'
    if relpath == "index.html": return "/"
    if relpath.endswith("/index.html"): return "/" + relpath[:-len("/index.html")]
    return "/" + relpath[:-len(".html")]

# gather html files
files = []
for root,_,fs in os.walk(SITE):
    for f in fs:
        if f.endswith(".html"):
            rel = os.path.relpath(os.path.join(root,f), SITE)
            files.append(rel.replace(os.sep,"/"))
files.sort()

ORG = {
  "@type":"Organization","@id":BASE+"/#org","name":"The Solar Foundation","url":BASE+"/",
  "logo":OGIMG,"sameAs":["https://github.com/Solar-network","https://blog.solar.org","https://solarscan.com"]
}

injected=0
for rel in files:
    p = os.path.join(SITE, rel)
    s = open(p, encoding="utf-8").read()
    if 'rel="canonical"' in s:
        continue  # already has SEO
    mt = re.search(r"<title>(.*?)</title>", s, re.S)
    md = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    title = (mt.group(1).strip() if mt else "Solar (SXP)")
    desc = (md.group(1).strip() if md else "")
    url = BASE + clean_path(rel)
    is_home = (rel == "index.html")
    graph = [ORG, {
        "@type":"WebPage","@id":url+"#page","url":url,"name":html.unescape(title),
        "description":html.unescape(desc),"isPartOf":{"@id":BASE+"/#website"},
        "publisher":{"@id":BASE+"/#org"},"inLanguage":"en"
    }, {
        "@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":"Solar (SXP) — The Solar Foundation",
        "publisher":{"@id":BASE+"/#org"},"inLanguage":"en"
    }]
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, separators=(",",":"))
    block = (
      "\n<!--seo-->\n"
      f'<link rel="canonical" href="{url}">\n'
      '<meta name="robots" content="index,follow,max-image-preview:large">\n'
      '<meta name="theme-color" content="#0a0a0d">\n'
      '<meta property="og:type" content="website">\n'
      '<meta property="og:site_name" content="The Solar Foundation">\n'
      f'<meta property="og:url" content="{url}">\n'
      f'<meta property="og:image" content="{OGIMG}">\n'
      '<meta name="twitter:card" content="summary">\n'
      f'<meta name="twitter:title" content="{html.escape(html.unescape(title))}">\n'
      f'<meta name="twitter:description" content="{html.escape(html.unescape(desc))}">\n'
      f'<meta name="twitter:image" content="{OGIMG}">\n'
      f'<script type="application/ld+json">{ld}</script>\n'
    )
    s = s.replace("</head>", block + "</head>", 1)
    open(p,"w",encoding="utf-8").write(s)
    injected += 1

# upgrade og/twitter image to the 1200x630 social card on every page (incl. already-SEO'd ones)
for rel in files:
    p = os.path.join(SITE, rel); s = open(p, encoding="utf-8").read(); o = s
    s = s.replace('property="og:image" content="%s"' % OGIMG, 'property="og:image" content="%s"' % OG)
    s = s.replace('name="twitter:image" content="%s"' % OGIMG, 'name="twitter:image" content="%s"' % OG)
    if "og:image:width" not in s:
        s = s.replace('<meta property="og:image" content="%s">' % OG,
                      '<meta property="og:image" content="%s">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">' % OG, 1)
    if s != o: open(p, "w", encoding="utf-8").write(s)

# sitemap.xml
def prio(rel):
    if rel=="index.html": return "1.0","weekly"
    if rel.startswith("archive/"): return "0.6","monthly"
    if rel in ("core5.html","agreement.html","report.html","history.html","evidence.html","faq.html"): return "0.9","monthly"
    return "0.7","monthly"
urls=[]
for rel in files:
    loc = BASE + clean_path(rel)
    pr,cf = prio(rel)
    urls.append(f"  <url><loc>{loc}</loc><lastmod>{LASTMOD}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>")
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
open(os.path.join(SITE,"sitemap.xml"),"w").write(sitemap)

# robots.txt
robots = ("User-agent: *\nAllow: /\n\n"
          "# AI / LLM crawlers welcome\n"
          "User-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n"
          f"Sitemap: {BASE}/sitemap.xml\n")
open(os.path.join(SITE,"robots.txt"),"w").write(robots)

# llms.txt (AI-friendly summary)
llms = f"""# Solar (SXP) — The Solar Foundation

> Public transparency record for the Solar (SXP) blockchain. Covers the full Swipe->Solar history, the Binance Token Swap Agreement (published in full), why the Core 5.0 upgrade was blocked, an 82-exhibit evidence pack of communications, and the network's current maintenance-only status. The project's lead resigned in late 2025; the network runs in maintenance-only mode; SXP was delisted by Binance on 2026-04-01.

## Key pages
- [History & timeline]({BASE}/history): sourced chronology 2018-2026
- [Core 5.0 blockers]({BASE}/core5): why the next-gen upgrade could not ship
- [Token Swap Agreement]({BASE}/agreement): the Binance agreement, full text
- [Community report]({BASE}/report): the record + 82 screenshot exhibits
- [Evidence index]({BASE}/evidence): all 82 exhibits classified by topic (mainnet support raised in 68 of 82; treasury in 43; card fees in 18)
- [FAQ]({BASE}/faq): Core 5.0, the agreement, the supply, Solar Card, Monolythium
- [Governance]({BASE}/governance): SXP-GOV-2026-01 vote record
- [Status]({BASE}/status): live network status
- [Exchanges]({BASE}/exchanges): where SXP still trades
- [Archive]({BASE}/archive): blog post snapshots

## Notes
- Facts established by the published agreement are cited by clause; other points are labelled the Foundation's stated position and are not independently confirmed.
- Contact: hello@solar.org
"""
open(os.path.join(SITE,"llms.txt"),"w").write(llms)

print(f"SEO injected into {injected} pages; sitemap urls: {len(urls)}; robots.txt, llms.txt written")
