---
title: "Frequently Asked Questions"
permalink: /docs/faq/
---

### Where do I find FAQs and tipps specific to the Eclipse plugin or the VS Code extension?
Questions and answers specific to different IDE plugin/extensions are documented on the following pages:

 * [Eclipse](/docs/eclipse/)
 * [Visual Studio Code](/docs/vs-code/)

### I read about a feature on the Context Mapper website but could not find it in the Visual Studio Code extension. Why?
We have only recently published Context Mapper for Visual Studio Code and do not support all features yet. You can find a feature support table [here](/docs/ide/). If you need all Context Mapper features, you have to use our Eclipse plugin for now. However, we continuously enhance our VS Code extension and want to support all features soon!

### How do I create a new Context Map?
Just create a file with the file extension **.cml** (Context Mapping Language). Take a look at our example to get an idea how the file content should look like: [https://github.com/ContextMapper/context-mapper-examples](https://github.com/ContextMapper/context-mapper-examples). Let the code completion and other editor features in Eclipse guide you while completing the map and modeling Bounded Contexts.

### Which DDD Patterns are supported by CML?
Have a look at our [CML Reference - Introduction](/docs/language-reference/) page. You will find all patterns supported by CML there.

### Which combinations of Strategic DDD Patterns are allowed? 
Have a look at the page [Language Semantic Model](/docs/language-model/). It introduces the semantic model of our DSL and lists the implemented semantic checkers.

### Where do I find a documentation regarding the tactic DDD syntax to specify a Bounded Context in detail?
The tactic DDD part of our DSL is based on the [Sculptor DSL](http://sculptorgenerator.org/). We provide a short introduction and examples how you can detail your bounded contexts on the pages [Aggregate](/docs/aggregate/) and [Tactic DDD Syntax](/docs/tactic-ddd/). If you are interested in more details and all features, we refer to the [Sculptor documentation](http://sculptorgenerator.org/documentation/advanced-tutorial).

### Which transformations can I apply to my CML model? Which generators are available?
Currently you can generate [Microservice Domain-Specific Language (MDSL)](https://microservice-api-patterns.github.io/MDSL-Specification/) (micro-)service contracts providing assistance regarding how your system can be implemented in an (micro-)service-oriented architecture, [Service Cutter](http://servicecutter.github.io/) input  to get suggestions for service cuts or new bounded context, and you can generate UML ([PlantUML](http://plantuml.com/)) diagrams out of your CML. The following pages explain the generators in detail:

 * [Generate graphical Context Maps](/docs/context-map-generator/)
 * [Generate PlantUML diagrams](/docs/plant-uml/)
 * [Generate MDSL (micro-)service contracts](/docs/mdsl/)
 * [Generate Service Cutter input files](/docs/service-cutter/)
 * [Generate arbitrary text files](/docs/generic-freemarker-generator/) (with Freemarker templates)

### How can I refactor my CML model?
The Context Mapper tool provides a set of [architectural refactorings](https://stefan.kapferer.ch/2019/09/05/service-decomposition-as-a-series-of-architectural-refactorings/) which you can apply to your model. Find more information and all
available refactorings [here](/docs/architectural-refactorings).

### Does Context Mapper support Event Sourcing and CQRS?
The concepts behind event sourcing and CQRS do not require special modeling objects other than _DomainEvents_, which are supported by the Context Mapper DSL (CML). The syntax to specify the domain models within Bounded Contexts is based on [Sculptor](http://sculptorgenerator.org/) which supports event-driven concepts. 
Have a look at our [Event Sourcing and CQRS Modeling in Context Mapper](/docs/event-sourcing-and-cqrs-modeling/) tutorial to learn how to model events in CML.  

### Can I use Context Mapper to document Event Stormings?
Yes, the results of an Event Storming are based on the DDD concepts that are supported by Context Mapper. Our 
[Model Event Storming Results in Context Mapper](/docs/event-storming/) tutorial explains how Context Mapper can be used to 
document an Event Storming.

### I have other questions not listed here. How can I contribute?
If you have any questions not answered by our documentation page, we appreciate if you create an issue in our documentation [repo](https://github.com/ContextMapper/contextmapper.github.io/issues). Of course, Pull Requests (PRs) are always welcome too.

Active [contributions](/getting-involved/) are welcome as well!
