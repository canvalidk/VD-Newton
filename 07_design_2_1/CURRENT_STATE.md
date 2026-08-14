# Current Design 2.1 State

## One Sentence

Design 2.1 is a conservative branch from Design 3 that aims to make the entry
structure more complete and usable by adding list machinery, cleaning wording,
and filling missing wall entries without fully implementing objects or witness
sheets.

## Confirmed Structural Bug — 2026-08-12

`DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md` is the active design
authority for a confirmed error in the force-accounting structure. A condition
on the aggregate produced by a collection cannot, in general, determine whether
one candidate belongs to that collection.

Accordingly, the E13-and-later force-sum, IFS, and dependent action/reaction
structure is under correction. Design work must first distinguish the candidate
universe, impressed-force identity/equality, an individual membership rule, the
constructed and closed IFS, and only then vector aggregation. This does not
invalidate the completed NML2 entry work, whose packets explicitly defer force
enumeration and force-sum production.

## Adopted Force-Sum Abstraction Boundary — 2026-08-14

`FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` is now owned and
maintained by Design 2.1. Its active structural result is the candidate
Force-Sum triplet

```text
net-force / interacting-forces-set (IFS) / impressed-force V(f)
```

Force-Sum consumes an already constructed, identity-bearing IFS and evaluates
each member through `V(f)`. Individual membership and closure remain behind the
IFS wall; force-member construction and the action/reaction orientation remain
behind the `impressed-force` wall. Aggregate equality cannot perform any of
those member-level jobs.

The note was transferred from the managed VD-docs snapshot
`canvalidk/VD-docs@cae6cd109c1dfcae4f6c1f57c89c5b91660351b2`, formerly at
`Newton/Design 3/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md`.
Its original chronological language is retained as historical evidence, but
all predecessor force-member names translate to the sole active headword
`impressed-force`.

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
list of impressed-force members
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
