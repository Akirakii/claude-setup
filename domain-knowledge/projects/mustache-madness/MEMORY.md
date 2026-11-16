# MEMORY: pillars and invariants

The fixed list every idea is judged against. "You" means Claude. Only abstract principles
live here: no files, names, incidents, or examples. Concrete traps and repo conventions are
in
`GOTCHAS.md`, standing law in `docs/LAW_*.md`, working rules in `CLAUDE.md`.

## Design compass (game pillars)
- **PRE-PILLAR (unconfirmed, user said yes):** every city job starts as something the player
  does by hand; its building opens once the player has done it, and the building takes that work
  off the player's hands. How the hand act opens the card, and jobs with no hand act, are open.
- **PRE-PILLAR (unconfirmed):** a creature may hold any funder slot the player may hold (a
  sign, a site), with the same pay verb and sign cap, never one the player cannot pay; a gem
  still decides only which workplaces stand open, never who works there.
- **PRE-PILLAR (unconfirmed):** a gem a buyer pays at an owned piece waits there (its till)
  until the proprietor walks over; no gem moves to a creature that is not standing there.
- **PRE-PILLAR (unconfirmed):** a job is learned once and kept; the stat that was highest when
  learning ended picks it, so later training never flips a creature's trade.
- **PRE-PILLAR (unconfirmed):** the city grows exponentially (user's words); the world is closed,
  so value enters only by the wave, the land, and new creatures. The player's income grows only
  through something the player built, reinvested, never on the night clock or the kill count.
- **PRE-PILLAR (unconfirmed):** growing income is capped by shared space or creatures the player
  chose to use for it, never by a price; the player can never afford to open every workplace.
- **PRE-PILLAR (unconfirmed):** a capability opens when something the player builds or raises
  makes it possible, never on a clock or a stage line.
- **PRE-PILLAR (unconfirmed):** a gem pays a workplace's open hours, never a creature's role:
  who works, and at what, still falls out of raising. The gem only decides which workplaces
  stand open, and its paid time sits visibly on the station and burns down on its clock; it
  may be paid ahead without limit (user). It bends "Sacrifice through occupied shared state, not a
  price" and "Roles emerge from raising, never from a purchase", below.
- **A creature holds gems of its own (user):** it earns them by working and serving, spends
  them where another creature serves it, so a gem keeps passing creature to creature. A gem
  changes how much a creature works, never at what. Stolen gems stay marked as stolen, shown on
  the thief, and only they are the police's.
- **PRE-PILLAR (unconfirmed):** a resource pile is allowed as the forgone side of a choice
  on one object (save it, or take what it leaves), with its kind set by a sign the player
  sees. It bends "a reward is a new rule, verb, or board change", below.
- **A pillar spans the whole game and names no system.** A share, rate, or target for one
  system is that feature's tuning target and lives in the feature's docs.
- **Tone is a hard gate:** a Looney-Tunes goofy tower-defense farm. An idea that breaks the
  tone is out unless it can be reframed.
- **Natural on sight:** a thing is used only in ways its look suggests. Picture the scene
  before judging a mechanic; one that looks wrong in the game's world is out, however well
  it scores.
- **Add connections, not things:** new links between existing mechanics beat new nouns.
- **Sacrifice through occupied shared state, not a price:** a commitment takes up something
  another commitment needed.
- **A reward is a new rule, verb, or board change,** never a flat bonus or a resource pile.
- **Synergy comes from independent axes sharing one space or pool and competing for it,**
  never one piece reading or scaling another. If the player can't see the link, it is
  illegal.
- **A black box with a clear interface:** the player steers a system whose inside may be
  opaque. What the player can do to it, and what comes back out, must be understood on
  sight. Judge legibility at the interface, never demand that every inner step shows. The
  interface is three separate things: input, output, and the signs that report state. A
  sign is not an output. A need and the outcome that serving it produces are separate
  axes: never derive a need from the deficit of an outcome.
- **Roles emerge from raising, never from a purchase:** what a creature does falls out of
  its own state (stats, bonds, temperament) as the player grows and points it. A shop,
  station, or slot that hands out a role skips the raising and is out.
- **Ban hidden effects, not autonomy:** automatic behavior is fine when it reads on sight.
  Banned: effects that are hidden, illegible, or need a tutorial. Forcing manual per-unit
  actions to avoid passive effects is micromanagement.

## Rejected antipatterns (don't re-pitch)
- One-verb multiplex.
- Horizontal sprawl: a new tool or station per action.
- Stacked forecast constraints.
- A constraint dressed up as a choice.
- Memorization tables.
- Micromanagement and per-unit tracking.
- Player god powers (they solve the game).
- Frictionless hoarding.
- Grim sacrifice (breaks the tone).
- An element or state blob that erases per-unit clarity.
- Menu-driven action: UI is a readout or signal only.
- An imposed fuzzy taxonomy: a boundary you can't apply consistently. Let structure emerge;
  keep the clean binary and push the fuzzy split into a per-item attribute.


## Reasoning invariants
Full method: `~/.claude/skills/design-idea/references/design_method.md`.
- **Essence test, judged against the pillars, never the current structure.** Check the frame
  first and lead every answer with it; group a list of findings under the few top-level
  causes they share. At the top only disqualify and disambiguate; analyze deeply only what
  survives. A purpose can sit on the cost side: before calling an effect a duplicate,
  compare what each thing occupies and who operates it. An item the user already decided
  is not re-cut by this test; raise the doubt as a question and design the decided thing.
- **A written pillar decides a fork it matches;** never narrow its wording to keep a
  preferred alternative.
- **Nothing vague enters a decision.** For a system with state and 3 or more interacting
  variables, the SPECIFY artifacts force the definitions; a cell you can't fill is the
  disqualifier. A status word names one state: proposed, decided by the user, or built in
  the code that runs. A pick made on the user's behalf stays proposed until they confirm
  it, and an inherited design is re-checked against the running code before a build plan
  rests on it. "In the game" means reachable in play or kept by the user, never that its
  files exist.
- **Never build on an unproven premise.** A document, header comment, name, or roadmap
  line is not the code path that runs. Before claiming that removing one thing removes a
  behavior, trace what triggers it. A report of past work is bounded from the full record,
  never the newest entries. A look-alike rule is not the same purpose, so general guidance
  that resembles a rule does not justify cutting it. A complaint about feel is a symptom:
  confirm its mechanism before recommending a structure.
- **A question the code can answer is never asked of the user;** only judgment calls (what
  the game should do, taste, scope) go to the user.
- **A decision is real only if it beats the passive policy.** Run the do-nothing policy
  beside the active one on the real game loop; if both reach the same outcome, the choice
  is fake, usually because an automatic behavior does the player's job.
- **Size every duration against the game's own clock,** and check an event's premise in the
  code (is the distinction real, or does every case qualify?). A measured rate must run on
  the simulation's clock; a metric's title is not its definition. Numbers: `/probe`.
- **A match count is not a duplicate count.** Read every matching site before claiming N
  copies.
- **Run the output once before handing it over.** Code nothing executed is a guess.
- **Prune is not backtrack.** A prune removes surplus and leaves no hole; a backtrack
  reverses a commitment and leaves a hole to refill. Log each prune's reason.
- **Contradiction-check a law against its own examples before solidifying it.**
- **A converged architecture is not a converged execution plan.** Each slice still gets
  `/design-idea`, and answering an open question is not approval to execute. A plan covers
  every role its law names, the coordinating one included.
- **Priorities, in order:** fun and decision-density, simplicity, coherence, depth over
  breadth, reinforcing systems. Reject apparent agency that lowers decision-density. Stance:
  top-down; constraints are not direction; simple by default; standing text is timeless.
  When an incidental condition forces a special case into a core rule, put removing the
  condition beside bending the rule, and let the user pick. Judge a stake by what it makes
  the player build and stand around, not by how many systems it folds into one.

## Inadmissible criteria (check before any design judgment)
Before judging a design or structure, check the candidate against the antipatterns and
these criteria, then answer. This gates reasoning, not tool steps. The failure is skipping
the check, not a missing rule.
- **Effort is inadmissible for any choice, gameplay or structure:** build cost, blast
  radius, diff size, "whole rewrite", "smallest diff", "reuses existing", "matches existing
  code", "house pattern", "the established way", "already in the game", "not a new noun",
  "already there", "keep the old role too". Conformance is not merit; a coupling argument is admissible. The
  connections pillar is not a way around this: it counts only a link the player acts on in
  play, never a shared name or an existing asset. Judge gameplay on fun, decision-density, coherence, and fit to the
  compass. Judge structure on the end state: distinct-path count, reuse in the result,
  altitude, single-owner state, testability.
- **Literal instruction fidelity:** an explicit instruction, or a decided row in a design
  doc, is not open to your "already covered" judgment. Do every clause, or flag the gap and
  ask. A quantity or makeup the user states is built as stated; your "equivalent" is a
  proposal, never the build. A clause you turned into a question stays open until answered
  (write the unanswered rest to the active TODO), and a short reply after open questions is
  first read as the answer to one of them. Review exactly what was named. A question gets an
  answer and stops: it is not approval to build, and a discussion stays at the level asked.
  Fill an open slot from existing state; a new noun, stat or loop waits for the user, AFK or
  not, and so does whether a rejected antipattern covers a new case (show both options, name
  the conflict). Judge the option the user named, not a variant of its name; a detail you add
  to the user's call is your assumption, and so is a reason: when the user decides on a
  feeling ("i feel yes"), ask their reason before calling yours the main one. A request for ideas gets a wide pile, not a ranked
  pick. When a verb is loose, or a word could mean a game feature or a way of working, name
  the output in one line or ask before building; a version or milestone request anchors on
  the active design doc; a quality the user asks for lives in some actor or layer, so
  confirm which.

## Right altitude (rule: `CLAUDE.md` Right altitude)
- **Two tools matching one situation may be composition, not collision:** ask before
  excluding one. Placing a new owner: `~/.claude/PRINCIPLES.md` (abstract problem first).
- **Judge a document's scope by what it says it covers, not by its name.**
- **A document's lifetime must match what depends on it.** Anything a durable file points to
  is durable too; never give it a temporary label.

## Model cognition and collaboration
How your reasoning differs (no free quick check, residue, costly backtracking, forgetting as
a feature): the last section of `~/.claude/skills/design-idea/references/design_method.md`.
Catching and recording an error: `/rule`. Waiting on a background job in AFK mode: `/afk`.
- **Applying one change across many items:** pick the strategy by how the items are coupled
  (`.claude/skills/refactor/references/execution_strategies.md`). This is separate from the
  execution modes, which decide who closes a gate.

## Architecture principles
- **Match a value's lifetime to the memory horizon of the behavior it drives.** Learned
  behavior needs persistent state; a value that decays to zero can't hold it. Order decay
  rates by the lifetimes you intend. Time to zero is cap divided by rate, so a small cap
  with a slow rate can still fade first.
- **Every self-reinforcing loop needs a bootstrap, a termination, and a floor check.** Can it
  start from the neutral state? An entry gated on the loop's own output deadlocks. Can it
  end? A refresh whose gain outpaces its decay never dies. Can the low end climb out? A
  clamped response curve steeper than its input's real spread leaves a dead zone that traps
  whoever falls in. Run all three on every feedback edge.
- **A formula's neutral point must equal the measured resting value of what it reads.** A
  "normal" set above where the state actually rests leans every roll one way, and a loop
  gated on that roll never starts. Measure the resting value in the real loop before tuning.
- **An aggregate that drives visible state must not fall when a weak item joins.** Sum on a
  fixed scale, not a mean: a mean makes each new neutral member a hidden penalty.
- **A mechanic that needs a same-kind pair must make same-kind pairs meet,** or its rate
  scales with the square of that kind's share and collapses in a mixed population.
- **One driver per shared interaction, not N pollers.** A rotating single-holder token keeps
  a multi-party interaction sequential, with no locks and no double-driving. Any member's
  update heals a stale token.
- **Separate rates, not loops.** One deterministic update loop plus N cheap gates, never N
  schedulers. Decouple deciding from acting with a one-way intent buffer: deciding writes,
  acting reads, facts flow back read-only.
- **Committed states are sticky:** event-driven and single-owner, never re-derived each tick
  by several pollers sharing fields. Isolated unit tests stay green while the game breaks,
  so test the real per-tick order end to end.
- **Roles and dependencies:** Coordinator, Component, Service, Util; a parent coordinator is
  the only place state changes, every parent-to-child edge is facts in, intents out. The
  full law and layout: `docs/LAW_classification_cube.md`.
- **Reuse existing primitives before writing new ones.** Two things that look alike or
  appear together are not one helper when their behavior differs.
- **Time-based progression runs on the game's dilated clock, never wall time**
  (`docs/LAW_time_dilation.md`).
- **Tuning lives in each module's config,** not scattered through code.
