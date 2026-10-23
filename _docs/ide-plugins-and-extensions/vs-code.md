---
title: Visual Studio Code Extension
permalink: /docs/vs-code/
---

This page contains FAQs and helpful tipps specific for the Visual Studio Code extension.

## Installation of the VS Code Extension

You find our Context Mapper VS Code extension in the VS Code marketplace:

 * [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension)
   * Option 1: Search our extension in the Extensions view in VS code: search for "Context Mapper"
   * Option 2: Press Ctrl+P in your VS code and then enter `ext install contextmapper.context-mapper-vscode-extension`
   * Option 3: Download the *.vsix file from the marketplace and use _Install from VSIX..._ in the options menu of the Extension view in VS code.
 * [Open VSX Registry](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension), for editors that support VS Code extensions but don't use the Microsoft marketplace (such as VSCodium)

The extension needs Java 17 or newer to start our language server; see the [system requirements](/docs/getting-started/#system-requirements).

## Frequently Asked Questions (FAQs)

### Which features does the extension support?
You find a feature table [here](/docs/ide/).

### How do I configure the graphical Context Map generator?
The generator does not ask for parameters each time you generate. You can configure them in the settings of the VS code extension instead. Open the settings (Ctrl+Shift+P -> search for "Open Settings (UI)") and search then open "Extensions -> Context Mapper":

<a target="_blank" href="/img/vs-code-context-mapper-settings.png">![Context Mapper Settings in VS Code](/img/vs-code-context-mapper-settings.png)</a>

### I have other questions not listed here. How can I contribute?
If you have any questions not answered by our documentation page, we appreciate if you create an issue in our documentation [repo](https://github.com/ContextMapper/contextmapper.github.io/issues). Of course, Pull Requests (PRs) are always welcome too.
