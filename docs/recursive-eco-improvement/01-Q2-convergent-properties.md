# Q2 — Who has good claims on "adaptive"?

*Every source named here has a row in `SOURCES.md`. Nothing here has been read in full;
read-status is `SUMMARY` throughout. Treat the reasoning as mine and the citations as
pointers, not as reportage from primary texts.*

---

## The one-page answer

At least eight traditions have independently tried to say what makes a system persist,
and they do not form a consensus so much as a set of partially overlapping shadows.
Cybernetics (Ashby) says a regulator must carry at least as much variety as the
disturbances it absorbs. Autopoiesis and enaction say a system must produce its own
boundary — and Di Paolo's 2005 amendment, which is the sharpest single move in this
literature, says that self-production alone is *not* adaptivity: a system that merely
maintains itself until it dies has no way to tell it is approaching death. Adaptivity
is the added capacity to sense and regulate one's distance from the viability boundary
*before* reaching it. The free energy principle says the same thing in a different
dialect and loses falsifiability in the process. Resilience ecology (Holling) contributes
the only property here that arrived with a measurement attached from the beginning: the
size of shock a system absorbs before it reorganises into a different regime, and the
explicit claim that optimising a system for mean output buys that resilience away.
Biodiversity–stability theory (Yachi & Loreau; Loreau & de Mazancourt) refines this into
something unusually crisp — the stabilising ingredient is not diversity but *asynchrony*,
the tendency of components to fail at different times. Commons governance (Ostrom) is
the only tradition in the list with a real empirical base behind its property list:
Cox, Arnold & Villamayor-Tomás reviewed 91 studies and found the eight design principles
broadly supported. Evolutionary game theory (Nowak; Axelrod) contributes threshold
inequalities — conditions under which cooperation beats defection — which are the most
precisely stated claims anywhere in this survey. And the major-transitions literature
(Maynard Smith & Szathmáry) contributes the awkward one: every time evolution built a
new level of organisation, it did so by *suppressing competition inside the new unit*.

They contradict each other in one place that matters. The insurance tradition says keep
variety; the major-transitions tradition says suppress it. This is not a semantic clash —
they are talking about different axes, and almost nobody says so out loud. Insurance
wants diversity in *how components respond to the environment*. Transitions want
uniformity in *how components treat each other*. A system can have both, and I think the
"thin protocol" result already sitting in this repo is an instance of exactly that
combination rather than a new phenomenon: `max_ext` and `min_coop` constrain how each
strategy treats the commons while leaving each strategy's environmental optimum untouched.
If that reading is right, the interesting claim is not "protocols help" — it is that the
two traditions are describing orthogonal dimensions and the adaptive configuration is
*diverse on the response axis, uniform on the extraction axis.*

They also fail differently. Ashby's law is a theorem, not an empirical property; you
cannot falsify it, you can only ask whether real regulators approach its bound, which is
a different and much better question. The free energy principle in its universal form is
close to unfalsifiable and should be quarantined from the operational list; the active
inference model class built on it is fine. Wong et al.'s proposed law of increasing
functional information is the most ambitious claim on the table — a selection law
covering non-living systems — and it is genuinely contested (Root-Bernstein's PNAS letter;
the authors' reply). Assembly theory is worse off than contested; treat it as a case
study in dispute, not as evidence.

The honest summary: roughly five properties survive contact with a falsifier, two survive
only if you specify a coupling that most authors leave vague, and one — the general
"increasing functional information / open-ended novelty" family — does not survive at all
in its universal form. That last one is the seductive one, so it is the one to be hardest on.

---

## The convergent-properties shortlist

Ordered by how much weight they can bear. Each is stated as a claim that could be wrong.

### P1 · Response asynchrony, not diversity as such
**Traditions:** biodiversity–stability (Yachi & Loreau 1999; Loreau & de Mazancourt 2013),
cybernetics (Ashby's requisite variety), resilience ecology (Holling — response diversity
across scales), cultural group selection (Boyd & Richerson — between-group variance).

**Claim (narrow form):** aggregate output variance falls with the *asynchrony* of
component responses to environmental fluctuation. Component count is a proxy for
asynchrony, not a cause of stability.

**Falsifier:** hold measured asynchrony constant (Loreau & de Mazancourt give a
community-wide synchrony index standardised 0–1 and independent of component count) and
vary component richness. If richness still explains variance reduction after conditioning
on asynchrony, the claim in this form is wrong and something else is doing the work.
**This is directly testable in `model_a_insurance_test.py` and is Experiment 01.**

**Status:** operationalisable, strongest item on the list.

---

### P2 · Anticipatory regulation — the system acts before viability is breached
**Traditions:** Di Paolo 2005 (this *is* his definition of adaptivity, and he explicitly
distinguishes it from self-maintenance), active inference (expected free energy), Barrett's
allostasis, and — by contrast — Ashby's ultrastability, which is reactive and therefore
marks the lower bound.

**Claim:** a regulator whose corrective action leads the disturbance outperforms an
otherwise identical regulator whose action lags it, and the gap widens with volatility.

**Falsifier:** measure the cross-correlation between disturbance and corrective response;
find the lead time. If a zero-lead (purely reactive) regulator matches an anticipatory one
on time-to-collapse across the whole volatility range, anticipation is decorative in that
system. Note this falsifier can come out *either way per system* — which is the point;
it converts "anticipation is adaptive" from a slogan into a measurement.

**Status:** operationalisable. Currently absent from every model in this repo — all three
ABMs are reactive. That is a gap, not a flaw.

---

### P3 · Monitoring with graduated sanction, cheap at the margin
**Traditions:** Ostrom (design principles 4 and 5), Nowak 2006 (direct and indirect
reciprocity, each with a threshold inequality), Axelrod (retaliation), Boyd & Richerson
(norm enforcement maintaining between-group variance).

**Claim:** commons persist longer when defection is detected locally and punished
proportionately, *and* when the cost of enforcement is below the cooperation surplus it
protects. The second clause is the part usually dropped, and it is the part that makes
the claim falsifiable.

**Falsifier:** groups with monitoring and sanctions do no better than groups without, at
matched resource predictability — or enforcement cost exceeds the surplus, in which case
the institution is ritual rather than adaptive. Cox et al. 2010 is the existing empirical
test bed (91 cases); the sanction-cost clause is the part their review does not settle.

**Status:** operationalisable, and the only property here with a real observational
literature behind it rather than a modelling literature.

---

### P4 · Suppression of within-unit competition as the price of a new level
**Traditions:** Maynard Smith & Szathmáry (explicit and central), Boyd & Richerson
(conformist transmission compressing within-group variance), Nowak (the group-selection
rule), Ostrom (collective-choice arrangements).

**Claim:** a system acquires a new unit of selection only by reducing variance *within*
that unit relative to variance *between* units.

**Falsifier:** a Price-equation partition across a putative transition showing no drop in
the within/between variance ratio. In a model: raise within-group competition and, if the
between-group selection response does not weaken, the claim fails there.

**Status:** operationalisable via the Price partition, which nothing in this repo currently
computes. Adding it is cheap.

**Tension to keep visible:** P4 pulls against P1. See the one-page answer — I believe they
are orthogonal axes, but that is a hypothesis, not an established reconciliation, and it
should be labelled as mine.

---

### P5 · The efficiency–resilience tradeoff
**Traditions:** Holling 1973, Yachi & Loreau (mean versus variance), Gunderson & Holling's
adaptive cycle.

**Claim (narrow form):** systems tuned to maximise mean output under observed conditions
lose disproportionate performance under unobserved conditions.

**Falsifier:** find a parameter regime that is simultaneously at maximum mean output and
maximum shock resistance. **Partial evidence against the strong form already exists in this
repo** — "thin protocol + diversity recovers most of the output while keeping the insurance
benefit" is precisely a point off the naive frontier. This does not refute the tradeoff;
it says the frontier is a Pareto surface with a knee, not a hard wall. Do not let this
become "there is no tradeoff."

**Status:** operationalisable; already partially tested here; the *shape* of the frontier
is an open and genuinely interesting question.

---

### P6 · Nested structure with slow outer cycles buffering fast inner ones
**Traditions:** Gunderson & Holling's panarchy ("remember" and "revolt" cross-scale
couplings), Ostrom (design principle 8, nested enterprises), Maynard Smith & Szathmáry
(hierarchy), Levin (multi-scale competency).

**Claim:** removing cross-scale coupling increases collapse probability after shock.

**Falsifier:** a single-scale system matching a nested one on recovery time across shock
magnitudes.

**Status:** **operationalisable only if you specify the coupling.** "Panarchy" as usually
written is a picture, not a mechanism. Stated as "the outer scale supplies X at rate Y
after a shock," it is testable; stated as "everything is nested," it is not. Marked
**conditional**.

---

### P7 · A boundary the system maintains and can act to defend
**Traditions:** autopoiesis (operational closure), free energy principle (Markov blanket),
Ostrom (design principle 1, clearly defined boundaries), major transitions (the unit of
selection).

**Claim:** persistence requires a boundary that is both statistically real and actively
defended.

**Falsifier:** Ostrom's version has one — commons with undefined boundaries persisting at
equal rates to those with defined boundaries, controlling for resource type — and Cox et
al. 2010 is the place to check whether it has already been run. The autopoietic and FEP
versions do **not** have a workable falsifier: "a system that persists indefinitely with
no statistical boundary between internal and external states" is not an observation anyone
could make.

**Status:** **split verdict.** Ostrom's boundary principle: operationalisable. The
autopoiesis/FEP boundary: **slogan, not specification** — keep the concept, drop the claim
that it is doing explanatory work.

---

### P8 · Increasing functional information / open-ended novelty generation
**Traditions:** Wong, Cleland & Hazen et al. 2023 (law of increasing functional
information), Kauffman (adjacent possible), Hughes et al. 2024 (open-endedness as novelty
plus learnability), assembly theory.

**Claim:** persistent evolving systems accumulate functional information under selection.

**Falsifier:** I cannot state one that does not smuggle in the answer. "Functional
information" requires a pre-specified function, and once the function is specified the law
is either trivially true or measuring something narrower than advertised. Open-endedness in
Hughes et al. is explicitly *observer-relative* by construction, which makes it a useful
engineering target and a bad natural law. Assembly theory's version is under technical
attack (see `SOURCES.md` §E).

**Status: slogan, not specification** — in the universal form. Fix an observer and a
function and it becomes a fine local metric. Do not build the programme on it, and be
suspicious of how good it sounds.

---

## Two direct answers you asked for

**"Did I rediscover an Ostrom result?"** Partly, and you should expect to find it.
`max_ext` is an appropriation limit and `min_coop` is a contribution floor; together they
are a crude version of Ostrom's principle 2, congruence between appropriation rules and
local conditions. What is *not* straightforwardly Ostrom is the interaction term — the
claim that a thin protocol is what lets response diversity keep paying off. That
interaction lives closer to the social-ecological-systems / "governing for resilience"
literature than to *Governing the Commons*, and I have not verified how much of it is
already published there. **Assume it is until you have checked.** The part most likely to
be genuinely yours is quantitative rather than conceptual: *how thin can the protocol get
before the insurance benefit collapses* — nobody plots that curve because nobody has your
particular model. That is Experiment 01's second panel.

**"Is 'recursive eco improvement' a rebranding of open-endedness?"** No, and I think it is
closer to a correction. Open-endedness as Hughes et al. define it optimises for novelty
that remains learnable *to an observer*; there is no viability constraint anywhere in the
definition, and the substrate the system runs on does not appear. Your question is about a
system embedded in a host it can damage. The two share only "no fixed objective." Stated
precisely, your programme is something like **open-endedness subject to a viability
constraint on the substrate** — which is a well-posed question that the open-endedness
literature has not asked, and which Sheth et al. gesture at from the safety side without
formalising. That framing is defensible. The vaguer framing — "properties that make a
system adaptive with the biosphere" — is not yet a research question, because "with" is
doing unexamined work. Pin "with" down to a measurable (substrate state stays inside
viability bounds while the agent's objective improves) and you have something.
