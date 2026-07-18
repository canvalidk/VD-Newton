# Design 2.1 Kinematic Entries - Final Notes

Status: agreed working notes, compiled 2026-05-16.

This note records the agreed Design 2.1 direction for the kinematic entries
before the main entry ledger is edited. The central decision is that `path`
should appear before particle-indexed and time-indexed kinematic entries,
because it recruits a spatial/geometric intuition that should not already
import particle identity or time.

## Core Decision

Kinematic quantities are not absolute bare properties of a particle. They are
properties of a point-particle as described in a reference-frame, often over or
at a selected time.

Use this working phrase:

```text
frame-indexed point-particle property
```

For two-particle quantities, use:

```text
frame-indexed two-point-particle relational property
```

The intuition-building shape is:

```text
path
  -> timeless spatial form/locus in a reference-frame, before particle
     identity and time-indexing

trajectory
  -> time-indexed description of a point-particle's motion
  -> position as trajectory evaluated at a selected time
  -> velocity as derivative of trajectory
  -> speed as magnitude of velocity
  -> acceleration as derivative of velocity / second derivative of trajectory
```

This avoids treating position, velocity, speed, and acceleration as independent
primitive properties, while also keeping the pre-particle and pre-time spatial
path intuition available for `uniform-motion`.

## Agreed Entry Table

| Row | Headword | Property status | Notes |
|---|---|---|---|
| K1 | `time` | Not a point-particle property. | Keep as background time parameter / ordering value. |
| K2 | `reference-frame` | Not a point-particle property. | Keep as coordinate and clock convention. It supplies the frame in which trajectory and displacement values are expressed. |
| K3 | `displacement` | Not itself a point-particle property. | Revise. Treat as a spatial vector with units of length, expressed in a chosen reference-frame. Do not define it as "between positions", because `position` will be defined using displacement. |
| K4 | `straight-line` | Not a point-particle property. | Keep as geometric pattern/object. Useful for `uniform-motion`. |
| K5 | `path` | Timeless, identity-free spatial object relative to a reference-frame. | Add before `time-interval` and before particle-indexed kinematic properties. Treat as a spatial locus/form in a reference-frame. It should not import particle identity, time, traversal rate, or trajectory. |
| K6 | `time-interval` | Not a point-particle property. | Add. This is not `duration`. It selects the span over which a trajectory or motion description is considered. It should carry a start time and end time. |
| K7 | `point-particle` | Object kind. | Keep unchanged. |
| K8 | `trajectory` | Frame-indexed point-particle property over a time-interval. | Add before `position`. Treat as the time-indexed kinematic attribute: a map from time to displacement vectors in the chosen reference-frame over a selected time-interval. This supplies the object needed for position lookup and derivatives. |
| K9 | `position` | Frame-indexed point-particle getter/property at a time. | Revise. Define as evaluation of the particle's trajectory at a selected time: the displacement vector returned by that trajectory in the chosen reference-frame. |
| K10 | `velocity` | Frame-indexed point-particle derivative property at a time. | Add with light revision. Define as the derivative of trajectory with respect to time at a selected time, when that derivative exists. |
| K11 | `speed` | Frame-indexed scalar point-particle property at a time. | Add with no major change. Define as the magnitude of velocity. |
| K12 | `acceleration` | Frame-indexed point-particle derivative property at a time. | Add with no major change, but define through trajectory/velocity: derivative of velocity, or second derivative of trajectory, when defined. |
| K13 | `relative-position` | Frame-indexed two-point-particle relational property at a time. | Add with light note. Difference between two position values in the same reference-frame at the same time. |
| K14 | `relative-velocity` | Frame-indexed two-point-particle relational property at a time. | Add with light note. Derivative of relative-position, or difference between two velocities, in the same reference-frame at the same time. |
| K15 | `path-length` | Derived path/trajectory quantity. | Add or mark optional. It is not a primitive particle property; once a time-interval and trajectory are supplied it can be computed over that interval. |
| K16 | `uniform-motion` | Frame-indexed interval property of a point-particle. | Add as the Newton I chimney. It combines a spatial condition and a temporal condition: rest, or a straight spatial path traversed uniformly over the time-interval. |

## Specific Wording Directions

### K3 Displacement

Do not use:

```text
displacement is the vector between two positions
```

because `position` is being defined in terms of displacement. Use instead:

```text
displacement := A spatial vector with units of length, expressed in a chosen
reference-frame.
```

This lets `position` become a particular use of displacement without circular
definition.

### K5 Path

Path should come before `time-interval` and before particle-indexed kinematic
properties.

Use:

```text
path := A timeless spatial locus or form in a reference-frame.
```

The point of this entry is to trigger spatial/geometric recognition:

```text
point
straight line
curve
```

Do not define `path` using a particle, particle identity, time, traversal rate,
or a time-indexed map. A particle may later be described as following,
occupying, or tracing a path, but the path itself is not yet the particle's
property.

### K6 Time-Interval

Do not collapse `time-interval` into `duration`.

Use:

```text
time-interval := A selected span of time from start-time to end-time over
which a motion description is considered.
```

The important operational role is selection:

```text
time-interval selects the part of the trajectory being considered.
```

### K8 Trajectory

Trajectory should be the first explicitly time-indexed kinematic property.

Use:

```text
trajectory := For a point-particle in a reference-frame over a time-interval,
a map from time to displacement vectors.
```

This makes velocity well-founded, because differentiating requires a
time-indexed map rather than a single isolated position.

### K9 Position

Position should be secondary to trajectory.

Use:

```text
position := The displacement vector returned by a point-particle's trajectory
at a selected time in a chosen reference-frame.
```

So `position` is a getter/evaluation, not the primitive object from which
trajectory is built.

## Dependency Guardrails

- `path` should remain spatial/geometric and should not import particle
  identity or time.
- `trajectory`, `position`, `velocity`, `speed`, `acceleration`, and
  `uniform-motion` should be marked as point-particle properties only in the
  frame-indexed sense.
- `relative-position` and `relative-velocity` require two point-particles, the
  same reference-frame, and the same time.
- `uniform-motion` uses both `path` and `time-interval`: spatially, rest or
  straight path; temporally, uniform traversal.
- `speed` and `acceleration` inherit their reference-frame dependence from
  velocity/trajectory.
- `path-length` is derived from the path/trajectory once the needed interval
  or traversal information is supplied; it is not a primitive particle
  property.

## Open Minor Question

`path-length` was not central in the later conversation, but it remains part of
the Design 2 kinematic scaffold. Keep it in the candidate set unless the next
ledger edit deliberately marks it optional or deferred.
