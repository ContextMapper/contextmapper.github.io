---
title: Service Cutter Generators
permalink: /docs/service-cutter/
---

## Introduction and Motivation
The [Service Cutter](http://servicecutter.github.io/) tool provides a structured way to service decomposition. Our _Service Cutter Input Generators_ allow you to generate the [input files for Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/User-Representations). The prototypical integration of Service Cutter demonstrates the opportunity to generate suggestions how to further decompose a context-modeled system.

For more information about Service Cutter we refer to its projects wiki and two publications on it:

 * [Service Cutter Wiki](https://github.com/ServiceCutter/ServiceCutter/wiki)
 * [Service Cutter: A Systematic Approach to Service Decomposition (Paper)](https://link.springer.com/chapter/10.1007/978-3-319-44482-6_12)
 * [Service Cutter: A Systematic Approach to Service Decomposition (HSR Bachelor Thesis)](https://eprints.hsr.ch/476/)

## User Guide
The following sections describe how to use the Service Cutter generators and create the input files for Service Cutter.

### Generate Entity Relationship Model File
Service Cutter uses an [Entity-Relationship Model](https://github.com/ServiceCutter/ServiceCutter/wiki/ERM) Diagram (ERD) file that contains entities and nanoentities to describe the applications structure as its first and mandatory input. 

We assume you have a CML file with your model in your IDE with Context Mapper installed. In the context menu of the editor you find the action **Generate Service Cutter Input (ERD as JSON)**. By running this command, you generate the Service Cutter ERD file in the required JSON format:

<a href="/img/service-cutter-input-generation-1.png">![Generate ServiceCutter ERD File](/img/service-cutter-input-generation-1.png)</a>

### Generate SCL File
The second input file for Service Cutter deals with additional *User representations*. Service Cutter takes them in JSON format, but  there is some manual work required to create these file. Hence, we implemented another DSL which makes this step much easier. These files have the file extension `*.scl*` (for *Service Cutter Language*).

An SCL file can be generated out of a CML file. Again, a right-click in the CML editor will allow you to call the action **Generate Service Cutter User Representations (SCL)**:

<a href="/img/service-cutter-input-generation-2.png">![Generate ServiceCutter SCL File](/img/service-cutter-input-generation-2.png)</a>

The SCL grammar allows you to describe all [user representations supported by Service Cutter](https://github.com/ServiceCutter/ServiceCutter/wiki/User-Representations):

 * Entity Relationship Model (ERM)
 * Use Cases
 * Shared Owner Groups
 * Aggregates
 * Entities
 * Predefined Services
 * Separated Security Zones
 * Security Access Groups
 * Compatibilities

Most of the user representations we derive from the CML model automatically. The ERM is derived from the Entities and their references in CML. The Use Cases and Shared Owner Groups can be modeled in CML as well (have a look at our [service decomposition tutorial](/docs/systematic-service-decomposition/)). We further derive the Aggregates and Entities for Service Cutter from the corresponding counterparts in CML. In addition, we derive Predefined Services from already existing Bounded Contexts of your CML model. The remaining user representations have to be described manually, in case they are relevant for your application.

However, the generated SCL file already contains most of the representations:

<a href="/img/service-cutter-input-generation-2-1.png">![Generated SCL File](/img/service-cutter-input-generation-2-1.png)</a>

**Note:** The automatically derived user representations are overwritten if you call the generator again.

#### Examplary SCL File
In case you want to add more user representations that are missing in the automatically generated ones, you can generate an exemplary SCL file that illustrates the syntax for all possible representations. Just call the **Generate Service Cutter User Representation Example File (SCL)** action to generate an example:

<a href="/img/service-cutter-input-generation-2-2.png">![Generate Exemplary SCL File](/img/service-cutter-input-generation-2-2.png)</a>

**Note:** This generated SCL file is only exemplary and intended to help you setting up the structure in the actual SCL file generated in the step above.

### Generate User Representations JSON File
Once you have prepared your SCL file, you can generate the corresponding JSON file with the action **Generate Service Cutter User Representation JSON File** in the context menu:

<a href="/img/service-cutter-input-generation-3.png">![Generate ServiceCutter JSON out of SCL File](/img/service-cutter-input-generation-3.png)</a>

### Using the JSON files in Service Cutter
Now you have both JSON files that are required for the Service Cutter tool, generated into the **src-gen** folder:

<a href="/img/service-cutter-input-generation-4.png">![Generated JSON files for Service Cutter](/img/service-cutter-input-generation-4.png)</a>

Have fun with cutting your services :)

*Note:* Service Cutter has not been updated in a while, and only intended to demonstrate the possibilities of criteria-based graph clustering in the context of service decomposition (and establish a method and a first catalog of criteria). So do not expect mature, production-ready cuts to be suggested, but view them as a discussion and design workshop input. Further research is required to harden the approach; such research is ongoing (evidence: [40+ citations of the Service Cutter paper presented at ESOCC 2016](https://www.researchgate.net/publication/307873263_Service_Cutter_A_Systematic_Approach_to_Service_Decomposition)).  

<a href="/img/service-cutter-insurance-example.png">![Service Cutter Insurance Example](/img/service-cutter-insurance-example.png)</a>

## Further Links
Note that you can also generate new service cuts in Context Mapper directly without using Service Cutter! We integrated the Service Cutter library into Context Mapper so that our users are able to generate new service decompositions out of CML models easily.

 * Have a look at our [Systematic Service Decomposition with Context Mapper and Service Cutter](/docs/systematic-service-decomposition/) tutorial.
