# E8-E10 Entry-Writing Pass Intake — 2026-07-26

Status: processed into the local Newton entry-production surface.

## Intake

Four unsubmitted files were copied from the VD Folders inbox. The originals were
left in place:

- `E8_ENTRY_WRITING_PASS_2026-07-25.md`
- `E9_ENTRY_WRITING_PASS_2026-07-25.md`
- `E10_ENTRY_WRITING_PASS_2026-07-25.md`
- `ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d2.md`

The three writing passes now live in `07_design_2_1/entry_writing_passes/`.
The versioned packet lives in `07_design_2_1/entry_packets/` beside the existing
unversioned E10 packet. No managed-context document was edited, moved, or copied
into a second maintained source collection.

## Managed-context check

Current VD-docs `main` was resolved once at commit
`93afa4f77ab334e632e1519be836f806e14733b0`.

Managed files inspected at that snapshot:

- `catalog.yaml`
- `inbox/VD unsorted important/entry_writing_guide_auditable_compositions.md`
- `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md`
- `Newton/nml/nml2/nml2.2/glass_ball_mdp_example_d1.md`
- `Newton/nml/nml2/nml2.2/vd_review_corrections_d1.md`

Selection method: exact incoming filenames and the terms `E8`, `E9`, `E10`,
`address`, `determination`, `tolerance`, and `ratification`, followed through the
catalog entries relevant to the E10 address/persistence seam.

The incoming E10 packet named the earlier commit
`b23f5a215783aca8811598ceb5e783a7fdfd9726`. The entry-writing guide and NML2.1
content spec are byte-identical at that commit and current `main`. Current `main`
also contains the glass-ball and review-corrections notes invoked by the E10
writing pass. The local d2 source block now records the current coherent snapshot
and treats those two newer notes as informing rather than governing sources.

Coverage limitation: this was a targeted intake, not an exhaustive synthesis of
all historical Newton or NML material. The four incoming files are local
active/unsubmitted material and are absent from the managed catalog at the
resolved commit.

## Applied now

The chosen E8, E9, and E10 strings were promoted into
`07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md`:

- E8 and E9 replace skimmable `[A]` address marks with one-object scope and
  possessive binding.
- E9 uses `times` rather than `multiplied by`.
- E10 uses the implicit positive-scalar characterization and drops
  `coefficient`.

E10 d2 is stored additively as a successor candidate. The existing unversioned
packet remains available as the prior packet state.

## Not silently decided

- The E8 and E9 writing passes are not full successor packets, so they do not
  replace the existing packet files.
- E10 d2 is not renamed over the unversioned packet until its evaluator
  requirements and open vocabulary are accepted.
- The `-material-object` headword-suffix question remains open.
- Direction tolerance, magnitude floor, dimensional checking, provenance depth,
  and the final zero/zero evaluator term remain open.
- No evaluator implementation was changed in this intake.

## Handoff

For the VD folders manager: these four inbox items now have an active local Newton
home. If they are later ingested into VD-docs, preserve their relationship as
entry-production evidence and do not treat the managed copy as grounds to delete
or demote the local active versions. Record the VD-docs commit used by any later
promotion.
