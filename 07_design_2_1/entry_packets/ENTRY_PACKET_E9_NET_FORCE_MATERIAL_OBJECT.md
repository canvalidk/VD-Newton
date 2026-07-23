# Entry Packet: E9 Net-Force-Material-Object

Status: structural fields fixed; residual logic and entry wording not yet drafted.

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
  1. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md`.
  2. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md`.
  3. E8 and E10 structural packets as the other triplet corners.
  4. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and the six-entry guide.
  5. D2[E22] and older local NML2 notes, only where consistent.

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
  - interacting-forces-set / attached-force / force-sum — later block.
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
  pending the sequential drafting pass.

IRIEs - ideal residually imparted effects:
  pending the sequential drafting pass.

Suggested wording:
  pending.

Draft entry:
  pending.
