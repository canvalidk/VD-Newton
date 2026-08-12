# NML3 Impressed-Force Terminology Decision — 2026-08-12

Status: ratified naming authority for the Newton force-account member-kind.
This decision is final for the current entry-production line unless the user
explicitly reopens it.

## Decision

The force-member headword is:

```text
impressed-force
```

Use `impressed-forces` for headword instances in the plural. In ordinary prose,
write “impressed force” and “impressed forces.”

This headword replaces every predecessor name used for the same member-kind:

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

An `impressed-force` is one independently warranted force-action upon a target
material object in a fixed context, keyed by the acting-object instance from
which that action arises, and eligible for membership in the target's
`interacting-forces-set`.

This fixes five distinctions:

1. **Action before sum.** Membership is warranted independently of whether the
   vector helps reproduce the measured net force.
2. **Target.** The force is impressed upon the material object whose force
   account is being constructed.
3. **Identity.** The acting-object instance is the member key. Equal vectors do
   not imply identical impressed forces.
4. **Role refinement.** A later action-or-reaction classification refines the
   same impressed-force member; it does not create another member with the same
   key.
5. **Composition after closure.** Only after the interacting-forces-set is
   independently closed are the vector values of all and only its
   impressed-force members summed to obtain net force.

`warranted` remains an admission condition or status. It is not a competing
force-member headword. `force-account member` and `force-instance` remain
acceptable explanatory phrases, but the formal entry headword is
`impressed-force`.

## Precedence and quarantine rule

This file supersedes
`NML3_CONTRIBUTING_FORCE_TERMINOLOGY_DECISION_2026-08-02.md` and controls every
active engine, trace, entry packet, design ledger, lesson, and template in this
workspace.

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
