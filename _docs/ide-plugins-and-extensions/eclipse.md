---
title: Eclipse Plugin
permalink: /docs/eclipse/
---

This page contains FAQs and helpful tipps specific for the Context Mapper Eclipse plugin.

## Installation of Eclipse Plugin

The Context Mapper Eclipse plugin can be installed via the marketplace or by using the update site URL in your Eclipse directly:

 * [Eclipse Marktplace](https://marketplace.eclipse.org/content/context-mapper)
 * Update site URL for manual installation: [https://contextmapper.org/eclipse-update-site/](https://contextmapper.org/eclipse-update-site/)

## Frequently Asked Questions (FAQs)

### How do I install the Eclipse plugin?
Open the [Eclipse Marketplace](https://marketplace.eclipse.org/content/context-mapper) in Eclipse, search for "Context Mapper", and press "Install".

Alternatively, use the following Eclipse Update site and install the plugin in Eclipse via *Help -> Install New Software...* (copy past the update site link).

Update Site: [https://contextmapper.org/eclipse-update-site/](https://contextmapper.org/eclipse-update-site/)

### How do I create an Eclipse project with a new CML model to start modeling my Context Map?
Consult the page [Create CML Model](/docs/getting-started-create-project/). It describes how to setup your project to get started with modeling CML Context Maps.

### How do I validate all CML models (*.cml files) in my Eclipse project?
The CML models are validated when you save the *.cml automatically, if _"Build Automatically"_ is enabled in the _Project_ menu.
If it is not enabled, you can validate all models by triggering _"Build All"_ in the _Project_ menu.

### I tried to apply a model transformation (AR or OOAD) but nothing happened. Why?
It is possible that a transformation or generation tool is not applicable of results in an error, depending on your input model (for example because preconditions are not fulfilled).
Errors are logged into the **Errors** view in Eclipse. In case one of our tools (transformation, generator, AR) does not work as expected, please check if there is a message in the Errors view

### An Architectural Refactoring (AR) leaded to an empty CML file as result. Why?
This can happen in case the model transformation was not successful with your input model. You can restore the previous state of you model by pressing Ctrl+Z. You can further check the error message that was logged in the **Errors** view in Eclipse.

### I have other questions not listed here. How can I contribute?
If you have any questions not answered by our documentation page, we appreciate if you create an issue in our documentation [repo](https://github.com/ContextMapper/contextmapper.github.io/issues). Of course, Pull Requests (PRs) are always welcome too.
