# VD Newton Project Guidance

## Project responsibility

This workspace is the Newton entry-production surface. Its primary job is to
translate managed VD context and analysis into entry packets, actual Newton
entries, and trace/evaluator checks. It does not own the organization or
maintenance of the NML document collection.

## Repository access and boundaries

The private GitHub repository `canvalidk/VD-Newton` is the backing repository
for this workspace. Its local `origin` points there, and the installed GitHub
connector has confirmed read/write access. Use that repository for normal
workspace commits and pushes, while still verifying the current remote and
authentication before a write.

`VDfirst/` is a separate local checkout of `canvalidk/VDfirst`. It is excluded
from VD-Newton and must not be staged, committed, or pushed as part of this
workspace. Do not write or push to `canvalidk/VDfirst` unless the user explicitly
asks for work on that repository.

Repository access does not change the context boundary below:
`canvalidk/VD-docs` remains the managed-context authority, while VD-Newton owns
the active Newton entry-production surface.

## VD-docs is the managed-context authority

The private GitHub repository `canvalidk/VD-docs` is the default source for VD
document discovery and current **managed** context. Use the installed GitHub
connector to read it. VD-docs is not necessarily exhaustive: this workspace
may contain active or newly created notes that have not yet been submitted to
the VD Folders inbox or organized into the managed collection.

For requests such as "find the document", "what have we said about X?", "tell
me everything pertaining to X", or other VD context/analysis questions:

1. Consult `canvalidk/VD-docs` automatically rather than assuming the answer
   must be found locally. Also inspect active local material when completeness,
   recency, or unsubmitted work may matter.
2. Treat `catalog.yaml` as the inventory and organization authority for the
   managed collection. Absence from the catalog is not evidence that no local
   or not-yet-ingested document exists.
3. For substantive work, resolve one `main` commit and read all task sources at
   that commit so the context is a coherent snapshot.
4. Fetch only the relevant canonical files and follow their `informs` links,
   source references, and context-bundle references as needed.
5. For broad or exhaustive synthesis, distinguish managed/current,
   managed/historical, inbox/unclassified, and local active/unsubmitted
   material. Report the commit, local scope, files inspected, search terms or
   selection method, and any coverage limitations.

Do not assume local NML, Newton-analysis, or Theory copies are current merely
because they are easier to access: they may be historical snapshots. Do not
assume they are stale merely because VD-docs has no matching record either:
they may be newer or unsubmitted. Determine and report their relationship. If
the GitHub connector is unavailable, say so and label the managed-context
coverage as unverified.

## Local authority and agency

Use local files first for active implementation surfaces: entry packets,
current Newton entry drafts, engine/code, trace tests, evaluator work, and
quick scoped changes needed to advance entry production.

Managed VD-docs context is read-only by default. Do not reorganize, rename,
deduplicate, refresh, or edit NML/context/informing documents in VD-docs unless
the user explicitly asks. Record important conflicts, stale sources, entry
decisions, and newly discovered dependencies as a handoff to the VD folders
manager instead.

Do not delete, archive, or demote a local document solely because a copy exists
in VD-docs. First establish whether the local file is historical, current,
unsubmitted, or divergent and whether the managed copy has actually absorbed
its content.

When an entry task consumes VD-docs context, record the repository commit and
source paths in the entry packet or handoff. Store locally the entry-facing
interpretation and decisions, not another maintained copy of the source
collection.

## Outbound handoffs to VD-docs

User policy established 2026-09-05: save new records and handoff documents
intended for VD-docs in the workspace-root folder `pass to VD-docs/`.
This is the local staging location for documents awaiting transfer to the
managed collection. Keep their source references and submission status in
the document; saving there does not itself mean VD-docs has received it.

Active entry packets, drafts, engine/code, and evaluator work remain on their
normal production surfaces. Apply this handoff policy to new documents and
documents the user identifies for transfer; do not bulk-move historical
handoffs solely because the new policy exists.

## 2026-08-26 pass closed — 2026-09-05

Applied the VD-docs checklist returned 2026-09-02 and re-issued 2026-09-05.
The returned checklist and the user's instruction authorize the managed copies
below, including the recorded terminology maps. The return was made against
the VD-docs working tree; no managed commit was supplied. Links use `main`.
This is a custody/deletion record, not a fresh content comparison.

All 13 Delete rulings are applied. Ten originals were deleted in this closure;
rows 3, 5 and 6 were already absent. The source column below is a historical
deletion ledger, not a list of local files to read.

| Row | Former local original | Disposition | Authoritative VD-docs copy |
|---:|---|---|---|
| 1 | `06_newton_analysis/abstract_interaction_candidate.md` | Deleted 2026-09-05 | [VD-docs: Newton-analysis/abstract_interaction_candidate/abstract_interaction_candidate_d1.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/abstract_interaction_candidate/abstract_interaction_candidate_d1.md) |
| 2 | `06_newton_analysis/newton_first_law_article.md` | Deleted 2026-09-05 | [VD-docs: Newton-analysis/newton_first_law_article.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/newton_first_law_article.md) |
| 3 | `06_newton_analysis/newton_vs_gibbs.md` | Already absent; Delete confirmed | [VD-docs: Newton-analysis/newton_vs_gibbs/newton_vs_gibbs_d1.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/newton_vs_gibbs/newton_vs_gibbs_d1.md) |
| 4 | `06_newton_analysis/nothing_vs_zero_somethings.md` | Deleted 2026-09-05 | [VD-docs: Newton-analysis/nothing_vs_zero_somethings/nothing_vs_zero_somethings (2)_d1.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/nothing_vs_zero_somethings/nothing_vs_zero_somethings%20%282%29_d1.md) |
| 5 | `06_newton_analysis/prediction_sets.md` | Already absent; Delete confirmed | [VD-docs: Theory/actually_there_prediction_sets/prediction_sets.md](https://github.com/canvalidk/VD-docs/blob/main/Theory/actually_there_prediction_sets/prediction_sets.md) |
| 6 | `06_newton_analysis/randomness_declarative_boundary.md` | Already absent; Delete confirmed | [VD-docs: Newton-analysis/randomness_declarative_boundary.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/randomness_declarative_boundary.md) |
| 7 | `06_newton_analysis/STATIC_ELECTRIC_ACTING_OBJECT_RESULT_2026-08-19.md` | Deleted 2026-09-05 | [VD-docs: Newton-analysis/_dscn_acting_object_primitives/STATIC_ELECTRIC_ACTING_OBJECT_RESULT_2026-08-19_d1.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/_dscn_acting_object_primitives/STATIC_ELECTRIC_ACTING_OBJECT_RESULT_2026-08-19_d1.md) |
| 8 | `06_newton_analysis/vd_composition_discovery_note.md` | Deleted 2026-09-05 | [VD-docs: Newton-analysis/composition_discovery/vd_composition_discovery_note_d1.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/composition_discovery/vd_composition_discovery_note_d1.md) |
| 9 | `06_newton_analysis/vd_design_3_newton_i_correction.md` | Deleted 2026-09-05 | [VD-docs: Newton-analysis/vd_design_3_newton_i_correction.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/vd_design_3_newton_i_correction.md) |
| 10 | `07_design_2_1/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md` | Deleted 2026-09-05 | [VD-docs: Newton-analysis/_dscn_entry_structure/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/_dscn_entry_structure/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md) |
| 12 | `07_design_2_1/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md` | Deleted 2026-09-05 | [VD-docs: Newton-analysis/_dscn_entry_structure/force_sum_member_value/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/_dscn_entry_structure/force_sum_member_value/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md) |
| 13 | `08_nm_lesson_drafts/nml1/NM_L1_E7_E8_decision_note.md` | Deleted 2026-09-05 | [VD-docs: Newton/nml/nml1/NM_L1_E7_E8_decision_note.md](https://github.com/canvalidk/VD-docs/blob/main/Newton/nml/nml1/NM_L1_E7_E8_decision_note.md) |
| 14 | `08_nm_lesson_drafts/nml1/NM_L1_E7_integrated_complete_draft.md` | Deleted 2026-09-05 | [VD-docs: Newton/nml/nml1/NM_L1_E7_integrated_complete_draft_d2.md](https://github.com/canvalidk/VD-docs/blob/main/Newton/nml/nml1/NM_L1_E7_integrated_complete_draft_d2.md) |

All six Keep originals remain unchanged:

- Row 11: `07_design_2_1/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` — UNDECIDED; both sides hold.
- Row 15: `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02.md` — UNDECIDED; both sides hold.
- Row 16: `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md` — steering.
- Row 17: `08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md` — steering.
- Row 18: `08_nm_lesson_drafts/nml3/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md` — UNDECIDED; both sides hold.
- Row 19: `08_nm_lesson_drafts/nml3/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md` — UNDECIDED; both sides hold.

No Keep document was reconciled or merged. The Design-3 steering copy at
`05_design_3_catchup/RANDOMNESS_DECLARATIVE_BOUNDARY.md` also remains unchanged.
The completed `pass to folders/2026-08-26/` bundle, including its original and
returned checklists, was deleted. This is the surviving closure record.
The separate 2026-09-05 receipt batch in `pass to VD-docs/` is outside this
08-26 cleanup and remains unchanged.

Local source references now point to the returned VD-docs paths. The user
explicitly authorized changing only the two source references in the E5
inertial-frame entry packet. All other packet content, passes, engine and
evaluator work remain unchanged.
