---
title: Create CML Project
permalink: /docs/getting-started-create-project/
---

This page describes how you can start with Context Mapper and create your first CML model. Getting started with Context Mapper is easy, the following three steps will do:

 1. Install Context Mapper in Visual Studio Code
 2. Open a folder
 3. Create a file with the file extension **.cml**
 
## 1. Install Context Mapper
Install our extension from the marketplace: [Context Mapper for VS Code](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension)

 1. Open the extensions view in VS Code (Ctrl+Shift+X)
 2. Search for "Context Mapper"
 3. Select the extension with our Context Mapper logo and press "Install".

The extension needs Java 17 or newer; see the [system requirements](/docs/getting-started/#system-requirements). For editors that use the [Open VSX Registry](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension) instead of the Microsoft marketplace, the extension is available there as well.

## 2. Open a Folder
Open the folder in which you want to keep your models (_File -> Open Folder..._). This can be an empty folder or an existing project, for example the repository of the system you want to model. You don't need any special project type or configuration.

## 3. Create .cml Model File
Create a file with the extension **.cml** (_File -> New File..._). VS Code opens it in the Context Mapper editor and you can start modeling.

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
    * [Generic generator](/docs/generic-freemarker-generator/) (Freemarker templates)
