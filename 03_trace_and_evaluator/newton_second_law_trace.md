# Newton II: short executed trace

Executed 2026-09-07 using the existing **VDfirst simulator/REPL** and the 45
active entries in `02_engine/newton.py`. Result: **3 m/s² to the right**.

## Question

At instant t0, p is modelled as a point-particle with inertial mass 2 kg in an
inertial frame R, with +x to the right. Two independently verified actuator
contacts, i_A and i_B, supply forces (10, 0, 0) N and (-4, 0, 0) N to p.
These are stipulated to be all and only the relevant interactions in this
idealised example. What is p's acceleration?

## Short trace

Entry numbers below follow the Newton document comments (one-based). The REPL
uses zero-based indices: document E21 appears as E20 in the raw transcript.

1. **Normalise:** ask for `inertial-acceleration(p, t0 | R)`.
   E20 supplies the quantity's point-particle/inertial-frame requirements.
   E3 is recalled for the particle idealisation; E18 is inspected for the frame.
   The question supplies both modelling commitments.
2. **Expand E21:** acceleration equals `net-force / inertial-mass`.
   The occurrence naming acceleration on the definition's left side is
   flattened as a label, with that interpretation recorded.
3. **Demand mass:** inspect E23's positive-scalar requirement and supply the
   question's **2 kg**. This value is an input, not a calculation from the
   acceleration being sought.
4. **Demand net force:** select and expand **E24**, the vector-sum definition.
   Recall **E26**, identifying the target-directed contribution supplied by
   an interaction, and expand **E25** to demand the closed interaction set.
5. **Supply the demanded context:** at t0, the independently warranted
   membership is **{i_A, i_B}**; each supplies its stated force to p.
   The set contains two distinct interactions. The interpreter applies E24's
   vector-sum instruction: **(10, 0, 0) + (-4, 0, 0) = (6, 0, 0) N**.
6. **Return through E21:** divide by 2 kg, obtaining
   **(3, 0, 0) m/s²**. Submit that arithmetic reduction to the REPL.

Actual final simulator output:

```text
at: root
(3, 0, 0) m/s^2
open positions: none
no open holes; trace is complete.
```

The answer is 3 m/s² to the right because the independently specified
interactions supply a resultant 6 N to the right, and E21 divides that
resultant by the supplied inertial mass of 2 kg.

## What this run establishes

The existing code supports this short interpreter-driven trace. Expansion,
recall, injection, flattening of self-labels, return, reduction, and event
recording all ran through the existing REPL. The driver checked the numerical
result, an empty worklist, degree zero, and unchanged engine/entry source hashes.
No engine implementation or entry wording was changed.

The exposed limitations are concrete:

- The mass value enters at the demanded quantity after E23 is inspected;
  this snapshot has no dedicated peripheral mass-input entry. That leaves a
  gap against the code project's wall-input principle.
- Interaction membership and completeness are supplied explicitly in response
  to E25. The run does not establish an independent recognition/closure procedure.
- `recall` exposes a definition as literal text, and `reduce` accepts an
  interpreter-supplied replacement. The simulator checks neither physical
  recognition nor arithmetic equivalence. Its early “trace complete” message
  means all text holes are settled; numerical evaluation follows in the
  recorded reductions.
- Forces are given. This example does not test deriving them from acting
  objects, activation conditions, or reaction partners.

## Reproduce and inspect

From the workspace root, with Python and `networkx` available:

```powershell
python -B 03_trace_and_evaluator/newton_second_law_trace.py
```

The runtime used for this execution was:

```powershell
& 'C:/Users/canva/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 03_trace_and_evaluator/newton_second_law_trace.py
```

`networkx` 3.6.1 was installed in the ignored workspace-local `.codex_deps/`.
The adjacent `newton_second_law_trace.json` holds all 39 events, exact inspected
definitions, command/prompt transcript, retained demand tree, and source hashes.
The adjacent Python file is a replay of this one example, not a new evaluator.

## Source scope

- **Code:** local `VDfirst/engine.py`, `simulator.py`, `repl.py`, `demand.py`,
  `definiens.py`, and `residual.py`, imported read-only. The local checkout's
  HEAD was `5a57790`; it also contained pre-existing documentation edits.
- **Entries:** local `02_engine/newton.py`, loaded as existing entry data into
  the newer engine. `VDfirst/newton.py` still contains the predecessor force-set
  semantics; it was inspected but not used or edited. The active Newton entries
  already implement the ratified interaction-identity / impressed-force distinction.
- **Local guidance:** `00_read_first/VD_CORE_MODEL_HANDLE_RESIDUAL.md`,
  `04_entry_design_guides/vd_dictionary_question_answering.md`,
  `04_entry_design_guides/vd_question_answering_because_trace.md`, the August 12
  and August 26 NML3 terminology decisions, and the reference v3 trace for its
  demand/return style (not its historical force-set semantics).
- **Managed context:** `canvalidk/VD-docs` at
  `743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6`; inspected `catalog.yaml` and its
  primary `Core/vd_dictionary_question_answering.md`. The managed note corroborates
  the local question-normalisation/expansion model. This was a scoped execution,
  not an exhaustive context review or a Design 3 entry validation.

This is an active local trace artifact; it has not been submitted to VD-docs.
