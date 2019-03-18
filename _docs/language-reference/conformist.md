---
title: Conformist
permalink: /docs/conformist/
---

The Conformist pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML.

## Syntax
The Conformist pattern can be used as a role for the downstream context in a Upstream/Downstream relationship by using the **CF** abbreviation.
The following example illustrates the syntax:

<div class="highlight"><pre><span></span>PolicyManagementContext [<span class="k">D</span>,<span class="k">CF</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] CustomerManagementContext {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
}
</pre></div>

## Semantic Rules
Note that semantic rules (validators) exist for Conformist within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a Conformist:

* The Conformist pattern is not applicable in a Customer/Supplier relationship.
 
For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).
