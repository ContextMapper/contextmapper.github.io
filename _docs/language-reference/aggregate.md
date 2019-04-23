---
title: Aggregate
permalink: /docs/aggregate/
---

The Aggregate pattern implementation from [Sculptor](http://sculptorgenerator.org/) has been adapted within CML to represent it with a separate grammar rule.
Note that all other tactic DDD patterns are not documented on this website. We refer to the [Sculptor project](http://sculptorgenerator.org/) and their [documentation](http://sculptorgenerator.org/documentation/advanced-tutorial).

## Syntax
The aggregate supports the [Responsibility Layers](/docs/responsibility-layers/) pattern and the [Knowledge Level](/docs/knowledge-level) pattern. 
An aggregate can further contain Services, Resources, Consumers and SimpleDomainObjects (Entities, Value Objects, Domain Events, etc.) 
which are not further introduced here. The according rules are defined by the [Sculptor DSL](http://sculptorgenerator.org/), as already mentioned. 
However, the following CML snippet illustrates an example of an aggregate to provide an impression how the rule can be used.

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Contract {
  <span class="k">responsibilities</span> = Contracts, Policies
  <span class="k">knowledgeLevel</span> = <span class="k">CONCRETE</span>
  
  <span class="k">Entity</span> Contract {
    <span class="k">aggregateRoot</span>
    
    - <span class="k">ContractId</span> identifier
    - <span class="k">Customer</span> client
    - <span class="k">List&lt;Product&gt;</span> products
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
</pre></div>

Further examples can be found within our Github example repository [context-mapper-examples](https://github.com/ContextMapper/context-mapper-examples).

## Aggregate Owner
CML allows to specify an owner on aggregate level. If aggregates are maintained by different teams, you can specify this as in the
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

This may be used for service decomposition by using the [Split Bounded Context by Owners](/docs/ar-split-bounded-context-by-owners) 
architectural refactoring.

Note that the _owner_ attribute refers to a team, which is a bounded context of the type _TEAM_: (see [Bounded Context](/docs/bounded-context) for more details)

<div class="highlight"><pre><span></span><span class="c">/* Team Definitions */</span>
<span class="k">BoundedContext</span> CustomerBackendTeam {
  <span class="k">type</span> = <span class="k">TEAM</span>
}

<span class="k">BoundedContext</span> CustomerFrontendTeam {
  <span class="k">type</span> = <span class="k">TEAM</span>
}
</pre></div>

## Aggregate Use Cases
With CML you can further specify by which use cases an aggregate is used. This may be used for service decomposition by using the
[Split Bounded Context by Use Cases](/docs/ar-split-bounded-context-by-use-cases) architectural refactoring.

Assigning aggregates to use cases can be done with the _useCases_ attribute as follows:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> PolicyManagementContext <span class="k">implements</span> PolicyManagementDomain {
  <span class="k">Aggregate</span> Offers {
    <span class="k">useCases</span> = CreateOfferForCustomer
    
    <span class="k">Entity</span> Offer {
      <span class="k">aggregateRoot</span>
      
      <span class="k">int</span> offerId
      - <span class="k">Customer</span> client
      - <span class="k">List&lt;Product&gt;</span> products
      <span class="k">BigDecimal</span> price
    }
  }
  <span class="k">Aggregate</span> Products {
    <span class="k">useCases</span> = CreateOfferForCustomer
    
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
    <span class="k">useCases</span> = UpdateContract
    
    <span class="k">Entity</span> Contract {
      <span class="k">aggregateRoot</span>
      
      - <span class="k">ContractId</span> identifier
      - <span class="k">Customer</span> client
      - <span class="k">List&lt;Product&gt;</span> products
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
</pre></div>

You can also refer to multiple use cases by providing a comma-separated list:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Offers {
  <span class="k">useCases</span> = CreateOfferForCustomer, UpdateOffer

  <span class="k">Entity</span> Offer {
    <span class="k">aggregateRoot</span>

    <span class="k">int</span> offerId
    - <span class="k">Customer</span> client
    - <span class="k">List&lt;Product&gt;</span> products
    <span class="k">BigDecimal</span> price
  }
}
</pre></div>

### Use Case Declaration
The use cases you refer to have to be declared on the root level of your CML file. To declare a use case, use the keyword _UseCase_.
A use case can be declared by simply give the case a name, as shown in the example below. If you want to provide further information
about the use case you can specify which attributes of which entities are read and written by this use case (strings only; no references): 

<div class="highlight"><pre><span></span><span class="c">/* Simple use case (only name given) */</span>
<span class="k">UseCase</span> UpdateContract
<span class="k">UseCase</span> UpdateOffer

<span class="c">/* Extended declaration with read and written attributes */</span>
<span class="k">UseCase</span> CreateOfferForCustomer {
  <span class="k">reads</span> <span class="s">&quot;Customer.id&quot;</span>, <span class="s">&quot;Customer.name&quot;</span>
  <span class="k">writes</span> <span class="s">&quot;Offer.offerId&quot;</span>, <span class="s">&quot;Offer.price&quot;</span>, <span class="s">&quot;Offer.products&quot;</span>, <span class="s">&quot;Offer.client&quot;</span>
}
</pre></div>

## Likelihood for Change
With the attribute _likelihoodForChange_ you can specify how [volatile](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-4-Structural-Volatility)
an aggregate is. The attribute takes one of the following three values:

 * RARELY
 * NORMAL
 * OFTEN
 
This attribute may be used for service decomposition, since parts which are likely to change should typically be isolated in separate
components (see [Parnas](https://dl.acm.org/citation.cfm?doid=361598.361623)). In CML you can use this by applying the 
[Extract Aggregates which are Likely to Change](/docs/ar-extract-aggregates-which-are-likely-to-change) architectural refactoring.

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

