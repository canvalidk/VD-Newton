# Entry Packet: E7 Inertial-Acceleration-Material-Object

Status: substantive packet draft, revised after the 2026-07-23 decision that
there is no separate point-particle inertial-acceleration headword.

## ENTRY PACKET

Entry id:
  [E7]

Headword:
  inertial-acceleration-material-object

Status:
  candidate

Role:
  chimney / peripheral November entry

Law/block:
  Newton II; first entry of the NML2.1 entry set

Source status:
  revised from D2[E20]. Governed by the NML2.1 managed-context snapshot at
  VD-docs commit `b23f5a215783aca8811598ceb5e783a7fdfd9726` and the local
  renumbering decision of 2026-07-23.

Source hierarchy:
  1. `07_design_2_1/notes/lesson_entry_notes/NML2_ENTRY_RENUMBERING_DECISION_2026-07-23.md`
     — current local steering decision.
  2. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md` — canonical NML2.1 content at
     the managed snapshot above.
  3. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md` — integrated lesson
     interpretation at the same snapshot.
  4. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and the entry-writing guides
     — active local structure and form.
  5. D2[E20] and the older NML1 E7/E8 notes — historical lineage only where
     consistent. Their separate point-particle inertial-acceleration proposal
     is superseded.

Old wording lineage:

```text
inertial-acceleration :=
The acceleration of a point-particle as measured in an inertial-frame.
```

Current steering formulation:

```text
generic point-particle motion quantity -> acceleration
material-object trajectory in an inertial-frame ->
    inertial-acceleration-material-object
Newton-II inward relation -> E8
```

Preserve:
  - inertial acceleration is read from a trajectory in an inertial frame;
  - the selected time remains explicit;
  - the entry is kinematic in operation even though its headword is restricted
    to the massive/material-object Newtonian domain;
  - E7 is outward-facing and contains no Newton-II equation;
  - zero is a valid inertial-acceleration value.

Change / reject:
  - Remove `inertial-acceleration_point-particle` as a separate headword.
  - Do not insert an intermediate binding between point-particle acceleration
    and material-object acceleration.
  - Do not use `massive-particle` as a second official target name.
  - Do not put net force, inertial mass, force composition, target construction,
    or full witness-sheet machinery in the entry string.
  - Do not infer that every generic point-particle acceleration is an
    inertial-acceleration-material-object.

Plain purpose:
  Give the Newton-II block its previously defined November word by naming the
  acceleration read at a selected time from a material object's trajectory in
  an inertial frame. Generic trajectory derivatives remain `acceleration`; the
  narrower headword already marks the material/massive domain.

Relationship to the packet set:
  - is redefined inwardly by E8;
  - supplies the acceleration headword used by E9 and E10;
  - contains no reference to the E9 or E10 winter headwords;
  - must remain meaningful without the E11 wall or deferred E12 wall.

Trace critical headword mentions:
  - material-object
  - trajectory
  - inertial-frame
  - acceleration

Forbidden headword mentions / hidden imports in the eventual entry wording:
  - point-particle — the extra domain split has been rejected for this
    headword.
  - inertial-acceleration_point-particle — superseded headword.
  - net-force-material-object — belongs to the triplet beginning at E8.
  - inertial-mass-material-object — belongs to the triplet beginning at E8.
  - interacting-forces-set / impressed-force — later force-sum machinery.
  - scale, weight, amount of matter — unlicensed mass identifications.

Question or trace moment this helps with:
  What acceleration is read at this time from this material object's trajectory
  in the selected inertial frame?

Witness kind:
  supplied material-object commitment with a trajectory; no full witness-sheet
  runtime required in Design 2.1.

Slots read:
  - material-object identity
  - trajectory associated with that material-object
  - selected inertial-frame
  - selected time
  - acceleration read from the trajectory at that time

Slots written / exposed:
  - inertial-acceleration-material-object
  - owner identity
  - frame and selected-time qualification
  - trajectory-read provenance

Boundary behavior:
  undefined referent:
    No material-object is identified.

  missing input:
    No trajectory, selected inertial-frame, selected time, or trajectory data
    adequate to read acceleration is available.

  contradiction:
    The proposed acceleration conflicts with the acceleration read from that
    material object's trajectory for the same frame and selected time.

  domain boundary:
    The demand concerns only a generic or massless point-particle rather than a
    material-object in the massive Newtonian domain.

  random/input boundary:
    A human/model must supply the material-object identification, trajectory
    association, or inertial-frame commitment when the problem does not.

IRIL - ideal residually imparted logic:

  Allowed:
    - Given an identified material-object with a trajectory in a selected
      inertial-frame, read the acceleration from that trajectory at the selected
      time.
    - Expose the resulting vector as
      `inertial-acceleration-material-object`, preserving owner, frame, time,
      and trajectory provenance.
    - Return the zero vector when the trajectory-read acceleration is zero.
    - Demand the earlier kinematic `acceleration` operation when the derivative
      has not already been supplied.

  Blocked:
    - Applying the E7 headword to a merely generic or massless point-particle.
    - Creating a second acceleration in addition to the trajectory derivative.
    - Reading acceleration from a trajectory belonging to another object.
    - Dropping or changing the selected frame or time.
    - Inferring net force, inertial mass, force contributions, or free-particle
      status.
    - Constructing or certifying the material-object at E7; NML2.1 begins with
      that target supplied.

  Trace consequence:
    - With compatible target, trajectory, frame, time, and derivative data,
      return the addressed inertial-acceleration vector.
    - If derivative data are missing, demand `acceleration` and its kinematic
      prerequisites.
    - If the material-object, trajectory, frame, or time is missing, suspend for
      the corresponding input rather than using Newton II to manufacture it.
    - If addresses or qualifications conflict, halt with a contradiction or
      mismatched-address signal.
    - If Newton-II calculation is demanded after E7 succeeds, route to E8.

IRIEs - ideal residually imparted effects:

  Reader/modeler behaviour to install:
    - Name the material object whose motion is being read.
    - Keep its trajectory distinct from the continuing object while preserving
      their association.
    - Check the inertial frame and selected time before reading acceleration.
    - Treat the trajectory derivative as the one acceleration later consumed by
      Newton II, not as a provisional value replaced by a second acceleration.
    - Retain owner, frame, time, and provenance beside the vector.

  Anti-habit / anti-misread:
    - Do not call every point-particle acceleration an inertial acceleration.
    - Do not begin with `F = ma` when the current job is to read motion.
    - Do not borrow another object's trajectory or acceleration.
    - Do not treat a change of entry definition at E8 as a change of physical
      quantity.
    - Do not infer free-particle status from zero acceleration.
    - Do not silently treat ordinary object recognition as the later NML2.2
      target-construction proof.

Suggested wording:

  A:

  ```text
  For a material-object with a trajectory described in an inertial-frame, the
  acceleration read from that trajectory at a selected time.
  ```

  B:

  ```text
  For a material-object in an inertial-frame, the acceleration read at a
  selected time from that material-object's trajectory.
  ```

  C:

  ```text
  The acceleration of a material-object read at a selected time from its
  trajectory in an inertial-frame.
  ```

Draft entry:

```text
inertial-acceleration-material-object :=

For a material-object with a trajectory described in an inertial-frame,
the acceleration read from that trajectory at a selected time.
```

## DEEP AUDIT ADD-ON

Role test:
  E7 is outward-facing. It connects the November word to already available
  material-object, trajectory, inertial-frame, acceleration, and time handles.
  It contains neither winter headword and does not state Newton II.

Necessary/sufficient/asymmetric relations:
  - Material-object identity, a trajectory, an inertial-frame commitment, and a
    selected time are necessary for the ordinary E7 readout.
  - A generic acceleration value alone is not sufficient; its material-object,
    frame, time, and trajectory address must match.
  - In the supplied-target regime of NML2.1, compatible target, trajectory,
    frame, time, and acceleration data are sufficient for E7.
  - E7 does not prove or originate inertial mass. The material-object domain is
    part of the headword's applicability, while the mass relation and outward
    mass account belong later.
  - E7 returning zero is not sufficient to infer free-particle status or the
    absence of force contributions.

Quantifier or modality:
  for; with; described in; selected.

Suspends for human/model input?
  yes; when material-object identity, trajectory association, frame status, or
  selected time is not supplied.

Boundary trigger:
  - no material-object;
  - no trajectory for that material-object;
  - no inertial-frame commitment;
  - no selected time or adequate derivative data;
  - cross-object, cross-frame, or cross-time mismatch;
  - request to infer Newton-II daughters from E7.

Boundary output:
  - demand the missing material-object/modelling commitment;
  - demand the trajectory, frame, time, or kinematic acceleration operation;
  - return a mismatched-address contradiction when qualifications conflict;
  - route Newton-II relation demands to E8;
  - route target/address-construction demands to NML2.2.

Residual provenance ledger:

| Phrase | Backing |
|---|---|
| `For a` | Grammar-level domain restriction; forces identification of the entity to which the definition applies. |
| `material-object` | Official NML2.1 target name and auditable scoped headword. |
| `with a trajectory` | Direct headword edge plus ordinary possession/association grammar used throughout the NML2.1 content specification. |
| `described in an inertial-frame` | Direct frame headword and established scientific modelling idiom. |
| `acceleration read from that trajectory` | Direct kinematic headword plus the NML1/NML2 lesson-installed motion-reading handle. |
| `at a selected time` | Existing kinematic entry pattern; forces the time argument rather than a free-floating value. |

Alternative wording assessment:
  - A makes every required prior headword visible and matches the current active
    draft.
  - B places the frame before the trajectory and makes ownership explicit, but
    the nested possessive is slightly heavier.
  - C is shortest, but its residual may encourage readers to treat acceleration
    as an innate object property rather than a frame-qualified trajectory
    derivative.

Chosen wording:
  Candidate A.

Why chosen:
  It is the shortest candidate that keeps material-object, trajectory,
  inertial-frame, acceleration, and selected time explicit. Its residual
  operation is familiar and narrow: locate the correct trajectory and read its
  derivative at the selected time.

Checks:
  - required trace-critical headwords present: yes;
  - rejected point-particle inertial-acceleration headword absent: yes;
  - Newton-II daughter headwords absent: yes;
  - outward peripheral role preserved: yes;
  - residual phrases have named provenance: yes;
  - wording matches the active draft entry: yes.

## Decisions made in this revision

1. There is no `inertial-acceleration_point-particle` entry.
2. Generic point-particle motion continues to use the kinematic `acceleration`
   entry.
3. E7 and E8 are the only two definitions of
   `inertial-acceleration-material-object`.
4. E7 reads directly from the material object's trajectory; no intermediate
   alias/binding entry exists.
5. The material/massive domain is carried by the official headword and supplied
   target commitment, not by mentioning inertial mass inside the E7 string.
6. E7 remains equation-free and outward-facing.

## Questions and decisions still open

1. Should the eventual formal object machinery make `material-object`
   sufficient to guarantee a positive inertial-mass referent, or should that
   implication remain a trace-side domain commitment until NML2.2/E12 is
   written?
2. Should E7 remain strictly instantaneous (`at a selected time`), or should a
   separate construct later represent a time-indexed acceleration history over
   an interval?
3. Does `with a trajectory` provide a sufficiently auditable association in
   Design 2.1, or will the later object model need an explicit trajectory slot
   or relation entry?
4. The old NML1 documents placed a generic point-particle E7 at the end of that
   lesson. With that entry removed, should NML1 end at E6 and leave the revised
   E7 wholly to NML2.1, or preview only the generic kinematic `acceleration`
   handle? This is a curriculum-placement cleanup, not an entry-definition
   blocker.
