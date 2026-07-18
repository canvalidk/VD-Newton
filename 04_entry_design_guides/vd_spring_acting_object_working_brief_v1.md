# Spring Acting-Object Working Brief v1

## Purpose

This note gathers the information needed before attempting spring
acting-object entries for Newton Design 3. It is not yet an entry proposal.
It is a staging document: ordinary mechanics content, VD architectural
requirements, trace-time residual inputs, and known traps are kept separate.

Local sources used:

- `vd_acting_object_architecture_consolidation.md`
- `qpt_envisioner_dispatch_deep_dive.md`
- `unfolding_forces.md`
- `vd_design_3_trace_architecture (1).md`
- `vd_design_3_todo.md`

## Ordinary Mechanics: Ideal Linear Spring

An ideal linear spring is normally represented by Hooke's law. In one
dimension:

```text
F = -k x
```

where:

- `F` is the force exerted by the spring on the endpoint being evaluated.
- `k` is the spring constant.
- `x` is signed displacement from the spring's equilibrium/rest position.
- The minus sign indicates that the force opposes displacement from
  equilibrium.

In a two-endpoint 3D form, with endpoints A and B:

```text
r = position(A) - position(B)
L = |r|
u = r / L
extension = L - L0
F_on_A = -k * extension * u
F_on_B = +k * extension * u
```

Equivalent sign conventions are possible, but a trace must state which endpoint
and which direction vector are being used.

The ideal spring can pull when stretched and push when compressed. At its rest
length, the spring force is zero. If the spring is slack, buckling, plastic,
damped, massive, nonlinear, or geometrically constrained, the ideal linear
spring model is no longer the whole story.

## Minimal Physical Data

A spring acting-object instance normally needs:

- two endpoint slots;
- a spring constant `k`;
- either a rest length `L0` or an equilibrium-point/equilibrium-configuration
  construct;
- endpoint positions in the frame used for the force calculation;
- a modelling assumption that the spring is ideal, linear, massless, and
  point-attached, if those approximations are intended.

For a one-end-fixed textbook problem, the fixed support can be represented as
the second endpoint, or as a construct/equilibrium point supplied by the viewer.
That choice is architectural, not just notational.

## VD Architecture Commitments

The current abstract acting-object triplet is:

```text
E34 acting-object:
  An acting-object is an object equipped with both an
  activation-condition_acting-object and a corresponding
  canonical-force_acting-object.

E35 activation-condition_acting-object:
  If a point-particle fulfills the activation-condition_acting-object of an
  acting-object, the canonical-force_acting-object of that acting-object will
  be an acting-force on the point-particle.

E36 canonical-force_acting-object:
  The canonical-force_acting-object is the acting-force that an acting-object
  exerts on a point-particle that fulfills the
  activation-condition_acting-object.
```

The consolidation note adds these commitments:

- The scenario is the collection of acting-object instances appearing in
  particles' `mechanical-composition_point-particle`s.
- There is no independent scenario-object layer.
- Producer and constraint acting-objects have the same fragment shape; they
  differ in what their canonical-force rule returns.
- A spring is a producer acting-object: its canonical-force rule routes demand
  inward to constructs and parameters.
- A spring instance should carry only what its canonical-force rule demands.
- A spring has fixed arity: two particle endpoint slots.
- Constructs and parameters are determined by the canonical-force formula.

## Slots, Constructs, Parameters

The consolidation note distinguishes three kinds of binding.

Slots:

- Endpoint 1: a particle-typed slot.
- Endpoint 2: a particle-typed slot.
- The point-particle being evaluated must be one of these endpoints if the
  spring force is to act on it.

Parameters:

- `k`, the spring constant: an atomic scalar parameter.
- Possibly `L0`, the rest length, if the spring is represented in two-endpoint
  length form.

Constructs:

- Equilibrium-point or equilibrium-configuration.
- Endpoint position relative to that equilibrium construct.
- Direction from the other endpoint to the evaluated endpoint, if using a 3D
  endpoint-pair formulation.

The important VD point: a construct is not just a geometric primitive. The
equilibrium construct earns law-rank status because its meaning is locked to
force behavior: it is the configuration at which the spring canonical-force
vanishes.

## Candidate Canonical-Force Shapes

### One-end/equilibrium-point shape

This is the shape suggested by the consolidation note:

```text
canonical-force_spring(endpoint)
  = -k * displacement-from-equilibrium(endpoint)
```

This makes `k` a parameter and `displacement-from-equilibrium` a construct
defined through endpoint and equilibrium-point.

Good for:

- textbook mass-on-spring oscillator;
- a spring attached to a fixed wall;
- simple 1D traces.

Risk:

- hides the second endpoint if the spring connects two moving particles;
- may smuggle a fixed support as a background object rather than an endpoint
  in mechanical-composition.

### Two-endpoint/rest-length shape

```text
canonical-force_spring(A)
  = -k * (|position(A) - position(B)| - L0) * unit(A - B)
```

Good for:

- two-body spring systems;
- moving endpoints;
- action-reaction accounting.

Risk:

- requires vector normalization and a zero-length exception;
- makes `L0` look like a parameter rather than a construct unless rest length
  is tied back to the zero-force state;
- may be too much geometry for the first Design 3 test.

### Half-interaction accounting variant

If the half-interaction hypothesis is used consistently, a two-sided spring
interaction may be represented by paired spring acting-objects:

```text
mechanical-composition(A) includes S_A
mechanical-composition(B) includes S_B
```

Then the force on A is recovered from:

```text
canonical-force(S_B on A) + reaction-force(S_A on A)
```

Each contribution may carry half the ordinary spring magnitude, so their sum
recovers the textbook spring force. This is promising by analogy with the
incline trace, but it is not yet validated for springs.

## Activation vs Modelling Assumption

The QPT/deep-dive notes warn that the current
`activation-condition_acting-object` can conflate two different things.

Modelling assumptions:

- This physical situation is being idealised as a spring interaction.
- Hooke's law is valid in the displacement range considered.
- The spring is massless, linear, undamped, and point-attached.
- The endpoint slots are the chosen grain of representation.

These are checked at instantiation. If they fail, the spring acting-object
should not be generated in this model.

Operating conditions:

- The endpoint remains attached.
- The displacement/extension is defined.
- The spring is not broken, slack-only outside its active range, or outside
  its elastic regime.

These are evaluated at trace time. The spring may remain in the scenario even
when its instantaneous force is zero.

Important correction: `extension != 0` should not be required for activation
if zero extension simply produces zero force. A spring at equilibrium is still
a valid active spring acting-object; its canonical-force evaluates to the zero
vector. Treating zero extension as inactive would confuse zero contribution
with absence of the acting-object.

## Trace-Time Human Inputs

A spring trace should mark human/viewer input at least at these points:

- Normalisation of the textbook question to a VD headword.
- Declaration that a spring acting-object instance exists in the relevant
  mechanical-composition.
- Endpoint slot fillers.
- Recognition that the endpoint fillers satisfy the required particle types.
- Modelling assumption that the ideal linear spring approximation is being
  used.
- Parameter value `k`.
- Rest length/equilibrium construct, unless derived from another entry.
- Frame or coordinate representation for endpoint positions.
- Any special regime: compressed/tension-only spring, slack string-like spring,
  damping ignored, mass ignored, fixed support approximation.

None of these should land at the abstract acting-object triplet entries. They
should land at walls, concrete spring entries, or construct/parameter entries.

## Force Attribution Pattern

A Design 3 spring trace should avoid:

```text
HUMAN INPUT: forces on mass are {spring force}
```

It should instead unfold the force:

```text
DEMAND: interacting-forces-set(p, t)
  -> demand next acting-object from mechanical-composition(p)
  -> spring acting-object instance enters
  -> dispatch/classify as spring
  -> check spring modelling assumptions
  -> evaluate activation condition
  -> evaluate canonical-force_spring
  -> demand k
  -> demand displacement-from-equilibrium or endpoint separation
  -> produce spring acting-force
  -> add acting-force to force sum
```

The force being in the interacting-forces-set and the activation condition
being satisfied should be two faces of one definitional commitment, not two
separate human declarations.

## Equilibrium Construct: The Hard Part

The spring's equilibrium construct is the deep encoding problem.

Naive wording:

```text
The equilibrium-point of a spring is its rest position.
```

Why this is weak:

- It treats the construct as an external geometric fact.
- It does not explain why that point matters for force.
- It does not lock the construct to the canonical-force behavior.

VD-shaped wording should instead make the construct law-like:

```text
The equilibrium-configuration_spring is the configuration at which the
canonical-force_spring vanishes.
```

Then displacement is not merely "distance from a point." It is displacement
from the zero-force configuration. The construct's meaning is fixed by the
canonical-force slot, and the canonical-force rule refers back to the construct.
This cyclicity is the attractive airtightness: the spring data are sorted by
their role in the force-producing cycle.

Candidate cycle to explore:

```text
canonical-force_spring
displacement-from-equilibrium_spring
equilibrium-configuration_spring
```

Possible readings:

- The canonical-force is proportional to displacement from equilibrium.
- Displacement from equilibrium is the positional difference from the
  equilibrium configuration.
- The equilibrium configuration is the configuration at which the
  canonical-force vanishes.

This is likely closer to a law-house than a mere entry cluster.

## Potential Entry Families

This is not final wording, but the likely entry family is:

- `spring-acting-object`
- `endpoint-slot_spring-acting-object`
- `spring-constant_spring-acting-object`
- `equilibrium-configuration_spring-acting-object`
- `displacement-from-equilibrium_spring-acting-object`
- `activation-condition_spring-acting-object`
- `canonical-force_spring-acting-object`
- possibly `rest-length_spring-acting-object`
- possibly `extension_spring-acting-object`

There may also need to be:

- a modelling-assumption wall for `ideal-linear-spring`;
- a dispatch hub that connects `spring-acting-object` to the abstract
  `acting-object`, `activation-condition_acting-object`, and
  `canonical-force_acting-object` slots;
- a two-endpoint action-reaction mapping compatible with the current
  `mechanical-composition_point-particle` architecture.

## Spring Variants to Keep Separate

Do not collapse these into the first entry:

- ideal linear spring;
- nonlinear spring;
- damped spring;
- massive spring;
- torsional spring;
- tension-only spring or elastic cord;
- compressed spring with buckling/contact complications;
- spring constrained to one dimension;
- spring between two moving particles;
- spring attached to a fixed support;
- spring in series or parallel with other springs.

The first Design 3 spring should probably be the ideal, massless, linear,
undamped, point-attached, two-endpoint spring. Simpler one-end-fixed textbook
cases can then be represented by a fixed support endpoint or a derived
equilibrium construct.

## Reliability Checklist For Proposed Spring Entries

A proposed spring entry set should pass these checks:

- It distinguishes slots, constructs, and parameters.
- It does not treat `k` and equilibrium configuration as the same kind of data.
- It does not make zero extension mean the spring is absent.
- It routes human inputs to walls/concrete entries, not abstract triplet
  entries.
- It can produce a symbolic force before solving a whole problem.
- It attributes the force to a concrete spring acting-object instance.
- It handles both canonical and reaction sides.
- It can represent a fixed support without silently creating a hidden scenario
  object layer.
- It makes the zero-force/equilibrium relation definitional, not merely
  descriptive.
- It remains compatible with lazy IFS iteration and `ao0` termination.

## Open Questions

1. Should the first spring entry be one-end/equilibrium-point shaped or
   two-endpoint/rest-length shaped?

2. Is `equilibrium-configuration_spring` a construct wall, or part of a new
   spring-specific law-house with `canonical-force_spring` and
   `displacement-from-equilibrium_spring`?

3. Under half-interaction accounting, should each side's spring acting-object
   carry half the ordinary spring magnitude, or should the paired acting-object
   structure be rewritten before springs are attempted?

4. Should `rest-length_spring` be treated as a parameter, a construct, or a
   derived scalar from the equilibrium configuration?

5. How should a fixed wall/support be represented without reintroducing a
   scenario-object layer?

6. What is the correct activation condition for an ideal spring if zero
   extension produces zero force but the spring interaction remains present?

7. Does the spring canonical-force rule require vector projection entries
   before it can be cleanly encoded?

## Recommended Next Test

Use the simplest nontrivial scenario:

```text
A point-particle mass m is attached to an ideal linear spring with spring
constant k. The other endpoint is fixed. The particle is displaced by x from
the spring equilibrium configuration. Find inertial-acceleration.
```

The target trace output should be:

```text
net-force(p, t) = -k*x
inertial-acceleration(p) = -k*x/m
```

But the success criterion is not the formula. The success criterion is whether
the trace shows:

- where the spring instance entered mechanical-composition;
- where endpoint slots were filled;
- where `k` entered as a parameter;
- where equilibrium/displacement entered as constructs;
- where the ideal-linear-spring modelling assumption landed;
- how the abstract acting-object triplet dispatched to concrete spring entries.
