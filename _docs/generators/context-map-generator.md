---
title: Context Map Generator
permalink: /docs/context-map-generator/
image: /img/context-mapper-example-context-map.png
---

## Introduction
Our Context Map generator produces graphical representations of Context Mapper DSL (CML) Context Maps. The visualization of the
generated Context Maps is inspired by the illustration style proposed by [Vernon](https://www.amazon.de/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577)
and [Brandolini](https://www.infoq.com/articles/ddd-contextmapping/).

## Examples
The following CML Context Map represents the DDD cargo sample application (find the complete CML file [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/ddd-sample)): 

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> DDDSampleMap {
  <span class="k">contains</span> CargoBookingContext
  <span class="k">contains</span> VoyagePlanningContext
  <span class="k">contains</span> LocationContext

  CargoBookingContext [<span class="k">SK</span>]&lt;-&gt;[<span class="k">SK</span>] VoyagePlanningContext

  CargoBookingContext [<span class="k">D</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext

  VoyagePlanningContext [<span class="k">D</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext
}
</pre></div>

Using our generator produces the following graphical Context Map for you:

<a href="/img/context-map-generator-ddd-sample.png">![DDD Cargo Sample Application Context Map](/img/context-map-generator-ddd-sample.png)</a>

As a second example, the following Context Map represents our [insurance company example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example)
(find the complete CML file [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example)):

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> InsuranceContextMap {
  <span class="k">type</span> = <span class="k">SYSTEM_LANDSCAPE</span>
  <span class="k">state</span> = <span class="k">TO_BE</span>

  <span class="c">/* Add bounded contexts to this context map: */</span>
  <span class="k">contains</span> CustomerManagementContext, CustomerSelfServiceContext, PrintingContext
  <span class="k">contains</span> PolicyManagementContext, RiskManagementContext, DebtCollection

  <span class="c">/* Define the context relationships: */</span>

  CustomerSelfServiceContext [<span class="k">D</span>,<span class="k">C</span>]&lt;-[<span class="k">U</span>,<span class="k">S</span>] CustomerManagementContext {
    <span class="k">exposedAggregates</span> = Customers
  }

  CustomerManagementContext [<span class="k">D</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] PrintingContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;SOAP&quot;</span>
    <span class="k">downstreamRights</span> = <span class="k">INFLUENCER</span>
    <span class="k">exposedAggregates</span> = Printing
  }

  PrintingContext [<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>]-&gt;[<span class="k">D</span>,<span class="k">ACL</span>] PolicyManagementContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;SOAP&quot;</span>
    <span class="k">exposedAggregates</span> = Printing
  }

  RiskManagementContext [<span class="k">P</span>]&lt;-&gt;[<span class="k">P</span>] PolicyManagementContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RabbitMQ&quot;</span>
  }

  PolicyManagementContext [<span class="k">D</span>,<span class="k">CF</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] CustomerManagementContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTfulHTTP&quot;</span>
    <span class="k">exposedAggregates</span> = Customers
  }

  DebtCollection [<span class="k">D</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] PrintingContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;SOAP&quot;</span>
    <span class="k">exposedAggregates</span> = Printing
  }

  PolicyManagementContext [<span class="k">SK</span>]&lt;-&gt;[<span class="k">SK</span>] DebtCollection {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;Shared Java Library, Communication over RESTful HTTP&quot;</span>
  }
}
</pre></div>

Our generator produces the following graphical result for the above Context Map:

<a href="/img/context-map-generator-insurance-sample.png">![Insurance Company Example Context Map](/img/context-map-generator-insurance-sample.png)</a>

## User Guide
The Context Map generator can be used within our Eclipse plugin as described below. 

### System Requirements
The generator requires [Graphviz](https://www.graphviz.org/) to be installed on your system because it uses it behind the scenes:

 * Ensure [Graphviz](https://www.graphviz.org/) is installed on your machine.
 * Verify that the binaries of the [Graphviz](https://www.graphviz.org/) installation are part of your PATH environment variable and can be called from the command line, for instance by executing `dot -V` from the command line. 
    * In Windows this is not the case after the installation of [Graphviz](https://www.graphviz.org/). The default installation path is
      `C:\Program Files (x86)\GraphvizX.XX`, which means you have to add `C:\Program Files (x86)\GraphvizX.XX\bin` to your PATH variable.

### Generating Context Maps
The generator can be called from the _Context Mapper_ context menu within the CML editor or on the corresponding CML file:

<a href="/img/context-map-generator-context-menu.png">![Context Map Generator Context Menu](/img/context-map-generator-context-menu.png)</a>

A dialog will allow you to adjust the following *parameters* before the Context Map is generated:

 * Formats which shall be exported (PNG, SVG, DOT)
 * Size of the image (you can fix the width or height of the image)
 * Spacing factor (you can increase or decrease the spacing between edges, which can help to handle overlapping labels)
 
All the diagrams will be generated into the *src-gen* folder.
