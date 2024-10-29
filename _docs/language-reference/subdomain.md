---
title: Domain and Subdomain
permalink: /docs/subdomain/
---

As bounded contexts, domains are defined on the root level of a CML (*.cml) file. 
They provide a container to specify all subdomains which are then referenced on a bounded context with the _implements_ keyword. 
A bounded context can also implement the compete domain. Have a look at [bounded context](/docs/bounded-context/) for an example.

## Syntax
The following example illustrates how you can specify a domain with subdomains in CML:

<div class="highlight"><pre><span></span><span class="c">/* Syntax example: Domain and Subdomains */</span>
<span class="k">Domain</span> Insurance {
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;Insurance domain vision statement ...&quot;</span>

  <span class="k">Subdomain</span> CustomerManagementDomain {
    <span class="k">type</span> = <span class="k">CORE_DOMAIN</span>
    <span class="k">domainVisionStatement</span> = <span class="s">&quot;Subdomain managing everything customer-related.&quot;</span>

    <span class="k">Entity</span> Customer {
      <span class="k">String</span> firstname
      <span class="k">String</span> familyname
    }

    <span class="c">/* Add more entities ... */</span>
  }

  <span class="k">Subdomain</span> ContractManagementDomain {}

  <span class="c">/* Add more subdomains ... */</span>
}
</pre></div>

Note that the equal sign (=) to assign an attribute value as done in the example above is optional and can be omitted.

### Subdomain Type
With the _type_ keyword you specify of which type your subdomain is. The following types exist:

 * CORE_DOMAIN
 * SUPPORTING_DOMAIN
 * GENERIC_SUBDOMAIN

### Implemented Features
The CML language supports the specification of user requirements or features in the form of [use cases or user stories](/docs/user-requirements/).
With the _supports_ keyword you can specify which user requirements a Subdomain implements. An example:

<div class="highlight"><pre><span></span><span class="c">/* Syntax example for Subdomain that supports specific user requirements: */</span>
<span class="k">Domain</span> Insurance {
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;Insurance domain vision statement ...&quot;</span>

  <span class="k">Subdomain</span> CustomerManagementDomain <span class="k">supports</span> CreateCustomers, CreateCustomerAddresses {
    <span class="k">type</span> = <span class="k">CORE_DOMAIN</span>
    <span class="k">domainVisionStatement</span> = <span class="s">&quot;Subdomain managing everything customer-related.&quot;</span>

    <span class="k">Entity</span> Customer {
      <span class="k">String</span> firstname
      <span class="k">String</span> familyname
    }
  }

}

<span class="k">UserStory</span> CreateCustomers {
  <span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Insurance Employee&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;create&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;firstname&quot;</span>, <span class="s">&quot;lastname&quot;</span>
  <span class="k">so</span> <span class="k">that</span> <span class="s">&quot;I am able to manage the customers data and offer them insurance contracts.&quot;</span>
}

<span class="k">UserStory</span> CreateCustomerAddresses {
  <span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Insurance Employee&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;create&quot;</span> <span class="k">an</span> <span class="s">&quot;Address&quot;</span> <span class="k">for</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;update&quot;</span> <span class="k">an</span> <span class="s">&quot;Address&quot;</span> <span class="k">for</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>
  <span class="k">so</span> <span class="k">that</span> <span class="s">&quot;I am able to manage the customers addresses.&quot;</span>
}
</pre></div>
 
### Domain Vision Statement
With the _domainVisionStatement_ keyword you can specify a vision statement for domains and subdomains, according to the DDD [Domain Vision Statement](/docs/domain-vision-statement/) 
pattern.

### Entities
In order to provide further details about your subdomain and which domain objects are part of it, you can use entities within a subdomain. Note that the used _Entity_ rule is integrated from the [Sculptor DSL](https://sculptor.github.io/). 
For more details about the features and possibilities of this Entity rule, we refer to the [Sculptor documentation](https://sculptor.github.io/documentation/advanced-tutorial).
An example of a simple entity with attributes is illustrated above.

<div class="alert alert-custom">
<strong>Note</strong> that only entities can be used within the subdomains. It is not possible to use <a href="/docs/aggregate/">Aggregates</a> or other
tactic DDD concepts within them. The entities within subdomains are only used for business modeling purposes and not respected by the generator tools. Generators
respect the domain model within Bounded Contexts.
</div>
