# emergence-lab

Computational models of how minds, groups, and cultures adapt — built to be run, not just read. This repo holds two connected lines of work:

1. **Cultural & group-selection ABMs** (already here) — agent-based models testing the insurance hypothesis and cultural group selection under environmental volatility.
2. **Evolutionary & predictive models of mind** (active, new) — reproducing and extending the modeling traditions of Donald Hoffman (Interface Theory of Perception) and Lisa Feldman Barrett (theory of constructed emotion), building toward original models of my own.

Both lines share a method: **start from a small reproducible simulation, understand it by running it, then push past it.**

---

## 1. What's already here

| File | Model | Tests |
|---|---|---|
| [`cultural_resilience_abm.py`](cultural_resilience_abm.py) | Groups extract/contribute to a shared resource pool under varying cooperation & extraction strategies | Recalibrated extraction/regeneration/population dynamics |
| [`model_a_group_competition.py`](model_a_group_competition.py) | Groups (not individuals) compete; groups vary in internal cultural diversity (1–12 strategies) | Cultural group selection (Boyd & Richerson) |
| [`model_a_insurance_test.py`](model_a_insurance_test.py) | Fixed-strategy "plots" tracked over a fluctuating environment, no group selection | Yachi & Loreau's insurance hypothesis (diversity reduces variance without cutting mean) — direct analogue of Tilman's Cedar Creek experiments |
| [`cultural_resilience_abm.jsx`](cultural_resilience_abm.jsx) | React/Recharts dashboard | Visualizes the above three scenarios (Monoculture / Pure Diversity / Protocol + Diversity) |

**Early finding across these:** pure diversity buys resilience but costs mean output; a *thin protocol* (minimum cooperation, maximum extraction) layered on top of diversity recovers most of the output while keeping the insurance benefit. This is the throughline into the mind-modeling work below — both are about what structure (biological, cultural, perceptual) survives selection pressure.

---

## 2. New line: evolutionary & predictive models of mind

### The question

Donald Hoffman and Lisa Feldman Barrett both argue that experience is *constructed*, not read off reality — but they build that claim with completely different machinery. Understanding both well enough to model them is the goal here.

| | Donald Hoffman | Lisa Feldman Barrett |
|---|---|---|
| **Core claim** | Perception is a species-specific *user interface* shaped by natural selection for fitness, not truth | Emotion (and much of experience) is *constructed* by the brain interpreting bodily signals through learned concepts |
| **Key mechanism** | Evolutionary game theory + Bayesian decision theory → Fitness-Beats-Truth (FBT) theorem | Predictive processing / allostasis — the brain anticipates bodily needs and categorizes interoceptive signals in context |
| **What's "real"?** | Consciousness is fundamental (*conscious realism*); physical objects are icons, not truth | Brain and body are real biological systems regulating an energy budget; concepts construct how regulation is *experienced* |
| **Scope** | Perception of external reality (vision, space, objects) | Interoception, affect, emotion, the self |

They overlap on rejecting naive realism and treating the brain as a prediction engine, but diverge sharply past that — Hoffman toward metaphysics (idealism), Barrett staying inside biological neuroscience with a clear clinical path (see the "body budget" framing of depression, anxiety, and somatization as allostatic dysregulation).

### Build order (reproduce before inventing)

Deliberately *not* a 6-month prerequisites-first curriculum. Each step is runnable before the next is needed; math and neuroscience background gets picked up just-in-time per project.

1. **Fitness-Beats-Truth game** — agent-based sim of "truth-perceiving" vs. "fitness-perceiving" critters competing for resources across generations (Hoffman's own illustration of the FBT theorem). No prerequisites beyond basic probability.
2. **Leaky integrate-and-fire neuron** — the smallest model that teaches real spiking dynamics. Cheap to run, immediately visual.
3. **Toy active inference agent** — a minimal predictive-processing agent that minimizes surprise about its own internal state (using [pymdp](https://github.com/infer-actively/pymdp)'s discrete-state framework). This is where Barrett's "body budget" language becomes a running model instead of a metaphor.
4. **Extend the existing ABMs** — cross the two lines: what happens if `model_a_group_competition.py`'s groups also have to maintain an internal "body budget," or if strategy selection follows an FBT-style fitness-over-truth rule instead of a fixed niche-optimum?
5. **Original model** — once 1–3 are running and understood, define a specific question neither Hoffman nor Barrett modeled directly and build for it.

### Bibliography

**Books**
- Donald Hoffman — *The Case Against Reality: Why Evolution Hid the Truth from Our Eyes* (2019)
- Lisa Feldman Barrett — *How Emotions Are Made: The Secret Life of the Brain* (2017)
- Peter Sterling & Simon Laughlin — *Principles of Neural Design* (2015) — metabolic/efficiency constraints on neural systems
- Peter Dayan & Larry Abbott — *Theoretical Neuroscience* — standard mathematical grounding for spiking/rate models
- Eugene Izhikevich — *Dynamical Systems in Neuroscience*

**Core papers to reproduce or read closely**
- Prakash, Stephens, Hoffman, Singh & Fields (2021), ["Fitness Beats Truth in the Evolution of Perception"](https://sites.socsci.uci.edu/~ddhoff/FitnessBeatsTruth_apa_PBR.pdf), *Acta Biotheoretica* 69(3) — states and proves the FBT theorem
- Friston (2010), ["The free-energy principle: a unified brain theory?"](https://www.nature.com/articles/nrn2787), *Nature Reviews Neuroscience* 11
- Heins et al. (2022), [pymdp: A Python library for active inference in discrete state spaces](https://arxiv.org/abs/2201.03904) — the implementation companion to the theory above
- Hodgkin & Huxley (1952) — original action potential model (historical reproduction target)
- Boyd & Richerson — cultural group selection (already the basis of `model_a_group_competition.py`)
- Yachi & Loreau — the insurance hypothesis (already the basis of `model_a_insurance_test.py`)

### People & where to follow them

- [Donald D. Hoffman](https://sites.socsci.uci.edu/~ddhoff/) — UC Irvine faculty page: papers, books, talks, Interface Theory of Perception
- [Lisa Feldman Barrett](https://affective-science.org/) — Interdisciplinary Affective Science Laboratory, Northeastern University
- [Karl Friston](https://www.fil.ion.ucl.ac.uk/~karl/) — UCL, Free Energy Principle / Active Inference
- [infer-actively/pymdp](https://github.com/infer-actively/pymdp) — open-source active inference library and tutorials

### Recommended course

- [Neuromatch Academy — Computational Neuroscience](https://compneuro.neuromatch.io/tutorials/intro.html) ([neuromatch.io](https://neuromatch.io/)) — free, project-based, cohort-run. The one structured curriculum here that's actually built the way this repo works: code against problem sets, not read-then-code.

### What we're building together, roughly in order

- [ ] FBT interface-theory agent-based simulation (Hoffman)
- [ ] Leaky integrate-and-fire neuron, visualized
- [ ] Toy active-inference / "body budget" agent (Barrett, via pymdp)
- [ ] Cross-over experiment: FBT-style fitness rule inside `model_a_group_competition.py`
- [ ] Write-up per model: assumptions, results, what it does and doesn't show

---

## Notes

- Python: NumPy / SciPy / Matplotlib, no exotic dependencies yet.
- The `.jsx` dashboard is a standalone Recharts component with simulation output embedded as static JSON — not wired to a build yet.
- Models are meant to be reproduced and understood, not treated as citable results. Every model here is a simplification; the write-ups should say so.
