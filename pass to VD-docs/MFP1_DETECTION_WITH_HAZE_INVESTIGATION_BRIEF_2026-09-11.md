# MFP1 detection with haze: investigation brief

**Date:** 2026-09-11.  
**Status:** user-requested brief capturing the agreed starting position and aims. Problem definition is in progress; no experimental design, statistical test, or result has been adopted.  
**Audience:** an investigator with comparable VD knowledge who needs to continue this investigation without reopening its settled premises.  
**Submission:** local in VD-Newton's `pass to VD-docs/`, awaiting transfer. Saving here does not submit it to VD-docs.

## 1. Purpose and scope

We want to understand how an investigator could detect the existence of an unidentified force contribution, and what role haze plays in the experimental and statistical reasoning. The present scope is **MFP1 detection**. Identifying the source and recovering its force law are later achievements.

The user distinguished two kinds of **Mysterious Force Problem (MFP)**:

| Kind | What is mysterious | Illustrative case supplied by the user |
|---|---|---|
| **MFP1** | Whether the account has omitted a contribution belonging to an already recognized kind of force or acting-object. The particular source or instance may still be unidentified. | Forgetting friction for a cart rolling down a hill; potentially the Neptune case. |
| **MFP2** | Whether an accounted or unaccounted effect involves an acting-object of a kind that is altogether unrecognized. | Magnetism when its nature was unrecognized. |

These examples indicate the conceptual distinction; they are not historical findings or selected experimental designs. MFP2 is outside the present investigation.

The investigator must not be given the omission as an established fact merely because the problem is called MFP1. We are asking what evidence could establish it. A simulation may eventually contain a known omitted contribution for validation, but that knowledge would belong to the experiment's designer, not automatically to the simulated investigator.

## 2. Starting commitment: we believe in haze

The user's governing instruction is:

> We are doing this investigation, 'believing in haze'.

There is already a story of haze. We take it as our starting premise: **haze is a function that takes a tolerance value $\epsilon$ and returns a zero vector with uncertainty based on $\epsilon$.** Schematically:

$$
Z_\epsilon=\operatorname{haze}(\epsilon)
=\text{a zero vector carrying uncertainty based on }\epsilon.
$$

This is a statement of the intended object, not a completed mathematical type. The nature of $\epsilon$, the form of the uncertainty, and their precise relationship remain open. The phrase **zero vector with uncertainty** must be preserved. Do not silently replace it with a zero-expectation random force, a Gaussian process, an exact deterministic zero, or a numerical threshold. Any such formalization would be a further proposal to examine explicitly.

The investigation concerns **what happens when haze is assumed**. It does not begin by requiring haze to earn admission. We may temporarily put it aside to understand what work it performs, while retaining the premise of the investigation.

Taking haze as a premise does not predetermine that it will perform every protective role suspected below. Those are questions about its consequences and mathematical realization.

## 3. The force-account context

Keep the net-force relation:

$$
\mathbf F_{\mathrm{net}}=m\mathbf a.
$$

The working haze expression is:

$$
\mathbf F_{\mathrm{net}}
=Z_\epsilon+\mathbf C
=Z_\epsilon+\mathbf F_{\mathrm{gravity}}+\mathbf C_{\mathrm{remaining}}.
$$

The user's latest name is **contributions**, replacing the earlier *Remainder* terminology. A contribution is described as **“a non-random identifiable superposition of impressed forces.”** It may be one identified impressed force or an identified aggregate. Exposing gravity removes it from the remaining contributions. Successive remaining accounts replace one another; they are not additional independent summands.

The earlier discussion suggested reading “non-random” as an identified composition and specified relation to inputs whose values may carry uncertainty. That interpretation remains a proposal, not a settled statistical restriction.

For this investigation, an **acting-object instance** supplies an identifiable, target-directed impressed force, with relevant participants, conditions of action, and a force relation or constraint. Its identity is not its current vector value. One material object can support several acting-object instances, and an interaction can be identified before its force value or general law has been determined. The older architecture provides background; its historical entry assignments are not imposed here.

For a partially specified account, a useful starting quantity is:

$$
\mathbf U
=\mathbf F_{\mathrm{net}}-\mathbf C_{\mathrm{accounted}}.
$$

This subtraction names what remains unexplained by the explicit account. It does not determine whether that quantity is adequately represented by haze or whether a further contribution exists that must become explicit. In an experiment, neither net force nor the accounted contribution is automatically known exactly; establishing their observation and uncertainty models is part of the work ahead. This expression is not yet a statistical test.

All compared quantities must refer to a consistent target, time or interval, frame, and physical context. The notation above is explanatory, not a ratified entry signature or change to the existing Force-Sum triplet.

## 4. The three roles we want to investigate

### A. Protection from an endless explicit force account

The user's phrase is **“protecting us from infinite force contributions.”** Investigate whether haze can justify ending with a finite explicit account while controlling what remains unresolved.

Distinguish a finite sufficient account from the assertion that only finitely many physical interactions exist. The relevant issue includes the combined effect of unresolved contributions, not just whether each proposed contribution is individually small. The earlier haze work proposed finite sufficiency at an admitted tolerance; it did not establish a finiteness theorem.

### B. Protection from “detecting” negligible contributions

We want to understand the relationship between these two possible claims:

1. There is evidence of a **nonzero omitted contribution**.
2. There is evidence of an unresolved contribution **beyond what the account may legitimately leave unexplained**.

**Do not choose one as the definition of detection in advance.** Whether they differ, how they differ, and what negligibility means in that difference are research aims.

We also want to understand what would have to be done experimentally to **reduce the difference**, where possible. No experimental design has yet been selected. Repetition, improved measurement, controlled changes of conditions, and observation over different intervals are possible questions to consider, not adopted solutions or assumptions that the difference must disappear.

As proposals develop, distinguish improving what is known about an unchanged situation from changing the physical situation, the observable, or the requested accuracy. This distinction helps specify what a claimed reduction of the difference actually achieves; it does not settle which route we should take.

### C. A natural role in the detection process

The user's expectation is that, as we work through detection, we will encounter a need or use for an object that looks **“eerily like the haze concept we were describing.”**

Investigate where that role occurs: in the experimental description, the permitted unresolved contribution, the statistical hypothesis, a relevance criterion, a stopping condition, or some combination. These are candidate locations to examine, not a chosen architecture.

This aim is consistent with believing in haze. We are exploring how an already assumed concept operates and becomes explicit in the reasoning, including what becomes difficult when it is temporarily set aside.

## 5. Detection, attribution, and the earlier haze insight

The central question inherited from the earlier discussion is:

> When is it that the remaining information can't be explained by the haze?

Keep the evidential steps visible. A discrepancy with an account, evidence for an omitted force contribution, and identification of a particular acting-object are different conclusions. The present investigation must determine what licenses the detection step without silently performing the later identification step.

The immediate scope does not require discovering a new force kind, finding a source, or reconstructing a force law. It does require understanding how uncertainty in the listed forces, motion measurements, and other inputs affects an alleged detection. When additional assumptions isolate omission as the explanation, state them.

Several earlier VD findings constrain this work:

- Accurate uncertainty calculations for the included contributions do not by themselves establish the sufficiency of the account's omissions.
- Numerical agreement does not establish a complete interaction account: omitted contributions can cancel.
- Subtraction alone does not warrant an acting-object or distinguish one omitted contribution from an aggregate.
- Haze must have commitments against which evidence can be assessed. Allowing an arbitrary repair for every discrepancy would erase the distinction we are trying to investigate.
- The tolerance expresses a requirement; evidence must establish the uncertainty or other characterization used with it. Neither supplies the other automatically.

These preserve the existing haze story. They do not select the statistical model. In particular, do not assume independent repetitions, uncertainty that shrinks under averaging, a particular distribution, a confidence level, or a force norm threshold merely from the word haze.

The earlier **Major Logical Failure** warning also applies: the prediction actually stated is the claim to assess. Revising its tolerance, uncertainty, or force account produces a revised claim; it must not silently turn a failed original prediction into a successful one.

## 6. What remains open before experiments and tests

Continue defining the problem incrementally. The following questions organize the unfinished work; they are not demands that every choice be fixed before any useful reasoning can begin.

| Open question | What needs to become explicit |
|---|---|
| What information does the investigator have? | The explicit force account, measured quantities, known parameters, and independently supported assumptions. |
| What is observed? | Motion, acceleration, a force readout, a stopping position, or another observable, with the relevant interval and uncertainty. |
| What is $\epsilon$? | Its nature, units or structure, what requirement it expresses, and how it relates to the question asked. |
| How does haze carry uncertainty? | Its mathematical representation, dependencies, and behavior across time, repeated trials, and changes of experimental conditions. |
| What is being detected? | The relationship between nonzero omission and inadequacy at the permitted unresolved level, retaining both as subjects of investigation. |
| What can an experiment change? | What measurements, controls, interventions, or repetitions would distinguish the claims or reduce their difference. |
| What licenses a conclusion? | The hypotheses, evidence rule, and possible outcomes, including a situation in which the available evidence does not decide. |
| What licenses stopping? | How haze could support a finite sufficient account, and what observations would require reopening it. |

A bounded continuation could first describe one candidate situation in words and list the investigator's information, then work out alternative detection claims before choosing a test. A cart with potentially omitted friction is available as an example; it has not been selected. Any proposed first design should make its assumptions visible and remain open to revision as the problem definition develops.

## 7. What a successful investigation should deliver

The eventual outcome should explain, through a specified experimental design and explicit statistical reasoning:

1. What evidence supports each meaning of detection, and what additional assumptions turn a discrepancy into evidence of an omitted contribution.
2. How negligibility enters, whether the two detection claims differ, and what experimental changes can or cannot reduce that difference under the chosen model.
3. Where haze enters the process, what work it performs, and which properties of haze that work requires.
4. Whether and under what conditions haze supports a finite explicit force account.
5. Which conclusions follow from the starting haze premise and which depend on additional mathematical or experimental choices.

This brief supplies the agreed starting position. No research result, experimental protocol, statistical test, simulation, or completed haze definition is claimed. Continuing the work should begin with the unresolved problem definition, rather than treating the illustrative equations as a finished detection method.

## 8. Sources, precedence, and custody

**Primary authority for this investigation:** the user-led September 11 conversation that defined MFP1/MFP2, narrowed the scope to detection, identified the three suspected roles, kept the difference between the two detection claims open, and established “believing in haze” as the starting premise. This brief was requested so other investigators with similar VD knowledge can carry the work forward. Those instructions govern this investigation where earlier exploratory wording differs.

**Local active ancestry**, read during the preparation and discussion leading to this brief:

- [Haze and the logic of Newtonian force accounts, September 10](NML3_HAZE_AND_THE_LOGIC_OF_NEWTONIAN_FORCE_ACCOUNTS_2026-09-10.md): the principal conceptual background, including the contributions terminology, uncertainty versus omissions, testability, and the open mathematics of zero.
- [Tolerance, special zero, and net-force uncertainty, September 9](NML3_TOLERANCE_SPECIAL_ZERO_AND_NET_FORCE_UNCERTAINTY_DISCOVERY_2026-09-09.md): the trace origin, independent tolerance input, and candidate finite-sufficiency commitment.
- [Remainder triplet and acting-object discovery proposal, September 9](NML3_REMAINDER_TRIPLET_AND_ACTING_OBJECT_DISCOVERY_PROPOSAL_2026-09-09.md): the path from an unexplained contribution to experimental inquiry; its older terminology is read through the later contributions discussion.
- [Force-Sum naming decision, August 26](../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md): the existing `net-force / impressed-force / interaction-set` naming authority and identity/value distinction. This investigation does not install a replacement entry group.

The September 10 argument asks whether a dedicated haze representation is necessary. **The September 11 instruction fixes a different investigative stance: assume haze and investigate its use and consequences.** The earlier document remains background; its open admission question is not the starting task here.

**Managed context:** `canvalidk/VD-docs@0ad969e068e77175e86f6fe8dd24e6f9f7a965ce`, resolved from `main` during the initial reading and reconfirmed on September 11 when writing this brief. Sources were selected through [catalog.yaml](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/catalog.yaml) and read at that coherent snapshot:

- [Warranted Force Account: Foundational Explication](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md): algebraic decomposition versus physical attribution.
- [NML3 Logical Consequences](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md): identity, cancellation, closure, and residual-test asymmetry.
- [Force-Sum member-value relational necessity](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_entry_structure/force_sum_member_value/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md): distinction between independently warranted membership and inverse determination of a member's force value.
- [Acting-object architecture consolidation](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/Design%203/vd_acting_object_architecture_consolidation.md): background on instances, participants, force rules, and symbolic constraints. Its historical architecture is not newly ratified here.

Coverage is scoped to this conversation, the recent local haze development, and its immediate managed Force-Sum/acting-object ancestry. It is not an exhaustive VD synthesis, an audit of unclassified inbox material, or a review of statistical literature. The September 9–11 haze work remains local and outside the managed catalog at this snapshot.

`outbox/VD-Newton/` was checked at the pinned commit when writing this brief. It contains only the September 8 receipt for the already closed earlier pass; it does not receive this brief or the newer haze drafts. No VD-docs source or existing local document was changed.
