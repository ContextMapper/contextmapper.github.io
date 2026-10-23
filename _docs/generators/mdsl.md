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
```cml
Entity Address {
  String street
  String lockbox nullable
  int postalCode
  String city
}
```
MDSL data type result:
```mdsl
data type Address { "street":D<string>, "lockbox":D<string>?, "postalCode":D<int>, "city":D<string> }
```

All abstract data types that are not base types and not specified in CML (no references to objects) will produce an abstract, 
unspecified placeholder element `P` in [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/), as the following example illustrates:
```mdsl
data type JustAnUnspecifiedParameterType P
```

**Hint**: Find more information in our SummerSoC 2020 paper on [Domain-driven Service Design - Context Modeling, Model Refactoring and Contract Generation](/media/SummerSoC-2020_Domain-driven-Service-Design_Authors-Copy.pdf) (authors copy).

## Example
An exemplary API description in [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/), generated by Context Mapper, is: 
```mdsl
// Generated from DDD Context Map 'Insurance-Example_Context-Map.cml' at 21.10.2019 17:48:52 CEST.
API description CustomerManagementContextAPI
usage context PUBLIC_API for BACKEND_INTEGRATION

data type Address { "street":D<string>, "postalCode":D<int>, "city":D<string> }
data type AddressId P
data type changeCustomerParameter { "firstname":D<string>, "lastname":D<string> }

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
        payload D<bool>

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

*Note:* This example has been generated from our [insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example), which you can find in our [examples repository](https://github.com/ContextMapper/context-mapper-examples).

## Microservice API Patterns (MAP) Decorators
The MDSL language allows modelers to specify the roles of endpoints and operations according to the endpoint- and operation-level 
[responsibility patterns in MAP](https://microservice-api-patterns.org/patterns/responsibility/). Our generators match the corresponding pattern names in comments on Aggregates and methods. The following CML code illustrates how
the MAP patterns can be added in CML. In this case we use the _Information Holder Resource_ pattern on the Aggregate level and the _Retrieval Operation_ pattern
on the method level:

```cml
BoundedContext CustomerManagementContext {

  "INFORMATION_HOLDER_RESOURCE"
  Aggregate Customers {

    Entity Customer {
      aggregateRoot

      - SocialInsuranceNumber sin
      String firstname
      String lastname
      - List<Address> addresses

      "RETRIEVAL_OPERATION"
      def @Address getAddress(AddressId addressId);
    }

    Entity Address
  }
}
``` 

The patterns are detected by our generator and mapped to the corresponding language features of MDSL. The following MDSL code illustrates the resulting resource for the Aggregate specified above:

```mdsl
data type Address { "street":D<string>, "postalCode":D<int>, "city":D<string> }
data type AddressId P

endpoint type CustomersAggregate
  serves as INFORMATION_HOLDER_RESOURCE
  exposes
    operation getAddress
      with responsibility RETRIEVAL_OPERATION
      expecting
        payload AddressId
      delivering
        payload Address
```

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
The generators can be called from the context menu of the CML editor in VS Code. A documentation how to call the generators can also be found [here](/docs/generators/#using-the-generators).

**Note:** All generator outputs will be generated into the *src-gen* folder.

## Protected Regions
After you have generated an MDSL contract, you can add protected regions for **data types**, **endpoint types**, **API providers**, and **API clients** if you want to modify parts of the contract and protect them from being overwritten. The following example shows the corresponding comments that are required to begin and end the four different protected regions:

```mdsl
// Generated from DDD Context Map 'Insurance-Example_Context-Map.cml' at 21.10.2019 17:48:52 CEST.
API description CustomerManagementContextAPI
usage context PUBLIC_API for BACKEND_INTEGRATION

// ** BEGIN PROTECTED REGION for data types

// ** END PROTECTED REGION for data types

data type Address { "street":D<string>, "postalCode":D<int>, "city":D<string> }
data type AddressId P
data type changeCustomerParameter { "firstname":D<string>, "lastname":D<string> }

// ** BEGIN PROTECTED REGION for endpoint types

// ** END PROTECTED REGION for endpoint types

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
        payload D<bool>

// ** BEGIN PROTECTED REGION for API providers

// ** END PROTECTED REGION for API providers

// Generated from DDD upstream Bounded Context 'CustomerManagementContext' implementing OPEN_HOST_SERVICE (OHS) and PUBLISHED_LANGUAGE (PL).
API provider CustomerManagementContextProvider
  // The customer management context is responsible for managing all the data of the insurance companies customers.
  offers CustomersAggregate
  at endpoint location "http://localhost:8001"
    via protocol "RESTfulHTTP"

// ** BEGIN PROTECTED REGION for API clients

// ** END PROTECTED REGION for API clients

// Generated from DDD downstream Bounded Context 'PolicyManagementContext' implementing CONFORMIST (CF).
API client PolicyManagementContextClient
  // This bounded context manages the contracts and policies of the customers.
  consumes CustomersAggregate
API client CustomerSelfServiceContextClient
  // This context represents a web application which allows the customer to login and change basic data records like the address.
  consumes CustomersAggregate

IPA
```

The protected regions allow you to guard _data types_, _endpoints_, _API providers_, and _API clients_ into so that they are not overwritten at re-generation. Thus, you can call the MDSL generator on the same file again and all objects within a protected region will still be there and remain unchanged. 

For example, you can move a set of _data types_ into the corresponding protected region if you changed the data types manually after generation and want to protect them:

```mdsl
// Generated from DDD Context Map 'Insurance-Example_Context-Map.cml' at 21.10.2019 17:48:52 CEST.
API description CustomerManagementContextAPI
usage context PUBLIC_API for BACKEND_INTEGRATION

// ** BEGIN PROTECTED REGION for data types

data type Address { "street":D<string>, "postalCode":D<int>, "city":D<string>, "manuallyChangedThisDataType":D<string> }

// ** END PROTECTED REGION for data types

data type AddressId P
data type changeCustomerParameter { "firstname":D<string>, "lastname":D<string> }

// removed the rest here to save space ...

IPA
```

## MDSL Support
The current version of our MDSL generator is compatible with the MDSL Version 5. For further questions regarding [MDSL](https://microservice-api-patterns.github.io/MDSL-Specification/), please visit its website [https://microservice-api-patterns.github.io/MDSL-Specification/](https://microservice-api-patterns.github.io/MDSL-Specification/). This is the [update site](https://microservice-api-patterns.github.io/MDSL-Specification/updates/) to install the MDSL tools plugin.
