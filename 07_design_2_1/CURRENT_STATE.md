# Current Design 2.1 State

## One Sentence

Design 2.1 is a conservative branch from Design 3 that aims to make the entry
structure more complete and usable by adding list machinery, cleaning wording,
and filling missing wall entries without fully implementing objects or witness
sheets.

## Starting Point

The starting artifact is:

```text
07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md
```

It was copied from:

```text
DESIGN_3_ENTRY_STRUCTURE.md
```

Only its title and opening ledger description have been renamed so far. The
entry content still mostly reflects the Design 3 structure and must be edited
deliberately.

## What Design 2.1 Keeps From Design 3

- The VD is an answer-producing trace system, not just a retrospective audit.
- Natural-language questions are normalised to headwords before expansion.
- Newton I is a frame bridge and justification layer, not the free-particle
  branch of Newton II.
- `ao0` and the old `Nothing -> Newton I` routing are not revived.
- Force accounting should not begin with a flat human-supplied force set.
- Human/model inputs should land at visible trace locations.
- Walls are allowed to carry recognition hooks, modelling commitments,
  placeholders, and ordinary peripheral meaning.

## What Design 2.1 Adds Or Emphasises

The new emphasis is lists.

The design should be able to talk about structures such as:

```text
list of acting-object candidates
list of attached-force contributions
interacting-forces-set as list-like accumulator or closed collection
no-more-items / list closure signal
empty list / zero-sum result where appropriate
```

The exact formal list vocabulary is not settled yet. Design 2.1 should create
enough explicit list treatment to keep force accounting and wall entries from
depending on vague prose.

## What Design 2.1 Defers

Design 2.1 does not attempt to finish:

- formal witness sheets;
- full object schemas;
- acting-object instance dispatch;
- spring, gravity, contact, or friction concrete clusters;
- external object detection;
- full closure reasoning through interaction-pairs;
- prediction-set machinery.

Deferred material can remain as notes or placeholders when needed.

## Working Attitude

Design 2.1 should prefer explicit placeholders over silent gaps.

If a wall entry is needed but the exact final content is not ready, the entry
should say what kind of content must eventually land there and what the current
placeholder allows the trace to do.

