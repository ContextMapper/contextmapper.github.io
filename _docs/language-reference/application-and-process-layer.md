---
title: Application and Process Layer
permalink: /docs/application-and-process-layer/
---

The original ["blue book"](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) (by Evans) as well as the ["red book"](https://www.amazon.com/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577) (by Vernon) talk about domain and application layers. Although Context Mapper is focused on strategic DDD and domain models (domain layer) inside Bounded Contexts, we support modeling services, commands, and events in an application layer. With the application layer concept in CML users have the possibility to declare which services and/or commands can be called/triggered from outside a Bounded Context and which events are published to the outside. 

In addition to that, the application layer offers a basic syntax to model processes or event/command flows. This can, for example, be helpful to bring events and commands (maybe outcome of an [Event Storming](/docs/event-storming/)) into a timeline and explicitly state which event are emitted by which commands (or service operations) and which commands are triggered by events.

The application layer also provides an alternative way to model processes without relying on event/command syntax. This is achieved by defining a coordination between service operations.

## Application Services and Commands
DDD practitioners and experts typically distinguish between domain services and application services. Therefore, CML offers the possibility to use the _service_ construct both inside Aggregates (domain service) and inside the _application_ layer (application service). Note that the grammar/syntax for application services is exactly the same as for the [services inside the Aggregates](/docs/tactic-ddd/#services).

The following example illustrates how to model an application layer in a Bounded Context and add application services:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> ClaimsManagement {
  <span class="k">Application</span> {
    <span class="k">Service</span> ClaimsApplicationService {
      <span class="k">void</span> submitClaim(@Claim claim);
      <span class="k">void</span> checkInsurance(@Claim claim);
      <span class="k">void</span> acceptClaim(@Claim claim);
      <span class="k">void</span> rejectClaim(@Claim claim);
    }
  }
  
  <span class="k">Aggregate</span> Claims {
    <span class="k">Entity</span> Claim {
      <span class="k">aggregateRoot</span>
      <span class="k">long</span> claimId
      CustomerId <span class="k">customer</span>
      <span class="k">String</span> description
      <span class="k">Blob</span> requestDocument
      <span class="k">boolean</span> isComplete
      <span class="k">boolean</span> isAssessed
      - <span class="k">ClaimState</span> claimState
    }
    <span class="k">enum</span> ClaimState {
      <span class="k">aggregateLifecycle</span>
      OPEN, REJECTED, ACCEPTED
    }
    
    <span class="k">abstract</span> <span class="k">DomainEvent</span> ClaimEvent {
      <span class="k">long</span> claimId
      <span class="k">Date</span> timestamp
    }
    <span class="k">DomainEvent</span> ClaimSubmitted <span class="k">extends</span> ClaimEvent
    <span class="k">DomainEvent</span> ClaimAccepted <span class="k">extends</span> ClaimEvent
    <span class="k">DomainEvent</span> ClaimRejected <span class="k">extends</span> ClaimEvent
  }
}
</pre></div>

Optionally, it is possible to name the application layer:

<div class="highlight"><pre><span></span><span class="k">Application</span> ClaimsApplicationLayer {
  <span class="k">Service</span> ClaimsApplicationService {
    <span class="k">void</span> submitClaim(@Claim claim);
    <span class="k">void</span> checkInsurance(@Claim claim);
    <span class="k">void</span> acceptClaim(@Claim claim);
    <span class="k">void</span> rejectClaim(@Claim claim);
  }
}
</pre></div>

As documented on the [Aggregate page](/docs/aggregate/#aggregate-lifecycle-and-state-transitions), it is also possible to specify state transitions made by operations. Please consult the Aggregate documentation for the syntax of state transitions. The same syntax is available for the operations of application services:

<div class="highlight"><pre><span></span><span class="k">Application</span> {
  <span class="k">Service</span> ClaimsApplicationService {
    <span class="k">void</span> submitClaim(@Claim claim) : <span class="k">write</span> [ -&gt; OPEN];
    <span class="k">void</span> checkInsurance(@Claim claim);
    <span class="k">void</span> acceptClaim(@Claim claim) : <span class="k">write</span> [ OPEN -&gt; ACCEPTED ];
    <span class="k">void</span> rejectClaim(@Claim claim) : <span class="k">write</span> [ OPEN -&gt; REJECTED ];
  }
}
</pre></div>

_Hint:_ If you model processes/flows (see documentation of syntax below) you may want to declare the state transitions in the flow steps instead of service operations.

As an alternative to "service operations" you can also create semantically equivalent commands and events in the application layer; maybe you work with [Event Sourcing and/or CQRS](/docs/event-sourcing-and-cqrs-modeling/), and these terms fit better.

The syntax for domain events and commands is documented on the [tactic DDD reference page](/docs/tactic-ddd/#domain-events). The following example illustrates how you can use those concepts in the application layer as well:

<div class="highlight"><pre><span></span><span class="k">Application</span> {
  <span class="k">Command</span> SubmitClaim {
    <span class="c">// attributes/body optional</span>
  }
  <span class="k">Command</span> AcceptClaim
  <span class="k">Command</span> RejectClaim
  
  <span class="k">Event</span> ClaimSubmitted {
    <span class="c">// attributes/body optional</span>
  }
  <span class="k">Event</span> ClaimAccepted
  <span class="k">Event</span> ClaimRejected
}
</pre></div>

_Hint:_ Modeling commands that are triggered by users or external systems in the application layer may feel natural. Events, however, may be part of your [domain model](https://github.com/socadk/design-practice-repository/blob/master/artifact-templates/DPR-DomainModel.md). Therefore you should decide consciously whether you want to model these events on the application layer or inside the corresponding domain layer Aggregate.

## Processes and Event/Command Flows
In addition to application services and commands, the application layer offers language features to model event/command flows. Events typically occur in a certain order over time. For example in [Event Stormings](/docs/event-storming/) Events are typically ordered by the timeline from left to right. An example: (from our [Event Storming tutorial](/docs/event-storming/))

<a target="_blank" href="/img/lakeside-mutual-event-storming-result.jpg">![Lakeside Mutual Claim Processing Event Storming](/img/lakeside-mutual-event-storming-result.jpg)</a>

Our flow grammar supports Context Mapper users in modeling such event/command flows in CML. The following example models the event storming result illustrated above:

<div class="highlight"><pre><span></span><span class="k">Application</span> {

  <span class="c">/* we removed commands and events here to keep the sample shorter */</span>

  <span class="k">Flow</span> ClaimsFlow {
    <span class="k">command</span> SubmitClaim <span class="k">emits</span> <span class="k">event</span> ClaimSubmitted
    <span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">command</span> CheckClaimDocumentation
    <span class="k">command</span> CheckClaimDocumentation <span class="k">emits</span> <span class="k">event</span> ClaimRegistered
    <span class="k">event</span> ClaimRegistered <span class="k">triggers</span> <span class="k">command</span> CheckInsurance
    <span class="k">command</span> CheckInsurance <span class="k">emits</span> <span class="k">event</span> AssessmentPerformed

    <span class="k">event</span> AssessmentPerformed <span class="k">triggers</span> <span class="k">command</span> AcceptClaim <span class="k">X</span> RejectClaim 
    <span class="k">command</span> AcceptClaim <span class="k">delegates</span> <span class="k">to</span> Claims [OPEN -&gt; ACCEPTED] <span class="k">emits</span> <span class="k">event</span> ClaimAccepted
    <span class="k">command</span> RejectClaim <span class="k">delegates</span> <span class="k">to</span> Claims [OPEN -&gt; REJECTED] <span class="k">emits</span> <span class="k">event</span> ClaimRejected

    <span class="k">event</span> ClaimAccepted <span class="k">triggers</span> <span class="k">command</span> SchedulePayment
    <span class="k">command</span> SchedulePayment <span class="k">emits</span> <span class="k">event</span> PaymentPerformed
    <span class="k">event</span> PaymentPerformed <span class="k">triggers</span> <span class="k">command</span> NofifyCustomer
    <span class="k">event</span> ClaimRejected <span class="k">triggers</span> <span class="k">command</span> NofifyCustomer
    <span class="k">command</span> NofifyCustomer <span class="k">delegates</span> <span class="k">to</span> Claims [ACCEPTED, REJECTED -&gt; CUSTOMER_NOTIFIED] <span class="k">emits</span> <span class="k">event</span> CustomerNotified
  }
}
</pre></div>

The example above works with commands. It is however possible to model the same flow with service operations:

<div class="highlight"><pre><span></span><span class="k">Application</span> {
  <span class="k">Service</span> ClaimsApplicationService {
    <span class="k">void</span> submitClaim(@Claim claim);
    <span class="k">void</span> checkClaimDocumentation(@Claim claim);
    <span class="k">void</span> checkInsurance(@Claim claim);
    <span class="k">void</span> acceptClaim(@Claim claim);
    <span class="k">void</span> rejectClaim(@Claim claim);
    <span class="k">void</span> schedulePayment(@Claim claim);
    <span class="k">void</span> nofifyCustomer(@Claim claim);
  }
  
  <span class="k">Flow</span> ClaimsFlow {
    <span class="k">operation</span> submitClaim <span class="k">emits</span> <span class="k">event</span> ClaimSubmitted
    <span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">operation</span> checkClaimDocumentation
    <span class="k">operation</span> checkClaimDocumentation <span class="k">emits</span> <span class="k">event</span> ClaimRegistered
    <span class="k">event</span> ClaimRegistered <span class="k">triggers</span> <span class="k">operation</span> checkInsurance
    <span class="k">operation</span> checkInsurance <span class="k">emits</span> <span class="k">event</span> AssessmentPerformed
    
    <span class="k">event</span> AssessmentPerformed <span class="k">triggers</span> <span class="k">operation</span> acceptClaim <span class="k">X</span> rejectClaim 
    <span class="k">operation</span> acceptClaim <span class="k">delegates</span> <span class="k">to</span> Claims [OPEN -&gt; ACCEPTED] <span class="k">emits</span> <span class="k">event</span> ClaimAccepted
    <span class="k">operation</span> rejectClaim <span class="k">delegates</span> <span class="k">to</span> Claims [OPEN -&gt; REJECTED] <span class="k">emits</span> <span class="k">event</span> ClaimRejected
    
    <span class="k">event</span> ClaimAccepted <span class="k">triggers</span> <span class="k">operation</span> schedulePayment
    <span class="k">operation</span> schedulePayment <span class="k">emits</span> <span class="k">event</span> PaymentPerformed
    <span class="k">event</span> PaymentPerformed <span class="k">triggers</span> <span class="k">operation</span> nofifyCustomer
    <span class="k">event</span> ClaimRejected <span class="k">triggers</span> <span class="k">operation</span> nofifyCustomer
    <span class="k">operation</span> nofifyCustomer <span class="k">delegates</span> <span class="k">to</span> Claims[ACCEPTED, REJECTED -&gt; CUSTOMER_NOTIFIED] <span class="k">emits</span> <span class="k">event</span> CustomerNotified
  }
}
</pre></div>

In the following we explain the grammar in detail and step by step...

### Flow Grammar
There are basically two types of flow steps that are supported by CML:

 * _Type 1:_ an event triggers an operation/command (_command/operation invocation_)
 * _Type 2:_ a command/operation emits an event (_event production_)

These types of steps are inspired by the [Event Storming Cheat sheet of the DDD crew](https://github.com/ddd-crew/eventstorming-glossary-cheat-sheet), the following illustration in particular:

<a href="https://github.com/ddd-crew/eventstorming-glossary-cheat-sheet" target="_blank">![Event Storming Picture](https://raw.githubusercontent.com/ddd-crew/eventstorming-glossary-cheat-sheet/master/resources/software-picture.jpg)</a>

_Note:_ We do not support all of the concepts illustrated above! Especially policies and the "query model / information" sticky are not supported explicitly.

The picture above illustrates the two main step types mentioned above.

 * _Type 1:_ an event _triggers_ (the DDD crew uses the term _issues_) a command (in CML without the policy in between)
 * _Type 2:_ a command (CML: or operation) _invoked on an_ Aggregate _emits_ (the DDD crew uses the term _produces_) an event

In the following we will see that we also support the Aggregate in _Type 2_; the _actor_ that can trigger a command/operation.

The following example illustrates the basic syntax of the two step types:

<div class="highlight"><pre><span></span><span class="k">Application</span> {

  <span class="c">/* we removed commands and events here to keep the sample shorter */</span>

  <span class="k">Flow</span> ClaimsFlow {
    <span class="c">/* type 2: (event production) */</span>
    <span class="k">command</span> SubmitClaim <span class="k">emits</span> <span class="k">event</span> ClaimSubmitted

    <span class="c">/* type 2 alternative: (event production) */</span>
    <span class="k">operation</span> submitClaim <span class="k">emits</span> <span class="k">event</span> ClaimSubmitted

    <span class="c">/* type 1: (command invokation) */</span>
    <span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">command</span> CheckClaimDocumentation

    <span class="c">/* type 1 alternative: (operation invokation) */</span>
    <span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">operation</span> checkClaimDocumentation
  }
}
</pre></div>

#### Emitting Events
A command or operation can emit multiple events. This is expressed with the _+_ sign as follows:

<div class="highlight"><pre><span></span><span class="k">command</span> SubmitClaim <span class="k">emits</span> <span class="k">event</span> Event1 + Event2 + Event3 <span class="c">// and so on... (emit as many events as you want)</span>

<span class="c">// alternative</span>
<span class="k">operation</span> submitClaim <span class="k">emits</span> <span class="k">event</span> Event1 + Event2
</pre></div>

The example above illustrates that an operation emits **multiple** events events, which means, **all events are emitted**!

There are situations in which you want to express that **one OR an other** event is emitted. In this case, we distinguish between exclusive OR (XOR: only one of the listed events is emitted) and inclusive OR (multiple events can be thrown, but not necessarily all). For these two cases we use the symbols _X_ and _O_, inspired by [BPMN](https://www.signavio.com/de/bpmn-einfuehrung/).

**Exclusive variant:**

<div class="highlight"><pre><span></span><span class="k">command</span> SubmitClaim <span class="k">emits</span> <span class="k">event</span> Event1 <span class="k">X</span> Event2 <span class="k">X</span> Event3

<span class="c">// alternative</span>
<span class="k">operation</span> submitClaim <span class="k">emits</span> <span class="k">event</span> Event1 <span class="k">X</span> Event2
</pre></div>

**Inclusive variant:**

<div class="highlight"><pre><span></span><span class="k">command</span> SubmitClaim <span class="k">emits</span> <span class="k">event</span> Event1 <span class="k">O</span> Event2 <span class="k">O</span> Event3

<span class="c">// alternative</span>
<span class="k">operation</span> submitClaim <span class="k">emits</span> <span class="k">event</span> Event1 <span class="k">O</span> Event2
</pre></div>

**Symbol Summary:**

The following table summarizes the three symbols that are supported here:

| Symbol         | Meaning                                                                        | Corresponding BPMN gateways (in German)                                                 |
|----------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| **+**          | **ALL** listed events are emitted.                                             | [Parallel Gateway](https://www.signavio.com/de/bpmn-einfuehrung/#Parallele-Gateways)  |
| **X** or **x** | **ONLY ONE** of the listed events is emitted.                                  | [Exclusive Gateway](https://www.signavio.com/de/bpmn-einfuehrung/#Exklusive-Gateways) |
| **O** or **o** | **ONE OR MULTIPLE, BUT NOT NECESSARILY ALL** of the listed events are emitted. | [Inclusive Gateway](https://www.signavio.com/de/bpmn-einfuehrung/#Inklusive-Gateways) |

_Note:_ It is not possible to mix the symbols inside a single flow step (we do not implement operator precedence).

#### Command/Operation triggered by multiple Events
On the other hand a command or operation may only be triggered if multiple events happen. This is modelled as follows:

<div class="highlight"><pre><span></span><span class="k">event</span> ClaimSubmitted + ContractChecked <span class="k">triggers</span> <span class="k">command</span> AssessClaim

<span class="c">// alternative</span>
<span class="k">event</span> ClaimSubmitted + ContractChecked <span class="k">triggers</span> <span class="k">operation</span> assessClaim
</pre></div>

This example expresses that both events (_ClaimSubmitted_ as well as _ContractChecked_) _must_ have been emitted so that _AssessClaim_ is triggered.

_Note:_ At this point only the _+_ symbol is supported.

#### Triggering Commands/Operations
Similar to the _event productions_ explained above, it is possible that events trigger multiple commands/operations. This syntax works with the symbols _+_, _X_, and _O_ again.

**Parallel variant:**

<div class="highlight"><pre><span></span><span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">command</span> CheckClaim + CheckPolicy

<span class="c">// operation alternative:</span>
<span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">operation</span> checkClaim + checkPolicy
</pre></div>

This example expresses that all listed operations/commands are triggered (parallel).

**Exclusive variant:**

<div class="highlight"><pre><span></span><span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">command</span> CheckClaim <span class="k">X</span> CheckPolicy

<span class="c">// operation alternative:</span>
<span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">operation</span> checkClaim <span class="k">X</span> checkPolicy
</pre></div>

This example means that only one of the commands/operations is triggered.

**Inclusive variant:**

<div class="highlight"><pre><span></span><span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">command</span> CheckClaim <span class="k">O</span> CheckPolicy

<span class="c">// operation alternative:</span>
<span class="k">event</span> ClaimSubmitted <span class="k">triggers</span> <span class="k">operation</span> checkClaim <span class="k">O</span> checkPolicy
</pre></div>

This example expresses that one or multiple but not necessarily all commands/operations are triggered.

**Symbol summary:**

The following table summarizes the meaning of the supported symbols in the _command/operation invokation_ steps:

| Symbol         | Meaning                                                                                       | Corresponding BPMN gateways                                                           |
|----------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| **+**          | **ALL** listed commands/operations are triggered.                                             | [Parallel Gateway](https://www.signavio.com/de/bpmn-einfuehrung/#Parallele-Gateways)  |
| **X** or **x** | **ONLY ONE** of the listed commands/operations is triggered.                                  | [Exclusive Gateway](https://www.signavio.com/de/bpmn-einfuehrung/#Exklusive-Gateways) |
| **O** or **o** | **ONE OR MULTIPLE, BUT NOT NECESSARILY ALL** of the listed commands/operations are triggered. | [Inclusive Gateway](https://www.signavio.com/de/bpmn-einfuehrung/#Inklusive-Gateways) |

#### Commands/Operations delegating to Aggregates
Commands and operations are typically delegated to an Aggregate. This also corresponds to the illustration of the [DDD crew](https://github.com/ddd-crew/eventstorming-glossary-cheat-sheet) depicted above.

In CML this means that you can optionally add the following reference to _event production_ steps (_Type 2_ above):

<div class="highlight"><pre><span></span><span class="k">command</span> SubmitClaim <span class="k">delegates</span> <span class="k">to</span> Claims <span class="k">emits</span> <span class="k">event</span> Event1 <span class="k">X</span> Event2 <span class="k">X</span> Event3

<span class="c">// alternative</span>
<span class="k">operation</span> submitClaim <span class="k">delegates</span> <span class="k">to</span> Claims <span class="k">emits</span> <span class="k">event</span> Event1 <span class="k">X</span> Event2
</pre></div>

Note that this is a reference to an Aggregate that must actually exist in your Bounded Context. In the example above there must be an Aggregate called _Claims_ in the same Bounded Context.

#### State Transitions
In case your flow step delegates to an Aggregate (contains part _delegates to_) as in the example above, it is possible to declare the state transition that is caused right here.

_Note:_ State transition can be modelled on service and domain object operations as [documented on the Aggregate doc page](/docs/aggregate/#aggregate-lifecycle-and-state-transitions).

If you use flows you can add the state transitions to the flow steps instead of modeling them inside the Aggregate (operations). The state transitions can be added to the _event production_ steps (_type 2_ above) as follows (optionally):

<div class="highlight"><pre><span></span><span class="k">command</span> SubmitClaim <span class="k">delegates</span> <span class="k">to</span> Claims [ -&gt; SUBMITTED ] <span class="k">emits</span> <span class="k">event</span> Event1 <span class="k">X</span> Event2 <span class="k">X</span> Event3

<span class="c">// alternative</span>
<span class="k">operation</span> submitClaim <span class="k">delegates</span> <span class="k">to</span> Claims [ -&gt; SUBMITTED ] <span class="k">emits</span> <span class="k">event</span> Event1 <span class="k">X</span> Event2
</pre></div>

For a complete documentation and examples for the state transition grammar we refer to the [Aggregate page](/docs/aggregate/#aggregate-lifecycle-and-state-transitions).

#### Actors
Commands or operations can be triggered by actors/users. In CML you can specify this (optionally) as follows:

<div class="highlight"><pre><span></span><span class="k">command</span> SubmitClaim [ <span class="k">initiated</span> <span class="k">by</span> <span class="s">&quot;Customer&quot;</span> ] <span class="k">delegates</span> <span class="k">to</span> Claims [ -&gt; SUBMITTED ] <span class="k">emits</span> <span class="k">event</span> Event1

<span class="c">// alternative</span>
<span class="k">operation</span> submitClaim [ <span class="k">initiated</span> <span class="k">by</span> <span class="s">&quot;Customer&quot;</span> ] <span class="k">delegates</span> <span class="k">to</span> Claims [ -&gt; SUBMITTED ] <span class="k">emits</span> <span class="k">event</span> Event1
</pre></div>

### Visualization with BPMN Sketch Miner
Once you modelled an application flow you can visualize it in the [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/). Use Context Mapper's [BPMN Sketch Miner generator](/docs/bpmn-sketch-miner/) to generate the Sketch Miner DSL output or directly open the visualization in the browser. 

An example output: (visualization powered by [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/))

![BPMN Sketch Miner Example](/img/bpmn-sketch-miner-example-1.png)

_Note:_ This is a process we took (modeled) from the [Lakeside Mutual project](https://github.com/Microservice-API-Patterns/LakesideMutual).

## Coordination between Application Services
In case you want to model processes/workflows that span multiple Bounded Contexts without the use of event/command syntax, you can also do so by defining a coordination between application services. This language feature is based on the concept of Coordination from the ["Software Architecture: The Hard Parts"](https://www.amazon.com/Software-Architecture-Trade-Off-Distributed-Architectures/dp/1492086894) book by Neal Ford and others. They define Coordination as a property of workflows, which can either be orchestrated (the workflow steps are coordinated by a central component) or choreographed (each step of the workflow shares coordination logic).

To model these workflows in Context Mapper, you use the _coordination_ construct inside the _application_ layer of a Bounded Context. The following example illustrates this using an adaptation of the same claims processing concept from before:

<div class="highlight"><pre><span></span><span class="k">ContextMap</span> {
  <span class="k">contains</span> ClaimsManagement
  <span class="k">contains</span> InsuranceManagement
  <span class="k">contains</span> PaymentManagement

  ClaimsManagement &lt;-&gt; InsuranceManagement
  ClaimsManagement &lt;-&gt; PaymentManagement
}

<span class="k">BoundedContext</span> ClaimsManagement {
  <span class="k">Application</span> {
    <span class="k">Coordination</span> SubmitValidClaimCoordination {
      ClaimsManagement::ClaimsApplicationService::submitClaim;
      InsuranceManagement::InsuranceApplicationService::checkInsurance;
      ClaimsManagement::ClaimsApplicationService::acceptClaim;
      PaymentManagement::PaymentApplicationService::performPayment;
    }

    <span class="k">Service</span> ClaimsApplicationService {
      <span class="k">void</span> submitClaim(@Claim claim);
      <span class="k">void</span> acceptClaim(@Claim claim);
    }
  }
}

<span class="k">BoundedContext</span> InsuranceManagement {
  <span class="k">Application</span> {
    <span class="k">Service</span> InsuranceApplicationService {
      <span class="k">void</span> checkInsurance(@Claim claim);
    }
  }
}

<span class="k">BoundedContext</span> PaymentManagement {
  <span class="k">Application</span> {
    <span class="k">Service</span> PaymentApplicationService {
      <span class="k">void</span> performPayment(@Claim claim);
    }
  }
}

</pre></div>

_Note:_ The type of workflow coordination (orchestration or choreography) is not explicitly supported in the syntax, but can still be modeled by assuming that the Bounded Context where the coordination is defined serves as either the orchestrator, or the start of the choreography.

### Coordination Grammar
In CML, coordinations are composed of coordination steps. Each coordination step represents a call to an application service operation, which can be defined inside the same Bounded Context or in an outer Bounded Context.

To correctly reference an application service operation, a coordination step is divided into three segments, separated by the `::` symbol:

 *  The name of the Bounded Context where the operation is defined;
 *  The name of the application service where the operation is defined;
 *  And the name of the operation.

The following is an example of a coordination step:

<div class="highlight"><pre><span></span><span class="c">// Bounded context name :: application service name :: service operation name</span>
ClaimsManagement::ClaimsApplicationService::submitClaim;

</pre></div>

Each of the three segments of a coordination step is also subject to certain syntax rules to maintain the integrity of the model. Respectively, these are:

 *  A coordination step can only reference outer Bounded Contexts that are upstream (by means of an upstream/downstream relationship or a symmetrical relationship in a Context Map definition);
 *  A coordination step can only reference services defined in the application layer of a Bounded Context (which means domain services defined inside aggregates are not applicable);
 *  A reference to a service operation in a coordination step should be unique within the service.

### Coordination visualization in BPMN
Like flows, coordinations can also be visualized with [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/). The following example shows the output when using Context Mapper’s [BPMN Sketch Miner generator](/docs/bpmn-sketch-miner/) on coordinations:

![BPMN Sketch Miner Example](/img/bpmn-sketch-miner-example-2.png)
