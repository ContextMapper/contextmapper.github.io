---
title: "Value-Driven Analysis and Design (VDAD) Support"
permalink: /docs/vdad-support/
---

Context Mapper offers tool support for multiple steps of the [Value-Driven Analysis and Design](https://ethical-se.github.io/value-driven-analysis-and-design) process (such as [Stakeholder Mapping](https://ethical-se.github.io/value-driven-analysis-and-design/practices/stakeholder-mapping) and [Value Impact Mapping](https://ethical-se.github.io/value-driven-analysis-and-design/practices/value-impact-mapping)) as well as [Story Valuation](https://github.com/ethical-se/ese-practices/blob/main/practices/ESE-StoryValuation.md) by [Ethical Software Engineering (ESE)](https://github.com/ethical-se/ese-practices). 

## Language Features

The following pages document the CML features that support modelling stakeholders of a project or system and the ethical values important to them:

 * [Stakeholder](/docs/stakeholders/)
 * [Value Registers](/docs/value-registers/)
 * [User Requirements (see "Story Valuation")](/docs/user-requirements/#story-valuation)

## Transformations

Context Mapper provides several transformations that ease the modelling of stakeholders and their values. These transformations are documented [here](/docs/stakeholder-and-value-modelling-transformations/).

## Generators

By using the language features mentioned above, you can automatically generate:

 * [Stakeholder Maps](https://ethical-se.github.io/value-driven-analysis-and-design/practices/stakeholder-mapping) with our [PlantUML generator](/docs/plant-uml/)
 * [Value Impact Maps](https://ethical-se.github.io/value-driven-analysis-and-design/practices/value-impact-mapping) with our [PlantUML generator](/docs/plant-uml/)
 * CSV files with the stakeholder data by using our [Generic Generator (Freemarker Templating)](/docs/generic-freemarker-generator/)
 * CSV files with the value register data by using our [Generic Generator (Freemarker Templating)](/docs/generic-freemarker-generator/)

**Note**: The freemarker templates can be found [here](https://github.com/ContextMapper/context-mapper-dsl/tree/master/org.contextmapper.dsl.ui/samples/freemarker/csv-files). 

## Background and Further Information

For more information about the project and our initiatives towards ethical- and value-driven (software) engineering we refer to our project repositories:

 * [Value-Driven Analysis and Design (VDAD)](https://github.com/ethical-se/value-driven-analysis-and-design)
 * [Ethical Software Engineering (ESE)](https://github.com/ethical-se/ese-practices)
