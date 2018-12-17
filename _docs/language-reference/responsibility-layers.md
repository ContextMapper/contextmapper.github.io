---
title: Responsibility Layers
permalink: /docs/responsibility-layers/
---

The Responsibility Layers pattern can be used on bounded contexts and aggregates to specify their responsibilities.

## Syntax
The responsibilities can either be simply defined by a keyword or with an additional description. The following two CML snippets illustrate both variants 
on a bounded context and on an aggregate as well:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerManagementContext <span class="k">implements</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">FEATURE</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;The customer management context is responsible for ...&quot;</span>
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java, JEE Application&quot;</span>
  <span class="k">responsibilities</span> = Customers, Addresses { <span class="s">&quot;Address description ...&quot;</span> }
}
</pre></div>

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Customers {
  <span class="k">responsibilities</span> = Customers, Addresses { <span class="s">&quot;Address description ...&quot;</span> }
  
  <span class="k">Entity</span> Customer { 
    <span class="k">aggregateRoot</span>
    
    - <span class="k">SocialInsuranceNumber</span> sin
    <span class="k">String</span> firstname
    <span class="k">String</span> lastname
    - <span class="k">List&lt;Address&gt;</span> addresses
  }
}
</pre></div>
