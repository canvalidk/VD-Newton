# NM L1 Lesson Draft: The Path-Problem Behind Newton I, with E7 Motion-Reading

**Status:** integrated working draft  
**Project:** VD Newton / VD Pedagogy  
**Date:** 2026-06-17  
**Lesson length:** 80 minutes, with compressed and extended variants included  
**Core unit:** Newton I law-house plus E7 as the motion-reading bridge  
**Audience range:** adaptable from young learners to introductory undergraduate mechanics  

---

## 0. One-Sentence Thesis

**NM L1 is not a first lesson on forces. It is the installation of the Newton I law-house as a runnable conceptual object, plus the first E7 handle: read motion-change from a path/trajectory before explaining that motion-change by force.**

The central route is:

```text
world of messy paths
  -> influence / free-body contrast
  -> free-body + inertial-frame -> uniform-motion
  -> if motion is not uniform, read how it changes
  -> E7 inertial-acceleration_point-particle
  -> later, in NM L2, force-accounting explains that acceleration
```

The youngest student-facing version is:

```text
First: is the motion simple?
Second: if not, how is the motion changing?
```

The teacher-facing version is:

```text
First: read the motion pattern in a frame.
Second: if uniform-motion fails, identify the velocity-change.
Third: only later, for massive targets, account for that acceleration using force and mass.
```

The student should eventually be able to answer two signature questions:

> A puck appears to curve while no other object influences it. What should you suspect?

Expected VD-native answer:

> If the puck is genuinely a free-body but does not exhibit uniform-motion, suspect that the frame is not inertial. If the frame is inertial, suspect that the puck was misclassified as free.

And:

> A car, leaf, moon, or planet follows a curved path. What is the first thing to do before force-talk?

Expected E7-native answer:

> Watch the path. Draw how the motion is changing. Then ask what might be shaping that change.

That answer is not slogan recall. It is the Newtonian trace made visible.

---

## 1. What Makes This Lesson VD-Native

Most Newtonian Mechanics Lesson 1s start from a statement of Newton's First Law or a list of Newton's three laws. They often say something like:

```text
An object continues at rest or in uniform motion unless acted on by a net external force.
```

That is not the VD-native beginning.

The VD-native beginning is:

```text
Look at the world: almost nothing appears to go straight.
```

Leaves swirl. Balls fall. Cars slow down. Cars turn. Smoke twists. Boats drift sideways in currents. The Moon orbits Earth. Earth orbits the Sun. Mars appears to loop backward in the sky. A puck viewed from a turning frame may appear to bend away from a straight path.

The student first becomes familiar with the problem Newton I solves:

> If real paths are messy, curved, interrupted, and frame-dependent, under what commitments should simple straight-line motion appear?

Newton I is then introduced as a law-house that answers this path-problem:

```text
free-body + inertial-frame -> uniform-motion
```

More completely:

```text
uniform-motion
inertial-frame
free-body
```

These are not three independent vocabulary words. They are three corners of a single law structure.

E7 is then introduced as the immediate bridge:

```text
If motion is not uniform, read how the motion changes.
```

That is the crucial ordering. The lesson does not say:

```text
force causes acceleration, so memorize acceleration.
```

It says:

```text
motion changes are visible before they are explained.
```

This makes acceleration arrive as a thing the student has already learned to *read*.

---

## 2. VD Entry Unit Being Taught

### 2.1 Naming note

The current Newton entry structure uses `free-particle`. For this lesson draft, I use **free-body** as the pedagogical wall-facing handle, because the intended wall meaning includes ordinary massive bodies and path-questions involving massless objects such as photons.

If the final Design 3 entries retain `free-particle`, the lesson can say:

```text
In the formal dictionary this role may be called free-particle.
In the lesson we say free-body because students first meet it as a body/path status.
```

### 2.2 Prerequisites

The lesson begins from ideas students can already grip, at least informally:

```text
object/body
path
curve
straight line
speed
stationary
moving steadily
turning
viewpoint/frame, informally
other objects can affect a path
```

For older students, the same ideas can be named more formally:

```text
point-particle
trajectory
reference-frame
velocity
constant speed
constant velocity
straight-line motion
external influence
```

### 2.3 Kinematic caution: path versus trajectory

For young learners, the handle is usually **path**. That is acceptable as a first wall-facing word.

Teacher-facing precision:

```text
path = timeless spatial curve or locus
trajectory = time-indexed motion of a point-particle in a frame
acceleration = how velocity changes along that trajectory
```

So the turning-arrow worksheet should either:

```text
A. use paths that are implicitly travelled at steady speed, or
B. include equal-time dots so speed changes are visible.
```

For the first young-learner E7 sheet, use equal-time dots sparingly. Do not overexplain them. They are there to protect the later physics.

### 2.4 Active entries

NM L1 installs Newton I and introduces E7 as a motion-reading bridge.

| Structural role | Headword | Lesson wording |
|---|---|---|
| Chimney | `uniform-motion` | Motion that is either stationary or along a straight line at constant speed, described in a chosen frame. |
| Triplet | `uniform-motion` | The motion exhibited by a `free-body` when described in an `inertial-frame`. |
| Triplet | `inertial-frame` | A `reference-frame` in which `free-bodies` exhibit `uniform-motion`. |
| Triplet | `free-body` | A body which, when described in an `inertial-frame`, exhibits `uniform-motion`. |
| Wall | `free-body` | An object whose trajectory is not being influenced by other objects in the modelling context; this can include massive objects and massless path-cases such as photons. |
| Wall | `inertial-frame` | A frame in which the mechanics of particles is understood most simply; most introductory mechanics questions assume such a frame unless stated otherwise. |
| Bridge / next chimney | `inertial-acceleration_point-particle` / E7 | The acceleration read from a point-particle trajectory in an inertial-frame; in lesson language, how the motion is changing. |

### 2.5 E7 wording

Formal entry-facing candidate:

```text
inertial-acceleration_point-particle :=

The inertial-acceleration of a point-particle is the acceleration returned by
that point-particle's trajectory when the trajectory is read in an inertial-frame.
```

Lesson-facing wording:

```text
E7 acceleration is how a point-particle's motion changes when we read its
trajectory from an inertial-frame.
```

Young learner wording:

```text
If the motion is not simple, draw how it is changing.
```

Teacher gloss:

```text
Acceleration is read from motion before it is explained by force.
```

### 2.6 Deferred entries and forbidden active branches

The following should not be taught as active concepts in NM L1:

```text
force
net force
F = ma
mass as inertia
balanced forces
free-body diagrams
normal force
friction as a calculated force
centripetal force
Newton's three laws as a list
detailed force-accounting calculations
E8 inertial-acceleration_massive-particle
E9 Newton II force/mass/acceleration relation
interacting-forces-set
attached-force
acting-object
```

They may be mentioned only as future vocabulary, not as active explanation machinery.

The pre-force handle is **influence**.

Use:

```text
The wind influences the leaf's path.
Earth influences the ball's path.
The road influences the car's path.
The Sun influences Earth's path.
```

Avoid:

```text
The wind exerts a force.
The net force is nonzero.
The car has friction force.
The planet has centripetal force.
```

Those are later entries.

### 2.7 E7/E8 boundary

Use this division:

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

NM L1 includes E7 but not E8.

---

## 3. Core Pedagogical Claim

A conventional lesson often aims for:

```text
Students know Newton's First Law.
Students can say what acceleration is.
```

NM L1 aims for:

```text
Students can run the Newton I trace.
Students have begun to install the E7 motion-reading reaction.
```

The Newton I trace is:

```text
Question about a path
  -> identify motion-pattern demand
  -> inspect free-body commitment
  -> inspect frame commitment
  -> apply Newton I law-house
  -> return uniform-motion, or diagnose which commitment must be questioned
```

The E7 trace is:

```text
Question about non-uniform motion
  -> observe path/trajectory in an inertial-frame
  -> ask whether the motion is simple
  -> if not simple, identify how velocity is changing
  -> return trajectory-read acceleration
```

For young learners, this is installed as:

```text
curving path -> draw inward turning-arrows
```

For older learners, this becomes:

```text
velocity changes if speed changes, direction changes, or both
```

For mathematically ready learners, this becomes:

```text
a(t) = dv/dt = d²r/dt²
```

The important point is that this is still **kinematic**. E7 reads motion. It does not yet explain motion by force.

---

## 4. Learning Objectives

By the end of NM L1, students should be able to:

1. Recognise `uniform-motion` as stationary or straight-line constant-speed motion.
2. Describe the world as full of influenced paths rather than naturally obvious straight paths.
3. Explain `free-body` using the pre-force handle: a body whose path is not being shaped by other objects in the modelling context.
4. Explain `inertial-frame` as the frame in which free-body motion appears simple.
5. State the Newton I triangle:

   ```text
   free-body + inertial-frame -> uniform-motion
   ```

6. Use the triangle diagnostically: if one corner fails, inspect the other commitments.
7. Avoid collapsing Newton I into the zero-force case of Newton II.
8. Avoid saying that uniform-motion automatically implies free-body status.
9. Avoid treating inertial-frame as invisible background.
10. Read simple motion-change before force-talk.
11. For a curved steady-speed path, draw rough arrows toward the inside of the turn.
12. Notice that for circular motion, the turning-arrows point toward the centre.
13. Distinguish the motion-change arrow from the later cause/explanation of that motion-change.
14. Understand that Newton II later explains the E7 acceleration of massive particles.
15. Answer the signature puck question.

---

## 5. The E7 Worksheet Is Not a Test

The E7 worksheet is not a substitute for education and not a memorisation test.

It is a **handle-installation object**.

Its purpose is not:

```text
teach fact -> test recall -> grade correctness
```

Its purpose is:

```text
ordinary ability
  -> disciplined repetition
  -> teacher feedback
  -> installed reaction
  -> later Newtonian use
```

The student already has the primitive abilities:

```text
watch a path
notice a bend
draw an arrow
repeat a mark carefully
enjoy recognition from a teacher
```

The worksheet composes those into a new Newtonian reflex:

```text
curving path -> draw inward motion-change arrows
```

This reflex is not yet the full concept of acceleration. It is the young-learner handle by which E7 later becomes natural.

### 5.1 The worksheet's central sentence

```text
The E7 sheet does not test whether the student already understands acceleration.
It installs the behaviour by which acceleration becomes visible.
```

### 5.2 Teacher feedback target

Reward the trace, not mere correctness.

Use feedback like:

```text
You looked carefully.
You placed the arrow on the bend.
You noticed the arrows gather toward the centre.
You kept going long enough for the pattern to appear.
You checked the path before guessing the cause.
```

Avoid making the sheet feel like:

```text
Correct: acceleration points to centre.
Incorrect: acceleration does not point to centre.
```

The desired moment is:

```text
“I drew all these little arrows...
wait...
they all point to the middle.”
```

That self-noticing is the educational product.

### 5.3 Name of the worksheet

Preferred names:

```text
Motion-Reading Practice Sheet
Path-to-Arrow Installation Sheet
Turning-Arrow Sheet
```

Avoid:

```text
Acceleration Quiz
Centripetal Force Worksheet
Test on Circular Motion
```

Those names open later branches too early.

---

## 6. Criteria of Instillment

Because the worksheet is not primarily an assessment, do not evaluate it only by correct/incorrect answers. The thing being installed is a behaviour.

A teacher can infer that the E7 handle is being installed when the student begins to show the following behaviours.

### 6.1 Basic instillment criteria

| Criterion | Evidence |
|---|---|
| Sustained path attention | Student keeps following the path rather than jumping straight to a verbal answer. |
| Arrow discipline | Student places arrows at many points along the curve, not only one symbolic arrow at the end. |
| Inside-of-turn response | On steady-speed curves, arrows point roughly toward the inside of the turn. |
| Straight-path restraint | On straight steady paths, student does not invent turning-arrows. |
| S-curve sensitivity | On an S-shaped curve, arrows switch sides when the bend switches sides. |
| Circle discovery | On a circle, student notices that all arrows point toward the centre. |
| Transfer | Student can repeat the behaviour on leaves, cars, falling objects, moons, planets, and drawn paths. |
| Cause-delay | Student can draw the motion-change before naming the cause. |
| Path-shaper question | After drawing arrows, student asks what object or environment might be shaping the path. |

### 6.2 Strong instillment criteria

A stronger installation has occurred when the student spontaneously performs this route:

```text
curved or changing motion
  -> draw/read motion-change
  -> ask what the arrows point toward
  -> ask what might be shaping the path
  -> check whether the frame/view might be misleading
```

This is the young-learner seed of Newtonian mechanics.

### 6.3 Longitudinal criterion

The later payoff appears when the student meets Newton II and reacts like this:

```text
F = ma explains the acceleration we already learned how to read from motion.
```

Not:

```text
F = ma is a formula that creates acceleration from nowhere.
```

That is the main delayed outcome.

---

## 7. How E7 Ties Into the Rest of Newtonian Mechanics

E7 is the hinge between Newton I and Newton II.

### 7.1 Newton I

Newton I says:

```text
free-body + inertial-frame -> uniform-motion
```

So NM L1 first trains the student to ask:

```text
Under what commitments should simple motion appear?
```

### 7.2 E7

E7 says:

```text
If the motion is not uniform, read how it changes.
```

So E7 asks:

```text
What acceleration is read from the trajectory?
```

For young learners:

```text
Where is the path turning?
```

For older learners:

```text
How is velocity changing?
```

### 7.3 Newton II

Newton II later asks:

```text
For a massive particle, what accounts for that acceleration?
```

This opens:

```text
massive-particle
inertial-mass
net-force
F = ma
```

### 7.4 Force sum and acting objects

Force-sum later asks:

```text
What acting-force contributions make up the net-force?
```

Acting-object structure later asks:

```text
Which object or mechanism is contributing each force?
```

So the full Newtonian growth route is:

```text
watch path
-> identify uniform or non-uniform motion
-> read E7 acceleration from motion
-> if target is massive, account for acceleration by Newton II
-> decompose net-force by force-sum
-> identify acting objects and activation conditions
```

In young-learner language:

```text
Watch the path.
Draw how it changes.
Ask what is shaping it.
Later, learn the force-language for that shaping.
```

### 7.5 The witness-sheet model

Do not say:

```text
A massive-particle contains a point-particle.
```

Say:

```text
The same target can be described with a point-particle motion sheet.
If it is also treated as massive, it receives a massive-particle force-accounting sheet.
```

Student-facing version:

```text
First fill out the motion sheet.
Later, if the object is massive, open the force-accounting sheet.
```

Motion sheet:

```text
path / trajectory
position
velocity
motion-change
E7 acceleration
```

Force-accounting sheet:

```text
mass
forces
net-force
Newton-II acceleration role
```

---

## 8. 80-Minute Lesson Plan

### Overview table

| Time | Segment | VD purpose | Student output |
|---:|---|---|---|
| 0-5 | Opening puzzle: paths everywhere | Make the path-problem visible | Students notice most paths are not straight and steady. |
| 5-13 | Path gallery | Install influence-vs-path intuition | Students identify what may shape each path. |
| 13-21 | Influence game | Build pre-force `free-body` handle | Students distinguish influenced from not-influenced path cases. |
| 21-30 | Uniform-motion chimney | Ground the November word | Students classify stationary / straight-steady / not uniform. |
| 30-42 | Newton I law-house | Expose the triplet | Students see `free-body + inertial-frame -> uniform-motion`. |
| 42-58 | E7 motion-reading | Install motion-change as a readout | Students draw turning-arrows and notice circle-centre pattern. |
| 58-66 | Sky and orbit transfer | Connect worksheet to astronomy | Students draw arrows for Moon/Earth/Sun path cases. |
| 66-74 | Anti-inversion and trace practice | Prevent false routes | Students diagnose puck, block, turning car, orbit examples. |
| 74-80 | Exit/reflection | Check installed routes without treating it as a memorisation test | Students answer signature prompts and notice what the worksheet was for. |

The compressed lesson must not drop the path gallery or E7 sheet. Those are the installation surfaces.

---

## 9. Segment-by-Segment Draft

## 9.1 Segment 1: Opening Puzzle — The World Is Made of Messy Paths

**Time:** 0-5 minutes

### Teacher aim

Begin with the problem, not the law.

Students should feel:

```text
Straight-line constant-speed motion is not obvious from everyday experience.
```

### Teacher script

> Before we learn any law, I want you to look at motion itself. Think about the paths things take. Do most things around you move in perfect straight lines forever?

Show quick examples verbally or visually:

```text
A leaf in the wind.
A thrown ball.
A car turning.
A car stopping.
The Moon orbiting Earth.
Earth orbiting the Sun.
Smoke curling upward.
Mars appearing to loop backward in the sky.
A boat drifting in a current.
```

Ask:

> If almost nothing seems to go straight, why would anybody ever think straight-line motion is fundamental?

Do not answer yet. Let that question hang.

### Board

```text
Observation:
Most paths we see are curved, interrupted, or changing.

Problem:
When should simple motion appear?
```

---

## 9.2 Segment 2: Path Gallery — Who Is Bending the Path?

**Time:** 5-13 minutes

### Teacher aim

Install the pre-force handle **influence**.

Do not use formal force language yet.

### Activity

Show or describe one path at a time. For each, ask:

```text
1. What is moving?
2. What does its path look like?
3. What other object or surroundings might be influencing that path?
4. What might the path look like if that influence were removed?
```

### Examples

| Moving thing | Observed path | Influence-language answer |
|---|---|---|
| Leaf | Swirls, zigzags, falls irregularly | Wind influences its path. |
| Ball | Falls downward after being thrown | Earth influences its path. |
| Car slowing | Straight path but changing speed | Road/tyres/air influence its motion. |
| Car on curve | Curves with the road | Road and steering system influence its path. |
| Planet | Curves around a star | Star influences its path. |
| Moon | Curves around Earth | Earth influences its path. |
| Smoke | Curls upward | Air currents influence its path. |
| Boat | Drifts sideways | Water current influences its path. |
| Mars in sky | Appears to loop | The viewing frame from Earth affects the apparent path. |

### Teacher script

> Notice the pattern. When paths are messy, curved, or changing, we often ask: what is influencing the path?

> Today we are not yet turning influence into force. Force is later. Today we are asking a more basic question: what would motion look like if a body's path were not being influenced by other objects, and if we watched it from the right kind of frame?

### Board

```text
Path shaped by other objects -> influenced path
Path not shaped by other objects -> free-body candidate
```

---

## 9.3 Segment 3: Influence Game — Birth of the Free-Body Handle

**Time:** 13-21 minutes

### Teacher aim

Install the outward-facing wall handle for `free-body` before the formal triplet.

### Teacher script for younger students

> A free-body is a thing whose path is not being pushed, pulled, blown, blocked, carried, or shaped by other things.

### Teacher script for older students

> A free-body is an object whose trajectory is not being influenced by other objects in the modelling context.

### Important wording

Use:

```text
not being influenced by other objects
not being shaped by other objects
not relevantly affected in this model
```

Avoid:

```text
zero net force
no forces
balanced forces
```

### Mini-drill

Ask students to classify these as free-body candidates or not:

| Case | Free-body candidate? | Reason |
|---|---:|---|
| Leaf in wind | No | Wind influences path. |
| Ball falling near Earth | No | Earth influences path. |
| Car slowing on road | No | Road/tyres influence path. |
| Puck gliding in empty space | Yes, approximately | No relevant path-shaping object. |
| Photon in empty space, for a path question | Yes | It has no inertial-mass route, but its path can be treated as free. |
| Block resting on table | No | Table and Earth influence it, even though it is stationary. |

### Teacher note

The block-on-table example is essential. It prevents the student from thinking:

```text
stationary -> free
```

A stationary object can be heavily influenced.

---

## 9.4 Segment 4: Uniform-Motion Chimney

**Time:** 21-30 minutes

### Teacher aim

Ground the November word: `uniform-motion`.

This should be the easiest formal idea in the lesson.

### Definition

```text
Uniform-motion is motion that is either:
1. stationary, or
2. along a straight line at constant speed.
```

For older students:

```text
Uniform-motion is constant velocity motion in a chosen frame, including zero velocity as the stationary case.
```

### Classification examples

| Case | Uniform-motion? | Why |
|---|---:|---|
| Stone stationary on desk | Yes | Stationary counts. |
| Puck gliding straight at steady speed | Yes | Straight line, constant speed. |
| Car turning at constant speed | No | Direction changes. |
| Planet in circular orbit | No | Direction changes. |
| Ball falling downward faster and faster | No | Speed changes. |
| Smoke curling upward | No | Path and speed vary. |

### Teacher script

> Uniform-motion is a path-pattern. It is not yet a statement about why the path happens. A block on a table may be stationary, so it has uniform-motion, but that does not mean it is free.

### Board

```text
uniform-motion = stationary OR straight-line steady motion

Do not invert:
uniform-motion does not automatically mean free-body.
```

---

## 9.5 Segment 5: The Newton I Law-House

**Time:** 30-42 minutes

### Teacher aim

Expose the triplet as a mutual lock, not as three separate definitions.

### Board diagram

```text
                 uniform-motion
                /              \
               /                \
        free-body -------- inertial-frame
```

Then write the operational route:

```text
free-body + inertial-frame -> uniform-motion
```

### Teacher script

> Newton I is not just a sentence. It is a triangle of ideas. A free-body, watched in an inertial-frame, exhibits uniform-motion.

> The three ideas support one another. If a body is genuinely free and the frame is inertial, the motion should be uniform. If the motion is not uniform, then one of the other commitments must be inspected.

### The three triplet statements

Use these in age-adjusted form.

```text
uniform-motion:
The motion exhibited by a free-body when described in an inertial-frame.

inertial-frame:
A frame in which free-bodies exhibit uniform-motion.

free-body:
A body which, when described in an inertial-frame, exhibits uniform-motion.
```

### Make the circularity explicit

Say:

> These definitions circle around each other. That is not a mistake. That is the law. The point is not to define one word and throw the others away. The point is to learn the structure that holds the three together.

For younger students:

> These three ideas are a team. You do not really get one without the other two.

### Install the walls

Free-body wall:

```text
A free-body is something whose path is not being shaped by other things.
```

Inertial-frame wall:

```text
An inertial-frame is the view from which free things move in the simplest way: still or straight and steady.
```

Older versions:

```text
A free-body is an object whose trajectory is not being influenced by other objects in the modelling context.

An inertial-frame is a reference frame in which the mechanics of particles is understood most simply. Most introductory mechanics questions assume such a frame unless stated otherwise.
```

---

## 9.6 Segment 6: E7 Motion-Reading — From Path to Arrow

**Time:** 42-58 minutes

### Teacher aim

Install E7 as a motion-change reader without opening force-accounting.

### Board

```text
First: is the motion simple?
Second: if not, how is the motion changing?
```

Then:

```text
E7:
trajectory in inertial-frame
  -> velocity-change
  -> acceleration read from motion
```

For young learners:

```text
curving path -> draw where the motion is turning
```

### Teacher script

> We have learned that free bodies in an inertial-frame move simply: still or straight and steady. But many motions are not simple. When motion is not simple, we do not jump straight to force. First we read the motion-change.

> For today, when a path bends, draw a small arrow toward the inside of the bend. Do this again and again along the path. Do not worry about force yet. Just read how the motion is changing.

### Important young-learner phrasing

Use:

```text
draw the turning-arrow
where is the path bending?
where is the motion turning?
follow the path carefully
```

Avoid at first:

```text
draw the force
draw the centripetal force
draw the exact acceleration vector
```

The first worksheet trains the turning part of acceleration. Later lessons add speed-change.

### Technical teacher note

For constant-speed turning:

```text
acceleration points toward the inside of the turn
```

For a straight path with changing speed:

```text
acceleration points along the path if speeding up
acceleration points backward along the path if slowing down
```

For a path that turns and changes speed:

```text
acceleration combines direction-change and speed-change
```

Do not give young learners the full vector decomposition unless they are ready. But do not say anything that would make them believe acceleration always points toward the inside of the path.

---

## 9.7 Segment 7: The Path-to-Arrow Installation Sheet

**Time:** included inside Segment 6 or assigned as repeated practice

### Instruction printed on the sheet

```text
At each marked point, draw a short arrow showing where the motion is turning.
If the path is straight and steady, draw no turning-arrow.
Keep going until you notice a pattern.
```

### Sheet progression

| Page / row | Path type | Student action | Intended noticing |
|---|---|---|---|
| 1 | Straight line with equal dots | Draw no turning-arrows | Straight steady motion has no turning-change. |
| 2 | Gentle curve | Draw arrows toward inside of curve | Curving means direction is changing. |
| 3 | Tighter curve | Draw stronger/more inward arrows | Tighter bend means stronger turning-change. |
| 4 | S-shaped curve | Arrows switch sides | The direction of turning can change. |
| 5 | Circle | Arrows all point inward | Circular motion changes toward the centre. |
| 6 | Car turning | Arrows toward inside of road curve | The road/tyres are path-shaper candidates. |
| 7 | Moon around Earth | Arrows roughly toward Earth | Orbiting motion is continually turning inward. |
| 8 | Earth around Sun | Arrows roughly toward Sun | The same reading scales to astronomy. |
| 9 | Falling object with equal-time dots spreading | Arrows downward along path | Motion can change by speeding up even on a straight path. |
| 10 | Mars apparent loop | Mark the apparent path and ask about frame | Some sky paths are frame/view effects. |

### Teacher role

The teacher should walk around rewarding the process:

```text
careful looking
many arrows
noticing the pattern
asking what the arrows point toward
not jumping to memorised force words
```

The teacher should not present the sheet as a high-stakes correctness test.

### Expected discovery

By the bottom of the circle page, the student should be able to say something like:

```text
The arrows point to the middle.
```

Then the teacher can say:

```text
Yes. When motion goes around a circle at steady speed, the motion-change points toward the centre.
Later we will learn how Newtonian mechanics explains that motion-change.
```

---

## 9.8 Segment 8: Sky and Orbit Transfer

**Time:** 58-66 minutes

### Teacher aim

Show that the same path-reading behaviour applies to astronomy.

This is not a lesson in orbital mechanics yet. It is a transfer of the E7 handle.

### Examples

#### Moon around Earth

Student action:

```text
Draw turning-arrows along the Moon's orbit.
Notice that they point roughly toward Earth.
```

Teacher language:

> The Moon's path is not straight. Its motion is continually changing direction. The arrows point toward Earth, so Earth is a candidate path-shaper.

Avoid:

```text
The centripetal force is mv²/r.
```

That belongs later.

#### Earth around Sun

Student action:

```text
Draw turning-arrows along Earth's orbit.
Notice that they point roughly toward the Sun.
```

Teacher language:

> The same path-reading move works at a larger scale. The path bends around the Sun, so the motion-change points inward toward the Sun.

#### Moon's full path around the Sun

Teacher caution:

```text
Do not make young learners handle all orbital layers at once.
```

Use this phrase:

```text
Sometimes one path-pattern rides on a bigger path-pattern.
```

Layer the drawings:

```text
Moon around Earth:
  turning-arrows roughly toward Earth.

Earth/Moon system around Sun:
  turning-arrows roughly toward Sun.

Full Moon path around Sun:
  combined motion; keep this for older students.
```

#### Mars retrograde

Teacher language:

> Sometimes a sky path looks strange because of the frame we are watching from. Before inventing a cause, inspect the frame.

This connects directly back to the signature puck question.

### Rationality transfer

Do not turn this into a lesson mocking astrology or folk belief. The more precise aim is:

```text
When someone makes a physical claim about the sky affecting something,
ask what path is changing, what motion-change is visible, and what frame is being used.
```

This trains disciplined wonder rather than superstition or anti-superstitious sneering.

---

## 9.9 Segment 9: Anti-Inversion and Boundary Drills

**Time:** 66-74 minutes

### Teacher aim

Prevent common wrong routes.

### Drill 1: Does uniform-motion imply free-body?

Ask:

> A block is stationary on a table. It has uniform-motion. Is it a free-body?

Expected answer:

```text
No. It is stationary, so it has uniform-motion, but Earth and the table influence it. Uniform-motion does not imply free-body.
```

### Drill 2: Does constant speed imply uniform-motion?

Ask:

> A car drives around a circular track at constant speed. Is it in uniform-motion?

Expected answer:

```text
No. Its speed is constant, but its direction changes, so its path is not straight.
```

E7 follow-up:

```text
Draw the turning-arrows.
They point toward the inside of the curve.
```

### Drill 3: Does curved path always mean influenced body?

Ask:

> A puck appears to curve, but you are told no object influences it. What should you inspect?

Expected answer:

```text
The frame. If the body is free and the path is not uniform, the frame may not be inertial.
```

### Drill 4: Can a massless thing be a free-body?

Ask:

> Can a photon in empty space be treated as a free-body for a path question?

Expected answer:

```text
Yes, for a path question. Do not route the question through inertial-mass or Newton II acceleration. The path question can use the free-body/Newton I route.
```

### Drill 5: Does drawing an inward arrow explain the motion?

Ask:

> If you draw arrows toward the centre of a circular path, have you explained the cause yet?

Expected answer:

```text
No. We have read how the motion changes. The cause/explanation comes later.
```

### Drill table

| Scenario | Uniform-motion? | E7 readout | Free-body? | Inertial-frame? | Main lesson |
|---|---:|---|---:|---:|---|
| Isolated puck gliding in lab | Yes | zero | Yes, approximately | Yes, approximately | Clean Newton I case. |
| Block resting on table | Yes | zero | No | Yes | Uniform-motion does not imply free-body. |
| Car moving straight at constant speed | Yes | zero | Usually no | Yes | Maintained motion may still involve influences. |
| Car turning at constant speed | No | inward turning-change | No | Yes | Constant speed is not enough. |
| Ball falling near Earth | No | downward speed-change | No | Yes | Earth influences trajectory. |
| Photon in empty space, path question | Yes | zero path-change in inertial frame | Yes | Yes/path framing | Free-body need not mean massive body. |
| Free puck viewed from accelerating train | Appears no | apparent acceleration | Yes | No | Non-inertial frame can make free motion appear non-uniform. |
| Moon around Earth | No | inward toward Earth, in simplified layer | No | approximately | Orbiting motion is changing direction. |

---

## 9.10 Segment 10: Exit / Reflection

**Time:** 74-80 minutes

These are not memorisation tests. They are diagnostic prompts for whether the route is becoming installed.

Give some or all of these:

```text
1. A puck appears to curve while no other object influences it. What should you suspect?

2. A block sits still on a table. Is it a free-body? Explain without using the word force.

3. What are the three corners of Newton I in today's lesson?

4. Why is a car turning at constant speed not in uniform-motion?

5. On a circular path, where did your turning-arrows point?

6. Did those arrows explain the cause of the motion, or only read the motion-change?

7. What question should you ask after drawing motion-change arrows?
```

Expected high-quality responses:

1. Inspect the frame; it may not be inertial. If the frame is inertial, the body may not really be free.
2. No. It is stationary, but Earth/table influence its path/status; stationary does not mean free.
3. `free-body`, `inertial-frame`, `uniform-motion`.
4. Direction/path changes; uniform-motion requires stationary or straight-line steady motion.
5. Toward the centre.
6. Only read the motion-change; cause/explanation comes later.
7. What might be shaping the path? Or: is the frame/view misleading?

---

## 10. Rubrics and Diagnostics

## 10.1 Signature Newton I question rubric

Question:

```text
A puck appears to curve while no other object influences it. What should you suspect?
```

| Level | Response | Interpretation |
|---:|---|---|
| 0 | “There must be a force/friction/hidden push.” | Premature force import; does not use NM L1 structure. |
| 1 | “Maybe something is influencing it.” | Notices free-body issue but ignores frame possibility. |
| 2 | “Maybe the frame is wrong/non-inertial.” | Correct main diagnosis but thin trace. |
| 3 | “If no object influences it, suspect a non-inertial frame.” | Good use of held free-body commitment. |
| 4 | “Newton I says free-body + inertial-frame gives uniform-motion. Since free-body is given but uniform-motion fails, inspect inertial-frame; if the frame is inertial, inspect the free-body classification.” | Full trace competence. |

## 10.2 E7 installation diagnostic

Prompt:

```text
Here is a path. Draw how the motion is changing.
```

| Level | Behaviour | Interpretation |
|---:|---|---|
| 0 | No arrow discipline; guesses words or waits for formula. | E7 handle not installed. |
| 1 | Draws one memorised arrow on circle only. | Some recall, weak path-reading. |
| 2 | Draws inward arrows on simple curves with prompting. | Beginning installation. |
| 3 | Draws arrows along multiple curves and notices inside-of-turn pattern. | Useful young E7 handle installed. |
| 4 | Transfers to cars, moons, falling bodies, and frame-effect cases; distinguishes readout from cause. | Strong E7 bridge competence. |

## 10.3 Error categories to track

| Error type | Example | VD interpretation |
|---|---|---|
| Premature force import | “There must be a force.” | Student opened downstream force branch. |
| Frame erasure | “Free things move straight,” with no frame condition. | Student lost inertial-frame corner. |
| Inversion error | “It moves uniformly, so it is free.” | Student reversed the law route. |
| Mass contamination | “A photon cannot be free because it has no mass.” | Student routed path question through Newton II/mass. |
| Newton II collapse | “Newton I is just F=ma with F=0.” | Student collapsed separate law-houses. |
| Dangling slogan | “Inertial frames are non-accelerating frames,” with no use-rule. | Student has memorised a handle that does not route. |
| Object/frame collapse | “The puck curves, so it is not free,” with no frame inspection. | Student cannot distribute pressure across commitments. |
| Arrow-as-force collapse | “The arrow is the force.” | Student collapsed E7 readout into force-accounting. |
| Path-only overreach | “Any curve gives the whole acceleration.” | Student has not separated path from trajectory/speed. |
| Centre-memorisation | “Acceleration points to the centre” for every case. | Student memorised circle result without reading local motion-change. |

---

## 11. 40-Minute Compressed Version

| Time | Segment | Keep | Cut |
|---:|---|---|---|
| 0-5 | Path gallery | Leaf, ball, car, Moon, retrograde path | Most extra examples |
| 5-11 | Influence vs free-body | Pre-force influence handle | Extended classification table |
| 11-17 | Uniform-motion | Stationary / straight steady classification | Long edge cases |
| 17-26 | Newton I triangle | Law-house and walls | Detailed circularity explanation |
| 26-35 | E7 turning-arrow sheet | Straight, curve, S-curve, circle | Full orbit layering |
| 35-40 | Diagnostic reflection | Puck, block, turning car, circle arrows | Photon if time short |

The compressed lesson must still preserve the full conceptual route:

```text
messy paths
-> influence
-> free-body
-> uniform-motion
-> inertial-frame
-> E7 motion-change readout
```

Do not compress by dropping the path gallery or the arrow sheet. Those are the installation surfaces.

---

## 12. Extended Multi-Day Version

A stronger implementation can spread NM L1 over multiple short sessions.

### Day 1: Path-world

```text
watch paths
name influences
sort simple / not simple
```

### Day 2: Newton I law-house

```text
free-body
inertial-frame
uniform-motion
signature puck question
```

### Day 3: E7 path-to-arrow sheet

```text
straight
curve
S-curve
circle
student notices centre pattern
```

### Day 4: Sky paths

```text
Moon around Earth
Earth around Sun
Mars retrograde
frame suspicion
```

### Day 5: Bridge forward

```text
motion sheet first
force-accounting later
what F = ma will eventually explain
```

This version better matches the claim that the worksheet installs a behaviour. Instillment benefits from repetition and teacher feedback.

---

## 13. Age-Adapted Handles

The structure should remain stable across ages. What changes is the local handle.

| VD role | Young learner handle | Teen handle | Undergraduate handle |
|---|---|---|---|
| path / trajectory | path | path/trajectory | trajectory `r(t)` |
| influence | what is changing its path? | external influence | relevant external interaction |
| free-body | nothing is shaping its path | trajectory not influenced by other objects | free-particle/free-body status in modelling context |
| inertial-frame | the view where free things move simply | frame where free bodies move uniformly | reference frame satisfying Newton I criterion |
| uniform-motion | still or straight and steady | stationary or straight at constant speed | constant velocity in chosen frame |
| E7 acceleration | how the motion changes | velocity-change read from trajectory | `a(t)=dv/dt=d²r/dt²` |
| turning acceleration | arrow toward inside of bend | normal component of acceleration | curvature/normal acceleration |
| speed-change acceleration | speeding up / slowing down arrow | tangential component | tangential acceleration |
| diagnostic trace | which promise broke? | which assumption failed? | which commitment is inconsistent with the observed trajectory? |

### Young learner phrasing

```text
Most paths are bent because something is messing with them.
A free-body is one whose path is not being messed with.
In the right view, a free-body is still or goes straight steadily.
If motion is not simple, draw how it is changing.
If it curves, draw arrows toward the inside of the turn.
If the arrows all point to something, ask what might be shaping the path.
If a free thing still looks curved, maybe you are watching from the wrong view.
```

### Teen phrasing

```text
Uniform-motion means constant velocity: stationary or straight-line constant-speed motion.
If velocity changes, there is acceleration.
Velocity can change because speed changes, direction changes, or both.
A curved constant-speed path has acceleration because direction changes.
```

### Undergraduate phrasing

```text
Newton I is not merely the zero-force limit of Newton II. It is the law-house that locks the status of a free-particle, the selection of an inertial-frame, and the observation of uniform-motion. E7 then names the acceleration read from a point-particle trajectory in an inertial frame. For a massive target, NM L2 binds that E7 readout into the Newton II force-accounting sheet.
```

---

## 14. Teacher Warnings

### 14.1 Do not say “no net force” in the first pass

The phrase `net force` belongs to later entries.

Use:

```text
No other object is influencing the path.
```

Do not use:

```text
The net force is zero.
```

### 14.2 Do not use free-body diagrams

A free-body diagram opens the force-sum branch. NM L1 is pre-force.

The student must first learn:

```text
free-body as path-status
```

before learning:

```text
free-body diagrams as force-accounting tools
```

### 14.3 Do not define inertial-frame only as “non-accelerating frame”

That wording can become a dangling slogan. It may be useful later, but NM L1 should define the role by the law-house:

```text
An inertial-frame is the frame in which free-bodies exhibit uniform-motion.
```

The wall meaning can then say:

```text
It is the frame in which particle mechanics is understood most simply.
```

### 14.4 Do not let uniform-motion become evidence of freedom by itself

Keep repeating:

```text
free-body + inertial-frame -> uniform-motion
```

not:

```text
uniform-motion -> free-body
```

The block-on-table example should appear at least twice.

### 14.5 Do not let the E7 arrow become a force arrow

Use:

```text
This arrow reads how the motion is changing.
Later we will learn what explains that change.
```

Avoid:

```text
This is the force.
```

### 14.6 Do not teach “centripetal force” in NM L1

The young circle result is:

```text
constant-speed circular motion has inward motion-change
```

not:

```text
centripetal force equals mv²/r
```

That comes later.

### 14.7 Do not let students think acceleration always points inward

For turning-only motion, inward arrows are correct.

But acceleration can also come from speed-change:

```text
speeding up on a straight path -> acceleration along the path
slowing down on a straight path -> acceleration opposite motion
turning and speeding up -> combined acceleration
```

### 14.8 Do not collapse Moon/Earth/Sun layers too early

Use separate layers:

```text
Moon around Earth
Earth/Moon system around Sun
full Moon path around Sun
```

Young learners can understand the first two layers separately before combining them.

### 14.9 Do not let the lesson become historical trivia or anti-superstition rhetoric

Historical struggle can motivate the lesson, but the aim is not history. Astronomy transfer can support rationality, but the aim is not to mock beliefs.

The aim is trace competence:

```text
watch path
read motion-change
ask about path-shaper
check frame
```

---

## 15. Auditable Composition / Handle Provenance Note

This lesson deliberately installs handles that later entries may rely on.

The key installed handles are:

| Phrase / handle | Backing of expected reaction | Role |
|---|---|---|
| influence | Lesson-installed pre-force handle | Lets students speak of path-shaping before force. |
| free-body | Lesson-installed wall handle | Lets students identify a body whose path is not being shaped by other objects. |
| inertial-frame | Lesson-installed frame handle plus stock mechanics use | Lets students ask whether the view/frame is the one where free things move simply. |
| uniform-motion | Kinematic handle | Names stationary or straight steady motion. |
| turning-arrow | Lesson-installed E7 handle | Lets young learners mark direction-change along a path. |
| motion-change | Lesson-installed bridge handle | Lets acceleration be read before force-accounting. |
| path-shaper | Informal extension of influence | Lets students ask what object/environment may be responsible without saying force. |
| artifact of the frame/view | Scientific-culture and lesson-installed frame diagnostic | Lets students inspect frame-effects such as Mars retrograde or accelerating train cases. |

Entry-writing consequence:

```text
A later entry or teacher script may lean on these reactions only for students who have passed through the lesson.
```

Do not hide novel machinery inside an entry string. If a new phrase is doing definitional work, either install it through pedagogy, promote it to an entry, or replace it with already-installed wording.

---

## 16. Why the Path Opening Matters

The path opening is not decorative. It is the motivation for the law-house and for E7.

Without the path opening, Newton I sounds like a bland authority statement:

```text
Objects move straight unless acted on.
```

With the path opening, Newton I becomes a response to a real observational puzzle:

```text
The world presents messy paths.
Newton I tells us the commitments under which simple paths appear.
```

The student now understands why the law is not obvious:

```text
Raw experience does not show free-body inertial motion cleanly.
It shows influenced paths inside imperfect frames.
```

The law is therefore a purification procedure:

```text
remove relevant object-influences
choose an inertial frame
then uniform-motion appears
```

E7 then handles the remaining question:

```text
when motion is not uniform, read the motion-change
```

That is the intellectual drama of NM L1.

---

## 17. Consensus Deviation

| Standard NM L1 | VD-native NM L1 with E7 |
|---|---|
| Starts with Newton's laws. | Starts with a gallery of paths. |
| Treats Newton I as a statement about force. | Treats Newton I as a law-house about path, body-status, and frame-status. |
| Introduces `net force` early. | Uses pre-force `influence` and delays formal force. |
| Treats inertial frames as background. | Makes inertial-frame a central winter word. |
| Treats free-body as preparation for free-body diagrams. | Treats free-body as trajectory-status before force accounting. |
| Asks students to memorise “unless acted upon.” | Asks students to diagnose which corner of the triangle failed. |
| Often collapses Newton I into Newton II. | Keeps Newton I and Newton II as distinct law-houses. |
| Gives acceleration as a formula. | Installs acceleration first as motion-change read from trajectories. |
| Uses examples to illustrate the law. | Uses examples as probes of whether the trace runs. |
| Uses worksheets as tests. | Uses the E7 sheet as a handle-installation ritual. |

The sharpest deviation:

> NM L1 does not teach force. It teaches the motion-reading stage on which force-talk will later become simple.

---

## 18. Optional Research Test

This lesson can be used to test the VD pedagogy hypothesis.

### 18.1 Hypothesis

Students trained with the path-to-arrow E7 sheet before formal force-accounting will later produce fewer dangling explanations, fewer premature force imports, and less confusion about circular acceleration and Newton II than students taught by verbal/formulaic acceleration instruction alone.

A compact prediction:

```text
students trained to draw motion-change arrows on paths
will later find circular acceleration, orbits, and Newton II less mysterious
than students who only receive verbal/formulaic instruction.
```

### 18.2 Test design

Group A receives a conventional lesson:

```text
Newton I as no-net-force / constant-velocity statement.
Acceleration introduced by formula or teacher declaration.
```

Group B receives the VD-native lesson:

```text
path gallery
influence vs free-body
uniform-motion chimney
Newton I triangle
walls for free-body and inertial-frame
E7 path-to-arrow installation sheet
diagnostic trace practice
```

### 18.3 Pre/post questions

```text
1. What is a free-body?
2. What is an inertial-frame?
3. Is Newton I just the zero-force case of Newton II?
4. A puck appears to curve while no other object influences it. What should you suspect?
5. A block sits still on a table. Is it free?
6. Can a photon in empty space be treated as free for a path question?
7. A car moves around a circle at constant speed. Is it accelerating?
8. Draw arrows showing how the Moon's motion changes as it orbits Earth.
9. Have those arrows explained the cause, or only read the motion-change?
10. When a sky path looks strange, what should you check before inventing a cause?
```

### 18.4 Measured outcome

Do not only measure correct/incorrect.

Code error types:

```text
premature force import
frame erasure
inversion error
mass contamination
Newton II collapse
dangling slogan
object/frame collapse
arrow-as-force collapse
path-only overreach
centre-memorisation
```

The VD prediction is that the error distribution changes.

### 18.5 Longitudinal outcome

The most important test may occur later, when students first encounter Newton II:

```text
Does the student treat acceleration as something already read from motion,
or as an alien symbol introduced by F = ma?
```

---

## 19. Bridge to NM L2

NM L1 ends before force-accounting.

NM L2 can begin by saying:

> Last lesson, we learned that other objects can influence paths, and we learned how to read motion-change before explaining it. Today we introduce the formal Newtonian machinery for accounting for those influences in massive particles.

Possible NM L2 target:

```text
inertial-acceleration_massive-particle / net-force / inertial-mass
```

The bridge is:

```text
NM L1:
What happens when no relevant influence shapes the path?
If motion is not uniform, how do we read the motion-change?

NM L2:
For massive particles, how do we account for that acceleration?
```

This preserves the VD order:

```text
path-problem
-> free-body/inertial-frame/uniform-motion
-> E7 inertial-acceleration_point-particle
-> E8 inertial-acceleration_massive-particle
-> Newton II: net-force/inertial-mass/inertial-acceleration
-> force-sum
-> acting-objects
```

The key NM L2 sentence:

```text
F = ma explains the acceleration the motion sheet already returned.
```

---

## 20. Printable Student Sheet

## 20.1 Path gallery table

| Moving thing | What does the path look like? | What might be influencing it? | What if the influence were removed? |
|---|---|---|---|
| Leaf |  |  |  |
| Ball |  |  |  |
| Car stopping |  |  |  |
| Car turning |  |  |  |
| Moon |  |  |  |
| Earth |  |  |  |
| Smoke |  |  |  |
| Puck |  |  |  |
| Mars in sky |  |  |  |

## 20.2 Newton I triangle

Fill in the corners:

```text
                 __________________
                /                  \
               /                    \
      __________________      __________________
```

Write the route:

```text
__________________ + __________________ -> __________________
```

## 20.3 E7 path-to-arrow sheet

Instructions:

```text
Follow the path.
At each marked point, draw a short arrow showing where the motion is turning.
If the path is straight and steady, draw no turning-arrow.
Keep going until you notice a pattern.
```

Rows to print/draw:

```text
1. straight line with equal dots
2. gentle curve
3. tighter curve
4. S-curve
5. circle
6. car turning
7. Moon around Earth
8. Earth around Sun
9. falling object with equal-time dots
10. apparent Mars loop
```

Reflection:

```text
What did you notice about the circle?


What did the arrows point toward in the Moon example?


Did the arrows explain the cause, or only show how the motion changed?


What should you ask next?


```

## 20.4 Motion sheet

```text
MOTION SHEET

Target:
Frame / view:
Observed path or trajectory:

1. Is the motion simple?
   [ ] still
   [ ] straight and steady
   [ ] not simple

2. If not simple, how is it changing?
   [ ] speeding up
   [ ] slowing down
   [ ] turning
   [ ] changing speed and direction

3. E7 readout:
   [ ] zero motion-change
   [ ] nonzero motion-change
   Direction, if visible:

4. Free-body / influence question:
   [ ] free-body candidate
   [ ] influenced path
   [ ] not sure

5. Frame question:
   [ ] frame seems ordinary/inertial enough
   [ ] frame may be misleading
   [ ] not sure

6. Future Newton II question:
   What might account for this acceleration later?
```

## 20.5 Exit answer

Question:

```text
A puck appears to curve while no other object influences it. What should you suspect?
```

Answer:

```text



```

---

## 21. Final Teacher Summary

At the end, say:

> Today we did not learn how to calculate forces. We learned the stage on which Newtonian mechanics becomes simple.

> The world shows us messy paths. Newton I tells us that if a body is free and the frame is inertial, the path is uniform: stationary or straight and steady.

> When motion is not uniform, we first read how it changes. That is the beginning of acceleration. Drawing the arrows is not the explanation yet. It is how we find the thing that later needs explaining.

> So when a free body does not look uniform, do not immediately hunt for a formula. Ask which commitment failed: is the body really free, or is the frame really inertial? And when a path bends, first draw the motion-change before naming the cause.

The final board should read:

```text
Newton I law-house:

free-body + inertial-frame -> uniform-motion

E7 bridge:

if motion is not uniform
  -> read how velocity changes
  -> acceleration from the motion sheet

If uniform-motion fails:
  inspect free-body status
  inspect inertial-frame status

If acceleration is read:
  do not call it force yet
  force-accounting comes later
```

---

## 22. Working Summary

NM L1 is the first demonstration of VD pedagogy inside Newtonian mechanics.

It teaches a closed law-house rather than a textbook slogan. It begins from the path-problem: the world appears full of curved, interrupted, influenced, and frame-dependent paths. It then installs the pre-force handle `influence`, the wall concept `free-body`, the chimney concept `uniform-motion`, and the frame concept `inertial-frame`. The lesson culminates in the student being able to run the diagnostic trace:

```text
free-body + inertial-frame -> uniform-motion
```

The E7 addition gives the student the next handle:

```text
If motion is not uniform, read how it changes.
```

For young learners, this is installed through the boring but powerful ritual of drawing turning-arrows along paths until the pattern becomes visible. The worksheet is not a test of memorisation. It is a connection that can only be instilled: an ordinary drawing ability is disciplined, rewarded, and linked to the larger Newtonian architecture.

The delayed payoff is that Newton II later arrives as an answer to a prepared question:

```text
We have read an acceleration from the motion.
Now what accounts for it?
```

A student who reaches that question has not merely memorised a formula. They have learned where the formula attaches.
