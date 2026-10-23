---
title: Context Map Discovery
permalink: /docs/reverse-engineering/
---

Our "context map discovery" or "reverse engineering" library allows you to derive a CML context map from existing source code. If you work in a project involving an existing monolith, you may want to generate a Bounded Context that represents and contains your domain model. Afterwards, you can analyze and decompose the architecture with our tools. This helps you to get started with our tool and avoids huge efforts to re-model the existing system. If your system already has a (micro-)service-oriented architecture, you may want to reverse engineer the CML context map illustrating all bounded contexts and their relationships.

The discovery library supports the reverse engineering of bounded contexts and context maps (including relationships between bounded contexts). It is extensible and designed to plug-in new discovery [strategies](https://en.wikipedia.org/wiki/Strategy_pattern). The current prototype supports bounded context discovery for [Spring Boot ](https://spring.io/projects/spring-boot) applications and relationship discovery on the basis of Docker compose.

Contributions to the discovery library are very welcome! If you implement a new discovery strategy for another programming language or framework, please contribute it to our project and create a Pull Request (PR) in our [GitHub repository](https://github.com/ContextMapper/context-map-discovery).

## Usage
The latest version of the discovery library is available through Maven Central: [org.contextmapper:context-map-discovery on Maven Central](https://central.sonatype.com/artifact/org.contextmapper/context-map-discovery)

You can find all information about the library, how to use it, and how to extend it with new discovery strategies in our Github repository:

[https://github.com/ContextMapper/context-map-discovery](https://github.com/ContextMapper/context-map-discovery)

Note that this is a prototype and limited in the discovery strategies already implemented. Additional strategies will have to be implemented in the future.
  
## Lakeside Mutual Case Study
The following example illustrates how the discovery library works. We applied it to the [Lakeside Mutual](https://github.com/Microservice-API-Patterns/LakesideMutual) project, a fictitious insurance company. It is a sample application to demonstrate microservices. With our [context map discovery library](https://github.com/ContextMapper/context-map-discovery) we derived a CML context map from the [Lakeside Mutual source code](https://github.com/Microservice-API-Patterns/LakesideMutual).

The following diagram, courtesy of the Lakeside Mutual project itself, illustrates the architecture:

![Lakeside Mutual Architecture Overview](/img/lakeside-mutual-overview.png)

With the [strategies already available](https://github.com/ContextMapper/context-map-discovery) we are able to discover the bounded contexts:

 * Customer Management
 * Customer Self-Service
 * Policy Management
 * Customer Core

The _risk management context_ is currently not detected, since a strategy on the basis of Node.js is not available yet.

The following piece of code is all that is needed to generate the context map with our discovery library:

```java
public class LakesideMutualContextMapDiscoverer {

  public static void main(String[] args) throws IOException {
    // configure the discoverer
    ContextMapDiscoverer discoverer = new ContextMapDiscoverer()
        .usingBoundedContextDiscoveryStrategies(
            new SpringBootBoundedContextDiscoveryStrategy("com.lakesidemutual"))
        .usingRelationshipDiscoveryStrategies(
            new DockerComposeRelationshipDiscoveryStrategy(
                new File(System.getProperty("user.home") + "/source/LakesideMutual/")))
        .usingBoundedContextNameMappingStrategies(
            new SeparatorToCamelCaseBoundedContextNameMappingStrategy("-") {
              @Override
              public String mapBoundedContextName(String s) {
                // remove the "Backend" part of the Docker service names to map correctly...
                String name = super.mapBoundedContextName(s);
                return name.endsWith("Backend") ? name.substring(0, name.length() - 7) : name;
              }
            });

    // run the discovery process to get the Context Map
    ContextMap contextmap = discoverer.discoverContextMap();

    // serialize the Context Map to CML
    new ContextMapSerializer().serializeContextMap(contextmap, new File("./src-gen/lakesidemutual.cml"));
  }

}
```

The library is based on strategies implementing the three interfaces `BoundedContextDiscoveryStrategy`, `RelationshipDiscoveryStrategy`, and `BoundedContextNameMappingStrategy`. The `BoundedContextNameMappingStrategy` strategy can be used to map different bounded context names between the bounded context and relationship strategies.

In this example we use the `SpringBootBoundedContextDiscoveryStrategy` to discover the bounded contexts via Spring annotations. It
derives [Bounded Contexts](/docs/language-reference/bounded_context) from applications, [Aggregates](/docs/language-reference/aggregate) from REST endpoints, and Entities from the REST endpoint methods. The `DockerComposeRelationshipDiscoveryStrategy` strategy is used to derive the relationships between the bounded context from the `docker-compose.yml` file. The extended `SeparatorToCamelCaseBoundedContextNameMappingStrategy` in the example above is used to map names such as 'customer-management-backend' (name according to relationship strategy) to 'CustomerManagement' (name according the discovered bounded context).

The code above creates the following context map for the application:

```cml
ContextMap {
  contains PolicyManagement
  contains CustomerManagement
  contains CustomerSelfService
  contains CustomerCore

  CustomerCore -> PolicyManagement

  CustomerCore -> CustomerManagement

  PolicyManagement -> CustomerSelfService

  CustomerCore -> CustomerSelfService

}

BoundedContext PolicyManagement {
  implementationTechnology "Spring Boot"
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.policymanagement.interfaces.RiskComputationService.
  Aggregate riskfactor
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.policymanagement.interfaces.InsuranceQuoteRequestInformationHolder.
  Aggregate PolicyManagement_insurance_quote_requests {
    /* removed to save space here */
  }
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.policymanagement.interfaces.PolicyInformationHolder.
  Aggregate policies {
    /* removed to save space here */
  }
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.policymanagement.interfaces.CustomerInformationHolder.
  Aggregate PolicyManagement_customers {
    /* removed to save space here */
  }
}

BoundedContext CustomerManagement {
  implementationTechnology "Spring Boot"
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customermanagement.interfaces.CustomerInformationHolder.
  Aggregate CustomerManagement_customers {
    /* removed to save space here */
  }
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customermanagement.interfaces.InteractionLogInformationHolder.
  Aggregate interaction_logs {
    /* removed to save space here */
  }
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customermanagement.interfaces.NotificationInformationHolder.
  Aggregate notifications
}

BoundedContext CustomerSelfService {
  implementationTechnology "Spring Boot"
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.AuthenticationController.
  Aggregate auth
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.CityStaticDataHolder.
  Aggregate cities {
    /* removed to save space here */
  }
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.InsuranceQuoteRequestInformationHolder.
  Aggregate insurance_quote_requests {
    /* removed to save space here */
  }
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.CustomerInformationHolder.
  Aggregate customers {
    /* removed to save space here */
  }
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.UserInformationHolder.
  Aggregate user {
    /* removed to save space here */
  }
}

BoundedContext CustomerCore {
  implementationTechnology "Spring Boot"
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customercore.interfaces.CityStaticDataHolder.
  Aggregate CustomerCore_cities {
    /* removed to save space here */
  }
  // This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customercore.interfaces.CustomerInformationHolder.
  Aggregate CustomerCore_customers {
    /* removed to save space here */
  }
}
```

Note that we removed the entities in the CML model above in order to save space here. The full example and the project source code can be found 
[here](https://github.com/ContextMapper/context-map-discovery/tree/master/Examples/LakesideMutual).
