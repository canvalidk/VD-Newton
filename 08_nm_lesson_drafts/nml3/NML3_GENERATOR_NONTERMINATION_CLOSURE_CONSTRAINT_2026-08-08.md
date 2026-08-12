# NML3 Generator Nontermination and Closure Constraint

Status: active local design constraint, recorded 2026-08-08. This note does not
select final entry wording.

## Observation

The positive force generator has the recursive structure

$$
R(N)=\{W_N\}\cup R(N+1),
$$

where \(R(N)\) is the not-yet-unfolded remainder of the force account and
\(W_N\) is the impressed-force member determined at step \(N\).

This successor form is endless by itself. After any generated member it asks
for another remainder. It has no internal case that says the current member is
the final force on the object. Iterating it a finite number of times therefore
establishes only positive membership facts:

$$
\{W_0,W_1,\ldots,W_n\}\subseteq\operatorname{IFS}(M).
$$

It does not establish the completeness claim

$$
\operatorname{IFS}(M)=\{W_0,W_1,\ldots,W_n\}.
$$

Knowing any number of forces is not the same as knowing that there are no more
forces.

## The missing terminal determination

A finite force account requires an additional base case, schematically:

$$
R(K)=\varnothing
$$

or, in evidential language,

```text
no further impressed-force member exists for this target and conditions
```

That is not another positive output of the generator. It is a negative or
exhaustiveness determination supplied by the closer. The closer is therefore
logically independent of however many force members the generator has already
found.

The empty IFS is the limiting case in which the closer supplies this base case
at the initial state, before any positive member is generated.

## Why a matching net force cannot terminate generation

Suppose the current account contains warranted spring and gravitational
members:

$$
\mathbf F_{\mathrm{net}}=-kx+mg.
$$

Determining those two interactions establishes that their keyed members belong
to the IFS. Even if their vector values already add to the measured net force,
it does not establish that they exhaust the IFS. There could still be an
additional warranted collection \(C\) such that

$$
C\neq\varnothing,
\qquad
\sum_{W\in C}\operatorname{vec}(W)=\mathbf 0.
$$

Then

$$
\mathbf F_{\mathrm{net}}
=-kx+mg+\sum_{W\in C}\operatorname{vec}(W)
=-kx+mg
$$

while the two-member account remains incomplete. The hidden collection may be
a cancelling pair or a larger cancelling collection. Agreement with the net
force is therefore insensitive to precisely the omitted members that sum to
zero.

The closer cannot use “the known forces already reproduce the net force” as
its stopping rule. Doing so would confuse algebraic residual-zero with
ontological exhaustion and would make completeness circular.

## Design consequence

NML3 fixes the following division of labour:

- The generator provides positive determination: this acting-object-keyed
  warranted force is a member.
- Repeated generator success provides a larger warranted subset, never by
  itself a complete set.
- The closer provides the terminal determination: no further warranted member
  remains.
- The terminal determination is the base case that makes the recursively
  generated account finite and closed.
- Neither the current member count nor equality between the current vector sum
  and the measured net force can supply that base case.
- The index \(N\) belongs to the generation trace; it does not impose an order
  on the completed mathematical set.

## Required evaluator contrast

```text
spring member warranted
gravity member warranted
current sum equals measured net force
no closer witness
    -> sound partial account; closure fails

spring member warranted
gravity member warranted
additional warranted cancelling collection not yet considered
    -> current account is incomplete despite the matching sum

all generated members warranted
independent no-further-member determination succeeds
    -> IFS may close and its complete vector sum may be taken
```

## Scope and provenance

Primary source: the 2026-08-08 observation that the recursive
`rest_of_the_forces_set(N)` generator contains only a successor step, so
positive determination of spring and gravity members does not determine a
final force or exclude further cancelling members.

This is local active/unsubmitted NML3 material. The resolved managed-context
snapshot `canvalidk/VD-docs@8e09dbf9d3e521cbe76e36426ead656c04a71650`
contains no NML3 or impressed-force material, and no managed VD-docs file was
edited.
