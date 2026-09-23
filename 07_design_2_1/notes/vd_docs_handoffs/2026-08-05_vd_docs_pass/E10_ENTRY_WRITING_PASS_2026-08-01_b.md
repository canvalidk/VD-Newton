# E10 Entry Writing Pass — `inertial-mass-material-object`

Status: independent drafting pass against
`ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d5.md`.
Date: 2026-08-01. Second pass of that date; filed `_b` to avoid colliding with
`E10_ENTRY_WRITING_PASS_2026-08-01.md`. Rename freely.

**Constraint on this pass.** Written blind to every prior E10 entry writing pass,
by instruction. Sources read: the d2–d5 packets, the E8 and E9 passes, the law
writing guide, `why_reconciliation_cannot_be_upstream_of_E10.md`,
`why_the_mass_entry_must_be_long_joint_measurement_d3.md`, `NML2_1_CONTENT_d2.md`,
and the pedagogy note. No E10 pass was opened. Any agreement with the earlier
passes is convergence, not inheritance; any disagreement is a genuine second
opinion and should be read as one.

---

## 1. The entry

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
If both are exact, check that they are codirectional and then divide the
net-force magnitude by the inertial-acceleration magnitude; a zero-zero pair
leaves the scalar undetermined. If either is measured, estimate two underlying
codirectional vectors and then recover the positive scalar relating them.
```

57 words, 444 characters. The d4/d5 carried candidate is 137 words, 1000
characters. Under short headwords this entry is 412 characters — the suffix tax
on E10 is now 32 characters rather than the ~200 it was, because the quantities
are named in full once and by magnitude thereafter.

---

## 2. The shape, and why it is this shape

The entry says one thing three times at descending scope:

```text
mass is the positive scalar relating a codirectional pair
  exact inputs   -> CHECK codirectionality, then read the scalar
  measured inputs -> ESTIMATE codirectionality, then read the scalar
```

Both branches secure codirectionality first and read the scalar second. That is
not a stylistic parallel; it is the content. `why_reconciliation_cannot_be_
upstream_of_E10.md` §"Terminological care" says the magnitude quotient reads an
already-established relation rather than establishing it, and d3 §1 says the same
of the exact branch. The only difference between the branches is *how* the
relation gets established — by inspection when the values are stipulated, by
estimation when they are not.

Making the two branches one shape is what carries the estimation across to a
reader who has never estimated anything. The student already knows step two; they
have done it on the exact branch. What is new on the measured branch is only that
step one is now an estimate rather than a check. That is a much smaller thing to
learn than "there is a second, statistical procedure for measured data", which is
what the longer wordings communicate.

### Why `if`

Technically the entry does not need it. The measured branch is the general case
and the exact branch is its degenerate instance, so a single estimation clause
would be sufficient and would be shorter still.

It is used anyway, and for one reason: **it forces the reader to classify their
inputs before they can act, and the classification is exactly the one that
separates what they can do from what they cannot.**

- `If both are exact` — the reader can run this. Division is installed.
- `If either is measured` — the reader cannot run this. Estimation is not
  installed, and per d5 it is never going to be, because it lies outside the
  dictionary.

Both branches terminate. The first terminates in a number; the second terminates
in a named operation the reader can recognise, request, or hand off. Under the
pedagogy note's criterion — a student is confused when a word points onward but
not to anything they can act with — a named external operation is a termination
and a silent one is not.

A useful side effect: an input with no epistemic classification satisfies neither
`if`, so no branch opens at all. Acceptance test 11 (halt for classification) is
enforced by the sentence structure rather than by a clause about it.

`both` and `either` are load-bearing and are not interchangeable. `both` is the
restrictive quantifier and `either` the permissive one, so the pair is exhaustive
and non-overlapping, and a mixed pair — one supplied exact value, one measurement
— routes to estimation, which is correct. The routing turns on where a value came
from, not on how it looks on the page, which is what acceptance test 6
(displayed alignment) requires.

---

## 3. What was cut, and on whose authority

The d4/d5 candidate carries four things this entry does not. Each cut is
authorised by d5's own results, not by a preference for brevity.

| Cut | Authority |
|---|---|
| `Retain the original measurements, their uncertainty and discrepancy, the policy, and their provenance.` | d5 §"What E10 is not required to establish" and decision 8: retention rests on the separate self-confirmation chain and belongs to the evaluator. Conflating the two chains "is what lets evaluator requirements migrate into the definitional core and inflate the entry." |
| `If either result already depended on the mass being sought … consistency restatement.` | Same chain. Evidential standing is a property of the result, not a step the reader performs at this node. |
| `keep the two results separate and check their provenance` | Same. What the entry must carry structurally is that the estimate happens *inside* the mass determination; siting the estimate in E10's own definiens carries it without a clause. |
| `if no policy is available, report that estimation is required` | The `if either is measured` branch already leaves a reader without an estimator holding a named operation they cannot perform. `EstimationRequired` is the evaluator's name for that state, not a further instruction. |

Two further compressions:

**`jointly` is dropped.** d5's audit says `jointly estimate` "declares that
neither latent vector is selected independently once the Newton-II constraint is
imposed." But `codirectional` already says that: two vectors cannot be estimated
to be codirectional independently of one another. The adverb restates the
constraint the adjective enforces — the same defect E8's pass found in its D5 and
rejected. The Preserve list's protected lesson-facing route omits `jointly` too.

**The exact no-fit clause is dropped** (`any other incompatible exact pair has no
exact positive-mass fit`). This is the pass's most arguable cut; see §7.

---

## 4. Drafting record

```text
D1  For one material-object, its net-force-material-object divided by
    its inertial-acceleration-material-object.
```
The pattern-continuation E9's pass §9 predicted E10 would want. Rejected for the
reason that pass gives in advance: vector-by-vector division is not an operation.
Recorded because the shape is what a reader arriving from E8 and E9 expects, and
the entry has to break it visibly enough that the reader does not supply it.

```text
D2  For one material-object, the positive scalar that multiplies its
    inertial-acceleration-material-object to give its net-force-material-object.
```
Correct, and it survives as sentence one. Rejected as the whole entry by horn one
of the governing dilemma: independently determined vectors are generically
non-conforming, so a definition that only names the scalar is inert over the
entire domain traces actually run on. Note that D2 fails for a reason no reading
of D2 reveals — which is why it is worth having the horn.

```text
D3  … Therefore the two point the same way, and the scalar is the net-force
    magnitude divided by the inertial-acceleration magnitude.
```
Rejected. Independently rederived, and then found to match d3's rejection of its
own candidate D: `Therefore` asserts codirectionality, so a measured mismatch
contradicts an assertion. The installed reactions to a contradicted assertion are
"the law failed" and "the object has no mass" — the catastrophic fork. The entry
needs the reader to *check* rather than to *be told*, because a failed check
indicts the values and a contradicted assertion indicts the world.

```text
D4  If the values are exact … if they are measured …
```
Rejected on the quantifiers. `the values` and `they` treat the pair as a unit and
leave the mixed case unrouted; `both` and `either` route it, and route it the
right way. See §2.

```text
D5  … For empirical force and acceleration measurement results, keep the two
    results separate and check their provenance. … Retain the original
    measurements, their uncertainty and discrepancy, the policy, and their
    provenance. …
```
The d4/d5 shape. Rejected here per §3. Every clause is true and none of them
changes which branch a reader takes or what they do on it. They describe the
standing of a result rather than trigger an operation, which makes them evaluator
requirements wearing an entry's clothes.

```text
D6  … check that they point the same way … estimate two underlying
    codirectional vectors …
```
Rejected on vocabulary. `point the same way` is the stronger trigger in
isolation, but using it alongside `codirectional` names one condition twice
inside one entry, and a reader who does not know they are the same condition will
read the branches as testing different things. Unified on `codirectional`, which
`NML2_1_CONTENT_d2.md` §6.3 defines outright ("parallel and pointing in the same
direction") and which a reader who does not know it can terminate by lookup. Used
twice, it becomes the entry's hinge rather than its jargon.

```text
D7  … divide the net-force magnitude by the inertial-acceleration magnitude.
    If either is measured, …
```
The zero rider dropped. Rejected. The rest trial — zero net force, zero
acceleration — is the commonest situation a student will ever point this entry
at, and `0/0` is only *nearly* self-triggering: the installed reaction is
"undefined", the required reaction is "not fixed by these values, and the object
still has a mass". Six words buy the difference, and they buy it exactly where
the reader has just produced the `0/0`.

```text
D8  For one material-object, the positive scalar that multiplies its
    inertial-acceleration-material-object to give its net-force-material-object.
    If both are exact, check that they are codirectional and then divide the
    net-force magnitude by the inertial-acceleration magnitude; a zero-zero pair
    leaves the scalar undetermined. If either is measured, estimate two
    underlying codirectional vectors and then recover the positive scalar
    relating them.                                                    ← chosen
```

Minimality check on D8. Drop `For one material-object` and both possessives lose
their antecedent. Drop either `its` and that input floats free. Drop `positive`
and the algebra admits a negative scalar and antiparallel motion — the commitment
E8 and E9 both delegate here. Drop `check that they are codirectional and then`
and the entry licenses the magnitude quotient in exactly the cases where the law
fails. Drop either `if` and one class of reader is left with no route. Drop
`underlying` and the measured values become the law's quantities. Drop the
zero-zero clause and see D7. Nothing else is removable; `and then` appears twice
on purpose, and is the parallel.

---

## 5. Residual provenance ledger

| Phrase | Backing |
|---|---|
| `For one …` | Grammar-level scope idiom; house style across E8, E9, K3, K9–K15. `one` triggers singularity, which cross-target borrowing violates. |
| `its` (×2) | Grammar-level possessive anaphora. Cannot be parsed without fixing a referent and cannot bind two referents in a coordinate structure, so it enforces same-owner rather than describing it. |
| `positive scalar` | Newton II's own commitment. Excludes the antiparallel fit the triplet algebra otherwise admits, and states isotropic response. Not derivable from E8 or E9, both of which delegate it here. |
| `multiplies … to give` | Stock scalar-by-vector arithmetic, scalar before vector, matching E9's `times`. States the inward relation without inventing vector division and without going near `product` (E9's standing trap). |
| `If both … If either …` | Grammar-level quantifiers. Exhaustive, non-overlapping, and provenance-keyed; they halt on an unclassified input without a clause saying so. |
| `exact` / `measured` | `NML2_1_CONTENT_d2.md`'s own branch vocabulary, and d5 decision 1: this is the *dispatchable* form of the distinction — a reader at the node can answer it. |
| `check that they are codirectional and then divide …` | d3 §1 and the type-theoretic analysis §§1–6: compatibility is established first and the magnitude quotient reads the result. `check` localises failure to the supplied values, which `Therefore` (D3) does not. |
| `a zero-zero pair leaves the scalar undetermined` | Newton II admits every positive mass for the exact zero/zero pair. `leaves … undetermined` blames the pair, not the object; it is not `no mass` and not `zero`. |
| `estimate two underlying codirectional vectors and then recover the positive scalar relating them` | Protected verbatim from the d5 Preserve list and d3 §8's minimum honest handoff. `underlying` is what stops the measurements being read as the law's quantities. Siting it inside E10's definiens is what locates the estimation inside the determination rather than upstream of it. |

No row is backed by this writer's invention. The two branch selectors and the
protected route are quoted from live documents; everything else is grammar or
stock arithmetic.

---

## 6. Checks

- exactly two daughter headwords exposed — yes
- same-owner constraint enforced rather than described — yes, grammatically
- positivity carried, as E8 and E9 require — yes
- no vector-by-vector division stated or implied — yes
- compatibility established before the magnitude quotient — yes, on both branches
- branch selected by provenance, not by displayed alignment — yes (`either`)
- measured values distinguished from the law's quantities — yes (`underlying`)
- estimation sited inside the mass determination, not upstream — yes, structurally
- no estimator, policy, covariance model or fitting rule named — yes
- no entry number for the estimation capability — yes
- no scale, weight, gravitational mass, density mass or amount of matter — yes
- no additivity, persistence, trackability, lumping, or force composition — yes
- no `product` near `vector`, no `given by` for a computed value — yes
- every opened branch terminates — yes (number, named outcome, named operation,
  or halt-for-classification)
- residual entirely grammar-level, stock arithmetic, or quoted from live docs — yes

One property of E8 and E9 is deliberately broken: **this entry uses imperatives.**
E8's checks record "no causal prose, no attitude verb, no imperative". E10 cannot
keep that. Since d2 the house position has been that a determination step the
string does not trigger is machinery living where no audit reaches; the
imperatives are the trigger. E9's pass §9 predicted this corner would be the one
where the pattern genuinely breaks, and it breaks here, in the mood of the verb.

---

## 7. Acceptance tests, and the two the string leaves to inference

Walking d5's fifteen:

| # | Result |
|---|---|
| 1 | exact codirectional → `6/2 = 3 kg`. Clean. |
| 2 | exact zero/zero → named by the rider. Clean. |
| 3 | exact one-zero → **inferred**, see below. |
| 4 | exact antiparallel / oblique → **inferred**, see below. |
| 5 | oblique measured, no policy → `either is measured` → named operation, unperformable → estimation required. Clean. |
| 6 | aligned measured, no policy → same, because the selector is provenance. Clean. |
| 7 | measured with licensed policy → estimate, then recover. Clean; result fields are evaluator-side. |
| 8, 9, 13 | evaluator-side by d5 decision 8 and the Change/reject list. Deliberately not in the string. |
| 10 | `underlying` keeps the measurement and the latent value distinct. Clean. |
| 11 | neither `if` fires → no branch opens. Enforced by structure. |
| 12 | `For one material-object … its … its`. Clean. |
| 14 | structural, not a property of the string. |
| 15 | the string names no entry. Clean. |

**Tests 3 and 4 are the honest weakness of this pass.** The exact one-zero and
exact non-codirectional cases have no named outcome in the string. The reader
runs the check, it fails, and they are left to conclude that no positive scalar
fits the supplied values.

Kept out anyway, on three grounds. First, `check` already localises the failure to
the values rather than to the object, so the catastrophic fork — "no mass" — is
not the natural reading of a failed check the way it is of a contradicted
assertion. Second, sentence one is still in scope: no positive scalar multiplies
zero to give a nonzero net force, and none takes a vector to a vector pointing
elsewhere. The reader who asks "which positive scalar?" gets "none" from the
relation itself. Third, an exact non-codirectional pair only ever arrives as a
deliberately constructed probe; the ordinary route for a mismatched pair is the
measured branch, and that branch is named.

If reader testing shows this cut is wrong, the repair is one clause — `no other
exact pair admits one` — and it costs six words. It should be added on evidence,
not on principle.

---

## 8. What this pass does not touch

Unchanged and unchallenged: the governing correction, the three-stage
architecture, `JointNewtonIIFit` and its result contents, the circularity gate,
the lesson boundary's teach / must-not-teach lists, the IRIL and IRIEs, the
evaluator routing, and the permanence of capability-naming. This pass is a
wording pass. It moves four requirements out of the string and into the evaluator
where d5 already says they live; it does not remove them from the account.

The headword suffix question, which the E8 pass ranks above every packet open
question, is untouched. This entry is unusually cheap under it — 32 characters —
because sentence one names both quantities in full and sentences two and three
refer to them by magnitude and by anaphora. That is a small argument that the
suffix tax is partly a symptom of restating headwords, not only of their length.

---

## 9. Open, for the next reader

1. **Tests 3 and 4.** §7. The one cut in this pass made on judgement rather than
   on d5's authority.
2. **`codirectional` versus `point the same way`.** Unified on the former for
   consistency. Whether the plainer phrase is a strong enough trigger to be worth
   using in *both* positions — breaking the Preserve list's protected route to do
   it — is a question for reader testing, not for argument.
3. **Where `undetermined` lands.** It is meant to be heard as "these values do
   not fix it", not as "there is none" and not as "it is zero". This is the
   single word in the entry most likely to fail empirically, and it sits on the
   most common case a student will meet.
4. **Whether an entry may be this short.** d3 §7 argues at length that E10 must
   be long. This entry accepts every one of that section's five required
   distinctions and still comes in at 57 words, because d5 subsequently moved
   distinction five — fit standing — to the evaluator. If d3 §7 is still read as
   requiring length rather than requiring distinctions, this pass contradicts it,
   and the contradiction should be resolved in d3's favour or d3 should be
   annotated.
