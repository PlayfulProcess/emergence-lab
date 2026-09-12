# Start here — session bootstrap

**Any new Claude session, in any surface, reads this file first.** Everything else is
retrieved, not remembered. The repo is the memory; the chat is disposable.

Owner: PlayfulProcess. Repo: `PlayfulProcess/emergence-lab` (**private** as of Sept 2026 —
publish decisions are deferred, so nothing here needs to be written for an audience yet).
Working branch: `claude/recursive-eco-research-pgrdck`.

## Two tracks, one repo

**Track A — the research programme.** `docs/recursive-eco-improvement/`
Recursive *eco* improvement, not recursive *self* improvement: what properties make a system
adaptive with the substrate it is embedded in, and can they be specified, measured and
required. Start at `00-AGENDA.md`; it has the file map, the working method, the triaged
reading list and a session log with ordered next steps.

**Track B — positioning and career.** `docs/positioning/`
A possible redirection from pricing/analytics into AI research on selection environments.
`POSITIONING-REVIEW.md` is the pressure test; `FACT-CHECK-2026-09-12.md` is the
claim-by-claim audit of the source document. Track B exists to be *argued with*, not
executed — read the review before helping with any application or essay.

The tracks connect at one point: Track A's Experiment 01 instrument (measured response
asynchrony) is the operational definition Track B currently lacks for "ecosystem-level
adaptive range."

## The three standing disciplines

1. **`SOURCES.md` before prose.** No citation, and **no number**, in any document without a
   row in `docs/recursive-eco-improvement/SOURCES.md`. Read-status (`FULL` / `ABSTRACT` /
   `SUMMARY` / `UNREAD`) is a separate column from existence, because "I verified it exists"
   and "I read it" are different facts and blurring them is how citation rot starts.
2. **Every property gets a falsifier or gets marked "slogan, not specification."** This is
   the difference between a research programme and a vibe, and it is easy to let slide when
   a sentence sounds good.
3. **One commit per session, with the session log in `00-AGENDA.md` updated.** The log is
   the handoff.

## Getting papers in

Direct fetching of arXiv, journal sites and Wikipedia is blocked in the *remote* Claude Code
environment (GitHub only). MCP servers fetch server-side and are unaffected. A **desktop**
session does not have this restriction and can browse directly — if you are running on
desktop, fetch papers yourself rather than asking for uploads.

- **Corpus (the PDFs):** Google Drive folder `recursive-eco-research-corpus`
  (id `1mfHuDAHdl7ABodqN_nJbjfQl4siGkaar`). Private. Naming:
  `<identifier>--<first-author>-<year>.pdf`.
- **Library of record (the conclusions):** this repo, `docs/recursive-eco-improvement/notes/`,
  one file per paper on the four-heading template in that folder's README.
- **Bulk collection:** `docs/recursive-eco-improvement/corpus-collection-prompt.md` is a
  ready instruction block for a browsing session. Only identifiers already verified in
  `SOURCES.md` may be added to it — a wrong arXiv ID sends the collector after a real paper
  that is the wrong paper, which is worse than a missing one.

Two failure modes that have actually happened, both from a phone: the browser's "Save page
as" yields a `.mht` wrapper, and a share sheet yields a 32-byte text file containing the URL.
Check the file size. Under ~100 KB is not a paper.

## How to work here

PlayfulProcess vibe-codes, reads fast, and has asked explicitly to be corrected rather than
agreed with. Do not soften a finding to be encouraging. When she is wrong, say so early and
plainly, then continue. When a claim is contested, name who contests it. When the honest
version of a sentence is narrower than the satisfying version, write the narrow one.

Her name does not appear in published content — she publishes as **PlayfulProcess**.
