---
layout: post
title:  "A Domain-specific Language for Service Decomposition"
author: Stefan Kapferer
---

The Context Mapper project has been developed in a term project at [HSR](https://www.hsr.ch). The project report with details and further 
background information about the project, **A Domain-specific Language for Service Decomposition**, has been published and can be 
downloaded [here](https://eprints.hsr.ch/722/).

## Abstract
Microservices have gained a huge attention in the industry and in the academic field over the last years. Companies are adopting microservice architectures in order to increase agility, maintainability and scalability of their software. At the same time, decomposing an application into appropriately sized services is challenging. With its strategic patterns and especially the Bounded Contexts, Domain-driven Design (DDD) provides an approach for decomposing a domain into multiple independently deployable services. However, existing modeling tools supporting DDD mainly focus on the tactical patterns. Not many approaches to a formal definition of the strategic patterns exist and there are different interpretations and opinions regarding their applicability.

This project presents a Domain-specific Language (DSL) based on the strategic DDD patterns. The model behind the language and its semantic rules aim to provide one concise interpretation of the patterns and how they can be combined. The DSL concept offers a tool to model a system in an expressive way, using the DDD language. With the implemented Service Cutter integration we further provide a proof of concept showing how the DSL can be used as input for structured service decomposition approaches. The presented results and our evaluation of this approach illustrate the capabilities of DDD-based models towards service decomposition. To convert the DSL-based models into a graphical representation, the developed tool offers an additional transformation to create PlantUML diagrams.

The DSL is meant to provide a foundation for other service decomposition approaches. Future projects may propose architectural refactorings for the DSL based on model transformations. Other approaches based on algorithms and heuristics similar to Service Cutter could be applied as well. A code generator to create microservice project templates for the modeled Bounded Contexts might be another promising feature for the future.

## Full report
The full project report can be found here: [https://eprints.hsr.ch/722/](https://eprints.hsr.ch/722/)
