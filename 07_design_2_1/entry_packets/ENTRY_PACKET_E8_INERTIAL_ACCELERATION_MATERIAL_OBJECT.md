# Entry Packet: E8 Inertial-Acceleration-Material-Object

Status: substantive packet draft; structural fields, residual design, and a
candidate entry are present, with open decisions recorded below.

## ENTRY PACKET

Entry id:
  [E8]

Headword:
  inertial-acceleration-material-object

Status:
  candidate

Role:
  triplet-November redefine

Law/block:
  Newton II; acceleration corner of the addressed triplet

Source status:
  revised from D2[E21]. Governed by the NML2.1 managed-context snapshot at
  VD-docs commit `b23f5a215783aca8811598ceb5e783a7fdfd9726`.

Source hierarchy:
  1. `07_design_2_1/notes/lesson_entry_notes/NML2_ENTRY_RENUMBERING_DECISION_2026-07-23.md`.
  2. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md`.
  3. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md`.
  4. E7, E9, and E10 packets as the other parts of this house.
  5. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and the six-entry guide.
  6. D2[E21] and the older NML2 first-pass note, only where consistent.

Old wording lineage:

```text
inertial-acceleration :=
For a point-particle, inertial-acceleration equals net-force divided by
inertial-mass: a = F/m.
```

Preserve:
  - Newton II determines the acceleration corner from the other two addressed
    quantities when their inputs are licensed.
  - The result is a vector in the selected inertial frame.
  - All three values have the same material-object owner and compatible
    time/interval qualification.

Change / reject:
  - Replace free-floating symbols with the three official material-object
    headwords.
  - Do not make Newton II generate missing information.
  - Do not restate E7's trajectory-read explanation inside the triplet.
  - Do not enumerate or sum force contributions.

Plain purpose:
  State the acceleration-facing relation among the three official Newton-II
  headwords for one addressed material object.

Relationship to the packet set:
  - inward redefinition of E7;
  - consumes the E9 and E10 headwords as its two winter daughters;
  - must agree algebraically and address-wise with E9 and E10;
  - does not perform the outward jobs of E11 or deferred E12.

Trace critical headword mentions:
  - net-force-material-object
  - inertial-mass-material-object

Other structural qualifier:
  - the same material-object address must govern all three values.

Forbidden headword mentions / hidden imports in the eventual entry wording:
  - trajectory / velocity construction — belongs to E7 and existing kinematics.
  - interacting-forces-set / attached-force / force contribution — deferred.
  - scale / weight / gravitational mass / material-amount mass — unlicensed.
  - force causes acceleration — replaces a constraint with causal prose.

Question or trace moment this helps with:
  Given this material object's net force and inertial mass, what inertial
  acceleration does Newton II return?

Witness kind:
  addressed material-object force-accounting commitment; lightweight slots only.

Slots read:
  - material-object identity
  - net-force-material-object
  - inertial-mass-material-object
  - common frame and time/interval qualification
  - provenance/licence status of both inputs

Slots written / exposed:
  - inertial-acceleration-material-object
  - Newton-II calculation provenance
  - information-sufficiency or halt status

Boundary behavior:
  - missing input: either daughter quantity is absent or not supplied;
  - undefined/domain boundary: inertial mass has no positive licensed referent;
  - contradiction: daughter quantities belong to different owners, frames, or
    incompatible intervals;
  - unlicensed input: a mass-reuse trigger has expired the supplied binding.

IRIL - ideal residually imparted logic:

  Allowed:
    - On a demand for `inertial-acceleration-material-object[A]`, demand
      `net-force-material-object[A]` and
      `inertial-mass-material-object[A]` for the same material-object address.
    - When both daughter values are present, compatible, and licensed, divide
      the net-force vector by the positive inertial-mass scalar.
    - Return a vector with the same direction as the net-force vector when the
      latter is nonzero; return the zero vector when net force is zero.
    - Preserve the common material-object, inertial-frame, and time/interval
      qualifications and record E8 as the calculation provenance.
    - If an independently trajectory-read E7 value is also present, compare it
      with the E8 result as a consistency check rather than replacing either
      silently.

  Blocked:
    - Combining daughter values belonging to different material objects.
    - Dividing by a missing, zero, negative, undefined, or unlicensed mass
      value. E10 supplies the positive-scalar law role; E8 does not repair a
      failed mass referent.
    - Treating one supplied daughter value as enough to determine the result.
    - Generating a numerical result when either daughter is merely named but
      has no bound value.
    - Enumerating force contributions, reading a force meter, or treating the
      net-force daughter as already decomposed.
    - Re-reading a trajectory, integrating motion, or constructing a future
      trajectory inside the triplet entry.
    - Treating division as a causal claim that force produces or causes
      acceleration.

  Trace consequence:
    - With two compatible, licensed daughter values, return
      `net-force-material-object[A] / inertial-mass-material-object[A]` as the
      E8 acceleration answer and record the daughter exposures.
    - If net force is absent, demand E9/E11 or a visible supplied input.
    - If inertial mass is absent, demand E10 or the currently supplied binding;
      if its outward account is required, halt at the deferred E12/NML2.2
      boundary.
    - If owner, frame, or time qualifications conflict, return a contradiction
      or mismatched-address halt.
    - If the mass-reuse licence has expired, return an unlicensed-input halt.
    - If an E7 value disagrees with the E8 result under the same qualifications,
      return a Newton-II consistency contradiction.

IRIEs - ideal residually imparted effects:

  Reader/modeler behaviour to install:
    - Put the material-object address on both input quantities before dividing.
    - Ask whether two independent, licensed daughter values are actually
      present.
    - Divide a vector by a positive scalar and preserve vector direction.
    - Keep object, frame, and time/interval qualifications attached to the
      result.
    - Distinguish a calculated E8 value from a trajectory-read E7 value while
      recognising that the two must agree when both apply.
    - Treat disagreement between E7 and E8 as information about an inconsistent
      model or input set, not as permission to choose the preferred value.

  Anti-habit / anti-misread:
    - Do not combine a force belonging to one object with another object's mass.
    - Do not treat Newton II as an information generator when fewer than two
      independent triplet values are available.
    - Do not replace `net-force-material-object` with a salient push, pull, or
      meter reading.
    - Do not read `a = F/m` as an explanation of physical force provenance.
    - Do not treat zero acceleration as zero velocity, free-particle status, or
      proof that no force contributions exist.
    - Do not continue after a material change has invalidated the mass binding.

Suggested wording:

  A, explicitly addressed:

  ```text
  inertial-acceleration-material-object[A] :=

  net-force-material-object[A] divided by
  inertial-mass-material-object[A].
  ```

  B, prose binder:

  ```text
  inertial-acceleration-material-object :=

  For one material-object, net-force-material-object divided by
  inertial-mass-material-object, with both quantities belonging to that same
  material-object.
  ```

  C, conventional mathematical compression:

  ```text
  inertial-acceleration-material-object[A] :=

  net-force-material-object[A] / inertial-mass-material-object[A].
  ```

Draft entry:

```text
inertial-acceleration-material-object[A] :=

net-force-material-object[A] divided by
inertial-mass-material-object[A].
```

## DEEP AUDIT ADD-ON

Role test:
  E8 is inward-facing. Its definiens exposes only the two other Newton-II
  triplet headwords. Address notation scopes all three headword instances to
  the same material object without adding wall content, examples, measurement
  procedures, or downstream mechanics.

Necessary/sufficient/asymmetric relations:
  - A licensed `net-force-material-object[A]` and a licensed positive
    `inertial-mass-material-object[A]` are jointly sufficient to determine
    `inertial-acceleration-material-object[A]` through E8.
  - Either daughter alone is insufficient.
  - Matching the material-object address is necessary; matching units without
    matching the owner is insufficient.
  - Frame and time/interval compatibility are necessary trace qualifications,
    even though they are not additional triplet headwords in the entry string.
  - A zero net-force vector with finite positive inertial mass is sufficient for
    a zero inertial-acceleration vector.
  - Zero acceleration is not sufficient for free-particle status or absence of
    force contributions.
  - E8 can calculate an acceleration before a future trajectory is known;
    initial conditions and motion construction remain separate.

Quantifier or modality:
  the shared address variable `[A]`; no verbal modal required in the chosen
  entry string.

Suspends for human/model input?
  yes; when either daughter value, its owner, its frame/time qualification, or
  its licence/provenance is not already available through entries or supplied
  problem data.

Boundary trigger:
  - missing net-force value;
  - missing or non-positive inertial-mass value;
  - expired mass-reuse licence;
  - different material-object addresses;
  - incompatible frame or time/interval qualifications;
  - dimensional or vector/scalar type mismatch;
  - disagreement with an independently available E7 value.

Boundary output:
  - demand E9/E11 or a supplied net-force input;
  - demand E10 or a supplied inertial-mass binding;
  - route the full mass-address account to deferred E12/NML2.2;
  - return an unlicensed-input halt after mass-binding expiry;
  - return a contradiction for address, qualification, type, dimensional, or
    E7/E8 consistency failure.

Residual provenance ledger:

| Phrase or symbol | Backing |
|---|---|
| `[A]` on all three headwords | NML2.1's canonical addressed-triplet notation (`m[A]`, `a[A]`, `F_net[A]`); mechanically repeats one owner token. |
| `divided by` | Elementary arithmetic operation already installed in the target culture; directs vector-by-positive-scalar division at stock strength. |
| line order: net force before inertial mass | Ordinary dividend/divisor grammar; matches the Newton-II acceleration form without adding causal prose. |

Alternative wording assessment:
  - A is explicit, auditable, and readable. Repeating `[A]` prevents the lesson's
    central cross-target error while leaving only two daughter headwords in the
    definiens.
  - B avoids parameterised headword syntax, but is longer and repeats
    `material-object` as an additional visible headword inside the triplet.
  - C is shortest, but `/` can be visually misread or overlooked more easily
    than the installed phrase `divided by`, especially for younger readers.

Chosen wording:
  Candidate A.

Why chosen:
  It makes the same-owner constraint structural rather than explanatory. The
  residual is only the familiar division operation; all physics content is
  carried by the two daughter headwords and their shared address.

Checks:
  - exactly two daughter headwords exposed: yes;
  - same material-object address explicit: yes;
  - no E7 chimney content repeated: yes;
  - no wall, force-composition, measurement, or trajectory-construction content
    imported: yes;
  - residual operation familiar and auditable: yes;
  - candidate agrees with the intended E9/E10 triplet symmetry: yes.

## Decisions made in this pass

1. E8 uses parameterised headword instances with the shared address `[A]`.
2. The final residual says `divided by` rather than using bare `/`.
3. Positivity is not restated in E8's entry string; it belongs to E10's
   inertial-mass corner.
4. Frame, time, provenance, and licence remain trace qualifications rather than
   extra headwords in the inward triplet string.
5. E8 calculates from two daughter values and may check against E7, but it does
   not read trajectories or construct future motion.
6. A zero net-force input yields zero acceleration without any free-particle or
   no-contributions inference.

## Questions and decisions still open

1. Does the engine/tokenizer preserve the base headword match when `[A]` is
   appended directly, or should address arguments be represented in a separate
   syntax while retaining the same human-facing entry?
2. Should frame and selected time/interval eventually appear as explicit
   arguments alongside `[A]`, or is trace-side qualification the correct level?
3. When all three triplet values are supplied, should E8 itself emit the
   consistency comparison, or should that be a general evaluator operation
   applied after any triplet corner resolves?
4. Should an expired mass binding be represented as `unlicensed input`,
   `undefined referent`, or a distinct certificate-expired halt in the eventual
   evaluator vocabulary?
5. Should dimensional checking (`N / kg -> m s^-2`) be an E8 residual effect,
   a general quantity-type operation, or both?
