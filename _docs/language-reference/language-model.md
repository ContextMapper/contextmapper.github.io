---
title: Language Semantics
permalink: /docs/language-model/
---

The CML language is based on the following strategic DDD domain model (or semantic model):

<a href="/img/Strategic_DDD_Domain_Model.png"><img src="/img/Strategic_DDD_Domain_Model.png" alt="CML Language Semantic Model" width="700px"></a>

The language representation of the DDD patterns is derived from Evan's DDD book and DDD reference:

 * [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)
 * [DDD Reference](http://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)

<!-- How about the I-DDD book by VV (mentioned in papers, thesis)? Other sources? -->

<!-- skipped rest of file in review; please "retrofit" latest paper/thesis version -->
## Semantic Rules
The following semantic rules are either implicitly given by the domain model on which the language is based (see above), or enforced by corresponding semantic checkers. 

Note that the model and the semantic rules express how we understand the DDD patterns and how they can be combined, and how we applied DDD on projects ourselves. Rationale: the literature is somewhat ambiguous.  

**\#1: The relationship patterns Open Host Service (OHS), Published Language, Anticorruption Layer (ACL) and Conformist are not applicable for Partnership and Shared Kernel relationships.**
A violation of this rule would lead to contradictions regarding the definitions of the patterns and how we understand them. In a Shared Kernel relationship, two bounded contexts share a subset of its domain model and thus, technically, share code. The interaction between the two bounded contexts happens via this shared code. The usage of the four mentioned patterns contradicts with this approach. The same applies to the very tightly coupled Partnership pattern. Even if the contexts do not share code, the two contexts can only succeed or fail together.

**\#2: The patterns Open Host Service (OHS) and Published Language can only be implemented by the upstream in an upstream/downstream relationship.**
Trivially given by the definition of these patterns. Applying them to the downstream does not make sense, since the downstream context is calling the upstream context.

**\#3: The relationship patterns ACL and Conformist can only be implemented by the downstream context in an upstream/downstream relationship.**
Trivially given by the definition of these patterns. Applying them to the upstream does not make sense, since the upstream context is one who is called by the downstream. The upstream itself does not depend on the downstream and therefore does not have to conform or protect itself from changes of the downstream.

**\#4: The Conformist pattern is not applicable within a customer/supplier relationship.**
In a customer/supplier relationship, the customer has an influence on the supplier and can at least negotiate regarding priorities of the requirements and the implementation. A conformist in contrast has no possibilities to influence the upstream and has to conform to what he gets.

**\#5: The Open Host Service (OHS) pattern is not applicable within a customer/supplier relationship.**
Whereas the customer/supplier pattern implies that the two involved teams work closely together, meaning that the downstream team delivers the input in the upstreams planning sessions, the OHS pattern is meant to be applied if an upstream is used by many downstreams and the upstream team decides to implement one API in an «one for all» approach. This is somehow contradictory since it is unlikely that such an upstream implementing an OHS is able to have a close customer/supplier relationship with all its downstreams and fulfill all their expectations at the same time.

**\#6: The Anticorruption Layer (ACL) pattern should not be needed within a customer/supplier relationship. Note: This checker only produces a compiler warning, not an error.**
Similarly as in rule \#2 the application of the ACL pattern is contradictory with the close customer/supplier relationship, where it should not be the case that the supplier implements changes from which the downstream has to protect itself. However, we only produce a warning questioning this situation since one might argue that a translation layer can be needed anyway and the difference between a translation layer and an anticorruption layer is not clearly defined or depends on how defensive it is implemented.

**\#7: A bounded context which is not contained by the context map can not be part of a relationship either.**
This checker provides consistency within the generated model.

**\#8: A context map of the type *ORGANIZATIONAL* (team map), can only contain bounded contexts of the type *TEAM*.**
This checker provides consistency within team maps. On such a map a bounded context represents a team and not a classical bounded context such as a system, feature or application.

**\#9: A bounded context of the type *TEAM* can not be contained by a context map of the type *SYSTEM\_LANDSCAPE*.**
This checker provides consistency within context maps. Can be seen as the inverse case of rule \#5.

**\#10: Only teams can realize bounded contexts.**
This checker ensures that the *realize* keyword can only be used for bounded contexts of the type *TEAM*. The keyword is added to the language definition in order to reference the bounded contexts a team is realizing. It would not make sense for a classical bounded context (system, feature or application).
