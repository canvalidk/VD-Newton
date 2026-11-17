# Entry Packet: P-I1 — Recursive Contribution

Status: substantive candidate packet, written 2026-11-17. Candidate wording is
included for review; it is not installed in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.

## ENTRY PACKET

**Entry id:** [P-I1] — temporary ledger address.

**Headword:** `contribution_n`.

**Status:** candidate — primary proposed continuation.

**Role:** triplet-November; Force-Sum wall.

**Law/block:** Interaction.

### Source Status And Lineage

New candidate implementing the user's corrected single conditional. The 12 November record supersedes both the shrinking-set state and the suggestion of two dispatched definitions.

Source hierarchy: the user's 17 November naming correction and approved packet
selection; the current entry ledger; the source decisions and their stated
grades; then the packet template as an authoring scaffold. Candidate deductions
and interface choices below are not promoted to user rulings.

- [Entry structure at the authoring snapshot](https://github.com/canvalidk/VD-Newton/blob/19990f826e31d60376eab1080cdc1f0f64172154/07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md).
- [Packet template](../../04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md) and [editing rules](../EDITING_RULES.md).
- [12 November recursion](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/how_the_list_works_contribution_recursion_2026-11-12.md), §§1–8, 9.3 and 11.
- [11 November decisions](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/contribution_law_and_force_sum_decisions_2026-11-11.md), §§3–5, as corrected on 12 November.

All managed source links use **VD-docs@90383f7dfa8225e8b5496d7b3d795e13cbff3151**. The
entry-production snapshot is **VD-Newton@19990f826e31d60376eab1080cdc1f0f64172154**. Older
sources use “contribution law” for the current Force-Sum law and “Force-Sum”
for the current Interaction law.

### Plain Purpose

Expand the remaining explicit contribution by walking a fixed, already supplied numbered interaction set, or finish at its length with the additive zero.

### Preserve

- One conditional definition, tested at each expansion.
- A fixed numbered set I, length L, and indices 0 through L-1; only n changes.
- A surviving tail in every partial expansion.
- The exact zero vector as the terminal value, not as a stop test.

### Change / Reject

- The off-by-one comparison L > n+1.
- Building or shrinking I during this traversal.
- Dropping the tail, adding haze inside the recursion, or stopping because a force/sum happens to be zero.
- Treating an empty account as a Newton-I/free-particle routing instruction.

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
- impressed-force
- contribution_n (recursive self-reference at the next counter)

These are required daughter mentions for the proposed entry, including a
recursive occurrence where listed. Their placement may involve a conditional
demand rather than evaluation of every daughter in advance.

**Other headword mentions / surrounding entries:** net-force-material-object and haze occur in the surrounding Force-Sum house. Neither is a daughter of this definition.

### Forbidden Headword Mentions / Hidden Imports

- A hidden membership generator or no-more-elements question inside each iteration.
- A second zero-case definition selected outside the entry.
- A force-value equality used to decide whether two members have the same identity.

### Question Or Trace Moment

What explicit contribution remains from member n onward in this supplied account?

### Witness Kind And Explicit Bindings

**Witness kind:** fixed interaction-set and target-account commitment, supplied through explicit bindings.

**Slots read:**

- Target p and context κ, selecting the same account throughout.
- I = interaction-set[p,κ], supplied with length and a one-to-one numbering.
- A nonnegative integer counter; valid traversal starts at zero and reaches L.
- The addressed impressed force only when that numbered member exists.

**Slots written / exposed:**

- A member-force demand plus the next contribution demand, or the zero vector.
- The fixed account, counter transition, and condition used at each step.

### Boundary Behaviour

- An unknown length or unresolved numbering prevents deciding the branch/member; it does not justify the terminal zero.
- At n = L the condition is false: return zero without demanding member L or C_(L+1).
- Negative/noninteger counters are outside the proposed traversal domain. A directly supplied n > L is not reached by correct traversal; the literal conditional returns zero, but this is no certificate that the preceding steps were valid.
- A duplicated or inconsistent enumeration is an input/interface fault; the arithmetic does not repair it or prove physical admission.

### IRIL — Ideal Residually Imparted Logic

**Allowed:**

- Expose I's length and judge L > n before demanding either branch's quantities.
- When true, expose member n's impressed-force and contribution_n at n+1, with I, p, and κ preserved.
- When false, return zero; no member or further tail is demanded.
- Keep an unresolved tail explicitly if expansion stops early; do not require every force value to be numerical before writing the symbolic sum.

**Blocked:**

- Demanding a nonexistent member in the base case.
- A new physical-world claim in the comparison step.
- Changing I midway or adding one identity twice by re-spelling it.
- Using a mechanical zero to absorb haze or an unknown tail.

**Trace consequence:** Starting at zero yields f_0 + (f_1 + ... + (f_(L-1) + 0)). Every prefix retains its remaining contribution. Branch judgment, member selection, and increment are identifiable meaningful operations; their mechanical nature does not mean an interpreter cannot make a mistake.

### IRIEs — Ideal Residually Imparted Effects

**Reader/modeler behaviour to install:**

- Read the condition before pursuing a member demand.
- Keep the counter visible and the account fixed.
- Distinguish the physical no-more-elements claim from reaching the supplied length.

**Anti-habit / anti-misread:**

- Zero value does not mean no interactions.
- A partial true expression is not automatically a completed numerical prediction.

### Suggested Wording

Use the source's one conditional with a local binding for I. The next-call notation below is mathematical; it makes no claim that the current tokenizer evaluates n+1.

### Draft Entry

Provisional human-facing candidate:

```text
contribution_n[p,κ; n] :=
    let I be interaction-set[p,κ];
    if length(I) > n,
        impressed-force[member n of I, p,κ]
        plus contribution_n[p,κ; n+1];
    otherwise, (0,0,0).
```

### Residual Design And Provenance

Working handle: `Res_P_I1(interaction-set, impressed-force demand, next contribution_n demand; n)`.

The handle belongs to this packet's entry; it is not a globally shared
operation or a settled E-number. This is a dependency/demand sketch. Conditional
or index-dependent demands are exposed after their bindings are available,
not evaluated eagerly merely because they appear in the sketch.

| Residual phrase / operation | Provenance and permitted work |
|---|---|
| let I be ... | One local alias for the same exposed interaction-set; not a second changing set. |
| length(I) > n | Arithmetic comparison on supplied list structure, not a physical closure judgment. |
| member n / n+1 | Numbered lookup and increment under the fixed enumeration. |
| plus / (0,0,0) | Binary vector addition and its identity; compatible coordinates/units required. |

## DEEP AUDIT ADD-ON

### Role Test

The outward contribution definition is the Interaction November corner. It exposes interaction-set and impressed-force and recurs on the same contribution headword. The self-reference must remain explicit in the packet; its treatment by law/house detection remains unresolved.

### Worked Semantic Checks

These are desk checks of the proposed meaning, not engine executions or
physical validation. The examples use exact vectors in one common frame;
they do not impose an uncertainty model.

| Situation | Required consequence / limit |
|---|---|
| L = 0, n = 0 | Zero immediately; no impressed-force or next-tail demand. |
| One member f_0 = (3,0,0) N | C_0 = f_0 + C_1, C_1 = 0; includes the last member. |
| Members (3,0,0), (-3,0,0), (2,0,0) N | C_0 = (2,0,0) N; the cancelling first pair cannot stop traversal. |
| Stop after the first member | C_0 = f_0 + C_1 remains; replacing C_1 with zero is not licensed. |
| Enumeration contains one interaction twice | Any double count is a fault in the supplied enumeration; the recursion does not establish uniqueness. |

### Open Questions

1. The final argument grammar and how the next counter is represented.
2. How branch selection prevents unused member/tail demands in the engine.
3. Where interaction identity and numbering are grounded by P-I4.
4. How recursive self-reference is represented by the law graph.
5. The 12 November probe used supplied next calls, recorded increments as inputs, and left comparisons unchecked; these implementation issues are not resolved by this wording.

### Related Packets

- [P-FS2: Total Contribution](ENTRY_PACKET_P_FS2_TOTAL_CONTRIBUTION.md)
- [P-FS1: Net Force Through Contribution And Haze](ENTRY_PACKET_P_FS1_NET_FORCE.md)
- [P-I3: Impressed Force From Adjacent Contributions](ENTRY_PACKET_P_I3_IMPRESSED_FORCE.md)
