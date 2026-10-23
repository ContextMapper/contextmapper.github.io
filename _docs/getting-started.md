---
title: Getting started
permalink: /docs/getting-started/
---

To model with Context Mapper you need our extension for [Visual Studio Code](https://code.visualstudio.com/). It provides the CML editor (validation, auto-completion, quick fixes) and all our refactorings, transformations and generators.

## VS Code Extension
You can install the extension from the marketplace:

**VS Code Marketplace: [Context Mapper](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension)**

Or search for "Context Mapper" in the extensions view of VS Code. For editors that are compatible with VS Code extensions but don't use the Microsoft marketplace (such as VSCodium), the extension is available in the [Open VSX Registry](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension).

**Note:** The Eclipse plugin is discontinued; version 6.12.0 is the last one for Eclipse. Find more information [here](/docs/eclipse/).

## System Requirements
Besides the extension, you need the following tools on your machine:

* [Java](https://adoptium.net/) (JRE or JDK 17 or newer); the extension starts our language server with it.
* If you want to use our [Context Map generator](/docs/context-map-generator/), you must have installed [Graphviz](https://www.graphviz.org/) on your system.
    * Ensure that the binaries are part of the _PATH_ environment variable and can be called from the terminal.
    * Especially on Windows this is not the case after the installation of [Graphviz](https://www.graphviz.org/). The default installation path is
      `C:\Program Files (x86)\GraphvizX.XX`, which means you have to add `C:\Program Files (x86)\GraphvizX.XX\bin` to your _PATH_ variable.
* A PlantUML extension to display the generated [PlantUML](/docs/plant-uml/) diagrams directly in VS Code, for example [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml).
    * Alternatively you can use a [PlantUML online server](https://www.plantuml.com/plantuml/uml).

**Note**: If you want to integrate the DSL and its tools as library within your application, find more information [here](/docs/library/).

### Latest Releases
Release notes for all our latest releases can be found [here](https://github.com/ContextMapper/context-mapper-dsl/releases).

## Example 
The following example gives you a first impression how CML context maps look like: ([DDD Sample Application](https://github.com/citerus/dddsample-core))

```cml
/**
 * The DDD Cargo sample application modeled in CML. Note that we split the application into
 * multiple bounded contexts.
 *
 */
ContextMap {
  contains CargoBookingContext
  contains VoyagePlanningContext
  contains LocationContext

  CargoBookingContext [SK]<->[SK] VoyagePlanningContext

  CargoBookingContext [D]<-[U,OHS,PL] LocationContext

  VoyagePlanningContext [D]<-[U,OHS,PL] LocationContext
}
```

The bounded contexts have to be specified before you can use them within a context map.
A simple example of a bounded context definition is:

```cml
BoundedContext LocationContext {
  Module location {
    Aggregate Location {
      Entity Location {
        aggregateRoot

        PortCode portcode
        - UnLocode unLocode
          String name
      }

      ValueObject UnLocode {
        String unLocode
      }

      ValueObject LocationShared {
        PortCode portCode
        - Location location
      }
    }
  }
}
```

## Next steps...

### A First Model 
Once you have installed Context Mapper, you can open a folder in VS Code and start modeling. Find more information how to create your first model here:
 * [Create CML Project](/docs/getting-started-create-project/)
 
Check out our [example models](/docs/examples/) and the [language reference](/docs/language-reference/) if you do not want to start with an empty CML model.

### Refactorings and Generators
Once you created your first Context Map in CML you can use the following tools to evolve your model and generate other representations of your architecture:

 * Use [Architectural Refactorings (ARs)](/docs/architectural-refactorings/) to evolve your model iteratively.
 * Generate [graphical Context Maps](/docs/context-map-generator/)
 * Generate [PlantUML](/docs/plant-uml/) component and class diagrams
 * Generate [MDSL](/docs/mdsl) (micro-)service contracts
 * Generate [arbitrary textual files with Freemarker templates](/docs/generic-freemarker-generator/)
 
### Reverse Engineer Context Map and Bounded Contexts
In case you work on a project with existing monolithic or (micro-)service-oriented architectures you may want to reverse engineer an initial Context Map or the domain models within your Bounded Contexts to simplify the start with our tool. In this case have a look at our [reverse engineering library](/docs/reverse-engineering)
which is able to generate CML models from existing source code. 
