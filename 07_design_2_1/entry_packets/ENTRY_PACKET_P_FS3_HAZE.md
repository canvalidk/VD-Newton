# Entry Packet: P-FS3 — Haze As The Force-Sum Difference

Status: substantive candidate packet, written 2026-11-17. Candidate wording is
included for review; it is not installed in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.

## ENTRY PACKET

**Entry id:** [P-FS3] — temporary ledger address.

**Headword:** `haze`.

**Status:** candidate — primary proposed continuation.

**Role:** triplet-winter.

**Law/block:** Force-Sum.

### Source Status And Lineage

New inward haze corner in the November proposal, under the user's current Force-Sum name. It does not supply the deferred P-FS4 wall.

Source hierarchy: the user's 17 November naming correction and approved packet
selection; the current entry ledger; the source decisions and their stated
grades; then the packet template as an authoring scaffold. Candidate deductions
and interface choices below are not promoted to user rulings.

- [Entry structure at the authoring snapshot](https://github.com/canvalidk/VD-Newton/blob/19990f826e31d60376eab1080cdc1f0f64172154/07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md).
- [Packet template](../../04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md) and [editing rules](../EDITING_RULES.md).
- [11 November decisions](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/contribution_law_and_force_sum_decisions_2026-11-11.md), §2.
- [12 November recursion](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/how_the_list_works_contribution_recursion_2026-11-12.md), §§4–6.

All managed source links use **VD-docs@90383f7dfa8225e8b5496d7b3d795e13cbff3151**. The
entry-production snapshot is **VD-Newton@19990f826e31d60376eab1080cdc1f0f64172154**. Older
sources use “contribution law” for the current Force-Sum law and “Force-Sum”
for the current Interaction law.

### Plain Purpose

Express the haze required by this account as the difference between net force and total explicit contribution.

### Preserve

- One target/context and the total contribution at n = 0.
- The value relation H = F - C_0.
- Separation between computing a difference and admitting it as suitable haze.

### Change / Reject

- Declaring every residual acceptable haze merely because it can be subtracted.
- Selecting a bound, a distribution, or a no-reproducible-structure criterion inside this inward definition.
- Moving an unexpanded known tail into haze.

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
- contribution_n

These are required daughter mentions for the proposed entry, including a
recursive occurrence where listed. Their placement may involve a conditional
demand rather than evaluation of every daughter in advance.

**Other headword mentions / surrounding entries:** P-FS4 is the unfinished outward haze wall. P-I1 defines the explicit contribution's recursive expansion.

### Forbidden Headword Mentions / Hidden Imports

- A tolerance supplied secretly by the residual.
- A concrete missing-force identity inferred from the difference alone.
- A partial contribution substituted for C_0 without its remaining tail.

### Question Or Trace Moment

What haze would be required for this explicit account to agree with the addressed net force?

### Witness Kind And Explicit Bindings

**Witness kind:** material-object force-accounting commitment and its stated approximation context.

**Slots read:**

- Target p and account/context κ.
- The net-force vector or constraint.
- Total contribution_n at n = 0, preserving any unresolved tail.

**Slots written / exposed:**

- The required haze difference, with its input provenance.
- A separate unresolved demand for peripheral admissibility when that question is asked.

### Boundary Behaviour

- Unknown F or C_0 leaves a symbolic relation or missing demand.
- Incompatible addresses/qualifications cannot be subtracted for this account.
- A computed difference may conflict with an independently supplied haze constraint. That is incompatibility of the account's joint commitments, not a license to enlarge haze automatically.

### IRIL — Ideal Residually Imparted Logic

**Allowed:**

- Expose F and C_0 for the same target/account and take their vector difference.
- Retain any dependencies when the two inputs carry uncertainty.
- With a partial expansion C_0 = f_0 + C_1, retain H = F - (f_0 + C_1).
- Route admissibility questions to the outward haze content rather than asserting acceptance here.

**Blocked:**

- Identifying the computed residual with a particular omitted interaction.
- Calling a difference small or random without a supplied criterion.
- Discarding C_1 and naming F - f_0 as the haze of the original account.
- Treating an algebraically forced fit as independent confirmation.

**Trace consequence:** The corner exposes net force and contribution at zero, then their difference. The trace may determine a required H while still lacking the grounds for treating that value as admissible haze.

### IRIEs — Ideal Residually Imparted Effects

**Reader/modeler behaviour to install:**

- Ask separately what haze is required and whether the account permits it.
- Keep the explicit account fixed while comparing its implied haze.

**Anti-habit / anti-misread:**

- A remainder is not automatically harmless error.
- Changing the explicit account changes the corresponding haze question.

### Suggested Wording

The subtraction itself is sufficient inward wording. Its admissibility distinction belongs in the packet's effects and at P-FS4, not as an extra inward daughter.

### Draft Entry

Provisional human-facing candidate:

```text
haze[p,κ] :=
    net-force-material-object[p,κ]
    minus (contribution_n[p,κ; n] where n = 0).
```

### Residual Design And Provenance

Working handle: `Res_P_FS3(net-force-material-object, contribution_n where n = 0)`.

The handle belongs to this packet's entry; it is not a globally shared
operation or a settled E-number. This is a dependency/demand sketch. Conditional
or index-dependent demands are exposed after their bindings are available,
not evaluated eagerly merely because they appear in the sketch.

| Residual phrase / operation | Provenance and permitted work |
|---|---|
| minus | Vector difference of the two daughter quantities. |
| where n = 0 | Selects the total explicit contribution, not an arbitrary tail. |
| Parenthesized contribution | Preserves the whole expanded expression when subtraction is distributed. |

## DEEP AUDIT ADD-ON

### Role Test

Exactly the other two Force-Sum headwords are exposed. P-FS4 remains necessary for peripheral meaning; this packet does not reduce that wall to an unrestricted residual.

### Worked Semantic Checks

These are desk checks of the proposed meaning, not engine executions or
physical validation. The examples use exact vectors in one common frame;
they do not impose an uncertainty model.

| Situation | Required consequence / limit |
|---|---|
| F = (5,2,0), C_0 = (4,3,0) N | H = (1,-1,0) N. |
| C_0 = f_0 + C_1 | H = F - f_0 - C_1, not F - f_0. |
| Independent wall input requires H = 0, but the difference is nonzero | The commitments disagree; this entry cannot redefine the wall input. |
| F = C_0 | H = 0 for this account; no unique interaction inventory or mechanical closure follows. |

### Open Questions

1. The P-FS4 contract and how its admissibility is expressed.
2. How uncertainty/dependence is represented across the two determinations.
3. Final call/binder syntax; no new generic subtraction engine rule is adopted here.

### Related Packets

- [P-FS1: Net Force Through Contribution And Haze](ENTRY_PACKET_P_FS1_NET_FORCE.md)
- [P-FS2: Total Contribution](ENTRY_PACKET_P_FS2_TOTAL_CONTRIBUTION.md)
- [P-I1: Recursive Contribution](ENTRY_PACKET_P_I1_RECURSIVE_CONTRIBUTION.md)
