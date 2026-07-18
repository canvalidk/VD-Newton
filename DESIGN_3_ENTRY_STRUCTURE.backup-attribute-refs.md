# Design 3 Entry Structure

Working structure ledger. This file is for placing entry roles before writing
final entry wording.

Columns:

- **Number**: proposed Design 3 entry number.
- **Role**: structural role in the VD, including triplet/chimney/wall status.
- **Contents**: plain description of what the entry text should contain.
- **Notes**: comments, routed changes, uncertainties, and links to Design 2
  where useful.

## Negative And Zero Entries

These entries sit before the Newtonian kinematic sequence. Positive entry
numbers begin only once the physics/kinematics entries begin.

| Number | Role | Contents | Notes |
|---|---|---|---|
| [E-2] | Raw physical-law entry. | Establishes raw physical law as a pre-Newtonian structural kind. |  |
| [E-1] | Raw meaning entry. | Establishes raw meaning as a pre-entry structural kind. |  |
| [E0] | Raw definition entry. | Establishes raw definition as the immediate prelude to ordinary VD entries. |  |

## Kinematics Table

Entry [E1] is the first kinematic/Newtonian entry included in Design 3.

| Number | Role | Contents | Notes |
|---|---|---|---|
| [K1] | time. | Captures D2[E1]. | Might be referred to by later object-impacted entries. |
| [K2] | reference-frame. | Captures D2[E2]. | Might be referred to by later object-impacted entries. |
| [K3] | displacement. | Captures D2[E5]. | Might be referred to by later object-impacted entries. |
| [K4] | straight-line. | Captures D2[E10]. | Might be referred to by later object-impacted entries. |

## Law Table

Six-entry law blocks. Each law keeps its chimney, triplet, and two wall slots
sequential.

| Number | Role | Contents | Notes |
|---|---|---|---|
| [E1] | Newton I chimney; uniform-motion. | Captures D2[E14]. |  |
| [E2] | Newton I triplet; uniform-motion November redefine. | Captures D2[E15]. |  |
| [E3] | Newton I triplet; inertial-frame winter entry. | Captures D2[E16]. |  |
| [E4] | Newton I triplet; free-particle winter entry. | Captures D2[E17]. |  |
| [E5] | Newton I wall; inertial-frame. | Captures D2[E18]. |  |
| [E6] | Newton I wall; free-particle. | Captures D2[E19]. |  |
| [E7] | Newton II chimney; inertial-acceleration. | Captures D2[E20]. |  |
| [E8] | Newton II triplet; inertial-acceleration November redefine. | Captures D2[E21]. |  |
| [E9] | Newton II triplet; net-force winter entry. | Captures D2[E22]. |  |
| [E10] | Newton II triplet; inertial-mass winter entry. | Captures D2[E23]. |  |
| [E11] | Newton II wall; net-force. |  |  |
| [E12] | Newton II wall; inertial-mass. |  |  |
| [E13] | Force-sum chimney; net-force. |  |  |
| [E14] | Force-sum triplet; net-force November redefine. | Captures D2[E24]. |  |
| [E15] | Force-sum triplet; interacting-forces-set winter entry. | Captures D2[E25]. |  |
| [E16] | Force-sum triplet; acting-force winter entry. | Captures D2[E26]. |  |
| [E17] | Force-sum wall; IFS generator. | Supports one-at-a-time unfolding of acting-forces through mechanical-composition. |  |
| [E18] | Force-sum wall; IFS closer / terminator. | Supports explicit closure when no more acting-objects are to be considered. |  |
| [E19] | Meta-typing chimney; raw-class. | Captures D2[E27]. |  |
| [E20] | Meta-typing triplet; raw-class November redefine. | Captures D2[E28]. |  |
| [E21] | Meta-typing triplet; class-specific-features winter entry. | Captures D2[E29]. |  |
| [E22] | Meta-typing triplet; instance-of winter entry. | Captures D2[E30]. |  |
| [E23] | Meta-typing wall; class-specific-features. |  |  |
| [E24] | Meta-typing wall; instance-of. |  |  |
| [E25] | Action-reaction chimney; acting-force. |  |  |
| [E26] | Action-reaction triplet; acting-force November redefine. | Captures D2[E31]. |  |
| [E27] | Action-reaction triplet; canonical-force_acting-object winter entry. | Captures D2[E32]. |  |
| [E28] | Action-reaction triplet; reaction-force_acting-object winter entry. | Captures D2[E33]. |  |
| [E29] | Action-reaction wall; canonical-force_acting-object. |  |  |
| [E30] | Action-reaction wall; reaction-force_acting-object. |  |  |
| [E31] | Acting-object chimney; canonical-force_acting-object. |  |  |
| [E32] | Acting-object triplet; canonical-force_acting-object November redefine. | Captures D2[E36]. |  |
| [E33] | Acting-object triplet; acting-object winter entry. | Captures D2[E34]. |  |
| [E34] | Acting-object triplet; activation-condition_acting-object winter entry. | Captures D2[E35]. |  |
| [E35] | Acting-object wall; acting-object. | Peripheral meaning for acting-object. | Unclear what should be here. |
| [E36] | Acting-object wall; activation-condition_acting-object. | Physical circumstance under which a concrete acting-object's force contribution is coherent. |  |
| [E37] | Closure chimney; interaction-candidate. | Captures D2[E40]. |  |
| [E38] | Closure triplet; interaction-candidate November redefine. | Captures D2[E41]. |  |
| [E39] | Closure triplet; interaction-pair winter entry. | Captures D2[E42]. |  |
| [E40] | Closure triplet; mechanically-closed-system winter entry. | Captures D2[E43]. |  |
| [E41] | Closure wall; interaction-pair. | Captures D2[E44]. |  |
| [E42] | Closure wall; mechanically-closed-system. | Captures D2[E45]. |  |

## Object Inventory

Objects and object-like witnesses we may want the Design 3 structure to
recognise explicitly.

| Object | Contents | Notes |
|---|---|---|
| point-particle | Particle-like object whose spatial extent/internal structure is neglected. | D2[E3]. May need to become a broad object kind or split. |
| massive-particle | Particle object with an inertial-mass slot/referent. | Needed for Newton II acceleration route. |
| free-particle | Particle object considered free for Newton I / frame reasoning. | D2[E17], D2[E19]. Keep separate from Newton II routing. |
| massless-free-particle | Free particle object without inertial-mass. | Important for separating path/uniform-motion questions from inertial-acceleration questions. |
| reference-frame | Coordinate/time convention object. | D3[E2], from D2[E2]. |
| inertial-frame | Reference-frame accepted for inertial-acceleration / Newtonian force accounting. | D2[E16], D2[E18]. |
| mechanical-system | Selected collection of particle objects. | D2[E39]. |
| interacting-forces-set | Force-set witness for a particle at a time. | D2[E25], Design 3 generator/closer issue. |
| acting-force | Force contribution object/handle. | D2[E26], D2[E31]. |
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
| massive-particle | identity token; point-particle slots; inertial-mass; mechanical-composition_point-particle; interacting-forces-set; net-force; inertial-acceleration | `inertial-mass` has a referent; the Newton II / force-accounting slots belong here. |
| free-particle | identity token; point-particle slots; free-particle status; uniform-motion; frame of description | Question routing decides whether this is used. |
| massless-free-particle | identity token; free-particle slots; no inertial-mass referent; path / trajectory; uniform-motion | Does not enter Newton II through inertial-mass. |
| reference-frame | identity token; origin; basis vectors; clock; coordinates assigned to events | D2[E2]. |
| inertial-frame | identity token; reference-frame slots; inertial-frame commitment; free-particle / uniform-motion criterion | Frame commitment should land at the wall. |
| mechanical-system | identity token; member particles; force-accounting member particles; interaction-candidates; mechanically-closed-system status | Selected by observer for analysis; closure only sees members with force-accounting structure. |
| interacting-forces-set | target massive-particle; time; acting-force members; generator state; closer / no-more-acting-objects signal | Design 3 should not fill this as a batch. |
| acting-force | identity token or derived identity; source acting-object; target massive-particle; force value/equation; canonical-or-reaction status | Force identity may derive from acting-object plus target. |
| acting-object | identity token; concrete type; paired massive-particle; activation-condition; canonical-force; reaction-force; participant slots; modelling assumptions | Exact wall content still unclear. |
| concrete acting-object | identity token; abstract acting-object slots; concrete activation-condition; concrete canonical-force; participant slots; constructs; parameters; force-accounting targets | Type hub should dispatch abstract slots to concrete entries. |
| interaction-candidate | acting-force; target massive-particle; mechanical-system; time; pairability status | Closure-side view of forces. |
| interaction-pair | two interaction-candidates; shared acting-object; canonical/reaction roles; paired-particle target | D2[E44]. |
| object witness / witness sheet | identity token; object kind; slot bindings; unbound slots; source of each binding | Trace artifact, not final entry machinery yet. |
| attribute slot | slot name; owning witness kind; binding status; value or boundary | Later possible entry family. |
