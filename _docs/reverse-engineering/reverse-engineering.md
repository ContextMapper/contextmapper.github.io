---
title: Context Map Discovery
permalink: /docs/reverse-engineering/
---

Our "context map discovery" or "reverse engineering" library allows you to derive a CML context map from existing source code. If you work in a project involving an existing monolith, you may want to generate a Bounded Context that represents and contains your domain model. Afterwards, you can analyze and decompose the architecture with our tools. This helps you to get started with our tool and avoids huge efforts to re-model the existing system. If your system already has a (micro-)service-oriented architecture, you may want to reverse engineer the CML context map illustrating all bounded contexts and their relationships.

The discovery library supports the reverse engineering of bounded contexts and context maps (including relationships between bounded contexts). It is extensible and designed to plug-in new discovery [strategies](https://en.wikipedia.org/wiki/Strategy_pattern). The current prototype supports bounded context discovery for [Spring Boot ](https://spring.io/projects/spring-boot) applications and relationship discovery on the basis of Docker compose.

Contributions to the discovery library are very welcome! If you implement a new discovery strategy for another programming language or framework, please contribute it to our project and create a Pull Request (PR) in our [GitHub repository](https://github.com/ContextMapper/context-map-discovery).

## Usage
The latest version of the discovery library is available through Maven Central: [![Maven Central](https://img.shields.io/maven-central/v/org.contextmapper/context-map-discovery.svg?label=Maven%20Central)](https://search.maven.org/search?q=g:%22org.contextmapper%22%20AND%20a:%22context-map-discovery%22)

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

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> {
  <span class="k">contains</span> PolicyManagement
  <span class="k">contains</span> CustomerManagement
  <span class="k">contains</span> CustomerSelfService
  <span class="k">contains</span> CustomerCore

  CustomerCore -&gt; PolicyManagement

  CustomerCore -&gt; CustomerManagement

  PolicyManagement -&gt; CustomerSelfService

  CustomerCore -&gt; CustomerSelfService

}

<span class="k">BoundedContext</span> PolicyManagement {
  <span class="k">implementationTechnology</span> <span class="s">&quot;Spring Boot&quot;</span>
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.policymanagement.interfaces.RiskComputationService.</span>
  <span class="k">Aggregate</span> riskfactor
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.policymanagement.interfaces.InsuranceQuoteRequestInformationHolder.</span>
  <span class="k">Aggregate</span> PolicyManagement_insurance_quote_requests {
    <span class="c">/* removed to save space here */</span>
  }
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.policymanagement.interfaces.PolicyInformationHolder.</span>
  <span class="k">Aggregate</span> policies {
    <span class="c">/* removed to save space here */</span>
  }
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.policymanagement.interfaces.CustomerInformationHolder.</span>
  <span class="k">Aggregate</span> PolicyManagement_customers {
    <span class="c">/* removed to save space here */</span>
  }
}

<span class="k">BoundedContext</span> CustomerManagement {
  <span class="k">implementationTechnology</span> <span class="s">&quot;Spring Boot&quot;</span>
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customermanagement.interfaces.CustomerInformationHolder.</span>
  <span class="k">Aggregate</span> CustomerManagement_customers {
    <span class="c">/* removed to save space here */</span>
  }
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customermanagement.interfaces.InteractionLogInformationHolder.</span>
  <span class="k">Aggregate</span> interaction_logs {
    <span class="c">/* removed to save space here */</span>
  }
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customermanagement.interfaces.NotificationInformationHolder.</span>
  <span class="k">Aggregate</span> notifications
}

<span class="k">BoundedContext</span> CustomerSelfService {
  <span class="k">implementationTechnology</span> <span class="s">&quot;Spring Boot&quot;</span>
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.AuthenticationController.</span>
  <span class="k">Aggregate</span> auth
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.CityStaticDataHolder.</span>
  <span class="k">Aggregate</span> cities {
    <span class="c">/* removed to save space here */</span>
  }
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.InsuranceQuoteRequestInformationHolder.</span>
  <span class="k">Aggregate</span> insurance_quote_requests {
    <span class="c">/* removed to save space here */</span>
  }
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.CustomerInformationHolder.</span>
  <span class="k">Aggregate</span> customers {
    <span class="c">/* removed to save space here */</span>
  }
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customerselfservice.interfaces.UserInformationHolder.</span>
  <span class="k">Aggregate</span> user {
    <span class="c">/* removed to save space here */</span>
  }
}

<span class="k">BoundedContext</span> CustomerCore {
  <span class="k">implementationTechnology</span> <span class="s">&quot;Spring Boot&quot;</span>
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customercore.interfaces.CityStaticDataHolder.</span>
  <span class="k">Aggregate</span> CustomerCore_cities {
    <span class="c">/* removed to save space here */</span>
  }
  <span class="c">// This Aggregate has been created on the basis of the Spring REST controller com.lakesidemutual.customercore.interfaces.CustomerInformationHolder.</span>
  <span class="k">Aggregate</span> CustomerCore_customers {
    <span class="c">/* removed to save space here */</span>
  }
}
</pre></div>

Note that we removed the entities in the CML model above in order to save space here. The full example and the project source code can be found 
[here](https://github.com/ContextMapper/context-map-discovery/tree/master/Examples/LakesideMutual).
