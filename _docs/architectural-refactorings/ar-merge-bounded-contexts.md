---
title: "AR-7: Merge Bounded Contexts"
permalink: /docs/ar-merge-bounded-contexts/
---

Merges two bounded contexts together. The result is one bounded context containing all the aggregates of the two input bounded
contexts.

<div class="alert alert-custom">
<strong>Known limitation:</strong> Unfortunately, this AR does not work in <a href="/docs/vs-code/">VS Code</a> and <a href="/docs/online-ide/">online</a> in case the removed Bounded Context is referenced in a Context Map. This is due to <a href="https://github.com/eclipse/xtext-core/issues/1494">a bug in the Xtext framework</a>.
</div>

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
 * The AR merges all Bounded Context attributes (such as _exposed aggregates_, _implementation technology_, etc.) which are possible
   to merge. However, there are still attributes which cannot be merged (such as the _name_ or the _domain vision statement_).
    * All attributes which cannot be merged are taken from the first Bounded Context (by default) selected in the dialog 
      (see screenshot below).
    * You have to use the corresponding checkbox on the input dialog, if you want to take the attributes from the second Bounded Context.

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
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings).

### Input
The following model contains two bounded contexts with one aggregate each. Therefore the AR is available on both bounded contexts:

<a href="/img/merge-bounded-contexts-input.png">![Merge Bounded Contexts Example Input](/img/merge-bounded-contexts-input.png)</a>

### Selection Dialog
After triggering this refactoring, a dialog pops up on which you can choose with which other bounded context you want to merge:

<a href="/img/merge-bounded-contexts-dialog.png">![Merge Bounded Contexts Example Dialog](/img/merge-bounded-contexts-dialog.png)</a>

<div class="alert alert-custom">
<strong>Note:</strong> Use the checkbox "Take attributes which cannot be merged (incl. Bounded Context name) from second Bounded
Context.", if you prefer that the attributes which cannot be merged (also see hint <a href="#goal">above</a>) are taken from the 
second Bounded Context. <strong>By default, the attributes are taken from the first Bounded Context.</strong>
</div>

### Result
The resulting model contains one bounded context with both aggregates of the selected bounded contexts:

<a href="/img/merge-bounded-contexts-output.png">![Merge Bounded Contexts Example Output](/img/merge-bounded-contexts-output.png)</a>

## Example Sources
 * You can find the CML sources for this AR example 
   [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings/AR-7-Merge-Bounded-Contexts).
