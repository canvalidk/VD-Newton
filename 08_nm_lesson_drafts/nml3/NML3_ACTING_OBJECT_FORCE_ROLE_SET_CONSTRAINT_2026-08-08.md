# NML3 Acting-Object / Force-Role Set Constraint

Status: active local design constraint, recorded 2026-08-08. This note does not
select the full entry definition. Its member terminology is governed by
`NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`.

## Observation

Every warranted force is keyed by exactly one acting-object instance. The
acting-object instance is not merely provenance attached to an independently
identified force; it is the force member's identity key.

For a fixed target, time, and physical conditions, this entails

$$
\left|\left\{
w\in\operatorname{IFS}(M):
\operatorname{source}(w)=A
\right\}\right|\leq 1.
$$

Equivalently,

$$
\operatorname{key}(w_1)=\operatorname{key}(w_2)
\Longrightarrow w_1=w_2.
$$

Because a set cannot contain the same keyed element twice, acting-object
instance \(A\) cannot enter the same IFS once under an action-force description
and again under a reaction-force description. If every impressed force is
later classified as action or reaction, the one admitted member keyed by that
acting-object instance must occupy one role or the other.

This is the precise consequence: for one acting-object instance in one fixed
target's force account, action and reaction are exclusive member roles. The
same acting-object instance cannot key two impressed-force members distinguished
only by labelling one `action` and the other `reaction`.

This does **not** make the material object the key. A material object owns or is
the target of the IFS, but it may have several forces acting on it from several
acting-object instances. If the material object were used as the member key,
all of those forces would collapse into one set member. That representation
therefore would not work.

## Design consequence

NML3 therefore fixes the following identity constraint:

- The acting-object instance is the impressed-force member key.
- The material object is the IFS owner or force target, not the member key.
- Within one fixed IFS, one acting-object instance contributes at most one
  impressed-force member.
- That member may later be classified as action or reaction, but not duplicated
  under both roles.
- The IFS generator's duplicate check must compare acting-object-instance keys.
- The later action-reaction block must refine the member without replacing or
  weakening this identity rule.

## Required evaluator contrast

The eventual trace/evaluator should distinguish:

```text
same acting-object instance rediscovered
    -> duplicate; do not add a second set member

same acting-object instance proposed under the other force role
    -> same key; invalid as a second member

same material-object target, different acting-object instance
    -> different key; may be a distinct impressed-force member
```

The evaluator must not use material-object equality as its duplicate test, and
must not manufacture a second member by appending a different force-role label
to an acting-object instance already present in the IFS.

## Scope and provenance

Primary source: the 2026-08-08 observation that associating each warranted
force with one acting-object instance, together with set uniqueness, forces an
action-or-reaction exclusivity for that keyed instance.

This note records the acting-object instance as the intended identity key and
rejects the material object as a substitute key. It is local
active/unsubmitted NML3 material. The resolved managed-context snapshot
`canvalidk/VD-docs@8e09dbf9d3e521cbe76e36426ead656c04a71650` contains no
NML3 or impressed-force material, and no managed VD-docs file was edited.
