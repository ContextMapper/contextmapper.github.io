---
title: "AR-3: Split Bounded Context by Owner"
permalink: /docs/ar-split-bounded-context-by-owners/
---

Splits a bounded context by grouping those aggregates together into one bounded context which belong to the same team.

**Hint:** An aggregate in CML can belong to one owner/team (therefore the singular _owner_ in the AR name).

## Context & Rationales
By decomposing a system into multiple bounded contexts we aim for loose coupling between the bounded context and a high cohesion 
within them. One approach to achieve this and to decompose a system into components or (micro-) services is to split by owner (team).

**See also:**
 * Coupling criterion [Shared Owner](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-3-Shared-Owner) of [ServiceCutter](https://servicecutter.github.io/)
 * [Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)
 * ["Bounded contexts decouple PARTS. Parts are code **and teams**."](http://ntcoding.co.uk/speaking/talks/domain-driven-design-hidden-lessons-from-the-big-blue-book/craft-conf-budapest-may-2019) 
 by [Nick Tune](http://www.ntcoding.co.uk/)

In Context Mapper you can assign an aggregate the owning team. Consult our 
[aggregate documentation page](https://contextmapper.github.io/docs/aggregate/#aggregate-owner) to see
how this can be modeled in CML.

## Goal
This Architectural Refactoring (AR) splits a bounded context by the owners of the aggregates. This means, it creates bounded contexts
containing aggregates which all belong to the same team. It can be applied if your model exhibits a bounded contexts with 
aggregates which are owned by different teams.

**Inverse AR's:**
 * [AR-7: Merge Bounded Contexts](/docs/ar-merge-bounded-contexts/)

## Preconditions
  * The bounded context must contain **at least two aggregates**.
  * The aggregates must be **assigned to different teams**.

## Input
 * One bounded context.
 
## Output
 * The AR creates multiple bounded contexts. Each bounded context contains one or more aggregates which are owned by the same
 team.
 
## Example
The following example illustrates how this AR can be applied. The corresponding sources can be found in our 
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings).

### Input
The examples bounded context contains two aggregates which belong to different teams. The AR is available on the bounded context:

<a href="/img/split-bc-by-owners-input.png">![Split Bounded Context by Owners Example Input](/img/split-bc-by-owners-input.png)</a>

### Result
The resulting model contains two bounded context, one for each team:

<a href="/img/split-bc-by-owners-output.png">![Split Bounded Context by Owners Example Output](/img/split-bc-by-owners-output.png)</a>

## Example Sources
 * You can find the CML sources for this AR example 
   [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings/AR-3-Split-Bounded-Context-by-Owner).
