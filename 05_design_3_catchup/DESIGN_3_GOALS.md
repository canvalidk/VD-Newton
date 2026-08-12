# Design 3 Goals

## Main Goal

Move Newton v0.6 from a working abstract instance toward a traceable Design 3
instance where force attribution, acting-object dispatch, residual handles, and
human inputs are explicit enough that answers and traces can be produced
cheaply and audited exactly.

## Standing Principles

- The VD gives the answer and the trace; the trace is the answer-production
  route through exposed headwords, residual handles, witness demands, inputs,
  computations, and halts.
- Human/model inputs should land at walls, scaffold entries, concrete entries,
  or explicit residual points, not at triplet entries.
- The dictionary expands headwords; natural-language questions must first be
  normalised to headwords.
- The evaluator is not a physics solver. Its output can be an attributed
  symbolic equation system.
- Acting-object instances are callables declared through
  `mechanical-composition_point-particle`.
- Concrete acting-object entries are dispatch destinations, not informal
  explanations.

## Entry Work Still Standing

1. Rewrite E18, the inertial-frame wall.
   - It should carry the frame commitment as a modelling input.
   - It should explain the protective role: accelerations in this frame
     correspond to real force sources rather than frame artifacts.

2. Revise E20, the inertial-acceleration chimney.
   - It should make the gap from raw `acceleration` load-bearing.
   - It should mark `inertial-acceleration` as the frame-purified quantity
     Newton II consumes.

3. Add an acting-object wall.
   - Recognition should not land at the acting-object triplet alone.
   - The wall should give a peripheral meaning: a force-producing or
     force-contributing callable mechanism possessed through mechanical
     composition.

4. Add an activation-condition wall.
   - The wall should describe activation conditions as physical circumstances
     under which a concrete acting-object's force contribution is coherent.
   - It should not swallow modelling assumptions; those may need separate
     wall treatment.

5. Add or rewrite interacting-forces-set walls.
   - E25 keeps the triplet role.
   - A wall/generator should support one-at-a-time force unfolding.
   - A wall/closer should support explicit "no more acting-objects" closure.
   - No `ao0`.

6. Add concrete acting-object entry clusters.
   - Start with a spring, unless near-earth gravity is needed as an easier
     first dispatch proof.
   - Each cluster needs a type hub, participant slots, concrete activation
     condition, concrete canonical-force rule, constructs, and parameters.

7. Review mechanical-composition.
   - Treat it as scenario declaration, not passive bookkeeping.
   - It is where acting-object instances enter the trace.

8. Add activation-condition parity with paired-particle.
   - Force membership should entail that the activation condition can be
     exhibited.
   - Concrete activation conditions must retain independent checkable content.

9. Keep closure routing deferred.
   - Closure-forced modelling inputs still need homes.
   - Do not solve this before the core acting-object dispatch layer is tested.

10. Add the identity rule to the rule ledger.
    - Entities have user-supplied identity tokens.
    - Equality is token equality.
    - The evaluator does not generate IDs.

## Next Concrete Test

The best next stress test is a spring acting-object cluster.

Target scenario:

```text
A point-particle p of inertial mass m is attached to an ideal linear spring
with spring constant k. The other endpoint or equilibrium construct is fixed.
The particle is displaced by x from equilibrium. Find inertial-acceleration(p).
```

Success is not just returning `a = -kx/m`. The trace must show:

- where the spring instance enters mechanical-composition;
- how the type hub dispatches abstract slots to concrete spring slots;
- where participant slots are filled;
- where modelling assumptions land;
- where `k` enters as a parameter;
- where equilibrium/displacement enters as a construct;
- where the canonical-force rule produces an attributed force;
- how that impressed-force enters the IFS and then the net-force sum.

## Locked-In Later Goal

After Design 3 can produce accountable Newtonian traces, use those traces to
test whether the VD can generate Newtonian prediction sets.

The target is described in `06_newton_analysis/prediction_sets.md`.

In brief: a Newtonian point prediction is only one branch of the honest
prediction set. The VD should be able to expose the other Newton-licensed
branches too: trace-production error, bad inputs, bad frame commitment,
unclosed system, unaccounted acting objects, external influences, approximation
failure, undefined referent, or theory failure.

Success would mean the VD can make theory-protective reasoning auditable. The
question after a failed observation becomes: which licensed branch did the
trace expose, what does that branch now demand, and when have all
Newton-preserving branches become too costly or closed?
