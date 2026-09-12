# Recursive ECO improvement — research agenda

*Not recursive **self** improvement. The question is not how to build an AI that does not
kill us; it is what properties make a system adaptive **with** the substrate it is embedded
in — and whether those properties can be specified, measured, and eventually required.*

Author: PlayfulProcess. Started 2026-09-12.

**New session? Read `../START-HERE.md` first.** The repo went **private** in Sept 2026
(publish decisions deferred) and a second track — `../positioning/` — now exists alongside
this one.

## Files

| File | What it is |
|---|---|
| `00-AGENDA.md` | This. Working method, reading list, session log. |
| `01-Q2-convergent-properties.md` | Q2: who has good claims on "adaptive", and the eight-property shortlist with falsifiers. |
| `02-Q1-ai-valence-PROVISIONAL.md` | Q1: state of the evidence on LLM self-report. **Provisional — anchor paper unread.** |
| `03-EXPERIMENT-01.md` | The next experiment, extending `model_a_insurance_test.py`. |
| `SOURCES.md` | Verified-citation ledger. Nothing enters prose without a row here. |

---

## Constraint discovered 2026-09-12 — read this before planning a session

**Claude Code running remotely has an egress allowlist. GitHub is reachable. arXiv,
journal sites, Wikipedia and general web hosts are not.** Web *search* works and returns
summaries; web *fetch* does not. MCP servers fetch server-side and are unaffected
(Google Drive, Wikipedia-via-MCP, the recursive-eco corpus search all work).

Consequence: a research programme run from this chat **cannot read a paper live**. Sources
must be brought inside the perimeter first. This is not a nuisance to work around — it is
the reason the architecture below is shaped the way it is, and it makes the corpus durable
rather than re-fetched every session.

**The corpus lives in Drive; the library of record lives here.** These are different
things and conflating them is the mistake to avoid. `emergence-lab` is a **public** repo, so
no paywalled PDF and no substantial verbatim third-party text may be committed to it —
the `recursive-books` rule applies unchanged: notes and paraphrase in, raw copyrighted
text out.

| Layer | Where | Contains |
|---|---|---|
| **Corpus** (the PDFs) | Google Drive → **`recursive-eco-research-corpus`** (folder id `1mfHuDAHdl7ABodqN_nJbjfQl4siGkaar`) | Source PDFs, private, readable by the Drive MCP server-side. Never leaves Drive. |
| **Library of record** (what we concluded) | `docs/recursive-eco-improvement/` + `SOURCES.md` | Per-paper notes, the falsifiers, the ledger. Public, paraphrase only, versioned. |
| **Triage reader** | NotebookLM, sourcing from the Drive folder | Deciding what deserves a full read. Its output is disposable; the conclusion goes in the repo. |

**Naming convention in the Drive folder:** `<arxiv-id-or-doi-slug>--<first-author>-<year>.pdf`
— e.g. `2510.24797--berg-2025.pdf`. The identifier first, so it matches the `SOURCES.md` row
without a lookup.

**Per paper, once read, commit one file:** `notes/<same-slug>.md` — the claim, the method,
what would have to be true for it to be wrong, and how it changes a property in `01-Q2`.
That file, not the PDF, is what future sessions retrieve. Paraphrase only; quotations under
~30 words with attribution if the exact wording is argumentatively necessary.

---

## The way of working

The goal is one chat at a time, in Claude Code, able to retrieve everything. That works if
each kind of knowledge lives in exactly one place and the session prompt says where.

**Repos are the memory. Grammars are the reading list. Supabase and R2 are for things with
many readers.**

| Thing | Lives in | Why there |
|---|---|---|
| Models, results, plots | `emergence-lab` | Code belongs with the code. |
| Research prose, falsifiers, experiment specs | `emergence-lab/docs/recursive-eco-improvement/` | Retrievable by `grep`, versioned, diffable. Reasoning that changes should show its history. |
| Verified citations | `SOURCES.md` (one file, one table) | A single ledger is the only thing that makes "never cite from memory" enforceable. |
| Source PDFs / extracted text | `emergence-lab/corpus/` | The egress constraint above. |
| The reading list *as a thing you read and annotate* | a recursive.eco **grammar** | This is what grammars are for: an ordered set of items with per-item sections, a viewer, and an assistant grounded in it. Triage tier becomes a section; read-status becomes metadata. One item per source. |
| Emotion/valence vocabulary | `recursive-repatterning` | Already a constructionist-substrate corpus. Q1's "words that convey the social construct we understand emotions" is already partly built there. Do not rebuild it. |
| Anything with many readers or needing query | Supabase | Only when a flat file genuinely stops working. It has not yet. |
| Large binaries (figures, audio, images) | R2 | Same rule — only when a repo would choke. |

**The rule that keeps it resilient: the session prompt is a pointer, not a payload.** Start
every session with "read `emergence-lab/docs/recursive-eco-improvement/00-AGENDA.md` and the
session log at the bottom, then do X." Everything else is retrieved, not remembered. A chat
that ends is then never a loss.

**Three standing disciplines:**

1. **`SOURCES.md` before prose.** No citation in any document without a row. Read-status is
   a separate column from existence — `SUMMARY` is honest, a missing row is not.
2. **Every property gets a falsifier or gets marked "slogan, not specification."** This is
   the whole difference between the programme and a vibe, and it is easy to let slide when a
   sentence sounds good.
3. **One commit per session, with the session log updated.** The log below is the handoff.

---

## Reading list, triaged

Cuts and corrections are marked. Full citations in `SOURCES.md`.

### READ FIRST (5)

1. **Berg, de Lucena & Rosenblatt 2025, arXiv:2510.24797** — the anchor. Everything in Q1
   is provisional until this is read in full.
2. **Kaiser & Enderby, arXiv:2601.15334, "No Reliable Evidence of Self-Reported Sentience in
   Small Large Language Models"** — *not on the original list.* The closest thing to a direct
   counterweight: overlapping methodology, roughly opposite sign. Read it beside the anchor,
   not after.
3. **Butlin et al. 2023, arXiv:2308.08708** — the field's shared map. Read for the indicator-
   property framework, not for the verdict.
4. **Di Paolo 2005** — the single most useful conceptual tool in the whole Q2 list. It is
   what separates adaptivity from staying alive, and it is short.
5. **Seth 2025, BBS** — the strongest case against computational functionalism. Read before
   getting attached to the affirmative side, as you said.

### READ SOON

- Long, Sebo et al. 2024, arXiv:2411.00986 — *this* is the real citation behind the vague
  "Robert Long / Eleos; Jeff Sebo" entry.
- Shanahan, McDonell & Reynolds 2023, Nature 623 — role-play. Directly load-bearing: the
  anchor's manipulated features are labelled *deception and roleplay*.
- Lindsey 2025 (Anthropic introspection) + Chen et al. 2025 (persona vectors) — these two,
  plus the Claude 4 welfare section, are the "Anthropic study" you were reaching for.
- Ostrom, *Governing the Commons* + **Cox, Arnold & Villamayor-Tomás 2010** — *added.* The
  91-case empirical review of the eight principles. This is where you find out whether you
  rediscovered Ostrom, and it is the only real falsification evidence in Q2.
- **Loreau & de Mazancourt 2013, Ecology Letters 16** — *added.* The asynchrony index that
  Experiment 01 depends on.
- Holling 1973 — short, and the source of P5.
- Nowak 2006 — for the threshold inequalities, which are the most precise claims in Q2.
- Hughes et al. 2024, arXiv:2406.04268 — **attribution corrected**, see below.
- Sheth et al., arXiv:2502.04512 — read against Hughes et al., as you intended.
- Baker et al. 2025, arXiv:2503.11926 — your section-D claim, **verified correct**.
- Manheim & Garrabrant on Goodhart; Krakovna's specification-gaming list.
- Wong et al. 2023 PNAS **as a set with** Root-Bernstein's critique and the authors' reply.
  Reading the paper alone would give you a false sense of how settled it is.

### BACKGROUND

Ashby (requisite-variety chapter only — and note it is a *theorem*, so it is not falsifiable;
the empirical question is whether real regulators approach the bound); Maturana & Varela;
Thompson, *Mind in Life*; Friston 2010 with a critique alongside; Maynard Smith & Szathmáry;
Axelrod; Boyd & Richerson and Yachi & Loreau (already implemented here); Kauffman; Deacon;
Levin; Frankish (needs one specific essay, not "illusionism"); Schwitzgebel (same); OMNI
(arXiv:2306.01711 — ID unverified); `jennyzzt/awesome-open-ended`.

### CUT, with reasons

- **Walker & Cronin, assembly theory** → demoted to *read the controversy only*. Zenil et al.
  argue the assembly index reduces to Shannon entropy; Hazen, Jaeger and Benner also object;
  a Nature journal found undisclosed competing interests during review of a critical paper.
  It cannot carry weight in your argument. Keep it as a case study in how a "law of X" fails
  in public — which is directly useful, since P8 is the same temptation.
- **Solms and Damasio** → demoted to background, and read knowing they cut *against* the
  LLM-valence claim. If affect is brainstem-and-body, a system with neither has no valence to
  report. They are the ancestors of the intuition and also its strongest internal objection.
- **Lehman & Stanley, *Why Greatness Cannot Be Planned*** → background. The ICML position
  paper does the same work in citable form.
- **Birch, *The Edge of Sentience*** → moved out of READ FIRST to READ SOON. It is very good
  and it is a book; Butlin, Seth and Long/Sebo cover the precaution-under-uncertainty ground
  faster.

### Corrections to the v0 list

- **The ICML 2024 open-endedness position paper is not Stanley, Lehman & Clune.** It is
  Hughes, Dennis, Parker-Holder, Behbahani, Mavalankar, Shi, Schaul & Rocktäschel
  (DeepMind), arXiv:2406.04268. Stanley, Lehman and Clune are the novelty-search lineage
  that it builds on; they are not its authors.
- **Chalmers is not an author of Butlin et al. 2023.** He is an author of *Taking AI Welfare
  Seriously*. The two lists are easy to blend and a reviewer would notice.
- **Seth's biological-naturalism piece is now a 2025 BBS target article**, not a 2024
  preprint (the preprint exists; cite the BBS version).
- **arXiv:2502.04512's author list** is Sheth, Wehner, Abdelnabi, Binkyte & Fritz, and its
  title has drifted across versions — check which version you are citing.
- **Your section-D claim is right.** Baker et al. found that applying strong optimisation
  pressure to the chain-of-thought produces *obfuscated* reward hacking — the model keeps
  cheating and stops saying so — and recommend paying a "monitorability tax" by not
  optimising the CoT directly. You had it correctly.

---

## Session log

### 2026-09-12 — session 1
Read `emergence-lab` README and all three ABMs. Verified ~25 citations by search; found
three errors in the v0 reading list (above). Discovered the egress constraint and designed
the working method around it. Wrote Q2, the provisional Q1, Experiment 01, and `SOURCES.md`.

**Then unblocked.** Both PDFs reached the Drive corpus and the anchor was read in full.
`02-Q1` is rewritten and no longer provisional.

**One thing I had wrong, recorded because it is the exact failure this ledger exists to
prevent:** the provisional Q1 proposed a semantically-matched non-self-referential recursion
control as "the cheapest real replication", on the assumption the anchor lacked it. It has it —
the history control matches the iterative feedback structure and returns 0% for six of seven
models. Guessing at a paper's controls from its abstract produced a confident, wrong
recommendation. The replacement proposals are in `02-Q1` §"The cheapest real contribution".

**Next session, in order:**
1. Read Kaiser & Enderby (arXiv:2601.15334, already in the corpus) and write its note. It is
   the counterweight and Q1's §"Who disputes it" is `SUMMARY`-level until it is read.
2. Build Experiment 01. Panel C first — the allocation-exponent honesty panel — because if
   `/ n` is doing the work, Panels A and B need reinterpreting before they are run.
3. Read down the READ SOON list, one note per paper, ledger updated each time.
4. Only then: the reading list as a recursive.eco grammar.
