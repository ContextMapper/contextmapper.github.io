---
title: Architectural Refactorings
permalink: /docs/architectural-refactorings/
image: /img/cm-og-image.png
---

Within this section, we provide a documentation of all architectural refactorings (ARs) available in the Context Mapper tool.

## Motivation: Why refactorings?
The provided refactorings offer the advantage that the result is always a correct CML model which compiles without errors. 
If you perform similar changes manually, you also have to fix upcoming errors within the [Context Map](/docs/context-map/) manually.
The AR's ensure that corresponding references and dependencies in other parts of the model are respected and adjusted if necessary.

## Refactoring Overview
The Context Mapper tool offers you a set of architectural refactorings which can be applied to your CML models. The refactorings shall
support you with evolving and improving the architecture of your system.

We currently provide the following ARs:

| Name                                                                                                    | Subject         | Description                                                                                                                                                     | Input              | Output             |
|---------------------------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|
| [**AR-1: Split Aggregate by Entities**](/docs/ar-split-aggregate-by-entities)                           | Aggregate       | Splits an aggregate which contains multiple entities and produces one aggregate per entity.                                                                     | 1 Aggregate        | n Aggregates       |
| [**AR-2: Split Bounded Context by Use Cases**<sup>1</sup>](/docs/ar-split-bounded-context-by-use-cases) | Bounded Context | Splits a bounded context by grouping those aggregates together into one bounded context which are used by the same use case(s).                                 | 1 Bounded Context  | n Bounded Contexts |
| [**AR-3: Split Bounded Context by Owner**<sup>1</sup>](/docs/ar-split-bounded-context-by-owners)        | Bounded Context | Splits a bounded context by grouping those aggregates together into one bounded context which belong to the same team.                                          | 1 Bounded Context  | n Bounded Contexts |
| [**AR-4: Extract Aggregates by Volatility**](/docs/ar-extract-aggregates-by-volatility)                 | Bounded Context | Extracts all aggregates from a bounded context by a given volatility, or likelihood for change (RARELY, NORMAL or OFTEN), and moves them to a separate context. | 1 Bounded Context  | 2 Bounded Contexts |
| [**AR-5: Extract Aggregates by Cohesion**](/docs/ar-extract-aggregates-by-cohesion)                     | Bounded Context | Extracts a set of aggregates which are chosen by certain cohesion criteria and moves them to a separate bounded context.                                        | 1 Bounded Context  | 2 Bounded Contexts |
| [**AR-6: Merge Aggregates**](/docs/ar-merge-aggregates)                                                 | Aggregate       | Merges two aggregates within a bounded context together to one aggregate.                                                                                       | 2 Aggregates       | 1 Aggregate        |
| [**AR-7: Merge Bounded Contexts**](/docs/ar-merge-bounded-contexts)                                     | Bounded Context | Merges two bounded contexts together. The result is one bounded context containing all the aggregates of the two input boundedcontexts.                         | 2 Bounded Contexts | 1 Bounded Context  |


<sup>1</sup>: An aggregate in CML can be used by **multiple** use cases and is owned by **one** owner (team).

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
