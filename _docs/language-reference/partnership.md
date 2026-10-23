---
title: Partnership
permalink: /docs/partnership/
---

The Partnership pattern describes a symmetric relationship between two bounded contexts and is used within a [context map](/docs/context-map/) in CML. The [Language Semantics](https://contextmapper.org/docs/language-model/) page describes all relationship types that are supported in CML.

## Syntax
Note that currently two different syntax variants exist. The following code snippets illustrate both variants:

```cml
ContractsContext [P]<->[P] ClaimsContext {
  implementationTechnology = "Messaging"
}
```

Note that with this syntax (with the arrows _&lt;-&gt;_) it does not matter which bounded context is on which side, since this is a symmetric relationship. If you switch the bounded contexts, it has the same meaning semantically.

```cml
ContractsContext Partnership ClaimsContext {
  implementationTechnology = "Messaging"
}
```

### Implementation Technology
With the _implementationTechnology_ keyword you can specify how the relationship is implemented.

### Relationship Name
With a colon it is possible (optionally) to add a relationship name to the specification, as illustrated within this example:

```cml
ContractsContext [P]<->[P] ClaimsContext : ContractClaimRelationship {
  implementationTechnology = "Messaging"
}
```
