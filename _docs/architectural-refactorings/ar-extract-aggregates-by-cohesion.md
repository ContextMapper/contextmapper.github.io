---
title: Extract Aggregates by Cohesion
permalink: /docs/ar-extract-aggregates-by-cohesion/
---

## Goal
This refactoring allows the user/architect to extract a set of aggregates into a new bounded context based on any non-functional
requirement criteria concerning cohesion between the bounded contexts. The refactoring allows to choose those aggregates manually 
and creates a new bounded context for the selection.

## Preconditions
 * The selected bounded context must at least contain two aggregates.

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/extract-aggregates-by-cohesion-input.png">![Extract Aggregates by Cohesion Example Input](/img/extract-aggregates-by-cohesion-input.png)</a>

### Manual Selection Dialog
Once you triggered the refactoring a dialog will pop up, allowing you to choose a name for the new bounded context and the aggregates
which should be extracted:

<a href="/img/extract-aggregates-by-cohesion-dialog.png">![Extract Aggregates by Cohesion Example Dialog](/img/extract-aggregates-by-cohesion-dialog.png)</a>

### Result
<a href="/img/extract-aggregates-by-cohesion-output.png">![Extract Aggregates by Cohesion Example Output](/img/extract-aggregates-by-cohesion-output.png)</a>
