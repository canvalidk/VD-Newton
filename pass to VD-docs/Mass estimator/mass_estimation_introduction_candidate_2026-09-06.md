# Why measuring inertial mass is not just dividing force by acceleration

**Working introduction — revised 2026-09-06.** Local candidate, awaiting transfer to VD-docs; no managed draft number assigned. [Source and drafting record](mass_estimation_introduction_candidate_sources_2026-09-06.md).

## 1. The problem

Newton's Second Law appears to tell us how to determine any one of three quantities from the other two. For one material object, over the same interval and in the same inertial frame, let $\mathbf F$ denote the net force, $m$ the inertial mass, and $\mathbf a$ the acceleration. Given mass and acceleration, multiply to obtain force. Given force and mass, divide to obtain acceleration. Given force and acceleration, the apparent instruction is to divide again:

$$
\mathbf F=m\mathbf a.
\tag{1}
$$

$$
\mathbf a=\frac{\mathbf F}{m}.
\tag{2}
$$

$$
m\stackrel{?}{=}\frac{\mathbf F}{\mathbf a}.
\tag{3}
$$

The first two operations are well defined. Inertial mass is a positive scalar; net force and acceleration are vectors. A vector can be multiplied by a scalar, and it can be divided by a nonzero scalar. The condition $m>0$ supplies exactly what equation (2) needs.

But what does the third instruction mean? Vector division is not defined. What, then, is mass?

The difficulty is already present in the kinds of quantities being used. Equation (3) presents a quotient without supplying an operation that takes the two vectors and returns the required positive scalar. Writing it like the other two equations does not give it the same mathematical standing.

There is another asymmetry. Although mass is positive, acceleration can be the zero vector. If net force is also zero, Newton's law holds for every positive mass. Yet the proposed division asks us to evaluate $0/0$. The object's mass need not be undefined; these inputs simply do not identify it. An account of mass determination must say what happens here, while the apparent rearrangement leaves us with undefined arithmetic.

## 2. Why the magnitude quotient is insufficient

Perhaps the division was only meant as shorthand for dividing the lengths of the vectors. That gives a familiar scalar expression:

$$
m\stackrel{?}{=}\frac{\|\mathbf F\|}{\|\mathbf a\|}.
\tag{4}
$$

For nonzero force and acceleration pointing in the same direction, this quotient does recover the positive scalar relating them. But what happens when the supplied vectors do not point in the same direction?

Suppose the reported measurements are $\widetilde{\mathbf F}=(10,0)\,\mathrm N$ and $\widetilde{\mathbf a}=(0,5)\,\mathrm{m\,s^{-2}}$. Their magnitude quotient is $2\,\mathrm{kg}$. Multiplying the reported acceleration by that mass, however, gives $(0,10)\,\mathrm N$, not the reported force $(10,0)\,\mathrm N$. No scalar can rotate one vector into the other. The quotient has produced a positive number with the right units, but it has not recovered a scalar satisfying the original vector relation.

Directional disagreement is not confined to an artificial example. Force and acceleration obtained through measurement arrive with uncertainty. Even when the underlying Newtonian vectors share a direction, errors in their reported components need not preserve that direction. The disagreement can be very small; it still prevents any one scalar from relating the two reported vectors exactly. A common experimental axis can avoid this particular difficulty, but general vector measurements do not come with that restriction.

Taking magnitudes removes the directional information without explaining how the discrepancy should affect the mass determination. It also leaves the zero denominator untouched. Equation (4) therefore cannot serve as an unrestricted inverse of the vector relation.

A natural response is to restrict its inputs: perhaps we should first obtain force and acceleration values that are properly aligned, and only then divide their magnitudes. That response brings us to the crucial question. Must the force and acceleration supplied to mass determination already be aligned—and can we require that while retaining their use in the other two Newton-II operations?

## 3. Must the input vectors already be aligned?

The three equations must use the same force and acceleration quantities. Given evidence for an object's net force, we should be able to ask for that force without first saying whether we intend to use it to calculate acceleration or mass. For fixed evidence and a fixed determination procedure, the result should not change merely because a different equation will consume it. The same requirement applies to acceleration.

Each operation must also remain usable when the quantity it determines is not already available. We use equation (1) to obtain force from mass and acceleration, and equation (2) to obtain acceleration from force and mass. This constrains what obtaining their inputs can require.

Consider equation (1). Suppose mass is supplied and measurements of the object's motion provide acceleration. We want to determine the net force. If that acceleration could qualify as an input only after being aligned with the force, obtaining it would require information about the force direction we are trying to determine. We could no longer supply the input without first obtaining information that the operation was meant to provide.

Equation (2) imposes the corresponding constraint on force. Suppose mass is supplied and a force account provides the net force. We want to determine acceleration. If the force could qualify as an input only after being aligned with the acceleration, obtaining the input would require the acceleration direction that is still unavailable.

Adjusting only one vector does not avoid this difficulty. Making acceleration depend on force obstructs force determination; making force depend on acceleration obstructs acceleration determination. To preserve both operations, acceleration must have a route that does not require the force being sought, and force must have a route that does not require the acceleration being sought. Those routes must remain admissible when their evidence is available.

Force and acceleration can still be calculated from one another. Their measurement errors can also be correlated. The requirement concerns which information must already be available to obtain an input: prior alignment to the other vector cannot be compulsory for the shared quantity.

The mass operation consequently has to address the independently obtainable measurements discussed in section 2, including pairs that do not agree in direction. Such disagreement does not, by itself, make either result cease to be a force or acceleration measurement. It raises a question about their joint compatibility. Restricting a quotient to already compatible pairs is legitimate, but leaves the mass demand arising from the other measurements unanswered. The determination may find that the evidence does not support a mass value, but that assessment is part of the task.

We can use both measurements together to construct a distinct pair of compatible estimates. That is a possible way forward, but the joint construction is then part of determining mass from the supplied evidence. A magnitude quotient may read off the scalar afterward. It does not explain how the compatible pair was obtained, so it cannot stand alone as the complete determination.

## 4. Do dot products repair the definition?

A different proposal is to retain directional information by using dot products. Starting from $\mathbf F=m\mathbf a$, taking the dot product with acceleration and solving for the scalar suggests

$$
m_a=\frac{\mathbf F\cdot\mathbf a}{\mathbf a\cdot\mathbf a}.
\tag{5}
$$

But taking the dot product with force instead suggests

$$
m_F=\frac{\mathbf F\cdot\mathbf F}{\mathbf F\cdot\mathbf a}.
\tag{6}
$$

Here the subscripts distinguish the two proposed scalar readouts. On exact, nonzero, codirectional inputs, both recover the same mass. On unaligned measurements, they can give different answers.

For example, take $\widetilde{\mathbf F}=(2,1)\,\mathrm N$ and $\widetilde{\mathbf a}=(1,0)\,\mathrm{m\,s^{-2}}$. Equation (5) gives $2\,\mathrm{kg}$; equation (6) gives $2.5\,\mathrm{kg}$. The magnitude quotient gives a third result, $\sqrt5\,\mathrm{kg}$. All three are finite positive scalars with the appropriate units. Which one is mass?

The disagreement has a simple geometric form. For nonzero input vectors separated by an acute angle $\theta$,

$$
m_a=\frac{\|\mathbf F\|}{\|\mathbf a\|}\cos\theta,
\tag{7}
$$

whereas

$$
m_F=\frac{\|\mathbf F\|}{\|\mathbf a\|}\frac{1}{\cos\theta}.
\tag{8}
$$

One answer falls below the magnitude quotient; the other rises above it. At a right angle, the first proposal returns zero and the second has a zero denominator. For an obtuse angle, both return negative values. Dot products supply defined vector operations, but these particular quotients do not thereby supply a generally applicable positive-mass determination.

The fact that both formulas can be derived from Newton's equation does not resolve their disagreement. Their derivations assume the exact vector relation holds. When a supplied pair fails that relation, choosing one of the resulting formulas extends it to inputs for which the derivation no longer establishes a mass.

That choice can have a justification: a measurement model or a fitting rule might favor one treatment of the discrepancy. But the justification must be supplied. Newton's equation alone does not say why acceleration should be the vector we dot with rather than force, or why either resulting scalar should be accepted as the measured mass. Calling the chosen expression a rearrangement leaves that decision unexplained.

## 5. What, then, is mass?

The difficulty is more than a missing convention for writing division. The magnitude quotient requires a suitable relation between its inputs; the dot-product proposals offer different answers once that relation fails. A procedure that first constructs compatible values must explain how it obtains them. A procedure that chooses among conflicting scalar readouts must explain what warrants its choice. That work belongs to the account of mass determination.

Thus $m=\mathbf F/\mathbf a$ does not supply a definition, and replacing its symbols with familiar scalar arithmetic does not, by itself, rescue it. The exact quotients remain useful where their conditions hold. What is missing is an account of what determines mass from the force and acceleration evidence we can actually supply.

What, then, is inertial mass—and what would count as defining how it is determined?
