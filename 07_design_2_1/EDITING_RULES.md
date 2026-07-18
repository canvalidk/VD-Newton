# Design 2.1 Editing Rules

## Main Rule

Edit Design 2.1 as a consolidation pass, not as a full Design 3
implementation.

## Entry Wording

- Prefer short operational wording over explanatory paragraphs.
- Keep headwords visible.
- Keep residual handles disciplined.
- Avoid importing textbook habits that the trace did not demand.
- Do not make triplet entries carry wall content.
- Do not make wall entries pretend to solve downstream mechanics.

## Lists

When an entry uses a collection, decide whether it needs list treatment.

Useful distinctions:

```text
candidate list
  Items that may be considered one at a time.

accumulator list
  Items already accepted into the current trace product.

closed list
  A list for which the trace has received a no-more-items signal.

empty list
  A closed list with no accepted items.

zero-sum result
  The force-sum result of summing an empty or cancelling force list where the
  summation operation is valid.
```

Do not use empty-list handling to revive the old `Nothing -> Newton I` route.

## Walls

Every wall should eventually have one of these statuses:

```text
usable
  The wall has enough content for Design 2.1.

placeholder
  The wall marks what must later be supplied but still gives the reader a
  controlled landing site.

deferred-to-design-3
  The wall depends on witness sheets, acting-object dispatch, or closure
  machinery that Design 2.1 is not implementing.
```

Placeholders should say what they are placeholders for.

## Witness Sheets

Witness sheets are deferred machinery in Design 2.1.

Allowed:

- mention a future witness-sheet slot in notes;
- mark a demand as eventually needing a witness sheet;
- use witness-sheet language to explain why Design 3 went further.

Avoid:

- making witness sheets required for Design 2.1 entry completion;
- adding full object schemas;
- writing entries that assume a finished witness-sheet runtime.

## Acting Objects

Acting-object machinery may remain skeletal.

Allowed:

- keep acting-object entries in the ledger;
- give walls placeholder content;
- keep the force-list generator idea.

Avoid:

- building concrete spring/gravity/contact clusters now;
- requiring full abstract-to-concrete dispatch;
- treating `mechanical-composition_point-particle` as fully implemented object
  machinery.

## Language Cleanup Checklist

For each edited row, ask:

- Is the role still clear?
- Is the entry Design 2.1, or is it secretly full Design 3?
- Does it mention lists clearly if a list is involved?
- Does it have real content or an honest placeholder?
- Does it preserve the Newton I correction?
- Does it avoid `ao0` and old `Nothing` routing?

