# Proposal: put the remainder in the Force-Sum triplet

**Date:** 2026-09-09.  
**Status:** proposal written at the user's request. It argues for changing the triplet and explores a possible connection to acting-object discovery. Final entries, downstream structure, and interpreter operations remain to be developed.  
**Submission:** awaiting transfer to VD-docs; saved locally in `pass to VD-docs/`. The existing naming decision and managed documents have not been changed.

## 1. The proposed change

Change the Force-Sum triplet from:

```text
net-force / impressed-force / interaction-set
```

to:

```text
net-force / impressed-force / remainder
```

The proposed inward relation makes a decomposition explicit:

```text
net-force = impressed-force + remainder
```

The individual contribution and the remainder together account for the same total force. Further contributions can be exposed by expanding the remainder. The interaction set, member identity, activation, and closure would be designated through later entries that give this decomposition its full content.

The motivating experimental statement is the user's:

> A new acting object is one which, if impressed on an object, drives the remainder to zero/ towards zero

This sentence gives the proposal its direction. It identifies a quantity that needs explaining, a possible source of explanation, and a result by which that explanation can be tested. It suggests a way of understanding why a new acting-object enters the theory: its impressed force accounts for something the existing account leaves over.

The proposal is to make that remainder available as a named concept in the law itself, so that the later logic of discovery has something explicit to operate on.

## 2. How the expression-construction problem exposed the remainder

The immediate task was to make a VD trace construct an intermediate expression of this form:

```text
0 + impressed-force(interaction-1 -> p | C)
  + impressed-force(interaction-2 -> p | C)
  + ...
```

Each term remains available for later expansion. With supplied spring and gravity interactions, the expression can eventually become `0 + (-k*x) + (m*g)` under the appropriate sign convention. The construction must first produce the member-specific calls, before their force formulas have all been evaluated.

A residual-fold approach has already been demonstrated in scratch. It carries an accumulator `A` and adds one force call per iteration. That mechanism requires changes to the interpreter because residual work would create additional active headword calls.

The alternative observation was that each stage could state:

```text
F_net = A + remainder
```

The user clarified that this gives meaning to the **accumulator**. `A` is the contribution already accounted for, related to the same total force through what remains. For example:

```text
F_net = impressed-force(gravity) + remainder(after gravity)

F_net = impressed-force(gravity)
      + impressed-force(spring)
      + remainder(after gravity and spring)
```

Target and context are fixed throughout these schematic statements. Once the independently established account has been fully traversed, the remaining contribution is zero and the exposed terms constitute the intermediate expression.

This suggested a stronger change than adding a convenient accumulator to the implementation. The decomposition itself could organize the law. Each expansion would expose another impressed force while preserving a statement about the same `net-force`.

The remainder is a force quantity. It is distinct from the interpreter's *residual layer*, which is where certain reasoning and rewriting operations occur. Naming the force remainder does not by itself settle which interpreter operations should manipulate it.

## 3. Why this might expose the logic of acting-object discovery

The remainder becomes especially useful when the direction of inquiry changes. Suppose an independent route through motion, with the other required quantities established, constrains net force. Let `A(C)` be the contributions already accounted for in context `C`. Then:

```text
R(C) = F_net(C) - A(C)
```

This identifies what the account has yet to explain. We can investigate how `R(C)` behaves before possessing a force law for whatever contributes to it. The unknown therefore has a place in the theory before its eventual explanation is available.

That is the proposed connection to discovering a new acting-object. Experimental work can examine whether a particular source, arrangement, or condition supplies a contribution that accounts for the remainder. A candidate contribution `F_candidate(C)` gives a testable continuation:

```text
R_after(C) = R_before(C) - F_candidate(C)
```

If the candidate explains the whole outstanding contribution, `R_after(C)` is zero in the idealized account. If it explains part, the remaining discrepancy becomes the subject of further work. In measurements, the relevant comparison is with zero at the experiment's resolution, using its uncertainties.

### A magnetic-discovery scenario

Magnetism provides a conceptual test of this intended logic. This is a reconstruction of the reasoning the entries should be able to support, rather than a claim about the historical sequence of its discovery.

Suppose the target's motion and the currently understood contributions leave a reproducible remainder. Experiments vary conditions associated with a suspected source and examine whether those changes track the remainder. The work seeks an identifiable interaction and a stable relationship between the controlled conditions and its impressed force.

There are several achievements to distinguish:

1. Establishing a reproducible effect that the present account leaves unexplained.
2. Identifying an interaction or acting-object instance responsible for a contribution.
3. Recovering that contribution's force values under sufficiently controlled conditions.
4. Developing and testing a force law across those conditions.
5. Determining whether the result calls for a new acting-object kind within the theory, or an instance or refinement of an existing kind.

The remainder gives this sequence a common quantity to investigate. It does not require a magnetic force formula before the magnetic contribution can become a subject of inquiry.

Once an independently identified magnetic interaction is the only unknown contribution in an otherwise complete account, the remainder determines its impressed-force value. Before that isolation has been established, the remainder may combine several contributions. The distinction belongs in the downstream experimental logic.

This is what makes the proposed triplet promising: the law would contain an explicit opening for incomplete explanations. The later acting-object entries could explain how an experimentally supported contribution takes its place in that opening.

## 4. Reading the proposed discovery statement carefully

The user's sentence is clear about the experimental job of a candidate acting-object. Its contribution should explain an outstanding part of the target's force account. This gives “new acting-object” a role connected to observation and a criterion of success.

The phrase “if impressed on an object” needs a definite reading in the eventual entries. In this proposal, the acting-object supplies an impressed force on the target. Its proposed contribution is tested against the unexplained effect. Accounting for that contribution reduces the remainder of the same force account.

Physically introducing a source into an experiment can change the target's motion and net force as well. Such an intervention is useful evidence when the resulting changes are tracked. It is not equivalent to subtracting a freely chosen force from an unchanged observation. The aim is to identify the contribution responsible for the effect.

A possible expanded reading of the sentence is:

> A candidate acting-object gains experimental support when its identifiable impressed-force contribution accounts for a reproducible part of the remainder, with a complete explanation bringing that remainder to zero within experimental resolution.

This elaborates the user's proposal; it is not final entry wording. It preserves the central idea while making the experimental association between the candidate and the contribution explicit.

### What “towards zero” would mean

“Towards zero” expresses the aim of improving the explanatory account across controlled experiments. A force remainder is a vector, so a precise experimental procedure will need to specify how agreement is assessed, including uncertainty and which conditions are varied.

It cannot be a requirement that every correct contribution, considered in any arbitrary order, makes the remainder smaller in magnitude. Opposing contributions can cancel; correctly accounting for one can temporarily enlarge the remainder. The completed account must reproduce the net force, and controlled experiments must support how its contributions are attributed.

Likewise, zero remainder in one condition does not establish completeness: omitted contributions can cancel. A candidate also cannot earn recognition solely because an adjustable expression was chosen to fit the discrepancy. Its source, conditions of action, and behavior across further tests give the proposed explanation empirical content.

These points define work for the later entries. They do not remove the usefulness of the sentence as an organizing proposal. The remainder supplies the question; experimentation establishes what can answer it.

## 5. What would move downstream, and what must survive

Moving `interaction-set` out of the immediate triplet changes where the full accounting structure is introduced. It does not eliminate the need for that structure.

The downstream entries would need to establish:

- **What the remainder is relative to:** the target, frame/context, and contributions already accounted for.
- **Which contributions belong to the account:** identity-bearing interactions, their conditions of action, and their target-directed impressed forces.
- **How another contribution is exposed:** the relation between the old remainder, the next impressed force, and the new remainder.
- **When the account is complete:** independently supported membership and closure, including the valid empty case.
- **How experiment bears on an unknown contribution:** controlled variation, identification of its source, recovery of force values, and testing of a proposed force law.

The formal relation connecting net force to all of its member contributions must remain available. Repeatedly decomposing the remainder should recover that relation. The proposal changes the concept made immediate in the triplet and asks the later structure to make the full account explicit.

This is a deliberate departure from the earlier Force-Sum placement argument. That argument required the closed interaction set and individual impressed-force value to be exposed together in the triplet, partly because the relation must support inverse force determination and force-law discovery. The new proposal retains that experimental requirement but suggests that `remainder` is the more useful immediate concept for reaching it.

The burden on the proposed re-cut is therefore concrete: show that later entries preserve the member/value distinction, independent closure, and inverse use of the force relation, while giving the remainder enough content to support both unfolding and experimental inquiry. These requirements have not yet been discharged by a completed entry group.

## 6. Why this is a VD clarification, and the present status

The need for the remainder emerged from trying to make the entries produce an expression. That implementation question exposed a concept with a wider role: the portion of an account that is still to be explained.

Naming that concept connects several activities that previously appeared farther apart:

```text
expose one contribution in a trace
    -> preserve the meaning of the accumulated contribution
    -> identify what remains to be accounted for
    -> investigate a candidate source of that contribution
    -> test whether its impressed force explains the remainder
```

The proposed understanding of Newtonian force accounting includes this experimental direction. Known acting-objects help determine a resultant; an independently constrained resultant also helps investigate the contributions that the account does not yet explain. The remainder gives that second direction an explicit place in the vocabulary.

**Proposed decision:** develop `net-force / impressed-force / remainder` as the replacement Force-Sum triplet, and place the interaction-set and discovery machinery downstream. The quoted discovery statement is a guiding proposition to develop and test, not yet a sufficient definition of a new acting-object.

**Work completed:** the accumulator/remainder relation has been identified and its connection to experimental inquiry articulated. The separate residual-fold experiment demonstrated expression construction, as recorded in the earlier two-approach document.

**Work still open:** the replacement entries and their signatures; the downstream membership and discovery structure; how the remainder will be represented in the trace; the interpretation of experimental progress towards zero; and whether this route requires the same interpreter extension as the residual fold. No new prototype of the proposed triplet has been executed.

## Sources and provenance

The primary source is the user-led discussion of 2026-09-09, particularly the proposed replacement of `interaction-set` by `remainder`, the clarification that the equality gives meaning to the accumulator, and the discovery statement quoted in section 1.

Managed sources were selected using `catalog.yaml` and consulted coherently at the resolved VD-docs `main` commit **`adfe14bbaafb29856f0a30da088495b7c9d483d2`**:

- [`catalog.yaml`](https://github.com/canvalidk/VD-docs/blob/adfe14bbaafb29856f0a30da088495b7c9d483d2/catalog.yaml): confirms source locations and identifies the un-suffixed Force-Sum record below as the successor to its `_d1` version.
- [`Newton-analysis/_dscn_entry_structure/force_sum_member_value/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md`](https://github.com/canvalidk/VD-docs/blob/adfe14bbaafb29856f0a30da088495b7c9d483d2/Newton-analysis/_dscn_entry_structure/force_sum_member_value/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md): the existing placement argument, inverse member-value determination, magnetic-kernel discovery scenario, and distinction between a residual and an independently warranted interaction. Its placement conclusion is the position this proposal seeks to revise.
- [`Newton/Design 3/vd_acting_object_architecture_consolidation.md`](https://github.com/canvalidk/VD-docs/blob/adfe14bbaafb29856f0a30da088495b7c9d483d2/Newton/Design%203/vd_acting_object_architecture_consolidation.md): architectural context for acting-object instances, conditions of action, force rules, and symbolic force attribution. Its historical vocabulary is not a new naming authority for this proposal.

Active local sources, with paths relative to VD-Newton:

- `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`: the existing local naming decision. The managed catalog records that this steering document remains in VD-Newton custody. This proposal explicitly seeks to change its three-word selection while preserving the distinction between interactions and their impressed-force contributions.
- `pass to VD-docs/NML3_INTERMEDIATE_EXPRESSION_TWO_APPROACHES_2026-09-09.md`: the preceding local record of the residual fold and accumulator/remainder equality, including their different implementation statuses. It predates this proposed triplet change and remains awaiting transfer according to its header.

This is a scoped proposal based on those sources and the conversation. It does not claim a completed theory of experimental discovery, a historical account of magnetism, or a proof that the proposed triplet is sufficient. It supplies an argument for the next entry-design attempt.
