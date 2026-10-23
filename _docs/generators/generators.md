---
title: Generators Overview
permalink: /docs/generators/
---

The Context Mapper generators provide transformations to derive graphical Context Maps, [PlantUML diagrams](http://plantuml.com/), and 
[Microservice Domain-Specific Langauge (MDSL)](https://microservice-api-patterns.github.io/MDSL-Specification/) (micro-)service contracts from your CML context map. We also provide a [generic, template-based generator](/docs/generic-freemarker-generator/) 
based on Freemarker which allows to generate arbitrary textual files.

**Generators:**
 * [Graphical context maps](#graphical-context-maps)
 * [PlantUML diagrams](#plantuml-diagrams)
 * [MDSL (micro-)service contracts](#mdsl-micro-service-contracts)
 * [Generic, template-based textual generator (Freemarker Templating)](#generic-textual-generator-freemarker-templating)

## Using the Generators

### Visual Studio Code
The generators are implemented as commands in VS Code. You can find them in the context menu of the CML editor:

<a href="/img/generators-in-vscode-1.png">![Generators Context Menu in VS Code](/img/generators-in-vscode-1.png)</a>

Alternatively you find them in the command palette (Ctrl+Shift+P):

<a href="/img/generators-in-vscode-2.png">![Generators in the VS Code Command Palette](/img/generators-in-vscode-2.png)</a>

### Eclipse
The generators can be accessed through the Context Menu in the project explorer (right-click to *.cml file) or directly in the CML editor as the following screenshot shows:

<a href="/img/generators-context-menu.png">![Generators Context Menu in Eclipse](/img/generators-context-menu.png)</a>

_Note_: In the CML editor, you can also access all generators with the keybinding **Shift+Alt+G** quickly.

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
With our [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/) generator you can generate (micro-)service contracts from your Context Maps (or, more precisely, from upstream bounded contexts that expose at least one aggregate that contains at least one operation in a service or entity).
The resulting contracts illustrate how you can derive (micro-)services from strategic DDD context maps and provide 
assistance regarding how to implement your system as a (micro-)service-oriented architecture.

This is an examplary [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/) service contract for our 
[insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example): 

```mdsl
// Generated from DDD Context Map 'Insurance-Example_Context-Map.cml' at 21.10.2019 17:48:52 CEST.
API description CustomerManagementContextAPI
usage context PUBLIC_API for BACKEND_INTEGRATION

data type Address { "street":V<string>, "postalCode":V<int>, "city":V<string> }
data type AddressId P
data type changeCustomerParameter { "firstname":V<string>, "lastname":V<string> }

endpoint type CustomersAggregate
  serves as INFORMATION_HOLDER_RESOURCE
  exposes
    operation createAddress
      with responsibility "Creates new address for customer"
      expecting
        payload Address
      delivering
        payload AddressId
    operation changeCustomer
      with responsibility "Changes existing customer address"
      expecting
        payload changeCustomerParameter
      delivering
        payload V<bool>

// Generated from DDD upstream Bounded Context 'CustomerManagementContext' implementing OPEN_HOST_SERVICE (OHS) and PUBLISHED_LANGUAGE (PL).
API provider CustomerManagementContextProvider
  // The customer management context is responsible for managing all the data of the insurance companies customers.
  offers CustomersAggregate
  at endpoint location "http://localhost:8001"
    via protocol "RESTfulHTTP"

// Generated from DDD upstream Bounded Context 'CustomerManagementContext' implementing OPEN_HOST_SERVICE (OHS) and PUBLISHED_LANGUAGE (PL).
API client PolicyManagementContextClient
  // This bounded context manages the contracts and policies of the customers.
  consumes CustomersAggregate
API client CustomerSelfServiceContextClient
  // This context represents a web application which allows the customer to login and change basic data records like the address.
  consumes CustomersAggregate

IPA
```

Learn more about the [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/) generator [here](/docs/mdsl/).

## Generic Textual Generator (Freemarker)
The generic, template-based generator allows you to generate arbitrary text files from CML Context Maps. It uses [Freemarker](https://freemarker.apache.org/) as its template engine and exposes the entire CML content as an object tree whose elements can be injected into the template.

Learn more about this generator [here](/docs/generic-freemarker-generator/).
