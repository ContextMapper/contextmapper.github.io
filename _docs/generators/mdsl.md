---
title: MDSL (Micro-)Service Contracts Generator
permalink: /docs/mdsl/
---

## Introduction and Motivation
The [Microservices Domain Specific Language (MDSL)](https://microservice-api-patterns.github.io/MDSL-Specification/) is a [Domain-Specific Language (DSL)](https://en.wikipedia.org/wiki/Domain-specific_language) to specify (micro-)service contracts and data representations, jointly realizing the technical part of the [API Description](https://microservice-api-patterns.org/patterns/foundation/APIDescription) pattern from [Microservice API Patterns (MAP)](https://microservice-api-patterns.org/). MDSL, in turn, has [generator tools](https://microservice-api-patterns.github.io/MDSL-Specification/tools) for Open API, gRPC, GraphQL, Jolie, and plain Java.

Our [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/) generator automatically produces (micro-)service contracts out of strategic DDD context maps written in CML. The generator creates the contracts according to the following mapping, which reflects our proposal
how we would derive (micro-)services from models based on strategic DDD. The generator aims at providing assistance regarding how your system can be implemented as a (micro-)service-oriented architecture.

## Language Mapping

| CML Input                                                                                                                        | MDSL Output                                        | Description                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Upstream Bounded Contexts from upstream-downstream [relationships](/docs/context-map/#relationships)                             | Service Specification (API description)            | We create one service specification for each upstream Bounded Context of your Context Map.                                                                                                                                                                              |
| [Exposed Aggregates](/docs/context-map/#exposed-aggregates)                                                                      | Endpoint                                           | Every exposed Aggregate of your upstream Bounded Context results in one endpoint.                                                                                                                                                                                       |
| [Application layer](/docs/application-and-process-layer)                                                                         | Endpoint, Flow                                           | In case you model an application layer, we generate an additional endpoint for it. The endpoint contains the operations of the application services and/or commands. *Update:* CML flows are mapped to MDSL flows as well; they must not contain any operations.                                                                                                   |
| Public methods/operations of the [aggregate root entity](/docs/tactic-ddd/#entity) or of [Services](/docs/tactic-ddd/#services). | Operation                                          | Your exposed Aggregates should contain methods/operations, either on the [aggregate root entity](/docs/tactic-ddd/#entity) or in [Services](/docs/tactic-ddd/#services). For every method/operation in those objects we generate an operation in MDSL.                  |
| Parameters & return values of methods/operations                                                                                 | Base types or data type specifications if possible | If you use primitive data types in CML, they are mapped to the base types of MDSL. If you refer to objects (such as entities) in CML, we produce a corresponding parameter tree. Types which are not further declared are mapped to abstract, unspecified elements (P). |
| Upstream Bounded Contexts from upstream-downstream [relationships](/docs/context-map/#relationships)                             | API provider                                       | For the upstream Bounded Context we also generate an API provider.                                                                                                                                                                                                      |
| Downstream Bounded Contexts from upstream-downstream [relationships](/docs/context-map/#relationships)                           | API client                                         | Downstream Bounded Contexts are mapped to corresponding API clients.                                                                                                                                                                                                    |

### Data Type Mapping
The base/primitive types are mapped to [Atomic Parameters](https://microservice-api-patterns.org/patterns/structure/representationElements/AtomicParameter) as this:

| CML type         | MDSL type                                   |
|------------------|---------------------------------------------|
| String           | D&lt;string&gt;                             |
| int or Integer   | D&lt;int&gt;                                |
| long or Long     | D&lt;long&gt;                               |
| double or Double | D&lt;double&gt;                             |
| boolean          | D&lt;bool&gt;                               |
| Blob             | D&lt;raw&gt;                                |
| Date             | D&lt;string&gt; (no date available in MDSL) |

<div class="alert alert-custom">
<strong>Note:</strong> Types in CML are case-sensitive. For example: If you write "string" instead of "String", you create a new abstract data type instead of using the primitive type "String".
</div>

If you declare a method with multiple parameters or refer to an object (such as Entity or Value Object) in CML, we generate a corresponding [Parameter Tree](https://microservice-api-patterns.org/patterns/structure/representationElements/ParameterTree). For example the following entity would be mapped to the (rather flat) parameter tree below:

CML input:
```
Entity Address {
  String street
  String lockbox nullable
  int postalCode
  String city
}
```
MDSL data type result:
<div class="highlight"><pre><span></span><span class="k">data type</span> Address { <span class="s">&quot;street&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;lockbox&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;?, <span class="s">&quot;postalCode&quot;</span>:<span class="k">D</span>&lt;<span class="k">int</span>&gt;, <span class="s">&quot;city&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }
</pre></div>

All abstract data types that are not base types and not specified in CML (no references to objects) will produce an abstract, 
unspecified placeholder element `P` in [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/), as the following example illustrates:
<div class="highlight"><pre><span></span><span class="k">data type</span> JustAnUnspecifiedParameterType <span class="k">P</span>
</pre></div>

**Hint**: Find more information in our SummerSoC 2020 paper on [Domain-driven Service Design - Context Modeling, Model Refactoring and Contract Generation](/media/SummerSoC-2020_Domain-driven-Service-Design_Authors-Copy.pdf) (authors copy).

## Example
An exemplary API description in [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/), generated by Context Mapper, is: 
<div class="highlight"><pre><span></span><span class="c">// Generated from DDD Context Map &#39;Insurance-Example_Context-Map.cml&#39; at 21.10.2019 17:48:52 CEST.</span>
<span class="k">API description</span> CustomerManagementContextAPI
<span class="k">usage context</span> <span class="k">PUBLIC_API</span> <span class="k">for</span> <span class="k">BACKEND_INTEGRATION</span>

<span class="k">data type</span> Address { <span class="s">&quot;street&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;postalCode&quot;</span>:<span class="k">D</span>&lt;<span class="k">int</span>&gt;, <span class="s">&quot;city&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }
<span class="k">data type</span> AddressId <span class="k">P</span>
<span class="k">data type</span> changeCustomerParameter { <span class="s">&quot;firstname&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;lastname&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }

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
        <span class="k">payload</span> D&lt;<span class="k">bool</span>&gt;

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

*Note:* This example has been generated from our [insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example), which you can find in our [examples repository](https://github.com/ContextMapper/context-mapper-examples).

## Microservice API Patterns (MAP) Decorators
The MDSL language allows modelers to specify the roles of endpoints and operations according to the endpoint- and operation-level 
[responsibility patterns in MAP](https://microservice-api-patterns.org/patterns/responsibility/). Our generators match the corresponding pattern names in comments on Aggregates and methods. The following CML code illustrates how
the MAP patterns can be added in CML. In this case we use the _Information Holder Resource_ pattern on the Aggregate level and the _Retrieval Operation_ pattern
on the method level:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerManagementContext {

  <span class="s">&quot;INFORMATION_HOLDER_RESOURCE&quot;</span>
  <span class="k">Aggregate</span> Customers {

    <span class="k">Entity</span> Customer {
      <span class="k">aggregateRoot</span>

      - <span class="k">SocialInsuranceNumber</span> sin
      <span class="k">String</span> firstname
      <span class="k">String</span> lastname
      - <span class="k">List</span>&lt;Address&gt; addresses

      <span class="s">&quot;RETRIEVAL_OPERATION&quot;</span>
      <span class="k">def</span> @Address getAddress(AddressId addressId);
    }

    <span class="k">Entity</span> Address
  }
}
</pre></div> 

The patterns are detected by our generator and mapped to the corresponding language features of MDSL. The following MDSL code illustrates the resulting resource for the Aggregate specified above:

<div class="highlight"><pre><span></span><span class="k">data type</span> Address { <span class="s">&quot;street&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;postalCode&quot;</span>:<span class="k">D</span>&lt;<span class="k">int</span>&gt;, <span class="s">&quot;city&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }
<span class="k">data type</span> AddressId <span class="k">P</span>

<span class="k">endpoint type</span> CustomersAggregate
  <span class="k">serves as</span> <span class="k">INFORMATION_HOLDER_RESOURCE</span>
  <span class="k">exposes</span>
    <span class="k">operation</span> getAddress
      <span class="k">with</span> <span class="k">responsibility</span> <span class="k">RETRIEVAL_OPERATION</span>
      <span class="k">expecting</span>
        <span class="k">payload</span> AddressId
      <span class="k">delivering</span>
        <span class="k">payload</span> Address
</pre></div>

As illustrated above, the patterns on the endpoint/resource level are added with the _serves as_ keyword and on the operation level with the _with responsibility_ keyword. In the following we list the supported patterns:

### Endpoint Role Patterns
 * [PROCESSING_RESOURCE](https://microservice-api-patterns.org/patterns/responsibility/endpointRoles/ProcessingResource)
 * [INFORMATION_HOLDER_RESOURCE](https://microservice-api-patterns.org/patterns/responsibility/endpointRoles/InformationHolderResource)
 * [OPERATIONAL_DATA_HOLDER](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpoints/OperationalDataHolder)
 * [MASTER_DATA_HOLDER](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpoints/MasterDataHolder)
 * [REFERENCE_DATA_HOLDER](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpoints/ReferenceDataHolder)
 * [DATA_TRANSFER_RESOURCE](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpointTypes/DataTransferResource)
 * [LINK_LOOKUP_RESOURCE](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpointTypes/LinkLookupResource)

#### Operation Responsibility Patterns
 * [COMPUTATION_FUNCTION](https://microservice-api-patterns.org/patterns/responsibility/operationResponsibilities/ComputationFunction)
 * [STATE_CREATION_OPERATION](https://microservice-api-patterns.org/patterns/responsibility/operationResponsibilities/StateCreationOperation)
 * [RETRIEVAL_OPERATION](https://microservice-api-patterns.org/patterns/responsibility/operationResponsibilities/RetrievalOperation)
 * [STATE_TRANSITION_OPERATION](https://microservice-api-patterns.org/patterns/responsibility/operationResponsibilities/StateTransitionOperation)

Please refer to the pattern texts on the MAP website for explanations of these decorators.

## Generating the MDSL Contracts
The generators can be called from the context menus of the CML editors in VS Code or Eclipse. A documentation how to call the generators can also be found [here](/docs/generators/#using-the-generators).

**Note:** All generator outputs will be generated into the *src-gen* folder.

## Protected Regions
After you have generated an MDSL contract, you can add protected regions for **data types**, **endpoint types**, **API providers**, and **API clients** if you want to modify parts of the contract and protect them from being overwritten. The following example shows the corresponding comments that are required to begin and end the four different protected regions:

<div class="highlight"><pre><span></span><span class="c">// Generated from DDD Context Map &#39;Insurance-Example_Context-Map.cml&#39; at 21.10.2019 17:48:52 CEST.</span>
<span class="k">API description</span> CustomerManagementContextAPI
<span class="k">usage context</span> <span class="k">PUBLIC_API</span> <span class="k">for</span> <span class="k">BACKEND_INTEGRATION</span>

<span class="c">// ** BEGIN PROTECTED REGION for data types</span>

<span class="c">// ** END PROTECTED REGION for data types</span>

<span class="k">data type</span> Address { <span class="s">&quot;street&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;postalCode&quot;</span>:<span class="k">D</span>&lt;<span class="k">int</span>&gt;, <span class="s">&quot;city&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }
<span class="k">data type</span> AddressId <span class="k">P</span>
<span class="k">data type</span> changeCustomerParameter { <span class="s">&quot;firstname&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;lastname&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }

<span class="c">// ** BEGIN PROTECTED REGION for endpoint types</span>

<span class="c">// ** END PROTECTED REGION for endpoint types</span>

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
        <span class="k">payload</span> <span class="k">D</span>&lt;<span class="k">bool</span>&gt;

<span class="c">// ** BEGIN PROTECTED REGION for API providers</span>

<span class="c">// ** END PROTECTED REGION for API providers</span>

<span class="c">// Generated from DDD upstream Bounded Context &#39;CustomerManagementContext&#39; implementing OPEN_HOST_SERVICE (OHS) and PUBLISHED_LANGUAGE (PL).</span>
<span class="k">API provider</span> CustomerManagementContextProvider
  <span class="c">// The customer management context is responsible for managing all the data of the insurance companies customers.</span>
  <span class="k">offers</span> CustomersAggregate
  <span class="k">at</span> <span class="k">endpoint</span> <span class="k">location</span> <span class="s">&quot;http://localhost:8001&quot;</span>
    <span class="k">via</span> <span class="k">protocol</span> <span class="s">&quot;RESTfulHTTP&quot;</span>

<span class="c">// ** BEGIN PROTECTED REGION for API clients</span>

<span class="c">// ** END PROTECTED REGION for API clients</span>

<span class="c">// Generated from DDD downstream Bounded Context &#39;PolicyManagementContext&#39; implementing CONFORMIST (CF).</span>
<span class="k">API client</span> PolicyManagementContextClient
  <span class="c">// This bounded context manages the contracts and policies of the customers.</span>
  <span class="k">consumes</span> CustomersAggregate
<span class="k">API client</span> CustomerSelfServiceContextClient
  <span class="c">// This context represents a web application which allows the customer to login and change basic data records like the address.</span>
  <span class="k">consumes</span> CustomersAggregate

<span class="k">IPA</span>
</pre></div>

The protected regions allow you to guard _data types_, _endpoints_, _API providers_, and _API clients_ into so that they are not overwritten at re-generation. Thus, you can call the MDSL generator on the same file again and all objects within a protected region will still be there and remain unchanged. 

For example, you can move a set of _data types_ into the corresponding protected region if you changed the data types manually after generation and want to protect them:

<div class="highlight"><pre><span></span><span class="c">// Generated from DDD Context Map &#39;Insurance-Example_Context-Map.cml&#39; at 21.10.2019 17:48:52 CEST.</span>
<span class="k">API description</span> CustomerManagementContextAPI
<span class="k">usage context</span> <span class="k">PUBLIC_API</span> <span class="k">for</span> <span class="k">BACKEND_INTEGRATION</span>

<span class="c">// ** BEGIN PROTECTED REGION for data types</span>

<span class="k">data type</span> Address { <span class="s">&quot;street&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;postalCode&quot;</span>:<span class="k">D</span>&lt;<span class="k">int</span>&gt;, <span class="s">&quot;city&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;manuallyChangedThisDataType&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }

<span class="c">// ** END PROTECTED REGION for data types</span>

<span class="k">data type</span> AddressId <span class="k">P</span>
<span class="k">data type</span> changeCustomerParameter { <span class="s">&quot;firstname&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;lastname&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }

<span class="c">// removed the rest here to save space ...</span>

<span class="k">IPA</span>
</pre></div>

## MDSL Support
The current version of our MDSL generator is compatible with the MDSL Version 5. For further questions regarding [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/), please visit its website [https://microservice-api-patterns.github.io/MDSL-Specification/](https://microservice-api-patterns.github.io/MDSL-Specification/). This is the [update site](https://microservice-api-patterns.github.io/MDSL-Specification/updates/) to install the MDSL tools plugin.
