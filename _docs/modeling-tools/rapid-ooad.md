---
title: Rapid Object-oriented Analysis and Design
permalink: /docs/rapid-ooad/
image: /img/cm-og-image.png
---

Context Mapper offers transformation tools that support users in creating object-oriented models (that leverage DDD patterns) from use cases or user stories (functional
requirements) rapidly. 

## Modeling Process
The tools support the following process:

 - **Step 1**: Define **Use Cases** and/or **User Stories** in the Context Mapper DSL (CML)
   - The syntax documentation can be found [here](/docs/user-requirements/)
 - **Step 2**: Derive DDD **Subdomains** from the functional requirements
   - We offer a transformation that automates this step
   - Of course you can adjust and improve the generated Subdomains manually
 - **Step 3**: Derive DDD **Bounded Contexts** from the Subdomains
   - Context Mapper offers a transformation that executes this step

In the following we illustrate the process with an example (fictitious insurance example).

## Step 1: User Requirements
The Context Mapper DSL (CML) language allows you to model requirements in the form of user stories or use cases. Both approaches, either use cases or user stories, provide the same
information in CML. The following example illustrates the syntax for both variants:

```text
UserStory US1_Example {
  As an "Insurance Employee" I want to "create" a "Customer" so that "I am able to manage customer data ..."
}

UseCase UC1_Example {
  actor = "Insurance Employee"
  interactions = "create" a "Customer"
  benefit = "I am able to manage customer data ..."
}
```

In addition, it is possible to specify multiple interactions in one use case or user story:

 ```text
UserStory US1_Example {
  As an "Insurance Employee" 
    I want to "create" a "Customer"
    I want to "update" a "Customer"
    I want to "offer" a "Contract" 
  so that "I am able to manage the customers data and offer them insurance contracts."
}

UseCase UC1_Example {
  actor = "Insurance Employee"
  interactions = "create" a "Customer", "update" a "Customer", "offer" a "Contract"
  benefit = "I am able to manage the customers data and offer them insurance contracts."
}
```

## Step 2: Derive Subdomains
Once you specified your user stories and/or use cases you can select them in the CML editor and derive Subdomains automatically. The transformation can be found in Context Mappers
refactoring context menu:

<a target="_blank" href="/img/derive-subdomain-from-ur-1.png">![Derive Subdomain from User Requirements (Context Menu)](/img/derive-subdomain-from-ur-1.png)</a>
 
A dialog allows you then to choose your domain (declare the domain first) and define the name of the subdomain that shall be created:

*Note:* It is also possible to select an already existing Subdomain. In this case the transformation will only re-create the elements inside the Subdomain which do not already exist.
Thereby you can update a Subdomain with new user stories or use cases iteratively without loosing your manual changes. 

<a target="_blank" href="/img/derive-subdomain-from-ur-2.png">![Derive Subdomain from User Requirements (Domain Definition Dialog)](/img/derive-subdomain-from-ur-2.png)</a>

If we use the example user story above and apply the transformation, we get the following Subdomain:

```text
Domain InsuranceDomain {
  Subdomain CustomerDomain {
    domainVisionStatement "Aims at promoting the following benefit for a Insurance Employee: I am able to manage the customers data and offer them insurance contracts."
    Entity Customer
    Entity Contract
    Service US1_ExampleService {
      createCustomer;
      updateCustomer;
      offerContract;
    }
  }
}
```

The resulting Subdomains contain the entities and services including simple service operations. After the generation of the Subdomain one can detail and improve it manually.

## Step 3: Derive Bounded Contexts
Another transformation allows users to generate Bounded Context definitions from existing Subdomains in CML. You can simple select one or multiple Subdomains and apply 
the _Derive Bounded Context from Subdomains_ transformation that can be found in the refactoring context menu:

<a target="_blank" href="/img/derive-bc-from-subdomain-1.png">![Derive Bounded Context from Subdomains (Context Menu)](/img/derive-bc-from-subdomain-1.png)</a>

Note that the transformation always creates one Bounded Context for all selected Subdomains.  

Using the example Subdomain above, the transformation generates the following Bounded Context:

```text
BoundedContext NewContextFromSubdomains implements CustomerDomain {
  domainVisionStatement "This Bounded Context realizes the following subdomains: CustomerDomain"
  /* This Aggregate contains the entities and services of the 'CustomerDomain' subdomain.
   * TODO: You can now refactor the Aggregate, for example by using the 'Split Aggregate by Entities' architectural refactoring.
   * TODO: Add attributes and operations to the entities.
   * TODO: Add operations to the services.
   * Find examples and further instructions on our website: https://contextmapper.org/docs/rapid-ooad/ */
  Aggregate CustomerDomainAggregate {
    Service US1_ExampleService {
      CreateCustomerOutput createCustomer (CreateCustomerInput input);
      UpdateCustomerOutput updateCustomer (UpdateCustomerInput input);
      OfferContractOutput offerContract (OfferContractInput input);
    }
    Entity Customer {
      CustomerID customerId
    }
    Entity Contract {
      ContractID contractId
    }
  }
}
```

The generated Bounded Context implements the previously selected Subdomains and initially contains an Aggregate per Subdomain that includes all entities and services of those 
Subdomains. The entities are enriched with identify attributes and the services operations get a generic return type and parameter. As the _TODO_ comments indicate, a user can
now refactor the resulting Aggregate (for example by using [Split Aggregate by Entities](/docs/ar-split-aggregate-by-entities/)), and add further details such as attributes (entities)
and operations (entities/services).

## Whats’s Next?
Once you derived your initial Bounded Contexts, you can:

 - Add more details to the domain models (attributes, operations, services, repositories, etc.)
   - [Here](/docs/tactic-ddd/) you can find a quick introduction into the tactic DDD syntax (based on [Sculptor](http://sculptorgenerator.org/)).
 - Refine and refactor them by using our [Architectural Refactorings](/docs/architectural-refactorings/).
 - Define a [Context Map](/docs/context-map/) that specifies the relationships between your Bounded Contexts.
 - [Generate](/docs/generators/) output and other representations of you CML model:
   - [Graphical Context Map](/docs/context-map-generator/)
   - [PlantUML diagrams](/docs/plant-uml/)
   - [MDSL (micro-)service contracts](/docs/mdsl/)
   - [Service Cutter input files](/docs/service-cutter/)
   - [Generic output with Freemarker templates](/docs/generic-freemarker-generator/)
