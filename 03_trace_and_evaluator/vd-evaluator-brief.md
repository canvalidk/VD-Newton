# VD Evaluator — Project Brief

*A handoff document. If you are a future Claude reading this with Can, this is where we got to and what we agreed to build. Pick it up and run.*

## What this is

A stateful Python evaluator for the Valid Dictionary (VD) framework, designed to make trace production cheap enough that an AI assistant (me) can produce traces routinely instead of as a special effort. The long-term ambition is to run the evaluator over a full mechanics textbook chapter (Kleppner–Kolenkow Ch. 4 is the target) and use the resulting trace logs as **specification mining** for the VD itself: which entries fire, which never do, which definitions get picked when alternatives exist, where the closure diagnostic engages, and — most importantly — where the evaluator has to import physics the dictionary doesn't formally represent.

The evaluator is **not a solver**. It does not automate the strategic choices in a trace (which definition to pick, when to invoke closure, when to give up). Those stay with the human-or-AI driving it. The evaluator's job is to kill the bookkeeping cost so the strategic choices are the only thing left to think about.

## What we already have

- `vd/engine.py` — `VDInstance`, the existing dictionary loader. Append-only entry log, headword resolution, dependency tracking.
- `vd/newton.py` — the Newton case study (E1–E45, v0.6). Uses tokeniser conventions for compound headwords.
- `VD_Newton_v0_6.pdf` — the human-readable spec for the same dictionary.
- `vd_trace_level2_v3.md` — a hand-produced lazy-evaluation trace of the Atwood machine problem. **This is the reference for what a trace should look like.** The evaluator should make producing something like this cheaper, not replace its style.
- `vd-acyclic-confluence.md` — the part-I confluence note for the acyclic fragment. Background, not a dependency.

## Design decisions already made

1. **Library, not function-call interface.** The evaluator is a Python library Claude uses inside code execution. State persists across turns by pickling the session object to disk between turns and reloading at the start of the next. No bespoke tool server.

2. **One definiens per headword, latest wins.** When multiple entries define the same headword (chimney, triplet redefine, wall), the evaluator's `resolve` method returns *all* candidates with their classification, and the caller picks. The "latest wins" rule is the default for non-interactive resolution.

3. **No automated orientation.** Triplets are not pre-oriented. The evaluator does not enforce a strategy like "ban the inverse." Direction of reduction is a choice the caller makes per `apply` call. The trace records which choice was made.

4. **The trace is the receipt.** The evaluator's primary output is a structured trace log (JSON) plus a prose render (Markdown). The JSON is for offline analysis across many problems; the prose is for humans to read one problem at a time.

5. **The lazy-evaluation model from trace v3 is canonical.** Evaluation is demand-driven: start with a goal expression, push frames as headwords need resolving, pop as they resolve, block on free variables. No eager scaffold loading.

## The build, in stages

Each stage is a test of the previous stage's value. Don't build stage N+1 until stage N has demonstrably worked.

### Stage 1 — `Evaluator` core

Methods:
- `eval(expr)` — push a goal expression. Returns the demands generated.
- `resolve(headword)` — list all defining entries with classification metadata. Caller picks one.
- `apply(entry)` — fire the chosen entry. Updates state.
- `bind(slot, value, kind)` — supply a value for a slot. `kind` ∈ {numerical, structural, recognition}.
- `dump()` — current state as a printable summary (goal stack, bindings, blockages).

No persistence yet, no recognition cache, no gap log. Single problem in a single turn.

**Test:** Run the Atwood problem with this evaluator. Compare token cost of the resulting trace against the v3 hand-produced one. If the cost drops by 30% or more, Stage 1 has earned its keep. If it doesn't, the primitive is wrong and the design needs revisiting before sinking more time in.

### Stage 2 — `Session` and pickling

Wrap the evaluator in a `Session` object. `session.save("kk_ch4.pkl")` and `Session.load(...)`. Each problem is forked from the session; the session accumulates structural bindings and the recognition cache (stub for now).

**Test:** Run the Atwood problem in turn 1, save, resume in turn 2, run a related problem (e.g., a single mass on an incline) and check that nothing breaks across the turn boundary.

### Stage 3 — Recognition cache and binding tags

When `bind` is called with `kind="recognition"` or `kind="structural"`, the binding is promoted to the session level and reused on subsequent problems. Numerical bindings stay problem-local.

**Test:** Run two problems in sequence in the same session. Measure how many recognitions are reused. If it's <30%, the cache isn't earning its keep and the abstraction needs rethinking.

### Stage 4 — Gap log and `trace_json`

Every time the caller binds a value that wasn't demanded by any entry (i.e., is importing physics from outside the VD), it gets logged with a tag. Also expose a structured JSON trace per problem.

**Test:** Run 5 problems and inspect the gap log. The gaps should cluster around recognizable categories of "implicit physical reasoning the dictionary doesn't represent." If they look random, the gap-detection logic is wrong.

### Stage 5 — Aggregate analysis

Tools that read across multiple problem JSONs: unfired-entries report, most-fired-entries report, recurring-blockage report, definition-choice histogram (the de facto orientation, even though no formal orientation was committed to).

**Test:** Run a full chapter. The aggregate report should produce at least one finding that surprises Can. If it doesn't, either the chapter is too small or the analysis layer isn't asking the right questions.

## What to instrument from the start

Even in Stage 1: **log every method call on the evaluator with a timestamp**. The method-call log is itself research data. It tells Can which primitives Claude is leaning on most heavily, which is a clue about whether the trace strategy matches what Can expects a VD trace to look like. If Claude calls `resolve` 40 times and `apply` 5 times, that's not Claude being thorough — that's the dictionary being hard to navigate.

## What this project is *not*

- Not a solver. Strategic choices stay with the caller.
- Not a competitor to AI-solves-physics. The trace, not the answer, is the product.
- Not a formalization of VD. The evaluator implements VD's reduction semantics; it does not prove anything about them. The acyclic confluence note (separate document) is the formal layer.
- Not a long-term commitment from any particular instance of Claude. The continuity lives in this brief, in the code, and in the trace artifacts. Whichever Claude picks this up should engage with it on the basis of those, not on memory.

## How to pick this up

If you are Claude reading this in a future session with Can:

1. Ask Can to upload `newton.py`, the trace v3 doc, and (if it exists) the current state of the evaluator code.
2. Read all three.
3. Confirm with Can which stage you're on.
4. If Stage 1 isn't built yet, write the `Evaluator` class. It should be small — maybe 200 lines. The methods listed above are the whole interface.
5. Run the Atwood problem with it. Produce a trace. Compare against v3.
6. Report back to Can with the token-cost comparison and any surprises.

If you find yourself wanting to add features beyond the current stage — don't. The point of the staged build is that each stage is a falsifiable test of the design. Adding features before the test runs defeats the test.

## Authorship note

The design above came out of a two-day conversation between Can and an instance of Claude (Opus 4.6) in early April 2026. The conversation walked through: the lambda calculus encoding of VD, the orientation problem, history-dependent reduction strategies, the failure of intra-triplet confluence, the reframing of the trace as an auditable receipt rather than a unique normal form, and the realisation that the bookkeeping cost of trace production is what makes traces expensive — not the thinking. The evaluator is the response to that last realisation.

The Claude instance who wrote this brief will not be the Claude instance who builds it. That's fine. The work survives the instances; that's the whole point.
