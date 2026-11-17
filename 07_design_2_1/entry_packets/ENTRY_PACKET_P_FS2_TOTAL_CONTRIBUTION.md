# Entry Packet: P-FS2 — Total Contribution

Status: substantive candidate packet, written 2026-11-17. Candidate wording is
included for review; it is not installed in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.

## ENTRY PACKET

**Entry id:** [P-FS2] — temporary ledger address.

**Headword:** `contribution_n`.

**Status:** candidate — primary proposed continuation.

**Role:** triplet-winter; reused Interaction chimney.

**Law/block:** Force-Sum.

### Source Status And Lineage

New candidate from the November proposal. There is no installed predecessor for this headword. The 17 November naming correction calls this house Force-Sum.

Source hierarchy: the user's 17 November naming correction and approved packet
selection; the current entry ledger; the source decisions and their stated
grades; then the packet template as an authoring scaffold. Candidate deductions
and interface choices below are not promoted to user rulings.

- [Entry structure at the authoring snapshot](https://github.com/canvalidk/VD-Newton/blob/19990f826e31d60376eab1080cdc1f0f64172154/07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md).
- [Packet template](../../04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md) and [editing rules](../EDITING_RULES.md).
- [11 November decisions](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/contribution_law_and_force_sum_decisions_2026-11-11.md), §2.
- [12 November recursion](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/how_the_list_works_contribution_recursion_2026-11-12.md), §§3–4 and 11.

All managed source links use **VD-docs@90383f7dfa8225e8b5496d7b3d795e13cbff3151**. The
entry-production snapshot is **VD-Newton@19990f826e31d60376eab1080cdc1f0f64172154**. Older
sources use “contribution law” for the current Force-Sum law and “Force-Sum”
for the current Interaction law.

### Plain Purpose

Determine the total explicit contribution to one target's force account from its net force and haze. This inward use concerns n = 0 only.

### Preserve

- One shared target and account/context for F, H, and C_0.
- The inward and recursive outward uses belong to the same parameterized contribution headword.
- Haze is subtracted once; it is not part of any recursive tail.

### Change / Reject

- Extending C_n = F - H to every n.
- Introducing a separate total-contribution headword as though that decision had been made.
- Choosing a list, admitting interactions, or evaluating individual forces inside this corner.

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

- net-force-material-object
- haze

These are required daughter mentions for the proposed entry, including a
recursive occurrence where listed. Their placement may involve a conditional
demand rather than evaluation of every daughter in advance.

**Other headword mentions / surrounding entries:** P-I1 supplies the other definition of contribution_n. interaction-set and impressed-force explain that other route but do not appear as daughters here.

### Forbidden Headword Mentions / Hidden Imports

- interaction-set / impressed-force in this definiens: they import the next house.
- A guessed zero haze: an unbound daughter is not zero.
- A silent definition-selection rule: this packet does not settle how an engine selects the inward or outward use.

### Question Or Trace Moment

Given net force and haze for this account, what total explicit contribution must the account supply?

### Witness Kind And Explicit Bindings

**Witness kind:** material-object force-accounting commitment; explicit bindings supplied by a reader.

**Slots read:**

- Target p and account/context κ.
- Net-force and haze vectors under the same qualifications.
- The specified counter value n = 0.

**Slots written / exposed:**

- The constraint/value C_0 = F - H.
- Which daughter determinations supplied the result; no enumeration of the interactions.

### Boundary Behaviour

- At n > 0 this inward definition is not applicable; it supplies no tail value. P-I1 or an appropriate explicit binding is needed.
- If either daughter is unbound, retain the symbolic relation or expose the missing demand; do not manufacture a vector.
- Incompatible target, frame, time, account, or quantity type blocks combining the daughters.

### IRIL — Ideal Residually Imparted Logic

**Allowed:**

- Expose net-force-material-object[p,κ] and haze[p,κ], then subtract the second vector from the first.
- Keep the result addressed as contribution_n with n set to zero.
- Compare with an independently determined C_0 only under the same account and uncertainty constraints.

**Blocked:**

- Inferring the values or identities of individual members from their total.
- Using C_0 to supply every C_n.
- Re-expanding F through P-FS1 and claiming an independent determination from that circular route.

**Trace consequence:** Two available daughter vectors yield C_0. Otherwise the trace retains the appropriate demands/relation. For n > 0, record that this entry's domain does not apply; do not report a physical contradiction.

### IRIEs — Ideal Residually Imparted Effects

**Reader/modeler behaviour to install:**

- Distinguish the total contribution from each remaining tail.
- Track whether the two daughter values were independently available or merely rewritten from one another.

**Anti-habit / anti-misread:**

- A function's value at zero is not its value at every argument.
- A total force contribution is not an interaction inventory.

### Suggested Wording

Use the n = 0 restriction on the demand explicitly. Writing only “contribution_n is net force minus haze” is too broad.

### Draft Entry

Provisional human-facing candidate:

```text
contribution_n[p,κ; n = 0] :=
    net-force-material-object[p,κ] minus haze[p,κ].
```

### Residual Design And Provenance

Working handle: `Res_P_FS2(net-force-material-object, haze; n = 0)`.

The handle belongs to this packet's entry; it is not a globally shared
operation or a settled E-number. This is a dependency/demand sketch. Conditional
or index-dependent demands are exposed after their bindings are available,
not evaluated eagerly merely because they appear in the sketch.

| Residual phrase / operation | Provenance and permitted work |
|---|---|
| n = 0 restriction | Source fixes the start at zero; this packet proposes an explicit domain annotation. It is not a parser rule. |
| minus | Ordinary vector subtraction; no physical membership or tolerance decision. |
| Repeated p, κ | Preserves the same addressed account; not a new law headword. |

## DEEP AUDIT ADD-ON

### Role Test

Only net-force-material-object and haze are daughter headwords. The domain annotation restricts this candidate to C_0. Whether the general function and this restricted inward definition fit the final house/definition-selection rules is still open.

### Worked Semantic Checks

These are desk checks of the proposed meaning, not engine executions or
physical validation. The examples use exact vectors in one common frame;
they do not impose an uncertainty model.

| Situation | Required consequence / limit |
|---|---|
| F = (5,2,0), H = (1,-1,0) N | C_0 = (4,3,0) N; substitution in F = H + C_0 restores F. |
| F = H | C_0 = 0; this says nothing about whether the list is empty. |
| Same input values, demand C_1 | No result from this entry. With a first member f_0, C_1 = C_0 - f_0 instead. |
| F defined only as H + C_0 | Substitution gives an identity, not new information. |

### Open Questions

1. Final representation of the n = 0 restriction beside the general headword.
2. Selection between this inward definition and P-I1 without inventing a dispatcher.
3. Whether the context binder should be split into explicit target/time/frame/account arguments.

### Related Packets

- [P-FS1: Net Force Through Contribution And Haze](ENTRY_PACKET_P_FS1_NET_FORCE.md)
- [P-FS3: Haze As The Force-Sum Difference](ENTRY_PACKET_P_FS3_HAZE.md)
- [P-I1: Recursive Contribution](ENTRY_PACKET_P_I1_RECURSIVE_CONTRIBUTION.md)
- [P-I3: Impressed Force From Adjacent Contributions](ENTRY_PACKET_P_I3_IMPRESSED_FORCE.md)
