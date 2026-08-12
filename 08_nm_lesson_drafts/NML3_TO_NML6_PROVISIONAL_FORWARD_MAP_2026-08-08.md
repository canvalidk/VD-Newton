# NML3–NML6 Provisional Forward Map

Status: route-planning scaffold, recorded 2026-08-08. This map does not ratify
lesson boundaries, entry numbers, or the final position of meta-typing and
object-definition entries.

## Why map ahead now

NML3 has exposed dependencies that cross the current lesson boundaries. In
particular, force-sum membership now uses acting-object-instance identities,
while the active ledger currently places the full acting-object block after the
action-reaction block. Design 3 may allow the point at which an object is
defined to move, so a minimal acting-object identity may be slotted before the
force-sum law without requiring the full later acting-object development to
move with it.

The purpose of this map is to expose that dependency pressure. It is not to
freeze a solution before the meta-typing and object-cleanup methods are ready.

## Provisional lesson route

| Lesson | Provisional centre | Current ledger region | Confidence |
|---|---|---|---|
| NML3 | Force-sum membership, generation, and IFS closure | E13–E17 | Active work |
| NML4 | Action-reaction classification and reciprocal force structure | E18–E23 | Provisional |
| NML5 | Acting-object and activation-condition refinement | E24–E29 | Provisional |
| NML6 | Mechanical-system closure and interaction pairing | E30–E35 | Provisional |

The meta-typing block currently appears at E36–E41, but it is not assigned to a
lesson here. Its content and implementation remain under development, and
Design 3 may move object-definition points independently of this provisional
lesson route.

## The movable acting-object seam

The current dependency pressure is:

~~~text
NML3 impressed-force member
    -> needs acting-object-instance identity as its set key

current ledger
    -> places the full acting-object block after action-reaction

Design 3 possibility
    -> insert the minimal entries that define the needed acting-object identity
       before force sum
    -> leave later acting-object entries to refine activation conditions,
       participants, concrete type, and force behaviour
~~~

This gives three live architectural possibilities:

1. **Early minimal identity:** define only enough acting-object identity before
   force sum for NML3 to use it as a key; retain NML5 as the later refinement.
2. **Move the full block:** place the complete acting-object block before force
   sum and renumber/reallocate the later lessons accordingly.
3. **No early entry required:** treat acting-object-instance identity as
   available through the Design 3 object-cleanup mechanism without a separate
   earlier law entry, if the final meta-typing method licenses that use.

The forward map does not choose among these yet. The first option is the current
working preference because it exposes the identity NML3 needs without forcing
unfinished meta-typing or full acting-object semantics into the force-sum
lesson.

## Boundary between NML3 and NML6 closure

The two uses of closure must remain distinct:

- **NML3 IFS closure:** no further acting-object-keyed impressed-force member
  remains for one target and fixed conditions.
- **NML6 mechanical closure:** interaction candidates belonging to a selected
  mechanical system pair appropriately, so the system has no unaccounted
  interaction leak under the theory's closure rules.

Closing one target's IFS is necessary input to later system-level reasoning,
but it is not by itself mechanical-system closure.

## Questions this map is meant to expose

1. What is the minimum content required to make an acting-object instance a
   usable identity before force sum?
2. Does that minimum require an entry, a movable object-definition point, or a
   meta-typing mechanism external to the lesson order?
3. Does the same acting-object instance represent reciprocal roles across two
   target IFSs, or do those roles require distinct instances?
4. What finite or otherwise exhaustive candidate domain lets the NML3 closer
   establish that no further impressed-force member remains?
5. Which later acting-object properties are genuine refinements rather than
   prerequisites for NML3 membership?
6. Does resolving these questions preserve the provisional NML4–NML6 split, or
   require the lesson numbers to move?

## Use of the placeholder folders

The NML4, NML5, and NML6 folders are holding surfaces for dependency notes and
boundary decisions. They must not be treated as proof that their entries,
numbers, or lesson allocations are settled. No lesson prose should be drafted
there until the forward dependency map has been checked.
