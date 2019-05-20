---
title: Welcome
permalink: /docs/home/
redirect_from: /docs/index.html
---

Context Mapper provides a DSL to create context maps based on **Domain-driven Design (DDD)** and its strategic patterns. 
The model behind the language and its semantic rules aim to formalize **our interpretation of the DDD patterns** and how they can be 
combined in a concise manner. DDD and its bounded contexts further provide an approach for **decomposing a domain** into multiple 
bounded contexts. With our **[Service Cutter](https://servicecutter.github.io/)** integration (proof-of-concept) we illustrate how 
the Context Mapper DSL (CML) can be used as a foundation for structured service decomposition approaches. 
Additionally, our context maps can be transformed into **[PlantUML](http://plantuml.com/)** models (proof-of-concept).

The Context Mapper project has been developed in a term project at [HSR](https://www.hsr.ch). You can find further background information 
and details in the project report, **["A Domain-specific Language for Service Decomposition"](https://eprints.hsr.ch/722/)**.

## Getting started
To start with Context Mapper install our Eclipse plugin by using the following update site: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/).

### System Requirements
To use the ContextMapper DSL you need the following tools:

* [Java JDK](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) (JDK 8 or newer)
* [Eclipse](https://www.eclipse.org/downloads/packages/)
* ContextMapper Eclipse Plugin (Eclipse Update Site: [https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/))
* You may want to install one the following two plugins to display the plantUML diagrams directly in Eclipse:
    * [Asciidoctor Editor](https://marketplace.eclipse.org/content/asciidoctor-editor) (Update site: [https://dl.bintray.com/de-jcup/asciidoctoreditor](https://dl.bintray.com/de-jcup/asciidoctoreditor))
    * [PlantUML Eclipse Plugin](https://github.com/hallvard/plantuml) (Update site: [http://hallvard.github.io/plantuml/](http://hallvard.github.io/plantuml/))
    * **Note:** Both plugins require [Graphviz](http://www.graphviz.org/) to be installed on your machine!
    * Alternatively you can use the [plantUML online server](http://www.plantuml.com/plantuml/uml).

### CML Models
As soon as you have installed our Eclipse plugin, you can start creating context maps. Start with a new context map by creating a file 
with the file extension **.cml** in an Eclipse project which has the Xtext nature enabled. You can find a detailed manual how you create
such a project and a CML file [here](/docs/getting-started-create-project/).

Checkout our [examples repository](https://github.com/ContextMapper/context-mapper-examples) to find examples of complete context maps. One of the examples is the [DDD Sample Application](https://github.com/citerus/dddsample-core). The following CML code snippets
give you a first impression how the DSL looks like.

The context map for the [DDD Sample Application](https://github.com/citerus/dddsample-core) which is split into three bounded contexts:

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

Checkout our [Language Reference](/docs/language-reference/) section to learn all details about the Context Mapper DSL.

Note that the DSL elements within the modules and aggregates (tactic DDD patterns) is based on the [Sculptor DSL](https://github.com/sculptor/sculptor). 
You can find a short introduction into the syntax of the aggregates [here](/docs/aggregate/). A short manual regarding the other 
tactic DDD patterns is provided on [this page](/docs/tactic-ddd/).
A complete documentation regarding the syntax for the tactic DDD patterns can be found on the [Sculptor website](http://sculptorgenerator.org/documentation/).

### Domain-driven Design Patterns

#### Strategic Patterns
Find a list of all supported strategic DDD patterns and their syntax within our DSL [here](/docs/language-reference/).

#### Tactic Patterns
The implementation of the tactic DDD patterns is based on [Sculptor DSL](https://github.com/sculptor/sculptor). 
You can find their documentation and the supported patterns under the following link: [http://sculptorgenerator.org/documentation/](http://sculptorgenerator.org/documentation/).
Our short introduction into the syntax can be found [here](/docs/tactic-ddd/).

### Architectural Refactorings (ARs)
The Context Mapper tool provides a series of architectural refactorings which allow you to improve and evolve your models iteratively.
Find more information and the documentation of all available refactorings [here](/docs/architectural-refactorings).

### Transformations / Generators
Context Mapper provides tools to transform CML models to [MDSL](https://socadk.github.io/MDSL/) (micro-)service contracts,  
[PlantUML diagrams](http://plantuml.com/) and [ServiceCutter input](https://servicecutter.github.io/).

#### MDSL (Micro-)Service Contracts
With our [MDSL](https://socadk.github.io/MDSL/) generator you can generate (micro-)service contracts out of your Context Maps.
The resulting contracts illustrate how you can derive (micro-)services from strategic DDD context maps and aim for providing 
assistance regarding how your system can be implemented in an (micro-)service-oriented architectural style.

This is an example [MDSL](https://socadk.github.io/MDSL/) service contract for our 
[insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/insurance-example): 

```
API description CustomerManagementContextAPI

data type Address { "street":V<string>, "postalCode":V<int>, "city":V<string> }
data type AddressId P
data type changeCustomerParameter { "firstname":V<string>, "lastname":V<string> }

endpoint type CustomersAggregate
  exposes
    operation createAddress
      expecting
        payload Address
      delivering
        payload AddressId
    operation changeCustomer
      expecting
        payload changeCustomerParameter

API provider CustomerManagementContextProvider
  offers CustomersAggregate
  at endpoint location "http://localhost:8001"
    via protocol "RESTful HTTP"

API client PolicyManagementContextClient
  consumes CustomersAggregate
API client CustomerSelfServiceContextClient
  consumes CustomersAggregate

IPA
```

Learn more about the [MDSL](https://socadk.github.io/MDSL/) generator [here](/docs/mdsl/).

#### plantUML Diagrams
You can generate [plantUML](http://plantuml.com/) component diagrams out of CML context maps. Additionally, the transformation 
generates class diagrams for all bounded contexts. [Here](/docs/plant-uml/) you can find out how to generate them.

Example component diagram (DDD sample): 
<img src="/img/plantuml-ddd-sample.png" alt="DDD Sample Component Diagram" width="400px">

Example class diagram (Cargo booking context): 
<img src="/img/plantuml-cargo-booking-context.png" alt="Cargo Booking Context" width="500px">

#### Service Cutter Integration
Find out [here](/docs/service-cutter/) how to produce Service Cutter input to calculate possible service cuts or new bounded contexts:

![Service Cutter DDD Sample](/img/service-cutter-ddd-sample.png)
