# solar.org — Landing Page & Transparency Site — Design Brief

**For:** Claude (design/build session)
**Site:** solar.org — the official site of **The Solar Foundation**, stewarding the open-source Solar blockchain (token: **SXP**).
**Voice:** Institutional, third-person, **foundation perspective**. Do **not** write in first person; do **not** foreground any individual's name. Where a named public document must be linked (e.g., the lead developer's resignation statement), link it plainly without building copy around the person. Primary contact everywhere: **hello@solar.org**.
**Goal:** A calm, honest, high-tech site that (1) presents Solar and SXP, (2) gives a transparent, cited account of the project's history and current maintenance-only status, (3) routes exchanges, holders, validators, and would-be stewards to the right place, and (4) ends speculation by making the record authoritative and public.

---

## 1. Brand system (carry over exactly — consistency with Solarscan)

- **Primary gradient:** gold→coral `linear-gradient(135deg, #ffc24a, #ff6a5e)`
- **Background:** warm near-black `#0a0a0d`; panels `#0e0d12`; borders `#1c1b21`
- **Accents:** gold `#f6a623`, green `#46d39a`, red `#f76a6a`
- **Fonts:** Space Grotesk (display), Manrope (UI/body), JetBrains Mono (numerics/hashes/addresses)
- **Logo/favicon:** `https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png`
- **Aesthetic:** dark, sleek, high-tech, subtle glows; restrained motion. **Avoid** AI-slop rainbow gradients, emoji, and stock-art. Mono font for all on-chain values (heights, hashes, addresses, token amounts).
- **Accessibility:** WCAG-AA contrast on the dark theme; respect `prefers-reduced-motion`.

---

## 2. Site map

| Route | Purpose |
|-------|---------|
| `/` | Landing page (hero → stats → what-is-Solar → status → history accordion → exchanges → get-involved → footer) |
| `/status` | Live + narrative current status (can also be an anchored section on `/`) |
| `/history` | Full transparency record: timeline + accordion + citations (long-form version of the homepage accordion) |
| `/governance` | The rejected proposal SXP-GOV-2026-01, with exact figures + integrity hashes |
| `/archive` | Archived blog posts (durable snapshots of blog.solar.org) |
| `/exchanges` | Where SXP still trades + holder guidance (can be a homepage section + standalone) |

Keep it shippable as a single long landing page first, with the deeper routes as expandable "Read the full record" destinations.

---

## 3. Homepage — section-by-section spec (with copy)

### 3.1 Hero
- **Eyebrow:** `THE SOLAR FOUNDATION`
- **Headline:** *Solar — an open-source dPoS blockchain.*
- **Subhead:** *Native token SXP. 8-second blocks, 53 block producers, fully on-chain. This site is the Foundation's transparent record of the network — its history, its present status, and how to take part.*
- **Primary CTA:** `Open Explorer` → https://solarscan.com
- **Secondary CTA:** `Read the record` → `#history`
- **Status chip** (top-right of hero, small): `● Maintenance-only` (amber dot) → links to `#status`. Be honest up front — it builds trust and pre-empts the "is this still alive?" question.

### 3.2 Key stats band (pull live from Solarscan; static fallbacks below)
> Pull from the Solarscan API at build/runtime. Hardcode nothing that drifts. Show a subtle "from Solarscan" label.

| Stat | Live source | Static fallback |
|------|-------------|-----------------|
| Block time | Solarscan | **8s** |
| Active block producers | Solarscan | **53** |
| Block reward (dynamic) | Solarscan | **6.75–13.25 SXP** |
| Circulating supply | Solarscan / CoinGecko | **~673–684M SXP** |
| Fee burn | mainnet config | **partial — 90% of fees burned** |
| Mainnet genesis | static | **2022-03-28** |

*(Footnote the stats band: "Live metrics from Solarscan; some figures depend on current validator participation.")*

### 3.3 What is Solar
> **Solar is an independent, open-source Layer-1 blockchain** secured by Delegated Proof-of-Stake (dPoS): 53 elected block producers, 8-second blocks, BIP340 Schnorr signatures, and a partial fee burn. Its native token is **SXP**. Solar's mainnet launched on **28 March 2022** as a community-driven fork of ARK Core, and the SXP token migrated to it 1:1 in 2023. The network is open-source on GitHub and explorable on Solarscan.

Three feature cards: **Fast & low-fee** (8s blocks, dynamic fees, deflationary burn) · **Delegated PoS** (53 producers, on-chain voting) · **Open & verifiable** (open-source core, public explorer, on-chain governance).

### 3.4 Current status module → see §4
### 3.5 History & transparency accordion → see §5
### 3.6 Where SXP trades → see §6
### 3.7 Get involved / stewardship → see §7
### 3.8 Footer → see §8

---

## 4. Current status module (`/status`)

**Headline:** *Where Solar stands today.*

**Status copy (foundation voice):**
> **Solar is in a maintenance-only state.** There is no active development team and no further protocol updates are planned. The network continues to operate through its independent block producers, and the Foundation maintains seed infrastructure and this record on a best-effort basis so the chain remains reachable for existing holders and integrations.
>
> Following the resignation of the project's lead developer in November 2025 ([statement](https://blog.solar.org/resignation-statement-nayiem-w/)), the Foundation published a full [Project Status Update](https://blog.solar.org/solar-project-status-update/) (January 2026) and held an [open governance vote](https://proposals.solar.org/) on an optional path forward. After that vote did not reach quorum ([outcome](https://blog.solar.org/governance-proposal-outcome/)), no successor development team came forward. Solar remains open for any credible organization to steward — see [Get involved](#get-involved).

**Live status row (from Solarscan):** last block height · last block time · active producers now · is-the-chain-advancing indicator. *If block production has stalled, show an honest amber/red banner with the last block timestamp — this is the answer when people ask "is the network down?"*

**Honesty callouts (small cards):**
- *No active development* — last protocol release: Core 4.3.1.
- *Exchange support reduced* — major listings closed in 2025–2026 (see history).
- *Seed nodes maintained* — best-effort, no SLA.

---

## 5. History & transparency — accordion content (`/history`)

**Intro copy:**
> The Solar Foundation believes the network's history should be public and verifiable. Below is a sourced timeline of the project, from Swipe's founding through the Binance acquisition, the 2023 rebrand to Solar, and the 2025–2026 wind-down. **Verifiable facts link to primary sources** (exchange announcements, Etherscan, on-chain records). A small number of points reflect **the Solar team's own account** of internal events and are **labelled as such** — they are consistent with the public record but have not been independently adjudicated, and the other parties have not publicly responded.

> **Design:** render each era as an accordion panel. Inside each, 4–6 short fact lines, each with an inline source link (open in new tab). Use a small tag on each fact: `Verified` (green), `Reported` (gold), or `Foundation account` (muted/outline). Put a "View full research dossier" link at the bottom.

### Accordion item 1 — *Swipe origins & the SXP token (2018–2019)* `Verified`
- Swipe — a multi-asset crypto wallet and Visa debit-card platform — was founded in **2018** by Joselito Lizarondo. [[CMC]](https://coinmarketcap.com/alexandria/people/joselito-lizarondo)
- **SXP launched as an ERC-20 on Ethereum** (contract `0x8ce9…b6a9`), original max supply **300,000,000**, deflationary toward a 100M floor. [[Etherscan]](https://etherscan.io/token/0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9)
- **Token sale (Aug 2019):** $0.20/SXP, **$12M raised** (private 6.52% + public 13.48%). [[Binance Research]](https://www.binance.com/en/research/projects/swipe)
- Genesis allocation: Founder 20% · Team 20% · Reserve 40% · Public 13.48% · Private 6.52%.

### Accordion item 2 — *Binance acquires Swipe (2020–2021)* `Verified`
- **2020-07-07 — Binance announced its acquisition of Swipe and listed SXP.** [[Binance]](https://www.binance.com/en-IN/support/announcement/binance-announces-acquisition-of-swipe-and-lists-swipe-sxp-4ef2d3389f4143c2986c685a88501939)
- **2020-10-22 — Binance opened BEP2 & BEP20 deposits/withdrawals for SXP.** [[Binance]](https://www.binance.com/en/support/announcement/binance-opens-bep2-bep20-deposits-and-withdrawals-for-inj-pax-sxp-usdc-9b2dc1d114ee462aaedebf73041f5807)
- The founder **burned his entire 60M founder allocation** (10M in 2020; the remaining **50M in April 2021**, ~17.5% of supply, reported >$200M). [[Ethereum World News]](https://en.ethereumworldnews.com/swipe-founder-and-ceo-burns-his-sxp-token-allocation-worth-over-200m/)
- SXP reached its **all-time high (~$5.79–$5.86) on 2021-05-03**. [[CoinGecko]](https://www.coingecko.com/en/coins/solar-2)
- **2021-12-30 — Binance announced it would acquire the remaining shares of Swipe** (full ownership; Swipe as its card-program manager). [[Binance]](https://www.binance.com/en/support/announcement/binance-to-acquire-outstanding-shares-in-swipe-efa96d9a856f4620b2fa6e372edbe290)

### Accordion item 3 — *Solar: the independent Layer-1 (2022–2023)* `Verified`
- **The Solar Blockchain Foundation was established (~Dec 2021)** to steward SXP as an independent, community-driven, DAO-governed network. [[CryptoRank]](https://cryptorank.io/news/feed/ebcaf-solar-project-resignation-nayiem-willems)
- **2022-03-28 — Solar mainnet went live** (dPoS fork of ARK Core: 53 producers, 8s blocks). [[Solar]](https://blog.solar.org/get-ready-for-mainnet/)
- **2023-03-28 — Binance announced support for the SXP mainnet swap & rebrand to Solar**, migrating all ERC20/BEP2/BEP20 SXP **1:1** and linking Solar's own *"A Decentralised Community-Driven Project"* article. [[Binance]](https://www.binance.com/en/support/announcement/binance-will-support-the-swipe-sxp-mainnet-swap-rebranding-plan-to-solar-sxp-73bded28e8dc48e081c5e577a5436c55) · [[CMC]](https://coinmarketcap.com/community/articles/63ea0fe5c9f0fe137e905394/)
- **2023-05-15 — the swap executed;** the Solar swap portal closed 2023-07-05. [[Solar]](https://blog.solar.org/swap-portal-officially-closed/)
- **Core 4.3.1** (2023-07-20) is the current stable mainnet. [[GitHub]](https://github.com/Solar-network/core/releases)

### Accordion item 4 — *Products & Core 5.0 (2024–2025)* `Verified`
- The team expanded into consumer products: **Solar Card, tymt (game launcher), District 53, BrighterVPN**, under "Solar Enterprises" (2024-05-30). [[Solar]](https://blog.solar.org/introducing-solar-enterprises-brighter-blockchain-solutions/)
- **Core 5.0** — a next-generation consensus upgrade (BFT + BLS signatures, decoupled RPC nodes, ~20× throughput) — entered alpha in **June 2024** and reached **~90% testnet completion by November 2025**. *It was never released.* [[Solar]](https://blog.solar.org/core-5-0-update-alpha-testing-performance-comparison/) · [[Nov 2025 update]](https://blog.solar.org/solar-november-2025-update-3/)

### Accordion item 5 — *Resignation & wind-down (2025–2026)* `Verified` + `Foundation account`
- **November 2025 — the project's lead developer resigned**, citing conditions that prevented further progress and confidentiality that limited transparency at the time. [[Statement]](https://blog.solar.org/resignation-statement-nayiem-w/) `Verified`
- **January 2026 — the Foundation's Project Status Update** stated **no further protocol updates are planned**, and that prospective successor teams declined after due diligence. It cited unresolved concerns about **treasury custody residing outside the Solar team, card-fee/utility changes made without notice, and duplicated token supply on BSC distributed via external infrastructure** — *the Foundation's account; the other parties have not publicly responded.* [[Status Update]](https://blog.solar.org/solar-project-status-update/) `Foundation account`
- **27–30 January 2026 — an open governance vote (SXP-GOV-2026-01)** on an optional, voluntary migration framework **was rejected on quorum** (54.7% participation vs 67% required) despite **100% approval among votes cast**. [[Proposal]](https://proposals.solar.org/) · [[Outcome]](https://blog.solar.org/governance-proposal-outcome/) `Verified`
- **2025–2026 — exchange support narrowed:** Korean exchanges delisted SXP (March 2025); **Binance ended SXP spot trading on 1 April 2026**. [[CryptoRank]](https://cryptorank.io/news/feed/6a6db-sxp-delisting-upbit-bithumb-coinone) · [[MEXC]](https://www.mexc.com/news/961572) `Verified`
- The Foundation maintains seed infrastructure and this record; **no Solar assets, code, governance authority, or infrastructure have been transferred** to any successor. [[Outcome]](https://blog.solar.org/governance-proposal-outcome/) `Verified`

**Below the accordion:** button → *"Read the full research dossier (88 sources)"* and *"Read the community transparency report."*

---

## 6. Where SXP still trades (`/exchanges`)

**Headline:** *Where SXP trades.*
**Copy:**
> SXP is the native token of the Solar mainnet. After major exchanges delisted in 2025–2026, remaining trading is on a small number of venues with low liquidity. The Foundation lists these for informational continuity only — **this is not an endorsement or financial advice.** Before depositing or withdrawing, **confirm the deposit network is Solar mainnet** (not a legacy contract).

**Table:**

| Exchange | Pair(s) | Market link | Notes |
|----------|---------|-------------|-------|
| **HTX** | SXP/USDT | https://www.htx.com/en-us/trade/sxp_usdt | Active; CoinGecko flags volume as anomaly/outlier — treat displayed volume skeptically |
| **BVOX** | SXP/USDT | https://www.bitvenus.me/exchange/SXP/USDT | Active; flagged anomaly |
| **Poloniex** | SXP/USDT | https://poloniex.com/spot/SXP_USDT | Listed but effectively inactive |
| **HitBTC** | SXP/USDT, SXP/BTC, SXP/USDC | https://hitbtc.com/sxp-to-usdt · https://hitbtc.com/SXP-to-BTC · https://hitbtc.com/SXP-to-USDC | Near-dead (~$1/day); page explicitly lists **"Solar mainnet SXP"** |

**Holder guidance card:**
> If you self-custody SXP, your wallet and the network continue to operate. Verify balances and transactions on [Solarscan](https://solarscan.com). The Foundation makes no price predictions and no guarantees about liquidity or future listings.

**For exchanges card:**
> Exchanges needing to support SXP deposits/withdrawals during wind-down can reach the Foundation for **technical** continuity help (node endpoints, explorer, network parameters): **hello@solar.org**. The Foundation cannot make listing or market decisions.

> **Design note:** mark the exchange table "informational only — verify network before depositing." Add a small `Last reviewed: [DATE]` so it's clearly a snapshot. Consider pulling live market data from CoinGecko's Solar (SXP) tickers endpoint and flagging anomaly markets automatically.

---

## 7. Get involved / stewardship (`#get-involved`)

**Headline:** *Solar is open for stewardship.*
**Copy:**
> Solar is open-source and remains open for any credible organization, foundation, or contributor better positioned to take a more active role in its development. The Foundation will reasonably assist a genuine successor's technical transition. **If your team is interested, contact [hello@solar.org](mailto:hello@solar.org).**

**Cards / links:**
- **GitHub** → https://github.com/Solar-network
- **Block explorer (Solarscan)** → https://solarscan.com
- **Governance record** → https://proposals.solar.org/ (and `/governance`)
- **Transparency record** → `/history`
- **Discord** → `[DISCORD INVITE URL — fill in]`
- **Community / X** → `[X/Twitter URL — fill in]` · `[Telegram URL — fill in]`
- **Contact** → hello@solar.org

---

## 8. Footer

- Left: logo + `© The Solar Foundation` + one-line: *"An open-source dPoS blockchain. Maintained for transparency and continuity."*
- Columns: **Network** (Explorer, GitHub, Status) · **Record** (History, Governance, Archive, Community Report) · **Community** (Discord, X, Telegram) · **Contact** (hello@solar.org).
- Bottom disclaimer (small, muted):
> *This site is a transparency and information record published by The Solar Foundation. It is not financial, investment, or legal advice. Factual statements link to primary sources; some statements reflect the Foundation's own account of events and are labelled accordingly. Nothing here is an offer, solicitation, or endorsement of any token or exchange.*

---

## 9. Archive page (`/archive`)

**Purpose:** durable, self-hosted access to Solar's blog history (so the record survives even if blog.solar.org is retired).

**Spec:**
- Title: *Blog Archive.* Intro: *"An archive of Solar's official announcements and updates."*
- Render a reverse-chronological **list** (title · date · short excerpt · link). Group by year with sticky year headers.
- **Source options (pick one, in order of durability):**
  1. **Snapshot to static** — capture each post from blog.solar.org as static HTML/Markdown into the new site (most durable; survives Ghost hosting lapse). Use the Ghost sitemap for the full list: `https://blog.solar.org/sitemap-posts.xml`.
  2. **Ghost Content API** — pull live from blog.solar.org with an API key (easy, but depends on Ghost staying up).
  3. **Link out + web.archive.org fallback** per post (lightest).
- **Prioritize archiving these critical posts as durable static pages** (link them from `/history` and `/status`):
  - `solar-november-2025-update-3` (2025-11-25)
  - `resignation-statement-nayiem-w` (2025-11-28)
  - `solar-project-status-update` (2026-01-26)
  - `solar-governance-update-block-producer-proposal-initiation` (2026-01-26)
  - `governance-proposal-outcome` (2026-01-30)
- Also surface historical product/protocol posts (get-ready-for-mainnet, solar-core-3-3-0, introducing-solar-card, swap-portal-officially-closed, introducing-solar-enterprises, core-5-0 alpha, brightervpn, q1-2025-update, tymt releases).
- Add a **search/filter** box and **tags** (Governance · Protocol · Product · Status).

---

## 10. Governance page (`/governance`)

Render **SXP-GOV-2026-01** as a clean record:
- Title, submitter (*"on behalf of former Solar contributors and validator participants"*), window **27–30 Jan 2026 (UTC)**, snapshot height **15,111,674**, 53 validators, 89.31M SXP voting power.
- **Rules:** quorum ≥67% of voting power; approval ≥67% of (YES+NO).
- **Result table:** YES 28 (47.28M) · NO 0 · ABSTAIN 1 (1.62M) · NOT VOTED 24 (40.42M) · participation 54.7% · approval 100% · **REJECTED (quorum not reached).**
- **Integrity (mono font):** SHA-256 `2e43956672c6dda1c2066335a60a025be6aa364555eaf29f3996d5432c5e2295`; anchor tx `b8f80f27d9228473acf370f5c2f69b0437344ad97bcfea75924ec2f71bca267a` → link to Solarscan tx.
- One-line explainer: *"The proposal was supported by every validator who voted, but too few validators participated to meet the 67% quorum, so it did not pass."*

---

## 11. Live data sources (don't hardcode drift)

- **Network stats / tx / blocks / supply:** Solarscan (https://solarscan.com) — use its API for height, producers, block reward, supply.
- **Market / tickers / anomaly flags:** CoinGecko *Solar (SXP)* (`solar-2`) tickers endpoint.
- **Blog content:** Ghost sitemap `https://blog.solar.org/sitemap-posts.xml` (full list) or Ghost Content API.
- Build with graceful fallbacks to the static figures in §3.2 if an API is unavailable.

---

## 12. Tone & guardrails (important)

1. **Foundation voice, no first person, no name-foregrounding.** The only place a name appears is via the linked resignation statement's own title.
2. **Keep `Verified` vs `Foundation account` visually distinct** on every history fact. Never present the Binance-related grievances (treasury custody, duplicated supply, card fees, unresponsiveness) as adjudicated fact — attribute them to the Foundation's published Status Update and link it.
3. **No legal claims, no accusations of wrongdoing.** Describe events; let sources speak.
4. **Not financial advice / no endorsement** on the exchanges section.
5. **Snapshot dates** on anything that drifts (status, exchanges, stats).
6. **Durability:** prefer self-hosted static snapshots for the critical posts; keep the site archivable (clean HTML, web.archive.org-friendly).

---

## 13. Kickoff prompt (paste this to start the design session)

> Build a modern, dark, high-tech landing + transparency site for **solar.org**, the official site of **The Solar Foundation**, stewarding the open-source **Solar** dPoS blockchain (token **SXP**). Write everything in **institutional foundation voice — third person, no first person, do not foreground any individual's name.** Primary contact: **hello@solar.org**.
>
> **Brand system:** primary gradient `linear-gradient(135deg,#ffc24a,#ff6a5e)`; background `#0a0a0d`, panels `#0e0d12`, borders `#1c1b21`; accents gold `#f6a623`, green `#46d39a`, red `#f76a6a`; fonts Space Grotesk (display), Manrope (body), JetBrains Mono (numbers/hashes); favicon `https://storage.ghost.io/c/32/25/3225f39c-c8f7-41ca-b74e-7db2f5ea653a/content/images/size/w256h256/2025/03/favicon.png`. Dark, sleek, subtle glows; no emoji, no AI-slop gradients.
>
> **Homepage sections:** (1) hero with an honest `● Maintenance-only` status chip and CTAs *Open Explorer* (→ solarscan.com) and *Read the record*; (2) live stats band (8s blocks, 53 producers, dynamic 6.75–13.25 SXP reward, ~673–684M supply, partial/90% fee burn, genesis 2022-03-28 — pull live from Solarscan with static fallbacks); (3) what-is-Solar + 3 feature cards; (4) current-status module with a live "is the chain advancing" indicator; (5) **History & Transparency accordion** (5 era panels, each fact tagged `Verified`/`Reported`/`Foundation account` with inline source links); (6) "Where SXP trades" table (HTX, BVOX, Poloniex, HitBTC — informational only, verify network before depositing); (7) "Solar is open for stewardship" with links to GitHub, Solarscan, governance, Discord, community, and a contact CTA to hello@solar.org; (8) footer with disclaimer.
>
> Also build routes: `/history`, `/governance` (render proposal SXP-GOV-2026-01 with exact vote figures + integrity hashes), `/archive` (durable snapshots of blog.solar.org posts, sourced from the Ghost sitemap; prioritize the Nov-2025→Jan-2026 posts), `/exchanges`, `/status`.
>
> Use the content, copy, links, and citations from the attached **SOLAR_ORG_DESIGN_BRIEF.md** verbatim where provided. Keep `Verified` vs `Foundation account` visually distinct; never present the Binance-related grievances as adjudicated fact — attribute them to the Foundation's published Status Update. Mark anything that drifts with a "Last reviewed" date. No financial advice, no accusations. Explore 3 hero directions.
>
> Open questions to confirm with me first: exact tagline, the Discord/X/Telegram URLs, and whether the archive should be static snapshots or Ghost-API-driven.

---

*Companion files: `SOLAR_HISTORY_RESEARCH.md` (the 88-source dossier — use for any fact-check) and `SOLAR_ROADMAP.md` (the foundation's forward posture). Underlying evidence: `solar-community-report (2).docx`.*
