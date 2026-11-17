# Entry Packet: P-I3 — Impressed Force From Adjacent Contributions

Status: substantive candidate packet, written 2026-11-17. Candidate wording is
included for review; it is not installed in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.

## ENTRY PACKET

**Entry id:** [P-I3] — temporary ledger address.

**Headword:** `impressed-force`.

**Status:** candidate — primary proposed continuation.

**Role:** triplet-winter; reused chimney for downstream alternatives.

**Law/block:** Interaction.

### Source Status And Lineage

Candidate inverse direction derived from the specified Interaction recurrence and placed in the 17 November ledger. The subtraction is a drafting deduction, not a separately quoted user ruling.

Source hierarchy: the user's 17 November naming correction and approved packet
selection; the current entry ledger; the source decisions and their stated
grades; then the packet template as an authoring scaffold. Candidate deductions
and interface choices below are not promoted to user rulings.

- [Entry structure at the authoring snapshot](https://github.com/canvalidk/VD-Newton/blob/19990f826e31d60376eab1080cdc1f0f64172154/07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md).
- [Packet template](../../04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md) and [editing rules](../EDITING_RULES.md).
- [12 November recursion](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/how_the_list_works_contribution_recursion_2026-11-12.md), §§2–4 and 8.
- [8 November entry synthesis](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/NEWTON_ENTRY_STRUCTURE_SYNTHESIS_2026-11-08.md), §§8–9 and 15.

All managed source links use **VD-docs@90383f7dfa8225e8b5496d7b3d795e13cbff3151**. The
entry-production snapshot is **VD-Newton@19990f826e31d60376eab1080cdc1f0f64172154**. Older
sources use “contribution law” for the current Force-Sum law and “Force-Sum”
for the current Interaction law.

### Plain Purpose

Determine or constrain the target-directed force of one already identified member by subtracting the contribution after that member from the contribution beginning with it.

### Preserve

- The same fixed numbered account in both tail calls.
- The identity of member i and the target of its impressed force.
- The restriction that i has a unique index n < L in this account.
- The distinction between an unknown value of an admitted member and an unidentified/missing member.

### Change / Reject

- Treating equal force vectors as equal interaction identities.
- Using a total alone to solve several unknown member forces.
- Inferring membership or activation from aggregate agreement.
- Treating an empty set's zero contribution as a zero-valued impressed-force member.

### Notation And Input Boundary

The brackets in the candidate string are human-readable argument notation,
not a claim about accepted tokenizer syntax. `p` is a target; `i` is an
interaction identity where used. `κ` is a proposed explicit context binder for
the same time/frame and force-account or convention commitments throughout a
determination. Its final argument decomposition remains open. It is not
permission to fetch hidden information.

`contribution_n` remains the headword; `n` is its counter. C_n is only a
mathematical abbreviation for a call at n. Physical kind and identity
commitments may be required without their numerical values being known.

The template's witness/slot fields below describe explicit trace demands and
supplied bindings. A person may consult peripheral testimony to answer them;
the entry does not read a witness-sheet schema. Packet boundaries describe
intended interpretation, not an implemented checking mechanism. With uncertain
inputs, preserve their joint constraints and dependence; no probability model,
independence assumption, or tolerance policy is supplied by this packet.

### Trace Critical Headword Mentions

- interaction-set
- contribution_n (at the selected index and the next index)

These are required daughter mentions for the proposed entry, including a
recursive occurrence where listed. Their placement may involve a conditional
demand rather than evaluation of every daughter in advance.

**Other headword mentions / surrounding entries:** The outward impressed-force definition is still a choice between P-AR1 and P-O1. Neither action/reaction content nor an orientation convention is imported into this inward corner.

### Forbidden Headword Mentions / Hidden Imports

- net-force-material-object / haze as additional inward daughters: those appear only when C_0 is expanded through the preceding house.
- Concrete force laws or activation predicates inside the residual.
- A guessed identity or ordinal used to make subtraction possible.

### Question Or Trace Moment

For this particular admitted interaction on this target, what force is left after the later tail is removed?

### Witness Kind And Explicit Bindings

**Witness kind:** identified interaction within one fixed target-indexed interaction-set.

**Slots read:**

- Target p, context κ, and interaction identity i.
- The unique index of i in I = interaction-set[p,κ].
- contribution_n at that index and at the next index, both for the same I.

**Slots written / exposed:**

- The same member's target-directed impressed-force relation/value.
- Its relation to the neighboring tails without changing its identity or recipient.

### Boundary Behaviour

- If i is not a member, this entry is inapplicable; it does not return zero.
- An absent/ambiguous numbering leaves the selection unresolved.
- If either tail is unbound, retain a constraint or demand it. A recurrence containing the very same unknown force cannot independently determine it.
- Different enumerations or accounts across the two tail calls invalidate the subtraction as this member's force.

### IRIL — Ideal Residually Imparted Logic

**Allowed:**

- Expose I, locate the unique number n assigned to i, and demand C_n and C_(n+1).
- Subtract the next tail from the current tail.
- When independent constraints are available, compare the resulting force with the same addressed quantity obtained outwardly.
- Preserve dependence between the adjacent tails; do not assume their uncertainties are independent.

**Blocked:**

- Evaluating a nonexistent final member at n = L.
- Removing an arbitrary equal-valued term instead of the identified member.
- Counting an algebraic identity as an independent force measurement.
- Renaming an incompatible concrete-force determination as another quantity to evade disagreement.

**Trace consequence:** For i = member n, C_n = f_i + C_(n+1) gives f_i = C_n - C_(n+1). Both tail calls must use the same fixed enumeration. Substitution of the forward recurrence merely recovers f_i and supplies no new data.

### IRIEs — Ideal Residually Imparted Effects

**Reader/modeler behaviour to install:**

- Identify the member before isolating its value.
- Carry the same interaction, target, frame/time and account through inward and outward determinations.

**Anti-habit / anti-misread:**

- The total does not tell us what the members are.
- Two ways of writing the same dependent data are not two independent determinations.

### Suggested Wording

Use interaction-set visibly to obtain the member's index. A bare “C_n minus C_(n+1)” would hide how the requested force acquired its index and omit a required daughter.

### Draft Entry

Provisional human-facing candidate:

```text
impressed-force[i,p,κ] :=
    let n be the unique number of i in interaction-set[p,κ];
    contribution_n[p,κ; n]
    minus contribution_n[p,κ; n+1].
```

### Residual Design And Provenance

Working handle: `Res_P_I3(interaction-set, contribution_n at n, contribution_n at n+1; i)`.

The handle belongs to this packet's entry; it is not a globally shared
operation or a settled E-number. This is a dependency/demand sketch. Conditional
or index-dependent demands are exposed after their bindings are available,
not evaluated eagerly merely because they appear in the sketch.

| Residual phrase / operation | Provenance and permitted work |
|---|---|
| unique number of i | Lookup within the supplied enumeration, conditional on membership; no new physical admission. |
| n+1 | Adjacent tail in the same enumeration. |
| minus | Inverse of the forward vector addition; carries no independence assumption. |

## DEEP AUDIT ADD-ON

### Role Test

The daughter headwords are interaction-set and contribution_n. Two calls to contribution_n are instances of one headword. Set lookup is essential to bind the force identity to its index; the exact relation/type treatment of this inverse corner remains a candidate.

### Worked Semantic Checks

These are desk checks of the proposed meaning, not engine executions or
physical validation. The examples use exact vectors in one common frame;
they do not impose an uncertainty model.

| Situation | Required consequence / limit |
|---|---|
| I = [i_0,i_1], C_0 = (5,2,0), C_1 = (-2,1,0) N | f_(i_0) = (7,1,0) N. |
| Last member i_1, C_2 = 0 | f_(i_1) = C_1; there is no member i_2. |
| i absent from I | Inapplicable, not zero. |
| Only C_0 known for two unknown member forces | No unique individual value; retain the unresolved relation. |
| C_n computed from f_i + C_(n+1) | The inverse recovers f_i identically; no independent validation. |

### Open Questions

1. Final argument grammar for interaction identity, lookup, and two calls to the same headword.
2. The membership/identity warrant belongs to the unfinished collection wall.
3. How this candidate inward corner and the unfinished P-I2 jointly meet the final triplet criteria.
4. How paired uncertainty constraints are represented without an invented independence rule.

### Related Packets

- [P-I1: Recursive Contribution](ENTRY_PACKET_P_I1_RECURSIVE_CONTRIBUTION.md)
- [P-FS2: Total Contribution](ENTRY_PACKET_P_FS2_TOTAL_CONTRIBUTION.md)
- [P-FS1: Net Force Through Contribution And Haze](ENTRY_PACKET_P_FS1_NET_FORCE.md)
- [P-O1: Impressed Force Under A Declared Orientation](ENTRY_PACKET_P_O1_ORIENTED_IMPRESSED_FORCE.md)
