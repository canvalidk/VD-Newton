# VD Dictionary — Answering Textbook Questions

**Date:** 2026-04-19
**Status:** Introductory note — stub for a later discussion of the philosophical and mathematical implications
**Context:** Session conversation established the headword-lookup model of question answering

---

## The model

A textbook question is a request to evaluate a **headword**. The VD answers the question in two steps:

1. **Normalisation.** The natural-language question is translated into a headword. Textbook English is under-specified: "what is the acceleration of the particle?" technically admits many answers depending on reference frame, but pedagogical convention silently maps it to `inertial-acceleration`. The normalisation step makes that translation explicit. It is an act of interpretation that happens before the dictionary is consulted.

2. **Expansion.** The dictionary is consulted for the chosen headword. Its definition is expanded recursively, pulling in sub-definitions as needed, until the expansion terminates.

The answer to the question is whatever the expansion produces.

## The three outcomes

An expansion can end in one of three ways.

**Termination with a value.** The definition resolves to a computable quantity. This is the standard case. *"What is the inertial-acceleration of m₁ in this Atwood setup?"* → E21 expansion → `net-force / inertial-mass` → numerical answer.

**Termination on an undefined referent.** The expansion requires a term that has no referent for the given arguments. The lookup halts. The correct answer is N/A — the absence of a well-defined quantity, not zero and not infinity. *"What is the inertial-acceleration of a photon?"* → E21 expansion → requires `inertial-mass` → photon has no referent for `inertial-mass` → halt. The halt is diagnostic: it says the question, as normalised, has no answer.

**Termination on contradiction.** The expansion produces inconsistent commitments. The question's premises are incompatible — with each other, or with the dictionary. The answer is "the question is malformed," and the specific contradiction tells the modeller where.

## Why normalisation matters

Normalisation is where most of the apparent strangeness of the VD's question-answering lives. Standard pedagogy hides it. Textbook questions are written in a shared convention that assumes inertial frames, massive particles, and well-defined quantities. The reader performs the normalisation silently and unconsciously.

The dictionary treats normalisation as an explicit act — a choice of which headword is being queried — because different normalisations produce different expansions, different ancestries, and sometimes different outcomes. The same physical object can give a clean answer under one normalisation and halt under another:

- *What is the **inertial-acceleration** of a photon?* → halt. N/A.
- *What is the **path** of a photon?* → path of a free-body → Newton I triplet → uniform motion in an inertial frame.

Both questions are "about" the same photon. The dictionary does not distinguish objects by what they are; it distinguishes questions by what they ask.

## Worked examples

**Q: What is the acceleration of m₁ in the Atwood setup?**
- Normalisation: `inertial-acceleration(m₁)` (inertial-frame convention).
- Expansion: E21 → requires `net-force(m₁)` and `inertial-mass(m₁)`.
- Terminates with a value.

**Q: What is the acceleration of a free massive particle in an inertial frame?**
- Normalisation: `inertial-acceleration(p)` (free particle, inertial frame).
- Expansion: E21 → `net-force / inertial-mass`. The IFS is empty. The sum is the zero vector. Mass has a referent.
- Terminates with value 0. No branching, no special case.

**Q: What is the inertial-acceleration of a photon?**
- Normalisation: `inertial-acceleration(photon)`.
- Expansion: E21 → requires `inertial-mass(photon)` → no referent.
- Halts on undefined referent. Answer: N/A.

**Q: What is the path of a photon in empty space?**
- Normalisation: `path(free-body)`. Photon is a free-body regardless of mass.
- Expansion: Newton I triplet → uniform-motion in an inertial-frame. Mass is not invoked.
- Terminates. Answer: uniform motion in an inertial frame.

The same photon gives a crash for one question and a clean answer for another, because the headword being queried determines the ancestry.

## What the VD does differently

Textbook physics handles the photon case by either refusing to ask the question (photons are declared outside Newtonian mechanics by convention) or importing a special-case procedure from relativity. The VD does neither. It lets the expansion run and reports honestly on whether it terminates.

This honesty is bought by making normalisation explicit. The cost is that the reader has to decide, before consulting the dictionary, which headword the question actually targets. The benefit is that the dictionary's answer is always structurally legible: if it terminates, the ancestry tells you exactly what was invoked; if it halts, the missing referent tells you exactly what the question presupposed that the dictionary does not grant.

## What comes next

The deeper implications are left for a separate discussion. Topics to develop:

- What it means for the dictionary to have genuine **domains of applicability**, rather than a universal answer set.
- The status of the normalisation step as a **semantic bridge** between ordinary language and formal mechanics — and whether it is itself something the VD can formalise or is irreducibly a reader's responsibility.
- What the crash-on-undefined-referent behaviour reveals about the **boundary structure** of physical theories, and how that boundary can be detected from inside the formalism.
- The relationship between normalisation choices and the **residual/poetic layer** of the VD — whether different normalisations of the same natural-language question reflect distinct but equally legitimate interpretive commitments.

This note establishes the model. The implications are for another conversation.
