# Entry Packet: E10 Inertial-Mass-Material-Object

Status: substantive packet draft; structural fields, residual design, and a
candidate entry are present, with open decisions recorded below.

## ENTRY PACKET

Entry id:
  [E10]

Headword:
  inertial-mass-material-object

Status:
  candidate

Role:
  triplet-winter

Law/block:
  Newton II; inertial-mass corner of the addressed triplet

Source status:
  revised from D2[E23]. Governed by the NML2.1 managed-context snapshot at
  VD-docs commit `b23f5a215783aca8811598ceb5e783a7fdfd9726`.

Source hierarchy:
  1. `07_design_2_1/notes/lesson_entry_notes/NML2_ENTRY_RENUMBERING_DECISION_2026-07-23.md`.
  2. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md`.
  3. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md`.
  4. E8 and E9 packets as the other triplet corners.
  5. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and the six-entry guide.
  6. D2[E23] and older local NML2 notes, only where consistent.

Old wording lineage:

```text
inertial-mass :=
The positive scalar coefficient m such that net-force = m times
inertial-acceleration for a point-particle.
```

Preserve:
  - inertial mass is positive and scalar;
  - this entry states its inward Newton-II relation only;
  - the value is addressed to the same material object as the other corners;
  - a suitable nonzero trial can constrain or infer the coefficient.

Change / reject:
  - Do not perform the deferred outward wall's target/address construction.
  - Do not equate inertial mass with gravitational mass, material amount,
    density mass, weight, or a scale reading.
  - Do not use unrestricted vector division as the defining operation.
  - Do not let `0/0` determine a mass.

Plain purpose:
  Complete the Newton-II triplet by identifying the positive scalar coefficient
  relating this material object's addressed inertial acceleration and net force,
  without yet supplying the full NML2.2 mass-address wall.

Relationship to the packet set:
  - one winter daughter of E8;
  - relates E9's net force to E8's inertial acceleration;
  - deliberately does not replace the deferred E12 outward wall;
  - its supplied value may be consumed by E8 and E9 only while licensed.

Trace critical headword mentions:
  - net-force-material-object
  - inertial-acceleration-material-object

Other structural qualifier:
  - the same material-object address must govern all three values.

Forbidden headword mentions / hidden imports in the eventual entry wording:
  - scale / weight / gravitational mass / amount of matter / density mass.
  - mass additivity — no additivity licence is granted here.
  - target construction / trackability / lumping — NML2.2.
  - interacting-forces-set / impressed-force — later force-sum machinery.

Question or trace moment this helps with:
  What positive scalar coefficient relates this material object's net force and
  inertial acceleration in the Newton-II triplet?

Witness kind:
  addressed material-object force-accounting commitment; lightweight supplied
  binding only, not the deferred NML2.2 address-construction machinery.

Slots read:
  - material-object identity
  - net-force-material-object
  - inertial-acceleration-material-object
  - common frame and time/interval qualification
  - supplied mass binding or suitable nonzero Newton-II trial
  - licence/provenance status

Slots written / exposed:
  - inertial-mass-material-object
  - positive-scalar status
  - supplied or Newton-II-inferred provenance
  - indeterminate/halt status for unsuitable trials

Boundary behavior:
  - missing input: no supplied binding and no suitable pair of other triplet
    values;
  - indeterminate: the zero/zero case does not determine a coefficient;
  - contradiction: force and acceleration are directionally incompatible with
    one positive scalar coefficient, or values have different owners;
  - unlicensed input: the previous mass binding has expired after a reuse
    trigger;
  - deferred boundary: origination, address construction, and persistence
    certification route to NML2.2/E12.

IRIL - ideal residually imparted logic:

  Allowed:
    - On a demand for `inertial-mass-material-object[A]`, demand
      `net-force-material-object[A]` and
      `inertial-acceleration-material-object[A]` for the same material-object
      address, unless a licensed mass binding is already supplied.
    - For a suitable nonzero trial, find the unique positive scalar coefficient
      whose multiplication of the acceleration vector gives the net-force
      vector.
    - Treat a nonzero pair as suitable only when the two vectors are parallel,
      point in the same direction, and share compatible frame and time/interval
      qualifications.
    - When a licensed mass binding is already supplied, preserve it and use the
      two other triplet values as a Newton-II consistency check rather than as
      an automatic replacement.
    - If both vectors are zero, accept their compatibility with a supplied
      positive mass binding while refusing to infer a unique mass from that
      trial.
    - Record whether the returned value was supplied or Newton-II-inferred.

  Blocked:
    - Unrestricted division of one vector by another.
    - Inferring a mass from the zero-vector/zero-vector case.
    - Combining force and acceleration values belonging to different material
      objects.
    - Returning a positive finite coefficient when exactly one of the two
      vectors is zero.
    - Inferring a positive coefficient from nonparallel or oppositely directed
      vectors, even when their magnitudes have a numerical ratio.
    - Treating a scale reading, weight, gravitational mass, density mass, or
      amount of matter as this value without a separately licensed bridge.
    - Inferring mass additivity, target construction, or persistence from the
      inward triplet relation.
    - Reusing a supplied mass binding after its licence has expired.

  Trace consequence:
    - With a compatible nonzero pair, return the unique coefficient satisfying
      `net-force-material-object[A] = inertial-mass-material-object[A] *
      inertial-acceleration-material-object[A]` and mark it
      `Newton-II-inferred`.
    - With two zero vectors and no supplied mass binding, return indeterminate:
      the relation is satisfied by every positive mass and determines none.
    - With two zero vectors and a licensed supplied mass binding, retain that
      binding and mark the trial consistent without claiming it inferred the
      mass.
    - If exactly one vector is zero, or the nonzero vectors differ in direction,
      return a Newton-II contradiction for a positive finite mass.
    - If either other triplet value is absent, demand E9 or E8/E7 as
      appropriate; a cycle with no second independent value terminates as
      insufficient information.
    - If the full origin, address, or persistence account for the mass is
      required, halt at deferred E12/NML2.2.

IRIEs - ideal residually imparted effects:

  Reader/modeler behaviour to install:
    - Look for one positive scalar coefficient linking the two vectors rather
      than trying to divide vectors mechanically.
    - Verify that force and acceleration belong to the same material object and
      share frame and time/interval qualifications.
    - For an inference, require a nonzero acceleration and verify that the force
      is parallel and points in the same direction.
    - Distinguish a supplied mass binding from a coefficient inferred from a
      suitable Newton-II trial.
    - Read a zero-force/zero-acceleration trial as compatible with positive mass
      but insufficient to determine its value.
    - Treat incompatibility as evidence of a bad address, qualification, input,
      or model rather than silently taking a magnitude ratio.

  Anti-habit / anti-misread:
    - Do not write or calculate unrestricted `force / acceleration` for vectors.
    - Do not let `0/0` choose a mass.
    - Do not ignore vector direction when magnitudes happen to divide cleanly.
    - Do not substitute weight, a scale reading, gravitational mass, or an
      amount-of-matter idea for inertial mass.
    - Do not assume masses add merely because they are positive scalars.
    - Do not reuse an old mass value across a material change without a current
      licence.

Suggested wording:

  A, positive-coefficient relation:

  ```text
  inertial-mass-material-object[A] :=

  the positive scalar coefficient that multiplies
  inertial-acceleration-material-object[A] to give
  net-force-material-object[A].
  ```

  B, shorter relational prose:

  ```text
  inertial-mass-material-object[A] :=

  the positive scalar coefficient relating
  inertial-acceleration-material-object[A] to
  net-force-material-object[A].
  ```

  C, nonzero-trial calculation:

  ```text
  inertial-mass-material-object[A] :=

  the magnitude of net-force-material-object[A] divided by the magnitude of
  inertial-acceleration-material-object[A], when both vectors are nonzero and
  point in the same direction.
  ```

Draft entry:

```text
inertial-mass-material-object[A] :=

the positive scalar coefficient that multiplies
inertial-acceleration-material-object[A] to give
net-force-material-object[A].
```

## DEEP AUDIT ADD-ON

Role test:
  E10 is inward-facing. Its definiens exposes only the two other Newton-II
  triplet headwords. The positive-scalar coefficient relation distinguishes
  the mass corner without importing the deferred E12 mass-address wall.

Necessary/sufficient/asymmetric relations:
  - A nonzero `inertial-acceleration-material-object[A]` and a same-direction
    `net-force-material-object[A]`, under compatible qualifications, are jointly
    sufficient to determine one positive scalar coefficient.
  - Either vector alone is insufficient.
  - Matching the material-object address is necessary; matching numerical
    values or units without matching the owner is insufficient.
  - Parallelism and the same direction are necessary for a positive scalar
    coefficient. Magnitude agreement alone is insufficient.
  - A zero acceleration and zero net force are compatible with any licensed
    positive mass but are insufficient to infer one.
  - Exactly one zero vector is sufficient for a Newton-II contradiction under
    the positive finite-mass commitment.
  - A supplied positive mass can satisfy the relation in a zero/zero trial, but
    that trial is not sufficient to establish the supplied value.
  - E10 identifies the coefficient role; it does not establish a general
    measurement procedure, mass additivity, gravitational equivalence, or the
    validity and persistence of the material-object address.

Quantifier or modality:
  `the` asserts uniqueness when a suitable trial determines the coefficient;
  `positive` fixes its scalar domain; `[A]` binds the common material-object
  address.

Suspends for human/model input?
  yes; when no licensed mass binding and no suitable nonzero force/acceleration
  pair is available, or when ownership, qualification, or provenance is
  missing.

Boundary trigger:
  - absent mass binding and an absent or zero/zero comparison pair;
  - expired mass-reuse licence;
  - different material-object addresses;
  - incompatible frame or time/interval qualifications;
  - exactly one zero vector;
  - nonparallel or oppositely directed nonzero vectors;
  - scalar/vector type or dimensional mismatch;
  - disagreement between a supplied mass and the other triplet values.

Boundary output:
  - demand E9 and E8/E7 values for a suitable nonzero trial;
  - return indeterminate for a zero/zero trial without a supplied binding;
  - preserve a licensed supplied binding through a consistent zero/zero trial;
  - return a contradiction for address, qualification, direction, zero/nonzero,
    type, dimensional, or triplet-consistency failure;
  - return an unlicensed-input halt after mass-binding expiry;
  - route mass origination, address construction, and persistence questions to
    deferred E12/NML2.2.

Residual provenance ledger:

| Phrase or symbol | Backing |
|---|---|
| `[A]` on all three headwords | NML2.1's canonical addressed-triplet notation (`m[A]`, `a[A]`, `F_net[A]`); mechanically repeats one owner token. |
| `the` | Marks the uniqueness of the coefficient for a suitable nonzero Newton-II trial; does not claim that every available trial determines it. |
| `positive scalar coefficient` | Preserved from the D2[E23] lineage and the NML2.1 triplet design; uses stock mathematical vocabulary. |
| `multiplies ... to give` | Elementary scalar-vector multiplication language; states `F = ma` without unsafe vector division. |

Alternative wording assessment:
  - A states the algebraic role directly, carries positivity in the mass corner,
    and remains valid in the zero/zero case without pretending that case infers
    the value.
  - B is shorter, but `relating` leaves the operation and scalar/vector typing
    less explicit.
  - C gives a useful fenced calculation for a suitable nonzero trial, but is too
    long and conditional for the core entry and can tempt magnitude-only
    reasoning if its direction condition is lost.

Chosen wording:
  Candidate A.

Why chosen:
  It defines inertial mass by its positive-scalar role in the addressed triplet,
  avoids vector division, and exposes exactly the acceleration and net-force
  headwords. It also allows the trace layer to distinguish definition,
  inference, consistency checking, and indeterminacy.

Checks:
  - exactly two daughter headwords exposed: yes;
  - same material-object address explicit: yes;
  - positive-scalar status explicit in the mass corner: yes;
  - no vector division or magnitude-only shortcut: yes;
  - zero/zero remains compatible but non-determining: yes;
  - no E12 wall content, scale semantics, or mass additivity imported: yes;
  - candidate completes the algebraic E8/E9/E10 triplet: yes.

## Decisions made in this pass

1. E10 uses parameterised headword instances with the shared address `[A]`.
2. The entry states a positive scalar coefficient relation rather than a
   quotient of vectors or magnitudes.
3. Positivity is explicit here because E10 is the inertial-mass corner.
4. A nonzero, same-direction force/acceleration pair can determine the unique
   coefficient; a zero/zero pair cannot.
5. Directional incompatibility and a one-zero/one-nonzero pair are Newton-II
   contradictions under the positive finite-mass commitment.
6. E10 does not originate the mass address or provide scale, gravitational,
   additivity, or persistence semantics; those remain outside this entry.

## Questions and decisions still open

1. Does the engine/tokenizer preserve the base headword match when `[A]` is
   appended directly, or should address arguments use a separate internal
   representation?
2. Should frame and selected time/interval eventually appear as explicit
   arguments alongside `[A]`, or is trace-side qualification sufficient?
3. Should a zero/zero trial receive the evaluator status `indeterminate`,
   `insufficient information`, or a distinct status that records both
   compatibility and non-identification?
4. Should directional and one-zero/one-nonzero failures be classified directly
   as contradictions by E10 or by a general Newton-II consistency evaluator?
5. Does `Newton-II-inferred` need a formal provenance tag distinct from
   `supplied`, and can that inference create a fresh binding after an older
   mass-reuse licence has expired?
6. Should dimensional checking and the meaning of `positive scalar
   coefficient` live in E10's residual effects, general quantity-type
   machinery, or both?
