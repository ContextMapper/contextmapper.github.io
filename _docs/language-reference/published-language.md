---
title: Published Language
permalink: /docs/published-language/
---

The Published Language pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML.

## Syntax
The Published Language pattern can be used as a role for the upstream context in a Upstream/Downstream relationship.
The following example illustrates the syntax:

<div class="highlight"><pre><span></span>PolicyManagementContext -&gt; CustomerManagementContext : <span class="k">Upstream-Downstream</span> {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
  <span class="k">upstream</span> <span class="k">implements</span> <span class="k">OPEN_HOST_SERVICE</span>, <span class="k">PUBLISHED_LANGUAGE</span>
  <span class="k">downstream</span> <span class="k">implements</span> <span class="k">CONFORMIST</span>
}
</pre></div>
