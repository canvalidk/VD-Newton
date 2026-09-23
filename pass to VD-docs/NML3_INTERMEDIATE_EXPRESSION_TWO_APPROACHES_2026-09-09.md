# NML3 intermediate expression: two approaches to its construction

**Date:** 2026-09-09.  
**Status:** user-requested record of the discussion and the work demonstrated so far. The residual-fold mechanism has been demonstrated in scratch; the accumulator/remainder equality is a working design idea. Neither is an installed Newton entry implementation.  
**Submission:** awaiting transfer to VD-docs. Saving this record in `pass to VD-docs/` does not mean the managed collection has received it.

## 1. The intermediate expression and the problem

For a fixed target particle `p` and context `C`, suppose the interaction set is already fully formed. Its members are identity-bearing interactions. Each interaction supplies a target-directed `impressed-force`, and their sum gives `net-force`.

The desired intermediate expression exposes one still-expandable force call for each member:

```text
0 + impressed-force(interaction-1 -> p | C)
  + impressed-force(interaction-2 -> p | C)
  + ...
```

This is intermediate because the interactions have been enumerated but their force calls have not yet been expanded into the applicable force expressions. For a supplied spring-and-gravity example, that later expansion can produce:

```text
0 + (-k*x) + (m*g)
```

With the corresponding one-dimensional sign convention, this gives the intended route to `F_net = -k*x + m*g`. Removing the leading zero is a further simplification. In a vector treatment, the initial zero is the zero force vector.

The construction problem is how the entries and interpreter should produce the intermediate expression. At the end of each iteration, the trace must retain the contributions already exposed and have a way to continue through the remaining interactions. Those retained force calls must remain available for subsequent expansion. Supplying the complete expression from outside the trace would not demonstrate this construction.

An additional constraint from the discussion is that the original statement must contain all three words:

```text
net-force / impressed-force / interaction-set
```

The old member-and-tail list structure gives a possible traversal mechanism: opening a cell exposes one member and the remaining list. For a finite enumeration of `n` interactions, there are `n` term-producing iterations, followed by termination at the empty tail.

Both approaches below concern consumption of an already-established interaction set. They do not establish membership or closure. Membership must remain independently warranted; agreement with a resultant cannot establish it. Distinct interactions must remain distinct even when their force values are equal or cancel. The traversal order is an implementation choice, rather than a new ordering of the physical set.

The user also observed that people usually skip the explicit term-by-term buildup. There is consequently no requirement that this bookkeeping imitate an elegant human reasoning procedure. A mechanical implementation can be adequate if it preserves the required meaning and produces the expression correctly.

## 2. Approach one: construct the expression through a residual fold

### The proposed statement

The fold formulation keeps the three words visible in the original statement:

```text
net-force(p,C) :=
  foldl((A,i) => A + impressed-force(i,p,C),
        0,
        interaction-set(p,C))
```

Here `A` is the accumulator and `i` is the current interaction. The body says how to construct the next accumulator. The initial accumulator is `0`.

For each member, the interpreter binds `i`, inserts the existing expression for `A`, and continues with the tail. Showing only the accumulator, a spring-and-gravity traversal progresses through:

```text
0
0 + impressed-force(spring)
0 + impressed-force(spring) + impressed-force(gravity)
```

Target and context arguments are suppressed in this illustration; the executed calls retain them. At the empty tail, the fold returns the accumulated expression. The force calls can then be expanded.

### How the scratch implementation works

The prototype represents `A` as a piece of expression with unresolved headword holes. This allows the whole previous expression to be inserted into the next body without passing a compound expression as an atomic headword argument.

One iteration performs these operations:

1. Expand the next supplied list cell into a member and a tail.
2. Use the parameterized-headword implementation's flat substitution to bind the member variable in the body.
3. Treat the accumulator variable as a local hole and use the existing residual fill operation to insert the previous accumulator.
4. Retain the resulting force calls as open and continue with the tail.

The fold handler keeps the body suspended until the member variable is bound. The addition syntax comes from the authored body. Changing the body's `+` to `-` in a diagnostic counterfactual changed the emitted expression accordingly; the driver was not independently manufacturing the force-sum formula.

The executable scratch spelling was:

```text
net-force_p_c :=
  foldl [a,i => a + impressed-force_i_p_c] 0 interaction-set_p_c
```

The engine recognized both `impressed-force` and `interaction-set` as references in the right-hand side. This addressed the problem in the preceding callback experiment, where `impressed-force` occurred inside another call's argument string and was not recognized as a separate dependency.

### What has been demonstrated

The scratch interpreter produced the following intermediate expression with actual open force calls:

```text
0 + {impressed-force_spring-pull_P_C0}
  + {impressed-force_gravity-pull_P_C0}
```

Braces here mark unresolved headword holes. Subsequent dictionary expansion and flat argument substitution produced:

```text
0 + (-k*x) + (m*g)
```

Checks passed for an empty list, a singleton, spring and gravity together, reversed traversal, and distinct interactions with equal force values. They checked one additional member-specific call per iteration and preservation of the earlier calls. The probe also rejected repeated identities, cyclic lists, and a missing tail definition.

These are checks of the proposed mechanism against supplied fixtures. The membership account, finite enumeration, target/context, and force-provider applicability were supplied. The prototype does not implement general lambda evaluation. The existing engine can also leave an unknown provider as ordinary residual text; absence of open holes therefore does not itself certify a successfully evaluated physical force.

### The interpreter change this requires

The user identified the central consequence: this approach makes the term-producing iteration residual work. It requires that residual work be able to return an expression containing active headword calls.

For example, the bound template `impressed-force(i)` produces separate calls for `interaction-1`, `interaction-2`, and so on. These are additional occurrences of an existing headword. They must become demands that can subsequently be expanded.

The current interpreter does not permit this through its residual-reduction operation. In the inspected code, reduction requires a fully resolved node and rejects replacement text containing recognized headwords. Escaping a word would make it literal rather than creating the active call needed here.

The scratch prototype operates directly on the underlying expression objects and adds its own fold handling. It demonstrates the transformation but bypasses the current REPL's restrictions. Supporting it normally requires a change to the permitted role of residual work as well as implementation work: binding, creation of active calls, and their continued tracking must be supported. Merely accepting a replacement string would not supply that behavior.

**Current position:** the construction mechanism is substantially resolved and demonstrated in scratch. Interpreter integration and the corresponding rule change remain to be done. No production entry or VDfirst checkout was changed by the experiment.

## 3. Approach two: give the accumulator meaning through an equality

### The proposed relation

The user's alternative began with:

```text
F_net = F_g + Remaining_force
```

The subsequent clarification was that this gives meaning to the **accumulator**. The general form is:

```text
F_net = A + Remaining_force
```

`A` is the contribution already accounted for. Its intermediate value has an explicit relationship to the total force: together with the contribution of the unprocessed interactions, it gives `F_net`.

The first approach already accumulates a partial sum. This proposal makes the equality relating that partial sum to the whole explicit at every stage.

### How an iteration would preserve the statement

Let `S` be the established interaction set and `T` its unprocessed members. Write `R(T)` for their total impressed-force contribution. Then the maintained statement is:

```text
F_net = A + R(T)
```

Initially, `A = 0` and `T = S`. When a member `i` is taken from `T`, write the old remainder as a disjoint member-and-tail decomposition. Schematically:

```text
R({i} union T') = impressed-force(i) + R(T')
```

Here `i` is not in `T'`. Substituting this into the maintained statement gives:

```text
F_net = A + impressed-force(i) + R(T')
```

The new accumulator is `A + impressed-force(i)`, and the new remaining set is `T'`. Each iteration preserves an equality for the same total force.

For gravity followed by a spring, with `F_g` and `F_s` standing for their respective impressed-force calls:

```text
F_net = 0 + R({gravity, spring})
F_net = F_g + R({spring})
F_net = (F_g + F_s) + R({})
F_net = F_g + F_s
```

The accumulators are successively `0`, `F_g`, and `F_g + F_s`. Each has meaning through its place in the equality. The base case is `R({}) = 0`.

`R(T)` is a subtotal over the remaining warranted interactions. It does not introduce an extra physical interaction. Nor does the equality license choosing members to fit a measured total. Termination follows from exhausting the established enumeration; a zero-valued remainder alone would not prove that no members remain, because contributions can cancel.

### What has been established and what remains open

The invariant and the schematic update are understood. They explain how the accumulator can have an explicit meaning throughout the construction, while every complete statement continues to concern the same `F_net`.

The VD entry implementation has not been worked out or executed. Open points include:

- How the initial statement and entry group express the invariant while satisfying the three-word constraint.
- How the current member, remaining set, and accumulated expression are represented and passed through the trace.
- Which updates come from dictionary expansion and which require residual work.
- Whether this route can use the existing interpreter rules, or also requires changing them.

`Remaining_force` and `R(T)` are working notation. They have not been adopted as new headwords or assigned final entry roles. The mathematical recurrence alone does not establish that its steps are licensed operations in the current interpreter.

**Current position:** the semantic proposal is clear, including the meaning of the accumulator and the equality preserved by an iteration. Its expression through entries and permitted interpreter operations remains work in progress.

## 4. Where the two approaches stand

| Question | Residual fold | Accumulator/remainder equality |
|---|---|---|
| Central mechanism | The interpreter repeatedly applies a body to build the expression. | Each update preserves `F_net = A + R(T)`. |
| What is established? | A working scratch mechanism, with deferred force calls and checked examples. | The accumulator's meaning, the invariant, and its schematic update. |
| Three-word constraint | Met by the tested original fold statement, including both right-hand-side references. | Still to be met in the eventual entry formulation. |
| Interpreter status | Requires residual work to produce active headword calls; not integrated into the normal REPL. | Requirements not yet settled; no claim that it avoids the existing restriction. |
| Main remaining work | Specify and integrate the interpreter rule, then develop production entries. | Develop the entries and trace operations, then test them. |

These are two directions at different stages of development. They are not necessarily incompatible: a fold could also maintain the explicit equality. No combined implementation has been demonstrated. Neither approach resolves the separate membership-construction problem or selects the final NML3 entry cut.

## 5. Sources and scope

The primary source for the distinction between these approaches, including the clarification about the accumulator, is the user-led discussion of 2026-09-08/09. This record preserves that discussion and the evidence already produced; it does not ratify final entries or change interpreter policy by itself.

Managed context was checked through the GitHub connector at the single resolved VD-docs `main` commit **`adfe14bbaafb29856f0a30da088495b7c9d483d2`**. The scoped sources were:

- [`catalog.yaml`](https://github.com/canvalidk/VD-docs/blob/adfe14bbaafb29856f0a30da088495b7c9d483d2/catalog.yaml), used to confirm managed source locations.
- [`Newton/Design 3/unfolding_forces.md`](https://github.com/canvalidk/VD-docs/blob/adfe14bbaafb29856f0a30da088495b7c9d483d2/Newton/Design%203/unfolding_forces.md), historical context for exposing recursive structure. Its earlier force-set terminology and membership proposal are not installed by this record.

Active local sources and evidence, with paths relative to VD-Newton:

- `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`: local steering authority for the three words and the interaction/contribution distinction. No matching naming-decision file was found in the inspected managed catalog; its authority here comes from the local steering material and the user's discussion.
- `pass to VD-docs/NML3_MEMBERSHIP_AND_SUMMATION_LOOPS_2026-09-07.md`: the earlier local record separating membership construction from summation traversal; its header still marks it awaiting transfer.
- `.tools/nml3_beta_probe/fold_statement_probe.py` and `.json`: the new fold handler and its saved execution evidence, inspected for this record. These are ignored local scratch artifacts, not files delivered to VD-docs with this document.
- The unchanged VDfirst source used by that probe is pinned to **`11bfd8df1d27a5c7f2190aade2470a8a8801dc1f`**, from `codex/parameterized-headwords`, in `.tools/nml3_beta_probe/11bfd8d/`. Relevant files are `application.py`, `definiens.py`, `residual.py`, `engine.py`, `simulator.py`, `demand.py`, and `repl.py`. The saved probe includes their hashes. `repl.py`'s `cmd_reduce` and `_apply_reduction` were also inspected to confirm the existing restriction on residual reductions.

This was a scoped review of the conversation, named local implementation evidence, and the cited managed context, rather than an exhaustive review of the NML collection. The later equality approach has no executed prototype in this evidence set.
