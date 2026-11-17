# Entry Packet: P-O1 — Impressed Force Under A Declared Orientation

Status: substantive candidate packet, written 2026-11-17. Candidate wording is
included for review; it is not installed in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.
This packet belongs exclusively to the orientation-based alternative. It does
not settle the choice between that house and Action–Reaction.

## ENTRY PACKET

**Entry id:** [P-O1] — temporary ledger address.

**Headword:** `impressed-force`.

**Status:** candidate — alternative house only.

**Role:** triplet-November; alternative Interaction wall.

**Law/block:** Orientation-based evaluation (provisional name).

### Source Status And Lineage

New candidate for the alternative house added to the ledger on 17 November. It competes with P-AR1 at the same impressed-force definition site; both are not installed consecutively.

Source hierarchy: the user's 17 November naming correction and approved packet
selection; the current entry ledger; the source decisions and their stated
grades; then the packet template as an authoring scaffold. Candidate deductions
and interface choices below are not promoted to user rulings.

- [Entry structure at the authoring snapshot](https://github.com/canvalidk/VD-Newton/blob/19990f826e31d60376eab1080cdc1f0f64172154/07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md).
- [Packet template](../../04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md) and [editing rules](../EDITING_RULES.md).
- [Canonical-force orientation](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/Newton-analysis/criticism_history/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md), §§1–3 and 7–10.
- [Member-named force-law direction](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/Newton-analysis/criticism_history/participant_symmetric_canonical_orientation/VD_PARTICIPANT_SYMMETRIC_CANONICAL_ORIENTATION_MESHING_d2.md), Part IX, §§24–26.
- [8 November entry synthesis](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/NEWTON_ENTRY_STRUCTURE_SYNTHESIS_2026-11-08.md), §10.

All managed source links use **VD-docs@90383f7dfa8225e8b5496d7b3d795e13cbff3151**. The
entry-production snapshot is **VD-Newton@19990f826e31d60376eab1080cdc1f0f64172154**. Older
sources use “contribution law” for the current Force-Sum law and “Force-Sum”
for the current Interaction law.

### Plain Purpose

Evaluate the force delivered to a target from the quoted canonical vector and an explicit recipient convention for one binary interaction.

### Preserve

- The distinction between interaction identity, force recipient, and numerical vector.
- An explicit declaration of which participant receives the quoted canonical vector.
- The nonparticipant branch: neither member applies.
- Value invariance when quoted recipient and quoted vector are both reversed.

### Change / Reject

- Interpreting “not canonical” as automatically meaning “the other participant.”
- Treating canonical force as an additional physical force.
- Inferring the participants or reciprocal occurrence from a sign flip.
- Installing a half-weighting convention or the two-owned-instance architecture by default.

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

- canonical-force_acting-object
- canonical-force-orientation

These are required daughter mentions for the proposed entry, including a
recursive occurrence where listed. Their placement may involve a conditional
demand rather than evaluation of every daughter in advance.

**Other headword mentions / surrounding entries:** P-I3 supplies earlier impressed-force grounding. Action–Reaction's separate candidate and the concrete member-named entries are design context, not additional daughter demands here.

### Forbidden Headword Mentions / Hidden Imports

- An implicit sign function with no declared convention behind it.
- A direct read of peripheral witness testimony to discover the recipient.
- A second reaction-force daughter: that would mix the competing house cuts.
- A default numerical zero for a nonparticipant.

### Question Or Trace Moment

Which member of this interaction's quoted equal-and-opposite pair acts on this target?

### Witness Kind And Explicit Bindings

**Witness kind:** one binary interaction and its explicitly bound participants/quoted-member convention.

**Slots read:**

- Interaction i, target p, and context κ.
- Canonical vector K for this same interaction and declared quotation convention.
- Orientation content exposing distinct participants a,b and canonical recipient c in {a,b}.

**Slots written / exposed:**

- The target's impressed-force value K or -K, or inapplicability for a nonparticipant.
- The specific recipient/convention branch used.

### Boundary Behaviour

- Unknown participants or canonical recipient leave the branch unresolved; noncanonical status alone is insufficient.
- A target outside the declared pair is inapplicable even when K = 0.
- An invalid declaration c outside the pair, coincident participant addresses, or incompatible contexts prevents this binary interpretation.
- Unbound K can remain symbolic after the recipient branch is known; it does not erase the structural pairing obligation.

### IRIL — Ideal Residually Imparted Logic

**Allowed:**

- Expose the orientation daughter and the quoted canonical-force daughter.
- Return K for the declared canonical recipient and -K for the other declared participant.
- Preserve the original interaction and activation bindings on either route.
- Carry a supplied convention's authority rather than treating a familiar formula's sign as self-explanatory.

**Blocked:**

- Returning -K for every object other than c.
- Inventing a counterpart's physical identity from the opposite vector.
- Conflating mechanism ownership with which force member is quoted.
- Counting the two members as two contributions of this same interaction on one participant.

**Trace consequence:** The orientation binds the target to one member. The quoted force is then retained or negated. A reciprocal occurrence and the suitability of the binary participant model remain structural premises; evaluation alone does not establish them.

### IRIEs — Ideal Residually Imparted Effects

**Reader/modeler behaviour to install:**

- Read both the quoted formula and its intended recipient.
- Check participant membership before choosing a sign.

**Anti-habit / anti-misread:**

- A familiar force formula does not by itself say who receives it.
- Negation is a value operation, not object discovery.

### Suggested Wording

Expose a convention that carries the pair and its quoted recipient. This is a proposed explicit interface for the orientation daughter, not a finished P-O5 definition.

### Draft Entry

Provisional human-facing candidate:

```text
impressed-force[i,p,κ] :=
    let (a,b;c) be the participant pair and canonical recipient
        exposed by canonical-force-orientation[i,κ];
    if p is neither a nor b, inapplicable;
    otherwise,
        let K be canonical-force_acting-object[i,κ];
        if p = c, K;
        otherwise, -K.
```

### Residual Design And Provenance

Working handle: `Res_P_O1(canonical-force_acting-object, canonical-force-orientation; p)`.

The handle belongs to this packet's entry; it is not a globally shared
operation or a settled E-number. This is a dependency/demand sketch. Conditional
or index-dependent demands are exposed after their bindings are available,
not evaluated eagerly merely because they appear in the sketch.

| Residual phrase / operation | Provenance and permitted work |
|---|---|
| (a,b;c) | Proposed projection of the orientation daughter's declared participant/recipient bindings. Pair existence is not inferred by this notation. |
| p = c / other member | Identity comparison on supplied bindings, with participant membership checked. |
| -K | Ordinary vector negation under the same coordinates and units. |
| inapplicable | No force of this interaction is delivered to that nonparticipant; not a zero-valued member. |

## DEEP AUDIT ADD-ON

### Role Test

Only canonical-force_acting-object and canonical-force-orientation are daughter headwords. The participant projection must be supplied explicitly by the second daughter's eventual content; otherwise this candidate has an unresolved hidden-input problem.

### Worked Semantic Checks

These are desk checks of the proposed meaning, not engine executions or
physical validation. The examples use exact vectors in one common frame;
they do not impose an uncertainty model.

| Situation | Required consequence / limit |
|---|---|
| a quoted, K = (3,-2,0) N | Force on a is (3,-2,0); force on b is (-3,2,0). |
| Quote b instead and set K' = (-3,2,0) N | Forces on a and b remain unchanged. |
| Reverse only K, keeping the quoted recipient | The physical target-side values change; this is not the equivalent convention reversal. |
| Third target d, K = 0 | Inapplicable, not a zero force member on d. |
| K unbound, pair known | Recipient branches are known; numerical values remain unbound. |

### Open Questions

1. Final name and outward contract of canonical-force-orientation, including how it carries participant bindings.
2. Whether canonical-force_acting-object is retained or aligned with the action-force vocabulary; no new physical quantity is intended.
3. Where reciprocal existence and participant-domain obligations are encoded if this alternative is chosen.
4. Exact choice between this house and Action–Reaction; candidate packets do not ratify the choice.

### Related Packets

- [P-O2: Canonical Force From An Addressed Impressed Force](ENTRY_PACKET_P_O2_CANONICAL_FORCE.md)
- [P-I3: Impressed Force From Adjacent Contributions](ENTRY_PACKET_P_I3_IMPRESSED_FORCE.md)
