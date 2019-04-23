---
title: Extract Aggregates which are Likely to Change
permalink: /docs/ar-extract-aggregates-which-are-likely-to-change/
---

## Goal
This architectural refactoring extracts all aggregates from a bounded contexts which are very likely to change 
(_likelihoodForChange_ = _OFTEN_). It is inspired one of the first papers concerning modularization and thus service decomposition
by [D. L. Parnas](https://dl.acm.org/citation.cfm?doid=361598.361623). See also the [Structural Volatility](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-4-Structural-Volatility)
coupling criteria by [ServiceCutter](https://servicecutter.github.io/).

## Preconditions
 * The selected bounded context must contain at least one aggregate on which the attribute _likelihoodForChange_ is set to _OFTEN_.
 * The context must further contain at least one other aggregate which is not likely to change (_RARELY_ or _NORMAL_)

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/extract-aggregates-likely-to-change-input.png">![Extract Aggregates which are Likely to Change Example Input](/img/extract-aggregates-likely-to-change-input.png)</a>

### Result
<a href="/img/extract-aggregates-likely-to-change-output.png">![Extract Aggregates which are Likely to Change Example Output](/img/extract-aggregates-likely-to-change-output.png)</a>
