---
title: BPMN Sketch Miner Generator
permalink: /docs/bpmn-sketch-miner/
---

## Introduction and Motivation
We use the [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/) tool to visualize [event/command flows in our application layers](/docs/application-and-process-layer/#processes-and-eventcommand-flows). You can model flows (for example as a result of an [Event Storming](/docs/event-storming/)) in the CML application layer of a Bounded Context and then generate the [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/) DSL or directly open the tool from Context Mapper.

## Example Flow
The following CML code illustrates how you can model flows. A complete documentation on the syntax can be found in the [language reference](/docs/application-and-process-layer/#processes-and-eventcommand-flows).

<div class="highlight"><pre><span></span><span class="c">/**</span>
<span class="c"> * A flow inspired by the Lakeside Mutual project (https://github.com/Microservice-API-Patterns/LakesideMutual).</span>
<span class="c"> * Find the original process visualization here:</span>
<span class="c"> * https://github.com/Microservice-API-Patterns/LakesideMutual/blob/master/policy-management-backend/src/main/java/com/lakesidemutual/policymanagement/domain/insurancequoterequest/RequestStatus.java</span>
<span class="c"> **/</span>
<span class="k">BoundedContext</span> InsuranceQuotes {
  <span class="k">Application</span> {
    <span class="k">Flow</span> QuoteRequestFlow {
      <span class="k">operation</span> submitRequest <span class="k">delegates</span> <span class="k">to</span> QuoteRequest[-<span class="k">&gt;</span> SUBMITTED] <span class="k">emits</span> <span class="k">event</span> RequestSubmitted
      <span class="k">event</span> RequestSubmitted + RequestSubmitted <span class="k">triggers</span> <span class="k">operation</span> checkRequest
      <span class="k">operation</span> checkRequest <span class="k">delegates</span> <span class="k">to</span> QuoteRequest[SUBMITTED -&gt; RECEIVED <span class="k">X</span> REJECTED] <span class="k">emits</span> <span class="k">event</span> QuoteReceived <span class="k">X</span> RequestRejected
      <span class="k">event</span> QuoteReceived <span class="k">triggers</span> <span class="k">operation</span> receiveAndCheckQuote
      <span class="k">operation</span> receiveAndCheckQuote <span class="k">delegates</span> <span class="k">to</span> QuoteRequest[RECEIVED -&gt; REJECTED <span class="k">X</span> ACCEPTED <span class="k">X</span> EXPIRED] <span class="k">emits</span> <span class="k">event</span> QuoteRejected <span class="k">X</span> QuoteAccepted <span class="k">X</span> QuoteExpired
      <span class="k">event</span> QuoteAccepted <span class="k">triggers</span> <span class="k">operation</span> accept
      <span class="k">operation</span> accept <span class="k">delegates</span> <span class="k">to</span> QuoteRequest[ACCEPTED -&gt; POLICY_CREATED <span class="k">X</span> EXPIRED] <span class="k">emits</span> <span class="k">event</span> PolicyCreated <span class="k">X</span> QuoteExpired
    }
  }
  <span class="k">Aggregate</span> QuoteRequest {
    <span class="k">Entity</span> Request {
      <span class="k">aggregateRoot</span>
    }
    <span class="k">DomainEvent</span> RequestSubmitted
    <span class="k">DomainEvent</span> QuoteReceived
    <span class="k">DomainEvent</span> RequestRejected
    <span class="k">DomainEvent</span> QuoteRejected
    <span class="k">DomainEvent</span> QuoteAccepted
    <span class="k">DomainEvent</span> QuoteExpired
    <span class="k">DomainEvent</span> PolicyCreated
    <span class="k">Service</span> QuoteRequestService {
      <span class="k">void</span> submitRequest(@Request request);
      <span class="k">void</span> checkRequest(@Request request);
      <span class="k">void</span> receiveAndCheckQuote(@Request request);
      <span class="k">void</span> reject(@Request request);
      <span class="k">void</span> accept(@Request request);
    }
    <span class="k">enum</span> RequestState {
      <span class="k">aggregateLifecycle</span>
       SUBMITTED, RECEIVED, REJECTED, ACCEPTED, EXPIRED, POLICY_CREATED
    }
  }
}
</pre></div>

## Open Flow in BPMN Sketch Miner
The Context Mapper IDEs ([VS Code extension](/docs/vs-code/) as well as [Eclipse plugin](/docs/eclipse/)) allow you to open a flow in [BPMN Sketch Miner](https://www.bpmn-sketch-miner.ai/) with two (or max. three) clicks. The following example illustrates this in VS Code (Eclipse works the same way).

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
