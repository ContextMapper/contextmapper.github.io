---
title: Context Map
permalink: /docs/context-map/
---

The context map is the most important element of CML, implementing the DDD Context Map pattern.
A context map contains bounded contexts and defines their relationships.

## Syntax

The following CML code snippet illustrates an example for a context map, according to our customized [DDD Sample](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/ddd-sample).
With the _contains_ keyword you add a bounded context to the map.

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> {
  <span class="k">type</span> = <span class="k">SYSTEM_LANDSCAPE</span>
  <span class="k">state</span> = <span class="k">AS_IS</span>

  <span class="k">contains</span> CargoBookingContext
  <span class="k">contains</span> VoyagePlanningContext
  <span class="k">contains</span> LocationContext
	
  CargoBookingContext [<span class="k">SK</span>]&lt;-&gt;[<span class="k">SK</span>] VoyagePlanningContext
}
</pre></div>

Alternatively, you can use only one _contains_ keyword and list all bounded contexts comma-separated:

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> DDDSampleContextMap {
  <span class="k">type</span> <span class="k">SYSTEM_LANDSCAPE</span>
  <span class="k">state</span> <span class="k">AS_IS</span>

  <span class="k">contains</span> CargoBookingContext, VoyagePlanningContext, LocationContext

  CargoBookingContext [<span class="k">SK</span>]&lt;-&gt;[<span class="k">SK</span>] VoyagePlanningContext
}
</pre></div>

As you can see in the example above, it is also possible to name a context map (the name is optional). The equal sign (=) to assign an attribute value as done in the first example can be omitted as well.

A context map can be of one of the following **types**:

* SYSTEM_LANDSCAPE
* ORGANIZATIONAL

A SYSTEM_LANDSCAPE represents the default type of context map in which the bounded contexts represent software systems (or applications). The second type, an ORGANIZATIONAL map (or 'team map'), illustrates the relationships between teams. An example for such a team map can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example).

The **state** attribute accepts the following two values, expressing whether the given context map represents the current or a desired state (this distinction is often made in [enterprise architecture management](https://searcherp.techtarget.com/definition/enterprise-asset-management-EAM) and [portfolio- or program-level project planning](https://www.pmi.org/learning/library/integrated-portfolio-program-management-7409)):

* AS_IS
* TO_BE

## Relationships
According to our [semantic model](/docs/language-model/), we support the following symmetric relationships:

* Partnership (P)
* Shared Kernel (SK)

The asymmetric relationships are represented by the following two types:

* Upstream-Downstream (generic)
* Customer-Supplier (C/S), a special form of an Upstream-Downstream relationship

<div class="alert alert-custom">
<strong>Note:</strong> A customer-supplier relationship is an upstream-downstream relationship where the downstream priorities factor
into upstream planning. The upstream team may succeed interdependently of the fate of the downstream team and therefore the needs of
the downstream have to be addressed by the upstream. They interact as <strong>customer</strong> and <strong>supplier</strong>.
A generic upstream-downstream relationship is not necessarily a customer-supplier relationship! (in CML you have to express this
explicitly)  
<br/><br/>
The syntax for upstream-downstream relationships is explained below. To learn about the syntax of customer-supplier relationships, please visit <a href="/docs/customer-supplier/" class="alert-link">Customer/Supplier</a>.
</div>

The symmetric relationships and their syntax are introduced on separate pages: [Partnership](/docs/partnership/) and [Shared Kernel](/docs/shared-kernel/).

Upstream-Downstream relationships can be defined with three different syntax variants, all illustrated with the examples below:

<div class="highlight"><pre><span></span>CargoBookingContext [<span class="k">D</span>]&lt;-[<span class="k">U</span>] LocationContext
</pre></div>

<div class="highlight"><pre><span></span>LocationContext [<span class="k">U</span>]-&gt;[<span class="k">D</span>] CargoBookingContext
</pre></div>

<div class="highlight"><pre><span></span>LocationContext <span class="k">Upstream-Downstream</span> CargoBookingContext
</pre></div>

<div class="highlight"><pre><span></span>CargoBookingContext <span class="k">Downstream-Upstream</span> LocationContext
</pre></div>

All of the four variants are semantically equivalent. Note that the arrow _-&gt;_ always points from the upstream to the downstream and thus expresses an *influence flow* 
(the upstream has an influence on the downstream, but the downstream has no influence on the upstream).

A colon at the end assigns a relationship a name:
<div class="highlight"><pre><span></span>CargoBookingContext [<span class="k">D</span>]&lt;-[<span class="k">U</span>] LocationContext : CargoLocationRelationship
</pre></div>

**Note:** The following quick upstream/downstream syntax without brackets can be used as well. It denotes a common upstream/downstream relationship without any roles. However, with this syntax it is less clear for a reader that you declare an upstream/downstream and *not* a customer/supplier relationship.

<div class="highlight"><pre><span></span>CargoBookingContext &lt;- LocationContext
</pre></div>

<div class="highlight"><pre><span></span>LocationContext -&gt; CargoBookingContext
</pre></div>

### Relationship Roles
You can further specify the relationship roles such as Open Host Service (OHS) or Anti-Corruption Layer (ACL) within the brackets.
Roles must always be specified behind the **U** (upstream) and the **D** (downstream) if they are not omitted. 

<div class="highlight"><pre><span></span>VoyagePlanningContext [<span class="k">D</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext
</pre></div>

Since the arrow already indicates which Bounded Context is upstream and which is downstream, it is also possible to add the relationship roles within the brackets without the **U** and the **D**:

<div class="highlight"><pre><span></span>VoyagePlanningContext [<span class="k">ACL</span>]&lt;-[<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext
</pre></div>

If you use the _Upstream-Downstream_ or _Downstream-Upstream_ keywords the roles are declared equivalently, but without the **D** and **U** (note that it does not matter if you write a whitespace before or after the brackets, or both):

<div class="highlight"><pre><span></span>VoyagePlanningContext[<span class="k">ACL</span>] <span class="k">Downstream-Upstream</span> [<span class="k">OHS</span>,<span class="k">PL</span>]LocationContext
</pre></div>

Upstream roles are defined by the [Open Host Service (OHS)](/docs/open-host-service/) and 
[Published Language (PL)](/docs/published-language/) patterns. Downstream roles are [Conformist (CF)](/docs/conformist/) and 
[Anticorruption Layer (ACL)](/docs/anticorruption-layer/).

### Relationship Attributes
By using brackets {}, you can specify additional attributes for a relationship:

* implementationTechnology
* downstreamRights
* exposedAggregates

#### Implementation Technology
Within the body of the declaration, it is possible to specify the implementation technology used to realize this relationship:
<div class="highlight"><pre><span></span>VoyagePlanningContext [<span class="k">D</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
}
</pre></div>

#### Downstream Governance Rights
The attribute _downstreamRights_ defines which governance rights, and therefore which influence, the downstream has on the upstream within the specified relationship:

<div class="highlight"><pre><span></span>VoyagePlanningContext [<span class="k">D</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
    <span class="k">downstreamRights</span> = <span class="k">VETO_RIGHT</span>
}
</pre></div>

The possible governance rights values are:

* INFLUENCER
* OPINION_LEADER
* VETO_RIGHT
* DECISION_MAKER
* MONOPOLIST

#### Exposed Aggregates
The _exposedAggregates_ attribute offers the possibility to declare which [Aggregates](/docs/aggregate) of the **upstream** bounded context are exposed in order to realize this relationship. The attribute takes a comma-separated list of references to Aggregates. The referenced Aggregates must be part of the upstream context of the relationship.

<div class="highlight"><pre><span></span>VoyagePlanningContext [<span class="k">D</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] LocationContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
    <span class="k">downstreamRights</span> = <span class="k">VETO_RIGHT</span>
    <span class="k">exposedAggregates</span> = Customers, Addresses
}
</pre></div>
 
### Special Case: Customer/Supplier
For the Customer-Supplier relationship, which is a special form of Upstream-Downstream relationship, please visit [Customer-Supplier](/docs/customer-supplier).

## Semantic Rules
Note that semantic rules (validators) exist for context maps within CML. This means that not every combination of patterns and concepts is allowed (even if it was syntactically correct).
The following rules apply to a context map:

* A Bounded Context which is not part of the Context Map (referenced with the _contains_ keyword), can not be referenced from a relationship rule within that Context Map.
* A Bounded Context of the type TEAM can not be contained in a Context Map of type SYSTEM_LANDSCAPE. 
* If the type of a Context Map is ORGANIZATIONAL, every Bounded Context added to it (indicated by the keyword _contains_) has to be of the type TEAM.
 
For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).
