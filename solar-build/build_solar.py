#!/usr/bin/env python3
import re, json, os, html

SRC = "/home/blackwell/workspace/monolythium-ecosystem/solar-foundation-site"
OUT = "/home/blackwell/workspace/monolythium-ecosystem/solar-site"
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(OUT, "archive"), exist_ok=True)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">')
FAVICON = '<link rel="icon" href="https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png">'

LINKMAP = [
    ("Solar.dc.html", "index.html"),
    ("History.dc.html", "history.html"),
    ("Governance.dc.html", "governance.html"),
    ("Status.dc.html", "status.html"),
    ("Exchanges.dc.html", "exchanges.html"),
    ("Archive.dc.html", "archive.html"),
]

def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read()

def extract_xdc(src):
    m = re.search(r"<x-dc>(.*)</x-dc>", src, re.DOTALL)
    return m.group(1)

def split_helmet(xdc):
    m = re.search(r"<helmet>(.*?)</helmet>", xdc, re.DOTALL)
    helmet = m.group(1) if m else ""
    body = xdc[m.end():] if m else xdc
    # keep only the <style>...</style> from helmet (fonts/favicon we re-add ourselves)
    sm = re.search(r"<style>(.*?)</style>", helmet, re.DOTALL)
    style = sm.group(0) if sm else ""
    return style, body.strip()

def mark_chainstate(s):
    pat = re.compile(
        r"<span style=\"(display:inline-flex;align-items:center;gap:7px;font-family:'JetBrains Mono',monospace;font-size:1[23]px;color:#46d39a;)\">"
        r"(<span style=\"[^\"]*background:#46d39a;[^\"]*animation:solarPulse[^\"]*\"></span>)"
        r"([^<]*)</span>")
    def rep(m):
        dot = m.group(2).replace("<span ", '<span data-live="chaindot" ', 1)
        return f'<span data-live="chainstate" style="{m.group(1)}">{dot}{m.group(3)}</span>'
    return pat.sub(rep, s)

def common(body):
    for a, b in LINKMAP:
        body = body.replace(a, b)
    body = body.replace("style-hover=", "data-h=")
    body = mark_chainstate(body)
    # fix broken / 404 link -> live proposal
    body = body.replace("https://github.com/NayiemW/solar-proposal", "https://proposals.solar.org/")
    # --- relabel tier-3 so it reads as a neutral official statement, not an admission of fault ---
    body = body.replace(
        "the Foundation's own account of internal events and are labelled as such — they are consistent with the public record but have not been independently adjudicated, and the other parties have not publicly responded.",
        "statements the Foundation has placed on record about internal events, labelled accordingly. They are consistent with the public record but have not yet been independently confirmed, and the parties involved have not responded publicly.")
    body = body.replace(
        "the Foundation's account; the other parties have not publicly responded.",
        "the Foundation's stated position; the parties involved have not responded publicly.")
    body = body.replace("the Foundation's own account</span>",
                        "the Foundation's statement, not yet independently confirmed</span>")
    body = body.replace("FOUNDATION ACCOUNT", "FOUNDATION STATEMENT")
    body = body.replace(">ACCOUNT</span>", ">FOUNDATION STATEMENT</span>")
    body = body.replace("the Foundation's own account of events", "the Foundation's stated position")
    # widen the tag column so the longer "FOUNDATION STATEMENT" pill never wraps
    body = body.replace("flex:none;width:120px;", "flex:none;width:152px;white-space:nowrap;")
    # link the now-published Token Swap Agreement from the wind-down record (history Era V / homepage panel 5)
    body = body.replace(
        ">Status Update ↗</a>",
        ">Status Update ↗</a> <a href=\"agreement.html\" style=\"color:#cbb27e;text-decoration:underline;\">Token Swap Agreement ↗</a>")
    # prominent button under the homepage history accordion
    body = body.replace(
        "Read the full research dossier (88 sources) →</a>",
        "Read the full research dossier (88 sources) →</a>"
        "<a href=\"agreement.html\" data-h=\"border-color:rgba(246,166,35,.5);\" style=\"display:inline-flex;align-items:center;gap:8px;background:rgba(246,166,35,.08);border:1px solid rgba(246,166,35,.3);color:#f6a623;font-size:14px;font-weight:600;text-decoration:none;padding:13px 20px;border-radius:9px;\">Binance Token Swap Agreement →</a>")
    # add Core 5.0 + FAQ to the nav on every page (inserted before the Open Explorer CTA)
    body = body.replace(
        '<a class="nav-cta" href="https://solarscan.com" target="_blank" rel="noopener"',
        '<a href="core5.html" style="text-decoration:none;" data-h="color:#f4f3f6;">Core 5.0</a>'
        '<a href="report.html" style="text-decoration:none;" data-h="color:#f4f3f6;">Report</a>'
        '<a href="faq.html" style="text-decoration:none;" data-h="color:#f4f3f6;">FAQ</a>'
        '<a class="nav-cta" href="https://solarscan.com" target="_blank" rel="noopener"')
    # homepage callout band emphasising the Core 5.0 story (injected before the Exchanges section)
    band = ('<div style="border-top:1px solid #1c1b21;background:#0c0b10;position:relative;overflow:hidden;">'
      '<div style="position:absolute;top:0;left:50%;transform:translateX(-50%);width:760px;height:260px;background:radial-gradient(ellipse at top,rgba(255,140,90,.10),rgba(255,140,90,0) 70%);pointer-events:none;"></div>'
      '<div class="pagewrap" style="position:relative;max-width:1240px;margin:0 auto;padding:70px 32px;">'
      '<div style="font-family:\'JetBrains Mono\',monospace;font-size:12px;letter-spacing:.18em;color:#f6a623;text-transform:uppercase;margin-bottom:16px;">The upgrade that was blocked</div>'
      '<h2 class="h2sec" style="font-family:\'Space Grotesk\',sans-serif;font-weight:600;font-size:34px;line-height:1.12;letter-spacing:-.02em;margin:0 0 14px;max-width:780px;">Core 5.0 was ready &mdash; here&rsquo;s why it could never ship.</h2>'
      '<p style="font-size:16.5px;line-height:1.7;color:#9a99a2;max-width:780px;margin:0 0 30px;">Core 5.0 reached ~90% testnet completion. Releasing it required Binance&rsquo;s consent &mdash; conditioned, in the Foundation&rsquo;s account, on cancelling the agreed monthly timelock, transferring all remaining 18M SXP at once, and accepting personal liability, with no guarantee of listing. The underlying agreement is published in full.</p>'
      '<div class="g3" style="display:grid;grid-template-columns:repeat(5,1fr);gap:16px;">'
      '<a href="core5.html" data-h="border-color:#2a2930;" style="background:#0e0d12;border:1px solid #1c1b21;border-radius:14px;padding:24px;text-decoration:none;display:block;"><div style="font-family:\'Space Grotesk\',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;margin-bottom:6px;">Core 5.0 &mdash; the blockers &rarr;</div><div style="font-size:13.5px;color:#8b8a93;line-height:1.5;">The full, document-backed breakdown</div></a>'
      '<a href="agreement.html" data-h="border-color:#2a2930;" style="background:#0e0d12;border:1px solid #1c1b21;border-radius:14px;padding:24px;text-decoration:none;display:block;"><div style="font-family:\'Space Grotesk\',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;margin-bottom:6px;">Token Swap Agreement &rarr;</div><div style="font-size:13.5px;color:#8b8a93;line-height:1.5;">The Binance agreement, published in full</div></a>'
      '<a href="report.html" data-h="border-color:#2a2930;" style="background:#0e0d12;border:1px solid #1c1b21;border-radius:14px;padding:24px;text-decoration:none;display:block;"><div style="font-family:\'Space Grotesk\',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;margin-bottom:6px;">Community report &rarr;</div><div style="font-size:13.5px;color:#8b8a93;line-height:1.5;">The record + 82 screenshot exhibits</div></a>'
      '<a href="evidence.html" data-h="border-color:#2a2930;" style="background:#0e0d12;border:1px solid #1c1b21;border-radius:14px;padding:24px;text-decoration:none;display:block;"><div style="font-family:\'Space Grotesk\',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;margin-bottom:6px;">Evidence index &rarr;</div><div style="font-size:13.5px;color:#8b8a93;line-height:1.5;">All 82 exhibits, tallied by topic</div></a>'
      '<a href="faq.html" data-h="border-color:#2a2930;" style="background:#0e0d12;border:1px solid #1c1b21;border-radius:14px;padding:24px;text-decoration:none;display:block;"><div style="font-family:\'Space Grotesk\',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;margin-bottom:6px;">Read the FAQ &rarr;</div><div style="font-size:13.5px;color:#8b8a93;line-height:1.5;">Straight answers to common questions</div></a>'
      '</div></div></div>\n')
    body = body.replace("<!-- ===================== EXCHANGES ===================== -->",
                        band + "<!-- ===================== EXCHANGES ===================== -->")
    # remove dead placeholder cards (Discord / Community-X had no real URL) to avoid broken links
    body = re.sub(r'<a href="#"[^>]*>.*?</a>', '', body, flags=re.DOTALL)
    # repoint the (previously mis-linked) "community transparency report" button to the new report page
    body = body.replace(
        '<a href="archive.html" style="display:inline-flex;align-items:center;gap:8px;background:transparent;border:1px solid #1c1b21;color:#a9a8b0;font-size:14px;font-weight:500;text-decoration:none;padding:13px 20px;border-radius:9px;" data-h="border-color:#2a2930;color:#f4f3f6;">Read the community transparency report →</a>',
        '<a href="report.html" data-h="border-color:#2a2930;color:#f4f3f6;" style="display:inline-flex;align-items:center;gap:8px;background:transparent;border:1px solid #1c1b21;color:#a9a8b0;font-size:14px;font-weight:500;text-decoration:none;padding:13px 20px;border-radius:9px;">Read the community report &amp; 82 exhibits →</a>')
    return body

def live_spans(body):
    body = body.replace("{{ heightStr }}", '<span data-live="height">16,561,603</span>')
    body = body.replace("{{ lastBlockAgo }}", '<span data-live="ago">15</span>')
    body = body.replace("{{ supply }}", '<span data-live="supply">684</span>')
    body = body.replace("{{ blockTime }}", "8")
    body = body.replace("{{ producers }}", "53")
    body = body.replace("{{ burn }}", "90")
    return body

def accordion(body):
    for i in range(1, 6):
        body = body.replace(f'onClick="{{{{ toggle{i} }}}}"', f'data-acc="{i}"')
        disp = "block" if i == 5 else "none"
        body = body.replace(f"display:{{{{ d{i} }}}}", f"display:{disp}")
        rot = "45deg" if i == 5 else "0deg"
        body = body.replace(f"transform:rotate({{{{ r{i} }}}})", f"transform:rotate({rot})")
    return body

def wrap(title, desc, style, body, app_rel="app.js"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
{FAVICON}
{FONTS}
{style}
</head>
<body>
{body}
<script src="{app_rel}"></script>
</body>
</html>
"""

# ---------------- archive data (CORRECTED against research dossier) ----------------
POSTS = [
 ("governance-proposal-outcome","Governance Proposal Outcome","2026-01-30","2026","Governance",True,"The community governance vote SXP-GOV-2026-01 did not reach quorum. No further protocol development is planned, and Solar remains open for any credible organization to steward."),
 ("solar-governance-update-block-producer-proposal-initiation","Solar Governance Update: Block Producer Proposal Initiation","2026-01-26","2026","Governance",True,"Initiation of a non-binding, time-bound block-producer signaling proposal on an optional, voluntary path forward for the network."),
 ("solar-project-status-update","Solar Project Status Update","2026-01-26","2026","Status",True,"A full account of the project's status: no further protocol updates are planned, and prospective successor teams declined after due diligence."),
 ("resignation-statement-nayiem-w","Resignation Statement — Nayiem W.","2025-11-28","2025","Status",True,"The project's lead developer announces resignation, citing conditions that prevented further progress and confidentiality that limited transparency at the time."),
 ("solar-november-2025-update-3","Solar November 2025 — Update #3","2025-11-25","2025","Protocol",True,"November 2025 development update. Core 5.0 reached approximately 90% testnet completion."),
 ("solar-q1-2025-update-full-speed-ahead","Solar Q1 2025 Update: Full Speed Ahead","2025-03-28","2025","Status",False,"First-quarter 2025 progress across the protocol and consumer products."),
 ("brightervpn-is-here-the-crypto-first-vpn-has-arrived","BrighterVPN Is Here","2024-10-18","2024","Product",False,"A crypto-first VPN with SXP login and payments."),
 ("core-5-0-update-alpha-testing-performance-comparison","Core 5.0 — Alpha Testing & Performance Comparison","2024-06-09","2024","Protocol",False,"Core 5.0 alpha testing results and a performance comparison against the current stable Core 4.3.1 (~20x faster)."),
 ("introducing-solar-enterprises-brighter-blockchain-solutions","Introducing Solar Enterprises","2024-05-30","2024","Product",False,"Bringing Solar Card, tymt, District 53, and BrighterVPN together under the Solar Enterprises umbrella."),
 ("swap-portal-officially-closed","Swap Portal Officially Closed","2023-07-05","2023","Protocol",False,"The SXP mainnet swap portal is officially closed following the 1:1 token migration."),
 ("introducing-solar-card","Introducing Solar Card","2023-02-12","2023","Product",False,"A crypto debit card built around SXP, available across ~140 countries."),
 ("district-53","District 53 — Pre-launch Announcement","2022-08-14","2022","Product",False,"A metaverse game on Solar; 90% of land-sale proceeds burned."),
 ("release-update-solar-core-3-3-0-went-live","Solar Core 3.3.0 Went Live","2022-05-30","2022","Protocol",False,"Solar Core 3.3.0 — adds a 5% dev fund and BIP340 Schnorr signatures."),
 ("sxp-mainnet-launched","SXP Mainnet Launched","2022-03-28","2022","Protocol",False,"The Solar mainnet is live — a dPoS Layer-1 with 53 block producers and 8-second blocks."),
 ("get-ready-for-mainnet","Get Ready for Mainnet","2022-03-21","2022","Protocol",False,"Preparing for the Solar mainnet launch on 28 March 2022."),
]
TAGSTYLE = {
 "Governance": ("#f6a623","rgba(246,166,35,.08)","rgba(246,166,35,.25)"),
 "Protocol":   ("#cbb27e","rgba(203,178,126,.08)","rgba(203,178,126,.25)"),
 "Product":    ("#8fb8e8","rgba(143,184,232,.08)","rgba(143,184,232,.22)"),
 "Status":     ("#f76a6a","rgba(247,106,106,.08)","rgba(247,106,106,.25)"),
}

def build_archive_listing():
    # pills
    pills = []
    for i, name in enumerate(["All","Governance","Protocol","Product","Status"]):
        active = (name == "All")
        b = "#3a3942" if active else "#1c1b21"
        c = "#f4f3f6" if active else "#8b8a93"
        g = "rgba(255,255,255,.05)" if active else "transparent"
        pills.append(f'<span class="pill" data-tag="{name}" style="cursor:pointer;font-family:\'JetBrains Mono\',monospace;font-size:12px;padding:8px 14px;border-radius:8px;border:1px solid {b};color:{c};background:{g};">{name}</span>')
    controls = ('<div style="position:sticky;top:65px;z-index:40;background:rgba(10,10,13,.92);backdrop-filter:blur(8px);padding:24px 0 18px;margin-top:30px;">'
      '<input id="arcSearch" type="text" placeholder="Search the archive…" style="width:100%;background:#0e0d12;border:1px solid #1c1b21;border-radius:10px;padding:14px 16px;color:#f4f3f6;font-family:\'Manrope\',sans-serif;font-size:15px;outline:none;" />'
      '<div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap;">' + "".join(pills) + '</div></div>')
    # groups by year (preserve order of POSTS, descending years already)
    years = []
    for p in POSTS:
        slug,title,date,year,tag,snap,exc = p
        g = next((y for y in years if y[0]==year), None)
        if not g:
            g = (year, []); years.append(g)
        g[1].append(p)
    blocks = ['<div id="arcList">']
    for year, plist in years:
        cards = []
        for slug,title,date,year2,tag,snap,exc in plist:
            tc,tbg,tb = TAGSTYLE[tag]
            href = f"archive/{slug}.html" if snap else f"https://blog.solar.org/{slug}/"
            target = "" if snap else ' target="_blank" rel="noopener"'
            snapbadge = ('<span style="font-family:\'JetBrains Mono\',monospace;font-size:10px;letter-spacing:.04em;padding:4px 9px;border-radius:5px;color:#46d39a;background:rgba(70,211,154,.08);border:1px solid rgba(70,211,154,.25);">&#9670; SNAPSHOT</span>' if snap else
                         '<span style="font-family:\'JetBrains Mono\',monospace;font-size:10px;letter-spacing:.04em;padding:4px 9px;border-radius:5px;color:#5f5e66;border:1px solid #1c1b21;">live &#8599;</span>')
            txt = (title + " " + exc + " " + tag).lower().replace('"',"'")
            cards.append(
              f'<a class="arc-card" data-tag="{tag}" data-text="{html.escape(txt)}" href="{href}"{target} style="display:block;background:#0e0d12;border:1px solid #1c1b21;border-radius:13px;padding:22px 24px;text-decoration:none;margin-top:10px;" data-h="border-color:#2a2930;">'
              f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;flex-wrap:wrap;">'
              f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:10px;letter-spacing:.04em;padding:4px 9px;border-radius:5px;color:{tc};background:{tbg};border:1px solid {tb};">{tag}</span>'
              f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:12px;color:#5f5e66;">{date}</span>{snapbadge}</div>'
              f'<div style="font-family:\'Space Grotesk\',sans-serif;font-weight:600;font-size:18px;color:#f4f3f6;margin-bottom:8px;">{html.escape(title)}</div>'
              f'<div style="font-size:14px;line-height:1.6;color:#8b8a93;">{html.escape(exc)}</div></a>')
        blocks.append(
          f'<div class="arc-group" data-year="{year}" style="margin-top:14px;">'
          f'<div style="position:sticky;top:188px;z-index:30;display:flex;align-items:center;gap:14px;padding:10px 0;background:rgba(10,10,13,.92);backdrop-filter:blur(8px);">'
          f'<span style="font-family:\'Space Grotesk\',sans-serif;font-weight:700;font-size:22px;color:#f4f3f6;">{year}</span>'
          f'<div style="flex:1;height:1px;background:#1c1b21;"></div>'
          f'<span class="arc-count" style="font-family:\'JetBrains Mono\',monospace;font-size:12px;color:#5f5e66;">{len(plist)} posts</span></div>'
          + "".join(cards) + '</div>')
    blocks.append('<div id="arcEmpty" style="display:none;text-align:center;padding:60px 0;color:#5f5e66;font-size:15px;">No posts match your search.</div>')
    blocks.append('</div>')
    return controls + "\n" + "\n".join(blocks)

# ---------------- build main pages ----------------
PAGES = {
 "Solar.dc.html": ("index.html", "Solar — The Solar Foundation", "The Solar Foundation's transparent record of the Solar (SXP) dPoS blockchain — history, current status, governance, and how to take part."),
 "History.dc.html": ("history.html", "History & Transparency — Solar", "A sourced, public timeline of Swipe and Solar (SXP), from 2018 to 2026, with primary-source citations."),
 "Governance.dc.html": ("governance.html", "Governance — SXP-GOV-2026-01 — Solar", "The full record of Solar governance proposal SXP-GOV-2026-01, including the exact on-chain vote outcome."),
 "Status.dc.html": ("status.html", "Network Status — Solar", "The current operational status of the Solar (SXP) network — maintenance-only, with live chain metrics."),
 "Exchanges.dc.html": ("exchanges.html", "Where SXP Trades — Solar", "Where Solar (SXP) still trades, plus holder and exchange guidance. Informational only, not financial advice."),
 "Archive.dc.html": ("archive.html", "Blog Archive — Solar", "An archive of Solar's official announcements, with durable snapshots of the critical 2025-2026 posts."),
}

for srcname, (outname, title, desc) in PAGES.items():
    xdc = extract_xdc(read(srcname))
    style, body = split_helmet(xdc)
    body = common(body)
    if srcname == "Solar.dc.html":
        body = accordion(body)
        body = live_spans(body)
    elif srcname == "Status.dc.html":
        body = live_spans(body)
    elif srcname == "Archive.dc.html":
        body = live_spans(body)  # harmless
        listing = build_archive_listing()
        # replace region between '<!-- controls -->' and '<!-- source note -->'
        pre, _, rest = body.partition("<!-- controls -->")
        _, _, post = rest.partition("<!-- source note -->")
        body = pre + listing + "\n<!-- source note -->" + post
    with open(os.path.join(OUT, outname), "w", encoding="utf-8") as f:
        f.write(wrap(title, desc, style, body))
    print("wrote", outname, len(body), "b")

# ---------------- build snapshot pages ----------------
posts_full = json.load(open("/tmp/solar_snap/posts_full.json"))
SNAP_STYLE = """<style>
*{box-sizing:border-box;} html{scroll-behavior:smooth;} body{margin:0;background:#0a0a0d;}
::selection{background:rgba(255,150,90,.3);color:#fff;}
a{color:inherit;}
.post-body{font-family:'Manrope',sans-serif;}
.post-body p{font-size:16.5px;line-height:1.78;color:#bcbbc4;margin:0 0 18px;}
.post-body h2,.post-body h3,.post-body h4{font-family:'Space Grotesk',sans-serif;color:#f4f3f6;line-height:1.2;margin:34px 0 14px;letter-spacing:-.01em;}
.post-body h2{font-size:25px;} .post-body h3{font-size:20px;}
.post-body ul,.post-body ol{color:#bcbbc4;font-size:16px;line-height:1.7;padding-left:22px;margin:0 0 18px;}
.post-body li{margin:7px 0;}
.post-body a{color:#cbb27e;text-decoration:underline;}
.post-body strong{color:#e9e8ee;} .post-body blockquote{border-left:3px solid #2a2930;margin:0 0 18px;padding:4px 0 4px 18px;color:#9a99a2;}
.post-body hr{border:none;border-top:1px solid #1c1b21;margin:26px 0;}
@media (max-width:680px){.snap-h1{font-size:30px !important;}}
</style>"""

def snap_nav():
    return ('<div style="position:sticky;top:0;z-index:60;background:rgba(10,10,13,.82);backdrop-filter:blur(12px);border-bottom:1px solid #1c1b21;">'
      '<div style="max-width:820px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:16px 28px;gap:14px;">'
      '<a href="../index.html" style="display:flex;align-items:center;gap:11px;text-decoration:none;">'
      '<img src="https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png" alt="Solar" style="width:26px;height:26px;border-radius:6px;" />'
      '<span style="font-family:\'Space Grotesk\',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;">Solar</span>'
      '<span style="font-family:\'JetBrains Mono\',monospace;font-size:10px;color:#5f5e66;border:1px solid #1c1b21;border-radius:4px;padding:2px 7px;letter-spacing:.06em;">FOUNDATION</span></a>'
      '<a href="../archive.html" data-h="color:#f4f3f6;" style="font-size:14px;color:#a9a8b0;text-decoration:none;">&#8592; Back to archive</a>'
      '</div></div>')

for slug,title,date,year,tag,snap,exc in POSTS:
    if not snap: continue
    pf = posts_full.get(slug)
    if not pf:
        print("WARN no full body for", slug); continue
    tc,tbg,tb = TAGSTYLE[tag]
    body_html = pf["body"]
    orig = f"https://blog.solar.org/{slug}/"
    page_body = f"""<div style="background:#0a0a0d;font-family:'Manrope',sans-serif;color:#f4f3f6;min-height:100vh;">
{snap_nav()}
<div style="max-width:820px;margin:0 auto;padding:44px 28px 80px;">
  <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5f5e66;margin-bottom:22px;"><a href="../index.html" style="color:#5f5e66;text-decoration:none;">solar.org</a> / <a href="../archive.html" style="color:#5f5e66;text-decoration:none;">archive</a> / <span style="color:#a9a8b0;">{slug}</span></div>
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:18px;flex-wrap:wrap;">
    <span style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.04em;padding:4px 9px;border-radius:5px;color:{tc};background:{tbg};border:1px solid {tb};">{tag}</span>
    <span style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5f5e66;">{date}</span>
    <span style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.04em;padding:4px 9px;border-radius:5px;color:#46d39a;background:rgba(70,211,154,.08);border:1px solid rgba(70,211,154,.25);">&#9670; SNAPSHOT</span>
  </div>
  <h1 class="snap-h1" style="font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:38px;line-height:1.08;letter-spacing:-.025em;color:#f4f3f6;margin:0 0 22px;">{html.escape(title)}</h1>
  <div style="background:#0c0b10;border:1px solid #1c1b21;border-radius:12px;padding:16px 20px;margin-bottom:30px;font-size:13.5px;line-height:1.6;color:#8b8a93;">
    <span style="color:#46d39a;">&#9670; Archived snapshot</span> held by The Solar Foundation for durability. Originally published {date} on blog.solar.org. <a href="{orig}" target="_blank" rel="noopener" style="color:#cbb27e;text-decoration:underline;">View original &#8599;</a>
  </div>
  <div class="post-body">
  {body_html}
  </div>
  <div style="border-top:1px solid #1c1b21;margin-top:46px;padding-top:22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;font-size:13px;color:#5f5e66;">
    <span>&copy; The Solar Foundation &middot; archived for transparency</span>
    <a href="../archive.html" data-h="color:#f4f3f6;" style="color:#a9a8b0;text-decoration:none;">All archived posts &#8594;</a>
  </div>
</div>
</div>"""
    with open(os.path.join(OUT, "archive", f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(wrap(f"{title} — Solar Archive", exc, SNAP_STYLE, page_body, app_rel="../app.js"))
    print("wrote archive/"+slug+".html", len(body_html), "b")

print("DONE")
