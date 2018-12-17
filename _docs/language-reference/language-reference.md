---
title: CML Reference - Introduction
permalink: /docs/language-reference/
---

Within this section, we provide a documentation of all patterns and the according CML language features.

## Semantic Model
On the [Language Semantics](/docs/language-model/) page you find a diagram illustrating the domain model on which the CML language is based.
It helps to understand the structure of the language and semantics. The [page](/docs/language-model/) further describes all implemented semantic rules in a textual form.

## Strategic DDD Patterns
The following strategic DDD patterns are supported by CML. 
For detailed descriptions of the patterns itself we refer to Evan's [book](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) 
and his [DDD reference](http://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf).

The syntax and semantic rules of all the patterns are documented on their individual pages:

 * **[Context Map](/docs/context-map)**
 * **[Bounded Context](/docs/bounded-context)**
 * **[Subdomain](/docs/subdomain)** (Core, Supporting, Generic)
 * **[Domain Vision Statement](/docs/domain-vision-statement)**
 * **[Partnership](/docs/partnership)**
 * **[Shared Kernel](/docs/shared-kernel)**
 * **[Customer/Supplier](/docs/customer-supplier)**
 * **[Conformist](/docs/conformist)**
 * **[Open Host Service](/docs/open-host-service)** (OHS)
 * **[Anticurruption Layer](/docs/anticorruption-layer)** (ACL)
 * **[Published Language](/docs/published-language)**
 * **[Responsibility Layers](/docs/responsibility-layers)**
 * **[Knowledge Level](/docs/knowledge-level)**
 
 
## Tactic DDD Patterns
The tactic DDD part of the CML language, meaning all rules inside *aggregates*, are based on the [Sculptor DSL](https://github.com/sculptor/sculptor). Thus, we refer to their [documentation](http://sculptorgenerator.org/documentation/advanced-tutorial#domain-driven-design) for details regarding the tactic DDD patterns.
 
However, the most important tactic DDD patterns we also use for our transformations (Service Cutter integration and plantUML generation) are the following:
 
 * **Module**
 * **[Aggregate](/docs/aggregate)** (and *Aggregate Root*)
 * **Entity**
 * **Value Object**
 * **Domain Event**
 
The following patterns are supported as well, but currently not used in the transformations:
 
 * **Service**
 * **Repository**
  
**Note:** The aggregate pattern implementation has been changed and no longer corresponds to Sculptors implementation. Therefore it is documented [here](/docs/aggregate). 
