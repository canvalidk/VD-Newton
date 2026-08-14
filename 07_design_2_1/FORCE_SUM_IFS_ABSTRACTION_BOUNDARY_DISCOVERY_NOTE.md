# HISTORICAL TERMINOLOGY QUARANTINE

> **This quarantine applies to names, not to the structural result.** The note
> is an active Design 2.1 source, but it preserves the vocabulary used during
> discovery. Translate every predecessor force-member name to
> `impressed-force`; none reopens the ratified terminology decision.

---

# From Set Membership to the Force-Sum Triplet

## A chronological discovery note for the VD Newton project

**Date:** 13 August 2026
**Status:** Working design-discovery record
**Scope:** Reconstruction of the discussion that exposed the aggregate/member-level bug in Design 2.1, separated force-occurrence identity from force-vector value, and produced a new candidate Force-Sum triplet:

> **Design 2.1 custody and terminology notice — 14 August 2026:** This full
> chronological note was transferred from
> `canvalidk/VD-docs@cae6cd109c1dfcae4f6c1f57c89c5b91660351b2:Newton/Design 3/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md`.
> VD-Newton now owns and maintains it as the positive structural correction to
> the aggregate/member bug. Provisional force-member names in the chronology
> are historical evidence only; in active entry work they translate to the
> sole ratified headword `impressed-force`.

$$
\boxed{
\text{net-force},
\qquad
V(f),
\qquad
\mathrm{IFS}
}
$$

Here `IFS` is used as the project's current placeholder for the target-indexed force set. Its final name is not settled by this note.

---

## 1. Why this note exists

The discussion began as a basic question about sets and ordering. It ended by changing the apparent structure of the Force-Sum law.

The decisive discoveries were not obtained by starting from the desired final equation and trying to decorate it with enough machinery. They were obtained by keeping every intermediate operation explicit:

```text
What collection exists?
What determines its members?
What kind of things are its members?
What value is extracted from each member?
What operation combines those values?
Which of these relations belong to one physical law?
```

The discussion repeatedly found that two things which had been treated as one were actually distinct:

```text
constructing a set
versus
operating over a set

a member predicate
versus
a constraint on the completed set

a force occurrence
versus
its force-vector value

the identity of an IFS member
versus
the mathematical value returned from it

the Force-Sum law
versus
the later law or structure that constructs the IFS
```

The final result is not yet a complete design of the IFS. It is a cleaner abstraction boundary within which that design can now be carried out.

---

# Part I — The set-theoretic route into the problem

## 2. Sets do not supply order

The first issue was whether a set can be folded by an order-dependent operation.

A bare set such as

$$
S=\{a,b,c\}
$$

does not contain a first, second, or third member. It records membership, not traversal order.

If a computation depends on order, the data must contain additional ordering structure, for example:

$$
(S,<)
$$

or an enumeration

$$
e:\{1,\ldots,n\}\to S.
$$

For order-insensitive aggregation, such as exact finite vector addition, a bare set can still be suitable because the result does not depend on the enumeration.

This gave the first useful separation:

```text
set identity and membership
are not
traversal order
```

---

## 3. Set construction and aggregation are different stages

The even-number example made the distinction concrete.

Start with a candidate set:

$$
N=\{1,2,3,4,5,6,7,8\}.
$$

Construct the even subset:

$$
E=\{x\in N\mid x\text{ is even}\}.
$$

Only afterwards aggregate its members:

$$
S=\sum_{x\in E}x.
$$

The complete route is:

$$
N
\longrightarrow
E=\{x\in N\mid P(x)\}
\longrightarrow
\sum_{x\in E}x.
$$

The variable $x$ in

$$
\sum_{x\in E}x
$$

does not construct $E$. By the time the summation ranges over $x\in E$, the membership of $E$ has already been settled.

This exposed a structural mistake in the earlier force-set thinking: the aggregation expression had been asked to help determine the collection it was supposed to consume.

---

## 4. A member predicate is not a whole-set constraint

A set-builder definition has the form

$$
E=\{x\in U\mid P(x)\}.
$$

Here:

- $U$ is the candidate universe;
- $x$ is one candidate member;
- $P(x)$ is a predicate on that individual candidate.

Its type is schematically:

$$
P:U\to\{\mathrm{true},\mathrm{false}\}.
$$

By contrast, the condition

$$
\sum_{x\in E}F(x)=R
$$

is a property of the completed collection $E$, not normally a property of an individual candidate $x$.

Its type is schematically:

$$
Q:\mathcal P(U)\to\{\mathrm{true},\mathrm{false}\}.
$$

So:

$$
P(x)
$$

and

$$
Q(E)
$$

operate at different logical levels.

If the aggregate condition is genuinely being used to select among candidate sets, the correct form is something like

$$
E\in
\left\{
A\subseteq U
\;\middle|\;
\sum_{x\in A}F(x)=R
\right\}.
$$

Now the candidate variable is the whole subset $A$, because the predicate concerns the whole subset.

---

## 5. Why the aggregate condition cannot uniquely construct the force set

Even when placed at the correct level, the condition

$$
\sum_{x\in E}F(x)=R
$$

usually fails to determine one unique set.

For a scalar example with $R=10$, all of the following may satisfy the same aggregate condition:

$$
\{10\},
\qquad
\{6,4\},
\qquad
\{20,-10\}.
$$

Therefore:

$$
\boxed{
\text{aggregate constraint}
\neq
\text{membership rule}
}
$$

and also:

$$
\boxed{
\text{aggregate constraint}
\not\Rightarrow
\text{unique collection}
}
$$

This became the Design 2.1 bug:

> The previous IFS entry partly characterized the set by saying that its members sum to net force. But “sums to net force” is a constraint on the set as a whole, not the individual-member condition that constructs its membership.

The correction required the Force-Sum law and the IFS-construction machinery to be separated.

---

# Part II — The literature detour and the identity problem

## 6. The historical clue: indexed force occurrences

A literature search found axiomatic treatments that distinguished force occurrences by indices rather than identifying them with their vector values.

The most important clue was the explicit recognition that two different force occurrences may return the same vector. If the collection were literally a set of vectors, then equal values would collapse:

$$
\{\mathbf v,\mathbf v\}=\{\mathbf v\}.
$$

One physical contribution would disappear from the sum.

This supplied a powerful design constraint:

$$
\boxed{
\text{an IFS member cannot simply be its force-vector value}
}
$$

More precisely, there must be room for:

$$
f_1\neq f_2
$$

while

$$
\operatorname{value}(f_1)
=
\operatorname{value}(f_2).
$$

The member identities remain distinct even when their mathematical outputs coincide.

---

## 7. Why ordered particle-pair notation was still insufficient

The indexed notation

$$
\mathbf F_{12}=-\mathbf F_{21}
$$

successfully distinguishes two force occurrences and relates their values.

But the discussion uncovered a deeper omission.

Suppose we also know a spring law:

$$
\mathbf F_{\mathrm{spring}}=-k\mathbf x.
$$

The two statements

$$
\mathbf F_{12}=-\mathbf F_{21}
$$

and

$$
\mathbf F_{\mathrm{spring}}=-k\mathbf x
$$

do not tell us whether

$$
\mathbf F_{\mathrm{spring}}=\mathbf F_{12}
$$

or

$$
\mathbf F_{\mathrm{spring}}=\mathbf F_{21}.
$$

Both assignments satisfy the equal-and-opposite relation.

Therefore, even after:

1. identifying the interaction pair;
2. knowing that the two force values are negatives;
3. knowing the spring-law output;

the forces on the two targets are still not assigned.

The missing datum is:

$$
\boxed{
\text{Which participant is the spring or constitutive acting object?}
}
$$

Once the spring object is identified, its constitutive state supplies the spring-law value. That value applies to the non-spring participant. The negative value applies back to the particular spring object whose constitutive information generated the action.

This exposed a real asymmetry between action and reaction forces:

```text
action force:
acting-object state
  -> constitutive law
  -> force value applied to the non-acting participant

reaction force:
already-constructed action force
  -> negation
  -> force value applied to the acting object
```

Thus action and reaction are not merely arbitrary names for $+\mathbf F$ and $-\mathbf F$. They have different construction histories and target restrictions.

This result remains important for the later excavation of IFS member structure. However, it is not yet part of the newly isolated Force-Sum law itself.

---

# Part III — The first agreed properties of an IFS member

## 8. Property 1: target

For a target particle $A$, every member of its IFS must have $A$ as target:

$$
f\in\mathrm{IFS}(A,t)
\quad\Rightarrow\quad
\operatorname{target}(f)=A.
$$

This is the first and least controversial membership property.

---

## 9. Property 2: temporal applicability

If the IFS is time-indexed, each member must be applicable or present at the relevant time:

$$
f\in\mathrm{IFS}(A,t)
\quad\Rightarrow\quad
\operatorname{active}(f,t).
$$

A possible force mechanism is not automatically a currently contributing force occurrence.

---

## 10. Property 3: a force-vector value

Each member must yield a vector in the force-vector value space:

$$
V(f)\in\mathbb V_F,
$$

where, in ordinary three-dimensional Newtonian mechanics,

$$
\mathbb V_F\cong\mathbb R^3
$$

with force units.

This is the value eventually supplied to vector addition.

---

## 11. Property 4: identity distinct from value

An IFS member must possess identity independently of the vector it returns.

Therefore:

$$
f_1\neq f_2
$$

is compatible with

$$
V(f_1)=V(f_2).
$$

This is essential. If two distinct $5\,\mathrm N$ contributions act on the same target, both must be counted:

$$
V(f_1)+V(f_2)=2V(f_1).
$$

A set of force values would erase that multiplicity. A set of identity-bearing force occurrences does not.

At this point, the discussion deliberately stopped short of declaring what the members fundamentally are. The only settled result was that they are not reducible to their force-vector outputs.

---

# Part IV — The unavoidable intermediate function

## 12. Why an evaluator is forced into existence

Once the IFS contains identity-bearing objects rather than vectors, its members cannot be added directly:

$$
f_1+f_2+f_3
$$

is not a vector operation.

An intermediate map is required:

$$
V:U\to\mathbb V_F,
$$

where:

- $U$ is the, as yet unspecified, type or universe of IFS members;
- $\mathbb V_F$ is the force-vector value space;
- $V(f)$ is the force-vector value returned from member $f$.

The net-force expression therefore becomes:

$$
\boxed{
\mathbf F_{\mathrm{net}}(A,t)
=
\sum_{f\in\mathrm{IFS}(A,t)}
V(f)
}
$$

This expression makes three stages visible:

```text
IFS members
  -> evaluate each member with V
  -> sum the returned force vectors
```

Computationally:

```text
for each member f in IFS(A,t):
    vector_value = V(f)
    accumulator = accumulator + vector_value
```

or functionally:

```text
fold (+) 0 (map V IFS)
```

The mathematical summation should be understood as indexed by the identity-bearing members.

---

## 13. Why we must not form an ordinary set of returned vectors

One might try to write an intermediate image set:

$$
\{V(f)\mid f\in\mathrm{IFS}(A,t)\}.
$$

But if:

$$
f_1\neq f_2
$$

and

$$
V(f_1)=V(f_2)=\mathbf v,
$$

then the image set becomes:

$$
\{\mathbf v,\mathbf v\}=\{\mathbf v\}.
$$

The multiplicity has been lost again.

So the design must not replace the IFS with an ordinary set of its returned values before aggregation.

Three safe alternatives are:

1. sum directly over the identity-bearing members:

   $$
   \sum_{f\in\mathrm{IFS}}V(f);
   $$

2. retain an indexed family:

   $$
   \bigl(V(f)\bigr)_{f\in\mathrm{IFS}};
   $$

3. retain identity–value pairs:

   $$
   \{(f,V(f))\mid f\in\mathrm{IFS}\}.
   $$

The direct indexed sum is the cleanest expression because it never discards the index that preserves multiplicity.

---

# Part V — The decisive abstraction insight

## 14. The member type can remain opaque inside Force-Sum

At first, introducing $V$ seemed to create another burden: perhaps the Force-Sum law would now have to define the nature of an IFS member before $V$ could be specified.

The decisive correction was to pay attention only to the required types.

Force-Sum needs:

$$
\mathrm{IFS}(A,t)\subseteq U
$$

for some member universe $U$,

and:

$$
V:U\to\mathbb V_F.
$$

It does **not** need to state what $U$ fundamentally contains.

Whatever IFS members later turn out to be, $V$ can be the operation that maps that type to force-vector values.

Thus Force-Sum can remain polymorphic or abstract over the member type:

$$
\boxed{
\mathrm{Set}(U)
\times
(U\to\mathbb V_F)
\longrightarrow
\mathbb V_F
}
$$

via:

$$
(S,V)
\longmapsto
\sum_{f\in S}V(f).
$$

The internal structure of $f$ is not part of the Force-Sum law. It is hidden behind the interface supplied by $V$.

This produces a strong abstraction boundary:

```text
later IFS-member theory
  may redesign what f is

provided that

V(f)
  still returns a force vector

therefore

the Force-Sum law remains unchanged
```

---

## 15. The Force-Sum law does not construct the IFS

The corrected relationship is:

```text
some later/upstream machinery constructs IFS(A,t)

Force-Sum consumes:
  IFS(A,t)
  V(f)

Force-Sum returns:
  net-force(A,t)
```

Therefore:

$$
\boxed{
\text{Force-Sum law}
\neq
\text{IFS-construction law}
}
$$

Force-Sum does not need to state:

- what an IFS member is;
- how candidate members are found;
- what membership predicate selects them;
- whether members are action or reaction force occurrences;
- which acting object supplies their constitutive information;
- how their identities are generated.

It needs only:

1. a set of members;
2. an evaluator returning a force vector from each member;
3. vector summation.

This is precisely the kind of separation that the earlier aggregate/member bug had demanded.

---

# Part VI — The triplet epiphany

## 16. The old apparent triplet

The earlier Design 2 Force-Sum structure was roughly:

$$
\text{net-force},
\qquad
\text{interacting-forces-set},
\qquad
\text{acting-force}.
$$

But `acting-force` was quietly being asked to do two incompatible jobs:

1. be the identity-bearing member of the set;
2. be the force vector that can be added.

That conflation made the IFS entry carry both membership and aggregation content.

---

## 17. The new candidate triplet

Once occurrence identity is separated from vector value, the three Force-Sum concepts become:

$$
\boxed{
\text{net-force}
\qquad
V(f)
\qquad
\mathrm{IFS}
}
$$

with the law:

$$
\boxed{
\mathbf F_{\mathrm{net}}(A,t)
=
\sum_{f\in\mathrm{IFS}(A,t)}
V(f)
}
$$

The key insight is that the variable $f$ does not have to be fully characterized inside this triplet.

The three corners have the following provisional inward-facing roles.

### 17.1 `net-force`

`net-force` is the force vector obtained by summing the values $V(f)$ indexed by the members $f$ of the IFS.

### 17.2 `IFS`

`IFS` is the set whose members index the evaluations $V(f)$ that are summed to yield net force.

### 17.3 `V(f)`

`V(f)` is the force-vector value returned from an IFS member $f$ for the summation that yields net force.

These are descriptions of roles inside the law, not final entry wording.

---

## 18. Why this is a genuine triplet rather than a pipeline of four concepts

The whole broader computation still contains more stages:

```text
candidate member universe
  -> membership selection
  -> IFS
  -> V(f)
  -> net-force
```

But the Force-Sum law itself does not include candidate generation or the membership predicate.

At the Force-Sum abstraction level, the inputs and output are only:

```text
one set: IFS
one member-to-vector evaluator: V
one aggregate vector: net-force
```

That is why the triplet survives.

The triplet restriction did not force the theory to omit necessary information. It forced the design to locate the correct abstraction boundary.

---

# Part VII — Six-entry implications

## 19. The triplet faces inward

The Force-Sum triplet should say only how:

$$
\mathrm{IFS},
\quad
V(f),
\quad
\mathbf F_{\mathrm{net}}
$$

relate to one another.

It should not define the internal anatomy of $f$.

This follows the VD distinction:

```text
triplet entries:
inward-facing law relations

walls/chimneys:
outward-facing definitions and links to surrounding theory
```

---

## 20. The IFS wall now has a clean job

The outward-facing IFS entry can take up the question:

$$
\boxed{
\text{What kinds of things are members of an IFS, and how is the set constructed?}
}
$$

That later analysis may involve:

- target;
- time or activation;
- occurrence identity;
- acting-object provenance;
- action/reaction provenance;
- partner occurrence;
- membership selection;
- set closure or termination.

None of that must be smuggled into the Force-Sum triplet.

---

## 21. The $V(f)$ wall now has a clean job

The outward-facing value entry can take up the question:

$$
\boxed{
\text{Given one IFS member, how does it yield a force vector?}
}
$$

That later structure may branch according to the member's nature.

For example, the action/reaction discovery suggests that some members may obtain their values through different construction routes:

```text
constitutive evaluation
versus
negation of a paired action value
```

But Force-Sum needs only the common interface:

$$
V(f)\in\mathbb V_F.
$$

---

## 22. Prospective overlap into deeper laws

The two winter walls may become chimneys into deeper structures:

```text
IFS wall
  -> IFS construction / membership law

V(f) wall
  -> force-occurrence evaluation / acting-object law
```

This is only a structural prospect. The exact downstream triplets have not yet been established.

---

# Part VIII — What is now confirmed

## 23. Confirmed results

The discussion supports the following conclusions.

### 23.1 The summation variable cannot construct its own domain

In:

$$
\sum_{f\in\mathrm{IFS}}(\cdots),
$$

the IFS must already exist.

### 23.2 “Sums to net force” is not an individual-member predicate

It is a constraint on the completed collection and therefore cannot, by itself, define which individual candidates are members.

### 23.3 The IFS cannot be a bare set of force-vector values

Distinct force occurrences may return equal vectors. A set of vectors would collapse them.

### 23.4 An IFS member and its force value are different objects

$$
f\neq V(f).
$$

### 23.5 A value-extraction operation is necessary

$$
V:U\to\mathbb V_F.
$$

### 23.6 Summation must remain indexed by member identity

$$
\mathbf F_{\mathrm{net}}
=
\sum_{f\in\mathrm{IFS}}V(f).
$$

### 23.7 Force-Sum need not determine the member type

It may remain abstract over $U$.

### 23.8 The candidate Force-Sum triplet is

$$
\boxed{
\text{net-force},
\quad
V(f),
\quad
\mathrm{IFS}
}
$$

### 23.9 IFS construction belongs outside this triplet

The Force-Sum law consumes an IFS; it does not construct one.

---

# Part IX — What remains open

## 24. The nature of an IFS member

The discussion has not yet settled whether an IFS member is fundamentally:

- an impressed-force occurrence;
- an attached-force occurrence;
- an acting-object output;
- an action-force or reaction-force instance;
- an interaction-side instance;
- another identity-bearing object not yet named.

The Force-Sum law no longer needs this answer immediately.

---

## 25. The exact signature of $V$

Several possibilities remain:

$$
V:U\to\mathbb V_F,
$$

$$
V_t:U\to\mathbb V_F,
$$

$$
V:U\times T\to\mathbb V_F,
$$

or a context-dependent evaluator whose target and time are already encoded by the member or supplied by the IFS evaluation context.

The triplet insight requires only that an IFS member can be evaluated to a force vector. It does not yet settle how contextual arguments are represented.

---

## 26. IFS membership and construction

The full membership rule remains to be excavated.

Currently agreed minimum properties include:

1. target $A$;
2. applicability at $t$;
3. a force-vector value through $V$;
4. identity distinct from that value.

Further candidate properties include acting-object provenance and action/reaction construction history, but these have not yet been installed as the definitive member type.

---

## 27. Action/reaction structure

The discussion strongly suggests:

- an action force obtains its value from the constitutive information of an acting object;
- it applies to the non-acting participant;
- the reaction obtains the negative value;
- it applies specifically to the acting object.

This may become central to IFS construction, because it determines which side of an interaction may enter which target's IFS.

However, its exact type representation remains open.

---

## 28. Final terminology

The following names remain provisional:

- `IFS`;
- `interacting-forces-set`;
- `impressed-forces-set`;
- `attached-force`;
- `impressed-force occurrence`;
- `force-value`;
- notation $V(f)$.

The structural distinctions should be preserved even if the vocabulary changes.

---

# Part X — The methodological result

## 29. The “hand on the wall” method

The discussion also demonstrated a repeatable design method.

Do not begin from the polished physics equation and assume the intermediate assignments are obvious.

Instead, keep contact with every dependency:

```text
What is the candidate object?
What establishes its identity?
What establishes membership?
What information does the member carry?
What operation extracts a usable value?
What collection is traversed?
What operation combines the values?
Which facts are local to one member?
Which facts concern the completed set?
Which relations are universal laws?
Which are supplied by a particular constitutive object?
```

A crack becomes visible whenever the formalism jumps over one of these questions.

This method exposed:

- the member/aggregate predicate mismatch;
- the occurrence/value conflation;
- the duplicate-vector collapse;
- the missing action/reaction assignment datum;
- the hidden member-to-vector evaluator;
- the correct abstraction boundary for the Force-Sum triplet.

---

# 30. Compact final picture

The full architecture currently visible is:

$$
\text{candidate force-occurrence universe }U
$$

$$
\downarrow\quad\text{later membership/construction machinery}
$$

$$
\mathrm{IFS}(A,t)\subseteq U
$$

$$
\downarrow\quad V(f)
$$

$$
\text{force-vector value for each identity-bearing member}
$$

$$
\downarrow\quad\sum_{f\in\mathrm{IFS}(A,t)}
$$

$$
\boxed{
\mathbf F_{\mathrm{net}}(A,t)
=
\sum_{f\in\mathrm{IFS}(A,t)}V(f)
}
$$

Inside the Force-Sum law, the member universe $U$ may remain opaque.

Therefore the new candidate law-house is centered on:

$$
\boxed{
\text{net-force}
\leftrightarrow
V(f)
\leftrightarrow
\mathrm{IFS}
}
$$

The IFS wall will later explain what the members are and how the set is constructed.

The $V(f)$ wall will later explain how an individual member yields a force vector.

That is the present epiphany.
