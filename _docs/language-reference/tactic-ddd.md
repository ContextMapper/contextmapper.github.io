---
title: Tactic DDD Syntax
permalink: /docs/tactic-ddd/
---

The Context Mapper syntax for the tactic DDD part is based on the [Sculptor DSL](http://sculptorgenerator.org/). For this reason we do not
document all details of the tactic language part, since all the information can be found in Sculptor's [documentation](http://sculptorgenerator.org/documentation/advanced-tutorial).
However, we still provide a short introduction into the most important elements on this page.

## Aggregates
The stategic DDD's [bounded contexts](/docs/bounded-context) typically contain multiple aggregates. Within the aggregates, you can model
your system with the tactic DDD patterns, such as _Entity_, _Value Object_, _Domain Event_, _Service_ and _Repository_.

The page [Aggregate](/docs/aggregate) describes how you can create aggregates. The following sections introduce the other patterns syntax 
briefly. All of those language elements can be used within the aggregate.

## Entity
An entity is declared with the _Entity_ keyword, as illustrated below. With the optional keyword _aggregateRoot_ you can specify which entity
within your aggregate is the root entity. The language provides primitive data types such as _String_, _int_ and _boolean_ etc., similar to 
Java. You can further use the collection types _List_, _Set_ and _Bag_.

<div class="highlight"><pre><span></span><span class="k">Entity</span> Customer {
  <span class="k">aggregateRoot</span>

  <span>SocialInsuranceNumber</span> <span>sin</span>
  <span class="k">String</span> firstname
  <span class="k">String</span> lastname
  <span class="k">List</span>&lt;Address&gt; <span>addresses</span>
}
</pre></div>

As illustrated in the example above, you can declare your own types (such as _Address_ and _SocialInsuranceNumber_ above). These types don't
have to be further specified anywhere. However, you can also use references to existing types (entities, value objects, etc.) as described 
below.

### Type References
To reference another type of your model within an attribute, you have to use the **-** (minus) sign:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Customers {
  <span class="k">Entity</span> Customer { 
    <span class="k">aggregateRoot</span>
    
    - <span class="k">SocialInsuranceNumber</span> sin <span class="c">// Reference syntax for simple attribute</span>
    <span class="k">String</span> firstname
    <span class="k">String</span> lastname
    - <span class="k">List&lt;Address&gt;</span> addresses <span class="c">// Reference syntax for collections</span>
  }
  
  <span class="k">Entity</span> Address {
    <span class="k">String</span> street
    <span class="k">int</span> postalCode
    <span class="k">String</span> city
  }
  
  <span class="k">ValueObject</span> SocialInsuranceNumber {
    <span class="k">String</span> sin <span class="k">key</span>
  }
}
</pre></div>


When you use this reference notation with the _-_ (minus) sign, the language checks that the types (_Address_ and _SocialInsuranceNumber_
above) are declared.

### Operations / Methods
Of course you can also declare methods/operations on your _Entities_, _Value Objects_ and _Domain Events_. The declaration of methods
is started with the **def** keyword. As illustrated below, you can use abstract data types which are not further declared in your 
method parameters and return types:

<div class="highlight"><pre><span></span><span class="k">Entity</span> Customer { 
  <span class="k">aggregateRoot</span>
  
  - <span class="k">SocialInsuranceNumber</span> sin
  <span class="k">String</span> firstname
  <span class="k">String</span> lastname
  - <span class="k">List&lt;Address&gt;</span> addresses
  
  <span class="k">def</span> AddressId createAddress(Address address);
  <span class="k">def</span> void changeCustomer(Customer customer, Address address);
}
</pre></div>

If you want to **refer** existing types in your operation/method parameters and return types, you have to use the **@** character:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Customers {
  <span class="k">Entity</span> Customer { 
    <span class="k">aggregateRoot</span>
    
    - <span class="k">SocialInsuranceNumber</span> sin
    <span class="k">String</span> firstname
    <span class="k">String</span> lastname
    - <span class="k">List&lt;Address&gt;</span> addresses
    
    <span class="k">def</span> @AddressId createAddress(@Address address); <span class="c">// Method/Operation declaration with references</span>
    <span class="k">def</span> void changeCustomer(@Customer customer, @Address address); <span class="c">// Method/Operation declaration with references</span>
  }
  
  <span class="k">Entity</span> Address {
    <span class="k">String</span> street
    <span class="k">int</span> postalCode
    <span class="k">String</span> city
  }
  
  <span class="k">ValueObject</span> SocialInsuranceNumber {
    <span class="k">String</span> sin <span class="k">key</span>
  }
  
  <span class="k">ValueObject</span> AddressId {
    <span class="k">int</span> id
  }
}
</pre></div>

## Value Objects
The declaration of value objects is done with the _ValueObject_ keyword:

<div class="highlight"><pre><span></span><span class="k">ValueObject</span> HandlingHistory {
  - <span class="k">List&lt;HandlingEvent&gt;</span> handlingEvents
}
</pre></div>

### Attributes & Methods/Operations
Attributes (incl. type references) and methods/operations in value objects can be specified exactly the same way as within entities (see sections above).

## Domain Events
The declaration of domain events is done with the _DomainEvent_ keyword:

<div class="highlight"><pre><span></span><span class="k">DomainEvent</span> HandlingEvent {
  <span class="k">Type</span> handlingType;
  - <span class="k">Voyage</span> voyage;
  - <span class="k">LocationShared</span> location;
  <span class="k">Date</span> completionTime;
  <span class="k">Date</span> registrationTime;
  - <span class="k">Cargo</span> cargo;
}
</pre></div>

### Attributes & Methods/Operations
Attributes (incl. type references) and methods/operations in domain events can be specified exactly the same way as within entities (see sections above).

## Services
Within your aggregate you can also specify services according to the tactic DDD _Service_ pattern. Services are declared with the _Service_
keyword and contain one or more methods/operations. These methods/operations are declared exactly the same way as within entities, value
objects or domain events, **but without the _def_ keyword**:

<div class="highlight"><pre><span></span><span class="k">Service</span> RoutingService {
  <span class="k">List&lt;@Itinerary&gt;</span> fetchRoutesForSpecification(@RouteSpecification routeSpecification) <span class="k">throws</span> LocationNotFoundException;
}
</pre></div>

With the _throws_ keyword you can specify that the method/operation can throw a specific exception (as in Java).
 
## Repositories
You can specify a repository with the _Repository_ keyword **within your aggregate root**. Only aggregate roots can contain repositories, 
which is ensured by a semantic checker of the language. A repository can contain one or more methods/operations, as illustrated in
the example below. These methods/operations are declared exactly the same way as within entities, value objects or domain events, 
**but without the _def_ keyword**:

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Location {
  <span class="k">Entity</span> Location {
    <span class="k">aggregateRoot</span>
    
    <span class="k">PortCode</span> portcode
    - <span class="k">UnLocode</span> unLocode;
    <span class="k">String</span> name;
    
    <span class="k">Repository</span> LocationRepository {
      @Location find(@UnLocode unLocode);
      <span class="k">List&lt;@Location&gt;</span> findAll();
    }
  }
  
  <span class="k">ValueObject</span> UnLocode {
    <span class="k">String</span> unLocode
  }
  
  <span class="k">ValueObject</span> LocationShared {
    <span class="k">PortCode</span> portCode
    - <span class="k">Location</span> location
  }
}
</pre></div>

## More Details about the Tactic DDD Syntax
If you want to read more details about the syntax of the tactic DDD part within bounded contexts, we refer to the [Sculptor documentation](http://sculptorgenerator.org/documentation/advanced-tutorial).
