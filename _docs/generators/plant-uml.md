---
title: PlantUML Generator
permalink: /docs/plant-uml/
---

## Introduction and Motivation
The [PlantUML](http://plantuml.com/) tool let you create UML diagrams quickly. You can generate UML component diagrams representing entire Context Maps and UML class diagrams for each Bounded Context in your model. If the implemented Subdomains contain Entities, the generator produces class diagrams for these Subdomains as well. We offer a transformation from our DSL into a graphical representation of the system this way. The component diagram illustrates all Bounded Contexts and their relationships, while the class diagrams show the domain models of the Bounded Contexts and Subdomains (if you used the [Tactic DDD Syntax](/docs/tactic-ddd/) to specify them). 

## UML Component Diagram
The generator creates a component diagram for your Context Map, showing the Bounded Contexts and its relationships. For example, the component diagram for our insurance scenario (example model) looks like this:

<a href="/img/plantuml-insurance-example-component-diagram.png">![PlantUML Component Diagram](/img/plantuml-insurance-example-component-diagram.png)</a>

## UML Class Diagram
The generator also creates class diagrams for every bounded context and subdomain. An example from the insurance scenario is:

<a href="/img/plantuml-insurance-example-class-diagram.png">![PlantUML Class Diagram](/img/plantuml-insurance-example-class-diagram.png)</a>

Once you generated the `.puml` files, you can of course not only view them in Eclipse or VS Code but also process them further. For instance, they can be integrated into Markdown and [pandoc](https://pandoc.org/extras.html) nicely.

## Generating the PlantUML Diagrams
The generators can be called from the context menus of the CML editors in VS Code or Eclipse. A documentation how to call the generators can also be found [here](/docs/generators/#using-the-generators).

**Note:** All generator outputs will be generated into the *src-gen* folder.
