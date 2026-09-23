# Randomness And The Declarative Boundary

## Short Version

In a declarative theory, facts are supposed to follow from fixed definitions,
relations, and inputs.

Randomness is different.

A random value is not produced by the ordinary object-attribute machinery of
the theory. It enters at a boundary.

For the VD, this matters because witness sheets let a trace say:

```text
This attribute belongs to this object witness.
```

But a genuinely random outcome cannot always be handled that way.

The trace may be able to say:

```text
This is where the random value enters.
```

It cannot necessarily say:

```text
This ordinary physical object produced the exact value.
```

unless the theory has added some further hidden structure that determines the
value.

## Declarative Languages Make The Boundary Visible

In a pure declarative or functional setting, a value is determined by the
program's definitions and its inputs.

For example, a Haskell-style record can store a particle's mass:

```haskell
data Particle = Particle
  { identifier :: String
  , mass       :: Double
  }
```

If the program has:

```haskell
p1 = Particle "p1" 3.0
```

then `mass p1` returns `3.0`.

That is ordinary object-backed lookup. The value is already part of the object
record.

Randomness is not like that in pure Haskell. A pure value cannot secretly roll
a die. Randomness has to be pushed into an effect or made explicit as an input:

```haskell
makeParticle :: IO Particle
```

or:

```haskell
makeParticle :: StdGen -> (Particle, StdGen)
```

or represented symbolically:

```text
mass(p1) ~ Uniform(1, 10)
```

The point is simple: the random value is not created by the pure declarative
core alone. It comes through an outside channel, an effect, a seed, a sampled
input, or a distribution.

## The VD Version

In the VD, ordinary object-backed facts work through witness sheets.

Example:

```text
Demand:
  inertial-mass(p1)

Witness sheet:
  point-particle p1
    inertial-mass: 3 kg
```

The demand finds or forces an object witness, then reads or fills the slot.

But a genuinely random outcome has a different shape:

```text
Demand:
  outcome(q1)

Theory supplies:
  possible outcomes and probabilities

Trace action:
  random input boundary
  bind actual outcome(q1) = observed value
```

The theory may tell us the distribution. It may tell us which outcomes are
allowed. It may tell us how probabilities change with the setup.

But the individual sampled value is not explained as the determined attribute
of an ordinary object witness.

## Why This Matters For Quantum Mechanics

The Newtonian picture encourages a very strong habit:

```text
If something unexplained appears in the trace, look for the missing object.
```

For example:

```text
Particle p1 accelerates.
  -> net-force(p1) is nonzero.
  -> some impressed-force is present.
  -> some acting-object witness must be involved.
  -> if that witness is outside the system, the system is open.
```

That is a good rule for Newtonian force accounting. An unexplained force points
to a missing source, support, field, string, spring, surface, or other object
commitment.

Quantum randomness does not fit that pattern in the same way.

If a quantum model gives a random measurement outcome, the trace should not
automatically infer:

```text
There must be an ordinary missing object that determined this exact outcome.
```

That would change the theory. It would turn the random outcome into a hidden
object-backed attribute.

Instead the VD should mark:

```text
Here the theory gives probabilities.
Here the actual value enters as a random outcome.
Here the value is bound for the rest of this trace.
```

So the random outcome is accountable, but not object-explained in the ordinary
Newtonian way.

## The Contrast

Newtonian external force:

```text
unexplained force
  -> force must have an acting-object source
  -> trace demands a source witness
  -> source may be outside the system
```

Quantum/random outcome:

```text
unexplained sampled value
  -> theory supplies distribution/rule
  -> trace marks random boundary
  -> actual value enters
  -> value is bound for later use
```

The first case forces an external object.

The second case forces an input boundary.

That is the gist.

## Why This Is Interesting

If physical theories are expected to be fixed before the question is asked,
and to apply unchangingly to any question, they start to look like declarative
systems.

They say:

```text
Here are the definitions.
Here are the object kinds.
Here are the relations.
Now ask a question, and the answer follows.
```

Classical mechanics fits that style very well. It lets us imagine that the
world has a huge witness sheet already filled in, and the trace merely asks
for the relevant slots.

Quantum mechanics strains that picture.

Not only because it is unfamiliar, but because genuine random outcomes do not
behave like ordinary pre-filled object slots.

The theory can define the setup and the probability rule. But when the actual
outcome arrives, the trace has reached a point where declarative object
accounting cannot continue in the normal way.

The value enters. It is recorded. But it is not backed by an ordinary source
object unless the theory is changed to include one.

## What Not To Do

Do not hide the problem by inventing a fake witness sheet like:

```text
random-source r1
  next outcome: spin up
```

If `next outcome` was already sitting there as an attribute, then the model is
not using randomness in the same sense. It has replaced randomness with a
hidden determiner.

That may be a valid different theory, but it is not the same explanatory
structure.

The VD should keep the distinction clear:

```text
object-backed input:
  value belongs to a witness sheet slot

random input:
  value enters at a random boundary, then may be bound on a sheet for reuse
```

## Trace Shape

A VD-style trace should show the boundary plainly.

Example shape:

```text
DEMAND:
  measurement-outcome(q1, apparatus_A)

EXPAND:
  theory supplies allowed outcomes
  theory supplies probability weights

BOUNDARY:
  no ordinary object witness determines the individual sample
  random outcome is required

INPUT:
  observed outcome = up

BIND:
  measurement-outcome(q1, apparatus_A) := up
```

After binding, the value is stable for that trace. Later steps can consult it.

But the trace should remember how it entered:

```text
source of binding: random boundary / measurement input
```

not:

```text
source of binding: ordinary object attribute
```

## Working Principle

Use this distinction going forward:

```text
The VD can force object witnesses for object-backed attributes.
The VD can force random boundaries for genuinely random outcomes.
It should not confuse the two.
```

This is the important QM point.

Randomness is not merely a blank slot waiting to be filled by a hidden object
sheet. It is a place where the ordinary object-witness machinery reaches its
limit.

