# NML2 Entry Renumbering Decision — 2026-07-23

Status: current steering decision for the active Design 2.1 entry surface.

## Decision

There are exactly two definitions of the Newton-II acceleration headword:

```text
[E7] inertial-acceleration-material-object — peripheral/chimney definition
[E8] inertial-acceleration-material-object — inward Newton-II definition
```

There is no separate `inertial-acceleration_point-particle` entry. Generic
point-particle motion is already covered by the earlier kinematic
`acceleration` entry. In the current Newton design, calling a quantity
`inertial-acceleration-material-object` places it in the massive/material-object
domain.

The NML2.1 entries therefore read:

```text
[E7]  inertial-acceleration-material-object — chimney
[E8]  inertial-acceleration-material-object — triplet November redefine
[E9]  net-force-material-object — triplet winter entry
[E10] inertial-mass-material-object — triplet winter entry
[E11] net-force-material-object — wall
[E12] inertial-mass wall — deferred until NML2.2
```

All later ledger entries move up by one number. The older NML1 E7/E8 decision
notes are retained as historical development records, but their separate
point-particle inertial-acceleration proposal is superseded by this decision.
