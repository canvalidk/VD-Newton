# Entry Packet: E10 Inertial-Mass-Material-Object — d4

Status: successor candidate after the independent-measurement / joint-fit
correction. This packet supersedes d3 as the working account of E10. It does not
promote new wording into the active Design 2.1 entry draft. The d3 packet remains
as the pre-correction reasoning state.

## ENTRY PACKET

Entry id:
  [E10]

Headword:
  inertial-mass-material-object

Status:
  candidate; not yet promoted

Role:
  triplet-winter

Law/block:
  Newton II; checked exact-recovery and joint-estimation corner of the addressed
  triplet

Source status:
  Revised from the E10 d3 packet using the local ingestion-ready handoff
  `07_design_2_1/notes/vd_docs_handoffs/why_the_mass_entry_must_be_long_joint_measurement_d3.md`.
  Both were drafted against the coherent VD-docs `main` snapshot at commit
  `8e09dbf9d3e521cbe76e36426ead656c04a71650` (2026-07-31). No claim is made here
  that the local handoff has already been ingested into VD-docs.

Managed sources at that commit:

  1. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT_d2.md` — current NML2.1 content
     authority and lesson-side exact/measured boundary.
  2. `Newton-analysis/vector_division_mass_estimation/type_theoretic_analysis_newton_II_mass_recovery_d2.md`
     — exact checked-recovery analysis in sections 1–6. Its measured-vector
     extension is superseded by the local d3 handoff.
  3. `Newton-analysis/vector_division_mass_estimation/vector_division_inertial_mass_measurement_d1.md`
     — still-live estimator mathematics, including estimator non-uniqueness,
     errors-in-variables structure, limiting cases, and the multiple-trial
     argument.
  4. `Newton-analysis/vector_division_mass_estimation/why_the_mass_entry_cannot_be_short.md`
     — historical entry-writing argument, fully superseded by the local d3
     handoff.
  5. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md` — lesson-plan draft,
     subordinate to NML2.1 content d2 where they conflict.
  6. `Newton/entry passes/E10_ENTRY_WRITING_PASS_2026-07-25.md` and
     `Newton/entry packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d2.md`
     — managed reasoning history, not current semantic authority.

Active local sources:

  1. `07_design_2_1/notes/vd_docs_handoffs/why_the_mass_entry_must_be_long_joint_measurement_d3.md`
     — governing correction for this packet.
  2. `07_design_2_1/entry_packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d3.md`
     — immediate predecessor and pre-correction packet state.
  3. `07_design_2_1/entry_writing_passes/E10_ENTRY_WRITING_PASS_2026-07-25.md`
     — earlier local reasoning record.
  4. `07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md` — active entry draft; not
     changed by this packet.
  5. `07_design_2_1/notes/lesson_entry_notes/ENTRY_WRITING_PASS_INTAKE_2026-07-26.md`
     — provenance and integration record.

Selection method:
  Inherited d3's catalog and informing-link search for `E10`,
  `vector_division_mass_estimation`, `mass recovery`, `codirectional`,
  `estimation`, and `NML2.1`, then applied every correction stated in the local
  d3 handoff to the packet, candidate entry, evaluator requirements, and tests.

### Governing correction

E10 sits at the junction of two operations:

```text
explicitly exact Newton-II quantities
    -> checked exact recovery

independently produced empirical measurement results
    -> joint Newton-II-constrained estimation
```

The empirical branch is not a noisy version of the exact branch. Before the
joint operation, three things must remain distinct:

```text
observations
independent measurement results
jointly estimated latent Newton-II quantities
```

Observations feed the separate force-side and acceleration-side measurement
procedures. Those procedures return measurement results with uncertainty and
provenance. A later joint fit consumes both results and a declared estimation
policy, imposes the Newton-II relation on latent values, and returns a result in
which inertial mass is one field.

Therefore the measured branch is selected by empirical provenance, not by
visible non-codirectionality. Even an exactly aligned displayed measurement pair
remains measured and takes the joint branch. The fit must retain the original
measurements and their discrepancy; otherwise the imposed relation can appear
to confirm itself.

### Old wording lineage

The d3 candidate ended with:

```text
For non-codirectional measured vectors, estimate two underlying codirectional
vectors and then recover the positive scalar relating them.
```

That was too narrow. It made displayed alignment rather than epistemic status
the branch selector, treated measurement results as bare vectors, and allowed a
bare `MassEstimateResult` to hide the latent values and residual.

### Preserve

  - inertial mass is a positive scalar;
  - all three Newton-II quantities belong to the same material object and carry
    compatible frame and time/interval qualifications;
  - the inward relation is
    `net-force-material-object = inertial-mass-material-object ×
    inertial-acceleration-material-object`;
  - an explicitly exact compatible nonzero pair determines one positive scalar;
  - an exact zero/zero pair is compatible but non-determining;
  - exact one-zero and exact non-codirectional pairs admit no exact positive-mass
    fit for those premises;
  - supplied mass bindings remain distinct from exact recoveries, joint
    estimates, and consistency restatements;
  - the lesson-facing joint route remains `estimate two underlying
    codirectional vectors and then recover the positive scalar relating them`;
  - mass-address origination, persistence, additivity, gravitational bridges,
    and force-composition provenance remain outside E10.

### Change / reject

  - Do not route only visibly non-codirectional measurements to estimation.
    Every empirical mass determination takes the joint branch.
  - Do not relabel an aligned empirical pair as exact merely because rounded or
    displayed values point the same way.
  - Do not treat a measurement result as a bare vector. Preserve its uncertainty,
    calibration/model basis, and provenance.
  - Do not redefine either independent measurement so that it already agrees
    with the other through Newton II.
  - Do not return a bare `MassEstimateResult`. Return the latent force, latent
    acceleration, mass, uncertainty, corrections or residual, goodness of fit,
    estimation policy, and measurement provenance together.
  - Do not discard the discrepancy after imposing codirectionality on the latent
    values. A fit without a surviving residual makes the law appear to confirm
    itself.
  - Do not treat two evidentially circular inputs as an independent mass
    determination.
  - Do not divide vectors or choose a magnitude-ratio, projection,
    componentwise, least-squares, or other estimator without a declared policy.
  - Do not use a fixed direction tolerance and magnitude floor as a measurement
    model.
  - Do not hide the joint operation inside the word `measurement`, the IRIL, a
    packet note, or an unnamed refined type.

Plain purpose:
  Complete the Newton-II triplet by identifying the positive scalar relating one
  material object's addressed inertial acceleration and net force, while
  distinguishing checked recovery from exact supplied quantities from joint
  inference using independent empirical measurement results. NML2.1 exposes the
  route but does not teach the estimator mathematics.

Relationship to the packet set:

  - one winter daughter of E8;
  - relates E9's net force to E8's inertial acceleration;
  - unlike E8 and E9, does not define a total operation on its ordinary pair of
    input quantity types;
  - triggers, but does not itself choose or teach, the later joint estimation
    machinery;
  - deliberately does not replace the deferred outward mass-address wall.

Trace-critical headword mentions:

  - net-force-material-object
  - inertial-acceleration-material-object

Other structural qualifiers:

  - one material object owns the mass, force, and acceleration values;
  - each force/acceleration input is classified as explicitly exact/supplied or
    empirically measured;
  - a measurement result carries uncertainty and provenance rather than only a
    displayed vector value;
  - the two empirical channels must have sufficiently independent provenance
    for the joint result to stand as independent evidence for mass;
  - a joint fit preserves both original measurement results and the discrepancy
    between them and its latent outputs.

Forbidden headword mentions / hidden imports in the eventual entry wording:

  - scale / weight / gravitational mass / amount of matter / density mass;
  - mass additivity;
  - target construction / trackability / lumping;
  - interacting-forces-set / attached-force;
  - constancy or persistence across trials;
  - a particular estimator, covariance model, or fitting formula;
  - a claim that the independently measured values were already the reconciled
    latent values.

Question or trace moment this helps with:

  1. Exact branch: do these explicitly exact force and acceleration values admit
     one positive scalar, and if so what is it?
  2. Empirical branch: what joint operation is required to infer mass from two
     independent measurement results?
  3. Fit-standing branch: what discrepancy and provenance must survive before
     the joint result can count as evidence rather than self-confirmation?
  4. Consumption branch: is there already a licensed supplied mass binding?

Witness kind:
  addressed material-object force-accounting commitment; checked exact recovery
  or joint-estimation handoff, not the deferred material-object construction or
  mass-persistence machinery.

Slots read:

  - material-object identity;
  - net-force-material-object and inertial-acceleration-material-object;
  - exact/supplied versus empirical-measurement status;
  - common frame, time/interval, units, and quantity qualifications;
  - supplied mass binding, where one exists;
  - licence and provenance status;
  - for empirical inputs, separate `MeasuredForceResult` and
    `MeasuredAccelerationResult` values, uncertainties, and provenance;
  - measurement-channel independence or circular-dependence record;
  - a declared estimation policy only after routing to the empirical branch.

Slots written / exposed:

  - inertial-mass-material-object when supplied, exactly recovered, or returned
    as a field of a licensed joint fit;
  - `ExactMass(m)`;
  - `ZeroZeroUnderdetermined`;
  - `ZeroNonzeroInconsistency`;
  - `NoncodirectionalExactInconsistency`;
  - `EstimationRequired` when empirical inputs reach the NML2.1 boundary without
    in-scope machinery;
  - `JointNewtonIIFitResult` when licensed machinery is available;
  - supplied / exact-recovered / jointly-estimated / consistency-restatement
    provenance.

## Exact and empirical operations

Exact recovery is result-valued:

```text
MassExact:
  ExactForceVector × ExactAccelerationVector
  -> MassRecoveryResult
```

Its outcomes include:

```text
ExactMass(m)
ZeroZeroUnderdetermined
ZeroNonzeroInconsistency
NoncodirectionalExactInconsistency
```

For an exact, nonzero, codirectional pair:

```text
m = |net force| / |inertial acceleration|
```

The codirectionality check establishes that a positive scalar exists. The
magnitude quotient then reads that scalar; it does not establish compatibility.

The independent measurement channels return richer inputs:

```text
MeasuredForceResult(
  displayed_force,
  uncertainty,
  measurement_provenance
)

MeasuredAccelerationResult(
  displayed_acceleration,
  uncertainty,
  measurement_provenance
)
```

Joint empirical estimation is a third operation:

```text
JointNewtonIIFit:
  MeasuredForceResult
  × MeasuredAccelerationResult
  × EstimationPolicy
  -> JointNewtonIIFitResult
```

with a result containing at least:

```text
JointNewtonIIFitResult(
  original_force_measurement,
  original_acceleration_measurement,
  underlying_force = F*,
  underlying_acceleration = a*,
  inertial_mass = m,
  uncertainty,
  corrections_or_residual,
  goodness_of_fit,
  estimation_policy,
  measurement_and_policy_provenance,
  independence_or_circularity_status
)
```

subject to:

```text
F* = m a*, with m > 0
```

Neither latent vector is selected independently once the constraint is imposed.
The star values are model-constrained outputs, not corrected meanings silently
substituted for the two independent measurements.

## Lesson boundary

NML2.1 should transfer the topology of the empirical operation without teaching
its statistical formula.

Students should retain:

```text
estimate two underlying codirectional vectors and then recover the positive
scalar relating them
```

NML2.1 may teach:

  - exact supplied values and empirical measurement results are different input
    kinds;
  - exact mass recovery checks compatibility before taking a magnitude quotient;
  - exact zero/zero does not determine mass;
  - independent force and acceleration measurements need not be codirectional;
  - every empirical mass determination takes the joint branch, even when the
    displayed values happen to align;
  - a measured disagreement does not mean the object has no mass;
  - the joint estimator would estimate two underlying codirectional vectors and
    then recover the positive scalar relating them;
  - the course-level output may be
    `estimation required — method outside the present scope`.

NML2.1 must not teach or silently select:

  - magnitude ratio as a general estimator for measured data;
  - either projection estimator;
  - componentwise averaging;
  - least squares, errors-in-variables, Deming regression, orthogonal-distance
    regression, likelihood construction, or covariance weighting;
  - how an estimation policy is selected or certified;
  - how the force-side or acceleration-side uncertainty models are certified;
  - how later force-composition machinery constructs net force.

The boundary remains capability-named:

```text
NML2.1 owns recognition and conceptual routing.
Later joint-measurement/estimation machinery owns policy selection and execution.
```

Whether that later capability is E12 or a separately named entry remains open.

## Boundary behavior

  - Licensed supplied binding: return it, preserving provenance and licence.
  - Exact, nonzero, codirectional pair: return `ExactMass(m)`.
  - Exact zero/zero pair: return `ZeroZeroUnderdetermined`; do not overwrite a
    licensed supplied binding.
  - Exact pair with exactly one zero: return `ZeroNonzeroInconsistency`.
  - Exact nonzero pair with no positive-scalar fit: return
    `NoncodirectionalExactInconsistency`.
  - Any empirical measurement-result pair without in-scope joint machinery:
    return `EstimationRequired`, irrespective of displayed alignment.
  - Empirical results with a declared, licensed policy: invoke
    `JointNewtonIIFit` and preserve all required result fields.
  - Empirical inputs whose evidential paths depend on the demanded mass or on
    each other through this same Newton-II relation: mark the outcome as a
    consistency restatement, not an independent mass determination.
  - A joint output that omits the original results, residual, uncertainty,
    policy, or provenance: reject as an incomplete fit result.
  - Missing exact/measured status: halt for classification; do not guess.
  - Missing value: demand it if the graph has an independent route; otherwise
    return insufficient information.
  - Address, frame, time, type, or dimensional mismatch: halt before either
    exact recovery or joint estimation.
  - Expired binding: do not reuse it automatically.

## IRIL — ideal residually imparted logic

Allowed:

  - On a demand for `inertial-mass-material-object` for one material object,
    first return a licensed supplied binding if present.
  - Otherwise demand that object's net-force and inertial-acceleration inputs
    together with their exact/supplied or empirical-measurement status and
    common qualifications.
  - If the pair is explicitly exact, run `MassExact`:
    1. check zero/nonzero status;
    2. for a nonzero pair, check whether one positive scalar relates them;
    3. only after compatibility passes, divide net-force magnitude by
       inertial-acceleration magnitude;
    4. return the appropriate result-valued outcome.
  - If the inputs are empirical measurement results, preserve each result,
    uncertainty account, and provenance as a separate input to the joint branch,
    regardless of displayed codirectionality.
  - Test whether either empirical input already depended on the demanded mass or
    on the other input through the same Newton-II relation.
  - Within NML2.1, stop the empirical branch at `EstimationRequired` and state
    the conceptual route: estimate two underlying codirectional vectors and then
    recover the positive scalar relating them.
  - Outside that lesson boundary, invoke `JointNewtonIIFit` only with a declared,
    licensed estimation policy.
  - Preserve the original measurement results alongside the latent values and
    retain uncertainty, corrections or residual, goodness of fit, policy, and
    provenance in the joint result.
  - Record whether a mass value was supplied, exactly recovered, jointly
    estimated from sufficiently independent channels, or merely restated through
    circular inputs.
  - When a licensed mass binding and the other two corners are all present, use
    the relation as a consistency check; do not silently replace the binding.

Blocked:

  - Dividing one vector by another.
  - Dividing magnitudes before checking compatibility on the exact branch.
  - Applying the exact branch to empirical results because their displayed
    vectors align.
  - Sending only visibly non-codirectional empirical pairs to joint estimation.
  - Rewriting either independent measurement so that it already satisfies
    Newton II before the joint fit.
  - Returning only a mass or only compatible latent values from the joint fit.
  - Discarding the original discrepancy, correction record, or goodness of fit.
  - Reporting circularly derived inputs as independent evidence for mass.
  - Applying an undeclared direction tolerance, magnitude floor, magnitude
    ratio, projection, componentwise division, or fitting formula.
  - Returning a value from an exact zero/zero trial.
  - Combining values belonging to different material objects or incompatible
    frame/time qualifications.
  - Treating scale readings, weight, gravitational mass, density mass, or amount
    of matter as this value without a separately licensed bridge.
  - Inferring mass additivity, target construction, persistence, or constancy
    from the inward triplet relation.
  - Reusing an expired binding.

Trace consequence:

  - exact, nonzero, codirectional: return the magnitude quotient, marked
    `exact-recovered`;
  - exact zero/zero, no supplied binding: return `ZeroZeroUnderdetermined`;
  - exact zero/zero, licensed supplied binding: retain the binding and mark the
    trial compatible but non-identifying;
  - exact one-zero or exact non-codirectional: return the corresponding no-fit
    result for the supplied exact premises;
  - any empirical pair without a licensed in-scope policy: return
    `EstimationRequired`, even if its displayed vectors align;
  - empirical pair with licensed policy: return a complete
    `JointNewtonIIFitResult`, not a bare mass estimate;
  - circular empirical provenance: preserve any consistency result but withhold
    independent-evidence standing;
  - fit missing its residual or original measurements: reject as incomplete;
  - absent independent values: terminate as insufficient information rather
    than recurse through the triplet;
  - unresolved estimator ownership: route by capability name
    `joint-mass-estimation`, not prematurely by entry number.

## IRIEs — ideal residually imparted effects

Reader/modeler behaviour to install:

  - Ask first whether the inputs are explicitly exact quantities or empirical
    measurement results.
  - Treat exact mass recovery as a checked operation, not an unconditional
    rearrangement.
  - Preserve independent force-side and acceleration-side measurement results
    before applying Newton II jointly.
  - Route every empirical mass determination to joint estimation, including an
    accidentally or approximately aligned displayed pair.
  - Distinguish the original measurements from the latent codirectional values
    selected by the joint model.
  - Require a declared estimation policy and retain uncertainty, residual,
    goodness of fit, and provenance.
  - Check whether the evidential paths are sufficiently independent before
    calling the result an empirical mass determination.
  - Distinguish exact incompatibility, empirical estimation required, poor fit,
    and circular restatement.

Anti-habit / anti-misread:

  - Do not write or calculate unrestricted `force / acceleration` for vectors.
  - Do not let `0/0` choose a mass.
  - Do not confuse displayed empirical alignment with exact supply.
  - Do not confuse a measurement with a latent value already reconciled under
    Newton II.
  - Do not confuse `no exact fit for these exact premises` with `this object has
    no mass`.
  - Do not confuse `estimation required` with `experiment unusable`.
  - Do not allow an imposed fit to confirm itself by hiding its residual.
  - Do not count a circular reconstruction as independent evidence.
  - Do not substitute weight, scale reading, gravitational mass, or amount of
    matter for inertial mass.

## Suggested wording

### A — chosen d4 candidate

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
For exact supplied vectors, first check that both are nonzero and codirectional,
then divide the net-force magnitude by the inertial-acceleration magnitude. A
zero-zero pair does not determine the scalar; any other incompatible exact pair
has no exact positive-mass fit. For empirical force and acceleration measurement
results, keep the two results separate and check their provenance. With
sufficiently independent results and a declared policy, jointly estimate two
underlying codirectional vectors and the positive scalar relating them; if no
policy is available, report that estimation is required. Retain the original
measurements, their uncertainty and discrepancy, the policy, and their
provenance. If either result already depended on the mass being sought or on the
other result through this relation, the outcome is only a consistency
restatement.
```

### B — lesson-facing compression

```text
For empirical force and acceleration measurement results, estimate two
underlying codirectional vectors and then recover the positive scalar relating
them.
```

This is the minimum honest conceptual handoff for NML2.1. It is acceptable only
where surrounding lesson content already makes the preservation of the original
measurements, uncertainty, residual, policy, and provenance explicit.

### C — d3 measured sentence, rejected

```text
For non-codirectional measured vectors, estimate two underlying codirectional
vectors and then recover the positive scalar relating them.
```

Rejected because empirical provenance, not visible alignment, selects the joint
branch. It also treats measurement results as bare vectors and omits fit standing.

### D — short refined-type form, deferred

```text
For a certified Newton-II pair, the positive scalar relating its force and
acceleration.
```

Potentially valid only after a named predecessor constructs the refined input by
an exact check or a joint fit. In the current graph it hides the machinery inside
`certified` and is not acceptable as E10.

## Draft entry

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
For exact supplied vectors, first check that both are nonzero and codirectional,
then divide the net-force magnitude by the inertial-acceleration magnitude. A
zero-zero pair does not determine the scalar; any other incompatible exact pair
has no exact positive-mass fit. For empirical force and acceleration measurement
results, keep the two results separate and check their provenance. With
sufficiently independent results and a declared policy, jointly estimate two
underlying codirectional vectors and the positive scalar relating them; if no
policy is available, report that estimation is required. Retain the original
measurements, their uncertainty and discrepancy, the policy, and their
provenance. If either result already depended on the mass being sought or on the
other result through this relation, the outcome is only a consistency
restatement.
```

This is intentionally longer than E8 and E9. It makes the branch, the joint
operation, and the standing of the result visible. It does not teach or choose
the estimator formula.

## Deep audit add-on

Role test:
  E10 remains inward-facing. It exposes the other two Newton-II quantities and
  the branch required to recover or estimate the scalar relating them. It does
  not construct the material object, certify persistence, compose force
  contributions, or teach a statistical fitting rule.

Necessary / sufficient / asymmetric relations:

  - On the exact branch, a nonzero codirectional pair under compatible
    qualifications is sufficient to determine one positive scalar.
  - Ordinary `ForceVector × AccelerationVector` typing is not sufficient.
  - Exact zero/zero is compatible but not identifying.
  - Exact one-zero and exact non-codirectional pairs admit no positive-scalar fit.
  - Empirical alignment is neither necessary nor sufficient to license exact
    recovery.
  - Separate empirical measurement results plus a declared estimation policy
    are jointly sufficient to define a joint estimation problem; the displayed
    values alone are not.
  - A complete joint result requires latent values, mass, uncertainty, residual
    or goodness of fit, policy, and provenance.
  - Sufficiently independent evidential paths are necessary for the result to
    count as independent evidence for mass.
  - Matching material-object address, frame, interval, quantity type, units, and
    epistemic status is necessary before either branch runs.

Quantifier or modality:
  `the positive scalar` states the Newton-II role. `exact supplied` and
  `empirical ... measurement results` are branch selectors. `Jointly estimate`
  declares that neither latent vector is selected independently after the
  Newton-II constraint is imposed. `Retain` makes fit standing part of the
  result rather than optional evaluator metadata.

Suspends for human/model input?
  yes; for missing values, missing epistemic classification, missing
  qualifications, unresolved measurement provenance, or an empirical request
  whose joint estimation policy is not installed in the current scope.

Boundary trigger:

  - no licensed binding and no independent input pair;
  - exact zero/zero, exact one-zero, or exact non-codirectionality;
  - any empirical measurement-result pair;
  - absent joint policy where an actual empirical estimate is demanded;
  - circular or unresolved evidential provenance;
  - joint result missing original measurements, uncertainty, residual, policy,
    or provenance;
  - address, frame, time, units, type, or provenance mismatch;
  - expired mass-reuse licence.

Boundary output:

  - exact scalar;
  - exact underdetermination;
  - exact incompatibility result;
  - estimation-required handoff;
  - complete joint fit result outside NML2.1;
  - consistency-restatement status for circular inputs;
  - incomplete-fit rejection;
  - insufficient-information, qualification, or unlicensed-input halt.

Residual provenance ledger:

| Phrase | Backing |
|---|---|
| `For one material-object` / `its` | Current E8–E10 one-owner grammar; prevents cross-target mixing without a free address mark. |
| `positive scalar` | Newton II's mass commitment; excludes antiparallel exact fits and states isotropic response. |
| `multiplies ... to give` | Stock scalar-vector arithmetic; states the inward relation without inventing vector division. |
| `exact supplied vectors` | NML2.1 content d2's required exact/measured distinction and the surviving exact analysis. |
| `nonzero and codirectional` | Exact `MassRecoveryResult` domain preserved from the type-theoretic analysis. |
| `divide the net-force magnitude by the inertial-acceleration magnitude` | Exact scalar readout after compatibility, never a general empirical estimator. |
| `zero-zero ... does not determine` | Newton II admits every positive mass for the exact zero/zero pair. |
| `no exact positive-mass fit` | Failure belongs to the supplied exact premises, not to the object's possession of mass. |
| `empirical ... measurement results` / `keep the two results separate and check their provenance` | Local d3 handoff's separation of the measurement channels from the joint fit and its evidential-independence test. |
| `jointly estimate two underlying codirectional vectors and the positive scalar` | Explicit conceptual topology of `JointNewtonIIFit`; neither latent vector is independently selected after imposing Newton II. |
| `Retain the original measurements ...` | Prevents the imposed relation from self-confirming and preserves uncertainty, residual, policy, and provenance. |

Why candidate A is chosen:
  It corrects d3's alignment-based empirical branch, triggers rather than
  assumes the independence check, preserves the distinction between measurements
  and latent fitted values, and makes fit standing visible without selecting
  estimator mathematics. Candidate B is the approved conceptual compression for
  lesson prose, not the complete packet candidate.

Checks:

  - same material-object ownership explicit: yes;
  - positive-scalar commitment explicit: yes;
  - exact branch result-valued rather than total: yes;
  - exact compatibility checked before magnitude quotient: yes;
  - exact zero/zero non-determination explicit: yes;
  - empirical provenance, not displayed alignment, selects the joint branch:
    yes;
  - measurement results distinguished from latent fitted values: yes;
  - joint result retains original measurements and residual: yes;
  - uncertainty, policy, and provenance retained: yes;
  - circular evidence distinguished from independent determination: yes;
  - no estimator formula silently selected: yes;
  - no E12 ownership assumed before ratification: yes;
  - no mass-address construction, persistence, additivity, gravitational bridge,
    or force-composition provenance imported: yes.

## Decisions made in d4

1. The branch selector is explicitly exact/supplied versus empirically measured,
   not codirectional versus non-codirectional.
2. Every empirical mass determination takes the joint estimation branch,
   including an aligned displayed measurement pair.
3. Observation, independent measurement result, and jointly estimated latent
   value are three distinct stages.
4. The force-side and acceleration-side measurement results remain independent
   inputs; neither is redefined by reference to the other merely to earn the
   word `measurement`.
5. The empirical operation is `JointNewtonIIFit`, not the d3
   `MeasuredForceVector × MeasuredAccelerationVector -> MassEstimateResult`
   signature.
6. A joint result contains the original measurements, latent force, latent
   acceleration, mass, uncertainty, corrections or residual, goodness of fit,
   policy, provenance, and independence/circularity status.
7. The residual survives because the latent outputs satisfy Newton II by
   construction; without the discrepancy the imposed law could appear to
   confirm itself.
8. Inputs derived through the demanded mass or through each other via the same
   Newton-II relation support only a consistency restatement, not independent
   mass evidence.
9. The exact branch and its result vocabulary survive from d3 unchanged.
10. NML2.1 teaches the topology of the joint operation but does not select or
    execute an estimator.
11. Estimator ownership remains capability-named until the E12-versus-separate-
    measurement-entry decision is ratified.
12. The active Design 2.1 draft is not automatically updated by this packet.

## Evaluator requirements

The evaluator needs this branch architecture:

```text
input provenance
  -> explicitly exact/supplied?
     -> MassExact -> MassRecoveryResult
  -> empirical measurement results?
     -> provenance sufficiently independent?
        -> no: ConsistencyRestatement
        -> unresolved: ProvenanceRequired
        -> yes: joint policy available?
           -> no: EstimationRequired
           -> yes: JointNewtonIIFit -> JointNewtonIIFitResult
```

Minimum exact-result vocabulary:

```text
ExactMass(m)
ZeroZeroUnderdetermined
ZeroNonzeroInconsistency
NoncodirectionalExactInconsistency
```

Minimum empirical boundary result in NML2.1:

```text
EstimationRequired(
  conceptual_route =
    "estimate two underlying codirectional vectors and then recover the
     positive scalar relating them",
  method_status = "outside present scope"
)
```

The evaluator must never silently convert

```text
MeasuredForceResult × MeasuredAccelerationResult
```

into `ExactMass`, even when their displayed vectors align. It must also reject a
joint result that returns only `m` or only the compatible latent values.

## Acceptance tests

1. **Exact compatible pair**

   ```text
   F = (6, 0) N
   a = (2, 0) m s^-2
   status = exact
   -> ExactMass(3 kg)
   ```

2. **Exact zero/zero**

   ```text
   F = 0
   a = 0
   status = exact
   -> ZeroZeroUnderdetermined
   ```

3. **Exact one-zero**

   ```text
   F = (1, 0) N
   a = 0
   status = exact
   -> ZeroNonzeroInconsistency
   ```

4. **Exact antiparallel or oblique pair**

   ```text
   F = (-6, 0) N, a = (2, 0) m s^-2, status = exact
   -> NoncodirectionalExactInconsistency

   F = (6, 0) N, a = (2, 0.1) m s^-2, status = exact
   -> NoncodirectionalExactInconsistency
   ```

5. **Oblique empirical measurement results, no policy**

   ```text
   measured F = (6, 0) N with uncertainty and provenance
   measured a = (2, 0.1) m s^-2 with uncertainty and provenance
   -> EstimationRequired
   ```

   This must not return exact inconsistency, `no mass`, or an unqualified
   magnitude ratio.

6. **Aligned empirical measurement results, no policy**

   ```text
   measured F = (6, 0) N with uncertainty and provenance
   measured a = (2, 0) m s^-2 with uncertainty and provenance
   -> EstimationRequired
   ```

   Displayed alignment must not silently route to `ExactMass(3 kg)`.

7. **Independent empirical results with a licensed policy**

   ```text
   MeasuredForceResult, MeasuredAccelerationResult, licensed EstimationPolicy
   -> JointNewtonIIFitResult(
        original measurements,
        F*, a*, m,
        uncertainty,
        residual/goodness of fit,
        policy and provenance,
        independent-evidence standing
      )
   ```

8. **Joint fit omits residual**

   ```text
   result = (F*, a*, m) only
   -> reject incomplete fit result
   ```

9. **Circular empirical provenance**

   ```text
   measured a was calculated from measured F and the demanded/supplied m
   -> ConsistencyRestatement, not independent mass determination
   ```

10. **Independent measurements remain distinct from latent outputs**

    ```text
    hold force-side observations and procedure fixed;
    change only trajectory observations
    -> MeasuredForceResult unchanged; jointly fitted F* may change
    ```

11. **Missing epistemic status**

    ```text
    F and a present; exact/measured status absent
    -> halt for classification
    ```

12. **Different owners or incompatible qualifications**

    ```text
    F[A], a[B]
    -> address mismatch halt
    ```

## Questions and decisions still open

1. **Final wording.** Candidate A is semantically complete, but its rhythm and
   length still require reader testing before promotion.
2. **Headword suffixes.** Repeating `-material-object` remains expensive, but
   opaque anaphora would lose trace-critical edges.
3. **Estimator ownership.** Decide whether E12 is the joint estimation operation,
   the mass-address wall, both, or neither before wiring a numbered edge.
4. **Result vocabulary.** Ratify the exact names for underdetermination, exact
   incompatibility, estimation required, provenance required, consistency
   restatement, incomplete fit, and insufficient information.
5. **Finiteness and quantity types.** Confirm whether `positive scalar` is
   already restricted to finite real mass values by general quantity machinery.
6. **Provenance threshold.** Specify how the evaluator decides that the two
   measurement channels are sufficiently independent and how it reports partial
   dependence.
7. **Joint-result schema.** Ratify the exact representation of corrections,
   residual, goodness of fit, uncertainty, and repeated-trial evidence.
8. **Lesson-plan successor.** NML2.1 lesson d1 remains behind content d2 and this
   packet. A successor should install the exact/empirical split and the joint
   route before E10 is taught from it.
