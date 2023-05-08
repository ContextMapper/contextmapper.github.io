---
title: Aggregate
permalink: /docs/aggregate/
---

The Aggregate pattern implementation from [Sculptor](http://sculptorgenerator.org/) has been adapted within CML to represent it with a separate grammar rule. 

For a short introduction to the syntax of the other tactic DDD patterns, please have a look at [Tactic DDD Syntax](/docs/tactic-ddd/). 
For more details, we refer to the [Sculptor project](http://sculptorgenerator.org/) and its [documentation](http://sculptorgenerator.org/documentation/advanced-tutorial).

## Syntax
The aggregate supports the [Responsibility Layers](/docs/responsibility-layers/) pattern and the [Knowledge Level](/docs/knowledge-level) pattern. An aggregate can further 
contain Services, Resources, Consumers and SimpleDomainObjects (Entities, Value Objects, Domain Events, etc.) which are not further introduced here. 
The respective rules are defined by the [Sculptor DSL](http://sculptorgenerator.org/), as already mentioned. 

The following CML snippet illustrates an example of an aggregate to provide an impression how the rule can be used:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Contract {
  <span class="k">responsibilities</span> = <span class="s">&quot;Contracts&quot;</span>, <span class="s">&quot;Policies&quot;</span>
  <span class="k">knowledgeLevel</span> = <span class="k">CONCRETE</span>

  <span class="k">Entity</span> Contract {
    <span class="k">aggregateRoot</span>

    - <span class="k">ContractId</span> identifier
    - <span class="k">Customer</span> client
    - <span class="k">List</span>&lt;Product&gt; products
  }

  <span class="k">enum</span> States {
    <span class="k">aggregateLifecycle</span>
    CREATED, POLICE_CREATED, RECALLED
  }

  <span class="k">ValueObject</span> ContractId {
    <span class="k">int</span> contractId <span class="k">key</span>
  }

  <span class="k">Entity</span> Policy {
    <span class="k">int</span> policyNr
    - <span class="k">Contract</span> contract
    <span class="k">BigDecimal</span> price
  }

  <span class="k">Service</span> ContractService {
    @ContractId createContract(@Contract contrace) : <span class="k">write</span> [ -&gt; CREATED];
    @Contract getContract(@ContractId contractId) : <span class="k">read</span>-<span class="k">only</span>;
    <span class="k">boolean</span> createPolicy(@ContractId contractId) : <span class="k">write</span> [ CREATED -&gt; POLICE_CREATED ];
    <span class="k">boolean</span> recall(@ContractId contractId) : <span class="k">write</span> [ CREATED, POLICE_CREATED -&gt; RECALLED ];
  }
}
</pre></div>

The equal sign (=) to assign an attribute value is always optional and therefore can be omitted.

<div class="alert alert-custom">
<strong>Note:</strong> Aggregate names must be unique within the whole CML model.
</div>

Further examples can be found within our GitHub example repository [context-mapper-examples](https://github.com/ContextMapper/context-mapper-examples).

## Aggregate Lifecycle and State Transitions
As already illustrated in the example above, you can declare an Aggregate's states with an _enum_. The _aggregateLifecycle_ keyword marks the enum that defines the states:

<div class="highlight"><pre><span></span><span class="k">enum</span> States {
  <span class="k">aggregateLifecycle</span>
  CREATED, POLICE_CREATED, RECALLED
}
</pre></div>

In addition, every operation (no matter whether it is specified in a _Service_ or an _Entity_) can declare whether it is a "read only" or "write" operation with the keywords _read-only_ and _write_:

<div class="highlight"><pre><span></span><span class="k">Service</span> ContractService {
  @ContractId createContract(@Contract contrace) : <span class="k">write</span>;
  @Contract getContract(@ContractId contractId) : <span class="k">read</span>-<span class="k">only</span>;
  <span class="k">boolean</span> createPolicy(@ContractId contractId) : <span class="k">write</span>;
  <span class="k">boolean</span> recall(@ContractId contractId) : <span class="k">write</span>;
}
</pre></div>

A _write_ operation may changes the state of the Aggregate. Such state transitions can be specified in square brackets:

<div class="highlight"><pre><span></span><span class="k">Service</span> ContractService {
  @ContractId createContract(@Contract contrace) : <span class="k">write</span> [ -&gt; CREATED];
  @Contract getContract(@ContractId contractId) : <span class="k">read</span>-<span class="k">only</span>;
  <span class="k">boolean</span> createPolicy(@ContractId contractId) : <span class="k">write</span> [ CREATED -&gt; POLICE_CREATED ];
  <span class="k">boolean</span> recall(@ContractId contractId) : <span class="k">write</span> [ CREATED, POLICE_CREATED -&gt; RECALLED ];
}
</pre></div>

These language features allow you to define the lifecycle of an Aggregate. The following examples show all possible variants of state transitions:

<div class="highlight"><pre><span></span><span class="c">// an initial state:</span>
-<span class="k">&gt;</span> CREATED

<span class="c">// simple state transition from one state into the other</span>
CREATED -&gt; CHECK_REQUESTED

<span class="c">// the left side can contain multiple states:</span>
<span class="c">// (this means that the state on the right can be reached by any of those on the left side)</span>
CREATED, CHECK_REQUESTED -&gt; CHECK_IN_PROGRESS

<span class="c">// multiple target states possible</span>
<span class="c">// X stands for XOR and means one OR the other will be reached but not both at the same time (exclusive OR)</span>
CHECK_IN_PROGRESS -&gt; ACCEPTED <span class="k">X</span> REJECTED

<span class="c">// target states can be marked as end states with a star:</span>
CHECK_IN_PROGRESS -&gt; ACCEPTED* <span class="k">X</span> REJECTED*

<span class="c">// a combination of multiple on the left and multiple on the right</span>
CREATED, CHECK_REQUESTED -&gt; ACCEPTED <span class="k">X</span> REJECTED
</pre></div>

_Hint:_ You can also model the state transition inside your [event flows in the application layer]().

With our [PlantUML generator](/docs/plant-uml/) you can visualize the lifecycle of your Aggregates with state diagrams. For example, the model at the top of this page generates the following state diagram:

![Sample State Diagram](/img/LangRef-Aggregate_Sample-StateDiagram.png)

**Note:** If you use the _target state_ markers (*) as documented above, we also use this information in our [PlantUML Generator](/docs/plant-uml/) and generate the corresponding end states:

![Sample State Diagram](/img/LangRef-Aggregate_Sample-StateDiagram_with-end-States.png)

## Aggregate Owner
CML allows specifying an owner on the aggregate level. If aggregates are maintained by different teams, you can specify this as in the
following example:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerSelfServiceContext <span class="k">implements</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">APPLICATION</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;This context represents a web application which allows the customer to login and change basic data records like the address.&quot;</span>
  <span class="k">responsibilities</span> = <span class="s">&quot;AddressChange&quot;</span>
  <span class="k">implementationTechnology</span> = <span class="s">&quot;PHP Web Application&quot;</span>

  <span class="k">Aggregate</span> CustomerFrontend {
    <span class="k">owner</span> = CustomerFrontendTeam

    <span class="k">DomainEvent</span> CustomerAddressChange {
      <span class="k">aggregateRoot</span>

      - <span class="k">UserAccount</span> issuer
      - <span class="k">Address</span> changedAddress
    }
  }
  <span class="k">Aggregate</span> Acounts {
    <span class="k">owner</span> = CustomerBackendTeam

    <span class="k">Entity</span> UserAccount {
      <span class="k">aggregateRoot</span>

      <span class="k">String</span> username
      - <span class="k">Customer</span> accountCustomer
    }
  }
}
</pre></div>

The _owner_ attribute may be used for service decomposition by using the [Split Bounded Context by Owners](/docs/ar-split-bounded-context-by-owners) 
architectural refactoring.

Note that the _owner_ attribute refers to a team, which must be a bounded context of the type _TEAM_: (see [Bounded Context](/docs/bounded-context) for more details):

<div class="highlight"><pre><span></span><span class="c">/* Team Definitions */</span>
<span class="k">BoundedContext</span> CustomerBackendTeam {
  <span class="k">type</span> = <span class="k">TEAM</span>
}

<span class="k">BoundedContext</span> CustomerFrontendTeam {
  <span class="k">type</span> = <span class="k">TEAM</span>
}
</pre></div>

## Aggregate Features
With CML you can further specify which [features or user requirements (use cases and/or user stories)](/docs/user-requirements/) an Aggregate supports. This information may be used for service decomposition when applying the [Split Bounded Context by Features](/docs/ar-split-bounded-context-by-features) architectural refactoring.

Use Cases can be assigned with the _useCases_ keyword and User Stories with the _userStories_ keyword. You can also use the _features_ keyword and assign both, Use Cases and User Stories, at the same time:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> PolicyManagementContext <span class="k">implements</span> PolicyManagementDomain {
  <span class="k">Aggregate</span> Offers {
    <span class="k">useCases</span> = CreateOfferForCustomer
    
    <span class="k">Entity</span> Offer {
      <span class="k">aggregateRoot</span>
      
      <span class="k">int</span> offerId
      - <span class="k">Customer</span> client
      - <span class="k">List</span>&lt;Product&gt; products
      <span class="k">BigDecimal</span> price
    }
  }
  <span class="k">Aggregate</span> Products {
    <span class="k">userStories</span> = AddProductToOffer
    
    <span class="k">Entity</span> Product {
      <span class="k">aggregateRoot</span>
      
      - <span class="k">ProductId</span> identifier
      <span class="k">String</span> productName
    }
    <span class="k">ValueObject</span> ProductId {
      <span class="k">int</span> productId <span class="k">key</span>
    }
  }
  <span class="k">Aggregate</span> Contract {
    <span class="k">features</span> = CreateOfferForCustomer, UpdateContract
    
    <span class="k">Entity</span> Contract {
      <span class="k">aggregateRoot</span>
      
      - <span class="k">ContractId</span> identifier
      - <span class="k">Customer</span> client
      - <span class="k">List</span>&lt;Product&gt; products
    }
    <span class="k">ValueObject</span> ContractId {
      <span class="k">int</span> contractId <span class="k">key</span>
    }
    
    <span class="k">Entity</span> Policy {
      <span class="k">int</span> policyNr
      - <span class="k">Contract</span> contract
      <span class="k">BigDecimal</span> price
    }
  }
}

<span class="k">UseCase</span> CreateOfferForCustomer
<span class="k">UserStory</span> UpdateContract
<span class="k">UserStory</span> AddProductToOffer
</pre></div>

Multiple User Stories and/or Use Cases can be assigned as a comma-separated list, as shown in the last Aggregate example above.

### Use Case and User Story Declaration
The Use Cases and User Stories you refer to have to be declared on the root level of your CML file. Have a look at our [user requirements](/docs/user-requirements/) page to see how you can declare and specify your cases and stories.

## Security Zones
The attribute _securityZone_ allows you to assign different Aggregates into different _security zones_. This language feature is primarily used to generate the [user representations for Service Cutter](/docs/service-cutter-context-map-suggestions/#input-and-preconditions), i.e. the [separated security zones](https://github.com/ServiceCutter/ServiceCutter/wiki/Separated-security-zones).

This can be very helpful to model security-related requirements which can later help in decomposing a Bounded Context.

A simple example:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> MyMonolith {
  <span class="k">Aggregate</span> CustomerManagement {
    <span class="k">securityZone</span> <span class="s">&quot;Internal&quot;</span>
    <span class="k">Entity</span> Customer {
      <span class="k">String</span> firstName
      <span class="k">String</span> lastName
    }
    <span class="k">Entity</span> Address {
      - <span class="k">Customer</span> customer
      <span class="k">String</span> street
      <span class="k">String</span> city
    }
  }
  <span class="k">Aggregate</span> CustomerFrontend {
    <span class="k">securityZone</span> <span class="s">&quot;Public&quot;</span>
    <span class="k">DomainEvent</span> AddressChanged {
      - <span class="k">Address</span> address
    }
  }
}
</pre></div>

## Security Access Groups
The attribute _securityAccessGroup_ allows you to assign different Aggregates to different _security access groups_. This feature is primarily used to generate the [user representations for Service Cutter](/docs/service-cutter-context-map-suggestions/#input-and-preconditions), i.e. the [security access groups](https://github.com/ServiceCutter/ServiceCutter/wiki/Security-access-groups).

This can be very helpful to declare that your Aggregates have different access requirements, which can later help when decomposing a Bounded Context.

An example:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> MyMonolith {
  <span class="k">Aggregate</span> CustomerManagement {
    <span class="k">securityAccessGroup</span> <span class="s">&quot;InsuranceEmployees&quot;</span>
    <span class="k">Entity</span> Customer {
      <span class="k">String</span> firstName
      <span class="k">String</span> lastName
    }
    <span class="k">Entity</span> Address {
      - <span class="k">Customer</span> customer
      <span class="k">String</span> street
      <span class="k">String</span> city
    }
  }
  <span class="k">Aggregate</span> CustomerFrontend {
    <span class="k">securityAccessGroup</span> <span class="s">&quot;Customers&quot;</span>
    <span class="k">DomainEvent</span> AddressChanged {
      - <span class="k">Address</span> address
    }
  }
}
</pre></div>

## Characteristics Classification
On the Aggregate level it is possible to classify parts of your domain model [according to Service Cutter's characteristics (compatibilities)](https://github.com/ServiceCutter/ServiceCutter/wiki/Compatibilities). This is primarily used to generate the [user representations for Service Cutter](/docs/service-cutter-context-map-suggestions/#input-and-preconditions), in case you generate service decomposition suggestions with Context Mapper.

For example: you can declare how often a certain Aggregate changes. Later, when you decompose your system, parts that change often should probably be separated from parts that basically never change. You find all the characteristics in the [Service Cutter wiki](https://github.com/ServiceCutter/ServiceCutter/wiki/Compatibilities).

In the following you find examples how you can classify Aggregates according to these criteria/characteristics in CML:

 * [Content Volatility](#content-volatility)
 * [Structural Volatility (a.k.a. Likelihood for Change)](#likelihood-for-change)
 * [Availability Criticality](#availability-criticality)
 * [Consistency Criticality](#consistency-criticality)
 * [Storage Similarity](#storage-similarity)
 * [Security Criticality](#security-criticality)

### Content Volatility
This characteristic corresponds to the [Content Volatility](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-8-Content-Volatility) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _contentVolatility_ takes the following values:
 * RARELY
 * NORMAL
 * OFTEN

An example:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> AggregateDemo1 {
  <span class="k">contentVolatility</span> = <span class="k">OFTEN</span> <span class="c">// content changes more often in this Aggregate</span>
  
  <span class="k">Entity</span> DemoEntityOne
}

<span class="k">Aggregate</span> AggregateDemo2 {
  <span class="k">contentVolatility</span> = <span class="k">NORMAL</span>
  
  <span class="k">Entity</span> DemoEntityTwo
}
</pre></div>


### Likelihood for Change
With the attribute _likelihoodForChange_ (or _structuralVolatility_) you can specify how [volatile](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-4-Structural-Volatility) an Aggregate is ([Structural Volatility](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-4-Structural-Volatility)). The attribute takes one of the following three values:

 * RARELY
 * NORMAL
 * OFTEN
 
This attribute may be used for service decomposition, since parts which are likely to change should typically be isolated in separate
components (see [Parnas](https://dl.acm.org/citation.cfm?doid=361598.361623)). Besides for [proposing new service cuts](/docs/service-cutter-context-map-suggestions), you can use this in CML by applying the 
[Extract Aggregates by Volatility](/docs/ar-extract-aggregates-by-volatility) architectural refactoring.

The likelihood on an aggregate is declared as follows:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> CustomerFrontend {
  <span class="k">likelihoodForChange</span> = OFTEN
  
  <span class="k">DomainEvent</span> CustomerAddressChange {
    <span class="k">aggregateRoot</span>
    
    - <span class="k">UserAccount</span> issuer
    - <span class="k">Address</span> changedAddress
  }
}
</pre></div>

You can also use the _structuralVolatility_ keyword:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> CustomerFrontend {
  <span class="k">structuralVolatility</span> = <span class="k">OFTEN</span>
  
  <span class="k">DomainEvent</span> CustomerAddressChange {
    <span class="k">aggregateRoot</span>
    
    - <span class="k">UserAccount</span> issuer
    - <span class="k">Address</span> changedAddress
  }
}
</pre></div>

### Availability Criticality
This characteristic corresponds to the [Availability Criticality](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-7-Availability-Criticality) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _availabilityCriticality_ takes the following values:
 * LOW
 * NORMAL
 * HIGH

An example:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> AggregateDemo1 {
  <span class="k">availabilityCriticality</span> = <span class="k">HIGH</span> <span class="c">// higher availability requirements then other aggregate</span>
  
  <span class="k">Entity</span> DemoEntityOne
}

<span class="k">Aggregate</span> AggregateDemo2 {
  <span class="k">availabilityCriticality</span> = <span class="k">NORMAL</span>
  
  <span class="k">Entity</span> DemoEntityTwo
}
</pre></div>

### Consistency Criticality
This characteristic corresponds to the [Consistency Criticality](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-6-Consistency-Criticality) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _consistencyCriticality_ takes the following values:
 * LOW
 * NORMAL
 * HIGH

An example:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> AggregateDemo1 {
  <span class="k">consistencyCriticality</span> = <span class="k">HIGH</span> <span class="c">// higher consistency requirements then other aggregate</span>
  
  <span class="k">Entity</span> DemoEntityOne
}

<span class="k">Aggregate</span> AggregateDemo2 {
  <span class="k">consistencyCriticality</span> = <span class="k">NORMAL</span>
  
  <span class="k">Entity</span> DemoEntityTwo
}
</pre></div>

### Storage Similarity
This characteristic corresponds to the [Storage Similarity](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-11-Storage-Similarity) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _storageSimilarity_ takes the following values:
 * TINY
 * NORMAL
 * HUGE

An example:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> AggregateDemo1 {
  <span class="k">storageSimilarity</span> = <span class="k">HUGE</span> <span class="c">// similar storage requirements as AggregateDemo3</span>
  
  <span class="k">Entity</span> DemoEntityOne
}

<span class="k">Aggregate</span> AggregateDemo2 {
  <span class="k">storageSimilarity</span> = <span class="k">NORMAL</span>
  
  <span class="k">Entity</span> DemoEntityTwo
}

<span class="k">Aggregate</span> AggregateDemo3 {
  <span class="k">storageSimilarity</span> = <span class="k">HUGE</span> <span class="c">// similar storage requirements as AggregateDemo1</span>
  
  <span class="k">Entity</span> DemoEntityThree
}
</pre></div>

### Security Criticality
This characteristic corresponds to the [Security Criticality](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-15-Security-Criticality) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _securityCriticality_ takes the following values:
 * LOW
 * NORMAL
 * HIGH

An example:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> AggregateDemo1 {
  <span class="k">securityCriticality</span> = <span class="k">HIGH</span> <span class="c">// high security requirements</span>
  
  <span class="k">Entity</span> DemoEntityOne
}

<span class="k">Aggregate</span> AggregateDemo2 {
  <span class="k">securityCriticality</span> = <span class="k">NORMAL</span>
  
  <span class="k">Entity</span> DemoEntityTwo
}
</pre></div>

