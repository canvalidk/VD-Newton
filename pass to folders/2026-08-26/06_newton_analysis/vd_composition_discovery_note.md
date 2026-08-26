# Composition: A Newtonian Word

**Date:** 2026-03-26
**Context:** Discovered while fixing the acting-object ownership bug in the VD Newton instance

---

## How We Got Here

The acting-object ownership bug required inverting an arrow: instead of acting-objects being standalone entities that "have" a paired-particle, particles should *own* their acting-objects. The fix was straightforward in principle — define a new entry that says "a particle has zero or more acting-objects" and redefine paired-particle as the back-reference.

The question that slowed us down was: what do we call the thing? What is the set of acting-objects that a particle has?

The first instinct was something functional: "set-of-acting-objects." Accurate but lifeless. Then we considered "constituents" — closer, but too generic. Then we asked: what's the standard term in computing for "object A has objects B, C, D as components"?

Composition.

And then the realisation hit: this isn't a metaphor. The computer science concept of composition — "has-a" as opposed to "is-a" — isn't borrowed from some abstract mathematical idea that happens to also apply to physics. It *is* the physics idea. Or rather, both the CS concept and the physics concept are the same concept, encountered in different contexts and given the same name independently because the underlying structure is identical.

## What Composition Means in CS

In object-oriented programming, composition is one of the two fundamental relationships between objects. Inheritance ("is-a") says a spring IS an acting-object. Composition ("has-a") says a particle HAS acting-objects. The Gang of Four design patterns book famously advises "favour composition over inheritance" — meaning, build complex behaviour by assembling components rather than by extending class hierarchies.

Composition means:

- The container owns its components
- Components don't exist independently of their container (they live and die with it)
- The container's identity is partly constituted by what it contains
- You understand the container by understanding its parts

## What Composition Means in Newtonian Mechanics

A point-particle in Newtonian mechanics is a modelling abstraction. It represents some physical body — a ball, a planet, a car — by reducing it to a single point (typically the centre of mass) and attributing to that point all the force-producing mechanisms of the original body.

A ball has gravity. A planet has gravity and tidal forces. A car has gravity, friction, air drag, engine thrust, normal forces from the road. Each of these is an acting-object: a mechanism with an activation-condition and a canonical-force.

The particle's mechanical identity — what it *does* to the rest of the universe, force-wise — is exactly its composition of acting-objects. Strip away the acting-objects and the particle is just a position and a mass. The acting-objects are what make it mechanically interesting. They are the components that constitute the particle's mechanical behaviour.

This is composition in the CS sense, exactly:

- The particle owns its acting-objects
- The acting-objects don't exist independently (they're located at the particle's position, they belong exclusively to one particle)
- The particle's mechanical identity is constituted by its acting-objects
- You understand the particle by understanding its components

## Why This Isn't a Coincidence

The reason the same word applies in both domains is that both domains are modelling the same structural pattern: a whole that is understood through its parts.

CS didn't invent composition. Nor did Newton. Humans have been reasoning about wholes and parts since before either discipline existed. A ship has sails, a cart has wheels, a body has organs. The "has-a" relationship is one of the most basic structures in human cognition.

What Newton did — and what the VD makes explicit — is formalise a specific instance of this pattern for mechanical systems. A point-particle "has" acting-objects the way a ship "has" sails. The sails are what make the ship move; the acting-objects are what make the particle exert forces. The ship's behaviour is the composition of its parts' behaviours; the particle's force contribution is the composition (more precisely, the union) of its acting-objects' contributions.

What CS did, three centuries later, was rediscover the same pattern in a different medium and give it a technical name. When the Gang of Four said "favour composition over inheritance," they were expressing a design preference that Newton had already followed implicitly: the way to build complex mechanical systems is to compose simple force-producing components, not to build elaborate type hierarchies.

## The Connection to Mass

This is perhaps the most striking implication. In Newtonian mechanics, there are two numbers that define a particle: its inertial mass and its position. Mass tells you how the particle *responds* to forces (Newton II: F = ma). Position tells you where the particle *is*.

But neither mass nor position tells you what forces the particle *produces*. That's the mechanical-composition. And arguably, the composition is at least as fundamental to the particle's identity as its mass. Mass is a scalar — one number. Composition is a structured object — a set of mechanisms, each with its own activation-condition and force law. Mass tells you the particle's passive response. Composition tells you its active contribution to the universe.

In a sense, mass and composition are complementary halves of a particle's mechanical identity:

- **Mass** — how the particle receives force (passive, scalar, Newton II)
- **Composition** — how the particle produces force (active, structured, acting-object law + force-sum)

That composition has been implicit in Newtonian mechanics for three centuries — every physicist works with it constantly — but it never got its own name in physics. It took the VD, with its requirement to name every concept used in a definition, to surface it as a first-class idea. And when it was surfaced, it turned out to already have a name — just in a different field.

## What This Says About the VD

The VD's job is to take the implicit structure of a theory and make it explicit. Most of the time this means naming things that physicists do without thinking: the interacting-forces-set, the activation-condition, the paired-particle. These are all concepts that every physicist uses but no textbook defines.

Mechanical-composition is another one — but it's special because it connects to a concept that *was* defined, just in computer science rather than physics. The VD didn't invent composition. It discovered that composition was already there, hiding inside the relationship between particles and their force-producing mechanisms, waiting for someone to name it.

That's the kind of thing that makes a formalism feel like it's finding real structure rather than imposing artificial structure. When you name something and discover the name already exists in another field — because the structure you found is the same structure someone else found independently — that's evidence that you're carving at the joints.
