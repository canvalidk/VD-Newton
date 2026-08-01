# Entry Packet: E10 Inertial-Mass-Material-Object — d3

Status: successor candidate produced after the checked-mass-recovery discovery.
This packet replaces d2 as the working account of E10, but it does not promote
new wording into the active Design 2.1 entry draft. The d2 packet remains as the
reasoning record that exposed the defect.

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
  Newton II; checked inertial-mass corner of the addressed triplet

Source status:
  Drafted from one coherent VD-docs `main` snapshot at commit
  `8e09dbf9d3e521cbe76e36426ead656c04a71650` (2026-07-31), together with the
  active local E10 packet and entry-writing evidence.

Managed sources at that commit:

  1. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT_d2.md` — current NML2.1 content
     authority and lesson-side exact/measured boundary.
  2. `Newton-analysis/vector_division_mass_estimation/type_theoretic_analysis_newton_II_mass_recovery_d2.md`
     — the total/checked asymmetry and result-valued exact operation.
  3. `Newton-analysis/vector_division_mass_estimation/vector_division_inertial_mass_measurement_d1.md`
     — the fuller estimator analysis. Its catalog `current: false` flag does not
     mean d2 supersedes this content; the catalog records that exception.
  4. `Newton-analysis/vector_division_mass_estimation/why_the_mass_entry_cannot_be_short.md`
     — why the route must be triggered by E10 rather than hidden in packet or
     evaluator machinery.
  5. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md` — current lesson-plan
     draft, read as subordinate to the d2 content specification where they
     conflict.
  6. `Newton/entry passes/E10_ENTRY_WRITING_PASS_2026-07-25.md` and
     `Newton/entry packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d2.md`
     — managed reasoning history, not current semantic authority.

Active local sources:

  - `07_design_2_1/entry_writing_passes/E10_ENTRY_WRITING_PASS_2026-07-25.md`
  - `07_design_2_1/entry_packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d2.md`
  - `07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md`
  - `07_design_2_1/notes/lesson_entry_notes/ENTRY_WRITING_PASS_INTAKE_2026-07-26.md`

Selection method:
  Followed the catalog entries and informing links for `E10`,
  `vector_division_mass_estimation`, `mass recovery`, `codirectional`,
  `estimation`, and `NML2.1`, then compared them with the active local packet,
  pass, and promoted draft string.

### Governing correction

E8 and E9 are total operations on their ordinary input types:

```text
PositiveMass × AccelerationVector -> ForceVector
ForceVector × PositiveMass       -> AccelerationVector
```

E10 is not:

```text
ForceVector × AccelerationVector -> checked MassRecoveryResult
```

The ordinary vector types do not establish the value-level relation required
for a positive mass. E10 must distinguish exact compatibility from measured-data
estimation. Its shortness cannot be borrowed from E8 and E9 because their input
types discharge a precondition that E10's do not.

### Old wording lineage

```text
inertial-mass :=
The positive scalar coefficient m such that net-force = m times
inertial-acceleration for a point-particle.
```

The d2 working string was:

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
```

A managed revision added:

```text
Therefore the two point the same way, and the scalar is the net-force
magnitude divided by the inertial-acceleration magnitude.
```

The first form is true but does not trigger the determination or measured-data
route. The added sentence strengthens the trigger in the wrong direction: a
reader holding ordinary non-codirectional measurements is led toward “no mass”
instead of toward estimation of an underlying Newton-II-compatible pair.

### Preserve

  - inertial mass is a positive scalar;
  - all three quantities belong to the same material object and compatible
    frame and time/interval qualifications;
  - the inward Newton-II relation is
    `net-force-material-object = inertial-mass-material-object ×
    inertial-acceleration-material-object`;
  - an exact compatible nonzero pair determines one positive scalar;
  - a zero/zero exact trial is compatible but non-determining;
  - supplied mass bindings remain distinct from values determined by a trial;
  - mass-address origination, persistence, additivity, gravitational bridges,
    and force-composition provenance remain outside E10.

### Change / reject

  - Do not model E10 as a total function from any force vector and acceleration
    vector to a positive mass.
  - Do not divide vectors.
  - Do not make exact codirectionality a universal precondition for measured
    inputs.
  - Do not classify a non-codirectional measured pair as evidence that the
    material object has no inertial mass.
  - Do not use a fixed direction tolerance and magnitude floor as a substitute
    for a measurement model.
  - Do not silently choose `|F|/|a|`, force-on-acceleration projection,
    acceleration-on-force projection, or orthogonal-distance fitting for
    imperfect measurements. Newton II alone chooses none of them.
  - Do not hide the conceptual estimation route in the IRIL, packet notes, or a
    deferred entry. E10 must trigger the route; the later machinery may execute
    it.
  - Do not use `infer an underlying compatible pair` in lesson-facing wording.
    `Compatible pair` is too opaque to preserve the operation students need to
    remember.

Plain purpose:
  Complete the Newton-II triplet by identifying the positive scalar that relates
  one material object's addressed inertial acceleration and net force, while
  installing the checked exact route and the measured-data handoff without
  teaching a statistical estimator in NML2.1.

Relationship to the packet set:

  - one winter daughter of E8;
  - relates E9's net force to E8's inertial acceleration;
  - unlike E8 and E9, returns a checked result rather than always returning its
    demanded quantity;
  - triggers, but does not itself supply, measured-data estimation machinery;
  - deliberately does not replace the deferred outward mass-address wall.

Trace-critical headword mentions:

  - net-force-material-object
  - inertial-acceleration-material-object

Other structural qualifier:

  - one material-object owns the mass, force, and acceleration values;
  - each force/acceleration input must carry an epistemic-status tag declaring
    whether it is exact/supplied or measured;
  - measured inputs must identify a measurement model or return an estimation
    handoff rather than an exact result.

Forbidden headword mentions / hidden imports in the eventual entry wording:

  - scale / weight / gravitational mass / amount of matter / density mass;
  - mass additivity;
  - target construction / trackability / lumping;
  - interacting-forces-set / attached-force;
  - constancy or persistence across trials;
  - a particular estimator, covariance model, or fitting formula.

Question or trace moment this helps with:

  1. Exact branch: do these exact force and acceleration values admit one
     positive scalar, and if so what is it?
  2. Measured branch: what must happen before imperfect force and acceleration
     measurements can yield an inertial-mass estimate?
  3. Consumption branch: is there already a licensed supplied mass binding?

Witness kind:
  addressed material-object force-accounting commitment; exact recovery or
  measured-estimation handoff, not the deferred material-object construction or
  mass-persistence machinery.

Slots read:

  - material-object identity;
  - net-force-material-object;
  - inertial-acceleration-material-object;
  - exact-versus-measured status for each vector;
  - common frame and time/interval qualifications;
  - supplied mass binding, where one exists;
  - licence and provenance status;
  - an estimation policy / measurement model only after routing to the measured
    branch.

Slots written / exposed:

  - inertial-mass-material-object when supplied or exactly recovered;
  - `ExactMass(m)`;
  - `ZeroZeroUnderdetermined`;
  - `ZeroNonzeroInconsistency`;
  - `NoncodirectionalExactInconsistency`;
  - `EstimationRequired` for measured data when NML2.1 reaches its boundary;
  - `MassEstimateResult` only when separately licensed estimation machinery is
    available;
  - supplied / exact-recovered / estimated provenance.

## Exact and measured operations

Exact recovery is result-valued:

```text
MassExact:
  ForceVector × AccelerationVector
  -> MassRecoveryResult
```

with the input pair explicitly declared exact. Its outcomes are:

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

Measured-data estimation is a different operation:

```text
MassEstimate:
  MeasuredForceVector
  × MeasuredAccelerationVector
  × EstimationPolicy
  -> MassEstimateResult
```

Newton II supplies the constraint on the underlying vectors. The estimation
policy supplies the rule for selecting underlying values from imperfect
measurements. The measured vectors alone do not select that rule.

## Lesson boundary

NML2.1 must transfer the conceptual route without teaching the estimator's
mathematical formula.

Students should retain:

```text
estimate two underlying codirectional vectors and then recover the positive
scalar relating them
```

This wording replaces `infer an underlying compatible pair`. It makes the
unavailable estimator's job explicit without specifying how the fit is
performed.

NML2.1 may teach:

  - that exact and measured inputs take different branches;
  - the exact nonzero codirectionality check;
  - the exact magnitude quotient after that check;
  - the zero/zero non-determination result;
  - the difference between no exact positive-mass fit and estimation required;
  - that an estimator would estimate two underlying codirectional vectors and
    then recover the positive scalar relating them;
  - the course-level output `estimation required — method outside the present
    scope`.

NML2.1 must not teach or silently select:

  - a magnitude-ratio estimator for misaligned measured data;
  - either projection estimator;
  - componentwise averaging;
  - least squares, errors-in-variables, Deming regression, orthogonal-distance
    regression, covariance weighting, or likelihood construction;
  - how an estimation policy is chosen or certified;
  - how force or acceleration measurement errors were experimentally obtained.

The boundary is therefore:

```text
NML2.1 owns recognition and conceptual routing.
Later measurement/estimation machinery owns policy selection and execution.
```

Whether that later machinery is E12 or a separately named measurement entry is
still an open architecture decision. E10 must not hard-code the destination
before that ownership is ratified.

## Boundary behavior

  - Licensed supplied binding: return it, preserving its provenance and licence.
  - Exact, nonzero, codirectional pair: return `ExactMass(m)`.
  - Exact zero/zero pair: return `ZeroZeroUnderdetermined`; do not overwrite a
    licensed supplied binding.
  - Exact pair with exactly one zero: return `ZeroNonzeroInconsistency`.
  - Exact nonzero pair with no positive-scalar fit: return
    `NoncodirectionalExactInconsistency`.
  - Non-codirectional measured pair without in-scope estimation machinery:
    return `EstimationRequired`, not an inconsistency and never “no mass”.
  - Measured pair with a declared, licensed estimation policy: route to
    `MassEstimate`; preserve the model and input provenance in the result.
  - Missing exact/measured status: halt for classification. Do not guess.
  - Missing value: demand it if the graph has an independent route; otherwise
    return insufficient information.
  - Expired binding: do not reuse it automatically; a fresh independent exact
    recovery or licensed estimation may still produce a new value.
  - Address, frame, time, type, or dimensional mismatch: halt before either
    exact recovery or estimation.

## IRIL — ideal residually imparted logic

Allowed:

  - On a demand for `inertial-mass-material-object` for one material object,
    first return a licensed supplied binding if present.
  - Otherwise demand that object's net force and inertial acceleration together
    with their exact/measured status and common qualifications.
  - If the pair is declared exact, run `MassExact`:
    1. check zero/nonzero status;
    2. for a nonzero pair, check codirectionality;
    3. only after compatibility passes, divide net-force magnitude by
       inertial-acceleration magnitude;
    4. return the appropriate result-valued outcome rather than forcing every
       branch into a mass value.
  - If the pair is measured and non-codirectional, trigger the conceptual route:
    estimate two underlying codirectional vectors and then recover the positive
    scalar relating them.
  - Within NML2.1, stop that measured branch at `EstimationRequired` and identify
    the method as outside the present scope.
  - Outside that lesson boundary, invoke `MassEstimate` only with a declared,
    licensed estimation policy / measurement model.
  - Preserve the common material-object, inertial-frame, time/interval, units,
    uncertainty, and provenance qualifications.
  - Record whether the returned value was supplied, exactly recovered, or
    estimated, and which independent route supplied the acceleration.
  - When a licensed mass binding and the other two corners are all present, use
    the relation as a consistency check; do not silently replace the binding.

Blocked:

  - Dividing one vector by another.
  - Dividing magnitudes before checking compatibility on the exact branch.
  - Applying the exact branch to inputs merely because their measured values are
    numerically available.
  - Treating measured misalignment as `NoncodirectionalExactInconsistency`.
  - Returning “no mass” from measured misalignment.
  - Applying an undeclared direction tolerance or magnitude floor.
  - Treating a direction tolerance plus magnitude floor as an estimation model.
  - Defaulting to magnitude ratio, either projection formula, componentwise
    division, or unweighted least squares for imperfect measurements.
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
  - exact zero/zero, no supplied binding: return
    `ZeroZeroUnderdetermined`;
  - exact zero/zero, licensed supplied binding: retain the binding and mark the
    trial compatible but non-confirming;
  - exact one-zero or exact non-codirectional: return the corresponding no-fit
    result for the supplied exact premises;
  - measured non-codirectional: return `EstimationRequired` in NML2.1 and the
    explicit conceptual route, not a terminal no-mass conclusion;
  - measured with licensed policy outside NML2.1: return `MassEstimateResult`
    with uncertainty and policy provenance;
  - absent independent values: terminate as insufficient information rather
    than recurse through the triplet;
  - unresolved estimator ownership: route by capability name
    `mass-estimation`, not prematurely by entry number.

## IRIEs — ideal residually imparted effects

Reader/modeler behaviour to install:

  - Ask first whether the vectors are exact inputs or measurements.
  - Treat exact mass recovery as a checked operation, not a rearrangement that
    always returns a scalar.
  - Check codirectionality before using magnitudes on the exact branch.
  - Distinguish zero/zero underdetermination from an incompatible exact pair.
  - Read measured misalignment as a prompt to estimate underlying vectors, not
    as proof of absent mass.
  - Retain the conceptual measured-data procedure even when its mathematics is
    deferred: estimate two underlying codirectional vectors and then recover the
    positive scalar relating them.
  - Demand a declared estimation policy before producing a measured-data mass
    estimate.
  - Preserve owner, frame, time, units, uncertainty, and provenance.

Anti-habit / anti-misread:

  - Do not write or calculate unrestricted `force / acceleration` for vectors.
  - Do not let `0/0` choose a mass.
  - Do not confuse “no exact fit for these exact premises” with “this material
    object has no mass”.
  - Do not confuse “estimation required” with “experiment unusable”.
  - Do not treat exact codirectionality as an event expected from raw measured
    vectors.
  - Do not hide the estimator choice behind a tolerance.
  - Do not substitute weight, a scale reading, gravitational mass, or amount of
    matter for inertial mass.
  - Do not reuse a mass value across a material change without a current licence.

## Suggested wording

### A — chosen d3 candidate

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
For exact supplied vectors, first check that both are nonzero and codirectional,
then divide the net-force magnitude by the inertial-acceleration magnitude. A
zero-zero pair does not determine the scalar; any other incompatible exact pair
has no exact positive-mass fit. For non-codirectional measured vectors, estimate
two underlying codirectional vectors and then recover the positive scalar
relating them.
```

### B — shorter, rejected

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
For compatible inputs, recover the scalar; otherwise use an estimator.
```

Rejected because `compatible` and `estimator` are opaque exactly where the
entry must preserve the route. It recreates the defect in fewer words.

### C — exact-only, rejected as the general E10 entry

```text
inertial-mass-material-object :=

For one material-object with exact nonzero codirectional net force and inertial
acceleration, the net-force magnitude divided by the inertial-acceleration
magnitude.
```

Rejected because it defines only the exact determination procedure, fails on a
massive object in a zero/zero trial, and says nothing about ordinary measured
inputs. It may serve as an exact-branch gloss, not as E10.

### D — asserted direction, rejected

```text
Therefore the two point the same way, and the scalar is the net-force magnitude
divided by the inertial-acceleration magnitude.
```

Rejected because a measured mismatch evokes “no mass” or “law failure” rather
than the required estimation handoff.

## Draft entry

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
For exact supplied vectors, first check that both are nonzero and codirectional,
then divide the net-force magnitude by the inertial-acceleration magnitude. A
zero-zero pair does not determine the scalar; any other incompatible exact pair
has no exact positive-mass fit. For non-codirectional measured vectors, estimate
two underlying codirectional vectors and then recover the positive scalar
relating them.
```

This is intentionally longer than E8 and E9. The extra text is not scaffolding
around a short definition: it is the checked and measured branch structure that
the mass corner alone must carry.

## Deep audit add-on

Role test:
  E10 remains inward-facing. It exposes the two other Newton-II triplet
  quantities, but unlike its siblings it must also expose how exact and measured
  inputs branch. It does not construct the material object, certify persistence,
  or teach the measurement model.

Necessary / sufficient / asymmetric relations:

  - On the exact branch, a nonzero codirectional pair under compatible
    qualifications is sufficient to determine one positive scalar.
  - Ordinary `ForceVector × AccelerationVector` typing is not sufficient.
  - Exact zero/zero is compatible but not identifying.
  - Exact one-zero and exact non-codirectional pairs admit no positive-scalar fit.
  - Measured non-codirectionality is not an exact incompatibility result because
    the measured values are not asserted to be the underlying law quantities.
  - On the measured branch, the measurements plus an estimation policy are
    jointly sufficient to define an estimation problem; the measurements alone
    are not.
  - Matching material-object address, frame, interval, quantity type, units, and
    epistemic status is necessary before either branch runs.

Quantifier or modality:
  `the positive scalar` states the Newton-II role. `exact supplied` and
  `measured` are branch selectors, not adjectives of convenience. `Estimate`
  marks a non-exact operation requiring an additional policy.

Suspends for human/model input?
  yes; for missing values, missing exact/measured classification, missing
  qualifications, or a measured-data request whose estimation policy is not
  installed in the current scope.

Boundary trigger:

  - no licensed binding and no independent pair;
  - exact zero/zero;
  - exact one-zero;
  - exact non-codirectionality;
  - measured non-codirectionality;
  - absent measurement model where an actual estimate is demanded;
  - address, frame, time, units, type, or provenance mismatch;
  - expired mass-reuse licence.

Boundary output:

  - exact scalar;
  - exact underdetermination;
  - exact incompatibility result;
  - estimation-required handoff;
  - estimated result with policy provenance, outside NML2.1;
  - insufficient-information or qualification halt;
  - unlicensed-input halt.

Residual provenance ledger:

| Phrase | Backing |
|---|---|
| `For one material-object` / `its` | Current E8-E10 one-owner grammar; prevents cross-target mixing without a skimmable free address mark. |
| `positive scalar` | Newton II's mass commitment; excludes antiparallel exact fits and states isotropic response. |
| `multiplies ... to give` | Stock scalar-vector arithmetic; states the inward relation without inventing vector division. |
| `exact supplied vectors` | NML2.1 content d2's required exact/measured distinction. |
| `nonzero and codirectional` | Exact `MassRecoveryResult` domain from the type-theoretic analysis. |
| `divide the net-force magnitude by the inertial-acceleration magnitude` | Exact scalar readout after compatibility, not a general measured-data estimator. |
| `zero-zero ... does not determine` | Newton II admits every positive mass for the exact zero/zero pair. |
| `no exact positive-mass fit` | Preserves failure as a statement about the exact supplied pair, not about the object's possession of mass. |
| `estimate two underlying codirectional vectors and then recover the positive scalar relating them` | Explicit conceptual description of the deferred estimator's job; replaces the opaque `infer an underlying compatible pair`. |

Why candidate A is chosen:
  It is the only candidate here that causes a reader holding either exact or
  measured inputs to take the correct next step. It retains the defining relation,
  gives the exact procedure and zero boundary, avoids the catastrophic measured
  “no mass” fork, and transfers the estimator's conceptual role without crossing
  NML2.1's mathematical boundary.

Checks:

  - same material-object ownership explicit: yes;
  - positive-scalar commitment explicit: yes;
  - exact branch result-valued rather than total: yes;
  - exact scalar operation ordered and explicit: yes;
  - zero/zero non-determination explicit: yes;
  - exact incompatibility distinguished from absent mass: yes;
  - measured misalignment routes to estimation: yes;
  - estimator conceptual action stated without formula: yes;
  - no estimator silently selected: yes;
  - no direction tolerance or magnitude floor treated as a measurement model:
    yes;
  - no E12 ownership assumed before ratification: yes;
  - no mass-address construction, persistence, additivity, gravitational bridge,
    or force-composition provenance imported: yes.

## Decisions made in d3

1. E10 is a checked corner, not a total `ForceVector × AccelerationVector ->
   PositiveMass` operation.
2. Exact and measured inputs are different trace branches, and the evaluator must
   receive that distinction explicitly.
3. The exact nonzero branch checks codirectionality before taking the magnitude
   quotient.
4. Exact zero/zero returns underdetermination; exact one-zero and exact
   non-codirectionality return no exact positive-mass fit for those premises.
5. Measured non-codirectionality returns an estimation handoff, never a terminal
   no-mass result.
6. The entry itself carries the conceptual handoff. It is not hidden in the IRIL,
   packet notes, or a deferred entry.
7. Lesson-facing wording says `estimate two underlying codirectional vectors and
   then recover the positive scalar relating them`, not `infer an underlying
   compatible pair`.
8. NML2.1 names the estimator's conceptual task but does not give a formula,
   select a policy, or perform the fit.
9. A direction tolerance and magnitude floor are removed as E10 primitives.
   Actual measured-data estimation requires a measurement model.
10. The estimator destination is capability-named until the E12-versus-later-
    measurement architecture is ratified.
11. The active Design 2.1 draft is not automatically updated by this packet; the
    candidate wording requires review before promotion.

## Evaluator requirements

The evaluator must not implement E10 as one unconditional scalar computation.
It needs:

```text
input provenance
  -> exact or measured?
     -> exact: MassExact -> MassRecoveryResult
     -> measured: estimation policy available?
        -> no: EstimationRequired
        -> yes: MassEstimate -> MassEstimateResult
```

Minimum exact-result vocabulary:

```text
ExactMass(m)
ZeroZeroUnderdetermined
ZeroNonzeroInconsistency
NoncodirectionalExactInconsistency
```

Minimum measured-result vocabulary in NML2.1:

```text
EstimationRequired(
  conceptual_route =
    "estimate two underlying codirectional vectors and then recover the
     positive scalar relating them",
  method_status = "outside present scope"
)
```

The evaluator must preserve enough provenance to distinguish:

  - a supplied mass;
  - a mass recovered from independently supplied exact force and acceleration;
  - a circular restatement where acceleration was itself computed from the same
    force and mass;
  - a mass estimated from measurements under a declared policy.

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

4. **Exact antiparallel pair**

   ```text
   F = (-6, 0) N
   a = (2, 0) m s^-2
   status = exact
   -> NoncodirectionalExactInconsistency
   ```

5. **Exact oblique pair**

   ```text
   F = (6, 0) N
   a = (2, 0.1) m s^-2
   status = exact
   -> NoncodirectionalExactInconsistency
   ```

6. **The same oblique numbers declared measured**

   ```text
   measured F = (6, 0) N
   measured a = (2, 0.1) m s^-2
   no in-scope estimation policy
   -> EstimationRequired
   ```

   This must not return `NoncodirectionalExactInconsistency`, `no mass`, or the
   unqualified magnitude ratio.

7. **Measured pair with policy**

   ```text
   measured F, measured a, licensed EstimationPolicy
   -> MassEstimateResult(value, uncertainty, policy provenance)
   ```

8. **Missing epistemic status**

   ```text
   F and a present; exact/measured status absent
   -> halt for classification
   ```

9. **Different owners**

   ```text
   F[A], a[B]
   -> address mismatch halt
   ```

10. **Circular provenance**

    ```text
    a was calculated from F and supplied m; E10 is then asked to infer m from F,a
    -> preserve as consistency/restatement, not independent mass evidence
    ```

## Questions and decisions still open

1. **Final wording.** Candidate A is semantically complete, but its length and
   rhythm need reader testing before promotion.
2. **Headword suffixes.** Repeating `-material-object` in a multi-sentence entry
   remains expensive, but replacing headword edges with `the former` or opaque
   anaphora would be a structural regression. This packet does not decide the
   suffix question.
3. **Estimator ownership.** The latest entry analysis says E10 should trigger a
   handoff and E12 should carry estimation machinery; NML2.1 content d2 names a
   later measurement/estimation treatment and separately assigns the mass-address
   question to NML2.2. Decide whether E12 is that measurement operation, the
   mass-address wall, both, or neither before wiring a numbered edge.
4. **Result vocabulary.** Confirm the exact names for underdetermination,
   exact incompatibility, estimation required, and insufficient information.
5. **Finiteness and quantity types.** Confirm whether `positive scalar` is
   already restricted to finite real mass values by general quantity machinery.
6. **Provenance depth.** Ratify how the evaluator marks independent empirical
   recovery versus circular restatement.
7. **Measured codirectional inputs.** Decide whether the lesson treats an exactly
   aligned displayed measurement as the licensed simple case or still routes by
   its measured status. The general engine should retain the measurement model;
   classroom examples may deliberately supply exact vectors instead.
8. **Lesson-plan successor.** NML2.1 lesson d1 remains behind content d2 in its
   treatment of nonparallel inputs. A lesson d2 should install the exact/measured
   split and the explicit conceptual estimator wording before E10 is taught from
   the current plan.
