# Entry Packet: E8 Inertial-Acceleration-Material-Object

Status: structural fields fixed; residual logic and entry wording not yet drafted.

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
  1. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md`.
  2. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md`.
  3. E7, E9, and E10 structural packets as the other parts of this house.
  4. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and the six-entry guide.
  5. D2[E21] and the older NML2 first-pass note, only where consistent.

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
  pending the sequential drafting pass.

IRIEs - ideal residually imparted effects:
  pending the sequential drafting pass.

Suggested wording:
  pending.

Draft entry:
  pending.
