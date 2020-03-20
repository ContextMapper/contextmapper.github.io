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

### Language Mapping

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
| String           | D&lt;string&gt;                             |
| int or Integer   | D&lt;int&gt;                                |
| long or Long     | D&lt;long&gt;                               |
| double or Double | D&lt;double&gt;                             |
| boolean          | D&lt;bool&gt;                               |
| Blob             | D&lt;raw&gt;                                |
| Date             | D&lt;string&gt; (no date available in MDSL) |

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
  String lockbox nullable
  int postalCode
  String city
}
```
MDSL data type result:
<div class="highlight"><pre><span></span><span class="k">data type</span> Address { <span class="s">&quot;street&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;, <span class="s">&quot;lockbox&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt;?, <span class="s">&quot;postalCode&quot;</span>:<span class="k">D</span>&lt;<span class="k">int</span>&gt;, <span class="s">&quot;city&quot;</span>:<span class="k">D</span>&lt;<span class="k">string</span>&gt; }
</pre></div>

All abstract data types which are not base types and not specified in CML (no references to objects) will produce an abstract, 
unspecified element in [MDSL](https://socadk.github.io/MDSL/), as the following example illustrates:
<div class="highlight"><pre><span></span><span class="k">data type</span> JustAnUnspecifiedParameterType <span class="k">P</span>
</pre></div>

### Example
An example [MDSL](https://socadk.github.io/MDSL/) API description looks as follows: 
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

**Note:** This example has been generated from our [insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example) 
which you can find in our [examples repository](https://github.com/ContextMapper/context-mapper-examples).

### MAP Pattern Decorators
The MDSL language allows modelers to specify the roles of endpoints and operations according to the MAP ([https://microservice-api-patterns.org/](https://microservice-api-patterns.org/)) 
responsibility patterns. Our generators match the corresponding pattern names in comments on Aggregates and methods. The following CML code illustrates how
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

The patterns are detected by our generator and mapped to the corresponding language features of MDSL. The following MDSL code illustrates the resulting resource
for the Aggregate specified above:

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

As illustrated above, the patterns on the resource level are added with the _serves as_ keyword and on the operation level with the _with responsibility_ keyword.
In the following we list the supported patterns:

#### Endpoint Role Patterns
 * [PROCESSING_RESOURCE](https://microservice-api-patterns.org/patterns/responsibility/endpointRoles/ProcessingResource)
 * [INFORMATION_HOLDER_RESOURCE](https://microservice-api-patterns.org/patterns/responsibility/endpointRoles/InformationHolderResource)
 * OPERATIONAL_DATA_HOLDER
 * [MASTER_DATA_HOLDER](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpoints/MasterDataHolder)
 * REFERENCE_DATA_HOLDER
 * [TRANSFER_RESOURCE](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpoints/TransferResource)
 * [LOOKUP_RESOURCE](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpoints/LookupResource)

#### Operation Role Patterns
 * [COMPUTATION_FUNCTION](https://microservice-api-patterns.org/patterns/responsibility/processingResponsibilities/ComputationFunction)
 * NOTIFICATION_OPERATION
 * [RETRIEVAL_OPERATION](https://microservice-api-patterns.org/patterns/responsibility/processingResponsibilities/RetrievalOperation)
 * STATE_TRANSITION_OPERATION
 * [EVENT_PROCESSOR](https://microservice-api-patterns.org/patterns/responsibility/processingResponsibilities/EventProcessor)
 * [BUSINESS_ACTIVITY_PROCESSOR](https://microservice-api-patterns.org/patterns/responsibility/processingResponsibilities/BusinessActivityProcessor)

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

### Protected Regions
After you generated an MDSL contract you can add protected regions for **data types**, **endpoint types**, **API providers**, and **API clients**
if you want to modify parts of the contract and protect them from being overwritten. The following example shows the corresponding comments needed to begin and
end the four different protected regions:

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

The protected regions allow you to move _data types_, _endpoints_, _API providers_, and _API clients_ into its corresponding protected
region so that they are not overwritten at re-generation. Thus, you can call the MDSL generator on the same file again and all objects
within a protected region will not be changed. 

For example, you can move a set of _data types_ into the corresponding protected region 
if you changed the data types manually after generation and want to protect them:

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
The current version of our MDSL generator is compatible with the MDSL version _1.1.0_. For further questions regarding [MDSL](https://socadk.github.io/MDSL/) please visit the website [https://socadk.github.io/MDSL](https://socadk.github.io/MDSL)
or contact Olaf Zimmermann.
