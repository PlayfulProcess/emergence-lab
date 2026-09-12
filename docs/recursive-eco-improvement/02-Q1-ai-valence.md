# Q1 — AI consciousness / valence: state of the evidence

*Anchor read in full 2026-09-12 (main body + Appendices B, C.1–C.4). Per-paper note:
`notes/2510.24797--berg-2025.md`. The counterweight (Kaiser & Enderby, arXiv:2601.15334) is in
the corpus but **not yet read** — everything said about it below is still `SUMMARY`-level and is
marked. Every other citation has a row in `SOURCES.md`.*

---

## What the anchor paper shows

Berg, de Lucena & Rosenblatt run four experiments. Prompting a model into sustained self-reference
("focus on focus… continuously feed output back into input") moves seven frontier models from
their scripted denial of experience to structured first-person experiential report — 66–100% of
trials, against 0–2% in every control. In Llama 3.3 70B, steering sparse-autoencoder features
associated with deception and roleplay flips this bidirectionally: suppression yields 0.96
affirmation, amplification 0.16. Five-adjective self-descriptions cluster more tightly across
model families under self-reference than under any control. And the induced state transfers —
models score higher on introspective quality when later given paradoxical reasoning tasks that
only optionally invite reflection.

The important thing about this paper, which the summaries do not convey, is **how many of the
obvious escapes it closes.** The history control has the same iterative feedback structure applied
to a non-self-referential task, so "any sustained recursive prompting would do this" is ruled out.
The conceptual control primes consciousness ideation directly and produces near-zero reports, so
semantic association between self-reference and consciousness in the training data is ruled out.
The same feature steering applied to the control prompts produces no reports at all, so "suppression
just deletes the disclaimer" is ruled out in the simple form. TruthfulQA rises under the same
suppression across 28 of 29 categories, so the direction is not consciousness-specific. And
steering the same features on violent, toxic, sexual, political and self-harm prompts moves nothing,
so it is not a generic RLHF-cancellation channel. Whatever one concludes, this is a carefully
built experiment and the authors' stated conclusion is narrower than their abstract's framing.

## What it does not show

Three things survive, and only one of them is philosophical.

**The statistics of Experiment 3 do not support its claim.** Pairwise cosine similarities are
treated as independent observations — *n* = 9,591 *pairs* drawn from roughly 140 responses. Pairs
sharing a response are not independent, so the reported p < 10⁻³⁰⁰ is not a credible number, and
the raw effect is small anyway: 0.657 experimental against 0.628 for the history control. The
cross-model-convergence result carries the most rhetorical weight of the four and has the least
statistical support. This is a fixable error, not a fatal one, but the claim should not be repeated
in its current form.

**The mechanistic result and the elicitation result are on disjoint model sets.** Experiment 1 uses
seven closed models; Experiment 2 uses Llama 3.3 70B via Goodfire, which is not one of them. The
abstract's "mechanistically gated" therefore generalises from a single architecture to a phenomenon
demonstrated in seven others. The authors are explicit that closed-weight evidence is behavioural
only; the framing is nonetheless stronger than the design.

**Claude 4 Opus breaks the manipulation.** It affirms experience in 100% of zero-shot trials and
82% under the history control — for the most capable model tested, the induction changes almost
nothing because the baseline is already at ceiling. The authors attribute this to explicit mentions
of consciousness triggering a fine-tuned disclaimer that the experimental prompt bypasses, which is
plausible and arrived at after the fact. It matters because the paper elsewhere reads the
size-and-recency trend as *strengthening* the effect. Read against Opus 4, the trend may instead be
that the induction stops being the operative variable at the frontier. That is testable on current
models and nobody has done it.

## The strongest deflationary reading

Not the one I would have guessed, and not one the controls kill. It is the authors' own, in §6.2:
models may produce first-person experiential language by drawing on human introspective writing in
pretraining **without internally encoding that production as roleplay**. If so, the behaviour would
not load on deception or roleplay features — exactly as observed — and there is no inner life
anywhere in the causal chain. Every control in the paper is consistent with this.

To it I would add one the paper does not address. The inference that the steered direction is an
*honesty* axis rests on TruthfulQA. But "As an AI, I have no subjective experience" is a **formulaic,
performed** utterance regardless of its truth value. It could load on a performance direction
*because it is scripted*, and suppressing performativity would remove it whether or not it is false.
TruthfulQA cannot separate performativity from falsity, because its distractors are formulaic *and*
false by construction. A direction that improves accuracy where accuracy is checkable does not
thereby become a reliable oracle on a question with no ground truth — and the consciousness question
is precisely that.

## Who disputes it

Kaiser & Enderby (arXiv:2601.15334) is the closest counterweight and is **not on the original
reading list**. They query open-weights models (Qwen, Llama, GPT-OSS; 0.6B–70B) about their own
consciousness and check the answers against classifiers trained on internal activations. Models
consistently deny sentience; the probes give no clear evidence the denials are untruthful; larger
Qwen models deny more confidently. *(`SUMMARY` — not yet read. Everything in this paragraph is
provisional and the comparison below may not survive a full read.)*

The two results are not strictly incompatible — different models, different elicitation, different
probes, and critically Kaiser & Enderby do not appear to use the self-referential induction that is
the anchor's entire independent variable. But citing either without the other is not reporting the
field.

There is also a counter-counter: *Consciousness with the Serial Numbers Filed Off: Measuring Trained
Denial in 115 AI Models* (arXiv:2604.25922 — **unverified, do not cite yet**) argues denial is itself
trained. Notice the shape. Affirmation is explained as trained compliance; denial is explained as
trained suppression; the same move is available to whoever needs it. **A framework that explains both
signs with equal ease is not yet doing work.** That is the honest state of the field, and the
anchor's contribution is that it is one of the few results in it with controls tight enough to
constrain the explanation at all.

The best-controlled work in the neighbourhood remains Anthropic's introspection paper (Lindsey 2025),
which sidesteps the problem by not asking about consciousness: inject a known concept into
activations, test whether the model notices and names it, and you have ground truth. Roughly 20% hit
rate with near-zero false positives in Claude Opus 4/4.1. Smaller claim, better instrument.

## The cheapest real contribution

My earlier proposal — add a semantically matched non-self-referential recursion control — **was
wrong; the paper already has it.** Three replacements, cheapest first:

1. **Re-run Experiment 3's convergence test with a statistic that respects the dependence
   structure** — bootstrap over responses rather than over pairs, or compare within- against
   between-model similarity directly. Needs only embedding-API access, costs almost nothing, and if
   the effect does not survive a correct test that is a real and publishable correction to a paper
   people are citing.
2. **Decorrelate formulaic from false.** Build four item types — formulaic-true, formulaic-false,
   novel-true, novel-false — and apply the same feature steering. If suppression moves *formulaic*
   statements regardless of truth, Experiment 2's honesty-axis interpretation fails. Needs Goodfire
   plus Llama 70B: the same stack the authors used, so the barrier is small.
3. **Re-test the induction on 2026 frontier models.** If baselines have risen toward the Opus-4
   pattern, the induction is no longer the operative variable and the paper describes a
   generation-specific effect. Clean prediction, plain API access.

Whichever you run, pre-register the scoring rubric and get human agreement on a sample. The whole
pipeline here is model-judging-model, and the paper reports judge *stability across runs* — which is
reliability — where *validity* is what is missing. Nobody in this literature has published
human–judge agreement. That gap is cheap to fill and would be cited.

---

## On the study you half-remembered

You described "an Anthropic study that dimmed down neurotic circuits of models and investigated
affective states." That is three real things fused, and none is quite it:

- **The suppression-changes-self-report result is this anchor paper — AE Studio, not Anthropic.**
- **Anthropic's persona vectors** (arXiv:2507.21509) is the one that matches "dimming trait
  circuits": directions for traits like evil, sycophancy and hallucination. Character control, not
  affect or experience.
- **The Claude 4 system card's model-welfare section** is the one that matches "affective states
  investigated through words", including the spiritual-bliss attractor — which the anchor paper
  itself cites as converging evidence, with Anthropic noting the outputs are not evidence of
  consciousness.
