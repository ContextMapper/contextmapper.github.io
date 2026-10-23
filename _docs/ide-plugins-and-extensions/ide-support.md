---
title: Feature Support
permalink: /docs/ide/
image: /img/cm-og-image.png
---

Context Mapper is available for [Visual Studio Code](https://code.visualstudio.com/) and editors that support VS Code extensions:

 * [Context Mapper for VS Code](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension) (VS Code Marketplace)
 * [Context Mapper in the Open VSX Registry](https://open-vsx.org/extension/contextmapper/context-mapper-vscode-extension)

The Eclipse plugin is discontinued (last version: 6.12.0); see [Eclipse Plugin](/docs/eclipse/).

## Supported Features
The extension supports the following features:

| Feature                                                      | Supported in VS Code Extension              |
|--------------------------------------------------------------|---------------------------------------------|
| Editor: Syntax Highlighting                                  | yes                                         |
| Editor: Auto-completion                                      | yes                                         |
| Editor: Hover texts with pattern descriptions                | yes                                         |
| Editor: Semantic validators                                  | yes                                         |
| Graphical Context Map generator                              | yes                                         |
| PlantUML generator                                           | yes                                         |
| MDSL generator                                               | yes                                         |
| BPMN Sketch Miner generator                                  | yes                                         |
| Generic text file generator                                  | yes                                         |
| OOAD transformation: Derive Subdomain from user requirements | yes                                         |
| OOAD transformation: Derive Bounded Context from Subdomains  | yes                                         |
| OOAD transformation: Derive frontend and backend systems     | yes                                         |
| OOAD transformation: Split system context into subsystems    | yes                                         |
| Story splitting                                              | yes                                         |
| Stakeholder and value modelling transformations              | yes                                         |
| AR: "Split Aggregate by Entities"                            | yes                                         |
| AR: "Split Bounded Context by Features"                      | yes                                         |
| AR: "Split Bounded Context by Owner"                         | yes                                         |
| AR: "Extract Aggregates by Volatility"                       | yes                                         |
| AR: "Extract Aggregates by Cohesion"                         | yes                                         |
| AR: "Merge Aggregates"                                       | yes                                         |
| AR: "Merge Bounded Contexts"                                 | yes (with known limitation)                 |
| AR: "Extract Shared Kernel"                                  | yes                                         |
| AR: "Suspend Partnership"                                    | yes (with known limitation)                 |
| AR: "Change Shared Kernel to Partnership"                    | yes                                         |
| AR: "Change Partnership to Shared Kernel"                    | yes                                         |

The [Service Cutter](/docs/service-cutter-context-map-suggestions/) integration was removed in version 6.10.0.
