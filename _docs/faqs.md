---
title: FAQs
permalink: /docs/faq/
---

Frequently asked questions:

### Where can I download the Eclipse Plugin?
Use the following Eclipse Update Site and install the plugin in Eclipse via *Help -> Install New Software...* (copy past the update site link)

Update Site: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)

### How do I create an Eclipse project with a new CML model to start modeling my Context Map?
Consult the page [Create CML Model](/docs/getting-started-create-project/) which describes how you setup your project to get started with modeling CML
Context Maps.

### How do I create a new context map?
Just create a file with the file extension **cml** (Context Mapping Language). Take a look at our example to get an idea how it looks like: [https://github.com/ContextMapper/context-mapper-examples](https://github.com/ContextMapper/context-mapper-examples)

### Which DDD Patterns are supported by CML?
Have a look at our [CML Reference - Introduction](/docs/language-reference/) page. There you will find all patterns supported by CML.

### Which combinations of Strategic DDD Patterns are allowed? 
Have a look at the page [Language Semantic Model](/docs/language-model/) which introduces the semantic model of our DSL and lists the implemented semantic checkers.

### Which transformations can I apply to my CML model?
Currently you can generate [MDSL](https://socadk.github.io/MDSL/) (micro-)service contracts providing assistance regarding how your
system can be implemented in an (micro-)service-oriented architecture, [Service Cutter](http://servicecutter.github.io/) input 
to get suggestions for service cuts or new bounded context, and you can generate UML ([PlantUML](http://plantuml.com/)) diagrams 
out of your CML. The following pages explain the generators in detail:

 * [Generate graphical Context Maps](/docs/context-map-generator/)
 * [Generate PlantUML Diagrams](/docs/plant-uml/)
 * [Generate MDSL (Micro-)Service Contracts](/docs/mdsl/)
 * [Generate Service Cutter Input Files](/docs/service-cutter/)

### How can I refactor my CML model?
The Context Mapper tool provides a set of architectural refactorings which you can apply to your model. Find more information and all
available refactorings [here](/docs/architectural-refactorings).

### Where do I find a documentation regarding the tactic DDD syntax to specify a bounded context in detail?
The tactic DDD part of our DSL is based on the [Sculptor DSL](http://sculptorgenerator.org/). However, you can find a short introduction
and examples how you can detail your bounded contexts on the pages [Aggregate](/docs/aggregate/) and [Tactic DDD Syntax](/docs/tactic-ddd/).
If you are interested in more details and all features, we refer to the [Sculptor documentation](http://sculptorgenerator.org/documentation/advanced-tutorial).

### I have other questions not listed here. How can I contribute?
If you have any questions not answered by our documentation page, we are happy if you create an issue in our documentation [repo](https://github.com/ContextMapper/contextmapper.github.io/issues). Of course, PR's are always welcome as well.

### How do I validate all CML models (*.cml files) in my Eclipse project?
The CML models are validated when you save the *.cml automatically, if _"Build Automatically"_ is enabled in the _Project_ menu.
If it is not enabled you can validate all models by triggering _"Build All"_ in the _Project_ menu. 

Your [contribution](/getting-involved/) is welcome!

