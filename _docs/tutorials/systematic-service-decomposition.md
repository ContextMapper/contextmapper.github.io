---
title: Systematic Service Decomposition with Context Mapper and Service Cutter
permalink: /docs/systematic-service-decomposition/
image: /img/cm-og-image.png
---

Context Mapper provides a generator that decomposes your domain model into Bounded Contexts in a systematic manner. The service decomposition tool is based on [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/). Based on a [catalog of 16 coupling criteria](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria) and a graph clustering algorithm, the generator suggests how an application could be decomposed into Bounded Contexts, services, or components.

Note that it is not our goal to automate the job of domain modelers and software architects! The generated decompositions are just suggestions and can give you hints how your domain objects are coupled. Don't expect that the perfect decomposition is generated for you without questioning it.

<div class="alert alert-custom"><strong>Note:</strong> The Service Cutter tools in Context Mapper are now available for Visual Studio Code as well!
</div>

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

Most of the user representations we can now derive from our CML model. 

