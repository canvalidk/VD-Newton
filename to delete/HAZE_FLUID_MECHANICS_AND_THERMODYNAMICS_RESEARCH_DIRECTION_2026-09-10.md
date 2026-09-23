# Research direction: haze, fluid mechanics, and thermodynamics

**Date:** 2026-09-10.  
**Status:** user-requested exploratory research direction; no new physical result established.  
**Submission:** local draft in `pass to VD-docs/`, awaiting transfer; not yet submitted.

## The proposed connection

The user proposes that haze may help explain the relationship between Newtonian force accounts, fluid descriptions, and thermodynamics. The immediate connection is between two questions: **what unresolved motion can be tolerated while treating material as one object, and what unresolved force contribution can be tolerated while predicting that object's motion?** The earlier lumping work addresses the first; haze could help connect it to the second.

The working force expression remains $\mathbf F_{\mathrm{net}}=m\mathbf a=Z_\epsilon+\mathbf C$, where *contributions* names the part expressed through identified impressed forces. A candidate research question is whether information represented by haze at one resolution must become an explicit contribution, fluctuation model, or transport quantity at another.

Lagrangian fluid descriptions follow material parcels; Eulerian descriptions specify fields at spatial locations. Both can describe the same continuum motion. The issue to investigate is how changing resolution or averaging affects their relationship. James Price's [fluid-mechanics essay](https://ocw.mit.edu/courses/res-12-001-topics-in-fluid-dynamics-fall-2024/mitres_12_001_f24_essay1_pt2.pdf) supplies concrete leads: unresolved motion represented through effective diffusivity, and correlations producing Stokes drift. A fluctuation with zero mean need not have zero effect on averaged motion.

## A first investigation

Use a tracked particle or material parcel with specified resolved motion and a separately specified fluctuation model. Compare its trajectory description with the corresponding spatial probability or concentration field. Vary the observation interval and required accuracy, and identify when the unresolved effects require additional explicit information. A probabilistic particle-position density must be distinguished from the fluid's velocity field.

The useful comparison is between the conditions for a sufficient force account and those for valid lumping. Their tolerances concern different quantities and must be connected through the dynamics. Test whether haze adds a useful common structure to these conditions, rather than merely renaming an existing fluctuation or approximation term.

The relation to thermodynamics remains a research question. The same body may support both mechanical and thermal descriptions. Neither a universal boundary between them nor a martingale definition of haze has been established.

## Earlier VD context and provenance

Two canonical August 26 sources were selected through the [VD-docs catalog](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/catalog.yaml) and read at **`canvalidk/VD-docs@0ad969e068e77175e86f6fe8dd24e6f9f7a965ce`**, reconfirmed as `main`:

- [Identifiability and Fluid Representation](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_particle_and_mass_origins/identifiability_and_fluid_representation_discovery.md): the trackability/fluid/Newton–Gibbs connection, explicitly left as an uncompleted synthesis.
- [The Lumping Horizon](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_lumping_consequences/lumping_horizon_and_thermodynamic_boundary.md): tolerance and interval conditions under diffusive relative motion; moved from particle-and-mass origins to lumping consequences. Its quantitative and broader physical extensions are explicitly unchecked and require validation.

The new connection and terminology come from the September 10 task **Recover NML3 haze findings** (`01a08c58-8763-7590-b6e1-13e05a419a21`); see the local [haze argument](NML3_HAZE_AND_THE_LOGIC_OF_NEWTONIAN_FORCE_ACCOUNTS_2026-09-10.md). The proposed first investigation is a development suggestion, not work already performed. This is a scoped research lead, not a literature review. The outbox was checked; its September 8 receipt does not receive this draft. No managed source was changed.
