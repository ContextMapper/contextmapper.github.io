---
title: Context Map Suggestions with Service Cutter
permalink: /docs/service-cutter-context-map-suggestions/
---

The [Service Cutter](http://servicecutter.github.io/) tool proposes a structured way to service decomposition. It suggests how a system could be decomposed into services according to 14 prioritized [coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria). Domain model elements are required as input. The tool then applies graph clustering algorithms to identify possible *service cuts*, which are returned as output. The approach was proposed in [this paper](https://www.researchgate.net/publication/307873263_Service_Cutter_A_Systematic_Approach_to_Service_Decomposition).

## Context Mapper Integration
We provide a [Service Cutter library](https://github.com/ContextMapper/service-cutter-library), which is a fork of the original 
[Service Cutter](https://github.com/ServiceCutter/ServiceCutter), to be able to offer its structured decomposition approach in Context Mapper. The library allows you to propose new decomposition suggestions in the form of CML Context Maps. The decompositions are derived from the original [coupling criteria catalog](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).

Once you have modeled your system in [CML](/docs/language-reference/) or [discovered it from existing code](/docs/reverse-engineering/), you can generate new decomposition suggestions or _service cuts_ by using the following context menu entry:

<a href="/img/service-cut-generator-context-menu.png">![Generate New Service Cuts (Context Menu)](/img/service-cut-generator-context-menu.png)</a>

### Input and Preconditions
Service Cutter needs the system to be described in entities and so-called *nanoentities*. This structure is automatically derived from your CML model. The following **preconditions** have to be fulfilled so that we are able to derive the basic structure of your system required by Service Cutter ([ERD](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) part):

 * Your CML model must include Bounded Contexts with entities and attributes.
    * Without attributes, we cannot derive nanoentities and Service Cutter cannot calculate decompositions.

#### User Representations

In addition to the basic structures (including Bounded Contexts, Aggregates, domain objects, and attributes), Service Cutter takes so-called [user representations](https://github.com/ServiceCutter/ServiceCutter/wiki/User-Representations) which improve the suggested service cuts immensely. The [CML language](/docs/language-reference/) offers corresponding features so that Context Mapper can derive all the user representations automatically. Of course, we can only derive individual user representations if you use the corresponding CML features. The following list shows how the representations are derived and which CML features you have to use:

 * [Use Cases](https://github.com/ServiceCutter/ServiceCutter/wiki/Use-Cases): The use cases for Service Cutter are derived from the CML use cases and/or user stories. You can find examples how to model them [here](/docs/user-requirements/). Also have a look at [Olaf Zimmermann's blogpost](https://ozimmer.ch/practices/2020/06/10/ICWEKeynoteAndDemo.html) for an enhanced example.
   * **Note**: You have to specify your use cases with entities and their attributes, otherwise we cannot use them as user representations in Service Cutter.
 * [Shared Owner Groups](https://github.com/ServiceCutter/ServiceCutter/wiki/Shared-owner-groups): Shared owner groups are derived automatically, if you [assign owners to your Aggregates (define which development teams own which parts of the system/code)](/docs/aggregate/#aggregate-owner).
 * [Aggregates](https://github.com/ServiceCutter/ServiceCutter/wiki/Aggregates): [Aggregates](/docs/aggregate/) are first-class citizens in CML. Thus, the Aggregates for Service Cutter are simply derived by the CML Aggregates.
 * [Entities](https://github.com/ServiceCutter/ServiceCutter/wiki/Entities): [Entities](/docs/tactic-ddd/) are first-class citizens in CML. Thus, the Entities for Service Cutter are simply derived by the CML Entities, Value Objects, and Domain Events (see [tactic DDD](/docs/tactic-ddd/)).
 * [Predefined Services](https://github.com/ServiceCutter/ServiceCutter/wiki/Predefined-services): Predefined services are derived by the [Bounded Contexts](/docs/bounded-context/) you already provide before calling the service cut generator. This means: each Bounded Context you already identified is mapped to a predefined service.
 * [Separated Security Zones](https://github.com/ServiceCutter/ServiceCutter/wiki/Separated-security-zones): The CML language allows you to [assign each Aggregate to a _security zone_](/docs/aggregate/#security-zones). Thereby you can indicate that parts of your Bounded Contexts must be realized in _separated security zones_.
 * [Security Access Groups](https://github.com/ServiceCutter/ServiceCutter/wiki/Security-access-groups): The CML language allows you to [assign each Aggregate to a _security access group_](/docs/aggregate/#security-access-groups). Thereby you can indicate that parts of your Bounded Contexts have different security access requirements.
 * [Compatibilities](https://github.com/ServiceCutter/ServiceCutter/wiki/Compatibilities): All compatibilities (`contentVolatility`, `structuralVolatility`, `availabilityCriticality`, `consistencyCriticality`, `storageSimilarity`, and `securityCriticality`) can be [modeled on Aggregate level in CML](/docs/aggregate/#characteristics-classification).
    
### Solver Configuration
Once you generated your first service cut you will find a `.servicecutter.yml` file in the root directory of your project: (if you work with Eclipse you have to disable the _.* resources_ filter to see the file in the project/file/package explorer)

<a href="/img/service-cut-generator-config-file.png">![Service Cut Generator Configuration File](/img/service-cut-generator-config-file.png)</a>

In this file you can customize the priority of each coupling criterion, as you can in Service Cutter. You can further change the clustering algorithms. Details about the config file can be found [here](/docs/service-cutter-config-file/).

### Example Result
When calling _Propose New Service Cut_, Context Mapper will create a new CML file with a new decomposition suggestion. 
This is *one* example decomposition generated for the 
[DDD cargo sample application](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/ddd-sample): 

<a href="/img/service-cut-generator-ddd-sample-result.png">![Service Cut Generator Example Result (DDD Cargo sample application)](/img/service-cut-generator-ddd-sample-result.png)</a>

Besides decomposition suggestion itself, Context Mapper will generate a [Graphviz DOT file (*.gv)](https://de.wikipedia.org/wiki/DOT_(GraphViz)) that represents the graph that was used by Service Cutter (for the graph clustering). 

<a href="/img/service-cutter-gv-file-screenshot.png">![Generated GraphViz File (Example Screenshot)](/img/service-cutter-gv-file-screenshot.png)</a>

This file can help to understand and retrace the result produced by Service Cutter. Each edge of the graph has a comment that explains the weight value that has been calculated on the basis of the coupling criteria.

You can further use online tools such as [http://webgraphviz.com/](http://webgraphviz.com/) and [http://graphviz.it](http://graphviz.it) to illustrate the graph graphically: (just copy the file content into their editors)

<a href="/img/service-cutter-gv-file-online-screenshot.png">![Generated GraphViz File in Online Editor (Example Screenshot)](/img/service-cutter-gv-file-online-screenshot.png)</a>

**Note:** The graph that Service Cutter uses gets huge very quick. In our experience these online visualization tools can often not generate the visual graphs due to their complexity and size.

## Service Cutter Input File Generators
If you want to work with the original [Service Cutter](http://servicecutter.github.io/) tool, a [JHipster](https://www.jhipster.tech/) application, you can also use our [Service Cutter generators](/docs/service-cutter/) to derive the needed input files in the JSON format from your Context Map. Simply save them as JSON files (in Context Mapper) and upload them there (in the original Service Cutter). We also describe this in our [service decomposition tutorial](/docs/systematic-service-decomposition/).
