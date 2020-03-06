---
title: Model Event Storming Results in Context Mapper
permalink: /docs/event-storming/
---

Event storming is a workshop technique to explore domains originally invented by Alberto Brandolini. If you are not familiar with the technique we recommend the following literature and links:

 * [Introducing Event Storming](https://ziobrando.blogspot.com/2013/11/introducing-event-storming.html) by Alberto Brandolini (original blog post)
 * [Introducing Event Storming](https://leanpub.com/introducing_eventstorming) by Alberto Brandolini (Leanpub book)
 * [Domain-Driven Design Distilled](https://www.amazon.com/Domain-Driven-Design-Distilled-Vaughn-Vernon/dp/0134434420) by Vaughn Vernon
 * [Event Storming Cheatsheet](https://github.com/wwerner/event-storming-cheatsheet) by Wolfgang Werner (good cheat sheet for a quick introduction into the topic)
 
## Use Context Mapper to Model Event Storming Output
The output of an event storming basically describes the domain using the following DDD concepts:

 * Domain Events
 * Commands (that cause the Domain Events)
 * Aggregates 
 * Issues (optional)
 * User Roles (optional)
 * Views (optional)
 * Bounded Contexts
 * Subdomains
 * Event Flows (optional)

Context Mapper supports many of these concepts, and can therefore be used to document the output of an event storming workshop. Once captured in Context Mapper, the workshop results can be processed further, for instance to generate UML diagrams or service contracts.

### Domain Events
The tactic DDD syntax of CML is based on the [Sculptor DSL](http://sculptorgenerator.org/). Hence, you can model _DomainEvent_'s within your Aggregates.
The following two examples illustrate how to specify a domain event:

```text
DomainEvent CustomerVerifiedEvent {
  - CustomerId customer
}

DomainEvent AddressUpdatedEvent {
  - CustomerId customer  
  - AddressId address
}
```

*Note:* On the [Event Sourcing and CQRS Modeling in Context Mapper](/docs/event-sourcing-and-cqrs-modeling/) page we describe how event sourcing and CQRS based systems can be modeled in Context Mapper.

### Commands
Domain events often result from a user action or _command_ execution. Commands in CML can either be modeled as methods in services or as _CommandEvent_'s. The following examples illustrate how you can model commands in CML:

```text
Service CustomerCommandService {
  void updateCustomer(@Customer customer);
}

CommandEvent UpdateCustomer {
  - Customer customer
}
```

### Aggregates
Aggregates are supported by CML and can be modeled within Bounded Contexts. The syntax is documented [here](/docs/aggregate/). Optionally, you may want to add entities to them. 

<!-- TODO show example? rationale: some event storming material features entities rather than aggregates -->

### Issues
At present, Context Mapper does not have any language construct for issues. You can capture them as comments; however, it might make more sense to capture them in the issue tracking tool or Kanban board of the project straight away.

<!-- TODO show example: 
// TODO to be decided (tbd): which command causes this event to be emitted? 
-->

### User Roles
At present, there is no concept of a user role in the Context Mapper DSL; however, use cases can be sketched<!-- how? -->. As fallback, tagged comments can be used. <!-- but comments are not visible to the generators and the Freemarker templating, so of limited use? -->

### Views
tbd: as comments? <!-- how about a special `ViewAggregate` that exposes viewing services only (the R in CQRS)? -->

### Bounded Contexts
Bounded Contexts are first class citizens in CML. Their syntax in documented [here](/docs/bounded-context/).

### Subdomains
Just like Bounded Contexts, Subdomains are root objects in CML. The Subdomain syntax is documented [here](/docs/subdomain/).

### Event Flow
Events flow between contexts. Hence, you can use the upstream-downstream influence flow relationships of strategic DDD to model them. 
<!-- TODO tbd: maybe enhance Sculptor so that an Event can reference its predecessor? thereby one could model a flow (chain of events) -->
