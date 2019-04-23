---
title: Split Aggregate by Entities
permalink: /docs/ar-split-aggregate-by-entities/
---

## Goal
Splits an aggregate by its entities and creates one aggregate per entity. Each entity becomes the _aggregate root_ of the corresponding 
aggregate.

## Preconditions
 * The selected aggregate must at least contain **two entities**.

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/split-aggregate-by-entities-input.png">![Split Aggregate by Entities Example Input](/img/split-aggregate-by-entities-input.png)</a>

### Result
<a href="/img/split-aggregate-by-entities-output.png">![Split Aggregate by Entities Example Output](/img/split-aggregate-by-entities-output.png)</a>
