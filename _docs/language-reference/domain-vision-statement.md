---
title: Domain Vision Statement
permalink: /docs/domain-vision-statement/
---

The Domain Vision Statement pattern from the ["blue book"](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) is implemented as a String attribute on the [bounded context](/docs/bounded-context), the [domain](/docs/subdomain), and the 
[subdomain](/docs/subdomain).

## Syntax
The following two code snippets show an example for a bounded context, a domain, and a subdomain accordingly:

```cml
BoundedContext CustomerContext {
  domainVisionStatement = "This context is responsible for ..."
}
```

```cml
Domain Insurance {
  domainVisionStatement = "Insurance domain vision ..."

  Subdomain Customers {
    /* subdomain specification */
  }

  Subdomain PolicyManagement {
    /* subdomain specification */
  }
}
```

```cml
Subdomain CustomerManagementDomain {
  type = CORE_DOMAIN
  domainVisionStatement = "Subdomain managing everything customer-related."
}
```

