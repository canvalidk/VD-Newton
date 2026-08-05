# E11 Entry Writing Pass — `net-force-material-object` (wall)

Status: independent drafting pass against
`ENTRY_PACKET_E11_NET_FORCE_MATERIAL_OBJECT.md`.
Date: 2026-08-02.

**Revised three times after review.** Every shape is kept in §7, because the
differences between them are the substance of this pass:

| | Shape | Kept at |
|---|---|---|
| 1 | genus-first, five qualification fields, closing with a withholding | D9 |
| 2 | same, closing with the two routes named | D10 |
| 3 | same, closing with the routes counted and not named | D11 |
| chosen | **E9's scope-clause shape, interval dropped, routes counted** | D12 |

The three revisions each removed something the pass had argued for, and in each
case the argument turned out to be over-fitted rather than merely outweighed.
Those retractions are recorded at §2.3, §4.1 and §6, not buried.

Sources read: the E11 packet; the E8, E9 and E10 passes; the law writing guide
(§§4–7); `vd_six_entry_structure.md`; `entry_writing_guide_auditable_compositions.md`;
`NML2_1_CONTENT_d2.md`; `NML2_note_net_force_wall_withheld.md`;
`DESIGN_2_1_DRAFT_1_ENTRIES.md`.

---

## 1. The entry

```text
net-force-material-object :=

For a material-object in an inertial-frame, its vector in newtons. There are
exactly two ways to obtain this vector.
```

19 words, 116 characters. E9 is 8 words, 107 characters — so the wall and its
corner are now the same size on the page, which is the right outcome for two
definitions of one headword.

### 1.1 The fields

| # | Field | Text | Check it licenses |
|---|---|---|---|
| 1 | owner | `For a material-object … its` | not a system, a pair, or a trajectory |
| 2 | frame | `in an inertial-frame` | not a value read in a rotating or accelerating frame |
| 3 | type | `vector` | not a scalar, not a bare magnitude; and exactly one per owner |
| 4 | dimension | `in newtons` | not an acceleration, not a mass; recognisable on the page |
| 5 | provenance | `exactly two ways to obtain` | not a meter reading, not a salient push, not a sum |

Four fields in nine words, because `its` carries two of them at once — see §1.2
— and because the scope clause carries the owner and the frame together in the
position E9 already uses for scope.

### 1.2 What `its` does that the previous shape needed three devices for

The previous shape opened `The vector in newtons belonging to one
material-object …`. That spends `The` on uniqueness, `belonging to` on
ownership, and `one` on singularity of the owner. A singular possessive does
all three at once:

- *ownership*: `its` cannot be parsed without locating an owner, and the scope
  clause has just supplied one. This is grammar-level machinery, the
  auditable-compositions guide's strongest provenance category, at zero tokens.
- *uniqueness*: `its vector` presupposes exactly one, in the way `its mother`
  does. A reader who thinks a book on a table has two force vectors cannot
  satisfy the description.
- *singularity of the owner*: `a material-object` is already singular, so `one`
  has nothing left to add here — see §6 on why `one` earns its place at E8–E10
  and not at E11.

This is the E8 pass's own finding, arriving at the wall: *"`its` cannot be
skimmed. A possessive is not parseable until a referent is found."* The previous
shape described ownership; this one enforces it.

---

## 2. The one thing this pass is really about

E8, E9 and E10 are triplet corners. E11 is a **wall**. Nothing else in this
pass matters as much as that difference, and the packet does not price it.

The law writing guide §5 states the test outright:

> Take a peripheral entry and read it in isolation. It should be intelligible
> without knowing that a triplet exists. It should read like a normal
> dictionary definition. If it only makes sense in the context of the law, it
> is doing inward work and belongs in the triplet, not in the periphery.

And, immediately after:

> If you find a wall that seems to encode part of the law, move that content
> into the triplet.

Apply this to the packet's chosen wording:

```text
For a material-object at a selected time or interval in an inertial-frame,
the single vector assigned to that material-object for the Newton II relation,
measured in newtons.
```

Read in isolation, `the single vector assigned … for the Newton II relation` is
not intelligible to a reader who does not know the law. It is a pointer into
E9. The packet's own ledger says the phrase's job is to *"connect the outward
wall to E8-E10"* — which is the diagnosis, not the defence. Under the guide's
test that content is inward, and it already has a home.

The redundancy is also structural, not merely stylistic.
`vd_six_entry_structure.md` lists the edges:

> Some are "same headword, different definition" links (vertical: chimney to
> its triplet entry, triplet entries down to their wall entries).

E9 and E11 share a headword. The vertical edge between them exists in the
graph. A reader who needs the law relation follows that edge to E9 and finds
it stated properly. Putting `for the Newton II relation` in E11's string moves
a fact the graph already carries into the residual, where no audit reaches it.

That is the E9 pass's own rule. E9 dropped `the vector` because the type was
derivable *through graph edges*, and the pass wrote: *"Crucially that
derivation runs on graph edges, not on residual: it is the auditable case."*
The same rule applied at E11 removes the law reference for the same reason.

### 2.1 And it works in the other direction too

The identical rule tells E11 to **state** what E9 was right to leave out.

E9 omitted the type because its two daughters make it derivable. E11 has no
daughters. And the derivation E9 relied on runs *through the law* — which is
exactly the route a wall's reader is defined not to have taken. The guide, same
section:

> Outward-facing entries … can be read and understood without knowing anything
> about the law they belong to.

So `vector` and `in newtons` are stated at E11 precisely because they are only
derivable by entering the triplet, and the wall's audience is the reader
outside it. Same rule, opposite verdict at the two ends of the same edge —
which is the tidy result the E9 pass's §2 was reaching for.

**General finding, for every wall after this one.** A triplet corner states
only what is not derivable through its edges. A wall states what an outward
user needs to hold and use a value, and derivability *through the law* is not
a reason for its silence. The two entries at either end of a same-headword edge
are therefore not competing for the same content; they are partitioning it, and
the partition line is the law itself.

### 2.2 The chosen entry does not have to walk this line

An earlier shape had to defend a softening here. Its provenance field read
`inferred through Newton II`, which names the law inside a peripheral entry,
and the defence was that naming a *route* is not encoding the *relation*. That
defence was sound but it was a real weakening.

Counting the routes rather than naming them removes the problem outright. **The
chosen entry contains no reference to Newton II, to the triplet, or to any
daughter headword.** It passes the guide's isolation test without qualification:
every word of it is intelligible to a reader who does not know a law exists.

That gain was not the reason for the change — §5.3 was — and it is worth
recording that the more pedagogical wording turned out to be the more
structurally correct one.

### 2.3 Shape — a retraction

Two earlier versions of this pass argued that E11 must open with its genus and
must not open with a scope clause. The argument was: scope-clause-first is the
shape of the corners (E8, E9, E10) and of K9–K15; genus-first is the shape of
every peripheral entry (E3–E6) and of K3; and since E9 and E11 share a headword,
the reader needs a visible signal telling the inward entry from the outward one.

**That partition is wrong.** Sort the corpus by whether the quantity has an
owner rather than by whether the entry is peripheral:

- K3 `displacement` has no owner — *"A spatial vector with units of length,
  expressed in a chosen reference-frame."* No scope clause.
- K9 `position`, K10 `velocity`, K12 `acceleration`, K13, K14 all have an
  owner — *"For a point-particle …"*. Scope clause.
- E8, E9, E10 have an owner. Scope clause.

The rule is **owned quantities take a scope clause; unowned ones do not**, and
it holds across peripheral and triplet entries alike. K3 was never evidence
that peripheral entries are genus-first; it was evidence that displacement
belongs to nobody. Net force belongs to a material-object, so E11 takes the
scope clause, and it takes it in E9's exact form.

The distinguishing signal I was protecting is supplied by content, not shape:
E9 has two daughter headwords and an operation, E11 has neither. And there is a
gain the earlier argument missed — pairing the two entries visually is what
makes the same-headword edge of §2 *visible* on the page, rather than something
only the graph knows.

**On sentence count**, an earlier claim also needs narrowing: the one-noun-phrase
rule is the corner rule. The walls in this log are multi-sentence — E5 has four,
E6 has two, and K5 carries a second clause after a semicolon for exactly the job
field 5 does here. A wall may take a second sentence, and this one does.

---

## 3. The genus E9 could not supply

The E9 pass closed §2 with a task for this entry:

> `net-force-material-object` is a winter word born with **no genus available**
> … Which also tells E11 what its job is when it does land: **supply the genus
> E9 could not.**

That pass then argued no genus exists, because the only candidate is `force`
and NML2.1 forbids importing it. That argument looked for the wrong kind of
genus. It tested `net-force` against E3 and E6 — walls whose winter words are
*kinds* (`inertial-frame` is **a reference-frame**; `free-particle` is **a
point-particle**) and whose genus is a licensed prior kind.

`net-force` is not a kind. It is a quantity, and K3 shows what a quantity's
genus looks like in this house: not a prior kind but **type plus dimension** —
*"A spatial vector with units of length"*. That is available to net force:

```text
… its vector in newtons.
```

So the genus problem dissolves. It was never that net-force had no genus; it
was that the search was run against the property walls instead of the quantity
one.

### 3.1 One place E11 has to break K3's convention

K3 names a *dimension* (`units of length`), not a unit. No entry in the log
names a unit. E11 must, because the only dimension word available for this
quantity is `force`, which is circular here and unlicensed besides.

The unit is the better choice anyway, and not merely as a fallback. NML2.1 §2
licenses the newton by reduction — `1 N = 1 kg m s⁻²` — so `newtons` is
grounded in the two quantities that *are* licensed, and grounds the wall
without touching the ordinary force concept. This is also the entry's only
outward recognition handle: a value arrives on a page as `12 N east`, and
`newtons` is what lets the reader identify what kind of value it is before any
law is applied. That is what a wall is for.

### 3.2 The wall that cannot have an alias

E5 gives its winter word two aliases (*"sometimes called a Galilean frame or
the lab frame"*) and an applicability note (*"Earth can be treated as an
inertial reference-frame in ordinary circumstances"*). E6 gives one alias
(*"A free-particle or free body"*). Aliases and applicability notes are what
make those walls substantial.

E11 can have neither. Every ordinary alias for net force — *resultant force*,
*the resultant*, *total force* — encodes the force-sum account in the word
itself. And there is no NML2.1-licensed circumstance under which some familiar
object *counts as* a net force; that is the newton-meter error exactly.

This is the honest explanation of why E11 is thinner than the Newton I walls.
It is not a drafting failure and it is not a sign the wall should be withheld.
It is that two of the three things a wall in this house normally carries happen
to be unavailable for this word — and that the third, the field list, is
available in full.

---

## 4. The frame stays; the interval goes

### 4.1 A retraction, and the distinction that replaces it

Earlier versions of this pass kept `over a selected time or interval`, on the
E8 pass's rule:

> Owner is the only co-qualification that no daughter entry can state. Frame
> propagates down from the headword — `inertial` fixes it, and a quotient
> inherits it. Time propagates the same way.

The argument was that at E11 *nothing* propagates — no daughters, no `inertial`
in the headword, and a reader holding a supplied vector who has never touched
acceleration — so both qualifications must be stated here.

The first half of that is right and the second is not, and the reason is worth
having as a rule:

> **A wall states validity conditions. Instance selection belongs to the trace.**

`inertial-frame` is a validity condition. Outside an inertial frame this is not
the same quantity, and a supplied problem value almost never states its frame —
so if E11 does not carry it, nothing does, for the reader who most needs it.

A time index is an instance selector. It says which of the quantity's values you
are looking at, not what kind of thing the quantity is. And unlike the frame, it
*does* arrive with the data: NML2.1 §12.4 hands out *"one opaque net-force
vector for each interval"* — the interval comes attached to the value, because a
value handed over without one is not usable at all. There is nothing for the
entry to protect.

The two qualifications looked symmetric and are not. One is routinely omitted
from supplied data and unrecoverable; the other is routinely present and
unusable if absent.

**What this costs.** The anti-borrowing protection across spans moves entirely
to the trace, where the packet's `Slots read` already lists *selected time or
interval*. If traces are observed carrying a value from one interval into
another without challenge, that is the protection this decision gave up, and the
repair is a trace-side check rather than four words in the entry. §12.3.

### 4.2 `inertial-frame` in the scope clause

The frame now sits with the owner rather than trailing the definiens. That is
where E8's pass tested it (its D4: *"For one material-object at a selected
time …"*) and rejected it only because at a corner the tag is inherited. At E11
it is not inherited, so the scope clause is where it belongs, and putting it
there is also what keeps the definiens down to `its vector in newtons`.

---

## 5. The provenance field: the count

The packet's decision 6 keeps provenance out of the string entirely, and its
assessment of candidate C rejects naming the routes because doing so *"risks
making those routes exhaustive and thereby excluding later force-sum-produced
values."* This pass keeps provenance, drops the naming, and answers the
exhaustiveness objection at §5.6.

### 5.1 Why a wall needs a provenance field when a corner does not

**A corner is an operation. A wall is a recognition trigger.** A reader running
`m times a` has nothing to substitute — whatever they wrongly believe about net
force does not change the arithmetic in front of them. A reader meeting the
*word* is in the opposite position: the installed reaction has already fired
before the entry is read. Every reader arrives at `net force` with *all the
forces added together* pre-loaded, from every prior encounter with the phrase.

Silence therefore does not leave the provenance slot empty. It leaves it
**filled by the pre-installed reaction**, which is the one thing
`NML2_note_net_force_wall_withheld.md` exists to prevent. A wall must displace;
it is not enough to avoid installing.

### 5.2 Displacement by closure, not by denial

The earliest shape displaced by *withholding* — it said the production question
was open. The chosen entry displaces by **closing the count**.

*It is positive.* A withholding tells the reader what not to conclude; a closed
count tells them there is a short, findable list and sends them to find it. That
is an action at the node, which is the test the E10 pass used to decide what
stays in a string.

*It never names what it excludes.* Denials look safer and are not. *"It is not a
newton-meter reading"* requires the reader to hold `newton meter`; *"it is not
the sum of the forces"* names machinery that has no headword yet. Both are
forward hidden imports in negative clothing — the exact defect the
auditable-compositions guide catalogues. **You cannot tell a reader not to add
up the forces without telling them there are forces to add up.** A count says
nothing about force contributions at all.

NML2.1 §3's five forbidden identifications are then excluded by arithmetic
rather than by argument: the reader who has the two routes in hand and meets a
third candidate — a meter reading, a salient push, a sum — knows it is not one
of them, because there are not three.

### 5.3 Why count rather than name

`exactly two` and no more. The reasons, in the order they weigh:

**The entry is pedagogical, and the count is the whole lesson.** What NML2.1
needs a student to hold is not a lookup table of routes — the lesson supplies
those, twice, in §§6.1 and 12.3 — but the fact that the list is **closed**. The
student's error is never *forgetting a route*; it is *inventing one*. The count
is the part of the content that does the work, and it does it whether or not the
reader can currently recite the two.

**It removes the last law reference from a peripheral entry.** §2.2.

**It avoids a description the supplied route cannot have.** `supplied as an
opaque value` was doing two jobs — marking the route and excluding the meter —
and it needed `opaque` to do the second, which is a lesson-installed handle
(§12.4). The count needs neither word.

**The routes are recoverable and the count is not.** A reader can find the
inference route by following the same-headword edge to E9; NML2.1's exercises
hand them the supplied route on every sheet. Neither of those tells them the
list is complete. Put in the string exactly what only this entry can carry —
the E8 pass's rule — and what is left is the number.

### 5.4 What the count costs

**The supplied route has no entry anywhere in the log.** Naming it was the only
place it appeared. A reader inside NML2.1 will supply it without difficulty; a
reader coming to the dictionary cold is told there are two ways and can find
only one. That is a dangling count, and it is the real price of this shape.
§12.1.

**The meter exclusion is weaker.** Under D10, `opaque` excluded the newton meter
directly — a meter reading is a supplied value that arrives *with* an account,
which is precisely what makes it dangerous. Under the count the meter is
excluded only because it is not one of the two, which requires the reader to
know the two. Inside the lesson population that holds; outside it, the exclusion
is inherited rather than carried.

**The zero case is not blocked.** The earliest shape's withholding sentence
blocked the inference from a zero net force to *no force contributions exist*,
because making that inference meant answering a question the entry had declared
open. A count does not reach it.

Not lost from the account: the packet's IRIL already blocks *"inferring
free-particle status, zero velocity, or absence of force contributions from a
zero net-force vector"*, and `NML2_1_CONTENT_d2.md` §3 states the protection for
the lesson. Moving it out of the string is the same move the E10 pass made with
retention and provenance. But it is the one item on the packet's Preserve list
that the string does not carry, and the zero case is common. §12.2.

### 5.5 A reversal, recorded

An earlier version of this pass argued: *name the routes; do not count them* —
on the ground that a bare count is unactionable, and that once the routes are
named the numeral only describes what `either … or` already enforces.

The second half of that was right, and is why `exactly two` appears rather than
a disjunction plus a number: **whichever device closes the list, the other is
redundant.** What changed is which device does the closing, not the principle.

The first half was wrong, and the error was assuming a dictionary reader with no
lesson. For the population this entry is written for, a count is actionable: it
tells them the two things they already do are all there is. §5.3.

### 5.6 Exhaustiveness, and later values

The packet's objection to naming the routes — that force-sum will later produce
net-force values, and a closed list excludes them — applies to a closed count
just as much. It assumes E11 must remain the last word on this headword.

It need not, and in this log that is the normal case: `uniform-motion` has K16
and E2; `inertial-frame` has K2, E3 and E5. Every headword in the six-entry
model already carries several entries at different log positions. When the
force-sum block opens it will lay down its own entry for
`net-force-material-object`, and E11 will stand as what it always was — the wall
as of this position in the log.

That also disposes of *"is E12 removed from the dictionary or only from the
lesson?"* at `NML2_note_net_force_wall_withheld.md` §15.1 (that note's `E12` is
this net-force wall under the earlier numbering). It is withheld from the
lesson, landed in the dictionary, and superseded later — three different things,
and the note treats them as one choice.

---

## 6. The packet's words this pass drops

### `single`

The packet's decision 2 makes `single vector` load-bearing: it blocks
`vector sum`. But uniqueness is carried at grammar level and for free by the
possessive — `its vector` presupposes exactly one (§1.2). `single` **describes**
what `its` **enforces**, the same defect the E8 pass found in its D5 and the E10
pass found in `jointly`.

And `single` is contaminated. NML2.1 §3's own forbidden list reads *"a single
push or pull"*. In the source's vocabulary, `single` marks the individual
contribution — the error. Using it for the whole-object value asks one word to
carry two opposed reactions in one lesson.

### `assigned to`, and a retraction

The packet's open question 2 asks whether `assigned to` is the best
provenance-neutral verb. It is not, and the problem is not neutrality.
`assigned` names an act of assignment by a modeller, and NML2.1 §6 is titled
*"Newton II is a constraint, not an information generator."* A value that is
*assigned* is one somebody chose.

Earlier versions of this pass replaced it with `belonging to`, NML2.1 §§1 and
3's own word, and defended the choice with a distinction that now has to go:
that at E8–E10 ownership is a *constraint* between two inputs and so must be
enforced by `its`, whereas at E11 there is only one quantity and no constraint
to enforce, so *describing* ownership is correct.

**That was wrong.** Enforcement is not only for constraints. `its` cannot be
parsed without locating an owner whether there are two quantities or one, so the
possessive enforces ownership at E11 exactly as it does at E8 — and it costs
three words less than the description. The correct statement is the E8 pass's
original one, with no exception carved out for walls: put ownership in a
possessive wherever a scope clause can supply the antecedent.

`belonging to` remains the right *descriptive* phrase and is the fallback if the
scope clause ever has to go; it is not the right choice while the scope clause
is there.

### `one`

E8, E9 and E10 all say `For one material-object`, where `one` is doing real
work: it is what makes the two daughters' owners the *same* one. At E11 there is
one quantity and no same-owner constraint, and `a material-object` is already
singular, so `one` would be inherited rather than earned.

This is the one place the chosen entry deliberately does not mirror E9. If house
uniformity across the four Newton-II entries is judged worth more than removing
an idle word, it is a one-character change and nothing else in the pass moves.
§12.5.

### `measured in`

Cut to `in newtons`. `measured` implies a measurement occurred, and in NML2.1
the net force is *never* measured — it is supplied or inferred, which is what
the provenance field counts, and the meter misconception is the lesson's named
enemy. The packet's ledger defends the phrase by noting it *"does not identify
an instrument"*, which is true and beside the point: it identifies that there
was measuring.

### `for the Newton II relation`

§2 and §2.2. It is inward content in a peripheral entry, the same-headword edge
to E9 already carries it, and the chosen entry does not reintroduce it in any
form.

The obvious objection is that without it the definiens no longer says the vector
is *net* rather than one contribution. Three answers.

First, at this point in the log there is no competitor: `force-contribution`,
`attached-force` and `interacting-forces-set` have no headwords, so within the
dictionary a material-object's vector in newtons is unambiguous.

Second, the possessive does the blocking, and better than a law reference would.
A reader who knows a book on a table has two familiar forces on it will read
*its* vector and get stuck. Getting stuck is correct — that reader has just
found the force-sum question for themselves, which is worth more than being
told, and the second sentence tells them that neither of the two available ways
will resolve it.

Third, E5 is the precedent for how far a wall may reach toward its theory. E5
says *"the standard reference-frame for Newtonian mechanical analysis"* — it
names a **domain of practice**, then supplies content that stands on its own.
Naming a domain is not encoding a relation. The chosen entry does not even do
that much.

---

## 7. Drafting record

```text
D1  For a material-object at a selected time or interval in an inertial-frame,
    the single vector assigned to that material-object for the Newton II
    relation, measured in newtons.
```
Packet's candidate A. Rejected on §2 (inward content in a peripheral entry) and
§6 on every substantive word. Note what survived: the scope clause and its
opening `For a material-object` are the packet's, and after two revisions away
from them the entry has come back. What was wrong with D1 was never its shape.

```text
D2  net-force-material-object[A] := the single vector assigned to material
    object A …
```
Packet's candidate B. Rejected before argument by the E8 pass §7, which settled
for this house that address binding is a declared structural field, not
definiens syntax. At a wall the case is stronger still: the wall's reader is by
definition the one who has *not* been through NML2.1's bracket drill, so the
one population `[A]` was ever installed for is the one population E11 does not
serve.

```text
D3  … the single vector, measured in newtons, supplied or inferred for use in
    the Newton II relation.
```
Packet's candidate C. The right content, rejected in this form: `for use in the
Newton II relation` is the relation, not a route, and `supplied or inferred`
without a closure device reads as illustrative rather than complete.

```text
D4  The single vector, in newtons, that Newton II requires of one
    material-object over a relevant time or interval in an inertial-frame.
```
The best version of the packet's architecture. `requires` is a real improvement
on `assigned` — it is the constraint verb, against `determines` / `gives` /
`produces`, which are information-generator verbs — and it is the withheld
note's own word. Rejected on §2: a better law reference is still a law
reference.

```text
D5  A vector, in newtons, belonging to one material-object over a selected time
    or interval in an inertial-frame.
```
K3's shape exactly. Rejected on `A`: with the indefinite article the entry
admits *any* force-dimension vector belonging to the object, which is the
single-contribution error the packet forbids.

```text
D6  The vector, in newtons, belonging to one material-object over a selected
    time or interval in an inertial-frame.
```
The genus-first field list, in its first arrangement. Superseded twice: by the
comma and conjunction repairs of the third version, and then wholesale by §2.3's
retraction of the genus-first argument.

```text
D7  … It is not yet a claim about which physical interactions produce that
    vector.
```
A withholding, on K16/E1's shape (*"It is a kinematic path-pattern, not yet a
claim about why the motion occurs"*). Rejected on the subject: in E1 the
`It … not yet a claim` contrast is licensed by a positive first half in the same
sentence. Standing alone, *a vector is not a claim* is a category error the
reader has to repair before they can read it.

```text
D8  … This entry does not yet say which physical interactions produce it.
```
The withheld note §15.2's shape. Correct in content, rejected on
self-reference: it makes the entry talk about itself where every other entry in
the log talks about the world, and the note's fuller version (*"does not tell
the modeller how to …"*) is agent-directed, which the auditable-compositions
guide rules out.

```text
D9  … Which physical interactions produce that vector is a later question.
```
The first version's closing sentence. `is a later question` is the withheld note
§1's own construction and it is a good sentence — declarative, non-deontic, about
the world rather than about the entry, and it does not go stale. It is the only
shape that blocks the zero-case inference (§5.4), and if that protection is ever
judged to belong in the string, this is where it comes back from.

```text
D10 … either supplied as an opaque value or inferred through Newton II.
```
The second version's closing clause. Complete where the count is not: it names
both routes, and `opaque` excludes the newton meter directly rather than by
inheritance. Rejected per §5.3 — it writes `Newton II` into a peripheral entry,
and it leans on `opaque`, a lesson-installed handle, in the entry least likely
to be read by the lesson population. Standing fallback if §12.1 goes the other
way.

```text
D11 The vector in newtons belonging to one material-object over a selected time
    or interval and in an inertial-frame. There are exactly two ways to obtain
    this vector.
```
The third version. Superseded on shape (§2.3) and on the interval (§4.1). Its
provenance sentence survives unchanged into D12.

```text
D12 For a material-object in an inertial-frame, it is a vector quatity measured in newtons. There
    are exactly two ways to obtain this vector.                       ← chosen
```

`exactly` is the closure and is load-bearing: `two ways` alone reads as
illustrative — two among others — and every exclusion in §5.2 depends on the
list being complete.

`obtain` rather than `determine`. NML2.1 §6 uses *determine* as the name of the
three Newton-II operations and sets it against *supplied* in the same table
(*"Information supplied"* against *"What Newton II determines"*). Using it as
the umbrella over both routes would collide with the source's own contrast.
`obtain` is neutral between being handed a value and working one out.

`this vector` rather than `it`: the nearest noun to the pronoun would be
`newtons`.

**Minimality check on D12.**

- Drop `For a material-object` → `its` loses its antecedent and the entry has no
  owner at all.
- Drop `in an inertial-frame` → §4.1; the supplied-value reader has no frame
  qualification anywhere, and this is the one qualification the data does not
  carry.
- Drop `its` → ownership and uniqueness both go, and no other word in the entry
  supplies either (§1.2).
- Drop `vector` → the type is left derivable only through the law, which is the
  one route the wall's reader has not taken (§2.1).
- Drop `in newtons` → the log's only unit statement goes, and nothing separates
  this quantity from the acceleration vector.
- Drop `exactly` → the list stops being closed and the provenance field excludes
  nothing.
- Drop `two` → nothing is left but a claim that the vector can be obtained.
- Drop the second sentence → §5.1.

Nine content words, nothing removable. That is a smaller residual than any of
the three shapes it replaces.

---

## 8. Residual provenance ledger

| Phrase | Backing |
|---|---|
| `For a …` | Grammar-level scope idiom; house style across K9–K15, E8, E9, E10, and the packet's own candidate A. Supplies the antecedent `its` needs. `a` rather than `one` because `one`'s job at the corners — same owner for two daughters — does not exist here (§6). |
| `material-object` | Headword edge — the auditable case, not residual. Naming the owner concept converts ownership from a residual mark into a graph edge, which the auditable-compositions guide asks entries to prefer. |
| `in an inertial-frame` | Headword edge. Present as a validity condition, not an instance selector (§4.1), and in the scope clause because at E11 the frame is not inherited from anywhere. |
| `its` | Grammar-level possessive anaphora. Innate, language-wide, population-independent. Unparseable without a referent, and a singular possessive presupposes uniqueness — so one word carries ownership and one-per-owner together (§1.2). |
| `vector` | Stock mathematics, and K3's precedent for a quantity's genus (*"A spatial vector …"*). Stated here, unlike at E9, because the derivation E9 relied on runs through the law and the wall's reader has not entered it. |
| `in newtons` | NML2.1 §2's unit table, licensed by reduction (`1 N = 1 kg m s⁻²`), so it grounds the quantity without importing the ordinary force concept. Fills K3's dimension slot with the only word available (§3.1). |
| `exactly two` | Stock counting. The closure device; `exactly` is what makes it exclusive rather than illustrative. |
| `ways to obtain` | Plain English, chosen against NML2.1 §6's `determine` because that word is already committed there to the three Newton-II operations and stands in contrast to `supplied`. |

No row is backed by this writer's invention. Three rows are grammar, two are
headword edges, two are stock, and one is NML2.1's unit table. **The chosen
entry cites no lesson-installed handle at all**, which is a strict improvement
on D10's reliance on `opaque` (§12.4), and matters more at a wall than anywhere
else, since a wall is the entry most likely to be read outside the lesson
population.

**One phrase deliberately not used.** `force-accounting value` is the withheld
note's own coinage and would have been the most natural genus in the world. It
is out on two counts: it puts the bare word `force` to definitional work, which
the E9 pass's checks record as a thing this house has so far avoided (*"the bare
word `force` never does definitional work here; it appears only inside the
headword"*); and `accounting` is the ledger figure that the
auditable-compositions guide's worked example rejected at E5 as undeclared
residual machinery. Being at Newton II removes the forward-import half of that
objection, not the undeclared-machinery half.

---

## 9. Checks

- reads as a normal dictionary definition in isolation — yes, without
  qualification (§2.2)
- no reference to Newton II, the triplet, or any daughter headword — yes
- no formula, no causal claim, no attitude verb, no imperative, no
  agent-directed deontic — yes
- structurally parallel to E9, its same-headword partner — yes (§2.3)
- ownership enforced grammatically, not described — yes (`its`)
- uniqueness carried by the same word, not separately described — yes (§1.2)
- type stated, since it is not derivable outside the triplet — yes
- unit stated, and grounded by reduction rather than by instrument — yes
- frame present as a validity condition; instance selection left to the trace —
  yes (§4.1)
- provenance closed, and closed by one device only — yes (`exactly two`)
- NML2.1 §3's five forbidden identifications excluded — yes for the lesson
  population, by arithmetic (§5.2); inherited rather than carried outside it
  (§5.4)
- no `force-sum`, `attached-force`, `interacting-forces-set`, `newton meter`,
  `push`, `pull`, or `resultant` — yes, in the positive *and* in the negative
- no bare `force` doing definitional work; the word appears only in the headword
  — yes, unchanged from E8 and E9
- no lesson-installed handle relied on — yes
- zero vector admissible as a value — yes; but the zero-to-no-contributions
  inference is not blocked by the string (§5.4)
- residual entirely grammar-level, headword edges, or stock — yes

---

## 10. The packet's seven open questions

**1. `net-force-material-object[A]` on the left, or the prose owner binder?**
Prose binder, and now for a reason stronger than E8 pass §7's. `[A]` is
skimmable — a reader can execute the definiens without consulting the brackets.
`its` cannot be. At E11 the possessive additionally carries uniqueness (§1.2),
so replacing it with an address mark would cost two properties, not one. Add
that `[A]`'s only installed population is NML2.1's worksheet drill, and a wall's
defining audience is the reader who has not been through it.

**2. Is `assigned to` the best provenance-neutral verb?** The question dissolves.
No ownership verb is needed once a scope clause and a possessive are present.
`assigned` was wrong regardless — it installs a modeller-choice habit that
contradicts NML2.1 §6's *"constraint, not an information generator"* — and
`belonging to`, which two earlier versions of this pass chose, is a description
where `its` is an enforcement (§6).

**3. `at a selected time`, or `time or interval`?** Neither. §4.1: a time index
is an instance selector, not a validity condition, and unlike the frame it
arrives attached to any usable supplied value. It belongs to the trace, where
the packet's `Slots read` already has it. Recorded as a change of position from
earlier versions of this pass, with its cost at §12.3.

**4. Does the unit belong in the entry, or in quantity-type machinery?** In the
entry, and E11 is the only place in the six that can hold it: no corner states
units, and the unit is the outward recognition handle that lets a reader
identify `12 N east` as this quantity before any law is applied. §3.1. Drop
`measured`.

**5. What vocabulary distinguishes `supplied`, `Newton-II-inferred` and
`force-sum-produced`?** None of it goes in the entry. The string carries the
*number* of routes; the vocabulary for individual routes is trace-side, and the
third route belongs to the later entry for this headword (§5.6).

The distinction the entry does *not* draw is the one E9 pass §10.2 raises, and
it still stands: a net force inferred from a trajectory-read acceleration and
one inferred from an acceleration itself computed from a net force have the same
headword, the same value, and different standing. That is one level further back
than the entry reaches, and E9's pass is the place it is owed.

**6. Should E11 perform the E9 consistency comparison?** No. A comparison is an
operation, and this entry is a recognition site. It is a general evaluator
operation over inward/outward pairs. The entry supports it — a value carrying
two provenances under one set of qualifications is exactly the input the check
runs on — without performing it: the wall types the inputs, the evaluator runs
the check.

**7. Should the entry carry a pointer to the later force-sum block?** No. The
provenance field counts the routes available now; the force-sum block will lay
down its own entry for this headword (§5.6) rather than being pointed at from
here by an entry that cannot name it.

---

## 11. What this predicts for the other wall

The remaining wall is the outward entry for `inertial-mass-material-object`.
Called E12 below, on the assumption that the current numbering continues; the
renumbering decision note the packet cites is not in the repository, so treat
the label as provisional and the argument as attached to the *role*.

**Walls contend; corners only avoid.** E10 could be silent about weight, amount
of matter, density and gravitational mass because a reader executing a
determination has nothing to substitute. E12 cannot. Every reader arrives at
the word *mass* with *amount of stuff* and *weight* pre-installed, and
`NML2_1_CONTENT_d2.md` §4.3 already names three meanings that must not be
silently identified.

§5.2 says how to contend: **close the list, do not deny the misreadings.**

But the two walls should not come out the same shape, and §5.3's reasons say
why. E11 counts rather than names because naming reached into the law and
because the routes are recoverable from the lesson while the count is not. For
mass, neither holds. The routes are richer and more error-prone — a given mass,
a scale or known-mass reading standing in as a black-box supplier, and the
bounded Newton-II determination of §6.3 — and §4.3's warning that *"a scale
reading is not to be treated automatically as an inertial-mass measurement"* is
an exclusion a bare count cannot carry, because the scale is not a route the
student would drop from a list; it is one they would wrongly add. Naming is what
excludes it.

More generally: `inertial-mass` has real outward content available — resistance
to motion-change, sideways as well as vertically, which
`NML2_note_net_force_wall_withheld.md` §15.4 calls *"the actual pedagogical
heart of NML2"*. E12 should therefore be a substantial wall of the E5 kind, with
aliases and applicability notes. If E12 comes out as thin as E11, that is a
signal something has gone wrong, not a signal the house is consistent.

**Two rules from this pass that do transfer.** The scope-clause rule of §2.3:
inertial mass is owned, so E12 opens `For a material-object`, and its frame
qualification — if it has one at all — goes in the scope clause. And the
validity/instance rule of §4.1: mass has no time index in NML2.1 at all (§4.2's
reuse licence is explicitly persistent), which is a second confirmation that
temporal qualification is a trace matter rather than a definitional one for
Newton-II quantities.

---

## 12. Open, for the next reader

**12.1 The dangling count.** §5.4. The entry says there are exactly two ways and
the log states only one of them. The alternative, D10, states both and writes
`Newton II` into a peripheral entry. This is a straight trade between an
incomplete pointer and a weakened isolation test, and it is the judgement in
this pass most worth a second opinion. It has a third resolution nobody has
costed: give the supplied route an entry of its own.

**12.2 The zero case.** §5.4. Only D9 blocked the inference from a zero net
force to *no force contributions exist*. It is blocked in the IRIL and in the
lesson. The E10 pass faced the same choice with `0/0` and kept its rider in the
string, on the ground that the case is common and the installed reaction is
wrong; both are true here too. The counter is that any string-level repair has
to mention contributions, which §5.2 rules out. If a wording is found that
blocks it without naming what it blocks, it should go in.

**12.3 The interval, now trace-side.** §4.1. The frame/instance distinction is
new in this pass and has not been tested against anything but E11. The specific
exposure: NML2.1 §12.4's per-interval supplied vectors are exactly the data on
which a student might carry a value from one interval into the next, and after
this change nothing in the entry stops them. If that error shows up in traces,
the repair is a trace-side check, not four words in the string — but the
distinction itself should then be re-examined, because it will have made a
prediction and been wrong.

**12.4 What the count bought on provenance.** D10's `opaque` was the one
lesson-installed handle in the entry, and the auditable-compositions guide is
explicit that such handles *"count as installed for interpreters who passed
through the lesson — if the entry must work outside that population, do not lean
on them."* The chosen entry has no such row in its ledger. Set against §12.1,
this is the same trade seen from the other side: it is cleaner about what it
says and vaguer about what it means.

**12.5 `a` or `one`.** §6. `one` is idle at E11 on the argument given, but the
four Newton-II entries will be read together and three of them say `one`. A
one-character change either way, and the only reason to raise it is that it
should be a decision rather than an accident.

**12.6 The suffix, and the argument E11 supplies.** The E8 pass §8 ranks the
`-material-object` suffix question above every packet open question. E11
sharpens it: this entry's scope clause **states the owner**, so at the wall the
suffix and the definition say the same thing twice. That is a demonstration
rather than an argument. The counter is that the suffix may be reserving the
bare `net-force` headword for the force-sum block to define — which would be a
real job, and would make this a decision about the *next* law rather than about
this entry. It should be settled before E12, not after.

**12.7 Whether the six-entry model is fully satisfied here.** The model says a
wall gives a winter word its outward definition *"independent of the specific
law that introduced it"*. The chosen entry does that completely — no reference
to the law survives — but it does it by giving the word an identity that is a
typed, addressed slot with a counted provenance. That is a weaker kind of
independence than E5's or E6's, which give their winter words substantive
standalone content. Whether the model is satisfied by *outward but thin*, or
requires *outward and substantive*, is not settled anywhere in the guidance, and
E11 is the first entry where the difference bites.
`NML2_note_net_force_wall_withheld.md`'s Option C — that net force has no
independent outward life until force-sum opens — is refuted only if *outward but
thin* counts.
