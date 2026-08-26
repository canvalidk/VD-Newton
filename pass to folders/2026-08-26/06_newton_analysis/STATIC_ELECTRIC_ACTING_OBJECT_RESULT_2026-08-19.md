# Static Electric Action Without Electric Source Charge

## The new acting-object result for Newtonian EM statics

**Date:** 2026-08-19  
**Status:** Newton analysis note; candidate foundations result, not yet a Newton entry  
**Scope:** Acting-object identity, Galilean covariance, EM statics, and the limits of reduction to Coulomb, Ampere, and Biot-Savart

---

## Abstract

Consider an opaque tube containing a steady conveyor of closely spaced permanent magnets. In the continuum idealisation, the internal magnetic-moment distribution is stationary in tube coordinates even though its constituents move. Relativistic electromagnetism predicts that such a steady magnetic-moment flow can produce a stationary electric field outside the tube. A charged test particle at rest relative to the tube therefore experiences a static, charge-linear force.

This physical effect is not new. The acting-object consequence for a strictly Galilean Newtonian theory is the result of interest.

If the Newtonian theory requires acting-object identity, impressed-force-set membership, and acting-object kind to remain stable under Galilean changes of frame, the tube's electric action cannot be reduced to Coulomb, Ampere, or Biot-Savart. There is no warranted electric source charge for Coulomb; Ampere and Biot-Savart are magnetostatic laws and do not return this velocity-independent electric force on a stationary charge. A mathematically equivalent fictitious charge distribution does not supply the missing source warrant.

The Newtonian theory must therefore admit an additional primitive acting-object kind: a stationary electric action carried by a device or magnetic-moment-flow construct without electric source charge. It belongs to **EM statics** because its macroscopic source construct and force profile are stationary, instantaneous, and non-radiative. It is not an electrostatic-*charge* law.

The physical phenomenon and its relativistic derivation are established. What may be new is the acting-object no-reduction result and the resulting incompleteness claim for Newtonian electromagnetostatics. External novelty has not yet been established by an exhaustive literature review.

---

## 1. The result in one sentence

> A stationary electric force on charge does not entail an electric-charge source; consequently, a Galilean Newtonian EM statics containing only Coulomb, Ampere, and Biot-Savart acting objects is not acting-object complete.

The crack is the attempt to treat

\[
\text{electric source charge}
\Longrightarrow
\text{Coulomb electric action}
\]

as licensing its converse

\[
\text{observed static electric action}
\Longrightarrow
\text{electric source charge}.
\]

The first implication is licensed by Coulomb's law. The converse does not follow from it.

---

## 2. The opaque-tube case

Take a tube with the following properties:

- The enclosure is optically opaque but does not electrostatically shield the exterior.
- Inside it is a conveyor carrying very small, regularly spaced permanent magnets.
- The conveyor is in a steady operating state.
- The magnet spacing is treated in the continuum limit, or the resulting microscopic ripple is intentionally coarse-grained.
- At the Newtonian source-warrant grain, there are permanent magnets inside the tube but no electric charges acting as electrostatic sources.

The tube produces a reproducible exterior force on charged probes. The selected force component:

- reverses under \(q\mapsto -q\);
- scales linearly with \(|q|\) in the test-charge limit;
- is independent of probe mass;
- is independent of probe velocity;
- follows the position and orientation of the tube;
- is stationary in tube coordinates while the operating state is steady.

Those observations warrant a tube-associated static-electric impressed-force occurrence. They do not warrant a hidden electric source charge.

The tube may also produce a magnetostatic force on appropriate targets. That would warrant a separate acting-object occurrence. A single carrier may own more than one acting-object mechanism; the device must not be treated as one undifferentiated force merely because its interior is hidden.

---

## 3. What the new acting object is

At the first justified modelling grain, let \(A_T^{\mathrm{SE}}\) denote a provisional `tube-static-electric` acting-object instance.

Its structure is:

- **Carrier or representative:** the tube in a stable operating state.
- **Target slot:** a charged material object in the test-charge domain.
- **Source-side construct:** initially, the tube's body-fixed static electric response profile.
- **Operating construct:** a stable relational state of the device, without an assumption about its hidden mechanism.
- **Output:** an impressed-force occurrence \(f_{T,p}^{\mathrm{SE}}\) on target \(p\).

The field profile is not the impressed-force occurrence. The distinctions are:

\[
A_T^{\mathrm{SE}}
\quad\text{warrants}\quad
f_{T,p}^{\mathrm{SE}},
\]

\[
V_C\!\left(f_{T,p}^{\mathrm{SE}}\right)
\quad\text{is the occurrence's vector value},
\]

and

\[
\boldsymbol{\mathcal E}_{T,\chi}
\quad\text{is a tube-owned construct used by the value evaluator}.
\]

The construct is definitionally locked to the acting object's force behaviour. It is not a free-standing scenario object.

---

## 4. Warranting and recovering the impressed-force value

The tube member must be warranted before its value is recovered. An unexplained residual is not a membership rule.

Let the independently closed external impressed-force set for probe \(p\) in context \(C_i\) be

\[
\operatorname{IFS}(p\mid C_i)
=
K_i\cup\left\{f_{T,p,i}^{\mathrm{SE}}\right\},
\]

where the values of all members of \(K_i\) are independently known. Newton II and inverse Force Sum then give

\[
\boxed{
V_{C_i}\!\left(f_{T,p,i}^{\mathrm{SE}}\right)
=
m_p\mathbf a_p
-
\sum_{g\in K_i}V_{C_i}(g)
}.
\]

One context recovers one value. Repetition over probe charge, position, velocity, tube pose, time, and operating state discovers the evaluator.

Let:

- \(\mathbf X_T\) be the tube position;
- \(R_T\in SO(3)\) map tube-body coordinates into scenario coordinates;
- \(\boldsymbol\xi=R_T^{\mathsf T}(\mathbf x_p-\mathbf X_T)\) be the probe position in tube coordinates;
- \(\chi_T\) identify the tube's steady operating state.

The empirically earned target-side evaluator is

\[
\boxed{
V_C\!\left(f_{T,p}^{\mathrm{SE}}\right)
=
q_pR_T\,
\boldsymbol{\mathcal E}_{T,\chi_T}
\!\left(\boldsymbol\xi\right)
}.
\]

If closed-loop work measurements establish conservativity in the accessible exterior, the construct may equivalently be represented by a body-fixed potential:

\[
\boldsymbol{\mathcal E}_{T,\chi_T}
=
-\nabla_{\boldsymbol\xi}\Phi_{T,\chi_T},
\]

and hence

\[
\boxed{
V_C\!\left(f_{T,p}^{\mathrm{SE}}\right)
=
-q_pR_T\nabla_{\boldsymbol\xi}
\Phi_{T,\chi_T}(\boldsymbol\xi)
}.
\]

This equation says how a charged target responds. It does not identify the source as electric charge.

Because the tube is one constitutive carrier, the target-side value is the full returned force. No participant-symmetric half weighting is introduced merely because a reaction may also occur on the tube.

---

## 5. Why the law is Galilean covariant

Under a Galilean transformation,

\[
\mathbf x'_p=Q\mathbf x_p+\mathbf u t+\mathbf a,
\]

\[
\mathbf X'_T=Q\mathbf X_T+\mathbf u t+\mathbf a,
\]

\[
R'_T=QR_T.
\]

The tube-relative body coordinate is therefore unchanged:

\[
\boldsymbol\xi'
=
R_T'^{\mathsf T}(\mathbf x'_p-\mathbf X'_T)
=
\boldsymbol\xi.
\]

The occurrence value transforms as a spatial vector:

\[
V'\!\left(f_{T,p}^{\mathrm{SE}}\right)
=
Q\,V\!\left(f_{T,p}^{\mathrm{SE}}\right).
\]

For a pure boost, the vector value is unchanged. More importantly:

- the same acting object remains active;
- the same impressed-force occurrence remains in the target's IFS;
- the occurrence remains of static-electric kind;
- the same body-fixed construct is evaluated;
- no absolute coordinate velocity enters the rule.

Any internal transport descriptor must likewise use velocity relative to the tube, not coordinate velocity. If \(\mathbf u_{\mathrm{rel}}=\mathbf v_{\mathrm{belt}}-\mathbf v_{\mathrm{tube}}\), then a pure Galilean boost changes both coordinate velocities equally and leaves \(\mathbf u_{\mathrm{rel}}\) unchanged.

"Static" means stationary in tube-body coordinates. If the whole tube passes through another coordinate system, the profile is advected with the tube. That does not change its acting-object identity or kind.

---

## 6. Why it belongs to EM statics

The relevant meaning of **statics** is macroscopic stationarity, not the absence of microscopic motion.

Magnetostatics already makes this distinction. A steady electric current contains moving charge carriers, yet its current distribution and magnetic force law are stationary. It belongs to magnetostatics because the source construct is time-independent at the law's modelling grain.

The magnetic conveyor has the same temporal form:

- individual magnets move;
- the continuum magnetic-moment-flow distribution is stationary in tube coordinates;
- the exterior electric force profile is time-independent there;
- the evaluator requires no retarded history;
- no radiation term or propagating field degree of freedom is needed by the Newtonian law;
- the force on a stationary electric charge is persistent and reproducible.

The result is therefore part of **EM statics** even though it is not reducible to electrostatic charge. EM statics is the umbrella containing stationary electric and magnetic acting-object laws. It must not be defined circularly as "Coulomb plus magnetostatics," because the tube case is stationary while lying outside that list.

The preferred name is therefore `static-electric acting object` or, once the deeper construct is warranted, `magnetic-moment-flow static-electric acting object`. Calling it an `electrostatic-charge acting object` would assert a source ontology that the case denies.

---

## 7. Why it cannot be reduced to Coulomb

Coulomb reduction requires more than reproducing the same vector field. It requires a warranted Coulomb acting object with electric source charge filling its source slot.

The tube has no such source at the chosen Newtonian grain. Therefore the implication

\[
V(f)=q\mathbf E
\quad\Longrightarrow\quad
\text{electric source charge}
\]

is invalid.

A fictitious interior charge distribution may reproduce the same exterior potential. This is mathematical or extensional equivalence only. It does not establish:

- the identity of the impressed-force occurrence;
- the identity of the source mechanism;
- the acting-object kind;
- the source-slot witness required by Coulomb;
- a lawful reduction of the tube acting object.

In VD terms, equality of \(V_C(f_1)\) and \(V_C(f_2)\) does not imply \(f_1=f_2\), much less that their source acting objects are identical. Occurrence identity, source identity, and value are distinct.

An effective charge distribution may be retained as a calculation device only if it is explicitly marked as non-ontological. It must not enter the IFS or acting-object source slots as though it had been independently witnessed.

---

## 8. Why it cannot be reduced to Ampere or Biot-Savart

Biot-Savart maps a steady electric-current source construct to a magnetic profile. Ampere-type laws use magnetic profiles or current constructs to return magnetic forces on appropriate targets. Neither returns the observed velocity-independent electric force on a stationary electric charge.

The source and target signatures differ:

\[
\text{Biot-Savart:}
\quad
\mathcal J_e
\longmapsto
\mathbf B,
\]

\[
\text{tube static-electric action:}
\quad
\chi_T\ \text{or}\ \mathsf K_m
\longmapsto
\boldsymbol{\mathcal E}_T
\longmapsto
q\boldsymbol{\mathcal E}_T.
\]

The second mapping is not obtained by relabelling the first. In particular, applying the electromagnetic Lorentz force to convert a magnetic profile into an electric force would reintroduce target velocity and the unified EM field structure that the Newtonian theory does not possess.

Thus Ampere and Biot-Savart may coexist with the new acting object, but they do not reduce it.

---

## 9. Current and magnetic-moment flow as constructs

The acting-object architecture suggests a clean Newtonian typing of current.

For an ordinary magnetostatic acting object, the spatially directed current arrangement is a construct:

\[
\mathcal I_e
=
(\text{path},\text{orientation},\text{spatial profile}).
\]

The scalar current strength \(I\) may be an atomic parameter. The complete current construct is attached to its carrier and transforms with that carrier's pose. It is not definitionally identical to electric charge possessing coordinate velocity.

A magnetic-moment flow requires more structure because it has both a transport direction and a moment orientation. A candidate distributed construct is

\[
\mathsf K_{m,ij}(\boldsymbol\xi)
=
n(\boldsymbol\xi)
u_{\mathrm{rel},i}(\boldsymbol\xi)
m_j(\boldsymbol\xi).
\]

This rank-two construct is Galilean safe because \(\mathbf u_{\mathrm{rel}}\) is relational. It is not an electric charge distribution and is not an ordinary electric current.

The opaque-tube experiment alone does not warrant \(\mathsf K_m\), because many hidden interiors can produce the same exterior profile. It initially warrants only \(\boldsymbol{\mathcal E}_{T,\chi}\) or \(\Phi_{T,\chi}\). The deeper construct becomes warranted only through inspection or interventions such as reversing belt direction, reversing magnet orientation, and varying moment density or conveyor speed.

Once warranted, the universal candidate law has the form

\[
\boxed{
\boldsymbol{\mathcal E}
=
\mathscr L_{\mathrm{MSE}}
[\mathsf K_m,\text{geometry},\text{parameters}]
}
\]

followed by

\[
\boxed{
V(f)=q\boldsymbol{\mathcal E}.
}
\]

Here `MSE` abbreviates magnetic-moment-flow static-electric. The exact universal kernel remains to be established. The black-box tube profile is an acting-object instance law; it is not by itself a completed universal law.

---

## 10. The acting-object incompleteness proposition

The candidate foundations result can be stated as follows.

### Proposition

Suppose a Newtonian EM statics satisfies all of the following:

1. Acting-object identity, activation, impressed-force-set membership, and acting-object kind are equivariant under the Galilean group.
2. A Coulomb acting object requires independently warranted electric source charge.
3. Ampere and Biot-Savart retain their magnetostatic source and target signatures.
4. The theory contains a stationary magnetic-moment-flow device with no electric source charge at the theory's source-warrant grain.
5. Charged stationary probes experience a nonzero, charge-linear, tube-fixed static force from that device.

Then Coulomb, Ampere, and Biot-Savart are not acting-object complete for that Newtonian EM statics.

### Proof sketch

The observed target force independently warrants an impressed-force occurrence. It cannot be a Coulomb occurrence because the required electric source witness is absent. It cannot be an Ampere or Biot-Savart occurrence because their output and target signatures do not include the observed velocity-independent electric force on stationary charge. Reclassifying magnetic-moment flow as electric charge would change or invent the source kind rather than preserve it. A fictitious charge fit preserves values but not occurrence or source identity. Therefore the occurrence is not reducible to the admitted kinds, and an additional primitive acting-object kind is required. Its body-fixed evaluator is Galilean covariant by the calculation in section 5. QED.

This is an incompleteness result for a specified Newtonian law set, not a claim that Newtonian mechanics is the final theory.

---

## 11. Relation to full electromagnetism

Relativistic electromagnetism already predicts the physical effect. In the low-speed SI description, a magnetic dipole \(\mathbf m\) moving with velocity \(\mathbf u\) is assigned an electric dipole moment of the form

\[
\mathbf p
=
\frac{\mathbf u\times\mathbf m}{c^2}.
\]

A stationary continuum of moving magnetic moments therefore yields a stationary induced electric-polarisation pattern and can produce a stationary electric field. A pure steady spin current without charge current was explicitly analysed by Sun, Guo, and Wang, who derived electric-field formulas playing roles analogous to Biot-Savart and Ampere laws.

That EM explanation must not be mistaken for a Newtonian reduction. Full EM is permitted to combine electric and magnetic components through Lorentz covariance and to represent the result using induced polarisation charge. The stipulated Newtonian theory does not have that unified field ontology, and its acting-object kinds are required to survive Galilean changes of frame.

The physical prediction can therefore be a theorem of full EM while functioning as a new primitive law in the weaker Newtonian theory. Primitiveness and reducibility are theory-relative.

---

## 12. What is and is not new

### Not new

- The relativistic transformation relation between moving electric and magnetic dipoles.
- The prediction that a steady magnetic-moment or spin current can produce an electric field.
- The existence of Galilean electric and magnetic limits of Maxwell theory.
- The target response \(V(f)=q\mathbf E\).
- The mathematical representation of a conservative exterior field by a potential or fictitious source distribution.

### Potentially new within the VD

- The separation of target-response type from source acting-object identity.
- The use of frame-stable IFS membership and acting-object kind as a no-reclassification constraint.
- The proof that exterior force-profile equivalence does not license source reduction.
- The resulting incompleteness proposition for a Newtonian EM statics containing only Coulomb, Ampere, and Biot-Savart acting objects.
- The minimal completion by a magnetic-moment-flow static-electric acting-object kind.
- The typing of ordinary current and magnetic-moment flow as carrier-attached constructs rather than coordinate motion.

### Novelty status

This note does **not** establish external publication novelty. Existing work on Galilean electromagnetism is extensive, and the physical effect is explicitly known. A publishable claim would need to be framed as an acting-object, source-warrant, and reduction result rather than as the discovery of a new electromagnetic phenomenon.

The exact combination of:

- identity-bearing acting objects;
- independently warranted IFS membership;
- source-slot witness requirements;
- Galilean kind stability;
- extensional-versus-ontological non-reduction;

was not found in the scoped literature check used for this note. That is evidence for further investigation, not proof of originality.

The most plausible publication form is a focused foundations or philosophy-of-physics paper. A mainstream physics claim would likely require a new universal kernel, experimental prediction, or empirically discriminating consequence.

---

## 13. Open work before entry or publication status

1. **Universal kernel:** derive or empirically specify \(\mathscr L_{\mathrm{MSE}}\) rather than leaving each device with an arbitrary measured profile.
2. **Reciprocity:** state the corresponding tube-side force occurrence and its relation to Newton's third law for the combined closed system.
3. **Exact static domain:** separate the continuum idealisation, discrete periodic ripple, and time-averaged approximation.
4. **Shielding and boundary conditions:** specify which enclosures allow the exterior static-electric profile.
5. **Reduction definition:** formalise the difference between value-equivalence, evaluator factorisation, source reduction, and acting-object identity.
6. **Galilean-EM comparison:** compare the result directly with the electric and magnetic limits of Le Bellac and Levy-Leblond rather than treating all Galilean electromagnetism as one theory.
7. **Literature review:** search specifically for source-ontology and no-reduction treatments of steady magnetic-moment-current electric fields.
8. **Entry placement:** decide whether the universal object belongs in an EM-statics law house or remains a Newton-boundary analysis object.

---

## 14. Sources

### Physics and Galilean electromagnetism

- Qing-feng Sun, Hong Guo, and Jian Wang, **“Spin-current induced electric field,”** *Physical Review B* 69, 054409 (2004), preprint submitted 2003. The paper explicitly predicts an electric field from a pure steady spin current without charge current and derives source formulas analogous to Biot-Savart and Ampere laws.  
  <https://arxiv.org/abs/cond-mat/0301402>  
  <https://doi.org/10.1103/PhysRevB.69.054409>

- V. Hnizdo, **“Magnetic dipole moment of a moving electric dipole,”** *American Journal of Physics* 80, 645–647 (2012). A compact discussion of moving-dipole moments and the relativistic transformation of polarisation and magnetisation.  
  <https://arxiv.org/abs/1201.0938>  
  <https://doi.org/10.1119/1.4712308>

- M. Le Bellac and J.-M. Levy-Leblond, **“Galilean Electromagnetism,”** *Il Nuovo Cimento B* 14, 217–234 (1973). Establishes distinct Galilean electric and magnetic limits and is essential prior work for any publication claim concerning Galilean EM.  
  <https://doi.org/10.1007/BF02895715>

- Giovanni Manfredi, **“Non-relativistic limits of Maxwell's equations,”** 2013. Reviews and systematically derives the Galilei-covariant electric and magnetic limits.  
  <https://arxiv.org/abs/1303.5608>

- Harvey R. Brown and Peter R. Holland, **“The non-relativistic limits of the Maxwell and Dirac equations: the role of Galilean and gauge invariance,”** *Studies in History and Philosophy of Modern Physics* 34 (2003). Discusses the interpretation and limitations of the two Galilean Maxwell regimes.  
  <https://www.sciencedirect.com/science/article/pii/S1355219803000054>

### VD architecture and local analysis

- `Newton/Design 3/vd_acting_object_architecture_consolidation.md`, managed VD-docs snapshot at commit `26265de6e79013bd93b37f9ad278c3dab6ffc11b`. This supplies the distinction among acting-object identity, force occurrence, value, slots, constructs, and parameters.

- `07_design_2_1/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md`. This supplies the independent-closure requirement and inverse Force-Sum recovery of an already warranted member value.

- `04_entry_design_guides/vd_spring_acting_object_working_brief_v1.md`. This supplies the model of a law-locked, carrier-attached construct and the constitutive-carrier weighting branch.

### Coverage note

The managed VD source was read at one resolved `main` commit, `26265de6e79013bd93b37f9ad278c3dab6ffc11b`. The local scope included the current force-sum/IFS note and acting-object entry briefs. The external search was scoped to moving-dipole electric moments, spin-current-induced electric fields, and Galilean electric/magnetic limits. It was not an exhaustive novelty search across physics, philosophy of physics, or electromagnetic source ontology.
