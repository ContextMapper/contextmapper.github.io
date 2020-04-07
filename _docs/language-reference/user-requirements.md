---
title: User Requirements
permalink: /docs/user-requirements/
---

As described in our [Rapid Object-oriented Analysis and Design](/docs/rapid-ooad/) page, the CML syntax supports the specification of user stories and use cases. From those stories
and cases one can then derive DDD Subdomains and later Bounded Contexts.

The following examples illustrate the syntax for both concepts quickly. Both concepts allow to specify the _actor_/_user_, the _interactions_ (_so that I can_ part of user story), and
the _benefit_ of a use case or user story. 

## Use Case
The syntax to declare a use case is as follows:

<div class="highlight"><pre><span></span><span class="k">UseCase</span> UC1_Example {
  <span class="k">actor</span> = <span class="s">&quot;Insurance Employee&quot;</span>
  <span class="k">interactions</span> = <span class="s">&quot;create&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>, <span class="s">&quot;update&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>, <span class="s">&quot;offer&quot;</span> <span class="k">a</span> <span class="s">&quot;Contract&quot;</span>
  <span class="k">benefit</span> = <span class="s">&quot;I am able to manage the customers data and offer them insurance contracts.&quot;</span>
}
</pre></div>

## User Story
The user story in CML allows you to declare exactly the same information as seen in the use case above, but in another syntax:

<div class="highlight"><pre><span></span><span class="k">UserStory</span> US1_Example {
  <span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Insurance Employee&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;create&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;update&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;offer&quot;</span> <span class="k">a</span> <span class="s">&quot;Contract&quot;</span>
  <span class="k">so</span> <span class="k">that</span> <span class="s">&quot;I am able to manage the customers data and offer them insurance contracts.&quot;</span>
}
</pre></div>

*Note:* As you can see above, both variants allow users to specify multiple _interactions_ or _I want to_ parts in one use case or user story.
