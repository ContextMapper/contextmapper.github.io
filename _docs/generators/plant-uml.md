---
title: PlantUML Generator
permalink: /docs/plant-uml/
---

## Introduction and Motivation
The [PlantUML](http://plantuml.com/) tool allows to quickly write UML diagrams. With our PlantUML generator you can generate a UML component
diagram and class diagrams for every Bounded Context of your model. If the implemented Subdomains contain entities, the generator produces 
class diagrams for these subdomains as well. Thereby we offer a transformation from our DSL into a graphical representation of the system. 
The component diagram illustrates all Bounded Contexts and their relationships, while the class diagrams show the domain models of the 
Bounded Contexts and Subdomains if you used the [Tactic DDD Syntax](/docs/tactic-ddd/) to model them. 

## User Guide
The following section describes how you use the PlantUML generators to create the 
UML component and class diagrams of your modeled system.

### Generating plantUML Diagrams
We assume you have a CML file with your model in Eclipse (with our plugin installed). With a right-click to the CML-file you will find a **Context Mapper** context menu. With the action **PlantUML: Generate Diagrams** you generate all the plantUML diagrams for your context map:

<a href="/img/plantuml-generation-1.png">![PlantUML Generator](/img/plantuml-generation-1.png)</a>

<div class="alert alert-custom">
<strong>Note</strong> that the <strong>Context Mapper</strong> menu entry is also available within the context menu uf the CML editor. 
(right-click anywhere in the editor)
</div>

All the diagrams will be generated into the **src-gen** folder. If you have installed one of the recommended plantUML Eclipse plugins (see recommendations [here](/docs/home/)), you can directly open and view the diagrams in eclipse:

<a href="/img/plantuml-generation-2.png">![PlantUML View in Eclipse](/img/plantuml-generation-2.png)</a>

#### UML Component Diagram
The transformation will generate one component diagram for your context map, showing the bounded contexts and its relationships. The component diagram for our insurance example:

<a href="/img/plantuml-insurance-example-component-diagram.png">![PlantUML Component Diagram](/img/plantuml-insurance-example-component-diagram.png)</a>

#### UML Class Diagram
Further, the transformation generates a class diagram for every bounded context. An example from the insurance scenario:

<a href="/img/plantuml-insurance-example-class-diagram.png">![PlantUML Class Diagram](/img/plantuml-insurance-example-class-diagram.png)</a>


