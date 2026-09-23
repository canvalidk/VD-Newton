"""Execute a candidate recursive force-sum text traversal in VDfirst.

This consumes supplied list cells; it does not discover membership. All sum
syntax is emitted by the candidate entries through EXPAND. No injection,
RECALL, flattening, numerical summation or REPL reduction is used.
The result is a flat, left-associative addition expression, specialized to
foldl (+) 0. This is not a generic foldl implementation for arbitrary operators.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
COMMIT = "11bfd8df1d27a5c7f2190aade2470a8a8801dc1f"

# Candidate operational entries, not a ratified NML3 triplet/house cut.
TRAVERSAL_ENTRIES = [
    ("sum-interactions_l_p_c", "0 l_emit-force_p_c"),
    ("emit-force_i_tail_p_c", "+ impressed-force_i_p_c tail_emit-force_p_c"),
    ("list-end_step_p_c", ""),
]
FORCE_ENTRIES = [
    ("impressed-force_i_p_c", "i_p_c"),
    ("spring-pull_p_c", "(-k*x)"),
    ("gravity-pull_p_c", "(m*g)"),
    ("spring-pull-b_p_c", "(-k*x)"),
]


def run_case(VDInstance, Simulator, REPL, name, members):
    """Supply a finite membership list, then drive only demanded expansions."""
    assert len(set(members)) == len(members), "Input must enumerate each identity once"
    # These data entries contain only identities and links; no sum syntax.
    cells = []
    for index, member in enumerate(members):
        tail = f"cell-{index + 1}" if index + 1 < len(members) else "list-end"
        cells.append((f"cell-{index}_step_p_c", f"step_{member}_{tail}_p_c"))
    start = "cell-0" if members else "list-end"
    entries = TRAVERSAL_ENTRIES + FORCE_ENTRIES + cells
    vd = VDInstance(f"NML3 recursive sum attempt: {name}")
    vd.append_many(entries)
    transcript, expansions, iterations = [], [], []

    def unexpected(prompt):
        raise RuntimeError(f"Unexpected input prompt: {prompt}")

    repl = REPL(Simulator(vd), input_fn=unexpected,
                print_fn=lambda *parts: transcript.append(" ".join(map(str, parts))))

    def command(text):
        transcript.append("> " + text)
        verb, _, rest = text.partition(" ")
        repl.dispatch[verb](rest)

    def state():
        trace = repl.trace
        return {"raw_text": trace.root.text(), "text": trace.root.text().strip(),
                "open_calls": [node.headword_at(pos) for node, pos in trace.worklist],
                "degree": trace.root.degree}

    def expand_work_item(index, phase):
        node, position = repl.trace.worklist[index]
        call = node.headword_at(position)
        before = len(repl.trace.events)
        command(f"goto {index}")
        command(f"expand {position}")
        assert len(repl.trace.events) == before + 1
        assert repl.trace.events[-1].kind == "expand"
        expansions.append({"phase": phase, "call": call, **state()})
        if call.startswith("emit-force_"):
            iterations.append({"iteration": len(iterations) + 1, **state()})

    command("set reduce off")
    command("set cleanup off")
    command(f"trace sum-interactions_{start}_P_C0")

    # Interpreter policy: expand the remainder before the emitted force calls.
    # This loop does not know the input length or manufacture sum text.
    for _ in range(100):
        work = repl.trace.worklist
        next_index = next((index for index, (node, pos) in enumerate(work)
                           if not node.headword_at(pos).startswith("impressed-force_")), None)
        if next_index is None:
            break
        expand_work_item(next_index, "emit")
    else:
        raise RuntimeError("Traversal exceeded the diagnostic expansion limit")

    intermediate = state()
    expected_calls = [f"impressed-force_{member}_P_C0" for member in members]
    assert sorted(intermediate["open_calls"]) == sorted(expected_calls)
    assert intermediate["text"] == "0" + "".join(f" + {{{call}}}" for call in expected_calls)
    assert len(iterations) == len(members)
    for index, step in enumerate(iterations, 1):
        emitted = [call for call in step["open_calls"] if call.startswith("impressed-force_")]
        remainder = [call for call in step["open_calls"] if not call.startswith("impressed-force_")]
        assert sorted(emitted) == sorted(expected_calls[:index])
        assert len(remainder) == 1
    assert sum(e["call"].startswith("list-end_") for e in expansions) == 1

    # Now expand the deferred force calls, keeping each target/context address.
    for _ in range(100):
        if not repl.trace.worklist:
            break
        expand_work_item(0, "force")
    else:
        raise RuntimeError("Force expansion exceeded the diagnostic expansion limit")
    while repl.trace.active.parent is not None:
        command("return")
    command("state")
    command("worklist")
    final = state()
    kernels = {"spring-pull": "(-k*x)", "gravity-pull": "(m*g)",
               "spring-pull-b": "(-k*x)"}
    # This is an independent expected-output check, not the source of trace text.
    assert final["text"] == "0" + "".join(" + " + kernels[m] for m in members)
    assert repl.trace.is_complete and not repl.trace.worklist
    assert all(e.kind in {"trace", "expand", "return"} for e in repl.trace.events)
    assert [(e.headword, e.definition) for e in vd.entries] == entries
    return {"case": name, "supplied_members": members, "entries": entries,
            "iterations": iterations, "intermediate": intermediate, "final": final,
            "expansions": expansions, "events": [asdict(e) for e in repl.trace.events],
            "transcript": transcript, "complete": repl.trace.is_complete}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--code-root", type=Path,
                        default=ROOT / ".tools/nml3_beta_probe/11bfd8d")
    code = parser.parse_args().code_root.resolve()
    sys.path[:0] = [str(code), str(ROOT / ".codex_deps")]
    from engine import VDInstance
    from simulator import Simulator
    from repl import REPL

    files = ["application.py", "engine.py", "simulator.py", "repl.py",
             "demand.py", "definiens.py", "residual.py"]
    hashes = {p: hashlib.sha256((code / p).read_bytes()).hexdigest() for p in files}
    cases = [
        ("spring-and-gravity", ["spring-pull", "gravity-pull"]),
        ("empty", []),
        ("singleton", ["spring-pull"]),
        ("equal-values-distinct-interactions", ["spring-pull", "spring-pull-b"]),
        ("reversed-traversal", ["gravity-pull", "spring-pull"]),
    ]
    results = [run_case(VDInstance, Simulator, REPL, name, members) for name, members in cases]
    assert hashes == {p: hashlib.sha256((code / p).read_bytes()).hexdigest() for p in files}
    report = {"status": "candidate operational encoding; not ratified entries",
              "code_repository": "canvalidk/VDfirst", "code_commit": COMMIT,
              "source_sha256": hashes, "cases": results,
              "mechanism": "Seed 0; recursive list visitation emits infix plus and a deferred force call; empty tail emits empty text.",
              "limits": [
                  "Membership, closure and a duplicate-free finite enumeration are supplied.",
                  "The addition syntax is interpreted as left-associative; arbitrary accumulator expressions and general foldl are not implemented.",
                  "The callable interaction provider is provisional; kernels are supplied for fixed target P/context C0.",
                  "No new engine code, dynamic closures, arithmetic simplifier, or final NML3 triplet cut is supplied.",
              ]}
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for result in results:
        print(result["case"] + ": " + result["intermediate"]["text"])
        print("  -> " + result["final"]["text"])
    print(f"PASS: {len(results)} cases; all completed with unchanged sources and dictionary entries.")


if __name__ == "__main__":
    main()
