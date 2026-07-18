# Witness Sheets

## Short Version

A witness sheet is the trace-side record for a concrete object instance.

The VD entries define which object kinds and attributes are available. A trace
creates or consults witness sheets when those attributes are demanded.

For example:

```text
point-particle p1
  identifier: p1
  inertial-mass: 3 kg
  position: r1(t)
  velocity: v1(t)
  mechanical-composition_point-particle: {spring_1, gravity_1}
```

The sheet is called a witness sheet because it witnesses that an object is
really being committed to in the trace. The trace is no longer just mentioning
an attribute like `inertial-mass`; it is committing to an object that has that
attribute.

## Why The VD Needs Them

VD entries are general. They define words and their dependencies.

For example:

```text
inertial-acceleration depends on net-force and inertial-mass.
```

But a trace is particular:

```text
Find inertial-acceleration(p1).
```

That trace eventually demands:

```text
inertial-mass(p1)
```

At that point the trace needs a concrete place to store the fact that `p1` is a
particle and that its mass is, say, `3 kg`. That place is the witness sheet.

The dictionary does not need to contain every particular object in advance.
Instead:

```text
VD entry gives the schema.
Trace demand creates or consults the witness.
Viewer/model/world input fills missing slots.
Future demands reuse the same sheet.
```

## Haskell Analogy

Haskell is useful because it is lazy. A value can be declared without every
part of it being evaluated immediately.

For example:

```haskell
data Particle = Particle
  { identifier :: String
  , mass       :: Double
  , position   :: Position
  , velocity   :: Velocity
  }

p1 = Particle "p1" 3 r1 v1
```

If a program asks only for:

```haskell
mass p1
```

Haskell does not need to inspect every other field of `p1`. It evaluates just
enough of `p1` to know that it is a `Particle`, then reads the `mass` field.

The VD trace should work in the same spirit.

```text
Demand: inertial-mass(p1)
  -> create or consult witness sheet for p1
  -> fill/read inertial-mass
  -> leave position and velocity alone unless later demanded
```

So the object is not fully unpacked all at once. It is unfolded as the trace
needs it.

## Demand-Driven Witness Creation

A witness sheet can be created lazily.

That means the trace does not need to begin by writing complete sheets for
every possible object. It can start with the question and let demands force the
required witnesses.

Example:

```text
Question:
  Find inertial-acceleration(p1).

Demand:
  inertial-acceleration(p1)

Entry:
  inertial-acceleration = net-force / inertial-mass

Subdemands:
  net-force(p1)
  inertial-mass(p1)

Witness action:
  Open or consult witness sheet for p1.
  Bind p1 as a point-particle.
  Read or supply inertial-mass(p1).
```

If later the trace demands:

```text
position(p1)
```

the same witness sheet is consulted. The trace does not create a second `p1`.
It adds or reads another slot on the existing witness.

## Slots Can Stay Blank

A witness sheet does not need to be complete when it is first created.

It can contain blank slots:

```text
point-particle p1
  identifier: p1
  inertial-mass: 3 kg
  position: unbound
  velocity: unbound
```

This is important. The VD should not ask the viewer to fill irrelevant facts.
Only demanded facts need to be supplied.

The rule is:

```text
Do not fill a slot just because the object has that kind of slot.
Fill it when the trace demands it.
```

## Witness Sheets And Mechanical Composition

For Newton Design 3, the most important witness sheet slot is probably:

```text
mechanical-composition_point-particle
```

This is where acting-object instances appear.

Example:

```text
point-particle p1
  identifier: p1
  inertial-mass: 3 kg
  mechanical-composition_point-particle:
    - spring_1
    - earth_gravity_1
```

Each acting-object can have its own witness sheet:

```text
simple-spring spring_1
  identifier: spring_1
  target endpoint: p1
  other endpoint: wall_1
  spring constant: k
  equilibrium configuration: eq_1
```

The trace can move from particle sheet to acting-object sheet:

```text
Demand: interacting-forces-set(p1)
  -> consult p1.mechanical-composition_point-particle
  -> next acting-object is spring_1
  -> consult/create witness sheet for spring_1
  -> demand activation condition
  -> demand canonical force
```

This avoids the old bad move:

```text
Human: forces on p1 are {gravity, spring}
```

Instead the force list unfolds from witness sheets and definitions.

## External Object Detection

This is the big payoff.

In Newtonian mechanics, if something inside a mechanical system feels an
external force, that force should point back to something outside the system.

Witness sheets give the trace a way to make that explicit.

Example:

```text
Mechanical system S:
  contains p1

Trace finds:
  spring force acts on p1

Trace expands:
  spring force comes from spring_1
  spring_1 has other endpoint wall_1
  wall_1 is not in S

Conclusion:
  S is mechanically open.
```

The trace has inferred an external object commitment:

```text
If this force is really acting on p1, then there is a witness outside S that
the force depends on.
```

This is not fancy metaphysics. It is just good bookkeeping with consequences.

If a force term appears, the trace should be able to show its source witness.
If the source witness is outside the chosen system, the system boundary leaks.

## The Rule

The working Design 3 rule is:

```text
Attribute demand forces a witness sheet.
Force demand forces an acting-object witness.
An acting-object witness may force further participant/source witnesses.
If those witnesses lie outside the mechanical system, the system is open.
```

This lets the VD make useful object inferences without pretending that the
dictionary created the objects from nothing.

The dictionary supplies structure.

The trace supplies demand.

The witness sheet records the object commitment.

## What Witness Sheets Are Not

A witness sheet is not a new hidden physics theory.

It is not an attempt to make every input declarative.

It is not a claim that all facts are already known before the trace.

It is a trace artifact: a stable place to put the object commitments and slot
bindings that the trace has forced.

Some slots are filled by ordinary model input:

```text
inertial-mass(p1) = 3 kg
```

Some slots are filled by measurement:

```text
position(p1, t0) = r0
```

Some may remain symbolic:

```text
spring-constant(spring_1) = k
```

The important part is that once a slot is filled, later demands consult the
same witness sheet.

## Relation To Randomness

Random values mark a boundary.

If a slot value is genuinely random, the VD should not pretend that the value
was produced by an ordinary object witness unless the theory actually supplies
such an object.

Instead the trace should record something like:

```text
Demand: random outcome slot
  -> no deterministic witness slot supplies the value
  -> random input boundary
  -> sampled value is bound on the witness sheet
```

So witness sheets do not erase the randomness boundary. They make it clearer.

Ordinary object-backed facts are recorded as object slots. Random samples are
recorded as values that entered at a boundary and were then bound for later
reuse.

## Minimal Terminology

Use these terms going forward:

```text
witness sheet
  The trace-side record for a concrete object instance.

object witness
  The concrete instance whose existence is committed to by the trace.

slot
  A demandable attribute on a witness sheet.

slot binding
  A filled value for a slot.

unbound slot
  A slot whose value has not yet been demanded or supplied.

schema
  The object-kind template saying which slots may be demanded.
```

The phrase "object sheet" can still be used informally, but "witness sheet" is
the Design 3 term.

