# Experiment 01 — Does richness do anything once asynchrony is controlled?

**Extends:** `model_a_insurance_test.py` (do not start fresh — the environment generator,
the niche-match kernel and the plot runner are all reusable as-is).
**Tests:** property **P1** in `01-Q2-convergent-properties.md`.
**Estimated work:** one session to build and run, most of it plotting.

---

## The problem with the model as it stands

Two things are worth saying plainly before the design, because both are critiques of
code already in this repo.

**1. Richness and asynchrony are confounded.** `make_diverse_plots(n_strats, n_plots)`
draws `n_strats` strategies at random from the twelve fixed optima. A six-strategy plot
almost always spans more of the environmental axis than a one-strategy plot, so "how many
strategies" and "how spread out their responses are" move together and cannot be told
apart in the output. The insurance hypothesis, in Loreau & de Mazancourt's sharper form,
says the stabilising ingredient is **asynchrony** — richness is a proxy. As written, the
model cannot distinguish the hypothesis from its proxy. That is the whole experiment.

**2. "Diversity costs mean output" is partly an assumption, not a finding.** In
`group_output`, each strategy contributes

```python
output = niche_match * ext * (1 - coop) / n
```

The `/ n` divides total output by the number of strategies. A diverse plot is *mechanically*
penalised on mean output before any environmental dynamics run. So the README's framing —
"pure diversity buys resilience but costs mean output" — is at least in part reporting an
allocation assumption back to you. The assumption is defensible (attention and resources are
finite and split), but it must be labelled as a *parameter*, not a result, and it must be
varied. Right now it is hard-coded and invisible.

## Design

**Decouple richness from response spread.** Replace the random draw with constructed plots:
fix richness `n`, then place the `n` optima symmetrically about 0.5 with a controlled spread
`s`. At `s = 0` all `n` strategies share an identical optimum — richness `n`, zero response
diversity, the clone control that does not currently exist. At `s = max` they are evenly
spaced across [0, 1].

**Sweep:**

| Factor | Levels |
|---|---|
| richness `n` | 1, 3, 6, 12 |
| optima spread `s` | 0, 0.05, 0.10, 0.20, 0.35, max |
| volatility | 0.01, 0.03, 0.06, 0.10 (the existing `VOLS`) |
| protocol | none; thin (`max_ext 0.45`, `min_coop 0.15`) |
| allocation exponent `α` in `/ n**α` | 0, 0.5, 1.0 (1.0 = current behaviour, 0 = no dilution) |

20 environment seeds × 10 plots per cell, 2000 steps — the existing harness values.
(`n=1` has only `s=0`; skip the impossible cells.)

**Measure, per plot:**
- mean output, and coefficient of variation of output
- minimum 100-step rolling output
- P(resource drops below 20% of capacity at any t)
- **measured asynchrony φ** — Loreau & de Mazancourt's community-wide synchrony index
  (standardised 0–1, independent of component count), computed on the per-strategy output
  series. This is the new instrument and it is the point; `group_output` currently sums
  strategies internally and discards the per-strategy series, so it needs to return them.

## The graph

**Panel A — the test.** x-axis: *measured* asynchrony φ. y-axis: CV of output. One point per
plot. Colour by richness. Facet by volatility, and overlay protocol / no-protocol.

- **If P1 holds:** all points collapse onto one curve in φ. Richness colours are scrambled
  along that curve — meaning richness adds nothing once asynchrony is known.
- **If P1 fails:** the richness colours separate into parallel bands. Something other than
  asynchrony is stabilising the system, and the next job is finding out what.

**Panel B — the protocol knee.** Sweep `max_ext` ∈ [0.25, 1.0] and `min_coop` ∈ [0, 0.4] at
fixed high richness and high spread. Heatmap: mean output, overlaid with a contour of
P(collapse). The question is *how thin the protocol can get before the insurance benefit
collapses* — this is the quantitative claim most likely to be genuinely yours rather than
already in the commons literature.

**Panel C — the honesty panel.** Panel A repeated at α = 0, 0.5, 1.0. This shows how much of
"diversity costs output" is the allocation assumption. Publish it even if it is unflattering;
especially then.

## What would surprise us

1. **Richness bands persisting in Panel A after conditioning on φ.** The most likely culprit
   is the `/ n` divisor interacting with niche coverage, which would make it an artifact
   rather than a finding — Panel C is there to catch exactly this. If the bands survive
   α = 0 as well, that is a real second mechanism and worth chasing.
2. **The protocol's benefit not shrinking as φ → 0.** A protocol should only help when there
   is something to protect. If a thin protocol helps monocultures and clone-plots just as
   much as it helps genuinely diverse ones, then the protocol is not "enabling insurance" —
   it is just a resource cap, and the interaction story in `01-Q2` is wrong. This is the
   single cleanest way to kill my own reading of your result, which is why it is here.
3. **A cell that is simultaneously best on mean output and best on P(collapse)** — that would
   be evidence against the strong form of P5, and would need very careful checking for a bug
   before being believed.

## What this does not test

Nothing here touches anticipation (P2), the Price partition (P4), or cross-scale coupling
(P6). All three are absent from every model in this repo. P4 is the cheapest to add next:
it is a variance decomposition over data the group-competition model already produces.
