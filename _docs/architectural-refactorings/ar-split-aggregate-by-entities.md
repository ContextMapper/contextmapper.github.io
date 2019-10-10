---
title: "AR-1: Split Aggregate by Entities"
permalink: /docs/ar-split-aggregate-by-entities/
---

Splits an aggregate which contains multiple entities and produces one aggregate per entity.

## Context & Rationales
On the level of entities we typically try to group attributes or [nanoentities in the terminology of ServiceCutter](https://servicecutter.github.io/) 
together, which belong to the same identity and share a common lifecycle. Thereby we aim to reduce the coupling between the entities
and increase the cohesion within the entities.

 * **See also**: Coupling criterion [Identity and Lifecycle Commonality](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-1-Identity-and-Lifecycle-Commonality)
 of [ServiceCutter](https://servicecutter.github.io/).
 
The same approach can be applied on the aggregate level. The aggregates within one bounded context shall be structured in a way which
reduces coupling between the aggregates and increases the cohesion within them.

As your bounded context develops you may face the problem that an aggregate contains entities which exhibit an unsatisfying
cohesiveness. In such a case you may want to split your aggregate into multiple aggregates in order to improve coupling and cohesion.

## Goal
This Architectural Refactoring (AR) splits an aggregate and creates one aggregate for each entity. This AR can be applied when 
the entities within an aggregate exhibit unsatisfying cohesiveness and you decide to create multiple aggregates for the single 
entities.

**Inverse AR's:**
 * [AR-6: Merge Aggregates](/docs/ar-merge-aggregates/)

## Preconditions
 * The input aggregate must contain **at least two entities**.

## Input
 * The aggregate which shall be split.
 
## Output
 * Multiple aggregates which contain one entity each.
 * All entities become **aggregate roots** within their own aggregates.

## Example
The following example illustrates how this AR can be applied. The corresponding sources can be found in our 
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings).

### Input
In this example we have an aggregate containing two entities. The AR is available on the aggregate:

<a href="/img/split-aggregate-by-entities-input.png">![Split Aggregate by Entities Example Input](/img/split-aggregate-by-entities-input.png)</a>

### Result
The resulting bounded context contains two aggregates, one for each entity:

<a href="/img/split-aggregate-by-entities-output.png">![Split Aggregate by Entities Example Output](/img/split-aggregate-by-entities-output.png)</a>

## Example Sources
 * You can find the CML sources for this AR example 
   [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings/AR-1-Split-Aggregate-by-Entities).
