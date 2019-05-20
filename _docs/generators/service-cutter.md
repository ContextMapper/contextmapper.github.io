---
title: Service Cutter Generators
permalink: /docs/service-cutter/
---

## Introduction and Motivation
The [Service Cutter](http://servicecutter.github.io/) tool provides a structured way to service decomposition. Our _Service Cutter Input Generators_ allow you to generate
the input files for [Service Cutter](http://servicecutter.github.io/). Thereby you can generate suggestions how to further decompose 
your modeled system.

For more information about Service Cutter we refer to the projects wiki and the paper:

 * [Service Cutter Wiki](https://github.com/ServiceCutter/ServiceCutter/wiki)
 * [Service Cutter: A Systematic Approach to Service Decomposition (Paper)](https://link.springer.com/chapter/10.1007/978-3-319-44482-6_12)
 * [Service Cutter: A Systematic Approach to Service Decomposition (HSR Bachelor Thesis)](https://eprints.hsr.ch/476/)

## User Guide
The following sections describe how you use the Service Cutter generators to create the 
[Service Cutter](http://servicecutter.github.io/) input files.

### Generate Entity Relationship Model File
Service Cutter uses an ERD-file based on entities and nanoentities to describe the applications structure, the first input. 

We assume you have a CML file with your model in Eclipse (with our plugin installed). With a right-click to the CML-file you will find a **Context Mapper** context menu. With the action **Service Cutter: Generate Input File (JSON)** you generate the Service Cutter ERD file in the required JSON format:

<a href="/img/service-cutter-input-generation-1.png">![Generate ServiceCutter ERD File](/img/service-cutter-input-generation-1.png)</a>

<div class="alert alert-custom">
<strong>Note</strong> that the <strong>Context Mapper</strong> menu entry is also available within the context menu uf the CML editor. 
(right-click anywhere in the editor)
</div>

### Generate SCL File
The second input file for Service Cutter is representing its **User representations**. Service Cutter takes them in JSON format, but since there is some manual work needed to create them, we implemented another DSL which makes this much easier. Those files have the file extension **scl**, for **Service Cutter Language**.

A SCL file can be generated out of a CML file. Again, with a right-click to the CML-file you will find the **Context Mapper** context menu. With the action **Service Cutter: Initialize User Representations File (Exemplary)** you can initialize your SCL file:

<a href="/img/service-cutter-input-generation-2.png">![Generate ServiceCutter SCL File](/img/service-cutter-input-generation-2.png)</a>

**Note:** The generated SCL file is a template which helps you by giving the structure. The following generated parts are only examples and have to be adjusted:

 * **Use Cases**
 * **All Compatibilities**
 * **Security Access Groups**
 * **Separated Security Zone**
 * **Shared Owner Group**

Only the following elements are actually derived from your CML model and don't have to be changed:

 * **Aggregates** (derived from your Aggregates in the CML file)
 * **PredefinedService** (derived from your bounded contexts in the CML file)

### Generate User Representations JSON File
Once you have prepared your SCL file, you can generate the corresponding JSON file with the action **Service Cutter: Generate User Representations File (JSON)** in the context menu:

<a href="/img/service-cutter-input-generation-3.png">![Generate ServiceCutter JSON out of SCL File](/img/service-cutter-input-generation-3.png)</a>

### Using the JSON files in Service Cutter
You have now both JSON files needed for the Service Cutter tool, generated into the **src-gen** folder:

<a href="/img/service-cutter-input-generation-4.png">![Generated JSON files for Service Cutter](/img/service-cutter-input-generation-4.png)</a>

Have fun with cutting your services :)

<a href="/img/service-cutter-insurance-example.png">![Service Cutter Insurance Example](/img/service-cutter-insurance-example.png)</a>



