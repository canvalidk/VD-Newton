# NML3 Force-Sum Foundational Understanding — 2026-08-02

Status: current conceptual starting note for NML3. This note identifies the
problem the lesson and entries must solve. Its previously open naming question
was resolved by `NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`.

`impressed-force` is the ratified force-member headword.

## Goal

NML3 must establish how a material object's force account produces the
identity

```text
F_net = F_1 + F_2 + ...
```

The entries must support a trace that constructs the right-hand side as the
relevant forces are found, and then identifies its vector sum with the
`net-force-material-object` already available from Newton II.

This is not merely a lesson about performing vector addition. It must establish
which forces are permitted to appear in the addition and how the addition is
formed as a complete force account.

## Hurdles

### 1. Initiating a binary addition

Vector addition is a binary operation. The first discovered force therefore
needs an initiator: operationally, it is added to the zero vector. The trace
must accommodate that beginning without mistaking the zero vector for a
impressed force.

### 2. Beginning and ending with impressed forces

For a nonempty account, the exposed force identity should have contributing
forces at both ends:

```text
F_1 + F_2 + F_3
```

It should not expose an initial zero as though it were a force, or leave a
termination signal as though it were another term in the sum.

### 3. Preventing duplicate contributions

The same impressed force must not be admitted twice. A construction such as

```text
F_1 + F_1 + F_2
```

must be unavailable when both occurrences of `F_1` name the same force. This is
the most difficult hurdle because the entries need some basis for recognising
that a proposed term has already appeared.

The problem concerns duplicate force identity, not merely equal vector values:
two distinct forces may have equal vectors without being duplicates.

### 4. Producing the zero vector for an empty account

When there are no impressed forces, the completed force account must still
produce a result:

```text
F_net = 0
```

The empty case must therefore be a successful force-sum outcome, not a failure
to start the procedure.

### 5. Proceeding without knowing the number in advance

The trace cannot require the modeller to know beforehand how many contributing
forces exist. It must remain usable while forces are being discovered, so that
the next action is clear after each discovery and the account can eventually be
declared complete.

## Critical insight: decomposition is not force membership

A net-force vector admits indefinitely many algebraically valid vector
decompositions. For example:

```text
F_net = A + B
      = C + D + E
      = (1/2)F_net + (1/2)F_net
```

The existence of any such decomposition does not establish that its summands
are impressed forces. Algebra alone cannot turn `A`, `B`, or either
half-vector into members of a material object's force account.

The direction of dependence must therefore remain one-way:

```text
established force-account members
    -> vector addition
    -> net force

arbitrary decomposition of net force
    -/-> force-account members
```

NML3 must teach the difference between enumerating forces and decomposing a
vector. The right-hand side of the force-sum identity is licensed by the force
account, not by the mere fact that its vectors add to the desired result.

This distinction is why the predecessor name `contributing-force` was rejected:
it could suggest that appearing as a summand grants force status. The ratified
name `impressed-force` instead identifies the prior action upon the target body.
The entries must still make explicit what warrants that impressed action and
establishes its membership independently of the sum.
