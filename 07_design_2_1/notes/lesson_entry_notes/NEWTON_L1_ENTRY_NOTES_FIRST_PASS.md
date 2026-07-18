# Newtonian Mechanics Lesson 1 Entry Notes - First Pass

Status: first-pass notes for editing, compiled 2026-05-19.

These notes cover the proposed Lesson 1 teaching unit:

```text
uniform-motion chimney
Newton I triplet: uniform-motion / inertial-frame / free-particle
Newton I walls: inertial-frame / free-particle
```

The working hypothesis is that this forms a closed enough teaching unit for a
40 or 80 minute Newtonian mechanics lesson. It starts from kinematic entries
the student has just learned and ends by grounding both winter entries with
wall meanings, so the student should not be left holding dangling branches.

## Lesson-Level Claim

Newtonian Mechanics Lesson 1 teaches the First Law house as a usable entry
unit, not as a slogan. By the end, the student should be able to use
`uniform-motion`, `inertial-frame`, and `free-particle` without feeling that
the new words point into ungrounded space.

The lesson should make clear that Newton I is a frame-and-free-particle
structure. It is not the old route where "no force" automatically bypasses
Newton II. A free massive particle can still be handled by Newton II through an
empty or zero-summing force list; Newton I supplies the frame/free-particle
criterion and the justification for inertial-frame use.

## Old Notes Summary

In `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md`, the Notes column for entries
`[E1]` through `[E6]` is currently blank.

The old operational wording is therefore taken from `02_engine/newton.py`
Design 2 entries `E14` through `E19`.

## [E1] Newton I Chimney - `uniform-motion`

### Current Ledger Row

```text
| [E1] | Newton I chimney; uniform-motion. | Captures D2[E14]. | velocity; speed; straight-line; time interval |  |
```

### Old Design 2 Wording

```text
uniform-motion :=
The state of being either stationary or moving along a straight-line with
constant speed. Equivalently, a point-particle is in uniform-motion on an
interval I if its velocity is constant throughout I; i.e. for all t1, t2 in I,
v(t1) = v(t2). A point-particle is in uniform-motion at time t0 if there
exists epsilon > 0 such that it is in uniform-motion on
(t0 - epsilon, t0 + epsilon).
```

### Proposed Design 2.1 Note

This is the Lesson 1 entry point. It should lean on the kinematic scaffold,
especially `path`, `straight-line`, `time-interval`, `trajectory`, `velocity`,
and `speed`.

For Design 2.1, emphasise that `uniform-motion` is recognised by splitting it
into two components:

```text
spatial component
  straight line / straight path

temporal component
  constant velocity / uniform traversal through time
```

This matches the earlier recognition that Newton's wording joins two ideas:
particles move "in a straight line" and do so "uniformly." The student should
therefore learn `uniform-motion` as a compound kinematic recognition, not as a
single unanalyzed slogan.

Use the simpler teaching shape:

```text
rest, or straight spatial path traversed with constant velocity over a
selected time-interval
```

The note should say that `uniform-motion` is a frame-indexed interval property
of a point-particle. It combines a spatial condition and a temporal condition:
no change of position in the frame, or straight-line path with constant
velocity over the interval.

Reference for this decision: `../kinematics/KINEMATIC_ENTRIES_FINAL_NOTES.md`
records K16 as
the Newton I chimney and says it "combines a spatial condition and a temporal
condition"; the dependency guardrails restate this as "`uniform-motion` uses
both `path` and `time-interval`: spatially, rest or straight path; temporally,
uniform traversal."

Avoid making this entry carry Newton I itself. It is the chimney: it gives the
student the prior grip on `uniform-motion` before the First Law triplet uses
it.

## [E2] Newton I Triplet - `uniform-motion`

### Current Ledger Row

```text
| [E2] | Newton I triplet; uniform-motion November redefine. | Captures D2[E15]. | uniform-motion; free-particle status; inertial-frame commitment |  |
```

### Old Design 2 Wording

```text
uniform-motion :=
The state of motion exhibited by a free-particle when described in an
inertial-frame.
```

### Proposed Design 2.1 Note

This is the inward-facing triplet entry. It should keep the law relation short:

```text
uniform-motion is the trajectory-pattern of a free-particle in an
inertial-frame
```

The note should emphasise that this is not a general definition of all uniform
motion. It is the First Law relation viewed from the `uniform-motion` corner.
The operational use is to connect the already-understood kinematic pattern to
the two new law words: `free-particle` and `inertial-frame`.

Make the kinematic dependency explicit: this triplet entry reuses the Design
2.1 scaffold in which `trajectory` is the time-indexed kinematic attribute of a
point-particle in a reference-frame over a time-interval, and `uniform-motion`
is the recognised pattern of that trajectory: rest, or straight path with
constant velocity.

Do not add examples, measurement procedures, or Newton II force accounting
here. Those belong to walls, later entries, or trace inputs.

## [E3] Newton I Triplet - `inertial-frame`

### Current Ledger Row

```text
| [E3] | Newton I triplet; inertial-frame winter entry. | Captures D2[E16]. | reference-frame slots; free-particle status; uniform-motion |  |
```

### Old Design 2 Wording

```text
inertial-frame :=
A reference-frame in which every free-particle exhibits uniform-motion.
```

### Proposed Design 2.1 Note

This is the `inertial-frame` corner of the First Law triplet. It should remain
very close to the old wording because it is the cleanest statement of the
criterion:

```text
a reference-frame in which the trajectories of free particles exhibit
uniform-motion
```

The note should mark this as the internal law criterion, not the ordinary wall
meaning. It introduces `inertial-frame` as a frame judged by what happens to
free particles in it.

For Lesson 1, this is where students should see that a frame is not inertial
just because it is convenient. It earns the inertial commitment by making the
trajectory of a free particle come out as rest, or a straight path with
constant velocity, in that frame.

This should explicitly reference the Design 2.1 kinematic entries: a
`reference-frame` supplies the coordinate and clock convention; a `trajectory`
maps time to displacement vectors in that frame over a time-interval; and
`uniform-motion` classifies that trajectory by its straight-line/constant
velocity pattern.

## [E4] Newton I Triplet - `free-particle`

### Current Ledger Row

```text
| [E4] | Newton I triplet; free-particle winter entry. | Captures D2[E17]. | point-particle status; frame of description; uniform-motion |  |
```

### Old Design 2 Wording

```text
free-particle :=
A point-particle that, when described in an inertial-frame, exhibits
uniform-motion.
```

### Proposed Design 2.1 Note

This is the `free-particle` corner of the First Law triplet. It should connect
particle status, inertial-frame description, and the trajectory's
uniform-motion pattern.

The note should flag a likely student confusion: this triplet entry does not
mean "a particle that enters a no-force shortcut instead of Newton II." It
means the law relation characterises what a mechanically free particle does in
an inertial frame.

Use the kinematic wording here too:

```text
a free-particle is a point-particle whose trajectory in an inertial-frame has
the uniform-motion pattern
```

That keeps the entry tied to `point-particle`, `trajectory`,
`reference-frame`, `path`, `time-interval`, and `velocity` rather than making
`free-particle` sound like a merely verbal label.

The wall entry will supply the outward-facing recognition hook:

```text
particle with no relevant mechanical influence
```

Keep the triplet entry relational and spare.

## [E5] Newton I Wall - `inertial-frame`

### Current Ledger Row

```text
| [E5] | Newton I wall; inertial-frame. | Captures D2[E18]. | reference-frame slots; inertial-frame commitment; frame modelling input |  |
```

### Old Design 2 Wording

```text
inertial-frame :=
A reference-frame standard for Newtonian analysis of motion; historically, a
Galilean reference frame.
```

### Proposed Design 2.1 Note

This wall should ground `inertial-frame` for future Newtonian use. It is a good
place for the modelling commitment:

```text
the chosen frame is being treated as one in which accelerations represent
real mechanical influence rather than artifacts of the frame
```

The note should say that Lesson 1 students need the protective role of this
word: Newtonian force accounting only behaves cleanly after a suitable frame
has been chosen or assumed.

Add the fictitious-force warning here. In a non-inertial frame, raw
acceleration can include frame artifacts. If those artifacts are fed into
Newton II as though they were ordinary mechanical influences, the trace will
invent fictitious forces. The `inertial-frame` wall should therefore teach the
student that the frame commitment protects the later force account.

Also add the ordinary problem-reading convention:

```text
if a mechanics problem does not mention that the frame is accelerating,
rotating, or otherwise non-inertial, the intended classroom reading is usually
that the described frame is being treated as inertial
```

This convention should be marked as a modelling assumption, not as a theorem.

This wall may also carry the practical recognition hook:

```text
lab frame, Earth frame, or Galilean-style frame, when accepted as a modelling
approximation
```

Avoid saying that the wall "is for Newton II." The wall should be readable as
ordinary peripheral meaning, while still making the later Newton II frame
commitment possible.

## [E6] Newton I Wall - `free-particle`

### Current Ledger Row

```text
| [E6] | Newton I wall; free-particle. | Captures D2[E19]. | point-particle status; free-particle status; absence of relevant external influence |  |
```

### Old Design 2 Wording

```text
free-particle :=
A point-particle not subject to external influence relevant to its motion.
```

### Proposed Design 2.1 Note

This wall should give the outward-facing recognition hook for `free-particle`:

```text
a particle with no relevant mechanical influence
```

The note should preserve the Design 3 correction that massless particles such
as photons can count as free particles for path/uniform-motion reasoning, even
though they do not enter the Newton II inertial-mass pipeline.

Make the light/photon point visible. A freely propagating photon should be read
as a free particle for this wall: it has no `inertial-mass` referent for the
Newton II force/mass route, but it can still enter the Newton I path route.
That means:

```text
free photon + inertial-frame -> uniform-motion
```

and because `uniform-motion` has been split into straight path plus constant
velocity, light becomes the practical straight-path indicator for inertial
frame construction.

This is where Lesson 1 can allude to the first inertial-frame problem:

```text
freely propagating light helps determine what counts as a straight path in an
inertial frame
```

The note should also mark the broader boundary: all massless particles lack an
`inertial-mass` referent for Newton II, so any Newtonian path question about a
free massless particle has to route through the Newton I/free-particle
structure rather than through force divided by mass.

For Lesson 1, this entry should help students distinguish:

```text
free-particle
  no relevant mechanical influence

zero net force on a massive particle
  a force-accounting result that may later be computed by Newton II
```

This prevents the old mistake where `free-particle` becomes a hidden command to
skip force accounting.

## Suggested Lesson 1 Success Tests

After teaching these six entries, a student should be able to answer:

```text
What is uniform motion?
What makes a frame inertial?
What is a free particle?
Why is a free-particle not simply "an object with F = 0"?
Why does an acceleration question need a frame commitment?
Can a massless particle be free without being a Newton II massive particle?
```

The expected sign of success is not only correct answers. It is that the
student's answers terminate cleanly: they should point to kinematic entries,
the First Law relation, a modelling commitment, or a visible later boundary,
rather than to vague physics habit.
