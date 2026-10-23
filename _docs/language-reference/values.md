---
title: Value Registers
permalink: /docs/value-registers/
---

The CML language supports the modelling of stakeholders and their values that might be strengthened or harmed by digital systems. This feature has been introduced to support the [Value-Driven Analysis and Design (VDAD)](https://ethical-se.github.io/value-driven-analysis-and-design) process. Context Mapper and the language concepts documented on this page therefore support the modelling of ethical concerns in software projects. For more information about the whole process we refer to the [VDAD page](https://ethical-se.github.io/value-driven-analysis-and-design).

**Note**: Some of the terminology of the language, such as value register or value cluster, is based on the [IEEE Standard Model Process for Addressing Ethical Concerns during System Design (a.k.a. IEEE 7000 standard)](https://ieeexplore.ieee.org/document/9536679). Access to IEEE 7000 standard is free after registration for IEEE Xplore (click on "Access via Subscription"). However, you do not necessarily need to know that terminology; you can also simply model the values of your stakeholders within a `ValueRegister` block.

## Value Register
If you are interested in reading more about the ideas of a _value register_, we refer to the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679) or the [ESE Glossary](https://github.com/ethical-se/ese-practices/blob/main/ESE-Glossary.md). However, if you just want to move on quickly and model the values of your stakeholders - just consider the value register a _container object_ that allows to model values for a specific Bounded Context:

```cml
BoundedContext Online_Shop_Same_Day_Delivery

ValueRegister SDD_Stakeholder_Values for Online_Shop_Same_Day_Delivery {
  // model values inside value register
}
```

If you just want to start to model some values without separating by Bounded Contexts, you can create a `ValueRegister` without that reference:

```cml
ValueRegister SDD_Stakeholder_Values {
  // model values inside value register
}
```

## Values

Inside a value register you can define the values important to your project, software and/or feature:

```cml
ValueRegister SDD_Stakeholder_Values {

  Value Privacy
  Value Respect
  Value Integrity
  Value Love
  // etc.

}
```

The following attributes that can be added, namely whether a value is a _core value_, _value demonstrators_, _related values_ and _opposing values_, follow the terminology of the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679). We refer to the standard for a more detailed introduction into these terms; in CML the attributes are however not mandatory.

```cml
ValueRegister SDD_Stakeholder_Values {

  Value Privacy {
    isCore

    demonstrator = "right to be left alone"
    demonstrator = "the right to refuse sharing private data"
    relatedValue = "Intimacy"
    opposingValue = "Transparency"
    opposingValue = "Inclusiveness"
  }

}
```

As always in CML, the 'equal' (=) sign is optional:

```cml
ValueRegister SDD_Stakeholder_Values {

  Value Privacy {
    isCore

    demonstrator "right to be left alone"
    demonstrator "the right to refuse sharing private data"
    relatedValue "Intimacy"
    opposingValue "Transparency"
    opposingValue "Inclusiveness"
  }

}
```

<div class="alert alert-custom">
<strong>Note:</strong> Just modelling values, as seen here, does not allow you to generate any visualization yet (at least for now). Continue with the section <a href="#stakeholder-priorisation-impact--consequences">Stakeholder Priorisation, Impact & Consequences</a>, to define how important these values are to individual stakeholders and how these stakeholders are affected. After that, you can generate a [Value Impact Map](https://ethical-se.github.io/value-driven-analysis-and-design/practices/value-impact-mapping) with the <a href="/docs/plant-uml/">PlantUML generator</a>.
</div>

## Value Clusters

If one applies or follows the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679), values are clustered around core values. For example, the value _confidentiality_ (a demonstrator could be: _right to be left alone_), is an enabler for the core value of _privacy_. Therefore the value _confidentiality_ would be added to the value cluster with the core value _privacy_. This can be modelled in CML as follows:

```cml
ValueRegister SDD_Stakeholder_Values {

  ValueCluster Privacy {
    core PRIVACY

    Value Confidentiality {
      demonstrator = "right to be left alone"
    }
  }

}
```

The _core value_ can be modelled as shown above, by using the enumeration CML provides. That enumeration contains all _core values_ according to the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679): `AUTONOMY`, `CARE`, `CONTROL`, `FAIRNESS`, `INCLUSIVENESS`, `INNOVATION`, `PERFECTION`, `PRIVACY`, `RESPECT`, `SUSTAINABILITY`, `TRANSPARENCY`, `TRUST`.

Alteratively, you can define the core value by a custom string:

```cml
ValueRegister SDD_Stakeholder_Values {

  ValueCluster MyCluster {
    core "Respect"
  }

}
```

Further note that the attributes `demonstrator`, `relatedValue` and `opposingValue`, as documented for the `Value` object already, can also be applied to value clusters:

```cml
ValueRegister SDD_Stakeholder_Values {

  ValueCluster Privacy {
    core PRIVACY

    demonstrator = "right to be left alone"
    demonstrator = "the right to refuse sharing private data"
    relatedValue = "Intimacy"
    opposingValue = "Transparency"
    opposingValue = "Inclusiveness"
  }

}
```

Generally, you can cluster values in CML but you do not necessarily have to.

<div class="alert alert-custom">
<strong>Note:</strong> Just modelling values and value clusters as seen here does not yet allow you to generate any visualization (at least for now). Continue with the section <a href="#stakeholder-priorisation-impact--consequences">Stakeholder Priorisation, Impact & Consequences</a>, to define how important these values are to the individual stakeholders and how they are affected. After that step, you can generate a <a href="https://ethical-se.github.io/value-driven-analysis-and-design/practices/value-impact-mapping">Value Impact Map</a> with the <a href="/docs/plant-uml/">PlantUML generator</a>.
</div>

## Stakeholder Prioritization, Impact & Consequences

Note that the following model snippets require stakeholder modelling as precondition; please check the page [Stakeholders](/docs/stakeholders/) for the corresponding CML syntax.

The following example illustrates how you can assign the values ​​to the stakeholders who care about them. For each stakeholder you can define the `PRIORITY` this value has for the stakeholder, as well as the `IMPACT`. The `consequences` section allows you to model `good`, `bad`, and `neutral` consequences your system or feature has to the given value - from the perspective of the specific stakeholder:

```cml
BoundedContext SameDayDelivery

Stakeholders of SameDayDelivery {
  StakeholderGroup Customers_and_Shoppers
  StakeholderGroup Delivery_Staff_of_Suppliers
}

ValueRegister SD_Values for SameDayDelivery {
  Value Freedom {
      Stakeholder Customers_and_Shoppers {
        priority HIGH
        impact MEDIUM
        consequences
          good "increased freedom"
      }
      Stakeholder Delivery_Staff_of_Suppliers {
        priority HIGH
        impact HIGH
        consequences
          bad "work-life-balance"
      }
    }
}
```

This is again possible on the level of a `Value`, but as well on a `ValueCluster`:

```cml
BoundedContext SameDayDelivery

Stakeholders of SameDayDelivery {
  StakeholderGroup Customers_and_Shoppers
  StakeholderGroup Delivery_Staff_of_Suppliers
}

ValueRegister SD_Values for SameDayDelivery {
  ValueCluster Freedom {
      core AUTONOMY
      Stakeholder Customers_and_Shoppers {
        priority HIGH
        impact MEDIUM
        consequences
          good "increased freedom"
      }
      Stakeholder Delivery_Staff_of_Suppliers {
        priority HIGH
        impact HIGH
        consequences
          bad "work-life-balance"
      }
    }
}
```

## Mitigation Actions

In case your system has negative impact on values, you might want to model the mitigation actions you consider to implement to reduce harm. The following example shows how to model such mitigation actions in CML:

```cml
BoundedContext SameDayDelivery

Stakeholders of SameDayDelivery {
  StakeholderGroup Drivers
}

ValueRegister SD_Values for SameDayDelivery {
  Value WorkLifeBalance {
    demonstrator "Drivers value a healthy work-life-balance"
    Stakeholder Drivers {
      priority HIGH
      impact HIGH
      consequences
        bad "SDD will harm work-life-balance of drivers"
          action "hire more drivers" ACT
    }
  }
}
```

The action types can be `ACT` (actively do something to reduce harm to values), `MONITOR` (just monitor the issue; maybe to gather more information), or a custom string.

## Example
For a complete example, we refer to the [example repository](https://github.com/ContextMapper/context-mapper-examples). You can find a complete CML model for the "Same Day Delivery" example there. 

Once you have modelled your values and stakeholder priorities and impact, you can generate a [Value Impact Map (VDAD practice)](https://ethical-se.github.io/value-driven-analysis-and-design/practices/value-impact-mapping). The diagram is part of the [PlantUML generator](/docs/plant-uml/).

![Exemplary Value Impact Map - Generated out of a CML model with the PlantUML generator](./../../img/value-impact-map-sdd-sample.png)

## Stakeholders Export to CSV
In addition to the Value Impact Map visualization, you can export your modelled value register data as a CSV file. To do so, use the Freemarker temple [here](https://github.com/ContextMapper/context-mapper-dsl/blob/master/samples/freemarker/csv-files/value-registers.csv.ftl) together with our [Generic Generator (Freemarker Templating)](/docs/generic-freemarker-generator/).

## Additional ESE Formats

The following additional (experimental) CML features allow users to apply [Story Valuation](https://github.com/ethical-se/ese-practices/blob/main/practices/ESE-StoryValuation.md) as proposed in the Ethical Software Engineering (ESE) practice repository. Three ESE notations are supported: _Value Epic_, _Value Weighting_ and _Value Narrative_.

<div class="alert alert-custom">
<strong>Note:</strong> These language features are experimental and currently not used by any generator. The modelled information can therefore not be visualized, except you use the <a href="/docs/generic-freemarker-generator/">Generic Generator (Templating with Freemarker)</a> and process the data on your own.
</div>

```cml
Stakeholders {
  Stakeholder Conference_Participant
}

ValueRegister Conference_Management_Sample {
  ValueEpic Data_Privacy {
    As a Conference_Participant
    I value "data privacy"
    as demonstrated in
      realization of "confidentiality of sensitive personal information such as my passport number"
      reduction of "efficiency of operations for conference mansagement staff"
  }

  ValueWeigthing Data_Privacy {
    In the context of the SOI,
    stakeholder Conference_Participant values "data privacy" more than "efficiency from a registration management staff point of view"
    expecting benefits such as "confidentiality of sensitive personal information"
    running the risk of harms such as "higher conference fees and a slower registration process."
  }
}

ValueRegister Same_Day_Delivery_Sample {
  ValueNarrative Sample_Narrative {
    When the SOI executes "the same say delivery epic (incl. split user stories that meet the INVEST criteria)",
    stakeholders expect it to promote, protect or create "freedom and quality of life",
    possibly degrading or prohibiting "work-life balance of suppliers and shopper privacy"
    with the following externally observable and/or internally auditable behavior:

    "Given: Shop is operational and suited suppliers and logistics firms are available.
    When: Same day delivery is promised during order acceptance and confirmation.
    Then: Order arrives at shipment address until 11:59pm on the same say."
  }
}
```

## Transformations
Note that we offer several transformations that might help modelling stakeholders and their values according to [VDAD (Value-Driven Analysis and Design)](https://ethical-se.github.io/value-driven-analysis-and-design) more efficiently. The transformations are documented on the following page: [Stakeholder and Value Modelling Transformations](/docs/stakeholder-and-value-modelling-transformations/).

