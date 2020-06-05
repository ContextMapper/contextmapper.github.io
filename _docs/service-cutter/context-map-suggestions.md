---
title: Context Map Suggestions with Service Cutter
permalink: /docs/service-cutter-context-map-suggestions/
---

The [Service Cutter](http://servicecutter.github.io/) tool proposes a structured way to service decomposition. It suggests how a system could be decomposed into services according 
to 14 prioritized [coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria). Domain model elements are required as input. The tool then applies 
graph clustering algorithms to identify possible *service cuts*, which are returned as output. The approach was proposed by 
[this paper](https://link.springer.com/chapter/10.1007/978-3-319-44482-6_12).

<div class="alert alert-custom">
<strong>Note:</strong> This feature is not yet supported in our new Visual Studio Code extension. We continuously work on the extension and will support it soon! To use this feature you have to use the Eclipse plugin for now. You can find a feature support table for Eclipse and VS Code <a href="/docs/ide/">here</a>.
</div>

## Context Mapper Integration
We provide a [Service Cutter library](https://github.com/ContextMapper/service-cutter-library), which is a fork of the original 
[Service Cutter](https://github.com/ServiceCutter/ServiceCutter), to be able to offer its structured decomposition approach in Context Mapper. The library allows you to generate 
new decomposition suggestions in the form of CML Context Maps. The decompositions are derived from the original 
[coupling criteria catalog](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

Once you have modeled your system in [CML](/docs/language-reference/) or [discovered it from existing code](/docs/reverse-engineering/), you can generate new decomposition suggestions or _service cuts_ by using the following context menu entry:

<a href="/img/service-cut-generator-context-menu.png">![Generate New Service Cuts (Context Menu)](/img/service-cut-generator-context-menu.png)</a>

### Input and Preconditions
Service Cutter needs the system to be described in entities and so-called *nanoentities*. This structure is automatically derived from your CML model. In addition, you can provide user representations (use cases etc.) to improve the quality of the cuts. Thus, you can generate new Context Maps describing service decompositions with the following input:

 * CML file describing your system
 * **Optionally:** User descriptions in form of a SCL (Service Cutter Language) file.
    * You can find out [here](/docs/service-cutter/) how to create such file.
    
The following **preconditions** have to be fulfilled so that we are able to derive the structure required by Service Cutter 
(called [ERD](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)):

 * Your CML model must include Bounded Contexts with entities and attributes.
    * Without attributes, we cannot derive nanoentities and Service Cutter cannot calculate decompositions.
    
Note that if the _Leung_ algorithm is used, the decompositions can be different every time the generator is called (it is a non-deterministic algorithm).

### Solver Configuration
A dialog will allow you to configure the following inputs needed by Service Cutter:

 * **The algorithm**: Currently we only provide one algorithm, but others are forseen to be added in future releases (note that the _Girvan-Newman_ algorithm supported by Service Cutter cannot be integrated into Context Mapper due to licence issues). 
 * **Coupling criteria priorities**: You can customize the priority of each coupling criterion, as you can in Service Cutter.
 * **User representations (optional)**: The user representations can be provided with our SCL (Service Cutter Language) DSL. You can find out how to create/generate such a file [here](/docs/service-cutter/#generate-scl-file).

<a href="/img/service-cut-generator-dialog.png">![Service Cut Generator Dialog](/img/service-cut-generator-dialog.png)</a>

### Example Result
When finishing the wizard illustrated above, Context Mapper will create a new CML file with a new decomposition suggestion. Note that the Leung algorithm is non-deterministic and will derive new decompositions every time you execute it. 
This is *one* example decomposition generated for the 
[DDD cargo sample application](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/ddd-sample): 

<a href="/img/service-cut-generator-ddd-sample-result.png">![Service Cut Generator Example Result (DDD Cargo sample application)](/img/service-cut-generator-ddd-sample-result.png)</a>

*Known limitation*: Please note that the resulting model does not contain the original data types. We currently loose this information through the cutting process. However, the results still show how the entities are mapped to Bounded Contexts and how the single attributes are mapped to the entities. 

## Service Cutter Input File Generators
If you want to work with the original [Service Cutter](http://servicecutter.github.io/) tool, a [JHipster](https://www.jhipster.tech/) application, you can also use our [Service Cutter generators](/docs/service-cutter/) to derive the needed input files in the JSON format from your Context Map. Simply save them here (in Context Mapper) and upload them there (in the original Service Cutter). 
