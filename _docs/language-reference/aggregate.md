---
title: Aggregate
permalink: /docs/aggregate/
---

The Aggregate pattern implementation from [Sculptor](https://sculptor.github.io/) has been adapted within CML to represent it with a separate grammar rule. 

For a short introduction to the syntax of the other tactic DDD patterns, please have a look at [Tactic DDD Syntax](/docs/tactic-ddd/). 
For more details, we refer to the [Sculptor project](https://sculptor.github.io/) and its [documentation](https://sculptor.github.io/documentation/advanced-tutorial).

## Syntax
The aggregate supports the [Responsibility Layers](/docs/responsibility-layers/) pattern and the [Knowledge Level](/docs/knowledge-level) pattern. An aggregate can further 
contain Services, Resources, Consumers and SimpleDomainObjects (Entities, Value Objects, Domain Events, etc.) which are not further introduced here. 
The respective rules are defined by the [Sculptor DSL](https://sculptor.github.io/), as already mentioned. 

The following CML snippet illustrates an example of an aggregate to provide an impression how the rule can be used:

```cml
Aggregate Contract {
  responsibilities = "Contracts", "Policies"
  knowledgeLevel = CONCRETE

  Entity Contract {
    aggregateRoot

    - ContractId identifier
    - Customer client
    - List<Product> products
  }

  enum States {
    aggregateLifecycle
    CREATED, POLICE_CREATED, RECALLED
  }

  ValueObject ContractId {
    int contractId key
  }

  Entity Policy {
    int policyNr
    - Contract contract
    BigDecimal price
  }

  Service ContractService {
    @ContractId createContract(@Contract contrace) : write [ -> CREATED];
    @Contract getContract(@ContractId contractId) : read-only;
    boolean createPolicy(@ContractId contractId) : write [ CREATED -> POLICE_CREATED ];
    boolean recall(@ContractId contractId) : write [ CREATED, POLICE_CREATED -> RECALLED ];
  }
}
```

The equal sign (=) to assign an attribute value is always optional and therefore can be omitted.

<div class="alert alert-custom">
<strong>Note:</strong> Aggregate names must be unique within the whole CML model.
</div>

Further examples can be found within our GitHub example repository [context-mapper-examples](https://github.com/ContextMapper/context-mapper-examples).

## Aggregate Lifecycle and State Transitions
As already illustrated in the example above, you can declare an Aggregate's states with an _enum_. The _aggregateLifecycle_ keyword marks the enum that defines the states:

```cml
enum States {
  aggregateLifecycle
  CREATED, POLICE_CREATED, RECALLED
}
```

In addition, every operation (no matter whether it is specified in a _Service_ or an _Entity_) can declare whether it is a "read only" or "write" operation with the keywords _read-only_ and _write_:

```cml
Service ContractService {
  @ContractId createContract(@Contract contrace) : write;
  @Contract getContract(@ContractId contractId) : read-only;
  boolean createPolicy(@ContractId contractId) : write;
  boolean recall(@ContractId contractId) : write;
}
```

A _write_ operation may changes the state of the Aggregate. Such state transitions can be specified in square brackets:

```cml
Service ContractService {
  @ContractId createContract(@Contract contrace) : write [ -> CREATED];
  @Contract getContract(@ContractId contractId) : read-only;
  boolean createPolicy(@ContractId contractId) : write [ CREATED -> POLICE_CREATED ];
  boolean recall(@ContractId contractId) : write [ CREATED, POLICE_CREATED -> RECALLED ];
}
```

With our [PlantUML generator](/docs/plant-uml/) you can visualize the lifecycle of your Aggregates with state diagrams. For example, the model at the top of this page generates the following state diagram:

![Sample State Diagram](/img/LangRef-Aggregate_Sample-StateDiagram.png)

**Note:** If you use the _target state_ markers (*) as documented above, we also use this information in our [PlantUML Generator](/docs/plant-uml/) and generate the corresponding end states:

![Sample State Diagram](/img/LangRef-Aggregate_Sample-StateDiagram_with-end-States.png)

These language features allow you to define the lifecycle of an Aggregate. The following example show all possible variants of state transitions (note that the following example is not in line with the example above; it just shows all variants of possible state transitions):

```cml
// an initial state:
-> CREATED

// simple state transition from one state into the other
CREATED -> CHECK_REQUESTED

// the left side can contain multiple states:
// (this means that the state on the right can be reached by any of those on the left side)
CREATED, CHECK_REQUESTED -> CHECK_IN_PROGRESS

// multiple target states possible
// X stands for XOR and means one OR the other will be reached but not both at the same time (exclusive OR)
CHECK_IN_PROGRESS -> ACCEPTED X REJECTED

// target states can be marked as end states with a star:
CHECK_IN_PROGRESS -> ACCEPTED* X REJECTED*

// a combination of multiple on the left and multiple on the right
CREATED, CHECK_REQUESTED -> ACCEPTED X REJECTED
```

_Hint:_ You can also model the state transition inside your [event flows in the application layer](/docs/application-and-process-layer/#processes-and-eventcommand-flows).

## Aggregate Owner
CML allows specifying an owner on the aggregate level. If aggregates are maintained by different teams, you can specify this as in the
following example:

```cml
BoundedContext CustomerSelfServiceContext implements CustomerManagementDomain {
  type = APPLICATION
  domainVisionStatement = "This context represents a web application which allows the customer to login and change basic data records like the address."
  responsibilities = "AddressChange"
  implementationTechnology = "PHP Web Application"

  Aggregate CustomerFrontend {
    owner = CustomerFrontendTeam

    DomainEvent CustomerAddressChange {
      aggregateRoot

      - UserAccount issuer
      - Address changedAddress
    }
  }
  Aggregate Acounts {
    owner = CustomerBackendTeam

    Entity UserAccount {
      aggregateRoot

      String username
      - Customer accountCustomer
    }
  }
}
```

The _owner_ attribute may be used for service decomposition by using the [Split Bounded Context by Owners](/docs/ar-split-bounded-context-by-owners) 
architectural refactoring.

Note that the _owner_ attribute refers to a team, which must be a bounded context of the type _TEAM_: (see [Bounded Context](/docs/bounded-context) for more details):

```cml
/* Team Definitions */
BoundedContext CustomerBackendTeam {
  type = TEAM
}

BoundedContext CustomerFrontendTeam {
  type = TEAM
}
```

## Aggregate Features
With CML you can further specify which [features or user requirements (use cases and/or user stories)](/docs/user-requirements/) an Aggregate supports. This information may be used for service decomposition when applying the [Split Bounded Context by Features](/docs/ar-split-bounded-context-by-features) architectural refactoring.

Use Cases can be assigned with the _useCases_ keyword and User Stories with the _userStories_ keyword. You can also use the _features_ keyword and assign both, Use Cases and User Stories, at the same time:

```cml
BoundedContext PolicyManagementContext implements PolicyManagementDomain {
  Aggregate Offers {
    useCases = CreateOfferForCustomer

    Entity Offer {
      aggregateRoot

      int offerId
      - Customer client
      - List<Product> products
      BigDecimal price
    }
  }
  Aggregate Products {
    userStories = AddProductToOffer

    Entity Product {
      aggregateRoot

      - ProductId identifier
      String productName
    }
    ValueObject ProductId {
      int productId key
    }
  }
  Aggregate Contract {
    features = CreateOfferForCustomer, UpdateContract

    Entity Contract {
      aggregateRoot

      - ContractId identifier
      - Customer client
      - List<Product> products
    }
    ValueObject ContractId {
      int contractId key
    }

    Entity Policy {
      int policyNr
      - Contract contract
      BigDecimal price
    }
  }
}

UseCase CreateOfferForCustomer
UserStory UpdateContract
UserStory AddProductToOffer
```

Multiple User Stories and/or Use Cases can be assigned as a comma-separated list, as shown in the last Aggregate example above.

### Use Case and User Story Declaration
The Use Cases and User Stories you refer to have to be declared on the root level of your CML file. Have a look at our [user requirements](/docs/user-requirements/) page to see how you can declare and specify your cases and stories.

## Security Zones
The attribute _securityZone_ allows you to assign different Aggregates into different _security zones_. This language feature is primarily used to generate the [user representations for Service Cutter](/docs/service-cutter-context-map-suggestions/#input-and-preconditions), i.e. the [separated security zones](https://github.com/ServiceCutter/ServiceCutter/wiki/Separated-security-zones).

This can be very helpful to model security-related requirements which can later help in decomposing a Bounded Context.

A simple example:

```cml
BoundedContext MyMonolith {
  Aggregate CustomerManagement {
    securityZone "Internal"
    Entity Customer {
      String firstName
      String lastName
    }
    Entity Address {
      - Customer customer
      String street
      String city
    }
  }
  Aggregate CustomerFrontend {
    securityZone "Public"
    DomainEvent AddressChanged {
      - Address address
    }
  }
}
```

## Security Access Groups
The attribute _securityAccessGroup_ allows you to assign different Aggregates to different _security access groups_. This feature is primarily used to generate the [user representations for Service Cutter](/docs/service-cutter-context-map-suggestions/#input-and-preconditions), i.e. the [security access groups](https://github.com/ServiceCutter/ServiceCutter/wiki/Security-access-groups).

This can be very helpful to declare that your Aggregates have different access requirements, which can later help when decomposing a Bounded Context.

An example:

```cml
BoundedContext MyMonolith {
  Aggregate CustomerManagement {
    securityAccessGroup "InsuranceEmployees"
    Entity Customer {
      String firstName
      String lastName
    }
    Entity Address {
      - Customer customer
      String street
      String city
    }
  }
  Aggregate CustomerFrontend {
    securityAccessGroup "Customers"
    DomainEvent AddressChanged {
      - Address address
    }
  }
}
```

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

```cml
Aggregate AggregateDemo1 {
  contentVolatility = OFTEN // content changes more often in this Aggregate

  Entity DemoEntityOne
}

Aggregate AggregateDemo2 {
  contentVolatility = NORMAL

  Entity DemoEntityTwo
}
```


### Likelihood for Change
With the attribute _likelihoodForChange_ (or _structuralVolatility_) you can specify how [volatile](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-4-Structural-Volatility) an Aggregate is ([Structural Volatility](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-4-Structural-Volatility)). The attribute takes one of the following three values:

 * RARELY
 * NORMAL
 * OFTEN
 
This attribute may be used for service decomposition, since parts which are likely to change should typically be isolated in separate
components (see [Parnas](https://dl.acm.org/citation.cfm?doid=361598.361623)). Besides for [proposing new service cuts](/docs/service-cutter-context-map-suggestions), you can use this in CML by applying the 
[Extract Aggregates by Volatility](/docs/ar-extract-aggregates-by-volatility) architectural refactoring.

The likelihood on an aggregate is declared as follows:

```cml
Aggregate CustomerFrontend {
  likelihoodForChange = OFTEN

  DomainEvent CustomerAddressChange {
    aggregateRoot

    - UserAccount issuer
    - Address changedAddress
  }
}
```

You can also use the _structuralVolatility_ keyword:

```cml
Aggregate CustomerFrontend {
  structuralVolatility = OFTEN

  DomainEvent CustomerAddressChange {
    aggregateRoot

    - UserAccount issuer
    - Address changedAddress
  }
}
```

### Availability Criticality
This characteristic corresponds to the [Availability Criticality](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-7-Availability-Criticality) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _availabilityCriticality_ takes the following values:
 * LOW
 * NORMAL
 * HIGH

An example:

```cml
Aggregate AggregateDemo1 {
  availabilityCriticality = HIGH // higher availability requirements then other aggregate

  Entity DemoEntityOne
}

Aggregate AggregateDemo2 {
  availabilityCriticality = NORMAL

  Entity DemoEntityTwo
}
```

### Consistency Criticality
This characteristic corresponds to the [Consistency Criticality](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-6-Consistency-Criticality) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _consistencyCriticality_ takes the following values:
 * LOW
 * NORMAL
 * HIGH

An example:

```cml
Aggregate AggregateDemo1 {
  consistencyCriticality = HIGH // higher consistency requirements then other aggregate

  Entity DemoEntityOne
}

Aggregate AggregateDemo2 {
  consistencyCriticality = NORMAL

  Entity DemoEntityTwo
}
```

### Storage Similarity
This characteristic corresponds to the [Storage Similarity](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-11-Storage-Similarity) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _storageSimilarity_ takes the following values:
 * TINY
 * NORMAL
 * HUGE

An example:

```cml
Aggregate AggregateDemo1 {
  storageSimilarity = HUGE // similar storage requirements as AggregateDemo3

  Entity DemoEntityOne
}

Aggregate AggregateDemo2 {
  storageSimilarity = NORMAL

  Entity DemoEntityTwo
}

Aggregate AggregateDemo3 {
  storageSimilarity = HUGE // similar storage requirements as AggregateDemo1

  Entity DemoEntityThree
}
```

### Security Criticality
This characteristic corresponds to the [Security Criticality](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-15-Security-Criticality) criterion of [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

The attribute _securityCriticality_ takes the following values:
 * LOW
 * NORMAL
 * HIGH

An example:

```cml
Aggregate AggregateDemo1 {
  securityCriticality = HIGH // high security requirements

  Entity DemoEntityOne
}

Aggregate AggregateDemo2 {
  securityCriticality = NORMAL

  Entity DemoEntityTwo
}
```

