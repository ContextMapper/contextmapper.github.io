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
With a Bounded Context definition as the one above you are already able to generate new service decompositions or Service Cutter files. However, we highly recommend the model your use cases as well, since they have a big impact on the ideal service decomposition.

On the [User Requirements](/docs/user-requirements/) page of our language reference you can find out how use cases or user stories are modeled in CML. For this tutorial based on the DDD sample application we modeled the use cases provided by the [Service Cutter sample files](https://github.com/ServiceCutter/ServiceCutter/tree/master/Samples):

<div class="highlight"><pre><span></span><span class="k">UseCase</span> ViewTracking {
  <span class="k">reads</span> <span class="s">&quot;Cargo.trackingId&quot;</span>, <span class="s">&quot;HandlingEvent.type&quot;</span>, <span class="s">&quot;HandlingEvent.location&quot;</span>, <span class="s">&quot;HandlingEvent.completionTime&quot;</span>, <span class="s">&quot;Delivery.transportStatus&quot;</span>, <span class="s">&quot;Delivery.estimatedArrivalTime&quot;</span>, <span class="s">&quot;Delivery.misdirected&quot;</span>, <span class="s">&quot;Voyage.voyageNumber&quot;</span>, <span class="s">&quot;RouteSpecification.destination&quot;</span>
}

<span class="k">UseCase</span> ViewCargos {
  <span class="k">reads</span> <span class="s">&quot;Cargo.trackingId&quot;</span>, <span class="s">&quot;RouteSpecification.destination&quot;</span>, <span class="s">&quot;RouteSpecification.arrivalDeadline&quot;</span>, <span class="s">&quot;Delivery.routingStatus&quot;</span>, <span class="s">&quot;Itinerary.itineraryNumber&quot;</span>
}

<span class="k">UseCase</span> BookCargo {
  <span class="k">reads</span> <span class="s">&quot;Location.unLocode&quot;</span>
  <span class="k">writes</span> <span class="s">&quot;Cargo.trackingId&quot;</span>, <span class="s">&quot;RouteSpecification.origin&quot;</span>, <span class="s">&quot;RouteSpecification.arrivalDeadline&quot;</span>, <span class="s">&quot;RouteSpecification.destination&quot;</span>
}

<span class="k">UseCase</span> ChangeCargoDestination {
  <span class="k">reads</span> <span class="s">&quot;Cargo.trackingId&quot;</span>, <span class="s">&quot;RouteSpecification.destination&quot;</span>
  <span class="k">writes</span> <span class="s">&quot;RouteSpecification.destination&quot;</span>
}

<span class="c">/* we shortened this listing to save space (find all use cases in the original CML file) */</span>
</pre></div>

Note that we only modeled the _read_ and _written_ nanoentities here. You can model the user requirements in much more detail in CML, but these two attributes are necessary for the Service Cutter generators and tools.

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

## Additional User Representations
Besides _Use Cases_ and _Shared Owner Groups_ Service Cutter uses additional user representations that may influence the coupling between your model elements. This is the list of [all supported user representations](https://github.com/ServiceCutter/ServiceCutter/wiki/User-Representations):

 * Entity Relationship Model (ERM)
 * Use Cases
 * Shared Owner Groups
 * Aggregates
 * Entities
 * Predefined Services
 * Separated Security Zones
 * Security Access Groups
 * Compatibilities

Most of the user representations we can now derive from our CML model. The ERM is derived from the Entities and their references in CML. As already explained above, the Use Cases and Shared Owner Groups are modeled in CML as well. We further derive the Aggregates and Entities for Service Cutter from the corresponding counterparts in CML. In addition, we derive Predefined Services from already existing Bounded Contexts of your CML model. The remaining user representations have to be added manually, in case they are relevant for your application.

## The Service Cutter Configuration DSL (SCL)
The Service Cutter tool takes the user representations as a JSON file. In order to ease the description of these representations we created another DSL. Once you created a CML model, you can easily derive an initial SCL file from it. You find two SCL generators in Context Mapper:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-scl-menu-screenshot.png">![SCL Generators in Context Mapper](/img/systematic-service-decomposition-tutorial-scl-menu-screenshot.png)</a>

The first generator ("Generate Service Cutter User Representations (SCL)") generates an SCL file that contains the user representations which can be derived from your CML model. You can enhance this file with additional user representations. However, the representations that can be derived from CML code will always be overwritten as soon as you call the generator again or if you generate new Service Cut's in Context Mapper. 

**Note:** If you update your CML model (for example you create a new Aggregate with new Entities), you can always call the SCL generator again and it will update your *.scl file.

The second generator ("Generate Service Cutter User Representation Example File (SCL)") only generates an exemplary file that illustrates the SCL syntax. The generated user representations do not make sense and should not be used to generate Service Cut's! In this file you find syntactic examples for all potential user representations you can model:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-scl-example-file.png">![SCL Example File](/img/systematic-service-decomposition-tutorial-scl-example-file.png)</a>

Now, having a CML and a SCL model, you have two options how you can proceed:

 * Generate new service cut's in Context Mapper
 * Analyze your model in [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/)

## Generate Service Cut's
You can create new CML files with new service decompositions by calling "Generate New Service Cut":

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-generate-new-service-cut.png">![Generate New Service Cut (Context Menu in VS Code)](/img/systematic-service-decomposition-tutorial-generate-new-service-cut.png)</a>

Note that depending on the [graph clustering algorithm](#algorithms) (we explain how you can change the algorithm below) you may get a different result each time you call the generator.
In this case, you can generete multiple suggestions by calling the generator multiple times; it always create a new *.cml file containing a new service decomposition for your model:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-multiple-generation-screenshot.png">![Generate Multiple Service Cuts](/img/systematic-service-decomposition-tutorial-multiple-generation-screenshot.png)</a>

**Note:** The generator always uses the *.scl file with the same name your *.cml file has. For example: if you call the generator for a file called _mymodel.cml_, your SCL file must be called _mymodel.scl_ and it must be stored in the same directory. The SCL file generator already creates the file under the correct file name.

**Note:** If you have not already created an SCL file as described above, the service cut generator will automatically create one for you.

### Criteria Scoring
Service Cutter allows you to score the individual coupling criteria. Thereby you can define which criteria are more important than others in your specific case. In case you use Service Cutter, you can control the scores on the user interface (see screenshot below). In case you use the service cut generator in Context Mapper, you have to change the scores in the `.servicecutter.yml` file. The file is automatically generated into the root folder of your project when you call the service cut generator for the first time:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-servicecutter-config-file.png">![Generate Multiple Service Cuts](/img/systematic-service-decomposition-tutorial-servicecutter-config-file.png)</a>

You can change the scoring in the _priorities_ part of the YAML file (see screenshot above). The following values are allowed: _IGNORE_, _XS_, _S_, _M_, _L_, _XL_, and _XXL_.

**Note:** In case you work with Eclipse you have to ensure that the _.* resources_ filter is disabled in the project/file explorer (so that you can see the .servicecutter.yml file):

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-eclipse-dot-file-filter.png">![Eclipse: Disable .* File Filter](/img/systematic-service-decomposition-tutorial-eclipse-dot-file-filter.png)</a>

### Algorithms
You can further change the clustering algorithm in the `.servicecutter.yml` file. We currently support the following three algorithms:

 * [Markov Clustering (MCL)](https://www.micans.org/mcl/): `MARKOV_CLUSTERING` (default)
 * [Epidemic Label Propagation (Leung)](https://arxiv.org/abs/0808.2633): `LEUNG` (non-deterministic)
 * [Chinese Whispers](https://dl.acm.org/doi/10.5555/1654758.1654774): `CHINESE_WHISPERS` (randomized)

<div class="alert alert-custom">
<strong>Note</strong> that that LEUNG and CHINESE_WHISPERS produce randomized and non-deterministic results. That means that you get different results each time you generate a new service cut.
</div>

## Analyze Model in Service Cutter
Instead of generating new service cuts in Context Mapper, it is also possible to analyze the decompositions in Service Cutter. While Context Mapper generates new CML models, Service Cutter illustrates the graph clusterings graphically.

To use Service Cutter you need the ERM and user representations as JSON files. Both can now easily be generated with Context Mapper.
The ERM is generated out of the CML file...

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-generate-erm-json.png">![Generate ERM JSON File](/img/systematic-service-decomposition-tutorial-generate-erm-json.png)</a>

... and the user representations out of the SCL file:

<a target="_blank" href="/img/systematic-service-decomposition-tutorial-generate-ur-json.png">![Generate User Representations JSON File](/img/systematic-service-decomposition-tutorial-generate-ur-json.png)</a>

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

To extract new Bounded Contexts according to the ideas you have developed by using Service Cutter you may use our [Architectural Refactorings](/docs/architectural-refactorings/). For example, you can extract Aggregates by using [AR-5: Extract Aggregates by Cohesion](/docs/ar-extract-aggregates-by-cohesion/).

In order to present and discuss decomposition suggestions with your colleagues, you can use our [generators](/docs/generators/) to create graphical representations ([graphical Context Map](/docs/context-map-generator/) or [PlantUML diagrams](/docs/plant-uml/)) of the service decompositions.
