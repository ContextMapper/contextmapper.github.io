---
title: Shared Kernel
permalink: /docs/shared-kernel/
---

The Shared Kernel pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML. The [Language Semantics](https://contextmapper.org/docs/language-model/) page describes all relationship types that are supported in CML.

## Syntax
Note that currently two different syntax variants exist. The following code snippets illustrate both variants:

<div class="highlight"><pre><span></span>CargoBookingContext [<span class="k">SK</span>]&lt;-&gt;[<span class="k">SK</span>] VoyagePlanningContext {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java Library&quot;</span>
}
</pre></div>

Note that with this syntax (with the arrows _&lt;-&gt;_) it does not matter which bounded context is on which side, since this is a symmetric relationship. If you switch the bounded contexts, it has the same meaning semantically.

<div class="highlight"><pre><span></span>CargoBookingContext <span class="k">Shared-Kernel</span> VoyagePlanningContext {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java Library&quot;</span>
}
</pre></div>

### Default Symmetric Relationship
**Note** that the Shared Kernel is the default symmetric relationship. Omitting the concrete relationship type within the brackets as follows, declares a 
Shared Kernel relationship too. However, with this syntax a reader has to know this behavior and cannot explicitly see that it is **not** a Partnership
relationship:

<div class="highlight"><pre><span></span>CargoBookingContext &lt;-&gt; VoyagePlanningContext
</pre></div>

### Implementation Technology
With the _implementationTechnology_ keyword you can specify how the relationship is implemented.

### Relationship Name
With a colon it is possible (optionally) to add a relationship name to the specification, as illustrated within this example:

<div class="highlight"><pre><span></span>CargoBookingContext <span class="k">Shared-Kernel</span> VoyagePlanningContext : BookingVoyageRelationship {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java Library&quot;</span>
}
</pre></div>
