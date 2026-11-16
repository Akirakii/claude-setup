# Handoff — creature stats system (Phase 8) — LANDED

Built 2026-09-16 (full phase, AFK). The system + its design essence now live in
the creature code (`entities/creatures/`) and the machine code (`entities/machines/`)
(StatStation). This doc holds only what did NOT ship this pass.

## Shipped
STR/VIT/DEX/INT with use-based XP + real-target anti-grind guard; linear drive of
attack_damage / hp+regen+knockback / attack speed / reach+splash; stateless
`eligible_jobs(stats)` INT gate (retired `professions[]`); binary weapon `req_*` gate;
mustache SIZE = Σ stats + HUE = build (STR red / VIT green / DEX yellow / INT blue); idle
floor on the dilated clock; StatStation grinds; inspector + job-panel stat readouts; balance
probe counters; cheats F7 (pump aimed) / F8 (spawn stations). Tests in
`test/ci/entities/creatures/test_creature_stats*.gd`.

## Deferred to Phase 10 (cards / content)
- **StatStation as a DRAFTABLE card.** The behavior ships; drafting/placement waits on the
  card system (Phase 10, `HANDOFF_phase8_card_taxonomy.md`). Spawn via F8 until then.
- **Per-species stat identity.** Only frog (INT) + fox (DEX/STR) authored; bunny/generic use
  defaults. Author the full roster's base vectors with the card set.

## Deferred extension — the stat-modifier layer (design DECIDED 2026-09-16)

Shipped drive is `base + stat` only. Generalize to **effective = base + Σ active
modifiers**, each `{stat, delta, source}`, all shown in parens (`STR 12 (+2)`). One
computation, many feeders — do NOT build a separate buff path per source:
- **mood** (Phase 9) — transient, decays.
- **equipped weapon** (Phase 10 gear) — active while held; may debuff (heavy weapon →
  +STR-synergy but −DEX).
- (later: build auras, status effects — same slot, free extension.)

Mustache **HUE/SIZE reads BASE** (build identity stays legible); the modifier delta
shows only as the parenthetical. This is a real change to the SHIPPED effective-stat
computation; both Phase-9 mood and Phase-10 gear depend on it.

## OPEN (balance — tune with a real playtest / balance report)
- XP rates + drive per-point constants (`CreatureConfig.XP_*`, `*_PER_POINT`) are first-pass
  guesses; the station-vs-combat ratio especially. Register already done in `balance_probe.gd`.
- Hue readability once 4 stats blend in-engine (only red verified in tests).
- Whether `STAT_SIZE_BASELINE` (20) matches the authored mesh across species.
