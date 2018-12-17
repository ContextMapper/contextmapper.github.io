---
title: Anticorruption Layer
permalink: /docs/anticorruption-layer/
---

The Anticorruption Layer pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML.

## Syntax
The Anticorruption Layer pattern can be used as a role for the downstream context in a Upstream/Downstream relationship.
The following example illustrates the syntax:

<div class="highlight"><pre><span></span>DebtCollection -&gt; PrintingContext : <span class="k">Upstream-Downstream</span> {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;SOAP&quot;</span>
  <span class="k">upstream</span> <span class="k">implements</span> <span class="k">OPEN_HOST_SERVICE</span>, <span class="k">PUBLISHED_LANGUAGE</span>
  <span class="k">downstream</span> <span class="k">implements</span> <span class="k">ANTICORRUPTION_LAYER</span>
}
</pre></div>


## Semantic Rules
Note that semantic rules (validators) exist for Anticorruption Layer within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a Anticorruption Layer:

* The Anticorruption Layer pattern can be used in a Customer/Supplier relationship, but this leads to contradictions with the original pattern definition according to our understanding.
  * The usage of Anticorruption Layer in a Customer/Supplier relationship produces a **Warning** only.
 
For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).
