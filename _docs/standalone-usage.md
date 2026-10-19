---
title: Usage as Library
permalink: /docs/library/
---

The Context Mapper DSL (CML) and its tools cannot only be used within Visual Studio Code or Eclipse, but also be integrated into other applications as a
standalone library. This library allows you to parse CML files within a project, change the model programmatically, and unparse it back to CML. You can also use tools such as the [Architectural Refactorings](/docs/architectural-refactorings/) and the provided generators for [graphical context maps](/docs/context-map-generator/), [PlantUML](/docs/plant-uml/), [MDSL](/docs/mdsl/), and [Freemarker templates](/docs/generic-freemarker-generator/).

## Integration
All our releases are not only published as IDE extensions or plugins, but as updates to the standalone library as well. This library is published into the [Maven Central repository](https://search.maven.org/artifact/org.contextmapper/context-mapper-dsl/) and can easily be integrated into your Maven or Gradle build:

**Gradle**:
```gradle
implementation 'org.contextmapper:context-mapper-dsl:{our-latest-version}'
```

**Maven**:
```xml
<dependency>
  <groupId>org.contextmapper</groupId>
  <artifactId>context-mapper-dsl</artifactId>
  <version>{our-latest-version}</version>
</dependency>
```

The latest release can be found here: [org.contextmapper:context-mapper-dsl on Maven Central](https://central.sonatype.com/artifact/org.contextmapper/context-mapper-dsl)

The library runs on Java 11 or newer (tested with Java 11, 17 and 21).

## Reading a CML Model in Your Code or Tests
A common use case is to read your CML model in your own build or tests, for example to derive architecture tests or other checks from the context map. The following snippet loads a CML file and iterates over the relationships of its context map:

```java
StandaloneContextMapperAPI contextMapper = ContextMapperStandaloneSetup.getStandaloneAPI();
CMLResource cml = contextMapper.loadCML("./src/main/cml/transit.cml");

for (Relationship relationship : cml.getContextMappingModel().getMap().getRelationships()) {
    if (relationship instanceof UpstreamDownstreamRelationship) {
        UpstreamDownstreamRelationship upDown = (UpstreamDownstreamRelationship) relationship;
        System.out.println(upDown.getUpstream().getName() + " " + upDown.getUpstreamRoles() + " -> "
                + upDown.getDownstream().getName() + " " + upDown.getDownstreamRoles());
    }
}
// prints for example: PaymentProvider [OHS] -> TicketSales [ACL]
```

The model classes (`BoundedContext`, `Aggregate`, `UpstreamDownstreamRelationship`, etc.) are located in the package `org.contextmapper.dsl.contextMappingDSL`; the API in `org.contextmapper.dsl.standalone`. If you want to check tactic DDD elements (Aggregates, Entities, etc.) against your Java code, have a look at our [ArchUnit extension](https://github.com/ContextMapper/context-mapper-archunit-extension).

## Example Project
If you want to use Context Mapper as library within your application, have a look at our standalone example project:
[https://github.com/ContextMapper/context-mapper-standalone-example](https://github.com/ContextMapper/context-mapper-standalone-example)

This project illustrates how to setup your project (with Gradle) so that your CML files are compiled at build-time as well. It further provides code examples in Java that show how to use the models within your project (for example: parse, unparse, and use generators). 

If you have further questions regarding the library usage of Context Mapper, please 
[create an issue in our GitHub repository](https://github.com/ContextMapper/context-mapper-dsl/issues) or feel free to 
[get in touch with us](/getting-involved/#get-in-touch-with-us).
