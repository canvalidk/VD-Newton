# VD Newton — Read Me First

This is the **Newton branch working folder**, not the Theory branch.

The current project goal is to move from Newton Design 2/v0.6 toward **Design 3**:

- refine the meta-typing laws;
- make the engine/theory/viewer boundary explicit;
- encode acting objects correctly;
- turn rough traces into traces that can be followed exactly;
- prepare the ground for an evaluator that makes trace production cheap for LLM execution.

The VD gives the answer and the trace. The Newton entries and engine exist so that mechanics questions can be expanded through a lazy answer-producing route: what was demanded, which entries and residual handles were exposed, what the interpreter computed, what the viewer supplied, where acting objects entered, and why the final result follows.

## Current Orientation

Read in this order:

1. `00_read_first/VD_CORE_MODEL_HANDLE_RESIDUAL.md`
   - Current core understanding of the VD.
   - The VD is a lazy controlled-exposure system: it exposes headwords and residual handles in sequence so a disciplined interpreter produces the answer and the trace.
   - Read this first to avoid reducing the trace to a retrospective audit.

2. `01_current_newton/VD_Newton_v0.6.pdf`
   - Human-readable Newton v0.6 instance.
   - Contains Design 1 and Design 2; Design 2 is the relevant predecessor to the Python instance.

3. `02_engine/newton.py`
   - Operational Newton v0.6 entries, rewritten for the tokeniser.
   - Includes the v0.6 acting-object ownership inversion:
     `mechanical-composition_point-particle` owns acting objects, and `paired-particle_acting-object` is a back-reference.

4. `02_engine/engine.py`
   - Current Core-in-code layer.
   - Implements append-only log, tokenisation, dependency graph, law detection, six-entry house detection, law degree, and structural audits.

5. `03_trace_and_evaluator/vd_trace_level2_v3.md`
   - Reference trace style.
   - Shows lazy demand-driven evaluation, blocked thunks, closure as diagnostic, and human inputs attributed to demand points.

6. `05_design_3_catchup/README.md`
   - Current Design 3 catch-up pack assembled from the mixed chronology notes.
   - Read this before using the external Design 3 documents; it records which notes are current and which are superseded.

7. `06_newton_analysis/README.md`
   - Access shelf for Newton analysis insights: randomness/QM boundaries, Newton I corrections, composition, interaction candidates, particle distinguishability, and massless-force boundaries.
   - Use this when you want the conceptual discoveries together rather than scattered through old notes.

8. `03_trace_and_evaluator/vd_newton_trace_feedback.md`
   - The most direct bridge from rough traces to Design 3 needs.
   - Important issues: meta-typing clarity, acting-object ownership, concrete acting objects, string/constraint mechanisms, closure role.

9. `03_trace_and_evaluator/vd-evaluator-brief.md`
   - Evaluator roadmap.
   - The evaluator is a library/helper for cheap trace production, not a physics solver.

## Folder Map

`00_read_first/`

Core orientation:

- `READ_ME_FIRST.md`
- `VD_CORE_MODEL_HANDLE_RESIDUAL.md`

`01_current_newton/`

Current Newton snapshot and graph:

- `VD_Newton_v0.6.pdf`
- `vd_newton_v05_graph.png`

`02_engine/`

Operational code snapshot:

- `engine.py`
- `newton.py`

`03_trace_and_evaluator/`

Trace/evaluator working context:

- `vd_trace_level2_v3.md`
- `vd_logic_tracker_guidance_PRELIMINARY_v0.5.md`
- `vd-evaluator-brief.md`
- `vd_newton_trace_feedback.md`

Treat the logic-tracker guidance as useful but stale. It is v0.5/v0.6-era thinking and may not match Design 3.

`04_entry_design_guides/`

Guides for writing and interpreting Newton/VD entries:

- `vd_law_writing_guide.pdf`
- `vd_six_entry_structure.md`
- `vd_dictionary_question_answering.md`
- `vd_question_answering_because_trace.md`
- `vd_entry_writing_best_practices_handle_residual.md`
- `vd_acting_object_entry_authoring_guide_plan_v1.md`
- `vd_spring_acting_object_working_brief_v1.md`

`05_design_3_catchup/`

Current orientation over the mixed Design 3 chronology:

- `README.md`
- `CURRENT_STATE.md`
- `SOURCE_STATUS.md`
- `DESIGN_3_GOALS.md`

`06_newton_analysis/`

Newton analysis insight shelf:

- `README.md`
- `newton_first_law_article.md`
- `vd_design_3_newton_i_correction.md`
- `vd_composition_discovery_note.md`
- `abstract_interaction_candidate.md`
- `nothing_vs_zero_somethings.md`

`90_theory_reference/`

Theory background that is helpful but not the active Newton surface:

- `handle_derivation_note_rewritten.md`
- `residue_derivation_note_revised.docx`
- `factorial_vs_sum_residual_note.pdf`
- `vd_haskell_essay.md`

Use these for conceptual grounding. Do not treat them as the active Design 3 spec.

## What Matters For Design 3

Design 3 should reduce or eliminate accidental blocked thunks by making the missing layer explicit:

- what is built into the engine;
- what is encoded in the Newton theory entries;
- what the viewer/practitioner supplies;
- what acting objects contain;
- when the evaluator computes versus asks.

The key practical target is acting objects. Mechanics problem-solving becomes much more tractable if the LLM is given correctly structured acting objects: activation conditions, canonical forces, reaction/partner behavior, parameters, approximation regime, and constraint behavior where relevant.

## Known Warnings

- `VD_Newton_v0.6.pdf` is a snapshot, not Design 3.
- `vd_newton_v05_graph.png` is v0.5 graph material, useful visually but not fully current with v0.6 numbering.
- `vd_logic_tracker_guidance_PRELIMINARY_v0.5.md` is preliminary and may be stale.
- The old Core/history PDFs were read for grounding but are deliberately not part of this Newton working surface.
- The Theory branch does not exist here yet. Theory-style notes can be drafted from this context, but this folder is for Newton Design 3 and evaluator preparation.

## Current Mental Model

The VD stack here should be read as:

- Theory text is a disciplined causal apparatus that increases the chance a competent interpreter produces correct answers.
- Core specifies the append-only, tokenised, law/house structure.
- Code implements that structure and computes the graph overlays.
- Newton instantiates the structure for mechanics.
- The trace is the answer-production route: the ordered exposure of headwords, residual handles, witness demands, inputs, computations, and halts.

This folder is focused on the last three: Code, Newton, and trace production.
