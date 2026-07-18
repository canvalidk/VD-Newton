# The Abstract Interaction Candidate

## Context

During the VD encoding of Newtonian mechanics, the closure triplet (interaction candidate / closed interaction / closed system) was initially treated as a bookkeeping device specific to force-based mechanics. On reflection, the concept of "interaction candidate" turns out to be a theory-independent structural object — one that recurs across all branches of physics, with only its concrete content changing between theories.

This document develops the abstract concept from three features, derives an indexing requirement, and explains why the concept was deliberately kept free of conservation assumptions.

---

## The Three Features

### Feature 1 — Exchange

An interaction is an identifiable exchange mediated between two physical systems. At the abstract level, we do not specify *what* is exchanged — it could be force, energy, momentum, pressure, molecules, or something else entirely depending on the theory. The only requirement is that something identifiable passes between system A and system B.

### Feature 2 — Internalisation

If we construct a larger system C that contains both A and B, the interaction does not disappear. It becomes an internal feature of C. The same interaction object, now viewed from a higher level. The interaction is invariant under embedding — drawing a larger boundary around both participants changes the perspective but not the object.

### Feature 3 — Decomposition

The process runs in reverse. Starting from a single system C that contains an internal interaction, we can separate C into two subsystems A and B such that the interaction is now external to both. The same object that was internal to C is now the thing that couples A and B across their shared boundary.

---

## Summary of the Three Features

The interaction candidate is the object that survives the operations of composing and decomposing systems. It is the hinge: when you zoom out it becomes internal, when you zoom in it becomes external, but it is the same object either way.

A closed system is then one in which every interaction candidate has been internalised — and this can be verified by attempting to decompose along each interaction and confirming that both sides see it as accounted for.

---

## The Indexing Requirement (Derived)

Features 2 and 3 together impose a continuity constraint: the interaction must be identifiable as the same object across different views (internal to C, external to A and B). This means the formalism must carry some token — an index, a name, a handle — that tags each interaction and persists across the composition and decomposition operations.

The argument is computational: a mathematical object that is not forgotten must be remembered, and remembering requires a label. Without such an index, you could not verify closure — there would be no way to match up the interactions that A sees externally with the internal structure of C.

In the Newtonian case study, this requirement is already satisfied: the interaction candidate is indexed by the triple (p, q, acting_object), which uniquely identifies it whether viewed from inside or outside the system boundary.

---

## What Is Deliberately Excluded: Conservation

It is tempting to add a fourth feature: that whatever A gives, B receives — i.e., that the exchange is zero-sum. This would immediately yield conservation laws (closed systems conserve the exchanged quantity because all exchanges are internal and net to zero).

This temptation was explicitly resisted. The reason is thermodynamic: entropy can be *generated* inside a system, not merely shuffled between subsystems. If zero-sum exchange were baked into the abstract concept of interaction, the framework would break when applied to theories involving entropy production.

In the Newtonian case study, momentum conservation already follows from the specific structure of canonical and reaction forces being negatives of each other. That is content particular to the Newtonian interaction candidate, not a feature of the abstract concept.

By keeping the abstract interaction candidate free of conservation assumptions, it remains maximally general — compatible with any theory that has a notion of systems exchanging something across boundaries.

---

## Connection to the Equivalence Principle Discovery

The VD encoding of Newtonian mechanics revealed that "interaction candidate" (born in the closure triplet) and "acting force" (born in the action-reaction triplet) enter through different definitional doors but are silently treated as equivalent. This is structurally identical to the gravitational/inertial mass equivalence: two concepts with independent origins that happen to coincide.

Elevating the interaction candidate to a theory-independent object strengthens this finding. The equivalence between interaction candidates and acting forces is not just a quirk of Newtonian bookkeeping — it is an empirical commitment that the theory makes about how its specific notion of exchange (force) relates to the abstract structural role (interaction candidate). Other theories will make different commitments, and the VD can surface those too.
