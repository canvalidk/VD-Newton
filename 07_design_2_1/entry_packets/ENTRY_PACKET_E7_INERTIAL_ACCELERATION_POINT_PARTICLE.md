# Entry Packet: E7 Inertial-Acceleration Point-Particle

Status: draft packet, written for Design 2.1 / Design 3 reconciliation.

This packet uses the newer NML1 E7/E8 decision as the steering source. It
therefore revises the older first-pass picture in which E7 was a generic
Newton II chimney for `inertial-acceleration` with a material-object witness
domain.
The current packet treats E7 as the point-particle motion-sheet getter; E8 is
the later material-object force-accounting link.

## ENTRY PACKET

Entry id:
  [E7]

Headword:
  inertial-acceleration_point-particle

Status:
  candidate

Role:
  kinematic chimney / bridge / motion-sheet getter

Law/block:
  Bridge from Newton I / motion reading into Newton II. E7 is not the Newton II
  triplet. E8 begins the material-object force-accounting branch.

Source status:
  revised from D2[E20]; supersedes the first-pass D2.1 E7 wording where it
  treats E7 as a generic `inertial-acceleration` chimney for a
  material-object witness. Current steering source is the NML1 E7/E8 decision
  note.

Source audit:
  - `08_nm_lesson_drafts/nml1/NM_L1_E7_E8_decision_note.md` supplies the
    current decision: E7 is a trajectory-read motion quantity; E8 links that
    same quantity into the material-object force-accounting sheet; E9 is the
    Newton II law relation.
  - `08_nm_lesson_drafts/nml1/NM_L1_E7_integrated_complete_draft.md` supplies
    the lesson-facing purpose: after Newton I, if motion is not uniform, read
    how the motion changes before explaining it by force.
  - `08_nm_lesson_drafts/nml1/E7_INERTIAL_ACCELERATION_PLACEMENT_NOTE.md`
    supplies the older placement caution: E7 can be a light NML1 bridge only
    if it does not open `net-force`, `inertial-mass`, `F = ma`, or force
    diagrams.
  - `07_design_2_1/notes/lesson_entry_notes/NEWTON_L2_ENTRY_NOTES_FIRST_PASS.md`
    supplies the old first-pass E7 picture and old D2 wording. Its
    material-object wording is now treated as superseded for E7 and moved to
    the E8/E9 side of the boundary.
  - `DESIGN_3_ENTRY_STRUCTURE.md` supplies the old ledger row:
    `[E7] Newton II chimney; inertial-acceleration; captures D2[E20]`. This
    row should be updated if the current E7/E8 decision is accepted.
  - `04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md`,
    `04_entry_design_guides/vd_entry_writing_best_practices_handle_residual.md`,
    and `04_entry_design_guides/entry_writing_guide_auditable_compositions.md`
    supply the packet structure and residual discipline.

Old wording:

```text
inertial-acceleration :=
The acceleration of a point-particle as measured in an inertial-frame.
```

New steering formulation:

```text
E7 = motion-sheet getter
E8 = force-accounting sheet link
E9 = Newton II law relation
```

Preserve:
  - E7 is frame-qualified acceleration.
  - E7 reads from a point-particle trajectory in an inertial-frame.
  - E7 is kinematic: it reads motion before force-accounting explains motion.
  - E7 is the immediate bridge after Newton I: when `uniform-motion` fails,
    identify the motion-change.
  - The acceleration read by E7 is the same acceleration that E8 later binds
    into the material-object force-accounting sheet.
  - E7 does not require `inertial-mass`.
  - E7 can be lesson-installed through path / trajectory / turning-arrow
    practice without forcing Newton II calculation.

Change / reject:
  - Reject generic `inertial-acceleration` if it hides the object-sheet
    distinction between point-particle motion reading and material-object
    force accounting.
  - Reject putting `material-object` into the E7 draft wording. That belongs
    to E8.
  - Reject treating E8 as a second independent acceleration.
  - Reject any wording where a material-object witness physically contains a
    point-particle witness. The model is one target, multiple witness sheets.
  - Reject force explanation in E7: no `net-force`, `inertial-mass`,
    `interacting-forces-set`, `acting-object`, `F = ma`, or force diagrams.
  - Reject "centripetal force" and other force names in E7-facing pedagogy.
  - Reject path-only overreach: a timeless path shape alone does not determine
    full acceleration unless speed/time information is supplied or implicitly
    fixed.

Plain purpose:

  Give the trace a controlled way to name and return the acceleration read from
  a point-particle's trajectory in an inertial-frame. E7 answers the
  motion-reading question:

  ```text
  Given the trajectory in the chosen inertial-frame, how is the motion
  changing?
  ```

  This lets NM L1 proceed from Newton I to a first acceleration handle without
  opening force accounting. The later E8 entry can then say: if this same
  target also carries a material-object witness, bind the E7 readout into the
  material-object force-accounting sheet.

IRIL - ideal residually imparted logic:

  Allowed:
    - Given a point-particle, its trajectory, and an inertial-frame
      commitment, read acceleration from the trajectory.
    - If the trajectory is uniform-motion in the inertial-frame, return zero
      motion-change / zero acceleration for this motion sheet.
    - If speed changes, direction changes, or both, return nonzero
      trajectory-read acceleration.
    - For a young-learner route, allow "draw how the motion is changing" as
      the installed residual handle, especially for turning paths.
    - Preserve that E8 may later reuse this same acceleration as the
      Newton-II-facing acceleration for a material-object.

  Blocked:
    - Inferring `net-force` from E7 alone.
    - Demanding `inertial-mass` at E7.
    - Treating E7 as Newton II.
    - Treating E7 as a force explanation rather than a motion readout.
    - Treating a point-particle motion sheet and a material-object
      force-accounting sheet as two physical objects.
    - Assuming a path curve alone gives full acceleration without either
      steady-speed context, equal-time markers, velocity data, or another time
      parametrisation.
    - Feeding a non-inertial-frame acceleration directly into ordinary
      Newtonian force accounting.

  Trace consequence:
    - If point-particle, trajectory, and inertial-frame are supplied, E7
      returns an acceleration readout with motion-sheet provenance.
    - If the frame is missing, demand the selected frame / inertial-frame
      commitment.
    - If the trajectory or time information is missing, demand the trajectory
      or the data needed to read velocity-change.
    - If a force-accounting explanation is requested, route onward to E8/E9,
      not through E7 alone.
    - If the target has no material-object / inertial-mass referent, E7 can
      still supply motion-reading where the point-particle trajectory exists,
      but E8/E9 must halt at the material-object boundary.

IRIEs - ideal residually imparted effects:

  Reader/modeler behaviour to install:
    - After Newton I, first ask whether the observed motion is uniform.
    - If not uniform, read how the motion changes before naming a cause.
    - Read acceleration from trajectory / velocity-change in the selected
      inertial-frame.
    - For curved steady-speed paths, mark direction-change toward the inside of
      the turn.
    - For straight speeding-up or slowing-down paths, mark acceleration along
      or opposite the direction of motion.
    - Keep the E7 arrow / readout distinct from a force arrow.
    - Ask "what might account for this acceleration?" only after the E7 readout
      exists.
    - Preserve one target with multiple witness sheets: motion sheet first,
      force-accounting sheet later if the target carries a material-object
      witness.

  Anti-habit / anti-misread:
    - Do not jump from "curved path" to "there is a force" in NM L1.
    - Do not say "centripetal force" when the current job is only inward
      motion-change.
    - Do not treat `F = ma` as the source of acceleration.
    - Do not collapse E7 and E8 into one generic acceleration entry.
    - Do not read `uniform-motion -> free-body`.
    - Do not forget that frame choice is part of the readout.
    - Do not turn the worksheet into an acceleration quiz; it is handle
      installation.

Trace critical headword mentions:
  Earlier-entry headwords that must appear in the final entry wording:
  - point-particle
  - acceleration
  - trajectory
  - inertial-frame

Other headword mentions:
  Earlier-entry headwords mentioned incidentally or in notes:
  - uniform-motion
  - velocity
  - speed
  - free-body / free-particle
  - reference-frame

Forbidden headword mentions / hidden imports:
  - material-object:
    why forbidden or risky: E7 is the point-particle motion-sheet getter. The
    material-object witness binding belongs to E8.
  - inertial-mass:
    why forbidden or risky: opens the Newton II domain boundary too early.
  - net-force:
    why forbidden or risky: force-accounting belongs downstream.
  - F = ma:
    why forbidden or risky: collapses E7 into the Newton II law relation.
  - interacting-forces-set:
    why forbidden or risky: force-sum machinery belongs after Newton II.
  - attached-force / acting-object:
    why forbidden or risky: opens the object/force-contribution machinery
    before the acceleration readout exists.
  - force / centripetal force:
    why forbidden or risky: encourages explanation before motion-reading.
  - "contains a point-particle":
    why forbidden or risky: makes witness-sheet composition sound like physical
    containment or naive inheritance.

Question or trace moment this helps with:

  "A car, leaf, moon, or planet follows a curved path. What is the first thing
  to do before force-talk?"

  "Given this point-particle trajectory in an inertial-frame, how is the
  motion changing?"

  "A puck is not in uniform-motion in the selected frame. Before asking for
  forces, what acceleration does the motion sheet return?"

  "When NM L2 begins, what acceleration is Newton II going to account for?"

Witness kind:
  point-particle; inertial-frame; object witness / motion sheet

Slots read:
  - target identity
  - point-particle status
  - selected frame identity
  - inertial-frame commitment for the selected frame
  - trajectory in that frame
  - position as a time-indexed quantity, if needed
  - velocity or velocity-change, if already supplied
  - time parametrisation / equal-time markers / steady-speed assumption, if the
    path drawing alone is insufficient

Slots written / exposed:
  - inertial-acceleration_point-particle
  - trajectory-read acceleration
  - zero / nonzero motion-change status
  - direction of motion-change, where visible
  - motion-sheet provenance for the acceleration readout
  - eligibility for E8 to bind the same acceleration into a material-object
    force-accounting sheet, if the target carries a material-object witness

Boundary behavior:
  undefined referent:
    The named target does not resolve to a point-particle / trajectory-bearing
    target.

  missing input:
    No selected frame, no inertial-frame commitment, no trajectory, or no
    time/velocity information adequate to read acceleration.

  contradiction:
    The same motion sheet asserts both uniform-motion and a nonzero
    trajectory-read acceleration over the same interval in the same frame.

  domain boundary:
    The selected frame is non-inertial and no frame-bridge or non-inertial
    machinery has been supplied; or a force-accounting answer is demanded from
    E7 instead of E8/E9.

  random/input boundary:
    None expected, except where a human/model must supply the modelling choice
    that a drawn path is being treated as steady-speed or equal-time sampled.

Suggested wording:

  A:

  ```text
  For a point-particle with a trajectory described in an inertial-frame,
  inertial-acceleration_point-particle is the acceleration read from that
  trajectory at a selected time.
  ```

  B:

  ```text
  For a point-particle, inertial-acceleration_point-particle is the
  acceleration read from its trajectory in an inertial-frame.
  ```

  C, lesson-facing:

  ```text
  E7 acceleration is how a point-particle's motion changes when we read its
  trajectory from an inertial-frame.
  ```

Draft entry:

  ```text
  inertial-acceleration_point-particle :=

  For a point-particle with a trajectory described in an inertial-frame,
  the acceleration read from that trajectory at a selected time.
  ```

Open questions:
  - Should `DESIGN_3_ENTRY_STRUCTURE.md` and
    `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` be updated so E7's headword
    is `inertial-acceleration_point-particle` rather than generic
    `inertial-acceleration`?
  - Is `acceleration` already installed strongly enough as an earlier raw
    kinematic entry, or does E7 need an adjacent packet for the raw
    `acceleration` getter?
  - Should E7 be formally part of NML1, or should NML1 install the behaviour
    while NML2 installs the entry?
  - For massless path cases such as photons, should E7 be available as a
    point-particle trajectory readout, or should those questions route only
    through `path` / `uniform-motion` unless explicitly asking for E7?
  - How should the evaluator represent the motion sheet and its provenance:
    as witness slots, trace notes, or future typed human-input records?
  - resolved 2026-06-19: final draft uses "read from trajectory" language.

## DEEP AUDIT ADD-ON

Role test:
  If chimney/wall: can it be read outwardly as a normal definition?

  Mostly yes. It reads as a normal motion-readout definition, but its headword
  is intentionally scoped to the point-particle witness sheet so that the
  later material-object force-accounting role does not hide inside it.

Necessary/sufficient/asymmetric relations:
  - Point-particle status, a trajectory, and an inertial-frame commitment are
    necessary for E7's ordinary readout.
  - A material-object witness is not necessary for E7.
  - The material-object witness becomes relevant only at E8, where the same E7
    readout is bound into force accounting.
  - E7 returning zero acceleration is not sufficient to infer free-body status.
  - E7 returning nonzero acceleration is not sufficient to infer any particular
    force.
  - A curved path is not sufficient for a full acceleration vector unless the
    time/velocity information needed to read velocity-change is also supplied.
  - The inertial-frame condition is asymmetric: it licenses the Newtonian
    readout; the acceleration readout does not by itself prove the frame is
    inertial.

Quantifier or modality:
  given; when; if; read; returned; later

Suspends for human/model input?
  yes; when the trajectory, frame, time parametrisation, steady-speed
  assumption, or inertial-frame commitment is not explicit.

Boundary trigger:
  - no point-particle target
  - no trajectory
  - no selected frame
  - no inertial-frame commitment
  - path-only drawing with no time/velocity information where speed-change
    matters
  - request for force cause instead of motion readout
  - request to bind into Newton II without material-object / inertial-mass
    referent

Boundary output:
  - demand target point-particle / trajectory
  - demand selected frame / inertial-frame commitment
  - demand time/velocity data or mark steady-speed modelling assumption
  - route force-accounting question to E8/E9
  - halt at material-object boundary when Newton II is requested for a target
    without inertial-mass referent

Residual provenance ledger:

| Phrase | Backing |
|---|---|
| "returned by" | Getter / witness-sheet reaction from the E7/E8 decision note; acceptable in packet and draft if the reader has the lesson/entry context. |
| "read in an inertial-frame" | Lesson-installed E7 handle plus standard mechanics culture; routes to frame-conditioned motion reading. |
| "motion changes" | NML1 lesson-installed handle; safe for lesson-facing notes, too informal for the final formal entry unless paired with acceleration / trajectory. |
| "motion sheet" | Witness-sheet model from the E7/E8 decision note; use in packet notes, not necessarily final entry string. |
| "force-accounting sheet" | Witness-sheet model from the E7/E8 decision note; useful in notes to block E8 collapse, but forbidden in E7 final wording. |

Alternative wordings:

  A:

  ```text
  For a point-particle with a trajectory described in an inertial-frame,
  inertial-acceleration_point-particle is the acceleration read from that
  trajectory at a selected time.
  ```

  B:

  ```text
  For a point-particle in an inertial-frame, inertial-acceleration_point-particle
  is the acceleration read from its trajectory.
  ```

  C:

  ```text
  The inertial-acceleration_point-particle of a point-particle is the
  trajectory-read acceleration of that point-particle in an inertial-frame.
  ```

Chosen wording:

  ```text
  For a point-particle with a trajectory described in an inertial-frame,
  the acceleration read from that trajectory at a selected time.
  ```

Why chosen:

  The chosen wording keeps all trace-critical headwords visible:
  `point-particle`, `acceleration`, `trajectory`, and `inertial-frame`. It
  makes E7 a motion-sheet readout, adds the selected-time slot needed by the
  derivative wording, and avoids importing `material-object`, `inertial-mass`,
  `net-force`, or force-accounting.

Checks:
  - Required trace critical headwords present: yes.
  - Forbidden headwords avoided in draft entry: yes.
  - Intended question supported: yes, "what acceleration is read from this
    trajectory in this inertial-frame?"
  - Anti-misread blocked: mostly. Notes explicitly block force-accounting,
    second-acceleration, material-object/point-particle containment, and
    path-only overreach.
  - Simple enough for intended interpreter: yes for the formal entry; lesson
    wording remains available for young learners.
