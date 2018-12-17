---
title: Open Host Service
permalink: /docs/open-host-service/
---

The Open Host Service pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML.

## Syntax
The Open Host Service pattern can be used as a role for the upstream context in a Upstream/Downstream relationship.
The following example illustrates the syntax:

<div class="highlight"><pre><span></span>PrintingContext &lt;- PolicyManagementContext : <span class="k">Upstream-Downstream</span> {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;SOAP&quot;</span>
  <span class="k">upstream</span> <span class="k">implements</span> <span class="k">OPEN_HOST_SERVICE</span>
  <span class="k">downstream</span> <span class="k">implements</span> <span class="k">ANTICORRUPTION_LAYER</span>
}
</pre></div>

## Semantic Rules
Note that semantic rules (validators) exist for Open Host Service within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a Open Host Service:

* The Open Host Service pattern is not applicable in a Customer/Supplier relationship.
 
For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).
