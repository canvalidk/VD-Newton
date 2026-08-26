# NML3 Force-Sum Triplet Naming Decision — 2026-08-26

**Status:** ratified naming authority for the three Force-Sum corners.

## Decision

The Force-Sum triplet uses these headwords:

```text
net-force / impressed-force / interaction-set
```

`net-force` is unchanged. The other two choices are now settled:

- use `impressed-force`, not `V(f)`, `force-value`, or
  `impressed-force-value`, for the target-directed force contribution; and
- use `interaction-set`, not `IFS` or `interacting-forces-set`, for the
  target-indexed collection.

The inward relation is:

$$
\mathbf F_{\mathrm{net}}(p\mid C)
=
\sum_{i\in\operatorname{interaction\text{-}set}(p\mid C)}
\mathbf F_{\mathrm{impressed}}(i\to p\mid C).
$$

In ordinary language: the net force on a particle is the vector sum of the
impressed forces supplied by the interactions in that particle's interaction
set.

## Type boundary

The equation does not add interactions as though interactions were vectors.
It preserves this typed path:

```text
interaction i in interaction-set(p | C)
    -> impressed-force(i -> p | C)
    -> force-vector contribution to net-force(p | C)
```

Accordingly:

1. An `interaction-set` contains identity-bearing interactions, not anonymous
   vectors and not impressed-force values.
2. An `impressed-force` is the target-directed force action or vector
   contribution supplied by one of those interactions.
3. Distinct interactions remain distinct even when their impressed forces have
   equal vector values.
4. Membership and closure must be warranted independently of whether the
   resulting vector sum agrees with an independently determined net force.

## Scope deliberately left open

This decision settles only the three headwords and their minimum inward
relation. It does not settle:

- the new E-numbers or whether old numbers are reused;
- the final wall and chimney assignments;
- the exact interaction identity or membership warrant;
- the closure procedure for an interaction-set;
- the exact target, time, and context signature;
- the action/reaction representation;
- the remaining NML3 and later entry structure; or
- final entry prose beyond the naming and typed relation above.

The managed NML3 reset of 2026-08-17 still governs the retired E13–E17 cut.
This naming decision does not reinstate that numbering.

## Precedence and translation

This file has naming precedence for the Force-Sum triplet.

- Historical `IFS` and `interacting-forces-set` references translate to
  `interaction-set` when their underlying collection is carried forward.
- Historical `V(f)` references translate to the target-directed
  `impressed-force` supplied by the indexed interaction.
- Historical claims that the set itself contains impressed-force occurrences
  are not carried forward merely by renaming the set. The current set members
  are interactions.

`NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md` remains the authority
for choosing the word `impressed-force` and for rejecting its predecessor
names. This decision refines its earlier installed role by locating
`impressed-force` at the contribution corner of the Force-Sum triplet rather
than making it the identity-bearing member of the collection.

