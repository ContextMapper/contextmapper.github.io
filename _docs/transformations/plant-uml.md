---
title: plantUML Generator
permalink: /docs/plant-uml/
---

## Generating plantUML Diagrams

We assume you have a CML file with your model in Eclipse (with our plugin installed). With a right-click to the CML-file you will find a **Context Mapper** context menu. With the action **PlantUML: Generate Diagrams** you generate all the plantUML diagrams for your context map:

<a href="/img/plantuml-generation-1.png">![plantUML Generator](/img/plantuml-generation-1.png)</a>

All the diagrams will be generated into the **src-gen** folder. If you have installed one of the recommended plantUML Eclipse plugins (see recommendations [here](/docs/home/)), you can directly open and view the diagrams in eclipse:

<a href="/img/plantuml-generation-2.png">![plantUML View in Eclipse](/img/plantuml-generation-2.png)</a>

### UML Component Diagram
The transformation will generate one component diagram for your context map, showing the bounded contexts and its relationships. The component diagram for our insurance example:

<a href="/img/plantuml-insurance-example-component-diagram.png">![plantUML Component Diagram](/img/plantuml-insurance-example-component-diagram.png)</a>

### UML Class Diagram
Further, the transformation generates a class diagram for every bounded context. An example from the insurance scenario:

<a href="/img/plantuml-insurance-example-class-diagram.png">![plantUML Class Diagram](/img/plantuml-insurance-example-class-diagram.png)</a>


