---
title: Event Sourcing and CQRS Modeling in Context Mapper
permalink: /docs/event-sourcing-and-cqrs-modeling/
---

Event sourcing and CQRS (Command Query Responsibility Segregation) are two different approaches but they work very well together. However, both concepts deal with application state.
Event sourcing captures all changes to the state as a sequence of (or stream) of events so that state changes can be communicated flexibly in loosely coupled systems. This is why this 
concept is interesting for microservice architectures. CQRS separates query processing from the create, update, delete business logic so that NFRs for both read and write access
can be satisfied in complex domains.

If you are not familiar with the concepts of event sourcing and CQRS we recommend the following links:

 * [Event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) by Martin Fowler
 * [Event sourcing pattern](https://microservices.io/patterns/data/event-sourcing.html) by Chris Richardson
 * [Event sourcing workshop slides](https://speakerdeck.com/mploed/event-sourcing-workshop-at-software-architecture-summit-2016) by Michael Plöd
 * [Command query separation](https://martinfowler.com/bliki/CommandQuerySeparation.html) and [CQRS](https://martinfowler.com/bliki/CQRS.html) by Martin Fowler
 * [Developing Transactional Microservices Using Aggregates, Event Sourcing and CQRS](https://www.infoq.com/articles/microservices-aggregates-events-cqrs-part-1-richardson/) by Chris Richardson
 * [Designing Event Sourced Microservices](https://www.infoq.com/news/2017/11/event-sourcing-microservices/) by Jan Stenberg
 
## Modeling in Context Mapper
With this page we want to highlight the [Context Mapper DSL (CML)](/docs/language-reference/) concepts that support modeling event sourced systems and CQRS. 
Within CML Bounded Contexts and Aggregates we integrated the [Sculptor DSL](http://sculptorgenerator.org/) that allows to specify the domain model of the Bounded Contexts.

### Events
As documented in the [Sculptor documentation](http://sculptorgenerator.org/documentation/event-driven-tutorial) the syntax supports modeling events.

A domain event is something that happened that affects the application/resource state. [Plöd](https://speakerdeck.com/mploed/event-sourcing-workshop-at-software-architecture-summit-2016)
suggests that the scope of domain events is always based on Aggregates. The names of domain events shall indicate that the event happened in the past. The following example illustrates
how you can model domain events within your Aggregate:

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
Applying CQRS to a Bounded Context definition in Context Mapper does not require additional language constructs. You can simply apply it by separating the queries from the command 
methods and define separate services. 

```text
Service CustomerService {
  @Customer saveCustomer(@Customer customer);
  void updateCustomer(@Customer customer);
  @Customer findCustomerById(@CustomerId customerId);
  List<@Customer> findCustomersByName(String name);
}
```

For example instead of specifying the classic interface above, you can CQRS-ify it by splitting it into two interfaces:

```text
Service CustomerQueryService {
  @Customer findCustomerById(@CustomerId customerId);
  List<@Customer> findCustomersByName(String name);
}

Service CustomerCommandService {
  @Customer saveCustomer(@Customer customer);
  void updateCustomer(@Customer customer);
}
```

Sculptor additionally introduced so-called command events specifically to support CQRS (described [here](http://sculptorgenerator.org/documentation/event-driven-tutorial#commandevent)).
In comparison to a domain event which describes something that has happened a command event is something that the system is asked to perform. The following CML/Sculptor snippet 
illustrates an example how to model command events:

```text
CommmandEvent RecordShipmentArrival {
  - ShipmentId shipment
  Date arrivalDate
}
```

### Event Sourcing with Sculptor
The [Sculptor generator](http://sculptorgenerator.org) further supports event sourcing specifically as described here: 
[Event Sourcing with Sculptor](http://sculptorgenerator.org/2010/10/28/event-sourcing-with-sculptor). However, the DSL syntax itself does not need additional concepts to support it. 
It is based on the _DomainEvent_'s, _Repository_'s, and _Services_'s provided by the Sculptor and also CML. 
