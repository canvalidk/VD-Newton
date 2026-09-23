"""Small structural probe of VDfirst's parameterized-headword branch.

The three entries below are an explicit test fixture, not adopted NML3 entries.
Membership and force kernels are supplied to isolate argument substitution.
Use --code-root for an existing checkout of commit 11bfd8df1d27a5c7f2190aade2470a8a8801dc1f.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
COMMIT = "11bfd8df1d27a5c7f2190aade2470a8a8801dc1f"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--code-root", type=Path,
                        default=ROOT / ".tools/nml3_beta_probe/11bfd8d")
    code = parser.parse_args().code_root.resolve()
    sys.path[:0] = [str(code), str(ROOT / ".codex_deps")]
    from engine import VDInstance
    from repl import REPL
    from simulator import Simulator

    files = ["application.py", "engine.py", "simulator.py", "repl.py",
             "demand.py", "definiens.py", "residual.py"]
    hashes = {p: hashlib.sha256((code / p).read_bytes()).hexdigest() for p in files}
    # Proposed test-only interface: an admitted interaction handle is callable
    # with target/context and provides that target's force-expression text.
    entries = [
        ("impressed-force_i_p_c", "i_p_c"),
        ("spring-pull_p_c", "(-k*x)"),
        ("gravity-pull_p_c", "(m*g)"),
    ]
    vd = VDInstance("NML3 beta force-expression fixture")
    vd.append_many(entries)
    transcript, snapshots = [], []
    repl = REPL(Simulator(vd),
                input_fn=lambda prompt: (_ for _ in ()).throw(
                    RuntimeError("Unexpected prompt: " + prompt)),
                print_fn=lambda *parts: transcript.append(" ".join(map(str, parts))))

    def command(text):
        transcript.append("> " + text)
        verb, _, rest = text.partition(" ")
        repl.dispatch[verb](rest)

    def snapshot(label):
        trace = repl.trace
        snapshots.append({"stage": label, "text": trace.root.text(),
                          "degree": trace.root.degree,
                          "open_calls": [node.headword_at(pos) for node, pos in trace.worklist]})

    command("set reduce off")
    command("set cleanup off")
    command("trace 0 + impressed-force_spring-pull_P_C0 + impressed-force_gravity-pull_P_C0")
    snapshot("supplied output shape of a future summation traversal")
    command("expand 0")
    assert repl.trace.active.definiens.headwords == ["spring-pull_P_C0"]
    snapshot("first beta-like instantiation exposes the spring provider")
    command("expand 0")
    command("return")
    command("return")
    snapshot("first force expression exposed; second call remains lazy")
    command("expand 1")
    assert repl.trace.active.definiens.headwords == ["gravity-pull_P_C0"]
    command("expand 0")
    command("return")
    command("return")
    snapshot("both force expressions exposed")
    command("state")
    command("worklist")
    assert repl.trace.is_complete and not repl.trace.worklist
    assert repl.trace.root.text() == "0 + (-k*x) + (m*g)"
    assert hashes == {p: hashlib.sha256((code / p).read_bytes()).hexdigest() for p in files}
    report = {
        "repository": "canvalidk/VDfirst", "source_commit": COMMIT,
        "source_branch": "codex/parameterized-headwords", "source_sha256": hashes,
        "fixture_entries": entries, "snapshots": snapshots,
        "transcript": transcript, "events": [asdict(e) for e in repl.trace.events],
        "result": repl.trace.root.text(), "complete": repl.trace.is_complete,
        "open_demands": len(repl.trace.worklist),
        "limits": [
            "Initial force-sum syntax and membership are supplied; neither loop is implemented by this probe.",
            "The callable-interaction forwarding interface is a test proposal, not an adopted entry structure.",
            "Kernel definitions are supplied for fixed target P and context C0, with downward x from spring natural length.",
            "No recognition, automatic force-law dispatch, arithmetic simplification, or physics validation is claimed.",
        ],
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"snapshots": snapshots, "complete": report["complete"],
                      "open_demands": report["open_demands"]}, indent=2))


if __name__ == "__main__":
    main()
