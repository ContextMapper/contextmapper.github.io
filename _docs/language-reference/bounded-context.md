---
title: Bounded Context
permalink: /docs/bounded-context/
---

Bounded contexts are defined on the root level of a CML (*.cml) file and then referenced on a context map which defines the relationships with other bounded contexts.
Have a look at [context map](/docs/context-map/) to see how you add a bounded context to your context map. 

## Syntax
The following example illustrates how a bounded context is defined in CML (syntactical features). The **Customer Management** context is a context within our fictitious insurance company example. The whole example with the context map and all bounded contexts can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example).

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerManagementContext <span class="k">implements</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">FEATURE</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;The customer management context is responsible for ...&quot;</span>
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java, JEE Application&quot;</span>
  <span class="k">responsibilities</span> = Customers, Addresses { <span class="s">&quot;The addresses of a customer&quot;</span> }
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
 
With the _implements_ keyword you specify which subdomain is implemented by this bounded context. See [Subdomain](/docs/subdomain/) to learn how subdomains are specified.
  
Note that all of the following attributes are **optional** and you do not have to specify them all. 
 
### Bounded Context Type
With the _type_ keyword you define the bounded contexts type, which can be one of the following:

 * FEATURE
 * APPLICATION
 * SYSTEM
 * TEAM
 
The type provides an indicator for which reason a bounded context may have been evolved. It further allows you to specify from which viewpoint you describe your bounded contexts.
For example you may want to create a team map, within which every bounded context reflects a team, inspired by [Brandolini](https://www.infoq.com/articles/ddd-contextmapping). A team map further allows you to specify which team is implementing which bounded contexts. Note that the context map type must be ORGANIZATIONAL to specify a team map. The corresponding syntax is described under [context map](/docs/context-map) and an example for a team map can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example).

### Domain Vision Statement
With the _domainVisionStatement_ keyword you can describe the vision statement of your bounded context, according to the DDD Domain Vision Statment pattern.

### Implementation Technology
The _implementationTechnology_ attribute allows you to add information about how the corresponding bounded context is implemented.

### Responsibility Layers
With the _responsibilities_ keyword you are allowed to specify the responsibilities of the bounded context, according to the DDD Responsibility Layers pattern. See [responsibility layers](/docs/responsibility-layers/).

### Knowledge Level
With the _knowledgeLevel_ attribute you define the knowledge level of the bounded context which can be one of the following two:
 * CONCRETE
 * META
 
This attribute allow you to define the knowledge level according to the DDD Knowledge Level pattern.

### Team _realizes_ Bounded Context
If your bounded context is of the type TEAM, you can specify which bounded context the team implements by using the _realizes_ keyword. The following example illustrates this:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomersBackofficeTeam <span class="k">implements</span> CustomerManagementDomain <span class="k">realizes</span> CustomerManagementContext {
  <span class="k">type</span> = <span class="k">TEAM</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;This team is responsible for implementing ...&quot;</span>
}
</pre></div>


## The Bounded Context Building Blocks
Within a bounded context you can create _Modules_ and _Aggregates_, as illustrated in the example at the beginning of this page. On this tactical DDD level we integrated the [Sculptor DSL](http://sculptorgenerator.org/).
This means within a module and an aggregate you can use all the [Sculptor features](http://sculptorgenerator.org/documentation/advanced-tutorial) to specify your bounded context, such as Entities, Value Objects, Domain Events, Services, Repositories, etc.

Use the [Sculptor Documentation](http://sculptorgenerator.org/documentation/advanced-tutorial) and our [examples](https://github.com/ContextMapper/context-mapper-examples) to find out how you specify your bounded context.
Note that the Aggregate pattern is the only tactical DDD pattern where we changed the Sculptor syntax and adapted it to our interpretation and requirements. See [Aggregate](/docs/aggregate/).

## Semantic Rules
Note that semantic rules (validators) exist for bounded contexts within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a bounded context:

* The _realizes_ keyword of the bounded context rule can only be used if the type of the bounded context is TEAM.

For a summary of all semantic rules and justifications, please consult [Language Semantics](/docs/language-model/).
