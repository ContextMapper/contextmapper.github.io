---
title: Responsibility Layers
permalink: /docs/responsibility-layers/
---

The Responsibility Layers pattern from the ["blue book"](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) can be used on bounded contexts and aggregates to specify their responsibilities.

## Syntax
The responsibilities can simply be defined with the keyword/attribute _responsibilities_ and a list of responsibilities (as strings). On bounded contexts, you can additionally declare what the context is **not** responsible for with the _notResponsibleFor_ keyword (see [Bounded Context](/docs/bounded-context/#not-responsible-for)):

```cml
BoundedContext CustomerManagementContext implements CustomerManagementDomain {
  type = FEATURE
  domainVisionStatement = "The customer management context is responsible for ..."
  implementationTechnology = "Java, JEE Application"
  responsibilities = "Customers", "Addresses"
}
```

```cml
Aggregate Customers {
  responsibilities = "Customers", "Addresses"

  Entity Customer {
    aggregateRoot

    - SocialInsuranceNumber sin
    String firstname
    String lastname
    - List<Address> addresses
  }
}
```
