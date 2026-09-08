# Source and drafting record for the mass-estimation introduction candidate

**Date:** 2026-09-06; revised after C1–C9, the shorter introduction, and the subsequent request to fill the shared-quantity argument  
**Status:** local authoring record; awaiting transfer to VD-docs.  
**Candidate:** [mass_estimation_introduction_candidate_2026-09-06.md](mass_estimation_introduction_candidate_2026-09-06.md).

## 1. What was written

The active local candidate has been rewritten around a shorter problem-setting sequence:

1. Three numbered Newton-II operations, with the first two explained before the vector-division hook.
2. The early question "What, then, is mass?" and a brief zero-zero observation.
3. The magnitude proposal, a perpendicular-vector example, and measurement uncertainty.
4. The question whether prior alignment can be required, followed by the shared-quantity/input-dependency argument.
5. Two dot-product proposals that disagree on unaligned inputs.
6. The closing question that leads into the planned type-theory analysis.

The user initially requested a blank section 3, then authorized filling it after first isolating the pieces of the larger VD argument needed here. Section 3 now states the shared-quantity premise and the requirement that each operation remain usable when its output is unavailable, applies them in both directions, and distinguishes a complete empirical determination from a restricted quotient. The preceding counterexample alone does not establish that prior alignment is an inadmissible general input condition.

The rewrite implements C1–C5 and the example-before-dependency ordering in C8–C9. It uses ordinary mathematical notation and no VD branding in the audience-facing prose, as requested in C6. Section 3 includes C7's downstream-use consistency paragraph, qualified by fixed evidence and a fixed determination procedure. The numbering proposal does not commit the later type-theory analysis to treating VD operations as conventional delta reduction.

The detailed exact and measured zero discussion, bounds, positive-parameter illustration, and engineering example have been removed from the introduction. Their prose is retained in section 6 of this record for possible later use. The active introduction does not choose an estimator, loss, prior, or measured-null policy.

## 2. Managed context

**Snapshot:** canvalidk/VD-docs@743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6. This coherent snapshot was resolved and read earlier in the same drafting session; catalog.yaml supplied inventory and draft status. The present rewrite uses those established sources and the active local candidate, without claiming a fresh managed-context update.

Principal sources read at that snapshot:

- [Existing introduction](https://github.com/canvalidk/VD-docs/blob/743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6/Newton-analysis/_note_why_mass_estimation/why_mass_must_be_estimated_introduction_d2.md): catalog d4, partial, not current; its filename suffix is legacy. Supplies the opening material, exact cases, and measurement discussion.
- [Why reconciliation cannot be upstream of E10](https://github.com/canvalidk/VD-docs/blob/743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6/Newton-analysis/_dscn_mass_estimator/why_reconciliation_cannot_be_upstream_of_E10.md): the ratified input-dependency and shared-quantity argument; refetched for this draft.
- [Current full argument](https://github.com/canvalidk/VD-docs/blob/743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6/Newton-analysis/_note_why_mass_estimation/why_inertial_mass_must_be_estimated.md): catalog-current d3; read during this session. Supplies exact/empirical scope and the distinct latent-pair route.
- [Chain audit](https://github.com/canvalidk/VD-docs/blob/743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6/Newton-analysis/_dscn_mass_estimator/what_forces_the_chain_to_the_estimator.md): read during this session; restricts the inoperability claim to operations invoked when their outputs are unavailable.
- [September 5 research](https://github.com/canvalidk/VD-docs/blob/743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6/Newton-analysis/_dscn_mass_estimator/mass_estimator_originality_research_2026-09-05.md): source leads for the narrowly targeted external verification below.

Active local authoring inputs, both in this folder:

- [Introduction development plan](mass_estimation_introduction_development_plan_2026-09-06.md).
- [Robust VD argument and adjacent consequences](vd_shared_quantity_argument_mass_estimation_2026-09-06.md).

The user first authorized a new local candidate, then explicitly authorized this rewrite. No managed d-number has been assigned and no managed introduction has been edited or promoted.

## 3. Evidence for material deferred from the introduction

### A. Bound from an unresolved acceleration

This is an explicitly constructed illustration, not a report of an industrial experiment. The force is supplied as 5 N; the acceleration result has a stated admissible magnitude at most 0.01 m s^-2. Conditional on those premises and positive-mass Newton II, the allowed acceleration is positive and the compatible masses are at least 500 kg, with no finite upper limit from that bound alone.

If the acceleration allowance is probabilistic, its calibration and interpretation must be supplied; the calculation does not invent a confidence level. If force also has uncertainty, it must be incorporated rather than silently keeping the numerator exact. The example's purpose is to distinguish a finite lower bound from an undefined displayed quotient.

### B. Positive estimate from a zero Gaussian reading

Primary source checked on 2026-09-06: [Roe and Woodroofe, section II.A, equations (1)-(2)](https://arxiv.org/pdf/hep-ex/0007048). It supplies the conditional density. The zero-reading mean and force-to-mass application are our illustrative calculations; the paper does not propose that mass estimator. Positivity alone does not select the assumed prior or mean readout.

### C. Engineering treatment of null signals

Primary source checked on 2026-09-06: [Hans Butler, EP1455231A2, section 2.4](https://patents.google.com/patent/EP1455231A2/en), published 2004-09-08. The described adaptation is suspended when commanded acceleration is zero; the alternative bound applies to adaptation gain. It is not evidence that the device returns sigma_F/sigma_a. The deferred passage uses it only to establish a concrete engineering instance of null-signal handling.

The patent is used as a technical disclosure, not as a legal-status or patentability source. No claim that all industrial practice uses this method is made.

## 4. Editorial checks and remaining work

Every displayed equation in the rewrite has a unique sequential number, (1)–(8). The first three operations are displayed separately so later prose can refer to them without ambiguity. The magnitude example precedes the uncertainty paragraph, and both precede the question about the admissibility of requiring aligned inputs.

### The pieces of the VD argument used in section 3

The draft isolates two operational premises and one empirical fact:

1. **Shared quantities:** force and acceleration retain their meaning across the three operations. For fixed evidence and a fixed determination procedure, choosing a later consumer does not change the result. This does not require different instruments or differently conditioned estimates to return identical numbers.
2. **Determination with an unavailable output:** the force operation must remain usable from supplied mass and acceleration without an already obtained force; the acceleration operation must remain usable from supplied mass and force without an already obtained acceleration.
3. **Possible empirical disagreement:** the independently obtainable measurement results may be unaligned, as section 2 has already explained. A common direction imposed by experimental geometry is a special case, not a general guarantee.

From the two operational premises, derive the dependency constraint separately for each vector. Requiring acceleration to be aligned to the force being sought makes its admission require unavailable force-direction information. Requiring force to be aligned to the acceleration being sought creates the converse obstruction. Adjusting only one vector can already disable one required direction. The argument requires admissible independent routes where their evidence exists; it does not ban deriving one vector from the other or require uncorrelated errors.

The connection to the magnitude quotient has two distinct parts. Compulsory alignment cannot be built into obtaining the shared quantities. A helper restricted to compatible pairs is nevertheless legitimate, but does not by itself answer an empirical mass demand starting from unaligned measurements. A joint construction of a distinct compatible pair is also legitimate; its work belongs to the complete determination, even when a separate routine performs it before the final quotient.

Only these premises and consequences are needed here. The draft does not import VD terminology, dictionary expansion, delta reduction, trace structure, fit diagnostics, a specific uncertainty measure, or a readout-selection theorem. Its primary local source is sections 2–8 of the robust-argument note, grounded in the managed reconciliation ruling and chain audit at the snapshot above.

### Other checks

The dot-product calculations are elementary deductions in this drafting task, not claims attributed to an external source. Dotting the exact relation with acceleration yields equation (5); dotting with force yields equation (6), where the respective denominators are nonzero. For reported force (2,1) N and acceleration (1,0) m s^-2, the formulas give 2 kg and 2.5 kg, while the magnitude quotient gives sqrt(5) kg. Writing the dot product as the product of the norms and cos(theta) yields equations (7)–(8). The acute-angle condition keeps both denominators and both readouts positive; perpendicular and obtuse cases are discussed separately.

The argument establishes disagreement between candidate extensions, not the impossibility of a justified estimator. A measurement model or fitting criterion can favor a readout; that choice is additional content rather than an algebraic consequence on incompatible inputs. Exact nonzero codirectional scalar recovery remains valid.

The brief opening zero-zero discussion distinguishes the physical mass's positivity from a determination's failure to identify it. The later examples retained below continue to distinguish exact inconsistency, exact non-identification, a bound, a model-dependent point, and suspended adaptation.

The introduction stops at the need for a definition of empirical mass determination. The type-theory analysis and the estimator construction remain outside this rewrite.

## 5. Submission and coverage

Both files are saved under the workspace-root `pass to VD-docs/` policy. They are local active drafts awaiting transfer, not received managed records. This is a scoped local rewrite. The two primary-source checks were performed earlier in this drafting session; this revision is not a new literature, originality, or inbox review.

The existing managed introduction, local plans, robust-argument note, readout-uniqueness note, active Newton entries, and evaluator work remain unchanged.

## 6. Prose retained for later sections

The following text was moved out of the preceding local candidate. It is working material for later placement, not part of the revised introduction and not a commitment to the eventual section order.

For exact inputs, those arithmetic difficulties correspond to two different physical statements. If exactly one of force and acceleration is zero, no finite positive mass satisfies Newton II. If both are zero, every positive mass satisfies

$$
\mathbf0=m\mathbf0.
$$

The law is compatible with the pair, but the pair does not determine the mass. Multiplication by zero has erased the distinction among the possible positive values. Calling both situations 'undefined' hides the difference between a contradiction in the exact premises and agreement that leaves mass unidentified.

There is operational pressure here as well. Mass is supposed to supply the positive scalar that the other two calculations consume. If its determination returns an undefined result, those calculations cannot simply proceed as before. This need not mean that the object's physical mass is undefined; a particular determination can fail to identify a value. But then that failure and its consequences belong in the account of the operation. Assigning an arbitrary positive number would satisfy the numerical type without supplying the missing determination.

In empirical work, however, a reported zero is not an exact-zero premise. A force instrument that reports zero with a stated uncertainty has not established that the underlying net force vanishes. An acceleration channel that cannot resolve a change in motion has not established an exact absence of acceleration. The distinction changes what the mass demand can learn from the result.

Consider a simple one-dimensional illustration. Take a supplied net force of 5 N. Suppose an acceleration measurement reports zero, with a declared admissible range whose magnitude is at most 0.01 m s^-2. Under finite positive-mass Newton II, the acceleration must be positive in the force direction. Consequently, the compatible possibilities satisfy

$$
0<a\leq0.01\ \mathrm{m\,s^{-2}},
\qquad
m=\frac{5\ \mathrm N}{a}\geq500\ \mathrm{kg}.
$$

The unresolved reading can support a lower bound under those assumptions. It does not identify one finite mass, and the bound has whatever evidential standing the declared acceleration range has. But dividing by the displayed zero would communicate none of this. In the reciprocal situation, an unresolved force under a resolved positive acceleration can instead support an upper bound on mass.

Finite positive point estimates can also arise from a zero reading once an explicit measurement model is supplied. For example, consider a nonnegative quantity observed with Gaussian error of scale sigma, with uniform prior weight over its permitted values. At a reported zero, its conditional distribution is half-normal; its mean is sigma times sqrt(2/pi). This follows from the density in [Roe and Woodroofe, section II.A, equations (1)-(2)](https://arxiv.org/pdf/hep-ex/0007048).

Applied to force in a known direction, with acceleration supplied as 5 m s^-2, that particular mean-based determination gives

$$
\widehat m=
\frac{\sigma_F\sqrt{2/\pi}}{5\ \mathrm{m\,s^{-2}}}>0,
$$

where the quotient of the reported central values gives zero. This is an illustrative inference under stated assumptions, not a universal prescription for a zero reading. Its significance here is that the additional measurement assumptions change the answer. To accept such a result as a mass determination is to accept an operation that the quotient of the reported values does not describe.

The need to handle null signals is also visible in an actual engineering account. A published method for estimating the mass of a lithographic stage describes intervals with nominally zero force and acceleration in which noise dominates. It suspends adaptation at zero commanded acceleration, with a bound on the adaptation gain offered as an alternative. [Butler, section 2.4](https://patents.google.com/patent/EP1455231A2/en)

These examples pose different choices: report a bound, construct a point under a specified model, or refrain from updating an existing estimate. The equation F = ma does not, by itself, say which operation should be performed on a reported zero. Nor does the existence of a positive numerical output establish how much the experiment has determined about the object. At measured zero-zero, both questions become particularly pressing: what result should the operation produce, and what would that result warrant?
