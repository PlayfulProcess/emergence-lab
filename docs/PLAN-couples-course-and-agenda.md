# Plan — the couples line: one course, one agenda, and where it all lives

*Written 6 September 2026, after building Model 03 (`models/dyad-lab.html`).*

This is the working plan for the couples/relationship line of the lab. It records a
decision about repo layout, the design of the course, the research agenda, and the one
question still open (where "overflow" belongs in the stack).

---

## 0. The decision: Option C — split by layer

Three options were on the table: give Overflow its own repo, skew `recursive-repatterning`
into a couples platform, or split by layer. **Option C is the call.**

| Layer | Home | Why |
|---|---|---|
| **Engine** — the models, the sweeps, the failures | `emergence-lab` | Already the modelling repo. Already holds the ABM tradition, the Barrett/active-inference reading line, and `overflow-lab.html`. Its stated method — *reproduce before inventing* — is exactly right here. |
| **Surface** — course, tools, the couples-facing pages | `recursive-repatterning` | Already has the audience surface, the course viewer, the tools index, and four relational schools (`gottman-method`, `eft-bonds`, `attachment-theory`, `nvc-needs`) already carrying `evidence_tier` metadata. Added as a **branch**, not a rebrand. |
| **Argument** — the prose | `book-repo` (NWTO ch. 11 "The lip", ch. 17 the lab) | Unchanged. Cites the engine. |

**A new repo has one trigger and it has not fired yet:** the moment a model produces a
result someone outside needs to rerun and cite. Then it splits out with history. Not before
— a repo with no result in it is a folder with extra steps.

**Why not skew repatterning wholesale (Option B):** its own `CLAUDE.md` rule 7 forbids
totalising scope, and its value is precisely that it holds Rasa beside DBT beside the
Affektenlehre. Narrowing a deliberately broad library to one relational domain trades away
the only thing it has that nothing else does. A couples *branch* gets the reach without the
cost.

---

## 1. The claim is psychoeducational, not clinical

Stated once, plainly, because it sets the ceiling for everything below:

> **A simulation cannot make a claim about people true.** It can show that a story is
> internally coherent, generate hypotheses, and teach a mechanism you can feel in your
> thumb. That is the whole of what is on offer here.

This is a lower bar than a clinical claim and it is the *right* bar — the couples dossier
(`book-repo/books/what-survives-the-number/research/couples-therapy-dossier.md`) already
established that the efficacy literature is thin and allegiance-inflated. A lab that
claimed to settle it would be making the field's own mistake.

Concrete floor, inherited from repatterning's creed ("never state a feeling-label as a
diagnosis or as something to obey"), in its modelling form:

- **Never state a simulation output as a prediction about a person.**
- No scoring, no "your couple type", no persistence, nothing sent anywhere.
- The partner labels are **A and B**, not husband and wife.
- Every published model carries a *what this cannot tell you* table. Model 03 has one.

**Two use cases, cleanly separated.** *You driving it to illustrate an idea* is safe today.
*A couple using it alone* additionally requires the lessons on base rate and on what the
model cannot say — which is why those are lessons 7 and 8 of the course, not appendices.

---

## 2. Model 03 — The Dyad Lab (built, runs)

`models/dyad-lab.html`. Single file, no build, no dependencies, runs offline.

**Part one — the Gottman–Murray form, drawn.** Two coupled difference equations: inertia,
uninfluenced baseline, an asymmetric influence function with a negativity threshold, plus
repair and damping. Rendered as (a) the turn-by-turn conversation and (b) **the two
null-clines and their intersections** — which is the visual this model deserves and rarely
gets. Steady states are found by root-scan and classified stable/unstable from the 2×2
Jacobian. Raise the cold-side influence past ~1.4 and a second stable state appears with an
unstable watershed between them: same couple, same dials, two destinations depending only
on where the conversation opens.

**Part two — a population of dyads.** 400 couples, seeded RNG. This is the part that
answers the 94%/29% question, and it does it with two ordinary mechanisms, both on dials:

| Setting | Looking back | Looking forward | PPV | Type explains |
|---|---|---|---|---|
| Default | 95% | 84% | 68% | 35% |
| Life-after = 0 | 95% | 97% | 94% | 47% |
| Base rate 45% | 91% | 85% | 82% | 39% |
| Base rate 11% | 97% | 90% | 48% | 22% |
| **Couples identical** | **95%** | 51% | **32%** | **0%** |
| Identical + base 11% | 97% | 53% | **16%** | 0% |

Two findings worth keeping:

1. **The gap needs no dishonesty.** Base rate plus a future that contains new information
   produces it entirely. Set "how much life happens after" to zero and prediction becomes
   near-perfect — the gap *is* time passing.
2. **A 95% backward fit survives having nothing to fit.** With every couple identical —
   no types, no traits, type explains 0% of the outcome — the backward-looking number is
   unchanged. **An outcome distribution that looks like types can be produced with no types
   in it.**

**Hedge recorded on the page and here:** the no-types PPV of ~32% is *near* Heyman & Smith
Slep's 29%. That is a coincidence of dial positions, not a reproduction. Nothing is fitted
to any study. Moving any slider moves it.

### Calibration failure, logged

The first version chose its classification threshold by **maximising accuracy**. At a low
base rate that degenerates into "predict almost nobody separates" — 96% accuracy, two
couples flagged, a meaningless PPV of 100%. A rule of mine was deciding the answer, which
is failure #4 in the same family as the three logged in `LAB-DESIGN.md`. Replaced with
calibration at a **target sensitivity of 80%**, the way a screening instrument is actually
set. Noted on the page rather than quietly fixed.

---

## 3. The population *is* the instrument — the computational-economics move

The design principle behind part two, stated so it doesn't get lost:

**Do not analytically solve the representative couple. Simulate a heterogeneous population
and let the aggregate emerge.** The Gottman–Murray tradition solves one dyad's equations
and reads off its steady states — the same move microeconomics makes with a representative
agent, and it inherits the same blind spot: an aggregate produced by a distribution of
different agents is not the behaviour of the average agent.

This lab does the agent-based version instead. The unit of analysis is the **population of
dyads**; the "price" that emerges is the population-level outcome rate and the shape of its
distribution. That reframing is what makes the no-types result available at all — it is
invisible to any analytic solution of a single couple, because a single couple has no
distribution to confuse you.

Direct lineage: **Gode & Sunder (1993)**, already replicated in this repo as
`models/zero-intelligence.html`. Zero-intelligence traders find equilibrium prices because
the *market structure* does the work, not the traders' reasoning. The couples analogue is
exactly parallel: the spread of relationship outcomes may be substantially a property of
the interaction structure and of time, not of a taxonomy of couples. That is a real,
testable alternative hypothesis, and this lab is where it gets tested.

---

## 4. The course — one course, two beats per lesson

**Answering the question directly: one course, not two.** Splitting "how to run the models"
from "what it means on a Tuesday" would put the mechanics in one place and the only reason
to care in another. Instead **every lesson has two beats** — a *lab beat* (one dial, one
aha, one under-the-hood panel) and a *life beat* (the same idea, as a question to sit with,
never as advice).

Working title: **"Two Rims" — a course in moving one dial at a time.**

The pattern is lifted wholesale from AI 101 (`recursive-eco/apps/landing/pages/courses/
research/ai-101/PLAN-ai-101-course.md`): one concept per lesson, one toggle per lesson, big
readable text, works on a phone, ends with a "did you see it happen?" moment. **Yardstick:
a curious 70-year-old must enjoy it.** Where AI 101's under-the-hood panel shows the actual
request JSON, this one shows the actual equation and the term the slider touches.

| # | Dial | Lab beat — the aha | Life beat — on a Tuesday |
|---|---|---|---|
| 1 | Inertia | How much of this turn carries into the next. Set it high and nothing lets go. | How long does a bad morning get to own the afternoon? Inertia is a number, and numbers can be different. |
| 2 | Baseline | Where each person drifts *with nobody in the room*. | Some of what I feel here is not about here. Which part of my baseline am I asking this relationship to fix? |
| 3 | Influence | Turn it on and the pair settles somewhere neither baseline predicts. | The couple is a third thing in the room, with moods of its own. |
| 4 | Threshold | Where the steep slope starts. Hair-trigger vs. lets-a-lot-pass. | What counts as bad enough to react to — and when did we decide that? Both settings cost something. |
| 5 | Repair | A term with a **trigger**: it only fires once the other has gone below the threshold. | Repair is timing, not sweetness. Early and clumsy beats late and eloquent. |
| 6 | Two stable states | Same dials, two destinations, decided by where you open. | "We always end up here" is a property of the shape, not a verdict on anyone's character. |
| 7 | Base rate | Accuracy goes **up** while PPV goes **down**. | How to read any statistic about your own life: an accurate test can still be wrong most times it speaks. |
| 8 | Life-after | Set it to zero and prediction becomes near-perfect. | Nobody can tell you how this ends, and the reason is not that they lack a good enough instrument. |
| 9 | **Your own run** | Change a parameter. **Write down what you expect. Then press run.** | Being wrong on purpose, cheaply, in a place where it costs nothing. |

**Lesson 9 is the one that makes it a course in modelling rather than a course in
relationships.** The discipline it teaches — predict before you run, and keep the
prediction where you can't edit it — is exactly what `LAB-DESIGN.md` did with H1–H5, and
exactly what the field under critique mostly did not do.

**Ends in a usable tool**, per the house pattern: the last screen is the bare lab with all
dials exposed and a print/export of *your* nine written predictions versus what happened.

### Where it ships

`recursive-repatterning`, as a course (its `course/` pipeline and `pages/course-viewer.html`
already exist and work), with the lab embedded or linked from `emergence-lab`. It joins
`tools/_tools.json` beside the NVC and Living-Into-Values tools, which is where a person
looking for a practice already lands.

---

## 5. The research agenda — MSW-compatible, no participants needed

Rungs R1–R3 require **no human subjects**, which is what makes them fit a study timeline.

- **R0 — Reproduce.** Gottman & Murray (2002) from the book, seeded and rerunnable.
  *Reproduce before inventing.* Model 03 implements the published *form*; R0 is the version
  with their constants and their reported steady-state structure, checked against the text.
  ⟶ *Model 03 is the prototype; R0 is the honest version of it.*
- **R1 — Re-examine.** The gap between what the model claims and what got sold. The dossier
  is already the evidence base; Model 03 part two is already the demonstration. This is a
  methods piece with zero data collection and it is the most publishable thing in the line.
- **R2 — Extend (the original contribution).** Give each partner a **reserve / body-budget
  state variable** — Barrett's allostasis as a term rather than a metaphor. Gottman–Murray
  has no such variable. Then H3 from the Overflow Lab transposes to the dyad: *a gift given
  from depletion costs more than it delivers*, as a two-person result. This is the rung
  where the two lines of this repo actually meet.
- **R3 — Models as interfaces, made runnable.** Same dyad, three rule-sets: Gottman-shaped,
  attachment/EFT-shaped (pursue–withdraw), NVC-shaped. Test each against the one pattern
  that survives across the literature — **demand/withdraw**, *r* ≈ .36 (Schrodt, Witt &
  Shimkowski 2014). If several different machines all reproduce the one measured pattern,
  that is a finding about how much any of the machines can claim — and it is repatterning's
  founding creed ("the substrate, and interfaces above it") demonstrated rather than
  asserted.
- **R4 — Real data.** Human subjects, IRB, consent, supervision. A different kind of
  project. Do not drift into it by accident.

**Pre-register R2 and R3 the way `LAB-DESIGN.md` pre-registered H1–H5** — hypotheses
written down before the first run, and the regions where they fail published alongside the
regions where they hold.

---

## 6. Open — where "overflow" enters the stack

Still undecided, and worth leaving undecided a little longer.

The current position: **couples are one specific instance of overflow, not its home.** That
argues for keeping "overflow" as the *thesis under test* — a school in repatterning, a book
in NWTO, a hypothesis in the Overflow Lab — and **not** as the brand on the couples-facing
surface. A couple sitting down with a model should not be seated inside a conclusion.

Reasons to keep it separate, for now:
- The couples work has to be usable by someone who rejects the overflow thesis entirely.
  If it isn't, it is advocacy wearing a lab coat.
- R2 is precisely the test of whether overflow says anything a dyadic model needs. **If R2
  finds nothing, the couples line should not be carrying the name** — and that is the
  honest reason to wait.
- Conversely, if R2 works, the reserve variable *earns* the name from inside the model
  rather than being applied to the outside of it.

**Decision rule: let R2 decide.** Build the reserve variable; if the dyad needs it, overflow
enters the stack as mechanism. If it doesn't, overflow stays a book.

---

## 7. Next, in order of confidence

1. ~~Model 03, parts one and two~~ — **done, runs, failure logged.**
2. **R0** — the faithful reproduction with the published constants. Bounded, checkable
   against a printed source, and the only rung with a right answer to find.
3. **The course** — lessons 1–6 are already fully supported by the built lab; 7–9 need only
   text. Lowest-risk build in the whole plan.
4. **R2** — the reserve variable. The first genuinely new thing, and the decider for §6.
5. **R1 write-up** — whenever the dossier and part two are wanted in one place.

*CC-BY-SA-4.0.*
