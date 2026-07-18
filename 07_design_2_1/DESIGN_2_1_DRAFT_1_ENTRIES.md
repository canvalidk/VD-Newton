# Design 2.1 Draft 1 Entries

Status: Draft 1, compiled 2026-05-20.

## Kinematic Entries

### [K1] time

```text
time :=
A background ordering value, usually modelled by t ∈ R; a time-value selects
an instant, and the difference between two time-values is a duration.
```

### [K2] reference-frame

```text
reference-frame :=
A coordinate-and-clock convention for events: an origin, basis vectors, and a
clock, supplying the coordinates in which displacement and trajectory values
are expressed.
```

### [K3] displacement

```text
displacement :=
A spatial vector with units of length, expressed in a chosen reference-frame.
```

### [K4] straight-line

```text
straight-line :=
A geometric locus in a reference-frame whose displacement-vectors have the form
r0 + λu, with r0 fixed, u nonzero, and λ real.
```

### [K5] path

```text
path :=
A timeless spatial locus or form in a reference-frame, such as a point, straight
line, or curve; it does not yet include particle identity, time, traversal rate,
or a time-indexed map.
```

### [K6] time-interval

```text
time-interval :=
A selected span of time from a start-time to an end-time over which a motion
description is considered; it selects a span, not merely a duration.
```

### [K7] point-particle

```text
point-particle :=
An idealised object whose spatial extent and internal structure are neglected
for the motion description.
```

### [K8] trajectory

```text
trajectory :=
For a point-particle in a reference-frame over a time-interval, a time-indexed
map from selected time-values to displacement-vectors in that frame; this is the
kinematic object from which instant-values and derivatives are read.
```

### [K9] position

```text
position :=
For a point-particle with a trajectory, the displacement-vector returned by that
trajectory at a selected time in the chosen reference-frame.
```

### [K10] velocity

```text
velocity :=
For a point-particle with a trajectory in a reference-frame, the derivative of
that trajectory with respect to time at a selected time, when that derivative
exists.
```

### [K11] speed

```text
speed :=
For a point-particle at a selected time in a reference-frame, the scalar
magnitude of its velocity.
```

### [K12] acceleration

```text
acceleration :=
For a point-particle in a reference-frame, the derivative of velocity with
respect to time at a selected time; equivalently, the second derivative of the
trajectory, when defined.
```

### [K13] relative-position

```text
relative-position :=
For two point-particles in the same reference-frame at the same selected time,
the displacement-vector r2 - r1 obtained by subtracting the first position from
the second.
```

### [K14] relative-velocity

```text
relative-velocity :=
For two point-particles in the same reference-frame at the same selected time,
the derivative of relative-position with respect to time; equivalently, the
second velocity minus the first, when defined.
```

### [K15] path-length

```text
path-length :=
A derived scalar length assigned to a supplied path or to a trajectory over a
time-interval; for a differentiable trajectory, it is the integral of speed over
that interval.
```

### [K16 / E1] uniform-motion

```text
uniform-motion :=
A frame-indexed interval property of a point-particle: over the selected
time-interval, its trajectory either stays at one position in the chosen frame,
or traces a straight path with constant velocity, i.e. constant speed with
unchanged direction. It is a kinematic path-pattern, not yet a claim about why
the motion occurs.
```

## Newton I Entries

### [E2] uniform-motion

```text
uniform-motion :=

Uniform-motion is the motion a free-particle must exhibit when described in an
inertial-frame.
```

### [E3] inertial-frame

```text
inertial-frame :=

An inertial-frame is a reference-frame in which every free-particle must exhibit
uniform-motion.
```

### [E4] free-particle

```text
free-particle :=

A free-particle is a point-particle that must exhibit uniform-motion when
described in an inertial-frame. But a point-particle can exhibit uniform-motion
without being a free-particle.
```

### [E5] inertial-frame

```text
inertial-frame :=

An inertial-frame is the standard reference-frame for Newtonian mechanical
analysis. It is the frame of an observer treated as non-accelerating and
non-rotating. It is sometimes called a Galilean frame or the lab frame. Earth
can be treated as an inertial reference-frame in ordinary circumstances, to the
needed approximation.
```

### [E6] free-particle

```text
free-particle :=

A free-particle or free body is a point-particle whose trajectory is not being
influenced by any other object, i.e. is free from influence. This may be a
material-object represented as a point-particle, or a massless point-particle
like a photon.
```

### [E7] inertial-acceleration_point-particle

```text
inertial-acceleration_point-particle :=

For a point-particle with a trajectory described in an inertial-frame,
the acceleration read from that trajectory at a selected time.
```
