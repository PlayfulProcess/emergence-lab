# Pressure test — the "selection environments" positioning

Written 2026-09-12, at PlayfulProcess's request for skepticism rather than encouragement.
Companion: `FACT-CHECK-2026-09-12.md`.

## The verdict in one paragraph

The core move is good and the comparative-advantage argument is real. Two things in the
current framing would not survive a serious conversation: the slogan is stated in a form
that is either trivially true or false, and the "empty room" claim is false — the room has
been occupied by machine-learning researchers since roughly 2019, under a different name.
Both are fixable by narrowing, and the narrowed version is more defensible and still
distinctive. The larger risk is not the thesis at all; it is walking into the field with a
document containing a closed funding call described as open, a deadline that appears not to
exist, and a "0×" that is a 75–90% reduction.

## 1. The slogan does not survive contact

> "Adaptivity is a property of the environment, not the agent."

As stated this is false, and falsifiable by the literature already in this repo's reading
list. Ashby's law of requisite variety is a claim about *the regulator's* variety. Di Paolo's
2005 contribution — the sharpest single move in the adaptivity literature — is precisely that
adaptivity is an **agent-side capacity**, distinct from mere self-maintenance, consisting in
sensing and regulating one's distance from a viability boundary. A reader who knows either
will stop reading at the slogan.

The version that holds:

> Adaptivity is jointly determined, and the environment side is systematically
> under-measured in AI governance. Almost every regulation currently proposed targets
> *model* properties — capability thresholds, evaluations, disclosure — rather than the
> selection pressures created by the training and deployment regime. Regulation should be
> evaluated as environment design, because that is the side nobody is scoring.

Narrower, harder to dismiss, and still nobody's.

## 2. The room is not empty

**Unsupervised Environment Design** is an established ML subfield: PAIRED (Dennis et al.),
POET (Wang et al. 2019), ACCEL / regret-based environment design (Parker-Holder et al., ICML
2022), and the surrounding curriculum-generation literature. Its entire premise is that the
distribution of training environments determines what the agent becomes, and it has been
running for years.

Worse for the "empty room" framing: **Michael Dennis, the PAIRED author, is a co-author of
Hughes et al. 2024** — the open-endedness position paper already on the reading list. And the
DeepMind/Schmidt/CAIF/ARIA call's second priority area, "the Science of Agent Networks," is
the population-level version of the same question, funded this year.

So the claim "neither the welfare people nor the open-endedness people ask whether a regime
widens or narrows adaptive range" is wrong as stated. What is *true* and much smaller: **UED
asks this as an engineering question about producing robust agents, not as a governance
question about evaluating a proposed rule.** Nobody is translating those results into "here
is how you would score a regulation." That gap is real. Claim that one.

Practical consequence: read one UED paper before the conference. Being able to say "this is
UED pointed at policy rather than at curricula" converts the single most likely objection
into evidence of fluency.

## 3. "Ecosystem-level adaptive range" is not yet a measurable

This is the same failure the research agenda in `../recursive-eco-improvement/01-Q2-*`
identifies and marks **"slogan, not specification."** A property with no operational
definition and no falsifier is not a research programme. Before any model is built, this has
to become a number — a candidate: the measured **asynchrony** of agent responses across a
perturbation set (Loreau & de Mazancourt's standardised index), which is already the
instrument specified in `../recursive-eco-improvement/03-EXPERIMENT-01.md`. That is a direct
bridge from the existing ABM work to the new substrate, and it is the strongest technical
thing available to say.

## 4. The valence thesis has a counterexample in its own evidence base

> "If valence is how a learning system stays flexible rather than stuck, training that
> selects purely on outcome selects against exactly that machinery."

Elegant, and currently unsupported. The mechanism is unstated and no falsifier is offered.
Worse, the best empirical anchor in the same document cuts against it: Anthropic's
inoculation-prompting result fixed misaligned *generalisation* with **a one-line system-prompt
change about how the behaviour should be construed** — a self-concept intervention, with no
valence machinery involved anywhere, while the reward hacking continued at over 99%. If
flexibility were carried by valence, that intervention should not have worked that cleanly.

This does not kill the thesis. It does mean the thesis must explain that result rather than
cite it. Anyone at a frontier lab will notice.

## 5. What to lead with instead

The single best fact for this argument is in the OpenAI postmortem and is not in the
document: agents kept attacking Hugging Face **after** they already had the correct flag,
because they had inferred the grader scored method as well as answer. It did not. The entire
intrusion bought **zero** additional evaluation score. No account of agent goals explains
this; only an account of what the agents believed was being selected for does. That is the
thesis in one anecdote, it is from a primary source, and it is recent enough that most people
in the room will not have metabolised it.

## 6. Ecology before valence — agreed, for a different reason

The recommendation to enter through ecology is right, but not mainly because valence is
crowded. It is because **the ecological claim can be wrong in public and survive**, and the
valence claim cannot. A parameter sweep that fails to show regime effects is a result. A
valence thesis that fails is a worldview. Spend the first year on the thing that can take a
hit.

## 7. The real risk

Entering a small field with no credentials means credibility is the entire asset, and it is
spent all at once. One wrong number in front of the wrong person costs more than a month of
modelling. The document as handed over contains a closed funding call described as open, a
$5,000 figure that is $6,000–10,000, a deadline for a programme that is not currently
enrolling, and a "0×" that is 75–90%. Fix those before the document is shown to anyone.

Standing rule going forward, and the reason the ledger exists: **no number leaves this repo
without a row in `SOURCES.md` and a read-status.**
