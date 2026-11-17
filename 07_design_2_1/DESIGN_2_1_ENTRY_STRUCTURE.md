# Design 2.1 Entry Structure

Working structure ledger forked from Design 3. This file is for placing entry
roles before writing final Design 2.1 entry wording.

Updated 2026-11-17 with the user's Force-Sum / Interaction naming correction
and proposed Action–Reaction and alternative orientation-based houses.
The proposed continuation below is ahead of the installed entry wording in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.

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

The user's naming correction on 2026-11-17 governs this ledger:

| Law | Headwords | Role |
|---|---|---|
| **Force-Sum** | net-force / contribution / haze | Relates net force to explicit contribution and haze. |
| **Interaction** | contribution / impressed-force / interaction-set | Recursively expands contribution over the supplied interactions. |
| **Action–Reaction** (proposed house) | impressed-force / action-force_acting-object / reaction-force_acting-object | Connects a target's impressed force to a reciprocal pair with distinct recipients. |
| **Orientation-based evaluation** (alternative house; name provisional) | impressed-force / canonical-force_acting-object / canonical-force-orientation | Evaluates the target-side force from the quoted member and its recipient convention. |

The law previously labelled “contribution law” is **Force-Sum**. The recursive
law previously labelled “Force-Sum” is **Interaction**. The user described that
second law as otherwise unnamed. This corrects the current terminology; source
filenames and historical quotations retain the names they used.

The 11 November record supplies the haze/contribution relation and the choice
to expand contribution. The 12 November record supplies the corrected single
conditional, a fixed numbered set, and the start at counter zero. The names
above are now explicit user direction. Exact inward corner wording and the
unfinished walls remain proposals.

Action–Reaction is added as an entry-house candidate at the user's request.
Its pair obligation, recipient distinction, and value relation are clear
enough to place. Its final triplet cut and the peripheral orientation/identity
content still need completion; see its assessment below. The orientation-based
alternative is also laid out as P-O1–P-O5. These are competing cuts at the
impressed-force wall, not two consecutive houses to install together.

The 26 August decision established
`net-force / impressed-force / interaction-set` under its then-current
Force-Sum name. It remains historical evidence for the interaction/value/target
distinctions and is read alongside the current naming correction, not as a
reason to retain the earlier names. The retired E13–E17 cut is not reinstated.

Proposal labels now follow the law names. To locate references to the earlier
version of this ledger:

| Earlier label | Current label |
|---|---|
| P-C1, P-C2, P-C3 | P-FS1, P-FS2, P-FS3 |
| P-H | P-FS4 |
| P-F1, P-F2, P-F3, P-F4 | P-I1, P-I2, P-I3, P-I4 |
| P-F5 | P-AR1 (the impressed-force wall shared with Action–Reaction) |

Sources read at VD-docs commit `90383f7dfa8225e8b5496d7b3d795e13cbff3151`:

- [8 November entry synthesis](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/NEWTON_ENTRY_STRUCTURE_SYNTHESIS_2026-11-08.md), especially §§2, 9–10: activation, quantity identity, counterpart existence, participant location, and peripheral witness testimony.
- [11 November contribution-law decisions](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/contribution_law_and_force_sum_decisions_2026-11-11.md): earlier terminology, decision grades, haze, and open walls.
- [12 November contribution recursion](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/how_the_list_works_contribution_recursion_2026-11-12.md): supersedes the earlier shrinking-set and simultaneous-building suggestions.
- [Canonical-force orientation](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/Newton-analysis/criticism_history/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md), §§7–10: target assignment, a competing evaluation-triplet cut, and the structural counterpart obligation.
- [Member-named force laws](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/Newton-analysis/criticism_history/participant_symmetric_canonical_orientation/VD_PARTICIPANT_SYMMETRIC_CANONICAL_ORIENTATION_MESHING_d2.md), Part IX: the direction of installing the quoted-member convention in concrete entry headwords; final wording remains open.
- [Constitutive asymmetry sketch](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/Newton-analysis/criticism_history/ACTION_REACTION_CONSTITUTIVE_ASYMMETRY_SKETCH_d1.md): historical motivation and unresolved participant/mechanism distinction; its claim that the carrier uniquely fixes orientation is qualified by the later convention analysis.
- [26 August naming decision](../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md), [aggregate-versus-member bug report](DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md), and [abstraction boundary](FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md): earlier names and the enduring separation of membership from aggregation.

The old triplet wording was also checked in
[`02_engine/newton.py`](../02_engine/newton.py) at VD-Newton commit
`68d77605ccb1cf6987af3c695b7a716db4edc505`. It supplies historical
wording, not a completed implementation of the proposed house.

`action-force` remains the inherited action-side headword. Its conventional
designation must be stated; the synthesis's broader phrase “acting force”
does not settle a new headword.

## Entry Packets — 2026-11-17

Seven substantive candidate packets now accompany this ledger. Each contains
source provenance, IRIL/IRIEs, a candidate entry string, entry-owned residual
notes, boundary behaviour, worked semantic checks, and open questions.

Read P-FS2 and P-I1 together first: the former determines only C_0 through
Force-Sum, while the latter gives the general recursive tail. Packet argument
notation is provisional and has not been installed or tested as engine syntax.

| Packet | Scope and status |
|---|---|
| [P-FS2: Total Contribution](entry_packets/ENTRY_PACKET_P_FS2_TOTAL_CONTRIBUTION.md) | Primary candidate; inward contribution restricted to n = 0. |
| [P-I1: Recursive Contribution](entry_packets/ENTRY_PACKET_P_I1_RECURSIVE_CONTRIBUTION.md) | Primary candidate; one conditional over a fixed numbered set. |
| [P-FS1: Net Force Through Contribution And Haze](entry_packets/ENTRY_PACKET_P_FS1_NET_FORCE.md) | Primary candidate; net force from total contribution and haze. |
| [P-FS3: Haze As The Force-Sum Difference](entry_packets/ENTRY_PACKET_P_FS3_HAZE.md) | Primary candidate; required haze distinguished from its admissibility. |
| [P-I3: Impressed Force From Adjacent Contributions](entry_packets/ENTRY_PACKET_P_I3_IMPRESSED_FORCE.md) | Primary candidate; identified-member inverse with explicit set lookup. |
| [P-O1: Impressed Force Under A Declared Orientation](entry_packets/ENTRY_PACKET_P_O1_ORIENTED_IMPRESSED_FORCE.md) | Alternative candidate; target-side evaluation under declared orientation. |
| [P-O2: Canonical Force From An Addressed Impressed Force](entry_packets/ENTRY_PACKET_P_O2_CANONICAL_FORCE.md) | Alternative candidate; canonical vector from an explicitly selected participant. |

P-O1/P-O2 belong to the orientation-based alternative; their presence does not
select it over Action–Reaction. The other proposed entries remain at ledger
stage. In particular, the haze wall, collection construction/inward definition,
Action–Reaction corners/walls, and orientation inverse/walls remain unfinished.
The existing E9 packet supplies the earlier chimney; no duplicate was created.

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
| [E9] | Newton II triplet; net-force-material-object winter entry; proposed Force-Sum chimney. | Captures D2[E22]. | net-force-material-object; inertial-mass-material-object; inertial-acceleration-material-object | Official headword fixed for NML2.1. Supplies earlier grounding for the proposed Force-Sum law; no new chimney entry is inserted. |
| [E10] | Newton II triplet; inertial-mass-material-object winter entry. | Captures D2[E23]. | inertial-mass-material-object; net-force-material-object; inertial-acceleration-material-object | Official headword fixed for NML2.1; distinct from the deferred outward-facing inertial-mass wall. |
| [E11] | Newton II wall; net-force-material-object. |  | material-object; net-force-material-object; interaction-set | Official headword fixed for NML2.1. |
| [E12] | Newton II wall; inertial-mass (exact headword deferred). |  | material-object; inertial-mass | Deferred until NML2.2 supplies the target/address and persistence account. |

### Proposed Force-Sum House

The table gives entry roles and mathematical content, not tokeniser-ready
strings. Write `F` for `net-force-material-object`, `H` for `haze`, and
`C_n` for the parameterized headword `contribution_n`. All refer to the same
target, time/frame, and context. `C_0` is the total explicit contribution.

The Force-Sum law is `F = H + C_0`. Its joint dependencies are
`F -> (H, C_0)`, `C_0 -> (F, H)`, and `H -> (F, C_0)`.
The inward contribution corner below determines the **total at n = 0**.
It does not determine every tail from F and H alone. How the inward entry
expresses that domain beside the general function headword remains an entry
wording question.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [E9], reused | Force-Sum chimney. | Earlier Newton-II grounding of net-force-material-object. | target; inertial-mass; inertial-acceleration | Existing entry, not a second installation. |
| [P-FS1] | Force-Sum triplet; net-force-material-object November redefine. | Net force is haze plus contribution_n with n set to 0. | haze; contribution_n; target/context | Start the meaningful operation at n = 0; haze enters once here. Exact entry spelling remains open. |
| [P-FS2] | Force-Sum triplet; contribution_n winter entry, at n = 0. | The total explicit contribution is net force minus haze: C_0 = F - H. | net-force-material-object; haze; target/context | Proposed placement; also supplies the earlier grounding for the Interaction house. General tail values need the list relation below. |
| [P-FS3] | Force-Sum triplet; haze winter entry. | Haze is net force minus total explicit contribution: H = F - C_0. | net-force-material-object; contribution_n at n = 0 | Its independent peripheral content belongs at P-FS4, not inside this corner. |
| [P-FS4] | Force-Sum wall; haze. | Placeholder for the human-supplied tolerance and the conditions under which omitted influence may be treated as haze. | question tolerance; target/context; admissibility of haze | **placeholder**. Bound, distribution, and a possible bar on reproducible structure are unresolved alternatives. Haze does not recursively expand inside the trace. |

The other Force-Sum wall is **P-I1**, below: it gives contribution its
outward definition through the supplied interaction set and impressed forces,
and is the November corner of the next house. This is one proposed entry with
two structural roles, not a second copy of the same definition.

### Proposed Interaction House

For this traversal, let `I` be a fixed interaction-set, supplied with one
number for each member and a length `L`. Number its members `i_0 ... i_(L-1)`.
Let `f_n` be the impressed force of member `i_n` on the same target in the
same context. The counter is the changing state; I does not shrink.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [P-FS2], reused | Interaction chimney. | Prior Force-Sum grounding of the total contribution. | contribution_n at n = 0; net-force-material-object; haze | The general-tail/inward-definition interface remains to be written. |
| [P-I1] | Interaction triplet; contribution_n November redefine; Force-Sum wall. | One definition: if length(I) > n, return impressed force of member n plus contribution_(n+1); otherwise return the zero vector. | interaction-set; length; numbered member; impressed-force; next counter | **usable as a mathematical schema**; final wording/engine spelling pending. Re-test the condition on each expansion. |
| [P-I2] | Interaction triplet; interaction-set winter entry. | Placeholder for the inward relation between the supplied collection, its target-directed impressed forces, and contribution. | interaction identities; impressed-force; contribution_n | Full corner unwritten. Aggregate agreement constrains a proposed account; it neither identifies a unique set nor establishes membership or the no-more-elements claim. |
| [P-I3] | Interaction triplet; impressed-force winter entry. | Proposed inverse direction for an identified member: f_n = C_n - C_(n+1), when n < L; equivalently isolate that member from the total and all the others. | same interaction; target/context; contribution tails; uncertainties | Candidate corner content, not a claim that a total uniquely determines several unknown forces. Preserve the identity of the quantity when comparing with its acting-force expression. |
| [P-I4] | Interaction wall; interaction-set. | Supply the already constructed interaction set, its numbering, and its length. Expose the identity, admission, and no-more-elements commitments behind that account. | target/context; interaction identities; numbering; length; admission grounds | **placeholder** for construction and physical warrant. Placement of the physical claim at or behind this wall is proposed; its separation from traversal is settled. Identity and who supplies numbering remain open. |
| [P-AR1] | Interaction wall; impressed-force; proposed Action–Reaction November corner. | Ground one interaction's target-directed force through the pair and recipient relation specified below. | interaction; target; acting ID; activation bindings; action/reaction pair | **placeholder for final wording**. Shared entry with the proposed Action–Reaction house, not an extra impressed-force definition. |

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
| No more elements are to be added to the account | Physical claim about the system and the chosen account. | Outside the summation; P-I4 marks a proposed landing site, not a finished construction law. |
| Counter reaches the supplied length | Mechanical exhaustion of that given list. | P-I1's condition; says nothing further about the physical account. |
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

### Proposed Action–Reaction House

**Assessment:** sufficient content for a proposed structural house; not yet a
finished six-entry law. The candidate retains the historical three headwords:

```text
impressed-force / action-force_acting-object / reaction-force_acting-object
```

For one active binary Newtonian interaction i, let a and r be its distinct
action and reaction recipients under the declared convention, with vectors
A(i) and R(i) in the same time/frame/context. The content to preserve is:

```text
R(i) = -A(i)

impressed-force(i, p) =
    A(i), when p is the action recipient a
    R(i), when p is the reaction recipient r
    inapplicable, when p is neither participant
```

The pair also asserts that the reciprocal force occurrence exists on the other
participant. Writing a negative vector alone does not establish that occurrence
or identify its recipient. The two occurrences remain distinct even if both
vectors are zero. Neither the force's value nor “either action or reaction”
by itself supplies an interaction identity.

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [P-I3], reused | Action–Reaction chimney; impressed-force. | Earlier inward determination of an identified member's target-directed force through the Interaction law. | same interaction; target/context; contribution tails | Existing proposal reused as grounding. |
| [P-AR1], shared | Action–Reaction triplet; impressed-force November redefine; Interaction wall. | An interaction's impressed force on a participant is the action or reaction member addressed to that participant, with the reciprocal member on the other participant and equal-and-opposite values. | action-force_acting-object; reaction-force_acting-object; interaction; recipient bindings | Candidate inward content. The choice of branch must follow explicit bindings; a nonparticipant gets neither branch. This is the same P-AR1 listed in the Interaction house. |
| [P-AR2] | Action–Reaction triplet; action-force_acting-object winter entry. | The action-designated impressed force of this interaction, addressed to a, whose paired reaction force is addressed to r and has the opposite value. Conversely A(i) = -R(i) for that same pair. | impressed-force; reaction-force_acting-object; same interaction/context; action recipient | Candidate relational corner; designation and recipient grounding belong at the walls. It must refer to this interaction occurrence, not one global force per acting object. |
| [P-AR3] | Action–Reaction triplet; reaction-force_acting-object winter entry. | The reciprocal impressed force of this interaction, addressed to r, paired with the action on a, with R(i) = -A(i). | impressed-force; action-force_acting-object; same interaction/context; reaction recipient | Candidate relational corner. An unknown recipient can remain an existentially specified participant; an arbitrary opposite number cannot stand in for it. |
| [P-AR4] | Action–Reaction wall; action-force_acting-object. | Ground the designated action member through the concrete kind's recognition, participant assignment, and force expression or constraint, carrying the same acting ID and interaction. | concrete kind; action recipient; activation bindings; constructs/parameters; member-named force content | **placeholder**. Member-designating concrete entries are the sourced direction; exact headword/argument and convention content still need writing. |
| [P-AR5] | Action–Reaction wall; reaction-force_acting-object. | Ground which concrete member and participant the reaction demand concerns, connecting to the corresponding member-named content and the same interaction. | concrete kind; reaction recipient; original activation bindings; reciprocal relation | **placeholder**. A required peripheral grounding role, not a second independent numerical input by default. Merely repeating R = -A would not finish this wall. |

The proposed joint corner dependencies are
`impressed-force -> (action-force, reaction-force)`,
`action-force -> (impressed-force, reaction-force)`, and
`reaction-force -> (impressed-force, action-force)`, with full qualified
headwords as above. The final residues and argument bindings must make these
real dependencies. The displayed pair equation alone relates two quantities
and does not prove a three-corner law.

#### What Is Ready, And What Remains Open

- **Pairing and recipient obligations are ready to state.** Preserve one
  interaction across the two distinct recipient accounts. For this interaction,
  a participant receives one member of the pair; both members must not be
  inserted into that participant's account. A larger system may contain both
  recipients. One acting mechanism may participate in multiple interactions,
  so its ID alone need not identify a unique pair.
- **The convention needs a visible home.** A = -R does not choose which member
  a quoted concrete formula denotes. The member-named entry direction can
  supply that choice by dictionary authority. Reversing the quoted recipient
  and the quoted vector together preserves the target-side forces. Mechanical
  ownership, force recipient, and system membership must not be conflated.
- **Counterpart existence precedes known location or value.** An unresolved
  counterpart may be inside or outside the selected system. Establishing its
  participant inside the system forces the corresponding internal obligation.
  An omitted row is not evidence that the counterpart is external; a zero
  resultant is not evidence of mechanical closure.
- **The exact house cut remains a proposal.** The orientation record also
  proposes an evaluation triplet with impressed-force, canonical-force, and
  an orientation convention. This ledger adds the requested action/reaction
  candidate without claiming that the competing cut has been disproved.
  Final entries must account for both force delivery and pair existence.
- **Concrete grounding is unfinished.** The actor/mechanism-to-recipient link,
  argument identity, and both walls need actual entry wording. Preserve the
  original activation bindings on the reaction route. The conditional
  half-weighted two-instance architecture is not adopted by adding this house.

This house is scoped to the binary Newtonian pair being represented.
Generalisation to more participants and final executable wording are deferred.
The proposed rows do not claim that every force mechanism has an independently
supplied reaction formula, or that computing a negative vector independently
tests the physical account.

### Alternative Orientation-Based Evaluation House

This places the alternative proposed in the canonical-force orientation
record, §§7–10, as an explicit house candidate:

```text
impressed-force / canonical-force_acting-object / canonical-force-orientation
```

The latter two names are provisional source vocabulary. “Canonical force”
means the member selected for direct quotation, not an additional physical
force. Its relationship to the current `action-force_acting-object` headword
must be settled when choosing the cut.

For a fixed active binary interaction i with distinct participants a and b,
let the convention select a canonical recipient c and quote vector K for that
recipient. All quantities use the same interaction, time, and frame:

```text
impressed-force(i, p) =
    K(i),  when p = c(i)
   -K(i),  when p is the other participant
    inapplicable, when p is not a participant
```

| Number | Role | Contents | Attribute refs | Notes |
|---|---|---|---|---|
| [P-I3], reused | Alternative evaluation-house chimney; impressed-force. | Prior Interaction-law grounding of the target-directed force of an identified member. | interaction; target/context; contribution tails | Same earlier grounding as the Action–Reaction candidate. |
| [P-O1] | Alternative triplet; impressed-force November redefine; Interaction wall. | Return the quoted canonical vector to its declared recipient and its negative to the other participant; a nonparticipant receives neither. | canonical-force_acting-object; canonical-force-orientation; interaction; target | Alternative to P-AR1 at the same outward definition site, not an additional installed impressed-force definition. |
| [P-O2] | Alternative triplet; canonical-force_acting-object winter entry. | Relate the quoted vector to the impressed force under the declared orientation: K = f for the canonical recipient, and K = -f for the other participant. | impressed-force; canonical-force-orientation; interaction; target | Candidate inverse corner, restricted to a participant. |
| [P-O3] | Alternative triplet; canonical-force-orientation winter entry. | State which recipient/vector assignments are compatible with the quoted force and the target's impressed force under the same pair relation. | impressed-force; canonical-force_acting-object; participant identities | Inward relation unfinished. Agreement does not always determine a unique convention: when K = f = 0, values alone do not distinguish the recipients. |
| [P-O4] | Alternative wall; canonical-force_acting-object. | Ground the quoted member through concrete force content, parameters or constraints, and its specified recipient. | concrete kind; same acting/interaction identity; member-named expression; context | **placeholder**. Connects to the acting-object content without introducing a second force quantity for the same member. |
| [P-O5] | Alternative wall; canonical-force-orientation. | State which participant receives the quoted vector and which member the concrete formula denotes, preserving its coordinate and sign meanings. | participant bindings; quoted-member declaration; entry/convention authority | **placeholder**. The sourced direction is to install this declaration through member-named concrete entries; the final headword and placement remain open. |

The candidate joint dependencies are
`impressed-force -> (canonical-force, orientation)`,
`canonical-force -> (impressed-force, orientation)`, and
`orientation -> (impressed-force, canonical-force)`.
These indicate the intended corners; P-O3 still needs a satisfactory inward
definition, including its underdetermined cases.

Reversing both the canonical recipient and K leaves each participant's force
unchanged. Reversing K alone does not. The orientation must therefore accompany
the formula, even where dictionary authority supplies it once per kind rather
than the reader selecting it anew in every trace.

**Relationship to Action–Reaction:** P-O1–P-O5 and P-AR1–P-AR5 are alternatives
for developing the impressed-force wall. The orientation version makes force
delivery and the convention explicit. It still needs the structural content
that a reciprocal occurrence exists, belongs to the same interaction, and
addresses the other participant. Evaluating a negative vector does not supply
those facts. Their eventual entry location remains open, as does whether the
two candidates can be reconciled into one cut.

### Downstream Entry Requirements From The November Synthesis

These requirements connect the proposed Action–Reaction house to the
unfinished acting-object and closure rows. The acting object's own
three-property packaging remains open.

| Proposed content / role | What the entry structure must carry | Placement still open |
|---|---|---|
| Acting ID/name | Preserve which acting object, interaction, target, and context the activation and force routes concern. Equal vector values do not establish identity. | Minimal identity content must be available before membership; its headword and inward/outward cut are not fixed. |
| Activation-condition | Inclusion of an interaction's force entails activation under its original participant/context bindings. Recognition may require substantial peripheral prose. | The recognition wall and its connection to admission remain to be written. A reaction recipient does not replace the original activation bindings. |
| Acting-force expression or constraint | The independently evaluated force and the force isolated from net force minus haze and the other contributions concern the same quantity, with compatible uncertainty. An admitted force may still be numerically unknown. | P-I3 and P-AR1–P-AR5 must connect to this content; final abstract-to-concrete routing is deferred. |
| Reciprocal counterpart | Every action carries a counterpart obligation. If its recipient is unresolved, internal and external locations remain alternatives. Identified participants can force an internal counterpart. | Participant identification, mechanical composition, and system membership need explicit connections; an opposite vector alone does not locate its recipient. |
| System closure | Keep reciprocal incidence and membership of the chosen system distinct from list exhaustion and the account's no-more-elements claim. | Replacement closure entries remain placeholders. |

Acting force, activation condition, and acting ID are the three principal
properties in the synthesis. Whether they constitute one triplet is explicitly
open. A zero-valued active interaction is still an interaction.

### Remaining Entry-Writing Decisions

- Write the contribution headword's n = 0 inward domain and general recursive
  outward definition without treating every tail as F - H.
- Finish P-I2 and P-I3 as actual inward entries and check the proposed joint
  dependencies; the recursive schema alone does not complete the triplet.
- Set haze's peripheral contract; finish interaction identity, admission,
  numbering, and the no-more-elements warrant.
- Resolve how P-FS1 relates to E11's current “exactly two ways” wording in
  its NML2.1 scope. The suggestion that E11 needs changing is still a proposal.
- Decide final E-numbers and residual handles after the house cut is stable.
  P-labels are temporary ledger addresses.
- Finish the Action–Reaction corner dependencies, participant/identity
  arguments, and P-AR4/P-AR5 walls; resolve its relationship to the alternative
  orientation-triplet cut P-O1–P-O5, including P-O3's underdetermined cases.
- Write and check the downstream acting-object and system-closure connections
  before treating the historical houses as usable.

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
| impressed-force | Target-directed vector force-action supplied by one interaction to one participant and summed into explicit contribution. | Preserve interaction/target identity; net force also includes haze in the proposed Force-Sum law. |
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
