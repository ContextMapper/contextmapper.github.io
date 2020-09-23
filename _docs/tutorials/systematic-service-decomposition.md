---
title: Systematic Service Decomposition with Context Mapper and Service Cutter
permalink: /docs/systematic-service-decomposition/
image: /img/cm-og-image.png
---

Context Mapper provides a generator that decomposes your domain model into Bounded Contexts in a systematic manner. The service decomposition tool is based on [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/). Based on a [catalog of 16 coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria) and a graph clustering algorithm, the generator suggests how an application could be decomposed into Bounded Contexts, services, or components.

Note that it is not our goal to automate the job of domain modelers and software architects! The generated decompositions are just suggestions and can give you hints how your domain objects are coupled. Don't expect that the perfect decomposition is generated for you without questioning it.

This tutorial illustrates how you can use Service Cutter inside Context Mapper, or export your domain model for Service Cutter out of a CML file.

## The Domain Model
We use the [DDD sample application (Cargo Tracking)](https://github.com/citerus/dddsample-core) for this tutorial. As a first step, we modeled the domain of the application in CML. You can find the model [here](https://github.com/ContextMapper/context-mapper-examples/blob/master/src/main/cml/ddd-service-cutting-sample/DDD-Sample.cml).

We modeled the domain inside one single Bounded Context. The context contains four Aggregates with its Entities and Value Objects:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CargoTracking {
  <span class="k">Aggregate</span> Cargo {
    <span class="k">owner</span> CargoPlaner

    <span class="k">Entity</span> Cargo {
      <span class="k">aggregateRoot</span>
      - <span class="k">TrackingId</span> trackingId
      - <span class="k">Location</span> origin
      - <span class="k">RouteSpecification</span> routeSpecification
      - <span class="k">Itinerary</span> itinerary
      - <span class="k">Delivery</span> delivery
    }
    <span class="c">/* shortened Aggregate here */</span>
  }
  <span class="k">Aggregate</span> Location {
    <span class="k">owner</span> Administrators

    <span class="k">Entity</span> Location {
      <span class="k">aggregateRoot</span>
      - <span class="k">UnLocode</span> unLocode
      <span class="k">String</span> name
    }
    <span class="c">/* shortened Aggregate here */</span>
  }
  <span class="k">Aggregate</span> Handling {
    <span class="k">owner</span> CargoTracker

    <span class="k">DomainEvent</span> HandlingEvent {
      - <span class="k">HandlingEventType</span> handlingEventType
      - <span class="k">Voyage</span> voyage
      - <span class="k">Location</span> location
      <span class="k">Date</span> completionTime
      <span class="k">Date</span> registrationTime
      - <span class="k">Cargo</span> cargo
    }
    <span class="c">/* shortened Aggregate here */</span>
  }
  <span class="k">Aggregate</span> Voyage {
    <span class="k">owner</span> VoyageManager

    <span class="k">Entity</span> Voyage {
      <span class="k">aggregateRoot</span>
      - <span class="k">VoyageNumber</span> voyageNumber
      - <span class="k">Schedule</span> schedule
    }
    <span class="c">/* shortened Aggregate here */</span>
  }
}
</pre></div>

The CML code above just gives you an impression how the model looks like but is shortened a lot. Find the complete model [here](https://github.com/ContextMapper/context-mapper-examples/blob/master/src/main/cml/ddd-service-cutting-sample/DDD-Sample.cml). The following PlantUML diagram (generated with Context Mapper) illustrates the domain model graphically:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-ddd-sample-plantuml.png">![DDD Sample Application Domain Model (PlantUML generated with Context Mapper)](/img/systematic-service-decomposition-tutorial-ddd-sample-plantuml.png)</a>

## Use Case Modeling
With a Bounded Context definition as the one above you are already able to generate new service decompositions or Service Cutter files. However, we highly recommend to model your use cases as well, since they have a big impact on the ideal service decomposition.

On the [User Requirements](/docs/user-requirements/) page of our language reference you can find out how use cases or user stories are modeled in CML. For this tutorial based on the DDD sample application we modeled the use cases provided by the [Service Cutter sample files](https://github.com/ServiceCutter/ServiceCutter/tree/master/Samples):

<div class="highlight"><pre><span></span><span class="k">UseCase</span> ViewTracking {
  <span class="k">interactions</span>
    <span class="k">read</span> <span class="s">&quot;Cargo&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;trackindId&quot;</span>,
    <span class="k">read</span> <span class="s">&quot;HandlingEvent&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;handlingEventType&quot;</span>, <span class="s">&quot;location&quot;</span>, <span class="s">&quot;completionTime&quot;</span>,
    <span class="k">read</span> <span class="s">&quot;Delivery&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;transportStatus&quot;</span>, <span class="s">&quot;estimatedArrivalTime&quot;</span>, <span class="s">&quot;misdirected&quot;</span>, 
    <span class="k">read</span> <span class="s">&quot;Voyage&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;voyageNumber&quot;</span>,
    <span class="k">read</span> <span class="s">&quot;RouteSpecification&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;destination&quot;</span>
}

<span class="k">UseCase</span> ViewCargos {
  <span class="k">interactions</span>
    <span class="k">read</span> <span class="s">&quot;Cargo&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;trackingId&quot;</span>,
    <span class="k">read</span> <span class="s">&quot;RouteSpecification&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;destination&quot;</span>, <span class="s">&quot;arrivalDeadline&quot;</span>,
    <span class="k">read</span> <span class="s">&quot;Delivery&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;routingStatus&quot;</span>
}

<span class="k">UseCase</span> BookCargo {
  <span class="k">interactions</span>
    <span class="k">read</span> <span class="s">&quot;Location&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;unLocode&quot;</span>,
    <span class="k">update</span> <span class="s">&quot;Cargo&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;trackingId&quot;</span>,
    <span class="k">update</span> <span class="s">&quot;RouteSpecification&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;origin&quot;</span>, <span class="s">&quot;arrivalDeadline&quot;</span>, <span class="s">&quot;destination&quot;</span>
}

<span class="k">UseCase</span> ChangeCargoDestination {
  <span class="k">interactions</span>
    <span class="k">read</span> <span class="s">&quot;Cargo&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;trackingId&quot;</span>,
    <span class="k">read</span> <span class="s">&quot;RouteSpecification&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;destination&quot;</span>,
    <span class="k">update</span> <span class="s">&quot;RouteSpecification&quot;</span> <span class="k">with</span> <span class="k">its</span> <span class="s">&quot;destination&quot;</span>
}

<span class="c">/* we shortened this listing to save space (find all use cases in the original CML file) */</span>
</pre></div>

Note that we only modeled the Entities with its _read_ and _written_ attributes (nanoentities) here. The CML syntax allows you to add [more details to use cases and/or user stories](/docs/user-requirements/), but the information above are absolutely necessary for Context Mapper to use the cases/stories as user representations in Service Cutter.

The CML use cases or user stories will be mapped to the Service Cutter's [_Use Case_ definition](https://github.com/ServiceCutter/ServiceCutter/wiki/Use-Cases).

## Define Owners (Teams)
A Bounded Contexts is not necessarily a system or component. A team can constitute a Bounded Context as well. If you decompose a system you should respect existing teams (code and domain model owners) as well, since they have an influence to the coupling. In CML you can assign owners on the level of Aggregates.

This might not make sense for the DDD sample application, as the domain model is not that big. However, we assigned the Aggregates to four different teams to illustrate how this is done:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CargoTracking {
  <span class="k">Aggregate</span> Cargo {
    <span class="k">owner</span> CargoPlaner

    <span class="c">/* removed content here to save space */</span>
  }
  <span class="k">Aggregate</span> Location {
    <span class="k">owner</span> Administrators

    <span class="c">/* removed content here to save space */</span>
  }
  <span class="k">Aggregate</span> Handling {
    <span class="k">owner</span> CargoTracker

    <span class="c">/* removed content here to save space */</span> 
  }
  <span class="k">Aggregate</span> Voyage {
    <span class="k">owner</span> VoyageManager

    <span class="c">/* removed content here to save space */</span>
  }
}

<span class="c">/* team definitions: */</span>
<span class="k">BoundedContext</span> CargoPlaner { <span class="k">type</span> <span class="k">TEAM</span> }
<span class="k">BoundedContext</span> CargoTracker { <span class="k">type</span> <span class="k">TEAM</span> }
<span class="k">BoundedContext</span> VoyageManager { <span class="k">type</span> <span class="k">TEAM</span> }
<span class="k">BoundedContext</span> Administrators { <span class="k">type</span> <span class="k">TEAM</span> }
</pre></div>

The CML team assignments will be mapped to the Service Cutter's [_Shared Owner Group_ definition](https://github.com/ServiceCutter/ServiceCutter/wiki/Shared-owner-groups).

## Other User Representations
In our example we just used _Use Cases_ and _Shared Owner Groups_. However, Service Cutter supports many other [user representations](https://github.com/ServiceCutter/ServiceCutter/wiki/User-Representations) that can help to improve the suggested service decompositions:

 * Entity Relationship Model (ERM)
 * Use Cases
 * Shared Owner Groups
 * Aggregates
 * Entities
 * Predefined Services
 * Separated Security Zones
 * Security Access Groups
 * Compatibilities

**Note:** CML offers language features to cover all those user representations. That means: Context Mapper derives all Service Cutter user representations automatically for you, as long as you use the corresponding CML language feature. The following list summarizes how you can use all those language features (and links to the corresponding pages of the language reference):

 * [Use Cases](https://github.com/ServiceCutter/ServiceCutter/wiki/Use-Cases): The use cases for Service Cutter are derived from the CML use cases and/or user stories (already shown above). You can find examples how to model them [here](/docs/user-requirements/). Also have a look at [Olaf Zimmermann's blogpost](https://ozimmer.ch/practices/2020/06/10/ICWEKeynoteAndDemo.html) for an enhanced example.
   * **Note**: You have to specify your use cases with entities and their attributes, otherwise we cannot use them as user representations in Service Cutter.
 * [Shared Owner Groups](https://github.com/ServiceCutter/ServiceCutter/wiki/Shared-owner-groups): Shared owner groups are derived automatically, if you [assign owners to your Aggregates (define which development teams own which parts of the system/code)](/docs/aggregate/#aggregate-owner) as done above.
 * [Aggregates](https://github.com/ServiceCutter/ServiceCutter/wiki/Aggregates): [Aggregates](/docs/aggregate/) are first-class citizens in CML. Thus, the Aggregates for Service Cutter are simply derived by the CML Aggregates.
 * [Entities](https://github.com/ServiceCutter/ServiceCutter/wiki/Entities): [Entities](/docs/tactic-ddd/) are first-class citizens in CML. Thus, the Entities for Service Cutter are simply derived by the CML Entities, Value Objects, and Domain Events (see [tactic DDD](/docs/tactic-ddd/)).
 * [Predefined Services](https://github.com/ServiceCutter/ServiceCutter/wiki/Predefined-services): Predefined services are derived by the [Bounded Contexts](/docs/bounded-context/) you already provide before calling the service cut generator. This means: each Bounded Context you already identified is mapped to a predefined service.
 * [Separated Security Zones](https://github.com/ServiceCutter/ServiceCutter/wiki/Separated-security-zones): The CML language allows you to [assign each Aggregate to a _security zone_](/docs/aggregate/#security-zones). Thereby you can indicate that parts of your Bounded Contexts must be realized in _separated security zones_.
 * [Security Access Groups](https://github.com/ServiceCutter/ServiceCutter/wiki/Security-access-groups): The CML language allows you to [assign each Aggregate to a _security access group_](/docs/aggregate/#security-access-groups). Thereby you can indicate that parts of your Bounded Contexts have different security access requirements.
 * [Compatibilities](https://github.com/ServiceCutter/ServiceCutter/wiki/Compatibilities): All compatibilities (`contentVolatility`, `structuralVolatility`, `availabilityCriticality`, `consistencyCriticality`, `storageSimilarity`, and `securityCriticality`) can be [modeled on Aggregate level in CML](/docs/aggregate/#characteristics-classification).

## The Service Cutter Configuration DSL (SCL)

<div class="alert alert-custom">
<strong>Note:</strong> As soon as you generate service cut suggestions you will realize that Context Mapper creates a *.scl file besides your *.cml file. Since Context Mapper v6.x.x you can basically ignore this file. It contains the user representations and updates itself each time you create a new service decomposition suggestion.
</div>

We originally developed the _Service Cutter Configuration DSL (SCL)_ to ease the modeling of Service Cutter's user representations, since Service Cutter requires the data in JSON and this is cumbersome to write manually. To generate service decomposition suggestions in Context Mapper it is no longer required to modify it manually. It creates and updates itself automatically.

You only have to open and/or edit the file in one case: if you want to export the JSON files and analyze your system in the original Service Cutter tool. In case you generate service cut's in Context Mapper, it does not make sense to modify the file manually, as it is always overwritten with the data we derive from the CML model.

Now, having a CML and a SCL model, you have two options how you can proceed:

 * Generate new service cut's in Context Mapper
 * Analyze your model in [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/)

## Generate Service Cut's
You can create new CML files with new service decompositions by calling "Propose New Service Cut":

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-generate-new-service-cut.png">![Propose New Service Cut (Context Menu in VS Code)](/img/systematic-service-decomposition-tutorial-generate-new-service-cut.png)</a>

Note that depending on the [graph clustering algorithm](#algorithms) (we explain how you can change the algorithm below) you may get a different result each time you call the generator.
In this case, you can generate multiple suggestions by calling the generator multiple times; it always create a new *.cml file containing a new service decomposition for your model:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-multiple-generation-screenshot.png">![Generate Multiple Service Cuts](/img/systematic-service-decomposition-tutorial-multiple-generation-screenshot.png)</a>

As you can see above, the generator additionally creates a *.gv file each time:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-example-graphviz-file.png">![Example Graphviz DOT File (*.gv)](/img/systematic-service-decomposition-tutorial-example-graphviz-file.png)</a>

You don't necessarily need this file, but it can be useful for traceability and while trying to understand how Service Cutter works. It contains the graph Service Cutter uses for the clustering as [Graphviz DOT file](https://en.wikipedia.org/wiki/DOT_%28graph_description_language%29). Thereby you can for example change the scoring in the `.servicecutter.yml` file and analyze which impact this has on the actual graph behind the scenes. Besides the graph with the weighted egdes, each line/edge contains a comment that explains the calculated weight on the basis of the used coupling criteria.

If your model is not too big you can use online tools such as [http://webgraphviz.com/](http://webgraphviz.com/) or [http://graphviz.it/](http://graphviz.it/) to illustrate the graph graphically:

<a target="_blank" href="/img/service-cutter-gv-file-online-screenshot.png">![Example Graphviz DOT File (*.gv)](/img/service-cutter-gv-file-online-screenshot.png)</a>

However, the graph generated with our example above is already too big for those tools (they do not respond when pasting the DOT graph into their editors). In such a case you can generate a graphic locally on the command line (in case you have [Graphviz](https://graphviz.org/) installed):

```bash
dot -Tpng DDD-Sample_Markov_Clustering_Cut_4.gv -o DDD-Sample_Markov_Clustering_Cut_4.png
```

This can also take a while but you have the generated file after a some seconds.

Nevertheless, as you can see in the following image, this feature is really only usefull for small examples. The graph produced by our DDD sample model is simply too big:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-generated-png-graph.png">![Huge Graphviz graph for DDD Sample)](/img/systematic-service-decomposition-tutorial-generated-png-graph.png)</a>

### Criteria Scoring
Service Cutter allows you to score the individual coupling criteria. Thereby you can define which criteria are more important than others in your specific case. In case you use Service Cutter, you can control the scores on the user interface (see screenshot below). In case you use the service cut generator in Context Mapper, you have to change the scores in the `.servicecutter.yml` file. The file is automatically generated into the root folder of your project when you call the service cut generator for the first time:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-servicecutter-config-file.png">![Generate Multiple Service Cuts](/img/systematic-service-decomposition-tutorial-servicecutter-config-file.png)</a>

You can change the scoring in the _priorities_ part of the YAML file (see screenshot above). The following values are allowed: _IGNORE_, _XS_, _S_, _M_, _L_, _XL_, and _XXL_.

**Note:** In case you work with Eclipse you have to ensure that the _.* resources_ filter is disabled in the project/file explorer (so that you can see the .servicecutter.yml file):

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-eclipse-dot-file-filter.png">![Eclipse: Disable .* File Filter](/img/systematic-service-decomposition-tutorial-eclipse-dot-file-filter.png)</a>

**Note:** As you can see in the following screenshot, we always dump the current configuration as a comment into the generate service suggestions:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-configuration-dump.png">![Configuration dumped into generated CML models](/img/systematic-service-decomposition-tutorial-configuration-dump.png)</a>

This can be very helpful regarding traceability and understandability when analyzing the generated service cut's.

### Algorithms
You can further change the clustering algorithm in the `.servicecutter.yml` file. We currently support the following three algorithms:

 * [Markov Clustering (MCL)](https://www.micans.org/mcl/): `MARKOV_CLUSTERING` (default)
 * [Epidemic Label Propagation (Leung)](https://arxiv.org/abs/0808.2633): `LEUNG` (non-deterministic)
 * [Chinese Whispers](https://dl.acm.org/doi/10.5555/1654758.1654774): `CHINESE_WHISPERS` (randomized, and therefore non-deterministic)

<div class="alert alert-custom">
<strong>Note</strong> that that LEUNG and CHINESE_WHISPERS can produce different results for each execution due to their randomized and non-deterministic behavior. That means that you get CML models each time you generate a new service cut suggestion.
</div>

More information on the `.servicecutter.yml` configuration file can be found [here](/docs/service-cutter-config-file/).

## Extract a Suggested Service in the Original Model
The generated *.cml files with the service cut suggestions typically do not contain all the information you modeled into your original CML model. These files are not meant to continue to work with. We just use them as a suggestion on how a system could be decomposed and then (maybe) refactor the original model accordingly. 

In case a suggested cut contains a service which you find a suitable Bounded Context, you can extract such a service in the original model with a refactoring we provide.

With our example above we generated a cut that contained the following service (_Service\_C_):

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-extract-service-1.png">![An example service that could be extracted (Screenshot)](/img/systematic-service-decomposition-tutorial-extract-service-1.png)</a>

The service contains everything related to the _Location_ entity. Providing all the locations and their management as a separate service (Bounded Context) could be a reasonable design decision. 

Given such a service in a generated cutting suggestions, you can now apply the _Extract Suggested Service in Original Model_ refactoring:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-extract-service-2.png">![Extract Suggested Service in Original Model](/img/systematic-service-decomposition-tutorial-extract-service-2.png)</a>

As you may remember, our original model (at the beginning of this tutorial) only contained one single Bounded Context. This refactoring supports you in extracting the suggested service above from this exising (monolithic) context.

**Note:** For this refactoring to work properly, you are not allowed to rename the CML files. The refactoring has to locate the original model, which can only be done if they are still named according our given pattern.

The refactoring will ask you to provide a name for the selected Bounded Context first. We chose the name _LocationContext_ for the suggested service. Context Mapper will open the original model with the applied change: (in VS Code in a split view and the changes can be saved or reverted; in Eclipse in a normal editor and the changes are already persisted)

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-extracted-service-in-original-model.png">![The Extracted Service in the Original Model](/img/systematic-service-decomposition-tutorial-extracted-service-in-original-model.png)</a>

As you can see in the original model in the right view above, a new _LocationContext_ got extracted. However, the refactoring implementation is quite straight forward and typically requires you to do some manual cleanup work. For example: it currently does not delete the original entities (in this case _Location_ and _UnLocode_) since they could still contain some nanoentities (potentially). Therefore we generate unique names (in this case _Location\_2_ and _UnLocode\_2_), which might not be the desired names. If the original entities are no longer needed, you can delete those and rename the entities of your new Bounded Context with the rename refactoring in VS Code or Eclipse.

Thats it. This is how the current tooling in Context Mapper supports you in proposing service cut's and extract potential services in your original CML model. In the following we have a look at how you can use your CML model to generate the input files required by the Service Cutter tool.

## Analyze Model in Service Cutter
Instead of generating new service cuts in Context Mapper, it is also possible to analyze the decompositions in Service Cutter. While Context Mapper generates new CML models, Service Cutter illustrates the graph clusterings graphically.

To use Service Cutter you need the ERM and user representations as JSON files. Both can now easily be generated with Context Mapper.
The ERM is generated out of the CML file...

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-generate-erm-json.png">![Generate ERM JSON File](/img/systematic-service-decomposition-tutorial-generate-erm-json.png)</a>

... and the user representations out of the SCL file:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-generate-ur-json.png">![Generate User Representations JSON File](/img/systematic-service-decomposition-tutorial-generate-ur-json.png)</a>

**Note**: In case you haven't generated service cut's before, you don't have a SCL file already. No worries: you can simply generate it from your CML file by calling _Generate Service Cutter User Representations (SCL)_ in the context menu of the CML editor. Don't confuse this with the _Generate SCL Example File (Syntax Sample)_ entry, which only generates an exemplary SCL file (this can be used in case you want write your SCL file manually).

Now you can start Service Cutter and import the model to analyze it. You can start Service Cutter easily by cloning the repository and using Docker:

```bash
git clone git@github.com:ServiceCutter/ServiceCutter.git
cd ServiceCutter
docker-compose up
```

Once the application is up-and-running you can open it in your browser under http://localhost:8080 (user: admin, password: admin). 
Under the _System Specification_ tab you can upload the ERD file first, and then add the user representations:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-service-cutter-upload-files.png">![Import ERD and User Representations (JSON files) in Service Cutter](/img/systematic-service-decomposition-tutorial-service-cutter-upload-files.png)</a>

After you have imported the two files you can switch to the _Service Cuts_ tab and analyze different decompositions depending on the criteria scoring:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-service-cuts-in-service-cutter.png">![Analyze Service Cuts in Service Cutter](/img/systematic-service-decomposition-tutorial-service-cuts-in-service-cutter.png)</a>

## Summary
In this tutorial we have shown how you can use Service Cutter to generate decomposition suggestions for your system modeled in CML. It is important to note that we only understand them as suggestions. They can help to analyze the coupling between objects in your domain model and therefore may help you in finding the right service decomposition and Bounded Contexts. Don't expect that the produced result is the best decomposition without questioning them seriously!

For our DDD sample application we used the generated outputs to discover some parts of the domain model which seem to be loosely coupled from the rest. Concretely, we extracted a Bounded Context for the _Location_ Aggregate and one for the _Voyage_ Aggregate. You can find this CML model [here](https://github.com/ContextMapper/context-mapper-examples/blob/master/src/main/cml/ddd-sample/DDD-Sample-Stage-5.cml).

To extract new Bounded Contexts according to the ideas you have developed by using Service Cutter you may also use our [Architectural Refactorings](/docs/architectural-refactorings/). For example, you can extract Aggregates by using [AR-5: Extract Aggregates by Cohesion](/docs/ar-extract-aggregates-by-cohesion/).

In order to present and discuss decomposition suggestions with your colleagues, you can use our [generators](/docs/generators/) to create graphical representations ([graphical Context Map](/docs/context-map-generator/) or [PlantUML diagrams](/docs/plant-uml/)) of the service decompositions.
