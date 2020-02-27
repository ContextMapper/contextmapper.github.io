---
title: Generators Overview
permalink: /docs/generators/
---

The Context Mapper generators provide transformations to derive graphical Context Maps, [PlantUML diagrams](http://plantuml.com/), 
[MDSL](https://socadk.github.io/MDSL/) (micro-)service contracts, and [ServiceCutter input files](https://servicecutter.github.io/) from your 
CML context map. In addition we provide a [generic generator](/docs/generic-freemarker-generator/) based on Freemarker which allows to generate arbitrary textual files.

**Generators:**
 * [Graphical Context Maps](#graphical-context-maps)
 * [PlantUML Diagrams](#plantuml-diagrams)
 * [MDSL (Micro-)Service Contracts](#mdsl-micro-service-contracts)
 * [Service Cutter Input Files](#service-cutter-input-files)
 * [Generic Textual Generator (Freemarker Templating)](#generic-textual-generator-freemarker-templating)

## Graphical Context Maps
The Context Map generator allows you to transform the CML Context Map into graphical representation inspired by the illustrations of 
[Vernon](https://www.amazon.de/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577) and 
[Brandolini](https://www.infoq.com/articles/ddd-contextmapping/). [Here](/docs/context-map-generator/) you can find out how to generate them.

An example Context Map produced with our generator:
<a href="/img/context-map-generator-insurance-sample.png">![Insurance Company Example Context Map](/img/context-map-generator-insurance-sample.png)</a>

## PlantUML Diagrams
You can generate [plantUML](http://plantuml.com/) component diagrams out of CML context maps. Additionally, the transformation 
generates class diagrams for all bounded contexts. If the implemented subdomains contain entities, the generator produces class diagrams
for these subdomains as well. [Here](/docs/plant-uml/) you can find out how to generate them.

Example component diagram (DDD sample): 
<img src="/img/plantuml-ddd-sample.png" alt="DDD Sample Component Diagram" width="400px">

Example class diagram (Cargo booking context): 
<img src="/img/plantuml-cargo-booking-context.png" alt="Cargo Booking Context" width="500px">

## MDSL (Micro-)Service Contracts
With our [MDSL](https://socadk.github.io/MDSL/) generator you can generate (micro-)service contracts out of your Context Maps.
The resulting contracts illustrate how you can derive (micro-)services from strategic DDD context maps and aim for providing 
assistance regarding how your system can be implemented in an (micro-)service-oriented architecture.

This is an example [MDSL](https://socadk.github.io/MDSL/) service contract for our 
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
With the generic generator based on [Freemarker](https://freemarker.apache.org/) templates Context Mapper users are allowed to generate arbitrary text files from CML Context Maps.
Learn more about this generator [here](/docs/generic-freemarker-generator/)
