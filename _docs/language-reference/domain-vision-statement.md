---
title: Domain Vision Statement
permalink: /docs/domain-vision-statement/
---

The Domain Vision Statement pattern from the ["blue book"](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) is implemented as a String attribute on the [bounded context](/docs/bounded-context), the [domain](/docs/subdomain), and the 
[subdomain](/docs/subdomain).

## Syntax
The following two code snippets show an example for a bounded context, a domain, and a subdomain accordingly:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerContext {
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;This context is responsible for ...&quot;</span>
}
</pre></div>

<div class="highlight"><pre><span></span><span class="k">Domain</span> Insurance {
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;Insurance domain vision ...&quot;</span>

  <span class="k">Subdomain</span> Customers {
    <span class="c">/* subdomain specification */</span>
  }

  <span class="k">Subdomain</span> PolicyManagement {
    <span class="c">/* subdomain specification */</span>
  }
}
</pre></div>

<div class="highlight"><pre><span></span><span class="k">Subdomain</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">CORE_DOMAIN</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;Subdomain managing everything customer-related.&quot;</span>
}
</pre></div>

