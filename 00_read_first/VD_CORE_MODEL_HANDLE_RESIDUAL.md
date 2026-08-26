# VD Core Model - Handles, Residuals, Answer, Trace

Status: working orientation note, 2026-05-01.

This note records the current core understanding of the VD so future work does
not fall back into the weaker reading where the trace is only an audit trail.

## One Sentence

The VD is a lazy answer-producing theory representation: it exposes an
interpreter to the right headwords and residual handles in the right order so
that the interpreter performs the operations needed to produce the answer, and
the trace records that route.

## Answer And Trace

The VD gives the answer and the trace.

The trace is not a substitute for the answer. It is the ordered derivation path
through which the answer is produced. If the expansion terminates cleanly, the
VD output is:

```text
answer + accountable expansion route
```

If the expansion does not terminate cleanly, that failure is also an
answer-type:

```text
undefined referent
contradiction
missing contingent input
random/input boundary
domain boundary
```

The important correction is that the trace is not merely retrospective. It is
the sequence of exposures that makes the answer happen in a disciplined
interpreter.

## Theory Text As A Causal Object

A physics theory can be identified as text or symbolic structure that changes a
competent interpreter's response distribution so that they are more likely to
produce correct predictions and answers.

In this picture, a theory is not first a floating set of propositions. It is a
disciplined causal apparatus:

```text
interpreter + theory text + question/context
  -> shifted response distribution
  -> higher probability of correct answer/prediction
```

The VD tries to make that apparatus explicit and reproducible. It does not dump
the whole theory onto the interpreter at once. It routes demand lazily:

```text
question
  -> normalised headword
  -> demanded entry
  -> demanded daughter headwords
  -> residual handle
  -> operation
  -> next demand
  -> answer or halt
```

## Residuals

Several related things are called residuals. Keep them distinct.

### Residual String

At the token level, a residual is the string left in an entry's definiens after
recognised headwords are removed.

This is the mechanically extractable sense used by the engine:

```text
definition string - matched headwords = residual tokens/string
```

### Residual Handle

The residual string is not mere leftover prose. At a point where the dictionary
cannot reduce further through headword lookup, the residual acts as the handle
for the transformation the interpreter must perform on the information already
available.

When we write:

```text
F = Re_n(m, a)
```

`m` and `a` are the headword-accessible inputs. `Re_n()` is the handle for the
operation installed by entry `n`'s residual. It is a route by which the
interpreter takes up the available inputs and transforms them.

### Residual Causal Effect

For humans and LLMs, the handle is often the stimulant. The symbol on the page
is the thing that changes the interpreter's state.

This is the critical point:

```text
The residual string is the visible stimulant that acts as the operational
handle for a trained text interpreter.
```

In machine-code cases, it can be useful to distinguish physical stimulant,
local handle, and operation more cleanly. In human/LLM text interpretation, the
written residual is the causal grip. Seeing `+` in `3 + 5` strongly routes a
disciplined interpreter toward addition. Seeing a law-entry residual routes the
interpreter toward a modelling operation, if the residual is well written.

### Residual Function

`Re_n()` can also be used as an idealised function handle: the transformation
that entry `n` is supposed to trigger. This does not mean there is a ghostly
meaning-object behind the text. It is a useful abstraction over the causal
effect that a disciplined interpreter undergoes when exposed to the residual.

## Handles And Dossiers

The refined handle derivation note gives the background:

- a stimulant affects a target;
- a local handle routes the target;
- a dossier records what happens under probes;
- discipline stabilises the dossier;
- coarse-graining and a probability budget license a match;
- raw meaning is the convergent dossier-content held at a handle.

The important bridge into VD entry-writing is that a definition string has
authority only insofar as it successfully routes disciplined interpreters. If
the stable dossier of a handle conflicts with a formal definition, the
definition is what needs correction.

## Human Choice Does Not Break The Model

Humans do not respond to words as deterministically as CPUs respond to opcodes,
but they are still causally affected.

If a person hears "jump", they may choose not to jump. But they cannot choose
for the word to have had no effect. The exposure changes their state and shifts
the probability distribution of possible responses. Maybe it raises the chance
of actually jumping by only 1 percent. That is still a physical causal effect.

For highly disciplined handles such as `+` in `3 + 5`, the response
distribution is much tighter. A trained interpreter is strongly routed toward
addition, even if they can later refuse to answer, joke, or make a mistake.

VD residuals aim to be disciplined enough that the intended modelling operation
is reliably triggered under the relevant budget.

## Lazy Exposure

Lazy evaluation is central because it controls exposure order.

The VD does not merely say which concepts exist. It sequences the interpreter's
encounters with them. A headword demand exposes the next relevant entry. That
entry exposes daughter headwords and residual handles. Those exposures trigger
operations and further demands.

This is why trace production and answer production are the same event viewed
from two angles:

```text
answer production: the interpreter is routed through operations
trace production: the route is recorded
```

## Implication For Newton

For Newtonian mechanics, a well-written VD should route a mechanics question
roughly like this:

```text
natural-language question
  -> normalised headword, e.g. inertial-acceleration(p)
  -> point-particle and inertial-frame commitments
  -> Newton II expansion
  -> net-force demand
  -> interaction-set demand
  -> mechanical-composition / acting-object witnesses
  -> activation conditions
  -> canonical forces
  -> force sum
  -> acceleration answer
```

The VD should not merely explain after the fact why a textbook answer was
reasonable. It should be able to run the theory through the interpreter and
produce the answer.

## Entry-Writing Consequence

A good VD entry is not simply a true sentence.

It is interpreter-control machinery. It must:

- expose the right headwords;
- leave the right residual string;
- put the right stimulant at the right point in the lazy demand chain;
- trigger the intended operation in a disciplined interpreter;
- route contingent inputs to visible trace locations;
- either produce an answer or halt in an informative way.

When reviewing entries, ask not only "is this true?" but:

```text
What operation does this string cause the interpreter to perform?
At what point in the demand chain is the interpreter exposed to it?
Does it route the interpreter toward the answer or toward an uncontrolled
physics habit?
```
