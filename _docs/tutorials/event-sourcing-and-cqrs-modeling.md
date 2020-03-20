---
title: Event Sourcing and CQRS Modeling in Context Mapper
permalink: /docs/event-sourcing-and-cqrs-modeling/
---

Event sourcing and Command Query Responsibility Segregation (CQRS) are two different approaches, but they work very well together. Both concepts deal with application state.
Event sourcing captures all changes to the state as a sequence of (or stream) of events so that state changes can be communicated flexibly in loosely coupled systems. This is why this 
concept is interesting for microservice architectures. CQRS separates query processing from the create, update, delete business logic so that different Non-Functional Requirements (NFRs), for instance regarding performance, for read and write access can be satisfied in different ways. In complex domains, this is often desired. 

If you are not fully familiar with the concepts of event sourcing and CQRS yet, we recommend the following links:

 * [Event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) by Martin Fowler
 * [Event sourcing pattern](https://microservices.io/patterns/data/event-sourcing.html) by Chris Richardson
 * [Event sourcing workshop slides](https://speakerdeck.com/mploed/event-sourcing-workshop-at-software-architecture-summit-2016) by Michael Plöd
 * [Command query separation](https://martinfowler.com/bliki/CommandQuerySeparation.html) and [CQRS](https://martinfowler.com/bliki/CQRS.html) by Martin Fowler
 * [Developing Transactional Microservices Using Aggregates, Event Sourcing and CQRS](https://www.infoq.com/articles/microservices-aggregates-events-cqrs-part-1-richardson/) by Chris Richardson
 * [Designing Event Sourced Microservices](https://www.infoq.com/news/2017/11/event-sourcing-microservices/) by Jan Stenberg
 
## Modeling in Context Mapper
This page highlights the [Context Mapper DSL (CML)](/docs/language-reference/) concepts that support modeling event sourced systems and CQRS. 

Within CML Bounded Contexts and Aggregates we integrated the [Sculptor DSL](http://sculptorgenerator.org/) that allows to specify the domain model of the Bounded Contexts.

### Events
As explained in the [Sculptor documentation](http://sculptorgenerator.org/documentation/event-driven-tutorial), the tactic DDD syntax of Sculptor supports modeling events.

A domain event is something that happened that affects the application/resource state. [Michael Plöd](https://speakerdeck.com/mploed/event-sourcing-workshop-at-software-architecture-summit-2016)
suggests that the scope of domain events is always based on Aggregates. The names of domain events shall indicate that the event happened in the past. 

The following example illustrates how you can model domain events within your Aggregate: 

<!-- add timestamp to examples? or not needed (done in base class)? -->
```text
DomainEvent CustomerVerifiedEvent {
  - CustomerId customer
}

DomainEvent AddressUpdatedEvent {
  - CustomerId customer  
  - AddressId address
}
```

You can also reference your events in services, repositories, or any other tactic DDD objects:

```text
Service AddressService {
  @AddressUpdatedEvent updateAddress(@AddressId address);
}
```

### CQRS Example
Applying CQRS to a Bounded Context definition in Context Mapper can be expressed with the standard language constructs of Context Mapper and Sculptor: you can simply apply this architectural pattern by 

* First step: separating the queries from the command methods and defining separate services (1)
* Second step: defined separate command and query models (2)

#### 1: Separating Queries and Commands
Here is an example of a conventional service interface that exposes both create, read, update, delete, and search methods/operations:

```text
Service CustomerService {
  @CustomerId createCustomer(@Customer customer);
  void updateCustomer(@Customer customer);
  boolean deleteCustomer(@CustomerId customer);
  @Customer findCustomerById(@CustomerId customerId);
  List<@Customer> findCustomersByName(String name);
}
```

You can CQRS-ify the above the above interface by splitting it into two service interfaces:

```text
Service CustomerQueryService {
  @Customer findCustomerById(@CustomerId customerId);
  List<@Customer> findCustomersByName(String name);
}

Service CustomerCommandService {
  @CustomerId createCustomer(@Customer customer);
  void updateCustomer(@Customer customer);
  boolean deleteCustomer(@CustomerId customer);
}
```

Additionally, Sculptor introduces so-called command events specifically to support CQRS explicitly (described [here](http://sculptorgenerator.org/documentation/event-driven-tutorial#commandevent)).
In comparison to a domain event which describes something that has happened, a command event is something that the system is asked to perform. The following CML/Sculptor snippet illustrates an example how to model command events:

```text
CommmandEvent RecordShipmentArrival {
  - ShipmentId shipment
  Date arrivalDate
}
```

#### 2: Separating Read and Command Models
In a second step you may want to defined completely different models for read and command access. The Context Mapper DSL supports currently no specific language construct for read models
but we suggest that you use the Aggregate rule to specify your read models. The following example illustrates how you could model your Aggregate (command model) and the read model:

```text
Aggregate CustomerAggregate {
  ValueObject CustomerId {
    UUID uniqueCustomerId
  }

  Entity Customer {
    aggregateRoot

    CustomerId customerId
    String firstName
    String lastName
    List<Address> addresses
  }
 
  Entity Address

  Service CustomerCommandService {
    @CustomerId createCustomer(@Customer customer);
    void updateCustomer(@Customer customer);
    boolean deleteCustomer(@CustomerId customer);
  }
}

Aggregate CustomerReadModel {
  DataTransferObject CustomerDTO {
    String firstName
    String lastName
  }

  Service CustomerQueryService {
    @CustomerDTO findCustomerById(@CustomerId customerId);
    List<@CustomerDTO> findCustomersByName(String name);
  }
}
```

**Note:** If you initially create an Aggregate with separate Entities for _reading_ and _updating_ you can also use our Architectural Refactoring (AR) [Split Aggregate by Entities](/docs/ar-split-aggregate-by-entities/)
to separate the read model (Aggregate) from the command model Aggregate.

### Event Sourcing with Sculptor
The [Sculptor generator](http://sculptorgenerator.org) further supports event sourcing specifically as described here: 
[Event Sourcing with Sculptor](http://sculptorgenerator.org/2010/10/28/event-sourcing-with-sculptor). 
However, the DSL syntax itself does not need additional concepts to support it. It is based on the _DomainEvents_, _Repositories_, and _Services_ provided by the Sculptor and also CML.
  * **Note:** We only used the Sculptor syntax for the tactic DDD grammar of our CML language. Using the Sculptor generator in Context Mapper is currently not supported.
