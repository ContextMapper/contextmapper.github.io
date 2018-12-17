---
title: Context Map
permalink: /docs/context-map/
---

The context map is the most important element of CML, implementing the DDD Context Map pattern.
A context map contains bounded contexts and defines their relationships.

## Syntax

The following CML code snippet illustrates an example for a context map, according to our customized [DDD Sample](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/ddd-sample).
With the _contains_ keyword you add a bounded context to the map.

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> {
  <span class="k">type</span> = <span class="k">SYSTEM_LANDSCAPE</span>
  <span class="k">state</span> = <span class="k">AS_IS</span>

  <span class="k">contains</span> CargoBookingContext
  <span class="k">contains</span> VoyagePlanningContext
  <span class="k">contains</span> LocationContext
	
  CargoBookingContext &lt;-&gt; VoyagePlanningContext : <span class="k">Shared-Kernel</span>
}
</pre></div>

A context map can be of one of the following **types**:

* SYSTEM_LANDSCAPE
* ORGANIZATIONAL

While a SYSTEM_LANDSCAPE represents the typical context map with the relationships between bounded contexts, an ORGANIZATIONAL map (or 'team map') illustrates the relationships between teams. An example for such a team map can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/resources/insurance-example).

The **state** attribute accepts the following two values, expressing if the given context map represents the current or the desired state:

* AS_IS
* TO_BE

## Relationships
According to our [semantic model](/docs/language-model/), we support the following symmetric relationships:

* Partnership
* Shared Kernel

The asymmetric relationships are represented by the following two types:

* Upstream-Downstream (generic)
* Customer-Supplier (a special form of an Upstream-Downstream relationship)

For the symmetric relationships and their syntax please visit [Partnership](/docs/partnership/) and [Shared Kernel](/docs/shared-kernel/).

Upstream-Downstream relationships can be defined with three different syntax variants, all illustrated with the examples below:

<div class="highlight"><pre><span></span>CargoBookingContext -&gt; LocationContext : <span class="k">Upstream-Downstream</span>
</pre></div>

<div class="highlight"><pre><span></span>LocationContext &lt;- CargoBookingContext : <span class="k">Upstream-Downstream</span>
</pre></div>

<div class="highlight"><pre><span></span>LocationContext <span class="k">Upstream-Downstream</span> CargoBookingContext
</pre></div>

All of the three variants are semantically equivalent. Note that the arrow _-&gt;_ always points from the downstream to the upstream and thus, expresses the dependency (the downstream depends on the upstream, but the upstream is independent of the downstream).

With an _@_, you can annotate every relationship with a name:
<div class="highlight"><pre><span></span>@CargoLocationRelationship
CargoBookingContext -&gt; LocationContext : <span class="k">Upstream-Downstream</span>
</pre></div>

Within the body of the relationship definition, the implementation technology and upstream/downstream role patterns can be defined. The corresponding keywords are _implementationTechnology_, _upstream implements_ and _downstream implements_:

<div class="highlight"><pre><span></span>VoyagePlanningContext -&gt; LocationContext : <span class="k">Upstream-Downstream</span> {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
    <span class="k">upstream</span> <span class="k">implements</span> <span class="k">OPEN_HOST_SERVICE</span>, <span class="k">PUBLISHED_LANGUAGE</span>
    <span class="k">downstream</span> <span class="k">implements</span> <span class="k">ANTICORRUPTION_LAYER</span>
}
</pre></div>

Upstream roles are given by the [Open Host Service](/docs/open-host-service/) and [Published Language](/docs/published-language/) patterns. Downstream roles are [Conformist](/docs/conformist/) and [Anticorruption Layer](/docs/anticorruption-layer/).

For the Customer-Supplier relationship, which is a special form of Upstream-Downstream relationship, please visit [Customer-Supplier](/docs/customer-supplier).

<div class="alert alert-warning">
  <strong>Note!</strong> With the keyword 'Upstream-Downstream' you declare a 'generic' Upstream/Downstream relationship, 
  which is not a Customer/Supplier relationship (as illustrated in our <a href="/docs/language-model/" class="alert-link">semantic model</a>). 
  To declare a Customer/Supplier relationship you have to use the keyword 'Customer-Supplier', 
  which is a Upstream/Downstream relationship as well. We know that the language grammar is not expressing this explicitly, which may lead to confusion. 
  
  <br>There is already an open <a href="https://github.com/ContextMapper/context-mapper-dsl/issues/35" target="_blank" class="alert-link">Github Issue</a> 
  and if you have ideas how to solve this issue (better keywords or other grammar improvements), feel free to comment there. We have not found the perfect solution to solve this ambiguity yet.
  <br><a href="https://github.com/ContextMapper/context-mapper-dsl/issues/35" target="_blank" class="alert-link">Input and contribution is very welcome!</a>
</div>

## Semantic Rules
Note that semantic rules (validators) exist for context maps within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a context map:

* A bounded context which is not part of the context map (referenced with the _contains_ keyword), can not be referenced from a relationship rule within that context map.
* A bounded context of the type TEAM can not be contained in a context map if the context map type is SYSTEM_LANDSCAPE. 
* If the context map type of a context map is ORGANIZATIONAL, every bounded context added to the context map (with the _contains_ keyword) has to be of the type TEAM.
 
For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).
