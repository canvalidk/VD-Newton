# Design 2.1 Entry Structure

Working structure ledger forked from Design 3. This file is for placing entry
roles before writing final Design 2.1 entry wording.

Updated 2026-11-17 to include the November contribution, haze, and recursive
Force-Sum proposals. The proposed continuation below is ahead of the installed
entry wording in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.

Columns:

- **Number**: existing E-number or temporary proposal label. Labels beginning
  `P-` locate proposed entries without reusing retired E-numbers.
- **Role**: structural role in the VD, including triplet/chimney/wall status.
- **Contents**: plain description of what the entry text should contain.
- **Attribute refs**: list items, quantities, and object/context commitments
  the entry may demand. These are not a witness-sheet schema.
- **Notes**: comments, routed changes, placeholders, uncertainties, and links
  to Design 2 / Design 3 where useful.

## Current Proposal And Source Status

The working continuation now has two connected houses:

```text
contribution law: net-force / contribution / haze
Force-Sum:        contribution / impressed-force / interaction-set
```

The 11 November record states the contribution-law decision and the choice to
expand contribution. The 12 November record supplies the corrected single
conditional, a fixed numbered set, and the start at counter zero. Its reading
of the re-anchored Force-Sum triplet is graded **Agreed**, rather than a separate
ratification of every corner. This ledger places those proposals for entry
writing; it does not claim that the full houses have been written or checked.

The 26 August decision established
`net-force / impressed-force / interaction-set`. It remains the historical
naming authority until a replacement decision is made. The proposed
continuation separates its aggregation role from the relation to net force.
It preserves its interaction/value/target distinctions and the August
membership-versus-aggregation correction. The retired E13–E17 cut is not
reinstated.

Sources read at VD-docs commit `90383f7dfa8225e8b5496d7b3d795e13cbff3151`:

- [8 November entry synthesis](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/NEWTON_ENTRY_STRUCTURE_SYNTHESIS_2026-11-08.md): acting-object commitments, pairing, identity, and peripheral witness testimony.
- [11 November contribution-law decisions](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/contribution_law_and_force_sum_decisions_2026-11-11.md): decision grades, haze, expansion direction, and open walls.
- [12 November contribution recursion](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/how_the_list_works_contribution_recursion_2026-11-12.md): supersedes the earlier shrinking-set and simultaneous-building suggestions.
- [26 August Force-Sum naming decision](../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md): earlier authority and minimum typed distinctions.
- [Aggregate-versus-member bug report](DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md) and [abstraction boundary](FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md): aggregate agreement cannot admit or close a physical interaction set.

`action-force` remains the inherited name for the action-side force; the
synthesis's broader phrase “acting force” does not settle a new headword.

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

At the NML3 seam, use the proposed continuation below. E1–E12 retain their
existing locations. The E13-and-later rows are separated into a historical
routing table; they do not assign numbers, walls, or production order to the
November proposals.

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
| [E9] | Newton II triplet; net-force-material-object winter entry; proposed contribution-law chimney. | Captures D2[E22]. | net-force-material-object; inertial-mass-material-object; inertial-acceleration-material-object | Official headword fixed for NML2.1. Supplies earlier grounding for the proposed contribution law; no new chimney entry is inserted. |
| [E10] | Newton II triplet; inertial-mass-material-object winter entry. | Captures D2[E23]. | inertial-mass-material-object; net-force-material-object; inertial-acceleration-material-object | Official headword fixed for NML2.1; distinct from the deferred outward-facing inertial-mass wall. |
| [E11] | Newton II wall; net-force-material-object. |  | material-object; net-force-material-object; interaction-set | Official headword fixed for NML2.1. |
| [E12] | Newton II wall; inertial-mass (exact headword deferred). |  | material-object; inertial-mass | Deferred until NML2.2 supplies the target/address and persistence account. |

### Proposed Contribution-Law House

The table gives entry roles and mathematical content, not tokeniser-ready
strings. Write `F` for `net-force-material-object`, `H` for `haze`, and
`C_n` for the parameterized headword `contribution_n`. All refer to the same
target, time/frame, and context. `C_0` is the total explicit contribution.

The contribution law is `F = H + C_0`. Its joint dependencies are
`F -> (H, C_0)`, `C_0 -> (F, H)`, and `H -> (F, C_0)`.
The inward contribution corner below determines the **total at n = 0**.
It does not determine every tail from F and H alone. How the inward entry
expresses that domain beside the general function headword remains an entry
wording question.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [E9], reused | Contribution-law chimney. | Earlier Newton-II grounding of net-force-material-object. | target; inertial-mass; inertial-acceleration | Existing entry, not a second installation. |
| [P-C1] | Contribution-law triplet; net-force-material-object November redefine. | Net force is haze plus contribution_n with n set to 0. | haze; contribution_n; target/context | Start the meaningful operation at n = 0; haze enters once here. Exact entry spelling remains open. |
| [P-C2] | Contribution-law triplet; contribution_n winter entry, at n = 0. | The total explicit contribution is net force minus haze: C_0 = F - H. | net-force-material-object; haze; target/context | Proposed placement; also supplies the earlier grounding for the Force-Sum house. General tail values need the list relation below. |
| [P-C3] | Contribution-law triplet; haze winter entry. | Haze is net force minus total explicit contribution: H = F - C_0. | net-force-material-object; contribution_n at n = 0 | Its independent peripheral content belongs at P-H, not inside this corner. |
| [P-H] | Contribution-law wall; haze. | Placeholder for the human-supplied tolerance and the conditions under which omitted influence may be treated as haze. | question tolerance; target/context; admissibility of haze | **placeholder**. Bound, distribution, and a possible bar on reproducible structure are unresolved alternatives. Haze does not recursively expand inside the trace. |

The other contribution-law wall is **P-F1**, below: it gives contribution its
outward definition through the supplied interaction set and impressed forces,
and is the November corner of the next house. This is one proposed entry with
two structural roles, not a second copy of the same definition.

### Proposed Force-Sum House

For this traversal, let `I` be a fixed interaction-set, supplied with one
number for each member and a length `L`. Number its members `i_0 ... i_(L-1)`.
Let `f_n` be the impressed force of member `i_n` on the same target in the
same context. The counter is the changing state; I does not shrink.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [P-C2], reused | Force-Sum chimney. | Prior contribution-law grounding of the total contribution. | contribution_n at n = 0; net-force-material-object; haze | The general-tail/inward-definition interface remains to be written. |
| [P-F1] | Force-Sum triplet; contribution_n November redefine; contribution-law wall. | One definition: if length(I) > n, return impressed force of member n plus contribution_(n+1); otherwise return the zero vector. | interaction-set; length; numbered member; impressed-force; next counter | **usable as a mathematical schema**; final wording/engine spelling pending. Re-test the condition on each expansion. |
| [P-F2] | Force-Sum triplet; interaction-set winter entry. | Placeholder for the inward relation between the supplied collection, its target-directed impressed forces, and contribution. | interaction identities; impressed-force; contribution_n | Full corner unwritten. Aggregate agreement constrains a proposed account; it neither identifies a unique set nor establishes membership or the no-more-elements claim. |
| [P-F3] | Force-Sum triplet; impressed-force winter entry. | Proposed inverse direction for an identified member: f_n = C_n - C_(n+1), when n < L; equivalently isolate that member from the total and all the others. | same interaction; target/context; contribution tails; uncertainties | Candidate corner content, not a claim that a total uniquely determines several unknown forces. Preserve the identity of the quantity when comparing with its acting-force expression. |
| [P-F4] | Force-Sum wall; interaction-set. | Supply the already constructed interaction set, its numbering, and its length. Expose the identity, admission, and no-more-elements commitments behind that account. | target/context; interaction identities; numbering; length; admission grounds | **placeholder** for construction and physical warrant. Placement of the physical claim at or behind this wall is proposed; its separation from traversal is settled. Identity and who supplies numbering remain open. |
| [P-F5] | Force-Sum wall; impressed-force. | Ground one interaction's target-directed force; preserve its ID, participant bindings, and action/reaction convention when connecting to acting-force content. | interaction; target; acting ID; activation bindings; force expression/constraint | **placeholder**. Connects to the later acting-object/action-reaction work; the revised downstream house cut is open. |

The inverse expressions describe relations between the same quantities.
They do not move physical recognition into a triplet residual. Final
residuals must use the declared daughter demands; they may not silently look
up an object's testimony or select a new interaction.

#### Single Conditional And Its Boundary

```text
net-force := haze + (contribution_n where n = 0)

contribution_n :=
    if length(interaction-set) > n:
        impressed-force(member n, target, context) + contribution_(n+1)
    otherwise:
        (0, 0, 0)
```

This is mathematical notation. It is **one conditional definition**, not two
definitions chosen by an external dispatcher. The comparison is `L > n`,
not `L > n+1`. Starting at 0 and incrementing by 1 reaches L and then makes
no further member demand. A valid numbering contains each interaction once;
the unresolved identity rule must make “once” meaningful.

An empty supplied set returns zero immediately. Cancelling forces also sum
to zero, but zero is never the stop test. At every partial expansion, the
unexpanded `contribution_n` remains in the sentence. Stopping early with
that tail intact is allowed; silently discarding it is not this recursion.
The further policy “expand or bound the tail” remains a proposal.

| Event | Meaning | Entry location / status |
|---|---|---|
| No more elements are to be added to the account | Physical claim about the system and the chosen account. | Outside the summation; P-F4 marks a proposed landing site, not a finished construction law. |
| Counter reaches the supplied length | Mechanical exhaustion of that given list. | P-F1's condition; says nothing further about the physical account. |
| Wrong comparison, member, branch, or increment | Error in applying a meaningful step. | Locate it at that step; numerical agreement does not certify the step. |

Haze is outside this traversal. The terminal zero is the additive identity.
The completed set is supplied before summation starts; the earlier suggestions
of a shrinking remainder set and simultaneous set-building/summing are
superseded by the 12 November account.

The 12 November engine probe was hand-driven. Literal `n+1` in the tail
was not parsed as argument arithmetic; the working probe supplied a next call
through a separate argument. The increment was recorded as an input, the
comparison remained unchecked, and the graph dropped the self-reference.
This ledger therefore records entry design, not verified executable strings
or a completed law-detection result.

### Downstream Entry Requirements From The November Synthesis

These requirements steer the replacement of the historical acting-object and
closure rows. They do not ratify the old three-corner packaging or create a
new law for every requirement.

| Proposed content / role | What the entry structure must carry | Placement still open |
|---|---|---|
| Acting ID/name | Preserve which acting object, interaction, target, and context the activation and force routes concern. Equal vector values do not establish identity. | Minimal identity content must be available before membership; its headword and inward/outward cut are not fixed. |
| Activation-condition | Inclusion of an interaction's force entails activation under its original participant/context bindings. Recognition may require substantial peripheral prose. | The recognition wall and its connection to admission remain to be written. A reaction recipient does not replace the original activation bindings. |
| Acting-force expression or constraint | The independently evaluated force and the force isolated from net force minus haze and the other contributions concern the same quantity, with compatible uncertainty. An admitted force may still be numerically unknown. | P-F3/P-F5 must connect to this content; final abstract-to-concrete routing is deferred. |
| Reciprocal counterpart | Every action carries a counterpart obligation. If its recipient is unresolved, internal and external locations remain alternatives. Identified participants can force an internal counterpart. | Participant identification, mechanical composition, and system membership need explicit connections; an opposite vector alone does not locate its recipient. |
| System closure | Keep reciprocal incidence and membership of the chosen system distinct from list exhaustion and the account's no-more-elements claim. | Replacement closure entries remain placeholders. |

Acting force, activation condition, and acting ID are the three principal
properties in the synthesis. Whether they constitute one triplet is explicitly
open. A zero-valued active interaction is still an interaction.

### Remaining Entry-Writing Decisions

- Write the contribution headword's n = 0 inward domain and general recursive
  outward definition without treating every tail as F - H.
- Finish P-F2 and P-F3 as actual inward entries and check the proposed joint
  dependencies; the recursive schema alone does not complete the triplet.
- Set haze's peripheral contract; finish interaction identity, admission,
  numbering, and the no-more-elements warrant.
- Resolve how P-C1 relates to E11's current “exactly two ways” wording in
  its NML2.1 scope. The suggestion that E11 needs changing is still a proposal.
- Decide final E-numbers and residual handles after the house cut is stable.
  P-labels are temporary ledger addresses.
- Write and check the downstream acting-object, reciprocal-participant, and
  system-closure connections before treating the historical houses as usable.

### Historical E13-And-Later Routing

All rows in this table preserve earlier Design 2 / Design 3 routing only.
The November proposal labels above do not inherit these numbers. Unqualified
“triplet” and “wall” in these historical rows do not assert a current cut.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [E13] | Retired-cut Force-Sum triplet; net-force-material-object November redefine. | Historical D2[E24] routing. | material-object witness; net-force-material-object; interaction-set; impressed-force | Name translation applied; number and role not reinstated. |
| [E14] | Retired-cut Force-Sum triplet; interaction-set winter entry. | Historical D2[E25] routing. | material-object witness; interaction-set; interaction; impressed-force; net-force-material-object | Name translation applied; number and role not reinstated. |
| [E15] | Retired-cut Force-Sum triplet; impressed-force winter entry. | Historical D2[E26] routing. | impressed-force; interaction; interaction-set; net-force-material-object | Name translation applied; number and role not reinstated. |
| [E16] | Retired-cut Force-Sum wall; collection generator. | Historical one-at-a-time construction proposal. | material-object witness; mechanical-composition_point-particle; interaction; interaction-set | Role remains open. |
| [E17] | Retired-cut Force-Sum wall; collection closer / terminator. | Historical explicit-closure proposal. | interaction-set; generator state; no-more-interactions signal | Role remains open. |
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
| [E30] | Closure chimney; interaction-candidate. | Captures D2[E40]. | mechanical-system; force-accounting member particle; interaction; interaction-set |  |
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
| interaction-set | Target-indexed set of independently warranted interactions in a fixed context, supplied with a numbering and length for traversal. | Constructed before summation. Exact identity, admission, and the physical no-more-elements warrant remain open. |
| impressed-force | Target-directed vector force-action supplied by one interaction to one participant and summed into explicit contribution. | Preserve interaction/target identity; net force also includes haze in the proposed contribution law. |
| contribution_n | Vector-valued tail of the explicit account from counter n; contribution_0 is its total. | Proposed parameterized headword; I stays fixed as n changes. |
| haze | Omitted influence entering once alongside the total explicit contribution. | Proposed winter headword; peripheral tolerance/admissibility contract unfinished. |
| acting-object | Force-producing or force-contributing callable object. | D2[E34], Design 3 stress point. |
| concrete acting-object | Typed acting-object instance such as spring, gravity, contact, or string mechanism. | Needs later concrete clusters. |
| interaction-candidate | Closure-side force candidate. | D2[E40], D2[E41]. |
| interaction-pair | Closure-side pair object. | D2[E42], D2[E44]. |
| object witness / witness sheet | Peripheral testimony about a scene, which a person may consult when answering a wall. | Outside the trace; not a required schema or direct trace-side lookup mechanism. |
| explicit binding / attribute demand | Information requested and supplied at a trace site, preserving object and context. | Attribute existence does not supply its numerical value. |

## Peripheral Testimony And Demand Inventory

This inherited inventory lists possible demands and object commitments, not a
witness-sheet schema. A person can consult testimony outside the trace and
supply an explicit binding at a demanded site. The entries do not directly read
the testimony. Unfinished object relations remain design questions.

| Kind / commitment | Possible demanded information | Notes |
|---|---|---|
| point-particle | identity token; point-particle status; position; velocity; speed; trajectory | Kinematic slots only. Raw acceleration is not treated as an innate particle slot here. |
| material-object | identity token; point-particle slots; inertial-mass; mechanical-composition_point-particle; interaction-set; net-force; material-object inertial-acceleration | `inertial-mass` has a referent; the Newton II / force-accounting slots belong to this witness type. |
| free-particle | identity token; point-particle slots; free-particle status; uniform-motion; frame of description; kinematic acceleration in the stated frame | Uses the weaker trajectory-read acceleration entry, with no net-force / inertial-mass relation. |
| massless-free-particle | identity token; free-particle slots; no inertial-mass referent; path / trajectory; uniform-motion; kinematic acceleration in the stated frame | Does not enter Newton II through inertial-mass or net-force / inertial-mass. |
| reference-frame | identity token; origin; basis vectors; clock; coordinates assigned to events | D2[E2]. |
| inertial-frame | identity token; reference-frame slots; inertial-frame commitment; free-particle / uniform-motion criterion | Frame commitment should land at the wall. |
| mechanical-system | identity token; member particles; force-accounting member particles; interaction-candidates; mechanically-closed-system status | Selected by observer for analysis; closure only sees members with force-accounting structure. |
| interaction-set | target material-object; time/context; interaction members; numbering; length; admission and no-more-elements grounds | Do not infer membership or the physical claim from aggregate agreement or counter exhaustion. |
| impressed-force | source interaction; target material-object; force vector/equation; context; later action-or-reaction relation | Contribution is indexed by interaction and target; it is not the interaction-set member itself. |
| acting-object | identity token; concrete type; paired material-object; activation-condition; action-force; reaction-force; participant slots; modelling assumptions | Exact wall content still unclear. |
| concrete acting-object | identity token; abstract acting-object slots; concrete activation-condition; concrete action-force; participant slots; constructs; parameters; force-accounting targets | Type hub should dispatch abstract slots to concrete entries. |
| interaction-candidate | impressed-force; target material-object; mechanical-system; time; pairability status | Closure-side view of forces. |
| interaction-pair | two interaction-candidates; shared acting-object; canonical/reaction roles; paired-particle target | D2[E44]. |
| object witness / witness sheet | ordinary scene testimony; available identities, descriptions, measurements, and their sources | Peripheral material consulted by the person answering a demand. |
| explicit binding / attribute demand | requested quantity or commitment; object/context; supplied value or boundary; source | Recorded at the demanded trace site; no finished object runtime is assumed. |
