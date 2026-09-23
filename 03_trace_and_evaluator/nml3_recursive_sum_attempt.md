# NML3 recursive sum — implementation attempt

**Status:** candidate operational entry group, executed 2026-09-08. Not an
accepted NML3 cut; no E-numbers assigned. Entry roles within the eventual
triplet/house remain open. This implementation note belongs with the local
trace/evaluator work.

## Purpose and result

Consume a fully supplied finite traversal of an independently closed
interaction set and produce:

```text
0 + impressed-force(i1 -> p | C) + impressed-force(i2 -> p | C) + ...
```

Each iteration must leave one additional force call and one continuation for
the remainder. The force calls remain unexpanded until the intermediate sum
has been exposed. This is the user's requested next step after recognizing
the old member-plus-remainder structure as suitable for summation traversal.

The attempt works on the pinned parameterized-headword implementation. For
spring and gravity the actual trace produced:

```text
0 + {impressed-force_spring-pull_P_C0} {cell-1_emit-force_P_C0}

0 + {impressed-force_spring-pull_P_C0}
  + {impressed-force_gravity-pull_P_C0} {list-end_emit-force_P_C0}

0 + {impressed-force_spring-pull_P_C0}
  + {impressed-force_gravity-pull_P_C0}

0 + (-k*x) + (m*g)
```

Braces mark actual simulator demand holes. Line breaks above aid reading; the
saved JSON retains the original renders, including a harmless trailing space.

## Draft operational entries

The branch accepts atomic named arguments. A list cell can therefore be a
callable entry that passes its stored member and tail to a supplied step.
`l` is a list handle, `i` an interaction/provider handle, `tail` the next list
handle, `p` the target, and `c` the fixed context.

```text
sum-interactions_l_p_c :=
    0 l_emit-force_p_c

emit-force_i_tail_p_c :=
    + impressed-force_i_p_c tail_emit-force_p_c

list-end_step_p_c :=
    ""
```

`""` means an actual empty definition string, not two quote characters.

| Candidate | Role and intended residual effect | Reads | Leaves in the trace |
|---|---|---|---|
| `sum-interactions_l_p_c` | Operational starter: introduce the additive identity and demand traversal. | Supplied list handle, target, context. | `0` followed by the first list call. |
| `emit-force_i_tail_p_c` | Operational recursive step: append one force term and demand the tail. | Current member identity, tail handle, target, context. | `+ impressed-force_i_p_c` and `tail_emit-force_p_c`. |
| `list-end_step_p_c` | Operational base case: the supplied traversal has no more cells. | End-of-list representation. | Empty text; no further traversal demand. |

The additive identity is already present before the first iteration. Empty
text ends the emitted sequence of terms. It does not supply a zero-valued
interaction, certify physical closure, or silently drop an unknown force.
For the vector reading, the leading 0 is interpreted as the zero force vector;
the present engine treats it as residual text without checking its type.

## Supplied list representation

For the example the membership input is encoded as these two cells:

```text
cell-0_step_p_c := step_spring-pull_cell-1_p_c
cell-1_step_p_c := step_gravity-pull_list-end_p_c
```

These are data-bearing fixture entries, not a discovery procedure. They
contain only member identities and tail links, with no `+` or force-expression
syntax. The consumer never reads a numerical force value from a list cell.

Calling a cell with `step = emit-force` substitutes that argument, exposing
the shared step entry. Expanding the shared step leaves the next tail call.
This is the old next-member/remaining-tail mechanism expressed with the
branch's actual argument-substitution facilities.

## First iteration, one expansion at a time

Start with:

```text
sum-interactions_cell-0_P_C0
```

1. Expand the starter:

   ```text
   0 {cell-0_emit-force_P_C0}
   ```

2. Expand the cell. Substitution binds its step to `emit-force`, exposing its
   stored member and tail:

   ```text
   0 {emit-force_spring-pull_cell-1_P_C0}
   ```

3. Expand the step. Substitution binds `i = spring-pull`, `tail = cell-1`,
   `p = P`, and `c = C0`:

   ```text
   0 + {impressed-force_spring-pull_P_C0} {cell-1_emit-force_P_C0}
   ```

The first iteration is now complete. Select the tail demand while retaining
the force call as open. The second iteration repeats steps 2–3 using `cell-1`.
Expanding `list-end_emit-force_P_C0` ends traversal. For n members there are n
step expansions, plus a starter, n cell dispatches, and one terminal expansion.
The driver need not know n to select the next remainder demand.

## Connection to foldl

The semantic target remains:

```text
foldl (lambda a i: a + impressed-force(i -> p | C)) 0 L
```

This encoding specializes that target to producing its infix addition text.
The emitted `0 + f1 + f2` is read with left-associative addition. The prefix
already present in the parent trace carries the accumulated expression, so
there is no need to pass a compound expression such as `(0 + f1)` as an atomic
argument on each call.

This is an expression-emitting implementation for the requested addition
case. It is not a general `foldl` evaluator with arbitrary operators,
accumulator types, closures, or nested expression arguments. Choosing whether
to generalize it is a later implementation decision.

## Expanding the force calls

The same provisional provider interface as the preceding beta probe is used:

```text
impressed-force_i_p_c := i_p_c
spring-pull_p_c      := (-k*x)
gravity-pull_p_c     := (m*g)
```

The interpretation is scoped to target P and context C0: a vertical ideal
spring and gravity, downward positive, x measured from the spring's natural
length. Their applicability and the membership account are supplied inputs.
The code does not infer either physical kernel.

Selecting the deferred spring call exposes `spring-pull_P_C0`, then `(-k*x)`.
The gravity call similarly exposes `(m*g)`. This gives `0 + (-k*x) + (m*g)`.
Removing the zero or evaluating arithmetic is a later residual operation.

## Intended logic and boundaries

**Allowed:** enumerate every supplied interaction identity once, carry target
and context through every call, emit its force call, preserve pending calls,
and terminate at the supplied end of the list.

**Blocked:** infer membership from a force sum; treat equal-valued distinct
interactions as duplicates; infer closure from running out of investigated
candidates; evaluate all forces before exposing the sum; introduce a fake
zero-force member; or manufacture the answer in the replay driver.

**Trace-critical references:** the step must expose both the member-specific
`impressed-force` call and the call on the tail. The prefix is retained by the
parent demand structure. Choosing the remainder first is an explicit
interpreter policy, not an automatic engine strategy.

**Witness/inputs:** a finite, duplicate-free enumeration of the given closed
interaction set; identity-bearing members; target/context; applicable force
providers. This attempt does not yet define the route by which `net-force(p|C)`
obtains this enumeration from a general `interaction-set(p|C)` entry.

**Missing input:** absent provider definitions must not be treated as evidence
that a force has been evaluated. The current engine can leave unknown text as
residual, so structural completion alone cannot certify physical completion.
The executed fixture supplies all providers and checks their resulting text.

## Executed checks

The existing branch's REPL was driven through `trace`, `goto`, `expand`, and
`return`, with automatic cleanup/reduction disabled. No `inject`, `recall`,
`flatten`, or `reduce` operation occurred. Python constructed the supplied list
data and chose demanded expansions; the only producer of addition syntax was
the shared entry definition. Expected strings were constructed separately for
assertions and were never supplied to the trace.

Five cases passed:

- Spring and gravity: two open member-specific calls, then `0 + (-k*x) + (m*g)`.
- Empty list: `0`, with no emitted force call.
- Singleton: one emitted call, then `0 + (-k*x)`.
- Distinct interactions with equal values: both calls retained, then
  `0 + (-k*x) + (-k*x)`.
- Reversed traversal: corresponding reversed call order, then
  `0 + (m*g) + (-k*x)`.

Checks also verified one new force call and one remaining tail after each
iteration, exactly one terminal expansion, no open demands after force
expansion, unchanged dictionary entries, and unchanged engine source hashes.
The diagnostic driver has a bounded expansion guard; it does not prove
termination for malformed or cyclic input lists.

## Sources, artifacts, and next decision

- Source status: new candidate operational group informed by the user's
  2026-09-07/08 fold and old-list discussion. This adapts the repeated
  member-plus-remainder pattern; it is not old wording copied into new entries.
- Active local sources: `NML3_ENTRY_WORKING_PLAN.md`, the August 26 naming
  decision, and `NML3_GENERATOR_NONTERMINATION_CLOSURE_CONSTRAINT_2026-08-08.md`
  under `08_nm_lesson_drafts/nml3/`.
- Historical managed context consulted during this discussion:
  `canvalidk/VD-docs@adfe14bbaafb29856f0a30da088495b7c9d483d2`, `catalog.yaml`,
  `Newton/Design 3/unfolding_forces.md`, and
  `Newton/Design 3/vd_design_3_trace_architecture (1).md`. These preserve the
  old unfolding/iteration reasoning; their force-set semantics and zero-acting-
  object proposal are not installed by this candidate. The local generator
  note records the explicit R(N) member-plus-remainder schema.
- Code: `canvalidk/VDfirst@11bfd8df1d27a5c7f2190aade2470a8a8801dc1f`, the
  `codex/parameterized-headwords` implementation already fetched into the
  ignored `.tools/nml3_beta_probe/11bfd8d/` scratch directory.
- Replay: `03_trace_and_evaluator/nml3_recursive_sum_attempt.py`.
  Evidence: the adjacent `nml3_recursive_sum_attempt.json` contains every
  entry, expansion, iteration snapshot, command transcript, and source hash.
  Pass `--code-root` to use a checkout of the same code commit.

Run from the workspace root with Python and networkx available:

```powershell
python -B 03_trace_and_evaluator/nml3_recursive_sum_attempt.py
```

The immediate decision is whether this named-cell / shared-step representation
is a suitable first entry encoding of the summation traversal. It leaves the
membership-construction loop, production provider interface, general fold
machinery, and final law/house assignments open. No installed Newton entry or
VDfirst repository file was changed. This implementation note has not been submitted to
VD-docs.
