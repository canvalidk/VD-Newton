# Design 3 entry structure

Use one row per proposed definition. A headword can have several definitions, each with its own role. When a definition enters the [Python dictionary](newton_design_3.py), record its position here. The Python list gives the exact wording and order.

The K labels follow the [Design 2.1 kinematic draft](https://github.com/canvalidk/VD-Newton/blob/7903bb9d376f93a56ba5ec74ac429caba39acaff/07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md#kinematic-entries). Python indices start at zero. The references column lists the headwords VDfirst recognizes in each installed string.

| Entry | Headword | Role in the law or trace | Recognized headword references | Status / Python index |
| --- | --- | --- | --- | --- |
| K1 | `time` | Order instants and obtain durations. | None | Installed / 0 |
| K2 | `reference-frame` | Assign event coordinates. | None | Installed / 1 |
| K3 | `displacement` | Express a spatial vector in a frame. | `reference-frame` | Installed / 2 |
| K4 | `straight-line` | Specify a straight line geometrically. | `reference-frame` | Installed / 3 |
| K5 | `path` | Identify a timeless spatial locus. | `reference-frame` | Installed / 4 |
| K6 | `time-interval` | Select the span by its endpoints. | `time` | Installed / 5 |
| K7 | `point-particle` | Identify the object whose motion is described. | None | Installed / 6 |
| K8 | `trajectory` | Supply the time-indexed map for one particle. | `point-particle`, `reference-frame`, `time-interval` | Installed / 7 |
| K9 | `position` | Evaluate the trajectory at an instant. | `point-particle`, `reference-frame`, `time`, `trajectory` | Installed / 8 |
| K10 | `velocity` | Differentiate the trajectory. | `point-particle`, `reference-frame`, `time`, `trajectory` | Installed / 9 |
| K11 | `speed` | Take the magnitude of velocity. | `point-particle`, `reference-frame`, `time`, `velocity` | Installed / 10 |
| K12 | `acceleration` | Differentiate velocity. | `point-particle`, `reference-frame`, `time`, `trajectory`, `velocity` | Installed / 11 |
| K13 | `relative-position` | Subtract the first position from the second. | `position`, `reference-frame`, `time` | Installed / 12 |
| K14 | `relative-velocity` | Differentiate relative position or subtract velocities. | `reference-frame`, `relative-position`, `time`, `velocity` | Installed / 13 |
| K15 | `path-length` | Integrate the spatial line element along the path, counting each arc once. | `path`, `reference-frame` | Installed / 14 |
| K16 / E1 | `uniform-motion` | Connect the kinematic interval property to Newton I. The speed reference is retained. | `path`, `point-particle`, `position`, `speed`, `time-interval`, `trajectory`, `velocity` | Installed / 15 |

## First trace to describe

- **Question and givens.** Which quantity are we asking for, for which object and instant? What does the scene supply?
- **Entry demands.** At each step, which definition opens, what does it request, and what does the interpreter supply or calculate?
- **Result or stopping point.** What follows from the supplied inputs? If expansion stops early, what remains in the expression?

For the force-sum case, distinguish reaching the end of the supplied interaction set from establishing that the set accounts for every relevant interaction. The November packets give candidate wording for this step. [Design 2.1 packet index](https://github.com/canvalidk/VD-Newton/blob/7903bb9d376f93a56ba5ec74ac429caba39acaff/07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md#entry-packets--2026-11-17)
