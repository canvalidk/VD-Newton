# Haze and what a successful Newtonian approximation claims

**Date:** 2026-09-12.  
**Status:** user-requested argument draft explaining the latest interpretation of haze. Its mathematical representation and its place in core Newtonian mechanics remain open.  
**Submission:** local draft in VD-Newton's pass to VD-docs folder; not submitted to the managed collection.

The question motivating this draft is:

> Serious people say that we can model the car as not having friction and find that their expectations differ from experimental results. What logical understanding must they have of Newton for their belief in Newton not to be shaken by this result?

The puzzle is not simply why an imperfect calculation can be useful. It is what the claim of success actually says. If someone predicts one trajectory, observes another, and nevertheless says, “Look at how we are correct about the car,” what proposition could they have successfully asserted?

Haze is being developed as an explicit representation of the unresolved contribution permitted by that proposition. The proposed understanding is that a finite force account can be sufficient for a specified prediction even though it omits physical interactions. A discrepancy from its nominal trajectory can fall within the prediction's declared allowance. A discrepancy beyond that allowance defeats the sufficiency claim without, by itself, identifying Newton's laws as the failed part.

This is a proposed logical reconstruction of the reasoning in the question. It is not a finding about what all engineers privately mean, or a proof that haze must be a new primitive of Newtonian mechanics.

**The car makes different commitments visible.**

Take a car coasting on a straight, level track after propulsion has ended. Work with its longitudinal centre-of-mass motion in an inertial frame, with constant mass. Let the explicit longitudinal force account be zero. Gravity and the support force need not be physically absent; the present calculation concerns their longitudinal components and the assumption of a level track.

The idealized model gives

$$
m\ddot x_C=0,
\qquad
x_C(t)=x_0+v_0t.
$$

The predicted motion is constant velocity. This friction-free model does not predict that the car eventually stops. A stopping-distance question would require a different account.

The earlier illustration included friction and omitted air resistance. The latest question deliberately uses a friction-free account. The same haze reasoning applies to both, but the nominal predictions must follow the contributions actually included.

There are at least three possible meanings of “we model the car as having no friction”:

| Claim | What a discrepancy would bear on |
|---|---|
| The actual car has exactly no longitudinal force and therefore exactly constant velocity. | Secure evidence of deceleration contradicts that combined claim. |
| An ideal system with zero longitudinal force has constant velocity under Newtonian mechanics. | A real car with additional interactions is not automatically a counterexample to this conditional statement. |
| The zero-force model approximates this actual journey adequately for a declared purpose and accuracy. | The question is whether the departure exceeds the permitted amount, accounting for measurement uncertainty. |

The third claim is the target of this haze proposal. It can justify using the idealized trajectory to answer a real question. The second claim alone does not establish that practical adequacy.

Nor may the third claim be introduced silently after the first has failed. If an exact prediction was actually asserted, admitting an approximation later revises the claim. It does not make the original exact assertion correct.

**Haze makes the approximation's omitted contribution explicit.**

Keep the net-force relation:

$$
\mathbf F_{\mathrm{net}}=m\mathbf a.
$$

Let $\mathbf C$ be the explicit contribution of the selected interactions. In the developing terminology, contributions are identifiable superpositions of impressed forces. Their identity and composition do not come merely from their ability to reproduce a measured resultant.

An acting-object instance supplies an identifiable interaction contribution, with the relevant participants and conditions of action. Naming a residual does not establish such an instance. This preserves the earlier VD distinction between physical attribution and arbitrary vector decomposition.

For a fixed target, context, and account, define

$$
\boxed{\mathbf H_{\mathbf C}=\mathbf F_{\mathrm{net}}-\mathbf C.}
$$

The expanded expression is

$$
\mathbf F_{\mathrm{net}}
=\mathbf C+\underbrace{\mathbf 0}_{\text{nominal omitted contribution}}
+\underbrace{\mathbf H_{\mathbf C}}_{\text{actual remainder}}.
$$

The explicit zero is algebraically redundant. Its proposed role is representational: the nominal calculation replaces the unresolved contribution by zero, while retaining a restriction on what that replacement leaves out.

This version does not require haze to have zero mean. Haze can contain a persistent, directed frictional contribution. It need not be random at all. A bound, a probability model, and uncertainty about an unknown value are possible descriptions with different commitments.

The subtraction itself is always available. The substantive claim is that the remainder satisfies a restriction appropriate to the prediction. Without that restriction, any discrepancy could be named haze and the account would exclude nothing.

**The allowance belongs to a question about the journey.**

Suppose the question concerns position during a specified interval $0\le t\le T$, with an allowed position error $\epsilon_x$. For the coasting example, use the same initial position and velocity in the ideal and actual trajectories. The exact difference is

$$
x(T)-x_C(T)
=\frac1m\int_0^T(T-t)H(t)\,dt,
$$

where $H$ is the longitudinal unresolved force.

If a supported bound gives

$$
|H(t)|\le b
\quad\text{throughout }[0,T],
$$

then

$$
|x(t)-x_C(t)|
\le \frac{bt^2}{2m}
\le \frac{bT^2}{2m}
\quad\text{for every }t\in[0,T].
$$

Consequently,

$$
\frac{bT^2}{2m}\le\epsilon_x
$$

is a sufficient condition for the stated position accuracy.

This explains why a short journey and a generous tolerance can make an omitted force irrelevant to the requested answer. It does not assert that the force ceases to act. The allowed duration, force size, mass, initial-state determination, and observable all participate in the claim. Short distance alone is not a universal guarantee.

For a hypothetical numerical example, take $m=1000\,\mathrm{kg}$, $v_0=2\,\mathrm{m/s}$, and a constant unresolved force $H=-20\,\mathrm N$ while the car moves forward. The resulting acceleration is $-0.02\,\mathrm{m/s^2}$. With $x_0=0$,

$$
x_C(t)=2t,
\qquad
x(t)=2t-0.01t^2.
$$

At two seconds the ideal prediction is $4\,\mathrm m$, and the actual position in this example is $3.96\,\mathrm m$. The difference is $0.04\,\mathrm m$. An expressly stated $0.05\,\mathrm m$ position allowance is met. The statement “exactly $4\,\mathrm m$” is not.

At five seconds the difference is $0.25\,\mathrm m$, exceeding the same allowance. The force has not changed; the prediction's scope has. These are illustrative calculations, not measurements of a particular vehicle. Initial-state and measurement uncertainty have been set aside in the calculation and must be included in an experimental judgment.

For the earlier friction-included, air-resistance-omitted example, the simple difference integral applies directly when the retained force is the same prescribed function of time along both trajectories. If the retained forces depend on the evolving state, comparing trajectories requires the corresponding dynamical error analysis.

**A force bound and a prediction tolerance are distinct commitments.**

The bound on $H$ above is sufficient for the position guarantee. It is not necessary: cancellation over time can make the position error small even when the force exceeds that bound.

Therefore, if the account explicitly claims both a force bound and a position tolerance, the force claim can fail while the position claim succeeds. We must state which proposition is being assessed. Calling every violation of a sufficient force bound a failure of the position approximation would repeat the very confusion haze is intended to remove.

The same distinction can be expressed more generally. Let $Q$ name the question being answered and let $E_Q(H)$ measure how much omitting $H$ changes that answer under the specified model and conditions. The adequacy claim is

$$
E_Q(H_{\mathbf C})\le\epsilon_Q.
$$

This is explanatory notation, not a ratified haze interface. The error measure, domain, and interpretation of the allowance still have to be specified.

**The unresolved aggregate is what the account depends on.**

Suppose two physically distinct omitted contributions have signed values

$$
H_1=-0.30\,\mathrm N,
\qquad
H_2=+0.25\,\mathrm N.
$$

Their aggregate is $-0.05\,\mathrm N$, within a $0.1\,\mathrm N$ resultant-force allowance even though neither contribution is individually within it. Conversely, several small contributions can add to an excessive remainder.

Thus “friction was larger than expected” may be true without establishing failure of the approximate account. Another omitted interaction may compensate for it. Equally, a failed account does not identify friction as the responsible interaction.

Haze expresses the aggregate condition. It distinguishes that condition from the later task of explaining the remainder through particular acting-objects. A numerically successful account also need not be an interaction-complete account: cancellation does not erase the physical interactions.

This is a claim about the sufficiency of the chosen account in the original conditions. It does not establish that physically removing one of the cancelling interactions would leave the motion unchanged.

**Experiments assess the allowance as well as the nominal answer.**

An actual residual estimate has the form

$$
\widehat{\mathbf R}
=\widehat{\mathbf F}_{\mathrm{net}}-\widehat{\mathbf C}
=\mathbf H_{\mathbf C}
+(\widehat{\mathbf F}_{\mathrm{net}}-\mathbf F_{\mathrm{net}})
-(\widehat{\mathbf C}-\mathbf C).
$$

It combines the actual unresolved contribution with errors in determining net force and the included contributions. The uncertainties of these determinations, including their dependencies, belong in the experimental assessment. Uncertainty in a listed force is not automatically an additional physical interaction. Standard metrology distinguishes a correction from uncertainty about that correction and includes covariances when combining uncertainties. [NIST TN 1297, section 5](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty)

For example, let $I$ be a properly constructed confidence interval for the true position discrepancy at the declared endpoint. Its relationship to the tolerance region $[-\epsilon_x,\epsilon_x]$ can support different conclusions:

| Evidence | Conclusion under the interval's assumptions |
|---|---|
| $I$ excludes zero but lies entirely inside the tolerance region. | A nonzero discrepancy is detected, while the stated approximation is supported. |
| $I$ is disjoint from the tolerance region. | The stated position adequacy is rejected at the corresponding evidential level. |
| $I$ crosses a tolerance boundary. | The evidence does not yet decide adequacy. |

The relevant scope must match the inference: an interval for one endpoint does not certify the entire journey. Failure to reject inadequacy is also different from establishing adequacy.

Repeated experiments can reveal a small systematic effect while leaving an unchanged practical tolerance satisfied. Detectability and the importance of an omission to the requested answer are distinct.

**The latest proposal also asks how much haze the finite evidence requires.**

The user's reversal of the earlier detection question is important. Instead of fixing a haze model and asking whether a small omitted force will eventually be detectable, fix the finite evidence and significance level and ask how large a haze allowance would make that evidence cease to reject the account.

For a specified family of haze models and a specified statistical procedure, write schematically

$$
h_{\mathrm{required}}(D,\alpha)
=\inf\{h:\text{the specified check does not reject the account at size }h\}.
$$

Here $D$ is the evidence, $\alpha$ the significance level, and $h$ a declared measure of haze size. The model family and check are implicit arguments. The set can be empty, in which case no permitted size makes that check compatible with the account. When the compatible sizes are nested and the boundary is attained, this gives a direct threshold comparison; otherwise the full set of compatible sizes must be retained.

The corresponding allowance $h_{\mathrm{allowed}}$ must be connected to the accuracy needed for the journey and to the supported physical or statistical restrictions. The question is whether the account can accommodate the evidence within that allowance.

For a simple Gaussian test of a mean, increasing an assumed variance can make a fixed finite residual mean nonsignificant. That inversion gives a calculable required variance. But the observations also contain information about scatter, direction, and dependence. Increasing variance may fail to explain those features. In particular, the earlier martingale check found that consistently negative independent Gaussian residuals can reject every variance through their signs.

This makes the proposal a useful analysis of the allowance the account needs, rather than an unrestricted rule for increasing uncertainty until any result is accepted. Computing the required size after observing the data is legitimate. Declaring that size afterward does not show that the original smaller allowance was adequate.

There are consequently two directions of reasoning:

$$
\text{required accuracy and scope}
\longrightarrow
\text{haze that may be permitted},
$$

$$
\text{finite evidence and a specified check}
\longrightarrow
\text{haze needed to accommodate that evidence}.
$$

A broad allowance can make a discrepancy unsurprising while rendering the prediction too imprecise to answer the question. Statistical non-rejection alone is not the meaning of “we are correct about the car.”

**A martingale is still a candidate representation, not the established meaning of haze.**

A martingale satisfies

$$
\mathbb E[M_{j+1}\mid\mathcal F_j]=M_j,
$$

with the required integrability and adaptedness. It does not inherently supply a small size, a variance bound, or a zero force level. Independent zero-mean increments have a martingale cumulative sum, while successively updated conditional expectations provide another martingale construction. [MIT, Lecture 35](https://math.mit.edu/~sheffield/440/Lecture35.pdf)

Whether force itself, accumulated force effects, or an evolving estimate is the martingale changes the physical and statistical claim. Neglecting friction over a short journey establishes none of those properties by itself. The bounded-remainder interpretation can already represent a small persistent braking force. The finite-evidence interpretation can investigate particular martingale families without making every omitted interaction a martingale.

**What, then, licenses continued confidence in Newton?**

There are two cases that must remain separate.

If the observation differs from the nominal trajectory but remains within the warranted allowance, the approximate prediction has not failed on that ground. Its content already permitted the departure. Confidence need not be protected from a contradiction that never arose.

If the observation exceeds the allowance, something in the full predictive account has failed. A prediction depends on Newtonian laws together with the force account, parameters, initial conditions, frame and system assumptions, and the observation model. A discrepancy does not deductively identify which part failed.

Continued confidence in Newtonian mechanics can then be reasonable when there are independent grounds to revise a local assumption: for example, known friction was omitted, an independently calibrated force estimate was wrong, or the interval was long enough for neglected resistance to matter. A more complete account should explain the residual and support further predictions or independent checks.

The logical possibility of such a revision does not guarantee that it is justified in a particular experiment. If the force account and the other assumptions survive serious checks, confidence in the dynamical laws can also be challenged. Haze must preserve that possibility.

An arbitrary $H=ma-C$ fitted separately to every result establishes no physical explanation. It does not independently identify friction, certify a new acting-object, or test the equality used to define it. The restrictions on haze and the warrants for explicit contributions are what keep the account accountable.

The coherent understanding behind the quoted reasoning is therefore conditional: the nominal idealization was used with an allowance for its application to the real car; the experiment either met that allowance or supplied evidence about which part of the predictive account required revision. Neither response licenses silently changing what was originally claimed.

**Whether this belongs to core NM remains an open question about the scope of the theory.**

There are three claims of increasing strength:

| Claim | What this argument establishes |
|---|---|
| Newtonian equations can describe exact idealized systems. | Nothing here requires adding an approximation tolerance to every such mathematical description. |
| A warranted approximate application to a real car needs an account of the permitted departure from the idealized prediction. | The car argument identifies this role. Haze is a candidate explicit representation of it. |
| Core NM must contain a distinct haze object or primitive. | This does not yet follow. The role might be supplied through approximation conditions, uncertainty models, or the rules for applying and closing a force account. |

If “core NM” means only the dynamical equations, those equations do not choose a prediction's purpose, tolerance, or experiment. If it includes the conditions under which the theory makes warranted finite claims about real objects, the connection between explicit contributions and permissible omissions becomes part of what must be explained.

The live VD question is whether that connection is constitutive of a properly usable force-sum law: does the law need to carry an explicit account of what remains unresolved before it can license a finite prediction? Or can its application rules supply the same content without a separate haze object? The present argument sharpens this choice and leaves its resolution open.

Existing model-discrepancy work already separates a physical model's unresolved discrepancy from observation error and studies its effect on inference. That supports the relevance of the problem while leaving the proposed VD placement undecided. [Brynjarsdóttir and O'Hagan, 2014](https://www.tonyohagan.co.uk/academic/pdf/simmach.pdf)

The question for further development is whether haze makes the assertion “this force account is sufficient for this question” explicit in a way the intended core of NM must preserve. The car example supplies a concrete case against which that proposed requirement can be assessed.

---

**Sources, precedence, and custody**

The primary authority is the user-led September 11–12 discussion in this task: the bounded aggregate remainder, the explicit nominal zero, cancellation among omissions, the reversal to finite-evidence required haze, and the latest focus on what a successful approximate Newtonian claim means. These later instructions govern where the earlier local drafts left the definition open.

Local active sources inspected in this task or its preceding investigation include:

- [Haze and the logic of Newtonian force accounts, September 10](NML3_HAZE_AND_THE_LOGIC_OF_NEWTONIAN_FORCE_ACCOUNTS_2026-09-10.md): the earlier argument, the exact-prediction warning, and the open statistical meanings of zero.
- [MFP1 detection with haze: investigation brief, September 11](MFP1_DETECTION_WITH_HAZE_INVESTIGATION_BRIEF_2026-09-11.md): the investigation's premise and aims. It predates the latest bounded-remainder and finite-evidence refinements.
- [Force-Sum naming decision, August 26](../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md): current net-force / impressed-force / interaction-set terminology and the distinction between interaction identity and vector value.

Managed context was selected through [catalog.yaml](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/catalog.yaml), at **canvalidk/VD-docs@0ad969e068e77175e86f6fe8dd24e6f9f7a965ce**, resolved from main when preparing this draft:

- [Warranted Force Account: Foundational Explication](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md): independent warrant for interaction attribution and the insufficiency of successful vector decomposition.
- [NML3 Logical Consequences](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/nml/nml3/_dscn_nml3_content/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md): especially consequences 6, 14, and 15 on cancellation, closure, and residual-test asymmetry.
- [Acting-object architecture consolidation](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton/Design%203/vd_acting_object_architecture_consolidation.md): background on participants, activation, and force relations. Its historical entry architecture is not adopted by this draft.

The managed conceptual sources inform this interpretation; they do not contain or ratify this latest haze formulation. The September 9–12 haze development remains local and unsubmitted at this snapshot. No existing managed or local source was revised.

External sources are linked at the claims they support. The trajectory calculation and logical reconstruction are developed here. This is a scoped argument, not an exhaustive review of engineering practice, a survey of philosophies of Newtonian mechanics, or a claim of mathematical priority. Selection followed the relevant catalog entries and the local haze/MFP1 document lineage; unclassified inbox material was not exhaustively audited.

The managed outbox for VD-Newton was checked at the same commit. It contains the September 8 receipt for the previously closed pass; that receipt does not receive this draft. Saving the draft locally does not transfer it to VD-docs.
