---
title: Create CML Project
permalink: /docs/getting-started-create-project/
---

This page describes how you can start with Context Mapper and create your first CML model. Getting started with Context Mapper is easy, the following four steps will do:

 1. Install Context Mapper in Eclipse or Visual Studio Code
 2. Create a project
 3. _Eclipse only: enable the Xtext project nature_
 4. Create a file with the file extension **.cml**
 
## 1. Install Context Mapper
You can use Context Mapper in Eclipse, Visual Studio Code, or the online IDE Gitpod. Find the links to the marketplaces below:

 * **Visual Studio Code:**
   * Marketplace: [Context Mapper for VS Code](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension)
      1. Open the extensions view on your VS Code (Ctrl+Shift+X)
      2. Search for "Context Mapper"
      3. Select the plugin with our Context Mapper logo and press "Install".
   * Note: Does not support all features we have in Eclipse yet. You can find a feature support table [here](/docs/ide/).
 * **Open VSX Registry for Gitpod:**
   * Registry: [Context Mapper extension](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension)
      1. The easiest way to start: [Start Gitpod with our demo repository right now](https://contextmapper.org/demo/) (you can also fork the repo first, in case you want to commit your own models).
      2. Alternatively: Start your own [Gitpod](https://www.gitpod.io/) and search for "Context Mapper" in the extension view (and install it manually). You find [installation instructions here](/docs/online-ide/).
 * **Eclipse:**
   * Marketplace: [Context Mapper for Eclipse](https://marketplace.eclipse.org/content/context-mapper)
      1. Open the marketplace in your Eclipse with the menu entry _Help -> Eclipse Marketplace..._
      2. Search for "Context Mapper"
      3. Press "Install" on the Context Mapper plugin
   * Alternatively, you can follow this procedure to install the plugin from update site URL directly:
      1. Open the plugin installation dialog in Eclipse with the menu entry _Help -> Install New Software..._
      2. Enter the following update site URL to the field _Work with:_ on the top of the dialog:
    <br/>[https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/](https://dl.bintray.com/contextmapper/context-mapping-dsl/updates/)
      3. Select the two features _ContextMappingDSL_ and _ContextMappingDSL (Sources)_ and continue with _Next_.
      4. Finish the plugin installation by completing the wizard.

## 2. Create or Open your Project
In order to create a CML model, you need to create or open a project/workspace. 

For Eclipse users: you can use any project type such as _Java Project_, _Maven Project_, 
_Gradle Project_ or just a general _Project_. Use the _File -> New_ menu or the context menu in the Project Explorer to create a project. 

## 3. Eclipse Only: Enable Xtext Nature
As mentioned above, it does not matter which project type you use. However, your project has to be an Xtext project, which means it requires the Xtext *nature* in Eclipse. There are ways to achieve this:

 * **Option 1**: Open the context menu on your project (right-click) and use the menu entry _Configure -> Convert to Xtext Project_.
    <a href="/img/convert-to-xtext-project.png">![Enable Xtext nature on Eclipse project](/img/convert-to-xtext-project.png)</a>
 * **Option 2**: Just jump to step four and create a file with the extension **.cml**. Eclipse will ask you if you want to enable the Xtext nature. Press _Yes_.
 
## 4. Create .cml Model File
Once you have created your project, you can create a file with the extension **.cml** in order to start modeling with Context Mapper. 

**Note for Eclipse users**: If you already enabled the Xtext nature in step three, the file opens and you can start modeling. Otherwise Eclipse will ask you whether you want to enable it now:
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
