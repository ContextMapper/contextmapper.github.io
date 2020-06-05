---
title: Rapid Object-oriented Analysis and Design
permalink: /docs/rapid-ooad/
image: /img/cm-og-image.png
---

Context Mapper offers transformation tools that support users in creating object-oriented [domain models](https://martinfowler.com/eaaCatalog/domainModel.html) 
(that leverage DDD patterns) from use cases or user stories (functional requirements) rapidly. 

## Modeling Process
The transformations support the following process:

 - **Step 1**: Capture User Requirements as **Use Cases** and/or **User Stories** in the Context Mapper DSL (CML)
   - This is a manual step.
   - The syntax documentation can be found [here](/docs/user-requirements/).
 - **Step 2**: Derive DDD **Subdomains** from the functional requirements
   - We offer a transformation that automates this step.
   - Of course you can adjust and improve the generated Subdomains manually.
 - **Step 3**: Derive DDD **Bounded Contexts** (type [FEATURE](/docs/bounded-context/#bounded-context-type)) from the Subdomains
   - Context Mapper offers a transformation that executes this step.
   - The generated Bounded Contexts represent features or applications. Have a look at our [Bounded Context types](/docs/bounded-context/#bounded-context-type) to understand how we distinguish 
        between _features_, _applications_, _systems_, and _teams_.
   - The generated model elements contain `TODO` suggestions for further elaboration.
 - **Step 4**: Derive [SYSTEMs](/docs/bounded-context/#bounded-context-type) from the [FEATUREs](/docs/bounded-context/#bounded-context-type) (optionally, if you want to model
   the application from a more physical perspective)
   - We offer transformations to model the FEATURE or APPLICATION Bounded Contexts in terms SYSTEMS in order to model the physical (deployment) perspective.
     - Find more about the different types of Bounded Contexts [here](/docs/bounded-context/#bounded-context-type).
   - The generated Bounded Context model the different systems or subsystems of one application (frontend and backend, and/or other subsystems).

<div class="alert alert-custom">
<strong>Note:</strong> Our Visual Studio Code extension only supports the steps 1, 2, and 3 for now. The transformations in step 4 are not yet supported. If you want to use them, please use our Eclipse plugin.
</div>

In the following we illustrate the process with an example (fictitious insurance example).

## Step 1: Capture User Requirements
The Context Mapper DSL (CML) language allows you to model requirements in the form of [user stories](https://www.agilealliance.org/glossary/user-stories/) or rather 
brief [use cases](https://medium.com/@warren2lynch/all-you-need-to-know-about-use-case-modeling-828756da3215). These two concepts differ in their context, goals and 
templates widely; however, CML supports the same [role-feature-reason](https://www.agilealliance.org/glossary/user-story-template/) structure for both of them at present. 
The following example illustrates the syntax for both notations:

<div class="highlight"><pre><span></span><span class="k">UserStory</span> US1_Example {
  <span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Insurance Employee&quot;</span> <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;create&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span> <span class="k">so</span> <span class="k">that</span> <span class="s">&quot;I am able to manage customer data ...&quot;</span>
}

<span class="k">UseCase</span> UC1_Example {
  <span class="k">actor</span> = <span class="s">&quot;Insurance Employee&quot;</span>
  <span class="k">interactions</span> = <span class="s">&quot;create&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>
  <span class="k">benefit</span> = <span class="s">&quot;I am able to manage customer data ...&quot;</span>
}
</pre></div>

It is also possible to specify multiple features or interactions in one use case or user story:

<div class="highlight"><pre><span></span><span class="k">UserStory</span> US1_Example {
  <span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Insurance Employee&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;create&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;update&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;offer&quot;</span> <span class="k">a</span> <span class="s">&quot;Contract&quot;</span>
  <span class="k">so</span> <span class="k">that</span> <span class="s">&quot;I am able to manage the customers data and offer them insurance contracts.&quot;</span>
}

<span class="k">UseCase</span> UC1_Example {
  <span class="k">actor</span> = <span class="s">&quot;Insurance Employee&quot;</span>
  <span class="k">interactions</span> = <span class="s">&quot;create&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>, <span class="s">&quot;update&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>, <span class="s">&quot;offer&quot;</span> <span class="k">a</span> <span class="s">&quot;Contract&quot;</span>
  <span class="k">benefit</span> = <span class="s">&quot;I am able to manage the customers data and offer them insurance contracts.&quot;</span>
}
</pre></div>

## Step 2: Derive Subdomains (with Services and Entities)
Once you have specified your user stories and/or use cases, you can select them in the CML editor and derive Subdomains that contain tentative Entities and Services automatically. 
The transformation can be found in Context Mappers refactoring context menu:

<a target="_blank" href="/img/derive-subdomain-from-ur-1.png">![Derive Subdomain from User Requirements (Context Menu)](/img/derive-subdomain-from-ur-1.png)</a>
 
A dialog then allows you to choose your domain (declare the domain first) and define the name of the subdomain that shall be created:

*Note:* It is also possible to select an already existing Subdomain. In this case the transformation will only re-create the elements inside the Subdomain that do not exist already.
You can update a Subdomain with new user stories or use cases iteratively without loosing your manual changes this way. 

<a target="_blank" href="/img/derive-subdomain-from-ur-2.png">![Derive Subdomain from User Requirements (Domain Definition Dialog)](/img/derive-subdomain-from-ur-2.png)</a>

If we use the example user story above and apply the transformation, we get the following Subdomain:

<div class="highlight"><pre><span></span><span class="k">Domain</span> InsuranceDomain {
  <span class="k">Subdomain</span> CustomerDomain {
    <span class="k">domainVisionStatement</span> <span class="s">&quot;Aims at promoting the following benefit for a Insurance Employee: I am able to manage the customers data and offer them insurance contracts.&quot;</span>
    <span class="k">Entity</span> Customer
    <span class="k">Entity</span> Contract
    <span class="k">Service</span> US1_ExampleService {
      createCustomer;
      updateCustomer;
      offerContract;
    }
  }
}
</pre></div>

The resulting Subdomains contain entities that are derived from the objects that the use case/user story works with as as well as services that represent the use case/user story; 
the interactions are transformed into draft operations. 

After the generation of the Subdomain one can detail and improve it manually; in order not to loose any manual additions when the transformation is executed multiple times, it 
makes sense to rename the element. A "rename element" refactoring can be used for this.

## Step 3: Derive Bounded Contexts
Another transformation allows you to transition from analysis to design and generate Bounded Context definitions from existing Subdomains in CML. You can simple select one or 
multiple Subdomains and select the _Derive Bounded Context from Subdomains_ option that can be found in the refactoring context menu:

<a target="_blank" href="/img/derive-bc-from-subdomain-1.png">![Derive Bounded Context from Subdomains (Context Menu)](/img/derive-bc-from-subdomain-1.png)</a>

Note that the transformation always creates one Bounded Context for all selected Subdomains.  

Using the example Subdomain above, the transformation generates the following Bounded Context:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> NewContextFromSubdomains <span class="k">implements</span> CustomerDomain {
  <span class="k">domainVisionStatement</span> <span class="s">&quot;This Bounded Context realizes the following subdomains: CustomerDomain&quot;</span>
  <span class="c">/* This Aggregate contains the entities and services of the &#39;CustomerDomain&#39; subdomain.</span>
<span class="c">   * TODO: You can now refactor the Aggregate, for example by using the &#39;Split Aggregate by Entities&#39; architectural refactoring.</span>
<span class="c">   * TODO: Add attributes and operations to the entities.</span>
<span class="c">   * TODO: Add operations to the services.</span>
<span class="c">   * Find examples and further instructions on our website: https://contextmapper.org/docs/rapid-ooad/ */</span>
  <span class="k">Aggregate</span> CustomerDomainAggregate {
    <span class="k">Service</span> US1_ExampleService {
      CreateCustomerOutput createCustomer (CreateCustomerInput input);
      UpdateCustomerOutput updateCustomer (UpdateCustomerInput input);
      OfferContractOutput offerContract (OfferContractInput input);
    }
    <span class="k">Entity</span> Customer {
      CustomerID customerId
    }
    <span class="k">Entity</span> Contract {
      ContractID contractId
    }
  }
}
</pre></div>

The generated Bounded Context implements the previously selected Subdomains and initially contains an Aggregate per Subdomain that includes all entities and services of those 
Subdomains. The entities are enriched with identify attributes, and the services operations receive a generic return type and parameter. 

As the _TODO_ comments indicate, a user can now refactor the resulting Aggregate (for example by using [Split Aggregate by Entities](/docs/ar-split-aggregate-by-entities/)), and 
add further details such as attributes (entities) and operations (entities/services).

## Step 4: Derive Systems
The Bounded Contexts generated in the step three above represent FEATUREs and/or APPLICATIONs (find more about the different types of Bounded Context [here](/docs/bounded-context/#bounded-context-type)).
If you want to model such an application or feature context from a more physical- or deployment perspective, you can now derive Bounded Contexts of the type SYSTEM from them.

### Derive Frontend and Backend Systems
We renamed the Bounded Context _NewContextFromSubdomains_ from above to _CustomerManagement_ now. As already mentioned, it represents a feature or application. On such
Bounded Context we can now apply the _Derive Frontend and Backend Systems_ transformation to model the systems/subsystems of the application:

<a target="_blank" href="/img/derive-frontend-backend-from-feature-1.png">![Derive Frontend and Backend Systems from FEATURE](/img/derive-frontend-backend-from-feature-1.png)</a>

A dialog lets you choose the names of your frontend and backend application:

<a target="_blank" href="/img/derive-frontend-backend-from-feature-2.png">![Derive Frontend and Backend Systems from FEATURE (Dialog)](/img/derive-frontend-backend-from-feature-2.png)</a>

You can further configure the [implementation technologies](/docs/bounded-context/#implementation-technology) of the contexts. In addition, you can define how the backend
and frontend context shall integrate:

 * CONFORMIST: In this case the frontend domain model conforms to the backend model.
 * ACL: If the domain model of the frontend context differs from the backend, the frontend context needs a transformation or anticorruption layer.
 
Applying the transformation as shown above generates the following Bounded Contexts and Context Map relationship:

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> {
  <span class="k">contains</span> CustomerManagementFrontend
  <span class="k">contains</span> CustomerManagementBackend

  CustomerManagementBackend [<span class="k">PL</span>] -&gt; [<span class="k">CF</span>] CustomerManagementFrontend {
    <span class="k">implementationTechnology</span> <span class="s">&quot;RESTful HTTP&quot;</span>
    <span class="k">exposedAggregates</span> CustomerManagementAggregateBackend
  }
}

<span class="k">BoundedContext</span> CustomerManagementBackend <span class="k">implements</span> CustomerManagement {
  <span class="k">domainVisionStatement</span> <span class="s">&quot;This Bounded Context realizes the following subdomains: CustomerManagement&quot;</span>
  <span class="k">type</span> <span class="k">SYSTEM</span>
  <span class="k">implementationTechnology</span> <span class="s">&quot;Sprint Boot&quot;</span>
  <span class="k">Aggregate</span> CustomerManagementAggregateBackend {
    <span class="k">Service</span> US1_ExampleService {
      CreateCustomerOutput createCustomer (CreateCustomerInput input);
      UpdateCustomerOutput updateCustomer (UpdateCustomerInput input);
      OfferContractOutput offerContract (OfferContractInput input);
    }
    <span class="k">Entity</span> CustomerBackend {
      CustomerID customerId
    }
    <span class="k">Entity</span> ContractBackend {
      ContractID contractId
    }
  }
}

<span class="k">BoundedContext</span> CustomerManagementFrontend <span class="k">implements</span> CustomerManagement {
  <span class="k">domainVisionStatement</span> <span class="s">&quot;This Bounded Context realizes the following subdomains: CustomerManagement&quot;</span>
  <span class="k">type</span> <span class="k">SYSTEM</span>
  <span class="k">implementationTechnology</span> <span class="s">&quot;Angular&quot;</span>
  <span class="k">Aggregate</span> CustomerManagementAggregateViewModel {
    <span class="k">Service</span> US1_ExampleService {
      CreateCustomerOutput createCustomer (CreateCustomerInput input);
      UpdateCustomerOutput updateCustomer (UpdateCustomerInput input);
      OfferContractOutput offerContract (OfferContractInput input);
    }
    <span class="k">Entity</span> CustomerViewModel {
      CustomerID customerId
    }
    <span class="k">Entity</span> ContractViewModel {
      ContractID contractId
    }
  }
}
</pre></div>

Now you already have an Upstream-Downstream relationship that exposes an Aggregate, which means you can generate a service contract with our
[MDSL (Micro-)Service Contracts Generator](/docs/mdsl/). Of course you can use all the other [generators](/docs/generators/) as well.

### Split System Context Into Subsystems
Having derived a frontend and backend system, you may want to split the systems into multiple subsytems. For example: your backend maybe consists of a _domain logic_ and a 
_database_ subsystem (or _tier_). We provide another model transformation to split a system into two subsystems for such a case:

<a target="_blank" href="/img/split-system-into-two-tiers-1.png">![Split System Into Two Subsystems](/img/split-system-into-two-tiers-1.png)</a>

Similar to the last transformation you can configure how the subsystems are named and how they shall integrate (see CONFORMIST vs. ACL above):

<a target="_blank" href="/img/split-system-into-two-tiers-2.png">![Split System Into Two Subsystems (Dialog)](/img/split-system-into-two-tiers-2.png)</a>

_Note:_ This transformation does not create two new Bounded Contexts. It uses the existing context for the first subsystem and creates one new Bounded Context for the second subsystem.

The transformation leads to the following result (with the configuration as shown above):

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> {
  <span class="k">contains</span> CustomerManagementFrontend
  <span class="k">contains</span> CustomerManagementDomainLogic
  <span class="k">contains</span> CustomerManagementDatabase

  CustomerManagementDomainLogic [<span class="k">PL</span>] -&gt; [<span class="k">CF</span>] CustomerManagementFrontend {
    <span class="k">implementationTechnology</span> <span class="s">&quot;RESTful HTTP&quot;</span>
    <span class="k">exposedAggregates</span> CustomerManagementAggregateBackend
  }

  CustomerManagementDatabase [<span class="k">PL</span>] -&gt; [<span class="k">CF</span>] CustomerManagementDomainLogic {
    <span class="k">implementationTechnology</span> <span class="s">&quot;JDBC&quot;</span>
  }
}

<span class="k">BoundedContext</span> CustomerManagementFrontend <span class="k">implements</span> CustomerManagement {
  <span class="k">domainVisionStatement</span> <span class="s">&quot;This Bounded Context realizes the following subdomains: CustomerManagement&quot;</span>
  <span class="k">type</span> <span class="k">SYSTEM</span>
  <span class="k">implementationTechnology</span> <span class="s">&quot;Angular&quot;</span>
  <span class="k">Aggregate</span> CustomerManagementAggregateViewModel {
    <span class="k">Service</span> US1_ExampleService {
      CreateCustomerOutput createCustomer (CreateCustomerInput input);
      UpdateCustomerOutput updateCustomer (UpdateCustomerInput input);
      OfferContractOutput offerContract (OfferContractInput input);
    }
    <span class="k">Entity</span> CustomerViewModel {
      CustomerID customerId
    }
    <span class="k">Entity</span> ContractViewModel {
      ContractID contractId
    }
  }
}

<span class="k">BoundedContext</span> CustomerManagementDomainLogic <span class="k">implements</span> CustomerManagement {
  <span class="k">domainVisionStatement</span> <span class="s">&quot;This Bounded Context realizes the following subdomains: CustomerManagement&quot;</span>
  <span class="k">type</span> <span class="k">SYSTEM</span>
  <span class="k">implementationTechnology</span> <span class="s">&quot;Sprint Boot&quot;</span>
  <span class="k">Aggregate</span> CustomerManagementAggregateBackend {
    <span class="k">Service</span> US1_ExampleService {
      CreateCustomerOutput createCustomer (CreateCustomerInput input);
      UpdateCustomerOutput updateCustomer (UpdateCustomerInput input);
      OfferContractOutput offerContract (OfferContractInput input);
    }
    <span class="k">Entity</span> CustomerBackend {
      CustomerID customerId
    }
    <span class="k">Entity</span> ContractBackend {
      ContractID contractId
    }
  }
}

<span class="k">BoundedContext</span> CustomerManagementDatabase {
  <span class="k">type</span> <span class="k">SYSTEM</span>
  <span class="k">implementationTechnology</span> <span class="s">&quot;JDBC&quot;</span>
}
</pre></div>

_Note:_ It is also possible to copy the domain model into the second subsystem (was not selected for the _CustomerManagementDatabase_ context above) with the corresponding checkbox on the dialog.

You can model application architectures with more than two subsystems by applying this transformation multiple times.

## What’s Next?
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
     - Use our [JHipster JDL generator template](/docs/jhipster-microservice-generation/) to generate microservices code from your Context Map.

## Frequently Asked Questions (FAQs)

 * Whats the difference between the transformations described above and the [Architectural Refactorings (ARs)](/docs/architectural-refactorings/)?
   * Some of the model transformations described here, such as _Split System Context Into Two Subsystems_, may seem similar to some of our ARs (_Split Bounded Context by ..._). However, there
     are different ideas behind the concepts.
   * The OOAD transformations above are designed to evolve a CML model from functional requirements rapidly. The transformations typically generate new elements into your model.
   * The [Architectural Refactorings (ARs)](/docs/architectural-refactorings/) on the other hand are designed to change/improve an existing model and architecture. They 
     typically do not add new elements to the model, but restucture the existing CML model.
