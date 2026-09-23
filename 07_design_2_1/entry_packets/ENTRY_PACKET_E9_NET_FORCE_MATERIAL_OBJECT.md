# Entry Packet: E9 Net-Force-Material-Object

Status: substantive packet draft; structural fields, residual design, and a
candidate entry are present, with open decisions recorded below.

## ENTRY PACKET

Entry id:
  [E9]

Headword:
  net-force-material-object

Status:
  candidate

Role:
  triplet-winter

Law/block:
  Newton II; net-force corner of the addressed triplet

Source status:
  revised from D2[E22]. Governed by the NML2.1 managed-context snapshot at
  VD-docs commit `b23f5a215783aca8811598ceb5e783a7fdfd9726`.

Source hierarchy:
  1. `07_design_2_1/notes/lesson_entry_notes/NML2_ENTRY_RENUMBERING_DECISION_2026-07-23.md`.
  2. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md`.
  3. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md`.
  4. E8 and E10 packets as the other triplet corners.
  5. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and the six-entry guide.
  6. D2[E22] and older local NML2 notes, only where consistent.

Old wording lineage:

```text
net-force :=
The vector quantity satisfying net-force = inertial-mass times
inertial-acceleration for a point-particle.
```

Preserve:
  - the result is one vector addressed to one material object;
  - it is the product-side corner of the Newton-II constraint;
  - zero is a valid vector result for finite positive inertial mass and zero
    inertial acceleration.

Change / reject:
  - Use the official addressed headwords rather than generic quantities.
  - Do not identify this value with a single push, pull, or meter reading.
  - Do not define it as a sum of force contributions in this entry.
  - Do not infer free-particle status from a zero result.

Plain purpose:
  State the net-force-facing relation among the three official Newton-II
  headwords for one addressed material object.

Relationship to the packet set:
  - one winter daughter of E8;
  - relates E10's inertial mass to E8's inertial acceleration;
  - receives its outward-facing handle at E11;
  - its later physical production belongs beyond NML2.1.

Trace critical headword mentions:
  - inertial-mass-material-object
  - inertial-acceleration-material-object

Other structural qualifier:
  - the same material-object address must govern all three values.

Forbidden headword mentions / hidden imports in the eventual entry wording:
  - interacting-forces-set / impressed-force / force-sum — later block.
  - newton meter / pull / push — not identical to the net-force value.
  - free-particle — zero net force does not establish that status.
  - force causes motion — causal overclaim.

Question or trace moment this helps with:
  Given this material object's inertial mass and inertial acceleration, what net
  force does Newton II return?

Witness kind:
  addressed material-object force-accounting commitment; lightweight slots only.

Slots read:
  - material-object identity
  - inertial-mass-material-object
  - inertial-acceleration-material-object
  - common frame and time/interval qualification
  - provenance/licence status of both inputs

Slots written / exposed:
  - net-force-material-object
  - Newton-II inference provenance
  - zero/nonzero vector status

Boundary behavior:
  - missing input: either daughter quantity is absent or not supplied;
  - undefined/domain boundary: inertial mass lacks a positive licensed referent;
  - contradiction: daughter quantities do not share one owner or compatible
    frame/time qualification;
  - zero case: return the zero vector without inferring absence of contributions
    or free-particle status.

IRIL - ideal residually imparted logic:

  Allowed:
    - On a demand for `net-force-material-object[A]`, demand
      `inertial-mass-material-object[A]` and
      `inertial-acceleration-material-object[A]` for the same material-object
      address.
    - When both daughter values are present, compatible, and licensed, multiply
      the positive inertial-mass scalar by the inertial-acceleration vector.
    - Return a vector with the same direction as the acceleration vector when
      the latter is nonzero; return the zero vector when acceleration is zero.
    - Preserve the common material-object, inertial-frame, and time/interval
      qualifications and record E9 as the inference provenance.
    - If an independently supplied or wall-landed E11 net-force value is also
      present, compare it with the E9 result as a consistency check.

  Blocked:
    - Combining daughter values belonging to different material objects.
    - Multiplying by a missing, zero, negative, undefined, or unlicensed
      inertial-mass value. E10 supplies the positive-scalar law role.
    - Treating one supplied daughter value as enough to determine net force.
    - Generating a numerical vector when either daughter is merely named but
      has no bound value.
    - Treating the E9 result as a list or explanation of physical force
      contributions.
    - Identifying the result with one push, pull, newton-meter reading, or other
      salient interaction.
    - Inferring free-particle status or absence of force contributions from a
      zero vector.
    - Treating multiplication as the causal statement "force causes motion."

  Trace consequence:
    - With two compatible, licensed daughter values, return
      `inertial-mass-material-object[A] *
      inertial-acceleration-material-object[A]` as the E9 net-force answer and
      record both daughter exposures.
    - If inertial acceleration is absent, demand E8/E7 or a visible supplied
      input; a cycle with no second independent value terminates as insufficient
      information rather than generating an answer.
    - If inertial mass is absent, demand E10 or the currently supplied binding;
      if its outward account is required, halt at deferred E12/NML2.2.
    - If owner, frame, or time qualifications conflict, return a contradiction
      or mismatched-address halt.
    - If the mass-reuse licence has expired, return an unlicensed-input halt.
    - If an E11 value disagrees with the E9 result under the same
      qualifications, return a Newton-II consistency contradiction.

IRIEs - ideal residually imparted effects:

  Reader/modeler behaviour to install:
    - Put the same material-object address on mass and acceleration before
      multiplying.
    - Ask whether two independent, licensed daughter values are actually
      present.
    - Multiply a positive scalar by a vector and preserve the vector direction.
    - Keep object, frame, and time/interval qualifications attached to the
      resulting net-force vector.
    - Mark the result as Newton-II-inferred rather than physically decomposed.
    - Treat disagreement between an inferred E9 value and a supplied E11 value
      as an inconsistency to investigate, not as permission to choose one.

  Anti-habit / anti-misread:
    - Do not combine one object's mass with another object's acceleration.
    - Do not treat Newton II as an information generator when fewer than two
      independent triplet values are available.
    - Do not read the resulting vector as a newton-meter result or a named
      physical force contribution.
    - Do not infer which interactions produced the vector.
    - Do not read zero net force as zero velocity, free-particle status, or
      proof that no force contributions exist.
    - Do not continue after a material change has invalidated the mass binding.

Suggested wording:

  A, explicitly addressed:

  ```text
  net-force-material-object[A] :=

  inertial-mass-material-object[A] multiplied by
  inertial-acceleration-material-object[A].
  ```

  B, prose binder:

  ```text
  net-force-material-object :=

  For one material-object, inertial-mass-material-object multiplied by
  inertial-acceleration-material-object, with both quantities belonging to that
  same material-object.
  ```

  C, conventional mathematical compression:

  ```text
  net-force-material-object[A] :=

  inertial-mass-material-object[A] *
  inertial-acceleration-material-object[A].
  ```

Draft entry:

```text
net-force-material-object[A] :=

inertial-mass-material-object[A] multiplied by
inertial-acceleration-material-object[A].
```

## DEEP AUDIT ADD-ON

Role test:
  E9 is inward-facing. Its definiens exposes only the two other Newton-II
  triplet headwords. The repeated address makes this the net-force corner for
  one material object without importing E11 wall meaning or later force-sum
  machinery.

Necessary/sufficient/asymmetric relations:
  - A licensed positive `inertial-mass-material-object[A]` and a licensed
    `inertial-acceleration-material-object[A]` are jointly sufficient to
    determine `net-force-material-object[A]` through E9.
  - Either daughter alone is insufficient.
  - Matching the material-object address is necessary; matching numerical
    units without matching the owner is insufficient.
  - Frame and time/interval compatibility are necessary trace qualifications,
    although they are not additional triplet headwords in the entry string.
  - Zero acceleration with finite positive inertial mass is sufficient for a
    zero net-force vector.
  - A zero E9 result is not sufficient for free-particle status or absence of
    force contributions.
  - The E9 result constrains the value of net force but does not establish its
    physical provenance or decomposition.

Quantifier or modality:
  the shared address variable `[A]`; no verbal modal required in the chosen
  entry string.

Suspends for human/model input?
  yes; when either daughter value, its owner, its frame/time qualification, or
  its licence/provenance is not already available through entries or supplied
  problem data.

Boundary trigger:
  - missing inertial-mass value;
  - missing inertial-acceleration value;
  - expired mass-reuse licence;
  - different material-object addresses;
  - incompatible frame or time/interval qualifications;
  - dimensional or scalar/vector type mismatch;
  - disagreement with an independently supplied E11 net-force value.

Boundary output:
  - demand E10 or a supplied inertial-mass binding;
  - demand E8/E7 or a supplied inertial-acceleration input;
  - route the full mass-address account to deferred E12/NML2.2;
  - return an unlicensed-input halt after mass-binding expiry;
  - return a contradiction for address, qualification, type, dimensional, or
    E9/E11 consistency failure;
  - route force-provenance or contribution demands beyond E11 to the later
    force-sum block.

Residual provenance ledger:

| Phrase or symbol | Backing |
|---|---|
| `[A]` on all three headwords | NML2.1's canonical addressed-triplet notation (`m[A]`, `a[A]`, `F_net[A]`); mechanically repeats one owner token. |
| `multiplied by` | Elementary arithmetic operation already installed in the target culture; directs positive-scalar-by-vector multiplication at stock strength. |
| line order: inertial mass before inertial acceleration | Conventional Newton-II product order; makes scalar-by-vector typing visible without explanatory prose. |

Alternative wording assessment:
  - A is explicit and readable. Repeating `[A]` prevents cross-target borrowing
    while leaving only two daughter headwords in the definiens.
  - B avoids parameterised headword syntax, but is longer and repeats
    `material-object` as an additional visible headword inside the triplet.
  - C is shortest, but the bare multiplication symbol gives a weaker textual
    handle than `multiplied by` for less mathematically fluent interpreters.

Chosen wording:
  Candidate A.

Why chosen:
  It makes the same-owner constraint structural and leaves only the familiar
  multiplication operation as residual. The two daughter headwords carry the
  physics; E9 adds no force-source story or wall content.

Checks:
  - exactly two daughter headwords exposed: yes;
  - same material-object address explicit: yes;
  - no E11 wall content or force-sum machinery imported: yes;
  - zero case handled without free-particle overclaim: yes;
  - residual operation familiar and auditable: yes;
  - candidate is algebraically symmetric with E8 and the intended E10 corner:
    yes.

## Decisions made in this pass

1. E9 uses parameterised headword instances with the shared address `[A]`.
2. The final residual says `multiplied by` rather than using bare `*`.
3. Positivity is not restated in E9's entry string; it belongs to E10.
4. Frame, time, provenance, and licence remain trace qualifications rather than
   extra headwords in the inward triplet string.
5. E9 infers a net-force value but does not identify its physical contributions
   or measurement provenance.
6. Zero acceleration yields zero net force without a free-particle or
   no-contributions inference.

## Questions and decisions still open

1. Does the engine/tokenizer preserve the base headword match when `[A]` is
   appended directly, or should address arguments use a separate internal
   representation?
2. Should frame and selected time/interval eventually appear as explicit
   arguments alongside `[A]`, or is trace-side qualification sufficient?
3. When E11 supplies a net-force value independently, should E9 emit the
   consistency comparison itself, or should that be a general evaluator
   operation?
4. Should dimensional checking (`kg * m s^-2 -> N`) be an E9 residual effect,
   a general quantity-type operation, or both?
5. Does `Newton-II-inferred` need a formal provenance tag distinct from
   `supplied` and the later `force-sum-produced` provenance?
