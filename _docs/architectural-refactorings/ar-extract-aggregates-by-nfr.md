---
title: Extract Aggregates by NFR (Manual Selection)
permalink: /docs/ar-extract-aggregates-by-nfr/
---

## Goal
This refactoring allows the user/architect to extract a set of aggregates into a new bounded context based on any non-functional
requirement criteria. The refactoring allows to choose those aggregates manually and creates a new bounded context for the selection.

## Preconditions
 * The selected bounded context must at least contain two aggregates.

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/extract-aggregates-by-nfr-input.png">![Extract Aggregates by NFR Example Input](/img/extract-aggregates-by-nfr-input.png)</a>

### Manual Selection Dialog
Once you triggered the refactoring a dialog will pop up, allowing you to choose a name for the new bounded context and the aggregates
which should be extracted:

<a href="/img/extract-aggregates-by-nfr-dialog.png">![Extract Aggregates by NFR Example Dialog](/img/extract-aggregates-by-nfr-dialog.png)</a>

### Result
<a href="/img/extract-aggregates-by-nfr-output.png">![Extract Aggregates by NFR Example Output](/img/extract-aggregates-by-nfr-output.png)</a>
