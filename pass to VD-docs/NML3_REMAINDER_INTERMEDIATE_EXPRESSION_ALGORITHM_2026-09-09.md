# NML3: the remainder algorithm for building the intermediate expression

**Date:** 2026-09-09.  
**Kind:** user-requested algorithm record.  
**Status:** a proposed staged algorithm, with one simpler expansion step executed. The complete entry/interpreter problem remains unresolved.  
**Submission:** awaiting transfer to VD-docs; saved in VD-Newton's `pass to VD-docs/`. Saving here does not submit the record.

## 1. The operation we found

The working English relation is:

> The impressed force of an interaction is the expression taken out of the previous remainder when that interaction is accounted for as acting on the object.

Equivalently:

$$
R_{\mathrm{before}}
=
F_{\mathrm{impressed}}(\text{interaction})
+
R_{\mathrm{after}}.
$$

For this operation, the needed determinations can be supplied by black boxes. We are describing what to do when a determination is available. We do not first have to implement how the interaction or its force expression was determined.

Expanding a remainder should expose one impressed-force call and the continuing remainder. The surrounding expression retains the contributions already exposed. Repeating the operation can therefore build an intermediate sum whose individual force calls remain available for later expansion.

## 2. The proposed algorithm, with the information arriving in pieces

Fix the target and physical context throughout. In the user's notation, `IS(i+1)` means the next interaction in a chosen traversal of the interaction set. Here `i` is a traversal index, not an interaction identity or an intrinsic ordering of the physical set.

The proposed trace is:

```text
R-before(i)

→ {impressed-force of IS(i+1)} + {R-before(i+1)}

→ {impressed-force of spring} + {R-before(i+1)}

→ (-k*x) + {R-before(i+1)}
```

Braces in this schematic mark intended expandable demands. The stages do different jobs:

1. Expand the remainder to expose the next interaction's impressed force and the continuing remainder.
2. Resolve which interaction the pending force call addresses: for example, `IS(i+1)` supplies `spring`.
3. Expand that interaction's impressed force when its expression is needed.
4. Continue with the next remainder, retaining everything already exposed.

Step 3 can be deferred while step 4 repeats, giving the desired intermediate expression:

```text
{impressed-force of spring}
+ {impressed-force of gravity}
+ {continuing remainder}
```

The immediate idea is that the force call can be present before its interaction argument has been resolved. The selection of the interaction and the expansion of its force expression become separately visible.

At every stage, the same total remains represented:

$$
F_{\mathrm{net}}
=
\sum_{j=1}^{i}
F_{\mathrm{impressed}}\bigl(IS(j)\bigr)
+
R_{\mathrm{before}}(i).
$$

The exposed prefix supplies the accumulator's meaning. It records the contribution already accounted for.

## 3. What actually ran

A scratch probe used the existing VDfirst parameterized-headword implementation at commit `11bfd8df1d27a5c7f2190aade2470a8a8801dc1f`. Its temporary definition was:

```text
previous-remainder_i_r_p_c :=
    impressed-force_i_p_c + remainder_r_p_c
```

Here the fixture's `i` is an already supplied interaction handle, `r` identifies the new remainder, and `p,c` carry target and context. These signatures are test notation, not adopted entry names.

The actual REPL renders for the spring fixture were:

```text
R-before = {previous-remainder_spring-pull_after-spring_P_C0}

R-before = {impressed-force_spring-pull_P_C0} + {remainder_after-spring_P_C0}

R-before = {spring-pull_P_C0} + {remainder_after-spring_P_C0}

R-before = (-k*x) + {remainder_after-spring_P_C0}
```

`R-before` on the left is a supplied literal label for the starting quantity. The right side began as one demand; its addition syntax came from the definition. The engine did not independently verify a physical equality.

Ordinary expansion produced both right-side demands. Expanding the force left the new remainder open. Checks passed for two target/context bindings, preserved dictionary entries and engine source hashes, and used only trace creation and expansion events. The spring formula and its applicability were supplied fixture inputs; the second binding tests substitution rather than a second physical experiment.

Evidence is retained in VD-Newton at `.tools/nml3_remainder_step/probe.py` and `.tools/nml3_remainder_step/result.json`. These are local scratch artifacts, not part of this two-document handoff. The next remainder's provider was intentionally neither supplied nor expanded.

## 4. The earlier issue remains open

The probe started with `spring-pull` already supplied. It did **not** execute:

```text
impressed-force of IS(i+1)
    → impressed-force of spring
```

Resolving a demand inside a pending call's argument, then specializing that call, is still the critical untested stage. The inspected branch supplies flat atomic argument substitution; this record does not establish native support for the nested form.

The earlier named-cell summation and residual-fold experiments provide separate evidence, described in the [two-approach record](NML3_INTERMEDIATE_EXPRESSION_TWO_APPROACHES_2026-09-09.md). They do not complete this staged remainder algorithm. The residual fold still requires interpreter integration.

Final entry wording, signatures, triplet placement, and the terminal operation remain open. The [companion discovery record](NML3_TOLERANCE_SPECIAL_ZERO_AND_NET_FORCE_UNCERTAINTY_DISCOVERY_2026-09-09.md) develops what investigating termination revealed about tolerance and uncertainty. It supplies a conceptual direction, not a completed implementation.

## 5. Sources and custody

The primary source is the user-led discussion in the VD-Newton task **Review NML3 trace progress**, 2026-09-09: the black-box clarification, the previous-remainder relation, and the proposed `IS(i+1)` staging. Task identifier: `01a085b5-69da-7072-8a33-854ce9565cff`.

Managed context was consulted at **`canvalidk/VD-docs@0ad969e068e77175e86f6fe8dd24e6f9f7a965ce`**, reconfirmed as `main` when writing this record:

- [catalog.yaml](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/catalog.yaml), selecting the relevant conceptual sources.
- [NML3 Force-Sum Foundational Understanding](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02.md), especially decomposition versus membership and construction of the sum.

Local sources include the [earlier remainder-triplet proposal](NML3_REMAINDER_TRIPLET_AND_ACTING_OBJECT_DISCOVERY_PROPOSAL_2026-09-09.md), the [membership/summation distinction](NML3_MEMBERSHIP_AND_SUMMATION_LOOPS_2026-09-07.md), and the two-approach record above. The August 26 naming decision remains at `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`; the newer remainder naming remains a proposal. No final entry cut is adopted here.

The managed conceptual copy preserves earlier vocabulary; the local steering supplies the current interaction/impressed-force distinction. This was a scoped reading of those sources and the executed evidence, not an exhaustive NML3 review. The current `outbox/VD-Newton/` receipt was checked; it concerns the already closed mass-estimator pass and does not receive these new records.
