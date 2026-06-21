#!/usr/bin/env python3
import json, html, os
OUT = "/home/blackwell/workspace/monolythium-ecosystem/solar-site"
ex = json.load(open("/tmp/evidence.json"))
ex = sorted(ex, key=lambda e: e["id"])

TOPICS = [
 ("mainnet-support","Mainnet support","#f6a623"),
 ("treasury","Treasury","#f76a6a"),
 ("supply","Supply","#8fb8e8"),
 ("agreement-liability","Agreement / liability","#c9a0ff"),
 ("independent-messaging","“Independent” messaging","#46d39a"),
 ("listing-risk","Listing / delisting risk","#ff8c6a"),
 ("card-fees","Card fees","#e8c468"),
 ("timelock","Timelock","#6ad4d4"),
 ("ticker-ip","Ticker / IP","#d49a6a"),
 ("other","Other","#8b8a93"),
]
COLOR = {k:c for k,_,c in TOPICS}
LABEL = {k:l for k,l,_ in TOPICS}
counts = {k:0 for k,_,_ in TOPICS}
for e in ex:
    for t in e.get("topics",[]):
        if t in counts: counts[t]+=1
total = len(ex)
maxc = max(counts.values()) or 1

def esc(s): return html.escape(s or "")

# tally bars
bars=[]
for k,l,c in sorted(TOPICS, key=lambda x:-counts[x[0]]):
    n=counts[k]; w=round(100*n/maxc)
    bars.append(
      f'<div style="display:flex;align-items:center;gap:14px;margin:0 0 10px;">'
      f'<div style="flex:none;width:170px;font-size:13.5px;color:#bcbbc4;text-align:right;">{esc(l)}</div>'
      f'<div style="flex:1;background:#0c0b10;border:1px solid #1c1b21;border-radius:6px;height:24px;overflow:hidden;"><div style="width:{w}%;height:100%;background:{c};opacity:.75;"></div></div>'
      f'<div style="flex:none;width:64px;font-family:\'JetBrains Mono\',monospace;font-size:14px;color:#f4f3f6;">{n}<span style="color:#5f5e66;font-size:11px;">/{total}</span></div>'
      f'</div>')
bars_html="\n".join(bars)

# filter pills
pills=['<span class="epill" data-t="all" style="cursor:pointer;font-family:\'JetBrains Mono\',monospace;font-size:12px;padding:7px 13px;border-radius:8px;border:1px solid #3a3942;color:#f4f3f6;background:rgba(255,255,255,.05);">All ('+str(total)+')</span>']
for k,l,c in sorted(TOPICS, key=lambda x:-counts[x[0]]):
    if counts[k]==0: continue
    pills.append(f'<span class="epill" data-t="{k}" style="cursor:pointer;font-family:\'JetBrains Mono\',monospace;font-size:12px;padding:7px 13px;border-radius:8px;border:1px solid #1c1b21;color:{c};background:transparent;">{esc(l)} ({counts[k]})</span>')
pills_html="\n".join(pills)

# rows
rows=[]
for e in ex:
    tid=e["id"]; date=e.get("date",""); who=e.get("who_raised","unclear")
    tags=e.get("topics",[]); summ=e.get("summary",""); quote=e.get("quote","")
    whoC={"binance":"#f76a6a","solar":"#46d39a","unclear":"#8b8a93"}.get(who,"#8b8a93")
    whoL={"binance":"Binance","solar":"Solar","unclear":"—"}.get(who,who)
    tagspans="".join(f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:9.5px;letter-spacing:.03em;padding:3px 7px;border-radius:5px;color:{COLOR.get(t,"#8b8a93")};background:{COLOR.get(t,"#888")}14;border:1px solid {COLOR.get(t,"#8b8a93")}55;">{esc(LABEL.get(t,t))}</span>' for t in tags)
    dtxt=(" ".join([tid,date,summ,quote," ".join(LABEL.get(t,t) for t in tags)])).lower().replace('"',"'")
    img=f"report-assets/{tid}.jpg"
    quote_html=f'<div style="font-size:13px;line-height:1.55;color:#9a99a2;font-style:italic;border-left:2px solid #2a2930;padding-left:12px;margin-top:10px;">“{esc(quote)}”</div>' if quote else ""
    rows.append(
      f'<div class="erow" data-topics="{" ".join(tags)}" data-text="{esc(dtxt)}" style="background:#0e0d12;border:1px solid #1c1b21;border-radius:12px;padding:18px 20px;margin:0 0 10px;">'
      f'<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:9px;">'
      f'<a href="{img}" target="_blank" rel="noopener" style="font-family:\'JetBrains Mono\',monospace;font-size:12px;color:#f6a623;text-decoration:none;border:1px solid #2a2930;border-radius:5px;padding:3px 8px;" data-h="border-color:#f6a623;">{tid} ↗</a>'
      + (f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:11px;color:#5f5e66;">{esc(date)}</span>' if date else '')
      + f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:10px;color:{whoC};border:1px solid {whoC}55;border-radius:5px;padding:2px 7px;">{whoL}</span>'
      f'<span style="flex:1;"></span>{tagspans}</div>'
      f'<div style="font-size:14.5px;line-height:1.6;color:#c5c4cc;">{esc(summ)}</div>'
      f'{quote_html}'
      f'<button class="ev-shot" data-img="{img}" data-h="border-color:#3a3942;color:#f4f3f6;" style="margin-top:13px;font-family:\'JetBrains Mono\',monospace;font-size:11.5px;color:#a9a8b0;background:none;border:1px solid #2a2930;border-radius:7px;padding:6px 12px;cursor:pointer;">View screenshot &#9660;</button>'
      f'<div class="ev-shotbox" style="display:none;margin-top:10px;"></div>'
      f'</div>')
rows_html="\n".join(rows)

PAGE=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Evidence Index — 82 Exhibits — Solar (SXP)</title>
<meta name="description" content="A searchable index of all 82 Binance–Solar communication exhibits, classified by topic. Mainnet support was raised in 68 of 82; the treasury in 43; card fees in 18.">
<meta property="og:title" content="Evidence Index — 82 Exhibits — Solar (SXP)">
<meta property="og:description" content="All 82 exhibits classified by topic, searchable. Mainnet support raised in 68; treasury 43; card fees 18.">
<link rel="icon" href="https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;}} html{{scroll-behavior:smooth;}} body{{margin:0;background:#0a0a0d;}}
  ::selection{{background:rgba(255,150,90,.3);color:#fff;}}
  a{{color:inherit;}} input::placeholder{{color:#5f5e66;}}
  @media (max-width:680px){{.ev-h1{{font-size:32px !important;}} .tallyrow div:first-child{{width:120px !important;}}}}
</style>
</head>
<body>
<div style="background:#0a0a0d;font-family:'Manrope',sans-serif;color:#f4f3f6;min-height:100vh;">
  <div style="position:sticky;top:0;z-index:60;background:rgba(10,10,13,.82);backdrop-filter:blur(12px);border-bottom:1px solid #1c1b21;">
    <div style="max-width:960px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:16px 28px;gap:14px;">
      <a href="index.html" style="display:flex;align-items:center;gap:11px;text-decoration:none;">
        <img src="https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png" alt="Solar" style="width:26px;height:26px;border-radius:6px;" />
        <span style="font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:17px;color:#f4f3f6;">Solar</span>
        <span style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#5f5e66;border:1px solid #1c1b21;border-radius:4px;padding:2px 7px;letter-spacing:.06em;">FOUNDATION</span>
      </a>
      <div style="display:flex;gap:20px;font-size:14px;color:#a9a8b0;">
        <a href="report.html" data-h="color:#f4f3f6;" style="text-decoration:none;">Report</a>
        <a href="core5.html" data-h="color:#f4f3f6;" style="text-decoration:none;">Core 5.0</a>
        <a href="faq.html" data-h="color:#f4f3f6;" style="text-decoration:none;">FAQ</a>
      </div>
    </div>
  </div>

  <div style="max-width:960px;margin:0 auto;padding:48px 28px 90px;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5f5e66;margin-bottom:20px;"><a href="report.html" style="color:#5f5e66;text-decoration:none;">report</a> / <span style="color:#a9a8b0;">evidence index</span></div>
    <h1 class="ev-h1" style="font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:44px;line-height:1.05;letter-spacing:-.025em;margin:0 0 16px;">Evidence index.</h1>
    <p style="font-size:17px;line-height:1.7;color:#9a99a2;max-width:760px;margin:0 0 8px;">Every one of the <strong style="color:#f4f3f6;">{total}</strong> exhibits in the <a href="report.html" style="color:#cbb27e;text-decoration:underline;">community report</a>, read and classified by topic. The pattern is in the counts: <strong style="color:#f4f3f6;">mainnet support</strong> was raised in <strong style="color:#f4f3f6;">{counts['mainnet-support']}</strong> of {total} exhibits, the <strong style="color:#f4f3f6;">treasury</strong> in <strong style="color:#f4f3f6;">{counts['treasury']}</strong>, and <strong style="color:#f4f3f6;">card fees</strong> in <strong style="color:#f4f3f6;">{counts['card-fees']}</strong>. Each row links to the original screenshot.</p>
    <p style="font-size:12.5px;color:#5f5e66;margin:0 0 26px;">Classification was produced by automated reading of the screenshots; topics are interpretive aids, the linked images are the primary record. An exhibit can carry several topics.</p>

    <!-- tally -->
    <div style="background:#0c0b10;border:1px solid #1c1b21;border-radius:14px;padding:24px 26px;margin-bottom:28px;" class="tallyrow">
      <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#f6a623;letter-spacing:.1em;margin-bottom:16px;">TOPICS RAISED &mdash; ACROSS {total} EXHIBITS</div>
      {bars_html}
    </div>

    <!-- controls -->
    <div style="position:sticky;top:65px;z-index:40;background:rgba(10,10,13,.92);backdrop-filter:blur(8px);padding:18px 0;">
      <input id="evSearch" type="text" placeholder="Search exhibits (text, quotes, dates)…" style="width:100%;background:#0e0d12;border:1px solid #1c1b21;border-radius:10px;padding:13px 16px;color:#f4f3f6;font-family:'Manrope',sans-serif;font-size:15px;outline:none;" />
      <div style="display:flex;gap:9px;margin-top:13px;flex-wrap:wrap;">{pills_html}</div>
    </div>

    <div id="evList">{rows_html}</div>
    <div id="evEmpty" style="display:none;text-align:center;padding:50px 0;color:#5f5e66;">No exhibits match.</div>

    <div style="border-top:1px solid #1c1b21;margin-top:34px;padding-top:22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;font-size:13px;color:#5f5e66;">
      <span>&copy; The Solar Foundation &middot; published for transparency</span>
      <a href="report.html" data-h="color:#f4f3f6;" style="color:#a9a8b0;text-decoration:none;">All 82 exhibits &#8594;</a>
    </div>
  </div>
</div>
<script>
(function(){{
  var cur="all";
  var search=document.getElementById('evSearch');
  var pills=document.querySelectorAll('.epill');
  function apply(){{
    var q=(search.value||'').toLowerCase().trim();
    var any=false;
    document.querySelectorAll('.erow').forEach(function(r){{
      var okT=cur==='all'||(' '+r.getAttribute('data-topics')+' ').indexOf(' '+cur+' ')!==-1;
      var okQ=!q||(r.getAttribute('data-text')||'').indexOf(q)!==-1;
      var v=okT&&okQ; r.style.display=v?'block':'none'; if(v)any=true;
    }});
    document.getElementById('evEmpty').style.display=any?'none':'block';
  }}
  pills.forEach(function(p){{p.addEventListener('click',function(){{
    cur=p.getAttribute('data-t');
    pills.forEach(function(x){{var a=x===p;x.style.border='1px solid '+(a?'#3a3942':'#1c1b21');x.style.background=a?'rgba(255,255,255,.05)':'transparent';}});
    apply();
  }});}});
  search.addEventListener('input',apply);
}})();
</script>
<script src="app.js"></script>
</body>
</html>
"""
open(os.path.join(OUT,"evidence.html"),"w",encoding="utf-8").write(PAGE)
print("wrote evidence.html | rows:",len(rows),"| counts:",counts)
