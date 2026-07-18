# Entry Writing Guide: Auditable Compositions

Source: E5 `inertial-frame` wall feedback rounds, 2026-06-12 (Can + Claude);
COMBINING_REACTIONS_FOR_PREDICTION.md; D2.1 E5 entry packet
Status: active guidance
Code relevance: constrains how entry strings may be composed; gives the audit
practice for the residual layer that the dependency graph cannot see

---

## The principle

An entry's definiens is a composition of two kinds of material. Headword
references are mechanical: the tokeniser sees them, the dependency graph
records them, audits can reach them. Everything else is residual: latent
strings whose entire contribution is the reaction they produce in an
interpreter.

**The residual is a bet on pre-existing reactions. The dictionary can only
audit entries and edges. A novel figure that does definitional work is
therefore undeclared machinery hidden in the residual — outside audit
reach. An entry writer has exactly two honest options:**

1. **Promote the figure to its own entry.** It becomes structure: it gets a
   headword, it creates edges, audits and traces can reach it.
2. **Compose the residual only from reactions that are already installed.**
   The bet is then on training the culture has already done, not on
   training the entry quietly presumes.

Writing a definition out of invented conceptual devices while leaving them
out of the dictionary misrepresents what the words are claimed to
accomplish in the framework. If the intended reactions to a figure must be
documented in packet notes for anyone to see them, that is the proof the
machinery exists — it just lives where no audit can reach it.

## Why this follows from the framework

The VD combines reliable human reactions to presented strings into a
controlled computation. Reactions are partly innate, partly trained, partly
culturally installed. A wall entry is a compact behavioural trigger placed
where the trace needs the interpreter to perform an operation.

The reliability of the whole computation therefore rests on two pillars:
edges the graph can check, and residual reactions that are reliable
*independently of this dictionary*. A novel figure fails the second pillar
by construction — its reaction is not installed anywhere except in the
writer's intention. It is the residual-layer form of a hidden import, the
same defect the packets track for headwords, in metaphor's clothing.

A novel figure can also commit a *forward* hidden import: borrowing the
conceptual scheme of later entries before they exist. Example below.

## Reaction provenance

Residual material is acceptable when its reaction has a named backing:

- **Grammar-level mechanisms.** Innate, language-wide. A definite
  description forces referent-finding ("the frame in use" cannot be parsed
  without locating a frame). Presupposition, default-and-defeater shapes
  ("stands as X unless marked as Y"), scope idioms ("in ordinary
  problems").
- **General-English idioms, at idiom strength only.** "Used as standard",
  "serves as", "stands as". An idiom licenses its conventional reaction
  and nothing more — extrapolating a metaphor *system* from one idiom
  ("owes nothing to" → creditors, ledgers, who-collects-this-curve) is
  novel machinery again.
- **Community-installed terms.** Words the target culture has already
  trained reactions to. "Artifact" → discount it, attribute it to the
  apparatus, check the instrument. "Lab frame", "Galilean",
  "to the needed approximation".
- **Stock formulas.** Sentences the culture already says. "Mechanics is
  simplest in inertial frames" can be stated at stock strength because the
  reader has met it before.
- **Lesson-installed handles.** Reactions the pedagogy deliberately
  installs before or alongside the entry (NM L1's "influence" as the
  pre-force handle; "understood most simply" as the frame handle). These
  count as installed *for interpreters who passed through the lesson* —
  if the entry must work outside that population, do not lean on them.
- **Headword edges.** Not residual at all; the auditable case. Prefer
  moving load here when possible.

Caution even with installed material: an installed stimulant carries its
installed baggage. "Non-accelerating frame" is reliably triggering — and
what it reliably triggers includes the dangling-slogan recall and the
misreads the packets catalogue. Installed is necessary, not sufficient;
the handle must also route.

## The practice: residual provenance ledger

For each entry, alongside the packet checks, keep a table: every residual
phrase, and the backing of its expected reaction. Example row:

| Phrase | Backing |
|---|---|
| artifact of the frame itself | scientific-culture reaction (discount; check apparatus); packet vocabulary; matches the trace's frame-artifact warning |

The ledger must contain no row whose backing is the writer's own
invention. If such a row appears, apply the principle: promote or replace.

A bonus alignment worth recording in the ledger: residual vocabulary that
matches *machinery* vocabulary (entry says "artifact", trace emits
"frame-artifact warning") keeps string and simulator auditable against
each other.

## Worked example: the E5 wall

A draft sentence read:

```text
Acceleration appearing in a trajectory described in an inertial-frame owes
nothing to the frame itself; where nothing is owed to the frame, mechanics
runs at its simplest.
```

The debt figure was doing real definitional work: source-attribution,
artifact protection, and a diagnostic affordance (a curving free particle
leaves the frame as "the only open ledger line"). None of that machinery
was in the dictionary — and the ledger scheme forward-borrowed the force-
accounting frame from Newton II-side entries that come later. Two
violations: undeclared residual machinery, and a forward hidden import.

The repair recomposed the same jobs from installed material:

```text
Acceleration appearing in a trajectory described in an inertial-frame is
not an artifact of the frame itself.
```

"Artifact" is community-installed (discount it; check the apparatus —
frame-as-apparatus yields the diagnostic for free), is the packet's own
word, and matches the trace's warning vocabulary. The simplicity claim
moved to stock strength elsewhere in the entry ("mechanics is at its
simplest in such a frame").

## Quick test

Before installing an entry string, ask of every non-headword phrase:

1. Who installed the reaction this phrase is betting on — the culture, the
   language, the lesson, or me?
2. If me: which entry carries it? If none does, promote it or cut it.
3. Does the phrase claim only the reaction at installed strength, or does
   it quietly extend a metaphor into a system?
4. Does any figure borrow the conceptual scheme of entries that come
   later?

Related principles: no attitude verbs in entry strings (status lives in
practice words — "used as standard", not "accepted/treated as"); no
imperatives or agent-directed deontics (the declarative paradigm; nomic
"must" inside law triplets is a different animal and survives).
