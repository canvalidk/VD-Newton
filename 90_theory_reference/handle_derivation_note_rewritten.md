# A Mathematical Route to Handles

## Why `raw_meaning` is a derivable object

**Purpose.** This note derives the handle concept from a matching problem. The point is not to posit a special kind of meaning-object. The point is to show that, once we try to compare two interpreters without assuming in advance that their marks, opcodes, words, or signals mean the same thing, a certain kind of object is forced on us.

The note begins in the cleanest possible case: machine-code interpreters. No humans, no natural language, no poetry, no psychological vagueness. Even there, the matching problem forces a parameterised structure. The object introduced by that structure is what this note calls a **handle**.

Two terms will be used throughout.

A **stimulant** is the concrete thing presented to a target: an electrical signal, a light pattern, a sound wave, a tactile mark, a pressure event, a chemical trace, a pattern of voltage states, a stored charge pattern, or any other causal presentation.

A **handle** is the operable route by which the target can take up that stimulant inside a procedure: an opcode, glyph, word, gesture-form, command name, formal token, or other repeatable grip. A stimulant affects the target. A handle routes the target. The same handle may be carried by different stimulants, and the same stimulant may fail to install the same handle in different targets.

The argument has two stages. First, handles are shown to be necessary even in the pure machine-code case, because a reference-invariant matching procedure cannot be written without them. Second, discipline is shown to become unavoidable even in that pure case, because concrete interpreters can fail through bit flips, radiation events, hardware faults, and other low-probability disruptions. From that wedge, discipline enters as a graded concept, and the extension to less tidy targets follows without requiring new machinery.

## 1. The matching problem, in the clean case

Take two machine-code interpreters, `I1` and `I2`. Each accepts inputs and produces outputs. Each has primitive operations triggered by specific input patterns: arithmetic, comparison, conditional jumps, memory operations, and whatever else belongs to the instruction set.

For each interpreter, call the set of local operational triggers its **handle set**: `H1` for `I1`, `H2` for `I2`.

In an idealised description, the elements of `H1` and `H2` may be written as bit-strings. In a concrete machine, those bit-strings are realised through physical stimulants: voltages, charges, clocked transitions, stored states, and so on. The bit-string is the local handle; the physical event that presents it to the machine is the stimulant.

The important point is that a handle is not the operation itself. It is the local form by which a target is made to route into an operation. One interpreter may use one bit-pattern to trigger addition; another may use a different bit-pattern. Even when two interpreters use bit-identical input patterns, there is no guarantee that the same operation is triggered. If handles were already operations, matching would be string comparison. But they are not. That is why there is a problem to solve.

Now add a reference interpreter, `I0`, whose handle set `H0` we know by construction, because we built it, specified it, or documented it. There are two versions of the matching problem.

**Version A: the single-unknown case.** Given `I1` with unknown handle set `H1`, determine which element of `H0` each element of `H1` corresponds to.

**Version B: the two-unknowns case.** Given `I1` and `I2`, both with unknown handle sets, determine the correspondence between `H1` and `H2` in a way that does not depend on privileging `I0` as the hidden standard.

Version A is straightforward in outline. We can probe `I1` with candidate stimulants, observe outputs, test identities such as commutativity, associativity, neutral elements, inverses, and interaction with other operations, then compare the resulting behavioural signature with the signatures of known handles in `H0`. Call this procedure **description A**.

Version B is where the forcing move happens.

## 2. The forcing move

Description A, because it solves the single-unknown case, is concrete in a particular way: it is allowed to mention `H0` by name. It can contain steps such as:

- probe the unknown handle on successor-generated inputs and compare the result with addition in `H0`;
- test whether repeated use of the unknown handle behaves like multiplication in `H0`;
- check whether the candidate handle composes with equality, ordering, or zero in the way the corresponding `H0` handle does.

Those references are legitimate in Version A because `I0` is the reference interpreter. `H0` is available as an anchor.

Version B requires a procedure of the same general kind, but neither of the interpreters being matched is allowed to function as the already-known standard. More exactly: the resulting correspondence should be invariant under the choice of reference interpreter. We may use our own language to describe the procedure from outside, but the match itself should not depend on secretly treating `H0` as the thing all other handles must resemble.

So we need **description B**: a procedure that matches two unknown handle sets without hardcoding the named handles of `H0` into the body of the procedure.

Description B must still be a faithful generalisation of description A. By faithful, I mean this: if one of the two supposedly unknown interpreters in Version B happens to be `I0`, then description B should reduce to description A. It should produce the same correspondence that description A would have produced. If it does not, then B is not really a generalisation of A. It is a different procedure that happens to solve a related problem.

For that reduction to hold, description B must have a specific shape. Every place where description A mentions a specific known handle from `H0` must become, in description B, a position that can be filled at runtime by whatever local handle occupies that role on the target being probed.

Two alternatives fail.

If description B hardcodes the handles of `H0`, it fails to solve the genuine two-unknowns case. The procedure would still be routing everything through our own reference interpreter.

If description B simply deletes the references to `H0`, it no longer reduces to description A in the degenerate case. Description A's output depends on those anchor positions; removing them changes the problem.

The only route that preserves both generality and reducibility is parameterisation. The named anchors in A must be lifted out of the procedure body and replaced by positions that can be filled differently on different targets.

Those parameterised positions are **handles** in the sense derived here. They are not added because natural language is messy. They are forced by the attempt to write a reference-invariant matching procedure.

## 3. What a handle is

A handle, under this derivation, is an operational position in a procedure. It is individuated by the role it plays: where it appears in the procedure, what the procedure does with whatever fills it, what other handles it must compose with, and what consequences it produces under probing.

This requires one careful distinction. There are **local handles** and there are **matched handles**.

A local handle is target-specific: a machine opcode, a glyph recognised by a trained reader, a spoken word recognised by a listener, a gesture recognised by a trained participant, a formal token in a proof system, or a command name in a programming environment. A local handle is the thing by which a target is actually routed.

A matched handle is the procedure-position that survives comparison across targets. It is what lets us say that different local handles are playing the same role, under a stated discipline and budget.

Where the distinction matters, this note will say **local handle** or **handle-position**. Where it does not, it will simply say **handle**.

This avoids a regress. One might worry that, if handles are used to explain symbols, handles must themselves be symbols, and then some further thing would be needed to explain those symbols, and so on. But the handle derived here is not a self-interpreting symbol. It is a position in a procedure, filled by local handles when the procedure is run on concrete targets.

Take the expression:

`F = m · a`

A trained human reader sees the glyph `·` and routes it as multiplication. But that trained reaction is not universal. On a CPU, the relevant local handle may be an opcode or instruction pattern. In a programming language, it may be an operator token. In speech, it may be the word "times". On paper, it may be `·`, `*`, or `x`, depending on the convention. The physical stimulants are also different: photons from ink or pixels, sound waves, electrical states, tactile marks, and so on.

The handle at the multiplication position is not the glyph `·`. It is not the sound of the word "times". It is not an abstract object already known to be multiplication. It is the procedural grip at which whatever local handle routes multiplication on this target gets supplied.

That is why operator positions are handles too. In an expression like:

`a · b = c`

there are handle-positions for the operands, for the operation between them, and for the equality relation. The temptation to treat `·` and `=` as the known parts, while `a`, `b`, and `c` are the variable parts, comes from the fact that we are already trained readers. From the matching procedure's point of view, the operator marks are not privileged. They are local handles that must be installed and tested like everything else.

The handle is therefore not individuated by its name, because it has no intrinsic name. It is not individuated by its physical stimulant, because different stimulants can carry the same local handle. It is not individuated by a referent assumed in advance, because reference is precisely what the matching procedure is trying to establish. It is individuated by disciplined procedural role.

## 4. Stimulants, probes, and target access

A **probe** is a controlled attempt to learn what a handle does on a target. It presents a stimulant, attempts to route a local handle, and records the resulting behaviour.

The stimulant and the handle must not be collapsed.

When a calculator key is pressed, the physical event is a stimulant. The multiplication key, insofar as the calculator routes it as multiplication, is a local handle. When a reader sees `x` or `*`, the light pattern is the stimulant; the trained glyph-form is the local handle. When a listener hears "times", the acoustic waveform is the stimulant; the recognised word-form is the local handle. When a machine receives an instruction bit-pattern, the voltage or stored state is the stimulant; the recognised instruction pattern is the local handle.

This distinction matters because failure can occur at either layer. The stimulant may not reach the target cleanly: the sound may be muffled, the glyph may be smudged, the voltage may be corrupted. Or the stimulant may arrive cleanly but fail to install the intended handle: the child may not yet know the glyph, the machine may parse the bytes under a different instruction set, the reader may treat `x` as a variable rather than multiplication.

The matching procedure is not interested in one isolated presentation. It is interested in the pattern that emerges when many probes are run. A handle is known by its dossier.

## 5. The dossier

When description B is run on a pair of interpreters, each handle-position develops a running record of observations. We present stimulants, route local handles, observe outputs, test identities, record failures, vary surrounding contexts, and compare behaviour across targets.

The accumulating record of what a target does when a handle is probed is the **dossier** on that handle-target pair.

A dossier might look schematically like this:

`h := associative; commutative; h(3, 4) = 12; h(n, 0) = 0; h(n, 1) = n; distributes over k; ...`

The left-hand side picks out the handle-position. The right-hand side accumulates observations about what happens when local handles fill that position on a target. The ellipsis is not decoration. It marks that the dossier is a sample from a larger behavioural profile. More observations could be made, and those possible observations matter to the identity of the handle even before all of them have been explicitly recorded.

Two kinds of item appear in the dossier.

**Universal or structural observations** rule out broad classes of candidate roles: associativity, commutativity, identity elements, absorption laws, distributive relations, invertibility, interaction with equality, and so on.

**Point observations** tether the dossier to specific reproducible behaviour: `h(3, 4) = 12`, `h(2, 5) = 10`, `h(7, 0) = 0`, and similar checks.

Neither kind suffices alone. Universals without point observations float free of any actual target. Point observations without structural observations cannot distinguish operations that happen to agree on a small sample. The dossier needs both.

If we restrict ourselves to ideal machine-code interpreters and pretend they are perfectly deterministic, the dossier seems to converge sharply. Each handle-position appears to acquire a closed interpretation on each target, and matching across interpreters appears to reduce to checking whether dossiers agree.

That tidy picture is useful, but it is not the final picture. The reason is that concrete interpreters are not ideal mathematical objects. They are physical targets.

## 6. The wedge: bit flips

An abstract machine can be deterministic by stipulation. A concrete machine-code interpreter, however, is realised in hardware, and hardware can fail. A high-energy particle can flip a bit. Error-correcting memory can reduce this rate but not abolish all physical fault modes. Packaging materials, thermal effects, hardware ageing, power instability, and other low-probability disruptions can also make an observation go wrong.

This is usually a marginal engineering concern. For the matching framework, it is structurally important.

It means that no observed claim about a concrete machine-code interpreter can be asserted at exactly 100 percent confidence. A dossier entry such as `h(3, 4) = 12` is not an eternal fact stamped directly onto the world. It is a very high-confidence observation about what that target does when probed under those conditions. A universal such as "h is associative" is not something established by literally infinite inspection. It is a stable expectation supported by a body of probes, a model of the target, and an accepted error budget.

This forces a change in the unit of analysis. The dossier cannot be treated as a closed list of certain facts. It must be treated as a running estimate, revisable under further observation. The target cannot be reduced to "the operation itself". It must be treated as something that reliably behaves within bounds when reached through a handle.

The word for the property that makes the dossier converge is **discipline**.

Discipline is not perfect determinism. It is bounded, stable behaviour under probing. A disciplined target may still fail, but its failures have a shape. They occur with rates, conditions, distributions, and repair paths that can be measured, modelled, or at least bounded.

The important point is that discipline became necessary without leaving the machine-code case. We did not need human ambiguity to force it. We did not need natural language. The wedge is already present in the pure case, because the pure case must still be accessed through concrete acts of probing.

## 7. Discipline as a graded concept

Once discipline enters, it enters by degrees.

A hardened machine-code interpreter in a controlled environment may be highly disciplined: its dossier converges tightly, with rare failures measured in long mean times between errors. A physical measuring instrument may be disciplined up to thermal noise, calibration drift, and reference-standard stability. A trained human performing a rehearsed calculation with pen and paper may be disciplined enough for many purposes, though with attention lapses and fatigue. A casual speaker responding to an ordinary word may be disciplined only loosely, and the resulting dossier may converge only under coarse-graining.

These are not separate ontological categories. They are points on a gradient. In each case, a target is probed through stimulants and local handles; a dossier accumulates; and the question is how tightly and stably that dossier converges.

The graded notion needs three refinements.

First, discipline does not require the same output on every trial. What matters is that the statistical behaviour is stable. A target that produces one response half the time and another response half the time, with the same distribution over time, is disciplined in the relevant sense: the dossier converges on a bimodal distribution. Randomness is not the enemy. Drift is. If the statistical structure itself moves around, the dossier does not settle.

Second, discipline is usually installed. In machines, discipline is installed through engineering: transistors, instruction-set design, error correction, clocking, shielding, packaging, and verification. In humans, discipline on something like arithmetic is installed through training with feedback. The child learns that certain glyphs, sounds, and written forms route certain operations. A broad response distribution is narrowed by correction, reward, repetition, and use.

Before that installation, the glyph `+` is just a mark to the child. It may be a visual stimulant, but it is not yet a reliable local handle for addition. After installation, the same visual pattern can route an addition procedure. The glyph has become usable as a handle because the target has been disciplined to take it up that way.

Third, discipline is a joint property of target and access method. The same human may be poorly disciplined on multi-digit arithmetic when forced to do it mentally and much more disciplined when given pen and paper. The target has not simply changed from one being into another. The access method has changed. The probe now includes scaffolding that stabilises the dossier.

This is why a great deal of real-world matching works by installing or improving discipline rather than by discovering targets that were already perfectly disciplined.

Consider the multiplication position in `F = m · a`. On a calculator, the stimulant may be a keypress and the resulting electrical event; the local handle is the calculator's multiplication route. On a trained adult, the stimulant may be light from the glyph `·`, `x`, or `*`; the local handle is the recognised multiplication mark. In a programming environment, the stimulant may be a sequence of characters or bytes; the local handle is the operator or instruction pattern that routes multiplication. On a child who has not learned multiplication, the same visual mark may not install any stable multiplication handle at all.

The dossier across disciplined targets may still converge. That convergence is what licenses the claim that these different targets are doing "the same" multiplication for the present purpose, despite the local handles and stimulants being different.

## 8. Matching via dossiers

With discipline in hand, the two-unknowns matching procedure takes its final shape.

Two handles, instantiated through local handles on two targets, are candidates for identification when their dossiers agree. But agreement is not exact identity. No two concrete dossiers agree at every possible level. Targets differ in access method, output format, failure profile, speed, range, memory, representational limits, and surrounding conventions.

So dossier agreement is conditional in three ways.

First, both targets must be sufficiently disciplined on the relevant handle for their dossiers to have stabilised. If either dossier is still drifting, there is nothing stable to match.

Second, a coarse-graining of the output space must be chosen. Two targets may produce different physical outputs that should count as the same answer for the purpose at hand: a binary encoding, a decimal numeral, a spoken number, a mark on paper, a changed machine state. Deciding which differences matter and which differences can be ignored is part of the matching setup.

Third, a probability budget must be accepted. Because concrete targets are not perfectly disciplined, some rate of mismatch must be allowed without immediately destroying the identification. A match that holds at 99 percent under a declared coarse-graining is a real match under that budget. A match that holds at 99.9 percent is stronger. A match at exactly 100 percent is not something concrete probing can establish.

When a match is declared under these conditions, the claim is not that two local handles are literally identical. They are not. The glyph, opcode, word, and gesture are different objects in different systems. The claim is relational:

The disciplined consequences of routing one local handle on one target coincide, up to coarse-graining and budget, with the disciplined consequences of routing another local handle on another target.

The identification lives in the relation between dossiers. It is not hidden inside either local handle by itself.

## 9. Failure modes

Because matching is conditional, it can fail in several distinct ways. Distinguishing them matters.

**Discipline failure.** One or both targets are not stable enough on the relevant handle for the dossier to converge. The remedy is to improve the access method, scaffold the target, constrain the context, train the target, or accept that no match can be made at the current level of access.

**Coarse-graining failure.** Both dossiers converge, but no acceptable coarse-graining aligns their outputs. What one target treats as the same response, the other treats as distinct; or what one target distinguishes, the other collapses. The remedy is to negotiate a common output space or conclude that the targets carve the space differently.

**Budget failure.** Both dossiers converge, and the coarse-graining is agreed, but the observed mismatch rate exceeds the accepted probability budget. The remedy is either to loosen the budget, weakening the claim, or to reject the match at the required confidence.

Collapsing these into the single phrase "the match failed" loses information. Each failure points to a different part of the setup: the stability of the target, the translation between outputs, or the tolerance allowed by the comparison.

## 10. `raw_meaning`

The earlier informal formula can now be made precise:

> the meaning of a word is the total change in the relevant state of the world caused by the utterance of that word in a given context.

In the present vocabulary, `raw_meaning` is the convergent content of a dossier on a disciplined target, held at a handle.

That is the object. It is not a private mental item. It is not a ghostly referent behind the sign. It is not the stimulant itself. It is what a stable target does, and is disposed to do, when a handle is reached through appropriate stimulants and probes.

This object has an important asymmetry. The access route is target-dependent. Different targets require different stimulants and local handles: glyphs, opcodes, voltages, sounds, gestures, marks, or formal tokens. But the convergent content of the dossier can be target-independent in the disciplined limit. The dossier abstracts over differences in local handle and stimulant. What remains is the stable behavioural role.

So `raw_meaning` is derivable in three steps.

First, the attempt to write a reference-invariant procedure for matching two unknown interpreters forces the procedure into a parameterised shape. The positions created by that parameterisation are handles. This step is structural and already holds for machine-code interpreters.

Second, because concrete machine-code interpreters are physical targets, their behaviour under probing cannot be treated as certain at exactly 100 percent confidence. The right unit is therefore not a closed fact but a dossier, and the property that lets the dossier converge is discipline.

Third, once discipline is admitted as graded, the same machinery extends to less tidy targets. Humans, measuring instruments, proof systems, trained readers, and casual speakers differ in degree of discipline, not in the basic structure of the problem. Each can be treated as a target probed through stimulants and handles, with a dossier that may or may not converge under a declared budget.

This also explains why dossiers have authority over definitions. A definition is a constructed string. It may be well written or badly written. It may route the intended handle or fail to route it. But the dossier records how a disciplined target actually behaves when probed. If a formal definition conflicts with the stable dossier of the handles it uses, the definition is the thing that must be corrected. The record has priority over the construction.

That is the sense in which handles carry authority here. Not because they possess metaphysical depth. Not because their names are sacred. But because their dossiers report a constrained pattern of behaviour that was not simply chosen by the writer of the definition.

A stimulant affects. A local handle routes. A dossier records. Discipline stabilises. A budget licenses the match. `raw_meaning` is the convergent content that remains.
