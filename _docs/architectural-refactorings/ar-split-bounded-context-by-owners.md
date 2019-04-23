---
title: Split Bounded Context by Owners
permalink: /docs/ar-split-bounded-context-by-owners/
---

## Goal
This refactoring splits a bounded context and groups those aggregates together which are maintained by the same team (see 
[Shared Owner](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-3-Shared-Owner) coupling criteria of 
[ServiceCutter](https://servicecutter.github.io/) and [Conway's Law](https://en.wikipedia.org/wiki/Conway%27s_law)).

## Preconditions
 * The selected bounded context must at least contain two aggregates which belong to different teams.

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/split-bc-by-owners-input.png">![Split Bounded Context by Owners Example Input](/img/split-bc-by-owners-input.png)</a>

### Result
<a href="/img/split-bc-by-owners-output.png">![Split Bounded Context by Owners Example Output](/img/split-bc-by-owners-output.png)</a>
