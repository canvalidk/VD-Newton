# Why Force-Sum Must Relate the Interaction Set and Impressed Force

**Status:** active local entry-facing discovery note, 2026-08-18.

**Scope:** the semantic and evaluator requirement exposed by the NML3
entry-structure reset. The final triplet names were subsequently selected by
[`NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`](../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md);
this note still does not select final entry wording or E-numbers.

**Notation translation:** this historical filename and parts of the derivation
use `IFS` and `V(f)`. In current entry-facing language, the indexed domain is
`interaction-set`, its member variable is an interaction `i`, and `V(i)` is the
target-directed `impressed-force(i -> target)`.

## 0. Result

Force-Sum must preserve a three-corner relation among:

1. the target's net force;
2. the target's closed `interaction-set`; and
3. the target-directed `impressed-force` supplied by each member interaction.

The relation is:

$$
\boxed{
\mathbf F_{\mathrm{net}}(M\mid C)
=
\sum_{i\in\operatorname{interaction\text{-}set}(M\mid C)}
\mathbf F_{\mathrm{impressed}}(i\to M\mid C)
}
$$

provided that the interaction set is independently certified complete for target $M$ and
accounting context $C$.

This equation is not only a forward algorithm which consumes already-known
force laws. It is a constraint relation. When membership is closed, net force
and the known values of the other members can determine an otherwise unknown
`V(f)`. Repeating that determination over controlled contexts can supply the
observations from which a previously unknown force kernel is discovered.

Therefore `V(f)` cannot receive its first theoretical meaning only in a later
force-kind or acting-object triplet. Those later entries may provide an
independent constitutive equation for the same `V(f)`, but the individual
member-value variable and its resultant relation must already exist in
Force-Sum.

The compact reason is:

> A force member can be known to exist before its force expression is known.
> Closing the IFS fixes which member-value variables exist. Force-Sum can then
> determine an unknown member value from the amount of independently known net
> force left after every other member value has been accounted for.

The closure result is what licenses the ordinary-language word **the** in
"the amount remaining for this member." Without independent closure, the
remainder belongs only to this member **plus whatever members have not yet
been found**.

---

## 1. Four distinctions the implementation must preserve

### 1.1 Member existence is not member value

It may be established that a magnetic interaction contributes one
impressed-force member $f_B$ to a target's account while the magnetic force law
is still unknown:

$$
f_B\in\operatorname{IFS}(M\mid C),
$$

but

$$
V_C(f_B)=\;?
$$

The first statement concerns which physical force occurrence exists. The
second concerns the vector value of that occurrence in the stated context.
Neither statement is a substitute for the other.

In particular, distinct force occurrences may have the same value:

$$
f_1\neq f_2
\qquad\text{while}\qquad
V_C(f_1)=V_C(f_2)=\mathbf c.
$$

This includes the simple case of two independently warranted constant forces.
The member set correctly contains both $f_1$ and $f_2$, so both contributions
must be counted. Its ordinary value-image does not:

$$
\{V_C(f_1),V_C(f_2)\}=\{\mathbf c\}.
$$

Summing that value-set gives $\mathbf c$, not $2\mathbf c$. A list or multiset
can preserve multiplicity, but an unkeyed one no longer says which value
belongs to which admitted member. Keying each value by $f$ repairs both
problems and reinstates the map $f\mapsto V_C(f)$.

### 1.2 Membership closure is not value completion

An IFS is **membership-closed** when it contains all and only the impressed
forces acting on its target in the fixed context:

$$
\operatorname{ClosedIFS}(S;M,C)
\iff
\forall f\,
\bigl(
\operatorname{ImpressedForce}(f;M,C)
\leftrightarrow
f\in S
\bigr).
$$

This does not require every $V_C(f)$ to be known. Thus the following state is
coherent:

```text
membership:
    closed

members:
    f_spring
    f_gravity
    f_magnetic

values:
    V(f_spring)   known
    V(f_gravity)  known
    V(f_magnetic) unknown
```

The old Design 2.1 E17 closer was attempting to produce the first status, not
the second. Its historical bare `no-more-acting-objects` signal is too weak;
the required semantic output is an exhaustion or general-exclusion
certificate. Its structural role nevertheless remains important.

### 1.3 A particular force value is not a force kernel

One closed account at one context can determine one vector value:

$$
V_C(f_B)=\mathbf r_C.
$$

It does not by itself determine a general magnetic law. A kernel is a stable
relation over a family of admissible contexts:

$$
K_B:\ C\longmapsto V_C(f_{B,C}).
$$

Kernel discovery therefore requires repeated determinations, controlled
variation, known inputs, a suitable hypothesis class, and enough independent
excitation to distinguish candidate laws.

### 1.4 Closing by exhaustion is not closing by agreement

Numerical agreement with net force does not prove that an account is closed:

$$
\sum_{f\in S}V_C(f)=\mathbf F_{\mathrm{net}}(M\mid C)
\not\Longrightarrow
\operatorname{ClosedIFS}(S;M,C).
$$

Omitted forces may cancel. Closure must be established independently of the
resultant it later licenses.

---

## 2. The inverse Force-Sum theorem

Let $S$ be a finite membership-closed IFS for $(M,C)$ and let $f_*\in S$.
Assume:

1. $\mathbf F_{\mathrm{net}}(M\mid C)$ is independently known as a full force
   vector in the same frame and context;
2. $V_C(g)$ is known for every $g\in S\setminus\{f_*\}$;
3. vector addition is cancellative;
4. $f_*$ is the only member whose value remains unknown; and
5. the member value is determinate in the fixed context rather than
   stochastic or set-valued.

Force-Sum gives:

$$
\mathbf F_{\mathrm{net}}(M\mid C)
=
V_C(f_*)
+
\sum_{g\in S\setminus\{f_*\}}V_C(g).
$$

Therefore:

$$
\boxed{
V_C(f_*)
=
\mathbf F_{\mathrm{net}}(M\mid C)
-
\sum_{g\in S\setminus\{f_*\}}V_C(g)
}
$$

The right-hand side is the amount of net force remaining after every other
member of the otherwise value-complete, membership-closed account has been
paid.

This theorem does **not** infer that $f_*$ exists from an algebraic residual.
Its membership is a premise established independently through the relevant
interaction and activation machinery. Force-Sum determines the value of an
already admitted member.

If $S$ is not closed, the same subtraction yields only:

$$
\mathbf r
=
V_C(f_*)
+
\sum_{h\in\text{unseen members}}V_C(h),
$$

so $V_C(f_*)$ is not isolated. If several admitted members have unknown
values, Force-Sum determines at most their sum unless further independent
equations are supplied.

---

## 3. Magnetic-kernel discovery as the decisive test

Consider a charged target particle $M$ in a context $C$. Suppose independent
interaction evidence and the relevant activation machinery establish a
magnetic member $f_{B,C}$. Suppose the membership account is independently
closed:

$$
S_C
=
K_C\cup\{f_{B,C}\},
$$

where the values of every member in $K_C$ are known and the value of
$f_{B,C}$ is not.

The target's motion supplies an independent net-force route through Newton II:

$$
\mathbf F_{\mathrm{net}}(M\mid C)
=
m_M\mathbf a_M(C).
$$

Force-Sum then recovers the magnetic member value:

$$
\boxed{
V_C(f_{B,C})
=
m_M\mathbf a_M(C)
-
\sum_{g\in K_C}V_C(g)
}
$$

Repeat the experiment over controlled contexts $C_1,C_2,\ldots,C_n$. Each
context has its own admitted force occurrence $f_{B,i}$. Once independent
force-kind reasoning establishes that those occurrences instantiate the same
magnetic relation, the result is a family of recovered values:

$$
C_i\longmapsto V_{C_i}(f_{B,i}).
$$

Controlled variation may establish, for example:

- reversal when the sign of charge is reversed;
- linear dependence on charge magnitude;
- linear dependence on velocity and magnetic-field magnitude in the relevant
  regime;
- a zero magnetic value when velocity is parallel to the magnetic field;
- perpendicularity to both velocity and magnetic-field directions; and
- magnitude proportional to $|q|vB\sin\theta$.

Within a suitable rotationally covariant hypothesis class, these constraints
support the candidate kernel:

$$
V_C(f_{B,C})=q\,\mathbf v\times\mathbf B.
$$

The triplet does not magically select this formula from one observation. It
makes the value of the known magnetic member observable through the closed
force account. Experimental design and inference over many such values do the
remaining work. If the field variables or other inputs are themselves
unidentified, additional independent structure is required; Force-Sum alone
cannot overcome non-identifiability.

---

## 4. Why an expression-valued IFS fails this test

The tempting alternative is to make the IFS contain already-produced force
expressions:

$$
S_{\mathrm{expr}}
=
\{-k_1x_1,\;m_2g,\;-k_3x_3\},
$$

and then define:

$$
\mathbf F_{\mathrm{net}}
=
\sum_{e\in S_{\mathrm{expr}}}e.
$$

This can appear to work when every kernel is already installed and the written
expressions happen to remain distinguishable. As an ordinary set of vector
values, however, it already loses distinct equal-valued contributions, as the
constant-force case above shows.

Calling the elements "expression tokens" does not solve the problem. If two
tokens remain distinct even when they denote the same vector, they are
identity-bearing occurrences rather than vector values. An evaluation map is
still needed to take each token to the vector that is added. This is `V` under
another name.

A list or multiset can retain repeated outputs, but it still presupposes the
very thing the magnetic discovery case lacks: an output for every admitted
member.

If the magnetic member is known but its kernel is not, the attempted account
is:

$$
S_{\mathrm{expr}}
=
\{-k_1x_1,\;m_2g,\;?\}.
$$

There are three possible responses, and none eliminates the member-value
corner.

### 4.1 Omit the unknown expression

Then the set omits a member already known to exist and cannot be certified as
the closed IFS. Its residual may include that member and any other omitted
members.

### 4.2 Insert an anonymous vector variable `X`

Then the algebra can solve:

$$
\mathbf X
=
\mathbf F_{\mathrm{net}}
-
\sum S_{\mathrm{known}}.
$$

But nothing states that $\mathbf X$ is the value of the independently admitted
magnetic member. That missing association is exactly:

$$
\mathbf X=V_C(f_B).
$$

### 4.3 Insert `V(f_B)` or a named symbol `F_B`

Then the representation works:

$$
S
=
\{-k_1x_1,\;m_2g,\;V_C(f_B)\}.
$$

But this is no longer a set containing only already-known output expressions.
It contains an individual value variable indexed by an admitted force member.
The third corner has been restored, whether it is written as `V(f_B)`, `F_B`,
a typed symbolic slot, or a constraint-solver variable.

Therefore the expression-valued implementation is not rejected because
expressions cannot be added. It is rejected as a complete semantic account
because it cannot represent a known member whose value expression is not yet
known without recreating the relation between member identity and member
value.

---

## 5. The dependency failure when `V(f)` is introduced only later

Suppose Force-Sum is implemented as a one-way pipeline:

```text
force-kind kernel
    -> V(f)
    -> expression-valued IFS
    -> sum
    -> net force
```

Now suppose the magnetic kernel is the object of investigation. The later
evaluator attempts:

```text
evaluate f_B
    -> call magnetic kernel
    -> no kernel has yet been established
    -> no V(f_B)
```

Without `V(f_B)` there is no unknown slot in the Force-Sum equation. Without
that equation there is no closed-account residual identified as the value of
$f_B$. Without the recovered values there is no route by which the magnetic
kernel can be discovered. The proposed dependency graph is circular:

```text
kernel required to produce V(f_B)
    -> V(f_B) required to run Force-Sum
    -> Force-Sum evidence required to discover kernel
```

A later force-kind triplet could try to repair the problem by defining:

$$
V_C(f_B)
=
\mathbf F_{\mathrm{net}}(M\mid C)
-
\sum_{g\in S\setminus\{f_B\}}V_C(g).
$$

But this equation is Force-Sum oriented around the unknown member-value
corner. Putting it in the later triplet merely recreates the omitted
Force-Sum relation there. The earlier block was not the complete Force-Sum
law, and the later block has been forced to duplicate it.

This is a semantic placement result, not a ban on compilation strategies. A
constraint engine may store the equation wherever convenient. But whichever
module owns this equation is implementing the Force-Sum triplet, regardless of
its filename or execution order.

### 5.1 The two dependency shapes

With the triplet, independently established facts meet in one constraint:

```text
interaction and activation evidence ───────> f is a member
independent exhaustion evidence ───────────> IFS membership is closed
concrete force law, when known ─────────────> V_C(f)
Newton II or another independent route ────> F_net(M | C)

                                ┌──────────────────────────────┐
closed IFS + member values ────>│ F_net(M | C) = sum_f V_C(f) │
independent net force ─────────>│                              │
                                └──────────────────────────────┘
                                              │
                                              └──> solve for the one unknown
                                                   V_C(f), when licensed
```

If `V(f)` is removed and the IFS is made from already-produced expressions,
the only available shape is initially one-way:

```text
known concrete kernel
    -> produced expression
    -> expression-valued IFS
    -> sum
    -> net force
```

When the kernel is unknown, this path stops before the unknown even acquires
an address in the equation. Adding an indexed symbolic slot repairs it:

```text
known member f_B -> symbolic slot X_B -> closed sum equation -> solve X_B
                    where X_B means V(f_B)
```

But that repair is precisely the triplet again. It relates the closed member
domain, an individual member-value, and net force before the concrete kernel
is available.

---

## 6. What the triplet admits

The three roles are:

```text
previously admitted / November:
    net-force of the target material object

newly admitted / winter:
    the target's interacting-forces-set

co-admitted / winter:
    the individual member-value V(f)
```

The inward relation is:

$$
R_{\mathrm{FS}}(F,S,V;M,C)
\iff
\operatorname{ClosedIFS}(S;M,C)
\land
F=\sum_{f\in S}V_C(f).
$$

This relation supports several legitimate orientations:

### Forward evaluation

If $S$ is closed and all member values are known, determine net force:

$$
\{V_C(f):f\in S\}
\longrightarrow
\mathbf F_{\mathrm{net}}(M\mid C).
$$

### Inverse member-value determination

If $S$ is closed, net force is known, and exactly one member value is unknown,
determine that member value:

$$
\mathbf F_{\mathrm{net}},
S,
\{V_C(g):g\neq f_*\}
\longrightarrow
V_C(f_*).
$$

### Constraint preservation

If too many quantities are unknown, retain the Force-Sum equation as a
symbolic constraint rather than inventing a value or member.

### Independent audit

If the IFS is independently closed, all values are independently supplied,
and their sum disagrees with an independent net-force determination, report a
model, measurement, context, or theory inconsistency. Do not create an
algebraic repair member.

The triplet is therefore not a directional `map` followed by a `fold`. It is a
constraint relation whose direction is selected by which independently
licensed quantities are available.

---

## 7. Division of labour with later entries

Force-Sum gives `V(f)` its first relational role:

> `V_C(f)` is the individual force-vector value assigned to member `f` such
> that the values of all members of the closed target account have the target's
> net force as their resultant.

Later entries may then provide independent equations for the same variable:

```text
spring:
    V_C(f_s) = -k x

near-Earth gravity:
    V_C(f_g) = m g

magnetism:
    V_C(f_B) = q (v x B)

constraint force:
    V_C(f_N) = N
    together with constraint equations that determine N
```

Those later equations may compute a value forward, leave it symbolic, or be
tested against a value recovered through Force-Sum. They do not introduce a
different magnetic or spring value. They constrain the same `V_C(f)` first
admitted in the force account.

Likewise, outward activation and acting-object entries establish or expose why
`f` exists; they must not infer membership merely because an algebraic
residual is available. Member admission, member-value determination, and
account closure remain distinct logical operations.

---

## 8. Evaluator requirements

The eventual evaluator should treat Force-Sum approximately as a relational
equation constructor:

```text
force_sum(target M, context C, account S, closure certificate e):
    require e proves ClosedIFS(S; M, C)

    emit equation:
        F_net(M | C) = sum(V_C(f) for f in S)

    propagate only licensed consequences:
        all V_C(f) known
            -> determine or audit F_net

        F_net known and exactly one V_C(f) unknown
            -> determine that V_C(f)

        several V_C(f) unknown
            -> retain coupled symbolic equation

        account not independently closed
            -> do not identify the residual with any one member value
```

Required evaluator tests include:

1. closed account, all values known: compute net force;
2. closed account, one value unknown: recover that value;
3. closed account, several values unknown: return an underdetermined or coupled
   symbolic system;
4. open account, one named unknown member: do not equate the residual with that
   member's value;
5. partial sum equals net force: do not infer closure;
6. closed account and inconsistent independently supplied values: audit rather
   than invent a member; and
7. repeated one-unknown experiments: preserve the recovered values and their
   contexts as evidence for or against a proposed later kernel.

---

## 9. Entry-structure consequence

The entry-facing conclusion is:

> The Force-Sum inward relation must expose the closed IFS and the individual
> member-value `V(f)` together with net force. `V(f)` may later be redefined by
> action/reaction, acting-object, orientation, or concrete force-kind
> structures, but it cannot be born only there.

The exact headword form is now settled:

```text
net-force / impressed-force / interaction-set
```

The essential requirement remains that the trace can represent:

```text
known interaction i
known closed membership domain
unknown impressed-force(i -> target)
```

and can orient Force-Sum around that unknown value.

The August 17 managed NML3 reset retired the old E13-E17 wall assignment as
authority and did not install a replacement cut. Accordingly, this note does
not reinstate those numbers. It preserves the structural lesson behind the old
E17 closer while identifying a stronger reason that `V(f)` belongs in the
inward Force-Sum relation.

---

## 10. Boundaries and nonclaims

This argument does not establish that:

- a residual by itself warrants a new force member;
- numerical agreement proves IFS closure;
- one recovered vector determines a general force kernel;
- several unknown member values are individually identifiable from one vector
  equation;
- the current action/reaction representation is final;
- the global identity criterion for impressed-force occurrences is settled;
  or
- the triplet must be implemented as one literal software function.

It establishes that any faithful implementation must preserve the ternary
constraint relation and its inverse member-value orientation. An implementation
that replaces the triplet with a list of already-known expressions either loses
that orientation or reconstructs it through typed unknowns and equations which
are semantically the same triplet.

---

## 11. Sources and provenance

Local entry-production sources:

- [`FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md`](FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md)
  separates IFS membership from `V(f)`, makes Force-Sum abstract over member
  anatomy, and distinguishes construction from aggregation.
- [`DESIGN_2_1_ENTRY_STRUCTURE.md`](DESIGN_2_1_ENTRY_STRUCTURE.md) records the
  historical E13-E17 routing, including the old E17 closer role. Its numbering
  is not reinstated here.
- [`NML3_GENERATOR_NONTERMINATION_CLOSURE_CONSTRAINT_2026-08-08.md`](../08_nm_lesson_drafts/nml3/NML3_GENERATOR_NONTERMINATION_CLOSURE_CONSTRAINT_2026-08-08.md)
  separates positive member generation from universal-negative closure.
- [`NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md`](../08_nm_lesson_drafts/nml3/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md)
  records the consequences of member identity, closure, and residual testing.
- [`NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md`](../08_nm_lesson_drafts/nml3/NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05.md)
  states the correct-account, correct-member-kind, and resultant commitments of
  the Force-Sum triplet.

Managed-context authority was checked coherently at
`canvalidk/VD-docs@26265de6e79013bd93b37f9ad278c3dab6ffc11b` (latest `main`
resolved on 2026-08-18). Exact managed paths consulted were:

- `Newton/nml/nml3/NML3_ENTRY_STRUCTURE_RESET_2026-08-17.md`;
- `Newton/nml/nml3/conceptual/NML3_FORCE_SUM_STEELMAN_2026-08-08.md`;
- `Newton/nml/nml3/conceptual/NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md`;
  and
- `Newton/Design 3/vd_acting_object_architecture_consolidation.md`.

The managed reset preserves the entry-cut-independent conceptual findings and
retires the old cut without selecting a new one.
