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

We assume you have a CML file with your model in Eclipse (with our plugin installed). A right-click to the CML-file will guide you to a **Context Mapper** context menu. When selecting the action **Service Cutter: Generate Input File (JSON)**, you generate the Service Cutter ERD file in the required JSON format:

<a href="/img/service-cutter-input-generation-1.png">![Generate ServiceCutter ERD File](/img/service-cutter-input-generation-1.png)</a>

<div class="alert alert-custom">
<strong>Note</strong> that the <strong>Context Mapper</strong> menu entry is also available within the context menu uf the CML editor 
(right-click anywhere in the editor).
</div>

### Generate SCL File
The second input file for Service Cutter deals with additional *User representations*. Service Cutter takes them in JSON format, but  there is some manual work required to create these file. Hence, we implemented another DSL which makes this step much easier. These files have the file extension `*.scl*` (for *Service Cutter Language*).

A SCL file can be generated out of a CML file. Again, a right-click to the CML-file will open the **Context Mapper** context menu. You can initialize your SCL file with the action **Service Cutter: Initialize User Representations File (Exemplary)**:

<a href="/img/service-cutter-input-generation-2.png">![Generate ServiceCutter SCL File](/img/service-cutter-input-generation-2.png)</a>

**Note:** The generated SCL file is a template that intends to help you by setting the structure expected by Service Cutter. The following generated parts are only examples, and 
will have to be adjusted:

 * **[Use Cases](https://github.com/ServiceCutter/ServiceCutter/wiki/Use-Cases)**
 * **All [Compatibilities](https://github.com/ServiceCutter/ServiceCutter/wiki/Compatibilities)**
 * **[Security Access Groups](https://github.com/ServiceCutter/ServiceCutter/wiki/Security-access-groups)**
 * **[Separated Security Zone](https://github.com/ServiceCutter/ServiceCutter/wiki/Separated-security-zones)**
 * **[Shared Owner Group](https://github.com/ServiceCutter/ServiceCutter/wiki/Shared-owner-groups)**

The following elements are actually derived from the CML model and do not have to be changed:

 * **[Aggregates](https://github.com/ServiceCutter/ServiceCutter/wiki/Aggregates)** (derived from your Aggregates in the CML file)
 * **[PredefinedService](https://github.com/ServiceCutter/ServiceCutter/wiki/Predefined-services)** (derived from your bounded contexts in the CML file)

### Generate User Representations JSON File
Once you have prepared your SCL file, you can generate the corresponding JSON file with the action **Service Cutter: Generate User Representations File (JSON)** in the context menu:

<a href="/img/service-cutter-input-generation-3.png">![Generate ServiceCutter JSON out of SCL File](/img/service-cutter-input-generation-3.png)</a>

### Using the JSON files in Service Cutter
Now you have both JSON files that are required for the Service Cutter tool, generated into the **src-gen** folder:

<a href="/img/service-cutter-input-generation-4.png">![Generated JSON files for Service Cutter](/img/service-cutter-input-generation-4.png)</a>

Have fun with cutting your services :)

*Note:* Service Cutter has not been updated in a while, and only intended to demonstrate the possibilities of criteria-based graph clustering in the context of service decomposition (and establish a method and a first catalog of criteria). So do not expect mature, production-ready cuts to be suggested, but view them as a discussion and design workshop input. Further research is required to harden the approach; such research is ongoing (evidence: [40+ citations of the Service Cutter paper presented at ESOCC 2016](https://www.researchgate.net/publication/307873263_Service_Cutter_A_Systematic_Approach_to_Service_Decomposition)).  

<a href="/img/service-cutter-insurance-example.png">![Service Cutter Insurance Example](/img/service-cutter-insurance-example.png)</a>
