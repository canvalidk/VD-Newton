# NM L1 Decision Note: E7, E8, and Witness-Sheet Composition

**Status:** working decision note  
**Project:** VD Newton / NM L1  
**Purpose:** Record the current decision about how E7 and E8 relate to NM L1, and why the object-design surface should use witness-sheet composition rather than capability-interface language.

---

## 1. Decision Summary

NM L1 should include **E7** but not **E8**.

The lesson should treat E7 as the first explicit naming of acceleration as a **trajectory-read quantity**:

```text
Given a point-particle trajectory in an inertial-frame, read how the motion is changing.
```

NM L1 should not yet open E8, because E8 belongs to the Newton-II-facing route:

```text
If the same target is being treated as a massive-particle, then the trajectory-read acceleration is admitted as the acceleration to be accounted for by Newtonian force-accounting.
```

That step opens `massive-particle`, `inertial-mass`, `net-force`, and eventually `interacting-forces-set`. Those are NM L2 concerns.

The object-design decision is to use **Option C: witness-sheet composition** as the lesson-facing and entry-facing surface.

Option B, capability/interface design, remains useful as an implementation interpretation, but it is not the preferred pedagogical surface.

---

## 2. Why E7 Belongs in NM L1

NM L1 is primarily the Newton I lesson:

```text
free-body + inertial-frame -> uniform-motion
```

Its core question is:

```text
Under what commitments should simple motion appear?
```

Once students understand `uniform-motion`, they also need a lightweight way to name the failure of uniform-motion. A path can fail to be uniform because it curves, speeds up, slows down, or otherwise changes velocity.

That is where E7 belongs.

E7 gives a name to the motion-change visible from the trajectory. It should not be introduced as force-accounting. It should be introduced as a **getter** over the motion description:

```text
trajectory in inertial-frame
  -> velocity-change
  -> inertial-acceleration_point-particle
```

In student language:

```text
Acceleration is what you read when the motion changes.
```

For younger learners this can remain informal:

```text
Is the path still, straight-and-steady, speeding up, slowing down, or turning?
```

For older learners it can become explicit:

```text
Acceleration is read from the trajectory by looking at how velocity changes in the chosen inertial frame.
```

For mathematically ready students:

```text
a(t) = dv/dt = d²r/dt²
```

The important point is that this is still **kinematic**. It says how to read motion. It does not yet say what force, mass, or net-force explains the motion.

---

## 3. Why E8 Does Not Belong in NM L1

E8 opens a different branch.

E7 asks:

```text
What acceleration is read from the trajectory?
```

E8 asks:

```text
Is this target being treated as a massive-particle, so that the trajectory-read acceleration can enter Newtonian force-accounting?
```

That means E8 is not merely “more acceleration.” It is a gate into the massive-particle sheet.

Opening E8 pulls in the following machinery:

```text
massive-particle
inertial-mass
net-force
Newton II
interacting-forces-set
attached-force
acting-object
```

This is too much for NM L1. NM L1 should preserve its pre-force character. It teaches the conditions under which simple paths appear, not the force-accounting machinery used when influences are present.

So the bridge should be:

```text
NM L1:
  What happens when no relevant influence shapes the path?

E7 bridge:
  If motion changes, name that trajectory-read change as acceleration.

NM L2:
  If the target is massive, use force-accounting to explain that acceleration.
```

---

## 4. The E7/E8 Distinction

The distinction should be recorded as:

```text
E7 = motion-sheet getter
E8 = force-accounting sheet link
E9 = Newton II law relation
```

More explicitly:

```text
E7:
  Given a point-particle trajectory in an inertial-frame,
  return the acceleration read from that trajectory.

E8:
  If the same target is being treated as a massive-particle,
  bind the E7 trajectory-read acceleration into the massive-particle
  force-accounting sheet.

E9:
  For a massive-particle, that acceleration is locked to net-force
  and inertial-mass by Newton II.
```

This avoids treating E8 as a second independent acceleration. E8 does not create a new physical quantity. It gives the E7 quantity a new VD role when the object is being treated as massive.

---

## 5. Option B Considered: Capability / Interface Design

Option B would describe the structure as capability interfaces.

For example:

```text
TrajectoryReadable:
  trajectory
  position
  velocity
  acceleration getter

ForceAccountable:
  inertial-mass
  net-force
  interacting-forces-set
  Newton-II-facing acceleration
```

Then a massive-particle would be an object satisfying both:

```text
massive-particle = TrajectoryReadable + ForceAccountable
```

This is precise and useful for implementation. It makes clear that E8 functions like a type-gated adapter:

```text
if target satisfies massive-particle,
then expose the E7 acceleration as the Newton-II-facing acceleration.
```

But this language is less teachable. `Capability`, `interface`, and `adapter` are programming-native terms. They are helpful for us as designers, but they may obscure the lesson for students.

So Option B is retained as an implementation or audit interpretation, not as the primary lesson-facing surface.

---

## 6. Option C Chosen: Witness-Sheet Composition

Option C says:

```text
The same target object can carry multiple VD witness sheets.
```

For example:

```text
same target object:
  point-particle motion sheet
    -> trajectory, position, velocity, trajectory-read acceleration

  massive-particle force-accounting sheet
    -> inertial-mass, net-force, interacting-forces-set, Newton-II acceleration role
```

This is more intuitive for students.

They can understand:

```text
First, fill out the motion sheet.
Then, if the object is massive, open the force-accounting sheet too.
```

This also matches ordinary problem-solving. Students already separate motion information from force information:

```text
Motion information:
  path, position, velocity, acceleration

Force-accounting information:
  mass, forces, net force
```

VD simply makes the separation explicit.

---

## 7. Important Safeguard: One Target, Multiple Sheets

Option C must not be misunderstood as physical composition.

Do **not** say:

```text
A massive-particle contains a point-particle.
```

That sounds as if there are two physical objects.

Say instead:

```text
The same target can be described with a point-particle motion sheet.
If it is also treated as massive, it receives a massive-particle force-accounting sheet.
```

Or:

```text
The massive-particle sheet points back to the motion sheet of the same target.
```

This preserves the central idea:

```text
one target
multiple VD roles
multiple witness sheets
```

---

## 8. Lesson-Facing Version

The student-facing logic should be:

```text
1. Is the path simple?
   If the body is free and the frame is inertial, expect uniform-motion.

2. If the motion is not uniform, how is it changing?
   Read acceleration from the trajectory. This is E7.

3. If the object is massive, what explains that acceleration?
   Open the force-accounting sheet. This is E8 and belongs to NM L2.
```

For NM L1, only steps 1 and 2 are active.

Step 3 is previewed only as future work.

---

## 9. Possible E7 Wording

A provisional E7 wording:

```text
inertial-acceleration_point-particle :=

The inertial-acceleration of a point-particle is the acceleration returned by
that point-particle's trajectory when the trajectory is read in an inertial-frame.
```

A more lesson-facing wording:

```text
The inertial acceleration of a point-particle is the way its motion changes
when its trajectory is read from an inertial frame.
```

Teacher gloss:

```text
Acceleration is read from motion before it is explained by force.
```

---

## 10. Deferred E8 Wording

A provisional E8 wording for NM L2:

```text
inertial-acceleration_massive-particle :=

The inertial-acceleration of a massive-particle is the trajectory-read
inertial-acceleration of the same target, taken as the motion-quantity to be
accounted for by Newtonian force-accounting.
```

Teacher gloss:

```text
For a massive object, the acceleration read from motion is the acceleration
that Newton II must account for using mass and net-force.
```

This should not be active in NM L1.

---

## 11. Boundary Cases Preserved

This decision keeps the important boundary cases clean.

### Photon path question

```text
Question:
  What path does a photon follow in empty space?

Route:
  free-particle / path / trajectory / uniform-motion

Do not route:
  inertial-mass / net-force / Newton II
```

### Puck trajectory question

```text
Question:
  How is the puck's motion changing in the lab frame?

Route:
  point-particle motion sheet -> E7 trajectory-read acceleration
```

### Puck force-accounting question

```text
Question:
  What net-force accounts for the puck's acceleration?

Route:
  massive-particle force-accounting sheet -> E8/E9 -> Newton II
```

### Block on table

```text
Observation:
  trajectory-read acceleration is zero.

But:
  the block is not free, because Earth and table still influence it.

Lesson:
  zero acceleration or uniform-motion does not imply free-body status.
```

---

## 12. Final Decision

Use this division:

```text
NM L1 includes:
  Newton I law-house
  uniform-motion
  free-body / free-particle
  inertial-frame
  E7 as trajectory-read inertial acceleration

NM L1 excludes:
  E8 as massive-particle force-accounting acceleration
  Newton II
  net-force
  inertial-mass
  interacting-forces-set
  force diagrams
```

Use this object model:

```text
Surface model:
  Option C — witness-sheet composition.

Implementation/audit model:
  Option B — capability gates/interfaces.

Rejected model:
  naive inheritance, where later point-particle changes silently mutate
  massive-particle behaviour.
```

Final concise formulation:

```text
E7 names the acceleration read from the motion sheet.
E8, deferred to NM L2, links that same acceleration into the massive-particle
force-accounting sheet.
```
