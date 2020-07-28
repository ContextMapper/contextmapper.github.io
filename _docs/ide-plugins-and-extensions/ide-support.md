---
title: Feature Support
permalink: /docs/ide/
---

We currently offer Context Mapper for [Visual Studio Code](https://code.visualstudio.com/), in the Online IDE [Gitpod](https://www.gitpod.io/), and [Eclipse](https://www.eclipse.org/):

 * [Context Mapper for VS Code](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension) (Marketplace)
 * [Context Mapper Online (Gitpod)](/docs/online-ide/)
 * [Context Mapper for Eclipse](https://marketplace.eclipse.org/content/context-mapper) (Marketplace)

<div class="alert alert-custom"><strong>Note:</strong> We have only recently published the <strong>VS Code extension</strong> and it does <strong>not support all the features yet</strong>. In case you need all the features, you have to work with Eclipse for now. We work on the VS code extension and hope to <strong>support all the features soon</strong>!
</div>

<div class="alert alert-custom"><strong>Note:</strong> The Online IDE is based on our VS Code extension and supports the same features.
</div>

## Supported Features per IDE
The following table illustrates which features are already implemented in VS Code. Both IDEs shall support all features in the future.

| Feature                                                      | Supported in Eclipse Plugin | Supported in VS Code Extension (and online) |
|--------------------------------------------------------------|-----------------------------|---------------------------------------------|
| Editor: Syntax Highlighting                                  | yes                         | yes                                         |
| Editor: Auto-completion                                      | yes                         | yes                                         |
| Editor: Hover texts with pattern descriptions                | yes                         | no                                          |
| Editor: Semantic validators                                  | yes                         | yes                                         |
| Graphical Context Map generator                              | yes                         | yes                                         |
| PlantUML generator                                           | yes                         | yes                                         |
| MDSL generator                                               | yes                         | yes                                         |
| Generic text file generator                                  | yes                         | yes                                         |
| Service Cutter input file generators                         | yes                         | yes                                         |
| New service cut generator                                    | yes                         | yes                                         |
| OOAD transformation: Derive Subdomain from user requirements | yes                         | yes                                         |
| OOAD transformation: Derive Bounded Context from Subdomains  | yes                         | yes                                         |
| OOAD transformation: Derive frontend and backend systems     | yes                         | no                                          |
| OOAD transformation: Split system context into subsystems    | yes                         | no                                          |
| AR: "Split Aggregate by Entities"                            | yes                         | yes                                         |
| AR: "Split Bounded Context by Use Cases"                     | yes                         | yes                                         |
| AR: "Split Bounded Context by Owner"                         | yes                         | yes                                         |
| AR: "Extract Aggregates by Volatility"                       | yes                         | no                                          |
| AR: "Extract Aggregates by Cohesion"                         | yes                         | no                                          |
| AR: "Merge Aggregates"                                       | yes                         | no                                          |
| AR: "Merge Bounded Contexts"                                 | yes                         | no                                          |
| AR: "Extract Shared Kernel"                                  | yes                         | no                                          |
| AR: "Suspend Partnership"                                    | yes                         | no                                          |
| AR: "Change Shared Kernel to Partnership"                    | yes                         | no                                          |
| AR: "Change Partnership to Shared Kernel"                    | yes                         | no                                          |
