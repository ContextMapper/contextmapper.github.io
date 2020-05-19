---
title: Generate Microservices From Context Map Using JHipster
permalink: /docs/jhipster-microservice-generation/
image: /img/cm-og-image.png
---

[JHipster](https://www.jhipster.tech/) is a development platform to generate [Spring Boot](https://spring.io/projects/spring-boot) web applications and microservices. Applications
or microservices, including their Entities and relationships between these Entities, can be specified with the [JHipster Domain Language (JDL)](https://www.jhipster.tech/jdl/).
The JHipster generator is able to generate code for the microservices (based on the Spring framework and several frontend frameworks) with a JDL file as input.

By providing a JDL template for our [generic generator (templating based on Freemarker)](/docs/generic-freemarker-generator/), we offer a tool to generate microservices from 
your [CML Context Map](/docs/context-map/) using [JHipster](https://www.jhipster.tech/). In this tutorial we show you how you can generate microservice applications from 
DDD-based models in Context Mapper.

<div class="alert alert-custom">
<strong>Note</strong> that the current solution with the Freemarker template is only temporary. We are working on an integration of the JDL language into Context Mapper.
If you have problems using the JHipster generator with the produced JDL output please let us know and 
<a target="_blank" href="https://github.com/ContextMapper/context-mapper-dsl/issues/new">create a Github issue</a>.
</div>

## The Example Model
We use our fictitious insurance example application that can be found in the [examples repository](https://github.com/ContextMapper/context-mapper-examples) to illustrate the 
microservice generation with JDL and JHipster. The following graphical Context Map shows the Bounded Contexts of the system.

<a target="_blank" href="/img/insurance-example-for-JDL-generation_ContextMap.png">![Insurance example Context Map](/img/insurance-example-for-JDL-generation_ContextMap.png)</a> 

The complete CML model used for this tutorial can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/microservice-generation/JDL-example). 
Please note that the current JDL template only filters/ignores Bounded Contexts of the type _TEAM_ when creating microservices. For all other types of Bounded Contexts
(FEATURES, APPLICATIONS, and SYSTEMS) are mapped to a corresponding microservice. Our example Context Map, shown in the following CML snippet, contains several Bounded 
Contexts of the type _SYSTEM_. The generator creates one microservice per Bounded Context. 

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> InsuranceContextMap {
  <span class="k">type</span> = <span class="k">SYSTEM_LANDSCAPE</span>
  <span class="k">state</span> = <span class="k">TO_BE</span>

  <span class="k">contains</span> CustomerManagement, CustomerSelfService, Printing
  <span class="k">contains</span> PolicyManagement, RiskManagement, DebtCollection

  CustomerSelfService [<span class="k">D</span>,<span class="k">C</span>]&lt;-[<span class="k">U</span>,<span class="k">S</span>] CustomerManagement {
    <span class="k">exposedAggregates</span> = Customers
  }

  CustomerManagement [<span class="k">D</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] Printing {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;SOAP&quot;</span>
    <span class="k">downstreamRights</span> = INFLUENCER
    <span class="k">exposedAggregates</span> = Printing
  }

  Printing [<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>]-&gt;[<span class="k">D</span>,<span class="k">ACL</span>] PolicyManagement {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;SOAP&quot;</span>
    <span class="k">exposedAggregates</span> = Printing
  }

  RiskManagement [<span class="k">P</span>]&lt;-&gt;[<span class="k">P</span>] PolicyManagement {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RabbitMQ&quot;</span>
  }

  PolicyManagement [<span class="k">D</span>,<span class="k">CF</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] CustomerManagement {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTfulHTTP&quot;</span>
    <span class="k">exposedAggregates</span> = Customers
  }

  DebtCollection [<span class="k">D</span>,<span class="k">ACL</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] Printing {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;SOAP&quot;</span>
    <span class="k">exposedAggregates</span> = Printing
  }

  PolicyManagement [<span class="k">SK</span>]&lt;-&gt;[<span class="k">SK</span>] DebtCollection {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;Shared Java Library, Communication over RESTful HTTP&quot;</span>
  }
}
</pre></div>

Each Bounded Context of the model contains Aggregates with Entities and Services. The following CML snippet (CustomerManagement) illustrates an example:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerManagement <span class="k">implements</span> CustomerManagementDomain {
  <span class="k">type</span> = <span class="k">SYSTEM</span>
  <span class="k">domainVisionStatement</span> = <span class="s">&quot;The customer management context is responsible for managing all the data of the insurance companies customers.&quot;</span>
  <span class="k">implementationTechnology</span> = <span class="s">&quot;Java, JEE Application&quot;</span>
  <span class="k">responsibilities</span> = <span class="s">&quot;Customers, Addresses&quot;</span>

  <span class="k">Aggregate</span> Customers {
    <span class="k">Entity</span> Customer {
      <span class="k">aggregateRoot</span>

      - <span class="k">SocialInsuranceNumber</span> sin
      <span class="k">String</span> firstname
      <span class="k">String</span> lastname
      - <span class="k">List</span>&lt;Address&gt; addresses

      <span class="k">def</span> AddressId createAddress(@Address address);
      <span class="k">def</span> boolean changeCustomer(String firstname, String lastname);
    }

    <span class="k">Entity</span> Address {
      <span class="k">String</span> street
      <span class="k">int</span> postalCode
      <span class="k">String</span> city
    }

    <span class="k">ValueObject</span> SocialInsuranceNumber {
      <span class="k">String</span> sin <span class="k">key</span>
    }
  }
}
</pre></div>

All other Bounded Context definitions and the complete model can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/microservice-generation/JDL-example), as already mentioned. 

_Note:_ The Bounded Contexts (not of type _TEAM_) and their Entities are the objects used for the transformation to JDL. The CML relationship definitions on the Context Map are
not used for the microservice generation, since JDL does not support specifying interface details between the services. However, JHipster will generate interfaces for the 
communication between the services.

_Note:_ References between Entities in different Bounded Contexts are currently ignored by the generator, since the JHipster generator does not support this. You have to specify
the corresponding Entities in each Bounded Context manually (for now).  

## Generate JDL with Context Mapper
Once you modeled your Bounded Contexts with the Entities, you can generate a JDL file using our [generic generator](/docs/generic-freemarker-generator/).

The Freemarker template is available within our _example template project_ which can be created through `File > New > Example...`:
 
<a target="_blank" href="/img/jhipster-tutorial-freemarker-template-1.png">![Freemarker Example Templates (Create Menu)](/img/jhipster-tutorial-freemarker-template-1.png)</a>

<a target="_blank" href="/img/jhipster-tutorial-freemarker-template-2.png">![Freemarker Example Templates (Wizard 1)](/img/jhipster-tutorial-freemarker-template-2.png)</a>

Finishing the project creation wizard will add the template project containing the `JDL.ftl` file to your workspace:

<a target="_blank" href="/img/jhipster-tutorial-freemarker-template-3.png">![Freemarker Example Templates (JDL Template)](/img/jhipster-tutorial-freemarker-template-3.png)</a>

You can then call the generator through the context menu (or Shift-Alt-G) of the CML editor:

<a target="_blank" href="/img/jhipster-tutorial-generator-context-menu.png">![Generic Generator in Context Mapper Context Menu](/img/jhipster-tutorial-generator-context-menu.png)</a>

In the generator dialog you can then select the `JDL.ftl` file as template and define the name of the JDL file that shall be created:

<a target="_blank" href="/img/jhipster-tutorial-generator-dialog.png">![Generic Generator Dialog](/img/jhipster-tutorial-generator-dialog.png)</a>

By finishing the dialog you generate the file into the `src-gen` folder:

<a target="_blank" href="/img/jhipster-tutorial-generated-file-in-src-gen.png">![Generic Generator Dialog](/img/jhipster-tutorial-generated-file-in-src-gen.png)</a>

_Note_: Install the [JHipster IDE](https://www.jhipster.tech/jhipster-ide/) in your Eclipse if you want to have editing support for the JDL file (as in the Screenshot above).

_Note_: We do not introduce the JDL language itself in this tutorial. You find the documentation of the language [here](https://www.jhipster.tech/jdl/).

## Generate the Microservices with JHipster
The JDL file generated as described above contains one microservice per Bounded Context and an [API gateway](https://www.jhipster.tech/api-gateway/). In addition, we create 
_Entities_ within the applications and _relationships_ for the references you modeled between Entities in CML.

**Prerequisites:**

For the next steps we assume you have the following tools installed on your machine:
 * Java 8+
 * [JHipster generator](https://www.jhipster.tech/installation/)

**Generation Process:**
 
First, create a folder in your sources where you want to generate the microservices from your Context Map and change to that directory:
 
```bash
$ mkdir microservice-tutorial
$ cd microservice-tutorial/
```

You can then start the JHipster generator with the JDL file as input (adjust path the generated JDL file) by using the following command:
```bash
$ jhipster import-jdl ./../context-mapper-examples/src-gen/insurance-microservices.jdl
```

After the generator has done its work we can check the content of the directory to see what has been generated:

```bash
$ ls -l
total 28
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 CustomerManagement
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 CustomerSelfService
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 DebtCollection
drwxrwxr-x 8 ska ska 4096 Apr 21 11:13 gateway
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 PolicyManagement
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 Printing
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 RiskManagement
```

As you can see in the example above, the generator created a directory for each Bounded Context / microservice. In addition, an [API gateway](https://www.jhipster.tech/api-gateway/)
is generated into the `gateway` directory.

**Running the Application**:

To run the application with all its microservices you first have to download and run the [JHipster registry](https://www.jhipster.tech/jhipster-registry/) for the service discovery.
You have two options to run the registry:

1. Clone their repository and run it as described there: [https://github.com/jhipster/jhipster-registry](https://github.com/jhipster/jhipster-registry)
2. Download the [latest release](https://github.com/jhipster/jhipster-registry/releases) (JAR file) and run the application with `java -jar jhipster-registry-<version>.jar`

You also find a complete documentation on the installation process on [JHipsters website](https://www.jhipster.tech/jhipster-registry/#installation).

In our case, we just downloaded the latest JAR file and run the application with the command from the [JHipsters documentation](https://www.jhipster.tech/jhipster-registry/#installation):

```bash
$ wget https://github.com/jhipster/jhipster-registry/releases/download/v6.1.2/jhipster-registry-6.1.2.jar
$ java -jar jhipster-registry-6.1.2.jar --spring.profiles.active=dev --spring.security.user.password=admin --jhipster.security.authentication.jwt.secret=my-secret-key-which-should-be-changed-in-production-and-be-base64-encoded --spring.cloud.config.server.composite.0.type=git --spring.cloud.config.server.composite.0.uri=https://github.com/jhipster/jhipster-registry-sample-config
```

Before you continue, check the registry is up-and-running under the given port `http://localhost:8761/` (see console output; user=admin; pw=admin):

<a target="_blank" href="/img/jhipster-tutorial-registry-screenshot.png">![JHipster Registry Screenshot](/img/jhipster-tutorial-registry-screenshot.png)</a>

After that, we opened a terminal window for each microservice (including the gateway) and started each service with `./mvnw`:

```bash
$ cd CustomerManagement/
$ ./mvnw
```
```bash
$ cd CustomerSelfService/
$ ./mvnw
```
```bash
$ cd DebtCollection/
$ ./mvnw
```
```bash
$ cd PolicyManagement/
$ ./mvnw
```
```bash
$ cd Printing/
$ ./mvnw
```
```bash
$ cd RiskManagement/
$ ./mvnw
```
```bash
$ cd gateway/
$ ./mvnw
```

<a target="_blank" href="/img/jhipster-tutorial-all-services-started-terminal-screenshot.png">![Terminal with All Services Started (Screenshot)](/img/jhipster-tutorial-all-services-started-terminal-screenshot.png)</a>

Once all services are started you should also see them in the JHipster registry:

<a target="_blank" href="/img/jhipster-tutorial-registry-screenshot-2.png">![JHipster Registry Screenshot With Started Services](/img/jhipster-tutorial-registry-screenshot-2.png)</a>

**Access the Application**:

JHipster generates one user interface as part of the gateway application. The other microservices are accessed by the generated RESTful HTTP interfaces.
Our generator assigns the port 8080 to the gateway application. Therefore you can access the application after you started all the services on [http://localhost:8080/](http://localhost:8080/):

<a target="_blank" href="/img/jhipster-tutorial-started-application-home-screen.png">![Started Application](/img/jhipster-tutorial-started-application-home-screen.png)</a>

The generated application will include user interfaces for CRUD (create, read, update, delete) operations for all your entities:

<a target="_blank" href="/img/jhipster-tutorial-started-application-entities.png">![UIs for All Entities](/img/jhipster-tutorial-started-application-entities.png)</a>

The JHipster generator provides many options to adjust the generated applications (changing UI framework, database, etc.). Please consult the [JHipster documentation](https://www.jhipster.tech/)
if you want to adapt the JDL file and/or the generated microservices.

That's it. A very easy way to generate microservices from a DDD/CML Context Map, isn't it? :)

## Known Limitations
The current solution (JDL template) comes with a few limitations that we are aware of:

 * In CML you can create references from one Entity to another Entity that is contained in a different Bounded Context.
   * Unfortunately this is not possible in JDL. (would be nice if JHipster would create the Entities in both microservices automatically :)
   * For now, you have to create the Entities per Bounded Context manually and ensure that you only reference Entities within the same Bounded Context.
   * _Hint_: If you create _cross-BC-references_, they are currently completely ignored by the JDL template (the future JDL integration shall fix this automatically).
 * In CML you can declare duplicate Entity names as long as they are in different Bounded Contexts. For example: multiple contexts can have an Entity of the type _Customer_.
   * JDL does not support duplicate Entity names, even if they are in different microservices.
   * _Hint_: The JDL template does currently not fix this automatically. You have to ensure that you don't have duplicate Entity names in your CML model. Otherwise the generated
     JDL file will be invalid.
 * Bidirectional references: the JHipster generator creates bidirectional relationships for all _One-To-Many_ relationships in JDL. However, it does not detect that the relation
   may already be declared bidirectionally.
   * The JHipster generator will generate duplicate code which leads to compiler errors if you already specify the relation in a bidirectional way in CML/JDL (two references/relationships).
   * Currently, you have to avoid this by specifying one of the relationships only (fix it manually in JDL or CML model).
 * Services not used: In CML you can specify services with its operations. The JDL language does however not support such a feature and the JHipster generator creates its own
   services.
   * The service operations declared in CML do therefore not find their way into the generated applications.
   * Maybe JHipster will support the declaration of Services in JDL in the future?
 * Data type mapping: In CML it is possible to reference types that are not yet defined in the model. JDL only knows primitive types or relationships to other Entities. Thus,
   we cannot map such unknown types to JDL.
   * Such types are currently mapped to _blobs_. You can avoid this by declaring corresponding Entities in CML. The generator will then add it to the JDL file and will create a 
     corresponding relationship.
   * In the future we may create Entities for this types automatically (Post-Freemarker solution).
 * Potential keyword clashes: If you use keywords that are reserved in JDL (for example "microservice") as names of the used CML objects (Bounded Contexts, Entities, 
   or Entity attributes), the resulting JDL file will not compile/validate. Please avoid the usage of such JDL keywords in order to ensure that the resulting file compiles
   (instead of "microservice", you could use "AMicroservice" or "My_microservice").
   * The JDL language with its keywords is documented [here](https://www.jhipster.tech/jdl/getting-started).
 
If you run into other problems with the generator, [let us know](https://github.com/ContextMapper/context-mapper-dsl/issues/new/).

## Frequently Asked Questions (FAQs)
 * **How can I generate a monolithic application instead of microservices?**
   * You have to adjust the generated JDL file a bit: remove the _microservice_ and _application_ definitions (only keep the _entities_ and _relationships_).
   * After you changed the JDL as described above you can use the JHipster generator to generate a monolith with all Entities (for more instructions consult the
     [JHipster documentation](https://www.jhipster.tech/)).
   * _Hint_: You can also create one _application_ of the type _monolith_, so that you don't have to answer the questions during the generation. Find the corresponding JDL
     documentation [here](https://www.jhipster.tech/jdl/applications).
   * _Hint_: You can also change our Freemarker temple (JDL.ftl) accordingly.
 * **How can I change the UI framework (for example React instead of Angular) of the gateway application or other configurations?**
   * After you generated the JDL file with our template, you can adjust the _config_ section of all generated _applications_ in JDL.
   * For example: add `clientFramework react` to the config block. 
   * Find more documentation on how to configure your applications in JDL here: [https://www.jhipster.tech/jdl/applications#available-application-options](https://www.jhipster.tech/jdl/applications#available-application-options)
 * **Why does the resulting JDL file not compile/validate?**
   * Please check the known limitations list above. You probably used a reserved keyword of the JDL language for CML objects. For example: If you name a Bounded Context
     "microservice", which is a JDL keyword, the resulting JDL file will not be valid. Please avoid using such keywords (instead of "microservice", you could use "AMicroservice" or "My_microservice").
     * To check whether a word is a reserved keyword in JDL, please consult [JHipster's JDL documentation](https://www.jhipster.tech/jdl/getting-started). 
   * If you respected the known limitations, followed the corresponding instructions, and it still does not compile, please create a 
     [GitHub issue in our repository](https://github.com/ContextMapper/context-mapper-dsl/issues/new/).

## More Links and Resources
 * [JHipster](https://www.jhipster.tech/)
 * [JHipster Domain Language (JDL)](https://www.jhipster.tech/jdl/)
 * [JHipster Microservices](https://www.jhipster.tech/microservices-architecture/)
 * [Context Mapper: Generic Generator (Freemarker Templates)](/docs/generic-freemarker-generator/)
 * [Example model used for this tutorial](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/microservice-generation/JDL-example)
