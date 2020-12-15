---
layout: news
title:  "Master Thesis Published"
author: Stefan Kapferer
---

The Context Mapper project is developed at [HSR](https://www.hsr.ch). The master thesis of Stefan Kapferer, **A Modeling Framework for Strategic Domain-driven Design and Service Decomposition**,
which presents the framework architecture behind Context Mapper has been published now.

## Abstract
The decomposition of a system into modules or services is a challenging practical problem and research question that has not been answered satisfactorily yet. 
With the current trend towards microservices, Strategic Domain-driven Design (DDD) has become a popular technique to decompose a domain into so-called Bounded Contexts. 
In our previous work we presented Context Mapper, an open source tool offering a Domain-specific Language (DSL) based on the DDD patterns. It supports the evolution of 
DDD pattern-based architecture models in a formal and expressive way. By applying Architectural Refactorings (ARs), systems can be decomposed in an iterative manner. However, 
our validation activities have shown that our tool-based approach requires additional capabilities to expand the target user group. For instance, support for reverse engineering 
has been requested since re-modeling existing systems is often too expensive in brownfield projects. Decomposition on the basis of a systematic approach and generating graphical 
Context Maps are other user requirements. 

With this thesis we propose a modular and extensible component architecture for a modeling framework based on Strategic DDD. The already 
existing Context Mapper tool evolved into a framework offering components for reverse engineering, architecture modeling, refactoring, systematic decomposition, and generation of 
other representations from the Context Mapper DSL (CML) models. The DSL constitutes the core component of the framework. With our discovery library we propose a strategy-based 
approach to reverse engineer CML models. An extended set of ARs has been conceptualized allowing users to evolve the architecture models iteratively. With Service Cutter, we 
integrated a systematic service decomposition approach to derive new Context Maps that improve coupling and cohesion. A graphical Context Map generator enhances the transformation 
tools to convert CML code into visual diagrams. 

The proposed framework supports architects and business analysts in creating DDD-based models and improve their productivity at the 
same time. We hypothesize that the mentioned personas can benefit from a tool which assists them in evolving Context Maps. During this thesis we applied action research to validate 
our concepts and improve the prototype iteratively. With case studies such as the Lakeside Mutual microservice project and our own framework architecture we validated the usefulness 
and effectiveness of the suggested modeling framework. The conducted validation activities indicate that the hypothesis above holds true.

## Full report
The full master thesis report can be found here: [https://eprints.hsr.ch/821/](https://eprints.hsr.ch/821/)
