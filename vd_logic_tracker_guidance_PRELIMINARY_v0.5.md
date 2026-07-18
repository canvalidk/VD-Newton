# VD Logic Tracker: Implementation Guidance

**Date:** 2026-03-22
**Source:** Findings from program-trace exercises on Newton v0.5 (Levels 1–2, three iterations)
**Status:** Preliminary — based on a single case study; should be stress-tested against further instances

---

## Purpose

This document captures what we learned about how the VD operates as a program by tracing it against textbook exercises. It provides guidance for implementing a logic tracker — the runtime evaluation engine that would mechanise the parts of a VD trace that are currently performed by the human reader.

The document is divided into two parts:

**Part A — Necessary Instructions.** Things that must be true for the logic tracker to correctly implement VD evaluation. Violating these would produce incorrect traces.

**Part B — Helpful Guidance.** Design recommendations and architectural observations that emerged from the traces. These are not correctness requirements but would lead to a better implementation.

---

# Part A — Necessary Instructions

---

## A1. The evaluation model is lazy (demand-driven)

Evaluation begins with a goal expression and proceeds by demand propagation. A subexpression is only evaluated when something upstream requires its value. There is no eager setup phase, no pre-loading of scaffold entries, no initialisation step.

This is not a stylistic preference — it is a correctness requirement. The traces showed that eager evaluation produces incorrect sequencing (the free-particle check was inserted as an explicit step in v1/v2 but is never demanded by the dependency chain) and disguises the true causal structure (closure appeared to be a prerequisite in v2 but is actually a diagnostic response to a blocked evaluation in v3).

**The rule:** an entry is invoked if and only if the current expression under evaluation contains a headword that must be resolved for the expression to reduce.

---

## A2. The goal expression is the single evaluation root

The exercise question determines the goal. "Find the acceleration" means the top-level expression is `inertial-acceleration(particle)`. Everything else — meta-typing checks, force decomposition, closure diagnostics — fires because the goal demands it, directly or transitively.

There is one exception identified so far: the closure check (E38–E44) has no inbound dependency edge from the Newton II → Force Sum chain. In the current 44-entry instance, it is a separate evaluation root that the physicist invokes manually when the evaluator gets stuck. However, this appears to be an artifact of incomplete implementation — once all acting-objects have properly encoded force laws, the demand chain should flow through without breaking, and closure would revert to being a checkable property rather than a debugging tool. See B5 for further discussion.

**The rule:** the logic tracker must accept a goal expression as input and derive everything else from it. It must not pre-compute or eagerly evaluate entries that the goal does not demand.

---

## A3. Multiple definitions of the same headword require a resolution strategy

Many headwords have more than one entry: a chimney (peripheral definition), a triplet entry (relational definition), and sometimes a wall (grounding definition). For example, `inertial-acceleration` has E20 (chimney: "the acceleration of a point-particle as measured in an inertial-frame") and E21 (triplet: "equals net-force divided by inertial-mass").

These serve different roles:

- The **chimney** provides preconditions and type constraints. E20 tells you the particle must be a `point-particle` and the measurement must be in an `inertial-frame`. These are demands that must be satisfied before the computation rule can fire.
- The **triplet entry** provides the computation rule. E21 tells you how to compute the value.
- The **wall** provides external grounding — what the concept means in the broader context.

**The rule:** when a headword is demanded, the logic tracker must consult all definitions and extract:
1. **Preconditions** from the chimney/wall (type constraints that generate meta-typing demands)
2. **The computation rule** from the triplet entry (the expression that reduces the headword to other headwords)

The tracker must not treat multiple definitions as ambiguous or conflicting. They are complementary views of the same headword.

---

## A4. Meta-typing (E28–E30) is a subroutine, not a law to be checked

Whenever evaluation encounters a type constraint — "this must be a `point-particle`," "this must be in an `inertial-frame`" — the meta-typing subroutine fires. It is the most frequently called subroutine in the program. In the Atwood trace, it fired 9 times: 3 particle/frame classifications and 4 acting-object instantiations, plus the mechanical-system definition and one negative result.

The subroutine has three steps, prescribed by the entries:

1. **E28** (procedure): To check membership in a raw-class C, check whether the object possesses the class-specific-features of C.
2. **E29** (features): The class-specific-features of C are given by C's definition entries.
3. **E30** (result): If the object is recognised as possessing the features, treat it as an instance-of C.

**The rule:** the logic tracker must implement meta-typing as a callable subroutine with the following signature:

```
meta_type(object, class) → {YES, NO} + human_recognition
```

The subroutine retrieves the class-specific-features from the class's definition entries, presents them to the human for a recognition judgment, and returns the result. The tracker must record which entry supplied the features and what the human's recognition judgment was.

---

## A5. Human inputs are typed IO actions at specific demand points

The traces identified four kinds of human input, each triggered at a specific point in the demand chain:

1. **Recognition acts** — triggered by meta-typing (E28–E30). The program presents the class-specific-features; the human judges whether the object has them. The program prescribes the *procedure*; the human supplies the *perception*.

2. **Modelling decisions** — triggered by set-population demands (E25: interacting-forces-set, E38: mechanical-system). The program declares the type; the human decides what populates it.

3. **Empirical inputs** — triggered by demands for numerical values (E36: canonical-force, E37: paired-particle). The program provides the slot; the human fills in the value from domain knowledge.

4. **Closure-forced judgments** — triggered by closure failure (E42/E44). The program reports that the system leaks; the human justifies why the leaks don't matter, producing constraints that unblock evaluation.

**The rule:** the logic tracker must:
- Suspend evaluation at each human-input point
- Record the type of input (recognition / modelling / empirical / closure-forced)
- Record which entry demanded it
- Record the human's response
- Resume evaluation with the supplied value

The tracker must not silently supply human inputs from background knowledge. Every human input must be explicit and attributed.

---

## A6. Blocked thunks are legitimate evaluation states

When evaluation cannot reduce an expression because a subexpression depends on an unresolved value, the result is a blocked thunk — a partially evaluated expression with free variables. This is a normal state, not an error.

In the Atwood trace, both Newton II calls produced blocked thunks: `(T − 29.4) / 3` and `(T − 49.0) / 5`, both blocked on the free variable T. These thunks are informative — they carry the algebraic structure of the answer, even though the numerical value isn't yet available.

**The rule:** the logic tracker must support partially evaluated expressions. When a demand cannot be satisfied (because the value depends on an unresolved variable), the tracker must:
- Record the blocked thunk with its free variables identified
- Continue evaluating other branches if possible
- Report the set of blocked thunks and their shared free variables when evaluation can proceed no further

---

## A7. Dependency edges are authorial, not semantic

The dependency graph is built by the tokeniser: an edge from headword A to headword B exists when some entry with headword A uses headword B in its definition. These edges are authorial declarations — the author chose to use that headword. They do not encode causation, ownership, physical influence, or any semantic relationship.

**The rule:** the logic tracker must derive demands exclusively from the tokeniser-detected dependency edges. If a headword appears in a definition, it generates a demand. If it does not appear, it does not generate a demand, regardless of whether a human would consider it semantically relevant. This is why the free-particle check drops out — the headword `free-particle` does not appear in E20 or E21, so evaluating `inertial-acceleration` never demands it.

---

# Part B — Helpful Guidance

---

## B1. The for-each-particle iteration is implicit and should be handled by the tracker

The VD defines Newton II for "a point-particle" (singular). When multiple particles are present, the physicist applies it to each independently. This iteration is not encoded in any entry.

In Haskell terms, the physicist performs `map newtonII particles`. The VD provides the function; the human provides the map.

**Recommendation:** The logic tracker should accept a set of objects to evaluate the goal expression against, and iterate automatically. The iteration is semantically trivial (each application is independent) but needs to be tracked because the results may share free variables (as in the Atwood machine, where both thunks share T).

---

## B2. Multiple blocked thunks may form a solvable system

A single blocked thunk is stuck. But multiple blocked thunks sharing the same free variables may together form a solvable system of equations. In the Atwood trace, neither thunk alone determines T, but together they give two equations in two unknowns (after the kinematic coupling constraint is supplied).

**Recommendation:** The logic tracker should collect all blocked thunks and attempt algebraic resolution when human-supplied constraints reduce the number of free variables. The tracker should distinguish between:
- **Fully blocked**: no combination of thunks resolves the free variables.
- **Constraint-resolvable**: the thunks form a solvable system once external constraints are supplied.
- **Algebraically solvable**: the thunks already form a solvable system (all free variables can be eliminated).

---

## B3. Chimney, triplet, and wall entries have distinct computational roles

The six-entry house structure maps onto computational roles:

- **Chimney:** Provides the type signature and preconditions. When a headword is demanded, the chimney tells you what type of inputs it expects and what meta-typing checks must pass. This is like a function's type signature.

- **Triplet entry:** Provides the computation rule — how to reduce this headword to other headwords. This is like the function body.

- **Wall:** Provides external grounding and context — what the concept means in the broader dictionary. Computationally, the wall serves as documentation and as an alternative definition for contexts where the triplet's inward-facing relational definition isn't appropriate.

**Recommendation:** The logic tracker should tag each entry with its structural role (chimney / triplet / wall / scaffold / non-law) and use this to determine how to process it:
- Chimney → extract preconditions, generate meta-typing demands
- Triplet → extract computation rule, reduce expression
- Wall → available for grounding but not part of the primary reduction path

This tagging could be derived automatically from the house detection algorithm already in the engine.

---

## B4. Newton I and Newton II are parallel branches, not sequential

The physicist's habit is: "first check Newton I (is the particle free?), then apply Newton II (F = ma)." The lazy evaluation model reveals this is a heuristic, not a program dependency. Newton II's definition (E21) requires the particle to be a `point-particle` measured in an `inertial-frame` — it does not require the particle to be non-free. Newton I defines what an inertial frame *is* (E16 references `free-particle` and `uniform-motion`), but Newton II only *uses* `inertial-frame` as a precondition, without caring about the internal structure of its definition.

**Recommendation:** The logic tracker should not build in any assumed ordering between Newton I and Newton II. The demand structure will naturally invoke Newton I concepts (free-particle, uniform-motion) only when they are needed — which turns out to be during the meta-typing check for inertial-frame, not as a precondition for Newton II itself.

More broadly: the tracker should never assume sequencing between laws. The degree-of-law metric measures dependency depth, but that's a static property of the graph, not an execution order. The execution order is determined entirely by demand propagation from the goal.

---

## B5. Closure's role depends on the completeness of the instance

In the current 44-entry instance, the closure check (E38–E44) is disconnected from the Newton II → Force Sum demand chain. No entry in E20–E26 references any closure headword. The physicist invokes closure manually when the evaluator gets stuck.

This appears to be an artifact: if every acting-object had a fully encoded force law, the demand chain would flow through E36 (canonical-force) to the force law, which would demand the properties of the force mechanism (e.g., string masslessness, inextensibility), which would supply the constraints that currently come from the closure diagnostic. The evaluator would never get stuck, and closure would be a property to check rather than a debugger.

**Recommendation for the near term:** Implement closure as a separate callable diagnostic that the tracker (or the human) can invoke when evaluation blocks. The diagnostic takes a mechanical-system S as input and reports which interaction-candidates cannot be paired, identifying the external objects involved.

**Recommendation for the long term:** As acting-objects get fully implemented with force laws, the demand chain should naturally extend through them. Monitor whether the closure check becomes redundant as a diagnostic (because blockages disappear) or retains an independent role as a modelling validation (checking that the physicist's system boundary is self-consistent even when the algebra goes through).

---

## B6. The tracker should record the full evaluation tree

Each trace produced a demand tree: a tree rooted at the goal expression, with internal nodes being entry invocations and leaves being either resolved values or human-input suspension points. This tree is the primary output of the logic tracker — it records not just the answer but the complete derivation path.

**Recommendation:** The tracker should emit a structured evaluation tree with the following node types:

- **EVAL node**: an expression being reduced, annotated with which entry provides the reduction rule
- **DEMAND node**: a subexpression that must be resolved, annotated with which headword triggered it
- **META-TYPE node**: a meta-typing subroutine call, annotated with class, object, features source, and human recognition result
- **HUMAN-INPUT node**: a suspension point, annotated with input type (recognition / modelling / empirical / closure-forced), demanding entry, and human response
- **BLOCKED node**: a partially evaluated expression, annotated with free variables
- **VALUE node**: a fully resolved leaf

This tree is the trace. It can be inspected, audited, compared across exercises, and used to identify which entries are exercised by which problems.

---

## B7. The tracker can detect coverage gaps

By running traces against multiple exercises and collecting the evaluation trees, the tracker can report which entries are never demanded. In the Atwood trace, entries E5, E7, E9–E13 (displacement, speed, trajectory, straight-line, path-length, relative position/velocity) were loaded but never demanded. This isn't a bug — those entries serve other exercises. But systematic coverage analysis could reveal entries that are *never* demanded by *any* exercise, which might indicate dead code or missing dependency edges.

**Recommendation:** Maintain a coverage map: for each entry, which exercises demand it and via what path. This serves both as a test suite for the VD instance and as a guide for identifying structural gaps.

---

## B8. Error conditions the tracker should detect

The traces revealed several conditions that should be flagged:

- **Unresolvable demand**: a headword is demanded but has no entry. This would indicate a gap in the VD instance.
- **Circular demand**: evaluating headword A demands headword B, which demands headword A. Within a law triplet, this is expected (the three entries mutually reference each other). Outside a triplet, it would indicate a bug. The tracker should recognise triplet cycles as legitimate and flag non-triplet cycles as errors.
- **Type mismatch in meta-typing**: the object fails the recognition check. This is not an error in the VD — it's informative (as with the free-particle check returning NO). The tracker should record negative results as meaningful outcomes.
- **Closure failure**: not an error but a diagnostic result that should be surfaced with the specific unpaired interaction-candidates and their external destinations.
- **Multiple computation rules**: if two triplet entries for the same headword provide different computation rules, the tracker should flag the ambiguity. (In the current instance, this doesn't occur — each headword has at most one triplet entry.)
