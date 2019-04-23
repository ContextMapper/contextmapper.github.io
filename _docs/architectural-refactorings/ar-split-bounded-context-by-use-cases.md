---
title: Split Bounded Context by Use Cases
permalink: /docs/ar-split-bounded-context-by-use-cases/
---

## Goal
Splits a bounded context by grouping those aggregates together which are used by the same use cases. Partitioning services by use cases can
be a strategy which decreases coupling (see [Semantic Proximity](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-2-Semantic-Proximity) 
coupling criteria of [ServiceCutter](https://servicecutter.github.io/)).

## Preconditions
 * The selected bounded context must contain at least two aggregates which have different use cases assigned.

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/split-bc-by-use-cases-input.png">![Split Bounded Context by Use Cases Example Input](/img/split-bc-by-use-cases-input.png)</a>

### Result
<a href="/img/split-bc-by-use-cases-output.png">![Split Bounded Context by Use Cases Example Output](/img/split-bc-by-use-cases-output.png)</a>

