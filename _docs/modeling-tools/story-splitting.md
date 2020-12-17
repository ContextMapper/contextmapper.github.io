---
title: Story Splitting (PoC)
permalink: /docs/story-splitting/
image: /img/cm-og-image.png
---

The Context Mapper DSL (CML) allows our users to [write user stories](/docs/user-requirements/#user-story). Together with our [OOAD transformations](/docs/rapid-ooad/) it is possible to prototype an application rapidly. However, before you start generating Subdomains and Bounded Contexts, you have to evolve a set of use cases or user stories. During this process (in case you work with user stories) you may want to [split your stories](https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/). With our story splitting transformations based on [_Patterns for Splitting User Stories_](https://agileforall.com/patterns-for-splitting-user-stories/) we want to support our users in splitting their stories.

<div class="alert alert-custom">
<strong>Note:</strong> This feature is in "proof of concept" state. It might not be stable and we currently only support one transformation. In the future we may support all <a href="https://agileforall.com/patterns-for-splitting-user-stories/" target="_blank">Patterns for Splitting User Stories</a>
</div>

## Split Story by Verb/Operation
As a first proof of concept for this feature we implemented the transformation "Split Story by Verb/Operation". It splits a CML user story by its verb. An example...

We illustrate the idea with the following user story written in CML:

<div class="highlight"><pre><span></span><span class="k">UserStory</span> Account_Admin_Story {
    <span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Admin&quot;</span> <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;manage&quot;</span> <span class="k">an</span> <span class="s">&quot;Account&quot;</span> <span class="k">so</span> <span class="k">that</span> <span class="s">&quot;can enable users to work with the system.&quot;</span>
}
</pre></div>

The Context Mapper editor provides a quick fix on the verb:

<a href="/img/story-splitting-example-1.png">![Story Splitting in VS Code - Example (1)](/img/story-splitting-example-1.png)</a>

By clicking on the verb, and then on the light bulb, users can click "Split Story by Verb/Operation":

<a href="/img/story-splitting-example-2.png">![Story Splitting in VS Code - Example (2)](/img/story-splitting-example-2.png)</a>

Users can then enter multiple new verbs - one after the other:

<a href="/img/story-splitting-example-3.png">![Story Splitting in VS Code - Example (3)](/img/story-splitting-example-3.png)</a>

After you entered all the verbs you can press `ESC` and the transformation will be applied. In our case here we entered the verbs **create**, **edit**, and **cancel**. This leads to the following CML result:

<a href="/img/story-splitting-example-4.png">![Story Splitting in VS Code - Example (4)](/img/story-splitting-example-4.png)</a>

The resulting CML code:

<div class="highlight"><pre><span></span><span class="k">UserStory</span> Account_Admin_Story <span class="k">split</span> <span class="k">by</span> Account_Admin_Story_Split {
	<span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Admin&quot;</span> <span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;manage&quot;</span> <span class="k">an</span> <span class="s">&quot;Account&quot;</span> <span class="k">so</span> <span class="k">that</span> <span class="s">&quot;can enable users to work with the system.&quot;</span>
}

<span class="k">UserStory</span> Account_Admin_Story_Split {
	<span class="k">As</span> <span class="k">an</span> <span class="s">&quot;Admin&quot;</span>
	<span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;cancel&quot;</span> <span class="k">an</span> <span class="s">&quot;Account&quot;</span>
	<span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="s">&quot;edit&quot;</span> <span class="k">an</span> <span class="s">&quot;Account&quot;</span>
	<span class="k">I</span> <span class="k">want</span> <span class="k">to</span> <span class="k">create</span> <span class="k">an</span> <span class="s">&quot;Account&quot;</span>
	<span class="k">so</span> <span class="k">that</span> <span class="s">&quot;can enable users to work with the system.&quot;</span>
}
</pre></div>

With the _split by_ keyword we provide a back-reference so that you still know which story was split by which other story (and how the original story looked like).

## Next Steps
After you modelled your user stories you can use our [OOAD transformations](/docs/rapid-ooad/) to derive Subdomains and Bounded Contexts with tool support. The transformations will always use the _splitted_ version of a story and ignore the original one!
