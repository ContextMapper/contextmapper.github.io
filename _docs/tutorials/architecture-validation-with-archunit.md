---
title: Validating the Implementation against the Model (with ArchUnit)
permalink: /docs/architecture-validation-with-archunit/
image: /img/cm-og-image.png
---

One of Context Mapper's core features, besides modeling the higher-level architecture based on strategic DDD, is that users are able to model their tactic designs of their individual Bounded Contexts (the **domain models**). The tool can be used very early in projects to design your domain models and evolve the DDD ubiquitous language. We can then use the models to:

 - Generate graphical design/architecture diagrams
 - Discuss the design with the customer and other stakeholders
 - Generate service contracts and/or prototypes (code)
 - etc.

However, once you start implementing your applications/services/components, the concepts of your model find its way into the code and _gaps between your model and the code_ potentially emerge. We are all aware of this problem that happens with documentation that is not updated as well. Changes to the domain model may only be applied to the actual implementation and your model and/or documentation gets deprecated.

When you work with Context Mapper and have a `*.cml` file with your model in your Git repository, you want to keep this model _up-to-date_ and ensure that it is _in-sync_ with the actual implementation. As a software architect and/or modeler, you also want to ensure that the system is implemented according to your model. In the following we present one approach how to _avoid gaps between the model and the code_ and to _ensure that the implementation conforms to your model_. If you integrate the automatically generated design/architecture diagrams into your documentation (in an automated process), this approach can also ensure that your documentation is always _up-to-date_.

Our [ArchUnit extension](https://github.com/ContextMapper/context-mapper-archunit-extension) presented in this tutorial helps Context Mapper users to keep their Java code and CML models _in-sync_.

## Example Model
In this tutorial we assume that you are aware of the [Context Mapper DSL (CML) language](/docs/language-reference/) and have already created CML models.

We will illustrate our validation approach with [ArchUnit](https://www.archunit.org/) with a small, exemplary domain model:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> eCommerceContext {

  <span class="k">Aggregate</span> Product {
    <span class="k">Entity</span> Product {
      <span class="k">aggregateRoot</span>

      - <span class="k">ProductId</span> id;
      <span class="k">String</span> name;
      <span class="k">String</span> description;
      <span class="k">double</span> price;
    }

    <span class="k">ValueObject</span> ProductId {
      <span class="k">String</span> value;
    }
  }

  <span class="k">Aggregate</span> Order {
    <span class="k">Entity</span> Order {
      <span class="k">aggregateRoot</span>

      - <span class="k">OrderId</span> id;
      - <span class="k">UserId</span> purchaserId;
      - <span class="k">List</span>&lt;OrderItem&gt; items;
      <span class="k">DateTime</span> ordered;
    }

    <span class="k">ValueObject</span> OrderItem {
      - <span class="k">ProductId</span> productId;
      <span class="k">int</span> amount;
    }

    <span class="k">ValueObject</span> OrderId {
      <span class="k">String</span> value;
    }
  }

  <span class="k">Aggregate</span> User {
    <span class="k">Entity</span> User {
      <span class="k">aggregateRoot</span>

      - <span class="k">UserId</span> id;
      <span class="k">String</span> name;
      <span class="k">String</span> ^email;
    }

    <span class="k">ValueObject</span> UserId {
      <span class="k">String</span> value;
    }
  }

}
</pre></div>

With our [PlantUML generator](/docs/plant-uml/) we can visualize the model as follows:

<a target="_blank" href="/img/model_BC_eCommerceContext.png">![eCommerce Sample Domain Model](/img/model_BC_eCommerceContext.png)</a>

We use a simple eShop scenario where we basically just have _products_ that can be _ordered_ by _users_. An _order_ consists of multiple _order items_.

## Expressing DDD Concepts in the Code
The ability to express the tactic DDD concepts (aggregates, entities, value objects, etc.) in the code is a prerequisite for this approach. Only if your are able to map pieces of code (such as classes in Java) to these concepts, you are able to compare it with a CML model. In Java, this is typically done by using annotations or by implementing corresponding interfaces.

[jMolecules](https://github.com/xmolecules/jmolecules) is a Java library that supports expressing architectural abstractions, including tactic DDD concepts, in your code. In this tutorial we will work with [jMolecules](https://github.com/xmolecules/jmolecules). Our [ArchUnit extension](https://github.com/ContextMapper/context-mapper-archunit-extension) further provides predefined rules for [jMolecules](https://github.com/xmolecules/jmolecules) out of the box. However, using [jMolecules](https://github.com/xmolecules/jmolecules) is not a must! You can use your own custom annotations or any other library. We will explain later in this tutorial how you write your custom rules in this case.

The following simplified Java examples illustrate how we would annotate our classes. 

We assume that one creates a Java package for each Aggregate. We annotate the Aggregate root entities as in the following example:

```java
package org.contextmapper.archunit.example.domain.product;

import org.jmolecules.ddd.annotation.AggregateRoot;
import org.jmolecules.ddd.annotation.Entity;

import java.math.BigDecimal;

@Entity
@AggregateRoot
public class Product {

    private ProductId id;
    private String name;
    private String description;
    private BigDecimal price;

    // we removed the rest of the code to simplify the examples ...

}
```

Similarly, we annotate value objects, domain events, services, repositories, etc.:

```java
package org.contextmapper.archunit.example.domain.order;

import org.contextmapper.archunit.example.domain.product.ProductId;
import org.jmolecules.ddd.annotation.ValueObject;

@ValueObject
public class OrderItem {

    private final ProductId productId;
    private final int amount;

    // we removed the rest of the code to simplify the examples ...

}
```

## Validating Code against Model
As illustrated above, we now have a CML model and a corresponding Java implementation with DDD annotations (in our case [jMolecules](https://github.com/xmolecules/jmolecules) annotations).
Now we want to ensure that objects (annotated with DDD concepts) that are implemented in the code also exist in the CML model.

**Design decicion**: We currently only validate in one direction. We ensure that objects in the code also exist in the model. But we do not validate whether objects in the model also exist in the code. The reason: When we start implementing our application, we typically don't want to realize the complete model right away. Some parts of the CML model might not yet be implemented in the code. That means **all objects in the code must exist in the CML model** but **not all objects in the CML model have to be implemented in the code**.

To implement our validation we use the tool [ArchUnit](https://www.archunit.org/). [ArchUnit](https://www.archunit.org/) allows you to enforce architectural rules by implementing simple JUnit tests. With our [ArchUnit extension](https://github.com/ContextMapper/context-mapper-archunit-extension) we provide predefined rules and conditions to validate your code against a CML model.

The extension offers:

 - Predefined conditions that check specific things in your CML model. For example: _Does the Aggregate «Product» exist in the Bounded Context «eCommerceContext»?_
 - Predefined rules in case you want to work with [jMolecules](https://github.com/xmolecules/jmolecules) as we do. For example: _Ensure that the CML model contains entities for all classes annotated with @Entity._
   - _Note:_ In case you work with your custom annotations, you can implement your own rules by just using our conditions.

### Using the Extension
Our ArchUnit extension is published into the Maven Central and therefore an integration into your project (via Gradle, Maven, etc.) is easy. (replace `1.0.0` with the latest version)

**Gradle**:

```gradle
testImplementation 'org.contextmapper:context-mapper-archunit-extension:1.0.0'
```

**Maven**:

```xml
<dependency>
  <groupId>org.contextmapper</groupId>
  <artifactId>context-mapper-archunit-extension</artifactId>
  <version>1.0.0</version>
</dependency>
```

### Available Rules and Conditions
Currently we provide rules and conditions to validate the following tactic DDD objects, if used in the code, also exist in the CML model:

 - Aggregate
 - Module
 - Entity
 - Value Object
 - Domain Event
 - Service
 - Repository

In addition to that you can validate:

 - whether Aggregates consist of the same objects (entities, value objects, domain events).
 - whether all fields of Entities in the code are modeled in CML.
 - whether all fields of Value Objects in the code are modeled in CML.
 - whether all fields of Domain Events in the code are modeled in CML.

A list of all available rules and conditions can be found in the [README of the extension repository](https://github.com/ContextMapper/context-mapper-archunit-extension) or in the JavaDoc documentation:

 - [Predefined conditions (JavaDoc)](https://www.javadoc.io/doc/org.contextmapper/context-mapper-archunit-extension/latest/org/contextmapper/archunit/ContextMapperArchConditions.html)
 - [Predefined rules for jMolecules annotations (JavaDoc)](https://www.javadoc.io/doc/org.contextmapper/context-mapper-archunit-extension/latest/org/contextmapper/archunit/ContextMapperJMoleculesArchRules.html)

### Applying All Rules
In case you use the [jMolecules](https://github.com/xmolecules/jmolecules) annotations and want to apply all our predefined rules, the implementation of the validation is very simple. For this use case we provide an abstract JUnit test case which you simply have to extend:

```java
class TacticArchUnitTestExample extends AbstractTacticArchUnitTest {

    @Override
    protected String getBoundedContextName() {
        return "eCommerceContext";
    }

    @Override
    protected String getCMLFilePath() {
        return "src/main/cml/model.cml";
    }

    @Override
    protected String getJavaPackageName2Test() {
        return "org.contextmapper.archunit.example.domain";
    }
}
```

By implementing the three abstract methods, you provide the following parameters:

 - the name of the CML Bounded Context against you want to validate
 - the path to the `*.cml` file (the model)
 - the Java package that contains the code you want to validate

### Applying Custom Set of Rules
Maybe you want to use [jMolecules](https://github.com/xmolecules/jmolecules), but you only want to apply a subset of our predefined rules (or your own rules). In this case you can implement your custom JUnit test case and call our predefined rules as in the following example:

```java
import static org.contextmapper.archunit.ContextMapperJMoleculesArchRules.*;

class CmlArchUnitTestExample {

    private BoundedContext context;
    private JavaClasses classes;

    @BeforeEach
    protected void setup() {
        this.context = new BoundedContextResolver()
                .resolveBoundedContextFromModel("./src/main/cml/model.cml", "eCommerceContext");
        this.classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("org.contextmapper.archunit.example.domain");
    }

    @Test
    void aggregatesShouldBeModeledInCML() {
        aggregateClassesShouldBeModeledInCml(context).check(classes);
    }

    @Test
    void aggregatesShouldAdhereToCmlAggregateStructure() {
        aggregatesShouldAdhereToCmlStructure(context).check(classes);
    }

    @Test
    void modulesShouldBeModeledInCML() {
        modulePackagesShouldBeModeledInCml(context).check(classes);
    }

    @Test
    void entitiesShouldBeModeledInCML() {
        entityClassesShouldBeModeledInCml(context).check(classes);
    }

    @Test
    void valueObjectsShouldBeModeledInCML() {
        valueObjectClassesShouldBeModeledInCml(context).check(classes);
    }

    @Test
    void domainEventsShouldBeModeledInCML() {
        domainEventClassesShouldBeModeledInCml(context).check(classes);
    }

    @Test
    void servicesShouldBeModeledInCML() {
        serviceClassesShouldBeModeledInCml(context).check(classes);
    }

    @Test
    void repositoriesShouldBeModeledInCML() {
        repositoryClassesShouldBeModeledInCml(context).check(classes);
    }

    @Test
    void entitiesShouldAdhereToCmlStructure() {
        entitiesShouldAdhereToCmlEntityStructure(context).check(classes);
    }

    @Test
    void valueObjectsShouldAdhereToCmlStructure() {
        valueObjectsShouldAdhereToCmlValueObjectStructure(context).check(classes);
    }

    @Test
    void domainEventsShouldAdhereToCmlStructure() {
        domainEventsShouldAdhereToCmlDomainEventStructure(context).check(classes);
    }
}
```

As already mentioned, the rules as used above work with the [jMolecules](https://github.com/xmolecules/jmolecules) annotations. The next section illustrates how you can implement the same rules with your own annotations.

### Use Custom Annotations
In case you don't want to use [jMolecules](https://github.com/xmolecules/jmolecules), you can implement your validation with your own annotations as well. In this case you can simply select the classes by yourself and use our predefined conditions to check against the CML model. An example:

```java
import static org.contextmapper.archunit.ContextMapperArchConditions.*;

class CmlArchUnitTestExample {

    private BoundedContext context;
    private JavaClasses classes;

    @BeforeEach
    protected void setup() {
        this.context = new BoundedContextResolver()
                .resolveBoundedContextFromModel("./src/main/cml/model.cml", "eCommerceContext");
        this.classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("org.contextmapper.archunit.example.domain");
    }

    @Test
    void aggregatesShouldBeModeledInCML() {
        classes().that().areAnnotatedWith(AggregateRoot.class)
                .should(beModeledAsAggregatesInCML(context)).check(classes);
    }

    @Test
    void modulesShouldBeModeledInCML() {
        classes().that().areAnnotatedWith(Module.class)
                .should(beModeledAsModulesInCML(context)).check(classes);
    }

    @Test
    void entitiesShouldBeModeledInCML() {
        classes().that().areAnnotatedWith(Entity.class)
                .should(beModeledAsEntityInCML(context)).check(classes);
    }

    @Test
    void valueObjectsShouldBeModeledInCML() {
        classes().that().areAnnotatedWith(ValueObject.class)
                .should(beModeledAsValueObjectInCML(context)).check(classes);
    }

    @Test
    void domainEventsShouldBeModeledInCML() {
        classes().that().areAnnotatedWith(DomainEvent.class)
                .should(beModeledAsDomainEventInCML(context)).check(classes);
    }

    @Test
    void servicesShouldBeModeledInCML() {
        classes().that().areAnnotatedWith(Service.class)
                .should(beModeledAsServiceInCML(context)).check(classes);
    }

    @Test
    void repositoriesShouldBeModeledInCML() {
        classes().that().areAnnotatedWith(Repository.class)
                .should(beModeledAsRepositoryInCML(context)).check(classes);
    }

    @Test
    void entitiesShouldAdhereToCmlStructure() {
        classes().that().areAnnotatedWith(Entity.class)
                .should(adhereToCmlEntityStructure(context)).check(classes);
    }

    @Test
    void valueObjectsShouldAdhereToCmlStructure() {
        classes().that().areAnnotatedWith(ValueObject.class)
                .should(adhereToCmlValueObjectStructure(context)).check(classes);
    }

    @Test
    void domainEventsShouldAdhereToCmlStructure() {
        classes().that().areAnnotatedWith(DomainEvent.class)
                .should(adhereToCmlDomainEventStructure(context)).check(classes);
    }
}
```

Basically you can implement your custom _classes().that()..._ part and use our predefined conditions in the _.should(...)_ part of the rules.

### Result
No matter in which of the three ways you implement your tests, you can realize a validation of your code against the CML model in a simple way with this approach.

If a developer adds a new object that is not modeled your build will fail. For example, let us assume someone adds a new value object `ProductDetail` to the `Product` aggregate:

```java
package org.contextmapper.archunit.example.domain.product;

import org.jmolecules.ddd.annotation.AggregateRoot;
import org.jmolecules.ddd.annotation.Entity;

import java.math.BigDecimal;

@Entity
@AggregateRoot
public class Product {

    private ProductId id;
    private String name;
    private String description;
    private BigDecimal price;
    private ProductDetail detail;

    // we removed the rest of the code to simplify the examples ...

}
```

```java
package org.contextmapper.archunit.example.domain.product;

@ValueObject
public class ProductDetail {
}
```

... building your project, or just running the unit tests, will fail with an exception: (the rule `valueObjectsShouldBeModeledInCML` is violated)

```text
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 2.701 s - in org.contextmapper.archunit.example.SampleApplicationTest
2021-05-31 08:48:54.186  INFO 15800 --- [extShutdownHook] o.s.s.concurrent.ThreadPoolTaskExecutor  : Shutting down ExecutorService 'applicationTaskExecutor'
[INFO] 
[INFO] Results:
[INFO] 
[ERROR] Failures: 
[ERROR]   CmlArchUnitTestExample.valueObjectsShouldBeModeledInCML:64 Architecture Violation [Priority: MEDIUM] - Rule 'classes that are annotated with @ValueObject should be modeled as value object in CML.' was violated (1 times):
The value object 'ProductDetail' is not modeled in CML.
[INFO] 
[ERROR] Tests run: 26, Failures: 1, Errors: 0, Skipped: 0
[INFO] 
```

With this approach we can ensure that the model, and maybe automatically generated documentation, is updated with the code.

That's it. Try it out and give us your feedback if you have any issues in implementing your architecture validation with CML!

## Next Steps

 - Try it out!
 - Do you have problems using our ArchUnit extension? Please create an issue [here](https://github.com/ContextMapper/context-mapper-archunit-extension/issues).
 - Do you need additional rules and/or conditions? Contributions are always welcome! Create a pull request in our [GitHub repo](https://github.com/ContextMapper/context-mapper-archunit-extension) or create an [issue](https://github.com/ContextMapper/context-mapper-archunit-extension/issues) so that we know which rules would be interesting for you.
 - Any other feedback is welcome too! [Contact us](/getting-involved/).
