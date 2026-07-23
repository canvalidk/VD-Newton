# Entry Packet: E10 Inertial-Mass-Material-Object

Status: structural fields fixed; residual logic and entry wording not yet drafted.

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
  1. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md`.
  2. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md`.
  3. E8 and E9 structural packets as the other triplet corners.
  4. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and the six-entry guide.
  5. D2[E23] and older local NML2 notes, only where consistent.

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
  - interacting-forces-set / attached-force — later force-sum machinery.

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
  pending the sequential drafting pass.

IRIEs - ideal residually imparted effects:
  pending the sequential drafting pass.

Suggested wording:
  pending.

Draft entry:
  pending.
