# Newtonian Mechanics Lesson 2 Entry Notes - First Pass

Status: first-pass notes for editing, compiled 2026-06-03.

These notes cover the proposed Lesson 2 teaching unit:

```text
Newton II chimney: inertial-acceleration
Newton II triplet: inertial-acceleration / net-force / inertial-mass
Newton II walls: net-force / inertial-mass
```

The working hypothesis is that Lesson 2 should be the next six-entry law block
after the Newton I lesson:

```text
[E7]  inertial-acceleration chimney
[E8]  inertial-acceleration triplet
[E9]  net-force triplet
[E10] inertial-mass triplet
[E11] net-force wall
[E12] inertial-mass wall
```

This means Lesson 2 should not yet be the force-sum or list-machinery lesson.
It should teach the Newton II house itself: what quantity Newton II solves for,
which domain it applies to, and which two winter words it needs before later
force accounting can populate `net-force`.

## Lesson-Level Claim

Newtonian Mechanics Lesson 2 teaches Newton II as a frame-qualified,
mass-domain-limited calculation entry, not as the whole free-body-diagram
pipeline.

By the end, the student should be able to use:

```text
inertial-acceleration
net-force
inertial-mass
```

without collapsing them into ordinary textbook habits such as:

```text
acceleration is always inertial-acceleration
net-force is already the sum of listed forces
every point-particle has an inertial-mass
zero net force is the same as free-particle
```

The lesson should explicitly inherit Lesson 1's frame commitment:

```text
raw acceleration + inertial-frame commitment -> inertial-acceleration
```

It should also make the massive-particle boundary visible. Newton II applies
where `inertial-mass` has a positive scalar referent. A massless free particle
can still be handled by the Newton I path/uniform-motion route, but it does
not enter the Newton II `net-force / inertial-mass` route.

## Old Notes Summary

In `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md`, the Notes column for entries
`[E7]` through `[E12]` is currently blank.

The old operational wording is taken from `02_engine/newton.py` Design 2
entries `E20` through `E23`.

```text
E20 inertial-acceleration :=
The acceleration of a point-particle as measured in an inertial-frame.

E21 inertial-acceleration :=
For a point-particle, inertial-acceleration equals net-force divided by
inertial-mass: a = F/m.

E22 net-force :=
The vector quantity satisfying net-force = inertial-mass times
inertial-acceleration for a point-particle.

E23 inertial-mass :=
The positive scalar coefficient m such that net-force = m times
inertial-acceleration for a point-particle.
```

Design 2.1 should revise the repeated `point-particle` wording to the safer
Newton II domain wording:

```text
massive-particle
```

or:

```text
point-particle with an inertial-mass referent
```

The shorter `massive-particle` wording is probably better for the entry text,
provided the `inertial-mass` wall makes the referent boundary clear.

## What NML2 Should Be

NML2 should be the Newton II block, with a small prerequisite reminder that
Newton II concerns a massive point-particle described in an inertial-frame.

It should do three jobs:

1. Bridge the kinematic `acceleration` entry from Lesson 1's frame commitment
   into `inertial-acceleration`.
2. Install the Newton II relation among `inertial-acceleration`, `net-force`,
   and `inertial-mass`.
3. Mark the two immediate walls: `net-force` is the resultant force vector that
   later force-sum machinery must justify, and `inertial-mass` is the positive
   scalar referent that gates the massive-particle domain.

It should deliberately not do these jobs yet:

```text
enumerate acting objects
build interacting-forces-set
close a force list
dispatch spring/gravity/contact/friction entries
teach action-reaction pairing
solve full free-body diagrams
```

Those belong to the next block, probably NML3:

```text
Force-sum / interacting-forces-set / attached-force
```

## [E7] Newton II Chimney - `inertial-acceleration`

### Current Ledger Row

```text
| [E7] | Newton II chimney; inertial-acceleration. | Captures D2[E20]. | massive-particle status; inertial-frame commitment; inertial-acceleration |  |
```

### Old Design 2 Wording

```text
inertial-acceleration :=
The acceleration of a point-particle as measured in an inertial-frame.
```

### Proposed Design 2.1 Note

This is the Lesson 2 entry point. It should connect the already-known
kinematic entry `acceleration` to the Newton I wall's `inertial-frame`
commitment.

Use the simple teaching shape:

```text
acceleration, when the selected frame is being treated as inertial
```

The entry should make clear that `inertial-acceleration` is not a new
kinematic derivative. The derivative work was already done by `acceleration`.
The new content is the frame status: this acceleration is being read in a
frame where ordinary Newtonian force accounting is licensed.

Prefer wording close to:

```text
inertial-acceleration :=
For a massive-particle, inertial-acceleration is its acceleration as described
in an inertial-frame.
```

Open wording issue:

`massive-particle` is not yet a separate kinematic entry. If that feels too
early, the chimney can say:

```text
For a point-particle with an inertial-mass referent...
```

But this is heavier. The better lesson design is probably to let the
`inertial-mass` wall establish that a massive-particle is a point-particle for
which `inertial-mass` has a positive scalar referent.

Avoid putting the equation here. This chimney should prepare the Newton II
triplet, not state the law.

## [E8] Newton II Triplet - `inertial-acceleration`

### Current Ledger Row

```text
| [E8] | Newton II triplet; inertial-acceleration November redefine. | Captures D2[E21]. | massive-particle; inertial-acceleration; net-force; inertial-mass |  |
```

### Old Design 2 Wording

```text
inertial-acceleration :=
For a point-particle, inertial-acceleration equals net-force divided by
inertial-mass: a = F/m.
```

### Proposed Design 2.1 Note

This is the inward-facing Newton II November entry. It should expose only the
two winter headwords needed to answer an `inertial-acceleration` demand:

```text
net-force
inertial-mass
```

Use the safer domain wording:

```text
For a massive-particle, inertial-acceleration is net-force divided by
inertial-mass.
```

The trace effect is:

```text
demand inertial-acceleration
  -> demand net-force
  -> demand inertial-mass
  -> divide vector by positive scalar
```

Do not make this entry enumerate forces. It should accept `net-force` as a
headword demand whose own wall/triplet/future block supplies the value.

Do not treat a missing `inertial-mass` as zero. Missing inertial mass is an
undefined-referent or domain boundary, especially for massless particles.

## [E9] Newton II Triplet - `net-force`

### Current Ledger Row

```text
| [E9] | Newton II triplet; net-force winter entry. | Captures D2[E22]. | massive-particle; net-force; inertial-mass; inertial-acceleration |  |
```

### Old Design 2 Wording

```text
net-force :=
The vector quantity satisfying net-force = inertial-mass times
inertial-acceleration for a point-particle.
```

### Proposed Design 2.1 Note

This is the `net-force` corner of the Newton II triplet. It should define
`net-force` only as the Newton II counterpart of `inertial-mass` and
`inertial-acceleration`.

Use:

```text
For a massive-particle, net-force is inertial-mass times
inertial-acceleration.
```

This triplet entry should not say what individual forces are acting. That
belongs to the force-sum block. Here, `net-force` is the single resultant
vector required by the Newton II relation.

The lesson should flag that `net-force = 0` is a possible Newton II value for
a massive-particle. It is not the same phrase as `free-particle`.

Useful student contrast:

```text
zero net force
  a Newton II force-accounting result for a massive-particle

free-particle
  a Newton I status: no relevant mechanical influence for the path/frame route
```

## [E10] Newton II Triplet - `inertial-mass`

### Current Ledger Row

```text
| [E10] | Newton II triplet; inertial-mass winter entry. | Captures D2[E23]. | massive-particle; inertial-mass; net-force; inertial-acceleration |  |
```

### Old Design 2 Wording

```text
inertial-mass :=
The positive scalar coefficient m such that net-force = m times
inertial-acceleration for a point-particle.
```

### Proposed Design 2.1 Note

This is the `inertial-mass` corner of the Newton II triplet. It should preserve
three things:

```text
positive
scalar
coefficient relating net-force to inertial-acceleration
```

Use:

```text
For a massive-particle, inertial-mass is the positive scalar coefficient in the
relation net-force = inertial-mass times inertial-acceleration.
```

This entry should not define inertial mass as "amount of matter" or as weight.
Those are ordinary teaching associations, but they are not the residual handle
needed here.

It should also avoid a brittle algebraic inversion such as:

```text
inertial-mass = net-force / inertial-acceleration
```

because zero acceleration and vector division make that form a bad general
handle. The coefficient wording is safer.

## [E11] Newton II Wall - `net-force`

### Current Ledger Row

```text
| [E11] | Newton II wall; net-force. |  | massive-particle; net-force; interacting-forces-set |  |
```

### Old Design 2 Wording

There is no old standalone Newton II wall for `net-force` in the Design 2
operational source. The next old `net-force` entry is the force-sum November
entry:

```text
net-force on particle p at time t is the vector sum of the acting-force
element|s in the interacting-forces-set for p at t.
```

### Proposed Design 2.1 Note

This wall should give outward-facing meaning without stealing the force-sum
block's work.

Use the wall to install:

```text
net-force is the single resultant force vector assigned to a massive-particle
at a selected time for the Newton II relation
```

Then mark its source as deliberately open:

```text
It may be supplied as a modelling input, measured or inferred from motion, or
produced later by summing a closed interacting-forces-set.
```

This gives the student a practical handle while preserving the Design 2.1
list decision. The wall may mention `interacting-forces-set`, but only as the
later source of the value, not as something Lesson 2 already unfolds.

The wall should explicitly protect the zero case:

```text
a zero net-force is the zero vector result of a force account, not a command to
route the particle through Newton I
```

That sentence may be too long for the final entry text, but it belongs in the
lesson note.

Possible draft wording:

```text
net-force :=
The single resultant force vector assigned to a massive-particle at a selected
time for the Newton II relation. In Design 2.1, its detailed production is
handled by the later force-sum entries.
```

This is probably a usable placeholder wall. It does not yet tell the trace how
to generate the force list, but it gives `net-force` a controlled landing site.

## [E12] Newton II Wall - `inertial-mass`

### Current Ledger Row

```text
| [E12] | Newton II wall; inertial-mass. |  | massive-particle; inertial-mass |  |
```

### Old Design 2 Wording

There is no old standalone Newton II wall for `inertial-mass` in the Design 2
operational source beyond the triplet wording in E23.

### Proposed Design 2.1 Note

This wall should give the outward-facing recognition hook for `inertial-mass`
and establish the Newton II domain boundary.

Use the wall to say:

```text
inertial-mass is the positive scalar property of a massive-particle that
appears as the denominator/coefficient in Newton II
```

It should mention ordinary units only if useful:

```text
usually measured in kilograms
```

The most important lesson role is the boundary:

```text
If a point-particle has no inertial-mass referent, Newton II does not return an
inertial-acceleration for it.
```

This preserves the massless-particle correction from Lesson 1. A photon can be
free for Newton I path reasoning while still being outside the Newton II
massive-particle pipeline.

Possible draft wording:

```text
inertial-mass :=
The positive scalar property of a massive-particle, usually measured in
kilograms, that relates net-force to inertial-acceleration in Newton II. A
point-particle without this referent is outside the Newton II acceleration
route.
```

This wording is longer than ideal but probably acceptable for a wall. The final
entry may be shortened after the lesson boundary is accepted.

## Suggested Lesson 2 Success Tests

After teaching these six entries, a student should be able to answer:

```text
What is inertial-acceleration, and how is it different from raw acceleration?
Why did Lesson 1 need an inertial-frame wall before Newton II?
What does Newton II demand when asked for inertial-acceleration?
What is net-force in the Newton II relation?
What is inertial-mass in the Newton II relation?
Why is a massless free particle outside the Newton II acceleration route?
Why is zero net-force not the same phrase as free-particle?
Why is the force-sum/list machinery not part of this lesson yet?
```

The expected sign of success is that the student's answers terminate cleanly:
they should point to the kinematic acceleration entry, the inertial-frame
commitment, the Newton II triplet, the net-force placeholder wall, the
inertial-mass domain boundary, or the later force-sum block.

They should not terminate in vague textbook habits such as:

```text
just use F = ma
forces are whatever is in the diagram
if F is zero, use Newton I instead
mass is whatever all particles have
acceleration is frame-independent
```

## Recommended Next Move

If this Lesson 2 boundary is accepted, the next drafting pass should produce
the actual Design 2.1 draft entries for `[E7]` through `[E12]`.

The likely final entry style is:

```text
[E7]  short chimney for inertial-acceleration
[E8]  inward Newton II formula from inertial-acceleration
[E9]  inward Newton II formula from net-force
[E10] inward Newton II coefficient wording from inertial-mass
[E11] usable placeholder wall for net-force, pointing to force-sum
[E12] usable wall for inertial-mass, including the undefined-referent boundary
```

Then NML3 can take up:

```text
[E13]-[E18] force-sum / interacting-forces-set / attached-force / list closure
```
