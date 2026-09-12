# Prompt for a Claude Desktop / Cowork session — corpus collection

Paste the block below into a Cowork session. It is standalone: it assumes no memory of the
Claude Code chat. Re-run it with a different list whenever the READ SOON list grows.

Only identifiers verified in `SOURCES.md` appear here. Do not add an arXiv ID to this prompt
that has not been verified first — a wrong ID sends the collector after a real paper that is
the wrong paper, which is worse than a missing one.

---

```
I'm assembling a research corpus. Please download the PDFs listed below and put them in my
Google Drive folder "recursive-eco-research-corpus".

Naming: <identifier>--<first-author>-<year>.pdf, identifier first, e.g.
  2308.08708--butlin-2023.pdf
  10.1073-pnas.96.4.1463--yachi-1999.pdf     (slashes in a DOI become hyphens)

Rules:
- Download the actual PDF file. Do not use the browser's "Save page as" (that produces .mht)
  and do not use a share sheet (that saves a link). If a file lands under ~100 KB, it is not
  a paper — flag it rather than uploading it.
- arXiv: go to arxiv.org/abs/<id>, then the PDF link, then download.
- If a paper is paywalled, do NOT try to bypass it. Check for a legitimate free copy in this
  order: the publisher's own open-access version, PubMed Central, the author's university
  page, or the journal's public archive. If none exists, skip it and list it as paywalled.
- Do not download anything not on this list.

arXiv (all free):
  2308.08708   Butlin et al. 2023, Consciousness in Artificial Intelligence
  2411.00986   Long, Sebo et al. 2024, Taking AI Welfare Seriously
  2406.04268   Hughes et al. 2024, Open-Endedness is Essential for ASI
  2502.04512   Sheth et al. 2025, Safety Must Precede the Deployment of Open-Ended AI
  2503.11926   Baker et al. 2025, Monitoring Reasoning Models for Misbehavior
  2507.21509   Chen et al. 2025, Persona Vectors
  2601.01828   Lindsey 2025, Emergent Introspective Awareness in LLMs

Open-access journals:
  10.1073/pnas.96.4.1463    Yachi & Loreau 1999, insurance hypothesis (PNAS)
  10.1073/pnas.2310223120   Wong, Cleland, Hazen et al. 2023 (PNAS)
  10.1073/pnas.2318689121   Root-Bernstein 2024, critique of the above (PNAS)
  10.1073/pnas.2406598121   Wong et al. 2024, reply to Root-Bernstein (PNAS)
  Cox, Arnold & Villamayor-Tomas 2010, A Review of Design Principles for Community-based
    Natural Resource Management — Ecology and Society 15(4) art.38, fully open at
    ecologyandsociety.org/vol15/iss4/art38/

Likely paywalled — try, then report:
  10.1146/annurev.es.04.110173.000245   Holling 1973, Resilience and Stability (Ann Rev Ecol Syst)
  10.1007/s11097-005-9002-y             Di Paolo 2005, Autopoiesis, adaptivity, teleology, agency
  10.1126/science.1133755               Nowak 2006, Five Rules for the Evolution of Cooperation
  10.1038/s41586-023-06647-8            Shanahan, McDonell & Reynolds 2023, Role play with LLMs
  10.1017/S0140525X25000032             Seth 2025, Conscious AI and biological naturalism (BBS)
  10.1111/ele.12073                     Loreau & de Mazancourt 2013 (Ecology Letters)

When you're done, give me a table: filename, size, and status (downloaded / paywalled /
not found). Don't summarise the papers — I only need them collected.
```

---

Then, back in the Claude Code session: "read the new PDFs in the corpus folder and write their
notes." Priority order is the READ SOON list in `00-AGENDA.md`.
