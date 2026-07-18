# The Object Cop-Out Is Not A Cop-Out

## Claim

For the current Design 3 stage, object sheets may be treated as a trace-side
operation outside the declarative VD entries.

That is not a retreat from the VD. It is an honest boundary between:

- what dictionary definitions can force;
- what the trace can demand and record;
- what the viewer, model, or world must supply.

In short:

```text
VD entries define object schemas and slot dependencies.
Trace demands force object-sheet creation or consultation.
Viewer/world input fills contingent slots.
The trace records the supply event.
```

The VD does not need to pretend it can generate every concrete fact from
definitions alone.

## The Vision

Before running a trace, the viewer compiles the relevant object kinds into
schemas.

For example:

```text
point-particle:
  identifier
  position
  velocity
  inertial-mass
  mechanical-composition_point-particle

simple-spring:
  identifier
  spring-constant
  equilibrium-configuration
  endpoint slots
  paired particle / participant structure
```

During the trace, when an entry demands an attribute belonging to an object
kind, the trace pauses and opens or consults an object sheet.

For example:

```text
Demand: inertial-mass(p1)

Object sheet:
  object: p1
  kind: point-particle
  inertial-mass: 3 kg
```

Once the sheet is filled, later demands consult it rather than asking again.

## Why This Is Not A Cop-Out

Declarative systems do not create contingent facts from nowhere.

A declarative structure can say:

```text
If x is a point-particle, then inertial-mass(x) is a demandable attribute.
Newton II requires inertial-mass(x).
```

But it cannot derive:

```text
inertial-mass(p1) = 3 kg
```

from the meaning of `point-particle` alone.

That value is not definitional. It is contingent. It belongs to the modelled
situation. Therefore it must enter as an input, measurement, modelling
commitment, or previously stored binding.

The VD's job is not to supply the value. The VD's job is to force the exact
place where the value is needed.

That is a strength, not a failure. It prevents hidden physics from entering
the trace unmarked.

## The Declarative-Language Analogy

In a pure declarative or functional core, values are determined by definitions,
relations, and inputs.

For example, a Haskell-style record can define the shape of an object:

```haskell
data Particle = Particle
  { identifier :: String
  , mass       :: Double
  , position   :: Position
  }
```

But pure Haskell cannot secretly choose a random `mass` when the program asks
for it. Genuine randomness has to be represented as something outside the pure
value:

```haskell
makeParticle :: IO Particle
```

or as an explicit random generator:

```haskell
makeParticle :: StdGen -> (Particle, StdGen)
```

or as symbolic probabilistic data:

```text
mass(p1) ~ Uniform(1, 10)
```

The same principle applies to VD object sheets.

The VD can declare that a particle has a mass slot. It cannot derive the
particular mass of this particle unless that value is supplied by the model.

So placing sheet construction and slot filling in the trace/viewer layer is not
an evasion. It mirrors the way declarative languages handle effects,
randomness, measurement, and other non-derived facts.

## Lazy Demand And Object Sheets

The useful part of the Haskell analogy is laziness.

If a list contains many objects, a lazy program does not need to evaluate every
field of every object immediately. It evaluates only what is demanded.

VD object sheets should behave similarly:

```text
Demand: inertial-mass(p1)
  -> create or consult object sheet p1
  -> fill or read inertial-mass
  -> leave position, velocity, and other slots unresolved unless demanded
```

This gives Design 3 a disciplined trace behaviour:

- object schemas can be compiled before the trace;
- object sheets can be instantiated lazily;
- slots can remain latent until demanded;
- first demand fixes or records a binding;
- later demands reuse the same binding.

The object is not fully expanded merely because it exists. It is expanded only
where the trace needs it.

## The Metaphysical Payoff

The important VD principle is:

```text
Demanding an attribute forces an object witness.
```

An attribute is not free-floating. If the trace demands:

```text
inertial-mass(p1)
```

then the trace has committed to an object witness `p1` of a kind for which
`inertial-mass` is a coherent slot.

Likewise, if the trace demands:

```text
canonical-force_acting-object(a1)
```

then it has committed to an acting-object witness `a1`.

This matters for Newtonian mechanics because force attribution is ontological.
If a particle inside a mechanical system has an external force acting on it,
the trace should not merely record an unexplained vector. It should force a
witness for the cause of that force.

For example:

```text
F acts on p1
  -> F is an acting-force
  -> F is supplied by canonical-force_acting-object(a1)
  -> a1 is an acting-object
  -> a1 has participant / paired / source structure
  -> some required witness lies outside mechanical-system S
  -> S is mechanically open
```

This is the closure payoff. External force detection becomes external object
detection.

## What Stays Outside For Now

For this stage, the following can remain outside the declarative VD entry
system:

- the act of opening an object sheet;
- the user interface or trace notation for a sheet;
- the filling of contingent slot values;
- random or measured values;
- the persistence/cache mechanism for already-filled sheets.

These should still be recorded in the trace. They are outside the declarative
entry structure, not outside accountability.

## What The VD Still Forces

Even if object sheets are trace artifacts, the VD can still force:

- which object kind is required;
- which attribute slot is being demanded;
- whether an existing sheet can satisfy the demand;
- whether the demanded slot is coherent for that object kind;
- whether a missing slot requires viewer/world input;
- whether force attribution implies an external object witness.

So the stage-one position is:

```text
Object sheets are not VD entries yet.
Object-sheet demands are forced by VD entries.
Slot values are supplied outside the declarative core.
Every supply event is trace-visible.
```

That is not a cop-out. It is the same boundary respected by declarative
languages: definitions determine structure, but contingent facts must enter as
inputs, effects, seeds, measurements, or bindings.

## Later Internalisation

Later Design 3 work may internalise some of this machinery with entries such
as:

- `object-sheet`
- `object-witness`
- `attribute-slot`
- `compiled-object-schema`
- `slot-binding`
- `unbound-slot`

But this should not be rushed.

The first goal is to make traces honest:

```text
When the dictionary needs a concrete object fact, the trace shows exactly
where the object witness and slot binding entered.
```

That is enough for the next stage.
