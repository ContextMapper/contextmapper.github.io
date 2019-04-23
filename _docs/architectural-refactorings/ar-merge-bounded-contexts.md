---
title: Merge Bounded Contexts
permalink: /docs/ar-merge-bounded-contexts/
---

## Goal
This refactoring allows you to merge two bounded contexts together.

**Note:** Start the refactoring on one bounded context. A dialog will ask you for the second bounded context with which you want to merge. 

## Preconditions
 * Your model must at least contain two bounded contexts.

## Example
An example input CML file for the refactoring can be found in our [examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
<a href="/img/merge-bounded-contexts-input.png">![Merge Bounded Contexts Example Input](/img/merge-bounded-contexts-input.png)</a>

### Selection Dialog
After triggering this refactoring, a dialog pops up on which you can choose with which other bounded context you want to merge:

<a href="/img/merge-bounded-contexts-dialog.png">![Merge Bounded Contexts Example Dialog](/img/merge-bounded-contexts-dialog.png)</a>

### Result
<a href="/img/merge-bounded-contexts-output.png">![Merge Bounded Contexts Example Output](/img/merge-bounded-contexts-output.png)</a>
