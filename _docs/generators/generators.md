---
title: Generators Overview
permalink: /docs/generators/
---

The Context Mapper generators provide transformations to derive graphical Context Maps, [PlantUML diagrams](http://plantuml.com/), 
[Microservice Domain-Specific Langauge (MDSL)](https://socadk.github.io/MDSL/) (micro-)service contracts, and 
[Service Cutter](https://servicecutter.github.io/) input files from your CML context map. We also provide a [generic, template-based generator](/docs/generic-freemarker-generator/) based on Freemarker which allows to generate arbitrary textual files.

**Generators:**
 * [Graphical context maps](#graphical-context-maps)
 * [PlantUML diagrams](#plantuml-diagrams)
 * [MDSL (micro-)service contracts](#mdsl-micro-service-contracts)
 * [Service Cutter input files](#service-cutter-input-files)
 * [Generic, template-based textual generator (Freemarker Templating)](#generic-textual-generator-freemarker-templating)

The generator can be accessed through the Context Menu of the CML editor or with a right-click on the `*.cml` file in the project explorer. In the CML editor, you can access all generators with the keybinding Shift-Alt-G quickly.

## Graphical Context Maps
The Context Map generator allows you to transform the CML Context Map into graphical representation inspired by the illustrations of 
[Vernon](https://www.amazon.de/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577) and 
[Brandolini](https://www.infoq.com/articles/ddd-contextmapping/). You can find out how to generate them [here](/docs/context-map-generator/).

A sample Context Map produced with our generator is:
<a href="/img/context-map-generator-insurance-sample.png">![Insurance Company Example Context Map](/img/context-map-generator-insurance-sample.png)</a>

## PlantUML Diagrams
You can generate [plantUML](http://plantuml.com/) component diagrams out of CML context maps. Additionally, the transformation 
generates UML class diagrams for all bounded contexts. If the implemented subdomains contain entities, the generator produces class diagrams for these subdomains as well. [This page](/docs/plant-uml/) describes how to generate them.

Example component diagram (DDD sample): 
<img src="/img/plantuml-ddd-sample.png" alt="DDD Sample Component Diagram" width="400px">

Example class diagram (Cargo booking context): 
<img src="/img/plantuml-cargo-booking-context.png" alt="Cargo Booking Context" width="500px">

## MDSL (Micro-)Service Contracts
With our [MDSL](https://socadk.github.io/MDSL/) generator you can generate (micro-)service contracts from your Context Maps (or, more precisely, from upstream bounded contexts that expose at least one aggregate that contains at least one operation in a service or entity).
The resulting contracts illustrate how you can derive (micro-)services from strategic DDD context maps and provide 
assistance regarding how to implement your system as a (micro-)service-oriented architecture.

This is an examplary [MDSL](https://socadk.github.io/MDSL/) service contract for our 
[insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example): 

<div class="highlight"><pre><span></span><span class="c">// Generated from DDD Context Map &#39;Insurance-Example_Context-Map.cml&#39; at 21.10.2019 17:48:52 CEST.</span>
<span class="k">API description</span> CustomerManagementContextAPI
<span class="k">usage context</span> <span class="k">PUBLIC_API</span> <span class="k">for</span> <span class="k">BACKEND_INTEGRATION</span>

<span class="k">data type</span> Address { <span class="s">&quot;street&quot;</span>:<span class="k">V</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;postalCode&quot;</span>:<span class="k">V</span>&lt;<span class="k">int</span>&gt;, <span class="s">&quot;city&quot;</span>:<span class="k">V</span>&lt;<span class="k">string</span>&gt; }
<span class="k">data type</span> AddressId <span class="k">P</span>
<span class="k">data type</span> changeCustomerParameter { <span class="s">&quot;firstname&quot;</span>:<span class="k">V</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;lastname&quot;</span>:<span class="k">V</span>&lt;<span class="k">string</span>&gt; }

<span class="k">endpoint type</span> CustomersAggregate
  <span class="k">serves as</span> <span class="k">INFORMATION_HOLDER_RESOURCE</span>
  <span class="k">exposes</span>
    <span class="k">operation</span> createAddress
      <span class="k">with</span> <span class="k">responsibility</span> <span class="s">&quot;Creates new address for customer&quot;</span>
      <span class="k">expecting</span>
        <span class="k">payload</span> Address
      <span class="k">delivering</span>
        <span class="k">payload</span> AddressId
    <span class="k">operation</span> changeCustomer
      <span class="k">with</span> <span class="k">responsibility</span> <span class="s">&quot;Changes existing customer address&quot;</span>
      <span class="k">expecting</span>
        <span class="k">payload</span> changeCustomerParameter
      <span class="k">delivering</span>
        <span class="k">payload</span> V&lt;<span class="k">bool</span>&gt;

<span class="c">// Generated from DDD upstream Bounded Context &#39;CustomerManagementContext&#39; implementing OPEN_HOST_SERVICE (OHS) and PUBLISHED_LANGUAGE (PL).</span>
<span class="k">API provider</span> CustomerManagementContextProvider
  <span class="c">// The customer management context is responsible for managing all the data of the insurance companies customers.</span>
  <span class="k">offers</span> CustomersAggregate
  <span class="k">at</span> <span class="k">endpoint</span> <span class="k">location</span> <span class="s">&quot;http://localhost:8001&quot;</span>
    <span class="k">via</span> <span class="k">protocol</span> <span class="s">&quot;RESTfulHTTP&quot;</span>

<span class="c">// Generated from DDD upstream Bounded Context &#39;CustomerManagementContext&#39; implementing OPEN_HOST_SERVICE (OHS) and PUBLISHED_LANGUAGE (PL).</span>
<span class="k">API client</span> PolicyManagementContextClient
  <span class="c">// This bounded context manages the contracts and policies of the customers.</span>
  <span class="k">consumes</span> CustomersAggregate
<span class="k">API client</span> CustomerSelfServiceContextClient
  <span class="c">// This context represents a web application which allows the customer to login and change basic data records like the address.</span>
  <span class="k">consumes</span> CustomersAggregate

<span class="k">IPA</span>
</pre></div>

Learn more about the [MDSL](https://socadk.github.io/MDSL/) generator [here](/docs/mdsl/).

## Service Cutter Input Files
Find out how to produce Service Cutter input to calculate possible service cuts or new bounded contexts [here](/docs/service-cutter/):

![Service Cutter DDD Sample](/img/service-cutter-ddd-sample.png)

## Generic Textual Generator (Freemarker)
The generic, template-based generator allows you to generate arbitrary text files from CML Context Maps. It uses [Freemarker](https://freemarker.apache.org/) as its template engine and exposes the entire CML content as an object tree whose elements can be injected into the template.

Learn more about this generator [here](/docs/generic-freemarker-generator/).

<!-- TODO document new control key here? and//or on individual generator pages? -->
