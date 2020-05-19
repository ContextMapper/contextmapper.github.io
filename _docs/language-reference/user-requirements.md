---
title: User Requirements
permalink: /docs/user-requirements/
---

As described in our [Rapid Object-oriented Analysis and Design](/docs/rapid-ooad/) page, the CML syntax supports the specification of user stories and use cases.
One can then derive DDD Subdomains and later Bounded Contexts from these stories and cases.

The following examples illustrate the syntax for both concepts quickly. Both concepts allow to specify the _actor_/_user_, the _interactions_ (_so that I can_ part of user story), 
and the _benefit_ of a use case or user story. 

## Use Case
The syntax to declare a use case rather briefly is as follows:

<div class="highlight"><pre><span></span><span class="k">UseCase</span> UC1_Example {
  <span class="k">actor</span> = <span class="s">&quot;Insurance Employee&quot;</span>
  <span class="k">interactions</span> = <span class="k">create</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>, <span class="k">update</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>, <span class="s">&quot;offer&quot;</span> <span class="k">a</span> <span class="s">&quot;Contract&quot;</span>
  <span class="k">benefit</span> = <span class="s">&quot;I am able to manage the customers data and offer them insurance contracts.&quot;</span>
}
</pre></div>

The predicate (verb) in the `interaction` can be one of the keywords `create`, `read`, `update`, `delete` (CRUD), or any string.

Optionally, it is further possible to add _attributes_ to the Entities and/or a reference to another Entity that acts as a _container_. The following example illustrates
the use case including this features:

<div class="highlight"><pre><span></span><span class="k">UseCase</span> UC1_Example {
  <span class="k">actor</span> <span class="s">&quot;Insurance Employee&quot;</span>
  <span class="k">interactions</span>
    <span class="k">create</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;firstname&quot;</span>, <span class="s">&quot;lastname&quot;</span>,
    <span class="k">update</span> <span class="k">an</span> <span class="s">&quot;Address&quot;</span> <span class="k">for</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>,
    <span class="s">&quot;offer&quot;</span> <span class="k">a</span> <span class="s">&quot;Contract&quot;</span> <span class="k">for</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span>
  <span class="k">benefit</span> <span class="s">&quot;I am able to manage the customers data and offer them insurance contracts.&quot;</span>
}
</pre></div>

The entity attributes follow the keyword _with its_ as illustrated above. The reference to the container Entity can be modelled with the following keywords: _for a_,
_for an_, _in a_, _in an_.

### Cockburn Styles
Our grammar supports creating Use Cases according to the _brief_ or _casual_ format [suggested by A. Cockburn](https://en.wikipedia.org/wiki/Use_case#Cockburn_style), 
but gives the prose paragraphs some structure. The following example illustrates the Use Case 2 ("Get paid for car accident") of [A. Cockburn's book](https://www.amazon.de/Writing-Effective-Crystal-Software-Development/dp/0201702258)
written in CML:

<div class="highlight"><pre><span></span><span class="k">UseCase</span> Get_paid_for_car_accident { <span class="c">// title</span>
  <span class="k">actor</span> <span class="s">&quot;Claimant&quot;</span> <span class="c">// primary actor</span>
  <span class="k">scope</span> <span class="s">&quot;Insurance company&quot;</span> <span class="c">// scope</span>
  <span class="k">level</span> <span class="s">&quot;Summary&quot;</span> <span class="c">// level</span>
  <span class="k">benefit</span> <span class="s">&quot;A claimant submits a claim and and gets paid from the insurance company.&quot;</span> <span class="c">// story (brief summary)</span>
}
</pre></div>

We do not support all attributes for a _fully dressed_ Use Case (another style [suggested by A. Cockburn](https://en.wikipedia.org/wiki/Use_case#Cockburn_style)), but
you can use the _interactions_ introduced above to model the _main success scenario_:

<div class="highlight"><pre><span></span><span class="k">UseCase</span> Get_paid_for_car_accident { <span class="c">// title</span>
  <span class="k">actor</span> <span class="s">&quot;Claimant&quot;</span> <span class="c">// primary actor</span>
  <span class="k">scope</span> <span class="s">&quot;Insurance company&quot;</span> <span class="c">// scope</span>
  <span class="k">level</span> <span class="s">&quot;Summary&quot;</span> <span class="c">// level</span>
  <span class="k">benefit</span> <span class="s">&quot;A claimant submits a claim and and gets paid from the insurance company.&quot;</span> <span class="c">// story (brief summary)</span>
  <span class="k">interactions</span>
    <span class="s">&quot;submit&quot;</span> <span class="k">a</span> <span class="s">&quot;Claim&quot;</span>,                <span class="c">// step 1: claimant submits claim</span>
    <span class="s">&quot;verifyExistanceOf&quot;</span> <span class="s">&quot;Policy&quot;</span>,      <span class="c">// step 2: insurance company verifies that valid policy exists</span>
    <span class="s">&quot;assign&quot;</span> <span class="k">an</span> <span class="s">&quot;Agent&quot;</span> <span class="k">for</span> <span class="k">a</span> <span class="s">&quot;Claim&quot;</span>, <span class="c">// step 3: agent is assigned to claim</span>
    <span class="s">&quot;verify&quot;</span> <span class="s">&quot;Policy&quot;</span>,                 <span class="c">// step 4: agent verifies all details are within policy guidelines</span>
    <span class="s">&quot;pay&quot;</span> <span class="s">&quot;Claimant&quot;</span>,                  <span class="c">// step 5 (1): claimant gets paid</span>
    <span class="s">&quot;close&quot;</span> <span class="s">&quot;Claim&quot;</span>                    <span class="c">// step 5 (2): file/claim gets closed</span>
}
</pre></div>

## User Story
First and foremost, a user story is an invitation to communicate and collaborate, as well a planning item. That said, the [role-feature-reason template](https://www.agilealliance.org/glossary/user-story-template/) can also serve as a requirements specification element. Hence, the user story support in CML allows you to declare exactly the same information as seen in the use case above, but in another syntax:

<div class="highlight"><pre><span></span><span class="k">UserStory</span> US1_Example {
  <span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Insurance Employee&quot;</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;create&quot;</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;firstname&quot;</span>, <span class="s">&quot;lastname&quot;</span> <span class="c">// attributes are optional (&#39;with its&#39; part)</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;update&quot;</span> <span class="k">an</span> <span class="s">&quot;Address&quot;</span> <span class="k">for</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span> <span class="c">// reference is optional (&#39;for a&#39; part)</span>
    <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;offer&quot;</span> <span class="k">a</span> <span class="s">&quot;Contract&quot;</span> <span class="k">for</span> <span class="k">a</span> <span class="s">&quot;Customer&quot;</span> <span class="c">// reference is optional (&#39;for a&#39; part)</span>
  <span class="k">so</span> <span class="k">that</span> <span class="s">&quot;I am able to manage the customers data and offer them insurance contracts.&quot;</span>
}
</pre></div>

*Note:* As you can see above, both variants allow users to specify multiple _interactions_ or _I want to_ parts in one use case or user story. You can see this as a way of 
expressing related features, for instance those originating from splitting a larger story - or the steps in a use case scenario.
