---
title: Eclipse Plugin (discontinued)
permalink: /docs/eclipse/
---

<div class="alert alert-custom">
<strong>Note:</strong> The Context Mapper Eclipse plugin is <strong>discontinued</strong>. Version 6.12.0 is the last version available for Eclipse and can still be installed via our update site (<a href="https://contextmapper.org/eclipse-update-site/">https://contextmapper.org/eclipse-update-site/</a>). New features and fixes are only released for <a href="/docs/vs-code/">Visual Studio Code</a> and the <a href="/docs/library/">standalone library</a>.
</div>

## Why?
Context Mapper is built on [Xtext](https://eclipse.dev/Xtext/), which is no longer actively maintained. We will therefore move away from the Eclipse stack step by step:

 * **Version 6.13.0** is the first step: Context Mapper is available as VS Code extension (based on our language server) and standalone library only. The language server supports all refactorings, transformations and generators the Eclipse plugin offered.
 * **Version 7** will come with a new language server based on [Langium](https://langium.org/). With it, we will continue to offer the VS Code extension, add a plugin for IntelliJ IDEA, and aim for a solution that runs in the browser.

Our goal is to bring Context Mapper to the editors and IDEs most developers work with today.

## I still want to use Eclipse
The last version (6.12.0) remains available, but it won't receive any updates:

 * [Eclipse Marketplace](https://marketplace.eclipse.org/content/context-mapper)
 * Update site URL for manual installation (_Help -> Install New Software..._): [https://contextmapper.org/eclipse-update-site/](https://contextmapper.org/eclipse-update-site/)

New language features (such as invariants on Aggregates) are not supported in Eclipse.

## Moving to VS Code
Your CML files work in VS Code as they are; you don't need any project configuration (such as the Xtext nature in Eclipse). Install the [VS Code extension](/docs/getting-started/) and open the folder that contains your models.
