# HISTORICAL TERMINOLOGY QUARANTINE

> **Do not use this file as naming authority.** It preserves an earlier state and may use obsolete force-member names. The sole active headword is `impressed-force`, governed by `08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`. Translate any predecessor force-member name to `impressed-force` before carrying content forward. Historical wording does not reopen the decision.

---
# Design 2.1 Conversation Entry Considerations - 2026-05-14

Status: conceptual capture from conversation. These are not final entries.

This note records proposed entry directions and design considerations raised
while preparing for Design 2.1. The purpose is to preserve the live conceptual
work before converting it into the main entry ledger.

## Global Orientation

### Physics Theory As String-Presentation Machinery

A physics theory can be treated as a collection of writings/strings which,
when thoroughly presented to a trained person, increases that person's
probability of predicting the future correctly.

The simulator should be read as a machine that presents strings to people. A
displayed string becomes a stimulant. A disciplined interpreter reacts to that
stimulant with behaviours learned from physics, mathematics, and ordinary
language. If the simulator presents the string that triggers the next behaviour
needed to compute Newton's theory, the interpreter becomes more likely to
produce a correct prediction.

This makes the VD a controlled combination of disciplined behaviours toward
strings.

### Wall Entry Purpose

The primary purpose of wall entries is to facilitate the algorithm of the
theory. A wall entry is not mainly a place to explain the whole concept. It is
a place to present a short string that induces useful recognition,
substitution, classification, measurement, or modelling behaviour at the right
point in the trace.

### Brevity And Induced Behaviour

Entry writing must balance:

- induced behaviour in the target audience;
- enough conceptual grip for ordinary physics intuition;
- enough precision to avoid wrong substitutions or wrong object commitments;
- brevity, so the entry system remains usable.

The current candidate entries are deliberately rough. The goal of this note is
to keep the considerations, not to pretend these are already good final
entries.

### Wall Entries Should Not Reference Triplets

Wall entries should not point back into triplet entries or name the law-block
role they serve. The simulator structure and shared headword already create
that connection. The wall should present peripheral/recognition-facing meaning
for the same headword.

Example: a `free-particle` wall should not say "for Newton I path reasoning."
The shared headword `free-particle` and the demand structure already create
that connection.

## Proposed / Discussed Wall Entries

### Inertial-Mass Wall

#### First Attempt

```text
Inertial mass := Value that represents this particles ressistance to
acceleration. Measured in kilograms, often using weights.
```

Notes on cleanup:

- `particles` should become `particle's`.
- `ressistance` should become `resistance`.
- "using weights" is a useful everyday measurement cue but risks conflating
  mass and weight.

#### Candidate Direction

```text
Inertial mass := Value representing this particle's resistance to acceleration;
measured in kilograms, often obtained by weighing or calibration.
```

#### Intended Behaviours

The wall should induce the interpreter to:

- replace `inertial-mass` with the correct mass value for the relevant
  particle;
- use kilograms;
- choose the target particle's mass, not another particle's mass or a total
  mass;
- keep the value symbolic, usually `m`, when no number has been supplied;
- relate statements like `3 kg = inertial-mass` back to measurement/model
  input when the trace needs provenance.

#### Open Wording Issue

We considered a computation-facing version:

```text
Inertial mass := This particle's mass value for Newton II; represents
resistance to acceleration, is measured in kilograms, and may be substituted
numerically or kept symbolic.
```

But the later wall-entry rule suggests avoiding explicit triplet/law
references such as "for Newton II" in the final wall wording.

### Net-Force Wall

#### Candidate Direction

```text
Net force := Total force vector on this particle, measured in newtons.
```

#### Intended Behaviours

The wall should induce the interpreter to:

- use the total force on the relevant particle;
- not confuse a single force contribution with the net force;
- preserve vector direction/component/sign information;
- use newtons;
- substitute a given result into the right slot, or keep it symbolic if no
  value is available.

#### Economy Note

The word `vector` is doing useful work. It is shorter than repeatedly saying
"with direction/sign included."

### Inertial-Acceleration Wall / Peripheral Treatment

The current six-entry layout gives Newton II wall slots to `net-force` and
`inertial-mass`, not obviously to `inertial-acceleration`. Still, a similar
peripheral treatment may be useful because users may be given an acceleration
result and need to substitute it correctly.

#### Candidate Direction

```text
Inertial acceleration := Acceleration vector of this particle in the chosen
inertial frame, measured in m/s^2.
```

#### Intended Behaviours

The treatment should induce the interpreter to:

- use the acceleration of the relevant particle;
- use the chosen inertial frame;
- preserve vector direction/component/sign information;
- use metres per second squared;
- substitute a given result into the right slot, or keep it symbolic if no
  value is available.

### Free-Particle Wall

#### Conceptual Correction

The free-particle wall was confusing before the Newton I correction. The
current conceptual direction is:

- a free particle is a particle with no relevant mechanical influence;
- massless particles such as photons also count as free particles;
- Newton II still has a separate mass boundary, so photons should not be
  routed through the Newton II force/mass pipeline.

One motivating thought: Newton I and Newton II together suggest that a
mechanically uninfluenced particle travels the path of photons. This remains
interesting even after Einstein, because photons remain free in the relevant
non-force/path sense.

#### Candidate Direction

```text
Free particle := Particle with no relevant mechanical influence; includes
massless particles such as photons.
```

#### Intended Behaviours

The wall should induce the interpreter to:

- classify mechanically uninfluenced massive particles as free particles;
- classify photons/massless particles as free particles;
- not treat `free-particle` as a command to enter the old `Nothing -> Newton I`
  route;
- keep the Newton II inertial-mass boundary visible elsewhere.

#### Important Wording Rule

Do not say "for Newton I path reasoning" in the wall. That imports the triplet
role into the wall wording. The shared headword and simulator structure should
make the connection.

## Attached-Force / Action-Reaction Area

### Attached-Force Wall

#### Working Thought

An `attached-force` is either an action force or a reaction force. Once one
side is attached to the target particle's force account, the other side needs
to "fizzle" for that target and belong elsewhere.

#### Rough Candidate

```text
Attached force := Force value attached to this particle's force account;
substitute the member of an action/reaction pair that acts on this particle.
```

This is not a final entry. It was a rough attempt to capture the useful
behaviour.

#### Intended Behaviours

The wall should induce the interpreter to:

- use the force contribution on this particle;
- not accidentally include the paired opposite in the same particle's force
  account;
- treat `attached` as attachment to the target particle's force account;
- leave room for the fact that an attached force later resolves as either
  action-side or reaction-side.

### Asymmetrical Information In Action And Reaction Forces

#### Core Idea

Knowing that an attached force is an action force or a reaction force gives
different information about the system. These are "asymmetrical forces" in the
sense that action-side and reaction-side force labels provide asymmetrical
information about the particles they involve.

#### Spring Example

If a particle has the action force of a spring on it:

- this tells us little about the particle beyond the fact that it must be
  fulfilling the spring conditions;
- it tells us that a spring exists in the model;
- that existence claim needs precise VD bookkeeping, not vague prose.

If a particle has the spring's reaction force on it:

- this suggests the particle has the spring in its mechanical-composition;
- it tells us that another particle must fulfill the spring activation
  conditions;
- it tells comparatively little else about this particle's own condition
  fulfilment.

#### Design Importance

This asymmetry will recur. It matters for:

- `attached-force`;
- `action-force`;
- `reaction-force`;
- `acting-object`;
- `activation-condition_acting-object`;
- `mechanical-composition_point-particle`;
- future witness-sheet/object commitments.

## Gravity / Electrical Halving

### Half-Interaction / Force-Halving Principle

#### Core Idea

Gravity and electrical forces introduce a special halving issue. This is not a
general rule for all action/reaction pairs.

Only consider halving when duplicate same-kind source acting-objects would
otherwise double-count the same physical interaction.

#### Gravity Case

For gravity, the proposal discussed was:

```text
half gravitational contribution = 1/2 * mg
```

To recover full gravity on a particle, the particle needs one action-side
half-force and one reaction-side half-force:

```text
action half-force + reaction half-force = full gravitational force
```

This means the ordinary textbook gravitational force `mg` is a compressed
result of paired half-contributions in the deeper bookkeeping.

#### Information Revealed By Halving And Doubling

Because the full gravitational force is recovered by halving and doubling, the
existence of the force `mg` tells us more than the ordinary notation suggests.

It tells us that:

- both particles of the interaction must have gravitational acting-object
  structure, i.e. gravitational fields or source roles;
- both particles must fulfill the gravitational conditions;
- in ordinary Newtonian terms, both particles must have mass.

This differs from the spring case. A spring action force on a particle tells us
that there is a spring and that the target fulfills spring conditions. A full
gravitational force tells us that both sides participate gravitationally.

#### Why This Is Easy To Miss

Ordinary notation compresses away the bookkeeping:

```text
F = mg
```

Without VD-style declarative bookkeeping, it is easy to read this as a
one-sided force: source has gravity, target has mass. The halving/doubling
analysis reveals the stronger commitment: both participants carry the relevant
gravitational structure and both satisfy the relevant condition.

This is an example of why the VD effort matters. It exposes commitments that
ordinary physics fluency tends to hide.

## Mechanical-Composition And Missing List Machinery

### Missing Mechanical-Composition Item Word

#### Initial Thought

We first considered a missing law that would lock:

```text
reaction force present on a particle
-> the relevant acting-object is present in that particle's
   mechanical-composition
```

This is related, but not yet the precise missing piece.

#### Corrected Structural Need

The better observation is by analogy with the IFS law.

In the force-sum law, `attached-force` acts as the item-kind inside
`interacting-forces-set`, while remaining separate from `action-force` and
`reaction-force`.

Mechanical-composition needs an analogous item-kind:

```text
mechanical-composition_point-particle
??? item-role
acting-object
```

The new word should represent an acting-object as one member in a particle's
mechanical-composition list. It should not be identical to abstract
`acting-object`, just as `attached-force` is not identical to `action-force` or
`reaction-force`.

#### Candidate Names Mentioned

No name was chosen. Possible placeholders:

```text
composed-acting-object
mechanical-composition-item
composition-acting-object
attached-acting-object
member-acting-object
acting-object_member
```

#### Intended Role

The new item word should allow an entry/law pattern like:

```text
mechanical-composition list
composition item
acting-object
```

where the item word means "this acting-object as one listed member of this
particle's mechanical-composition."

### Mechanical-Composition As List

#### Needed Entries

Design 2.1 likely needs additional entries that develop
`mechanical-composition_point-particle` as a list of acting-objects.

At minimum, the list treatment needs to support:

- acting-object members considered one at a time;
- generation of candidate members;
- accumulation or recognition of members;
- closure / no-more-items signal;
- empty-list behaviour where appropriate.

The conversation specifically noted that developing mechanical-composition as
a list of acting-objects would require two more entries, but their exact
headwords and positions are still unresolved.

#### Relationship To IFS

The likely parallel is:

```text
interacting-forces-set -> attached-force
mechanical-composition_point-particle -> [new acting-object item word]
```

This is the central list-design pressure currently exposed.

## Larger Design Lesson

Design 2.1 is not just an editing pass over prose. It is still discovering
which operational headwords must exist before the entries can be honest.

The key discovered pattern:

```text
list container -> item-role -> downstream typed alternatives
```

For force accounting:

```text
interacting-forces-set -> attached-force -> action-force / reaction-force
```

For mechanical-composition, the analogous structure is missing:

```text
mechanical-composition_point-particle
  -> [new item-role]
  -> acting-object
```

Until that item-role exists, the mechanical-composition list cannot be cleanly
expressed in Design 2.1.
