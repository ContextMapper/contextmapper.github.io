---
title: Welcome
permalink: /docs/home/
redirect_from: /docs/index.html
---

Context Mapper is a modular and extensible modeling framework based on **Domain-driven Design (DDD)** and its strategic patterns.
The **[core component](/docs/language-reference/)** provides a DSL to create context maps based on these DDD patterns. The model behind the language and its semantic rules aim 
to formalize **our interpretation of the DDD patterns** and how they can be combined in a concise manner. 

**Eclipse Update Site: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)**

![Context Mapper Framework Components](/img/context-mapper-framework-components.png)

DDD and its bounded contexts further provide an approach for **decomposing a domain** into multiple 
bounded contexts. With our **[Service Cutter](/docs/service-cutter-context-map-suggestions/)** integration (proof-of-concept) we illustrate how 
the Context Mapper DSL (CML) can be used as a foundation for structured service decomposition approaches. Based on its [coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria)
the Context Mapper tool suggests new Context Maps which may improve the architecture with respect to coupling and cohesion.
The **[Architectural Refactorings (ARs)](/docs/architectural-refactorings)** support to decompose a Context Map in an iterative manner. 

If you work on a project with an existing monolithic or (micro-)service-oriented architecture, you can initially use our 
**[reverse engineering library](/docs/reverse-engineering)** to generate a CML context map out of existing code. The library is built in an extensible fashion
and allows to implement different bounded context and context map discovery strategies.

The provided **[generators](/docs/generators)** allow to transform the CML context maps into other representations of the architectural model. We currently
offer the following generators:
 * [MDSL](https://socadk.github.io/MDSL/) (micro-)service contracts [generator](/docs/mdsl/)
 * [PlantUML](http://plantuml.com/) component and class diagram [generator](/docs/plant-uml/)
 * [Service Cutter](http://servicecutter.github.io/) input files [generators](/docs/service-cutter/)

**Find out [how to start using Context Mapper](/docs/getting-started) right now.**
