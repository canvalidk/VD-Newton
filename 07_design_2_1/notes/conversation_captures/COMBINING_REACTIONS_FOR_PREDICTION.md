# Combining Reactions For Prediction

Status: quick concept note for Design 2.1.

One important way to understand the VD is that it combines reliable human
reactions to presented strings into a controlled computation.

A physics theory is not only a set of propositions. It is also a collection of
symbols, words, diagrams, and equations that changes what a trained
interpreter is likely to do. When a person sees `+`, `vector`, `mass`, `F =
ma`, or `measured in kilograms`, those strings act as stimulants. They trigger
partly innate, partly trained, and partly culturally installed behaviours:
adding, substituting, keeping direction, looking for a mass value, assigning
units, drawing a free-body diagram, or preserving an unknown.

The VD tries to make this usable. It does not merely present the whole theory
at once. It presents strings in a controlled order. Each entry exposes the
interpreter to a headword, residual phrase, equation, or wall meaning that
should trigger the next useful behaviour. The trace is the record of those
exposures and responses.

The important point is combination. A single reaction to a single string is
not enough to predict the future. But many small reliable reactions can be
chained:

```text
recognise the target particle
-> find its mass
-> identify the relevant forces
-> preserve vector direction
-> keep an unknown tension symbol
-> bind the paired reaction force to the same unknown
-> write the equation
-> solve
-> predict the motion
```

Each step only needs to increase the probability of the next correct
behaviour. If the sequence is well controlled, the whole chain increases the
probability of a correct prediction.

This gives wall entries their practical importance. A wall entry is a short
string placed where the trace needs the interpreter to perform a useful
operation: substitute a value, classify a particle, recognise a vector, choose
the correct force, preserve an unknown, or notice a modelling commitment. Good
wall entries are not mini-essays. They are compact behavioural triggers inside
the computation of the theory.

In this sense, the VD is a machine for exploiting and combining disciplined
reactions to strings. It turns theory text into an ordered interface for
prediction-producing behaviour.

