# E8 Entry Writing Pass — `inertial-acceleration-material-object`

Status: independent drafting pass against `ENTRY_PACKET_E8_INERTIAL_ACCELERATION_MATERIAL_OBJECT.md`.
Date: 2026-07-25.
Outcome: entry chosen; three of the packet's decisions are contested; one of its
open questions is answered; one new open question is raised that outranks the rest.

---

## 1. The entry

```text
inertial-acceleration-material-object :=

For one material-object, its net-force-material-object divided by
its inertial-mass-material-object.
```

Nine words. Every one is load-bearing:

| Word | Job |
|---|---|
| `For one material-object` | scopes the entry and supplies the antecedent the two possessives need |
| `its` (×2) | binds both inputs to that one object — grammatically, not by convention |
| `divided by` | the operation, and its direction |

Nothing else is present, because nothing else is E8's.

---

## 2. Three departures from the packet

### 2.1 `[A]` is replaced by the English possessive

The packet chose `inertial-acceleration-material-object[A] := net-force-material-object[A]
divided by inertial-mass-material-object[A]`, on the grounds that this makes the
same-owner constraint *structural rather than explanatory*.

It does not. It makes it **inert**.

Apply the entry-writing guide's own test — who installed the reaction the phrase
bets on? `[A]` bets on two things: ordinary algebraic indexing, and NML2.1's
worksheet drill (*"Rewrite free-floating symbols as `m[A]`, `a[A]`, and `F_net[A]`"*).
The first is real but weak; the second is a lesson-installed handle, and the guide
is explicit that those *"count as installed for interpreters who passed through the
lesson — if the entry must work outside that population, do not lean on them."*
The dictionary is not the lesson.

The decisive point is not provenance but **routing**. The guide's caution is that an
installed handle *must also route*. `[A]` does not route, because a reader can
execute the whole definiens without ever consulting the brackets. `F/m` is
computable while the addresses go unread. The bracket is skimmable; the constraint
it carries — which the packet itself calls the lesson's central error — is therefore
skimmable too.

`its` cannot be skimmed. A possessive is not parseable until a referent is found.
The reader who reaches `its net-force-material-object` has already been forced to
locate an owner, and English anaphora will not let the second `its` pick a different
one. The same-owner constraint is enforced by grammar-level machinery — the guide's
first and strongest provenance category — at a cost of zero extra tokens.

So the packet had the comparison backwards. `[A]` is the *explanatory* option
(a mark that documents ownership); `its` is the *structural* one (a construction
that cannot be completed without it).

### 2.2 Naming `material-object` is a gain, not a cost

The packet rejected its own candidate B partly because it *"repeats `material-object`
as an additional visible headword inside the triplet."* But the guide says the
opposite about headword mentions: *"Headword edges. Not residual at all; the
auditable case. Prefer moving load here when possible."*

Naming the owner concept converts the ownership constraint from a residual mark into
a graph edge. That is the direction the guide asks entries to move in. It is also
house style: E3 names `reference-frame` (not a Newton I triplet member) as its genus,
and every kinematic quantity entry opens with a `For a …` scope clause naming
non-triplet headwords. A triplet entry must *expose* its two daughters; it was never
required to mention nothing else.

### 2.3 The definiens is a noun phrase, not a formula fragment

Candidate A is a bare quotient. Every quantity definition in
`DESIGN_2_1_DRAFT_1_ENTRIES.md` — K3, K9–K15 — is a noun phrase with a scope clause,
and the direct ancestor D2[E21] was a full sentence (*"For a point particle, inertial
acceleration equals net force divided by inertial mass"*). The chosen entry keeps the
ancestor's `For a …` opener and its `divided by`, and drops only the trailing
`a = F/m`, which is the free-floating-symbol form the packet correctly rejects.

**Retained from the packet, and right:** `divided by` over `/` (installed at stock
strength; harder to overlook); positivity left to E10; frame left to the headword's
own `inertial`; no causal prose; no trajectory content.

---

## 3. Why frame and time stay out, on a better argument than the packet's

The packet's decision 4 asserts that frame, time, provenance and licence are trace
qualifications. That is the right call, but the packet gives no reason, and the
asymmetry looks arbitrary: if owner is structural, why not interval, which the
content spec lists among the errors to be diagnosed?

The reason is this:

> **Owner is the only co-qualification that no daughter entry can state.**

Frame propagates down from the headword — `inertial` fixes it, and a quotient
inherits it. Time propagates the same way: the acceleration is at a selected time,
so the net force must be. At this corner only one input is time-varying, so a single
inherited tag fully determines the result's time; there is no second time to
mismatch.

Ownership does not propagate. Each daughter headword says its quantity belongs to
*a* material-object, indefinitely. That the two are the *same* one is a relation
between the daughters, and no daughter can say it. Only the triplet corner can.

Put in the string exactly what only this entry can carry. That rule yields owner in
and frame/time out, and it survives the question the packet's decision 4 does not.

A corollary worth recording: E8 needs no `when defined` clause — unlike K10 and K12,
which carry one because a derivative can fail to exist for otherwise-valid inputs.
Vector-by-positive-scalar division never fails. That clause is absent *because*
E10 carries positivity, which is the sharpest available reason not to restate
positivity here.

---

## 4. Drafting record

```text
D1  inertial-acceleration-material-object[A] :=
    net-force-material-object[A] divided by inertial-mass-material-object[A].
```
Packet's candidate A. Rejected: the address mark is skimmable, so the constraint is.

```text
D2  The inertial-acceleration-material-object of a material-object is its
    net-force-material-object divided by its inertial-mass-material-object.
```
Newton I sentence style (E2–E4). Correct but long, and repeats the headword for no
gain — the Newton I entries repeat it because they define properties, not quantities.

```text
D3  A material-object's net-force-material-object divided by its
    inertial-mass-material-object.
```
Two words shorter than the chosen form. Rejected: `A material-object's
net-force-material-object` collides the possessive with the suffix immediately, and
`A` reads generically where `one` reads singularly — and singularity is the point.

```text
D4  For one material-object at a selected time, its net-force-material-object
    divided by its inertial-mass-material-object.
```
Tested against K13's precedent (*"For two point-particles in the same
reference-frame at the same selected time"*). Rejected by §3: the time tag is
inherited, and admitting it invites the frame clause too, and then the entry is a
qualification list rather than a relation.

```text
D5  For one material-object, net-force-material-object divided by
    inertial-mass-material-object, with both belonging to that same
    material-object.
```
Packet's candidate B. Rejected: the trailing clause *explains* the constraint that
`its` *enforces*. Length is the symptom; explanation is the defect.

```text
D6  For one material-object, its net-force-material-object divided by
    its inertial-mass-material-object.                            ← chosen
```

Minimality check on D6: drop the scope clause and both possessives lose their
antecedent; drop either `its` and that input floats free — the exact defect the
packet's *Change/reject* list forbids. Nothing is removable.

---

## 5. Residual provenance ledger

| Phrase | Backing |
|---|---|
| `For one …` | Grammar-level scope idiom; house style across K3, K9–K15 and D2[E21]. `one` rather than `a` triggers singularity, which is what the cross-target error violates. |
| `its` (×2) | Grammar-level possessive anaphora. Innate, language-wide, population-independent. Cannot be parsed without fixing a referent, and cannot bind two different referents in a coordinate structure. |
| `divided by` | Stock arithmetic already installed in the target culture; directs vector-by-positive-scalar division at stock strength; the word form resists the visual skip that `/` permits. |
| dividend before divisor | Ordinary arithmetic grammar; matches D2[E21] without adding causal prose. |

No row is backed by this writer's invention.

---

## 6. Checks

- exactly two daughter headwords exposed — yes
- same-owner constraint enforced, not described — yes, grammatically
- no E7 chimney content (trajectory-read, frame) repeated — yes
- no wall, force-composition, measurement or trajectory-construction content — yes
- no causal prose, no attitude verb, no imperative — yes
- positivity, provenance, licence left to their owners — yes
- residual entirely grammar-level or stock arithmetic — yes
- symmetric with the intended E9 (`net-force = its inertial-mass times its
  inertial-acceleration`) and E10 — yes, and the same `its` device carries across
  all three corners, which is worth confirming when E9 and E10 are drafted

One honest caveat, unchanged from the packet: `a = F/m` is algebraically
interderivable with `F = ma`, so E8 alone yields the law's algebra. The corners
differ in what they *determine from what*, not in algebraic content. The thing no
corner states — the daughter-to-daughter relation — remains unstated here, which is
what the six-entry model actually requires.

---

## 7. The packet's open question 1, answered

> *Does the engine preserve the base headword match when `[A]` is appended, or
> should address arguments be represented in a separate syntax while retaining
> the same human-facing entry?*

Separate syntax — and the choice is not a tokeniser convenience, it is the guide's
two-pillar rule.

The entry string is the human-facing artifact and must compose only from installed
reactions; that is `its`. The graph needs a checkable variable, and anaphora is not
resolvable by a tokeniser; that is a declared structural field. The packet's own
format already separates entry string from structure — *slots read*, *slots
written*, *witness kind*. Addressing belongs there:

```text
Address binding:
  one material-object address, shared by the headword instance,
  net-force-material-object, and inertial-mass-material-object.
```

Both pillars then hold, and neither is asked to do the other's job. Embedding `[A]`
in the definiens is the failure mode where the string is bent toward the engine and
loses the reader.

---

## 8. A question that outranks the packet's five

**Is `material-object` a licensed headword at this point in the log, and if it is,
do `net-force` and `inertial-mass` need the suffix at all?**

Two findings sit behind this.

*First:* the `-material-object` headwords appear nowhere in the repository outside
this packet. `DESIGN_2_1_DRAFT_1_ENTRIES.md` has no `material-object` entry.
All three Newton II headwords embed the term, so if it is unlicensed the defect is
in the headwords, not in any entry that mentions them. If it is licensed, §2.2
applies and naming it is free.

*Second, and sharper:* `VD_Newton_inertial_acceleration_two_entries.md` explicitly
retracted domain-encoding in headword strings — *"The `_point-particle` /
`_massive-particle` headword encoding. This encodes a domain into the headword
string. The correct cut is by relation-to-the-second-law, not by object domain."*
The `-material-object` suffix is domain-encoding in the headword string.

For `inertial-acceleration` the suffix is at least doing a real job: it separates
the Newton-II-related entry from the free-particle one, which is the definitional-role
cut the note endorses — though on that note's own argument the suffix should name
the *role*, not the object domain. For `net-force` and `inertial-mass` there is no
competing entry and no cut. Their suffixes are decoration.

The cost is not cosmetic. Compare:

```text
inertial-acceleration-material-object :=
For one material-object, its net-force divided by its inertial-mass.
```

The same nine words — but 68 characters against 100. The suffixes are not adding
words, they are adding a third to the length of every word that matters, and the
same tax lands on E9, E10, E11, E12 and every later entry that mentions net force
or mass. The entry above is what E8 wants to be. Resolving the suffix question is worth more
to this house than any of the five questions the packet carries forward.
