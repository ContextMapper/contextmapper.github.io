---
title: Create CML Project
permalink: /docs/getting-started-create-project/
---

This page describes how you can start with Context Mapper and create your first CML model. Getting started with Context Mapper is easy and 
includes the following first steps:

 1. Install Context Mapper plugin
 2. Create an Eclipse project
 3. Enable the Xtext project nature
 4. Create a file with the file extension **.cml**
 
## 1. Install Context Mapper Plugin
Follow this procedure to install the Context Mapper plugin:

 1. Open the plugin installation dialog in Eclipse with the menu entry _Help -> Install New Software..._
 2. Enter the following update site URL to the field _Work with:_ on the top of the dialog:
    <br/>[https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)
 3. Select the two features _ContextMappingDSL_ and _ContextMappingDSL (Sources)_ and continue with _Next_.
 4. Finish the plugin installation by completing the wizard.
 
## 2. Create an Eclipse Project
In order to create a CML model, you need an Eclipse project. You can use any project type such as _Java Project_, _Maven Project_, 
_Gradle Project_ or just a general _Project_. Use the _File -> New_ menu or the context menu in the project explorer to create a project. 

**Note:** You can also use one of your existing projects and create a CML model there. In this case go to the next step.

## 3. Enable the Xtext Project Nature
As mentioned above, it does not matter which project type you use. However, your project has to be an Xtext project which means it needs
the Xtext nature. There are **two** easy **possibilities** to enable the Xtext nature on your project:

 * **Option 1**: Open the context menu on your project (right-click) and use the menu entry _Configure -> Convert to Xtext Project_.
    <a href="/img/convert-to-xtext-project.png">![Enable Xtext nature on Eclipse project](/img/convert-to-xtext-project.png)</a>
 * **Option 2**: Just jump to step four and create a file with the extension **.cml**. Eclipse will ask you if you want to enable the Xtext nature. Press _Yes_.
 
## 4. Create .cml File
Once you created your project, you can create a file with the extension **.cml** in order to start modeling with Context Mapper. Use the 
_New File_ wizard:
<a href="/img/create-cml-file.png">![Create CML file](/img/create-cml-file.png)</a>

**Note**: If you already enabled the Xtext nature in step three, the file opens and you can start modeling. Otherwise Eclipse will ask you now if you
want to enable it:
<a href="/img/create-cml-file-enable-nature.png">![Enable Xtext nature at CML file creation](/img/create-cml-file-enable-nature.png)</a>

In this case you have to confirm with _Yes_. 

## Ready to Model
You can now start with writing CML in the Context Mapper editor. Use the following resources to get started:

 * Introductory CML snippets on our [welcome page](/docs/home/)
 * Example models in our [examples repository](https://github.com/ContextMapper/context-mapper-examples)
 * Detailed documentation about the language features in our [language reference](/docs/language-reference/) section.
 * [FAQ's](/docs/faq/)
 
 <div class="alert alert-custom">
 <strong>Note</strong> that a CML Context Map with all Bounded Contexts etc. currently has to be modeled within one single .cml file.
 Splitting the model into multiple files is not yet supported but we have an <a href="https://github.com/ContextMapper/context-mapper-dsl/issues/86">
 open issue</a> on Github for this. Currently each .cml file contains its own model and cannot reference objects located in other files.
 In addition, each .cml file (model) can only contain one Context Map.  
 </div>
 
Once you have modeled your system with CML you may want use our generators to produce other representations or evolve the model by using
out Architectural Refactorings (ARs):

 * [Architectural Refactorings (ARs)](/docs/architectural-refactorings/)
 * User Guides for generators:
    * [PlantUML generator](/docs/plant-uml/)
    * [MDSL (Micro-)Service Contracts Generator](/docs/mdsl/)
    * [ServiceCutter generator](/docs/service-cutter/)
