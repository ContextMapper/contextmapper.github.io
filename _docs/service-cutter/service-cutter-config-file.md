---
title: Service Cutter Configuration File (.servicecutter.yml)
permalink: /docs/service-cutter-config-file/
---

<div class="alert alert-danger">
<strong>Note:</strong> This feature has been <strong>deactivated</strong> with <a href="https://contextmapper.org/news/2023/11/24/v6.10.0-released/">release v6.10.0</a> of Context Mapper.
</div>

Context Mapper uses [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/) to [propose new Context Maps (service decompositions)](/docs/service-cutter-context-map-suggestions/). There is also a [tutorial](/docs/systematic-service-decomposition/) that explains how this works.

However, since we do not provide a user interface to configure the coupling criteria priorities as the original [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/) tool does, we provide a file called `.servicecutter.yml` that allows you to configure the service cutting engine.

The file is automatically generated into your project root directory once you call the [Propose New Service Cut](/docs/service-cutter-context-map-suggestions/) generator.

Initially, the files looks as follows:

```yaml
algorithm: MARKOV_CLUSTERING
algorithmParams:
  mclExpansionOperations: 2.0
  mclPowerCoefficient: 2.0
  leungM: 0.1
  leungDelta: 0.55
  cwNodeWeighting: 0.0
priorities:
  Identity & Lifecycle Commonality: M
  Security Constraint: M
  Storage Similarity: XS
  Security Criticality: XS
  Latency: M
  Structural Volatility: XS
  Consistency Criticality: XS
  Predefined Service Constraint: M
  Availability Criticality: XS
  Semantic Proximity: M
  Consistency Constraint: M
  Shared Owner: M
  Content Volatility: XS
  Security Contextuality: M
```

## Changing the Algorithm
The `algorithm` property allows you to change the graph clustering algorithm that is used. We currently support the following three algorithms:

 * [Markov Clustering (MCL)](https://www.micans.org/mcl/): `MARKOV_CLUSTERING` (default)
 * [Epidemic Label Propagation (Leung)](https://arxiv.org/abs/0808.2633): `LEUNG`
 * [Chinese Whispers](https://dl.acm.org/doi/10.5555/1654758.1654774): `CHINESE_WHISPERS`

Note that that _LEUNG_ and _CHINESE_WHISPERS_ produce randomized results. That means that you get different results each time you generate a new service cut.

## Algorithm Parameters
The `algorithmParams` property allows users to change parameters of the clustering algorithms. The properties use the following prefixes:

 * **mcl**: [Markov Clustering (MCL)](https://www.micans.org/mcl/) parameters
 * **leung**: [Epidemic Label Propagation (Leung)](https://arxiv.org/abs/0808.2633) parameters
 * **cw**: [Chinese Whispers](https://dl.acm.org/doi/10.5555/1654758.1654774) parameters

We do however not provide a detailed documentation of the individual parameters here. In case you really want to change them, which should not be necessary (we use recommended default values), we refer to the documentation of the algorithms themselves.

## Criteria Priorities
The `priorities` property allows you to influence the scoring mechanism of Service Cutter. The priorities can be set to the same values that are supported by the [Service Cutter](https://github.com/ServiceCutter/ServiceCutter/) user interface:

 * _IGNORE_
 * _XS_
 * _S_
 * _M_
 * _L_
 * _XL_
 * _XXL_

The available criteria come from [Service Cutter's criteria catalog](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria).
