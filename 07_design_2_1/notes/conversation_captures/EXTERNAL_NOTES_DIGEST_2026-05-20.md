# External Notes Digest - 2026-05-20

Status: quick digest of three notes from `VD docs/VD unsorted important`,
read into the Design 2.1 workspace on 2026-05-20.

Source files:

```text
C:\Users\canva\Documents\Amy hobby\VD instructions\VD docs\VD unsorted important\vd_newton_structure_session.md
C:\Users\canva\Documents\Amy hobby\VD instructions\VD docs\VD unsorted important\nm_l1_lesson_draft.md
C:\Users\canva\Documents\Amy hobby\VD instructions\VD docs\VD unsorted important\vd_pedagogy_note.md
```

## `nm_l1_lesson_draft.md`

Use for Newtonian Mechanics Lesson 1 notes.

Main claim:

```text
NM L1 installs the Newton I law-house as a runnable conceptual object.
```

The lesson starts with the path-problem rather than with force:

```text
Most observed paths are messy, curved, interrupted, or frame-dependent.
Newton I explains the commitments under which simple paths appear.
```

Lesson route:

```text
messy paths
-> influence
-> free-body / free-particle
-> uniform-motion
-> inertial-frame
-> diagnostic triangle
```

Core diagnostic:

```text
A puck appears to curve while no other object influences it. What should you
suspect?
```

Expected VD-native answer:

```text
If the body is genuinely free but does not exhibit uniform-motion, inspect the
frame. If the frame is inertial, inspect the free-body classification.
```

Important lesson constraints:

- Do not teach `force`, `net-force`, `F = ma`, balanced forces, free-body
  diagrams, normal force, or friction as formal force in NM L1.
- Use the pre-force handle `influence`.
- Treat `free-body` as a pedagogical outward-facing handle; the formal entry
  may remain `free-particle`.
- Do not let `uniform-motion` imply `free-body`.
- Do not define `inertial-frame` only as "non-accelerating frame."
- Include photons as massless free path-cases where useful.

## `vd_pedagogy_note.md`

Use for the general pedagogy framing behind NM L1.

Core claim:

```text
A good lesson is a controlled exposure sequence through a closed region of a
theory's entry graph.
```

Student confusion is described structurally:

```text
A student is confused when a word points onward but not to anything they can
act with.
```

Pedagogical consequences:

- A lesson should be defined by the entry-region being installed, not merely by
  a textbook topic.
- A six-entry law-house is a natural candidate lesson-size for teaching a law.
- Triplet work and wall work must be distinguished:

```text
Triplet work:
  how the new concepts lock together.

Wall work:
  how the new concepts become usable in ordinary modelling.
```

- Clarity means every opened branch has a visible termination.
- Age adaptation is handle translation, not structural dilution.
- Probes should test trace competence, not just definition recall.
- Assessments should track the shape of errors, such as premature force
  import, frame erasure, inversion error, mass contamination, Newton II
  collapse, and dangling slogan.

## `vd_newton_structure_session.md`

Use with caution. This is useful for later force-list and acting-object work,
but it partly conflicts with current Design 2.1 commitments.

Main points recorded:

1. The IFS fold may require an explicit seed.

```text
net-force = fold(+) over [acting-forces]
```

The note argues that the empty case needs a zero-vector seed. It leaves open
whether the seed lives in the data as `ao0` or in the operation as an explicit
fold accumulator.

Design 2.1 caution:

```text
Current Design 2.1 says `ao0` is rejected and old Nothing routing should not
be revived. If this seed argument is used, prefer "seed in the operation" until
the branch deliberately reopens the `ao0` question.
```

2. A Mechanical Membership law may be missing.

Candidate triplet:

```text
mechanical-composition_point-particle
mechanical-constituent
reaction-force_acting-object
```

The role would be to make mechanical-composition a list of constituents,
parallel to the IFS list of attached forces.

Design 2.1 relevance:

```text
This matches the existing Design 2.1 pressure for a missing item-role between
mechanical-composition_point-particle and acting-object.
```

3. No per-type acting-object law-houses.

The note rejects separate structural law-houses for spring, string, gravity,
etc. Concrete acting-object types should bind a name parameter in the generic
acting-object law rather than create new 3-cycles.

4. Dispatch belongs in the residual layer.

The proposed residual instruction:

```text
There are spring forces and spring activation-conditions. Couple them together
by the fact that they both share the name `spring`.
```

Shared name acts as the join key. The name-indexed database records the result
of this residual act.

Design 2.1 relevance:

```text
Useful later for acting-object notes, but probably beyond NM L1.
```

