---
title: Welcome
permalink: /docs/home/
redirect_from: /docs/index.html
---

Context Mapper is a modular and extensible modeling framework for **Domain-driven Design (DDD)** and its strategic patterns.
The **[core component](/docs/language-reference/)** provides a DSL to create context maps featuring these DDD patterns. The model behind the language and its semantic rules express 
**our interpretation of the DDD patterns** and how these patterns can be combined in a concise and consistent manner. At present, Context Mapper comes as an Eclipse plugin, a Visual Studio Code extension, or as a standalone Java [library version](/docs/library/):

## Installation

**Visual Studio Code Marketplace: [Context Mapper](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension)**
 * Does not support all features we have in Eclipse yet. You can find a feature support table [here](/docs/ide/).

**Eclipse Marketplace: [Context Mapper](https://marketplace.eclipse.org/content/context-mapper/)**
 * Alternatively you can install the Eclipse plugin manually with the following update site URL: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)

**Online IDE (Gitpod)**: In case you don't want to install Context Mapper locally and your project is hosted on Github, you can use [Gitpod](https://www.gitpod.io/) as online IDE with our VS Code extension.
 * The extension is published to the [Open VSX Registry](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension), so you can easily find the extension in Gitpod. Installation instructions can be found [here](/docs/online-ide/).
 * Or: **Start modeling in our Context Mapper demo repository [right now](https://contextmapper.org/demo/)**.

## Framework Architecture

![Context Mapper Framework Components](/img/context-mapper-framework-components.png)

DDD and its Bounded Contexts provide an approach for **decomposing a domain**. With our **[Service Cutter](/docs/service-cutter-context-map-suggestions/)** integration 
(currently in proof-of-concept state) we illustrate how the Context Mapper DSL (CML) can be used as a foundation for even more structured service decomposition approaches. 
Based on its [coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria), Context Mapper suggests new Context Maps which may improve the 
architecture with respect to coupling and cohesion. **[Architectural Refactorings (ARs)](/docs/architectural-refactorings)** support to decompose a Context Map in an 
iterative manner.

If you work on a project with an existing monolithic or (micro-)service-oriented architecture, you can use our 
**[reverse engineering library](/docs/reverse-engineering)** to recreate a CML context map from the existing code ([architecture recovery](https://en.wikipedia.org/wiki/Software_architecture_recovery)). This library is built in an extensible fashion, allowing the implementation different bounded context and context map discovery strategies. At present, Spring Boot applications and Docker compose files can be analyzed by existing strategies. 

The provided model transformations and **[generators](/docs/generators)** allow transforming the CML context maps into other representations of the architectural model. We 
currently offer the following generators:

 * Graphical Context Map [generator](/docs/context-map-generator/) based on Graphviz (supported formats: .png, .cvg., .dot), 
 * [PlantUML](http://plantuml.com/) component and class diagram [generator](/docs/plant-uml/)
 * [Microservice Domain-Speciifc Language (MDSL)](https://microservice-api-patterns.github.io/MDSL-Specification/) (micro-)service contracts [generator](/docs/mdsl/)
 * [Service Cutter](http://servicecutter.github.io/) input files [generators](/docs/service-cutter/)
 * [Generic Textual Generator based on Freemarker Templates](/docs/generic-freemarker-generator/)

**Find out [how to start using Context Mapper](/docs/getting-started/) right now.**
