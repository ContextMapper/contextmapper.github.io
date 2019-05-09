---
title: Merge Aggregates
permalink: /docs/ar-merge-aggregates/
---

## Goal
This refactoring allows you to merge two aggregates within a bounded context together.

**Note:** Start the refactoring on one aggregate. A dialog will ask you for the second aggregate with which you want to merge. 

## Preconditions
 * Your model must at least contain two aggregates.

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/merge-aggregates-input.png">![Merge Aggregates Example Input](/img/merge-aggregates-input.png)</a>

### Selection Dialog
After triggering this refactoring, a dialog pops up on which you can choose with which other aggregate you want to merge:

<a href="/img/merge-aggregates-dialog.png">![Merge Aggregates Example Dialog](/img/merge-aggregates-dialog.png)</a>

### Result
<a href="/img/merge-aggregates-output.png">![Merge Aggregates Example Output](/img/merge-aggregates-output.png)</a>
