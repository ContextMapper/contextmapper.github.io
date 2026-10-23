---
title: Context Map Generator
permalink: /docs/context-map-generator/
image: /img/context-mapper-example-context-map.png
---

## Introduction
Our Context Map generator produces graphical representations of Context Mapper DSL (CML) Context Maps. The visualization of the
generated Context Maps is inspired by the illustration style proposed by [Vernon](https://www.amazon.de/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577)
and [Brandolini](https://www.infoq.com/articles/ddd-contextmapping/).

## Examples
The following CML Context Map represents the DDD cargo sample application (find the complete CML file [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/ddd-sample)): 

```cml
ContextMap DDDSampleMap {
  contains CargoBookingContext
  contains VoyagePlanningContext
  contains LocationContext

  CargoBookingContext [SK]<->[SK] VoyagePlanningContext

  CargoBookingContext [D]<-[U,OHS,PL] LocationContext

  VoyagePlanningContext [D]<-[U,OHS,PL] LocationContext
}
```

Using our generator produces the following graphical Context Map for you:

<a href="/img/context-map-generator-ddd-sample.png">![DDD Cargo Sample Application Context Map](/img/context-map-generator-ddd-sample.png)</a>

As a second example, the following Context Map represents our [insurance company example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example)
(find the complete CML file [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example)):

```cml
ContextMap InsuranceContextMap {
  type = SYSTEM_LANDSCAPE
  state = TO_BE

  /* Add bounded contexts to this context map: */
  contains CustomerManagementContext, CustomerSelfServiceContext, PrintingContext
  contains PolicyManagementContext, RiskManagementContext, DebtCollection

  /* Define the context relationships: */

  CustomerSelfServiceContext [D,C]<-[U,S] CustomerManagementContext {
    exposedAggregates = Customers
  }

  CustomerManagementContext [D,ACL]<-[U,OHS,PL] PrintingContext {
    implementationTechnology = "SOAP"
    downstreamRights = INFLUENCER
    exposedAggregates = Printing
  }

  PrintingContext [U,OHS,PL]->[D,ACL] PolicyManagementContext {
    implementationTechnology = "SOAP"
    exposedAggregates = Printing
  }

  RiskManagementContext [P]<->[P] PolicyManagementContext {
    implementationTechnology = "RabbitMQ"
  }

  PolicyManagementContext [D,CF]<-[U,OHS,PL] CustomerManagementContext {
    implementationTechnology = "RESTfulHTTP"
    exposedAggregates = Customers
  }

  DebtCollection [D,ACL]<-[U,OHS,PL] PrintingContext {
    implementationTechnology = "SOAP"
    exposedAggregates = Printing
  }

  PolicyManagementContext [SK]<->[SK] DebtCollection {
    implementationTechnology = "Shared Java Library, Communication over RESTful HTTP"
  }
}
```

Our generator produces the following graphical result for the above Context Map:

<a href="/img/context-map-generator-insurance-sample.png">![Insurance Company Example Context Map](/img/context-map-generator-insurance-sample.png)</a>

Besides Context Maps of the type _SYSTEM\_LANDSCAPE_, CML allows you to create maps that illustrate which development teams work on which subsystems or components (Context Map type _ORGANZATIONAL_). The following CML example illustrates how this can be done:

```cml
ContextMap InsuranceTeamMap {
  type = ORGANIZATIONAL
  state = TO_BE

  /* Add contexts that represent subsystems/components to this organizational map: */
  contains CustomerManagementContext, CustomerSelfServiceContext, PolicyManagementContext, RiskManagementContext

  /* Add teams to this organizational map: */
  contains CustomersBackofficeTeam, CustomersFrontofficeTeam, ContractsTeam

  /* Define the subsystem/component relationships: */

  CustomerSelfServiceContext [D,C]<-[U,S] CustomerManagementContext

  PolicyManagementContext [D,CF]<-[U,OHS,PL] CustomerManagementContext

  PolicyManagementContext [P]<->[P] RiskManagementContext

  /* Define the team relationships: */

  CustomersBackofficeTeam [U,S]->[D,C] CustomersFrontofficeTeam

  CustomersBackofficeTeam [U]->[D] ContractsTeam

}

/* Team Definitions */
BoundedContext CustomersBackofficeTeam realizes CustomerManagementContext {
  type = TEAM
  domainVisionStatement = "This team is responsible for implementing the customers module in the back-office system."
}

BoundedContext CustomersFrontofficeTeam realizes CustomerSelfServiceContext {
  type = TEAM
  domainVisionStatement = "This team is responsible for implementing the front-office application for the insurance customers."
}

BoundedContext ContractsTeam realizes PolicyManagementContext, RiskManagementContext {
  type = TEAM
  domainVisionStatement = "This team is responsible for implementing the contract-, policy-, and risk-management modules in the back-office system."
}

/* Subsystem/component definitions */
BoundedContext CustomerManagementContext
BoundedContext CustomerSelfServiceContext
BoundedContext PolicyManagementContext
BoundedContext RiskManagementContext
```

Depending on how you configure the the generator (clustering parameter), it will generate one of the following visualizations for you. Not clustered:

<a href="/img/TeamMap-Illustration-1.png">![Team Map Example (Unclustered)](/img/TeamMap-Illustration-1.png)</a>

... or clustered:

<a href="/img/TeamMap-Illustration-2.png">![Team Map Example (Clustered)](/img/TeamMap-Illustration-2.png)</a>

## Generating Context Maps
The generators can be called from the context menus of the CML editors in VS Code or Eclipse. A documentation how to call the generators can also be found [here](/docs/generators/#using-the-generators).

**Note:** All generator outputs will be generated into the *src-gen* folder.

### System Requirements for this Generator
The generator requires [Graphviz](https://www.graphviz.org/) to be installed on your system because it uses it behind the scenes:

 * Ensure [Graphviz](https://www.graphviz.org/) is installed on your machine.
 * Verify that the binaries of the [Graphviz](https://www.graphviz.org/) installation are part of your PATH environment variable and can be called from the command line, for instance by executing `dot -V` from the command line. 
    * In Windows this is not the case after the installation of [Graphviz](https://www.graphviz.org/). The default installation path is
      `C:\Program Files (x86)\GraphvizX.XX`, which means you have to add `C:\Program Files (x86)\GraphvizX.XX\bin` to your PATH variable.
