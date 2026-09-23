# HISTORICAL TERMINOLOGY QUARANTINE

> **Do not use this file as naming authority.** It preserves an earlier state and may use obsolete force-member names. The sole active headword is `impressed-force`, governed by `08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`. Translate any predecessor force-member name to `impressed-force` before carrying content forward. Historical wording does not reopen the decision.

---
# NML3 Force-Sum Foundational Understanding — 2026-08-02

Status: current conceptual starting note for NML3. This note identifies the
problem the lesson and entries must solve; it does not yet select the detailed
mechanism or final force-member headword.

`contributing-force` is used below as a provisional working term.

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
contributing force.

### 2. Beginning and ending with contributing forces

For a nonempty account, the exposed force identity should have contributing
forces at both ends:

```text
F_1 + F_2 + F_3
```

It should not expose an initial zero as though it were a force, or leave a
termination signal as though it were another term in the sum.

### 3. Preventing duplicate contributions

The same contributing force must not be admitted twice. A construction such as

```text
F_1 + F_1 + F_2
```

must be unavailable when both occurrences of `F_1` name the same force. This is
the most difficult hurdle because the entries need some basis for recognising
that a proposed term has already appeared.

The problem concerns duplicate force identity, not merely equal vector values:
two distinct forces may have equal vectors without being duplicates.

### 4. Producing the zero vector for an empty account

When there are no contributing forces, the completed force account must still
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
are contributing forces. Algebra alone cannot turn `A`, `B`, or either
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

This distinction also reopens the force-member name. `contributing-force` may
suggest that appearing as a summand is enough to grant force status. The final
headword should be chosen only after the entries make clear what establishes
membership independently of the sum.
