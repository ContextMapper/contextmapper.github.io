---
title: Welcome
permalink: /docs/home/
redirect_from: /docs/index.html
---

Context Mapper is a modular and extensible modeling framework for **Domain-driven Design (DDD)** and its strategic patterns.
The **[core component](/docs/language-reference/)** provides a DSL to create context maps featuring these DDD patterns. The model behind the language and its semantic rules express 
**our interpretation of the DDD patterns** and how these patterns can be combined in a concise and consistent manner. Context Mapper comes as a Visual Studio Code extension or as a standalone Java [library version](/docs/library/):

## Installation

**Visual Studio Code Marketplace: [Context Mapper](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension)**
 * Also available in the [Open VSX Registry](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension).
 * The Eclipse plugin is discontinued (last version: 6.12.0); see [Eclipse Plugin](/docs/eclipse/).

## Framework Architecture

![Context Mapper Framework Components](/img/context-mapper-framework-components.png)

DDD and its Bounded Contexts provide an approach for **decomposing a domain**. **[Architectural Refactorings (ARs)](/docs/architectural-refactorings)** support to decompose a Context Map in an 
iterative manner.

If you work on a project with an existing monolithic or (micro-)service-oriented architecture, you can use our 
**[reverse engineering library](/docs/reverse-engineering)** to recreate a CML context map from the existing code ([architecture recovery](https://en.wikipedia.org/wiki/Software_architecture_recovery)). This library is built in an extensible fashion, allowing the implementation different bounded context and context map discovery strategies. At present, Spring Boot applications and Docker compose files can be analyzed by existing strategies. 

The provided model transformations and **[generators](/docs/generators)** allow transforming the CML context maps into other representations of the architectural model. We 
currently offer the following generators:

 * Graphical Context Map [generator](/docs/context-map-generator/) based on Graphviz (supported formats: .png, .cvg., .dot), 
 * [PlantUML](http://plantuml.com/) component and class diagram [generator](/docs/plant-uml/)
 * [Microservice Domain-Specific Language (MDSL)](https://microservice-api-patterns.github.io/MDSL-Specification/) (micro-)service contracts [generator](/docs/mdsl/)
 * [Generic Textual Generator based on Freemarker Templates](/docs/generic-freemarker-generator/)

**Find out [how to start using Context Mapper](/docs/getting-started/) right now.**
