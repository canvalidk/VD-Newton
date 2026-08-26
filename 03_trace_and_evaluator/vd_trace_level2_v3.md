# VD Program Trace — Level 2 (v3, Lazy Evaluation)

> **Force-Sum compatibility notice — 2026-08-26:** this trace predates the
> ratified `net-force / impressed-force / interaction-set` naming and still
> models the old set as containing impressed-force elements. Use it for trace
> mechanics only. Its Force-Sum passages require a later semantic rewrite in
> which the interaction set contains interactions and each interaction supplies
> a target-directed impressed force.

## Exercise

An Atwood machine: two masses m₁ = 3 kg and m₂ = 5 kg are connected by a massless, inextensible string over a frictionless pulley. Find the acceleration of each mass and the tension in the string.

---

## Evaluation model

This trace treats the VD as a lazy functional program. Evaluation is demand-driven: we start with the goal expression and reduce it. Each subexpression is only evaluated when something upstream needs its value. No eager setup, no pre-loading of scaffold — everything fires on demand.

The notation:

- **EVAL** — the evaluator attempts to reduce an expression to a value.
- **DEMANDS** — the expression contains a headword that must be resolved before evaluation can continue.
- **→ human** — the evaluator reaches a point where it cannot proceed without external input. The reduction is suspended until the human supplies a value.
- **BLOCKED** — the evaluator cannot reduce an expression because a subexpression is stuck on unresolved input.

---

## The Trace

### EVAL: `inertial-acceleration(m₁)`

The exercise asks for the acceleration of each mass. We begin with m₁.

**Resolve `inertial-acceleration`:** Two definitions exist.

E20 (chimney): "The acceleration of a **point-particle** as measured in an **inertial-frame**."

E21 (triplet): "For a **point-particle**, inertial-acceleration equals **net-force** divided by **inertial-mass**: a = F/m."

E20 gives the type signature. E21 gives the computation rule. Both demand the same preconditions: the object must be a `point-particle` and the measurement must be in an `inertial-frame`. The evaluator encounters these headwords and must resolve them before it can apply the computation rule.

---

### DEMAND 1: "m₁ is a `point-particle`"

E20 and E21 both require the argument to be a `point-particle`. The evaluator must verify this.

**Resolve `point-particle`:** E3 — "An idealised object whose spatial extent and internal structure are neglected."

This is a `raw-class` (E28). To check membership, the evaluator invokes the meta-typing subroutine:

**E28** (procedure): check whether the object possesses the `class-specific-features`.

**E29** (features): for C = `point-particle`, the features are E3's definition — spatial extent and internal structure neglected.

**E30** (result): if recognised, treat as `instance-of`.

```
META-TYPING  (demanded by E20)
  class    :=  point-particle (E3)
  object   :=  m₁
  features :=  "spatial extent and internal structure neglected"
  → human:    Does m₁ have these features?
  response :=  YES (the block's size is negligible for this problem)
  result   :=  m₁ is instance-of point-particle  ✓
```

Demand satisfied. The evaluator continues.

---

### DEMAND 2: "measured in an `inertial-frame`"

E20 requires the acceleration to be measured in an `inertial-frame`. The evaluator must verify that the reference frame in use is one.

**Resolve `inertial-frame`:** E16 (triplet) — "A **reference-frame** in which every **free-particle** exhibits **uniform-motion**."

The evaluator must check this criterion against the lab frame. Note what this demands: the *concept* of `free-particle` and `uniform-motion`. It does NOT demand checking whether m₁ specifically is a free-particle — it demands a universal quantifier about all free-particles in this frame.

**Resolve `free-particle`** (demanded by E16's definition):

E17: "A **point-particle** that, when described in an **inertial-frame**, exhibits **uniform-motion**."
E19 (wall): "A **point-particle** not subject to external influence relevant to its motion."

**Resolve `uniform-motion`** (demanded by E16's definition):

E14 (chimney): "The state of being either stationary or moving along a **straight-line** with constant **speed**."

The evaluator now has enough to check E16:

```
META-TYPING  (demanded by E20)
  class    :=  inertial-frame (E16)
  object   :=  the lab frame (origin at pulley, y up)
  features :=  "every free-particle exhibits uniform-motion in it"
  → human:    Does the lab frame satisfy this?
  response :=  YES (approximately; modelling commitment)
  result   :=  lab frame is instance-of inertial-frame  ✓
```

**Note what did NOT happen.** The evaluator did not check whether m₁ is a free-particle. Nothing in the demand chain asked that question. The free-particle concept was needed only to *define* what an inertial frame is — not to classify the ball. In v1 and v2, I eagerly checked "is m₁ free?" as Step 3. In strict lazy evaluation, that check never fires, because nothing demands it. Newton II applies to all point-particles, free or not. If net-force happens to be zero, the acceleration is zero — consistent with uniform motion, but you don't need to check that in advance.

**This is a genuine finding: Newton I and Newton II are parallel branches, not sequential.** Newton I defines inertial-frame and free-particle; Newton II uses inertial-frame but never asks "is this particle free?" The free-particle check was physicist's habit, not program demand.

---

### APPLY E21: `inertial-acceleration(m₁) = net-force(m₁, t) / inertial-mass(m₁)`

Preconditions satisfied. The evaluator applies the computation rule and now demands two subexpressions:

---

### DEMAND 3: `inertial-mass(m₁)`

**Resolve `inertial-mass`:** E23 — "The positive scalar coefficient m such that **net-force** = m × **inertial-acceleration** for a **point-particle**."

E23 defines the type. The numerical value is empirical input:

```
BIND  inertial-mass(m₁)
  → human:    What is the inertial-mass of m₁?
  response := 3 kg  (given by the problem statement)
```

---

### DEMAND 4: `net-force(m₁, t)`

**Resolve `net-force`:** Two definitions exist.

E22 (triplet): "The vector quantity satisfying **net-force** = **inertial-mass** × **inertial-acceleration**." — This is a type-definition, not a computation rule.

E24 (Force Sum, triplet redefine): "**net-force** on particle p at time t is the vector sum of the **impressed-force** elements in the **interacting-forces-set** for p at t." — This is the computation rule.

The evaluator applies E24:

```
EVAL: net-force(m₁, t) = Σ { f : f ∈ interacting-forces-set(m₁, t) }
```

---

### DEMAND 5: `interacting-forces-set(m₁, t)`

**Resolve `interacting-forces-set`:** E25 — "The set of **impressed-force** elements taken to be acting on particle p at time t, whose vector sum is the **net-force** on p at t."

E25 declares the type but does not prescribe how to populate it. The evaluator must request the set contents:

```
POPULATE  interacting-forces-set(m₁, t)
  → human:    What impressed-forces act on m₁?
  response := { F_gravity_1, F_tension_1 }
```

Each element must satisfy the type `impressed-force` (E26: "A vector force-contribution that appears as an element of some **interacting-forces-set** and thereby contributes to the **net-force**"). Both qualify.

---

### DEMAND 6: numerical values of each `impressed-force`

The evaluator needs to sum the impressed-forces. Each must reduce to a vector value.

**F_gravity_1:** The evaluator needs a numerical value for this force.

The Action-Reaction law (E31) tells us every impressed-force is either a `canonical-force_acting-object` or a `reaction-force_acting-object`. The Acting Object architecture (E34–E36) tells us each comes from an `acting-object` with an `activation-condition` and a `canonical-force`.

```
EVAL: F_gravity_1

  DEMAND: classify per E31
    F_gravity_1 is a canonical-force_acting-object

  DEMAND: identify the acting-object per E34
    → human:  What acting-object produces this force?
    response: Earth's gravitational interaction with m₁

    META-TYPING  (demanded by E34)
      class    :=  acting-object (E34)
      features :=  "equipped with activation-condition and canonical-force"
      object   :=  Earth-gravity-m₁ interaction
      → human:    Does it have these features?
      response := YES

  DEMAND: activation-condition per E35
    "If a point-particle fulfills the activation-condition, the canonical-force
     of that acting-object will be an impressed-force on the point-particle."
    → human:  What is the activation-condition?
    response: "m₁ has nonzero mass and is in Earth's gravitational field"
    → human:  Does m₁ satisfy it?
    response: YES

  DEMAND: canonical-force per E36
    "The canonical-force is the impressed-force that an acting-object exerts on a
     point-particle that fulfills the activation-condition."
    → human:  What is the force value?
    response: F_gravity_1 = −m₁g ŷ = −29.4 N ŷ  (empirical: gravitational force law)

  DEMAND: paired-particle per E37
    "Each acting-object carries an associated particle, its paired-particle."
    → human:  What is the paired-particle?
    response: the Earth

  VALUE: F_gravity_1 = −29.4 N ŷ  ✓
```

**F_tension_1:** Same demand chain.

```
EVAL: F_tension_1

  DEMAND: acting-object per E34
    → human:  What acting-object produces this force?
    response: string-contact mechanism at m₁'s end

    META-TYPING (E28–E30): YES, it's instance-of acting-object

  DEMAND: activation-condition per E35
    → human: "m₁ is attached to the string" — satisfied? YES

  DEMAND: canonical-force per E36
    → human:  What is the force value?
    response: F_tension_1 = +T ŷ    ... but T is UNKNOWN

  *** BLOCKED ***
  The evaluator cannot reduce F_tension_1 to a numerical value.
  T is an unresolved symbol with no entry and no empirical value supplied.
```

---

### BLOCKED: `net-force(m₁, t)` cannot be evaluated

The sum F_gravity_1 + F_tension_1 = (−29.4 + T) ŷ contains the unresolved symbol T.

```
net-force(m₁, t) = (−29.4 + T) ŷ     [BLOCKED on T]
inertial-acceleration(m₁) = (−29.4 + T) / 3  ŷ     [BLOCKED on T]
```

The evaluator cannot return a value for the original goal. It has reduced as far as it can — the expression is in a partially-evaluated form with a free variable.

---

### The evaluator tries the second particle

The exercise asks for the acceleration of *each* mass. Perhaps evaluating the second particle will resolve T.

**EVAL: `inertial-acceleration(m₂)`**

The same demand chain fires. I'll compress since the structure is identical:

```
DEMAND: m₂ is point-particle         → human: YES
        (inertial-frame already verified — the evaluator can reuse the result)

APPLY E21: inertial-acceleration(m₂) = net-force(m₂, t) / inertial-mass(m₂)

DEMAND: inertial-mass(m₂)            → human: 5 kg

DEMAND: net-force(m₂, t) via E24     → sum of interacting-forces-set(m₂, t)

DEMAND: interacting-forces-set(m₂, t)
  → human: { F_gravity_2, F_tension_2 }

EVAL F_gravity_2:
  acting-object: Earth-gravity-m₂
  canonical-force: −m₂g ŷ = −49.0 N ŷ
  paired-particle: the Earth
  VALUE: −49.0 N ŷ  ✓

EVAL F_tension_2:
  acting-object: string-contact at m₂'s end
  canonical-force: +T ŷ    ... T is STILL UNKNOWN

  *** BLOCKED ***
```

```
net-force(m₂, t) = (−49.0 + T) ŷ     [BLOCKED on T]
inertial-acceleration(m₂) = (−49.0 + T) / 5  ŷ     [BLOCKED on T]
```

Both particles are blocked on the same unresolved symbol. Evaluating the second particle did not resolve T — it produced a second equation with the same free variable.

---

### State of the evaluator: two blocked thunks

```
inertial-acceleration(m₁) = (T − 29.4) / 3  ŷ     [blocked]
inertial-acceleration(m₂) = (T − 49.0) / 5  ŷ     [blocked]
```

Two equations, three unknowns (a₁, a₂, T). The VD program has been reduced as far as it can go. The dependency graph has been fully walked — every entry that the goal expression demands has been invoked. And the evaluator is stuck.

**This is the moment when the physicist, not the program, must act.**

---

### Why is the evaluator stuck?

The evaluator is stuck because the two Newton II calls share a free variable (T) that is not determined by any entry in the VD. The Force Sum law (E24) decomposes net-force into a sum of impressed-forces, and the Acting Object architecture (E34–E37) traces each force to its source — but the *magnitude* of the tension is not given by any force law entry. Unlike gravity (where the human supplied F = −mg from empirical knowledge), the tension is a *constraint force* whose value is determined by the coupled dynamics, not by an independent force law.

The physicist recognises this and asks: *why* are the equations underdetermined? Is something missing from the force accounting, or is the system fundamentally open?

**This is where the physicist invokes the closure machinery — not because the demand chain requires it, but because the evaluator is stuck and the physicist needs a diagnostic.**

---

### DIAGNOSTIC: Is S = {m₁, m₂} a `mechanically-closed-system`?

This is a new evaluation root — a separate question from the original goal. The physicist asks it because the computation is stuck, not because any entry in the Newton II → Force Sum chain demanded it.

**Invoke E38** (`mechanical-system`): "An arbitrary subset of particles selected by the observer for analysis."

```
DEFINE  S = {m₁, m₂}    (the physicist's choice)
```

**Invoke E39** (chimney for `interaction-candidate`): "For a particle p in a **mechanical-system** S at time t, an **interaction-candidate** is any **impressed-force** in the **interacting-forces-set** for p at t."

```
ENUMERATE  interaction-candidates for S:
  From m₁: { F_gravity_1, F_tension_1 }
  From m₂: { F_gravity_2, F_tension_2 }
  Total: 4 interaction-candidates
```

**Invoke E40–E42** (closure triplet):

E40: "An **interaction-candidate** is an elementary force-unit, every one of which must be able to be placed in an **interaction-pair** for the **mechanical-system** to be a **mechanically-closed-system**."

E42: "A **mechanically-closed-system** is a **mechanical-system** in which every **interaction-candidate** can be placed in an **interaction-pair**."

**Invoke E43** (pairing rule): "Two **interaction-candidate**s form an **interaction-pair** when they correspond to the same **acting-object**, one being the **canonical-force_acting-object** and the other being the **reaction-force_acting-object**, the latter exerted on the **paired-particle_acting-object**."

Attempt to pair each interaction-candidate:

| Interaction-candidate | Acting-object | Reaction force | Lands on | In S? | Pairs? |
|---|---|---|---|---|---|
| F_gravity_1 (on m₁) | Earth-grav-m₁ | +m₁g ŷ | Earth | NO | **NO** |
| F_tension_1 (on m₁) | String-contact-m₁ | −T ŷ | string-pulley | NO | **NO** |
| F_gravity_2 (on m₂) | Earth-grav-m₂ | +m₂g ŷ | Earth | NO | **NO** |
| F_tension_2 (on m₂) | String-contact-m₂ | −T ŷ | string-pulley | NO | **NO** |

**Result: 0/4 pair. S is NOT a mechanically-closed-system.**

**Invoke E44** (residual): "A **mechanically-closed-system** is a **mechanical-system** whose future behaviour is determined by the equations produced from the interactions internal to it."

Contrapositive: S's future behaviour is **not** determined by the internal equations alone. This is exactly the situation the evaluator is in — two equations, three unknowns, no way to reduce further.

---

### The diagnostic explains the blockage

The closure check has done two things:

**First**, it has systematically identified *where* the system leaks. Four reaction forces leave S — two to the Earth, two to the string-pulley assembly. These are the external connections.

**Second**, it has explained *why* the evaluator is stuck. The tension T is a constraint force mediated by the string-pulley assembly, which is external to S. Its value cannot be determined from the internal equations because the mechanism that determines it (the massless inextensible string) is not represented in S.

The physicist must now respond to the diagnostic. For each leak, they either expand S or justify why the leak doesn't matter:

---

### HUMAN RESPONSE TO DIAGNOSTIC

**Leak 1–2: Gravity reactions land on Earth.**

```
→ human:  The Earth receives reactions +m₁g and +m₂g. Its acceleration
          would be (m₁+m₂)g / M_Earth ≈ 10⁻²³ m/s². This is negligible.
          Gravity can be treated as a known external input: F = −mg ŷ.
```

This doesn't help with T — we already had the gravity values.

**Leak 3–4: Tension reactions land on the string-pulley assembly.**

The physicist must now confront the string-pulley mechanism. The string is massless; the pulley is frictionless; the bracket is bolted to the wall.

```
→ human:  The string is massless. If it had nonzero net force, it would
          have infinite acceleration (F/m = F/0). Therefore the net force
          on the string must be zero at every instant.
```

This constraint is powerful. The string receives:
- −T ŷ from m₁ (reaction of acting-object #3)
- −T ŷ from m₂ (reaction of acting-object #4)
- A support force from the pulley bracket

For the string's net force to be zero, the tensions at both ends must be equal (by symmetry of the frictionless pulley). So T₁ = T₂ = T. We already assumed this — but now it's *justified* by the closure diagnostic rather than silently imported.

```
→ human:  The string is inextensible. When m₁ moves up by Δy, m₂ moves
          down by Δy. Therefore a₁ = −a₂.
```

**The closure failure has extracted two constraints from the physicist:**

1. T₁ = T₂ = T (from masslessness of string)
2. a₁ = −a₂ (from inextensibility of string)

These are precisely the missing equations that unblock the evaluator.

---

### Resume evaluation

The human has supplied two constraints. The evaluator can now reduce:

Let a = a₁ (positive upward for m₁). Then a₂ = −a.

```
From the blocked thunk for m₁:   3a  = T − 29.4     ... (i)
From the blocked thunk for m₂:   5(−a) = T − 49.0   ... (ii)
```

Two equations, two unknowns. The evaluator can now complete the reduction:

```
From (i):  T = 3a + 29.4
From (ii): T = 49.0 − 5a

3a + 29.4 = 49.0 − 5a
8a = 19.6
a = 2.45 m/s²

T = 3(2.45) + 29.4 = 36.75 N
```

### RETURN

```
inertial-acceleration(m₁) = +2.45 m/s² ŷ   (upward)
inertial-acceleration(m₂) = −2.45 m/s² ŷ   (downward)
tension T = 36.75 N
```

---

## The complete demand tree

```
GOAL: inertial-acceleration(m₁)                          [E21]
│
├─ DEMANDS: m₁ is point-particle                         [E3 via E28-E30]
│    └─ → human: recognition (YES)
│
├─ DEMANDS: frame is inertial-frame                       [E16 via E28-E30]
│    ├─ DEMANDS: concept of free-particle                 [E17, E19]
│    ├─ DEMANDS: concept of uniform-motion                [E14]
│    └─ → human: recognition (YES, approximate)
│
├─ DEMANDS: inertial-mass(m₁)                             [E23]
│    └─ → human: 3 kg (given)
│
└─ DEMANDS: net-force(m₁, t)                              [E24]
     └─ DEMANDS: interacting-forces-set(m₁, t)           [E25]
          ├─ → human: { F_gravity_1, F_tension_1 }
          │
          ├─ EVAL F_gravity_1                              [E31→E34→E35→E36→E37]
          │    ├─ acting-object: Earth-gravity-m₁          [E34 via E28-E30]
          │    ├─ canonical-force: −29.4 N ŷ               [E36, → human: force law]
          │    ├─ paired-particle: Earth                    [E37, → human]
          │    └─ VALUE: −29.4 N ŷ  ✓
          │
          └─ EVAL F_tension_1                              [E31→E34→E35→E36→E37]
               ├─ acting-object: string-contact-m₁         [E34 via E28-E30]
               ├─ canonical-force: +T ŷ                    [E36, → human: T unknown]
               ├─ paired-particle: string-pulley            [E37, → human]
               └─ *** BLOCKED on T ***


GOAL: inertial-acceleration(m₂)                           [parallel evaluation]
│
└── ... (same structure, also BLOCKED on T)


EVALUATOR STATE: two thunks blocked on shared free variable T
                 two equations, three unknowns


DIAGNOSTIC: is S = {m₁, m₂} mechanically closed?          [separate root]
│
├─ E38: define S                    → human: S = {m₁, m₂}
├─ E39: enumerate candidates        → 4 interaction-candidates
├─ E40-E42: attempt pairing         → 0/4 pair
├─ E43: pairing rule applied        → all reactions land outside S
├─ E44: consequence                 → internal equations insufficient
│
└─ HUMAN RESPONSE TO FAILURE:
     ├─ Earth: negligible acceleration          → gravity is known input
     ├─ String: massless → equal tensions       → T₁ = T₂ = T
     ├─ String: inextensible → coupling         → a₁ = −a₂
     └─ Wall: doesn't accelerate                → pulley stationary


CONSTRAINTS SUPPLIED → T determined → thunks unblock → VALUES RETURN
```

---

## Structural findings

### 1. The free-particle check drops out entirely

In v1 and v2, I checked "is m₁ a free-particle?" as an explicit step. In lazy evaluation, this check is never demanded. Nothing in the Newton II chain asks whether the particle is free. Newton II applies to all point-particles — if the net-force happens to be zero, the acceleration is zero.

The free-particle concept *is* demanded, but only as a dependency of `inertial-frame` (E16: "a reference-frame in which every **free-particle** exhibits uniform-motion"). It's needed to *define* the measurement context, not to *classify* the object being measured.

**Implication for the VD:** Newton I and Newton II are parallel branches in the dependency graph, not sequential. The physicist's habit of "first check Newton I, then apply Newton II" is a heuristic, not a program demand. This is clean — it means Newton II doesn't have a hidden precondition that the entries fail to encode.

### 2. Closure is a separate evaluation root, not a demanded dependency

No entry in the Newton II → Force Sum → Acting Object chain references `interaction-candidate`, `mechanical-system`, or `mechanically-closed-system`. There is no dependency edge from the computation to the closure check. The closure machinery lives in a disconnected component of the demand graph.

The physicist invokes closure not because the program demands it, but because the evaluator is stuck. The blocked thunks are the symptom; closure is the diagnostic tool. In programming terms, closure is like a debugger, not a subroutine — you reach for it when execution can't proceed.

**Implication for the VD:** Should there be a dependency edge from the computation chain to the closure check? If the VD is meant to be a complete program, then the fact that the evaluator can get stuck without any entry telling it *why* is arguably a gap. The program could include an entry somewhere in the Force Sum or Newton II chain that says something like: "the equations produced by Newton II for all particles in a mechanical-system are solvable if and only if the system is a mechanically-closed-system." That would create a demand edge from Newton II to closure, making the diagnostic part of the normal evaluation path rather than a separate debugging tool.

### 3. The evaluator gets stuck on shared free variables, not missing definitions

The blockage is not "I don't know what `tension` means" — it's "I know what tension is (a canonical-force from a string-contact acting-object) but I don't know its numerical value." The VD has successfully reduced the expression as far as the *definitions* allow. What's missing is *data*: the value of T, which depends on constraints external to S.

This is a clean separation. The VD provides the *algebraic structure* (every force is an impressed-force from an acting-object; the net-force is their sum; the acceleration is net-force / mass). The external inputs provide the *numerical content* (the force law for gravity, the constraint equations for the string). The evaluator reduces the algebra and then blocks on the numerics.

### 4. Closure failure produces the missing constraints

When the physicist runs the closure diagnostic, the failure report points to specific leaks: reaction forces that land outside S. Confronting each leak forces the physicist to model the external object and justify an approximation. The constraints that unblock the evaluator (equal tensions, kinematic coupling) emerge as *consequences* of these justifications.

In v2, I presented this correctly but with the wrong sequencing — the closure check ran before the evaluator got stuck. In v3, the sequencing is honest: the evaluator gets stuck first, the physicist invokes closure to diagnose the blockage, and the closure failure generates the constraints that resolve it.

### 5. The for-each-particle iteration is not encoded

The VD defines Newton II for "a point-particle" (singular). When there are two particles, the physicist recognises that Newton II applies to each independently and evaluates both. This iteration is not prescribed by any entry — the program says what Newton II does for one particle, and the human recognises that it should be applied to all of them.

In Haskell, this would be a `map` operation: `map newtonII particles`. The VD has no equivalent of `map`. This is arguably fine — the VD is a declarative language, not an imperative one, and "apply this definition to each relevant object" is a natural enough operation that encoding it explicitly might be overengineering. But a logic tracker would need to handle it.

---

## Human inputs: final taxonomy

| # | Kind | What | Demanded by | 
|---|------|------|-------------|
| 1 | Recognition | m₁ is point-particle | E20 → E3 via E28-E30 |
| 2 | Recognition | m₂ is point-particle | E20 → E3 via E28-E30 |
| 3 | Recognition | Lab frame is inertial-frame | E20 → E16 via E28-E30 |
| 4 | Recognition | Earth-grav-m₁ is acting-object | E34 via E28-E30 |
| 5 | Recognition | String-contact-m₁ is acting-object | E34 via E28-E30 |
| 6 | Recognition | Earth-grav-m₂ is acting-object | E34 via E28-E30 |
| 7 | Recognition | String-contact-m₂ is acting-object | E34 via E28-E30 |
| 8 | Modelling | IFS(m₁) = {gravity, tension} | E25 |
| 9 | Modelling | IFS(m₂) = {gravity, tension} | E25 |
| 10 | Modelling | S = {m₁, m₂} | E38 (physicist's diagnostic choice) |
| 11 | Empirical | F_gravity = −mg ŷ | E36 |
| 12 | Empirical | Paired-particle of gravity = Earth | E37 |
| 13 | Empirical | Paired-particle of string-contact = string-pulley | E37 |
| 14 | Closure-forced | Earth's acceleration negligible | Closure failure (E42/E44) |
| 15 | Closure-forced | Equal tensions (massless string) | Closure failure |
| 16 | Closure-forced | Kinematic coupling (inextensible string) | Closure failure |
| 17 | Closure-forced | Wall doesn't accelerate | Closure failure |

Every human input now has a "demanded by" attribution — either to a specific entry that needed the information, or to the closure failure diagnostic. Nothing is supplied eagerly.

---

## Comparison: v1 → v2 → v3

| Aspect | v1 | v2 | v3 |
|--------|----|----|-----|
| Evaluation model | Physics-first, entries as labels | Entry-driven, but eager | Lazy, demand-driven |
| Free-particle check | Explicit step | Explicit step | **Drops out entirely** |
| Closure | Not invoked | Invoked before equations | **Invoked when evaluator blocks** |
| Why closure fires | N/A | Because the trace says to | **Because the evaluator is stuck on T** |
| Constraint extraction | Imported from physics | Forced by closure failure | **Forced by closure failure, demanded by blocked thunks** |
| Human inputs | Retrospective list | Categorised | **Each attributed to demanding entry** |
| Meta-typing | Implicit | Explicit, but eager | **On-demand, fires when precondition is checked** |
| Control flow | Physicist's narrative | Physicist's narrative | **Emergent from demand propagation** |
