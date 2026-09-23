# NML3 Impressed-Force Terminology Decision — 2026-08-12

> **Role refinement — 2026-08-26:** `impressed-force` remains the ratified
> headword, but its Force-Sum role is now governed by
> `NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`. The target's
> `interaction-set` contains interactions; each interaction supplies a
> target-directed `impressed-force`. Earlier statements below that make an
> impressed force the identity-bearing set member are superseded by that
> refinement.

Status: ratified word-choice authority for the Newton force contribution,
with its current triplet role fixed by the 2026-08-26 naming decision.
This decision is final for the current entry-production line unless the user
explicitly reopens it.

## Decision

The force-contribution headword is:

```text
impressed-force
```

Use `impressed-forces` for headword instances in the plural. In ordinary prose,
write “impressed force” and “impressed forces.”

This headword replaces every predecessor name used for the same contribution:

```text
acting-force -> attached-force -> contributing-force -> impressed-force
```

Those predecessor expressions may remain only inside explicitly marked
historical evidence. They are not alternative current names and must be
translated to `impressed-force` whenever old content is carried forward.

## Newtonian basis

Newton's *Principia*, Definition IV, calls *vis impressa* an action exerted upon
a body in order to change its state. Newton then says that the force consists in
the action itself, does not remain in the body after the action, and may have
different origins, including percussion, pressure, and centripetal force.

The Laws and their first corollary preserve the needed order of dependence:

```text
one or more forces are impressed upon the body
    -> the forces act separately or conjointly
    -> their resultant change of motion is determined
```

The force is therefore identified as an action upon the target before it is
composed with other forces. This is the direction NML3 requires. A vector does
not become an impressed force merely because it is a convenient summand in a
decomposition of the net force.

Primary-source references:

- Newton, *Principia*, Definition IV:
  <https://en.wikisource.org/wiki/Page:Newton%27s_Principia_(1846).djvu/80>
- Newton, *Principia*, Laws I and II:
  <https://en.wikisource.org/wiki/Page:Newton%27s_Principia_(1846).djvu/89>
- Newton, *Principia*, Corollary I on conjoint forces:
  <https://en.wikisource.org/wiki/Page:Newton%27s_Principia_(1846).djvu/90>
- Latin Definition IV, *vis impressa*:
  <https://la.wikisource.org/wiki/Pagina:Principia_newton_la.djvu/9>

The user ratified this selection on 2026-08-12 after obtaining further
confirming information. That information was not supplied as a file or citation
in this workspace, so the references above are the recorded textual basis.

## Installed project meaning

An `impressed-force` is the target-directed force action or vector contribution
that an interaction in a material object's `interaction-set` supplies to that
material object in a fixed context. It is the quantity contributed by that
interaction to the target's net-force sum.

This fixes five distinctions:

1. **Action before sum.** The interaction's membership is warranted
   independently of whether its impressed force helps reproduce the measured
   net force.
2. **Target.** The force is impressed upon the material object whose force
   account is being constructed.
3. **Identity.** Interaction identity is preserved by the `interaction-set`.
   Equal impressed-force vectors supplied by distinct interactions do not
   collapse those interactions.
4. **Target direction.** The same underlying interaction may have a distinct
   target-directed impressed-force for each participating material object; the
   target is part of the address.
5. **Composition after closure.** Only after the `interaction-set` is
   independently closed are the impressed forces supplied by all and only its
   interactions summed to obtain net force.

`warranted` remains an admission condition or status for an interaction. It is
not a competing headword. `force contribution` and `target-directed force
action` remain acceptable explanatory phrases, but the formal entry headword is
`impressed-force`.

## Precedence and quarantine rule

This file supersedes
`NML3_CONTRIBUTING_FORCE_TERMINOLOGY_DECISION_2026-08-02.md` and controls every
active use of predecessor force names. Its Force-Sum role is refined by
`NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`.

Preserved backups, conversation captures, handoff snapshots, and dated writing
passes retain their historical wording only as evidence. They do not have
terminological authority. Any tool or reader using one of them as context must
apply this translation before producing new work:

```text
old force-member name -> impressed-force
```

No historical document may reopen the naming question merely by describing an
earlier state as current or provisional.

Run `check_force_member_terminology.ps1` after terminology-sensitive
edits. It fails if a predecessor member name reappears on an active surface or
if a historical occurrence lacks the quarantine banner.
