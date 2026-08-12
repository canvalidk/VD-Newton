# Entry Packet: E11 Net-Force-Material-Object

Status: substantive packet draft; structural fields, residual design, and a
candidate entry are present, with open decisions recorded below.

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
  1. `07_design_2_1/notes/lesson_entry_notes/NML2_ENTRY_RENUMBERING_DECISION_2026-07-23.md`.
  2. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md` — canonical thin net-force wall.
  3. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md` — integrated lesson use.
  4. `Newton/nml/nml2/NML2_note_net_force_wall_withheld.md` — parent working
     note, read through the canonical NML2.1 sources.
  5. E9 packet — inward triplet definition to complement, not
     repeat.
  6. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` and entry-writing guides.

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
  - interacting-forces-set / impressed-force / force-sum as completed machinery.
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

  Allowed:
    - On a demand to land `net-force-material-object`, require one identified
      material object, one selected inertial frame, and one selected time or
      interval.
    - Accept one force-dimension vector either as an explicit modelling input or
      as the licensed result of E9, and preserve its provenance.
    - Bind that vector to the identified material object and its frame/time
      qualifications as one net-force value measured in newtons.
    - Accept the zero vector as a valid net-force value.
    - When a supplied value and an E9-inferred value are both available under
      the same qualifications, compare them as a Newton-II consistency check.
    - Preserve an unresolved-production marker when a valid value has landed but
      its physical force contributions have not yet been produced.

  Blocked:
    - Landing a value without an identified material-object owner.
    - Combining a value, owner, frame, and time/interval from incompatible
      contexts.
    - Accepting a scalar, a bare magnitude, or a directionless verbal answer in
      place of the required vector.
    - Treating one push, pull, impressed force, or newton-meter reading as the net
      force without a licensed account connecting it to the single vector.
    - Generating the vector by silently inventing, accumulating, or closing an
      interacting-forces set.
    - Inferring free-particle status, zero velocity, or absence of force
      contributions from a zero net-force vector.
    - Treating the wall as the causal assertion that force causes acceleration.
    - Dropping whether the value was supplied, E9-inferred, or later produced.

  Trace consequence:
    - With a qualified supplied vector, land it as
      `net-force-material-object` and mark the provenance `supplied`.
    - With a licensed E9 result, land that result and mark the provenance
      `Newton-II-inferred`.
    - With both values, return the common value when they agree and a Newton-II
      consistency contradiction when they disagree under the same
      qualifications.
    - With no value, demand the E9 daughters or an explicit supplied input; a
      cycle with no independent values terminates as insufficient information.
    - With a zero vector, retain the value and qualifications without routing to
      Newton I or inferring that no contributions exist.
    - When the user or trace asks which physical contributions produce the
      vector, halt at the later force-sum block rather than manufacturing an
      answer inside E11.

IRIEs - ideal residually imparted effects:

  Reader/modeler behaviour to install:
    - Look for one vector belonging to one material object, not an unaddressed
      force number.
    - Keep the selected inertial frame and time or interval attached to the
      vector.
    - Recognize newtons as the unit and preserve vector direction as part of the
      value.
    - Record how the value entered the trace: supplied, Newton-II-inferred, or
      later force-sum-produced.
    - Use E11 as a landing and recognition site; use E9 when the value must be
      inferred from mass and acceleration.
    - Treat a request for physical force contributions as an explicit downstream
      dependency rather than filling the gap with textbook habit.

  Anti-habit / anti-misread:
    - Do not read net force as merely the largest or most salient force.
    - Do not identify it automatically with a newton-meter reading.
    - Do not replace the vector with its magnitude.
    - Do not combine values belonging to different objects, frames, or times.
    - Do not define it here as "all the forces added together."
    - Do not read zero net force as proof of a free particle, zero velocity, or
      no force contributions.

Suggested wording:

  A, thin outward wall:

  ```text
  net-force-material-object :=

  For a material-object at a selected time or interval in an inertial-frame,
  the single vector assigned to that material-object for the Newton II relation,
  measured in newtons.
  ```

  B, explicit address variable:

  ```text
  net-force-material-object[A] :=

  the single vector assigned to material object A at a selected time or interval
  in an inertial-frame for the Newton II relation, measured in newtons.
  ```

  C, provenance-explicit wall:

  ```text
  net-force-material-object :=

  For a material-object at a selected time or interval in an inertial-frame,
  the single vector, measured in newtons, supplied or inferred for use in the
  Newton II relation.
  ```

Draft entry:

```text
net-force-material-object :=

For a material-object at a selected time or interval in an inertial-frame,
the single vector assigned to that material-object for the Newton II relation,
measured in newtons.
```

## DEEP AUDIT ADD-ON

Role test:
  E11 is outward-facing. It gives the E9 headword a recognizable, typed landing
  site and explicitly addresses the value to a material object. It neither
  repeats the inward Newton-II formula nor defines the later mechanism by which
  physical force contributions produce the value.

Necessary/sufficient/asymmetric relations:
  - An identified material object, a compatible frame/time qualification, and
    one force-dimension vector with licensed provenance are jointly sufficient
    to land an E11 value.
  - A vector without an owner is insufficient; an owner without a vector is
    insufficient.
  - A magnitude and unit without direction are insufficient for a nonzero
    net-force vector.
  - An E9 result is sufficient as one permitted value source, but E11 does not
    require that every value be inferred by E9.
  - A supplied vector is sufficient to land a modelling input, but supply alone
    does not explain its physical production.
  - A single interaction or instrument reading is not sufficient to identify
    net force without a licensed bridge to the whole addressed value.
  - The zero vector is sufficient as a value. It is not sufficient for
    free-particle status, zero velocity, or the conclusion that no force
    contributions exist.
  - Agreement between supplied and E9-inferred values is sufficient for local
    Newton-II consistency under matching qualifications, not for validating a
    later force-contribution account.

Quantifier or modality:
  `For a material-object` opens an arbitrary addressed instance; `the single`
  commits the trace to one resultant vector for that owner and qualification.

Suspends for human/model input?
  yes; when the material object, vector value, frame, selected time/interval, or
  provenance is missing, and whenever physical production is demanded before
  the later force-sum machinery is available.

Boundary trigger:
  - missing or ambiguous material-object owner;
  - no supplied vector and no eligible E9 inference;
  - scalar/vector or dimensional mismatch;
  - incompatible owner, frame, or time/interval qualifications;
  - disagreement between supplied and E9-inferred values;
  - a demand for the impressed forces or their closure;
  - an unsupported claim that one interaction or reading is the net force.

Boundary output:
  - demand a material-object address and full vector qualification;
  - demand an explicit input or route to E9 and its two daughter values;
  - return a contradiction for type, dimension, address, qualification, or
    E9/E11 consistency failure;
  - retain a zero vector without free-particle or no-contributions inference;
  - preserve `unresolved-production` when the value is usable but its physical
    production has not been established;
  - route physical contribution, completeness, or vector-sum demands to the
    later force-sum entries.

Residual provenance ledger:

| Phrase or symbol | Backing |
|---|---|
| `For a material-object` | The revised NML2.1 domain and official addressed headword; binds one owner without performing target construction. |
| `at a selected time or interval` | Canonical thin-wall qualification; prevents borrowing a force value across temporal contexts. |
| `in an inertial-frame` | Newton-II frame qualification inherited from the NML2.1 lesson context. |
| `the single vector` | Canonical wall commitment to one addressed net result while withholding its later force-list production. |
| `assigned to that material-object` | Provenance-neutral modelling language that lands a value without asserting how it was measured or produced. |
| `for the Newton II relation` | Connects the outward wall to E8-E10 without repeating the E9 formula or asserting a causal slogan. |
| `measured in newtons` | Canonical force-dimension recognition handle; does not identify an instrument or measurement procedure. |

Alternative wording assessment:
  - A makes owner, time/interval, frame, vector type, law role, and unit visible
    while leaving production open.
  - B makes the triplet-style address token explicit, but `material object A`
    introduces a second address notation whose parsing and relation to the
    official headword are not yet settled.
  - C usefully names the two NML2.1 provenance routes, but risks making those
    routes exhaustive and thereby excluding later force-sum-produced values.

Chosen wording:
  Candidate A.

Why chosen:
  It is a thin, source-neutral wall. It supplies enough outward meaning to land
  and recognize a net-force vector while preserving E9's inward role and the
  later force-sum block's production work.

Checks:
  - one material-object owner explicit: yes;
  - vector character and newton unit explicit: yes;
  - frame and time/interval qualifications explicit: yes;
  - no E9 formula repeated: yes;
  - no force list generated or closed: yes;
  - no newton-meter or single-interaction identity imported: yes;
  - zero case protected in the residual logic: yes.

## Decisions made in this pass

1. E11 uses the plain headword on the left and binds the material-object owner
   in prose, matching the outward E7 style rather than the inward triplet syntax.
2. The wall says `single vector`, not `vector sum`, so later force-composition
   machinery remains withheld.
3. The entry retains selected time/interval, inertial-frame, and newton-unit
   qualifications as part of the outward recognition handle.
4. `assigned` is provenance-neutral: supplied, E9-inferred, and later-produced
   values may all land here.
5. The entry mentions the Newton II relation but does not repeat E9's formula or
   make a causal claim.
6. The zero-vector protections and later force-sum routing remain residual
   effects rather than lengthening the entry string.

## Questions and decisions still open

1. Should the outward wall eventually use `net-force-material-object[A]` on the
   left, or is the prose owner binder preferable for consistency with E7?
2. Is `assigned to` the best provenance-neutral verb, or would `associated
   with` or `attributed to` install a better modelling habit?
3. Should the wall say only `at a selected time`, as in the earliest lesson
   note, or retain `time or interval` for supplied or averaged problem data?
4. Does `measured in newtons` belong in the compact entry wording, or should the
   unit live entirely in quantity-type and evaluator machinery?
5. What exact provenance vocabulary should distinguish `supplied`,
   `Newton-II-inferred`, and later `force-sum-produced` values?
6. Should E11 perform the E9 consistency comparison, or should that be a
   general evaluator operation shared by all inward/outward entry pairs?
7. Should the entry itself carry a short pointer to the later force-sum block,
   or is trace-side routing enough?
