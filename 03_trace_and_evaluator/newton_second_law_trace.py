"""Replay one interpreter-driven question through the existing VDfirst REPL.

Run with Python and networkx available. This is a worked trace, not a solver:
entry choices, recognition, context bindings, and reductions are explicit below.
VDfirst is imported read-only; entries come from the active Newton workspace.
"""
from __future__ import annotations

import ast
from collections import deque
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "VDfirst"), str(ROOT / ".codex_deps")]

from engine import VDInstance
from repl import REPL
from simulator import Simulator


def main():
    source_paths = [
        "VDfirst/engine.py", "VDfirst/simulator.py", "VDfirst/repl.py",
        "VDfirst/demand.py", "VDfirst/definiens.py", "VDfirst/residual.py",
        "02_engine/newton.py",
    ]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
              for p in source_paths}
    # Read the literal entry data without importing the older engine package.
    module = ast.parse((ROOT / "02_engine/newton.py").read_text(encoding="utf-8"))
    entries = next(ast.literal_eval(n.value) for n in module.body
                   if isinstance(n, ast.Assign) and any(
                       isinstance(t, ast.Name) and t.id == "NEWTON_ENTRIES"
                       for t in n.targets))
    vd = VDInstance("Active Newton entries with VDfirst simulator")
    vd.append_many(entries)
    sim = Simulator(vd)
    transcript, exposures = [], []
    responses = deque()

    def answer(prompt):
        if not responses:
            raise RuntimeError(f"Unexpected prompt: {prompt}")
        result = responses.popleft()
        transcript.append(prompt + result)
        return result

    repl = REPL(sim, input_fn=answer,
                print_fn=lambda *parts: transcript.append(" ".join(map(str, parts))))

    def command(text, *answers):
        transcript.append("> " + text)
        responses.extend(answers)
        verb, _, rest = text.partition(" ")
        repl.dispatch[verb](rest)
        assert not responses, f"Unused answers for {text}"

    def expose(number, reason):
        """Entry numbers here follow the documents (one-based)."""
        index = number - 1
        item = {"document_entry": number, "code_index": index,
                "headword": sim.entry_headword(index),
                "definition": sim.entry_text(index), "reason": reason}
        exposures.append(item)
        transcript.append(f"LOOKUP document E{number} / code E{index}: {item['definition']}")
        if repl.trace is not None:
            repl.trace.record_event("entry-inspection", f"document E{number}: {reason}")

    def record(kind, text):
        repl.trace.record_event(kind, text)
        transcript.append(kind.upper() + ": " + text)

    def position(headword):
        active = repl.trace.active
        return next(p for p in active.open_positions if active.headword_at(p) == headword)

    def inject(headword, text):
        command(f"inject {position(headword)}", text)
        assert repl.trace.active.is_resolved, "Injected input introduced another demand"
        command("return")

    question = (
        "At instant t0, p is modelled as a point-particle of inertial mass 2 kg "
        "in an inertial frame R, with +x to the right. Two independently verified "
        "actuator contacts i_A and i_B supply forces (10,0,0) N and (-4,0,0) N "
        "to p. These are stipulated to be all and only the relevant interactions "
        "in this idealised example. What is p's acceleration?"
    )
    mass = 2
    forces = {"i_A": (10, 0, 0), "i_B": (-4, 0, 0)}
    command("set reduce off")
    command("set cleanup off")
    command("trace inertial-acceleration")
    record("normalisation", "Question targets inertial-acceleration(p, t0 | R); p, t0, R are fixed throughout.")
    expose(20, "Read the quantity's point-particle and inertial-frame requirements.")
    expose(18, "Peripheral inertial-frame description; R is stipulated inertial in the question.")
    record("recognition", "R is accepted as inertial from the question, not inferred from this particle's motion.")
    expose(21, "Choose the acceleration orientation a = F/m.")
    command("expand", "20")
    command(f"recall {position('point-particle')}")
    record("recognition", "E3's spatial-extent/internal-structure idealisation is stipulated for p.")
    command(f"flatten {position('inertial-acceleration')}")
    record("interpretation", "The self-named quantity on E21's left side labels the goal; flatten only that occurrence.")

    expose(23, "Positive scalar mass requirement; 2 kg is supplied, not inferred using the unknown acceleration.")
    assert mass > 0
    record("empirical-input", "E21 demands inertial-mass(p): bind the problem's 2 kg. No separate mass-input wall exists in this snapshot.")
    inject("inertial-mass", f"{mass} kg")

    expose(24, "Choose the force sum instead of the inverse F = ma, which needs the unknown answer.")
    command(f"expand {position('net-force')}", "23")
    command(f"flatten {position('net-force')}")
    record("interpretation", "The E24 self-reference labels the quantity being computed.")
    inject("time", "instant t0")
    expose(26, "Read the target-directed force-contribution meaning; individual numerical forces are given.")
    command(f"recall {position('impressed-force')}", "25")
    expose(25, "Demand the independently warranted, closed interaction membership before summing.")
    command(f"expand {position('interaction-set')}")
    inject("time", "instant t0")
    record("structural-input", "E25: membership is {i_A, i_B}, two independently verified contacts with target p. Completeness is stipulated, not fitted to a desired net force.")
    force_text = "; ".join(f"{name} -> p: {vector} N" for name, vector in forces.items())
    record("empirical-input", "E25/E26 demand the force supplied by each member: " + force_text)
    inject("impressed-force", force_text)
    command("reduce", "{i_A, i_B}; " + force_text)

    # The interpreter implements the vector-sum residual just exposed by E24.
    net = tuple(sum(f[axis] for f in forces.values()) for axis in range(3))
    record("interpreter-computation", f"E24 vector sum over both distinct interaction identities = {net} N.")
    command("reduce", f"{net} N")
    # The interpreter implements E21's divide-by-mass residual, then submits it.
    acceleration = tuple(component / mass for component in net)
    result = "(" + ", ".join(f"{x:g}" for x in acceleration) + ") m/s^2"
    record("interpreter-computation", f"E21: {net} N / {mass} kg = {result}.")
    command("reduce", result)
    command("state")
    command("worklist")

    trace = repl.trace
    assert trace.is_complete and trace.root.degree == 0 and not trace.worklist
    assert trace.root.text() == result
    assert acceleration == (3, 0, 0)
    assert hashes == {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                      for p in source_paths}, "A source changed during the run"

    def node_data(node):
        return {
            "provenance": asdict(node.provenance),
            "original_headwords": list(node.definiens.headwords),
            "render": node.text(), "reduced": node.reduced,
            "degree": node.degree,
            "resolutions": {str(p): {"kind": type(r).__name__,
                            **{k: v for k, v in vars(r).items() if k != "child"}}
                            for p, r in node.resolutions.items()},
            "children": {str(p): node_data(child) for p, child in node.children().items()},
        }

    report = {
        "question": question, "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_sha256": hashes, "entry_count": sim.entry_count(),
        "engine_file": str(Path(sys.modules["engine"].__file__).resolve()),
        "managed_context": {"repository": "canvalidk/VD-docs",
            "commit": "743f82b2aaa3cf09d6a1be45508b6da1c85bbfc6",
            "paths": ["catalog.yaml", "Core/vd_dictionary_question_answering.md"]},
        "exposures": exposures, "events": [asdict(e) for e in trace.events],
        "transcript": transcript, "tree": node_data(trace.root),
        "result": result, "complete": trace.is_complete,
        "degree": trace.root.degree, "open_demands": len(trace.worklist),
        "limits": [
            "Interpreter-guided use of existing REPL; no automatic physics or natural-language solver.",
            "Membership, completeness, inertial frame, idealisation, mass and force values are problem inputs.",
            "The mass value enters at the demanded quantity without a dedicated peripheral mass-input entry.",
            "Interaction membership/closure has no executable recognition procedure here; its evidence is supplied explicitly.",
            "RECALL exposes literal definitions without recursively settling their headwords; degree zero alone is not a physics proof.",
            "REDUCE checks text eligibility, not mathematical equivalence; this driver performs and checks the arithmetic.",
            "No acting-object force law or reaction-partner derivation is tested because target force values are supplied.",
        ],
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("result", "complete", "degree", "open_demands", "entry_count")}, indent=2))
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
