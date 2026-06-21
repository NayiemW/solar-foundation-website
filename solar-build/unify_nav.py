#!/usr/bin/env python3
import os
SITE = "/home/blackwell/workspace/monolythium-ecosystem/solar-site"
FAV = "https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png"

NAV_CSS = """
<style>/*navcss*/
.snav{position:sticky;top:0;z-index:100;background:rgba(10,10,13,.85);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid #1c1b21;}
.snav-in{max-width:1240px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:14px;padding:13px 28px;}
.snav-logo{display:flex;align-items:center;gap:11px;text-decoration:none;flex:none;}
.snav-menu{display:flex;align-items:center;gap:4px;}
.snav-menu>a,.snav-ddbtn{font-family:'Manrope',sans-serif;font-size:14px;color:#a9a8b0;text-decoration:none;background:none;border:none;cursor:pointer;padding:8px 12px;border-radius:8px;display:inline-flex;align-items:center;gap:6px;line-height:1;}
.snav-menu>a:hover,.snav-ddbtn:hover{color:#f4f3f6;background:rgba(255,255,255,.05);}
.snav-dd{position:relative;}
.snav-ddmenu{position:absolute;top:calc(100% + 8px);left:0;min-width:248px;background:#0e0d12;border:1px solid #232228;border-radius:12px;padding:7px;box-shadow:0 24px 60px rgba(0,0,0,.55);display:none;flex-direction:column;gap:1px;z-index:130;}
.snav-dd:hover .snav-ddmenu,.snav-dd.open .snav-ddmenu{display:flex;}
.snav-ddmenu a{font-family:'Manrope',sans-serif;font-size:13.5px;color:#bcbbc4;text-decoration:none;padding:10px 12px;border-radius:8px;white-space:nowrap;display:flex;flex-direction:column;gap:2px;}
.snav-ddmenu a:hover{background:rgba(255,255,255,.05);color:#f4f3f6;}
.snav-ddmenu a small{color:#5f5e66;font-size:11.5px;}
.snav-cta{flex:none;font-family:'Manrope',sans-serif;font-size:14px;color:#f4f3f6;text-decoration:none;border:1px solid #2a2930;border-radius:8px;padding:8px 15px;}
.snav-cta:hover{border-color:#3a3942;background:rgba(255,255,255,.04);}
.snav-tg{display:none;background:none;border:1px solid #2a2930;border-radius:8px;color:#f4f3f6;font-size:17px;line-height:1;padding:7px 12px;cursor:pointer;}
.snav-caret{font-size:9px;opacity:.65;}
@media (max-width:880px){
  .snav-tg{display:block;}
  .snav-cta{display:none;}
  .snav-menu{display:none;position:absolute;top:100%;left:0;right:0;background:#0b0a0e;border-bottom:1px solid #1c1b21;flex-direction:column;align-items:stretch;gap:0;padding:8px 16px 18px;max-height:82vh;overflow:auto;}
  .snav.open .snav-menu{display:flex;}
  .snav-menu>a{padding:13px 8px;border-bottom:1px solid #15141a;}
  .snav-ddbtn{width:100%;justify-content:space-between;padding:14px 8px 6px;color:#f6a623;font-size:12px;letter-spacing:.06em;text-transform:uppercase;}
  .snav-ddmenu{position:static;display:flex;box-shadow:none;border:none;background:transparent;padding:0 0 8px 6px;min-width:0;}
  .snav-caret{display:none;}
}
</style>
"""

NAV_HTML = """<header class="snav">
  <div class="snav-in">
    <a class="snav-logo" href="/"><img src="__FAV__" alt="Solar" style="width:26px;height:26px;border-radius:6px;" /><span style="font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;">Solar</span><span style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#5f5e66;border:1px solid #1c1b21;border-radius:4px;padding:2px 7px;letter-spacing:.06em;">FOUNDATION</span></a>
    <button class="snav-tg" aria-label="Toggle menu">&#9776;</button>
    <nav class="snav-menu">
      <a href="/status">Status</a>
      <div class="snav-dd">
        <button class="snav-ddbtn" type="button">Transparency <span class="snav-caret">&#9660;</span></button>
        <div class="snav-ddmenu">
          <a href="/history">History &amp; timeline<small>Full sourced chronology, 2018&ndash;2026</small></a>
          <a href="/core5">Core 5.0 &mdash; the blockers<small>Why the upgrade could never ship</small></a>
          <a href="/agreement">Token Swap Agreement<small>The Binance agreement, full text</small></a>
          <a href="/report">Community report<small>The record + 82 screenshot exhibits</small></a>
          <a href="/evidence">Evidence index<small>All 82 exhibits, tallied by topic</small></a>
          <a href="/archive">Blog archive<small>Snapshots of official posts</small></a>
        </div>
      </div>
      <div class="snav-dd">
        <button class="snav-ddbtn" type="button">Network <span class="snav-caret">&#9660;</span></button>
        <div class="snav-ddmenu">
          <a href="/governance">Governance<small>SXP-GOV-2026-01 vote record</small></a>
          <a href="/exchanges">Where SXP trades<small>Remaining venues + guidance</small></a>
          <a href="https://solarscan.com" target="_blank" rel="noopener">Block explorer &#8599;<small>Solarscan</small></a>
          <a href="https://github.com/Solar-network" target="_blank" rel="noopener">GitHub &#8599;<small>Open-source core</small></a>
          <a href="mailto:hello@solar.org">Contact<small>hello@solar.org</small></a>
        </div>
      </div>
      <a href="/faq">FAQ</a>
    </nav>
    <a class="snav-cta" href="https://solarscan.com" target="_blank" rel="noopener">Open Explorer</a>
  </div>
</header>""".replace("__FAV__", FAV)

def find_nav_block(s):
    start = s.find('<div style="position:sticky;top:0;')
    if start == -1: return None, None
    i = start; depth = 0; end = None
    while i < len(s):
        if s.startswith('<div', i):
            depth += 1; i += 4; continue
        if s.startswith('</div>', i):
            depth -= 1; i += 6
            if depth == 0: end = i; break
            continue
        i += 1
    return start, end

files = []
for root,_,fs in os.walk(SITE):
    for f in fs:
        if f.endswith(".html"):
            files.append(os.path.join(root,f))
files.sort()

done=0; skipped=[]
for p in files:
    s = open(p, encoding="utf-8").read()
    changed=False
    if '/*navcss*/' not in s:
        s = s.replace("</head>", NAV_CSS + "</head>", 1); changed=True
    if 'class="snav-in"' not in s:
        start,end = find_nav_block(s)
        if start is not None and end is not None:
            s = s[:start] + NAV_HTML + s[end:]; changed=True
        else:
            skipped.append(os.path.relpath(p,SITE))
    if changed:
        open(p,"w",encoding="utf-8").write(s); done+=1

print(f"unified nav on {done} files")
if skipped: print("NO nav block found (left as-is):", skipped)
