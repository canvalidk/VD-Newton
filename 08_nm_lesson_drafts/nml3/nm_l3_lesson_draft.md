# NML3 Lesson Draft: Force Sum

Status: scaffold only, created 2026-08-02. No lesson wording or entry wording has
been selected.

## Provisional purpose

Open the force-accounting route from the already-installed
`net-force-material-object` entry, define its relation to a closed
`interacting-forces-set` of `impressed-force` members, and make the
construction and closure of that collection trace-visible.

## Entry spine

```text
E9   existing force-sum chimney
E13  net-force-material-object triplet redefine
E14  interacting-forces-set triplet entry
E15  impressed-force triplet entry
E16  interacting-forces-set generator wall
E17  interacting-forces-set closer wall
```

## Lesson sections to draft

1. Opening demand: where a net-force value comes from when it is not supplied.
2. Collection/member distinction: `interacting-forces-set` and
   `impressed-force`, including the acting-object instance as the member key
   and the material object as owner/target rather than key.
3. Vector-sum operation after closure.
4. One-at-a-time positive generation from mechanical composition and why its
   successor form does not terminate itself.
5. Independent final-member determination, including why a matching net-force
   sum cannot exclude further cancelling members.
6. Explicit termination and the empty-collection/zero-vector case.
7. Exit trace and evaluator checks.

## Boundaries

- Do not fill or renumber the reserved E12 inertial-mass wall.
- Do not treat the force collection as a flat unexplained human-supplied list.
- Do not import action-reaction, concrete force laws, or mechanical closure
  before their later blocks.
- Do preserve the acting-object-instance member key for the later
  action-reaction block: the same key cannot be added a second time merely by
  changing its force-role label.
- Do not treat a known force count or a zero residual between the current sum
  and measured net force as a closure witness.
- Do not draft the relocated meta-typing block as part of this first NML3 pass.

The numbering authority is
`NML3_ENTRY_SEQUENCE_DECISION_2026-08-02.md`. The unresolved architectural
questions are recorded in `NML3_ENTRY_WORKING_PLAN.md`.
