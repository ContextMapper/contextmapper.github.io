---
title: Imports
permalink: /docs/imports/
---

CML models can be divided into multiple *.cml files. For example, you may want to specify Bounded Contexts in separate files and use them in multiple Context Maps.
One *.cml file can only contain one Context Map. However, multiple Context Maps in separate *.cml files can import the same files describing the Bounded Contexts.

## Example

The following CML snippet could be in a file `BoundedContexts.cml` and specify some Bounded Contexts:

<div class="highlight"><pre><span></span><span class="k">BoundedContext</span> CustomerManagementContext <span class="k">implements</span> CustomerManagementDomain {
  <span class="k">Aggregate</span> Customers {
    <span class="k">Entity</span> Customer {
      <span class="k">aggregateRoot</span>

      - <span class="k">SocialInsuranceNumber</span> sin
      <span class="k">String</span> firstname
      <span class="k">String</span> lastname
      - <span class="k">List</span>&lt;Address&gt; addresses
    }

    <span class="k">Entity</span> Address {
      <span class="k">String</span> street
      <span class="k">int</span> postalCode
      <span class="k">String</span> city
    }
  }
}

<span class="k">BoundedContext</span> PolicyManagementContext <span class="k">implements</span> PolicyManagementDomain {
  <span class="k">Aggregate</span> Contract {
    <span class="k">Entity</span> Contract {
      <span class="k">aggregateRoot</span>

      - <span class="k">ContractId</span> identifier
      - <span class="k">Customer</span> client
      - <span class="k">List</span>&lt;Product&gt; products
    }

    <span class="k">Entity</span> Policy {
      <span class="k">int</span> policyNr
      - <span class="k">Contract</span> contract
      <span class="k">BigDecimal</span> price
    }
  }
}
</pre></div>

A file containing the ContextMap can then import the Bounded Contexts with the **import keyword**:

<div class="highlight"><pre><span></span><span class="k">import</span> <span class="s">&quot;./BoundedContexts.cml&quot;</span>

<span class="k">ContextMap</span> InsuranceContextMap {
  <span class="k">contains</span> CustomerManagementContext
  <span class="k">contains</span> PolicyManagementContext

  PolicyManagementContext [<span class="k">D</span>,<span class="k">CF</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] CustomerManagementContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTfulHTTP&quot;</span>
    <span class="k">exposedAggregates</span> = Customers
  }
}
</pre></div>

It is also possible to import *.cml files located in other directories:

<div class="highlight"><pre><span></span><span class="k">import</span> <span class="s">&quot;./BoundedContexts/CustomerManagement.cml&quot;</span>
<span class="k">import</span> <span class="s">&quot;./BoundedContexts/PolicyManagement.cml&quot;</span>

<span class="k">ContextMap</span> InsuranceContextMap {
  <span class="k">contains</span> CustomerManagementContext
  <span class="k">contains</span> PolicyManagementContext

  PolicyManagementContext [<span class="k">D</span>,<span class="k">CF</span>]&lt;-[<span class="k">U</span>,<span class="k">OHS</span>,<span class="k">PL</span>] CustomerManagementContext {
    <span class="k">implementationTechnology</span> = <span class="s">&quot;RESTfulHTTP&quot;</span>
    <span class="k">exposedAggregates</span> = Customers
  }
}
</pre></div>

<div class="alert alert-custom">
<strong>Note:</strong> Although you can import *.cml files from different directories our Eclipse IDE plugin will only be able to resolve files 
within the same Eclipse project.
</div>
