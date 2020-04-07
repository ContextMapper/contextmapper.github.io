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
 - **Step 3**: Derive DDD **Bounded Contexts** from the Subdomains
   - Context Mapper offers a transformation that executes this step.
   - The generated model elements contain `TODO` suggestions for further elaboration.

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
