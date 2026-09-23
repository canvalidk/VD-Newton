# Discovery: the human tolerance input, the special zero, and net-force uncertainty

**Date:** 2026-09-09.  
**Kind:** user-requested discovery record.  
**Status:** a conceptual discovery arising from trace development, with a candidate remainder law to develop. The earlier entry/interpreter issue remains unresolved; no uncertainty model, finiteness theorem, or final entry group has been implemented here.  
**Submission:** awaiting transfer to VD-docs; saved in VD-Newton's `pass to VD-docs/`. Saving here does not submit the record.

## 1. The discovery

Following the uncertainties through a force-account trace exposed an input that the uncertainty analysis cannot itself determine: **the accuracy the person asking the question requires**.

The evidence can tell us how well a remainder has been determined. It does not, by itself, tell us how well it needs to be determined before we may stop. That requirement is the tolerance, provisionally written $\varepsilon$. It is supplied by the person or inherited from the task specification.

This led to the user's proposed expression:

```text
F_net = special-zero-vector + Remainders
```

The special zero, provisionally $Z_\varepsilon$, would represent a contribution reported as zero at the chosen resolution while retaining its unresolved force content and uncertainty description. Its presence could make explicit something otherwise hidden when a calculation calls a contribution negligible.

The proposed connection is between a finite force expression, the contribution left implicit, and the human requirement under which the answer is adequate. For a determination that uses this approximation, correctly describing net-force uncertainty may require retaining the meaning of $Z_\varepsilon$ instead of simplifying it away as ordinary zero.

The [companion algorithm record](NML3_REMAINDER_INTERMEDIATE_EXPRESSION_ALGORITHM_2026-09-09.md) states what has and has not been demonstrated computationally.

## 2. How the trace led to the idea

### From arbitrary decomposition to a particular remainder

The earlier NML3 puzzle was that a net-force vector permits indefinitely many algebraic decompositions. For any vector $G$,

$$
F_{\mathrm{net}}=G+(F_{\mathrm{net}}-G).
$$

The equality does not identify an interaction. The existing Force-Sum discussion therefore sought the meaning that distinguishes an impressed force from a freely chosen summand.

The user redirected the investigation toward black-box use: first describe what to do when a determination is available, allowing the manner of determination to remain inside its box. In English, accounting for one acting interaction removes its impressed-force expression from the previous remainder:

$$
R_{\mathrm{before}}
=
F_{\mathrm{impressed}}(\text{interaction})
+
R_{\mathrm{after}}.
$$

The proposed staged trace then became:

```text
R-before(i)
→ {impressed-force of IS(i+1)} + {new remainder}
→ {impressed-force of spring} + {new remainder}
```

Here `IS(i+1)` denotes the next interaction in a traversal, with target and context fixed. Identifying that interaction and expanding its force expression are separate demands.

This gives the remainder meaning through its continuation. It refers to what remains in a particular force account and is committed to exposing particular interaction contributions. Its vector value alone does not identify it. Two remainders may have the same value while having different remaining interactions.

### From the remainder to the apparent zeros at the end

The user then asked what happens after the interaction traversal is emptied out. Could expansion keep leaving remainders that display as:

```text
+ 0 + 0 + 0 + ...
```

Perhaps stopping could be established as a theorem about the output instead of being hidden in an unexplained decision to stop. Following the uncertainties of these apparent zeros exposed a further question: what did each zero actually establish?

An exact empty sum has value zero. A measured or inferred contribution reported as zero can still have uncertainty. Repeatedly writing zero does not generate repeated independent measurements. Also, $R=0+R$ is true for any $R$, so that recurrence alone cannot prove its continuing remainder vanishes. The right to stop needs a determination about the remainder.

That determination could state exact completion, or it could provide a bound adequate for the question. The possibility of the latter exposed the tolerance.

## 3. The human input that uncertainty does not supply

The user's correction was crucial:

> No amount of knowledge of the uncertainties of the "remainders" will tell you your tolerance bound.

The discussion also corrected “if you are very careful” to **“if you are not very careful”**: insufficiently careful analysis can conceal the separate requirement by making “good enough” look as though it emerged from the uncertainty calculation.

Two determinations are involved:

| Item | What it contributes |
|---|---|
| Evidence and uncertainty analysis | What can be established about the unresolved contribution |
| Required tolerance | How much unresolved effect is acceptable for this question |

Two people can have the same evidence about the same physical situation and legitimately require different accuracies. One may have enough to answer; the other may need further determination.

The proposed VD process therefore has an additional explicit input:

```text
physical situation and evidence
+ question being asked
+ required accuracy

→ answer with its uncertainty and a justification for stopping
```

The tolerance can remain a black-box input. A second black box supplies a bound or statistical characterization of the remainder. The theory can state what follows when that characterization satisfies the requirement.

The insight concerns the explicit role of a human requirement in VD question answering. It is not a claim that tolerance is unfamiliar in engineering or physics. Expressions such as “negligible,” “approximately,” and “sufficiently accurate” already rely on such requirements. The proposed structure makes that role available to the trace.

## 4. A possible meaning for the special zero

The working English description is:

> A contribution represented as zero at the chosen resolution, while retaining what is known about its possible unresolved value.

One possible formal reading is:

$$
F_{\mathrm{net}}=Z_\varepsilon+R_0(\varepsilon).
$$

In this reading, $Z_\varepsilon$ accounts for the combined contribution left implicit under the chosen resolution. $R_0(\varepsilon)$ is the part selected for explicit unfolding. The distinction is an accounting choice under a supplied rule; it does not change the underlying net force.

Repeated expansion of the explicit part could give:

$$
R_0(\varepsilon)
\longrightarrow F_1+R_1(\varepsilon)
\longrightarrow F_1+F_2+R_2(\varepsilon)
\longrightarrow\cdots.
$$

If this selected account has a finite traversal, its final remainder is an exact empty-list result. The resulting force relation is then:

$$
F_{\mathrm{net}}
=
Z_\varepsilon+\sum_{j=1}^{N(\varepsilon)}F_j.
$$

This is a candidate interpretation of the user's plural “Remainders,” not a settled syntax. Successive traversal remainders are replaced as they unfold; they are not all added as independent force contributions. The aggregate unresolved contribution is represented once.

The symbol $Z_\varepsilon$ in the relation names unresolved force content whose *reported* contribution is zero. It does not assert that this content is the exact vector $\mathbf 0$. Nor does reporting zero establish that its statistical mean is zero. Its eventual type may need to include a force estimate, a bound or distribution, and its dependencies on the other quantities.

The displayed zero therefore need not exhaust the item's meaning. This continues the earlier discovery that an item's vector value does not exhaust its meaning in the trace.

## 5. The candidate law: finite expansion at a declared resolution

The user proposed that the expression ultimately conveys that contributions above a threshold form a finite list. A fuller candidate statement is:

> For a fixed target and context, each admitted positive tolerance permits a finite explicit force account, with the combined unresolved contribution represented by a special zero carrying its bound or uncertainty.

This would make finite sufficiency at the requested resolution a theoretical commitment. It has not been proved here, and it does not follow from arbitrary vector decomposition.

The aggregate condition matters. Many individually small contributions can add to a large one, so a rule that simply excludes each term below $\varepsilon$ does not by itself bound the total omitted force. The proposed law needs both a finite explicit account and control of what that account leaves implicit.

The candidate also separates two achievements: exhausting the selected traversal and meeting the accuracy requirement for the full force determination. An empty selected list can coexist with unresolved force content represented by $Z_\varepsilon$.

The precise domain of tolerances, norm or output quantity being controlled, selection rule, and conditions guaranteeing finite sufficiency remain open. “Remainder law” is a working description, not a ratified law name or entry assignment.

## 6. Why this could matter for net-force uncertainty

Let the true retained contribution be

$$
A_\varepsilon=\sum_{j=1}^{N(\varepsilon)}F_j,
$$

and let $\widehat A_\varepsilon$ be the calculated estimate. Under the proposed accounting relation,

$$
F_{\mathrm{net}}-\widehat A_\varepsilon
=
(A_\varepsilon-\widehat A_\varepsilon)+Z_\varepsilon.
$$

The total error contains both the retained calculation's error and the unresolved contribution. Reporting the retained estimate with only its own uncertainty could omit the second part.

For a concrete bound interpretation, suppose the supplied determinations establish

$$
\|A_\varepsilon-\widehat A_\varepsilon\|\leq b_\varepsilon,
\qquad
\|Z_\varepsilon\|\leq\varepsilon.
$$

Then the triangle inequality gives

$$
\|F_{\mathrm{net}}-\widehat A_\varepsilon\|
\leq b_\varepsilon+\varepsilon.
$$

Here $b_\varepsilon$ and $\varepsilon$ are bounds, not standard deviations. A probabilistic version requires a specified probability model or coverage statement. Choosing a tolerance does not by itself establish that the omitted contribution obeys it.

For a joint uncertainty model with finite covariances, addition instead gives

$$
\Sigma_{\mathrm{net}}
=
\Sigma_{A_\varepsilon}
+\Sigma_{Z_\varepsilon}
+\operatorname{Cov}(A_\varepsilon,Z_\varepsilon)
+\operatorname{Cov}(Z_\varepsilon,A_\varepsilon).
$$

Thus a statistical uncertainty cannot generally be calculated by attaching independent error bars to each displayed term. Correlations matter. The standard metrology treatment also explicitly allows a correction with estimated value zero and nonzero uncertainty, and requires dependence to be retained when combining uncertain quantities. [GUM §§5.1.5 and 5.2](https://www.iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/05_e.html).

This is consistent with the earlier VD mass-estimator reuse work: preserving the relationships among uncertain quantities can preserve a sharply determined result that would be distorted by treating those quantities independently.

### The scope of the claim about tolerance

The proposed need for $\varepsilon$ concerns a finite answer obtained by omitting or absorbing contributions under a resolution rule. The required resolution cannot be inferred from the uncertainty data alone. Once supplied, it helps specify the approximation whose uncertainty is being reported.

The tolerance is not sufficient to calculate that uncertainty. The bound or statistical description of $Z_\varepsilon$, the retained uncertainties, and their dependence are also needed. In particular, a bound does not select a uniform, Gaussian, or any other probability distribution.

If the same complete joint information is merely reorganized between $A_\varepsilon$ and $Z_\varepsilon$, the uncertainty of their sum must remain unchanged. More expansion cannot manufacture uncertainty. A changed approximation or additional evidence can change the reported uncertainty; a relabeling alone cannot.

The proposal also does not show that each zero is inherently a fresh random event. The unresolved contribution could reflect measurement uncertainty, unresolved physical contributions, a stochastic model, or a combination. The relevant black box would have to specify which description is being supplied.

## 7. Why disagreement with observation becomes inspectable

The user connected the discovery to an intuitive analysis of a Newtonian prediction that disagrees with observation. The proposed trace retains places to investigate each possibility:

| Possible source of disagreement | Relevant trace content |
|---|---|
| The mathematics was performed incorrectly | Expansions, substitutions, and calculations |
| An interaction was identified or represented incorrectly | The determination supplying the interaction and force call |
| An interaction's uncertainty was assessed or propagated incorrectly | Its uncertainty description and dependencies |
| Contributions treated as negligible were not negligible enough | The unresolved aggregate, its bound, and the tolerance used to stop |

The accuracy of observations and the physical context also remain inputs to examine. A persistent disagreement after these checks can bear on the physical assumptions or law; the trace does not guarantee that Newtonian mechanics agrees with reality.

The conceptual achievement is that the route to the answer also provides the structure for investigating its failure. This is the user's proposed VD gain: meanings, computation, uncertainty, and the stopping requirement become parts of the same inspectable account. Automatic uncertainty tracking and fault diagnosis have not yet been implemented.

## 8. What is established, and what remains to develop

The discussion has identified a coherent candidate structure:

- remainder expansion links a force quantity to a continuing interaction account;
- an uncertainty characterization and a required tolerance are distinct inputs;
- the special zero could retain an unresolved contribution that ordinary presentation hides;
- a finite answer could carry both its force expression and the account of why its unresolved part is acceptable.

The immediate computational gap remains the staged transition

```text
impressed-force of IS(i+1)
    → impressed-force of spring.
```

The successful probe supplied the interaction argument in advance. It did not resolve a nested selection demand inside a pending force call, implement the complete new algorithm, or handle $Z_\varepsilon$.

Further work must specify the special zero's type, the meaning and ownership of the tolerance, the aggregate remainder determination, and how uncertainty and dependence survive expansion and simplification. Finite sufficiency at every admitted tolerance remains a proposed requirement with conditions to establish. Final law wording, triplet placement, and entry numbers remain open.

These open points do not erase how the idea was reached. The discovery is the connection exposed by the trace investigation; completing its mathematical and computational realization is subsequent work.

## 9. Sources, provenance, and relationship to earlier material

The primary source is the user-led discussion in the VD-Newton task **Review NML3 trace progress**, 2026-09-09, task identifier `01a085b5-69da-7072-8a33-854ce9565cff`. It developed the black-box instruction, staged remainder expansion, apparent terminal zeros, the independent human tolerance, the uncertainty/failure analysis, and the proposed special zero. The equations defining one possible $Z_\varepsilon$ representation and the bound/covariance consequences above are formal elaborations of that discussion, not completed or ratified entries.

Managed sources were selected through [catalog.yaml](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/catalog.yaml) and read coherently at **`canvalidk/VD-docs@0ad969e068e77175e86f6fe8dd24e6f9f7a965ce`**, reconfirmed as `main` for this record:

- [Warranted Force Account: Foundational Explication](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md), especially the arbitrary-decomposition puzzle and the substantive meaning of a force account.
- [NML3 Logical Consequences](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md), especially cancellation, the asymmetry of residual tests, and the conditional finiteness consequence.
- [Mass-estimator uncertainty and reuse walkthrough](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_uncertainty_and_reuse_walkthrough_2026-09-07.md), §§4–6, for preserving dependence when uncertain quantities are reused.
- [Randomness and the Declarative Boundary](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/randomness_declarative_boundary.md), for recording how a random value enters and retaining that binding rather than resampling through expansion.

Local active sources are the companion algorithm record, the [earlier remainder-triplet proposal](NML3_REMAINDER_TRIPLET_AND_ACTING_OBJECT_DISCOVERY_PROPOSAL_2026-09-09.md), and the [two-approach record](NML3_INTERMEDIATE_EXPRESSION_TWO_APPROACHES_2026-09-09.md). Their newer proposals remain outside the managed catalog at this snapshot. The local NML3 steering has later terminology and identity clarifications than the early managed explication; the decomposition argument is carried forward in the current interaction/impressed-force vocabulary.

The earlier records remain unchanged. This record develops a new possible role for tolerance and the remainder; it does not retrospectively claim their proposed entry structures were completed. The current `outbox/VD-Newton/` receipt was checked and concerns the already closed mass-estimator pass, not this pair.

This is a scoped discovery record based on the conversation, named project sources, and the cited metrology passage. It is not an exhaustive literature review or a claim of historical priority.
