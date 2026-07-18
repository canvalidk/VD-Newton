# VD Newton Trace - Sliding Block on Incline (v1)

## Exercise

A block of inertial mass `m` slides down a fixed incline of angle `theta`.
The coefficient of kinetic friction is `mu_k`. Find the block's
inertial-acceleration.

This trace uses the Newton v0.6 entry numbering and treats the scenario as
declared through mechanical-compositions. It also tests the half-interaction
accounting hypothesis for paired acting-objects: each side of a two-particle
interaction contributes half the ordinary interaction magnitude, and the force
on a particle is recovered as the sum of the canonical contribution from the
other side plus the reaction contribution from its own side.

## Evaluation Model

The trace is lazy and demand-driven. It starts from the goal expression and
expands only what is demanded. Whenever expansion reaches a fully residual
entry, the trace records a human/viewer input rather than silently filling it.

Entry roles used here:

- E20: chimney for `inertial-acceleration`
- E21-E23: Newton II triplet
- E24-E26: Force Sum triplet
- E27-E30: meta-typing triplet
- E31-E36: action-reaction and acting-object architecture
- E37: `mechanical-composition_point-particle`
- E38: `paired-particle_acting-object`
- E39-E45: mechanical-system and closure machinery

## GOAL

```
EVAL: inertial-acceleration(block)
```

The textbook phrase "acceleration of the block" is normalised by the viewer as
`inertial-acceleration(block)`.

```
HUMAN INPUT
  kind: normalisation
  demanded by: exercise wording before VD lookup
  response: query headword is inertial-acceleration(block)
```

## Resolve `inertial-acceleration`

Two entries are relevant.

E20 gives the type/precondition shape:

```
inertial-acceleration = acceleration of a point-particle measured in an
inertial-frame
```

E21 gives the computation rule:

```
inertial-acceleration = net-force / inertial-mass
```

Before E21 can be used, E20 demands that the block be treated as a
`point-particle` and that the measurement frame be an `inertial-frame`.

### DEMAND 1: `block is point-particle`

Resolve `point-particle` through E3, then apply meta-typing E27-E30.

```
META-TYPING
  class: point-particle
  object: block
  features source: E3
  features: spatial extent and internal structure are neglected

HUMAN INPUT
  kind: recognition
  demanded by: E20 via E3 and E27-E30
  response: YES; the block is idealised as a point-particle for translation
            along the incline
```

Demand satisfied.

### DEMAND 2: `frame is inertial-frame`

Resolve `inertial-frame` through E16 and E18, then apply meta-typing E27-E30.
The definition invokes the concepts `reference-frame`, `free-particle`, and
`uniform-motion`, but the block itself is not checked as a free-particle.

```
META-TYPING
  class: inertial-frame
  object: lab frame fixed to Earth/incline
  features source: E16, grounded by E18
  features: every free-particle exhibits uniform-motion in this frame

HUMAN INPUT
  kind: recognition / modelling approximation
  demanded by: E20 via E16/E18 and E27-E30
  response: YES approximately; the Earth/incline frame is treated as inertial
            for this problem
```

Demand satisfied.

## APPLY E21

```
inertial-acceleration(block) =
    net-force(block, t) / inertial-mass(block)
```

This creates two sub-demands.

## DEMAND 3: `inertial-mass(block)`

Resolve `inertial-mass` through E23. The entry gives the role of inertial mass
inside Newton II, but not this block's numerical value.

```
HUMAN INPUT
  kind: empirical / given parameter
  demanded by: E23
  response: inertial-mass(block) = m
```

## DEMAND 4: `net-force(block, t)`

Resolve `net-force`.

E22 gives the Newton II relational definition. E24 gives the force-sum
computation rule:

```
net-force(block, t) =
    sum of acting-force elements in interacting-forces-set(block, t)
```

So the evaluator demands the interacting-forces-set.

## DEMAND 5: `interacting-forces-set(block, t)`

E25 declares the set but does not populate it. In the v0.6 architecture, the
scenario inventory is declared through `mechanical-composition_point-particle`
(E37). The current E25 text does not yet contain a direct dependency edge to
E37, so the viewer bridges E25 to E37 as a modelling act.

```
HUMAN INPUT
  kind: modelling
  demanded by: E25, with Design-3-style use of E37
  response: populate the relevant scenario mechanical-compositions with
            paired acting-object instances for:
            1. Earth-block gravity
            2. block-incline normal contact
            3. block-incline kinetic friction
```

### Mechanical-composition declarations

The viewer declares the following acting-object instances.

For gravity:

```
mechanical-composition(Earth) includes G_Earth
mechanical-composition(block) includes G_block
```

`G_Earth` is the Earth-side gravity acting-object. Its canonical-force acts on
the block. `G_block` is the block-side gravity acting-object. Its
reaction-force acts on the block.

For normal contact:

```
mechanical-composition(incline) includes N_incline
mechanical-composition(block) includes N_block
```

For kinetic friction:

```
mechanical-composition(incline) includes K_incline
mechanical-composition(block) includes K_block
```

Each declaration is a residual scenario declaration: there is no scenario
object behind it.

```
HUMAN INPUT
  kind: modelling / scenario declaration
  demanded by: E37
  response: the above six acting-object instances are the scenario inventory
```

The interacting-forces-set on the block is then:

```
interacting-forces-set(block, t) = {
  canonical-force(G_Earth on block),
  reaction-force(G_block on block),
  canonical-force(N_incline on block),
  reaction-force(N_block on block),
  canonical-force(K_incline on block),
  reaction-force(K_block on block)
}
```

This is the point where the half-interaction hypothesis enters: the ordinary
force associated with a two-sided interaction is recovered by summing the
canonical contribution from the other side and the reaction contribution from
the local side.

## Coordinate decomposition

The force sum is vector-valued. The Newton entries currently provide vectors
but do not encode a projection/component calculus for an incline basis. The
viewer chooses an adapted basis.

```
HUMAN INPUT
  kind: modelling / viewer coordinate choice
  demanded by: vector summation in E24
  response: use unit axis s down the plane and unit axis n outward normal
            to the plane
```

## EVAL acting-force elements

### 1. Gravity contribution from `G_Earth`

Resolve via E31-E36.

```
EVAL: canonical-force_acting-object(G_Earth on block)

META-TYPING
  class: acting-object
  object: G_Earth
  features source: E34
  features: equipped with activation-condition and canonical-force

HUMAN INPUT
  kind: recognition
  demanded by: E34 via E27-E30
  response: YES; G_Earth is the Earth-side gravity acting-object
```

Activation and force rule:

```
HUMAN INPUT
  kind: empirical / acting-object rule
  demanded by: E35-E36
  response: if the target point-particle is massive and in Earth's
            near-surface gravitational field, G_Earth contributes
            0.5*m*g downward to that target
```

Therefore:

```
canonical-force(G_Earth on block)
  = 0.5*m*g*sin(theta) s - 0.5*m*g*cos(theta) n
```

### 2. Gravity contribution from `G_block`

The block-side gravity acting-object has a canonical-force on Earth. The force
on the block is the reaction-force associated with that acting-object.

```
EVAL: reaction-force_acting-object(G_block on block)
```

Meta-typing and activation are analogous to `G_Earth`.

```
HUMAN INPUT
  kind: recognition
  demanded by: E34 via E27-E30
  response: YES; G_block is the block-side gravity acting-object

HUMAN INPUT
  kind: empirical / acting-object rule
  demanded by: E35-E36
  response: G_block's canonical-force on Earth has magnitude 0.5*m*g upward;
            its reaction on the block is 0.5*m*g downward
```

Therefore:

```
reaction-force(G_block on block)
  = 0.5*m*g*sin(theta) s - 0.5*m*g*cos(theta) n
```

Gravity subtotal on the block:

```
F_gravity_on_block =
    m*g*sin(theta) s - m*g*cos(theta) n
```

The half-interaction accounting recovers the ordinary block gravity term.

### 3. Normal contribution from `N_incline`

Normal contact is a constraint acting-object. Per the consolidation note, this
has the same fragment shape as producer forces: the canonical-force rule may
produce a fresh symbol rather than a closed-form value.

```
EVAL: canonical-force_acting-object(N_incline on block)

HUMAN INPUT
  kind: recognition
  demanded by: E34 via E27-E30
  response: YES; N_incline is the incline-side normal-contact acting-object

HUMAN INPUT
  kind: modelling / acting-object rule
  demanded by: E35-E36
  response: while the block satisfies the no-penetration contact condition,
            N_incline contributes +0.5*N n to the block
```

So:

```
canonical-force(N_incline on block) = +0.5*N n
```

### 4. Normal contribution from `N_block`

The local block-side normal acting-object contributes to the block through its
reaction-force.

```
EVAL: reaction-force_acting-object(N_block on block)

HUMAN INPUT
  kind: recognition
  demanded by: E34 via E27-E30
  response: YES; N_block is the block-side normal-contact acting-object

HUMAN INPUT
  kind: modelling / acting-object rule
  demanded by: E35-E36
  response: N_block's reaction on the block contributes +0.5*N n
```

So:

```
reaction-force(N_block on block) = +0.5*N n
```

Normal subtotal:

```
F_normal_on_block = +N n
```

`N` remains a fresh constraint symbol.

### 5. Kinetic friction contribution from `K_incline`

Kinetic friction is a contact acting-object whose canonical-force rule refers
to the normal-contact magnitude and the parameter `mu_k`.

```
EVAL: canonical-force_acting-object(K_incline on block)

HUMAN INPUT
  kind: recognition
  demanded by: E34 via E27-E30
  response: YES; K_incline is the incline-side kinetic-friction acting-object

HUMAN INPUT
  kind: modelling / activation condition
  demanded by: E35
  response: block is sliding down the incline relative to the surface, so
            kinetic friction is active and points up the incline

HUMAN INPUT
  kind: parameter
  demanded by: E36's friction rule
  response: coefficient of kinetic friction is mu_k
```

The current Newton entries do not encode the kinetic-friction force law, so the
viewer supplies it at the acting-object rule wall.

```
HUMAN INPUT
  kind: empirical / acting-object rule
  demanded by: E36
  response: total kinetic friction magnitude is mu_k*N; in half-interaction
            accounting this side contributes 0.5*mu_k*N up the incline
```

Thus:

```
canonical-force(K_incline on block) = -0.5*mu_k*N s
```

### 6. Kinetic friction contribution from `K_block`

```
EVAL: reaction-force_acting-object(K_block on block)

HUMAN INPUT
  kind: recognition
  demanded by: E34 via E27-E30
  response: YES; K_block is the block-side kinetic-friction acting-object

HUMAN INPUT
  kind: empirical / acting-object rule
  demanded by: E36
  response: K_block's reaction on the block contributes 0.5*mu_k*N up
            the incline
```

So:

```
reaction-force(K_block on block) = -0.5*mu_k*N s
```

Friction subtotal:

```
F_friction_on_block = -mu_k*N s
```

## Apply force sum E24

Summing all elements of `interacting-forces-set(block, t)` gives:

```
net-force(block, t)
  = (m*g*sin(theta) - mu_k*N) s
    + (N - m*g*cos(theta)) n
```

Then E21 gives:

```
inertial-acceleration(block)
  = [(m*g*sin(theta) - mu_k*N) / m] s
    + [(N - m*g*cos(theta)) / m] n
```

At this point the evaluator is blocked on the fresh constraint symbol `N`.

```
BLOCKED THUNK
  expression:
    inertial-acceleration(block)
      = (g*sin(theta) - mu_k*N/m) s
        + (N/m - g*cos(theta)) n
  free variable:
    N
```

## Constraint response

The block is sliding along the incline while remaining in contact with it.
The normal-contact acting-object routes demand sideways to the motion of the
contact surface, but the current Newton entries do not encode contact-surface
constructs or no-penetration as a law-house. The viewer supplies the constraint
at this residual wall.

```
HUMAN INPUT
  kind: closure/constraint-forced modelling
  demanded by: blocked normal-contact symbol N
  response: the incline is fixed and the block remains in contact with the
            surface; therefore the block has no acceleration normal to the
            incline:
            inertial-acceleration(block) dot n = 0
```

So:

```
(N - m*g*cos(theta)) / m = 0
N = m*g*cos(theta)
```

Substitute into the blocked thunk:

```
inertial-acceleration(block)
  = [g*sin(theta) - mu_k*g*cos(theta)] s
```

## RETURN

```
inertial-acceleration(block)
  = g*(sin(theta) - mu_k*cos(theta)) s
```

where `s` points down the incline.

## Demand Tree Summary

```
GOAL: inertial-acceleration(block)                         [E20/E21]
|
|-- DEMAND: block is point-particle                         [E3 via E27-E30]
|     `-- HUMAN INPUT: recognition YES
|
|-- DEMAND: frame is inertial-frame                         [E16/E18 via E27-E30]
|     `-- HUMAN INPUT: inertial-frame approximation YES
|
|-- DEMAND: inertial-mass(block)                            [E23]
|     `-- HUMAN INPUT: m
|
`-- DEMAND: net-force(block,t)                              [E24]
      `-- DEMAND: interacting-forces-set(block,t)           [E25]
            `-- HUMAN INPUT: populate via mechanical-compositions [E37]
                  |
                  |-- Gravity pair:
                  |     |-- canonical-force(G_Earth) = 0.5mg downward  [E31-E36]
                  |     `-- reaction-force(G_block) = 0.5mg downward   [E31-E36]
                  |
                  |-- Normal pair:
                  |     |-- canonical-force(N_incline) = +0.5N n       [E31-E36]
                  |     `-- reaction-force(N_block) = +0.5N n          [E31-E36]
                  |
                  `-- Friction pair:
                        |-- canonical-force(K_incline) = -0.5 mu_k N s [E31-E36]
                        `-- reaction-force(K_block) = -0.5 mu_k N s    [E31-E36]

BLOCKED on N
|
`-- HUMAN INPUT: no-penetration/fixed-incline constraint
      `-- N = m g cos(theta)

RETURN: a = g(sin(theta) - mu_k cos(theta)) s
```

## Findings

1. The half-interaction accounting is internally promising for gravity. Two
   0.5mg contributions recover the usual `mg` force on the block while leaving
   room for the Earth-side reaction accounting.

2. The same half-interaction pattern can be applied uniformly to normal force
   and kinetic friction: each two-sided interaction contributes half from the
   other side's canonical-force and half from the local side's reaction-force.

3. The trace still depends on a viewer bridge from E25
   `interacting-forces-set` to E37 `mechanical-composition_point-particle`.
   Design 3 probably needs to make this bridge explicit if mechanical-composition
   is the scenario declaration mechanism.

4. The current Newton instance does not yet encode contact-surface constructs,
   no-penetration, or kinetic-friction laws. Those enter as residual
   acting-object rules here.

5. The trace returns the correct textbook expression, but more importantly it
   returns an attributed equation system before solving:

   ```
   m*a_s = m*g*sin(theta) - mu_k*N
   m*a_n = N - m*g*cos(theta)
   a_n = 0
   ```

   The final answer is downstream of this trace output, not a replacement for
   it.
