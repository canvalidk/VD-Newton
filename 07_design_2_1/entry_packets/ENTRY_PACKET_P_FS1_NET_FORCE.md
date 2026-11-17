# Entry Packet: P-FS1 — Net Force Through Contribution And Haze

Status: substantive candidate packet, written 2026-11-17. Candidate wording is
included for review; it is not installed in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.

## ENTRY PACKET

**Entry id:** [P-FS1] — temporary ledger address.

**Headword:** `net-force-material-object`.

**Status:** candidate — primary proposed continuation.

**Role:** triplet-November.

**Law/block:** Force-Sum.

### Source Status And Lineage

New inward Force-Sum candidate following the existing E9 grounding. E11 currently says “There are exactly two ways to obtain this vector.” Its scope must be reconciled before installation; this packet does not rewrite E11.

Source hierarchy: the user's 17 November naming correction and approved packet
selection; the current entry ledger; the source decisions and their stated
grades; then the packet template as an authoring scaffold. Candidate deductions
and interface choices below are not promoted to user rulings.

- [Entry structure at the authoring snapshot](https://github.com/canvalidk/VD-Newton/blob/19990f826e31d60376eab1080cdc1f0f64172154/07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md).
- [Packet template](../../04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md) and [editing rules](../EDITING_RULES.md).
- [11 November decisions](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/contribution_law_and_force_sum_decisions_2026-11-11.md), §§1–2.
- [12 November recursion](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/how_the_list_works_contribution_recursion_2026-11-12.md), §4.

All managed source links use **VD-docs@90383f7dfa8225e8b5496d7b3d795e13cbff3151**. The
entry-production snapshot is **VD-Newton@19990f826e31d60376eab1080cdc1f0f64172154**. Older
sources use “contribution law” for the current Force-Sum law and “Force-Sum”
for the current Interaction law.

### Plain Purpose

Express one material object's net force as haze plus its total explicit contribution, starting the contribution function at zero.

### Preserve

- The official net-force-material-object headword and common target/context.
- The two daughters haze and contribution_n.
- The explicit initialization n = 0 and one occurrence of haze outside the Interaction recursion.

### Change / Reject

- Replacing contribution_n with a new unagreed total-contribution headword.
- Silently setting haze to zero.
- Putting membership construction, concrete force formulas, or uncertainty tolerances inside this corner.

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

- haze
- contribution_n

These are required daughter mentions for the proposed entry, including a
recursive occurrence where listed. Their placement may involve a conditional
demand rather than evaluation of every daughter in advance.

**Other headword mentions / surrounding entries:** E9 is the earlier chimney. P-I1 supplies the recursive contribution route. P-FS4 owns haze's unfinished peripheral contract.

### Forbidden Headword Mentions / Hidden Imports

- interaction-set / impressed-force / acting-object as extra daughters: these belong behind contribution.
- An automatic claim that a numerically matching account is physically warranted.
- Mass or acceleration in this definiens: those belong to the earlier Newton-II route.

### Question Or Trace Moment

What net force does this explicit contribution and this haze assign to the target?

### Witness Kind And Explicit Bindings

**Witness kind:** material-object force-accounting commitment; testimony remains peripheral.

**Slots read:**

- Target p and account/context κ.
- Haze for that account.
- contribution_n for the same account with n set to zero.

**Slots written / exposed:**

- The addressed net-force relation/value H + C_0.
- The zero initialization and the provenance of both daughter demands.

### Boundary Behaviour

- A missing daughter remains a demand or symbolic term, not zero.
- Daughters with different targets, times, frames, or account choices cannot be added as this result.
- A bound/set for haze yields a corresponding constrained result, not a uniquely chosen vector. This packet installs no probability model or uncertainty-combination rule.

### IRIL — Ideal Residually Imparted Logic

**Allowed:**

- Expose haze[p,κ] and contribution_n[p,κ;n] with n explicitly set to zero.
- Add compatible supplied vectors, or retain their sum as a symbolic/constrained expression.
- Preserve a contribution tail when the Interaction expansion is partial.
- Keep dependencies between uncertain inputs; arithmetic rewriting is not independent evidence.

**Blocked:**

- Expanding haze as another member of the interaction list.
- Demanding a fresh haze at each recursive step.
- Using the result itself to establish the list's physical warrant.
- Following a closed cycle through P-FS2 or P-FS3 as though it generated missing information.

**Trace consequence:** The first line is H + C_0. One Interaction step produces H + f_0 + C_1. H remains once at the outside throughout, and every unfinished tail remains visible.

### IRIEs — Ideal Residually Imparted Effects

**Reader/modeler behaviour to install:**

- Start the contribution traversal deliberately at zero.
- Keep the explicit account and the haze qualification attached to one target.

**Anti-habit / anti-misread:**

- A net-force value does not identify which interactions exist.
- A supplied or inferred haze value does not certify that the haze wall's conditions hold.

### Suggested Wording

Prefer a visible “where n = 0” binder for the source's intended meaningful initialization. The direct call C_0 is an equivalent mathematical abbreviation, not an extra headword.

### Draft Entry

Provisional human-facing candidate:

```text
net-force-material-object[p,κ] :=
    haze[p,κ]
    plus (contribution_n[p,κ; n] where n = 0).
```

### Residual Design And Provenance

Working handle: `Res_P_FS1(haze, contribution_n where n = 0)`.

The handle belongs to this packet's entry; it is not a globally shared
operation or a settled E-number. This is a dependency/demand sketch. Conditional
or index-dependent demands are exposed after their bindings are available,
not evaluated eagerly merely because they appear in the sketch.

| Residual phrase / operation | Provenance and permitted work |
|---|---|
| plus | Ordinary vector addition of compatible daughter quantities. |
| where n = 0 | Sets the contribution counter at the trace start; final syntax remains open. |
| Repeated p, κ | Preserves the same account/context across daughters. |

## DEEP AUDIT ADD-ON

### Role Test

The entry faces inward through haze and contribution_n only. No list construction or concrete interaction appears in its residual. The surrounding house's unfinished walls do not prevent specifying this relation.

### Worked Semantic Checks

These are desk checks of the proposed meaning, not engine executions or
physical validation. The examples use exact vectors in one common frame;
they do not impose an uncertainty model.

| Situation | Required consequence / limit |
|---|---|
| H = (1,-1,0), C_0 = (4,3,0) N | F = (5,2,0) N. |
| An explicitly empty I makes C_0 = 0 | F = H; neither F = 0 nor free-particle status follows without further content. |
| C_0 = f_0 + C_1 | F = H + f_0 + C_1; one haze and one retained tail. |
| H is unbound | Keep the demand; do not turn the explicit contribution into an exact net-force prediction. |

### Open Questions

1. Final spelling of the zero initialization.
2. Whether E11's existing “exactly two ways” wording is compatible within its NML2.1 scope or needs revision.
3. Haze's peripheral admissibility contract; this entry must not settle it implicitly.

### Related Packets

- [P-FS2: Total Contribution](ENTRY_PACKET_P_FS2_TOTAL_CONTRIBUTION.md)
- [P-FS3: Haze As The Force-Sum Difference](ENTRY_PACKET_P_FS3_HAZE.md)
- [P-I1: Recursive Contribution](ENTRY_PACKET_P_I1_RECURSIVE_CONTRIBUTION.md)
