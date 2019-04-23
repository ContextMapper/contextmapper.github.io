---
title: Responsibility Layers
permalink: /docs/responsibility-layers/
---

The Responsibility Layers pattern can be used on bounded contexts and aggregates to specify their responsibilities.

## Syntax
The responsibilities can simply be defined with the keyword/attribute _responsibilities_ and a list of responsibilities (as strings):

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerManagementContext <span class="k">implements</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">FEATURE</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;The customer management context is responsible for ...&quot;</span>
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java, JEE Application&quot;</span>
  <span class="k">responsibilities</span> = <span class="s">&quot;Customers&quot;</span>, <span class="s">&quot;Addresses&quot;</span>
}
</pre></div>

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Customers {
  <span class="k">responsibilities</span> = <span class="s">&quot;Customers&quot;</span>, <span class="s">&quot;Addresses&quot;</span>
  
  <span class="k">Entity</span> Customer { 
    <span class="k">aggregateRoot</span>
    
    - <span class="k">SocialInsuranceNumber</span> sin
    <span class="k">String</span> firstname
    <span class="k">String</span> lastname
    - <span class="k">List&lt;Address&gt;</span> addresses
  }
}
</pre></div>
