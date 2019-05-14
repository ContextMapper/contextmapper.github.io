---
title: "AR-5: Extract Aggregates by Cohesion"
permalink: /docs/ar-extract-aggregates-by-cohesion/
---

Extracts a set of aggregates which are chosen by certain cohesion criteria and moves them to a separate bounded context.

## Context & Rationales
By decomposing a system into multiple bounded contexts we aim for loose coupling between the bounded context and a high cohesion 
within them. There are many different approaches and different coupling criteria by which the software architect may want
to decompose a system into components.

**See also:**
 * [Coupling criteria catalog](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria) of [ServiceCutter](https://servicecutter.github.io/)

## Goal
This Architectural Refactoring (AR) allows to manually select the aggregates which should be extracted by any coupling criteria
or Non-functional Requirements (NFR). The goal of this AR is to isolate a set of aggregates within a new bounded context by
an individual criterion.

**Inverse AR's:**
 * [AR-7: Merge Bounded Contexts](/docs/ar-merge-bounded-contexts/)

## Preconditions
 * The selected bounded context must contain **at least two aggregates**.

## Input
 * One bounded context.
 * A selection of aggregates which shall be extracted to a new bounded context.
 
## Output
 * A new bounded context containing the selected aggregates.
 
## Example
The following example illustrates how this AR can be applied. The corresponding sources can be found in our 
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings).

### Input
The bounded context in the example contains multiple aggregates. The AR is available on this bounded context:

<a href="/img/extract-aggregates-by-cohesion-input.png">![Extract Aggregates by Cohesion Example Input](/img/extract-aggregates-by-cohesion-input.png)</a>

### Manual Selection Dialog
Once you triggered the refactoring a dialog will pop up, allowing you to choose a name for the new bounded context and the aggregates
which should be extracted:

<a href="/img/extract-aggregates-by-cohesion-dialog.png">![Extract Aggregates by Cohesion Example Dialog](/img/extract-aggregates-by-cohesion-dialog.png)</a>

### Result
The resulting model contains a new bounded context with the selected aggregates:

<a href="/img/extract-aggregates-by-cohesion-output.png">![Extract Aggregates by Cohesion Example Output](/img/extract-aggregates-by-cohesion-output.png)</a>

## Example Sources
 * You can find the CML sources for this AR example 
   [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings/AR-5-Extract-Aggregates-by-Cohesion).
