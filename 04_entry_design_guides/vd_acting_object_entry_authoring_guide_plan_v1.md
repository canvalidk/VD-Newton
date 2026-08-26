# VD Acting-Object Entry Authoring Guide - Plan v1

## Purpose

This document is a rough plan for a future guide that teaches LLMs how to
write reliable VD entries for acting-objects. It records lessons from the first
spring-force trial, where several plausible-looking answers turned out to be
wrong in VD-specific ways.

The goal is not merely to make an LLM produce physics formulas. The goal is to
make an LLM produce entries that preserve:

- VD law-house structure;
- scoped headword discipline;
- correct placement of human/residual inputs;
- acting-object dispatch structure;
- traceability through mechanical-composition and force-sum;
- model-boundary clarity.

## Core Thesis

Good VD entries require an LLM to resist a normal helpful instinct: expanding
too much too early.

In textbook physics, a good answer often explains the formula by unpacking all
its symbols. In VD entry-writing, that can be a structural error. If a law
entry expands its partner terms into their constituents, it may introduce too
many undefined ideas and cease to be a clean triplet entry.

The guide therefore needs to teach LLMs not only what to include, but where
each kind of information belongs.

## What We Learned From The Spring Trial

### 1. Do not use unscoped textbook symbols as if they were VD entries

Tempting bad form:

```text
F = -kx
```

Why this fails:

- `F`, `k`, and `x` are ordinary mathematical placeholders, not scoped VD
  headwords.
- Bare `x` accidentally gets captured as "the displacement used by springs"
  forever.
- Bare `k` similarly risks becoming a global stiffness-like symbol rather than
  the parameter of a specific acting-object type.

Better VD-shaped form:

```text
canonical-force_simple-spring
  = - spring-constant_simple-spring * displacement-from-equilibrium_simple-spring
```

or, once the scoped headwords are established:

```text
F_vec_simple-spring = -k_simple-spring * x_vec_simple-spring
```

The symbol form is allowed, but the symbols must be locally scoped and tied to
headwords.

### 2. Name the model regime in the headword

Tempting bad form:

```text
spring
```

Why this fails:

- Real springs can become plastic, break, buckle, slacken, damp, carry mass, or
  become nonlinear.
- A Hooke-law entry does not define all springs.
- If the entry is named too broadly, later traces inherit false commitments.

Better candidate:

```text
simple-spring
ideal-linear-spring
```

The name should delimit what the entry is allowed to say.

### 3. Do not halve spring force merely because there is action-reaction

We tested a half-interaction idea from gravity and initially overgeneralised it
to springs.

Correct distinction:

- Gravity may need halving because both massive participants carry gravity
  acting-objects/fields. Two same-kind source mechanisms are present.
- A block interacting with a spring does not automatically create a second
  spring acting-object. There is one spring mechanism in the scene.
- Action-reaction is not itself a reason to halve.

Guide rule:

```text
Only consider halving when the scenario contains duplicate same-kind source
acting-objects whose full contributions would double-count the same physical
interaction.
```

For a simple spring:

```text
canonical-force_simple-spring
  = - spring-constant_simple-spring * displacement-from-equilibrium_simple-spring
```

not half that.

### 4. Do not overload a triplet entry with constituent geometry

Tempting bad form:

```text
canonical-force_simple-spring =
  -k * (|position(endpoint-a) - position(endpoint-b)| - rest-length)
      * unit(endpoint-a - endpoint-b)
```

Why this fails as a first VD law entry:

- It imports `position`, `endpoint`, `rest-length`, `unit`, vector norm, and
  other ideas into one entry.
- It may no longer have the clean "one defined headword plus two partner ideas"
  shape expected of a triplet.
- It hides which concepts deserve their own entries, walls, or law-houses.

Better:

```text
canonical-force_simple-spring
  = - spring-constant_simple-spring * displacement-from-equilibrium_simple-spring
```

Then define `displacement-from-equilibrium_simple-spring` elsewhere.

### 5. The familiar physics-law form may emerge from VD constraints

The clean spring entry resembles ordinary Hooke's law, but for a different
reason than textbook habit. It emerges because:

- the headword is scoped;
- the model regime is scoped;
- only the two relevant partner ideas appear;
- geometry is deferred;
- parameter and construct information are separated.

This is useful evidence that VD discipline can recover familiar physics laws
while making their hidden assumptions explicit.

## Proposed Guide Structure

### Part 1 - Orientation

Explain what an acting-object entry is for.

Topics:

- Acting-objects as force-producing callable structures.
- Scenario declaration via `mechanical-composition_point-particle`.
- The trace, not the answer, is the product.
- Human inputs must land at walls or concrete entries, not abstract triplets.
- Concrete acting-object entries are dispatch destinations from the abstract
  acting-object triplet.

### Part 2 - The Minimal Abstract Architecture

Quote and analyze the three abstract acting-object entries:

- `acting-object`
- `activation-condition_acting-object`
- `canonical-force_acting-object`

Also include:

- `mechanical-composition_point-particle`
- `paired-particle_acting-object`
- `impressed-force`
- `canonical-force_acting-object`
- `reaction-force_acting-object`
- `interaction`
- `interaction-set`

The guide should teach LLMs to reason from the exact entry wording, not from
summaries.

### Part 3 - Entry Roles

Explain the difference between:

- triplet entries;
- chimneys;
- walls;
- scaffold entries;
- concrete dispatch entries;
- parameter entries;
- construct entries;
- modelling-assumption entries;
- activation-condition entries.

Key rule:

```text
Do not put wall content into triplet entries.
Do not put triplet content into walls unless the structure specifically
requires it.
```

### Part 4 - Naming Discipline

Teach scoped headword naming.

Bad:

```text
k
x
force
spring
friction
```

Better:

```text
spring-constant_simple-spring
displacement-from-equilibrium_simple-spring
canonical-force_simple-spring
activation-condition_simple-spring
coefficient-kinetic-friction_sliding-contact
```

Questions for the LLM:

- Does this headword accidentally claim a general word?
- Is the model regime named?
- Is the headword narrow enough that the entry is true?
- Does the name distinguish this acting-object from variants?

### Part 5 - Model Scope And Variant Control

Explain why acting-object entries should be narrow.

Examples:

- `simple-spring`, not all springs.
- `near-earth-gravity`, not all gravity.
- `kinetic-friction_sliding-contact`, not all friction.
- `normal-contact_rigid-surface`, not all contact.

The guide should teach that variants are separate entries or later extensions,
not hidden exceptions inside the first entry.

### Part 6 - Slots, Constructs, Parameters

Distinguish three categories from the consolidation note.

Slots:

- participants;
- target particle;
- source/paired particle;
- surface endpoint, support, field source, etc.

Constructs:

- spatial or relational structures whose meaning is locked by a definition or
  law;
- examples: equilibrium-configuration, contact-surface, source-point.

Parameters:

- atomic scalar values;
- examples: spring constant, coefficient of friction, gravitational constant.

Guide rule:

```text
Do not treat constructs and parameters as the same kind of input.
```

For springs:

- `spring-constant_simple-spring` is a parameter.
- `equilibrium-configuration_simple-spring` is likely a construct.
- `displacement-from-equilibrium_simple-spring` likely depends on a construct.

### Part 7 - Triplet Discipline

Teach LLMs how to keep a candidate law entry clean.

Checklist:

- What is the headword being defined?
- What are the two partner ideas?
- Are any extra undefined headwords sneaking in?
- Are symbols scoped to the concrete acting-object?
- Does the entry accidentally unfold one partner idea instead of naming it?
- Does the formula express the law at the intended abstraction level?

Spring example:

Good candidate:

```text
The canonical-force_simple-spring is the negative product of
spring-constant_simple-spring and
displacement-from-equilibrium_simple-spring.
```

Risky candidate:

```text
The canonical-force_simple-spring is -k times the distance between endpoint A
and endpoint B minus rest length in the direction from A to B.
```

The risky version may contain useful physics, but it belongs downstream in
construct definitions, not in the canonical-force entry.

### Part 8 - Activation Conditions vs Modelling Assumptions

Teach the split.

Modelling assumption:

- Should this concrete acting-object model be used at all?
- Checked at instantiation.
- Examples: ideal-linear spring, massless string, rigid surface,
  frictionless pulley.

Activation condition:

- Is the acting-object currently producing/eligible to produce its
  canonical-force?
- Evaluated at trace time.
- Examples: endpoint attached, surfaces in contact, sliding rather than
  sticking, particle within field regime.

Important spring lesson:

```text
zero displacement from equilibrium should produce zero force, not inactive
spring.
```

### Part 9 - Force Halving And Source Multiplicity

Document the corrected halving principle.

Do not halve because of:

- action-reaction alone;
- two endpoints alone;
- a force being mutual in ordinary physics language.

Consider halving only when:

- the scenario contains two same-kind source acting-objects;
- each would otherwise produce the full same interaction contribution;
- summing both would double-count.

Gravity may be such a case because both masses carry gravitational fields.
Spring is not such a case because a block attached to a spring does not thereby
become a spring source.

This section should remain provisional until more traces test the rule.

### Part 10 - Dispatch Pattern

Explain how concrete acting-object entries connect to the abstract triplet.

Likely pattern:

- type hub entry for the concrete acting-object;
- concrete activation-condition entry;
- concrete canonical-force entry;
- slot/participant entries;
- parameter entries;
- construct entries.

The guide should warn that dispatch is not just "recognize a word." The
concrete type determines which activation condition and canonical-force rule
the abstract slots call.

### Part 11 - Trace Test

Every proposed acting-object entry set should be tested in a minimal trace.

The trace should show:

- where the acting-object entered mechanical-composition;
- where participant slots were filled;
- where modelling assumptions landed;
- where activation was checked;
- where parameters were supplied;
- where constructs were resolved;
- where canonical-force was evaluated;
- where reaction-force followed;
- where net-force consumed the impressed-force.

If the trace needs a human input at a triplet entry, the entry set is probably
missing a wall or dispatch destination.

### Part 12 - Failure Mode Catalogue

The final guide should include tempting wrong entries and why they fail.

Initial failures from the spring trial:

1. Bare formula:

   ```text
   F = -kx
   ```

   Fails by symbol capture and missing scoped headwords.

2. Overbroad type:

   ```text
   spring
   ```

   Fails by including springs that are not simple/linear/ideal.

3. Geometry-loaded canonical force:

   ```text
   F = -k(|r_a-r_b|-L0) unit(r_a-r_b)
   ```

   Fails as a first triplet candidate by importing too much structure.

4. Incorrect halving:

   ```text
   F_spring = -0.5 k x
   ```

   Fails because spring has one acting-object source, not two duplicate
   same-kind source mechanisms.

5. Bad activation condition:

   ```text
   active iff displacement-from-equilibrium != 0
   ```

   Fails because zero force is not absence of the acting-object.

## Rough Authoring Procedure For An LLM

1. Choose the narrow phenomenon.

2. Name the concrete acting-object with its model regime.

3. Identify whether the acting-object is a producer, constraint, or something
   not yet classified.

4. Identify the canonical-force rule at the highest clean abstraction level.

5. List the two partner ideas in the candidate law entry.

6. Move all extra symbols/constituents into separate construct or parameter
   entries.

7. Identify slots, constructs, parameters, modelling assumptions, and
   activation conditions.

8. Check whether any human input is landing at a triplet entry.

9. Write a minimal trace against a simple problem.

10. Revise until the trace's human inputs land in acceptable places.

## Review Rubric

For each proposed acting-object entry set, ask:

- Is the headword scoped narrowly enough?
- Are bare symbols avoided or locally scoped?
- Does the canonical-force entry introduce only the intended partner ideas?
- Are constructs separated from parameters?
- Are activation conditions separated from modelling assumptions?
- Are variants excluded or explicitly named?
- Does action-reaction produce the expected paired force without duplicate
  source counting?
- If halving appears, is duplicate source multiplicity actually present?
- Can the entry set produce an attributed symbolic force before problem
  solving?
- Does a minimal trace run without hidden human inputs?

## First Worked Case To Develop

The first full worked guide example should be:

```text
simple-spring
```

Candidate central entry:

```text
canonical-force_simple-spring =
  - spring-constant_simple-spring
    * displacement-from-equilibrium_simple-spring
```

Open work:

- decide exact wording for `simple-spring`;
- decide whether `equilibrium-configuration_simple-spring` forms a law-house
  with `canonical-force_simple-spring` and
  `displacement-from-equilibrium_simple-spring`;
- decide how endpoint slots are represented;
- decide how a fixed support is represented without a scenario-object layer;
- write the minimal trace for mass-on-simple-spring.

## Long-Term Guide Goal

The guide should make an LLM reliable enough to draft candidate acting-object
entries, but not trusted blindly. Reliability should come from:

- constrained authoring procedure;
- failure-mode checks;
- exact-entry citation;
- trace testing;
- review against model-scope and triplet discipline;
- iterative correction.

The intended final workflow is:

```text
textbook/mechanics source
  -> candidate acting-object type
  -> scoped VD entry draft
  -> minimal trace test
  -> failure-mode review
  -> revised entry set
  -> human approval
```

The guide should teach the LLM to produce drafts that are structured enough for
review, not to pretend that first-pass entries are final.
