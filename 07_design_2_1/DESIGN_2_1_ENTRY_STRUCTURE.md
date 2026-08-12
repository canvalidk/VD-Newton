# Design 2.1 Entry Structure

Working structure ledger forked from Design 3. This file is for placing entry
roles before writing final Design 2.1 entry wording.

Columns:

- **Number**: proposed Design 2.1 entry number.
- **Role**: structural role in the VD, including triplet/chimney/wall status.
- **Contents**: plain description of what the entry text should contain.
- **Attribute refs**: list items, object-like commitments, or deferred
  witness-sheet attributes the entry may refer to.
- **Notes**: comments, routed changes, placeholders, uncertainties, and links
  to Design 2 / Design 3 where useful.

## Ratified Force-Member Naming

Design 2.1 uses `impressed-force` for one independently warranted force-action
upon a target material object, keyed by its acting-object instance and admitted
to the target's `interacting-forces-set`. The name follows Newton's *vis
impressa* and identifies the action on the target before any vector composition.
It is not a free-floating formula, a merely possible mechanism output, or a
vector granted physical status because it completes a desired sum. The naming
authority is
`../08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`.

Inherited from Design 3, Design 2.1 currently keeps `action-force` for the
force returned on the action side of an acting-object's action/reaction
structure. This replaces the colder earlier term `canonical-force`.

## Negative And Zero Entries

These entries sit before the Newtonian kinematic sequence. Positive entry
numbers begin only once the physics/kinematics entries begin.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [E-2] | Raw physical-law entry. | Establishes raw physical law as a pre-Newtonian structural kind. | raw physical-law kind |  |
| [E-1] | Raw meaning entry. | Establishes raw meaning as a pre-entry structural kind. | raw meaning handle |  |
| [E0] | Raw definition entry. | Establishes raw definition as the immediate prelude to ordinary VD entries. | headword; definiens; residual handle |  |

## Kinematics Table

Entry [E1] is the first kinematic/Newtonian entry included in this forked
ledger.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [K1] | time. | Captures D2[E1]. | time value; duration | Might be referred to by later object-impacted entries. |
| [K2] | reference-frame. | Captures D2[E2]. | origin; basis vectors; clock; coordinates | Might be referred to by later object-impacted entries. |
| [K3] | displacement. | Captures D2[E5]. | position; time; reference-frame | Might be referred to by later object-impacted entries. |
| [K4] | straight-line. | Captures D2[E10]. | geometric points; direction vector | Might be referred to by later object-impacted entries. |

## Law Table

Newton II follows the Newton I walls directly: E7 gives the peripheral
definition of `inertial-acceleration-material-object`, and E8 gives the same
headword its inward Newton-II definition. Generic point-particle motion remains
available through the earlier kinematic `acceleration` entry; there is no
separate point-particle inertial-acceleration headword.

At the NML3 seam, E9 does double duty: it is the Newton-II triplet entry for
`net-force-material-object` and the already-installed chimney for force sum.
There is therefore no standalone force-sum chimney at E13. E12 remains reserved
for the deferred inertial-mass wall, and the force-sum triplet begins at E13.
Meta-typing is placed after the physics blocks at the end of this ledger.

### Official NML2.1 headwords

The following entry headwords are fixed for the current NML2.1 drafting pass.
They may be shortened informally in discussion, but the ledger and eventual
entry headings use these full forms:

```text
[E7]  inertial-acceleration-material-object
[E8]  inertial-acceleration-material-object
[E9]  net-force-material-object
[E10] inertial-mass-material-object
[E11] net-force-material-object
```

The outward-facing inertial-mass wall at [E12] remains deferred until NML2.2.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [E1] | Newton I chimney; uniform-motion. | Captures D2[E14]. | velocity; speed; straight-line; time interval |  |
| [E2] | Newton I triplet; uniform-motion November redefine. | Captures D2[E15]. | uniform-motion; free-particle status; inertial-frame commitment |  |
| [E3] | Newton I triplet; inertial-frame winter entry. | Captures D2[E16]. | reference-frame slots; free-particle status; uniform-motion |  |
| [E4] | Newton I triplet; free-particle winter entry. | Captures D2[E17]. | point-particle status; frame of description; uniform-motion |  |
| [E5] | Newton I wall; inertial-frame. | Captures D2[E18]. | reference-frame slots; inertial-frame commitment; frame modelling input |  |
| [E6] | Newton I wall; free-particle. | Captures D2[E19]. | point-particle status; free-particle status; absence of relevant external influence |  |
| [E7] | Newton II chimney; inertial-acceleration-material-object. | Captures D2[E20], revised to make the massive/material-object domain part of the headword itself. | material-object; trajectory; inertial-frame; acceleration; selected time | First of exactly two inertial-acceleration-material-object definitions. Generic point-particle acceleration remains kinematic. |
| [E8] | Newton II triplet; inertial-acceleration-material-object November redefine. | Captures D2[E21]; for one material object, this acceleration is net-force-material-object divided by inertial-mass-material-object. | inertial-acceleration-material-object; net-force-material-object; inertial-mass-material-object | Second and final inertial-acceleration-material-object definition. |
| [E9] | Newton II triplet; net-force-material-object winter entry; force-sum chimney. | Captures D2[E22]. | net-force-material-object; inertial-mass-material-object; inertial-acceleration-material-object | Official headword fixed for NML2.1. Reused as NML3's already-installed force-sum chimney; no separate E13 chimney. |
| [E10] | Newton II triplet; inertial-mass-material-object winter entry. | Captures D2[E23]. | inertial-mass-material-object; net-force-material-object; inertial-acceleration-material-object | Official headword fixed for NML2.1; distinct from the deferred outward-facing inertial-mass wall. |
| [E11] | Newton II wall; net-force-material-object. |  | material-object; net-force-material-object; interacting-forces-set | Official headword fixed for NML2.1. |
| [E12] | Newton II wall; inertial-mass (exact headword deferred). |  | material-object; inertial-mass | Deferred until NML2.2 supplies the target/address and persistence account. |
| [E13] | Force-sum triplet; net-force-material-object November redefine. | Captures D2[E24]. | material-object witness; net-force-material-object; interacting-forces-set; impressed-force | E9 supplies the chimney role. |
| [E14] | Force-sum triplet; interacting-forces-set winter entry. | Captures D2[E25]. | material-object witness; interacting-forces-set; impressed-force; net-force-material-object |  |
| [E15] | Force-sum triplet; impressed-force winter entry. | Captures D2[E26]. | impressed-force; interacting-forces-set; net-force-material-object |  |
| [E16] | Force-sum wall; IFS generator. | Supports one-at-a-time unfolding of impressed-forces through mechanical-composition. | material-object witness; mechanical-composition_point-particle; acting-object; impressed-force; interacting-forces-set |  |
| [E17] | Force-sum wall; IFS closer / terminator. | Supports explicit closure when no more acting-objects are to be considered. | interacting-forces-set; generator state; no-more-acting-objects signal |  |
| [E18] | Action-reaction chimney; impressed-force. |  | impressed-force; action-or-reaction status |  |
| [E19] | Action-reaction triplet; impressed-force November redefine. | Captures D2[E31]. | impressed-force; action-force_acting-object; reaction-force_acting-object |  |
| [E20] | Action-reaction triplet; action-force_acting-object winter entry. | Captures D2[E32]. | acting-object; action-force; reaction-force; impressed-force |  |
| [E21] | Action-reaction triplet; reaction-force_acting-object winter entry. | Captures D2[E33]. | acting-object; reaction-force; action-force; impressed-force |  |
| [E22] | Action-reaction wall; action-force_acting-object. |  | acting-object; action-force; concrete action-force |  |
| [E23] | Action-reaction wall; reaction-force_acting-object. |  | acting-object; reaction-force; paired material-object; action-force |  |
| [E24] | Acting-object chimney; action-force_acting-object. |  | acting-object; action-force; activation-condition |  |
| [E25] | Acting-object triplet; action-force_acting-object November redefine. | Captures D2[E36]. | acting-object; action-force; activation-condition; target material-object |  |
| [E26] | Acting-object triplet; acting-object winter entry. | Captures D2[E34]. | acting-object; activation-condition; action-force |  |
| [E27] | Acting-object triplet; activation-condition_acting-object winter entry. | Captures D2[E35]. | acting-object; activation-condition; action-force; target material-object |  |
| [E28] | Acting-object wall; acting-object. | Peripheral meaning for acting-object. | acting-object identity; concrete type; paired material-object; participant slots | Unclear what should be here. |
| [E29] | Acting-object wall; activation-condition_acting-object. | Physical circumstance under which a concrete acting-object's force contribution is coherent. | activation-condition; concrete activation-condition; concrete acting-object |  |
| [E30] | Closure chimney; interaction-candidate. | Captures D2[E40]. | mechanical-system; force-accounting member particle; impressed-force; interacting-forces-set |  |
| [E31] | Closure triplet; interaction-candidate November redefine. | Captures D2[E41]. | interaction-candidate; interaction-pair; mechanically-closed-system |  |
| [E32] | Closure triplet; interaction-pair winter entry. | Captures D2[E42]. | interaction-candidate; interaction-pair; mechanically-closed-system |  |
| [E33] | Closure triplet; mechanically-closed-system winter entry. | Captures D2[E43]. | mechanical-system; interaction-candidate; interaction-pair |  |
| [E34] | Closure wall; interaction-pair. | Captures D2[E44]. | two interaction-candidates; shared acting-object; canonical/reaction roles; paired material-object |  |
| [E35] | Closure wall; mechanically-closed-system. | Captures D2[E45]. | mechanical-system; internal interactions; produced equations |  |
| [E36] | Meta-typing chimney; raw-class. | Captures D2[E27]. | raw-class status | Moved to the end of the active ledger for NML3 sequencing. |
| [E37] | Meta-typing triplet; raw-class November redefine. | Captures D2[E28]. | raw-class; class-specific-features; instance-of |  |
| [E38] | Meta-typing triplet; class-specific-features winter entry. | Captures D2[E29]. | raw-class; class-specific-features; instance-of |  |
| [E39] | Meta-typing triplet; instance-of winter entry. | Captures D2[E30]. | entity identity; instance-of; raw-class; class-specific-features |  |
| [E40] | Meta-typing wall; class-specific-features. |  | raw-class; class-specific-features |  |
| [E41] | Meta-typing wall; instance-of. |  | entity identity; instance-of; raw-class |  |

## Object Inventory

Objects and object-like commitments inherited from Design 3 that Design 2.1 may
keep, simplify, or mark as deferred.

| Object | Contents | Notes |
|---|---|---|
| point-particle | Particle-like object whose spatial extent/internal structure is neglected. | D2[E3]. May need to become a broad object kind or split. |
| material-object | Persistent, trackable physical individual with an inertial-mass slot/referent, represented through a point-particle motion witness. | Witness type accompanying the Newton II entries; not itself a VD entry. |
| free-particle | Particle object considered free for Newton I / frame reasoning. | D2[E17], D2[E19]. Keep separate from Newton II net-force / inertial-mass routing. |
| massless-free-particle | Free particle object without inertial-mass. | Important for separating path, uniform-motion, and trajectory-read acceleration questions from Newton II acceleration questions. |
| reference-frame | Coordinate/time convention object. | D3[E2], from D2[E2]. |
| inertial-frame | Reference-frame accepted for trajectory-read acceleration and Newtonian force accounting. | D2[E16], D2[E18]. |
| mechanical-system | Selected collection of particle objects. | D2[E39]. |
| interacting-forces-set | Force-set witness for a particle at a time. | D2[E25], Design 3 generator/closer issue. |
| impressed-force | Independently warranted force-action upon a target material object, keyed by its acting-object instance and admitted to the target's force account. | Ratified replacement for all predecessor force-member names; see the 2026-08-12 terminology authority. |
| acting-object | Force-producing or force-contributing callable object. | D2[E34], Design 3 stress point. |
| concrete acting-object | Typed acting-object instance such as spring, gravity, contact, or string mechanism. | Needs later concrete clusters. |
| interaction-candidate | Closure-side force candidate. | D2[E40], D2[E41]. |
| interaction-pair | Closure-side pair object. | D2[E42], D2[E44]. |
| object witness / witness sheet | Trace-side record of a concrete object commitment. | Not a VD entry yet; forced by attribute demands. |
| attribute slot | Demandable attribute on a witness sheet. | Later possible internalisation. |

## Abstract Witness Sheets

Draft witness sheets for abstract objects. These list what the trace may ask of
each object kind before concrete entries are written.

| Witness kind | Demandable attributes / slots | Notes |
|---|---|---|
| point-particle | identity token; point-particle status; position; velocity; speed; trajectory | Kinematic slots only. Raw acceleration is not treated as an innate particle slot here. |
| material-object | identity token; point-particle slots; inertial-mass; mechanical-composition_point-particle; interacting-forces-set; net-force; material-object inertial-acceleration | `inertial-mass` has a referent; the Newton II / force-accounting slots belong to this witness type. |
| free-particle | identity token; point-particle slots; free-particle status; uniform-motion; frame of description; inertial-frame-acceleration_particle-trajectory | Uses the weaker trajectory-read acceleration entry, with no net-force / inertial-mass relation. |
| massless-free-particle | identity token; free-particle slots; no inertial-mass referent; path / trajectory; uniform-motion; inertial-frame-acceleration_particle-trajectory | Does not enter Newton II through inertial-mass or net-force / inertial-mass. |
| reference-frame | identity token; origin; basis vectors; clock; coordinates assigned to events | D2[E2]. |
| inertial-frame | identity token; reference-frame slots; inertial-frame commitment; free-particle / uniform-motion criterion | Frame commitment should land at the wall. |
| mechanical-system | identity token; member particles; force-accounting member particles; interaction-candidates; mechanically-closed-system status | Selected by observer for analysis; closure only sees members with force-accounting structure. |
| interacting-forces-set | target material-object; time; impressed-force members; generator state; closer / no-more-acting-objects signal | Design 2.1 should not fill this as a batch. |
| impressed-force | identity token or derived identity; source acting-object; target material-object; force value/equation; action-or-reaction status | Force identity may derive from acting-object plus target. |
| acting-object | identity token; concrete type; paired material-object; activation-condition; action-force; reaction-force; participant slots; modelling assumptions | Exact wall content still unclear. |
| concrete acting-object | identity token; abstract acting-object slots; concrete activation-condition; concrete action-force; participant slots; constructs; parameters; force-accounting targets | Type hub should dispatch abstract slots to concrete entries. |
| interaction-candidate | impressed-force; target material-object; mechanical-system; time; pairability status | Closure-side view of forces. |
| interaction-pair | two interaction-candidates; shared acting-object; canonical/reaction roles; paired-particle target | D2[E44]. |
| object witness / witness sheet | identity token; object kind; slot bindings; unbound slots; source of each binding | Trace artifact, not final entry machinery yet. |
| attribute slot | slot name; owning witness kind; binding status; value or boundary | Later possible entry family. |
