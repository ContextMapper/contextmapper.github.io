---
title: Customer/Supplier
permalink: /docs/customer-supplier/
---

The Customer/Supplier pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML.

<div class="alert alert-warning">
<strong>Note</strong> that according to our understanding of the patterns and our <a href="/docs/language-model/" class="alert-link">semantic model</a>
the customer-supplier relationship is a special case of a upstream-downstream relationship. With the <strong>Customer-Supplier</strong> 
keyword you always declare customer-supplier relationships. For 'generic' upstream-downstream relationships which are not 
customer-supplier relationships, use the <strong>Upstream-Downstream</strong> keyword explained at <a href="/docs/context-map/" 
class="alert-link">context map</a>.
<br/><br/>
A customer-supplier relationship is an upstream-downstream relationship where the downstream priorities factor
into upstream planning. The upstream team may succeed interdependently of the fate of the downstream team and therefore the needs of
the downstream have to be addressed by the upstream. They interact as <strong>customer</strong> and <strong>supplier</strong>.
A generic upstream-downstream relationship is not necessarily a customer-supplier relationship! (in CML you have to express this
explicitely)
</div>

## Syntax
Customer-Supplier relationships can be defined with three different syntax variants, all illustrated with the examples below:

<div class="highlight"><pre><span></span>CustomerSelfServiceContext [<span class="k">D</span>,<span class="k">C</span>]&lt;-[<span class="k">U</span>,<span class="k">S</span>] CustomerManagementContext
</pre></div>

<div class="highlight"><pre><span></span>CustomerManagementContext [<span class="k">U</span>,<span class="k">S</span>]-&gt;[<span class="k">D</span>,<span class="k">C</span>] CustomerSelfServiceContext
</pre></div>

<div class="highlight"><pre><span></span>CustomerSelfServiceContext <span class="k">Customer-Supplier</span> CustomerManagementContext
</pre></div>

<div class="highlight"><pre><span></span>CustomerManagementContext <span class="k">Supplier-Customer</span> CustomerSelfServiceContext
</pre></div>

All of the four variants are semantically equivalent. Note that the arrow _-&gt;_ always points from the supplier (upstream) to the customer (downstream) 
and thus, expresses the influence flow (the supplier has an influence on the customer, but the customer has no influence on the supplier).

The syntax with the arrows and the abbreviations further allows to place the brackets with the supplier [U,S] / customer [D,C] and relationship role 
patterns specification flexible in front or after the Bounded Context name:

<div class="highlight"><pre><span></span>CustomerSelfServiceContext [<span class="k">D</span>,<span class="k">C</span>]&lt;-[<span class="k">U</span>,<span class="k">S</span>] CustomerManagementContext
</pre></div>

<div class="highlight"><pre><span></span>[<span class="k">D</span>,<span class="k">C</span>]CustomerSelfServiceContext &lt;- [<span class="k">U</span>,<span class="k">S</span>]CustomerManagementContext
</pre></div>

<div class="highlight"><pre><span></span>CustomerSelfServiceContext[<span class="k">D</span>,<span class="k">C</span>] &lt;- CustomerManagementContext[<span class="k">U</span>,<span class="k">S</span>]
</pre></div>

<div class="highlight"><pre><span></span>[<span class="k">D</span>,<span class="k">C</span>]CustomerSelfServiceContext &lt;- CustomerManagementContext[<span class="k">U</span>,<span class="k">S</span>]
</pre></div>

In a Customer/Supplier relationship definition you can also omit the **U** (upstream) and **D** (downstream) specification, since the supplier is always the
upstream and the customer always the downstream:

<div class="highlight"><pre><span></span>CustomerSelfServiceContext [<span class="k">C</span>]&lt;-[<span class="k">S</span>] CustomerManagementContext
</pre></div>

With a colon at the end, you can give every relationship a name:
<div class="highlight"><pre><span></span>CustomerSelfServiceContext [<span class="k">D</span>,<span class="k">C</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">S</span>,<span class="k">PL</span>] CustomerManagementContext : Customer_Frontend_Backend_Relationship { <span class="c">// Relationship name is optional</span>
  <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
}
</pre></div>

Within the brackets you can further specify the relationship roles such as Open Host Service (OHS) or Anti-Corruption Layer (ACL).
Roles must always be specified behind the **U**/**S** (upstream/supplier) and the **D**/**C** (downstream/customer) signs, as shown in the example above. 
Within the body of the declaration it is possible to specify the implementation technology.

Upstream roles are given by the [Open Host Service (OHS)](/docs/open-host-service/) and [Published Language (PL)](/docs/published-language/) patterns. 
Downstream roles are [Conformist (CF)](/docs/conformist/) and [Anticorruption Layer (ACL)](/docs/anticorruption-layer/). 
But have a look at the semantic rules below, to see what combinations are actually allowed.

## Semantic Rules
Note that semantic rules (validators) exist for Customer/Supplier relationships within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a Customer/Supplier:

* The Conformist pattern is not applicable in a Customer/Supplier relationship.
* The Open Host Service pattern is not applicable in a Customer/Supplier relationship.
* The Anticorruption Layer pattern can be used in a Customer/Supplier relationship, but this leads to contradictions with the original pattern definition according to our understanding.
  * The usage of Anticorruption Layer in a Customer/Supplier relationship produces a **Warning** only.
 
For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).
