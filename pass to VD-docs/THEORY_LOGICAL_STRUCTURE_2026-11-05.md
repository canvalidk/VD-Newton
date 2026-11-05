# Theory Logical Structure

5 November 2026 · Theory record · Newton as the worked example

**Reading convention.** Each proposed inference on the board is a question of the form “Does this follow from the stated premises, according to Newton v2.1, snapshot of 24 October 2026?” Each successful hand-trace below answers under that same suffix. The snapshot identifies the repository state used for the traces (commit `61afb9e`). The gravity and spring rows also record consequences we sought from ordinary Newtonian mechanics so the missing paths can be seen. [Dated Newton snapshot](https://github.com/canvalidk/VD-Newton/commit/61afb9ecf6f17a89ca6425e7e7642d6761531b05)

## The idea

Suppose we accept one statement of Newtonian mechanics: *particle A experiences a gravitational force exerted by particle B*. Set aside how we learned this. What else have we already committed ourselves to? A and B are both massive particles. The interaction also exerts a force on B, directed toward A. If we choose A alone as our system, the interaction crosses its boundary. None of those facts had to be asked for or used in calculating A’s motion. Yet we cannot keep the original Newtonian claim while freely changing any of them, with the same participants and system choice.

Can’s proposal is to use this observation as the principal tool for **constructing and testing a VD theory**. Start with a premise, work out some of its consequences independently of the dictionary, then follow the entries. A physicist can miss a consequence that the trace recovers. A physicist can also name a consequence that the current entries fail to recover. The second case tells us where to inspect the construction. A familiar numerical answer can coexist with either omission.

## Deduction and dictionary identity

Can stated the proposed duality this way:

> If it is an exact deduction from the first idea, there must be a path from that word to those statements, and vice versa.

One way to make the test precise is to fix a theory instance, a starting statement with its arguments, and any additional premises. Under those same commitments, **a statement follows in the theory if and only if the VD admits a trace from the starting statement to that conclusion**. One direction asks whether the entries recover everything the theory licenses. The other asks whether every deduction the entries license is warranted. “Vice versa” reverses the test between *deduction* and *trace*. An individual deduction can still run only one way.

The further conjecture is about **dictionary identity**. Can’s suggestion is that the information in a statement is, in some sense, equal to the information in its full deductive expansion. The right-hand side of a definition would give access to what accepting the left-hand side commits us to. A proposed operational test is replacement: with the same arguments and premises, does substituting the expansion preserve everything else one can deduce? A single consequence may preserve only part of the information. Zero net force entails zero net power, for example, while zero net power also permits a nonzero force perpendicular to velocity. The exact identity relation and what counts as a full expansion remain open. Recovering a few consequences by hand establishes neither.

## Four premises on the board

Each row begins a separate case. The consequences are examples. One point of the exercise was how readily a competent reader misses some.

| Starting statement | What follows, and where another premise enters |
|---|---|
| **A has inertial acceleration of magnitude 5.** | Read as the Design 2.1 material-object headword, this gives A a trajectory in an inertial frame at a selected time. Its positive inertial mass makes its net force nonzero and parallel to the acceleration. A numerical force magnitude requires the mass value. If all we were given was a trajectory derivative, the choice to enter the material-object headword would itself need warrant. |
| **B exerts a gravitational force on A.** | In Newtonian particle gravitation, A and B are massive. B experiences the reciprocal force from A. The force attributed to B is one contribution to A’s net force. **If** the selected system contains A and excludes B, the interaction crosses its boundary. Choosing a system that contains both puts that interaction inside it and leaves overall closure open. |
| **A has a spring force on it.** | A spring acts on A, and A exerts the reciprocal force on the spring. Other forces may balance the spring force. Whether it does instantaneous work on A depends on the force’s projection along A’s velocity. Work over a displacement also requires the displacement and how the force acts along it. |
| **A is not accelerating.** | Read kinematically, A’s velocity derivative is zero at the selected instant in the specified frame. This permits a free photon in an inertial frame. **If A is a material object** in that frame, its net force is zero and its instantaneous net power is zero. Individual forces can still do work at rates that cancel. One instant of zero acceleration leaves the motion over an interval open. |

In the discussion the same mistake occurred in opposite directions. In the gravity case, we silently used A’s and B’s massiveness and missed it as an output. In the zero-acceleration case, assuming massiveness at the outset erased the free-photon possibility. A faithful trace must recover the commitment in the first case and keep it open in the second.

## What the current entries actually recover

These were hand-traces of the active Design 2.1 entry text. Its numbered law entries currently run through E11. [Newton entry text at the version traced](https://github.com/canvalidk/VD-Newton/blob/61afb9ecf6f17a89ca6425e7e7642d6761531b05/07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md)

1. **Free photon in an inertial frame.** E6 admits a massless free particle such as a photon. E2 requires uniform motion in that frame. E1 supplies constant velocity over the selected interval. K12 then gives zero trajectory acceleration at an interior instant. This trace never demands a mass. E4 explicitly permits uniform motion without freedom, so the return inference from uniform motion to free-particle status would fail even with a whole interval of motion.
2. **Material object with zero inertial acceleration.** E9 gives zero net force. E10 requires a positive inertial mass and says explicitly that an exact zero-force, zero-acceleration pair leaves its value undetermined. The mass is *actually there* in the precise sense relevant here: denying that A has an inertial mass would break the accepted material-object account. Erasing its numerical value leaves that account coherent. The photon and the material object agree on the acceleration value while carrying different commitments.
3. **Material object with nonzero inertial acceleration.** E7 supplies the trajectory reading. E9 and E10 give the direction and nonzero magnitude status of the net force. There is a less direct deduction too. Suppose A had been free throughout an interval containing the instant in its interior. E2, E1 and K12 would give zero acceleration there, contrary to the premise. The entries support this argument. Whether a trace procedure will *find* it by starting at E7 is a separate question.
4. **B’s gravitational force on A.** There is no concrete gravity headword in the active entry text. Substituting E11’s net force on A loses B and changes the premise. The hand-trace therefore stops before it can establish either participant’s massiveness or the reciprocal force. The project explicitly defers concrete gravity and spring entries. This is a different outcome from the preceding case, where the entries supported a deduction that took some ingenuity to find. [Design 2.1 scope and deferred entries](https://github.com/canvalidk/VD-Newton/blob/61afb9ecf6f17a89ca6425e7e7642d6761531b05/07_design_2_1/CURRENT_STATE.md)

## What the distinction resolves

“Uniform motion,” “zero net force,” and “zero inertial acceleration” ask about different things. Uniform motion asks about an interval in a frame. Net force asks about a material object’s resultant. Zero acceleration can be read from a trajectory, while the Newton II headword also commits the reader to a material object. For a material object in an inertial frame, zero resultant and zero inertial acceleration entail each other at an instant. To conclude uniform motion, the zero must persist throughout the interval. The free photon reaches the kinematic conclusion through Newton I. Once the question, domain, and time span are explicit, the apparent conflict disappears. [Question answering](https://github.com/canvalidk/VD-docs/blob/4d155ba1954f5f44042c81da0f72a2d37e97c108/Core/vd_dictionary_question_answering.md)

This develops the earlier “actually there” work. A law can force a counterpart; admitting an object as a kind can commit us to an attribute whose value nobody requested. A witness sheet can supply facts about the scene. The entries determine what accepting those facts implies. The proposal here gives those commitments a direct role in testing a reconstruction: **starting from exactly this statement, show the path to the consequence, including the point where any extra premise enters.** How to recognise all such paths, especially those requiring a case split or a contradiction, is the outstanding question. The discussion concerns logical consequences within an accepted theory instance. Comparative evidential credit between rival theories remains a separate frontier. [It Is Actually There](https://github.com/canvalidk/VD-docs/blob/4d155ba1954f5f44042c81da0f72a2d37e97c108/Theory/actually_there_prediction_sets/IT_IS_ACTUALLY_THERE.md) · [Witness Sheets, §§4–5](https://github.com/canvalidk/VD-docs/blob/4d155ba1954f5f44042c81da0f72a2d37e97c108/Theory/witness_sheets/witness_sheets.md)

## Mathematics of sentences

Can’s final move was to put the name, version and date of the dictionary at the end of the statement. For example:

> If A is a material object with zero inertial acceleration at this instant, then A has zero net force at this instant, according to Newton v2.1, snapshot of 24 October 2026.

The suffix governs the whole conditional. We can establish this sentence by following E9 and carrying the same A and instant through the multiplication. Whether any particular object in the world satisfies the premise is a further question. The same suffix can be attached to “Does the gravitational force exerted by B on A imply that B has mass?” This time we can point to the precise dictionary in which the starting headword is missing.

Write \(P \vdash_D Q\) for “from sentence \(P\), sentence \(Q\) follows according to this dated dictionary \(D\).” Fixing \(D\) makes the proposed path a claim about a specified object. A later edition can supply a missing path while the claim about this edition remains available for inspection. This is the sense of *mathematics of sentences*: the sentences themselves can describe physical objects, while the relation we examine is the one their named dictionary establishes between them.
