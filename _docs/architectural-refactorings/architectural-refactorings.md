---
title: Architectural Refactorings
permalink: /docs/architectural-refactorings/
---

Within this section, we provide a documentation of all architectural refactorings (ARs) available in the Context Mapper tool.

## Refactoring Overview
The Context Mapper tool offers you a set of architectural refactorings which can be applied to your CML models. The refactorings shall
support you with evolving and improving the architecture of your system.

We currently provide the following ARs:

* **[Split Aggregate by Entities](/docs/ar-split-aggregate-by-entities)**
* **[Split Bounded Context by Use Cases](/docs/ar-split-bounded-context-by-use-cases)**
* **[Split Bounded Context by Owners](/docs/ar-split-bounded-context-by-owners)**
* **[Extract Aggregates which are Likely to Change](/docs/ar-extract-aggregates-which-are-likely-to-change)**
* **[Extract Aggregates by NFR (Manual Selection)](/docs/ar-extract-aggregates-by-nfr)**
* **[Split Bounded Context by Duplicate Entity Name](/docs/ar-split-bounded-context-by-duplicate-entity-name)**
* **[Merge Bounded Contexts](/docs/ar-merge-bounded-contexts)**

## Examples
Within our [examples repository](https://github.com/ContextMapper/context-mapper-examples) you can find [input and corresponding 
output examples](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/architectural-refactorings) 
for all ARs listed above.

## How to apply Architectural Refactorings (ARs)
Architectural refactorings can be applied within the Context Mapper Eclipse plugin by using the context menu in the DSL editor. With a
right-click on a bounded context or an aggregate the **Context Mapper: Refactor** menu entry appears and lists all refactorings which are 
applicable to the selected elements:

<a href="/img/architectural-refactorings-context-menu.png">![Architectural Refactoring Context Menu Example](/img/architectural-refactorings-context-menu.png)</a>

**Note** that the context menu only shows ARs for which your selected model element fulfills the preconditions.
The preconditions for all ARs are mentioned on the corresponding detail pages linked above. 
