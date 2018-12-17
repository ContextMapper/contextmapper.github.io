---
title: Knowledge Level
permalink: /docs/knowledge-level/
---

The Knowledge Level pattern can be used on bounded contexts and aggregates to specify their knowledge level, which can be one of the following values:

 * CONCRETE
 * META

## Syntax
The following examples show how you can specify the knowledge level on a bounded context and on an aggregate:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerManagementContext <span class="k">implements</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">FEATURE</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;The customer management context is responsible for ...&quot;</span>
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java, JEE Application&quot;</span>
  <span class="k">knowledgeLevel</span> = <span class="k">CONCRETE</span>
}
</pre></div>

<div class="highlight"><pre><span></span><span class="k">Aggregate</span> Customers {
  <span class="k">responsibilities</span> = Customers, Addresses { <span class="s">&quot;Address description ...&quot;</span> }
  <span class="k">knowledgeLevel</span> = <span class="k">CONCRETE</span>
    
  <span class="k">Entity</span> Customer { 
    <span class="k">aggregateRoot</span>
    
    - <span class="k">SocialInsuranceNumber</span> sin
    <span class="k">String</span> firstname
    <span class="k">String</span> lastname
    - <span class="k">List&lt;Address&gt;</span> addresses
  }
}
</pre></div>
