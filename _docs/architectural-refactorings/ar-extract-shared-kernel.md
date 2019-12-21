---
title: "AR-8: Extract Shared Kernel"
permalink: /docs/ar-extract-shared-kernel/
---

Extracts a new Bounded Context from a Shared Kernel relationship. It further established two upstream-downstream relationships
so that the existing Bounded Context can use the 'shared' functionality.

## Context & Rationales
The Shared Kernel pattern describes a close relationship between two Bounded Contexts which share a certain part of their domain
models. The pattern is typically implemented as a shared library which is maintained by both teams. However, both teams depend on
that shared code and each team has to deal with changes of the other one. If such a shared library gets very big and difficult to
maintain it may be better to create a separate Bounded Context for it. A dedicated team may maintain the model within this new 
Bounded Context.

## Goal
This Architectural Refactoring (AR) extracts a Shared Kernel into a new Bounded Context. The resulting Context Map will no
longer contain the Shared Kernel relationship, but two new upstream-downstream relationships between the new and the existing
two Bounded Contexts. This AR can be applied if a Shared Kernel gets big, difficult to maintain, and it may be better to have
a new team maintaining this shared part of the domain model in a separate Bounded Context. This may increase the autonomy of
all involved teams.   

<a href="/img/extract-shared-kernel.png">![Extract Shared Kernel Illustration](/img/extract-shared-kernel.png)</a>

## Preconditions
 * Your model needs **at least two bounded contexts** which are in a **Shared Kernel** relationship.

## Input
 * The Shared Kernel relationship.
 
## Output
 * A new Bounded Context for the shared domain model parts and two new upstream-downstream relationships between the new and the 
  existing two Bounded Contexts.
 
## Example
The following example illustrates how this AR can be applied. The corresponding sources can be found in our 
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings).

### Input
The following model contains a Shared Kernel relationship. Therefore the AR is available with a right-click on the relationship (arrow):

<a href="/img/extract-shared-kernel-input.png">![Extract Shared Kernel Example Input](/img/extract-shared-kernel-input.png)</a>

### Result
The resulting model contains an additional Bounded Context for the Shared Kernel (shared model parts) and two new upstream-downstream
relationships between the new and the existing Bounded Contexts:

<a href="/img/extract-shared-kernel-output.png">![Extract Shared Kernel Example Output](/img/extract-shared-kernel-output.png)</a>

## Example Sources
 * You can find the CML sources for this AR example 
   [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings/AR-8-Extract-Shared-Kernel).
