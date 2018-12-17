---
title: Customer/Supplier
permalink: /docs/customer-supplier/
---

The Customer/Supplier pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML.

Note that according to our understanding of the patterns and our [semantic model](/docs/language-model/) the Customer/Supplier relationship is a special case of a Upstream/Downstream relationship.
With the _Customer-Supplier_ keyword you always declare Customer/Supplier relationships. For 'generic' Upstream/Downstream relationships which are not Customer/Supplier relationships, use the _Upstream-Downstream_ keyword explained at [context map](/docs/context-map/).

## Syntax
Customer-Supplier relationships can be defined with three different syntax variants, all illustrated with the examples below:

<div class="highlight"><pre><span></span>CustomerSelfServiceContext -&gt; CustomerManagementContext : <span class="k">Customer-Supplier</span>
</pre></div>

<div class="highlight"><pre><span></span>CustomerManagementContext &lt;- CustomerSelfServiceContext : <span class="k">Customer-Supplier</span>
</pre></div>

<div class="highlight"><pre><span></span>CustomerSelfServiceContext <span class="k">Customer-Supplier</span> CustomerManagementContext
</pre></div>

All of the three variants are semantically equivalent. Note that the arrow _-&gt;_ always points from the customer to the supplier and thus, expresses the dependency (the customer depends on the supplier, but the supplier is independent of the customer).

With an @, you can annotate every relationship with a name:

<div class="highlight"><pre><span></span>@Customer_Frontend_Backend_Relationship <span class="c">// Relationship name is optional</span>
CustomerSelfServiceContext -&gt; CustomerManagementContext : <span class="k">Customer-Supplier</span> {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
  <span class="k">supplier</span> <span class="k">implements</span> <span class="k">PUBLISHED_LANGUAGE</span>
  <span class="k">customer</span> <span class="k">implements</span> <span class="k">ANTICORRUPTION_LAYER</span>
}
</pre></div>

Within the body of the relationship definition, the implementation technology and upstream/downstream role patterns can be defined. The corresponding keywords are _implementationTechnology_, _supplier implements_ and _customer implements_.

Upstream roles are given by the [Open Host Service](/docs/open-host-service/) and [Published Language](/docs/published-language/) patterns. Downstream roles are [Conformist](/docs/conformist/) and [Anticorruption Layer](/docs/anticorruption-layer/). But have a look at the semantic rules below, to see what combinations are actually allowed.

<div class="alert alert-warning">
  <strong>Note!</strong> With the keyword 'Customer-Supplier' you declare a Customer/Supplier relationship, but within our understanding of the
  DDD patterns and our <a href="/docs/language-model/" class="alert-link">semantic model</a>, a Customer/Supplier relationship is a Upstream/Downstream
  relationship as well. It is just a special form of an Upstream/Downstream relationship. To declare a 'generic' Upstream/Downstream relationship
  which is not a Customer/Supplier relationship, you have to use the 'Upstream-Downstream' keyword (see <a href="/docs/context-map/" class="alert-link">context map</a>).
  We know that the language grammar is not expressing this explicitly, which may lead to confusion. 

  <br>There is already an open <a href="https://github.com/ContextMapper/context-mapper-dsl/issues/35" target="_blank" class="alert-link">Github Issue</a> 
  and if you have ideas how to solve this issue (better keywords or other grammar improvements), feel free to comment there. We have not found the perfect solution to solve this ambiguity yet. 
  <br><a href="https://github.com/ContextMapper/context-mapper-dsl/issues/35" target="_blank" class="alert-link">Input and contribution is very welcome!</a>
</div>

## Semantic Rules
Note that semantic rules (validators) exist for Customer/Supplier relationships within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a Customer/Supplier:

* The Conformist pattern is not applicable in a Customer/Supplier relationship.
* The Open Host Service pattern is not applicable in a Customer/Supplier relationship.
* The Anticorruption Layer pattern can be used in a Customer/Supplier relationship, but this leads to contradictions with the original pattern definition according to our understanding.
  * The usage of Anticorruption Layer in a Customer/Supplier relationship produces a **Warning** only.
 
For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).
