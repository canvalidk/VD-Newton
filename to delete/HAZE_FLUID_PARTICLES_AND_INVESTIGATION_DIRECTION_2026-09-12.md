# Haze, fluid particles, and the limits of an adequate description

**Date:** 2026-09-12.  
**Status:** user-requested explanation and proposed investigation direction. The fluid-mechanical examples are established; their interpretation through haze is a proposal.  
**Submission:** local draft in VD-Newton's `pass to VD-docs/` folder; not submitted to the managed collection.

The motivating question is whether representing fluids as particles fails, why an Eulerian description might succeed where a Lagrangian description struggles, and whether haze helps explain the difference.

Particle descriptions of fluids do work. The more promising question concerns the adequacy of a chosen simplification: when we retain only some information about a fluid, under what conditions may we neglect the influence of the information we leave unresolved?

This connects directly to the latest haze argument. A force account can omit real contributions while remaining adequate for a specified prediction. Likewise, a fluid description can omit real motion while remaining adequate for a specified prediction. The connection between these two kinds of adequacy needs to be established through the dynamics; it cannot be assumed merely because both involve omission.

**Following material and describing locations are two ways of describing motion.**

The Lagrangian description follows labelled fluid parcels. The Eulerian description gives quantities such as velocity and density at spatial locations. Let $a$ label a parcel, $X(a,t)$ be its position, and $u(x,t)$ the Eulerian velocity field. They are connected by

$$
\frac{dX(a,t)}{dt}=u(X(a,t),t).
$$

For sufficiently regular flow, the chain rule gives

$$
\frac{d^2X(a,t)}{dt^2}
=\left[\partial_tu+(u\cdot\nabla)u\right]_{x=X(a,t)}.
$$

The expression on the right is the parcel's acceleration expressed through the field. These descriptions can therefore carry the same information. Merely changing between them does not average away motion. [McIntyre's Cambridge fluid-dynamics notes](https://www.damtp.cam.ac.uk/user/mem/FLUIDS-IB/kinem.pdf)

This gives the investigation an essential control: changing coordinates and changing resolution must be considered separately. Otherwise a consequence of simplifying the fluid may be mistakenly attributed to the choice of Eulerian or Lagrangian description.

**“Particle” can refer to different objects.**

An actual molecule, a continuum fluid parcel, and a numerical particle are different representations. Continuum fields describe averages over molecular detail. A parcel follows that continuum motion and may deform; it is not necessarily a rigid miniature object. Its mean motion also differs from the thermal motion of individual molecules. [Tong's fluid-mechanics lectures](https://www.damtp.cam.ac.uk/user/tong/fluids/fluids1.pdf)

A numerical particle carries the quantities selected by a computational model. Smoothed particle hydrodynamics is an example of a moving-particle method that successfully describes fluid behaviour, including turbulence in tested cases. Its success is direct evidence against a general claim that fluid dynamics cannot be represented through particles. [Monaghan's turbulence model for smoothed particle hydrodynamics](https://arxiv.org/abs/0911.2523)

The relevant question about a particle model is therefore what each particle represents, what information it carries, and what the model claims to predict.

**A useful particle approximation can become insufficient.**

Consider an illustrative fluid blob represented by its mass, centre position, and mean velocity. Those quantities do not specify how velocity varies inside it. Its upper portion might move faster than its lower portion, stretching the blob. Two blobs can share the same retained quantities while having different internal motion and therefore different subsequent shapes or interactions with their surroundings.

If the prediction concerns that deformation, the retained information is insufficient. Describing more of the internal motion can resolve the difficulty. A Lagrangian description can follow deforming material; it does not require every parcel to remain a rigid bead.

There is also a distinction between a valid equation and a sufficient predictive state. For a fixed collection of classical particles with constant total mass and cancelling internal forces,

$$
M\ddot X_{\mathrm{CM}}=F_{\mathrm{external}}.
$$

The particles need not remain close together for this centre-of-mass relation to hold. Their spatial distribution may nevertheless be needed to determine the external forces. Mass, centre position, and centre velocity alone need not supply those forces. [MIT's treatment of Newton's laws for systems of particles](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/6d6169c2a29a992114e615edc8e8d3e2_ZNVvYg1FOPk.pdf)

Thus a loss of compactness can defeat a particular lumping approximation without defeating the Newtonian momentum balance. Whether it does so depends on what the lump is being used to predict.

**Haze makes the omitted contribution relative to an account explicit.**

The current force-haze proposal can be written

$$
F_{\mathrm{net}}=C+H_C,
\qquad
H_C=F_{\mathrm{net}}-C.
$$

Here $C$ contains the selected, identified interaction contributions. Zero may be used as the nominal approximation to $H_C$, while the actual remainder is subject to a stated allowance. The actual remainder need not have zero mean or fluctuate randomly. Its mathematical type and admissible bounds remain part of the investigation.

Three quantities must remain distinct: the physical remainder, uncertainty about that remainder, and the error permitted by the intended use. Increasing permitted error does not physically reduce the remainder. Increasing an assumed variance does not establish that the corresponding uncertainty is justified.

In a fluid application, this suggests asking what remainder is generated by a chosen account and resolution, and how it affects the desired observable. The aggregate matters: omitted contributions may reinforce or cancel. The accuracy of a resultant does not establish the completeness of the interaction inventory.

**Fluid averaging already produces a concrete residual term.**

Let an overbar denote a spatial smoothing operation of width $\ell$. In incompressible flow with constant density $\rho$ and constant kinematic viscosity $\nu$, assuming the filter commutes with differentiation, the filtered momentum equation can be written

$$
\rho\left(\partial_t\bar u_i+\bar u_j\partial_j\bar u_i\right)
=-\partial_i\bar p+\rho\nu\nabla^2\bar u_i+\bar f_i
-\rho\partial_j\tau_{ij},
$$

where $\bar f_i$ is the filtered body-force density and repeated spatial indices are summed. The residual stress is

$$
\tau_{ij}=\overline{u_i u_j}-\bar u_i\bar u_j.
$$

Averaging the velocity product generally differs from multiplying the averaged velocities. The resulting residual stress must be determined or modelled to close the equations for the retained motion. This is established fluid mechanics. [Research on explicitly filtered equations and subgrid stresses](https://pmc.ncbi.nlm.nih.gov/articles/PMC6800707/)

For the haze investigation, define the candidate effective remainder

$$
h_{\ell,i}=-\rho\partial_j\tau_{ij}.
$$

This has units of force per volume. It expresses the contribution left out if the filtered equation retains pressure, viscosity, and body forces but omits the residual stress term. If a closure model already supplies $\tau^{\mathrm{model}}$, the remaining discrepancy is instead

$$
h^{\mathrm{remaining}}_{\ell,i}
=-\rho\partial_j\left(\tau_{ij}-\tau^{\mathrm{model}}_{ij}\right).
$$

This is a proposed mapping to haze. There is a material qualification: a residual in a coarse momentum equation is not automatically an additional impressed force from a newly identified acting-object. It can represent momentum transport by motion that the coarse description has suppressed. An integral of $h_\ell$ has force units, but identifying it with a particular material object's force remainder requires specifying that object and its momentum balance, including any transport across its boundary.

The fluid example therefore offers a precise test of haze's scope. Does haze refer specifically to omitted physical force contributions, or can it also organize effective discrepancies created by reducing the state description? Those roles may be related without being identical.

**Zero mean does not establish negligible consequences.**

The velocity-product expression shows why a zero-mean fluctuation can affect averaged dynamics: products and correlations can survive averaging. A nonzero residual stress does not guarantee a nonzero net force on every chosen region; its divergence and boundary contributions matter. Nevertheless, setting the mean fluctuation to zero does not justify deleting its influence.

A simpler illustration makes the observable dependence explicit. Consider the idealized one-dimensional diffusion model for a passive tracer, with constant diffusivity $\kappa$, a fixed initial position, and no resolved drift:

$$
dX_t=\sqrt{2\kappa}\,dW_t.
$$

Within this model,

$$
\mathbb E[X_t-X_0]=0,
\qquad
\mathbb E[(X_t-X_0)^2]=2\kappa t.
$$

Its position density obeys

$$
\partial_t c=\kappa\partial_{xx}c.
$$

The particle description and the spatial density describe the same spreading. Particle dispersion and diffusion are connected in Price's Eulerian–Lagrangian discussion. The density $c$ here describes tracer positions or concentration, not the fluid velocity field. [Price's fluid-mechanics essay](https://ocw.mit.edu/courses/res-12-001-topics-in-fluid-dynamics-fall-2024/mitres_12_001_f24_essay1_pt2.pdf)

In this example, zero displacement is exactly correct for the mean but increasingly inadequate for predicting an individual position accurately. If adequacy means root-mean-square displacement no greater than a length tolerance $\epsilon_x$, the model gives

$$
\sqrt{2\kappa t}\leq\epsilon_x,
\qquad
t\leq\frac{\epsilon_x^2}{2\kappa}.
$$

This is a derivation for this specified diffusion model and this RMS criterion. It is not a hard bound on every trajectory, a guarantee throughout the whole interval, or a universal lifetime of fluid parcels. A probability-of-containment criterion would require a different calculation. Confinement, correlated motion, or a different transport model can change the result.

The stochastic displacement in this example is a martingale, but it is not a literal instantaneous force. The example establishes what a martingale model can mean for one observable; it does not establish that force haze is generally a martingale.

**The earlier lumping suggestion should become a conditional research question.**

The earlier VD material connects fluid trackability, diffusive separation, lumping tolerances, and a possible boundary with thermodynamics. The useful proposal is that an admissible interval can depend on both unresolved motion and the precision required of a lumped description.

The broader claims need qualification. Diffusion does not show that all fluid material is intrinsically untrackable, that every continuum parcel follows Brownian motion, or that Newtonian mechanics ceases to apply when a blob disperses. Nor does a small centre-of-mass force remainder certify accurate temperature, mixing, or internal deformation.

The current question is whether the conditions for a sufficient force account and the conditions for a sufficient representation of material can be related quantitatively. A force tolerance and a position, shape, or concentration tolerance concern different quantities. The dynamical map between them is the work to be done.

**Context and source scope.**

This explanation develops the preceding conversation and the local [September 10 research direction](HAZE_FLUID_MECHANICS_AND_THERMODYNAMICS_RESEARCH_DIRECTION_2026-09-10.md). It uses the latest interpretation in [Haze and what a successful Newtonian approximation claims](HAZE_APPROXIMATE_CAR_PREDICTIONS_AND_CORE_NM_2026-09-12.md). These are active local drafts, not verified managed submissions.

The managed context was selected through `catalog.yaml` and read at **`canvalidk/VD-docs@0ad969e068e77175e86f6fe8dd24e6f9f7a965ce`**, reconfirmed as `main` on September 12:

- [Identifiability and Fluid Representation](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_particle_and_mass_origins/identifiability_and_fluid_representation_discovery.md), the exploratory connection between trackability and fluid representation.
- [The Lumping Horizon](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_lumping_consequences/lumping_horizon_and_thermodynamic_boundary.md), the proposed diffusion-based interval argument, whose quantitative and broader extensions were explicitly left unchecked.

This is a focused explanation of those questions and the cited fluid-mechanical examples, not an exhaustive literature or project audit. The outbox was checked at the same commit; its September 8 receipt does not cover this draft. No managed source was altered.

**Investigation direction: determine when unresolved motion must enter the explicit account.**

The proposed investigation should start with two linked cases. The first isolates the logic of tolerance; the second tests its connection to Newtonian force accounting.

**First, use passive-tracer dispersion.** Specify a simple resolved flow and an independently justified diffusion model. Compare a nominal trajectory, a stochastic trajectory ensemble, and the corresponding concentration field. Select observables such as mean position, RMS spread, and probability of containment. Vary the time interval and tolerance while keeping the underlying process fixed. Determine when the nominal trajectory remains sufficient and when diffusion must be represented explicitly. This provides a controlled example in which zero-mean unresolved motion can be negligible for one claim and significant for another.

**Then, use a fluid momentum example with controlled omission.** Start from a sufficiently resolved reference flow, with its numerical or measurement uncertainty assessed. Apply a specified filter at several resolutions. Compute the residual stress contribution and compare predictions that omit it with predictions that model it. Follow the same filtered velocity field in Eulerian coordinates and along its trajectories so that changing viewpoint is not confused with changing resolution. Test the consequences for a selected velocity, momentum, or material-object observable, with the object and transport terms explicitly defined.

The comparison should answer five questions:

1. **What is the actual remainder?** Determine its physical or effective meaning, units, dependence on resolution, and temporal structure. Establish whether it is biased, correlated, or reasonably represented by a particular stochastic model.
2. **What does the permitted haze license us to predict?** Declare the observable, norm or probability criterion, tolerance, and interval before assessing success. Translate the remainder through the dynamics into that criterion.
3. **Can a remainder be detected while remaining negligible?** Keep statistical evidence of departure from the nominal model separate from evidence that the departure exceeds the practical tolerance. Repeated measurements can reduce sampling uncertainty without reducing the physical spreading or omitted contribution.
4. **What improvement actually helps?** Compare better measurements, finer resolution, and adding a known omitted term. These improve different parts of the problem and need not reduce the same uncertainty or error.
5. **What can be attributed?** In an MFP1 interpretation, exceeding the supported allowance establishes a problem with the specified account. Identifying the omitted known interaction or transport contribution requires further structure or controlled comparison; the residual alone does not supply an acting-object identity.

The central hypothesis to investigate is that haze can express the conditions under which a finite representation is sufficient for a declared prediction, and indicate when unresolved effects must become explicit contributions or additional state variables. The decisive next step is to demonstrate that connection in the paired examples, including a case where the nominal prediction remains adequate and a case where it fails its declared tolerance. That would establish what haze contributes beyond naming a residual, while keeping open whether force haze and unresolved-motion allowances require one concept or two related concepts.
