# Verified sources ledger

**Rule of this file: nothing enters the programme's prose until it has a row here.**
Every row records what was checked, how, and — separately — how much of the source has
actually been *read*. "Exists" and "read" are different columns on purpose.

Read-status codes:

| Code | Meaning |
|---|---|
| `FULL` | Full text read in this project |
| `ABSTRACT` | Abstract / landing page read directly |
| `SUMMARY` | Only third-party summaries read (search results, blog posts, indexes) |
| `UNREAD` | Metadata verified, content not read |

**Verification method for every row below: web search returning the publisher/arXiv
landing page for the exact title.** Direct fetching of arxiv.org, journal sites and
Wikipedia is blocked by this environment's egress policy (see `00-AGENDA.md` §"Constraint");
sources reach a `FULL` read only by passing through the Drive corpus.

**`FULL` so far: 1 of 28.** Every other row is `SUMMARY` and must be read before it carries
any weight in prose.

---

## A · AI consciousness, valence, self-report

| Source | Verified identifier | Read |
|---|---|---|
| Berg, C., de Lucena, D. & Rosenblatt, J. (2025). *Large Language Models Report Subjective Experience Under Self-Referential Processing.* AE Studio. | arXiv:2510.24797 (v2 read) | **`FULL`** 2026-09-12 — main body + App. B, C.1–C.4. Note: `notes/2510.24797--berg-2025.md` |
| Kaiser, C. & Enderby, S. *No Reliable Evidence of Self-Reported Sentience in Small Large Language Models.* | arXiv:2601.15334 (v2) | `SUMMARY` — **PDF in corpus, next to read** |
| Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., Constant, A., Deane, G., Fleming, S. M., Frith, C., Ji, X., Kanai, R., Klein, C., Lindsay, G., Michel, M., Mudrik, L., Peters, M. A. K., Schwitzgebel, E., Simon, J. & VanRullen, R. (2023). *Consciousness in Artificial Intelligence: Insights from the Science of Consciousness.* | arXiv:2308.08708 (v1 17 Aug 2023; v2, v3 exist) | `SUMMARY` |
| Seth, A. K. (2025). *Conscious artificial intelligence and biological naturalism.* Behavioral and Brain Sciences. | doi:10.1017/S0140525X25000032 | `SUMMARY` |
| Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J. & Chalmers, D. (2024). *Taking AI Welfare Seriously.* | arXiv:2411.00986 | `SUMMARY` |
| Shanahan, M., McDonell, K. & Reynolds, L. (2023). *Role play with large language models.* Nature 623, 493–498. | doi:10.1038/s41586-023-06647-8 | `SUMMARY` |
| Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models.* Anthropic / Transformer Circuits, 29 Oct 2025. | transformer-circuits.pub/2025/introspection/ ; arXiv:2601.01828 | `SUMMARY` |
| Chen, R., Arditi, A., et al. (2025). *Persona Vectors: Monitoring and Controlling Character Traits in Language Models.* Anthropic. | arXiv:2507.21509 | `SUMMARY` |
| Anthropic (2025). *System Card: Claude Opus 4 & Claude Sonnet 4* — §model welfare assessment, incl. the "spiritual bliss attractor state". | anthropic.com/claude-4-system-card (May 2025) | `SUMMARY` |

**Not yet verified, do not cite until they are:** Birch, *The Edge of Sentience* (2024);
Frankish on illusionism (needs a specific essay, not "illusionism"); Schwitzgebel on
introspective unreliability (needs a specific paper); Solms, *The Hidden Spring*;
Damasio (needs a specific work, not "somatic markers").

## B · What makes a system adaptive

| Source | Verified identifier | Read |
|---|---|---|
| Di Paolo, E. A. (2005). *Autopoiesis, adaptivity, teleology, agency.* Phenomenology and the Cognitive Sciences 4, 429–452. | doi:10.1007/s11097-005-9002-y | `SUMMARY` |
| Holling, C. S. (1973). *Resilience and Stability of Ecological Systems.* Annual Review of Ecology and Systematics 4, 1–23. | doi:10.1146/annurev.es.04.110173.000245 | `SUMMARY` |
| Yachi, S. & Loreau, M. (1999). *Biodiversity and ecosystem productivity in a fluctuating environment: the insurance hypothesis.* PNAS 96(4), 1463–1468. | doi:10.1073/pnas.96.4.1463 | `SUMMARY` |
| Loreau, M. & de Mazancourt, C. (2013). *Biodiversity and ecosystem stability: a synthesis of underlying mechanisms.* Ecology Letters 16(s1), 106–115. | doi:10.1111/ele.12073 | `SUMMARY` |
| Cox, M., Arnold, G. & Villamayor-Tomás, S. (2010). *A review of design principles for community-based natural resource management.* Ecology and Society 15(4), art. 38. | ecologyandsociety.org/vol15/iss4/art38/ | `SUMMARY` |
| Nowak, M. A. (2006). *Five Rules for the Evolution of Cooperation.* Science 314, 1560–1563. | doi:10.1126/science.1133755 | `SUMMARY` |
| Wong, M. L., Cleland, C. E., Hazen, R. M., et al. (2023). *On the roles of function and selection in evolving systems.* PNAS 120(31), e2310223120. | doi:10.1073/pnas.2310223120 | `SUMMARY` |
| Root-Bernstein, M. (2024). *Evolution is not driven by and toward increasing information and complexity.* PNAS — letter contesting Wong et al. | doi:10.1073/pnas.2318689121 | `SUMMARY` |
| Wong et al. (2024). *Reply to Root-Bernstein…* PNAS. | doi:10.1073/pnas.2406598121 | `SUMMARY` |

**Books cited by title only (existence not in doubt, no page numbers asserted):**
Ashby, *Design for a Brain*; Maturana & Varela, *Autopoiesis and Cognition*;
Thompson, *Mind in Life*; Gunderson & Holling, *Panarchy*; Ostrom, *Governing the
Commons*; Maynard Smith & Szathmáry, *The Major Transitions in Evolution*; Axelrod,
*The Evolution of Cooperation*; Boyd & Richerson (cultural group selection);
Kauffman (autocatalytic sets); Deacon, *Incomplete Nature*.
**No page number from any of these may appear in the programme's prose until someone
has the book open.**

## C · Open-endedness (the ML-native neighbour)

| Source | Verified identifier | Read |
|---|---|---|
| Hughes, E., Dennis, M., Parker-Holder, J., Behbahani, F., Mavalankar, A., Shi, Y., Schaul, T. & Rocktäschel, T. (2024). *Position: Open-Endedness is Essential for Artificial Superhuman Intelligence.* ICML 2024. | arXiv:2406.04268 | `SUMMARY` |
| Sheth, I., Wehner, J., Abdelnabi, S., Binkyte, R. & Fritz, M. (2025). *Safety Must Precede the Deployment of Open-Ended AI* (v4 title: *Position: Safety Must Precede the Deployment of Open-Ended AI Agents*; accepted ICML'26). | arXiv:2502.04512 | `SUMMARY` |
| jennyzzt/awesome-open-ended — the field's own index. | github.com/jennyzzt/awesome-open-ended | `SUMMARY` |

**Not yet verified:** Zhang, Lehman, Stanley & Clune, *OMNI* (arXiv:2306.01711 — ID
asserted by the reading list, not independently confirmed); Lehman & Stanley,
*Why Greatness Cannot Be Planned*.

## D · Why the misalignment argument is fragile

| Source | Verified identifier | Read |
|---|---|---|
| Baker, B., et al. (2025). *Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation.* OpenAI. | arXiv:2503.11926 ; openai.com/index/chain-of-thought-monitoring/ | `SUMMARY` |

**Not yet verified:** Krakovna's specification-gaming list (a living document, needs a
stable URL + access date); Manheim & Garrabrant, *Categorizing Variants of Goodhart's Law*.

## E · Contested / handle with tongs

| Source | Status |
|---|---|
| Sharma, Walker, Cronin et al. — assembly theory (Nature 2023) | **Under sustained technical attack.** Zenil et al. argue assembly index reduces to Shannon entropy (arXiv:2408.15108). Critics include Zenil, Hazen, Jaeger, Benner. A Nature journal found Cronin and Walker had failed to disclose competing interests during review of a critical paper and removed them from that review process. Usable as a *case study in how a "law of X" gets contested*; **not usable as load-bearing evidence for anything.** |
| Friston — free energy principle | The universal formulation ("things that exist minimise free energy") is widely argued to be near-tautological. The *active inference* model class is testable. Keep the two apart in prose. Specific critiques not yet verified — do so before characterising them. |
