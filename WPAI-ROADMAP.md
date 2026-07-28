# Wizard Productions AI Studio (WPAI) — Company Roadmap

**Founder:** Robert "Rob" Bulkley (Mrwizard94)
**Tagline:** Forging the future of creative media
**Last updated:** 2026-07-07

---

## 1. The Model

WPAI is an umbrella studio. Divisions activate in sequence — each one funds and equips the next. Revenue-generating divisions come first; long-horizon research divisions come last, bankrolled by the earlier ones.

```
                    ┌─────────────────────────────┐
                    │   WPAI (umbrella / brand)   │
                    └──────────────┬──────────────┘
       ┌──────────┬──────────┬────┴─────┬────────────┬──────────┐
     Music     Graphics    Gaming    Software    AI Research  Quantum
    (ACTIVE)  (support)  (active,   (internal   (long-term   (last to
     funds     role now   external   tooling     flagship)    activate)
     the rest) for Music) repo)      first)
```

Each division has a charter in its folder's `README.md`. Division order of activation:

1. **Music** — active now. 22 tracks produced, 16 with release-grade licensed masters. Shortest path from existing assets to income. See `Music/CATALOG.md` and `Music/DISTRIBUTION-PLAN.md`.
2. **Graphics** — activates as Music's support arm (cover art, video assets, style guide), grows into standalone work.
3. **Gaming** — already active externally (Astral Sorcery port at `C:\WPAI\Gaming\Minecraft\Mods-1.20.1-Forge\Astral_Sorcery_Port`); ships under WPAI branding when ready.
4. **Software** — starts as internal tooling for the music release pipeline; products later.
5. **AI Research** — the flagship long-horizon division (von Neumann bottleneck, efficiency, novel architectures). Spends money; produces IP.
6. **Quantum** — last; longest path to value, depends on skills/funding from everything above.

## 2. Business Formation Checklist (sequenced, not all at once)

**Now (pre-revenue) — costs ~$0:**
- [x] Artist name decided (2026-07-07): **WPAI**. Web-level collision check done — no existing artist/band named WPAI found on streaming platforms; the acronym's main use is a medical questionnaire (Work Productivity and Activity Impairment), which competes for bare-term SEO but not in music. Residual checks before release day: search "WPAI" inside the Spotify and Apple Music apps directly, lock social handles (@wpai / @wpaistudio / @wpaimusic), check domains (wpai.studio, wpaistudio.com), and run a USPTO trademark search in the music/entertainment classes.
- [ ] Separate money trail from day one: a dedicated bank account (even a personal second account initially) so all WPAI income/expenses are traceable.
- [ ] Keep a simple ledger (spreadsheet is fine): every expense (distributor fees, AI subscriptions, gear) and every payment received. Needed for taxes regardless of entity type.

**At first real revenue (or ~$1k/yr trajectory):**
- [ ] Form an LLC in your home state ("Wizard Productions AI Studio LLC" or similar). Single-member LLC is cheap, protects personal assets, and lets divisions be DBAs under one entity rather than separate companies. *State fees and rules vary — verify with your state's Secretary of State site; this is a checklist, not legal advice.*
- [ ] Get an EIN (free, irs.gov, ~10 minutes).
- [ ] Move distributor/store accounts to the business entity and bank account.

**Deliberately later:** trademarks (after the name has proven value), S-corp election (only if profit makes self-employment tax savings real — talk to a CPA), separate legal entities per division (probably never — DBAs suffice unless a division takes outside investment).

## 3. Revenue Reality Check (Music as the funding engine)

Honest numbers so the plan stands on ground truth:

- **Streaming pays roughly $3–5 per 1,000 streams** (Spotify ~$0.003–0.005/stream gross, before distributor cut if any). 100k streams ≈ $300–500. Streaming alone funds gear slowly; it is the *catalog-building* channel, not the *income* channel at first.
- **YouTube** (you already have 12+ music videos): monetization needs 1k subs + 4k watch hours (or 10M Shorts views), then RPM for music content is typically $1–3. Same story — volume game.
- **Higher-$/unit channels to layer on:** Bandcamp (fans pay $5–10/album directly, ~85% to you), sync licensing (game devs, streamers, content creators need rock/metal — one placement can beat 100k streams), and selling to the creator economy directly (royalty-free licensing of your catalog).
- **Implication:** the funding-engine math works through *catalog size × multiple channels × time*, plus occasional high-value sync placements — not through one viral single. 21 tracks in a week means the production rate is the strength; the pipeline (master → package → release) is the bottleneck to fix.
- **⚠️ Rights caveat that gates everything:** commercial rights to AI-generated tracks depend on the generation tool's license tier, and copyright protection for AI output is limited (see `Music/DISTRIBUTION-PLAN.md`). Resolve this before the first upload.

## 4. 90-Day Plan (July → October 2026)

**Days 1–14 — Foundation (in progress):**
- [x] Catalog organized, per-track status known (`Music/CATALOG.md`)
- [x] Commercial rights: ✅ fully cleared (2026-07-07). Suno Pro since Jul 4 8:23 AM; pre-Pro tracks remastered under Pro and unlicensed originals deleted. All 22 tracks green — see distribution plan §0
- [ ] Name collision check + lock social handles
- [ ] Pick distributor and create account

**Days 15–45 — First releases:**
- [ ] Ship release #1: **Weaponized Mind** — the launch track (decided 2026-07-08). Package frozen in `Music/Releases/Weaponized Mind/`; at upload: artist WPAI, Explicit flag, AI disclosure, record ISRC. **Boots on the Ground** follows as #2, then Chain Reaction (Remastered)
- [ ] Establish the release cadence: 1 single every 1–2 weeks (the catalog already supports months of this)
- [ ] YouTube channel live with existing videos, branded with `Brand/` assets

**Days 46–90 — Pipeline and second channel:**
- [ ] Finish the audio backlog: Digital Demon (last video-only track), licensed WAV exports for the MP3-only tracks (Ashes in Drop C, Drop C Inferno, I Want Everything, The Sailor's Lament), Crimson Circuit vocal mix, Night Drive title decision
- [ ] Bandcamp storefront live (first EP bundle)
- [ ] First sync/licensing listing (e.g., royalty-free catalog page or a marketplace like Artlist/Pond5 — research their AI policies first)
- [ ] Review: streams/revenue data → decide Graphics division activation (style guide + per-release art)

## 5. Division Activation Gates

A division activates when its **trigger** fires, not on a calendar:

| Division | Activation trigger |
|---|---|
| Graphics | Music needs per-release art at cadence, or first external art request |
| Gaming (under WPAI brand) | Astral Sorcery port ready for public release |
| Software | A manual step in the music pipeline has been done 3+ times by hand |
| AI Research | Stable monthly revenue covers a defined compute budget |
| Quantum | AI Research running and stable; spare capacity exists |

---

*Update this file when milestones complete or the plan changes — it is the single source of truth for company sequencing.*
