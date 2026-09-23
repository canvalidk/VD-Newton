# VD Newton Project Guidance

## Human-facing spaces and working artifacts — user preference, 2026-09-08

The normal VD-Newton and VD-docs document areas are the user's curated,
human-readable spaces. Keep internal working artifacts in a clearly separate
scratch area, such as the workspace's `.tools/` directory. Scripts, logs,
probes, machine outputs, and scratch notes may be created there as needed to
complete authorized work; they do not each require an explicit request.
This is a boundary between the user's document collection and the agent's
working materials, not a ban on artifacts or a requirement to run checks only
in memory. Do not routinely add companion reports or experiment bundles to
the human-facing collection. Discuss exploratory ideas in the conversation
without turning each discussion into another document. Requested production
code, entry work, and necessary verification belong on their appropriate
production surfaces.
In VD-docs, a record is a specific document kind. The user decides when a
record is written. Do not independently create or label documents as records,
or create files merely to fit the document organization. Entry packets are
also a specific authoring format; implementation notes are not entry packets.
The record-keeping and handoff guidance below governs user-requested documents;
it is not a standing request to turn each discussion or experiment into files.
Do not delete existing artifacts as cleanup without the user's instruction.

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
the user explicitly asks. Raise important conflicts, stale sources, entry
decisions, and newly discovered dependencies in the conversation. Write a
record or handoff to the VD folders manager only when the user requests it.

Do not delete, archive, or demote a local document solely because a copy exists
in VD-docs. First establish whether the local file is historical, current,
unsubmitted, or divergent and whether the managed copy has actually absorbed
its content.

When an entry task consumes VD-docs context, include the repository commit and
source paths in the user-requested entry packet or handoff. If no saved
deliverable was requested, report the provenance in the conversation. Any
requested local document should hold entry-facing interpretation and decisions,
not another maintained copy of the source collection.

## Outbound handoffs to VD-docs

User policy established 2026-09-05, clarified 2026-09-08: when the user requests
a record or handoff document intended for VD-docs, save it in the workspace-root
folder `pass to VD-docs/`. The user decides when those documents are written.
This is the local staging location for documents awaiting transfer to the
managed collection. Keep their source references and submission status in
the document; saving there does not itself mean VD-docs has received it.

Returns for this workspace are issued in `canvalidk/VD-docs` at `outbox/VD-Newton/`; check there at the start of any task touching `pass to VD-docs/`, and if files are still sitting in that folder, a receipt may be waiting.

Active entry packets, drafts, engine/code, and evaluator work remain on their
normal production surfaces. Apply this handoff policy to new documents and
documents the user identifies for transfer; do not bulk-move historical
handoffs solely because the new policy exists.

## 2026-09-23 receipts reconciled; verified copies moved to `to delete/`

The user asked for one folder holding files that are definitely safe to delete,
rather than deleting those files now. Applied the
[amended September 23 receipt](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/outbox/VD-Newton/PASS_RECEIPT_2026-09-23.md)
together with the
[September 8 receipt](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/outbox/VD-Newton/PASS_RECEIPT_2026-09-08.md).
The amendment receives all five haze documents and supersedes the original
HELD wording. Two fluid-research documents are received and catalogued in
VD-docs `inbox/`, pending a final home; that is not a hold on their source copies.

All managed reads used `canvalidk/VD-docs@e22e150cc9cdb21d02932703e87eee5624fbf7e8`,
resolved once from `main`. Read `outbox/README.md`, both receipts, the relevant
`catalog.yaml` entries, the custody rule in `ORGANIZATION.md`, and the
unsanctioned-folder guidance. Checked all 49 receipt rows against the complete
managed Git tree and the local staging area.

**Outcome: 11 files moved unchanged to the workspace-root `to delete/` folder;
36 earlier deletion-approved files were already absent and remain absent;
one BOTH HOLD steering file and one hash-mismatched SVG remain at source.**
No file was destroyed in this task. The September 23 pass is not fully closed:
`equation.svg` is held, and the 11 moved copies await the user's deletion.

For the 11 moved files, full local SHA-256 matched the original bytes at
`VD-Newton@c2a08725895c473247463b5ba17b0208f353cc1d`, not just the receipt's
12-character prefixes. Their raw Git blob identities also matched the managed
files at the snapshot above. Hashes were checked again immediately before and
after each move. Paths within `to delete/` preserve their former paths relative
to `pass to VD-docs/`:

| September 23 receipt row | File within `to delete/` | Managed copy |
|---:|---|---|
| 1 | `Mass estimator equation/README.md` | [Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/README.md](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/README.md) |
| 2 | `Mass estimator equation/mass_estimator.pdf` | [Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/mass_estimator.pdf](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/mass_estimator.pdf) |
| 4 | `Mass estimator equation/equation.png` | [Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/equation.png](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/equation.png) |
| 5 | `Mass estimator equation/mass_estimator.py` | [Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/mass_estimator.py](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/mass_estimator.py) |
| 6 | `Mass estimator equation/example.py` | [Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/example.py](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/example.py) |
| 7 | `Mass estimator equation/requirements.txt` | [Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/requirements.txt](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/requirements.txt) |
| 8 | `NML3_HAZE_AND_THE_LOGIC_OF_NEWTONIAN_FORCE_ACCOUNTS_2026-09-10.md` | [Newton-analysis/_dscn_haze/NML3_HAZE_AND_THE_LOGIC_OF_NEWTONIAN_FORCE_ACCOUNTS_2026-09-10.md](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_haze/NML3_HAZE_AND_THE_LOGIC_OF_NEWTONIAN_FORCE_ACCOUNTS_2026-09-10.md) |
| 9 | `HAZE_FLUID_MECHANICS_AND_THERMODYNAMICS_RESEARCH_DIRECTION_2026-09-10.md` | [inbox/HAZE_FLUID_MECHANICS_AND_THERMODYNAMICS_RESEARCH_DIRECTION_2026-09-10.md](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/inbox/HAZE_FLUID_MECHANICS_AND_THERMODYNAMICS_RESEARCH_DIRECTION_2026-09-10.md) |
| 10 | `MFP1_DETECTION_WITH_HAZE_INVESTIGATION_BRIEF_2026-09-11.md` | [Newton-analysis/_dscn_haze/MFP1_DETECTION_WITH_HAZE_INVESTIGATION_BRIEF_2026-09-11.md](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_haze/MFP1_DETECTION_WITH_HAZE_INVESTIGATION_BRIEF_2026-09-11.md) |
| 11 | `HAZE_APPROXIMATE_CAR_PREDICTIONS_AND_CORE_NM_2026-09-12.md` | [Newton-analysis/_dscn_haze/HAZE_APPROXIMATE_CAR_PREDICTIONS_AND_CORE_NM_2026-09-12.md](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/Newton-analysis/_dscn_haze/HAZE_APPROXIMATE_CAR_PREDICTIONS_AND_CORE_NM_2026-09-12.md) |
| 12 | `HAZE_FLUID_PARTICLES_AND_INVESTIGATION_DIRECTION_2026-09-12.md` | [inbox/HAZE_FLUID_PARTICLES_AND_INVESTIGATION_DIRECTION_2026-09-12.md](https://github.com/canvalidk/VD-docs/blob/e22e150cc9cdb21d02932703e87eee5624fbf7e8/inbox/HAZE_FLUID_PARTICLES_AND_INVESTIGATION_DIRECTION_2026-09-12.md) |

**Keep `pass to VD-docs/Mass estimator equation/equation.svg`.** Its local
SHA-256 is `2bc29432c3184af349b18add772dbbdc4aece51421291c7c6328f12011e06cf8`;
the received original is
`33440e89a20e492734b22455f150f97f969ad5cbf4a777ca33ca6ca17e625c94`.
The only byte difference is 79 CRLF line endings in the local copy versus LF
in the received copy; the text matches after line-ending normalization.
Nevertheless the receipt's exact-hash condition was applied conservatively:
the file was not rewritten or placed in `to delete/`.

**Keep the BOTH HOLD steering file**
`pass to VD-docs/Mass estimator/mass_estimator_law_assumed_correct_steering_2026-09-07.md`.
Its bytes still match the received original.

The September 8 pass was already applied locally on September 9, as documented
below, but its 36 deletions and reference changes had not reached GitHub.
Rechecked all original hashes at
`VD-Newton@5ae1797dd5ab9a36b1c0ae56ac360ad4bff0d58a` against both receipts.
All 37 managed copies still exist: 13 are byte-identical to their source blobs,
and 24 match exactly after the documented math-delimiter normalization and the
single escaped-percent fix in the practical-limits document. No absent source
was recreated merely to place it in `to delete/`.

Seven older managed files now reside in
`Newton-analysis/_dscn_mass_estimator/unsanctioned/`, as recorded by the
catalog's September 15 ruling. Custody is preserved; they are not promoted into
the discussion's argument. The five laboratory README links to those files
now point to that actual location at the verified snapshot; its steering link
is pinned to the same snapshot. The old closure below retains its historical
paths and commit.

A filename/path reference scan covered 220 local documents and source/config
files, including ignored production material. Scratch/generated output,
dependencies, raw data/results, Git internals and the separate `VDfirst/`
checkout were excluded. No retained production document linked to the 11
newly moved source paths. Links between the moved documents and their historical
submission text are preserved as received; use their managed copies above for
reading. The moved equation README's SVG link refers to the original bundle;
the SVG itself is deliberately retained outside the deletion folder.

The eight unreceipted documents remain in `pass to VD-docs/`, including the two
September 9 haze sources requested by the receipt:
`NML3_TOLERANCE_SPECIAL_ZERO_AND_NET_FORCE_UNCERTAINTY_DISCOVERY_2026-09-09.md`
and `NML3_REMAINDER_INTERMEDIATE_EXPRESSION_ALGORITHM_2026-09-09.md`.
They were already staged locally for transfer but remain untracked and
unreceived; their presence is not authorization to delete them. No VD-docs
write was made. Live laboratory code, tests, results, unrelated work and the
separate `VDfirst/` checkout were left unchanged.

## 2026-09-08 pass closed — 2026-09-09

Applied [PASS_RECEIPT_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/outbox/VD-Newton/PASS_RECEIPT_2026-09-08.md)
and read [outbox/README.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/outbox/README.md) in full.
The receipt, `catalog.yaml`, and all 37 managed homes were verified at VD-docs
commit [`0ad969e068e77175e86f6fe8dd24e6f9f7a965ce`](https://github.com/canvalidk/VD-docs/commit/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce),
resolved from `main` on 2026-09-09. All new links below and in the laboratory
README are pinned to that commit.

The receipt prints 12-character SHA-256 prefixes. Each prefix was verified
against the full SHA-256 of its original blob in the receipt's source commit,
`canvalidk/VD-Newton@5ae1797dd5ab9a36b1c0ae56ac360ad4bff0d58a`.
All 34 present staging files matched those original blobs byte for byte.
The 33 eligible files were checked again immediately before deletion.
**No hash mismatches; no changed receipt files need another pass.**

All 36 Delete rulings are applied: 33 files deleted in this closure; rows
35–37 (the three root files received 2026-09-05) were already absent when this
task began. No current local hash can be reported for those absent files;
their source-commit hashes match the receipt prefixes. Their existing
deletions were left in place. This closes the separate September 5 batch
that was outside the August 26 closure.

The table is a custody/deletion ledger. Paths in its source column are relative
to `pass to VD-docs/`; deleted paths are historical references, not files to read.

| Receipt row | Source under `pass to VD-docs/` | Disposition | Managed VD-docs home |
|---:|---|---|---|
| 1 | `Mass estimator/mass_estimation_introduction_candidate_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_candidate_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_candidate_2026-09-06.md) |
| 2 | `Mass estimator/mass_estimation_introduction_candidate_sources_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_candidate_sources_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_candidate_sources_2026-09-06.md) |
| 3 | `Mass estimator/mass_estimation_introduction_development_plan_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_development_plan_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_development_plan_2026-09-06.md) |
| 4 | `Mass estimator/mass_estimator_air_track_trial_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/mass_estimator_air_track_trial_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_air_track_trial_2026-09-06.md) |
| 5 | `Mass estimator/mass_estimator_arrow_data_audit_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/mass_estimator_arrow_data_audit_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_arrow_data_audit_2026-09-06.md) |
| 6 | `Mass estimator/mass_estimator_behavior_test_report_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/mass_estimator_behavior_test_report_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_behavior_test_report_2026-09-06.md) |
| 7 | `Mass estimator/mass_estimator_contribution_statement_draft_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_estimator_contribution_statement_draft_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_estimator_contribution_statement_draft_2026-09-08.md) |
| 8 | `Mass estimator/mass_estimator_law_assumed_correct_steering_2026-09-07.md` | Kept unchanged — BOTH HOLD; laboratory steering | [Newton-analysis/_dscn_mass_estimator/mass_estimator_law_assumed_correct_steering_2026-09-07.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_law_assumed_correct_steering_2026-09-07.md) |
| 9 | `Mass estimator/mass_estimator_practical_limits_and_uncertainty_2026-09-07.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/mass_estimator_practical_limits_and_uncertainty_2026-09-07.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_practical_limits_and_uncertainty_2026-09-07.md) |
| 10 | `Mass estimator/mass_estimator_robot_cart_trials_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/mass_estimator_robot_cart_trials_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_robot_cart_trials_2026-09-06.md) |
| 11 | `Mass estimator/mass_estimator_uncertainty_and_reuse_walkthrough_2026-09-07.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/mass_estimator_uncertainty_and_reuse_walkthrough_2026-09-07.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_uncertainty_and_reuse_walkthrough_2026-09-07.md) |
| 12 | `Mass estimator/mass_readout_composition_uniqueness_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/mass_readout_composition_uniqueness_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_readout_composition_uniqueness_2026-09-06.md) |
| 13 | `Mass estimator/vd_shared_quantity_argument_mass_estimation_2026-09-06.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/vd_shared_quantity_argument_mass_estimation_2026-09-06.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/vd_shared_quantity_argument_mass_estimation_2026-09-06.md) |
| 14 | `Mass estimator literature review/mass_candidate_bartel_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_bartel_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_bartel_evidence_2026-09-08.md) |
| 15 | `Mass estimator literature review/mass_candidate_butler_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_butler_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_butler_evidence_2026-09-08.md) |
| 16 | `Mass estimator literature review/mass_candidate_fieller_geometry_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_fieller_geometry_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_fieller_geometry_evidence_2026-09-08.md) |
| 17 | `Mass estimator literature review/mass_candidate_huard_mailhot_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_huard_mailhot_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_huard_mailhot_evidence_2026-09-08.md) |
| 18 | `Mass estimator literature review/mass_candidate_katz_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_katz_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_katz_evidence_2026-09-08.md) |
| 19 | `Mass estimator literature review/mass_candidate_kelly_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_kelly_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_kelly_evidence_2026-09-08.md) |
| 20 | `Mass estimator literature review/mass_candidate_leonard_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_leonard_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_leonard_evidence_2026-09-08.md) |
| 21 | `Mass estimator literature review/mass_candidate_liseo_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_liseo_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_liseo_evidence_2026-09-08.md) |
| 22 | `Mass estimator literature review/mass_candidate_mantz_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_mantz_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_mantz_evidence_2026-09-08.md) |
| 23 | `Mass estimator literature review/mass_candidate_marchand_strawderman_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_marchand_strawderman_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_marchand_strawderman_evidence_2026-09-08.md) |
| 24 | `Mass estimator literature review/mass_candidate_mardia_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_mardia_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_mardia_evidence_2026-09-08.md) |
| 25 | `Mass estimator literature review/mass_candidate_roe_woodroofe_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_roe_woodroofe_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_roe_woodroofe_evidence_2026-09-08.md) |
| 26 | `Mass estimator literature review/mass_candidate_zhou_etal_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_zhou_etal_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_zhou_etal_evidence_2026-09-08.md) |
| 27 | `Mass estimator literature review/mass_equation_comparison_review_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_review_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_review_2026-09-08.md) |
| 28 | `Mass estimator literature review/mass_equation_comparison_second_review_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_second_review_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_second_review_2026-09-08.md) |
| 29 | `Mass estimator literature review/mass_equation_comparison_third_review_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_third_review_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_third_review_2026-09-08.md) |
| 30 | `Mass estimator literature review/mass_equation_final_focused_review_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_final_focused_review_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_final_focused_review_2026-09-08.md) |
| 31 | `Mass estimator literature review/mass_estimator_literature_recheck_2026-09-07.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_estimator_literature_recheck_2026-09-07.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_estimator_literature_recheck_2026-09-07.md) |
| 32 | `Mass estimator literature review/mass_point_functional_ancestry_evidence_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_point_functional_ancestry_evidence_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_point_functional_ancestry_evidence_2026-09-08.md) |
| 33 | `Mass estimator literature review/mass_predecessor_gull_werman_focused_check_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_predecessor_gull_werman_focused_check_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_predecessor_gull_werman_focused_check_2026-09-08.md) |
| 34 | `Mass estimator literature review/mass_predecessor_lindley_dellaportas_focused_check_2026-09-08.md` | Deleted 2026-09-09; full SHA-256 matched | [Newton-analysis/_dscn_mass_estimator/literature_review/mass_predecessor_lindley_dellaportas_focused_check_2026-09-08.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/literature_review/mass_predecessor_lindley_dellaportas_focused_check_2026-09-08.md) |
| 35 | `mass_estimation_zero_zero_two_cases.md` | Already absent; Delete confirmed | [Newton-analysis/_dscn_mass_estimator/mass_estimation_zero_zero_two_cases.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimation_zero_zero_two_cases.md) |
| 36 | `mass_estimator_additional_derivations_2026-09-05.md` | Already absent; Delete confirmed | [Newton-analysis/_dscn_mass_estimator/mass_estimator_additional_derivations_2026-09-05.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_additional_derivations_2026-09-05.md) |
| 37 | `mass_estimator_originality_research_2026-09-05.md` | Already absent; Delete confirmed | [Newton-analysis/_dscn_mass_estimator/mass_estimator_originality_research_2026-09-05.md](https://github.com/canvalidk/VD-docs/blob/0ad969e068e77175e86f6fe8dd24e6f9f7a965ce/Newton-analysis/_dscn_mass_estimator/mass_estimator_originality_research_2026-09-05.md) |

Only references changed in `03_trace_and_evaluator/mass_estimator/README.md`:
the steering record, behavior walkthrough, uncertainty/reuse walkthrough,
practical limits report, air-track trial, and robot/cart trial now link to
their managed homes. The relative robot/cart path is now a clickable link.
The existing derivation/source-identity pins and all substantive README
content remain unchanged.

A filename-based scan covered 150 local Markdown, text, HTML, reStructuredText,
and AsciiDoc documents, including ignored documents in the production areas.
Among documents retained after this closure, only the README held references
to this receipt's staging files. Links inside the deleted handoffs disappeared
with those copies. Scratch/generated output, dependency directories, Git
internals, and the separate `VDfirst/` checkout were excluded.

The BOTH HOLD steering copy remains byte-identical, including its historical
submission wording; this closure records its receipt without rewriting that
document. The practical-limits staging copy was deleted after matching its
pre-intake source hash. No local copy was retained, so no local percent-sign
fix was needed; receipt note 2 records the `95%` → `95\%` fix at its managed home.

Six root documents outside this receipt remain unchanged:

- `AUTHORITY_DICTIONARY_NAME_AND_ACCORDING_TO_RECONSTRUCTION_2026-09-08.md`
- `AUTHORITY_NAMES_PREDICTION_SETS_AND_FALSIFIABILITY_2026-09-08.md`
- `NML3_INTERMEDIATE_EXPRESSION_TWO_APPROACHES_2026-09-09.md`
- `NML3_MEMBERSHIP_AND_SUMMATION_LOOPS_2026-09-07.md`
- `NML3_REMAINDER_TRIPLET_AND_ACTING_OBJECT_DISCOVERY_PROPOSAL_2026-09-09.md`
- `WHY_A_THEORY_NEEDS_AN_IMMUTABLE_OBJECT_AND_UNIQUE_ID_2026-09-08.md`

No VD-docs file was edited, moved, or copied into this workspace. No historical
handoffs were moved. Existing laboratory code, tests, results, raw data, entry
packets, unrelated work, and earlier closure text remain unchanged.

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
