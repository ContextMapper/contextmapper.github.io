---
title: Welcome
permalink: /docs/home/
redirect_from: /docs/index.html
---

Context Mapper is a modular and extensible modeling framework for **Domain-driven Design (DDD)** and its strategic patterns.
The **[core component](/docs/language-reference/)** provides a DSL to create context maps featuring these DDD patterns. The model behind the language and its semantic rules express **our interpretation of the DDD patterns** and how these patterns can be combined in a concise and consistent manner. At present, Context Mappers comes as an Eclipse plugin (with a standalone Java [library version](/docs/library/) also being available): <!-- pls check edits in 1st paragraph -->

**Eclipse Marketplace: [https://marketplace.eclipse.org/content/context-mapper/](https://marketplace.eclipse.org/content/context-mapper/)**

**Update Site: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)**

<a href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=5009351" class="drag" title="Drag to your running Eclipse* workspace. *Requires Eclipse Marketplace Client"><img typeof="foaf:Image" class="img-responsive" src="https://marketplace.eclipse.org/sites/all/themes/solstice/public/images/marketplace/btn-install.png" alt="Drag to your running Eclipse* workspace. *Requires Eclipse Marketplace Client" /></a>

![Context Mapper Framework Components](/img/context-mapper-framework-components.png)

DDD and its Bounded Contexts provide an approach for **decomposing a domain**. With our **[Service Cutter](/docs/service-cutter-context-map-suggestions/)** integration (currently in proof-of-concept state) we illustrate how the Context Mapper DSL (CML) can be used as a foundation for even more structured service decomposition approaches. Based on its [coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria), Context Mapper suggests new Context Maps which may improve the architecture with respect to coupling and cohesion. **[Architectural Refactorings (ARs)](/docs/architectural-refactorings)** support to decompose a Context Map in an iterative manner.

If you work on a project with an existing monolithic or (micro-)service-oriented architecture, you can use our 
**[reverse engineering library](/docs/reverse-engineering)** to recreate a CML context map from the existing code ([architecture recovery](https://en.wikipedia.org/wiki/Software_architecture_recovery)). This library is built in an extensible fashion, allowing the implementation different bounded context and context map discovery strategies. At present, Spring Boot applications and Docker compose files can be analyzed by existing strategies. 

The provided model transformations and **[generators](/docs/generators)** allow transforming the CML context maps into other representations of the architectural model. We currently offer the following generators:

 * Graphical Context Map [generator](/docs/context-map-generator/) based on Graphviz (supported formats: .png, .cvg., .dot), 
 * [PlantUML](http://plantuml.com/) component and class diagram [generator](/docs/plant-uml/)
 * [Microservice Domain-Speciifc Language (MDSL)](https://socadk.github.io/MDSL/) (micro-)service contracts [generator](/docs/mdsl/)
 * [Service Cutter](http://servicecutter.github.io/) input files [generators](/docs/service-cutter/)
 * [Generic Textual Generator based on Freemarker Templates](/docs/generic-freemarker-generator/)

**Find out [how to start using Context Mapper](/docs/getting-started/) right now.**
