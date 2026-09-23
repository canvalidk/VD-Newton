# HISTORICAL TERMINOLOGY QUARANTINE

> **Do not use this file as naming authority.** It preserves an earlier state and may use obsolete force-member names. The sole active headword is `impressed-force`, governed by `08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`. Translate any predecessor force-member name to `impressed-force` before carrying content forward. Historical wording does not reopen the decision.

---
# E9 Entry Writing Pass — `net-force-material-object`

Status: independent drafting pass against `ENTRY_PACKET_E9_NET_FORCE_MATERIAL_OBJECT.md`.
Date: 2026-07-25. Companion to `E8_ENTRY_WRITING_PASS_2026-07-25.md`.
Revised after review: the genus is dropped. §2 records the retraction and what the
underlying observation actually shows.

---

## 1. The entry

```text
net-force-material-object :=

For one material-object, its inertial-mass-material-object times
its inertial-acceleration-material-object.
```

Eight words. Structurally identical to E8 — `For one material-object, its D₁ [op]
its D₂` — with no exception clause. The two corners of the triplet now read as the
matched pair a 3-cycle ought to produce.

---

## 2. Retracted: the genus

The first draft of this pass opened `the vector equal to …`, on the ground that E9 is a
birth entry with no chimney behind it and a withheld wall ahead, so nothing else in
the log says what kind of thing net-force is. That argument fails, and it fails by the
rule I had already written into the E8 pass.

**The type propagates, exactly as frame and time do.** E8 §3 says: put in the string
only what this entry alone can carry, because frame and time come down from the
headword and the daughters. The vector type comes down the same way — E10 makes
`inertial-mass-material-object` a positive scalar, E7/K12 make
`inertial-acceleration-material-object` a vector, and scalar × vector = vector is
stock arithmetic. Crucially that derivation runs on **graph edges**, not on residual:
it is the auditable case, not a bet on the reader. `the vector` restated what the
daughters already carry. Same rule, same verdict — I applied it to frame and time and
then failed to apply it to type.

**Also retracted:** the charge that the packet contradicted itself by listing *"the
result is one vector addressed to one material object"* under **Preserve** and then not
writing `vector`. Preserve names a property that must remain true of the result, not a
string that must appear. Scalar × vector yields one vector; the property is conserved.
The packet was consistent and I misread the field.

**Not load-bearing either way:** that E11 will call it a vector. E11 is appended after
E9, so it cannot license anything at E9's position, and it is the entry most likely not
to land at all. The argument above holds without it, and it should not be reused where
it would have to stand alone.

### What the observation actually shows

E9 *is* a birth entry and E8 is not, and that difference is real. It just does not
cash out as a missing genus. It cashes out here:

Newton I's winter words were born with genera that did substantive outward work —
`inertial-frame` is **a reference-frame**, `free-particle` is **a point-particle**.
Each names a licensed prior concept the new word is a species of. Ask the same question
of net-force and there is no answer available. The only candidate is `force`, and
`force` is precisely what NML2.1 forbids importing.

So `net-force-material-object` is a winter word born with **no genus available** —
a rarer condition than a winter word whose genus was forgotten. `the vector` was a
substitute genus assembled from type information, and type is the one kind of genus
that is derivable, hence the one kind that does no work.

This explains the withheld wall better than the working note does. `NML2_note_net_force_wall_withheld.md`
§3 rejects the two candidate walls separately — *"total force"* smuggles in force-sum,
*"the force that causes acceleration"* blurs the triplet. Those are the only two
candidates, and they fail for one underlying reason: neither has a licensed prior
concept standing behind it. Withholding E11 is therefore not a pedagogical preference
that could have gone the other way. It is forced, and it stays forced until force-sum
opens. Which also tells E11 what its job is when it does land: **supply the genus E9
could not.**

---

## 3. Carried over from E8 without change

- **`[A]` replaced by the English possessive.** The address mark is skimmable — a
  reader can execute `m × a` without ever consulting the brackets — whereas `its`
  cannot be parsed until an owner is found, and English will not let the second `its`
  bind elsewhere. Grammar-level machinery, the guide's strongest provenance category,
  at zero token cost. Full argument in the E8 pass, §2.1.
- **Naming `material-object` is a gain.** It converts the ownership constraint from a
  residual mark into a graph edge, which is the direction the entry-writing guide asks
  entries to move in. E8 pass, §2.2.
- **Frame and time stay out**, on the ground that owner is the only co-qualification
  no daughter entry can state. E8 pass, §3 — and now §2 above, applied to type.
- **Noun-phrase definiens**, matching every quantity entry in the corpus.
- **Positivity left to E10**; see §5, where E9's case is stronger than E8's.

---

## 4. `times`, not `multiplied by`

The packet's decision 2 sets the residual to `multiplied by`, echoing E8's
`divided by`. Its ancestor said `times` — *"net-force = inertial-mass times
inertial-acceleration"* — and the packet changed the word without recording that it
had. I am changing it back, for a reason beyond provenance.

`multiplied by` presents two symmetric operands. `times` presents a **scaling**:
*three times the length*, *m times the acceleration*. With a vector operand the
scaling reading is the one English delivers, and scaling is precisely the reaction the
packet's own IRIL asks for — *"Multiply a positive scalar by a vector and preserve the
vector direction."* Direction-preservation is a property of scaling, not of symmetric
product. `times` triggers it; `multiplied by` leaves it to be inferred.

It is also the shorter word, and scalar-first order (retained from the packet) already
makes the scalar-by-vector typing visible — which is part of why §2's derivation runs
so cleanly that the word `vector` is redundant.

The lexical pair `divided by` / `times` is unmatched across the two corners, and that
is an acceptable cost: what must be symmetric is the *structure*, and it is. Note also
that E8's case for `divided by` over `/` was **visibility** — a symbol can be skipped,
a word cannot. That argument does not transfer, because `times` is already a word.

---

## 5. Two places where the packet copied E8's reasoning across a real difference

**5.1 The mass failure mode is not the same at this corner.** The packet's boundary
list carries *"undefined/domain boundary: inertial mass lacks a positive licensed
referent"*, and blocks *"multiplying by a missing, zero, negative, undefined, or
unlicensed inertial-mass value"* — E8's categories, transplanted. But at E8, zero mass
is an *arithmetic* failure: the quotient does not exist. At E9, multiplying by zero or
by a negative is perfectly well defined and returns a vector. Nothing about E9's
arithmetic can fail.

So E9 has **no undefined case at all**. Every one of its mass failures is a licence
failure — E10 says inertial mass is a positive scalar, and a value violating that was
never a licensed input. The boundary category should be `unlicensed input`, not
`undefined referent`; the two produce different halts and different things to say to a
student. This also sharpens why positivity must not be restated in E9: at E8 one might
at least argue positivity guards the division, whereas at E9 it does no work
whatsoever except E10's.

**5.2 The E8↔E9 cycle is load-bearing, and stronger than the packet says.** The packet
notes that *"a cycle with no second independent value terminates as insufficient
information."* True, but it undersells what has been built: because E11 is withheld,
`net-force-material-object` is born with **no independent access route in the
dictionary at all**. It can only be supplied as problem data or inferred through E9.
The content spec's doctrine — *"Newton II is a constraint, not an information
generator"* — is therefore not merely taught in NML2.1; withholding the wall makes it
structurally impossible to violate. Worth recording as a positive result of the
withholding decision, which is currently filed as a pedagogical cost.

Neither point changes the entry string. Both belong in the packet's boundary and
trace-consequence fields.

---

## 6. Drafting record

```text
D1  net-force-material-object[A] :=
    inertial-mass-material-object[A] multiplied by
    inertial-acceleration-material-object[A].
```
Packet's candidate A. Rejected on the address mark (E8 pass §2.1) and on the verb (§4).

```text
D2  For one material-object, the vector equal to its inertial-mass-material-object
    times its inertial-acceleration-material-object.
```
Chosen in the first version of this pass; retracted per §2. The genus restates what
the daughters carry.

```text
D3  … the vector product of its inertial-mass-material-object and its
    inertial-acceleration-material-object.
```
Rejected hard, and recorded as a standing trap for E10 and the walls: **`vector
product` is the cross product.** `scalar product` is the dot product. Both are terms
of art with installed reactions that are flatly wrong here. `product` must not appear
near `vector` anywhere in this house, which also rules out the otherwise natural
*"the product of its mass and its acceleration."*

```text
D4  … the vector given by its inertial-mass-material-object times …
```
Rejected on vocabulary collision, and also standing guidance beyond E9: `given` is a
term of art throughout NML2.1 — *"a given mass belongs to a material-object"*,
*"already supplied inertial masses"* — where it means **handed to you as problem
data**. Using `given by` for a value the dictionary *computes* inverts the machinery
vocabulary the guide asks residual wording to match.

```text
D5  … the vector satisfying net-force-material-object = its
    inertial-mass-material-object × its inertial-acceleration-material-object.
```
The ancestor D2[E22]'s implicit-definition shape. Rejected: self-reference plus a
symbol string, the free-floating-symbol form the packets forbid. Worth recording that
the shape was doing something real — birth-by-constraint — and that the explicit
product now does that job in plainer words, without needing the genus the ancestor
carried.

```text
D6  For one material-object, its inertial-mass-material-object times
    its inertial-acceleration-material-object.                          ← chosen
```

Minimality check: drop the scope clause and both possessives lose their antecedent;
drop either `its` and that input floats free. Nothing is removable.

---

## 7. Residual provenance ledger

| Phrase | Backing |
|---|---|
| `For one …` | Grammar-level scope idiom; house style across K3, K9–K15 and D2[E22]. `one` triggers singularity, which is what cross-target borrowing violates. |
| `its` (×2) | Grammar-level possessive anaphora. Population-independent, unparseable without a referent, cannot bind two referents in a coordinate structure. |
| `times` | Stock arithmetic, and the ancestor's word. Triggers scaling rather than symmetric product, which is what preserves the vector's direction. |
| scalar before vector | Conventional Newton-II order; makes the scalar-by-vector typing visible without explanatory prose, and is what lets the result's type be derived rather than declared. |

No row is backed by this writer's invention. The ledger is now four rows against E8's
four — the two corners cost the same residual, which is the right outcome for a
symmetric pair.

---

## 8. Checks

- exactly two daughter headwords exposed — yes
- same-owner constraint enforced rather than described — yes, grammatically
- result type derivable from the daughters through graph edges, not declared — yes (§2)
- no force-sum, `interacting-forces-set` or `attached-force` — yes
- no push, pull or meter reading — and the bare word `force` never does definitional
  work here; it appears only inside the headword, so the ordinary force concept is not
  leaned on for anything, type included
- no `free-particle`, and the zero case falls out of the arithmetic without any licence
  to infer free-particle status or absence of contributions
- no causal claim — a scaling is not a causing
- positivity, provenance and licence left to their owners — yes, and §5.1 shows E9's
  case for silence is stronger than E8's
- structurally symmetric with E8 — yes, and now with no exception at all

Carried over unchanged: `F = ma` and `a = F/m` are algebraically interderivable, so
each corner yields the law's algebra. The corners differ in what they determine from
what, not in algebraic content, and the daughter-to-daughter relation stays unstated —
which is what the six-entry model requires.

---

## 9. What this predicts for E10

Dropping the genus makes the house regular, which makes the next corner's exception
visible instead of lost among three differently-shaped entries. On the pattern, E10
wants:

```text
For one material-object, its net-force-material-object divided by
its inertial-acceleration-material-object.
```

and that is where the pattern must genuinely break. E10 carries the positive-scalar
law role, and vector-by-vector division is not an operation. So E10 is the one corner
that cannot be a bare arithmetic expression over its two daughters — which is worth
knowing before its packet is opened, and is the sort of thing three same-shaped
entries reveal and three differently-shaped entries hide.

---

## 10. Open questions

The packet's five carry over from E8, and the E8 pass answers its first (address
binding belongs in a declared structural field, not the definiens) and ranks the
headword-suffix question above all of them. That question is unaffected by this
revision: the chosen entry is 107 characters, against 75 for the same eight words
under short headwords.

Two are E9's own:

**10.1 Does `inertial-acceleration-material-object` mean the E7 quantity or the E8 one,
when E9 reads it?** E9's `Slots read` names `inertial-acceleration-material-object`,
and the packet's trace consequence says *"If inertial acceleration is absent, demand
E8/E7"* — E8 **or** E7. Those are different routes to the value: E7 reads it from a
trajectory, E8 computes it from `F/m`. Taking E8's route inside E9 closes the trivial
cycle `F → a → F`. Taking E7's is the substantive case, and is the one the content
spec's *Mystery net-force sheet* is built on. The entry string cannot and should not
distinguish them — but the packet should say which demand E9 issues, because
*"demand E8/E7"* silently permits the circular one.

**10.2 Should E9 record which route produced the acceleration it consumed?** The
packet's open question 5 asks whether `Newton-II-inferred` needs a provenance tag
distinct from `supplied`. §10.1 suggests yes, and that one bit is not enough: a net
force inferred from a *trajectory-read* acceleration is an empirical result; a net
force inferred from an acceleration that was itself computed from a net force is a
tautology. Same headword, same value, different epistemic standing. The provenance tag
has to reach one level further back than the packet proposes.
