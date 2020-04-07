---
title: CML Reference - Introduction
permalink: /docs/language-reference/
---

This section of the online documentation covers all supported DDD patterns and the corresponding CML language features.

## Semantic Model
The [Language Semantics](/docs/language-model/) page contains a diagram illustrating the domain model on which the CML language is based. It helps to understand the structure of 
the language and semantics (for instance, the difference between bidirectional, symmetric context relationships and directed upstream-downstream relationships). 

The [Language Model](/docs/language-model/) page further describes all implemented semantic rules in textual form.

## Strategic DDD Patterns
The following strategic DDD patterns are supported by CML. For detailed descriptions of the patterns itself we refer to Evan's 
[original DDD book ("the blue book")](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) and his free 
[DDD reference](http://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf).

The syntax and semantic rules of all the patterns are documented on their individual pages:

 * **[Context Map](/docs/context-map)**
 * **[Bounded Context](/docs/bounded-context)**
 * **[Subdomain](/docs/subdomain)** (Core, Supporting, Generic)
 * **[Domain Vision Statement](/docs/domain-vision-statement)**
 * **[Partnership](/docs/partnership)** (P)
 * **[Shared Kernel](/docs/shared-kernel)** (SK)
 * **[Customer/Supplier](/docs/customer-supplier)** (C/S)
 * **[Open Host Service](/docs/open-host-service)** (OHS)
 * **[Published Language](/docs/published-language)** (PL)
 * **[Conformist](/docs/conformist)** (CF)
 * **[Anticorruption Layer](/docs/anticorruption-layer)** (ACL)
 * **[Responsibility Layers](/docs/responsibility-layers)**
 * **[Knowledge Level](/docs/knowledge-level)**
 
## Tactic DDD Patterns
The tactic DDD part of the CML language(all grammar rules inside *Aggregates*s that is), are based on the [Sculptor DSL](https://github.com/sculptor/sculptor). 
Thus, we refer to the [Sculptor documentation](http://sculptorgenerator.org/documentation/advanced-tutorial#domain-driven-design) for details regarding the tactic DDD patterns.
 
The most important tactic DDD patterns that we use in our [transformations (for instance, plantUML generation)](/docs/generators/generators) are the following:
 
 * **Module**
 * **[Aggregate](/docs/aggregate)** (and *Aggregate Root*)
 * **Entity**
 * **Service**
 * **Value Object**
 * **Domain Event**
 
The following patterns can be used in CML models as well (but currently are not processed by in any transformation): 

 * **Repository**
  
*Note:* Our Aggregate pattern implementation is different from the one in Sculptor; it does not correspond to Sculptor's implementation. 
Therefore it is documented [here](/docs/aggregate).  

## Additional Language Features
The following (not DDD specific) language features are supported by CML as well: 

 * **[User Requirements](/docs/user-requirements/)** (Use Cases and User Stories)
   * Used for the Architectural Refactoring (AR) [Split Bounded Context by Use Cases](/docs/ar-split-bounded-context-by-use-cases/) and our [Rapid OOAD](/docs/rapid-ooad/) tools.
 * **[Imports](/docs/imports/)** to include other CML files
