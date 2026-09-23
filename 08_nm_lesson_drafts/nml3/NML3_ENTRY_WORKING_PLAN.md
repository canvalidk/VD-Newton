# NML3 Entry Working Plan

Status: naming fixed; entry cut, numbering, walls, and final wording open.

## Settled Force-Sum triplet

The three headwords are fixed by
`NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`:

```text
net-force / impressed-force / interaction-set
```

Their minimum inward relation is:

```text
for target particle p in context C:
    interaction-set(p | C) supplies the relevant interactions i
    each i supplies impressed-force(i -> p | C)
    net-force(p | C) is the vector sum of those impressed forces
```

The `interaction-set` contains interactions. It does not contain anonymous
vectors or impressed-force values. `impressed-force` names the target-directed
contribution obtained from an indexed interaction.

## Retired numbering

The former plan assigned the Force-Sum triplet and two walls to E13–E17. The
managed NML3 reset of 2026-08-17 retired that cut without selecting a
replacement. This plan does not reinstate it.

The existing E13–E17 rows and references remain historical routing evidence
until a separate entry-structure decision either reuses or replaces them.

## Decisions still to settle

- Whether the new cut reuses E13–E17 or advances to fresh numbers.
- Which of the three headwords is the November redefine and which two are the
  winter entries, if the ordinary triplet pattern is retained.
- Which outward walls are required and what each wall owns.
- The owner and time/interval/context qualifications shared by net force, the
  interaction set, and each impressed force.
- The identity criterion for one interaction.
- The executable warrant procedure by which an interaction enters a target's
  `interaction-set`.
- The evidence and representation that certify the interaction set complete,
  including the valid empty-set case.
- Whether construction is one-at-a-time, list-like, relational, or represented
  another way.
- How an indexed interaction supplies its target-directed `impressed-force`.
- How action/reaction structure relates the impressed forces supplied to the
  participants in one interaction.
- How the force-sum route interacts with E11's currently counted provenance
  statement.

Agreement between a current vector sum and an independently determined net
force must not by itself establish interaction-set closure; further
interactions may supply cancelling impressed forces.

## Suggested next production step

Develop the `interaction-set` and `impressed-force` entry-facing meanings
together, because their index/result boundary controls the Force-Sum equation.
Then decide the walls and numbering before writing final entries.

For each selected entry: create an entry packet, run an independent writing
pass, place the chosen wording in
`07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md`, and add a trace/evaluator
acceptance check before treating it as active.
