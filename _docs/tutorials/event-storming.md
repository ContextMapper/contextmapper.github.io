---
title: Model Event Storming Results in Context Mapper
permalink: /docs/event-storming/
---

Event storming is a workshop technique to explore domains originally invented by Alberto Brandolini. If you are not familiar with the technique we recommend the following literature and links:

 * [Introducing Event Storming](https://ziobrando.blogspot.com/2013/11/introducing-event-storming.html) by Alberto Brandolini (original blog post)
 * [Introducing Event Storming](https://leanpub.com/introducing_eventstorming) by Alberto Brandolini (Leanpub book)
 * [Domain-Driven Design Distilled](https://www.amazon.com/Domain-Driven-Design-Distilled-Vaughn-Vernon/dp/0134434420) by Vaughn Vernon
 * [Event Storming Cheatsheet](https://github.com/wwerner/event-storming-cheatsheet) by Wolfgang Werner (good cheatsheet for a quick introduction into the topic)
 
## Use Context Mapper to Model Event Storming Output
The output of an event storming basically describes the domain using the following DDD concepts:

 * Domain Events
 * Commands (that cause the domain events)
 * Aggregates
 * Issues
 * User Roles?
 * Views ?
 * Bounded Contexts
 * Subdomains
 * Event Flow

Context Mapper supports modeling these concepts and can therefore be used to document the output of an event storming.

### Domain Events
The tactic DDD syntax of CML which is based on the [Sculptor DSL](http://sculptorgenerator.org/) supports to model _DomainEvent_'s within your Aggregates.
The following two examples illustrate how you can specify a domain event:

```text
DomainEvent CustomerVerifiedEvent {
  - CustomerId customer
}

DomainEvent AddressUpdatedEvent {
  - CustomerId customer  
  - AddressId address
}
```

On the [Event Sourcing and CQRS Modeling in Context Mapper](/docs/event-sourcing-and-cqrs-modeling/) page we also describe how event sourcing and CQRS based systems can be 
modeled in Context Mapper.

### Commands
The domain events are often a consequence of a user action or _command_. Commands in CML can either be modeled as methods in services or as _CommandEvent_'s.

### Aggregates
TODO

### Issues
TODO

### User Roles
TODO

### Views
TODO

### Bounded Contexts
TODO

### Subdomains
TODO

### Event Flow
TODO