---
title: Extract Aggregates by Volatility
permalink: /docs/ar-extract-aggregates-by-volatility/
---

## Goal
This architectural refactoring extracts all aggregates from a bounded contexts which have a given volatility, or _likelihood for change_ 
(RARELY, NORMAL or OFTEN). It is inspired one of the first papers concerning modularization and thus service decomposition
by [D. L. Parnas](https://dl.acm.org/citation.cfm?doid=361598.361623). See also the [Structural Volatility](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-4-Structural-Volatility)
coupling criteria by [ServiceCutter](https://servicecutter.github.io/).

## Preconditions
 * The selected bounded context must contain at least two aggregates which have a different value in the _likelihoodForChange_ attribute (RARELY, NORMAL, OFTEN).

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/extract-aggregates-by-volatility-input.png">![Extract Aggregates by Volatility Example Input](/img/extract-aggregates-by-volatility-input.png)</a>

### Selection Dialog
After triggering this refactoring, a dialog pops up on which you can choose by which volatility value you want to extract:

<a href="/img/extract-aggregates-by-volatility-dialog.png">![Merge Bounded Contexts Example Dialog](/img/extract-aggregates-by-volatility-dialog.png)</a>

### Result
<a href="/img/extract-aggregates-by-volatility-output.png">![Extract Aggregates by Volatility Example Output](/img/extract-aggregates-by-volatility-output.png)</a>
