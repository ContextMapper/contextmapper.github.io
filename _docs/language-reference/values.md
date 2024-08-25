---
title: Value Registers
permalink: /docs/value-registers/
---

The CML language supports the modelling of stakeholders and their values that might be strengthened or harmed by digital systems. This feature has been introduced to support the [JEDi project](tbd) and its Value-Driven Analysis and Design (VDAD) process. Context Mapper and the language concepts documented on this page therefore support the modelling of ethical concerns in software projects. For more information about the whole process we refer to the [JEDi page](tbd).

**Note**: Some of the terminology of the language, such as value register or value cluster, is based on the [IEEE Standard Model Process for Addressing Ethical Concerns during System Design (a.k.a. IEEE 7000 standard)](https://ieeexplore.ieee.org/document/9536679). However, you do not necessarily need to know that terminology; you can also simply model the values of your stakeholders within a `ValueRegister` block.

## Value Register
If you are interested in reading more about the ideas of a _value register_, we refer to the [Glossary of ESE](https://github.com/ethical-se/ese-practices/blob/main/ESE-Glossary.md) or the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679). However, if you just want to move on quickly and model the values of your stakeholders - just consider the value register a _container object_ that allows to model values for a specific Bounded Context:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">BoundedContext</span> <span class="n">Online_Shop_Same_Day_Delivery</span>

<span class="k">ValueRegister</span> <span class="n">SDD_Stakeholder_Values</span> <span class="k">for</span> <span class="n">Online_Shop_Same_Day_Delivery</span> <span class="p">{</span>
  <span class="c1">// model values inside value register</span>
<span class="p">}</span>
</pre></div>
</div>

If you just want to start to model some values without separating by Bounded Contexts, you can create a `ValueRegister` without that reference:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">ValueRegister</span> <span class="n">SDD_Stakeholder_Values</span> <span class="p">{</span>
  <span class="c1">// model values inside value register</span>
<span class="p">}</span>
</pre></div>
</div>

## Values

Inside a value register you can define the values important to your project, software and/or feature:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">ValueRegister</span> <span class="n">SDD_Stakeholder_Values</span> <span class="p">{</span>
  
  <span class="k">Value</span> <span class="n">Privacy</span>
  <span class="k">Value</span> <span class="n">Respect</span>
  <span class="k">Value</span> <span class="n">Integrity</span>
  <span class="k">Value</span> <span class="n">Love</span>
  <span class="c1">// etc.</span>

<span class="p">}</span>
</pre></div>
</div>

The following attributes that can be added, namely whether a value is a _core value_, _value demonstrators_, _related values_ and _opposing values_, follow the terminology of the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679). We refer to the standard or the [ESE Glossary](https://github.com/ethical-se/ese-practices/blob/main/ESE-Glossary.md) for a more detailed introduction into these terms; in CML the attributes are however not mandatory.

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">ValueRegister</span> <span class="n">SDD_Stakeholder_Values</span> <span class="p">{</span>
  
  <span class="k">Value</span> <span class="n">Privacy</span> <span class="p">{</span>
    <span class="k">isCore</span>

    <span class="k">demonstrator</span> = <span class="s">&quot;right to be left alone&quot;</span>
    <span class="k">demonstrator</span> = <span class="s">&quot;the right to refuse sharing private data&quot;</span>
    <span class="k">relatedValue</span> = <span class="s">&quot;Intimacy&quot;</span>
    <span class="k">opposingValue</span> = <span class="s">&quot;Transparency&quot;</span>
    <span class="k">opposingValue</span> = <span class="s">&quot;Inclusiveness&quot;</span>
  <span class="p">}</span>

<span class="p">}</span>
</pre></div>
</div>

As always in CML, the 'equal' (=) sign is optional:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">ValueRegister</span> <span class="n">SDD_Stakeholder_Values</span> <span class="p">{</span>
  
  <span class="k">Value</span> <span class="n">Privacy</span> <span class="p">{</span>
    <span class="k">isCore</span>

    <span class="k">demonstrator</span> <span class="s">&quot;right to be left alone&quot;</span>
    <span class="k">demonstrator</span> <span class="s">&quot;the right to refuse sharing private data&quot;</span>
    <span class="k">relatedValue</span> <span class="s">&quot;Intimacy&quot;</span>
    <span class="k">opposingValue</span> <span class="s">&quot;Transparency&quot;</span>
    <span class="k">opposingValue</span> <span class="s">&quot;Inclusiveness&quot;</span>
  <span class="p">}</span>

<span class="p">}</span>
</pre></div>
</div>

<div class="alert alert-custom">
<strong>Note:</strong> Just by modelling values as seen here, does not allow you to generate any visualization (at least for now). Continue with the section <a href="#stakeholder-priorisation-impact--consequences">Stakeholder Priorisation, Impact & Consequences</a>, do define how important these values are to the individual stakeholders and how they are affected. After that you can generate a [Value Stakeholder Map](tbd) wit the <a href="/docs/plant-uml/">PlantUML generator</a>.
</div>

## Value Clusters

If one applies or follows the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679), values are clustered around core values. For example, the value _confidentiality_ (a demonstrator could be: _right to be left alone_), is an enabler for the core value of _privacy_. Therefore the value _confidentiality_ would be added to the value cluster with the core value _privacy_. This can be modelled in CML as follows:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">ValueRegister</span> <span class="n">SDD_Stakeholder_Values</span> <span class="p">{</span>
  
  <span class="k">ValueCluster</span> <span class="n">Privacy</span> <span class="p">{</span>
    <span class="k">core</span> <span class="k">PRIVACY</span>

    <span class="k">Value</span> <span class="n">Confidentiality</span> <span class="p">{</span>
      <span class="k">demonstrator</span> = <span class="s">&quot;right to be left alone&quot;</span>  
    <span class="p">}</span>
  <span class="p">}</span>

<span class="p">}</span>
</pre></div>
</div>

The _core value_ can be modelled as shown above, by using the enumeration CML provides. That enumeration contains all _core values_ according to the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679): `AUTONOMY`, `CARE`, `CONTROL`, `FAIRNESS`, `INCLUSIVENESS`, `INNOVATION`, `PERFECTION`, `PRIVACY`, `RESPECT`, `SUSTAINABILITY`, `TRANSPARENCY`, `TRUST`.

Alteratively, you can define the core value by a custom string:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">ValueRegister</span> <span class="n">SDD_Stakeholder_Values</span> <span class="p">{</span>
  
  <span class="k">ValueCluster</span> <span class="n">MyCluster</span> <span class="p">{</span>
    <span class="k">core</span> <span class="s">&quot;Respect&quot;</span>
  <span class="p">}</span>

<span class="p">}</span>
</pre></div>
</div>

Further note that the attributes `demonstrator`, `relatedValue` and `opposingValue`, as documented for the `Value` object already, can also be applied to value clusters:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">ValueRegister</span> <span class="n">SDD_Stakeholder_Values</span> <span class="p">{</span>
  
  <span class="k">ValueCluster</span> <span class="n">Privacy</span> <span class="p">{</span>
    <span class="k">core</span> <span class="k">PRIVACY</span>

    <span class="k">demonstrator</span> = <span class="s">&quot;right to be left alone&quot;</span>
    <span class="k">demonstrator</span> = <span class="s">&quot;the right to refuse sharing private data&quot;</span>
    <span class="k">relatedValue</span> = <span class="s">&quot;Intimacy&quot;</span>
    <span class="k">opposingValue</span> = <span class="s">&quot;Transparency&quot;</span>
    <span class="k">opposingValue</span> = <span class="s">&quot;Inclusiveness&quot;</span>
  <span class="p">}</span>

<span class="p">}</span>
</pre></div>
</div>

Generally, you can cluster values in CML but you do not necessarily have to.

<div class="alert alert-custom">
<strong>Note:</strong> Just by modelling values and value clusters as seen here, does not allow you to generate any visualization (at least for now). Continue with the section <a href="#stakeholder-priorisation-impact--consequences">Stakeholder Priorisation, Impact & Consequences</a>, do define how important these values are to the individual stakeholders and how they are affected. After that you can generate a [Value Stakeholder Map](tbd) wit the <a href="/docs/plant-uml/">PlantUML generator</a>.
</div>

## Stakeholder Prioritization, Impact & Consequences

Note that the following model snippets require stakeholder modelling as precondition; please check the page [Stakeholders](/docs/stakeholders/) for the corresponding CML syntax.

The following example illustrates how you can assign the values ​​to the stakeholders who care about them. For each stakeholder you can define the `PRIORITY` this value has for the stakeholder, as well as the `IMPACT`. The `consequences` section allows you to model `good`, `bad`, and `neutral` consequences your system or feature has to the given value - from the perspective of the specific stakeholder:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">BoundedContext</span> <span class="n">SameDayDelivery</span>

<span class="k">Stakeholders</span> <span class="k">of</span> <span class="n">SameDayDelivery</span> <span class="p">{</span>
  <span class="k">StakeholderGroup</span> <span class="n">Customers_and_Shoppers</span>
  <span class="k">StakeholderGroup</span> <span class="n">Delivery_Staff_of_Suppliers</span>
<span class="p">}</span>

<span class="k">ValueRegister</span> <span class="n">SD_Values</span> <span class="k">for</span> <span class="n">SameDayDelivery</span> <span class="p">{</span>  
  <span class="k">Value</span> <span class="n">Freedom</span> <span class="p">{</span>
      <span class="k">Stakeholder</span> <span class="n">Customers_and_Shoppers</span> <span class="p">{</span>
        <span class="k">priority</span> <span class="k">HIGH</span>
        <span class="k">impact</span> <span class="k">MEDIUM</span>
        <span class="k">consequences</span>
          <span class="k">good</span> <span class="s">&quot;increased freedom&quot;</span>
      <span class="p">}</span>
      <span class="k">Stakeholder</span> <span class="n">Delivery_Staff_of_Suppliers</span> <span class="p">{</span>
        <span class="k">priority</span> <span class="k">HIGH</span>
        <span class="k">impact</span> <span class="k">HIGH</span>
        <span class="k">consequences</span>
          <span class="k">bad</span> <span class="s">&quot;work-life-balance&quot;</span>
      <span class="p">}</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>

This is again possible on the level of a `Value`, but as well on a `ValueCluster`:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">BoundedContext</span> <span class="n">SameDayDelivery</span>

<span class="k">Stakeholders</span> <span class="k">of</span> <span class="n">SameDayDelivery</span> <span class="p">{</span>
  <span class="k">StakeholderGroup</span> <span class="n">Customers_and_Shoppers</span>
  <span class="k">StakeholderGroup</span> <span class="n">Delivery_Staff_of_Suppliers</span>
<span class="p">}</span>

<span class="k">ValueRegister</span> <span class="n">SD_Values</span> <span class="k">for</span> <span class="n">SameDayDelivery</span> <span class="p">{</span>  
  <span class="k">ValueCluster</span> <span class="n">Freedom</span> <span class="p">{</span>
      <span class="k">core</span> <span class="n">AUTONOMY</span>
      <span class="k">Stakeholder</span> <span class="n">Customers_and_Shoppers</span> <span class="p">{</span>
        <span class="k">priority</span> <span class="k">HIGH</span>
        <span class="k">impact</span> <span class="k">MEDIUM</span>
        <span class="k">consequences</span>
          <span class="k">good</span> <span class="s">&quot;increased freedom&quot;</span>
      <span class="p">}</span>
      <span class="k">Stakeholder</span> <span class="n">Delivery_Staff_of_Suppliers</span> <span class="p">{</span>
        <span class="k">priority</span> <span class="k">HIGH</span>
        <span class="k">impact</span> <span class="k">HIGH</span>
        <span class="k">consequences</span>
          <span class="k">bad</span> <span class="s">&quot;work-life-balance&quot;</span>
      <span class="p">}</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>

## Mitigation Actions

In case your system has negative impact on values, you might want to model the mitigation actions you consider to implement to reduce harm. The following example shows how to model such mitigation actions in CML:

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">BoundedContext</span> <span class="n">SameDayDelivery</span>

<span class="k">Stakeholders</span> <span class="k">of</span> <span class="n">SameDayDelivery</span> <span class="p">{</span>
  <span class="k">StakeholderGroup</span> <span class="n">Drivers</span>
<span class="p">}</span>

<span class="k">ValueRegister</span> <span class="n">SD_Values</span> <span class="k">for</span> <span class="n">SameDayDelivery</span> <span class="p">{</span>  
  <span class="k">Value</span> <span class="n">WorkLifeBalance</span> <span class="p">{</span>
    <span class="k">demonstrator</span> <span class="s">&quot;Drivers value a healthy work-life-balance&quot;</span>
    <span class="k">Stakeholder</span> <span class="n">Drivers</span> <span class="p">{</span>
      <span class="k">priority</span> <span class="k">HIGH</span>
      <span class="k">impact</span> <span class="k">HIGH</span>
      <span class="k">consequences</span>
        <span class="k">bad</span> <span class="s">&quot;SDD will harm work-life-balance of drivers&quot;</span>
          <span class="k">action</span> <span class="s">&quot;hire more drivers&quot;</span> <span class="k">ACT</span>
    <span class="p">}</span>
  <span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>

The action types can be `ACT` (actively do something to reduce harm to values), `MONITOR` (just monitor the issue; maybe to gather more information), or a custom string.

## Example
For a complete example, we refer to the [example repository](https://github.com/ContextMapper/context-mapper-examples). There you can find a complete CML model for the "Same Day Delivery" example. 

Once you have modelled your values and stakeholder priorities and impact, you can generate a [Value Impact Map as suggested by the JEDi project](tbd). The diagram is part of the [PlantUML generator](/docs/plant-uml/).

![Exemplary Value Impact Map - Generated out of a CML model with the PlantUML generator](./../../img/value-impact-map-sdd-sample.png)

## Additional ESE Formats

The following additional (experimental) CML features allow users to apply [Story Valuation by ESE](https://github.com/ethical-se/ese-practices/blob/main/practices/ESE-StoryValuation.md) and use the suggested notations _Value Epic_, _Value Weighting_ and _Value Narrative_.

<div class="alert alert-custom">
<strong>Note:</strong> These language features are experimental and currently not used by any generator. The modelled information can therefore not be visualized, except you use the <a href="/docs/generic-freemarker-generator/">Generic Generator (Templating with Freemarker)</a> and process the data on your own.
</div>

<div class="highlight"><div class="highlight"><pre><span></span><span class="k">Stakeholders</span> <span class="p">{</span>
  <span class="k">Stakeholder</span> <span class="n">Conference_Participant</span>
<span class="p">}</span>

<span class="k">ValueRegister</span> <span class="n">Conference_Management_Sample</span> <span class="p">{</span>  
  <span class="k">ValueEpic</span> <span class="n">Data_Privacy</span> <span class="p">{</span>
    <span class="k">As</span> <span class="k">a</span> <span class="n">Conference_Participant</span>
    <span class="k">I</span> <span class="k">value</span> <span class="s">&quot;data privacy&quot;</span>
    <span class="k">as</span> <span class="k">demonstrated</span> <span class="k">in</span> 
      <span class="k">realization</span> <span class="k">of</span> <span class="s">&quot;confidentiality of sensitive personal information such as my passport number&quot;</span> 
      <span class="k">reduction</span> <span class="k">of</span> <span class="s">&quot;efficiency of operations for conference mansagement staff&quot;</span>
  <span class="p">}</span>

  <span class="k">ValueWeigthing</span> <span class="n">Data_Privacy</span> <span class="p">{</span>
    <span class="k">In the context of the SOI</span>,
    <span class="k">stakeholder</span> <span class="n">Conference_Participant</span> <span class="k">values</span> <span class="s">&quot;data privacy&quot;</span> <span class="k">more than</span> <span class="s">&quot;efficiency from a registration management staff point of view&quot;</span>
    <span class="k">expecting benefits such as</span> <span class="s">&quot;confidentiality of sensitive personal information&quot;</span>
    <span class="k">running the risk of harms such as</span> <span class="s">&quot;higher conference fees and a slower registration process.&quot;</span>
  <span class="p">}</span>
<span class="p">}</span>

<span class="k">ValueRegister</span> <span class="n">Same_Day_Delivery_Sample</span> <span class="p">{</span>
  <span class="k">ValueNarrative</span> <span class="n">Sample_Narrative</span> <span class="p">{</span>
    <span class="k">When the SOI executes</span> <span class="s">&quot;the same say delivery epic (incl. split user stories that meet the INVEST criteria)&quot;</span>,
    <span class="k">stakeholders expect it to promote, protect or create</span> <span class="s">&quot;freedom and quality of life&quot;</span>,
    <span class="k">possibly degrading or prohibiting</span> <span class="s">&quot;work-life balance of suppliers and shopper privacy&quot;</span>
    <span class="k">with the following externally observable and/or internally auditable behavior</span>:

    <span class="s">&quot;Given: Shop is operational and suited suppliers and logistics firms are available. </span>
<span class="s">    When: Same day delivery is promised during order acceptance and confirmation. </span>
<span class="s">    Then: Order arrives at shipment address until 11:59pm on the same say.&quot;</span>
  <span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
