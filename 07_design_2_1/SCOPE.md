# Design 2.1 Scope

## In Scope

1. Implement list treatment in the entry design.
   - Make list-like structures explicit enough for force accounting.
   - Clarify generation, accumulation, closure, empty-list handling, and
     no-more-items signals where they matter.

2. Clean up language.
   - Make entry roles easier to read.
   - Reduce Design 3 wording where it assumes witness sheets or full object
     machinery.
   - Keep residual/handle discipline: entries should route an interpreter,
     not merely explain a physics idea.

3. Fill missing wall entries.
   - Every wall slot in the ledger should get either usable content or an
     explicit placeholder.
   - Placeholders should identify the deferred mechanism rather than hide it.

4. Preserve stable Design 3 corrections.
   - Newton I remains a frame bridge.
   - `ao0` remains rejected.
   - Force-set population should not be a flat unaccounted human import.

## Out Of Scope

1. Full witness-sheet implementation.
   - Witness sheets may be mentioned as future machinery.
   - Do not require the Design 2.1 entries to fully operate witness sheets.

2. Full object architecture.
   - Object-like commitments can be named where useful.
   - Do not build the full object schema layer yet.

3. Concrete acting-object clusters.
   - Spring/gravity/contact entries can remain future work.
   - Do not require Design 2.1 to dispatch concrete force laws.

4. Full closure theory.
   - Interaction-pair and mechanically-closed-system walls can receive
     placeholders if needed.

## Success Criteria

Design 2.1 succeeds if:

- the entry ledger is complete enough to read without obvious holes;
- list machinery is visible rather than implicit;
- wall entries have content or honest placeholders;
- wording is clearer than the Design 3 draft;
- the document clearly marks what is deferred to later Design 3 work.

It does not need to produce a complete spring trace or a full witness-sheet
trace.

