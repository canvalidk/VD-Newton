# Entry Packet: P-O2 — Canonical Force From An Addressed Impressed Force

Status: substantive candidate packet, written 2026-11-17. Candidate wording is
included for review; it is not installed in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.
This packet belongs exclusively to the orientation-based alternative. It does
not settle the choice between that house and Action–Reaction.

## ENTRY PACKET

**Entry id:** [P-O2] — temporary ledger address.

**Headword:** `canonical-force_acting-object`.

**Status:** candidate — alternative house only.

**Role:** triplet-winter in the alternative evaluation house.

**Law/block:** Orientation-based evaluation (provisional name).

### Source Status And Lineage

Candidate inverse of the source's oriented evaluation relation, placed in the 17 November alternative ledger. The inverse spelling and auxiliary determination argument below are drafting proposals.

Source hierarchy: the user's 17 November naming correction and approved packet
selection; the current entry ledger; the source decisions and their stated
grades; then the packet template as an authoring scaffold. Candidate deductions
and interface choices below are not promoted to user rulings.

- [Entry structure at the authoring snapshot](https://github.com/canvalidk/VD-Newton/blob/19990f826e31d60376eab1080cdc1f0f64172154/07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md).
- [Packet template](../../04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md) and [editing rules](../EDITING_RULES.md).
- [Canonical-force orientation](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/Newton-analysis/criticism_history/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md), §§1–3 and 7–10.
- [Member-named force-law direction](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/Newton-analysis/criticism_history/participant_symmetric_canonical_orientation/VD_PARTICIPANT_SYMMETRIC_CANONICAL_ORIENTATION_MESHING_d2.md), Part IX.
- [8 November entry synthesis](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/inbox/NEWTON_ENTRY_STRUCTURE_SYNTHESIS_2026-11-08.md), §§9.3 and 10.2.

All managed source links use **VD-docs@90383f7dfa8225e8b5496d7b3d795e13cbff3151**. The
entry-production snapshot is **VD-Newton@19990f826e31d60376eab1080cdc1f0f64172154**. Older
sources use “contribution law” for the current Force-Sum law and “Force-Sum”
for the current Interaction law.

### Plain Purpose

Recover or constrain the quoted canonical vector using a participant's impressed force and the declared quoted-member convention.

### Preserve

- The same canonical quantity for one interaction/context, whichever participant provides the determination.
- The supplied orientation, including distinct participant identities.
- An explicit identity for the participant whose impressed force is used.

### Change / Reject

- Choosing the convention from the sign of a measured vector.
- Treating different source participants as different canonical-force identities.
- Introducing an independently valued reaction force as an additional daughter.
- Inferring a global force value from an acting-object name alone.

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

- impressed-force
- canonical-force-orientation

These are required daughter mentions for the proposed entry, including a
recursive occurrence where listed. Their placement may involve a conditional
demand rather than evaluation of every daughter in advance.

**Other headword mentions / surrounding entries:** The concrete quoted force's outward grounding remains P-O4. The unfinished orientation inverse is P-O3; neither is completed by this packet.

### Forbidden Headword Mentions / Hidden Imports

- A hidden choice of which impressed-force value to use.
- A third daughter for action-force or reaction-force from the competing house.
- Automatic independence of determinations made from the two participants.

### Question Or Trace Moment

Given this participant's impressed force, what canonical vector does the declared convention require?

### Witness Kind And Explicit Bindings

**Witness kind:** binary interaction, chosen source participant, and a declared orientation.

**Slots read:**

- Interaction i and context κ, retaining the same quoted-member convention.
- A supplied participant p used for this inward determination.
- impressed-force[i,p,κ].
- Orientation content exposing participants a,b and the quoted recipient c.

**Slots written / exposed:**

- The canonical vector K(i,κ) constrained or obtained through that participant.
- The source-participant and convention provenance of the determination.

### Boundary Behaviour

- The source p must belong to the declared pair; a nonparticipant cannot determine K through this entry.
- A missing/invalid orientation prevents choosing the branch even if the numerical force is known.
- An unbound impressed force leaves K symbolic/unbound.
- If the two participant determinations disagree under the declared pair model, retain the incompatibility; do not create two canonical forces to accommodate it.

### IRIL — Ideal Residually Imparted Logic

**Allowed:**

- For a canonical-recipient impressed force f, set K = f.
- For the other participant's impressed force f, set K = -f.
- Preserve the identity of K across either determination route.
- Compare two independently obtained target-side determinations with their dependencies and qualifications intact.

**Blocked:**

- Selecting or changing c to obtain the desired answer.
- Inferring orientation from K = f = 0.
- Treating P-O1's own output fed back here as an independent confirmation.
- Using a force from another interaction that happens to have the same numerical value.

**Trace consequence:** An explicitly chosen participant supplies the addressed impressed-force demand. The orientation says whether to preserve or negate that vector. Both legitimate recipient routes address the same K, although their input provenance differs.

### IRIEs — Ideal Residually Imparted Effects

**Reader/modeler behaviour to install:**

- Name whose impressed force is being used before applying the inverse.
- Keep the quoted force's recipient convention fixed during comparison.

**Anti-habit / anti-misread:**

- The same quoted quantity may have several determination routes without becoming several quantities.
- An inverse calculation does not prove either the chosen convention or the physical pairing premise.

### Suggested Wording

Make the source participant visible as an auxiliary determination argument. “using p” below does not make p part of a different canonical-force identity; final argument/lookup syntax remains open.

### Draft Entry

Provisional human-facing candidate:

```text
canonical-force_acting-object[i,κ; using p] :=
    let (a,b;c) be the participant pair and canonical recipient
        exposed by canonical-force-orientation[i,κ];
    if p = c, impressed-force[i,p,κ];
    if p is the other member of (a,b),
        minus impressed-force[i,p,κ];
    otherwise, inapplicable.
```

### Residual Design And Provenance

Working handle: `Res_P_O2(impressed-force, canonical-force-orientation; using p)`.

The handle belongs to this packet's entry; it is not a globally shared
operation or a settled E-number. This is a dependency/demand sketch. Conditional
or index-dependent demands are exposed after their bindings are available,
not evaluated eagerly merely because they appear in the sketch.

| Residual phrase / operation | Provenance and permitted work |
|---|---|
| using p | Explicit auxiliary selection of the source participant for this determination of K(i,κ); not a new physical identity key. |
| (a,b;c) / branch | Same proposed orientation interface as P-O1, not a separately invented recipient choice. |
| minus | Vector negation on the noncanonical participant branch. |
| Repeated i, κ | Preserves the same interaction and convention-qualified context. |

## DEEP AUDIT ADD-ON

### Role Test

The only daughter headwords are impressed-force and canonical-force-orientation. The source participant is an explicit auxiliary binding. How a generic canonical-force demand acquires that binding, and how it is kept distinct from quantity identity, remain open execution/interface questions.

### Worked Semantic Checks

These are desk checks of the proposed meaning, not engine executions or
physical validation. The examples use exact vectors in one common frame;
they do not impose an uncertainty model.

| Situation | Required consequence / limit |
|---|---|
| c = a, force on a = (3,-2,0) N | K = (3,-2,0) N. |
| c = a, force on b = (-3,2,0) N | K = (3,-2,0) N through the other participant. |
| Under c = a, supplied forces on a and b are both (3,-2,0) N | The two implied canonical vectors disagree; the joint pair account is incompatible. |
| Zero force on a valid participant, orientation supplied | K = 0; this does not recover an otherwise missing convention. |
| Force was produced by P-O1 from K | The round trip restores K algebraically; it is not independent evidence. |

### Open Questions

1. Final spelling and selection mechanism for the auxiliary source-participant binding.
2. Whether the orientation daughter itself supplies all participant bindings or another prior declared relation is needed; hidden access is not acceptable.
3. Concrete canonical-force wall content and naming.
4. The alternative-house choice and P-O3's underdetermined inward orientation relation.

### Related Packets

- [P-O1: Impressed Force Under A Declared Orientation](ENTRY_PACKET_P_O1_ORIENTED_IMPRESSED_FORCE.md)
- [P-I3: Impressed Force From Adjacent Contributions](ENTRY_PACKET_P_I3_IMPRESSED_FORCE.md)
