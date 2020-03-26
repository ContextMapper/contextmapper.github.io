---
title: PlantUML Generator
permalink: /docs/plant-uml/
---

## Introduction and Motivation
The [PlantUML](http://plantuml.com/) tool let you create UML diagrams quickly. You can generate UML component diagrams representing entire Context Maps and UML class diagrams for each Bounded Context in your model. If the implemented Subdomains contain Entities, the generator produces class diagrams for these Subdomains as well. We offer a transformation from our DSL into a graphical representation of the system this way. The component diagram illustrates all Bounded Contexts and their relationships, while the class diagrams show the domain models of the Bounded Contexts and Subdomains (if you used the [Tactic DDD Syntax](/docs/tactic-ddd/) to specify them). 

## User Guide
The following section describes how you use the PlantUML generators to create the UML component and class diagrams of your modeled system.

### Generating plantUML Diagrams
We assume you have a CML file with your model in Eclipse (with our plugin installed). Right-clicking on the CML-file, you will find a **Context Mapper** context menu. With the action **PlantUML: Generate Diagrams** you generate all the plantUML diagrams for your Context Map:

<a href="/img/plantuml-generation-1.png">![PlantUML Generator](/img/plantuml-generation-1.png)</a>

<div class="alert alert-custom">
<strong>Note</strong> that the <strong>Context Mapper</strong> menu entry is also available within the context menu uf the CML editor. 
(right-click anywhere in the editor)
</div>

All the diagrams will be generated into the **src-gen** folder. If you have installed one of the recommended plantUML Eclipse plugins 
(see recommendations [here](/docs/getting-started/)), you can directly open and view the diagrams in Eclipse:

<a href="/img/plantuml-generation-2.png">![PlantUML View in Eclipse](/img/plantuml-generation-2.png)</a>

#### UML Component Diagram
The transformation will generate one component diagram for your context map, showing the Bounded Contexts and its relationships. The component diagram for our insurance example is:

<a href="/img/plantuml-insurance-example-component-diagram.png">![PlantUML Component Diagram](/img/plantuml-insurance-example-component-diagram.png)</a>

#### UML Class Diagram
The transformation generates a class diagram for every bounded context as well. An example from the insurance scenario is:

<a href="/img/plantuml-insurance-example-class-diagram.png">![PlantUML Class Diagram](/img/plantuml-insurance-example-class-diagram.png)</a>

Once you have the generated `.puml` files available, you can of course not only view them in Eclipse but also process them further. For instance, they can be integrated into Markdown and [pandoc](https://pandoc.org/extras.html) nicely.


