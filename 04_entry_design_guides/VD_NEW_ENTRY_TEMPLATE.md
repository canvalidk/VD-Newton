# VD New Entry Template

Status: working template.

Use this file as a copy/paste scaffold for making or revising VD entries.
The main block is intentionally short. Paste it into chat, fill what you know,
and leave the rest as `unknown` or `unbound`.

## Quick Use

Copy one of the blocks below, fill only what is known, and leave unknown fields
as `unknown` or `unbound`.

Minimum spine:

- entry id
- headword
- role
- source status
- plain purpose
- IRIL - ideal residually imparted logic
- IRIEs - ideal residually imparted effects
- trace critical headword mentions
- forbidden headword mentions / hidden imports
- suggested wording
- draft entry

## Copy/Paste Entry Packet

```text
ENTRY PACKET

Entry id:
  [E__] or [K__]

Headword:

Status:
  draft | candidate | accepted | superseded

Role:
  kinematic | raw | scaffold | chimney | triplet-November |
  triplet-winter | wall | concrete acting-object | boundary | note

Law/block:

Source status:
  captures D2[E__] | revised from D2[E__] | new Design 3 entry |
  copied from:

Old wording:
  paste exact source if useful

Preserve:
  -

Change / reject:
  -

Plain purpose:

IRIL - ideal residually imparted logic:
  Allowed:
  Blocked:
  Trace consequence:

IRIEs - ideal residually imparted effects:
  Reader/modeler behaviour to install:
  Anti-habit / anti-misread:

Trace critical headword mentions:
  Earlier-entry headwords that must appear in the final entry wording:
  -

Other headword mentions:
  Earlier-entry headwords mentioned incidentally or in notes:
  -

Forbidden headword mentions / hidden imports:
  - headword or habit:
    why forbidden or risky:

Question or trace moment this helps with:
  Plain-language question, lookup, or trace situation.

Witness kind:
  point-particle | material-object | free-particle | reference-frame |
  inertial-frame | mechanical-system | interaction-set | interaction |
  impressed-force | acting-object | interaction-candidate |
  interaction-pair | other:

Slots read:
  -

Slots written / exposed:
  -

Boundary behavior:
  undefined referent | missing input | contradiction | random/input boundary |
  domain boundary | none expected

Suggested wording:
  Candidate wording or fragments under consideration. This is not the installed
  entry unless it is copied into Draft entry.

Draft entry:
  headword :=

Open questions:
  -
```

## Optional Deep-Audit Add-On

Use this only when an entry is tricky.

```text
DEEP AUDIT ADD-ON

Role test:
  If triplet: does it face inward toward only the other law headwords?
  If wall/chimney: can it be read outwardly as a normal definition?

Necessary/sufficient/asymmetric relations:
  -

Quantifier or modality:
  every | some | may | must | can | cannot | other:

Suspends for human/model input?
  yes/no; what input:

Boundary trigger:

Boundary output:

Alternative wordings:
  A:
  B:
  C:

Chosen wording:

Why chosen:

Checks:
  - required trace critical headwords present?
  - forbidden headwords avoided?
  - intended question or trace moment supported?
  - anti-misread blocked?
  - simple enough for intended interpreter?
```

## Six-Entry Law Block Packet

Use this when drafting a full house/chimney unit.

```text
SIX-ENTRY LAW BLOCK PACKET

Law/block name:

November word:

Winter word A:

Winter word B:

Operational question this block should answer:

Chimney / peripheral November entry:
  entry id:
  headword:
  outward definition job:
  source / preservation:
  trace critical headword mentions:
  other headword mentions:
  forbidden headword mentions / hidden imports:
  residual design:
  draft:

Triplet entry 1 / November redefine:
  entry id:
  headword:
  trace critical headword mentions:
  other headword mentions:
  forbidden headword mentions / hidden imports:
  IRIL - ideal residually imparted logic:
  IRIEs - ideal residually imparted effects:
  draft:

Triplet entry 2 / Winter A:
  entry id:
  headword:
  trace critical headword mentions:
  other headword mentions:
  forbidden headword mentions / hidden imports:
  IRIL - ideal residually imparted logic:
  IRIEs - ideal residually imparted effects:
  draft:

Triplet entry 3 / Winter B:
  entry id:
  headword:
  trace critical headword mentions:
  other headword mentions:
  forbidden headword mentions / hidden imports:
  IRIL - ideal residually imparted logic:
  IRIEs - ideal residually imparted effects:
  draft:

Wall / peripheral Winter A:
  entry id:
  headword:
  outward definition job:
  source / preservation:
  trace critical headword mentions:
  other headword mentions:
  forbidden headword mentions / hidden imports:
  witness or attribute slots:
  residual design:
  draft:

Wall / peripheral Winter B:
  entry id:
  headword:
  outward definition job:
  source / preservation:
  trace critical headword mentions:
  other headword mentions:
  forbidden headword mentions / hidden imports:
  witness or attribute slots:
  residual design:
  draft:

Overlap note:
  Which wall may become a later chimney?

Checks:
  - Does each triplet corner avoid stating the whole law by itself?
  - Does each triplet corner expose the intended trace critical headwords?
  - Does each entry avoid forbidden headwords and hidden imports?
  - Do the walls carry recognition hooks and practical outward meaning?
  - Are human/model inputs routed to witness slots, scaffolds, concrete entries,
    or explicit boundaries rather than hidden inside the abstract triplet?
  - Do the residual effects train the intended modelling behaviour?
```

## Copy/Paste Source Bin

Use this section when asking Codex to help. Paste exact source snippets here
instead of paraphrasing when wording matters.

```text
SOURCE BIN

Relevant current structure row:
  paste row from DESIGN_3_ENTRY_STRUCTURE.md

Relevant old entry:
  paste D2/D2.1 entry here

Relevant witness sheet:
  paste witness kind or slots here

Relevant guide rule:
  paste any rule from the entry-writing guide here

Human note:
  what you want changed, preserved, or tested
```

## Codex Request Starters

```text
Using this entry packet, draft the VD entry in the current Design 3 style.
Keep triplet entries inward-facing and peripheral entries outward-facing.
Tell me which fields are still underdetermined.
```

```text
Using this six-entry law block packet, check whether the house/chimney
structure is coherent. Flag any hidden textbook imports or missing witness
slots before rewriting.
```

```text
Copy the source wording into the draft only where it helps. Preserve the
handle/residual behavior over explanatory prose.
```
