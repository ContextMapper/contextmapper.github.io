---
title: "AR-7: Merge Bounded Contexts"
permalink: /docs/ar-merge-bounded-contexts/
---

Merges two bounded contexts together. The result is one bounded context containing all the aggregates of the two input bounded
contexts.

## Context & Rationales
By decomposing a system into multiple bounded contexts we aim for loose coupling between the bounded context and a high cohesion 
within them. However, sometimes a decomposition may be too fine-granular and merging bounded contexts with a high
coupling together improves the cohesion within the corresponding resulting bounded context.

## Goal
This Architectural Refactoring (AR) merges two bounded contexts together. The resulting bounded context contains all aggregates
of the two input bounded contexts. It can be applied if two bounded context are tightly coupled and the aggregates somehow
belong together. This may improve the cohesion within the resulting bounded context.

**Notes:**
 * By applying this AR multiple times you may end with one single Bounded Context and an empty Context Map (no relationships).

**Inverse AR's:**
 * [AR-4: Extract Aggregates by Volatility](/docs/ar-extract-aggregates-by-volatility/)
 * [AR-5: Extract Aggregates by Cohesion](/docs/ar-extract-aggregates-by-cohesion/)
 * [AR-2: Split Bounded Context by Use Cases](/docs/ar-split-bounded-context-by-use-cases/) (may need multiple merges to completely revert)
 * [AR-3: Split Bounded Context by Owner](/docs/ar-split-bounded-context-by-owners/) (may need multiple merges to completely revert)
 
## Preconditions
 * Your model needs **at least two bounded contexts** to merge.

## Input
 * Two bounded contexts.
 
## Output
 * One bounded context containing all aggregates of the two input bounded contexts.
 
## Example
The following example illustrates how this AR can be applied. The corresponding sources can be found in our 
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
The following model contains two bounded contexts with one aggregate each. Therefore the AR is available on both bounded contexts:

<a href="/img/merge-bounded-contexts-input.png">![Merge Bounded Contexts Example Input](/img/merge-bounded-contexts-input.png)</a>

### Selection Dialog
After triggering this refactoring, a dialog pops up on which you can choose with which other bounded context you want to merge:

<a href="/img/merge-bounded-contexts-dialog.png">![Merge Bounded Contexts Example Dialog](/img/merge-bounded-contexts-dialog.png)</a>

### Result
The resulting model contains one bounded context with both aggregates of the selected bounded contexts:

<a href="/img/merge-bounded-contexts-output.png">![Merge Bounded Contexts Example Output](/img/merge-bounded-contexts-output.png)</a>

## Example Sources
 * You can find the CML sources for this AR example 
   [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings/AR-7-Merge-Bounded-Contexts).
