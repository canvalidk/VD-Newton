# NML3 Warranted Force Account: Foundational Explication

Status: active local conceptual note, authored 2026-08-05 from the force-sum
discussion. This note sharpens the reason the force-sum triplet is needed. It
does not yet define the exact warranting mechanism or ratify final entry
wording.

## Central claim

The force-sum law is not fundamentally needed to tell us that vectors can be
added. Nor is it a licence to infer physical interactions from any algebraic
decomposition of a net-force vector.

Its deeper role is to admit the following theoretical commitment:

> For a specified material object under specified conditions, there is a
> correct interacting-forces-set. Its members are forces whose membership is
> warranted independently of their ability to reproduce the measured net
> force, and the vector sum of all and only those members is the material
> object's net force.

The word `warranted` and the symbol \(W\) will be used to mark the distinction
between a merely writable vector summand and a force that has earned membership
in the interaction account. What makes a force warranted is not settled merely
by introducing the word. That work belongs in the outward-facing walls of the
law.

This is a particularly implicit commitment in ordinary presentations of
Newtonian mechanics. Those presentations usually begin with a list of forces,
as though the existence, identity, ownership, and completeness of the list
were already unproblematic. Once that hidden assumption is removed, the size of
the force-identification problem is larger than the vector-sum rule contained
within it.

---

## 1. The spring experiment exposes the gap

Consider a material object \(M\) in an experimental arrangement containing a
spring. Let \(x\) be a measured displacement along a fixed experimental axis
and let \(F_{\mathrm{net}}\) be the independently measured signed component of
the material object's net force along that axis. Suppose the analysis
establishes

$$
\frac{dF_{\mathrm{net}}}{dx}=-k
$$

and, after fixing the relevant reference condition, supports the fitted
relation

$$
F_{\mathrm{net}}(x)=-kx.
$$

This is already a substantive empirical result. It establishes how the
measured net force varies with displacement in the investigated conditions.
It does **not** yet say that the material object is interacting with the
spring.

The equation contains a net-force quantity, a displacement variable, and a
fitted coefficient. It does not contain, merely by its algebraic form:

- the spring as an interaction relatum;
- a force-instance attached to the spring-object relation;
- a criterion by which that force-instance was distinguished from other
  possible force descriptions; or
- a warrant that no other interaction-force has been omitted.

The sentence

> The material object is interacting with the spring.

is therefore not a paraphrase of \(F_{\mathrm{net}}=-kx\). The equation
is a measured functional relation. The sentence is an attribution of a
physical relation between material objects. Moving from the first to the second
requires an additional evidential and theoretical bridge.

If the experiment is introduced by saying that the object is *only*
interacting with the spring, the word `only` has already supplied the very
interaction attribution and completeness claim that need explanation. Such a
setup may be legitimate, but its legitimacy cannot be derived afterward from
the shape of the fitted curve. The basis on which the experimental arrangement
was known to have that interaction structure must itself be made explicit.

---

## 2. Equality does not carry physical provenance

It is tempting to move from

$$
F_{\mathrm{net}}=-kx
$$

to

$$
F_{\mathrm{net}}=F_1=-kx
$$

and then to call \(\mathbf F_1\) the spring force. But the introduction of
\(\mathbf F_1\) has not added evidence. It may be nothing more than a new name
for the measured net-force vector.

The same established relation permits

$$
F_{\mathrm{net}}
=-\frac{k}{2}x-\frac{k}{2}x
=F_1+F_2.
$$

Nothing about this equally valid equation establishes two interactions or two
interacting objects. More generally, for any positive integer \(n\),

$$
F_{\mathrm{net}}
=\sum_{i=1}^{n}-\frac{k}{n}x.
$$

Arbitrary cancelling terms may also be introduced. For any signed force
quantity \(A\),

$$
F_{\mathrm{net}}
=(F_{\mathrm{net}}+A)+(-A).
$$

Every expression is algebraically legitimate. None increases the number of
physical interactions.

The same point applies to an object in free fall. A gravitational net force
may be written as one vector, as any number of fractional vectors, or as a
vector plus indefinitely many cancelling pairs. The object does not thereby
interact with an indefinitely large population of material objects.

Consequently:

$$
\boxed{
\text{The number of written vector terms does not determine the number of
physical interactions.}
}
$$

Writing \(F_{\mathrm{net}}=F_1\) is no more physically
privileged than writing
\(F_{\mathrm{net}}=F_1+F_2\). A one-term expression
does not establish one interaction, and a many-term expression does not
establish many interactions.

---

## 3. Four things that must not be collapsed

The reasoning becomes safer when four different kinds of item are kept
explicit.

### 3.1 Material objects

Let \(M\) be the target material object and let \(O_i\) be another material
object that may be interacting with it. Material objects are possible relata of
the physical interaction relation.

### 3.2 Force-instances

Let \(w_i\) be a force-instance attributed to the target side of a particular
interaction. A force-instance has identity beyond its numerical vector value.
Two distinct force-instances may have equal vector values without becoming one
and the same force.

This identity distinction is needed both to prevent duplicate admission of one
force and to preserve two genuinely distinct forces that happen to have the
same magnitude and direction.

### 3.3 Vector values

Let

$$
\operatorname{vec}(w_i)
$$

be the vector value of force-instance \(w_i\) under the chosen representation.
Vectors can be added, decomposed, resolved into coordinate components, and
rewritten. Those representational operations do not by themselves create,
destroy, merge, or multiply force-instances.

### 3.4 Warrants

Let

$$
W(M,O_i,w_i)
$$

mean that the available evidence and applicable admission procedure warrant
attributing force-instance \(w_i\) to an interaction between target object
\(M\) and other object \(O_i\).

The warrant is not another material object and is not an additional force
vector. It licenses an attribution. The correct conclusion is

$$
W(M,O_i,w_i)
\Longrightarrow
O_i\in I(M),
$$

where \(I(M)\) is the set of material objects warranted to be interacting with
\(M\) in the specified conditions.

It would be a category error to say that the net force interacts with
\(W_i\), or that one force interacts with another force. The intended claim is
that material object \(M\) interacts with material object \(O_i\), and that
\(W\) warrants attaching a force-instance to the target side of that material
relation.

When \(W(M,O_i,w_i)\) obtains, this note abbreviates the admitted force-instance
as \(W_i\). Thus \(W\) names the warrant relation, while \(W_i\) names a
force-instance carrying warranted member status. Neither is an interacting
material object.

Thus:

$$
\boxed{
\text{material object}
\neq\text{force-instance}
\neq\text{vector value}
\neq\text{warrant}.
}
$$

---

## 4. The forward force sum and the inverse identification problem

The familiar force-sum direction is a forward construction:

```text
independently warranted force-instances
    -> take their vector values
    -> add those vector values
    -> obtain the net-force vector
```

The spring question begins in the opposite direction:

```text
measured net-force behaviour
    -> identify the force-instances
    -> identify the other material objects
    -> establish the interaction account
```

These directions are not interchangeable. The forward map from force accounts
to resultant vectors is many-to-one. Infinitely many collections of vectors
can have the same sum. Therefore a net-force vector does not possess a unique
algebraic inverse that reveals its physical interaction history:

$$
\mathbf F_{\mathrm{net}}
\not\Longrightarrow
\{\mathbf F_1,\mathbf F_2,\ldots\}
\not\Longrightarrow
\{O_1,O_2,\ldots\}.
$$

The force-sum law must consequently do more than describe the forward vector
operation. It must distinguish the physically admitted domain on which that
operation is to be performed. Without that domain restriction, a reverse
decomposition of the net vector could manufacture any desired interaction
ontology.

---

## 5. The interacting-forces-set is the substantive commitment

For a specified target object, time or interval, and physical arrangement, let

$$
\operatorname{IFS}(M)
$$

denote the `interacting-forces-set`. This must not be understood as an
arbitrarily chosen collection of vectors whose sum happens to match the net
force. It is the force account whose membership tracks the material object's
actual interactions under the theory's warranting conditions.

The force-sum law commits the theory to there being a right account despite the
unlimited number of sum-preserving decompositions. In this sense, the IFS is
treated as a true object of nature and not as a free feature of the modeller's
notation.

Calling the IFS determinate does not mean that an investigator always knows its
membership with certainty. It means that membership is not constituted by
whichever decomposition the investigator chooses. A warranted determination
may be incomplete, uncertain, or revisable while still aiming at a fact of the
matter established by the law.

The singular word `correct` also matters. For fixed target and conditions, the
law is not proposing several equally correct IFSs corresponding to several
algebraic decompositions. It commits to one membership fact, up to harmless
changes of notation, coordinate representation, and ordering. If two proposed
accounts disagree about which force-instances exist, at least one account is
unwarranted or the warrant-and-closure procedure has not yet determined the
case. The `set` language makes ordering irrelevant; the force-instance
identities make membership non-arbitrary.

Strictly, the IFS cannot be only a set of bare vector values. If two distinct
interactions exert equal vector values, a value-set would collapse them into
one element. The IFS must preserve force-instance identity, ownership, and the
relevant interaction attachment; the vector-sum operation then maps each
member to its vector value.

The central relation is therefore:

$$
\boxed{
\mathbf F_{\mathrm{net}}(M)
=
\sum_{W_i\in\operatorname{IFS}(M)}
\operatorname{vec}(W_i)
}
$$

where \(W_i\) denotes a warranted force-instance, not merely a convenient
summand.

The equation is read in this order:

```text
warrant membership independently
    -> form the correct and complete IFS
    -> sum the vector values of its members
    -> identify the resultant as the net force
```

It must not be read backward as:

```text
choose vectors that reproduce the net force
    -> call those vectors warranted
    -> infer that matching material interactions exist
```

The backward reading would define the evidence by the conclusion and make the
force-sum law self-confirming.

---

## 6. What `warranted-force` must mean, and what remains open

A bare symbol such as \(\mathbf F_1\) is cheap: it can be created by naming any
part of any algebraic decomposition. A warranted force \(W_1\) is expensive:
its admission must be earned by a procedure that distinguishes a physical
force-instance independently of the desired resultant.

The warrant does not create the physical interaction. It is the theory's
licensed basis for admitting the interaction-force to the account rather than
leaving it as an unsupported candidate. `Warranted` therefore distinguishes a
correctly earned membership claim from an arbitrary or mistaken one; it does
not make nature depend on an investigator's choice of notation.

At minimum, the eventual account of warrant must satisfy the following
constraints.

### Independence from the sum

A candidate cannot become warranted merely because including it makes the
right-hand side equal the already measured net force. Otherwise arbitrary
halves, cancelling pairs, and invented residual terms would all be admissible.

### Physical attachment

The warrant must connect the candidate force-instance to a relation involving
the target material object and another warranted relatum or interaction
condition. A suggestive functional shape such as \(-kx\) is not by itself such
an attachment.

### Force-instance identity

The warrant must make it possible to distinguish rediscovering the same
force-instance from discovering a second, distinct force-instance with an
equal vector value.

### Non-circular empirical access

The observations used to warrant an interaction-force must not already require
the force-sum conclusion they are supposed to support. In particular, a force
account must not be called complete merely because its members have been
adjusted until their sum agrees with the measured net force.

### Traceability and revisability

The warrant should expose the observations, interventions, boundary
conditions, provenance, and admission rule used. A later evidential revision
may change which force-instances are currently warranted without turning
arbitrary decompositions into physical interactions.

These are constraints on an eventual definition, not yet that definition.
Possible ingredients such as controlled variation, intervention, removal,
relational dependence, and invariance may help establish a warrant, but listing
those ingredients does not complete the theory. The exact human-executable
route belongs in the force-sum walls.

The name `warranted-force` is conceptually informative because it foregrounds
the missing admission step. It remains provisional entry terminology. The
current working headword `contributing-force` is vulnerable precisely because
it can sound as though appearing in a successful vector sum is enough to earn
force status.

---

## 7. The force-sum triplet as an admission event

The triplet argument says that a theory does not honestly enlarge its ontology
by adding an isolated word. It must preserve:

1. a previously admitted candidate or point of contact;
2. a newly admitted result, kind, quantity, or state; and
3. a co-admitted differentiator, operation, or relational condition that makes
   the new distinction non-arbitrary.

For the force-sum house, the emerging roles are:

```text
previously admitted / November:
    net-force-material-object

newly admitted / winter:
    interacting-forces-set

co-admitted / winter:
    warranted-force
```

The ternary commitment can be represented schematically as

$$
T\big(
\text{net-force-material-object},
\text{interacting-forces-set},
\text{warranted-force}
\big).
$$

The triplet is not merely saying that three words occur together. It admits
three connected claims:

1. **Correct collection:** for the specified target and conditions, there is a
   physically correct IFS rather than only an unlimited family of
   sum-equivalent decompositions.
2. **Correct member-kind:** a force can earn the status required for membership
   in that IFS; bare vector summands do not have that status automatically.
3. **Resultant relation:** the net-force vector is the vector sum of all and
   only the warranted force-instances in the correct IFS.

The third headword does not require every particular IFS to contain an actual
member. It admits the *member-kind* and its role. A particular force account may
contain zero, one, or many warranted force-instances.

This is why the triplet is needed even though vector addition already exists.
The new theoretical content is not addition. It is the licensed distinction
between the correct interaction account and the indefinitely many incorrect
but algebraically successful decompositions.

---

## 8. Why the relation must say “all and only”

The phrase “all and only the warranted members” performs two separate jobs.

### Only warranted members

Every term admitted to the force account must possess an independent warrant.
This excludes arbitrary fractional terms, cancelling vectors, coordinate
components mistaken for separate forces, and residual terms invented solely to
repair a mismatch.

### All warranted members

Every force-instance that satisfies the membership conditions must be included.
A convenient partial account does not become the IFS merely because its current
members already produce an interesting or approximately correct resultant.

This distinction separates **member correctness** from **set completeness**.
An investigator may possess a list whose every current member is genuinely
warranted while still having failed to discover another warranted interaction.
The current list is then locally sound but not yet the complete IFS.

Several important asymmetries follow:

$$
\operatorname{IFS}(M)=\varnothing
\Longrightarrow
\mathbf F_{\mathrm{net}}(M)=\mathbf 0,
$$

but

$$
\mathbf F_{\mathrm{net}}(M)=\mathbf 0
\not\Longrightarrow
\operatorname{IFS}(M)=\varnothing.
$$

A nonempty IFS may contain forces whose vector values cancel. Likewise, a
nonzero net force does not reveal whether its IFS has one member or many.

---

## 9. The triplet and walls divide the theoretical labour

The law house now has a precise division of responsibility.

### Chimney: the prior net-force quantity

`net-force-material-object` is already available as the prior point of contact.
The force-sum law is not inventing the existence of measured net-force behaviour
from nothing.

### Triplet: admit the correct account and its resultant relation

The inward triplet states that there is a correct IFS, that its eligible members
are warranted force-instances, and that the net force is the resultant of all
and only those members.

The triplet does not need to contain the full experimental dossier by which a
specific force-instance is warranted. Its job is to admit the distinction and
state the constitutive relation.

### Generator wall: warrant one member at a time

The generator wall must make the newly admitted member-kind independently
usable. It explains how an investigator moves from a candidate interaction to
a warranted force-instance and adds that identified instance to the target's
force account without deriving it from a chosen decomposition of the net
vector.

This wall must also preserve force identity so that the same instance cannot be
admitted twice while distinct equal-valued instances remain admissible.

### Closer wall: warrant completeness

The closer or terminator wall must explain when the investigator is licensed to
say that the account is complete. It answers a different question from the
generator:

```text
generator:
    Is this candidate a warranted member?

closer:
    Are there any further warranted members not yet in the account?
```

Without the generator, the IFS is an unexplained human-supplied list. Without
the closer, it is an indefinitely extendable partial list rather than a
determined force account. The two walls operationalize the two halves of “all
and only.”

---

## 10. The careful route through the spring case

The spring case should ultimately proceed through distinct stages.

### Stage 1: establish the net-force regularity

$$
F_{\mathrm{net}}(x)=-kx.
$$

This is a force-side empirical result. It does not yet state its interaction
provenance.

### Stage 2: investigate a candidate material relation

The spring \(S\) is treated as a candidate other object in the interaction
account. The fact that the apparatus contains a spring may motivate the
investigation, but visual or linguistic presence alone does not establish the
force attachment.

### Stage 3: earn the warrant

The eventual generator procedure must establish something of the form

$$
W(M,S,w_S).
$$

Only here is a particular force-instance warranted as belonging to the
interaction between the target object and the spring. The measured relation
\(-kx\) may participate in the evidence, but it cannot do all the work merely
because it resembles a familiar equation named “Hooke's law.”

### Stage 4: close the account

The closer must warrant that no further force-instance belongs in the account
for the specified target, interval, and conditions. Only then may one write

$$
\operatorname{IFS}(M)=\{W_S\}.
$$

### Stage 5: apply the triplet relation

The force-sum law then gives

$$
\mathbf F_{\mathrm{net}}(M)=\operatorname{vec}(W_S).
$$

Agreement between this independently constructed force account and the
independently measured net-force behaviour can be assessed. It must not be
guaranteed in advance by defining \(W_S\) as “whatever vector makes the two
sides equal.”

### Stage 6: make the interaction statement

From the warranted attachment,

$$
W(M,S,w_S),
$$

one may state:

> The material object \(M\) is warranted to be interacting with the spring
> \(S\) under the specified conditions.

This conclusion comes from the warrant attached to the material relation, not
from the typography or term count of the force equation.

---

## 11. What the force-sum law does not claim

The clarified law must not be made to say more than it earns.

It does not claim that:

- every algebraically valid decomposition is a possible IFS;
- a fitted force-displacement relation identifies its source by shape alone;
- writing one force symbol establishes one interaction;
- writing several force symbols establishes several interactions;
- a zero net force means that no interactions exist;
- equal force vectors are necessarily the same force-instance;
- a human investigator has infallible or immediate knowledge of the IFS;
- the triplet alone supplies the measurement and intervention procedures needed
  to warrant a particular member; or
- agreement of a chosen sum with the measured net force can serve as the sole
  evidence for the membership and completeness of that same sum.

The law does claim that the theory distinguishes a correct force account from
arbitrary decompositions and that the resultant of that warranted, complete
account is the net force.

---

## 12. Consequences for traces and evaluators

A successful NML3 trace should make the interaction account visibly prior to
the addition. It should be impossible to pass merely by inventing a
decomposition that produces the expected resultant.

At minimum, the entries and evaluator should distinguish the following cases.

### Arbitrary half-vector decomposition

```text
F_net = (1/2)F_net + (1/2)F_net
```

This is valid vector algebra but provides no warranted force members.

### Cancelling invented pair

```text
F_net = (F_net + A) + (-A)
```

This is also valid vector algebra but does not earn two additional
interactions.

### Distinct equal-valued forces

Two separately warranted force-instances may have the same vector value. Both
must remain members because force identity is not vector-value identity.

### Duplicate force-instance

The same warranted force-instance must not be entered twice, even if repeating
it would produce a desired sum.

### Empty force account

An empty, successfully closed IFS must produce the zero vector as the empty
sum. Failure to discover any member is not by itself successful closure; the
absence must be warranted.

### Nonempty equilibrium account

A nonempty IFS whose members cancel must produce zero net force without being
mistaken for the empty IFS.

### Unknown cardinality

The generator must operate without assuming in advance how many interactions
will be found, and the closer must establish termination independently of the
current resultant.

These are not peripheral programming details. They are executable tests of the
ontological and evidential distinction admitted by the triplet.

---

## 13. Relation to the triplet-admission argument

The general triplet argument says that the minimum honest theoretical admission
contains a prior candidate, a newly admitted distinction, and a co-admitted
basis on which that distinction does work.

The force-sum case makes that argument concrete. Before the new law, the theory
can already speak of a material object's net force. What it cannot yet honestly
do is move from that resultant to a uniquely privileged list of interaction
forces. Introducing the phrase `interacting-forces-set` alone would be word
magic unless the theory also introduced the member-status by which the correct
set differs from arbitrary sum-equivalent collections.

Conversely, introducing `warranted-force` alone would leave the theory without
the complete collection whose resultant role gives those instances their
force-account significance. The IFS and its warranted member-kind are therefore
co-admitted relative to the already available net-force quantity.

The triplet records the constitutive commitment. The walls record how its new
terms become independently usable. In the language of the broader admission
argument:

```text
triplet:
    admit that there is a correct force account and state its resultant
    relation

walls:
    explain how a candidate earns membership and how the account earns closure
```

This prevents the theory from hiding the decisive work in an unexplained
instruction such as “list all the forces acting on the object.”

---

## 14. Open work

This explication identifies what the force-sum triplet must commit to. It does
not yet settle the mechanisms required to fulfil that commitment. The next work
must determine:

1. the exact headword for a warranted force-instance;
2. the owner, time, interval, and state qualifications carried by every IFS;
3. the identity conditions for one force-instance;
4. the exact evidential operation that warrants attachment to another material
   object or interaction condition;
5. how that operation avoids using net-force agreement as its own premise;
6. whether one material interaction can yield more than one relevant
   force-instance in the same account;
7. how the generator records provenance and prevents duplicate admission;
8. how the closer warrants that no eligible force-instance remains undiscovered;
9. how uncertainty and revisable evidence affect current warranted membership;
10. how later action-reaction and concrete force-law blocks refine the
    interaction attachment without being imported prematurely into NML3; and
11. how the evaluator distinguishes a closed warranted account from a merely
    successful vector fit.

Until those questions are answered, \(W\) is a required theoretical role and a
constraint on the walls, not a completed recipe.

---

## Conclusion

The equation

$$
F_{\mathrm{net}}=-kx
$$

does not contain the sentence “the object is interacting with the spring.” Nor
does rewriting the equation with one force symbol, two half-force symbols, or
any other number of summands create that sentence.

The missing bridge is warrant. A vector becomes eligible for the interaction
account only when a force-instance is independently warranted as attached to a
material interaction. A collection becomes the IFS only when its individual
members are warranted and its completeness is warranted. The net force is then
the resultant of that prior, correct account.

The essence of the force-sum triplet is therefore:

$$
\boxed{
\begin{gathered}
\text{a correct interacting-forces-set exists;}\\
\text{its legitimate members are warranted force-instances;}\\
\mathbf F_{\mathrm{net}}
=\sum\text{the vector values of all and only those members.}
\end{gathered}
}
$$

This is why the force-sum law lies inside a larger subtlety. Vector addition is
the comparatively small operation. The larger theoretical achievement is
earning the right to say which physical interactions the terms in the sum
represent at all.

---

## Source and scope note

Primary source: the 2026-08-05 discussion developing the spring example, the
unlimited-decomposition objection, the symbol \(W\), and the IFS interpretation
of the force-sum triplet.

Local active sources consulted:

- `NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02.md`;
- `NML3_CONTRIBUTING_FORCE_TERMINOLOGY_DECISION_2026-08-02.md`;
- `nm_l3_lesson_draft.md`; and
- `../../07_design_2_1/notes/vd_docs_handoffs/why_the_triplet_rule_is_needed_d2.md`.

The last of those records its managed-context basis as
`canvalidk/VD-docs@8e09dbf9d3e521cbe76e36426ead656c04a71650`.
No managed VD-docs file was edited. This note is an entry-facing local
explication for subsequent NML3 drafting.
