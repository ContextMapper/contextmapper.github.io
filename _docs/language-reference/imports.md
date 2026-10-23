---
title: Imports
permalink: /docs/imports/
---

CML models can be divided into multiple `*.cml` files. For example, you may want to specify Bounded Contexts in separate files and use them in multiple Context Maps.
One `*.cml` file can only contain one Context Map. However, multiple Context Maps in separate `*.cml` files can import the same files describing the Bounded Contexts.

## Example

The following CML snippet could be in a file `BoundedContexts.cml` and specify some Bounded Contexts:

```cml
BoundedContext CustomerManagementContext implements CustomerManagementDomain {
  Aggregate Customers {
    Entity Customer {
      aggregateRoot

      - SocialInsuranceNumber sin
      String firstname
      String lastname
      - List<Address> addresses
    }

    Entity Address {
      String street
      int postalCode
      String city
    }
  }
}

BoundedContext PolicyManagementContext implements PolicyManagementDomain {
  Aggregate Contract {
    Entity Contract {
      aggregateRoot

      - ContractId identifier
      - Customer client
      - List<Product> products
    }

    Entity Policy {
      int policyNr
      - Contract contract
      BigDecimal price
    }
  }
}
```

A file containing the ContextMap can then import the Bounded Contexts with the **import keyword**:

```cml
import "./BoundedContexts.cml"

ContextMap InsuranceContextMap {
  contains CustomerManagementContext
  contains PolicyManagementContext

  PolicyManagementContext [D,CF]<-[U,OHS,PL] CustomerManagementContext {
    implementationTechnology = "RESTfulHTTP"
    exposedAggregates = Customers
  }
}
```

It is also possible to import `*.cml` files located in other directories:

```cml
import "./BoundedContexts/CustomerManagement.cml"
import "./BoundedContexts/PolicyManagement.cml"

ContextMap InsuranceContextMap {
  contains CustomerManagementContext
  contains PolicyManagementContext

  PolicyManagementContext [D,CF]<-[U,OHS,PL] CustomerManagementContext {
    implementationTechnology = "RESTfulHTTP"
    exposedAggregates = Customers
  }
}
```

<div class="alert alert-custom">
<strong>Note:</strong> Although you can import <strong>*.cml</strong> files from different directories, our Eclipse plugin will only be able to resolve files within the same Eclipse project.
</div>
