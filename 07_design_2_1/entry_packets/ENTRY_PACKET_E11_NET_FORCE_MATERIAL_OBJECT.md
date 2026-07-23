# Entry Packet: E11 Net-Force-Material-Object

Status: structural fields fixed; residual logic and entry wording not yet drafted.

## ENTRY PACKET

Entry id:
  [E11]

Headword:
  net-force-material-object

Status:
  candidate

Role:
  wall / peripheral winter entry

Law/block:
  Newton II; outward net-force wall for NML2.1

Source status:
  new standalone wall relative to the D2 operational entries. Governed by the
  NML2.1 managed-context snapshot at VD-docs commit
  `b23f5a215783aca8811598ceb5e783a7fdfd9726`.

Source hierarchy:
  1. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md` — canonical thin net-force wall.
  2. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md` — integrated lesson use.
  3. `Newton/nml/nml2/NML2_note_net_force_wall_withheld.md` — parent working
     note, read through the canonical NML2.1 sources.
  4. E9 structural packet — inward triplet definition to complement, not
     repeat.
  5. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and entry-writing guides.

Old wording lineage:
  No D2 standalone Newton-II wall. The later force-sum definition is not to be
  copied into E11.

Preserve:
  - net-force-material-object is one vector addressed to one material object;
  - it is qualified by the relevant time or interval and inertial frame;
  - it is measured in newtons;
  - NML2.1 may receive it as a supplied value or infer it through Newton II;
  - zero net force remains distinct from no force contributions and from
    free-particle status.

Change / reject:
  - Do not define net force as "all the forces added together" here.
  - Do not equate it with a newton-meter reading or one salient interaction.
  - Do not make the wall generate, accumulate, or close a force list.
  - Do not repeat the full E9 triplet formula as the wall's ordinary meaning.

Plain purpose:
  Give the winter headword an outward, usable recognition handle while keeping
  its physical production explicitly open for the later force-sum entries.

Relationship to the packet set:
  - provides the outward companion to E9;
  - may supply a value later consumed by E8;
  - must not take over E9's inward relation;
  - marks, but does not solve, the handoff to the force-sum block.

Trace critical headword mentions:
  - material-object
  - vector

Other headword mentions permitted if needed:
  - inertial-frame
  - time / time-interval
  - newton

Forbidden headword mentions / hidden imports in the eventual entry wording:
  - interacting-forces-set / attached-force / force-sum as completed machinery.
  - newton meter as a net-force instrument.
  - push or pull as an identity claim.
  - free-particle as a consequence of the zero vector.
  - causes acceleration as the wall's definition.

Question or trace moment this helps with:
  What single addressed vector is the problem supplying or Newton II inferring
  for this material object before force composition has been taught?

Witness kind:
  addressed material-object force-accounting commitment; lightweight slot or
  explicit input, not a completed force-list witness.

Slots read:
  - material-object identity
  - selected inertial-frame
  - selected time or interval
  - supplied net-force vector or E9 inference result
  - value provenance

Slots written / exposed:
  - net-force-material-object
  - vector value and unit
  - owner/frame/time qualification
  - supplied or Newton-II-inferred provenance
  - unresolved-production marker when physical contributions are demanded

Boundary behavior:
  - undefined referent: no material object is identified;
  - missing input: neither a supplied value nor an eligible E9 inference is
    available;
  - contradiction: owner, frame, interval, units, or direction conflict;
  - downstream boundary: a demand for physical force contributions routes to
    the later force-sum block rather than being answered here.

IRIL - ideal residually imparted logic:
  pending the sequential drafting pass.

IRIEs - ideal residually imparted effects:
  pending the sequential drafting pass.

Suggested wording:
  pending.

Draft entry:
  pending.
