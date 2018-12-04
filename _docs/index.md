---
title: Welcome
permalink: /docs/home/
redirect_from: /docs/index.html
---

## Getting started
To start with Context Mapper install our Eclipse plugin by using the following update site: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/).

### System Requirements
To use the ContextMapper DSL you need the following tools:

* [Java JDK](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) (JDK 8 or newer)
* [Eclipse](https://www.eclipse.org/downloads/packages/)
* ContextMapper Eclipse Plugin (Eclipse Update Site: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/))
* We recommend to install one the following two plugins to display the plantUML diagrams directly in Eclipse:
    * [Asciidoctor Editor](https://marketplace.eclipse.org/content/asciidoctor-editor) (Update site: [https://dl.bintray.com/de-jcup/asciidoctoreditor](https://dl.bintray.com/de-jcup/asciidoctoreditor))
    * [PlantUML Eclipse Plugin](https://github.com/hallvard/plantuml) (Update site: [http://hallvard.github.io/plantuml/](http://hallvard.github.io/plantuml/))
    * **Note:** Both plugins require [Graphviz](http://www.graphviz.org/) to be installed on your machine!
    * Alternatively you can use the [plantUML online server](http://www.plantuml.com/plantuml/uml).

### CML Models
As soon as you have installed our Eclipse plugin, you can start creating context maps. Start with a new context map by creating a file with the file extension **.cml**.

Checkout our [examples repository](https://github.com/ContextMapper/context-mapper-examples) to find examples of complete context maps. One of the examples is the [DDD Sample Application](https://github.com/citerus/dddsample-core). The following CML code snippets
give you a first impression how the DSL looks like.

The context map for the [DDD Sample Application](https://github.com/citerus/dddsample-core) which is split into three bounded contexts:

<div class="highlight"><pre><span></span><span class="c">/** </span>
<span class="c"> * The DDD Cargo sample application modeled in CML. Note that we split the application into </span>
<span class="c"> * multiple bounded contexts.</span>
<span class="c"> */</span>
<span class="k">ContextMap</span> {
  <span class="k">contains</span> CargoBookingContext
  <span class="k">contains</span> VoyagePlanningContext
  <span class="k">contains</span> LocationContext

  CargoBookingContext &lt;-&gt; VoyagePlanningContext : <span class="k">Shared-Kernel</span>

  CargoBookingContext -&gt; LocationContext : <span class="k">Upstream-Downstream</span> {
    <span class="k">upstream</span> <span class="k">implements</span> <span class="k">OPEN_HOST_SERVICE</span>, <span class="k">PUBLISHED_LANGUAGE</span>
  }

  VoyagePlanningContext -&gt; LocationContext : <span class="k">Upstream-Downstream</span> {
    <span class="k">upstream</span> <span class="k">implements</span> <span class="k">OPEN_HOST_SERVICE</span>, <span class="k">PUBLISHED_LANGUAGE</span>
  }
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

Note that the DSL elements within the modules and aggregates is based on the [Sculptor DSL](https://github.com/sculptor/sculptor). You find a documentation regarding the syntax for the tactic DDD patterns [here](http://sculptorgenerator.org/documentation/).

### Domain-driven Design Patterns

#### Strategic Patterns
Find a list of all supported strategic DDD patterns [here](/docs/strategic-ddd).

#### Tactic Patterns
The implementation of the tactic DDD patterns is based on [Sculptor DSL](https://github.com/sculptor/sculptor). You can find their documentation and the supported patterns under the following link: [http://sculptorgenerator.org/documentation/](http://sculptorgenerator.org/documentation/).

### Transformations / Generators
Context Mapper provides tools to transform CML models to [ServiceCutter input](https://servicecutter.github.io/) and [plantUML diagrams](http://plantuml.com/).

#### Service Cutter Integration
Find out [here](/docs/service-cutter/) how to produce Service Cutter input to calculate possible service cuts or new bounded contexts:

![Service Cutter DDD Sample](/img/service-cutter-ddd-sample.png)

#### plantUML Diagrams
You can generate [plantUML](http://plantuml.com/) component diagrams out of CML context maps. Additionally, the transformation generates class diagrams for all bounded contexts. [Here](/docs/plant-uml/) you can find out how to generate them.

Example component diagram (DDD sample): 
<img src="/img/plantuml-ddd-sample.png" alt="DDD Sample Component Diagram" width="400px">

Example class diagram (Cargo booking context): 
<img src="/img/plantuml-cargo-booking-context.png" alt="Cargo Booking Context" width="500px">




