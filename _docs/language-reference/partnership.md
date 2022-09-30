---
title: Partnership
permalink: /docs/partnership/
---

The Partnership pattern describes a symmetric relationship between two bounded contexts and is used within a [context map](/docs/context-map/) in CML. See this [description of Strategic Domain-Driven Design](https://socadk.github.io/design-practice-repository/activities/DPR-StrategicDDD.html) for an explanation of the relationship semantics.

## Syntax
Note that currently two different syntax variants exist. The following code snippets illustrate both variants:

<div class="highlight"><pre><span></span>ContractsContext [<span class="k">P</span>]&lt;-&gt;[<span class="k">P</span>] ClaimsContext {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Messaging&quot;</span>
}
</pre></div>

Note that with this syntax (with the arrows _&lt;-&gt;_) it does not matter which bounded context is on which side, since this is a symmetric relationship. If you switch the bounded contexts, it has the same meaning semantically.

<div class="highlight"><pre><span></span>ContractsContext <span class="k">Partnership</span> ClaimsContext {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Messaging&quot;</span>
}
</pre></div>

### Implementation Technology
With the _implementationTechnology_ keyword you can specify how the relationship is implemented.

### Relationship Name
With a colon it is possible (optionally) to add a relationship name to the specification, as illustrated within this example:

<div class="highlight"><pre><span></span>ContractsContext [<span class="k">P</span>]&lt;-&gt;[<span class="k">P</span>] ClaimsContext : ContractClaimRelationship {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Messaging&quot;</span>
}
</pre></div>
