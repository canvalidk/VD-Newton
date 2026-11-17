# Current Design 2.1 State

## One Sentence

Design 2.1 consolidates the Newton entries; its working ledger now includes the
November contribution-law and recursive Force-Sum proposals, ahead of the
installed entry wording.

## Proposed Continuation — Updated 2026-11-17

[DESIGN_2_1_ENTRY_STRUCTURE.md](DESIGN_2_1_ENTRY_STRUCTURE.md) now places:

```text
contribution law: net-force / contribution / haze
Force-Sum:        contribution / impressed-force / interaction-set
```

The ledger's P-labels are provisional entry addresses. E1–E12 keep their
existing locations, while E13-and-later routing is explicitly historical.
This is a structure update, not installation of final entry strings or a
replacement ratification of the August naming decision.

The working sequence is now explicit:

1. Supply a constructed interaction set with consistent numbering and length.
2. Start contribution_n at n = 0; add haze once outside the recursion.
3. In one conditional definition, use the member's impressed force plus the
   next contribution when length > n; otherwise return the zero vector.
4. Preserve the unexpanded tail when stopping early.

The set stays fixed; the counter is the changing traversal state. Reaching its
length makes no new claim about the physical system. The physical
no-more-elements claim belongs outside summation; the ledger proposes a
landing site at or behind the interaction-set wall. An erroneous comparison,
selection, or increment is a located step error. A zero force value is not a
stop condition.

The ledger also carries the November acting-object requirements: membership
entails activation under preserved bindings; the inverse and concrete force
routes address the same quantity; counterpart location can remain internal
or external until constrained. Their final house packaging is open.

The pinned November sources and their decision grades are linked in the
ledger. The 12 November record supersedes the 11 November suggestions of a
shrinking set and summation beginning before set construction finishes.

## Earlier Ratified Force-Sum Triplet Names — 2026-08-26

The August naming decision settled:

```text
net-force / impressed-force / interaction-set
```

It fixed names and minimum typed distinctions, while leaving entry numbers,
walls, membership, and closure open. See
`../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`.
The new ledger proposals separate explicit contribution from net force through
haze. The August record remains an earlier authority and has not been rewritten.

## Confirmed Structural Bug — 2026-08-12

`DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md` is the active design
authority for a confirmed error in the force-accounting structure. A condition
on the aggregate produced by a collection cannot, in general, determine whether
one candidate belongs to that collection.

Accordingly, the historical E13-and-later Force-Sum and dependent
action/reaction structure remains under correction. Design work must distinguish
the interaction candidate universe, interaction identity/equality, an individual membership rule, the
constructed and closed `interaction-set`, the target-directed
`impressed-force`, and only then vector aggregation. This does not
invalidate the completed NML2 entry work, whose packets explicitly defer force
enumeration and force-sum production.

## Adopted Force-Sum Abstraction Boundary — 2026-08-14

`FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` is now owned and
maintained by Design 2.1. Its active structural result supplied the distinction
that the 2026-08-26 naming decision now expresses as

```text
net-force / interaction-set / impressed-force
```

Force-Sum consumes an already constructed, identity-bearing `interaction-set`
and obtains a target-directed `impressed-force` from each interaction.
Individual membership and closure remain outside the aggregate equality, which
cannot perform those member-level jobs.

The note was transferred from the managed VD-docs snapshot
`canvalidk/VD-docs@cae6cd109c1dfcae4f6c1f57c89c5b91660351b2`, formerly at
`Newton/Design 3/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md`.
Its original chronological language is retained as historical evidence. Its
provisional `IFS` and `V(f)` notation translates under the 2026-08-26 decision
to `interaction-set` and target-directed `impressed-force`.

## Starting Point

The starting artifact is:

```text
07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md
```

It was copied from:

```text
DESIGN_3_ENTRY_STRUCTURE.md
```

The ledger retains the earlier Newton structure and historical downstream
routing, and now includes the November proposals. Final entry wording remains
in `DESIGN_2_1_DRAFT_1_ENTRIES.md`; the new P-labelled entries are not installed
there.

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

The list traversal now has a specified mathematical form: a supplied numbered
set, its length, and one conditional contribution definition. Construction
still needs interaction identity, admission, and the grounds for the physical
no-more-elements claim. These are separate from the mechanical counter test.

The contribution-law corners, haze wall, Force-Sum corners and walls now have
provisional ledger locations. Haze's peripheral contract and the full inward
Force-Sum definitions remain unfinished. The total contribution is C_0; net
force and haze alone do not determine every tail C_n.

Witness sheets mean peripheral scene testimony, which a person may consult
when answering a wall. Explicit trace bindings record the supplied information.
The ledger's demand inventory does not impose a sheet schema or a trace-side
sheet reader.

## What Design 2.1 Defers

Design 2.1 does not attempt to finish:

- full object schemas or a witness-sheet runtime;
- acting-object instance dispatch;
- spring, gravity, contact, or friction concrete clusters;
- external object detection;
- full closure reasoning through interaction-pairs;
- prediction-set machinery.

Deferred material can remain as notes or placeholders when needed. The
12 November probe demonstrates hand-driven recursion with scratch entries,
not an automatically checked implementation: argument arithmetic, the filing
of the increment, branch checking, and graph treatment of self-reference
remain open.

## Working Attitude

Design 2.1 should prefer explicit placeholders over silent gaps.

If a wall entry is needed but the exact final content is not ready, the entry
should say what kind of content must eventually land there and what the current
placeholder allows the trace to do.
