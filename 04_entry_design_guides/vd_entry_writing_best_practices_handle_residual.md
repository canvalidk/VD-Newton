# VD Entry Writing Best Practices - Handle/Residual Version

Status: working guide, 2026-05-01.

This guide translates the handle/residual understanding of the VD into entry
writing practice. It should be read alongside:

- `00_read_first/VD_CORE_MODEL_HANDLE_RESIDUAL.md`
- `vd_six_entry_structure.md`
- `vd_acting_object_entry_authoring_guide_plan_v1.md`
- `vd_spring_acting_object_working_brief_v1.md`

## Core Rule

Write entries as controlled stimulants, not as explanatory prose.

An entry should expose a disciplined interpreter to:

- the headwords that must be expanded;
- the residual handle that tells the interpreter what operation to perform
  with those headwords;
- no extra uncontrolled physics habit.

## The Entry Test

For every candidate entry, ask:

```text
If a competent interpreter reaches this entry during a lazy trace, what will
this string make them do next?
```

If the answer is vague, or if the string encourages the interpreter to import
ordinary textbook knowledge that is not in the demand chain, the entry is not
yet good enough.

## Do Not Confuse The Four Residual Senses

Use these distinctions while drafting.

```text
residual string
  The leftover definiens text after headword removal.

residual handle
  The operable route, often written Re_n(), that tells the interpreter what
  transformation to perform.

residual causal effect
  The actual state-change produced when a human/LLM is exposed to the string.

residual function
  The idealised transformation that the entry is intended to trigger.
```

In text interpretation, the residual string is usually the stimulant that acts
as the handle. Do not treat it as decorative prose.

## Answer Plus Trace

The VD gives the answer and the trace. Entry-writing must support both.

An entry set succeeds when a query can be lazily expanded into:

```text
answer + accountable exposure route
```

or into a clear halt:

```text
undefined referent
contradiction
missing input
random/input boundary
domain boundary
```

Do not write entries that only make a retrospective explanation possible. The
entries must participate in answer production.

## Triplet Entries

Triplet entries are inward-facing residual handles.

They should expose only the two other headwords in the law plus the residual
string needed to route the interpreter through that corner of the law.

Avoid loading triplet entries with:

- examples;
- scaffolding;
- measurement procedures;
- parameter values;
- object slot filling;
- concrete force-model variants;
- downstream algebra;
- hidden recognition steps.

The usual failure mode is writing the whole law at one corner. That makes the
other two corners decorative and destroys the three-cornered structure.

## Chimneys And Walls

Peripheral entries are outward-facing.

The chimney makes the November word available from prior dictionary content.
The walls make winter words available for future use. These entries can carry
ordinary dictionary meaning, recognition hooks, and practical connection to the
rest of the log.

A useful test:

```text
Can this peripheral entry be read in isolation as a normal definition?
```

If yes, it is probably peripheral. If it only makes sense as one corner of a
law-cycle, it probably belongs in the triplet.

## Human Inputs

Human/model inputs are allowed, but they must land in the right place.

Good landing sites include:

- witness-sheet slot bindings;
- scaffold entries;
- walls and chimneys;
- concrete acting-object entries;
- modelling-assumption entries;
- parameter entries;
- construct entries;
- explicit random/input boundaries.

Bad landing sites include abstract triplet entries where the input is not part
of the law's irreducible residual operation.

Bad:

```text
At E25, human supplies: forces on p are {gravity, tension}.
```

Better:

```text
Demand interacting-forces-set(p)
  -> consult mechanical-composition_point-particle(p)
  -> unfold acting-object instances one at a time
  -> dispatch concrete type
  -> evaluate activation-condition
  -> produce canonical-force
  -> add impressed-force to the set
```

## Scoped Symbols

Bare textbook symbols are dangerous because they install the wrong handles.

Bad:

```text
F = -kx
```

Better:

```text
canonical-force_simple-spring
  = - spring-constant_simple-spring
    * displacement-from-equilibrium_simple-spring
```

The second version exposes scoped handles. It prevents the interpreter from
treating `k`, `x`, or `F` as global symbols whose meaning is supplied by
textbook habit.

## Model Scope

Name the model regime in the headword when the formula only applies in that
regime.

Bad:

```text
spring
friction
gravity
contact
```

Better:

```text
simple-spring
ideal-linear-spring
near-earth-gravity
sliding-contact_kinetic-friction
normal-contact_rigid-surface
```

The headword should be narrow enough that the residual handle it exposes is
truthful and operationally safe.

## Parameters, Constructs, Slots

Do not collapse these.

Slots are positions on object witnesses:

```text
target particle
other endpoint
paired particle
surface
field source
```

Parameters are atomic values:

```text
spring constant
coefficient of friction
mass
gravitational acceleration
```

Constructs are structured objects or relations that need their own meanings:

```text
equilibrium-configuration
displacement-from-equilibrium
contact-surface
normal direction
```

If a formula needs a construct, do not bury the construct's meaning inside the
formula entry. Give it an entry or a witness-sheet slot as appropriate.

## Activation Conditions And Modelling Assumptions

Keep these separate.

Modelling assumptions answer:

```text
Should this concrete model be used for this situation?
```

Activation conditions answer:

```text
Is this acting-object currently eligible to produce its canonical force?
```

For a simple spring, zero displacement should normally produce zero force, not
an inactive spring. Do not use activation conditions to hide force values.

## Acting Objects

Design 3 should treat acting-object instances as callable structures declared
through `mechanical-composition_point-particle`.

The preferred trace route is:

```text
point-particle witness
  -> mechanical-composition_point-particle
  -> acting-object witness
  -> concrete type hub
  -> activation-condition
  -> canonical-force
  -> impressed-force
  -> interacting-forces-set
  -> net-force
```

The acting-object entry cluster is successful only if it can produce an
attributed symbolic force before the algebraic solve.

## Witness Sheets

Witness sheets are trace-side records for concrete object commitments. They
are not a cop-out. They are where contingent facts enter visibly.

An attribute demand forces a witness:

```text
Demand inertial-mass(p1)
  -> open/consult point-particle witness p1
  -> bind/read inertial-mass slot
```

A force demand forces an acting-object witness:

```text
Demand spring force on p1
  -> consult p1 mechanical composition
  -> find spring_1
  -> open/consult spring_1 witness
  -> bind/read needed slots and parameters
```

Entries should force these witness actions, not smuggle their results in as
unattributed prose.

## Failure Signals

A good entry set should fail informatively.

When the trace cannot answer, it should be clear whether the problem is:

- no referent for a demanded headword;
- contradiction among commitments;
- unbound witness-sheet slot;
- random/input boundary;
- unencoded concrete acting-object;
- domain mismatch;
- insufficient discipline in a residual handle.

Do not erase these distinctions by writing entries that ask the human for a
final textbook answer.

## Minimal Review Checklist

Before accepting an entry, ask:

- What headword does this entry define?
- Which headwords in the definiens will the engine expose?
- What residual string remains after headword removal?
- What operation should that residual string trigger?
- Is the residual string disciplined enough for a human/LLM interpreter?
- Is this entry inward-facing or outward-facing?
- Are human inputs landing at visible trace locations?
- Are symbols scoped to the relevant object or model regime?
- Are slots, constructs, and parameters separated?
- Does the entry help produce the answer, not merely explain it afterwards?

