# Design 2.1 Kinematic Entry Candidates

Status: working list, created 2026-05-15.

This note lists the kinematic/scaffold entries that Design 2.1 should consider
adding back into the entry structure. The immediate purpose is to make the
remaining kinematic material visible before editing
`DESIGN_2_1_ENTRY_STRUCTURE.md`.

## Source Baseline

Design 2's current operational source is `02_engine/newton.py`.

That file marks:

```text
E1-E14: non-law kinematics scaffold
```

Design 2.1 currently includes only these kinematic rows in the copied ledger:

| Design 2.1 row | Headword | Source |
|---|---|---|
| K1 | `time` | D2[E1] |
| K2 | `reference-frame` | D2[E2] |
| K3 | `displacement` | D2[E5] |
| K4 | `straight-line` | D2[E10] |

So most of the original Design 2 scaffold remains to be added or deliberately
deferred.

## Remaining Design 2 Kinematic Scaffold Entries

These are the missing or not-yet-explicit kinematic entries from Design 2.

| D2 entry | Headword | Design 2 wording summary | Design 2.1 recommendation |
|---|---|---|---|
| E3 | `point-particle` | Idealised object whose extent and internal structure are neglected. | Add. Even with object ownership de-emphasised, many kinematic entries still need a particle target. |
| E4 | `position` | Location of a point-particle at time `t` in a reference-frame, represented by `r(t)`. | Add. This is the main anchor for displacement, velocity, trajectory, and spring-style constructs. |
| E6 | `velocity` | `v(t) = dr/dt`. | Add. Needed for speed, trajectory, uniform motion, and path-length. |
| E7 | `speed` | Scalar magnitude of velocity. | Add. Needed for path-length and uniform-motion wording. |
| E8 | `acceleration` | `a(t) = dv/dt = d^2 r/dt^2`. | Add. Needed as the raw kinematic counterpart to `inertial-acceleration`. |
| E9 | `trajectory` | Map `t -> r(t)` giving position over an interval. | Add. Needed for path/path-like questions and path-length. |
| E11 | `path-length` | Arc length of a differentiable trajectory over an interval. | Add or mark optional. Useful, but less central to Newton II force accounting. |
| E12 | `relative-position` | Difference between positions of two point-particles in the same reference-frame. | Add. Useful for pair, spring, separation, and interaction geometry. |
| E13 | `relative-velocity` | Derivative of relative-position. | Add or mark optional. Useful for contact/friction and relative-motion questions. |
| E14 | `uniform-motion` | Stationary or straight-line motion with constant speed / constant velocity over an interval. | Add as the Newton I chimney, not just a kinematic list item. |

## Already Present But Worth Reviewing

These are already in the Design 2.1 kinematic table, but their wording may need
to become more list-friendly or trace-friendly.

| Headword | Source | Review note |
|---|---|---|
| `time` | D2[E1] | Consider whether `duration` should become its own item or remain inside `time`. |
| `reference-frame` | D2[E2] | May need clearer links to coordinates, clock, and inertial-frame wall. |
| `displacement` | D2[E5] | Should stay general, but may later need scoped variants such as spring displacement. |
| `straight-line` | D2[E10] | Useful for uniform-motion and geometric path claims. |

## Additional Candidate Entries Found In Later Notes

These were not part of the original Design 2 kinematic scaffold, but newer
Design 2.1 / Design 3 notes suggest they may be useful.

| Candidate headword | Why it may be useful | Current recommendation |
|---|---|---|
| `path` | Later notes use `path(photon)` / path questions as distinct from `inertial-acceleration` questions. | Add or define as a question-facing wrapper around trajectory/geometric route. |
| `duration` | D2[E1] includes `delta t`; explicit duration may help traces that need intervals. | Optional. Add if list-style kinematic scaffolding wants interval items. |
| `event` | `reference-frame` assigns coordinates to events, but `event` has no entry. | Optional placeholder. Useful if frame wording becomes more explicit. |
| `coordinate` | Reference-frame wording depends on coordinates. | Optional placeholder. May be too basic unless trace demands it. |
| `interval` | `trajectory`, `path-length`, and `uniform-motion` all use an interval. | Add or placeholder; likely useful for cleaning language. |
| `constant-velocity` | Uniform motion can be expressed as constant velocity. | Optional. Could simplify uniform-motion wording, but may duplicate `uniform-motion`. |
| `relative-displacement` | Useful between `relative-position` and spring/endpoint separation. | Optional. Add only if spring or pair geometry needs it soon. |
| `separation` | Spring and interaction notes often need distance/separation between participants. | Optional construct candidate; likely future-facing. |
| `direction-vector` | `straight-line`, force components, and separation geometry may need direction. | Optional placeholder. |
| `unit-direction` | Spring and contact force formulas often need a unit vector. | Optional, probably later concrete-force work. |
| `endpoint-position` | Spring notes refer to endpoint positions. | Defer unless spring entries are pulled forward. |
| `equilibrium-configuration` | Needed for spring displacement-from-equilibrium. | Defer to spring/construct work. |
| `displacement-from-equilibrium` | Important for simple spring force wording. | Defer unless spring entries are pulled forward. |
| `inertial-acceleration` | Already exists as Newton II chimney, but conversation notes suggest a peripheral substitution-facing treatment. | Do not add to kinematic scaffold; flag for Newton II wall/chimney language cleanup. |

## Recommended First Push

For the next edit to `DESIGN_2_1_ENTRY_STRUCTURE.md`, add the remaining Design
2 scaffold entries in this order:

```text
point-particle
position
velocity
speed
acceleration
trajectory
path-length
relative-position
relative-velocity
uniform-motion
```

Then consider adding a small "Additional kinematic candidates" subsection with:

```text
path
duration
event
coordinate
interval
constant-velocity
relative-displacement
separation
direction-vector
unit-direction
```

Spring-specific constructs should stay deferred for now unless the next editing
round deliberately pulls spring material back in.

