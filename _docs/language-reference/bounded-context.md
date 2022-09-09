---
title: Bounded Context
permalink: /docs/bounded-context/
---

Bounded contexts are defined on the root level of a CML (*.cml) file and then referenced on a context map which defines the relationships with other bounded contexts. Have a look at [context map](/docs/context-map/) to see how you add a bounded context to your context map. 

## Syntax
The following example illustrates how a bounded context is defined in CML (syntactical features). The **Customer Management** context is a context within our fictitious insurance company example. The whole example with the context map and all bounded contexts can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example).

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerManagementContext <span class="k">implements</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">FEATURE</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;The customer management context is responsible for ...&quot;</span>
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java, JEE Application&quot;</span>
  <span class="k">responsibilities</span> = <span class="s">&quot;Customers&quot;</span>, <span class="s">&quot;Addresses&quot;</span>
  <span class="k">knowledgeLevel</span> = <span class="k">CONCRETE</span>

  <span class="k">Module</span> addresses {
    <span class="k">Aggregate</span> Addresses {
      <span class="k">Entity</span> Address {
        <span class="k">String</span> city
      }
    }
  }
  <span class="k">Aggregate</span> Customers {
    <span class="k">Entity</span> Customer {
      <span class="k">aggregateRoot</span>

      - <span class="k">SocialInsuranceNumber</span> sin
      <span class="k">String</span> firstname
      <span class="k">String</span> lastname
      - <span class="k">List&lt;Address&gt;</span> addresses
    }
  }
}
</pre></div>

<div class="alert alert-custom">
<strong>Note:</strong> Bounded Context names must be unique within your CML model.
</div>
 
The **implements** keyword specifies which domain or subdomains are implemented by this bounded context. Behind the **implements**
keyword you can either reference a list of subdomains (comma-separated) or one top-level domain. Consult [Subdomain](/docs/subdomain/) to  learn how subdomains are specified.

Attribute values are assigned as follows:
<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> ContextMapperTool <span class="k">refines</span> StrategicDomainDrivenDesignContext {
  <span class="k">type</span> <span class="k">FEATURE</span>
  <span class="k">domainVisionStatement</span> <span class="s">&quot;Context Mapper provides a formal way to model strategic DDD Context Maps.&quot;</span>
  <span class="k">implementationTechnology</span> <span class="s">&quot;Java, Eclipse&quot;</span>
}
</pre></div>
An equal sign (=) to assign attribute values may be present but can be omitted.

The example above also shows how you can let one bounded context refine another one (with the **refines** keyword). This feature allows you to create some kind of an inheritance hierarchy in case one bounded context can be seen as a refinement of another bounded context. However, note that this is only a modeling information and generators do not recursively resolve the domain model (Aggregates, etc.) of refined bounded contexts.
 
  
All of the following attributes are **optional** and you do not have to specify them all. 
 
### Bounded Context Type
With the _type_ keyword you define the bounded contexts type, which can be one of the following:

 * FEATURE
 * APPLICATION
 * SYSTEM
 * TEAM
 
The type provides an indicator for which reason a bounded context may have been evolved. It further allows you to specify from which 
viewpoint you describe your bounded contexts. FEATURE contexts are analysis or early design abstractions, taking a functional scenario view. Application contexts represent more 
elaborated, logical designs and implementation views; system contexts add a more physical, process- and deployment-oriented view.  
<!-- TODO compare this context taxonomy to Brown's C4 model --> 

Finally, you may want to create a team map, within which every bounded context reflects a team, inspired by [Brandolini](https://www.infoq.com/articles/ddd-contextmapping). A team map further allows you to specify which team is implementing which bounded contexts (of type FEATURE, APPLICATION, or SYSTEM). Note that the context map type must be ORGANIZATIONAL to specify a team map. The corresponding syntax is described under [context map](/docs/context-map) and an example for a team map can be found 
[here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example).

The following table lists examples for each Bounded Context type to illustrate how we interpret them:

| Context Type         | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FEATURE              | Such a Bounded Context represents a boundary around a set of functional features (user stories / use cases). For example, everything that is related to _customer_ management in an insurance scenario: create customer, update customer, update customer address, etc.                                                                                                                                                                                                                                                                                                                                     |
| APPLICATION          | A Bounded Context of this type represents an application from a logical viewpoint. For example, a software solution for an insurance company (an example can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example)) consists of multiple applications: a self-service frontend application for the customers, a backend system to manage the customers and contract, etc. An application typically encompasses multiple functional features. In a (micro-)service-oriented architecture, each (micro-)service can be seen as an application. |
| SYSTEM               | The system Bounded Context allow to model a software from a more physical perspective (deployment). Examples for systems: a single page application for the frontend, a Spring Boot application that realizes the domain logic, an Oracle database that holds the data, etc. Thus, an application typically consists of multiple systems.                                                                                                                                                                                                                                                                   |
| TEAM                 | A development team can also represent a Bounded Context. For example in our [insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example#team-map), multiple teams work on different parts of the software: _customer frontend_ team, customer backend_ team, _contracts_ team, etc.                                                                                                                                                                                                                                                             |

You can evolve the different types of Bounded Context with our [Rapid Object-oriented Analysis and Design](/docs/rapid-ooad/) CML transformations. From functional requirements
written as user stories or use cases you can derive Bounded Contexts of the type FEATURE and/or APPLICATON. From those features you can then derive Bounded Contexts of the
type SYSTEM automatically. You can find more about this automated transformations [here](/docs/rapid-ooad/).

### Domain Vision Statement
With the _domainVisionStatement_ keyword you can describe the vision statement of your bounded context, according to the DDD Domain Vision Statement pattern. See [this page](/docs/domain-vision-statement/).

### Implementation Technology
The _implementationTechnology_ attribute allows you to add information about how the corresponding bounded context is implemented. Note that this attribute does not correspond to any DDD pattern.

### Responsibility Layers
With the _responsibilities_ keyword you are allowed to specify the responsibilities of the bounded context, according to the DDD Responsibility Layers pattern. See [responsibility layers](/docs/responsibility-layers/).

### Knowledge Level
With the _knowledgeLevel_ attribute you define the knowledge level of the bounded context which can be one of the following two:
 * CONCRETE
 * META
 
This attribute allows you to define the knowledge level according to the DDD Knowledge Level pattern. See [this page](/docs/knowledge-level/).

### Support for Bounded Context Canvases

To support Bounded Context Canvases, use these optional fields in `BoundedContext`:
- `businessModel`. One of:
  * UNDEFINED
  * REVENUE
  * ENGAGEMENT
  * COMPLIANCE
  * COST_REDUCTION
- `evolution`. One of:
  * UNDEFINED
  * GENESIS
  * CUSTOM_BUILT
  * PRODUCT
  * COMMODITY

Further reading on bounded context canvases:
- [_The Bounded Context Canvas_](https://github.com/ddd-crew/bounded-context-canvas)
- [_Bounded Context Canvas V3: Simplifications and Additions_](https://medium.com/nick-tune-tech-strategy-blog/bounded-context-canvas-v2-simplifications-and-additions-229ed35f825f)
- [_DDD re-distilled_](https://yoan-thirion.gitbook.io/knowledge-base/software-architecture/ddd-re-distilled)
- [_What I talk about when I talk about Domain-Driven Design by Andrew Harmel-Law_](https://youtu.be/6nrRfCkeAKU)

### Team _realizes_ Bounded Context
If your bounded context is of the type TEAM, you can specify which bounded context the team implements by using the _realizes_ keyword. The following example illustrates this:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomersBackofficeTeam <span class="k">implements</span> CustomerManagementDomain <span class="k">realizes</span> CustomerManagementContext {
  <span class="k">type</span> = <span class="k">TEAM</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;This team is responsible for implementing ...&quot;</span>
}
</pre></div>


## The Bounded Context Building Blocks
Within a bounded context, you can create _Modules_ and _Aggregates_ as illustrated in the example at the beginning of this page. On this tactical DDD level we integrated the [Sculptor DSL](http://sculptorgenerator.org/).
This means within a module and an aggregate you can use all the [Sculptor features](http://sculptorgenerator.org/documentation/advanced-tutorial) to specify your bounded context, such as Entities, Value Objects, Domain Events, Services, Repositories, etc.

Use the [Sculptor Documentation](http://sculptorgenerator.org/documentation/advanced-tutorial) and our [examples](https://github.com/ContextMapper/context-mapper-examples) to find out how you specify your bounded context.
Note that the Aggregate pattern is the only tactical DDD pattern where we changed the Sculptor syntax and adapted it to our interpretation and requirements. See [Aggregate](/docs/aggregate/).

## Semantic Rules
Note that semantic rules (validators) exist for bounded contexts within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a bounded context:

* The _realizes_ keyword of the bounded context rule can only be used if the type of the bounded context is TEAM.

For a summary of all semantic rules and justifications, please consult [Language Semantics](/docs/language-model/).
