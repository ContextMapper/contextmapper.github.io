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
