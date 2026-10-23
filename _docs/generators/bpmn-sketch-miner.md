---
title: BPMN Sketch Miner Generator
permalink: /docs/bpmn-sketch-miner/
---

## Introduction and Motivation
We use the [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/) tool to visualize [event/command flows in our application layers](/docs/application-and-process-layer/#processes-and-eventcommand-flows). You can model flows (for example, as resulting from an [Event Storming](/docs/event-storming/) workshop) in the CML application layer of a Bounded Context and then generate the [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/) DSL or directly open the tool from Context Mapper.

## Example Flow
The following CML code illustrates how you can model flows. A complete documentation on the syntax can be found in the [language reference](/docs/application-and-process-layer/#processes-and-eventcommand-flows).

```cml
/**
 * A flow inspired by the Lakeside Mutual project (https://github.com/Microservice-API-Patterns/LakesideMutual).
 * Find the original process visualization here:
 * https://github.com/Microservice-API-Patterns/LakesideMutual/blob/master/policy-management-backend/src/main/java/com/lakesidemutual/policymanagement/domain/insurancequoterequest/RequestStatus.java
 **/
BoundedContext InsuranceQuotes {
  Application {
    Flow QuoteRequestFlow {
      operation submitRequest delegates to QuoteRequest[-> SUBMITTED] emits event RequestSubmitted
      event RequestSubmitted + RequestSubmitted triggers operation checkRequest
      operation checkRequest delegates to QuoteRequest[SUBMITTED -> RECEIVED X REJECTED] emits event QuoteReceived X RequestRejected
      event QuoteReceived triggers operation receiveAndCheckQuote
      operation receiveAndCheckQuote delegates to QuoteRequest[RECEIVED -> REJECTED X ACCEPTED X EXPIRED] emits event QuoteRejected X QuoteAccepted X QuoteExpired
      event QuoteAccepted triggers operation accept
      operation accept delegates to QuoteRequest[ACCEPTED -> POLICY_CREATED X EXPIRED] emits event PolicyCreated X QuoteExpired
    }
  }
  Aggregate QuoteRequest {
    Entity Request {
      aggregateRoot
    }
    DomainEvent RequestSubmitted
    DomainEvent QuoteReceived
    DomainEvent RequestRejected
    DomainEvent QuoteRejected
    DomainEvent QuoteAccepted
    DomainEvent QuoteExpired
    DomainEvent PolicyCreated
    Service QuoteRequestService {
      void submitRequest(@Request request);
      void checkRequest(@Request request);
      void receiveAndCheckQuote(@Request request);
      void reject(@Request request);
      void accept(@Request request);
    }
    enum RequestState {
      aggregateLifecycle
       SUBMITTED, RECEIVED, REJECTED, ACCEPTED, EXPIRED, POLICY_CREATED
    }
  }
}
```

## Open Flow in BPMN Sketch Miner
The [VS Code extension](/docs/vs-code/) allows you to open a flow in [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/) with two (or max. three) clicks:

Once you modelled your flow in CML, the editor will show a message and a light bulb on the line with the _flow name_:

<a href="/img/bpmn-sketch-miner-in-vs-code-1.png" target="_blank">![BPMN Sketch Miner message on CML flow](/img/bpmn-sketch-miner-in-vs-code-1.png)</a>

Just click on the light bulb and then "Open flow in BPMN Sketch Miner":

<a href="/img/bpmn-sketch-miner-in-vs-code-2.png" target="_blank">![Open flow in BPMN Sketch Miner (1)](/img/bpmn-sketch-miner-in-vs-code-2.png)</a>

In VS Code you have to click "Open" one more time to finally open [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/) in the browser:

<a href="/img/bpmn-sketch-miner-in-vs-code-3.png" target="_blank">![Open flow in BPMN Sketch Miner (2)](/img/bpmn-sketch-miner-in-vs-code-3.png)</a>

And, voilà... a visualization of your CML flow powered by [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/):

<a href="/img/bpmn-sketch-miner-in-vs-code-4.png" target="_blank">![CML flow visualized in BPMN Sketch Miner](/img/bpmn-sketch-miner-in-vs-code-4.png)</a>

## Generate BPMN Sketch Miner DSL File
Instead of directly opening the [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/) tool, you can also generate the Sketch Miner DSL into text files. This can be done by calling "Generate Sketch Miner Diagrams" in the context menu of the Context Mapper editor:

<a href="/img/bpmn-sketch-miner-in-vs-code-5.png" target="_blank">![Generate Sketch Miner Files](/img/bpmn-sketch-miner-in-vs-code-5.png)</a>

In this case Context Mapper generates the Sketch Miner DSL into a text file in the `src-gen` folder:

<a href="/img/bpmn-sketch-miner-in-vs-code-6.png" target="_blank">![Generate Sketch Miner Files](/img/bpmn-sketch-miner-in-vs-code-6.png)</a>

To visualize the flow you can then open [https://www.bpmn-sketch-miner.ai/](https://www.bpmn-sketch-miner.ai/) and copy the generated text manually.
