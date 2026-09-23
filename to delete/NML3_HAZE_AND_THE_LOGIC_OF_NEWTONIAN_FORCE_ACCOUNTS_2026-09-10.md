# Haze and the logic of Newtonian force accounts

## Why it may be needed, and in what sense it was already there

**Date:** 2026-09-10.  
**Status:** user-requested argument draft, developed from the September 9–10 NML3 discussion. The argument identifies a proposed logical role for haze; its mathematical definition and entry placement remain open.  
**Submission:** local draft in VD-Newton's `pass to VD-docs/`, awaiting transfer. Saving here does not submit it to VD-docs.  
**Terminology:** *haze* is the user's provisional name for $Z_\epsilon$.

The case for haze begins with a gap between two achievements. We can calculate the uncertainties of every force contribution in our account. We have not thereby established that the account includes everything needed to predict the object's motion to the required accuracy.

There remains a question about what the account leaves unresolved: could there be additional interactions, how much could their combined contribution matter, and what would show that the remainder requires further explanation? Haze is proposed as an explicit place for this remaining freedom, together with constraints on what it may explain.

The claim that haze “has always been in” Newtonian mechanics is strongest as a reconstruction of the logic of applying the theory. A justified finite prediction already needs some commitment about omitted effects. That commitment can be hidden in “only gravity acts,” “neglect air resistance,” or “the other effects are negligible.” Haze would bring it into the force expression and the reasoning that accompanies the prediction.

The functional claim concerns the need to account for omissions. Whether a separate term with the name *haze* is the best or necessary formal realization remains to be established.

## 1. Keep net force where it is

The user's starting instruction is to retain

$$
\mathbf F_{\mathrm{net}}=m\mathbf a.
$$

Haze does not replace this relation or redefine net force as merely the sum of the forces we currently know. The additional proposal concerns how net force is accounted for:

$$
\mathbf F_{\mathrm{net}}
=Z_\epsilon+\mathbf R_\epsilon,
\qquad
\mathbf R_\epsilon
=\sum_{i\in S_\epsilon}\mathbf F_{\mathrm{impressed},i}.
$$

Here $S_\epsilon$ denotes the interactions selected for explicit accounting at the requested resolution. This notation is an explanatory elaboration, not an adopted entry signature. Target, time, frame, and other physical conditions must remain fixed when quantities are compared.

The capitalized *Remainder* in the user's proposal is the part to be unfolded into an explicit sum of impressed forces after haze has been separated. During an unfinished traversal, each successive remainder contains what is still to be unfolded. Successive remainders replace one another; adding all of them would count contributions repeatedly.

**Terminology follow-up, 2026-09-10:** the user now proposes **contributions** in place of *Remainder*, giving an intermediate expression such as $\mathbf F_{\mathrm{net}}=Z_\epsilon+\mathbf F_{\mathrm{gravity}}+\mathbf C_{\mathrm{remaining}}$. The intended contribution is “a non-random identifiable superposition of impressed forces”: one identified impressed force or an identified aggregate, with gravity removed from the remaining account once exposed. The identity and composition of the contribution survive independently of its current vector value. A possible reading of “non-random” is that the composition and rule relating it to its inputs are specified, while those inputs and the resulting value may remain uncertain; the exact statistical restriction is still to be developed. This paragraph preserves the naming development without changing the earlier derivation or ratifying an entry structure.

In these candidate equalities, $Z_\epsilon$ names the unresolved force contribution, with its eventual uncertainty or other qualifying information. The user's description of it as a “zero vector” is important but not yet a settled mathematical type. The distinction between an exact zero and a contribution represented as zero is addressed in section 10.

Changing $\epsilon$ can change the division between explicit contributions and haze. It does not, by that accounting choice alone, change the underlying net force or the physical situation.

## 2. Why this arose while encoding NML3

The earlier NML3 puzzle was that vector decomposition is arbitrary while physical interaction attribution is not. For any vector $\mathbf G$,

$$
\mathbf F_{\mathrm{net}}
=\mathbf G+(\mathbf F_{\mathrm{net}}-\mathbf G).
$$

This identity does not establish an interaction that supplies $\mathbf G$. A physically meaningful force account needs identities and grounds for attribution beyond successful addition. That distinction is developed in the managed [Warranted Force Account explication](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md).

The trace work gave a remainder meaning through its continuation:

$$
\text{previous remainder}
=\text{impressed force of an identified interaction}
+\text{next remainder}.
$$

The determination of the interaction could remain inside a black box while the dictionary stated what follows once that determination is available. A simple version of this expansion ran successfully. Developing it exposed the question of termination: what licenses us to stop demanding more of the remainder?

An exact empty sum is zero. But an unfinished physical account is not made complete by repeatedly appending zeros. The equation $R=0+R$ holds for any $R$. Something must establish that the continuing remainder has no effect, or that its possible effect is sufficiently controlled for the question.

The tolerance appeared at that boundary. Evidence about the remainder cannot itself choose how much accuracy the question requires. The September 10 discussion then extended the idea from a stopping mechanism to the logic of finite Newtonian predictions generally.

## 3. The Major Logical Failure: changing the prediction through interpretation

Consider the user's cart example. Gravity, contact, and friction have been included in a calculation. The prediction is stated as a stopping value of $5\,\mathrm m$. The experiment returns $4.95\,\mathrm m$. Were we correct?

Under the exact comparison posed in the thought experiment, the answer is no:

$$
5\ne4.95.
$$

The assistant initially answered that the judgment depended on tolerance and uncertainty. The user's correction was that no approximate prediction had been stated. The assistant had introduced an interpretation and used it to avoid acknowledging the failure of the exact claim.

The user's name for this move was the **Major Logical Failure**, or **MLF**. Its essential feature is the substitution of a different proposition for the one tested. “Exactly $5$,” “within a declared interval around $5$,” and “distributed according to a specified model centred at $5$” have different contents. A discrepancy with the first cannot be answered by silently adopting the second or third.

The cart was subsequently revealed to be miniature, only $3\,\mathrm{mm}$ wide. The $50\,\mathrm{mm}$ discrepancy was approximately seventeen cart widths. The user also introduced a starting coordinate of $4.8\,\mathrm m$. If $5$ and $4.95$ are stopping coordinates, the corresponding travel distances are $0.20\,\mathrm m$ and $0.15\,\mathrm m$: a discrepancy of $25\%$ of the predicted travel.

There is a wording distinction to preserve. The initial scenario said “away from the starting position”; the later coordinate reading is a clarification or variant, not an inference licensed by that phrase alone. Under either reading, the exact numerical claim fails. The miniature scale exposes how unwarranted a casual “close enough” interpretation can be; it is not needed to establish the inequality.

In an actual experiment, the relation between a recorded measurement and the physical stopping position also requires an uncertainty account. That is part of specifying the empirical test. It does not authorize rewriting an exact numerical prediction after seeing the result. Nor does failure of the complete prediction identify which physical law, input, approximation, or calculation failed.

## 4. Repairing that failure does not yet establish the need for haze

The user explicitly recognized a first repair: state the uncertainties properly. A separate haze term has not yet been shown necessary merely because one stopping value differs from a nominal prediction.

Suppose the prediction is now expressly a distribution of stopping positions centred at $5\,\mathrm m$. Repeated experiments can be compared with that prediction. The centre, spread, shape, and relevant dependence between observations are part of its content. A single result of $4.95\,\mathrm m$ can be consistent with the statistical claim even though it differs from the centre. Statistical agreement is assessed through an evidential rule; finite agreement does not certify the model as exactly true.

Uncertainty in net force can also produce growing uncertainty in motion over time. Growing deviation from a mean trajectory therefore does not by itself require an additional physical source named haze.

The scope of uncertainty matters here. A fixed but unknown friction coefficient could shift all runs similarly. It does not become a freshly sampled coefficient merely because its value is uncertain. Trial variation and uncertainty about quantities shared across trials must be represented appropriately. Standard metrology distinguishes these contributions to an uncertainty account. [GUM §§3.1–3.3](https://www.iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/03_e.html).

This stage of the argument should not be skipped. Haze needs a role beyond repairing the omission of an ordinary uncertainty statement.

## 5. A successful distribution still leaves the interaction account open

Continue to suppose that repeated stopping positions are centred at $5\,\mathrm m$. The user identified three possibilities behind the spread:

1. There is variation in the included forces or initial conditions, together with measurement uncertainty.
2. Different trials contain different interactions missing from the explicit account.
3. One missing interaction remains present, but its varying state or stochastic action changes the appropriate centre for individual trials.

Calling the observed spread “uncertainty” does not choose among these physical explanations. Uncertainty describes what is determined or predicted; it is not, by itself, the physical mechanism that produces the variation. The possibilities can coexist.

The third possibility can be illustrated at the level of stopping positions by

$$
X_k=5+B_k+\eta_k,
$$

where $B_k$ is a trial-specific shift associated with a proposed missing influence and $\eta_k$ is the remaining variation. If

$$
\mathbb E[B_k]=0,
\qquad
\mathbb E[\eta_k\mid B_k]=0,
$$

then

$$
\mathbb E[X_k]=5,
\qquad
\mathbb E[X_k\mid B_k]=5+B_k.
$$

The overall centre can remain $5$ while the centre conditional on further information differs between runs. This is an illustration of the distinction, not a derivation of a new force law or evidence that such an interaction exists. If $B_k$ cannot be determined before the result, identifying its statistical role does not give us advance knowledge of its particular value.

Thus an account can reproduce the observed distribution while leaving its interaction attribution incomplete. This extends the earlier NML3 result that a matching resultant does not establish a complete interaction-set. The managed [Logical Consequences, especially consequences 14–15](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md), preserves the analogous point about hidden cancelling contributions.

## 6. The deeper danger in a missing force with a freely changing mean

The user's concern about the third possibility was stronger than a difficulty distinguishing models. If a missing force can have whatever unobserved mean each trial requires, how can we establish that it is absent? How can the account fail?

At the force level, imagine that motion has been observed and define

$$
\mathbf H(t)
=m\mathbf a_{\mathrm{observed}}(t)
-\mathbf F_{\mathrm{accounted}}(t).
$$

It follows automatically that

$$
m\mathbf a_{\mathrm{observed}}(t)
=\mathbf F_{\mathrm{accounted}}(t)+\mathbf H(t).
$$

If any history of $\mathbf H$ is admissible, every observed history can be accommodated. A trial-specific random mean provides no restriction when its distribution and relation to the experiment are themselves unconstrained. The account has used the discrepancy to define the quantity that makes it balance.

The freedom is the problem. A specified stochastic law can constrain observations even when it does not predict each realized value. Conversely, an arbitrary deterministic residual can provide the same escape as an arbitrary random one.

This establishes a conditional failure of testability: **an account protected by unrestricted residual repair has no empirical exclusions at that level**. It does not establish that every formulation of Newtonian mechanics is unfalsifiable, or that a failed prediction uniquely refutes Newton's second law. The complete prediction includes force laws, inputs, context, and other assumptions. The user’s broader concern is that leaving the admissible repairs implicit makes it too easy to protect the account without acknowledging that its commitments have changed.

The suggestion that there are no physical forces with a “random mean” remains unestablished here. The logical argument does not require that empirical claim. What it requires is a restriction on how an additional interaction may be proposed and used to explain a discrepancy.

## 7. The central turn: what remaining information cannot haze explain?

The user first proposed looking at the subtraction

$$
\mathbf F_{\mathrm{net}}-Z_\epsilon
=\mathbf R_\epsilon.
$$

The intended constraint was that impressed-force contributions account for “mean-like” effects in the net force. Haze would give the unresolved part a different, constrained role. “Mean-like” remains a developing phrase: its conditioning, temporal scope, and relationship to the identity of an interaction have not been defined.

The reverse subtraction then exposed the important question. Let $\mathbf K$ be the combined contribution already accounted for, and write

$$
\mathbf U=\mathbf F_{\mathrm{net}}-\mathbf K.
$$

The residual is not automatically haze merely because it is left over. The user redirected the reasoning:

> Ask yourself, when is it that the remaining information can't be explained by the haze.

This is the decisive proposed role. Haze has an admissible behaviour, relative to the question and tolerance. The unresolved information must be assessed against that behaviour. Evidence incompatible with it creates a demand for further explanation.

For example, a specified zero-mean model can be challenged by appropriate evidence of a residual mean. A model with a stated spread or dependence structure can be challenged on those features. Which findings matter depends on what the haze model actually commits to. A finite sample mean differing from zero does not automatically refute a zero-mean distribution, and a low-probability observation is not a logical impossibility. Statistical versions need a stated evidential procedure.

The resulting failure belongs first to the account that produced the prediction. It can prompt inspection of an existing force determination, a measurement, the physical context, or the haze assumption, as well as investigation of another interaction. It does not identify a new interaction by algebra alone.

Haze is therefore intended to limit the freedom of the unfinished account. Calling an unrestricted residual “haze” would accomplish nothing. Its physical and evidential meaning must supply restrictions beyond the subtraction identity.

## 8. Why “only gravity acts” is the revealing example

The user applied this reasoning to the familiar statement that a falling object acts under gravity. Someone asks about air resistance, the Earth's magnetic field, or the influence of other planets. The proposed answer is:

> They are not interacting at this tolerance.

The qualifier is essential. It proposes that participation in the explicit force account is a relation stated at a resolution. For a suitable object, situation, observable, and interval, the account can be sufficient without separately resolving every influence. Whether any of the named effects qualifies for omission is a determination to make in that situation, not a general assertion that those effects are always negligible.

Under this usage, the statement “only gravity acts” carries a further commitment: what has been left implicit does not require explanation beyond the permitted haze. If the question demands greater accuracy, or the prediction extends over a longer interval, another contribution may need to become explicit.

This is a proposed refinement of force-account language. It does not show that changing a human tolerance changes which physical relations exist. The older, tolerance-independent interaction-set and the proposed set of interactions resolved at $\epsilon$ must be distinguished until their relationship is defined.

The combined omitted effect matters. Excluding each contribution individually because it is below a threshold does not control their sum. Nor does a small resultant establish that its underlying contributions are individually small: large contributions may cancel. The criterion must concern the quantity relevant to the question and retain whatever information is needed for that purpose.

## 9. Why the uncertainties of the included parts do not finish the job

This is the user's culminating distinction. Even after calculating all the uncertainties associated with the contributing parts, the experimental description can leave open whether additional interactions are present below the tolerance.

Let $\mathbf K$ denote the force contribution of the included interactions and $\widehat{\mathbf K}$ its estimate. Then

$$
\mathbf F_{\mathrm{net}}-\widehat{\mathbf K}
=(\mathbf K-\widehat{\mathbf K})+\mathbf Z_\epsilon.
$$

The first term concerns the determination of the included contribution. The second concerns what the explicit account leaves out. Precision in the first does not establish that the second vanishes or is adequately controlled.

The same nominal experimental setup may admit several unresolved physical situations: an additional interaction may be absent, present with a sufficiently small effect, or variable across trials. That is additional freedom in what the specified setup leaves undetermined. It is not automatically a new fundamental degree of freedom, an independent random variable, or fresh randomness on every repetition.

There are two distinct judgements:

| Judgement | What must be established |
|---|---|
| Accuracy of the included contribution | How well the retained forces and inputs have been determined and combined |
| Sufficiency of the account | Whether the contribution left unresolved is adequately controlled for the question |

For an illustrative bound calculation, suppose evidence establishes

$$
\|\mathbf K-\widehat{\mathbf K}\|\leq b,
\qquad
\|\mathbf Z_\epsilon\|\leq\epsilon.
$$

Then

$$
\|\mathbf F_{\mathrm{net}}-\widehat{\mathbf K}\|
\leq b+\epsilon.
$$

Here $\epsilon$ has force units and bounds the unresolved contribution. If the task specifies a total force-error tolerance $\tau$, the bound supports that requirement when $b+\epsilon\leq\tau$. A stopping-position requirement instead needs propagation through the dynamics; a force bound alone is not a position bound.

For a joint probabilistic model with finite covariances,

$$
\Sigma_{\mathrm{net}}
=\Sigma_K+\Sigma_Z
+\operatorname{Cov}(\mathbf K,\mathbf Z)
+\operatorname{Cov}(\mathbf Z,\mathbf K).
$$

Neither a tolerance nor an independence assumption is supplied by writing the sum. The uncertainty description and dependencies must be established. Existing uncertainty accounting that already includes the omitted effects must not count them again under a new name. The [GUM treatment of combined uncertainty](https://www.iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/05_e.html) provides the standard propagation and dependence background; it does not establish this proposed haze definition.

The accurate claim is therefore that **all the uncertainties of the included contributions have been calculated**. Calling this “all the uncertainty of the net force” would assume the very sufficiency that remains to be established.

## 10. The unresolved mathematics of haze's zero

The user initially proposed three features: haze depends on $\epsilon$, it is a zero vector, and it has statistical character. The discussion considered a Gaussian description and a martingale description. These ideas need to be retained as proposals while their relationships are worked out.

Three meanings of zero must be distinguished:

1. **Exact zero:** the force quantity itself is $\mathbf 0$. Its magnitude is zero; a random variable identically equal to zero has no spread.
2. **Zero expectation:** the contribution may vary, but its expectation under a specified model and conditioning is zero.
3. **Zero at the reported resolution:** the contribution is represented as zero while information about its possible nonzero value is retained.

These statements are not interchangeable. Changing the tolerance cannot turn a nonzero expectation into an exact mathematical zero. Subtracting the known contributions cannot establish zero expectation either: it leaves a residual whose mean still requires determination.

The air-resistance example makes the distinction unavoidable. Drag opposes the relative motion; in a simple repeated fall through still air it can supply a consistently directed contribution. Such a contribution may be small enough for a particular approximation while retaining a nonzero mean. [NASA's falling-object account](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/falling-object-with-air-resistance/).

If haze is to include that kind of negligible directed effect, the exact-zero-mean definition alone is insufficient. The draft does not resolve this by silently changing the user's zero into an approximate equality. An eventual definition must specify how a reported zero, an underlying contribution, and the declared resolution relate. Standard metrology already permits a correction estimated as zero to carry nonzero uncertainty; that fact helps distinguish the quantities but does not settle the haze proposal. [GUM §5.1.5](https://www.iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/05_e.html).

A Gaussian distribution and a martingale property are also different specifications. For independent zero-mean Gaussian increments of variance $\sigma^2$, their cumulative sum $M_n$ is a martingale, with

$$
\mathbb E[M_n]=0,
\qquad
\operatorname{Var}(M_n)=n\sigma^2.
$$

Thus absence of predictable drift can coexist with increasing spread. A martingale does not inherently restore a trajectory to its original prediction. Its defining condition concerns conditional expectation given available information; it does not itself specify a small magnitude or variance. [MIT, Lecture 35](https://ocw.mit.edu/courses/18-440-probability-and-random-variables-spring-2014/95835880b8b2c186229980f4622897df_MIT18_440S14_Lecture35.pdf).

No martingale property of haze has been established. It would also matter which process is meant: force, accumulated impulse, velocity error, or a sequence of revised estimates. A property of one does not automatically transfer to the others. The argument for an explicit account of omissions survives while this statistical question remains open.

## 11. The human input and the evidence remain separate

The tolerance specifies what accuracy is required. Evidence and the model specify what uncertainty or unresolved contribution can be justified. Neither substitutes for the other.

Knowing the uncertainty very accurately does not tell us whether it is adequate for the user's purpose. Choosing a loose tolerance does not establish a probability distribution, a zero mean, a remainder bound, or the validity of an interaction attribution. A statistical confidence level and a practical tolerance are likewise different specifications.

The force account must also state what is being controlled. A force contribution small over a short interval may have a significant cumulative effect on a later position. Tolerance therefore belongs to a question with an observable, context, and interval, together with whatever allocation of error the calculation uses.

The proposed stopping claim is that the account is sufficient at that specification. It need not assert that every interaction has been identified. Conversely, failure to find another interaction does not establish that the residual meets the haze criterion. Some warranted determination or conditional assumption must support the stopping claim; evidence may later challenge it.

## 12. In what sense haze is needed and “has always been there”

The argument can now be stated without assuming a final mathematical definition:

1. A finite Newtonian prediction uses an explicit force account and other specified inputs.
2. A claim about the prediction's accuracy concerns the net force and resulting motion, including effects omitted from that account.
3. Uncertainty propagation restricted to the listed contributions does not establish the adequacy of the omissions.
4. Unlimited freedom to repair a discrepancy with an unaccounted force removes the restrictions needed to test that account.
5. A justified prediction therefore needs a constrained account of what may remain unresolved, and a way to recognize evidence that exceeds those constraints.
6. Haze is proposed as the explicit representation of that role in the force expression and trace.

This is the sense in which haze is needed: the **role** must be fulfilled for the stated adequacy of a finite, approximate force account to be warranted. The role might already be performed by a comprehensive uncertainty model, a controlled approximation, a bound, or explicit assumptions. The case for giving it a dedicated name and dictionary structure concerns making those commitments visible, connected, and reusable.

It is also the defensible sense of “has always been there.” Whenever an application has justifiably treated some effects as negligible, its justification already bears on what haze is intended to represent. An exact idealized model can instead explicitly assume no omitted contribution; its application to a physical experiment must justify that idealization to the accuracy claimed.

This is a logical reconstruction, not a historical finding that Newton or every later physicist explicitly possessed this term or one particular statistical theory. Standard uncertainty analysis already addresses incomplete models and omitted influences. [GUM §§3.3.2 and 3.4.2](https://www.iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/03_e.html). The distinctive VD proposal is to connect that issue to what counts as an explicit interaction contribution and to the point at which an unfinished force account must continue.

The central gain would be that a force expression carries both what has been accounted for and the constraint on what has not. A discrepancy could then be investigated against the same commitments used to produce the prediction. Revision remains possible, but revising the haze model, tolerance, or interaction account creates a revised claim; it does not retrospectively make the original exact prediction correct.

## 13. What remains to develop

The next work is concentrated in the definition, rather than in another numerical example of a near miss:

- Specify haze's type and the relationship between its force content, reported zero, mean, and uncertainty.
- Define the tolerance's observable, context, interval, and relationship to the total error requirement.
- State how evidence constrains the unresolved aggregate, including dependencies and systematic effects, and what can challenge that constraint.
- Explain the proposed “mean-like” role of impressed forces and how it handles stochastic interactions, cancellation, and small directed effects.
- Relate interaction membership at a tolerance to the existing interaction-set, without inferring physical absence from numerical insignificance.
- Establish the domain in which a finite explicit account suffices. Finite sufficiency at every admitted positive tolerance remains a proposed commitment, not a theorem established by this discussion.

The full staged NML3 algorithm, a haze entry, and automatic uncertainty handling have not been implemented. The successful earlier remainder expansion demonstrates one computational operation; it does not establish the physical or statistical claims in this draft. The existing ratified Force-Sum naming decision remains unchanged.

The working thesis is: **haze would make the sufficiency condition of a finite Newtonian force account explicit, by giving its unresolved contribution both a place and limits.**

## Sources, provenance, and scope

The primary source is the user-led conversation in **Recover NML3 haze findings**, 2026-09-10, task ID `01a08c58-8763-7590-b6e1-13e05a419a21`. The route from the literal cart prediction through statistical alternatives, the freely changing missing mean, the reversal toward what haze cannot explain, and tolerance-dependent interaction language comes from that conversation. The conditional-mean illustration and uncertainty equations are mathematical elaborations, not adopted VD entries.

The preceding task **Review NML3 trace progress**, 2026-09-09, ID `01a085b5-69da-7072-8a33-854ce9565cff`, supplied the trace-based origin. Relevant conversation turns and these local active sources were consulted:

- [Tolerance, special zero, and net-force uncertainty discovery, September 9](NML3_TOLERANCE_SPECIAL_ZERO_AND_NET_FORCE_UNCERTAINTY_DISCOVERY_2026-09-09.md): the original tolerance insight and candidate $Z_\epsilon$.
- [Remainder intermediate-expression algorithm, September 9](NML3_REMAINDER_INTERMEDIATE_EXPRESSION_ALGORITHM_2026-09-09.md): demonstrated expansion and unresolved staging.
- [Authority names, prediction sets, and falsifiability, September 8](AUTHORITY_NAMES_PREDICTION_SETS_AND_FALSIFIABILITY_2026-09-08.md): related provisional analysis of unrestricted auxiliary repair and the distinction between deriving a prediction and testing its premises. This local document preserves its own older source pins; it is supporting local analysis, not newly verified managed authority for this draft.
- [Ratified Force-Sum naming decision, August 26](../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md): current local `net-force / impressed-force / interaction-set` terminology and the identity/value distinction. This draft's remainder/haze proposal does not amend that decision.

Managed context was selected through [catalog.yaml](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/catalog.yaml), at **`canvalidk/VD-docs@0ad969e068e77175e86f6fe8dd24e6f9f7a965ce`**, reconfirmed from `main` when preparing this draft. The Warranted Force Account and Logical Consequences sources linked in sections 2 and 5 were read at that snapshot. The catalog retains them as entry-cut-independent conceptual sources; their earlier vocabulary is interpreted through the later local naming decision. Their historical entry formulations are not adopted here.

The September 9–10 haze work remains local and outside the managed catalog at this snapshot. `outbox/VD-Newton/` was checked: its September 8 receipt concerns the already closed earlier pass and does not receive this draft or the September 9 haze documents. No managed-context file was changed.

External checks are the primary metrology, mechanics, and probability sources linked where used: GUM sections 3 and 5, NASA's falling-object explanation, and MIT's martingale lecture. They support specific mathematical or methodological distinctions, not the claim that haze is a new physical discovery or a necessary new primitive.

Coverage is scoped to this argument and its immediate NML3 ancestry. Selection used the recent conversations, the local haze/algorithm/falsifiability documents, and catalog entries on force-account warrant and logical consequences; earlier discovery searches included `haze`, `epsilon`, `varepsilon`, and `remainder`. This is not an exhaustive NML3 synthesis, an audit of unclassified inbox material, a historical study of Newtonian practice, or a literature-priority review. Earlier documents remain unchanged.
