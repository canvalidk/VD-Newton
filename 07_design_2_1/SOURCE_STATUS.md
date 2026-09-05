# Design 2.1 Source Status

This file records which notes should steer Design 2.1.

## Primary Source For This Branch

| Source | Status | Use |
|---|---|---|
| `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md` | Ratified Force-Sum triplet naming authority | Use `net-force / impressed-force / interaction-set`. The interaction set contains interactions; each supplies a target-directed impressed force; net force is their vector sum. This settles names and the minimum typed relation only, not numbering, walls, closure machinery, or the remaining cut. |
| `07_design_2_1/DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md` | Confirmed structural bug authority | Use to prevent an aggregate constraint from being reused as an individual membership predicate. It leaves the E13-and-later structure under correction without invalidating completed NML2 work. |
| `07_design_2_1/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` | Adopted abstraction-boundary reasoning | Use for the identity/value and construction/aggregation distinctions. Translate its historical `IFS` to `interaction-set` and `V(f)` to the target-directed `impressed-force` supplied by interaction `i`; its provisional names do not override the 2026-08-26 decision. |
| [VD-docs: Newton-analysis/_dscn_entry_structure/force_sum_member_value/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/_dscn_entry_structure/force_sum_member_value/FORCE_SUM_TRIPLET_IFS_VALUE_RELATIONAL_NECESSITY_2026-08-18.md) | Managed relational rationale; historical filename | Use for the requirement that Force-Sum remain orientable around an unknown individual contribution. Apply the 2026-08-26 names: the indexed domain is `interaction-set`, and the contribution is `impressed-force`. It does not reinstate the retired E13–E17 numbering. |
| [VD-docs: Newton-analysis/_dscn_entry_structure/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/_dscn_entry_structure/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md) | Active downstream discovery note | Use for the result that equal-and-opposite pairing does not select a canonical recipient or quoted force. The canonical-orientation convention is a genuine runtime input behind the target-directed `impressed-force`, while the sign branch is derived. |
| `07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md` | Active output draft | Use as the current written output of the Design 2.1 entry-drafting effort. |
| `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md` | Working ledger | Edit this as the Design 2.1 entry structure. |
| `07_design_2_1/CURRENT_STATE.md` | Current branch orientation | Use to remember why Design 2.1 exists. |
| `07_design_2_1/SCOPE.md` | Scope boundary | Use to prevent Design 3 from expanding back into the branch. |
| `07_design_2_1/EDITING_RULES.md` | Practical editing guide | Use while revising entries. |
| `07_design_2_1/notes/conversation_captures/CONVERSATION_ENTRY_CONSIDERATIONS_2026-05-14.md` | Fresh conceptual capture | Use for proposed wall wording, induced-behaviour notes, asymmetrical force commitments, gravity/electrical halving, and mechanical-composition list gaps. |
| `07_design_2_1/notes/kinematics/KINEMATIC_ENTRY_CANDIDATES.md` | Working kinematic gap list | Use when adding Design 2 scaffold entries and optional extra kinematic constructs. |
| `07_design_2_1/notes/kinematics/KINEMATIC_ENTRIES_FINAL_NOTES.md` | Agreed kinematic notes | Use as the main guide for editing kinematic rows in the Design 2.1 ledger. |
| `07_design_2_1/entry_writing_passes/` | Active local drafting evidence | Use for the E8-E11 wording rationale and contested packet decisions. The 2026-08-01 `_b` E10 pass and 2026-08-02 E11 pass support the strings now used in the active draft. These are local active/unsubmitted files, not managed-context copies. |
| `07_design_2_1/notes/vd_docs_handoffs/why_the_mass_entry_must_be_long_joint_measurement_d3.md` | Current E10 analytical handoff | Governing source for the current E10 d4 packet. Intended as VD-docs `vector_division_mass_estimation` d3: fully supersedes the unnumbered short-entry argument, supersedes d2's measured-vector interpretation, and preserves d1's estimator mathematics plus d2's exact analysis. Drafted against VD-docs commit `8e09dbf9d3e521cbe76e36426ead656c04a71650`. |
| `07_design_2_1/entry_packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d4.md` | Latest E10 packet stored locally | Applies the independent-measurement / joint-fit correction: every empirical determination takes the joint branch, measurement results remain distinct from latent fitted values, and the joint result retains the original measurements, residual, uncertainty, policy, and provenance. The active E10 string has since advanced through `entry_writing_passes/E10_ENTRY_WRITING_PASS_2026-08-01_b.md`, whose declared source context includes d5; d5 is not stored here. |
| `07_design_2_1/entry_packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d3.md` | Superseded pre-correction packet | Retain as the packet state before the independent-measurement versus joint-estimate distinction was completed. Its exact branch remains incorporated into d4; its alignment-gated measured branch and bare mass-estimate result do not. |
| `07_design_2_1/entry_packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d2.md` | Superseded working packet | Preserve as the reasoning state that exposed the mass-estimation defect. Do not use its direction-tolerance/magnitude-floor treatment or its short E10 wording as current guidance. |
| `07_design_2_1/notes/lesson_entry_notes/ENTRY_WRITING_PASS_INTAKE_2026-07-26.md` | Intake and integration record | Use for provenance, applied changes, unresolved decisions, and the VD folders handoff. |
| `08_nm_lesson_drafts/nml3/NML3_ENTRY_SEQUENCE_DECISION_2026-08-02.md` | Retired-cut numbering record | Read as historical evidence for the old E13–E17 allocation. The managed NML3 reset of 2026-08-17 retired that cut and left replacement numbering open. |
| `08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md` | Ratified word choice; role refined 2026-08-26 | `impressed-force` remains the sole active replacement for predecessor force names. Its current Force-Sum role is the target-directed contribution supplied by an interaction, as governed by the 2026-08-26 triplet decision. |
| `08_nm_lesson_drafts/nml3/NML3_CONTRIBUTING_FORCE_TERMINOLOGY_DECISION_2026-08-02.md` | Superseded historical tombstone | Do not use as active context. It exists only to redirect readers to the 2026-08-12 authority and to prevent its former provisional instruction from being revived. |
| `08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02.md` | Current NML3 conceptual starting note | Records the force-sum lesson goal, the five construction hurdles, and the critical rule that an algebraic decomposition of net force does not establish force-account membership. Its naming question is resolved by the 2026-08-12 authority. |

## Design 3 Sources To Keep Nearby

| Source | Status | Use |
|---|---|---|
| `DESIGN_3_ENTRY_STRUCTURE.md` | Parent ledger | Compare when unsure what was inherited. |
| `05_design_3_catchup/CURRENT_STATE.md` | Current Design 3 synthesis | Trust for Newton I correction, acting-object architecture, and force accounting principles. |
| `05_design_3_catchup/DESIGN_3_GOALS.md` | Design 3 goal list | Use to identify what is being deferred or reduced. |
| `05_design_3_catchup/SOURCE_STATUS.md` | Design 3 source map | Use when a Design 3 claim needs provenance. |
| `05_design_3_catchup/WITNESS_SHEETS.md` | Deferred machinery | Use only as background; do not require full implementation in Design 2.1. |
| `05_design_3_catchup/OBJECT_COP_OUT.md` | Deferred machinery boundary | Use to justify leaving witness-sheet operations trace-side for now. |

## Core VD Sources

| Source | Status | Use |
|---|---|---|
| `00_read_first/VD_CORE_MODEL_HANDLE_RESIDUAL.md` | Current core orientation | Trust for answer-plus-trace and residual-handle vocabulary. |
| `04_entry_design_guides/vd_entry_writing_best_practices_handle_residual.md` | Entry-writing guide | Use when cleaning language. |
| `04_entry_design_guides/vd_six_entry_structure.md` | Entry-block guide | Use when checking chimney/triplet/wall roles. |
| `03_trace_and_evaluator/vd_trace_level2_v3.md` | Trace style reference; Force-Sum segment predates 2026-08-26 | Use for lazy demand and blocked-thunk style. Do not use its old impressed-force-element set model as naming or semantic authority. |

## Historical Or Deferred Sources

| Source | Status | Use |
|---|---|---|
| [VD-docs: Newton-analysis/nothing_vs_zero_somethings/nothing_vs_zero_somethings (2)_d1.md](https://github.com/canvalidk/VD-docs/blob/main/Newton-analysis/nothing_vs_zero_somethings/nothing_vs_zero_somethings%20%282%29_d1.md) | Superseded on routing | Keep only the empty-list / zero-sum intuition. Do not revive `Nothing -> Newton I`. |
| `04_entry_design_guides/vd_spring_acting_object_working_brief_v1.md` | Later Design 3 work | Use only if a placeholder needs to name the future spring direction. |
| `04_entry_design_guides/vd_acting_object_entry_authoring_guide_plan_v1.md` | Later Design 3 work | Use as background for deferred acting-object clusters. |
