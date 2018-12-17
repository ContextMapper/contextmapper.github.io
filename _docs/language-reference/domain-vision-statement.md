---
title: Domain Vision Statement
permalink: /docs/domain-vision-statement/
---

The Domain Vision Statement pattern is implemented as a String attribute on the [bounded context](/docs/bounded-context) and the [subdomain](/docs/subdomain).

## Syntax
The following two code snippets show an example for a bounded context and a subdomain accordingly:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerContext {
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;This context is responsible for ...&quot;</span>
}
</pre></div>

<div class="highlight"><pre><span></span><span class="k">Subdomain</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">CORE_DOMAIN</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;Subdomain managing everything customer-related.&quot;</span>
}
</pre></div>

