# Solar (SXP) — Full History & Timeline Research Dossier

*A factual, cited research record compiled for transparency.*

**Compiled:** 2026-06-20
**Scope:** Swipe origins (2018) → SXP token → Binance acquisition (2020/2021) → rebrand to Solar & native mainnet (2022) → product expansion → resignation & wind-down (2025–2026).
**Method:** Multi-agent web research (Solar blog via Ghost sitemap, Binance primary announcements, Etherscan, Binance Research, CoinMarketCap/CoinGecko, third-party press) cross-checked against the founder's own *Solar (SXP): Background and Timeline (2020–2023)* community report, and against the live `solar-network/core` mainnet configuration in this repository. Every load-bearing claim was adversarially fact-checked.

---

## 0. How to read this document — verified vs. account

This dossier deliberately separates three tiers of evidence. Keep them distinct when publishing anything:

| Tier | Meaning | Example |
|------|---------|---------|
| ✅ **Verified (public record)** | Confirmed by a primary source (Binance announcement, Etherscan, on-chain, exchange notice) or multiple independent outlets. | Binance acquired Swipe & listed SXP on 2020-07-07. |
| 🟡 **Reported / partial** | Stated by reputable secondary sources but with a caveat, ambiguity, or single-source dependency. | The 2021 founder burn's exact on-chain date. |
| ⚠️ **Founder / Solar-team account** | Rests *solely* on Nayiem Willems' private account or Solar's own statements; **not** independently corroborated and, in fairness, **no public Binance rebuttal exists either**. | The alleged demand to hand over the treasury wallet as a condition for the Core 5.0 upgrade. |

> **The single most important compliance point:** the claim that *progress on Core 5.0 was conditioned on transferring the treasury, removing timelocks, and accepting personal liability* is **Tier ⚠ — the founder's account**. It is consistent with the public record but is **not** publicly proven. It must always be presented as *"my account / Solar's account,"* never as established fact. See [§9](#9-what-rests-only-on-the-founders-account-caveats).

---

## 1. Executive summary

- **Swipe** was a crypto Visa-debit-card company founded **in 2018 by Joselito Lizarondo** (Philippines, with UK/Estonia operations). Its token **SXP** launched as an **ERC-20 on Ethereum** (Aug 2019), raising **$12M** at **$0.20/SXP** against an original **300,000,000** max supply with a deflationary burn toward a 100M floor. ✅
- **Binance acquired Swipe and listed SXP on 2020-07-07** (terms undisclosed; later described by Binance as a "majority stake"), driven by the **Binance Card**. On **2021-12-30** Binance announced it would buy the **remaining outstanding shares** (full ownership); founder Lizarondo would step down. ✅
- Lizarondo **burned his entire 60M founder allocation** in two steps — 10M (2020) and the remaining **50M around 2021-04-29** (reported **>$200M**, ~17.5% of supply). SXP hit its **all-time high ~$5.79–$5.86 on 2021-05-03**. ✅
- Around **December 2021, Nayiem Willems** (ARK background) established **The Solar Blockchain Foundation** and steered SXP toward an **independent, DAO-governed Layer-1**. **Solar mainnet went live 2022-03-28** — a DPoS fork of **ARK Core** (53 block producers, 8s blocks). 🟡/✅
- **Binance supported the rebrand and 1:1 mainnet swap**, announced **2023-03-28** (linking Solar's own *"A Decentralised Community-Driven Project"* article), executed from **2023-05-15**. ✅
- Solar built consumer products (Solar Card, tymt, District 53, BrighterVPN) and worked toward **Core 5.0** (BFT + BLS, ~20× faster). Public messaging stayed upbeat into **late 2025**. ✅
- **Nayiem Willems resigned (publicly 2025-11-28)**, citing "rigid, non-negotiable conditions," restricted utilities, and confidentiality that barred transparency. On **2026-01-26** the Solar team announced **"no further protocol updates are planned,"** citing treasury custody outside the team, unannounced card-fee changes, and an alleged **"duplicated supply on BSC."** A rescue vote (**SXP-GOV-2026-01**) was **rejected on quorum (54.7% vs 67%)** despite **100% approval**. ✅/⚠️
- **Binance delisted SXP spot trading on 2026-04-01**; SXP hit an **all-time low $0.00006995 on 2026-06-10** and trades around **$0.0036** today — a **~99.9% drawdown** from its peak. The network is in **maintenance-only** condition. ✅

---

## 2. Master timeline (2018 → 2026)

> Confidence and source URL given for each entry. Dates are UTC where known.

### Era I — Swipe origins & SXP genesis (2018–2019)

| Date | Event | Conf. | Source |
|------|-------|:----:|--------|
| 2018 | Joselito Lizarondo founds **Swipe**, a multi-asset crypto wallet + Visa debit-card platform (Philippines; UK/Estonia ops). Allocates himself **60,000,000 founder SXP (20%** of the 300M supply). | ✅ | [CMC](https://coinmarketcap.com/alexandria/people/joselito-lizarondo) · [lizarondo.com](https://lizarondo.com/) |
| 2019-08-01 | **SXP private sale** opens at **$0.20/SXP** — 19,575,000 SXP (6.52%), raising **$3,915,000**. | ✅ | [Binance Research](https://www.binance.com/en/research/projects/swipe) |
| 2019-08-02 → 08-09 | **SXP public sale** at $0.20/SXP — 40,425,000 SXP (13.48%), raising **$8,085,000**. **Total raise $12,000,000.** | ✅ | [Binance Research](https://www.binance.com/en/research/projects/swipe) |
| 2019-08-16 | **SXP ERC-20 contract** `0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9` verified on Etherscan. **Max supply 300,000,000**, 18 decimals, Solidity 0.5.1; deflationary (80% of fees burned on-chain) toward a 100M floor. | ✅ | [Etherscan](https://etherscan.io/token/0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9) |

### Era II — Binance acquisition & the Swipe Network DeFi era (2020–2021)

| Date | Event | Conf. | Source |
|------|-------|:----:|--------|
| 2020 | Lizarondo burns **10,000,000** of his founder SXP as a commitment signal. | ✅ | [CMC](https://coinmarketcap.com/alexandria/people/joselito-lizarondo) |
| 2020-06-22 | **ERC-20 → BEP-2** swap begins (ERC-20 withdrawals locked; BEP-2 distributed by 2020-07-14), making SWIPE tradable on Binance Chain. | ✅ | [Tokocrypto](https://support.tokocrypto.com/hc/en-us/articles/360044793192-Swap-Your-SWIPE-ERC20-to-SWIPE-BEP2-) |
| **2020-07-07** | **Binance announces acquisition of Swipe and lists SXP** (10:59 UTC); SXP/BTC, SXP/BNB, SXP/BUSD trading opens 14:00 UTC (0 BNB fee). *Binance's July post says "completed an acquisition"; the **"majority stake"** wording comes from Binance's later (Dec 2021) announcement and the founder bio. Terms undisclosed.* | ✅ | [Binance Support](https://www.binance.com/en-IN/support/announcement/binance-announces-acquisition-of-swipe-and-lists-swipe-sxp-4ef2d3389f4143c2986c685a88501939) · [Binance Blog](https://www.binance.com/en/blog/all/Binance-and-Swipe-Partner-to-Bridge-Crypto-and-Commerce-Announce-Acquisition--421499824684900723) |
| 2020-07-07 | SXP rallies **+24.7% to close $1.93** (intraday high $2.04) on the news. | ✅ | [Yahoo/FXEmpire](https://finance.yahoo.com/news/swipe-sxp-breaks-binance-acquisition-024634728.html) |
| 2020-07-07 | **Binance Research** publishes its *Swipe (SXP)* report (max 300M; 80% fee burn toward 100M; raise $12M; allocation Team 20% / Reserve 40% / Founder 20% / Public 13.48% / Private 6.52%). | ✅ | [Binance Research](https://www.binance.com/en/research/projects/swipe) |
| 2020-08 | **Swipe Network DeFi** launches (staking + Compound-style **SwipeFi** lending) on BSC; SXP issued as **BEP-20**. *The "Swipe Network" was smart contracts on Ethereum/BSC — **not** a sovereign chain.* | ✅ | [Swipe/Medium](https://medium.com/swipe/swipe-launches-network-staking-and-defi-on-binance-smart-chain-with-swipe-governance-22b607cd5bf8) |
| 2020-08-13 | SXP reaches a 2020 peak ~**$4.3** amid the DeFi expansion. | 🟡 | [Capital.com](https://capital.com/en-int/analysis/swipe-sxp-price-prediction) |
| 2020-10-22 | **Binance opens BEP2 & BEP20 deposits/withdrawals** for INJ, PAX, **SXP** & USDC (09:42 UTC). | ✅ | [Binance Support](https://www.binance.com/en/support/announcement/binance-opens-bep2-bep20-deposits-and-withdrawals-for-inj-pax-sxp-usdc-9b2dc1d114ee462aaedebf73041f5807) |
| 2021-04-05 | New SXP ATH **$5.14** reported (up 95% from $2.62 on 03-25). | ✅ | [Yahoo/BeInCrypto](https://finance.yahoo.com/news/swipe-sxp-briefly-taps-time-113400247.html) |
| ~2021-04-29 | Lizarondo **burns his remaining 50,000,000 founder SXP** (~17.5% of supply), reported **>$200M** (~$4/SXP; later quoted up to ~$257.5M). CZ tweets *"Respect"*; founder *"never cashed out a dime."* Exact on-chain day ambiguous (outlets cluster 28 Apr–2 May). | 🟡 | [Ethereum World News](https://en.ethereumworldnews.com/swipe-founder-and-ceo-burns-his-sxp-token-allocation-worth-over-200m/) · [Benzinga](https://www.benzinga.com/markets/cryptocurrency/21/04/20855854/why-swipe-sxp-crypto-founder-burned-all-his-tokens-worth-200m) |
| 2021-05-03 | **SXP all-time high ~$5.79–$5.86** (CoinGecko $5.79; CoinLore $5.84; Capital.com $5.86). | ✅ | [CoinGecko](https://www.coingecko.com/en/coins/solar-2) |
| **2021-12-30** | **Binance to Acquire Outstanding Shares in Swipe** — full ownership (undisclosed terms); Swipe described as Binance's **card program manager and technology platform**; **CEO Lizarondo to step down and leave Binance** after completion. | ✅ | [Binance Support](https://www.binance.com/en/support/announcement/binance-to-acquire-outstanding-shares-in-swipe-efa96d9a856f4620b2fa6e372edbe290) · [Finance Magnates](https://www.financemagnates.com/fintech/binance-to-acquire-all-outstanding-shares-of-swipe/) |

### Era III — Transition to Solar & the independent Layer-1 (Dec 2021 – 2023)

| Date | Event | Conf. | Source |
|------|-------|:----:|--------|
| 2021-12 | **Nayiem Willems** (ARK background; joined as technical advisor, then took leadership) establishes **The Solar Blockchain Foundation** (reported in Lithuania) as SXP transitions toward an independent, community-driven, DAO-governed Layer-1. | 🟡 | [CryptoRank](https://cryptorank.io/news/feed/ebcaf-solar-project-resignation-nayiem-willems) |
| **2022-03-28** | **Solar (SXP) mainnet goes live (18:00 UTC)** — a **DPoS Layer-1 forked from ARK Core**: 53 block producers, 8s blocks, BIP340 Schnorr. Bridge enables **1:1 Swipe→Solar** swap. *(Repo confirms genesis epoch `2022-03-28T18:00:00Z`, nethash `16db20c3…96dc`, 53 delegates, 8s, 90% native fee burn.)* | ✅ | [Solar blog](https://blog.solar.org/get-ready-for-mainnet/) · repo `crypto/networks/mainnet` |
| 2022-05-30 | **Solar Core 3.3.0** live at block 671,988 — adds a **5% dev fund** and BIP340 Schnorr. | ✅ | [Solar blog](https://blog.solar.org/release-update-solar-core-3-3-0-went-live/) |
| 2022-08-14 | **District 53** metaverse game announced; 90% of land-sale proceeds burned. | ✅ | [Solar blog](https://blog.solar.org/district-53/) |
| 2023-02-12 | **Solar Card** introduced via Choise/Crypterium (~140 countries). | ✅ | [Solar blog](https://blog.solar.org/introducing-solar-card/) |
| 2023-02-13 | Solar's **CoinMarketCap guest post** *"Solar — A Decentralised Community-Driven Project"* (DAO-governed; not controlled by VCs, exchanges, celebrities or influencers). Later linked directly by Binance's swap announcement. | ✅ | [CMC](https://coinmarketcap.com/community/articles/63ea0fe5c9f0fe137e905394/) |
| **2023-03-28** | **Binance Will Support the Swipe (SXP) Mainnet Swap & Rebranding Plan to Solar (SXP)** (03:05 UTC): all ERC20/BEP2/BEP20 SXP to migrate to Solar mainnet at **1:1**; body links Solar's CMC article. *Exact phrase used/linked is **"decentralised community-driven project"** — not "independent."* | ✅ | [Binance Support](https://www.binance.com/en/support/announcement/binance-will-support-the-swipe-sxp-mainnet-swap-rebranding-plan-to-solar-sxp-73bded28e8dc48e081c5e577a5436c55) |
| 2023-04-04 | CoinDesk: SXP rallies up to **+40%/24h** on South Korean buying ($490M+ SXP/KRW on Upbit, exceeding its ~$455M market cap) ahead of the migration. | ✅ | [CoinDesk](https://www.coindesk.com/markets/2023/04/04/south-korean-traders-are-jumping-on-sxp-icx-tokens) |
| 2023-05-12 | **Updates on the … Swap** with the concrete 2023-05-15 schedule. | ✅ | [Binance Support](https://www.binance.com/en/support/announcement/updates-on-the-swipe-sxp-mainnet-swap-rebranding-plan-to-solar-sxp-8301f70257ce47d484b89fbb8198fdb3) |
| **2023-05-15** | **04:00 UTC** — Binance suspends ERC20/BEP20 Swipe-SXP deposits/withdrawals and opens **Solar mainnet SXP** deposits/withdrawals (1:1; Binance handles the technical swap for users). | ✅ | [Binance Support](https://www.binance.com/en/support/announcement/updates-on-the-swipe-sxp-mainnet-swap-rebranding-plan-to-solar-sxp-8301f70257ce47d484b89fbb8198fdb3) |
| 2023-06-12 | **Poloniex** completes the migration, suspends ERC-20 SXP (10:00 UTC). | ✅ | [Poloniex](https://support.poloniex.com/hc/en-us/articles/15602286537495-Announcement-Regarding-the-Completion-of-Swipe-SXP-Mainnet-Migration-and-Rebranding-to-Solar-SXP) |
| 2023-07-05 | **Solar SXP swap portal officially closes.** | ✅ | [Solar blog](https://blog.solar.org/swap-portal-officially-closed/) |
| 2023-07-20 | **Solar Core 4.3.1 released** — the current stable mainnet (ARK-DPoS). | ✅ | [GitHub releases](https://github.com/Solar-network/core/releases) |

### Era IV — Product expansion under Solar Enterprises (2024–2025)

| Date | Event | Conf. | Source |
|------|-------|:----:|--------|
| 2024-05-30 | **"Solar Enterprises"** rebrand (ex-Dokdo team) — pivot to consumer products (Solar Card, BrighterVPN, tymt, District 53). | ✅ | [Solar blog](https://blog.solar.org/introducing-solar-enterprises-brighter-blockchain-solutions/) |
| 2024-06-09 | **Core 5.0 alpha** announced — reported **~20× faster** than 4.3.1. | ✅ | [Solar blog](https://blog.solar.org/core-5-0-update-alpha-testing-performance-comparison/) |
| 2024-07-10 | Binance **removes SXP/BNB** spot pair (eff. 2024-07-12), citing poor liquidity/volume. | ✅ | [Binance Support](https://www.binance.com/en/support/announcement/notice-of-removal-of-spot-trading-pairs-2024-07-12-08fb183272a8493184700d675aac6a52) |
| 2024-10-18 | **BrighterVPN** launches with SXP login/payments. | ✅ | [Solar blog](https://blog.solar.org/brightervpn-is-here-the-crypto-first-vpn-has-arrived/) |
| 2024-11-25 | **"The Brighter One"** super-app announced. | ✅ | [Solar blog](https://blog.solar.org/important-update-product-news-and-an-app-to-rule-them-all/) |
| ~2025-03 | Solar development reportedly **halts** amid financial-control issues (per later Crypto Times coverage). | 🟡 | [Crypto Times](https://www.cryptotimes.io/2026/03/18/binance-to-delist-8-major-altcoins-in-april-including-forth-idex-lrc/) |
| 2025-03-13 | **Korean DAXA exchanges (Upbit, Bithumb, Coinone) delist SXP** (06:00 UTC), citing unresolved "cautionary asset" issues (untimely disclosure; lack of procedural transparency during major project changes). | 🟡 | [CryptoRank](https://cryptorank.io/news/feed/6a6db-sxp-delisting-upbit-bithumb-coinone) |
| 2025-03-28 | **"Solar Q1 2025 Update: Full Speed Ahead"** — optimistic roadmap (Solar Card V1 PWA, wallet rebuild, tymt 108 games + Dev Console, BrighterVPN PC/Mac, Dubai Crypto Expo planned May 2025). | ✅ | [Solar blog](https://blog.solar.org/solar-q1-2025-update-full-speed-ahead/) |
| 2025-06-19 | **tymt v2.2.2** — the last major product post on the Solar blog. | ✅ | [Solar blog](https://blog.solar.org/tymt-v2-2-2-is-here/) |

### Era V — Decline, resignation & wind-down (2025–2026)

| Date | Event | Conf. | Source |
|------|-------|:----:|--------|
| 2025-11-25 | **"Solar November 2025 – Update #3"** — Core 5.0 testnet **"90% Complete"** on a 5-block-producer BFT+BLS network; *"next-generation Solar chain is almost ready."* **Upbeat, no mention of risk/Binance/treasury — 3 days before the resignation.** | ✅ | [Solar blog](https://blog.solar.org/solar-november-2025-update-3/) |
| **2025-11-28** | **Nayiem Willems' resignation statement** (*"I'm stepping down from Solar"*): collaboration "shifted into rigid, non-negotiable conditions," utilities restricted, "innovation required permission," "legacy baggage" on the card product, and confidentiality that "prevented me from being transparent." Signs **"-N"**; pledges to build independently. **Does not name Binance, treasury, or Core 5.0 directly.** *(His personal site frames the resignation as "December 2025"; the primary blog date is Nov 28.)* | ✅ | [Solar blog](https://blog.solar.org/resignation-statement-nayiem-w/) · [CryptoRank](https://cryptorank.io/news/feed/ebcaf-solar-project-resignation-nayiem-willems) |
| **2026-01-26** | **"Solar Project Status Update"** — **"no further protocol updates are planned."** After due diligence on the "legacy structure," multiple individuals/teams declined to take over. Three named grievances: (1) **treasury custody/control outside the Solar team**; (2) **card-related processing-fee/utility changes implemented without prior notice**; (3) **"duplicated supply on BSC"** distributed via "Binance-operated infrastructure and platforms." **Binance unresponsive despite repeated outreach.** | ✅ (post) / ⚠️ (allegations) | [Solar blog](https://blog.solar.org/solar-project-status-update/) |
| 2026-01-26 | **"Block Producer Proposal Initiation"** — a non-binding, non-executing, time-bound signaling vote to gauge support for designing/publishing an *optional, voluntary* migration framework. | ✅ | [Solar blog](https://blog.solar.org/solar-governance-update-block-producer-proposal-initiation/) |
| 2026-01-27 | **SXP-GOV-2026-01** voting opens 09:00 UTC (snapshot height 15,111,674; 53 validators; 89.31M SXP voting power). Memo voting: send `0.00000001 SXP` to `Sdao2USyAz9B6RBgZeFyNDePuQAxfzZZHE` with memo `MONO-PROPOSAL:YES/:NO/:ABSTAIN`. Quorum ≥67% of voting power; approval ≥67% of (YES+NO). | ✅ | [proposals.solar.org](https://proposals.solar.org/) |
| **2026-01-30** | **Voting closes.** YES **28** (47.28M SXP) · NO **0** · ABSTAIN **1** (1.62M) · NOT VOTED **24** (40.42M). 29/53 validators voted. **Approval 100% (MET)** but **quorum 54.7% vs 67% (NOT MET) → REJECTED.** Proposal SHA-256 `2e43…2295`; anchor tx `b8f80f…267a`. | ✅ | [proposals.solar.org](https://proposals.solar.org/) |
| 2026-01-30 | **"Governance Proposal Outcome"** — failed quorum; network continues unchanged (block production active, validators independent, supply/balances/consensus unchanged, **seed nodes/services still maintained**); no migration/swap/successor process initiated or endorsed; **no Solar assets/code/governance/infrastructure transferred**; invites any better-positioned org to step up. | ✅ | [Solar blog](https://blog.solar.org/governance-proposal-outcome/) |
| **2026-03-18** | **Binance announces SXP delisting** (with A2Z, FORTH, HOOK, IDEX, LRC, NTRN, RDNT); spot trading to cease **2026-04-01 03:00 UTC**, citing standard review criteria. | ✅ | [Binance TH](https://www.binance.th/en/academy/new-cryptocurrency-listing%7Cdelisting/aae35acdcb09494787ba014184011d40) · [MEXC](https://www.mexc.com/news/961572) |
| 2026-03-19 → 03-25 | Binance winds down SXP: margin borrowing stops (03-19), futures settled & margin delisted (03-24), Simple Earn auto-redeemed (~03-25). | ✅/🟡 | [MEXC](https://www.mexc.com/news/961572) |
| 2026-03-30 | **Bitvavo** delists SXP (and IDEX). | 🟡 | [Bitvavo](https://bitvavo.com/en/news/delist-idex-sxp) |
| **2026-04-01** | **Binance ceases SXP spot trading (03:00 UTC)**, cancels open orders. SXP ~$0.0019–$0.008 amid ~42% 24h volatility. | ✅ | [Bitget](https://www.bitget.com/news/detail/12560605332304) |
| 2026-04-02 | Binance stops crediting SXP deposits. | ✅ | [MEXC](https://www.mexc.com/news/961572) |
| 2026-06-01 | Deadline for SXP withdrawals from Binance. | ✅ | [MEXC](https://www.mexc.com/news/961572) |
| 2026-06-10 | **SXP all-time low $0.00006995** (CoinGecko) — ~99.9% below the 2021 peak. | ✅ | [CoinGecko](https://www.coingecko.com/en/coins/solar-2) |
| 2026-06-20 | SXP ~**$0.0036**, market cap ~**$2.41M**, rank #2108, 24h volume ~$593; circulating/total **673,393,198 SXP**; liquidity almost entirely on DEXs (PancakeSwap, ApeSwap, Uniswap V2). | ✅ | [CoinGecko](https://www.coingecko.com/en/coins/solar-2) |

*(Parallel track, for context — not part of Solar:* Willems' separate venture **Monolythium** (Mono Labs R&D LLC, San Francisco) reset its protocol ~2026-04-28 and launched a public testnet ~2026-06-07, **explicitly inheriting no Solar assets, governance, or obligations.** [The Block](https://www.theblock.co/amp/post/403890/monolythium-introduces-public-testnet-after-full-protocol-reset) · [crypto.news](https://crypto.news/monolythiumintroduces-public-testnet-after-full-protocol-reset/))*

---

## 3. The SXP token — origin, supply, distribution & the supply mystery

**Origin & contract.** SXP began as an **ERC-20** on Ethereum — contract `0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9` (18 decimals, Solidity 0.5.1, deployed by *Swipe: Deployer 1* `0x7724…730a`, verified 2019-08-16). ([Etherscan](https://etherscan.io/token/0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9))

**Original supply & burn.** The **original max/total supply was a fixed 300,000,000 SXP**, but this was a *design cap, not a permanent constant*: SXP's **deflationary model burns 80%** of fees (ERC-20 era) toward a **100M floor**. The live legacy ERC-20 contract today reports ~**285.4M**. *(On the native Solar chain, the repo's `milestones.json` sets the fee burn to **90%**.)*

**Token sale (Aug 2019, $0.20/SXP, $12M total):**

| Tranche | Date | SXP | % | Raised |
|---------|------|-----|---|--------|
| Private | 2019-08-01 | 19,575,000 | 6.52% | $3,915,000 |
| Public | 2019-08-02→09 | 40,425,000 | 13.48% | $8,085,000 |

**Genesis allocation of the 300M:** Founder 20% (60M) · Team 20% · Reserve 40% · Public 13.48% · Private 6.52%. *(Public-sale math checks the cap: 40,425,000 ÷ 0.1348 ≈ 300M.)*

**Founder burns (a defining trust signal of the SXP story):** Lizarondo's 60M founder allocation was burned in two steps — **10M in 2020**, then his **remaining 50M ~2021-04-29** (~17.5% of supply, **>$200M**). CZ replied *"Respect."* This is genuinely unusual founder behavior and is **verified** across many outlets. ([Ethereum World News](https://en.ethereumworldnews.com/swipe-founder-and-ceo-burns-his-sxp-token-allocation-worth-over-200m/), [Benzinga](https://www.benzinga.com/markets/cryptocurrency/21/04/20855854/why-swipe-sxp-crypto-founder-burned-all-his-tokens-worth-200m), [BSC.News](https://www.bsc.news/post/ceo-of-swipe-burns-17-of-sxp-supply-200m-dollars))

**The unresolved supply discrepancy (central to Solar's grievance):**
- Binance Research / CMC describe an *original* 300M cap (deflationary).
- CoinMarketCap Academy cites **~480M** total supply at the **Solar mainnet migration (2023)**.
- CoinGecko/CMC show **current circulating/total ≈ 673.4M**, with max supply listed as **"unlimited."**

The jump from ~480M (2023) to ~673M (2026) is exactly what Solar's January 2026 status update points to as **"duplicated supply on BSC" distributed via "Binance-operated infrastructure."** ⚠️ **This allegation is Solar's own** — *no independent on-chain analysis, contract, or quantified breakdown confirming a duplicate mint was found.* The gap is *consistent with* the claim but **not independently verified**. The exact current canonical supply remains uncertain.

---

## 4. Solar protocol facts (verified from the live repo + blog)

From `solar-network/core` mainnet config in this workspace and the Solar blog:

- **Genesis epoch:** `2022-03-28T18:00:00.000Z` · **nethash:** `16db20c30c52d53638ca537ad0ed113408da3ae686e2c4bfa7e315d4347196dc`
- **Consensus:** DPoS (ARK Core fork) · **53 active block producers** · **8-second blocks** · BIP340 Schnorr
- **Token:** SXP · address prefix **`S`** · explorer **explorer.solar.org**
- **Fee burn:** **90%** of fees (native chain) — deflationary
- **Current software:** **Core 4.3.1** (stable mainnet) · **Core 5.0** = unreleased upgrade (BFT + BLS, ~20× faster, was 90% through testnet at the Nov 2025 update)
- **Seed nodes:** 15 hardcoded mainnet seed peers in `core/bin/config/mainnet/peers.json` (port 6001)

---

## 5. The Binance relationship — what's verified vs. the account

**Verified (public record):**
- Binance **acquired Swipe and listed SXP** (2020-07-07), bought the **remaining shares** (2021-12-30), and **Swipe was Binance's card-program manager**. ✅
- Binance **supported and operated the 1:1 mainnet swap** to Solar (2023), **echoing Solar's own "decentralised community-driven project" framing** by linking the CMC article. ✅
- Binance **removed SXP/BNB** (2024) and ultimately **delisted SXP** (2026). ✅
- **Acquisition terms/valuations were never disclosed** ("undisclosed sum"); the precise equity % of the 2020 "majority stake" is not public. ✅ (as a *non*-disclosure)

**Solar-team / founder account (⚠️ — not independently corroborated, and not publicly rebutted):**
- That **treasury custody and administrative control resided outside the Solar team**.
- That **card-related processing-fee / utility changes were implemented without prior notice** to Solar or governance.
- That a **"duplicated supply on BSC"** was distributed via Binance-operated infrastructure.
- That **Binance was unresponsive** to repeated outreach.
- That **Core 5.0 progress was conditioned** on transferring the treasury, removing timelocks, and accepting personal liability (from the founder's community report).

> The resignation statement (Nov 2025) **does not name Binance at all**; the January 2026 status update names Binance but frames everything as **Solar's account**. No public Binance response to these specific allegations was located. This asymmetry should be stated plainly in any public material.

---

## 6. Core 5.0 — what it was

Per the Solar blog and the Nov 2025 update, **Core 5.0** was a ground-up consensus upgrade:
- **BFT consensus with BLS** signatures (proof-of-possession, identity verification), deterministic proposer rotation, extended proposer-window tolerance, deterministic fallback on missed slots.
- Decoupled **RPC/API nodes** from block-producing nodes; stable mempool sync across producers.
- Reported **~20× faster** than Core 4.3.1 (alpha, June 2024).
- As of **2025-11-25**, testnet was **"90% complete"** on a 5-producer network; remaining work was integration/stress tests, RPC tuning, docs and release packaging.

In the founder's framing ([community report](#)), Core 5.0 was *"the least harmful, most constructive path forward"* — a protocol-level way to add utility and decentralization **without** relying on card programs or external consent. It was **never publicly released**; development stopped with the resignation and the January 2026 freeze.

---

## 7. Governance & the rejected proposal (exact figures)

**SXP-GOV-2026-01 — "Optional Migration Framework & Transition Process"** — the *only* proposal ever published on proposals.solar.org. Submitted by **Nayiem Willems** "on behalf of former Solar contributors and validator participants." Explicitly **non-binding, non-executing, time-bound**: it would *not* execute a swap, change supply/economics, or force any action — it only authorized *designing and publishing* a migration framework for later, separate approval. Non-negotiable principles included: **optional/user-initiated, 1:1 ratio, no supply duplication/inflation**, transparent eligibility, audited tooling, defined windows, optional exchange participation.

**Mechanics:** validators voted on-chain by sending exactly `0.00000001 SXP` to `Sdao2USyAz9B6RBgZeFyNDePuQAxfzZZHE` with memo `MONO-PROPOSAL:YES|NO|ABSTAIN` (one vote/validator). Window **27 Jan 09:00 → 30 Jan 09:00 UTC 2026** (72h), snapshot height 15,111,674, 53 validators, 89.31M SXP voting power. Quorum **≥67%** of voting power; approval **≥67%** of (YES+NO).

**Result:**

| | Validators | SXP | |
|---|---:|---:|---|
| YES | 28 | 47.28M | |
| NO | 0 | 0 | |
| ABSTAIN | 1 | 1.62M | |
| NOT VOTED | 24 | 40.42M | |
| **Participation** | **29 / 53** | **48.90M / 89.31M** | **= 54.7%** |

- **Approval: 100.0%** of (YES+NO) → **MET**
- **Quorum: 54.7%** vs 67% required → **NOT MET**
- **Outcome: REJECTED (quorum not reached).** Proposal SHA-256 `2e43956672c6dda1c2066335a60a025be6aa364555eaf29f3996d5432c5e2295`; anchor tx `b8f80f27d9228473acf370f5c2f69b0437344ad97bcfea75924ec2f71bca267a`.

> **Precision for public use:** "100% of votes cast were YES" is the **approval** metric (YES ÷ (YES+NO)). One validator abstained, so strictly *29 ballots were cast, 28 of them YES.* The proposal failed **only because too few validators voted** — the 54.7% turnout is itself a symptom of validator disengagement after the January freeze. *(Caveat: tallies are self-reported on the project-controlled dashboard; the Solarscan anchor-tx page returned HTTP 403 to automated checks and could not be independently re-verified here.)*

---

## 8. Current status (mid-2026)

Solar is in **maintenance-only limbo** — not a documented catastrophic halt, but effectively wound down:
- Per the 2026-01-30 outcome post: block production active, validators independent, supply/consensus unchanged, **seed nodes & core services maintained** — but **no development planned**, **no team willing to take over**, open invitation for any org to step in.
- The rescue vote failed on quorum; only 29/53 validators participated → **validator attrition**.
- **Exchange support has collapsed:** Korean DAXA (2025-03), Bitvavo (~2026-03-30), and **Binance delisted spot (2026-04-01)**; deposits stopped 04-02, withdrawals closed 06-01. Liquidity is now DEX-only with negligible volume.
- **SXP: ATL $0.00006995 (2026-06-10); ~$0.0036 now; ~$2.41M cap; ~99.9% off its peak.**
- The three grievances remain unresolved; Binance has not publicly responded.

This matches the lived situation the founder describes: a network in **critical condition**, exchanges unable/unwilling to transact, and a community that still assumes the project (and the founder) is active.

---

## 9. What rests only on the founder's account (caveats)

These must be labelled as *"my account"* / *"Solar's account"* in any publication — they are **plausible and consistent with the record, but not independently proven**:

1. ⚠️ The alleged **demand to hand over the treasury wallet** (plus remove timelocks and accept personal liability) as a condition for the **Core 5.0** mainnet upgrade. The public posts say only "rigid, non-negotiable conditions" / "terms no reasonable person could sign" / treasury control "outside the Solar team" — they **do not** publicly state that specific quid-pro-quo.
2. ⚠️ That **Binance (or a Binance-aligned party)** was the counterparty imposing those conditions. The Nov 2025 resignation **doesn't name Binance**; the Jan 2026 update does, as Solar's characterization.
3. ⚠️ The **"duplicated supply on BSC"** allegation — no independent on-chain confirmation, contract, or quantified breakdown.
4. ⚠️ The **unannounced card-fee/utility changes** — Solar's account; no primary card-issuer/Binance document located.
5. ⚠️ That **"multiple teams" did due diligence and declined** — identities/substance not public.
6. ⚠️ That **Binance was unresponsive "despite repeated outreach"** — one-sided; the outreach record isn't public.
7. 🟡 **Governance tallies** are self-reported on the project-controlled dashboard (anchor tx not independently re-verifiable here).
8. ✅(as non-disclosure) **Acquisition terms/valuations** for both Binance deals were never disclosed.
9. 🟡 The founder's **own timeline** on nayiem.com (ARK-advisor → Swipe → leadership; a "December 2025" resignation framing) partly conflicts with the **Nov 28, 2025** primary blog date — reconcile "formal/effective resignation" vs "public announcement."

---

## 10. Full source list (88)

> Primary sources first, then research/data, then press. All were fetched during this research; a few (Solarscan, one bitcoinfoundation.org page) returned 403/404 to automated fetching and are flagged.

### Solar primary (blog / proposals / repo)
- https://blog.solar.org/ — blog index · https://blog.solar.org/sitemap-posts.xml — full sitemap (110 posts)
- https://blog.solar.org/sxp-mainnet-launched/ · https://blog.solar.org/get-ready-for-mainnet/ · https://blog.solar.org/release-update-solar-core-3-3-0-went-live/
- https://blog.solar.org/district-53/ · https://blog.solar.org/introducing-solar-card/ · https://blog.solar.org/swap-portal-officially-closed/
- https://blog.solar.org/introducing-solar-enterprises-brighter-blockchain-solutions/ · https://blog.solar.org/core-5-0-update-alpha-testing-performance-comparison/
- https://blog.solar.org/brightervpn-is-here-the-crypto-first-vpn-has-arrived/ · https://blog.solar.org/important-update-product-news-and-an-app-to-rule-them-all/
- https://blog.solar.org/solar-q1-2025-update-full-speed-ahead/ · https://blog.solar.org/tymt-v2-2-2-is-here/
- https://blog.solar.org/solar-november-2025-update-3/ · https://blog.solar.org/resignation-statement-nayiem-w/
- https://blog.solar.org/solar-project-status-update/ · https://blog.solar.org/solar-governance-update-block-producer-proposal-initiation/ · https://blog.solar.org/governance-proposal-outcome/
- https://proposals.solar.org/ — SXP-GOV-2026-01 · https://solarscan.com/transaction/b8f80f27d9228473acf370f5c2f69b0437344ad97bcfea75924ec2f71bca267a *(403)*
- https://github.com/Solar-network/core/releases — Core 4.3.1

### Swipe / Binance / token primary
- https://coinmarketcap.com/alexandria/people/joselito-lizarondo · https://lizarondo.com/ · https://nayiem.com/
- https://www.binance.com/en/research/projects/swipe (· research.binance.com mirror) · https://etherscan.io/token/0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9
- https://www.binance.com/en/academy/articles/what-is-swipe-token-sxp · https://www.binance.com/en/square/post/226947
- https://www.binance.com/en-IN/support/announcement/binance-announces-acquisition-of-swipe-and-lists-swipe-sxp-4ef2d3389f4143c2986c685a88501939 (· en-NG mirror)
- https://www.binance.com/en/blog/all/Binance-and-Swipe-Partner-to-Bridge-Crypto-and-Commerce-Announce-Acquisition--421499824684900723
- https://www.binance.com/en/support/announcement/binance-opens-bep2-bep20-deposits-and-withdrawals-for-inj-pax-sxp-usdc-9b2dc1d114ee462aaedebf73041f5807
- https://www.binance.com/en/support/announcement/binance-to-acquire-outstanding-shares-in-swipe-efa96d9a856f4620b2fa6e372edbe290
- https://www.binance.com/en/support/announcement/binance-will-support-the-swipe-sxp-mainnet-swap-rebranding-plan-to-solar-sxp-73bded28e8dc48e081c5e577a5436c55 (· Square 354300/354301)
- https://www.binance.com/en/support/announcement/updates-on-the-swipe-sxp-mainnet-swap-rebranding-plan-to-solar-sxp-8301f70257ce47d484b89fbb8198fdb3
- https://coinmarketcap.com/community/articles/63ea0fe5c9f0fe137e905394/ — "Solar — A Decentralised Community-Driven Project"
- https://www.binance.com/en/support/announcement/notice-of-removal-of-spot-trading-pairs-2024-07-12-08fb183272a8493184700d675aac6a52
- https://www.binance.th/en/academy/new-cryptocurrency-listing%7Cdelisting/aae35acdcb09494787ba014184011d40 — 2026 delisting · https://www.mexc.com/news/961572
- https://support.tokocrypto.com/hc/en-us/articles/360044793192-Swap-Your-SWIPE-ERC20-to-SWIPE-BEP2- · https://medium.com/swipe/swipe-launches-network-staking-and-defi-on-binance-smart-chain-with-swipe-governance-22b607cd5bf8
- https://misterkeem.medium.com/swipe-sxp-2020-white-paper-update-and-breakdown-f40b9e7cda53

### Data & market
- https://coinmarketcap.com/currencies/sxp/ · https://www.coingecko.com/en/coins/solar-2 · https://metamask.io/price/swipe
- https://coinmarketcap.com/academy/article/what-is-solar-sxp-features-tokenomics-and-price-prediction (· Alexandria mirror)
- https://capital.com/en-int/analysis/swipe-sxp-price-prediction

### Press / coverage
- https://www.financemagnates.com/cryptocurrency/news/binance-buys-crypto-card-issuer-swipe-for-an-undisclosed-sum/ · https://decrypt.co/34797/binance-acquires-swipe-boosting-its-plans-for-a-crypto-debit-card
- https://www.theblock.co/post/70592/binance-completes-acquisition-of-crypto-debit-card-provider-swipe-lists-its-sxp-token · https://cointelegraph.com/news/binances-second-acquisition-of-2020-is-related-to-crypto-debit-cards
- https://finance.yahoo.com/news/swipe-sxp-breaks-binance-acquisition-024634728.html · https://finance.yahoo.com/news/swipe-sxp-briefly-taps-time-113400247.html · https://coincodex.com/article/8831/binance-officially-confirms-swipe-acquisition-lists-sxp-token
- https://www.financemagnates.com/fintech/binance-to-acquire-all-outstanding-shares-of-swipe/ · https://www.cryptoninjas.net/2021/12/30/binance-to-acquire-outstanding-shares-in-crypto-card-issuing-platform-swipe/ · https://coingape.com/breaking-binance-to-acquire-outstanding-shares-of-crypto-visa-card-issuer-swipe/ · https://cryptopotato.com/sxp-soars-30-as-binance-agrees-to-acquire-the-outstanding-swipe-shares/ · https://ihodl.com/topnews/2021-12-30/swipe-ceo-step-down-binance-acquires-100-stake/
- https://en.ethereumworldnews.com/swipe-founder-and-ceo-burns-his-sxp-token-allocation-worth-over-200m/ · https://www.benzinga.com/markets/cryptocurrency/21/04/20855854/why-swipe-sxp-crypto-founder-burned-all-his-tokens-worth-200m · https://www.bsc.news/post/ceo-of-swipe-burns-17-of-sxp-supply-200m-dollars · https://cryptotvplus.com/2021/04/sxp-founder-burns-allocated-sxp-tokens-supply-drops-by-17-5/ · https://bitcoinheat.com/2021/05/02/swipe-founder-and-ceo-burns-his-sxp-token-allocation-worth-over-200m/ · https://deep-resonance.org/2021/04/29/swipe-founder-burns-all-his-allocated-holdings-200m-reduces-sxp-supply-by-17-5/
- https://www.coindesk.com/markets/2023/04/04/south-korean-traders-are-jumping-on-sxp-icx-tokens · https://support.poloniex.com/hc/en-us/articles/15602286537495-... · https://support.poloniex.com/hc/en-us/articles/15178572166807-...
- https://cryptorank.io/news/feed/6a6db-sxp-delisting-upbit-bithumb-coinone · https://cryptorank.io/news/feed/992b6-sxp-investment-warning-upbit-bithumb-coinone · https://bitcoinworld.co.in/sxp-delisting-upbit-bithumb-coinone/
- https://www.cryptotimes.io/2026/03/18/binance-to-delist-8-major-altcoins-in-april-including-forth-idex-lrc/ · https://dailycoin.com/binances-april-1-delistings-hammer-8-altcoins-in-minutes/ · https://beincrypto.com/binance-delists-eight-tokens-april-crash/ · https://www.bitget.com/news/detail/12560605332304 · https://bitvavo.com/en/news/delist-idex-sxp · https://en.bloomingbit.io/feed/news/104737
- https://cryptorank.io/news/feed/ebcaf-solar-project-resignation-nayiem-willems · https://intellectia.ai/news/crypto/stunning-departure-from-solar-project-... · https://bitcoinfoundation.org/news/analysis/what-is-solar-and-why-did-sxp-price-collapse-to-near-zero-in-2026/ *(403/522)*
- https://www.theblock.co/amp/post/403890/monolythium-introduces-public-testnet-after-full-protocol-reset · https://crypto.news/monolythiumintroduces-public-testnet-after-full-protocol-reset/
- https://bitcointalk.org/index.php?topic=5272550.0 *(an impersonation/phishing "SXP-BNB" scam thread — **NOT** an allegation against Swipe/Solar; listed only to pre-empt confusion)*

---

*Companion documents: `SOLAR_ROADMAP.md` (forward plan + landing-page content) and the founder's `solar-community-report (2).docx` (the underlying transparency record with screenshot exhibits A-001→A-082 and the March 2023 draft "Mainnet Token Swap Guarantee with Deposit").*
