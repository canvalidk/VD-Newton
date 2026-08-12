# HISTORICAL TERMINOLOGY QUARANTINE

> **Do not use this file as naming authority.** It preserves an earlier state and may use obsolete force-member names. The sole active headword is `impressed-force`, governed by `08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`. Translate any predecessor force-member name to `impressed-force` before carrying content forward. Historical wording does not reopen the decision.

---
# E10 Entry Writing Pass — `inertial-mass-material-object`

Status: independent drafting pass against `ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT.md`.
Date: 2026-07-25. Third of the Newton II triplet; companions
`E8_ENTRY_WRITING_PASS_2026-07-25.md`, `E9_ENTRY_WRITING_PASS_2026-07-25.md`.

Revised after review. §5 is new and is the important part: the entry is implicit, that
imposes a mental inversion at every use, and the fix belongs in the IRIL rather than
the entry string.

---

## 1. The entry

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
```

Fourteen words against E8's nine and E9's eight. The break is real and was predicted:
mass is not expressible as an operation over the other two corners, because
vector-by-vector division is not an operation. So E10's definiens is a
**characterisation** where E8's and E9's are **expressions** — the shared frame
`For one material-object, … its … its …` survives, and what sits inside it does not.

That difference has a cost at use time. §5.

---

## 2. Why E10 states its type and E9 must not

The E9 revision dropped `the vector`. This entry keeps `positive scalar`. The two
verdicts come from one test, worth stating in the form that survives to E11 and E12:

> **State a type when the type is a commitment. Omit it when the type is a
> consequence.**

E9's vector-ness is a consequence: scalar × vector = vector, derived across graph
edges the reader already has. Writing it would restate what the daughters carry.

E10's positivity is a consequence of nothing. Nothing in `net-force-material-object`
or `inertial-acceleration-material-object` forces the relating scalar to be positive —
the algebra is equally happy with a negative one, and would then quietly license
antiparallel force and acceleration. Positivity is a **substantive commitment Newton II
makes**, and `newton_II_cleaned.md` says so of the same word in E10's ancestor:
*"The positivity constraint stays — it's part of the commitment Newton II makes."*

By the standing rule from the E8 pass — put in the string exactly what only this entry
can carry — positivity is precisely what only E10 can carry. Same rule, three corners,
two different answers: that is the rule working, not bending.

`scalar` is the weaker half of the phrase and is closer to derivable, but it earns its
place on a second job: it says the thing being looked for is **not a vector**, which
blocks the vector-division misread the packet spends a whole IRIL clause forbidding.
One word, no prohibition.

A genus note, closing the pattern from the E9 pass: like net-force, inertial-mass is a
winter word with **no substantive prior concept available** to be a species of. Its
only candidates — material-amount mass, gravitational mass, weight — are exactly what
NML2.1 forbids identifying it with. So E10 opens with a type where Newton I's winter
words opened with a concept. It can do that only because, unlike E9's, its type is not
free.

---

## 3. One word out: `coefficient`

The packet's candidate A reads *"the positive scalar **coefficient** that multiplies …
to give …"*. A coefficient **is** a multiplying scalar. Once the relative clause states
the operation, the noun states it again.

The word is a fossil of the ancestor, where it had a job:

```text
D2[E23]  The positive scalar coefficient m such that net-force = m times
         inertial-acceleration for a point-particle.
```

There the equation carried the operation and `coefficient` carried the role. Moving the
operation into a relative clause makes the noun redundant.

There is a second and better reason to cut it. `coefficient` carries a faint claim of
**constancy** — a coefficient is a fixed property of the system, the same across
trials. E10 is explicitly forbidden from supplying that: persistence, reuse licensing
and address construction all route to deferred E12/NML2.2, and the packet's own
forbidden list includes target construction. `coefficient` is a small forward hidden
import of the persistence account. `scalar` claims only what E10 may claim.

---

## 4. What the packet got right, and undersold

Candidate A's real achievement is that it states **no conditions at all** and still
produces every boundary behaviour in the packet's IRIL. Two words do it: `the` and
`positive`.

`the` is a definite description, which the entry-writing guide names as its strongest
residual category — *"A definite description forces referent-finding."* It presupposes
existence and uniqueness. When either fails, the description fails to denote, and the
failure is the halt.

| Trial | Positive scalars taking `a` to `F` | Fails | Status |
|---|---|---|---|
| `a` ≠ 0, `F` parallel, same direction | exactly one | — | determined |
| `a` = 0, `F` = 0 | all of them | **uniqueness** | indeterminate — compatible, non-determining |
| `a` = 0, `F` ≠ 0 | none | **existence** | contradiction |
| `a` ≠ 0, `F` = 0 | none (`positive` excludes zero) | **existence** | contradiction |
| `a`, `F` ≠ 0, antiparallel | none (`positive` excludes negative) | **existence** | contradiction |
| `a`, `F` ≠ 0, not parallel | none | **existence** | contradiction |

Every row of the packet's *Blocked* and *Boundary behavior* lists is in that table, and
none of it is written in the entry. Parallelism is never mentioned — a positive scalar
cannot change a vector's direction, so same-direction is entailed by the operation
rather than fenced by a clause. `0/0` is never mentioned — it cannot arise, because no
division is named. The magnitude-ratio temptation never opens, because no magnitudes
are named.

Same virtue as `its` in E8: the constraint is enforced by what the reader must do to
parse the sentence, not described alongside it. The packet's audit calls candidate A
*"explicit and readable"*, which sells it short.

---

## 5. The inversion cost, and where it belongs

The objection: E10 names mass by a relation it satisfies, so getting a number out of it
means solving — every time. E8 and E9 hand you a computation; E10 hands you a puzzle.
That is a real cost, and it is not one an entry should impose casually.

### 5.1 It cannot be worded away

Two reasons, and the second closes the door properly.

*Vector-by-vector division is not an operation.* So no explicit form survives at vector
level. That much was already known.

*`F` and `a` are not dimensionally comparable.* Newtons against `m s⁻²`. Mass is not a
ratio of like things; it is a **conversion between unlike ones**. This kills the
primary-school escape route as well — *"how many times does `a` fit into `F`"* is
quotition division, which compares like with like, and here nothing is like anything
else. That route looked promising precisely because it phrases division as a forward
question rather than a reversal; it fails on dimension, not on style.

So any explicit form must drop to magnitudes and carry a domain fence. That is
candidate C. There is no fourth option.

### 5.2 The implicit form is the installed form for this kind of quantity

Mass is a **constant of proportionality**, and constants of proportionality are defined
implicitly throughout physics — the `k` in `F = -kx`, resistivity, the gas constant.
*"The k such that …"* is a shape the target culture has met many times. The house does
it too: the bundle's Hookean entries define their constants relationally —
*"a restoring response linearly proportional to that deformation"*, *"converted into a
vector attached-force by multiplying by a scalar stiffness"* — never as a quotient.

That does not make the reversal free. It moves it from *novel demand* to *stock
reaction*, which is the guide's own dividing line. Readers do not experience "the k such
that F = kx" as gymnastics, because they have performed it a hundred times.

### 5.3 The inference should be explicit — in the IRIL, not the entry

This is the actionable part, and I think it gets you what you want.

The corpus already houses the inversion twice, and neither place is an entry:
`NML2_1_CONTENT` §6's determination table (*"Suitable nonzero net force and
acceleration → Inertial-mass magnitude"*, with `m = |F_net|/|a|`), and the packet's own
*Allowed* clause. But the packet's clause is **itself implicit** —

> *"For a suitable nonzero trial, find the unique positive scalar coefficient whose
> multiplication of the acceleration vector gives the net-force vector."*

— which is where the reversal is actually being imposed on the reader a second time.
Make that clause explicit instead:

```text
Allowed:
  For a nonzero trial, verify that net-force-material-object and
  inertial-acceleration-material-object share a direction, then return the
  magnitude of the first divided by the magnitude of the second.
```

**§11 revises the framing of this clause.** The direction check is not a guard on the
division; it is the Newton-II claim itself. Once it passes, the division is
unconditional.

Now nobody inverts at use time, and the fragile part has moved somewhere it can be
enforced. A trailing *"when both vectors are nonzero and point in the same direction"*
inside an entry string is a subordinate clause a reader can drop — and the packet's own
anti-misread list names that exact failure: *"Do not ignore vector direction when
magnitudes happen to divide cleanly."* A verification step in a trace either ran or it
did not. This is the residual/auditable split from the E8 pass, applied one layer up:
put the fence where it can be checked, not where it can be skimmed.

### 5.4 The requirement this creates

If E10 stays implicit, the evaluator **must** have a declared solve-for-the-demanded-corner
step. That is a requirement, not an assumption to leave in the air, and it should be
written down — it is the load-bearing thing standing between this entry and the
objection.

It also reframes E8 and E9. They are not computation rules that happen to be handy;
they are relations that happen to be **directly readable**. All three corners state
relations, and the evaluator solves — which is what *"Newton II is a constraint, not an
information generator"* means operationally. The apparent asymmetry across the triplet
is a coincidence of which relations invert in closed form, not a difference in what the
entries are doing.

If that evaluator step does not exist and will not, then E10 must carry the inference —
but as a **second sentence alongside the relation**, never in place of it. Replacing it
loses the entire §4 table, and buys a fence for it.

---

## 6. Carried over from E8 and E9

- **`[A]` replaced by the English possessive** (E8 pass §2.1).
- **Naming `material-object` is a gain**, converting ownership from a residual mark into
  a graph edge (E8 pass §2.2).
- **Frame and time stay out** — owner is the only co-qualification no daughter can state
  (E8 pass §3).
- **`multiplies`, not `scales`.** E9 chose `times` over `multiplied by` because it
  triggers a *scaling* reaction, which is what preserves direction. The consistent move
  here is to keep getting that reaction from primary-school arithmetic rather than
  reaching for the technical word: `scales its a to its F` would name a reaction that
  `multiplies` already produces, in vocabulary installed later and less widely.
- **`to give` is arithmetic, not causal.** *"2 multiplied by 3 gives 6"* is stock and
  carries no production claim. Deliberately not `to produce`, which would read as
  acceleration producing force — a causal overclaim worse than the one forbidden at E8.

### One degradation to record

E8 and E9 close their possessive binding by grammar alone: `For one material-object,
its …` has exactly one available antecedent. E10 interposes a noun phrase — *"the
positive scalar that multiplies **its** …"* — so `the positive scalar` is grammatically
available as an antecedent, and the binding is closed by semantics instead: a scalar has
no inertial-acceleration.

It is closed, but by a weaker mechanism than the other two corners use. What closes it
fastest is the possessum's own morphology — `its
inertial-acceleration-**material-object**` names the type of thing its owner must be.
Which is a genuine point *for* the suffix, and the first one this review has found; §10.

---

## 7. Drafting record

```text
D1  inertial-mass-material-object[A] := the positive scalar coefficient that
    multiplies inertial-acceleration-material-object[A] to give
    net-force-material-object[A].
```
Packet's candidate A. Right in substance; `[A]` out per E8, `coefficient` out per §3.

```text
D2  … the positive scalar coefficient relating its inertial-acceleration-material-object
    to its net-force-material-object.
```
Packet's candidate B. Rejected with the packet: `relating` leaves the operation
unstated, and without the operation the definite description loses its grip — "the
scalar relating a to F" does not, by itself, fail to denote when they are antiparallel.
B's brevity costs the entire §4 table.

```text
D3  … the magnitude of its net-force-material-object divided by the magnitude of
    its inertial-acceleration-material-object, when both vectors are nonzero and
    point in the same direction.
```
Packet's candidate C, and the only wording that answers §5's objection head-on. Rejected
per §5.3 — not because the computation is wrong, but because its fence is a subordinate
clause in a string rather than a step in a trace. The computation itself is adopted, in
the IRIL.

```text
D4  For one material-object, its net-force-material-object divided by
    its inertial-acceleration-material-object.
```
The shape E8 and E9 predict. Recorded because predicting it and then finding it
impossible is what identified this corner as the exception.

```text
D5  … the positive scalar that scales its inertial-acceleration-material-object
    to its net-force-material-object.
```
One word shorter, and makes direction-preservation audible. Rejected per §6:
`multiplies` already produces the scaling reaction from more widely installed
vocabulary, and naming a reaction is not the same as earning it.

```text
D6  For one material-object, the number of times its inertial-acceleration-material-object
    fits into its net-force-material-object.
```
The one genuine attempt at an explicit form that reads forward rather than backward.
Rejected on dimension per §5.1: quotition division compares like with like, and newtons
against `m s⁻²` are not like. Recorded because the failure is instructive — it is *why*
no forward-reading wording exists, not merely that none was found.

```text
D7  For one material-object, the positive scalar that multiplies its
    inertial-acceleration-material-object to give its
    net-force-material-object.                                        ← chosen
```

Minimality check: drop `positive` and antiparallel and one-zero trials stop failing;
drop `scalar` and vector division reopens; drop `the` and the §4 table collapses; drop
either `its` and that input floats free; drop the scope clause and both possessives lose
their antecedent. Nothing is removable. `coefficient` was the only word that was.

---

## 8. Residual provenance ledger

| Phrase | Backing |
|---|---|
| `For one …` | Grammar-level scope idiom; house style across K3, K9–K15 and D2[E23]. `one` triggers singularity, which is what cross-target borrowing violates. |
| `the` | Grammar-level definite description — the guide's named first category. Presupposes existence and uniqueness; both failures are the entry's boundary behaviour (§4). |
| `positive scalar` | Preserved from D2[E23]. `positive` is Newton II's own commitment, derivable from nothing else in the triplet; `scalar` blocks the vector-division misread in one word. |
| `its` (×2) | Grammar-level possessive anaphora, here closed by semantics and by the possessum's morphology rather than by grammar alone (§6). |
| `multiplies … to give` | Primary-school arithmetic. States the scalar–vector relation without naming division, magnitudes, or a procedure. `give` is the arithmetic idiom, not a production claim. |
| the implicit shape itself | Stock across physics for a constant of proportionality (`F = -kx`), and house practice in the bundle's Hookean entries (§5.2). |

No row is backed by this writer's invention.

---

## 9. Checks

- exactly two daughter headwords exposed — yes
- same-owner constraint enforced rather than described — yes, though by a weaker
  mechanism than E8/E9 (§6)
- positivity explicit, because it is a commitment and not a consequence — yes (§2)
- no vector division, no magnitudes, no `0/0`, no procedure in the string — yes, and
  none of them needed forbidding (§4)
- direction condition entailed by the operation, not fenced by a clause — yes
- no scale, weight, gravitational mass, density mass or amount of matter — yes
- no additivity, no target construction, no persistence, no constancy — yes, and §3
  removes the one word that leaked constancy
- no causal claim — yes
- structurally continuous with E8 and E9 — the frame holds; the definiens is a
  characterisation rather than an expression, and that difference is forced
- **the use-time inversion is discharged in the IRIL, not left to the reader — §5.3, and
  this now depends on an evaluator requirement that must be written down (§5.4)**

One gap to record rather than fix: the packet's audit twice says *"positive finite-mass
commitment"* while the entry says only `positive`. Finiteness closes only if `scalar` is
defined over the reals — general quantity-type machinery, the packet's open question 6,
not this string.

---

## 10. Answers to three of the packet's open questions

**Q3 and Q4 together — what status does a failed trial get, and who classifies it.**
E10 classifies nothing, and needs no machinery to, because it states no conditions.
Every failure in §4 is a definite-description failure. But they are of two kinds, and
that is the distinction the packet is reaching for:

```text
existence failure   (no such positive scalar)   -> contradiction
uniqueness failure  (every positive scalar)     -> indeterminate
```

Zero/zero is the only uniqueness failure; every other bad trial is an existence failure.
So Q3's *"distinct status that records both compatibility and non-identification"* is
right, and it is not an ad-hoc third category — it is what uniqueness-failure-without-
existence-failure means. Q4 resolves to the general evaluator, not because that is
tidier but because E10 has nothing to classify with.

**Q5 — can a Newton-II inference create a fresh binding after a reuse licence has
expired?** The question dissolves into the already-deferred one. An expired licence kills
a *binding*, not the entry: E10 determines a coefficient for any address from any
suitable nonzero trial. What the trigger destroyed is confidence that the later target is
the same target — an **address** question, which is exactly E12/NML2.2. The glass-ball
note puts the order plainly: lumping decides which target may own a mass value, and only
then does a determination decide what value sits at that address. So: not blocked by the
expiry, blocked or not by whether the new target has a licensed address.

**Unchanged from E8:** Q1 (address binding belongs in a declared structural field, not
the definiens), and the headword-suffix question still outranks all of them — 141
characters here against 109 for the same fourteen words under short headwords.

With one honest qualification now on record. §6 found the first real argument *for* the
suffix: `its inertial-acceleration-material-object` names the type of thing its owner
must be, closing a possessive binding that `its inertial-acceleration` would leave to
inference. That does not overturn the objection — the two winter headwords still encode
a domain the two-entries note retracted, and still tax every entry in the house — but the
trade has a real cost on both sides, and E10 is where it shows.

---

## 11. Where the direction condition actually lives

Added after review. This revises §5.3's framing and strengthens §2.

### 11.1 The direction condition is not a second condition

For vectors `F` and `a`:

```text
∃ m > 0 such that F = m a      ≡      F and a are parallel and same-sense
```

These are the same statement. The existence of the coefficient **is** the direction
claim — not an extra fact to be checked alongside it. So `F = ma` is not a vector
equation carrying three independent components. It carries one magnitude relation plus
a direction identity that its own form asserts rather than tests.

### 11.2 Newton II never computes a direction

Run it across all three corners:

```text
E8   a := F / m        direction of a is inherited from F
E9   F := m · a        direction of F is inherited from a
E10  m                 a scalar; has no direction
```

No corner ever produces a direction. Every direction in the triplet is inherited from
an input or absent. The law scales magnitudes and passes direction through untouched.

For a law drilled in the classroom as *the* vector law — *"vector answers require
direction"*, per the content spec — that is worth having said out loud. The
direction discipline NML2.1 teaches is real, but it is entirely about **carrying**
directions correctly, never about **computing** one. Those are different skills and the
lesson currently presents them under one banner.

### 11.3 Why: `positive scalar` is where the isotropy lives

The pass-through happens because `m` is a positive scalar, and a positive scalar cannot
rotate a vector. That is not a typing detail. **It is the claim that inertial response
is isotropic** — that a material object is no harder to accelerate in one direction than
another.

Make `m` a tensor and every line above fails: `F` and `a` are no longer parallel,
direction becomes computed rather than inherited, and `m = |F|/|a|` is simply false.
That is not hypothetical — it is effective mass in a crystal lattice, and the house
already carries the same scalar-versus-tensor cut for the neighbouring law, in
`hookean_response_type_chain_d1.md`: *"It is not a scalar spring constant. It is a
fourth-rank tensor relation."*

So §2 was right but understated. `positive scalar` is not merely a commitment that
happens to live at the mass corner. It is **the only place in the Newton II triplet
where isotropy is stated at all**, and E10 is the only entry that can state it. That is
about as strong a case as the standing rule — *state a type when the type is a
commitment* — is ever going to get.

### 11.4 What this changes: the IRIL clause

§5.3's clause reads as though the direction check guards the division — as if dividing
magnitudes were unsafe until directions are confirmed. That framing is wrong. The
division is never unsafe. What the check tests is whether **Newton II holds for these
two values at all**.

So the trace has two steps with different jobs, and they should not be run together:

```text
1. consistency:   do these values satisfy Newton II?   (direction agreement)
                  failure -> law violation, not a domain error
2. determination: m = |F| / |a|                        (unconditional, given step 1)
```

This also improves the answer to the packet's open question 4. Directional failure
belongs to a general Newton-II consistency evaluator not merely because E10 has no
machinery to classify with (§10), but because it is not a *mass* question in the first
place — it is the law being tested, and the same test serves every corner.

### 11.5 What this does not change: the entry

The simplification licenses a **procedure**, not a **definition**. `m = |F|/|a|` cannot
be E10's string, for two reasons that survive everything above:

- A cart at rest under zero net force has an inertial mass and has no such ratio.
  `0/0` is not its mass; the ratio simply is not there, while the mass is.
- Any two non-parallel vectors divide cleanly. A definition built on the ratio would
  assign an "inertial mass" to values that violate the law — the exact error the
  packet's anti-misread list names: *"Do not ignore vector direction when magnitudes
  happen to divide cleanly."*

The magnitude form **presupposes the law and therefore cannot detect its violation**.
The implicit form presupposes it by *presupposition* — a definite description that
fails to denote — which is detectable, and is the whole §4 table.

### 11.6 The one place the crack does not go through

The equivalence in §11.1 quietly requires both vectors to have directions. The zero
vector has none. So at `a = 0, F = 0` the premise *"we know they point the same way"*
does not hold — not because they point different ways, but because neither points.

That is exactly the case the content spec singles out (*"The `0/0` case determines no
mass"*), and it is why the simplification is sound precisely on the domain where
directions exist. Worth keeping the boundary in view: the result is not that direction
is always free, but that it is free wherever it is defined.
