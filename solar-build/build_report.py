#!/usr/bin/env python3
import json, os, shutil, html, re

SRCDOCX_DIR = "/tmp/solar_docx/extracted/word"
OUT = "/home/blackwell/workspace/monolythium-ecosystem/solar-site"
ASSETS = os.path.join(OUT, "report-assets")
os.makedirs(ASSETS, exist_ok=True)

labeled = json.load(open("/tmp/solar_docx/exhibit_map.json"))   # [[ "A-001", "media/imageNN.jpg"], ...]
narr = json.load(open("/tmp/solar_docx/narrative.json"))

# copy original docx for download
shutil.copy("/home/blackwell/workspace/monolythium-ecosystem/solar-community-report (2).docx",
            os.path.join(OUT, "solar-community-report.docx"))

# copy exhibit images -> A-001.ext
exhibits = []
for label, target in labeled:
    src = os.path.join(SRCDOCX_DIR, target)
    ext = os.path.splitext(target)[1] or ".jpg"
    dest_name = f"{label}{ext}"
    shutil.copy(src, os.path.join(ASSETS, dest_name))
    exhibits.append((label, f"report-assets/{dest_name}"))

# ---- narrative formatting ----
HEAD2 = {
 "Disclaimer","Background Context: Binance (Pre-2023 and After)",
 "Open Letter to the Solar (SXP) Community","What Occurred (High-Level Overview)",
 "Key Issues Raised by Solar Leadership (Contextual Summary)",
 "Potential Legal and Regulatory Considerations (Contextual)",
 "Included and Excluded Materials","How to Read This Record",
 "Selected Findings (Illustrative Examples)","March 2023 Draft Agreement (Document D2)",
 "Closing Note",
}
HEAD3 = {
 "Solar Card / Ticker Constraints","Card Processing Fees","Treasury Custody and Listing Risk",
 "Messaging Coordination","BEP2 / BEP20 Infrastructure",
}

def esc(s): return html.escape(s)

parts = []
title = narr[0]
subtitle = narr[1] if len(narr) > 1 else ""
i = 2
# stop prose at the timeline table
STOP = "Chronological timeline (selected events)"
while i < len(narr):
    line = narr[i]
    if line.startswith(STOP) or line.startswith("Date") and i>3 and narr[i-1].startswith("My last response"):
        break
    if line.startswith(STOP):
        break
    if line in HEAD2:
        parts.append(f'<h2>{esc(line)}</h2>')
    elif line in HEAD3:
        parts.append(f'<h3>{esc(line)}</h3>')
    elif line in ("Included:","Excluded:"):
        parts.append(f'<p style="margin-bottom:4px;"><strong style="color:#e9e8ee;">{esc(line)}</strong></p>')
    elif line.startswith("My last response to Binance"):
        parts.append(f'<h2>{esc(line)}</h2>')
    else:
        parts.append(f'<p>{esc(line)}</p>')
    i += 1
prose = "\n".join(parts)

# exhibit gallery
gal = []
for label, path in exhibits:
    gal.append(
      f'<figure id="{label}" style="margin:0 0 22px;background:#0e0d12;border:1px solid #1c1b21;border-radius:12px;overflow:hidden;">'
      f'<figcaption style="display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid #1c1b21;font-family:\'JetBrains Mono\',monospace;font-size:12px;color:#a9a8b0;">'
      f'<span style="color:#f6a623;">Exhibit {label}</span><span style="color:#5f5e66;">Binance Proof &middot; screenshot</span></figcaption>'
      f'<a href="{path}" target="_blank" rel="noopener"><img loading="lazy" src="{path}" alt="Exhibit {label}" style="width:100%;display:block;background:#fff;" /></a>'
      f'</figure>')
gallery = "\n".join(gal)

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Community Report &amp; Evidence — Solar (SXP)</title>
<meta name="description" content="The Solar (SXP) community transparency report (2020-2023) with 82 screenshot exhibits documenting communications about mainnet support, the treasury, and card processing fees.">
<meta property="og:title" content="Community Report &amp; Evidence — Solar (SXP)">
<meta property="og:description" content="The transparency record with 82 screenshot exhibits.">
<link rel="icon" href="https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;}} html{{scroll-behavior:smooth;}} body{{margin:0;background:#0a0a0d;}}
  ::selection{{background:rgba(255,150,90,.3);color:#fff;}}
  a{{color:inherit;}}
  .rep{{font-family:'Manrope',sans-serif;}}
  .rep h2{{font-family:'Space Grotesk',sans-serif;color:#f4f3f6;font-size:23px;letter-spacing:-.01em;margin:36px 0 10px;}}
  .rep h3{{font-family:'Space Grotesk',sans-serif;color:#f4f3f6;font-size:18px;margin:24px 0 6px;}}
  .rep p{{font-size:15.5px;line-height:1.76;color:#bcbbc4;margin:0 0 14px;}}
  @media (max-width:680px){{.rep-h1{{font-size:32px !important;}} .nums{{grid-template-columns:1fr 1fr !important;}}}}
</style>
</head>
<body>
<div style="background:#0a0a0d;font-family:'Manrope',sans-serif;color:#f4f3f6;min-height:100vh;">

  <!-- NAV -->
  <div style="position:sticky;top:0;z-index:60;background:rgba(10,10,13,.82);backdrop-filter:blur(12px);border-bottom:1px solid #1c1b21;">
    <div style="max-width:900px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:16px 28px;gap:14px;">
      <a href="index.html" style="display:flex;align-items:center;gap:11px;text-decoration:none;">
        <img src="https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png" alt="Solar" style="width:26px;height:26px;border-radius:6px;" />
        <span style="font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;">Solar</span>
        <span style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#5f5e66;border:1px solid #1c1b21;border-radius:4px;padding:2px 7px;letter-spacing:.06em;">FOUNDATION</span>
      </a>
      <div style="display:flex;gap:20px;font-size:14px;color:#a9a8b0;">
        <a href="core5.html" data-h="color:#f4f3f6;" style="text-decoration:none;">Core 5.0</a>
        <a href="agreement.html" data-h="color:#f4f3f6;" style="text-decoration:none;">Agreement</a>
        <a href="faq.html" data-h="color:#f4f3f6;" style="text-decoration:none;">FAQ</a>
      </div>
    </div>
  </div>

  <div style="max-width:900px;margin:0 auto;padding:48px 28px 90px;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5f5e66;margin-bottom:20px;"><a href="index.html" style="color:#5f5e66;text-decoration:none;">solar.org</a> / <a href="history.html" style="color:#5f5e66;text-decoration:none;">record</a> / <span style="color:#a9a8b0;">community report</span></div>

    <h1 class="rep-h1" style="font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:42px;line-height:1.06;letter-spacing:-.025em;margin:0 0 8px;">{esc(title)}</h1>
    <p style="font-size:17px;color:#9a99a2;margin:0 0 24px;">{esc(subtitle)}</p>

    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:30px;">
      <a href="solar-community-report.docx" download data-h="filter:brightness(1.06);" style="display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,#ffc24a,#ff6a5e);color:#1a0d05;font-weight:600;font-size:14px;text-decoration:none;padding:12px 20px;border-radius:8px;">&#8595; Download the full report (.docx)</a>
      <a href="#exhibits" data-h="border-color:#3a3942;" style="display:inline-flex;align-items:center;gap:8px;background:transparent;color:#f4f3f6;font-weight:500;font-size:14px;text-decoration:none;padding:12px 20px;border-radius:8px;border:1px solid #2a2930;">Jump to the 82 exhibits &#8595;</a>
      <a href="evidence.html" data-h="border-color:#3a3942;" style="display:inline-flex;align-items:center;gap:8px;background:transparent;color:#f4f3f6;font-weight:500;font-size:14px;text-decoration:none;padding:12px 20px;border-radius:8px;border:1px solid #2a2930;">Evidence index (topic tally) &#8594;</a>
    </div>

    <!-- by the numbers -->
    <div class="nums" style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:14px;">
      <div style="background:#0e0d12;border:1px solid #1c1b21;border-radius:12px;padding:18px;"><div style="font-family:'JetBrains Mono',monospace;font-size:26px;color:#f4f3f6;font-weight:600;">82</div><div style="font-size:11.5px;color:#5f5e66;margin-top:4px;">screenshot exhibits</div></div>
      <div style="background:#0e0d12;border:1px solid #1c1b21;border-radius:12px;padding:18px;"><div style="font-family:'JetBrains Mono',monospace;font-size:26px;color:#f4f3f6;font-weight:600;">10</div><div style="font-size:11.5px;color:#5f5e66;margin-top:4px;">exhibits on card fees</div></div>
      <div style="background:#0e0d12;border:1px solid #1c1b21;border-radius:12px;padding:18px;"><div style="font-family:'JetBrains Mono',monospace;font-size:26px;color:#f4f3f6;font-weight:600;">2020&ndash;23</div><div style="font-size:11.5px;color:#5f5e66;margin-top:4px;">period documented</div></div>
      <div style="background:#0e0d12;border:1px solid #1c1b21;border-radius:12px;padding:18px;"><div style="font-family:'JetBrains Mono',monospace;font-size:26px;color:#f4f3f6;font-weight:600;">1</div><div style="font-size:11.5px;color:#5f5e66;margin-top:4px;">priority, every time</div></div>
    </div>

    <!-- the pattern we observed (Foundation account) -->
    <div style="background:#0c0b10;border:1px solid #1c1b21;border-radius:14px;padding:26px;margin:18px 0 30px;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;flex-wrap:wrap;"><span style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#f6a623;letter-spacing:.1em;">THE PATTERN WE OBSERVED</span><span style="font-family:'JetBrains Mono',monospace;font-size:9px;color:#8b8a93;background:rgba(255,255,255,.03);border:1px solid #2a2930;border-radius:5px;padding:3px 7px;">FOUNDATION STATEMENT</span></div>
      <p style="font-size:15px;line-height:1.74;color:#bcbbc4;margin:0 0 12px;">Across the communications compiled here, the Foundation repeatedly sought clarity on three things: <strong style="color:#f4f3f6;">whether mainnet would be supported</strong>, <strong style="color:#f4f3f6;">how the treasury would be handled</strong>, and <strong style="color:#f4f3f6;">whether SXP could be used for card processing fees</strong>. Card processing fees alone recur across ten exhibits (A-002, A-003, A-004, A-008, A-009, A-020, A-027, A-030, A-031, A-033).</p>
      <p style="font-size:15px;line-height:1.74;color:#bcbbc4;margin:0 0 12px;">In the Foundation&rsquo;s assessment of that record: questions about the project, the community, and later Core 5.0 went largely unanswered &mdash; while one subject was returned to consistently: the treasury. A public announcement describing the project as &ldquo;decentralised / community-driven&rdquo; was sought as a condition tied to mainnet support (Exhibit A-037), and concrete support for the mainnet listing appeared to materialise only after the Foundation signalled it would wind down swap support &mdash; at which point the remaining treasury was at stake.</p>
      <p style="font-size:15px;line-height:1.74;color:#bcbbc4;margin:0;">That leads to the concern at the heart of this record: once the entire treasury has been transferred, there is little remaining incentive to keep SXP listed or supported &mdash; the tokens could simply be sold. This is the Foundation&rsquo;s interpretation of the documents below; readers can review the exhibits and form their own view. The other parties have not responded publicly.</p>
    </div>

    <!-- on-chain supply (verifiable) -->
    <div style="background:#0e0d12;border:1px solid #1c1b21;border-radius:14px;padding:24px 26px;margin:0 0 30px;">
      <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#46d39a;letter-spacing:.1em;margin-bottom:12px;">ON-CHAIN SUPPLY &mdash; VERIFIABLE</div>
      <p style="font-size:14.5px;line-height:1.7;color:#bcbbc4;margin:0 0 10px;">SXP began as one ERC-20 with a <strong style="color:#f4f3f6;">300M</strong> hard cap. Today parallel supplies exist across chains: Ethereum ~<strong style="color:#f4f3f6;">285.4M</strong>, a separate &ldquo;Binance-Peg&rdquo; BSC BEP-20 ~<strong style="color:#f4f3f6;">289.7M</strong> (supply hard-coded, no mint function, deployed 5&nbsp;Oct&nbsp;2020 &mdash; after the July 2020 acquisition), and native Solar ~<strong style="color:#f4f3f6;">684M</strong>. The migration was <strong style="color:#f4f3f6;">lock-based, not burn-based</strong>, so ~<strong style="color:#f4f3f6;">575M</strong> SXP still exists on Ethereum + BSC alongside the native supply &mdash; despite the official &ldquo;480M, 1:1, supply not increased&rdquo; line. The <em>existence</em> of this parallel supply is verifiable; attributing it to a deliberate act is the Foundation&rsquo;s position (Binance has not responded).</p>
      <p style="font-size:13px;color:#8b8a93;margin:0;">Verify: <a href="https://etherscan.io/token/0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9" target="_blank" rel="noopener" style="color:#cbb27e;">Etherscan</a> &middot; <a href="https://bscscan.com/token/0x47bead2563dcbf3bf2c9407fea4dc236faba485a" target="_blank" rel="noopener" style="color:#cbb27e;">BscScan</a> &middot; <a href="https://api.solar.org/api/blockchain" target="_blank" rel="noopener" style="color:#cbb27e;">api.solar.org</a> &middot; full breakdown in the <a href="faq.html" style="color:#cbb27e;">FAQ</a>.</p>
    </div>

    <!-- narrative -->
    <div class="rep">
      {prose}
      <h2>Chronological timeline</h2>
      <p>The full chronology of events (2018&ndash;2026), with primary-source citations, is maintained on the <a href="history.html" style="color:#cbb27e;text-decoration:underline;">History &amp; Transparency</a> page. The selected timeline in the original document is included in the downloadable report above.</p>
    </div>

    <!-- exhibits -->
    <div id="exhibits" style="margin-top:46px;scroll-margin-top:70px;">
      <h2 style="font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:28px;letter-spacing:-.02em;margin:0 0 6px;">Appendix A &mdash; Screenshot exhibits</h2>
      <p style="font-size:14.5px;line-height:1.7;color:#9a99a2;margin:0 0 8px;">82 screenshots compiled from the communications (&ldquo;Binance Proof&rdquo;). Click any exhibit to open it full-size. Raw chat exports are excluded; these are the screenshots referenced throughout the report.</p>
      <div style="background:#0c0b10;border:1px solid #1c1b21;border-radius:10px;padding:12px 16px;margin-bottom:24px;font-size:12.5px;line-height:1.6;color:#8b8a93;">These materials are published by The Solar Foundation for transparency. They are presented as compiled; the Foundation makes no representation beyond what each image shows, and nothing here is an accusation of wrongdoing by any party.</div>
      {gallery}
    </div>

    <div style="border-top:1px solid #1c1b21;margin-top:40px;padding-top:22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;font-size:13px;color:#5f5e66;">
      <span>&copy; The Solar Foundation &middot; published for transparency</span>
      <a href="index.html" data-h="color:#f4f3f6;" style="color:#a9a8b0;text-decoration:none;">&#8592; Home</a>
    </div>
  </div>
</div>
<script src="app.js"></script>
</body>
</html>
"""

with open(os.path.join(OUT, "report.html"), "w", encoding="utf-8") as f:
    f.write(PAGE)
print("wrote report.html | exhibits:", len(exhibits), "| prose parts:", len(parts))
print("assets:", len(os.listdir(ASSETS)), "files;", round(sum(os.path.getsize(os.path.join(ASSETS,x)) for x in os.listdir(ASSETS))/1e6,1), "MB")
print("docx copied:", os.path.exists(os.path.join(OUT,"solar-community-report.docx")))
