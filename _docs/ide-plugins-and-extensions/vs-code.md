---
title: Visual Studio Code Extension
permalink: /docs/vs-code/
---

This page contains FAQs and helpful tipps specific for the Visual Studio Code extension.

## Installation of the VS Code Extension

You find our Context Mapper VS Code extension in the VS Code marketplace:

 * [VS Code Marktplace](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension)
   * Option 1: Search our extension in the Extensions view in VS code: search for "Context Mapper"
   * Option 2: Press Ctrl+P in your VS code and then enter `ext install contextmapper.context-mapper-vscode-extension`
   * Option 3: Download the *.vsix file from the marketplace and use _Install from VSIX..._ in the options menu of the Extension view in VS code.

## Frequently Asked Questions (FAQs)

### You did not find a Context Mapper feature in VS code?
We only recently released Context Mapper for VS code and not all features are already supported. You find a feature table [here](/docs/ide/). We work on the extension continuously and hope to support all features soon.

### The graphical Context Map generator in VS cCde has not the same input parameters as in Eclipse (dialog). Why?
With our new VS Code extension we try to reduce user input for commands to a minimum, so that you don't have to parameterize each time you generate. You can still configure the parameters, but in the settings of the VS code extension. Open the settings (Ctrl+Shift+P -> search for "Open Settings (UI)") and search then open "Extensions -> Context Mapper":

<a target="_blank" href="/img/vs-code-context-mapper-settings.png">![Context Mapper Settings in VS Code](/img/vs-code-context-mapper-settings.png)</a>

### I have other questions not listed here. How can I contribute?
If you have any questions not answered by our documentation page, we appreciate if you create an issue in our documentation [repo](https://github.com/ContextMapper/contextmapper.github.io/issues). Of course, Pull Requests (PRs) are always welcome too.
