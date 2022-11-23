---
title: Published Language
permalink: /docs/published-language/
---

The Published Language pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML. The [Language Semantics](https://contextmapper.org/docs/language-model/) page describes all relationship types that are supported in CML.

## Syntax
The Published Language pattern can be used as a role for the upstream context in a Upstream/Downstream relationship by using the **PL** abbreviation.
The following example illustrates the syntax:

<div class="highlight"><pre><span></span>PolicyManagementContext [<span class="k">D</span>,<span class="k">CF</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] CustomerManagementContext {
  <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTful HTTP&quot;</span>
}
</pre></div>
