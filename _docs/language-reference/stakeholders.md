---
title: Stakeholders
permalink: /docs/stakeholders/
---

The CML language supports the modelling of stakeholders of (digital) solutions and/or projects. This feature has been introduced to support the [JEDi project](tbd) and its Value-Driven Analysis and Design (VDAD) process. One part of this process supporting ethical software engineering is the identification of all relevant stakeholders. For more information about the whole process we refer to the [JEDi page](tbd). However, modelling stakeholders can support your requirements engineering process in different ways; no matter whether you apply VDAD or JEDi practices.

**Note**: With our [PlantUML generator](/docs/plant-uml/) you can automatically generate [Stakeholder Maps](tbd), once you modelled all your stakeholders and stakeholder groups. See example below.

## Stakeholders Container
On the root level of a CML file, one first needs to create a `Stakeholders` container. This can be done as simply as follows:

<div class="highlight"><pre><span></span><span class="k">Stakeholders</span> {

  <span class="c1">// add stakeholders and stakeholder groups here</span>

}
</pre></div>

However, if you want to model the stakeholders for a specific [Bounded Context](/docs/bounded-context/), you can declare that as follows:

<pre class="highlight"><span class="k">BoundedContext</span> ExampleContext

<span class="k">Stakeholders</span> <span class="k">of</span> ExampleContext {

  <span class="c1">// add stakeholders and stakeholder groups here</span>

}
</pre>

## Stakeholders
Inside a `Stakeholders` container, you can define your stakeholders. This can be done with the `Stakeholder` keyword an the name of the stakeholder:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">BoundedContext</span> <span class="n">ExampleContext</span>

<span class="k">Stakeholders</span> <span class="k">of</span> <span class="n">ExampleContext</span> <span class="p">{</span>

  <span class="k">Stakeholder</span> <span class="n">Shopper</span>

  <span class="k">Stakeholder</span> <span class="n">Software_Engineer</span>

  <span class="k">Stakeholder</span> <span class="n">Architect</span>

  <span class="c1">// etc.</span>

<span class="p">}</span>
</pre></div>
</div>

In addition, you can provide additional information for a stakeholder using the `description`, `incluence` and `interest` keywords:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">BoundedContext</span> <span class="n">ExampleContext</span>

<span class="k">Stakeholders</span> <span class="k">of</span> <span class="n">ExampleContext</span> <span class="p">{</span>

  <span class="k">Stakeholder</span> <span class="n">Shopper</span> <span class="p">{</span>
    <span class="k">description</span> <span class="s">&quot;Is using the shopping system to by everday goods.&quot;</span>
    
    <span class="k">influence</span> <span class="k">MEDIUM</span>
    <span class="k">interest</span> <span class="k">HIGH</span>
  <span class="p">}</span>

<span class="p">}</span>
</pre></div>
</div>

The `description` just describes why and/or how the stakeholder uses the system or is impacted by the system. As suggested by many stakeholder mapping tutorials (see [Miro](https://miro.com/blog/stakeholder-mapping/) or [Mural](https://www.mural.co/blog/stakeholder-mapping)), you can define what the `incluence` of the stakeholders is and how much they are interested (`interest`) in the new system or feature.

## Stakeholder Groups
Stakeholder maps often group stakeholders of similar roles or with similar interest together. This is also possible in CML with the `StakeholderGroup` keyword, which can again contain stakeholders with the `Stakeholder` keyword:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">BoundedContext</span> <span class="n">ExampleContext</span>

<span class="k">Stakeholders</span> <span class="k">of</span> <span class="n">ExampleContext</span> <span class="p">{</span>

  <span class="k">StakeholderGroup</span> <span class="n">Online_Shopping_Company</span> <span class="p">{</span>
    <span class="k">Stakeholder</span> <span class="n">Development_Team</span> <span class="p">{</span>
      <span class="k">influence</span> <span class="k">MEDIUM</span>
      <span class="k">interest</span> <span class="k">HIGH</span>
    <span class="p">}</span>
    <span class="k">Stakeholder</span> <span class="n">Product_Management</span> <span class="p">{</span>
      <span class="k">influence</span> <span class="k">HIGH</span>
      <span class="k">interest</span> <span class="k">HIGH</span>
    <span class="p">}</span>
    <span class="k">Stakeholder</span> <span class="n">Customer_Relationship_Manager</span> <span class="p">{</span>
      <span class="k">influence</span> <span class="k">HIGH</span>
      <span class="k">interest</span> <span class="k">MEDIUM</span>
    <span class="p">}</span>
  <span class="p">}</span>

  <span class="k">Stakeholder</span> <span class="n">Shopper</span> <span class="p">{</span>
    <span class="k">description</span> <span class="s">&quot;Is using the shopping system to by everday goods.&quot;</span>
    
    <span class="k">influence</span> <span class="k">MEDIUM</span>
    <span class="k">interest</span> <span class="k">HIGH</span>
  <span class="p">}</span>

<span class="p">}</span>
</pre></div>
</div>

## Visualization: Stakeholder Map
Once your stakeholders are modelled in CML, you can generate a visual stakeholder map automatically. An example:

![Sample Stakeholder Map (for a new 'same day delivery' feature for an online shop)](./../../img/stakeholder-map-sdd-sample-simple.png)

Check out our [PlantUML generator](/docs/plant-uml/) on how to generate such a diagram.
