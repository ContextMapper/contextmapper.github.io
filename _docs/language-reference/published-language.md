---
title: Published Language
permalink: /docs/published-language/
---

The Published Language pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML. The [Language Semantics](https://contextmapper.org/docs/language-model/) page describes all relationship types that are supported in CML.

## Syntax
The Published Language pattern can be used as a role for the upstream context in a Upstream/Downstream relationship by using the **PL** abbreviation.
The following example illustrates the syntax:

```cml
PolicyManagementContext [D,CF]<-[U,OHS,PL] CustomerManagementContext {
  implementationTechnology = "RESTful HTTP"
}
```
