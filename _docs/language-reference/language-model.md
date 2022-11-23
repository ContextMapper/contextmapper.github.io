---
title: Language Semantics
permalink: /docs/language-model/
---

The CML language is based on the following strategic DDD domain model (or semantic model):

<a href="/img/Strategic_DDD_Domain_Model.png"><img src="/img/Strategic_DDD_Domain_Model.png" alt="CML Language Semantic Model" width="700px"></a>

The language representation of the DDD patterns is derived from the DDD books of Evans and Vernon:

 * ["Domain-Driven Design: Tackling Complexity in the Heart of Software"](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) by Eric Evans
 * ["Implementing Domain-Driven Design"](https://www.amazon.de/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577) by Vaughn Vernon
 * ["DDD Reference"](http://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) by Eric Evans

 The [Strategic Domain-Driven Design](https://socadk.github.io/design-practice-repository/activities/DPR-StrategicDDD.html) activity in the "Design Practice Repository" (by Olaf Zimmermann and Mirko Stocker) summarizes the relationship types.

## Semantic Rules
The following semantic rules are either implicitly given by the domain model on which the language is based (see above), or enforced by corresponding semantic checkers. 

Note that the model and the semantic rules express how we understand the DDD patterns and how they can be combined, and how we applied DDD on projects ourselves. 
Rationale: the literature is somewhat ambiguous.  

**\#1: Permitted Upstream Roles:**
The patterns OHS and PL can only be implemented by the upstream context in an upstream-downstream relationship. The upstream context always provides and exposes a certain 
functionality. The downstream context uses and consumes this services and does not expose parts of his/her own domain model. If this was the case and the upstream used this 
functionality, the definition that the upstream is independent of the downstream would be contradicted.

**\#2: Permitted Downstream Roles:**
The patterns ACL and CF can only be applied by the downstream context in an upstream-downstream relationship. These patterns solve a downstream problem, namely how to deal with
a dependency to another context. It is always the downstream context that has to integrate the upstream model.

**\#3: Protect or Conform:**
The patterns ACL and CF cannot be applied jointly, but provide alternatives. The downstream either conforms (CF) _or_ protects itself with an ACL.

**\#4: Integrity of Symmetric Relationships:**
The patterns OHS, PL, ACL and CF are not applicable in symmetric relationships (Partnership and Shared Kernel), since doing so would lead to contradictions with the pattern 
definitions. In a Shared Kernel relationship, the two contexts communicate over shared code such as a library. Both contexts manage the shared code together, which clearly 
contradicts with the mentioned four pattern definitions. An OHS indicates a directed provider/consumer behavior which is not the case here. There is no need for a common 
inter-context language (PL), since the two contexts simply share the same model. An ACL is not required either since the two participants share the model anyway. And neither 
context has to conform to the model of the other since it is one _shared_ model. In a Partnership relationship both contexts depend on each other, which means they can 
only succeed or fail together. 

**\#5: Customer vs. Conformist:**
The CF pattern is not applicable within a customer-supplier relationship. In a customer-supplier relationship the customer has influence on the supplier and can at least 
negotiate regarding priorities of the requirements and the implementation. A conformist in contrast has no influence and simply decides to conform to what the upstream provides.

**\#6: Generic vs. Custom Service:**
The OHS pattern is not applicable within a customer-supplier relationship. Whereas the customer-supplier pattern implies that the involved teams work closely together, meaning 
that the upstream respects the downstreams requirements in his planning sessions, the OHS pattern indicates that the upstream team decides to implement one API in a _one for all_ 
approach. This is contradictory since it is unlikely that such an upstream implementing an OHS is able to have a close customer-supplier relationship with all its downstreams. 
From personal practical experience a customer-supplier relationship leads to individual requirements of single customers. As soon as the supplier implements a customer-specific 
API feature it is by pattern definition no longer an OHS.

**\#7: Protect or Cooperate:**
The ACL pattern should not be used within a customer-supplier relationship. Changes of the supplier should be in-sync with the needs of the customer. Protection should be 
unnecessary. Note that this is only a _soft_ rule since the combination is possible but not common. Our tool issues a warning rather than an error message if it detects 
a violation of the rule. 

**\#8: *ORGANIZATIONAL* Context Maps:**
A context map of the type *ORGANIZATIONAL* (team map), can only contain bounded contexts of the type *TEAM*. This checker provides consistency within team maps. On such a map a 
bounded context represents a team and not a classical bounded context such as a system, feature or application.

**\#9: SYSTEM LANDSCAPES:**
A bounded context of the type *TEAM* can not be contained by a context map of the type *SYSTEM\_LANDSCAPE*. This checker provides consistency within context maps. 
Can be seen as the inverse case of rule \#8.

**\#10: Teams realize Bounded Contexts:**
Only teams can realize bounded contexts. This checker ensures that the *realize* keyword can only be used for bounded contexts of the type *TEAM*. 
The keyword is added to the language definition in order to reference the bounded contexts a team is realizing. It would not make sense for a classical bounded context 
(system, feature or application).

## Links
 * We presented the CML meta-model and the rules above in the following conference paper: 
   [Domain-specific Language and Tools for Strategic Domain-driven Design, Context Mapping and Bounded Context Modeling](https://doi.org/10.5220/0008910502990306)
