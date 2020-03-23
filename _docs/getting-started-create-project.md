---
title: Create CML Project
permalink: /docs/getting-started-create-project/
---

This page describes how you can start with Context Mapper and create your first CML model. Getting started with Context Mapper is easy, the following four steps will do:

 1. Install Context Mapper plugin
 2. Create an Eclipse project
 3. Enable the Xtext project nature
 4. Create a file with the file extension **.cml**
 
## 1. Install Context Mapper Plugin
The Context Mapper Eclipse plugin can be installed via the marketplace:
<br>([https://marketplace.eclipse.org/content/context-mapper](https://marketplace.eclipse.org/content/context-mapper))

 1. Open the marketplace in your Eclipse with the menu entry _Help -> Eclipse Marketplace..._
 2. Search for "Context Mapper"
 3. Press "Install" on the Context Mapper plugin

<a href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=5009351" class="drag" title="Drag to your running Eclipse* workspace. *Requires Eclipse Marketplace Client"><img typeof="foaf:Image" class="img-responsive" src="https://marketplace.eclipse.org/sites/all/themes/solstice/public/images/marketplace/btn-install.png" alt="Drag to your running Eclipse* workspace. *Requires Eclipse Marketplace Client" /></a>

Alternatively, you can follow this procedure to install the plugin from update site URL directly:

 1. Open the plugin installation dialog in Eclipse with the menu entry _Help -> Install New Software..._
 2. Enter the following update site URL to the field _Work with:_ on the top of the dialog:
    <br/>[https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)
 3. Select the two features _ContextMappingDSL_ and _ContextMappingDSL (Sources)_ and continue with _Next_.
 4. Finish the plugin installation by completing the wizard.
 
## 2. Create an Eclipse Project
In order to create a CML model, you need an Eclipse project. You can use any project type such as _Java Project_, _Maven Project_, 
_Gradle Project_ or just a general _Project_. Use the _File -> New_ menu or the context menu in the Project Explorer to create a project. 

**Note:** You can also use one of your existing projects and create a CML model there. In this case, skip this and continue with the next step.

## 3. Enable the Xtext Project Nature
As mentioned above, it does not matter which project type you use. However, your project has to be an Xtext project, which means it requires the Xtext *nature* in Eclipse. There are ways to achieve this:

 * **Option 1**: Open the context menu on your project (right-click) and use the menu entry _Configure -> Convert to Xtext Project_.
    <a href="/img/convert-to-xtext-project.png">![Enable Xtext nature on Eclipse project](/img/convert-to-xtext-project.png)</a>
 * **Option 2**: Just jump to step four and create a file with the extension **.cml**. Eclipse will ask you if you want to enable the Xtext nature. Press _Yes_.
 
## 4. Create .cml Model File
Once you have created your project, you can create a file with the extension **.cml** in order to start modeling with Context Mapper. Use the _New Context Mapper DSL (CML) File_ wizard:
<a href="/img/screenshot-new-cml-file-1.png">![Create CML file wizard (1)](/img/screenshot-new-cml-file-1.png)</a>

<a href="/img/screenshot-new-cml-file-2.png">![Create CML file wizard (2)](/img/screenshot-new-cml-file-2.png)</a>

**Note**: If you already enabled the Xtext nature in step three, the file opens and you can start modeling. Otherwise Eclipse will ask you whether you want to enable it now:
<a href="/img/create-cml-file-enable-nature.png">![Enable Xtext nature at CML file creation](/img/create-cml-file-enable-nature.png)</a>

In this case you have to confirm with _Yes_. 

## Ready to Model
You can now start writing CML in the Context Mapper editor. Use the following resources to get started:

 * Introductory CML snippets on our [welcome page](/docs/home/)
 * Sample models in our [examples repository](https://github.com/ContextMapper/context-mapper-examples)
 * Detailed documentation about the language features in our [language reference](/docs/language-reference/) section.
 * [FAQ's](/docs/faq/)
 
*Note:* If you want to model across multiple *.cml files, for example to use Bounded Contexts in multiple Context Maps, consult the [Imports](/docs/imports/) page of our language reference.
 
Once you have modeled your system with CML, you may want use our generators to produce other representations or evolve the model by using [*Architectural Refactorings (ARs)*](https://www.infoq.com/articles/architectural-refactoring/):

 * [Architectural Refactorings (ARs)](/docs/architectural-refactorings/)
 * User Guides for generators:
    * [Graphical Context Map generator](/docs/context-map-generator/)
    * [PlantUML generator](/docs/plant-uml/)
    * [MDSL (Micro-)Service Contracts Generator](/docs/mdsl/)
    * [ServiceCutter generator](/docs/service-cutter/)
    * [Generic generator](/docs/generic-freemarker-generator/) (Freemarker templates)
