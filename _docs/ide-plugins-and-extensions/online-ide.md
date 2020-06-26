---
title: Online IDE (via Gitpod)
permalink: /docs/online-ide/
image: /img/cm-og-image.png
---

Instead of installing Context Mapper in [Eclipse](/docs/eclipse) or [Visual Studio Code](/docs/vs-code/), you can use our Editor and tools directly in the browser! If your project is hosted on Github, you can use our VS Code extension inside the online IDE provided by [Gitpod](https://www.gitpod.io/) (based on [Eclipse Theia](https://theia-ide.org/)).

You can easily find the Context Mapper extension in your Gitpod, as we publish it to the [Open VSX Registry](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension).

<a target="_blank" href="/img/gitpod-screenshot.png">![Screenshot of Browser IDE (Gitpod)](/img/gitpod-screenshot.png)</a>

## Getting Started
You can start a [Gitpod](https://www.gitpod.io/) online IDE for your Github repository by prepending `https://gitpod.io/#` to its URL. For example, if the Github repo URL is [https://github.com/ContextMapper/context-mapper-examples](https://github.com/ContextMapper/context-mapper-examples), you start the Gitpod with [https://gitpod.io/#https://github.com/ContextMapper/context-mapper-examples](https://gitpod.io/#https://github.com/ContextMapper/context-mapper-examples).

### Context Mapper Gitpod Demo
Start mapping your contexts using our demo repository right now: (you can also fork the repo first, in case you want to commit your own models)

**[Start online IDE with Context Mapper Demo](http://demo.contextmapper.org)** (http://demo.contextmapper.org)

### Context Mapper Examples Repository
Our examples repository already contains a Gitpod configuration as well. Therefore, you can simply start the online IDE and the Context Mapper extension will already be installed.

**[Start online IDE for Context Mapper Examples Now](https://gitpod.io/#https://github.com/ContextMapper/context-mapper-examples)**

### Configure Own Repository
If you start the online IDE for your any other repository (not yet configured), you can easily install the Context Mapper extension.

In case you want to configure Gitpod for all users of your repository, click "Setup Project" after you started the IDE to setup a `.gitpod.yml` file: 

<a target="_blank" href="/img/gitpod-setup-project.png">![Setup Gitpod Project (.gitpod.yml)](/img/gitpod-setup-project.png)</a>

To install Context Mapper, just open the extensions view, search for "Context Mapper", and click "Install":

<a target="_blank" href="/img/gitpod-install-contextmapper.png">![Install Context Mapper in Gitpod](/img/gitpod-install-contextmapper.png)</a>

In case you install the extension for the project (not only for user), it will be added to the `.gitpod.yml` file. By committing the file to your repo, you share the configuration with all users of your repository.

### Configure Additional Tools
Depending on how you use Context Mapper you may want to install additional tools in your Gitpod. For example: for the [graphical Context Map generator](/docs/context-map-generator/) you need [Graphviz](https://graphviz.org/) being installed on the system. This can be achieved by configuring a custom Dockerfile for your Gitpod. Just add a `.gitpod.Dockerfile` file to your Github repository. Here an example with Graphviz as additional tool:

```
FROM gitpod/workspace-full

# Install Graphviz
RUN sudo apt-get update \
    && sudo apt-get -y install graphviz
```

In the `.gitpod.yml` file you have to declare the file as follows:

```
image:
  file: .gitpod.Dockerfile
```

## Whats Next?

 * Check our [language reference](/docs/language-reference/) for the syntax of Context Mapper DSL (CML) files.
 * Have a look at our [example](/docs/examples/) models.
 * Once you are familiar with the DSL, learn more about the following tools and generators:
   * [Rapid prototyping transformations](/docs/rapid-ooad/)
   * [Architectural Refactorings (ARs)](/docs/architectural-refactorings/)
   * [Context Map Suggestions with Service Cutter](/docs/service-cutter-context-map-suggestions/)
   * [Discovery library](/docs/reverse-engineering/) to reverse engineer CML models from existing code.
   * [Generators](/docs/generators/)
