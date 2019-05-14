---
title: "AR-6: Merge Aggregates"
permalink: /docs/ar-merge-aggregates/
---

Merges two aggregates within a bounded context together to one aggregate.

## Context & Rationales
On the level of entities we typically try to group attributes or [nanoentities in the terminology of ServiceCutter](https://servicecutter.github.io/) 
together, which belong to the same identity and share a common lifecycle. Thereby we aim to reduce the coupling between the entities
and increase the cohesion within the entities.

 * **See also**: Coupling criterion [Identity and Lifecycle Commonality](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-1-Identity-and-Lifecycle-Commonality)
 of [ServiceCutter](https://servicecutter.github.io/).
 
The same approach can be applied on the aggregate level. The aggregates within one bounded context shall be structured in a way which
reduces coupling between the aggregates and increases the cohesion within them.

During the evolution of your bounded context you may find multiple aggregates containing entities which belong together (for
example because they share a common lifecycle) and merging the aggregates together improves coupling and cohesion.

## Goal
This Architectural Refactoring (AR) merges two aggregates in a bounded context together into one aggregate. It can be applied
in a situation where the entities in the two aggregates somehow belong together and a merge of the aggregates improves the 
coupling and cohesion. 

**Inverse AR's:**
 * [AR-1: Split Aggregate by Entities](/docs/ar-split-aggregate-by-entities/)

## Preconditions
 * Your bounded context must contain **at least two aggregates** which can be merged.

## Input
 * Two aggregates which belong to the same bounded context.
 
## Output
 * One aggregate containing all objects (entities, value objects, etc.) of the two input aggregates.
 
## Example
The following example illustrates how this AR can be applied. The corresponding sources can be found in our 
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
The following bounded context contains two aggregates. The AR is available on both of these aggregates:

<a href="/img/merge-aggregates-input.png">![Merge Aggregates Example Input](/img/merge-aggregates-input.png)</a>

### Selection Dialog
After triggering this refactoring, a dialog pops up on which you can choose with which other aggregate you want to merge:

<a href="/img/merge-aggregates-dialog.png">![Merge Aggregates Example Dialog](/img/merge-aggregates-dialog.png)</a>

### Result
The resulting bounded context contains only one aggregate containing all entities of the previously selected aggregates:

<a href="/img/merge-aggregates-output.png">![Merge Aggregates Example Output](/img/merge-aggregates-output.png)</a>

## Example Sources
 * You can find the CML sources for this AR example 
   [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings/AR-6-Merge-Aggregates).
