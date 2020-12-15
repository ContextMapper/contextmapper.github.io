---
title: Getting started
permalink: /docs/getting-started/
---

To model with Context Mapper you need either our Eclipse Plugin or our Visual Studio Code extension. Both provide support for the CML language and its surrounding tools. Please note that the VS Code extension does not support all our features yet. [Here](/docs/ide/) you can find a table that illustrates which features are available in Eclipse and VS code. The VS code extension shall support all features soon!

## VS Code Extension
To start using Context Mapper in Visual Studio code, you can simply install or download our extension via the marketplace:

**VS Code Marketplace: [Context Mapper](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension)**

Or search for "Context Mapper" in the extension view of your visual studio code.

**Note:** Does not support all features we have in Eclipse yet. You can find a feature support table [here](/docs/ide/).

## Eclipse Plugin
To start using Context Mapper in Eclipse, please install the plugin via the **Eclipse Marketplace** or our **update site**: 

**Eclipse Marketplace: [Context Mapper](https://marketplace.eclipse.org/content/context-mapper/)**
 * Alternatively you can use the following update site URL for manual installation in Eclipse: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)

## Online IDE (Gitpod)
In case your project is hosted by GitHub, you can use [Gitpod](https://www.gitpod.io/) as online IDE. Our VS Code extension is published to the [Open VSX Registry](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension) and can be found in the extensions in your [Gitpod](https://www.gitpod.io/).

**Start online IDE now**: Just try it out with our **demo repository, [right now](https://contextmapper.org/demo/)**.

## System Requirements
Besides the IDE plugin/extension, you need the following tools on your machine:

* [Java JDK](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) (JDK 8 or newer)
* If you want to use our [Context Map generator](/docs/context-map-generator/), you must have installed [Graphviz](https://www.graphviz.org/) on your system.
    * Ensure that the binaries are part of the _PATH_ environment variable and can be called from the terminal.
    * Especially on Windows this is not the case after the installation of [Graphviz](https://www.graphviz.org/). The default installation path is
      `C:\Program Files (x86)\GraphvizX.XX`, which means you have to add `C:\Program Files (x86)\GraphvizX.XX\bin` to your _PATH_ variable.
* A PlantUML viewer for the Eclipse or VS Code:
    * You may want to install one the following two plugins to display the plantUML diagrams directly in Eclipse:
      * [Asciidoctor Editor](https://marketplace.eclipse.org/content/asciidoctor-editor) (Update site: [https://dl.bintray.com/de-jcup/asciidoctoreditor](https://dl.bintray.com/de-jcup/asciidoctoreditor))
      * [PlantUML Eclipse Plugin](https://github.com/hallvard/plantuml) (Update site: [http://hallvard.github.io/plantuml/](http://hallvard.github.io/plantuml/))
      * **Note:** Both plugins also require [Graphviz](http://www.graphviz.org/) to be installed on your machine!
      * Alternatively you can use a [plantUML online server](http://www.plantuml.com/plantuml/uml).
    * In VS Code you can also find several extensions for PlantUML.
      * Just search for "PlantUML" in the extensions view of your VS code.

**Note**: If you want to integrate the DSL and its tools as library within your application, find more information [here](/docs/library/).

### Latest Releases
Release notes for all our latest releases can be found [here](https://github.com/ContextMapper/context-mapper-dsl/releases).

## Example 
The following example gives you a first impression how CML context maps look like: ([DDD Sample Application](https://github.com/citerus/dddsample-core))

<div class="highlight"><pre><span></span><span class="c">/** </span>
<span class="c"> * The DDD Cargo sample application modeled in CML. Note that we split the application into </span>
<span class="c"> * multiple bounded contexts.</span>
<span class="c"> *</span>
<span class="c"> */</span>
<span class="k">ContextMap</span> {
  <span class="k">contains</span> CargoBookingContext
  <span class="k">contains</span> VoyagePlanningContext
  <span class="k">contains</span> LocationContext
  
  CargoBookingContext [<span class="k">SK</span>]&lt;-&gt;[<span class="k">SK</span>] VoyagePlanningContext
  
  CargoBookingContext [<span class="k">D</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext

  VoyagePlanningContext [<span class="k">D</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext
}
</pre></div>

The bounded contexts have to be specified before you can use them within a context map.
A simple example of a bounded context definition is:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> LocationContext {
  <span class="k">Module</span> location {
    <span class="k">Aggregate</span> Location {
      <span class="k">Entity</span> Location {
        <span class="k">aggregateRoot</span>

        <span class="k">PortCode</span> portcode
        - <span class="k">UnLocode</span> unLocode
          <span class="k">String</span> name
      }

      <span class="k">ValueObject</span> UnLocode {
        <span class="k">String</span> unLocode
      }

      <span class="k">ValueObject</span> LocationShared {
        <span class="k">PortCode</span> portCode
        - <span class="k">Location</span> location
      }
    }
  }
}
</pre></div>

## Next steps...

### A First Model 
Once you have installed Context Mapper, you can create a CML (Xtext) project and start modeling. Find more information how to create such a project here:
 * [Create CML Project](/docs/getting-started-create-project/)
 
Check out our [example models](/docs/examples/) and the [language reference](/docs/language-reference/) if you do not want to start with an empty CML model.

### Refactorings and Generators
Once you created your first Context Map in CML you can use the following tools to evolve your model and generate other representations of your architecture:

 * Use [Architectural Refactorings (ARs)](/docs/architectural-refactorings/) to evolve your model iteratively.
 * Let [Service Cutter](/docs/service-cutter-context-map-suggestions/) analyze your model and suggest new Context Maps on the basis of its [coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).
 * Generate [graphical Context Maps](/docs/context-map-generator/)
 * Generate [PlantUML](/docs/plant-uml/) component and class diagrams
 * Generate [MDSL](/docs/mdsl) (micro-)service contracts
 * Generate [Service Cutter](/docs/service-cutter/) input files
 * Generate [arbitrary textual files with Freemarker templates](/docs/generic-freemarker-generator/)
 
### Reverse Engineer Context Map and Bounded Contexts
In case you work on a project with existing monolithic or (micro-)service-oriented architectures you may want to reverse engineer an initial Context Map or the domain models within your Bounded Contexts to simplify the start with our tool. In this case have a look at our [reverse engineering library](/docs/reverse-engineering)
which is able to generate CML models from existing source code. 
