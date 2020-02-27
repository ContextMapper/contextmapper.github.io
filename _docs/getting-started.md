---
title: Getting started
permalink: /docs/getting-started/
---

To model with Context Mapper you need our Eclipse Plugin providing the CML language and its surrounding tools. The integration of CML into other IDEs
will be released in the future but is not ready yet.

## Install Context Mapper Eclipse Plugin
To start with Context Mapper install our Eclipse plugin by using the following **update site**: 

**[https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)**

### System Requirements
To use the ContextMapper DSL Eclipse plugin you need the following tools:

* [Java JDK](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) (JDK 8 or newer)
* [Eclipse](https://www.eclipse.org/downloads/packages/)
* ContextMapper Eclipse Plugin (Eclipse Update Site: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/))
* If you want to use our [Context Map generator](/docs/context-map-generator/) you need to have [Graphviz](https://www.graphviz.org/) installed on your system.
    * Ensure that the binaries are part of the _PATH_ environment variable and can be called from the terminal.
    * Especially on Windows this is not the case after the installation of [Graphviz](https://www.graphviz.org/). The default installation path is
      `C:\Program Files (x86)\GraphvizX.XX`, which means you have to add `C:\Program Files (x86)\GraphvizX.XX\bin` to your _PATH_ variable.
* You may want to install one the following two plugins to display the plantUML diagrams directly in Eclipse:
    * [Asciidoctor Editor](https://marketplace.eclipse.org/content/asciidoctor-editor) (Update site: [https://dl.bintray.com/de-jcup/asciidoctoreditor](https://dl.bintray.com/de-jcup/asciidoctoreditor))
    * [PlantUML Eclipse Plugin](https://github.com/hallvard/plantuml) (Update site: [http://hallvard.github.io/plantuml/](http://hallvard.github.io/plantuml/))
    * **Note:** Both plugins require [Graphviz](http://www.graphviz.org/) to be installed on your machine!
    * Alternatively you can use the [plantUML online server](http://www.plantuml.com/plantuml/uml).

**Note**: If you want to integrate the DSL and its tools as library within your application, find more information [here](/docs/library/).

### Latest Releases
Release notes for all our latest releases can be found [here](https://github.com/ContextMapper/context-mapper-dsl/releases).

## Next steps ...
After you installed the Context Mapper Eclipse plugin you can create a CML (Xtext) project and start modeling. Find more information how to create
such a project here:
 * [Create CML Project](/docs/getting-started-create-project/)
 
Check out our **[example models](/docs/examples/)** and the [language reference](/docs/language-reference/) to create your first CML models.

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
A simple example of a bounded context definition:

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

## Refactorings and Generators
Once you created your first Context Map in CML you can use the following tools to evolve your model and generate other representations of your architecture:

 * Use [Architectural Refactorings (ARs)](/docs/architectural-refactorings/) to evolve your model iteratively.
 * Let [Service Cutter](/docs/service-cutter-context-map-suggestions/) analyze your model and suggest new Context Maps on the basis of its [coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).
 * Generate [graphical Context Maps](/docs/context-map-generator/)
 * Generate [PlantUML](/docs/plant-uml/) component and class diagrams
 * Generate [MDSL](/docs/mdsl) (micro-)service contracts
 * Generate [Service Cutter](/docs/service-cutter/) input files
 * Generate [arbitrary textual files with Freemarker templates](/docs/generic-freemarker-generator/)
 
## Reverse Engineer Context Map and Bounded Contexts
In case you work on a project with existing monolithic or (micro-)service-oriented architectures you may want to reverse engineer an initial Context Map
or the domain models within your Bounded Contexts to simplify the start with our tool. In this case have a look at our [reverse engineering library](/docs/reverse-engineering)
which is able to generate CML models from existing source code. 
