---
title: Usage as Library
permalink: /docs/library/
---

The Context Mapper DSL (CML) and its tools cannot only be used within Visual Studio Code or Eclipse, but also be integrated into other applications as a
standalone library. This library allows you to parse CML files within a project, change the model programmatically, and unparse it back to CML. You can also use tools such as the [Architectural Refactorings](/docs/architectural-refactorings/) and the provided generators for [graphical context maps](/docs/context-map-generator/), [PlantUML](/docs/plant-uml/), [MDSL](/docs/mdsl/), [Service Cutter](/docs/service-cutter/), and [Freemarker templates](/docs/generic-freemarker-generator/).

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

The latest release can be found here: [![Maven Central](https://img.shields.io/maven-central/v/org.contextmapper/context-mapper-dsl.svg?label=Maven%20Central)](https://search.maven.org/search?q=g:%22org.contextmapper%22%20AND%20a:%22context-mapper-dsl%22)

## Example Project
If you want to use Context Mapper as library within your application, have a look at our standalone example project:
[https://github.com/ContextMapper/context-mapper-standalone-example](https://github.com/ContextMapper/context-mapper-standalone-example)

This project illustrates how to setup your project (with Gradle) so that your CML files are compiled at build-time as well. It further provides code examples in Java that show how to use the models within your project (for example: parse, unparse, and use generators). 

If you have further questions regarding the library usage of Context Mapper, please 
[create an issue in our GitHub repository](https://github.com/ContextMapper/context-mapper-dsl/issues) or feel free to 
[get in touch with us](/getting-involved/#get-in-touch-with-us).
