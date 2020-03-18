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
The output of an event storming describes the domain using the following DDD concepts:

 * [Domain Events](#domain-events)
 * [Commands](#commands) (that cause the Domain Events)
 * [Aggregates](#aggregates) (or Aggregate root Entities)
 * [Issues](#issues) (optional)
 * [User Roles](#user-roles) (optional)
 * [Views / Read Models](#views--read-models) (optional)
 * [Bounded Contexts](#bounded-contexts)
 * [Subdomains](#subdomains)
 * [Event Flows](#event-flow) (optional)

*Note:* Some event stormers also introduce policies (a.k.a. business rules) as special, self-triggered types of commands.

Context Mapper supports most of these concepts, and can therefore be used to document the output of an event storming workshop. Once captured in Context Mapper, the workshop results can be processed further, for instance to generate UML diagrams or service contracts.

In the following we present an [example Event Storming](#example-lakeside-mutual) and how the result can be [modeled in CML](#event-storming-concepts-to-cml-mapping).

## Example: Lakeside Mutual
The [Lakeside Mutual project](https://github.com/Microservice-API-Patterns/LakesideMutual) is a fictitious insurance application that illustrates microservices and the application
of [Microservice API Patterns (MAP)](https://microservice-api-patterns.org/). The application does currently not support claim processing. To add this as a new feature to the application
we conducted an Event Storming.

The following graphic illustrates the result of the Event Storming: (click on image to enlarge)

<a target="_blank" href="/img/lakeside-mutual-event-storming-result.jpg">![Lakeside Mutual Claim Processing Event Storming](/img/lakeside-mutual-event-storming-result.jpg)</a>

The next sections will illustrate how we suggest to model the individual results of the Event Storming in CML.
The complete CML model resulting from this Event Storming can be found here: [https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/lakeside-mutual](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/lakeside-mutual).

## Event Storming Concepts to CML Mapping
The following examples and modeling suggestions are based on the Event Storming presented [above](#example-lakeside-mutual) (Lakeside Mutual).

### Domain Events
The domain events are typically the first objects that are discovered in an Event Storming.
The tactic DDD syntax of CML is based on the [Sculptor DSL](http://sculptorgenerator.org/), which [supports event-driven concepts](http://sculptorgenerator.org/documentation/event-driven-tutorial). 
Hence, you can model _DomainEvent_'s within your Aggregates.
The following examples illustrate how we modeled the domain events from our Event Storming for Lakeside Mutual:

```text
abstract DomainEvent AbstractClaimEvent {
  Date timestamp
  - Claim claim
}

DomainEvent ClaimRegistered extends @AbstractClaimEvent // triggers CheckInsurance command

DomainEvent AssessmentPerformed extends @AbstractClaimEvent // triggers AcceptClaim or RejectClaim command

DomainEvent ClaimAccepted extends @AbstractClaimEvent // triggers SchedulePayment command

DomainEvent ClaimRejected extends @AbstractClaimEvent // triggers NofifyCustomer command
```

<!-- *Note:* On the [Event Sourcing and CQRS Modeling in Context Mapper](/docs/event-sourcing-and-cqrs-modeling/) page we describe how event sourcing and CQRS based systems 
can be modeled in Context Mapper.-->

### Commands
Domain events often result from a user action or _command_ execution. Commands in CML can either be modeled as methods in services or as _CommandEvent_'s (or both). The following examples illustrate how you can model commands in CML:

```text
abstract CommandEvent AbstractClaimCommand {
  - Claim claim
}

"role: Administrator in charge"
CommandEvent CheckClaimDocumentation extends @AbstractClaimCommand

"role: Responsible person in claims department"
CommandEvent CheckInsurance extends @AbstractClaimCommand {
  - Set<PolicyId> policies
}

"role: Responsible person in claims department"
CommandEvent AcceptClaim extends @AbstractClaimCommand

"role: Responsible person in claims department"
CommandEvent RejectClaim extends @AbstractClaimCommand

Service ClaimService {
  @ClaimRegistered checkDocumentation(@CheckClaimDocumentation command);

  @AssessmentPerformed checkInsurance(@CheckInsurance command);

  @ClaimAccepted acceptClaim(@AcceptClaim command);

  @ClaimRejected rejectClaim(@RejectClaim commandcal);
}
```

Each command is represented as an operation; we grouped them by Aggregates (see below) in this case. `@CheckClaimDocumentation`represents the command input, which we modelled as a command event. Alternatively, a value object or an entity could have been defined.  The return type of service operation indicates that the result of a command is a certain event. For example: If the `CheckClaimDocumentation` command is performed, an event `ClaimRegistered` will be the result. 

Policies can be modelled in the same way, and optionally their if-then rule character be modeled explitly. <!--  show how? -->

### Aggregates
Aggregates are supported by CML and can be modeled within Bounded Contexts. The syntax is documented [here](/docs/aggregate/). Optionally, you may want to add entities to them.

The following example illustrates the `Notification` Aggregate derived from our Event Storming example above:

```text
Aggregate Notification {
  Entity Notification {
    aggregateRoot
    
    - Claim claim
  }
  
  CommandEvent NofifyCustomer
  
  DomainEvent CustomerNotified {
    Date timestamp
  }
  
  Service NotificationService {
    @CustomerNotified notifyCustomer(@NofifyCustomer command);
  }
}
``` 

*Note:* Some Event Storming tutorials/guides also feature Entities instead of Aggregates. Typically these Entities become Aggregate roots (often the Aggregate even has the same name as the Aggregate root Entity). In CML, it does not really matter whether you work with Aggregates or Entities in your Event Storming model: You have to create an Aggregate in all cases. Within this Aggregate you can then create your Entity, as shown in the example above.

### Issues
At present, we do not have a language construct for issues since they mostly only used as notes for potential future model changes and are not further processed (do not influence the model structurally). However, you can capture them as comments, although it might make more sense to capture them in the issue tracking tool or Kanban board of the project straight away.

The Lakeside Mutual Event Storming output above contains two issues (the two red cards) <!-- add this pointer to the card above too? --> for which we created the following comment in our CML model:

```text
/**
 * The 'Claims Management' context below is a result of our Event Storming for the new
 * claim processing feature.
 * 
 * Issue: We currently modeled the feature within a new Bounded Context, although it 
 * would also be possible to implement it as part of the Policy Management Context. 
 */
BoundedContext ClaimsManagement {
  // Bounded Context content removed for this example ...
}
```

### User Roles
At present, there is no concept of a user role in the Context Mapper DSL; however, we used [Sculptor](http://sculptorgenerator.org/)'s `doc` comment which can be added to all domain objects. Thereby we declare the user roles on our commands:
<!--- this is good but limits possibility to use doc string for MAP decorators later (?) -->

```text
"role: Administrator in charge"
CommandEvent CheckClaimDocumentation extends @AbstractClaimCommand

"role: Responsible person in claims department"
CommandEvent CheckInsurance extends @AbstractClaimCommand {
  - Set<PolicyId> policies
}

"role: Responsible person in claims department"
CommandEvent AcceptClaim extends @AbstractClaimCommand

"role: Responsible person in claims department"
CommandEvent RejectClaim extends @AbstractClaimCommand
```

### Views / Read Models
In our Event Storming for claims processing at Lakeside Mutual we did not work with read models; Context Mapper does not support read models explicitely yet. However, it is of course possible that you define your read model simply by using separate Aggregates or Entities. For example:

```text
Aggregate ClaimReadModel {
  Entity ClaimReadModel {
    String claimIdentifier
    ...
  }
}
```

### Bounded Contexts
Bounded Contexts are first class citizens in CML. Their syntax in documented [here](/docs/bounded-context/).

### Subdomains
Just like Bounded Contexts, Subdomains are root objects and first class citizens in CML. The Subdomain syntax is documented [here](/docs/subdomain/).

### Event Flow
In an Event Storming you order the events in the order they occur (in time). We did the same thing in the Event Storming above (Lakeside Mutual). The time line in the illustrated graphic above proceeds from left to right. 

Context Mapper does not provide any support for modeling this event flow (time) explicitly yet. For this reason we simply worked with comments to indicate which command is triggered after an event has been emitted:

```text
"role: Administrator in charge"
CommandEvent CheckClaimDocumentation extends @AbstractClaimCommand
	
DomainEvent ClaimRegistered extends @AbstractClaimEvent // triggers CheckInsurance command
	
"role: Responsible person in claims department"
CommandEvent CheckInsurance extends @AbstractClaimCommand {
	- Set<PolicyId> policies
}

DomainEvent AssessmentPerformed extends @AbstractClaimEvent // triggers AcceptClaim or RejectClaim command
	
"role: Responsible person in claims department"
CommandEvent AcceptClaim extends @AbstractClaimCommand

DomainEvent ClaimAccepted extends @AbstractClaimEvent // triggers SchedulePayment command
	
"role: Responsible person in claims department"
CommandEvent RejectClaim extends @AbstractClaimCommand

DomainEvent ClaimRejected extends @AbstractClaimEvent // triggers NofifyCustomer command
```

The order in which we listed the events/commands above and the comments `// triggers ...` indicate the time line in this example.

## Whats's Next? 

Once your CML that models the event storming output validates, you can:

* Refine it, or instance by defining the data (atributes, operation parameters and return types) in more detail
* Refactor it, starting with use cases and team assignments (AR-2, AR-3)
* Generate output from it, for instance a domain glossary, a contetx map, or MDSL contracts

