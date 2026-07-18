# VD Newton Case Study: Feedback from Program Trace Exercises

**Date:** 2026-03-22
**Source:** Trace exercises on Newton v0.5 — Levels 1–2 (three iterations: v1, v2, v3)
**Purpose:** Collect all identified improvements to the Newton case study entries and the VD architecture

---

## Feedback points agreed during session

### 1. The acting-object ownership bug is real and needs to be fixed

**Source:** v2 trace (Step 9, closure check) and v3 trace (blocked thunks + diagnostic)

**Problem:** The current acting-object entries (E34–E37) define acting-objects as standalone entities that "have" a paired-particle. This means you can't start at a particle and enumerate the acting-objects that affect it — you can only start at an acting-object and find where it fires. The closure algorithm requires being able to trace forces from inside a mechanical system S, but forces firing *into* S from external acting-objects (Case 3 in the bug report) are only visible as orphaned symptoms, not traceable to their source.

**Evidence from trace:** In the Atwood machine, all four forces on particles in S came from external sources (Earth and string-pulley assembly). The closure check correctly reported "0/4 pair," but it couldn't tell the physicist *which* external objects were involved — that required physics knowledge imported by the human.

**Action:** Fix the acting-object entries as described in the existing bug report. The two-legged closure check (internal completeness + no unexplained forces) should be encoded.

**Entries affected:** E34–E37, E39, E43.

---

### 2. Guidance for responding to closure failure could be encoded in the entries

**Source:** v2 trace (Step 11, human response to closure failure) and v3 trace (diagnostic section)

**Problem:** When closure fails, the current entries tell the physicist *that* the system leaks (E42) and *why* it matters (E44 — the equations aren't self-sufficient). But they provide no guidance on *what to do about it*. The physicist's response — identify external objects, estimate their dynamical contribution, either expand S or justify negligibility — follows a pattern, but that pattern is not encoded.

**Evidence from trace:** The closure-forced judgments (Earth's acceleration is negligible, string is massless, wall doesn't accelerate) all followed the same procedure: identify the external object receiving a reaction force, estimate whether its dynamics affect the particles in S, conclude that they don't. This procedure could be partially encoded in the residual/poetic layer.

**Action:** Consider adding guidance — either in E44's definition or in a new entry — that prescribes the response pattern: "for each interaction-candidate that cannot be paired, identify the external object receiving the reaction force, and either expand S to include it or justify why its dynamical contribution to particles in S is negligible."

**Entries affected:** E44, or a new post-closure entry.

---

### 3. The meta-typing law deserves more attention for clarity and correctness

**Source:** Level 1 trace (the meta-typing correction) and v3 trace (9 meta-typing calls)

**Problem:** Meta-typing (E28–E30) is not a peripheral law — it is the most frequently invoked subroutine in the entire program. Every instantiation, every classification, every "is this object an X?" question runs through it. In the Atwood trace it fired 9 times. Because it's so natural that people run it without noticing (the original Level 1 trace failed to attribute Steps 1–3 to meta-typing at all), the entries need to be especially clear and correct.

**Specific concerns:**

- E28–E30 define the *positive* case (recognise features → treat as instance-of). The *negative* case (features not recognised → not an instance) is logically implied but not explicitly stated. The trace relied on negative results (ball is NOT a free-particle) as meaningful outputs.

- The entries handle single-class membership checks ("is x an instance of C?"). The trace also involved enumeration ("which classes does this object belong to?") and negative classification ("the string is NOT a point-particle, which tells me it's outside the program's type system"). Whether these patterns are supported cleanly by the current wording should be checked.

- Meta-typing is invoked not just for physics types (point-particle, inertial-frame) but also for VD-internal types (acting-object, mechanical-system). The entries should be clear that meta-typing applies to all raw-classes in the dictionary, not just physics concepts.

**Action:** Review E28–E30 for clarity. Consider whether negative results and multi-class patterns need explicit treatment or are adequately covered by the current wording.

**Entries affected:** E28–E30.

---

### 4. Concrete acting-objects need to be encoded to stress-test the architecture

**Source:** v3 trace (blocked thunks on T) and the discussion about why the evaluator got stuck

**Problem:** The current 44-entry instance defines the *architecture* for forces (acting-object, activation-condition, canonical-force, paired-particle, reaction) but contains no specific force models. The gravitational force law, string tension, normal force — all are imported as raw human inputs. This means the demand chain breaks mid-evaluation (the evaluator blocks on unresolved force values), and the closure diagnostic has to serve as a debugger rather than a property check.

**Evidence from trace:** The evaluator blocked on T because the string-contact acting-object has no encoded force law. The human had to supply the string constraints (massless → equal tensions, inextensible → kinematic coupling) via the closure diagnostic. If the force law were encoded, the demand chain would flow through E36 to the force law, which would demand the string's properties, which would supply the constraints — no blockage, no separate diagnostic.

**What encoding force models will stress-test:**

- **Closed-form force laws** (gravity: F = −mg ŷ). Relatively straightforward — the acting-object has a formula that takes particle properties as input and returns a vector. But: what is the paired-particle for gravity? The Earth as a whole? Its centre of mass? How does a field force fit the point-to-point acting-object model?

- **Constraint force laws** (string tension, normal force). Structurally different — the force value is not given by a formula but by a constraint equation. The acting-object architecture (E34–E36) assumes a single canonical-force on a single target. A string exerts force on two particles through a mechanism. Whether this fits the current architecture or needs a new type is an open question.

- **The paired-particle identification problem.** E37 says every acting-object has a paired-particle, but provides no procedure for determining which particle it is. The human fills this slot using physics knowledge. As concrete acting-objects get encoded, this slot needs to become part of the acting-object's definition rather than a human judgment.

**Action:** Begin encoding concrete acting-objects, starting with simple cases (near-Earth gravity, contact normal force) and progressing to harder ones (string tension, spring forces). Each will surface specific architectural questions. The string case is the most architecturally consequential — it will determine whether constraint mechanisms fit the acting-object model or need a separate type.

**Entries affected:** New entries to be added; may require revisions to E34–E37.

---

## Additional feedback points identified by Claude

### 5. The program has implicit control flow that may or may not need encoding

**Source:** v1/v2 traces (for-each-particle iteration) and v3 trace (the evaluator applying Newton II to each particle independently)

**Problem:** The VD defines Newton II for "a point-particle" (singular). When multiple particles are present, the physicist applies it to each independently. This iteration is not encoded in any entry. Similarly, there is no branching logic ("if not free, apply Newton II") — the demand structure handles this implicitly in lazy evaluation.

**Finding from v3:** In the lazy evaluation model, explicit control flow may be unnecessary. The demand structure *is* the control flow — evaluation order emerges from the goal expression and the dependency edges. The for-each-particle iteration is the one remaining case where the human must recognise that a definition applies to multiple objects.

**Action:** Monitor whether this is a genuine gap or an acceptable feature. The logic tracker (B1 in the guidance document) should handle the iteration mechanically. If future traces reveal cases where the lack of explicit control flow causes incorrect evaluation order, entries encoding execution strategy may be needed.

**Status:** Open question. Low priority unless future traces reveal problems.

---

### 6. String/constraint mechanisms are a genuine type gap, not just a missing library

**Source:** v1 trace (structural observation 3), v2 trace (structural observation 4), v3 trace (blocked thunks)

**Problem:** The VD's acting-object architecture (E34–E37) models point-to-point forces: one acting-object, one activation-condition, one canonical-force on one target, one reaction on the paired-particle. A string over a pulley is a constraint mechanism that couples multiple particles simultaneously. It cannot be cleanly modelled as two separate acting-objects that happen to share a tension magnitude — the constraint *between* the two ends (masslessness → equal tension, inextensibility → kinematic coupling) is the essential feature, and it has no entry to hang on.

**Evidence from trace:** The Atwood trace required two separate string-contact acting-objects (one per end) plus two human-supplied constraint equations. The constraints came from the closure diagnostic, not from the acting-object definitions. This decomposition was physics knowledge dressed up as VD structure.

**Action:** This is related to point 4 but distinct. Point 4 is about encoding specific force models within the existing architecture. Point 6 is about whether the architecture itself needs a new type — something like "constraint mechanism" alongside "acting-object" — to handle forces that couple multiple particles through internal constraints. The answer will likely emerge from attempting point 4 with string and spring forces.

**Status:** Open question. Will be resolved by attempting to encode string mechanics as an acting-object.

---

### 7. Closure's architectural role depends on the completeness of the instance

**Source:** v3 trace (structural finding 2) and the subsequent discussion about why the evaluator blocked

**Problem:** In the current 44-entry instance, the closure check (E38–E44) has no inbound dependency edge from the Newton II → Force Sum chain. No entry in E20–E26 references any closure headword. The physicist invokes closure manually when evaluation blocks. This makes closure a separate evaluation root — a diagnostic tool, not part of the normal demand chain.

**Finding:** This is likely an artifact of incomplete implementation. Once acting-objects have properly encoded force laws, the demand chain should flow through E36 → force law → mechanism properties → constraints, without blocking. The evaluator would never get stuck, and closure would not be needed as a debugger.

**However:** Closure may retain an independent role even in a complete instance. E44 says a mechanically-closed-system is one "whose future behaviour is determined by the equations produced from the interactions internal to it." This is a modelling validation — it tells the physicist whether their system boundary is self-consistent — and that validation might be worth performing even when the algebra goes through.

**Action:** Consider whether the entries should encode a dependency from the computation chain to closure. Something like: "the equations produced by Newton II for particles in a mechanical-system are solvable if and only if the system is a mechanically-closed-system." This would make closure a demanded step rather than an external diagnostic. Whether this is correct — and whether it should be a hard dependency or just an advisory — is a design question.

**Status:** Deferred until acting-objects are implemented and the demand chain can be tested end-to-end.

---

## Summary table

| # | Point | Priority | Type | Entries affected |
|---|-------|----------|------|-----------------|
| 1 | Acting-object ownership bug | High | Bug fix | E34–E37, E39, E43 |
| 2 | Negligibility guidance in closure | Medium | New content | E44 or new entry |
| 3 | Meta-typing clarity review | Medium | Review/revise | E28–E30 |
| 4 | Encode concrete acting-objects | High | New content | New entries; possibly E34–E37 |
| 5 | Implicit control flow | Low | Open question | None yet |
| 6 | Constraint mechanism type gap | Medium | Architecture question | Depends on outcome of #4 |
| 7 | Closure's role in demand chain | Medium | Design question | E44 or new entry linking to E21/E24 |
