# Canonical-Force Orientation Convention

**Status:** working Design 2.1 discovery note
**Date:** 2026-08-14
**Scope:** canonical-force orientation, target-side impressed-force evaluation,
action/reaction pairing, and the human convention input exposed by the VD
six-entry structure

## Part I — The result

### 1. Statement of the convention

For one active binary interaction, the equal-and-opposite relation does not
determine which member of the force pair is to be quoted as the principal or
canonical force.

If the two target-side force values are $A$ and $R$, then

$$
A=-R
$$

is compatible with either assignment

$$
A=K,
\qquad
R=-K,
$$

or

$$
A=-K,
\qquad
R=K.
$$

Both assignments satisfy the same equal-and-opposite relation. The relation
therefore supplies opposition but not canonical orientation.

An additional convention is required:

> **Which member of the equal-and-opposite pair is selected as the canonical
> force that the model, calculation, entry, or lesson will quote directly?**

This is a real representational degree of freedom. It is not another physical
force and it is not determined by the equation $A=-R$.

### 2. Canonical recipient and impressed-force evaluation

Let $i$ be one active binary interaction with participant set

$$
P(i)=\{p_1,p_2\}.
$$

A convention $C$ supplies:

1. a canonical recipient

   $$
   c_C(i)\in P(i),
   $$

2. a canonical-force vector

   $$
   K_C(i).
   $$

For the target-side occurrence of interaction $i$ addressed to participant
$p$, the impressed-force value is

$$
V_C(i,p)
=
\begin{cases}
K_C(i),
&p=c_C(i),\\[4pt]
-K_C(i),
&p\in P(i)\setminus\{c_C(i)\},\\[4pt]
\text{undefined},
&p\notin P(i).
\end{cases}
$$

The final branch matters. A participant not belonging to the interaction does
not receive the negative force merely because it is not the canonical
recipient.

There is no need to introduce an independently named sign function such as
$\sigma(f)$. Such a function would only restate the result of the supplied
canonical orientation:

```text
canonical recipient  -> return K
paired participant   -> return -K
```

The convention is the input. The positive/negative branch is derived from it.

### 3. The opposite convention

An opposite convention \(\bar C\) may select the other participant as the
canonical recipient and quote the opposite vector as canonical:

$$
\{c_{\bar C}(i)\}
=
P(i)\setminus\{c_C(i)\},
$$

and

$$
K_{\bar C}(i)=-K_C(i).
$$

When the recipient and quoted canonical vector are both transformed
consistently, the target-side physical values do not change:

$$
V_{\bar C}(i,p)=V_C(i,p)
$$

for each participant $p\in P(i)$.

The convention changes which member and formula are treated as principal. It
does not change the physical pair represented by the complete account.

### 4. Hooke-law example

The familiar spring formula exposes the convention clearly.

One convention may quote the spring's force on an attached body as the
canonical force. Relative to the chosen displacement meaning, this may be
written

$$
F=-kx.
$$

The opposite convention may quote the attached body's force on the spring as
the canonical force. The corresponding quoted formula may be

$$
F=+kx.
$$

These expressions do not contradict one another when they name opposite
members of the same force pair. They are alternative conventions for which
force is principal in the representation.

They are not interchangeable while keeping the meanings of $F$, $x$, the
recipient, and the orientation unchanged. A valid convention reversal must
change the recipient assignment and the quoted canonical vector together.

### 5. What is physical and what is conventional

The physical or model-substantive structure includes:

```text
an active interaction exists;
the interaction has specified participants;
one target-side force occurrence belongs to each relevant target account;
the two evaluated values are equal and opposite under the Newtonian pair law;
the constitutive state and parameters determine the force scale and direction.
```

The conventional structure includes:

```text
which member is selected as the canonical or principal force;
which target is called the canonical recipient;
which of the two opposite formulas is quoted directly;
which member is then obtained by negating the quoted canonical value.
```

The convention must be explicit and applied consistently. It may be installed
by a modelling choice, a lesson convention, an entry authority, or another
human-supplied runtime record.

### 6. Separation from interaction discovery and system closure

Knowledge of the canonical-force value and its orientation convention is not
required to determine:

- whether an interaction exists;
- which objects participate in it;
- which target-side force occurrences exist;
- which occurrences belong to a target's force account;
- whether an interaction crosses a selected system boundary;
- or whether the interaction search is exhaustive.

For a selected system $S$, interaction closure is determined structurally.
If $P(i)$ is the participant set of active interaction $i$, then a strong
interaction-closure condition has the form

$$
P(i)\cap S\neq\varnothing
\Longrightarrow
P(i)\subseteq S.
$$

This condition uses system membership, interaction existence, participant
incidence, and exhaustiveness. It uses neither $K_C(i)$ nor $A=-R$.

Only after the interaction structure is known are the target-side occurrences
evaluated. The equality

$$
K_C(i)+(-K_C(i))=0
$$

then permits an internal pair to cancel in an aggregate system equation. That
cancellation is a consequence of an already-classified internal interaction;
it is not evidence that the interaction is internal and not a criterion of
system closure.

### 7. Entry-structure consequence

The Force-Sum law may consume identity-bearing force occurrences while
remaining abstract over their internal construction:

$$
\mathbf F_{\mathrm{net}}(M)
=
\sum_{f\in\operatorname{IFS}(M)}
V(f).
$$

On the present interpretation, $V(f)$ is the target-side
`impressed-force` value.

The candidate Force-Sum triplet is therefore:

$$
\boxed{
\text{net-force},
\qquad
\operatorname{IFS},
\qquad
\text{impressed-force }V(f)
}
$$

The outward wall of `impressed-force` may then become the chimney into a deeper
evaluation law whose provisional conceptual corners are:

$$
\boxed{
\text{impressed-force }V(f),
\qquad
\text{canonical-force-acting-object},
\qquad
\text{canonical-force orientation convention}
}
$$

The third phrase is a statement of function, not settled entry wording.
Possible vocabulary includes:

- canonical-force orientation;
- canonical recipient;
- force-delivery orientation;
- interface-direction rule;
- canonical-force application convention.

The eventual headword must expose the runtime human choice without suggesting
that the convention is an additional physical force.

### 8. Action and reaction after the correction

Action and reaction need not be stored as two independently valued forces plus
a third stored equation saying that they are negatives.

Instead, the network may store:

```text
one interaction identity;
its participant incidences;
one canonical-force value;
one canonical orientation convention;
and the target address of the occurrence being evaluated.
```

The evaluator returns the canonical value to the canonical recipient and its
negative to the paired participant. The relation $A=-R$ is then an invariant
of the evaluation network rather than duplicated data.

This does not remove all action/reaction content. A separate structural law may
still be needed to establish:

- that the counterpart occurrence exists;
- that the two occurrences belong to one interaction;
- that they address the appropriate distinct participants;
- and that the participant domain is suitable for a binary Newtonian pair.

What is removed is the need to store the reaction vector independently after
the canonical vector and orientation have already fixed it.

### 9. Tests of the result

A successful design should pass at least these tests.

#### Convention reversal

Reverse the canonical recipient and negate the quoted canonical formula. Every
target-side impressed-force value must remain unchanged.

#### Equal-and-opposite underdetermination

Supply only $A=-R$. The evaluator must refuse to determine which member is
canonical until an orientation convention is supplied.

#### Interaction-before-value

Construct the interaction incidences and determine system closure while all
canonical-force values remain unknown.

#### External cancellation

Two equal-and-opposite external interactions may sum to zero without making the
selected system interaction-closed.

#### Invalid target

Attempt to evaluate the interaction for a nonparticipant. The result must be
undefined or inapplicable, not the negative branch.

#### Spring convention pair

Represent the same spring interaction once with the body-side force as
canonical and once with the spring-side force as canonical. The quoted Hooke
formula should change sign while the complete physical pair remains invariant.

### 10. Open questions

1. What is the final VD headword for the canonical-orientation convention?
2. Is the convention supplied per acting-object instance, per acting-object
   type, per model, per lesson, or through a wider authority record?
3. Does the convention choose only the canonical recipient, or does it package
   recipient, displacement orientation, and quoted constitutive formula
   together?
4. How should symmetric mechanisms such as gravity represent canonical
   orientation when neither participant is a privileged constitutive carrier?
5. How does the construction generalise beyond binary interactions?
6. Should `action` and `reaction` remain entry headwords, derived labels, or
   teacher-facing vocabulary?
7. What empirical or ontological content remains for Newton III once the
   equal-and-opposite value relation is implemented by the evaluator?
8. How should a trace display convention provenance so that two opposite but
   equivalent representations can be compared automatically?

---

## Part II — How the convention was found

### 11. The aggregate/member correction

The route began with the confirmed Design 2.1 error recorded in
`DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md`.

The error was to allow a constraint on a completed aggregate to do the work of
an individual membership predicate. The correction separated:

```text
candidate universe
-> member identity and membership
-> completed collection
-> value extraction
-> aggregation.
```

For Force-Sum, this meant that the summation expression could not construct its
own IFS.

### 12. Force occurrence was separated from vector value

The next step was to recognise that an IFS cannot be a bare set of vectors.
Two distinct physical force occurrences may have equal vector values. A value
set would collapse them:

$$
\{\mathbf v,\mathbf v\}=\{\mathbf v\}.
$$

Therefore the IFS must preserve identity-bearing occurrences $f$, while an
evaluator supplies their vector values:

$$
V(f)\in\mathbb V_F.
$$

Force-Sum then became

$$
\mathbf F_{\mathrm{net}}
=
\sum_{f\in\operatorname{IFS}}V(f).
$$

This established the abstraction boundary: Force-Sum consumes an IFS and an
evaluator but does not need to know what the member type fundamentally is.

### 13. Action/reaction information moved behind the evaluator wall

Once $V(f)$ had an outward wall, the action/reaction relation could be placed
behind that wall rather than repeated in Force-Sum, IFS construction, or system
closure.

A first evaluator description was:

```text
if f is the action force:
    return the canonical force
otherwise, if f is its reaction counterpart:
    return the negative canonical force
```

This showed that $A=-R$ could be produced by the evaluation network. It did
not have to be stored independently elsewhere.

It also revealed that interaction discovery and system closure never needed
the equal-and-opposite value relation. Those tasks use the interaction network,
not its vector valuation.

### 14. The rejected sign-function placeholder

The branch was temporarily represented by a sign function:

$$
V(f)=\sigma(f)K.
$$

with $\sigma(f)=+1$ for action and $\sigma(f)=-1$ for reaction.

That representation was mathematically serviceable but structurally
unsatisfactory. A fixed piecewise function is not an independently supplied
runtime object. Giving it a separate conceptual wall would merely name an
implementation detail.

The VD working principle applied at this point was:

> **Every wall exposes an input.**

If the apparent third corner had a wall, it had to correspond to a genuine
runtime degree of freedom supplied by a human or modelling authority. The
fixed sign function did not provide one.

### 15. The two-way assignment

Removing the sign-function placeholder forced direct inspection of the
equal-and-opposite pair.

Given only a canonical vector $K$ and the relation $A=-R$, both of these
remain possible:

$$
(A,R)=(K,-K)
$$

and

$$
(A,R)=(-K,K).
$$

The convention that selected the first assignment had been treated as
obvious. It was not a consequence of the pair law.

The missing input was therefore identified as the convention specifying which
participant receives the canonical vector. The sign branch is downstream of
that input and requires no independent name.

### 16. The Hooke-law recognition

The abstract freedom became unmistakable in the spring case.

The familiar formula

$$
F=-kx
$$

quotes one target-side member of the spring interaction under a particular
recipient and displacement convention. An equally coherent presentation may
quote the opposite member as principal and write

$$
F=+kx.
$$

The two presentations describe the same complete force pair when their
referents and orientation conventions are transformed together.

This supplied the concrete interpretation of the wall input: a lesson,
calculation, or model must choose which member of the pair will be treated as
the principal force whose formula is quoted directly.

### 17. What the VD predicted

The VD did not predict a new experimental force or a new empirical law. It made
a structural prediction:

```text
the proposed law-house appears to require another wall
-> every wall must expose a genuine runtime input
-> a fixed sign function is not such an input
-> therefore an unrepresented degree of freedom must be present
-> the force-pair equations admit two canonical assignments
-> the missing input is the canonical-orientation convention.
```

The convention was found because the entry architecture refused to let
"obviously use this sign" pass as an unexplained step.

This is significant evidence for the design method. The structural demand for
an input arose before the physical meaning of that input had been identified.
Inspection of the mechanics then produced a clear, binary, convention-level
degree of freedom that occupied the demanded place.

### 18. Relationship to current sources

This note is the local Design 2.1 entry-facing interpretation of material read
from the coherent managed snapshot `canvalidk/VD-docs@cae6cd109c1dfcae4f6c1f57c89c5b91660351b2`, especially:

- `Newton/Design 3/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md`;
- `Newton/nml/nml3/NML3_OPEN_PROBLEM_IMPRESSED_FORCE_IDENTITY_ACTION_REACTION_EXCLUSIVITY.md`;
- `Newton-analysis/action_reaction_asymmetry/ACTION_REACTION_CONSTITUTIVE_ASYMMETRY_SKETCH_d1.md`;
- `Newton/nml/nml3/NML3_PRIMITIVE_EXERCISE_BANK_FORCE_ACCOUNTING.md`;
- `Newton/nml/nml3/NML3_FORCE_SUM_VOCABULARY_RESERVOIR.md`.

The decisive canonical-orientation result was articulated in the subsequent
Design 2.1 discussion on 2026-08-14. This document records that result locally
without editing or assuming custody of the NML documents.

## Compact conclusion

The equal-and-opposite force relation does not determine which member of the
pair is canonical. A human or modelling authority must supply a convention
selecting the canonical recipient and the corresponding quoted force formula.

Once supplied, the impressed-force evaluator returns the canonical vector for
that recipient and its negative for the paired participant. Reversing the
recipient and quoted vector together leaves the complete physical account
unchanged.

The convention is therefore a genuine runtime input exposed by the
`impressed-force` wall. The VD entry structure detected the missing input by
requiring a real degree of freedom where a fixed sign function had been
mistaken for sufficient explanation.
