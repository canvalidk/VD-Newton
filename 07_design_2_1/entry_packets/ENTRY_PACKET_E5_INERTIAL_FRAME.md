# Entry Packet: E5 Inertial-Frame

Status: draft packet, written for Design 2.1.

## ENTRY PACKET

Entry id:
  [E5]

Headword:
  inertial-frame

Status:
  candidate

Role:
  wall

Law/block:
  Newton I

Source status:
  captures D2[E18]; revised for Design 2.1 from the old Newton I wall wording
  and the Design 3 inertial-frame correction notes.

Source audit:
  - `07_design_2_1/notes/lesson_entry_notes/NEWTON_L1_ENTRY_NOTES_FIRST_PASS.md`
    supplies the direct E5 Design 2.1 note: the wall carries the frame
    modelling commitment, the fictitious-force warning, and the classroom
    lab/Earth-frame convention.
  - [VD-docs: Newton-analysis/vd_design_3_newton_i_correction.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/vd_design_3_newton_i_correction.md) supplies the
    correction that Newton I is a bridge between raw `acceleration` and
    `inertial-acceleration`; in already-inertial-frame questions, E18/E5 carries
    the modelling input while the triplet sits behind it as justification.
  - [VD-docs: Newton-analysis/newton_first_law_article.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/newton_first_law_article.md) supplies the strongest
    form of the human-input claim: the frame commitment starts the Newtonian
    programme and is presupposed by the later checking machinery, not audited by
    that machinery itself.
  - `05_design_3_catchup/CURRENT_STATE.md` and
    `05_design_3_catchup/DESIGN_3_GOALS.md` confirm the same E18 goal: carry the
    inertial-frame commitment and explain its protective role against frame
    artifacts.
  - `VD_Newton_v0.6.pdf` / `01_current_newton/VD_Newton_v0.6.pdf` confirm the
    old D2 wording for E18 and the neighbouring triplet/wall numbering.
  - `vd_law_writing_guide.pdf` / `04_entry_design_guides/vd_law_writing_guide.pdf`
    confirm the general point that Newtonian law words such as inertial frame
    are law-born structural commitments rather than ordinary independent
    vocabulary.

Old wording:

```text
inertial-frame :=
A reference-frame standard for Newtonian analysis of motion; historically, a
Galilean reference frame.
```

Current Design 2.1 draft wording:

```text
inertial-frame :=

An inertial-frame is a reference-frame used as a standard for Newtonian
analysis of motion; mechanics is simplest in such a frame. Acceleration
appearing in a trajectory described relative to an inertial-frame is not an
artifact of the frame itself. In ordinary mechanics problems, the frame in use
stands as the inertial-frame for the analysis unless it is marked as rotating or
otherwise accelerating. A lab frame, or Earth's frame to the needed
approximation, commonly serves as one; such a frame is sometimes called
Galilean.
```

Preserve:
  - An inertial-frame is a kind or status of reference-frame.
  - It is the frame standard used for Newtonian analysis of motion.
  - The historical "Galilean frame" phrase may remain as peripheral meaning.
  - The entry should install a modelling commitment, not a metaphysical claim.
  - Ordinary mechanics problems may supply this commitment implicitly.
  - The wall should protect later force accounting from frame artifacts.
  - The triplet remains the justification behind the commitment, but ordinary
    already-inertial questions can use the wall without traversing the triplet.
  - The commitment is a special human/model input: downstream machinery
    presupposes it and cannot fully audit it from inside the same machinery.

Change / reject:
  - Do not define this wall only by the triplet criterion "every free-particle
    exhibits uniform-motion"; that belongs to E3.
  - Do not say the frame is absolutely non-accelerating in a final cosmic
    sense; Design 2.1 only needs a modelling status.
  - Do not make the wall a Newton II entry. It can prepare later acceleration
    and force accounting, but it must remain readable as ordinary peripheral
    meaning.
  - Do not treat a rotating, accelerating, or otherwise marked non-inertial
    frame as licensed by the ordinary classroom assumption.
  - Do not imply that an inertial-frame removes forces or guarantees
    uniform-motion for non-free particles.
  - Do not make E5 itself perform the frame-bridging work; that belongs to the
    Newton I triplet when a question actually requires bridging.

Plain purpose:

  Give `inertial-frame` an outward-facing meaning that a reader or trace can use
  when a mechanics problem names, assumes, or withholds a frame. The entry
  should let the trace accept a chosen reference-frame as suitable for ordinary
  Newtonian motion analysis while marking that acceptance as a modelling
  commitment. Its practical effect is to prevent acceleration caused by the
  frame description itself from being misread as ordinary mechanical influence.
  It is also the place where an already-inertial-frame question receives its
  frame commitment without forcing a full triplet traversal.

IRIL - ideal residually imparted logic:

  Allowed:
    - When a selected frame has reference-frame slots and is stated or assumed
      to be inertial, expose `inertial-frame commitment` for that frame.
    - When a standard classroom problem supplies a lab, Earth, or Galilean-style
      frame and gives no acceleration, rotation, or non-inertial warning, allow
      the ordinary modelling assumption that the frame is being treated as
      inertial.
    - Let later demands for inertial-acceleration or Newtonian force accounting
      use the frame status as a prerequisite.
    - Treat the Newton I triplet as the justificatory background for the
      commitment, not as active machinery in ordinary already-inertial-frame
      questions.

  Blocked:
    - Inferring that every reference-frame is inertial.
    - Treating visible frame acceleration, frame rotation, or non-inertial
      wording as irrelevant without an explicit extra modelling step.
    - Using the wall to decide whether the particle is free.
    - Using the wall to enumerate or sum forces.
    - Treating the inertial-frame commitment as proof that the chosen physical
      frame is exactly inertial outside the model.
    - Auditing the first frame commitment solely by downstream force-accounting
      machinery that already presupposes the commitment.

  Trace consequence:
    - If the frame is supplied and treated as inertial, mark the selected
      reference-frame with `inertial-frame commitment` and record the assumption
      source: stated, conventional, or human/model input.
    - If no usable frame is supplied, demand a reference-frame or halt at a
      missing-input boundary.
    - If the supplied frame is explicitly rotating, accelerating, or otherwise
      non-inertial, halt at a domain/modelling boundary unless a later
      non-inertial-frame treatment has been supplied.

IRIEs - ideal residually imparted effects:

  Reader/modeler behaviour to install:
    - First ask which reference-frame the motion description is using.
    - Treat "inertial" as a modelling status attached to that frame.
    - If a standard Newtonian mechanics question does not specify a frame, read
      the intended frame as inertial unless the wording gives a reason not to.
    - Recognise that textbook lab/Earth-frame problems often use an implicit
      inertial-frame approximation.
    - Treat the inertial-frame commitment as the ground that lets later
      acceleration demands be normalised to `inertial-acceleration`.
    - Prefer doing Newtonian analysis in an inertial-frame when the modeler has
      a choice, because acceleration in that frame is substantive for the force
      account and the mathematics is simplest there.
    - In an inertial-frame, treat ordinary Newtonian force terms as non-virtual:
      each admitted force contribution should represent a real interaction with
      a source in the model, not an artifact of the frame choice.
    - Notice warning words such as rotating frame, accelerating frame, elevator
      frame, merry-go-round frame, or non-inertial frame.
    - Preserve the distinction between motion caused by modelled mechanical
      influence and apparent motion introduced by the frame description.

  Anti-habit / anti-misread:
    - Do not read "inertial-frame" as "a frame where there are no forces."
    - Do not route a free-particle question through old `Nothing -> Newton I`.
    - Do not turn ordinary acceleration in a non-inertial frame directly into
      ordinary force causes.
    - Do not let a frame-induced apparent acceleration enter the ordinary force
      account as though it were a non-virtual interaction force.
    - Do not use the Earth-frame approximation as a theorem.
    - Do not pretend the later trace can prove its own first frame commitment
      without an external modelling judgment.
    - Do not choose a non-inertial frame just because it is locally convenient
      without noticing that extra frame-artifact bookkeeping has been created.

Trace critical headword mentions:
  - none. E5 does not require any earlier-entry headword to be forced as a
    trace-critical mention in the wall wording.

Other headword mentions:
  - reference-frame
  - acceleration

Forbidden headword mentions / hidden imports:
  - net-force:
    why forbidden or risky: belongs downstream; mentioning it in the draft entry
    may make E5 look like a Newton II wall instead of a Newton I wall.
  - free-particle:
    why forbidden or risky: E5 should not restate the E3 triplet criterion.
    Free-particle can appear in audit notes, but not as the wall's main handle.
  - F = ma:
    why forbidden or risky: imports Newton II algebra before the frame word has
    done its own job.
  - true inertial frame:
    why forbidden or risky: encourages an absolute-physics reading instead of a
    controlled modelling commitment.
  - fictitious force:
    why forbidden or risky: useful as a warning in notes, but if placed in the
    entry string it may become a new unexplained force kind.

Question or trace moment this helps with:

  "The problem describes motion in the lab/Earth frame. Can the trace treat the
  measured acceleration as acceleration in a Newtonian frame?"

  "The problem describes a rotating frame. Should ordinary Newtonian force
  accounting proceed directly?"

  "Where does the assumption that the chosen frame is inertial land in the
  trace?"

  "Why does an already-inertial-frame problem not need to traverse the Newton I
  triplet body before using inertial-acceleration?"

Witness kind:
  inertial-frame; reference-frame

Slots read:
  - selected reference-frame identity
  - origin
  - basis vectors
  - clock
  - coordinates assigned to events
  - problem statement frame labels
  - explicit non-inertial markers
  - human/model frame modelling input

Slots written / exposed:
  - inertial-frame commitment
  - treated-as-inertial status
  - assumption provenance: stated, conventional, or human/model input
  - frame-artifact warning when non-inertial markers are present
  - eligibility for later inertial-acceleration use
  - note that the Newton I triplet is justificatory background unless frame
    bridging is demanded

Boundary behavior:
  undefined referent:
    The named frame does not resolve to a reference-frame.

  missing input:
    A motion or acceleration demand is made but no frame is selected.

  contradiction:
    The same frame is asserted to be inertial while also being asserted to have
    unhandled acceleration or rotation in the current model.

  domain boundary:
    The problem requires analysis in a rotating, accelerating, or otherwise
    non-inertial frame, and Design 2.1 has not supplied non-inertial-frame
    machinery.

  random/input boundary:
    None expected, except where a human/model must choose whether to accept a
    classroom approximation.

Suggested wording:

  ```text
  An inertial-frame is a reference-frame used as a standard for Newtonian
  analysis of motion; mechanics is simplest in such a frame. Acceleration
  appearing in a trajectory described relative to an inertial-frame is not an
  artifact of the frame itself. In ordinary mechanics problems, the frame in use
  stands as the inertial-frame for the analysis unless it is marked as rotating
  or otherwise accelerating. A lab frame, or Earth's frame to the needed
  approximation, commonly serves as one; such a frame is sometimes called
  Galilean.
  ```

Draft entry:

  ```text
  inertial-frame :=

  An inertial-frame is a reference-frame used as a standard for Newtonian
  analysis of motion; mechanics is simplest in such a frame. Acceleration
  appearing in a trajectory described relative to an inertial-frame is not an
  artifact of the frame itself. In ordinary mechanics problems, the frame in use
  stands as the inertial-frame for the analysis unless it is marked as rotating
  or otherwise accelerating. A lab frame, or Earth's frame to the needed
  approximation, commonly serves as one; such a frame is sometimes called
  Galilean.
  ```

Open questions:
  - Should Design 2.1 add `non-inertial-frame` as a named boundary placeholder,
    or is the boundary note enough?
  - Should `fictitious force` remain only a teacher-facing warning, or should a
    later design introduce it as a controlled headword?
  - Should assumption provenance be stored in a future witness sheet, or is a
    trace note enough for Design 2.1?
  - Should Design 2.1 explicitly mark the first frame commitment as
    not-auditable-by-downstream-force-accounting, or is that too much machinery
    for a wall packet?

## DEEP AUDIT ADD-ON

Role test:

  If wall/chimney: can it be read outwardly as a normal definition?

  Yes. The wording reads outwardly as a normal definition while leaving the
  modelling commitment visible.

Necessary/sufficient/asymmetric relations:
  - Being a reference-frame is necessary for being an inertial-frame.
  - Having reference-frame slots is not sufficient; the frame also needs an
    inertial-frame commitment.
  - The commitment may be stated, conventional, or supplied as human/model input.
  - The wall does not make a particle free; it only supplies the frame status in
    which free-particle and acceleration claims can later be interpreted.
  - A non-inertial marker defeats the ordinary classroom assumption unless an
    extra non-inertial treatment is supplied.
  - In an ordinary already-inertial-frame question, E5 is enough to land the
    modelling commitment; the Newton I triplet is justification in the
    background.
  - In a frame-bridging question, the Newton I triplet can become active because
    the trace must relate raw frame-dependent acceleration to
    `inertial-acceleration`.

Quantifier or modality:
  used; treated as; may; often; does not license

Suspends for human/model input?
  yes; when the frame is not explicitly stated as inertial and the ordinary
  classroom convention is not clearly applicable.

Boundary trigger:
  - no selected reference-frame
  - selected frame lacks reference-frame slots
  - selected frame is marked rotating, accelerating, or non-inertial
  - downstream demand tries to use ordinary Newtonian acceleration or force
    accounting before the frame commitment has landed

Boundary output:
  - demand selected reference-frame
  - demand inertial-frame modelling input
  - domain boundary: non-inertial-frame machinery not supplied in Design 2.1
  - contradiction if the same model asserts both ordinary inertial status and
    unhandled non-inertial frame behaviour

Alternative wordings:

  A:

  ```text
  An inertial-frame is a reference-frame used as standard for Newtonian
  analysis of motion; historically, such a frame is called Galilean.
  ```

  B:

  ```text
  An inertial-frame is a reference-frame used for Newtonian analysis as one
  in which observed accelerations are not artifacts of the frame's own
  acceleration or rotation.
  ```

  C:

  ```text
  An inertial-frame is a reference-frame whose coordinate description is being
  used under the modelling commitment that frame-induced accelerations are
  absent or outside the current model.
  ```

Chosen wording:

  ```text
  An inertial-frame is a reference-frame used as a standard for Newtonian
  analysis of motion; mechanics is simplest in such a frame. Acceleration
  appearing in a trajectory described relative to an inertial-frame is not an
  artifact of the frame itself. In ordinary mechanics problems, the frame in use
  stands as the inertial-frame for the analysis unless it is marked as rotating
  or otherwise accelerating. A lab frame, or Earth's frame to the needed
  approximation, commonly serves as one; such a frame is sometimes called
  Galilean.
  ```

Why chosen:

  This wording keeps the wall's load-bearing work while using only installed
  residual reactions: `used as a standard` gives the modelling role,
  `artifact of the frame itself` carries the frame-warning without importing a
  force account, the ordinary-problems sentence gives the default-and-defeater
  shape, and the lab/Earth/Galilean sentence gives ordinary recognition handles
  while marking the approximation.

Checks:
  The wording hits the residual goals. It exposes `reference-frame` and
  `acceleration`; makes the inertial status a modelling commitment;
  blocks frame-artifact acceleration without importing `net-force`,
  `free-particle`, `F = ma`, `true inertial frame`, or `fictitious force`; and
  is short enough to behave as a wall rather than as a lesson.
