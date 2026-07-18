# Current Design 3 State

## Core VD Orientation

The VD should be read as a lazy answer-producing theory representation, not
only as an audit system.

A textbook question is normalised to a headword. The selected headword starts a
demand chain. That chain exposes the interpreter to entries, daughter
headwords, residual strings, witness demands, and input boundaries in a
controlled order. A disciplined interpreter is thereby routed through the
operations needed to produce the answer.

The trace records that route. If the expansion terminates, the VD gives:

```text
answer + accountable expansion route
```

If the expansion halts, the halt is itself informative: undefined referent,
contradiction, unbound input, random/input boundary, or domain boundary.

For the residual/handle basis of this reading, see
`00_read_first/VD_CORE_MODEL_HANDLE_RESIDUAL.md` and
`90_theory_reference/handle_derivation_note_rewritten.md`.

The same trace also has a question-answering presentation layer. For
explain/describe questions, run the normalised trace and present each demanded
step under "And that's because:". The raw result is a because-chain; remove
steps too obvious to score and smooth the grammar afterwards. See
`04_entry_design_guides/vd_question_answering_because_trace.md`.

## Core Model

Design 3 should be read from the question side, not the particle side. A
textbook question is first normalised to a headword. The selected headword
determines the trace ancestry.

Examples:

- `inertial-acceleration(p)` expands through Newton II.
- `path(p)` can expand through Newton I / uniform-motion material.
- `inertial-acceleration(photon)` halts on undefined `inertial-mass`.
- `path(photon)` is a different question and may terminate cleanly.

Particles do not route themselves. Questions route by choosing headwords.

## Newton I Correction

The current correction is:

- Newton I is not the branch for free particles.
- Newton I is the bridge between raw `acceleration` and
  frame-purified `inertial-acceleration`.
- E18 should carry the inertial-frame modelling commitment in ordinary
  inertial-frame problems.
- The Newton I triplet sits behind that wall as justification.
- The triplet body becomes active when the question requires frame bridging,
  or when the question is about path/uniform-motion rather than
  inertial-acceleration.

Consequences:

- The old Nothing/Maybe branch is superseded.
- `ao0` is rejected.
- A free massive particle in an inertial frame may go through Newton II:
  empty force sum gives the zero vector, and `0 / m = 0`.
- A massless particle queried through Newton II halts because `inertial-mass`
  has no referent.

What survives from the older Nothing-vs-zero notes:

- `inertial-mass` has a real domain boundary.
- Massive and massless particles are structurally distinct.
- Newtonian force cannot act on massless particles inside the Newton II
  pipeline.
- The photon/gravity point remains a boundary-detection result.

## Acting-Object Architecture

The current architecture treats scenarios as mechanical-compositions.

There is no separate scenario-object layer. A scenario is declared by the
acting-object instances appearing in particles'
`mechanical-composition_point-particle`s. The apparent ordinary object
inventory is residual-layer shorthand.

An acting-object instance is a callable structure, not a force value. It is
declared in mechanical-composition and later evaluated on demand.

The important layers are:

- abstract acting-object law: `acting-object`,
  `activation-condition_acting-object`, `canonical-force_acting-object`;
- mechanical-composition: which acting-object instances a particle has;
- concrete type hub: spring, near-earth gravity, contact, friction, etc.;
- concrete activation condition and canonical-force entries;
- constructs and parameters demanded by the concrete canonical-force formula.

## Dispatch

The current practical answer is still Option A from the early dispatch note:
concrete type hub entries should carry the abstract-to-concrete mapping.

For example, a spring type hub should make it trace-visible that:

- this instance is an `acting-object`;
- its abstract activation-condition slot resolves to the spring-specific
  activation-condition;
- its abstract canonical-force slot resolves to the spring-specific
  canonical-force;
- its participant slots, constructs, and parameters are those demanded by the
  spring force rule.

No new dispatch law is justified yet. Try explicit concrete entry clusters
first.

## Activation And IFS

The force set should not be populated as a flat human list:

```text
human: forces on p are {gravity, tension}
```

Design 3 wants the force set to unfold through mechanical-composition:

```text
mechanical-composition(p) supplies an acting-object instance
dispatch resolves its concrete type
activation-condition is exhibited and evaluated
canonical-force is produced
acting-force joins the interacting-forces-set
repeat until explicit no-more input closes the list
```

The key structural target is activation-condition parity with
paired-particle. If a force is in the IFS, the trace should be able to exhibit
the activation condition that made that membership coherent. The condition
must also have independent checkable content, or the entailment becomes
vacuous.

## Producer And Constraint Forces

The current consolidation rejects an early proposed split between producer
acting-objects and constraint acting-objects.

For now, both use the same fragment shape. The difference is content:

- a spring may return `F = -k x`;
- normal contact may return a fresh symbol `N`;
- string tension may return a fresh symbol `T`;
- constraint equations appear alongside the force equations and downstream
  solving handles the coupled system.

The trace's product is attributed equations, not necessarily solved numeric
values.

## Entity Identity

The current identity rule is user-supplied haecceity:

- every VD entity has an explicit identity token;
- equality is token equality;
- the evaluator does not generate IDs;
- the dictionary remains stateless at its own level;
- repeated time evolution is an outer layer that reruns traces against fresh
  inputs.

Force identity is probably derived from acting-object instance plus target or
pairing, but that should be confirmed after the acting-object refactor.
