---
title: Eclipse Plugin (discontinued)
permalink: /docs/eclipse/
---

<div class="alert alert-custom">
<strong>Note:</strong> The Context Mapper Eclipse plugin is <strong>discontinued</strong>. Version 6.12.0 is the last version available for Eclipse; new features and fixes are only released for <a href="/docs/vs-code/">Visual Studio Code</a> and the <a href="/docs/library/">standalone library</a>.
</div>

## Why?
The language server behind our VS Code extension supports all the refactorings, transformations and generators the Eclipse plugin offered. Concentrating on one integration lets us keep the underlying frameworks (Xtext, Java) up to date.

## I still want to use Eclipse
The last version (6.12.0) remains available, but it won't receive any updates:

 * [Eclipse Marketplace](https://marketplace.eclipse.org/content/context-mapper)
 * Update site URL for manual installation (_Help -> Install New Software..._): [https://contextmapper.org/eclipse-update-site/](https://contextmapper.org/eclipse-update-site/)

New language features (such as invariants on Aggregates) are not supported in Eclipse.

## Moving to VS Code
Your CML files work in VS Code as they are; you don't need any project configuration (such as the Xtext nature in Eclipse). Install the [VS Code extension](/docs/getting-started/) and open the folder that contains your models.
