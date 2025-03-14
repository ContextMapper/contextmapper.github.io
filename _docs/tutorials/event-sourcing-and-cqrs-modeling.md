---
title: Event Sourcing and CQRS Modeling in Context Mapper
permalink: /docs/event-sourcing-and-cqrs-modeling/
image: /img/cm-og-image.png
---

Event sourcing and Command Query Responsibility Segregation (CQRS) are two different approaches, but they work together very well. Both concepts deal with application state.
Event sourcing captures all changes to the state as a sequence of (or stream) of events so that state changes can be communicated flexibly without tightly coupling sender and receiver of the change message. This is one reason why this concept is interesting for microservice architectures. 
CQRS separates query processing from the create, update, delete business logic so that different Non-Functional Requirements (NFRs), for instance regarding performance, for read and write access can be satisfied in different ways. In complex domains, this is often desired. 

If you are not fully familiar with the concepts of event sourcing and CQRS yet, you may find the following resources helpful:

 * [Event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) by Martin Fowler
 * [Event sourcing workshop slides](https://files.speakerdeck.com/presentations/8423591f0e0044a68efc188a430f6768/ArchitectureSummit_EventSourcingAndCQRS_Kopie.pdf) by Michael Plöd
 * [Event sourcing pattern](https://microservices.io/patterns/data/event-sourcing.html) by Chris Richardson
 * [CQRS and Event Sourcing (Video)](https://www.youtube.com/watch?v=JHGkaShoyNs) by Greg Young
 * [Command query separation](https://martinfowler.com/bliki/CommandQuerySeparation.html) and [CQRS](https://martinfowler.com/bliki/CQRS.html) by Martin Fowler
 * [Developing Transactional Microservices Using Aggregates, Event Sourcing and CQRS](https://www.infoq.com/articles/microservices-aggregates-events-cqrs-part-1-richardson/) by Chris Richardson
 * [Designing Event Sourced Microservices](https://www.infoq.com/news/2017/11/event-sourcing-microservices/) by Jan Stenberg

Chapter 22 in "Patterns, Principles, and Practices of Domain-Driven Design" by Scott Millett and Nick Tune (Wrox 2015) is about event sourcing; Chapter 24 in that book features CQRS. "Implementing Domain-Driven Design" by Vaughn Vernon (Addison Wesley 2013) covers event sourcing and CQRS in Chapter 4 and Appendix A.
 
## Tutorial
### Context and Objectives
This tutorial highlights the [Context Mapper DSL (CML)](/docs/language-reference/) concepts that support a) modeling event-sourced systems and b) CQRS. 

Within CML Bounded Contexts and Aggregates, we integrated the [Sculptor DSL for tactic DDD](https://sculptor.github.io/) that allows domain-driven designers to specify the domain model of Bounded Contexts. This tutorial features this DSL.

### Events
As explained in the [Sculptor documentation](https://sculptor.github.io/documentation/event-driven-tutorial), the syntax of Sculptor supports modeling events.

A domain event is something that happened that affects the application/resource state. [Michael Plöd](https://speakerdeck.com/mploed/event-sourcing-workshop-at-software-architecture-summit-2016)
suggests that the scope of domain events should always be based on Aggregates. The names of domain events shall indicate that the event happened in the past. 

The following example illustrates how you can model domain events within your Aggregate: 

```text
abstract DomainEvent AbstractDomainEvent {
  Date timestamp
}

DomainEvent CustomerVerifiedEvent extends AbstractDomainEvent {
  - CustomerId customer
}

DomainEvent AddressUpdatedEvent extends AbstractDomainEvent {
  - CustomerId customer  
  - AddressDto address
}

ValueObject AddressDto {
  String streetAddress
  String city
  String postalCode
}
```

You can also reference your events in services, repositories, or any other tactic DDD objects:

```text
Service AddressService {
  @AddressUpdatedEvent updateAddress(@AddressDto address);
}
```

### CQRS Example
Applying CQRS to a Bounded Context definition in Context Mapper can be expressed with the standard language constructs of Context Mapper and Sculptor: you can simply apply 
this architectural pattern by 

1. Separating the queries from the command methods and defining separate services
2. Defining separate command and query models

#### Step 1: Separating Queries and Commands
Here is an example of a conventional service interface that exposes both create, read, update, delete, and search methods/operations:

```text
ValueObject CustomerDTO {
  String customerId
  CustomerProfileDto customerProfile
  List<Link> links
}

Service CustomerService {
  @CustomerId createCustomer(@CustomerDTO customer);
  void updateCustomer(@CustomerDTO customer);
  boolean deleteCustomer(@CustomerId customer);
  @CustomerDTO findCustomerById(@CustomerId customerId);
  List<@CustomerDTO> findCustomersByName(String name);
}
```

You can CQRS-ify the above interface by splitting it into two service interfaces:

```text
Service CustomerCommandService {
  @CustomerId createCustomer(@CustomerDTO customer);
  void updateCustomer(@CustomerDTO customer);
  boolean deleteCustomer(@CustomerId customer);
}

Service CustomerQueryService {
  @CustomerDTO findCustomerById(@CustomerId customerId);
  List<@CustomerDTO> findCustomersByName(String name);
}
```

Additionally, Sculptor introduces so-called *command events* to support CQRS explicitly (described [here](https://sculptor.github.io/documentation/event-driven-tutorial#commandevent)).
In comparison to a domain event which describes something that has happened, a command event is something that the system is asked to perform. The following CML/Sculptor snippet illustrates an example how to model command events:

```text
CommandEvent RecordAddressChange {
  -AddressDto newAddress
  Date changeDate
}	
```

#### Step 2: Separating Read and Command Models
In a second step you may want to define completely different models for read and command access. At present, the Context Mapper DSL does not have any specific language construct for read models; we suggest that you use the Michael's Aggregate rule from above to specify read models. The following example illustrates how you could model your Aggregate (command model) and your read model:

```text
Aggregate CustomerAggregate {
  ValueObject CustomerId {
    UUID uniqueCustomerId
  }

  Entity Address // not designed in detail 

  Service CustomerCommandService {
    @CustomerId createCustomer(@CustomerDTO customer);
    void updateCustomer(@CustomerDTO customer);
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

*Note:* If you initially create an Aggregate with separate Entities for _reading_ and _updating_, you can also use our Architectural Refactoring (AR) [Split Aggregate by Entities](/docs/ar-split-aggregate-by-entities/)
to separate the read model (Aggregate) from the command model Aggregate.

*Note:* The two Aggregates representing the command model and the read model should probably be contained in the same Bounded Context; otherwise, two Bounded Contexts have to access a shared database, which is considered a microservices antipattern.  

### Event Sourcing with Sculptor
The [Sculptor generator](https://sculptor.github.io/) further supports event sourcing specifically as described here: 
[Event Sourcing with Sculptor](https://sculptor.github.io/2010/10/28/event-sourcing-with-sculptor). 
However, the DSL syntax itself does not need additional concepts to support it. It is based on the _DomainEvents_, _Repositories_, and _Services_ provided by the Sculptor and also CML.
  * *Note:* We only used the Sculptor syntax for the tactic DDD grammar of our CML language. Using the Sculptor generator in Context Mapper is currently not supported.


<!-- You can also model the CQRS infrastructure in Sculptor: 
	Aggregate CQRS_CommonInfrastructure {
		DomainEvent AbstractDomainEvent {
			Date timestamp
		}
		ValueObject EventSequence {
			-Set<@AbstractDomainEvent> events
		}   
	}
	Aggregate CQRS_CommandInfrastructure { 
		Service CommandDAO {
			@EventSequence storeAndForwardEvents() publish to EventHandlerChannel;
			// store in EventStore and let QueryInfrastructure know (via Handler)
		} 
		Entity EventStore { 
			aggregateRoot
			Repository EventStoreRepository {}
		}
	}
	Aggregate CQRS_QueryInfrastructure {
		Entity QueryDAO {
			// talks to ReadStorage (BAU)
		}
		Entity ReadStorage { 
			aggregateRoot
			Repository ReadStorageRepository {
				subscribe to EventHandlerChannel
			}
		}
	}
-->

## Other Tutorials and Links
 * Tutorial: [Document Event Storming Results with Context Mapper](/docs/event-storming/)
 * Presentation on Context Mapper: [Context Mapper: DSL and Tools for Domain-Driven Service Design - Bounded Context Modeling and Microservice Decomposition](https://contextmapper.org/media/ZIOSK-ContextMapper4JUGv10p.pdf)
  * Paper introducing the Context Mapper DSL (CML): [Domain-specific Language and Tools for Strategic Domain-driven Design, Context Mapping and Bounded Context Modeling](https://doi.org/10.5220/0008910502990306)
 
