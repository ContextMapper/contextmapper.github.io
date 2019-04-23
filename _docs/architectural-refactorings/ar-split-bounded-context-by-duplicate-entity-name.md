---
title: Split Bounded Context by Duplicate Entity Name
permalink: /docs/ar-split-bounded-context-by-duplicate-entity-name/
---

## Goal
As your bounded contexts develop you may find yourself in the situation that you have two terms with different meanings within 
the ubiquitous language of your bounded context, which should not be the case. This refactoring splits a bounded context if you 
have to aggregates which contains two such entities with the same name. The refactoring is inspired by [Brandolini](https://www.infoq.com/articles/ddd-contextmapping)
(Example 1: "Same term, different meaning").

## Preconditions
 * The selected bounded context must contain two aggregates which both contain an entity with the same name.

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/split-bc-by-duplicate-entity-name-input.png">![Split Bounded Context by Duplicate Entity Name Example Input](/img/split-bc-by-duplicate-entity-name-input.png)</a>

### Result
<a href="/img/split-bc-by-duplicate-entity-name-output.png">![Split Bounded Context by Duplicate Entity Name Example Output](/img/split-bc-by-duplicate-entity-name-output.png)</a>
