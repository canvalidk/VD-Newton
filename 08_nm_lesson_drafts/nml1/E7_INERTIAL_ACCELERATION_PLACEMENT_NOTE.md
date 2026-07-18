# E7 Inertial-Acceleration Placement Note

Status: first placement note, 2026-06-04.

## Question

Should `E7 inertial-acceleration` be included in NML1, or should NML1 end with
the Newton I house and leave `inertial-acceleration` for NML2?

## Source Lesson Boundary

The preserved NML1 draft is very explicit about its boundary:

```text
NM L1 ends before force.
```

It forbids these as active concepts in the lesson:

```text
force
net force
F = ma
mass as inertia
balanced forces
free-body diagrams
detailed acceleration calculations
```

The draft's final bridge says:

```text
NM L1:
What happens when no relevant influence shapes the path?

NM L2:
How do we calculate motion when influences are present?
```

That means full E7 mastery would be a real curriculum expansion, not a free
end-cap.

## What E7 Would Add

If E7 were taught as a full NML1 entry, the lesson would need to add:

```text
inertial-acceleration as a new headword
the contrast between raw acceleration and inertial-acceleration
the massive point-particle domain
the idea that Newtonian acceleration is acceleration in an inertial frame
the discipline of stopping before net-force and inertial-mass
```

That is conceptually elegant but pedagogically costly. It would lengthen both
the 80-minute version and the compressed 40-minute version, and it would create
a strong student expectation that the lesson should proceed to calculation.

## Same Headword, Different Entry Jobs

There are two consecutive entries with the same headword:

```text
E7 inertial-acceleration
  chimney / outward bridge from acceleration + inertial-frame

E8 inertial-acceleration
  Newton II triplet corner / inward relation to net-force and inertial-mass
```

So the curriculum question is not whether NML2 will contain
`inertial-acceleration`. It will. The real question is whether the chimney job
and the triplet job should be taught together in NML2, or split across the
NML1/NML2 boundary.

Splitting them has a real advantage:

```text
NML1 earns the frame condition.
E7 names the frame-qualified quantity that this earns.
NML2 begins by giving that quantity its Newton II law relation.
```

That means E7 can make NML1 feel consequential without yet opening
`net-force`, `inertial-mass`, or force calculation.

## Revised Best Current Judgment

Make E7 a light NML1 bridge/capstone in the 80-minute version, but not a full
mastery objective in the compressed 40-minute version.

```text
NML1 owns E1-E6.
NML1 may lightly install E7 as the bridge word.
NML2 owns E8-E12, with E7 reviewed as the already-earned chimney.
```

This keeps NML1's closure intact:

```text
free-body + inertial-frame -> uniform-motion
```

and preserves the lesson's central achievement:

```text
students can diagnose path problems without opening the force branch
```

The key restriction is that E7 must not become "Newton II starts now." It should
only say:

```text
when acceleration is read in an inertial frame, the later Newtonian acceleration
quantity is inertial-acceleration
```

## How E7 Can Fit In NML1 Without Opening Newton II

E7 can appear as a bridge sentence or teacher-facing coda:

```text
This is why later Newtonian acceleration must be read in an inertial frame.
Next lesson, that frame-qualified acceleration becomes inertial-acceleration.
```

For older or 80-minute classes, the teacher may add:

```text
We are naming the acceleration Newtonian mechanics will later calculate. We
are not calculating it yet.
```

Avoid adding `net-force`, `inertial-mass`, `F = ma`, force diagrams, or
acceleration calculations. If those open, E7 has turned into E8 too early.

## Why This Matters For NML2

This decision gives NML2 a clean opening:

```text
Last lesson, Newton I told us when a free body's path is uniform and why the
frame matters. Today we name the acceleration Newtonian mechanics is allowed
to use: inertial-acceleration.
```

If E7 has already been lightly installed, use:

```text
Last lesson, we named inertial-acceleration: acceleration read in an inertial
frame. Today Newton II tells us how that quantity is related to net-force and
inertial-mass.
```

Then NML2 can teach:

```text
E8  inertial-acceleration / net-force / inertial-mass
E9  net-force triplet corner
E10 inertial-mass triplet corner
E11 net-force wall
E12 inertial-mass wall
```

The bridge from NML1 to NML2 is therefore a controlled split:

```text
NML1 installs the E7 chimney lightly.
NML2 installs the E8 Newton II triplet relation.
```

## Decision Guardrail

If future drafts try to add E7 to NML1, check whether the lesson still passes
these tests:

```text
Can the 40-minute version still run?
Does the lesson still end before force?
Do students still leave with Newton I trace competence rather than a half-open
Newton II branch?
Is `inertial-acceleration` used only to show why frames matter, not to compute?
```

If any answer fails, E7 belongs wholly in NML2.
