---
title: Usage as Library
permalink: /docs/library/
---

Besides using the Context Mapper DSL (CML) and its tools within our Eclipse plugin, it can also be integrated into other applications as a
library. The library allows to parse CML files within a project, change the model programmatically and unparse it back to CML, and use our
tools such as the [Architectural Refactorings](/docs/architectural-refactorings/) and the provided generators 
([PlantUML](/docs/plant-uml/), [MDSL](/docs/mdsl/), [Service Cutter](/docs/service-cutter/)).

## Integration
All our releases are not only published as Eclipse Plugin but as standalone library as well. The library is published into the [Maven
central repository](https://search.maven.org/artifact/org.contextmapper/context-mapper-dsl/) and can easily be integrated into your Maven
or Gradle build:

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

You can find our latest release version [here](https://github.com/ContextMapper/context-mapper-dsl/releases/latest).

## Example Project
If you want to use Context Mapper as library within your application, have a look at our standalone example project here:
[https://github.com/ContextMapper/context-mapper-standalone-example](https://github.com/ContextMapper/context-mapper-standalone-example)

It illustrates how you can setup your project (with Gradle) so that your CML files are compiled at build-time as well. It further provides
code examples in Java how you can use the models within your project (parse, unparse, use generators). 

If you have further questions regarding the library usage of Context Mapper 
[create an issue in our Github repository](https://github.com/ContextMapper/context-mapper-dsl/issues) or feel free to 
[get in touch with us](/getting-involved/#get-in-touch-with-us).
