# NML3 Logical Consequences: Consolidated Statement

Status: active local consolidation, recorded 2026-08-08. This note deliberately
repeats material from the other NML3 notes so that the consequences can be read
in one place. It does not select final entry wording.

## Accepted premises

The consequences below start from these presently accepted NML3 premises.

1. For one material object under fixed time, state, and physical conditions,
   there is one correct interacting-forces-set (IFS).
2. An IFS member must be warranted independently of whether its vector value
   helps reproduce the measured net force.
3. Each impressed-force member is keyed by exactly one acting-object instance.
4. The material object owns or is the target of the IFS. It is not the member
   key.
5. The IFS is a set: member order and repeated presentation do not alter its
   membership.
6. The net force is the vector sum of all and only the members of the complete
   IFS.
7. The generator positively determines members through a successor structure,
   schematically

   $$
   R(N)=\{W_N\}\cup R(N+1).
   $$

8. The closer separately determines that no further warranted member remains,
   supplying a terminal case such as

   $$
   R(K)=\varnothing.
   $$

## Direct consequences

### 1. One acting-object-instance key can occur only once

For a fixed IFS,

$$
\operatorname{key}(W_i)=\operatorname{key}(W_j)
\Longrightarrow W_i=W_j.
$$

Rediscovering the same acting-object instance cannot add a second member or a
second copy of its vector value.

### 2. Action and reaction are exclusive roles for one key in one IFS

The same acting-object instance cannot enter one fixed IFS once as an action
force and again as a reaction force. Changing the force-role label does not
create a new set key.

### 3. The material object cannot serve as the member key

One material object may have several forces acting on it from several
acting-object instances. If the material object were the key, all those
legitimate members would collapse into one. The material object therefore
qualifies the force account as owner or target but does not identify its
members.

### 4. IFS cardinality is acting-object-key cardinality

Within one fixed context,

$$
|\operatorname{IFS}(M)|
=
|\{\operatorname{key}(W):W\in\operatorname{IFS}(M)\}|.
$$

The force count is not determined by the number of material objects, written
terms, distinct vector values, or named force-law types.

### 5. Equal vector values do not imply equal force members

Two different acting-object-instance keys may carry the same vector value:

$$
W_i\neq W_j
\quad\text{while}\quad
\operatorname{vec}(W_i)=\operatorname{vec}(W_j).
$$

Both remain members. Force identity is not vector-value identity.

### 6. Vector cancellation does not erase force membership

If

$$
W_i,W_j\in\operatorname{IFS}(M)
\quad\text{and}\quad
\operatorname{vec}(W_i)+\operatorname{vec}(W_j)=\mathbf 0,
$$

the two members do not disappear from the IFS. Cancellation occurs only after
members have been mapped to vector values. Algebraic simplification cannot be
applied backward to delete physical interaction members.

### 7. Zero net force does not determine an empty IFS

An empty, successfully closed IFS has the zero vector as its empty sum, but a
nonempty IFS may also sum to zero. Therefore

$$
\operatorname{IFS}(M)=\varnothing
\Longrightarrow
\mathbf F_{\mathrm{net}}(M)=\mathbf 0,
$$

while

$$
\mathbf F_{\mathrm{net}}(M)=\mathbf 0
\not\Longrightarrow
\operatorname{IFS}(M)=\varnothing.
$$

### 8. The force-account-to-resultant map is many-to-one

Different warranted force accounts can have the same vector resultant.
Consequently, equality of net forces across two objects, times, or models does
not imply equality of their IFSs, member counts, acting-object keys, sources, or
action/reaction roles. The net-force vector cannot be inverted to recover the
interaction account.

### 9. Repeated positive generation never establishes completeness

After any finite number of successful generator steps, the justified claim is

$$
\{W_0,\ldots,W_n\}\subseteq\operatorname{IFS}(M),
$$

not

$$
\{W_0,\ldots,W_n\}=\operatorname{IFS}(M).
$$

Knowing any number of warranted forces does not determine that the latest one
is the final force on the object.

### 10. Generation and closure have different logical forms

The generator supplies positive or existential determinations: an eligible
acting-object instance keys a warranted member. The closer must establish the
universal negative that no eligible, not-yet-admitted acting-object instance
remains. Repeating existential witnesses does not entail universal exhaustion.

Schematically, generation can establish

$$
\exists A\;\operatorname{eligible}(A),
$$

whereas closure requires

$$
\neg\exists A\;
\big(
\operatorname{eligible}(A)
\land
A\notin\operatorname{keys}(S)
\big).
$$

### 11. There is no intrinsic final force in the completed set

A set is unordered. “Final force” means the last member discovered in one
generation trace before the closer succeeds; it is not an intrinsic final
element of the IFS. Different generation orders may produce the same completed
set and the same net force.

### 12. Duplicate-freedom and completeness are independent

A partial account may contain only warranted members and no repeated keys while
still omitting other warranted members. The evaluator therefore requires at
least two independent judgments:

- member validity and key uniqueness; and
- account completeness.

Passing the first does not pass the second.

### 13. Failure to discover a member is not an empty-set determination

A generator that has produced no member may have encountered a genuinely empty
IFS, an incomplete search, or a failed warranting procedure. Only a successful
closer at the initial state determines the empty IFS.

### 14. A matching current sum does not establish closure

Suppose warranted spring and gravity members give

$$
\mathbf F_{\mathrm{net}}=-kx+mg.
$$

There may still be a nonempty warranted collection \(C\) for which

$$
\sum_{W\in C}\operatorname{vec}(W)=\mathbf 0.
$$

The omitted members may be a cancelling pair or a larger cancelling
collection. Their omission is invisible to the current resultant. Equality
between the current sum and the measured net force therefore cannot serve as a
closer witness.

### 15. Residual testing is asymmetric

For a warranted partial account \(S\), define

$$
\mathbf r
=
\mathbf F_{\mathrm{net}}
-
\sum_{W\in S}\operatorname{vec}(W).
$$

Assuming the net-force measurement and member vector values are correct:

- \(\mathbf r\neq\mathbf 0\) shows that \(S\) cannot be the complete IFS.
- \(\mathbf r=\mathbf 0\) does not show that \(S\) is complete, because omitted
  members may have zero resultant.

Residual disagreement can defeat closure; residual agreement cannot establish
it.

### 16. Closing the IFS requires exhausting the acting-object candidate domain

If the generator obtains force members from
`mechanical-composition_point-particle`, the closer must establish that no
unconsidered acting-object instance remains capable of keying another warranted
member. An open, partial, or merely searched mechanical composition cannot by
itself support a closed IFS.

### 17. Search failure is not proof of absence

The closer needs either an exhaustively bounded acting-object candidate domain
or a general exclusion argument that rules out all remaining candidates.
Merely asking for another candidate and receiving none does not establish that
none exists unless the search operation itself is warranted as exhaustive.

### 18. Correct closure is unique within a fixed context

Two proposed closed IFSs for the same material object, time, state, and physical
conditions cannot both be correct if they disagree about an acting-object key.
At least one membership warrant or closer judgment must be wrong, or the
supposedly identical contexts must differ.

Likewise, if a new warranted member is discovered after purported closure,
either the previous closer was invalid or the target conditions have changed.
It is not a harmless extension of a correctly closed account under unchanged
conditions.

### 19. The account is context-indexed

Set uniqueness and closure apply to one fixed target and fixed conditions. The
same acting-object instance may participate in force accounts at another time,
state, or target without duplicating a member of the original IFS, because the
contexts identify different force accounts.

### 20. Action-reaction pairing must respect the IFS key constraint

Because one acting-object instance cannot occupy both roles in one IFS, a later
action-reaction pair must be represented either across different target IFSs or
through distinct acting-object instances. The later action-reaction block must
decide the representation; it cannot add the opposite role as a second member
under an already-present key in the same IFS.

### 21. A scalar or component equation is weaker than a full vector account

Agreement in one measured component cannot establish closure of the full IFS.
Additional warranted forces may have zero projection on the selected axis, or
their projections may cancel. Coordinate projection can hide members
numerically without changing their force identities.

### 22. An account/resultant mismatch cannot be repaired algebraically

If an independently warranted and independently closed IFS does not sum to the
independently measured net force, at least one substantive element is wrong or
mis-scoped: a measurement, member warrant, force value, closer judgment, or
context assumption. An invented residual force cannot be admitted merely to
make the equation balance.

## Conditional architectural consequence

### 23. Finite termination commits the architecture to finite force accounts

If every valid trace must reach a finite index \(K\) satisfying

$$
R(K)=\varnothing,
$$

then every IFS handled by that architecture is finite. If an infinite IFS is to
be permitted, the present finite generator/closer structure is insufficient.
The theory would additionally need to specify infinite summation, convergence,
and whether the resultant is independent of enumeration order.

NML3 must therefore either accept finite IFSs in its intended domain or add
machinery for infinite accounts. The present notes have not yet selected the
second option.

## Compact evaluator summary

~~~text
warranted member + unique acting-object key
    -> sound member

sound members + no duplicates
    -> sound partial account
    -/-> complete IFS

current vector sum = measured net force
    -> algebraic agreement
    -/-> complete IFS

independent no-further-member determination
    -> closure witness

sound partial account + closure witness
    -> complete IFS

complete IFS
    -> sum all member vectors
    -> net force
~~~

## Scope and provenance

This consolidation restates consequences developed in the local NML3 notes and
the 2026-08-08 discussion. It distinguishes direct consequences from the
conditional finiteness consequence but deliberately preserves repetition for
clarity.

Local source notes:

- `NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02.md`;
- `NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md`;
- `NML3_ACTING_OBJECT_FORCE_ROLE_SET_CONSTRAINT_2026-08-08.md`;
- `NML3_GENERATOR_NONTERMINATION_CLOSURE_CONSTRAINT_2026-08-08.md`;
- `NML3_ENTRY_WORKING_PLAN.md`; and
- `nm_l3_lesson_draft.md`.

This is local active/unsubmitted NML3 material. The resolved managed-context
snapshot `canvalidk/VD-docs@8e09dbf9d3e521cbe76e36426ead656c04a71650`
contains no NML3 or impressed-force material, and no managed VD-docs file was
edited.
