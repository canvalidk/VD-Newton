# Pass to Folders Checklist — 2026-08-26

This bundle is a non-destructive copy pass from VD-Newton to the VD folders
branch. The original local files remain in place.

Managed-context comparison was made against:

```text
canvalidk/VD-docs
commit 9cd795c0220480e897776b4492c7eb40478b7503
```

## Return instructions

For every row, inspect or ingest the bundled copy and then mark exactly one of
the two boxes in the final column:

- `Delete` means the corresponding original source file in VD-Newton may be
  deleted after this checklist is returned.
- `Keep` means the original must remain in VD-Newton.
- If neither box, or both boxes, are marked, VD-Newton will keep the original.
- Use the Notes column for required merges, corrections, renamed destinations,
  or conditions that must be satisfied before deletion.

The paths below are the original VD-Newton source paths. The bundle preserves
those paths beneath this checklist.

## Checklist

| # | Original VD-Newton source | Proposed managed home or action | Current managed relation | Local deletion ruling | Notes |
|---:|---|---|---|---|---|
| 1 | `06_newton_analysis/abstract_interaction_candidate.md` | Correct the existing Newton-analysis record; do not overwrite it blindly. | Managed copy exists at `Newton-analysis/abstract_interaction_candidate/abstract_interaction_candidate_d1.md`. The local conclusion uses `impressed force` where the managed copy uses `acting force`; both require review against the 2026-08-26 interaction/impressed-force distinction. | ☐ Delete / ☐ Keep | |
| 2 | `06_newton_analysis/newton_first_law_article.md` | Verify the managed Newton-analysis/Newton copies, then no new ingest should be needed. | Byte-equivalent after newline normalization to the managed `Newton-analysis/newton_first_law_article.md`; another managed copy exists in `Newton/newton_first_law_article.md`. | ☐ Delete / ☐ Keep | |
| 3 | `06_newton_analysis/newton_vs_gibbs.md` | Verify existing Newton-analysis record. | Equivalent to `Newton-analysis/newton_vs_gibbs/newton_vs_gibbs_d1.md`. | ☐ Delete / ☐ Keep | |
| 4 | `06_newton_analysis/nothing_vs_zero_somethings.md` | Verify existing Newton-analysis record. | Equivalent to `Newton-analysis/nothing_vs_zero_somethings/nothing_vs_zero_somethings (2)_d1.md`. | ☐ Delete / ☐ Keep | |
| 5 | `06_newton_analysis/prediction_sets.md` | Verify the existing Theory placement or redirect according to the folders branch's present ownership rule. | Equivalent to `Theory/actually_there_prediction_sets/prediction_sets.md`. | ☐ Delete / ☐ Keep | |
| 6 | `06_newton_analysis/randomness_declarative_boundary.md` | New folders-branch ingest; proposed home is Newton-analysis unless a more direct branch address governs it. | No catalogued managed copy found at the comparison commit. A second local working copy exists at `05_design_3_catchup/RANDOMNESS_DECLARATIVE_BOUNDARY.md`. | ☐ Delete / ☐ Keep | |
| 7 | `06_newton_analysis/STATIC_ELECTRIC_ACTING_OBJECT_RESULT_2026-08-19.md` | Verify existing Newton-analysis record; prefer the managed math-normalized version. | Substantively equivalent to `Newton-analysis/_dscn_acting_object_primitives/STATIC_ELECTRIC_ACTING_OBJECT_RESULT_2026-08-19_d1.md`; differences are math-delimiter normalization. | ☐ Delete / ☐ Keep | |
| 8 | `06_newton_analysis/vd_composition_discovery_note.md` | Verify existing Newton-analysis record. | Equivalent to `Newton-analysis/composition_discovery/vd_composition_discovery_note_d1.md`. | ☐ Delete / ☐ Keep | |
| 9 | `06_newton_analysis/vd_design_3_newton_i_correction.md` | Verify the existing Newton-analysis/Newton copies. | Equivalent to `Newton-analysis/vd_design_3_newton_i_correction.md`; another managed copy exists at `Newton/Design 3/vd_design_3_newton_i_correction.md`. | ☐ Delete / ☐ Keep | |
| 10 | `07_design_2_1/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md` | Merge the local 2026-08-26 Force-Sum naming translation into the managed Newton-analysis record. | Managed predecessor exists at `Newton-analysis/_dscn_entry_structure/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14_d1.md`; local lines 226–256 use the newer `interaction-set / impressed-force` formulation. | ☐ Delete / ☐ Keep | |
| 11 | `07_design_2_1/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` | Reconsider for Newton-analysis under the clarified analysis-ownership rule; exact placement is for the folders manager. | Previously handed out of VD-docs to VD-Newton by explicit decision. It is not a current managed record, although an original survives in the math-originals bank. This bundle is a proposed fresh return, not an instruction to overwrite history. | ☐ Delete / ☐ Keep | |
| 12 | `07_design_2_1/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md` | Merge the local 2026-08-26 terminology correction into the existing Newton-analysis record. | Managed predecessor exists at `Newton-analysis/_dscn_entry_structure/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18_d1.md`; the local copy translates `IFS / V(f)` to `interaction-set / impressed-force`. | ☐ Delete / ☐ Keep | |
| 13 | `08_nm_lesson_drafts/nml1/NM_L1_E7_E8_decision_note.md` | Update the managed Newton NML1 copy if the terminology change remains wanted. | Managed copy exists at `Newton/nml/nml1/NM_L1_E7_E8_decision_note.md`; the principal local difference is `impressed-force` versus the managed `attached-force`. | ☐ Delete / ☐ Keep | |
| 14 | `08_nm_lesson_drafts/nml1/NM_L1_E7_integrated_complete_draft.md` | Update the managed Newton NML1 draft if the terminology change remains wanted. | Managed copy exists at `Newton/nml/nml1/NM_L1_E7_integrated_complete_draft_d2.md`; the principal local difference is `impressed-force` versus the managed `attached-force`. | ☐ Delete / ☐ Keep | |
| 15 | `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02.md` | Compare and merge selectively into the managed NML3 conceptual record. | Managed record exists at `Newton/nml/nml3/conceptual/NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02.md`; local terminology and decision references are newer, while the managed copy participates in the 2026-08-17 reset structure. Do not overwrite wholesale. | ☐ Delete / ☐ Keep | |
| 16 | `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md` | New shared Newton/NML3 record, proposed at `Newton/nml/nml3/` beside the reset record. | No catalogued managed copy found. This is the ratified `net-force / impressed-force / interaction-set` decision produced in VD-Newton. | ☐ Delete / ☐ Keep | |
| 17 | `08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md` | Ingest or merge into Newton/NML3 with the 2026-08-26 role refinement preserved. | No catalogued managed copy found under this filename. It remains the local word-choice authority and now points to the new triplet decision. | ☐ Delete / ☐ Keep | |
| 18 | `08_nm_lesson_drafts/nml3/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md` | Merge the small terminology delta into the managed conceptual record if still valid. | Managed record exists at `Newton/nml/nml3/conceptual/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md`; the main local difference is `impressed-force` versus `warranted-force`. | ☐ Delete / ☐ Keep | |
| 19 | `08_nm_lesson_drafts/nml3/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md` | Perform a substantive comparison and selective merge before deciding custody. | Managed record exists at `Newton/nml/nml3/conceptual/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md`. The local copy contains later acting-object-key, action/reaction-exclusivity, generator, and closer material not present verbatim in the managed version. Do not overwrite wholesale or delete before reconciliation. | ☐ Delete / ☐ Keep | |

## Bundle-level confirmation

- ☐ All 19 bundled files were received and are readable.
- ☐ Every `Delete` ruling above has either an authoritative managed copy or a
  completed ingest/merge.
- ☐ It is safe for VD-Newton to apply the marked deletion rulings.

Returned by:

```text
name/branch:
date:
managed commit after processing:
```
