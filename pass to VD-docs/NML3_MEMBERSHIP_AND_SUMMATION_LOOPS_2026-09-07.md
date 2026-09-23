# NML3: membership construction and summation are separate recursive jobs

**Date:** 2026-09-07.
**Status:** user-prompted design record and investigated interpretation. The
distinction and desired trace are recorded; a two-loop architecture, entry cut,
wall assignments, and final wording are not selected here.
**Submission:** awaiting transfer to VD-docs. Saving in `pass to VD-docs/` does
not mean the managed collection has received this record.

## 1. The realization to preserve

The user recalled that the original NML3 loop was intended to implement a
recursive list defining the interaction set. The subsequent objection was that
membership could not be established through the global force-sum constraint.
That objection does not remove the possible use of recursion. Two different
jobs had been combined:

1. Establish which interactions belong to the target's interaction set, and
   establish when that account is complete. This mechanism remains to be built.
2. Traverse those interactions, exposing each one's target-directed
   `impressed-force` and composing the contributions to obtain `net-force`.

The second job can retain a recursive implementation even though it cannot do
the first job's evidential work. Two explicit loops are one possible design;
the distinction between their responsibilities survives other designs.

The requested output from the summation side is an exposed expression:

```text
0 + impressed-force(interaction-1 -> p | C)
  + impressed-force(interaction-2 -> p | C)
  + ...
```

Each member-specific call must remain available for further expansion. The
desired route reaches expressions such as `F_net = -k*x + m*g` through those
calls. This is more demanding than supplying a numerical list to a host-language
sum and subsequently reporting which entries justified the arithmetic.

## 2. Membership construction: what recursion would have to expose

For fixed target p and context C, let S denote `interaction-set(p | C)`.
Its members are identity-bearing interactions i. Their target-directed vector
contributions are `impressed-force(i -> p | C)`.

A prospective membership procedure could progressively expose:

```text
candidate interaction
  -> independent membership warrant for this target/context
  -> admit this interaction identity once
  -> request the next candidate or an exhaustion determination
```

This is a possible operational route to warranted knowledge of S. The traversal
does not make membership physically true merely by admitting an item to a list.
The admission must answer to the relevant interaction evidence and model.

After k successful admissions, the result is a warranted partial account
`{i1, ..., ik} subset-of S`. A finite complete account additionally needs a
licensed determination that no relevant interaction has been omitted. A
generator's current failure to produce another item is not automatically that
determination. A bounded, independently justified candidate universe is one
possible way to make exhaustion meaningful; its justification is still work.

The excluded stopping rule is:

```text
the current contributions already add to the measured net force
therefore no more interactions exist
```

Further interactions can supply cancelling contributions. Thus this rule
cannot certify completeness, and a chosen algebraic decomposition cannot
independently warrant its members.

The restriction concerns this use of the resultant as membership evidence.
It does not prohibit every procedure involving a global claim: completeness
itself is a claim about the whole account, and can have independent evidence.

## 3. Summation traversal: recursion over a supplied membership domain

For the finite case, choose a traversal representation
`L = [i1, ..., in]` of S, containing each interaction identity exactly once.
The order belongs to this traversal representation; it need not be part of
the physical set's identity.

A schematic accumulator recurrence can construct the requested expression:

```text
emit([], A)        = A
emit(i :: rest, A) = emit(rest, A + impressed-force(i -> p | C))

emit(L, zero-force-vector)
```

Here A is an accumulated expression: adding a term may leave that term as an
unexpanded headword call. For two members, the visible stages are:

```text
0
0 + impressed-force(i1 -> p | C)
0 + impressed-force(i1 -> p | C) + impressed-force(i2 -> p | C)
```

These are pseudocode and display notation, not adopted VD headwords or syntax.
The initial 0 is the additive identity in the relevant force-vector space.
It is a seed for aggregation, not evidence that the physical interaction set
is empty. A closed empty interaction set is the case where this seed alone
is the complete resultant.

This recurrence terminates because each step consumes one list cell and an
empty-tail case exists. The statement **“this traversal is exhausted”** is
different from **“these are all the relevant interactions.”** Exhausting an
incomplete input list produces its complete partial sum, not a licensed total
net force. An open account can expose a partial expression, with an unresolved
remainder; it must not silently replace that remainder by zero.

Two equal-valued interactions still produce two terms. For example, distinct
i1 and i2 each contributing f must yield `0 + f + f`. Converting the returned
vectors into an ordinary set before summing would discard that multiplicity.

Exact finite vector addition gives the same resultant for different traversal
orders. Intermediate text and demand order can differ. Infinite accounts,
convergence rules, and floating-point order effects are outside this finite
trace proposal.

## 4. Member expansion and the spring/gravity trace

There is a third operation inside this account: instantiate and expand the
force expression belonging to a particular admitted interaction. It can occur
during summation or after the symbolic sum has been exposed.

For a scalar vertical example, take downward as positive and x as the spring's
signed extension from its natural length. Assume an ideal Hookean spring,
constant downward gravitational field, and independently closed membership
consisting of spring and gravity for the stated target/context. Then:

```text
independently closed interaction set: {i-spring, i-gravity}
  -> traversal: [i-spring, i-gravity]
  -> 0 + impressed-force(i-spring -> p | C)
       + impressed-force(i-gravity -> p | C)
  -> 0 + (-k*x) + impressed-force(i-gravity -> p | C)
  -> 0 + (-k*x) + (m*g)
  -> -k*x + m*g
```

The first arrow requires membership/closure evidence. The next exposes one
call per member. The following arrows require the member's force provider,
its applicability, and target/context bindings. Removing the leading zero is
an algebraic interpretation step. Beta-like substitution alone supplies
neither a physical force law nor algebraic simplification.

An admitted member can also have an unknown force value. Its call should remain
visible and unresolved rather than disappearing from the set. With independent
membership closure, independently known net force, and all other contributions
known, the Force-Sum relation can instead determine that member's value by
subtraction. This does not establish the member's existence from the residual.
The proposed forward summation loop therefore does not exhaust the meaning or
allowed orientations of the Force-Sum triplet.

## 5. What was found and executed in VDfirst

The parameterized implementation is on
[`codex/parameterized-headwords` at `11bfd8df1d27a5c7f2190aade2470a8a8801dc1f`](https://github.com/canvalidk/VDfirst/tree/11bfd8df1d27a5c7f2190aade2470a8a8801dc1f).
The local main checkout used in the earlier Newton II trace does not contain
this implementation.

The branch implements **flat partial instantiation**: a selected entry's
supplied actuals replace formal symbols simultaneously, then the resulting
text is tokenized. Known calls introduced by substitution become further lazy
demands. It is beta-like substitution, with genuine closures, alpha-renaming,
capture avoidance, and nested expression arguments explicitly deferred.

A small probe was executed against seven unchanged Python modules fetched at
that commit into an ignored local scratch directory. No VDfirst branch was
checked out or edited. The probe used these **test-only entries**:

```text
impressed-force_i_p_c := i_p_c
spring-pull_p_c      := (-k*x)
gravity-pull_p_c     := (m*g)
```

This fixture makes one possible interface concrete: an interaction handle
names a callable provider for the force on a target in a context. That
interface is a candidate bridge, not a ratified definition of interaction
identity or impressed force. The supplied kernels are scoped to the fixed
example; the fixture does not validate their applicability for arbitrary
targets or contexts.

Actual simulator renders were:

```text
0 + {impressed-force_spring-pull_P_C0}
  + {impressed-force_gravity-pull_P_C0}

0 + {spring-pull_P_C0}
  + {impressed-force_gravity-pull_P_C0}

0 + (-k*x) + {impressed-force_gravity-pull_P_C0}

0 + (-k*x) + (m*g)
```

The final worklist was empty. All changes of expression above came from
ordinary expansion and explicit return through the branch's REPL; no injected
answer or arithmetic reduction was needed. The probe supplied the initial
sum expression, membership, and kernel definitions. It therefore verifies the
member-call expansion path, **not either proposed loop**.

One concrete syntax constraint matters: this branch uses underscores as
positional argument separators. A mathematical label such as `interaction_1`
cannot be placed unchanged inside one atomic argument; use an atomic handle
such as `interaction-1`. The branch also accepts only one formal-parameter
list per headword stem. Nested list expressions as call arguments and an
automatic empty/cons dispatcher are not established by this probe or supplied
by beta substitution alone.

The existing active Newton entries have not been migrated to these signatures.
In particular, old static underscore qualifiers must be reviewed when using a
branch where every underscore suffix is positional.

## 6. Architecture remains open

The distinction permits several implementations:

| Shape | How it would work | Obligation retained |
|---|---|---|
| Two separate traversals | Build/close an interaction list, then emit and expand its force terms. | Establish membership and closure before calling the result total net force. |
| A lazy producer and consumer | Admission emits members; the consumer emits corresponding force terms as they become available. | A partial expression remains provisional until independent closure; ending consumption cannot manufacture closure. |
| A supplied closed account plus one traversal | Another layer provides S and its closure evidence; NML3's forward route traverses S. | Record who supplied that account and why it is accepted. |
| A relational account and summation expression | Represent membership relationally and expose an indexed sum without a materialized recursive list. | Preserve identity, target/context, all-and-only coverage, and demandable member calls. |

The entry graph's mutually referencing triplet is also distinct from these
operational traversals. A cycle of definitions by itself supplies neither a
decreasing list tail nor a base case. A productive recursive implementation
must expose the changing state and termination case somewhere. The sum of a
remaining tail should not be silently identified with the original target's
whole net force; its partial-domain meaning needs its own explicit expression
or state representation.

Decisions still needed include:

1. The membership-warrant interface, candidate scope, and independent closure
   evidence, including how a genuinely empty account is recognized.
2. Interaction identity and duplicate handling; the target/time/context address
   shared by membership and each impressed-force call.
3. List, iterator, named-tail, or relational representation; the location of
   empty/next cases and any needed helper entries or residual operations.
4. Whether force-call emission and expansion are staged or interleaved, and how
   a partial account or unknown member value stays visible.
5. How an admitted interaction routes to an applicable target-directed force
   provider: callable handles, explicit lookup, witnesses, or another protocol.
   Parameter substitution does not choose this protocol.
6. Which steps are dictionary expansion, interpreter operations, and supplied
   evidence, and how each appears in the trace.
7. Entry cut, wall assignments, and numbering. The 2026-08-17 reset remains in
   force; this note does not reinstate the retired E13–E17 structure.

The immediate acceptance target is the user's visible expression with one
parameterized `impressed-force` call per independently admitted interaction,
followed by inspectable expansion to a force expression such as `-k*x + m*g`.
This is a useful target before committing to either a general list language
or a two-loop architecture.

## 7. Relationship to the earlier numerical trace

The preceding Newton II demonstration supplied two force vectors and summed
them in the Python replay driver before submitting a REPL reduction. It showed
that the older trace machinery could record an interpreter-guided answer.
It did not implement a per-member sum expansion or beta-like force lookup.

This realization sharpens what the next trace should expose: the middle
expression, where membership has supplied identifiable interactions but the
individual force calls have not yet been reduced. The new probe establishes
that the branch's substitution machinery can support that middle-to-kernel
step with an explicit provider interface.

## 8. Sources, custody, and coverage

**Primary new input:** the user's 2026-09-07 realization in the Newton trace
task: distinguish membership construction from the original sum-producing
loop, keep a two-loop design optional, and expose member-specific
`impressed-force` calls before expansion.

**Managed sources:** one resolved main snapshot,
`canvalidk/VD-docs@743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6`.
`catalog.yaml` selected these files; their relevant conceptual and boundary
passages were inspected:

- [NML3 entry-structure reset](https://github.com/canvalidk/VD-docs/blob/743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6/Newton/nml/nml3/NML3_ENTRY_STRUCTURE_RESET_2026-08-17.md): preserves conceptual results and retires the old entry cut.
- [Warranted force-account explication](https://github.com/canvalidk/VD-docs/blob/743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6/Newton/nml/nml3/conceptual/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md): distinguishes membership warrant and completeness from resultant matching.
- [Force-Sum member-value relation](https://github.com/canvalidk/VD-docs/blob/743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6/Newton-analysis/_dscn_entry_structure/force_sum_member_value/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md): separates membership closure from value completion and preserves inverse determination of an already admitted member's value. The catalog identifies this un-suffixed record as superseding the adjacent d1; the d1 was not used as current authority.

**Active local sources:** the August 12 and August 26 NML3 naming decisions;
`08_nm_lesson_drafts/nml3/NML3_ENTRY_WORKING_PLAN.md`;
`NML3_GENERATOR_NONTERMINATION_CLOSURE_CONSTRAINT_2026-08-08.md` in that folder;
the local warranted-force-account explication, especially its generator/closer
sections; and
`07_design_2_1/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md`, especially
its construction/aggregation, ordering, map/fold, and multiplicity passages.
Historical names in these sources are translated using the ratified
`interaction-set / impressed-force / net-force` terminology.

The local generator note explicitly records the successor-without-base-case
problem; its filename was not found in this catalog. Its own submission claim
is dated against an earlier snapshot, so no inference is made that equivalent
content is absent everywhere in managed storage. The managed catalog records
the local warranted explication as an authoritative retained source; its
managed received version lacks the explicit recursive section inspected in the
local version. Neither copy was reconciled or changed. The local abstraction
boundary note remains on its retained production surface under the workspace's
custody record.

**Code evidence:** VDfirst commit
`11bfd8df1d27a5c7f2190aade2470a8a8801dc1f`, including
[`application.py`](https://github.com/canvalidk/VDfirst/blob/11bfd8df1d27a5c7f2190aade2470a8a8801dc1f/application.py),
[`the parameterized-headword spec`](https://github.com/canvalidk/VDfirst/blob/11bfd8df1d27a5c7f2190aade2470a8a8801dc1f/specs/2026-09-01-vd-parameterized-headwords.md),
`engine.py`, `simulator.py`, `repl.py`, `demand.py`, `definiens.py`,
`residual.py`, and `test_parameterized_repl.py`.

**Execution artifacts:**
`03_trace_and_evaluator/nml3_beta_force_probe.py` and its adjacent JSON contain
the exact fixture, source hashes, command transcript, events, renders, and
assertions. They remain active local evaluator work. The source modules used
for execution are an ignored scratch snapshot under
`.tools/nml3_beta_probe/11bfd8d/`, not another maintained code checkout. The
probe accepts `--code-root` for a checkout of the same commit.

Selection was scoped to NML3 membership, generator/closure, map/fold and
summation, and the parameterized branch's substitution path. This is not an
exhaustive synthesis of all NML3 or an implemented membership/summation engine.
No managed source, current entry, or VDfirst repository file was edited.
