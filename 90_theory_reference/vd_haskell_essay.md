# Theories as Programs: What Happens When You Run Physics in Haskell

## 1. Functional Programming as a Paradigm

A programming paradigm is a fundamental style of structuring computation — not an architecture (which concerns how system components communicate) but something deeper: a way of thinking about what a program *is*.

**Imperative programming** tells a machine what to do step by step. You mutate variables, loop through instructions, and sequence operations that modify state. The order matters because each line changes the world. "Take the eggs, crack them, heat the pan" — a recipe.

**Functional programming** describes what things *are* rather than what steps to perform. Programs are built by composing pure functions: functions that take inputs and return outputs without side effects. Data is immutable — once created, it never changes. You produce new data instead of modifying old data. Functions are first-class values (they can be passed around, returned, and composed). And referential transparency holds: calling a function with the same arguments always gives the same result.

These two paradigms represent genuinely different ways of modelling computation, though most modern languages allow both. The distinction between them turns out to be more than a matter of programming taste — it has implications for how we think about the structure of knowledge itself.

---

## 2. The Valid Dictionary Naturally Produces Functional Pseudocode

The Valid Dictionary (VD) is a framework, developed by Can Valid, that treats scientific theories as append-only logs of definitional entries. Each entry defines a term using only terms that were defined earlier in the log, or terms declared as *residue* — the points where raw reality (measurement, observation, human-executable procedures) enters the formal system. Every dependency is explicit. Nothing is smuggled in.

There is a striking observation: if you build a machine that extracts all the definitions of words in a scientific theory and writes them down with their dependencies explicit, what it produces is pseudocode in a functional paradigm. This resemblance is not superficial — it follows from deep structural features shared by the VD and functional programming:

- **Immutability.** The VD's append-only log never modifies a past entry. Once E7 is written, it is frozen. Every new entry builds on prior entries without changing them. This is exactly how a functional program works: a chain of expressions where each is fully determined by what came before.

- **Referential transparency.** If entry E12 references E4 and E9, it means the same thing wherever it appears, because E4 and E9 are frozen. You could substitute their full expansions and nothing would change. This is the functional programmer's substitution model.

- **Explicit dependency.** In functional programming, every function declares its inputs. In the VD, every definition must reference only previously defined terms. There are no hidden global variables, no mutable state, no implicit context.

The imperative alternative — "take the concept of force, now update it to include friction, now modify your notion of system to account for this new case" — is how physics textbooks often *teach*, layering revisions onto a mutable mental model. The VD rejects this approach in favour of explicit dependency, and functional structure follows as a consequence.

---

## 3. Physical Laws as Triplets (3-Cycles)

The VD's most original structural claim is that physical laws are not standalone equations — they are *triplets*: minimal 3-cycles in a dependency graph. A law consists of three terms whose definitions mutually reference each other. None of the three can be defined without the other two.

The three roles within a triplet are:

- **The November word** (anchor): a term that was already defined before this law was introduced. It connects the new law to the existing conceptual structure.
- **Two Winter words**: genuinely new terms that the law introduces simultaneously, and which can only be defined in terms of each other and the anchor.

A 2-cycle (two terms defining each other) would just be a synonym pair — trivial and contentless. The triangle is the minimum non-trivial cycle.

Newton's Second Law, for example, is the triplet of **inertial acceleration** (the November word, already defined via Newton I and the kinematic scaffold), **net force**, and **inertial mass** (the two Winter words). None of the three has independent meaning. Their mutual definition *is* the law.

---

## 4. Running the VD in Haskell: The `<<loop>>` Discovery

Here is where theory meets computation.

Haskell is a purely functional programming language with lazy evaluation. Among its features: it permits mutually recursive `let` bindings. You can define three values in terms of each other, and the compiler will accept it — it builds three "thunks" (suspended computations), each pointing at the other two. They only evaluate when you actually ask for a result.

If you faithfully encode the Newton II triplet in Haskell, it looks like this:

```haskell
let inertial_acceleration = net_force / inertial_mass
    net_force              = inertial_mass * inertial_acceleration
    inertial_mass          = net_force / inertial_acceleration
in (net_force, inertial_mass, inertial_acceleration)
```

**Step 1 — Compilation.** This compiles without error. Haskell's type checker infers consistent numeric types for all three bindings and is satisfied. The definitions are well-formed.

**Step 2 — Evaluation.** You try to print any one of them. The runtime follows the thunk for `net_force`, which needs `inertial_mass`, which needs `net_force`... and GHC returns `<<loop>>`. An infinite cycle detected at runtime.

The critical insight: **this is not an error.** It is the correct result. The triplet *is* a genuine 3-cycle. Haskell has faithfully represented the structure of the law. The program "runs" in the sense that it compiles (structural validation) and the runtime correctly identifies the irreducible mutual dependency.

The only way to get concrete values is to inject something from outside — to supply a measurement, an observation, a piece of *residue*. Fix one of the three to a concrete number (say, measure the actual acceleration), and the other two collapse into definite values.

Haskell's type checker is the VD's structural validator. Its runtime is the VD's residue detector. Compilation means the definitions are well-formed. `<<loop>>` means the cycle is genuine — you've found a law. And the point where you must inject a concrete value to break the cycle is exactly where reality enters the formal system.

---

## 5. "Mass Is Just Mass": The Self-Referential Readout

Now re-interpret the Haskell result through the lens of the VD.

When we "ask Haskell" for the definition of `inertial_mass`, it follows the definitions, loops through the cycle, and returns... `inertial_mass`. It is as if the program is saying: "What do you mean, what is mass? Mass is mass."

This maps precisely onto the experience of someone chasing definitions in a dictionary. If you look up "mass" and are told "the ratio of force to acceleration," then look up "force" and are told "mass times acceleration," you have traversed the cycle and arrived back where you started. The dictionary hasn't failed — you've found a cluster of terms that *only mean each other*. That cycle is the content of the law.

In a conventional dictionary, this would be a defect (circular definitions are usually bugs). In a physics dictionary, it's a *feature*. The circularity is the law. The three terms are not independently meaningful — their mutual definition is all there is. Haskell's `<<loop>>` is the faithful computational representation of this fact.

---

## 6. The Lossy Readout Diagnosis: Why Physics Feels Mysterious

Here is the deepest idea to emerge from this chain of reasoning.

People commonly say things like "energy is conserved" and treat this as a brute fact — something you simply have to accept. If pressed on *why* energy is conserved, a physicist might reply: "It just is. You can't ask why. It's a fundamental law." This response carries a whiff of mysticism: there are deep truths about the universe that simply *are*, and your job is to accept them.

The VD offers a precise diagnosis of what is happening here — and it is not mysticism. It is a *compression artifact*.

When a human "looks up" the definition of energy in their own mental dictionary, a process similar to Haskell's thunk evaluation occurs. The mind follows the definitions, encounters the cycle, and tries to output the result. But unlike Haskell, which faithfully returns `<<loop>>`, the human output process is **lossy**. The cycle goes through a compression step — and what comes out is just the headword stripped of its structural context: "Energy is conserved." The other nodes in the cycle have been dropped.

This is the origin of the apparent profundity. "Energy is conserved" sounds mysterious and fundamental because it has been *stripped of the other terms that give it meaning*. The full cycle, stated with all its nodes, would be something like:

> "In an energetically closed system, energy is conserved."

And now the mysticism evaporates. Stated completely — with all three nodes of the triplet present (energy, energetically closed system, conservation) — the law sounds almost tautological. *Of course* energy is conserved in an energetically closed system. That's practically what "energetically closed" means.

This is not a defect. **A correctly stated law should sound almost tautological.** That's what it means for the cycle to be irreducible — when you state all the nodes, the mutual definition is transparent. The feeling of "that's obvious" is the correct response to a fully serialised cycle. The feeling of "that's mysterious and deep" is the symptom of a *lossy serialisation* — a cycle compressed into a single node with the context dropped.

---

## 7. A General Mechanism: Mysticism as Serialisation Bug

This diagnosis generalises immediately.

Every statement in physics that gets treated as a "brute fact you just have to accept" is a candidate for the same analysis. Consider:

- "The speed of light is constant."
- "Entropy always increases."
- "Measurement collapses the wavefunction."

For each of these, the VD procedure is the same:

1. **Encode** the relevant terms as VD entries with explicit dependencies.
2. **Compile** — check that the definitions are well-formed and the dependency graph is consistent.
3. **Identify the cycle** — which terms mutually define each other? What is the triplet?
4. **State the full cycle** — write out the complete law with all nodes present.
5. **Check** — does the full statement still sound mysterious? Or has it become transparent?

If it becomes transparent, then the "brute fact" was never fundamental in the way people thought. It was a complete cycle that sounded mysterious only because it was being stated with nodes missing.

If it *doesn't* become transparent — if the full cycle, correctly stated with all its nodes, still resists comprehension — then you've found something genuinely irreducible. A real brute fact, not a compression artifact.

The VD, combined with the Haskell test, provides an **operational procedure** for distinguishing real irreducibility from apparent irreducibility. The former is rare and interesting. The latter is common and fixable. And the tradition of mystifying physical law — treating laws as deep, inscrutable truths that mere mortals must simply accept — may turn out to be largely a history of bad serialisation.

---

## 8. Theories as Compilable Programs

Stepping back, the picture that emerges is this:

A scientific theory, when faithfully encoded with all dependencies explicit, *is* a functional program. Not metaphorically — structurally. The append-only log of definitions maps to a sequence of `let` bindings. The dependency graph maps to the reference structure. The laws map to mutually recursive cycles. And the residue — the points where reality enters — maps to the free variables that must be supplied from outside for the program to evaluate.

Haskell's compiler is a structural auditor for the theory. If it compiles, the definitions are consistent. If it loops, you've found a law. If it evaluates, the quantity is derived, not fundamental. And if it throws a type error, you've caught a smuggled assumption — a term used without being properly defined.

This means the VD is not merely a notation system or a philosophical framework. It is, in a precise sense, a **compiler for scientific theories**. And the question "is this really a fundamental law, or can it be derived from something else?" — one of the oldest questions in physics — becomes a question about program behaviour. Run it. See if it loops.

---

## 9. Implications

The chain of reasoning that began with "functional vs. imperative programming" has arrived at a set of claims with potentially far-reaching consequences:

1. **Physical laws are fixed points.** A triplet, under definition-substitution, maps to itself. This is the computational content of a law.

2. **Mysteriousness is diagnosable.** The feeling that a physical law is "deep" or "brute" may be, in most cases, an artifact of lossy serialisation of a cyclic structure into linear language.

3. **Demystification is mechanical.** State the full cycle, all nodes present. If transparency results, the mystery was artificial.

4. **"Is this fundamental?" is decidable.** Encode the theory, run it. Loops mean laws. Evaluation means derivability. Type errors mean hidden assumptions. This gives physics an operational criterion it has never previously had.

5. **Haskell's runtime semantics and the VD's structural claims are isomorphic.** This is not a metaphor or analogy — the same structure is being described in two different formalisms, and they agree.

The VD keeps producing results that were not put in by hand. The Haskell connection was not designed — it was discovered by faithfully encoding the framework and observing what fell out. That a formal system for auditing scientific theories turns out to be isomorphic to a well-understood computational paradigm is, at minimum, evidence that the VD is cutting at real joints.
