# Design 2.1 Bug Report — Aggregate Constraint Misused as a Member Constraint

## Status

**Confirmed structural bug**

## Summary

Design 2.1 implicitly treats a condition on the result of aggregating a set as though it could serve as the condition that determines membership in that set.

This is not generally valid.

A standard set-builder definition has the form

$$
E=\{x\in U\mid P(x)\},
$$

where:

- $U$ is the candidate universe,
- $x$ is one candidate member,
- $P(x)$ is a predicate evaluated on that individual candidate,
- $E$ is the set of candidates for which $P(x)$ is true.

The important restriction is that $P(x)$ is a **member-level condition**. It answers:

> Should this particular candidate $x$ be a member of $E$?

By contrast, a condition such as

$$
\sum_{x\in E}F(x)=R
$$

is not ordinarily a property of an individual member $x$. It is a property of the **set $E$ as a whole**.

Therefore, an aggregate condition cannot simply be inserted into the member predicate and expected to determine the members of the set.

---

## Minimal Example

Suppose

$$
N=\{1,2,3,4,5,6,7,8\}.
$$

We can define the even-number subset by

$$
E=\{x\in N\mid x\text{ is even}\}.
$$

Here,

$$
P(x):=x\text{ is even}
$$

can be evaluated independently for each candidate $x$.

Once $E$ exists, we may then define

$$
S=\sum_{x\in E}x.
$$

These are two logically distinct stages:

$$
N
\longrightarrow
E=\{x\in N\mid P(x)\}
\longrightarrow
S=\sum_{x\in E}x.
$$

The first stage determines **membership**.

The second stage performs an **aggregation over the already-determined members**.

By the time the expression

$$
\sum_{x\in E}
$$

is being evaluated, the question of which objects belong to $E$ has already been answered.

---

## The Design 2.1 Error

The mistaken architecture is approximately:

$$
E=\{x\in U\mid \text{the members of }E\text{ aggregate to }R\}.
$$

The apparent predicate refers to the result of aggregating the entire set rather than to a property of the candidate $x$.

The question

> Does this $x$ belong?

has been replaced by the different question

> Does this collection have the required aggregate?

Those questions operate at different logical levels.

A member predicate has the form

$$
P:U\to\{\text{true},\text{false}\}.
$$

An aggregate constraint instead has the form

$$
Q:\mathcal P(U)\to\{\text{true},\text{false}\},
$$

where $\mathcal P(U)$ is the power set of $U$.

Thus:

$$
P(x)
$$

is a predicate on a **candidate member**, whereas

$$
Q(E)
$$

is a predicate on a **candidate set**.

They are not interchangeable.

---

## Correct Representation of an Aggregate Constraint

If the defining information really is

$$
\sum_{x\in E}F(x)=R,
$$

then the natural candidate objects are not individual elements $x$, but subsets $A\subseteq U$.

One may write

$$
E\in
\left\{
A\subseteq U
\;\middle|\;
\sum_{x\in A}F(x)=R
\right\}.
$$

Now the predicate is correctly typed:

$$
Q(A):=
\left(
\sum_{x\in A}F(x)=R
\right).
$$

The predicate acts on the candidate set $A$, because the condition genuinely concerns the set as a whole.

---

## Important Consequence: Aggregate Constraints Usually Do Not Determine Membership Uniquely

Even after moving the constraint to the correct logical level, another problem appears.

Suppose the required aggregate is

$$
R=10.
$$

Several different sets may satisfy it:

$$
\{10\},
$$

$$
\{6,4\},
$$

$$
\{20,-10\},
$$

and so on.

Therefore,

$$
\sum_{x\in E}F(x)=R
$$

usually constrains the permissible sets without uniquely identifying one of them.

So an aggregate equation is generally not a replacement for a genuine membership rule.

Instead, a design may require two separate statements:

### 1. Membership definition

$$
E=\{x\in U\mid P(x)\}.
$$

This determines which candidates belong to the set.

### 2. Aggregate law or constraint

$$
\sum_{x\in E}F(x)=R.
$$

This states something that must be true of the resulting set.

These have different jobs.

---

## General Design Principle

A collection-processing design should distinguish at least three stages:

$$
\boxed{
\text{candidate universe}
\longrightarrow
\text{membership rule}
\longrightarrow
\text{constructed collection}
\longrightarrow
\text{aggregate operation}
}
$$

More explicitly:

$$
U
\longrightarrow
\{x\in U\mid P(x)\}
\longrightarrow
E
\longrightarrow
\operatorname{Aggregate}(E).
$$

A condition on $\operatorname{Aggregate}(E)$ should not be assumed to supply $P(x)$.

The key diagnostic question is:

> Can this condition be evaluated for one candidate $x$, without already knowing the other members of the set?

If **yes**, it may be a member predicate.

If **no**, and it requires the completed collection, then it is a collection-level constraint.

---

## Why This Matters for Entry Design

If an entry structure was designed under the assumption that the aggregation expression itself could determine which entries participate, then the structure may be missing an explicit representation of:

1. the candidate universe,
2. the membership predicate,
3. the identity/equality relation used for members,
4. the aggregation performed only after membership has been established.

This means the bug is upstream of the aggregation operation.

The aggregation variable

$$
x\in E
$$

does not create or identify $E$. It only ranges over members of a set whose membership must already be defined.

---

## Design 2.1 Correction

Do not use an aggregate condition as though it were an individual-member predicate.

Instead, determine which of the following is intended:

### Case A — The collection has an independent membership rule

Define

$$
E=\{x\in U\mid P(x)\},
$$

then separately impose or derive

$$
\operatorname{Aggregate}(E)=R.
$$

### Case B — Only the aggregate condition is known

Treat entire subsets as candidates:

$$
E\in
\{A\subseteq U\mid \operatorname{Aggregate}(A)=R\}.
$$

Then recognize that this may define a family of admissible sets rather than a unique set.

Additional constraints are required if exactly one collection is intended.

---

## Core Result

The central correction is:

$$
\boxed{
\text{A constraint on what the members collectively produce is not, in general, a constraint on whether an individual candidate is a member.}
}
$$

Equivalently,

$$
\boxed{
P(x)\neq Q(E)
}
$$

unless additional structure specifically allows the collection-level condition to be reduced to an individual-member condition.

This distinction must be respected before the entry structure or aggregation law can be designed reliably.
