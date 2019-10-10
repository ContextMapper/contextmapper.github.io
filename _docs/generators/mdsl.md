---
title: MDSL (Micro-)Service Contracts Generator
permalink: /docs/mdsl/
---

## Introduction and Motivation
The [Microservices Domain Specific Language (MDSL)](https://socadk.github.io/MDSL/) is a DSL to specify (micro-)service contracts 
and data representations realizing the API Description pattern from [Microservice API Patterns (MAP)](https://microservice-api-patterns.org/).

With our [MDSL](https://socadk.github.io/MDSL/) generator you can automatically produce (micro-)service contracts out of your strategic
DDD context map written in CML. The generator creates the contracts according to the following mapping, which reflects our proposal
how we would derive (micro-)services from models based on strategic DDD. The generator aims for providing assistance regarding how your
system can be implemented in an (micro-)service-oriented architecture.

### Generator Mapping

| CML Input                                                                                                                        | MDSL Output                                        | Description                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Upstream Bounded Contexts from upstream-downstream [relationships](/docs/context-map/#relationships)                             | Service Specification (API description)            | We create one service specification for each upstream Bounded Context of your Context Map.                                                                                                                                                                              |
| [Exposed Aggregates](/docs/context-map/#exposed-aggregates)                                                                      | Endpoint                                           | Every exposed Aggregate of your upstream Bounded Context results in one endpoint.                                                                                                                                                                                       |
| Public methods/operations of the [aggregate root entity](/docs/tactic-ddd/#entity) or of [Services](/docs/tactic-ddd/#services). | Operation                                          | Your exposed Aggregates should contain methods/operations, either on the [aggregate root entity](/docs/tactic-ddd/#entity) or in [Services](/docs/tactic-ddd/#services). For every method/operation in those objects we generate an operation in MDSL.                  |
| Parameters & return values of methods/operations                                                                                 | Base types or data type specifications if possible | If you use primitive data types in CML, they are mapped to the base types of MDSL. If you refer to objects (such as entities) in CML, we produce a corresponding parameter tree. Types which are not further declared are mapped to abstract, unspecified elements (P). |
| Upstream Bounded Contexts from upstream-downstream [relationships](/docs/context-map/#relationships)                             | API provider                                       | For the upstream Bounded Context we also generate an API provider.                                                                                                                                                                                                      |
| Downstream Bounded Contexts from upstream-downstream [relationships](/docs/context-map/#relationships)                           | API client                                         | Downstream Bounded Contexts are mapped to corresponding API clients.                                                                                                                                                                                                    |

### Data Type Mapping
The base/primitive types are mapped as follows:

| CML type         | MDSL type                                   |
|------------------|---------------------------------------------|
| String           | V&lt;string&gt;                             |
| int or Integer   | V&lt;int&gt;                                |
| long or Long     | V&lt;long&gt;                               |
| double or Double | V&lt;double&gt;                             |
| boolean          | V&lt;bool&gt;                               |
| Blob             | V&lt;blob&gt;                               |
| Date             | V&lt;string&gt; (no date available in MDSL) |

<div class="alert alert-custom">
<strong>Note:</strong> Types in CML are case sensitive. For example: If you write "string" instead of "String", you create a new abstract
data type instead of using the primitive type "String".
</div>

If you declare a method with multiple parameters or refer to an object (such as entity or value object) in CML, we generate a corresponding
parameter tree. For example the following entity would be mapped to the parameter tree below:

CML input:
```
Entity Address {
  String street
  int postalCode
  String city
}
```
MDSL data type result:
```
data type Address { "street":V<string>, "postalCode":V<int>, "city":V<string> }
```

All abstract data types which are not base types and not specified in CML (no references to objects) will produce an abstract, 
unspecified element in [MDSL](https://socadk.github.io/MDSL/), as the following example illustrates:
```
data type JustAnUnspecifiedParameterType P
```

### Example
An example [MDSL](https://socadk.github.io/MDSL/) API description looks as follows: 
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
**Note:** This example has been generated from our [insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example) 
which you can find in our [examples repository](https://github.com/ContextMapper/context-mapper-examples).

### Known Limitations
We are aware of the following generator issues, which may lead to [MDSL](https://socadk.github.io/MDSL/) results which do not compile:
 * If you use reserved keywords of the MDSL language as _Aggregate name_, _Bounded Context name_, _operation name_ or _data type name_
   in CML, the result may not be valid MDSL.
   * Workaround: Do not use MDSL keywords within your CML model.

## User Guide
You can generate [MDSL](https://socadk.github.io/MDSL/) (micro-)service contracts from your CML model as follows.

With a right-click to your CML-file in Eclipse you will find a **Context Mapper** context menu. With the action **MDSL:
Generate Service Contracts** you generate the contracts for all upstreams in your Context Map:

<a href="/img/mdsl-generator-1.png">![MDSL Generator](/img/mdsl-generator-1.png)</a>

<div class="alert alert-custom">
<strong>Note</strong> that the <strong>Context Mapper</strong> menu entry is also available within the context menu uf the CML editor. 
(right-click anywhere in the editor)
</div>

All [MDSL](https://socadk.github.io/MDSL/) files will be generated into the **src-gen** folder of your project:

<a href="/img/mdsl-generator-2.png">![MDSL Generator Result](/img/mdsl-generator-2.png)</a>

<div class="alert alert-custom">
<strong>Note:</strong> The MDSL Eclipse plugin is not yet available for download (update site). At the moment you can open the *.mdsl 
files with a text editor only (no syntax highlighting and editor support available yet).
</div>

## MDSL Support
The current version of our MDSL generator is compatible with the MDSL version _v1.0_. For further questions regarding [MDSL](https://socadk.github.io/MDSL/) please visit the website [https://socadk.github.io/MDSL](https://socadk.github.io/MDSL)
or contact Olaf Zimmermann.
